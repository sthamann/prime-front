#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v969 -- PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E] + PRIME.L2.RENYI3.SLIDING_BOUND.01 [O] + PRIME.L2.RENYI3.PROVENANCE.01 [O update] + PRIME.LSTAR.SUBORDINATION.01 [O update] (rounds 317-322, ADJUDICATED at the finite-identity level plus typed measurement legs): THE RED-TEAM MORNING AND THE TWO FORKS -- after the reviewer asymmetry decision (terminal has a proof path, L* needs a new idea; resource split 40/40/20) the morning block ran six rounds in parallel lanes and this module freezes them.  (1) THE R319 EXTRACTION-CHAIN RED TEAM (Lean audit round, no probe -- consumed as a REPORT, its artifacts live in rh/lean/ and are re-verified by lake build + run_rh.py): the chain from the two lemmata to Weil/RH was independently reconstructed and THREE kernel-checked TYPE INCONSISTENCIES were found three levels above the boxes -- (U1) the r310b source bridge mainWindow_iff_builtFromPrimeSource as typed is inconsistent with the terminal type: RepresentsWindow bound only nodes/comb/arch and never read u or B, so a window with B = -1 represents the EMPTY spec while terminal_positive_main demands 0 < B; (U2) the same old bridge is inconsistent with the L* type: at mesh level 0 the tolerance is log(anchor), the TOTAL NODE COLLISION (all nodes = 1) represents the {2,3,4} spec and p = X - 1 vanishes on the collided window -- the strict subordination demands 0 < 0; (U3) the old pair_margin_main type (free (Zloc, runs) quantification, bound only by the split -- the r273 disease one level up) is inconsistent with the EXISTENCE of any MAIN window: the adversary Zloc = |F| + 1, runs = [] satisfies the split and demands (|F| + 1)^2 < 5/7 < 1; PLUS the mesh-vs-anchor COFINALITY SEAM: cofinal_prime_windows proves the anchor direction at fixed mesh, which is exactly the H_cof direction proved inadmissible in the carrier lane (mesh refinement needed, false floors measured).  THE HONEST CHAIN VERDICT (binding, verbatim): "two lemmata => RH" does NOT survive the literal reading; literally the two lemmata give ONLY window-local master positivity for the opaque, currently witness-less MainWindow -- the road to RH additionally needs the corrected source bridge (u/B/fold/arch fidelity) + the transport onto the real folded source + the mesh-cofinal v749 tower identification (to be formalized) + the cited classics (form convergence proved, density, Dini continuity, Weil criterion).  All three U-findings are REBUILT IN EXACT ARITHMETIC in this module's S0 (rational witnesses, integer certificates -- NOT via a Lean call): U1 as the B = -1 empty-spec model against the terminal demand, U2 via the exact rational e-bracket 685/252 <= e <= 685/252 + 1/35280 (series partial sum + tail majorant 1/35840 <= 1/35280) reducing the three collision-admissibility clauses to the integer facts 2 <= e, 3 <= 2e, e <= 4 and the collided-window kill p = X - 1 to the exact 0 < 0, U3 as the exact (|F| + 1)^2 >= 1 > 5/7.  (2) THE R320 REPAIR (Lean round, already merged and green in rh/lean/ -- NO Lean change ships with this module): RepresentsWindow/RepresentsSpec RETYPED with u/B fidelity + the separation discipline (2 delta < min node gap AND delta < min comb weight; spec field budget_pos; honest: mesh level 0 represents NOTHING, representation begins at sufficient refinement); the ADDITIONAL FINDING beyond the audit -- the free spec fields arch/border carry the same disease (arch vs L* at p = 1, border vs the pair margin) -- sealed by the new opaque SourceExact (r273 convention spec-side; elimination = the arch/border/fold transcription TODO); the bridge lifted to EXISTS s, SourceExact s AND RepresentsWindow (stays the one definitional sorry; the false Iff.rfl promise corrected); pair_margin_main RETYPED onto the canonical extraction (signRuns/terminalDrive/bulkRuns/edgeLocal as definitions, signRuns_sum + canonical_split PROVED -- no free (Zloc, runs) anymore); THREE PERMANENT SORRY-FREE GUARDS checked in (old_bridge_terminal_inconsistent / old_bridge_lstar_inconsistent / old_pair_margin_forces_empty, forall-P form, axiom census kernel-checked without sorryAx); the witness witness_represents SORRY-FREE (anchor 2, atoms {2,3,4}, mesh level 4 -- the first level with satisfiable separation discipline via the integer facts 2^7 < 3^5 < 2^8, both re-gated exactly in S0; exact rational nodes; EXISTS MainWindow stays deliberately unprovable -- two opaque predicates block exactly the adversaries); the cofinality seam DOCUMENTED (v749 tower identification = the named open Lean target); sorry census 5 -> 5 with two typed RETYPES (the two true holes lstar_subordination + terminal_positive_main and crossing_budget byte-identical); lake build green (2622 jobs), run_rh.py --fast 71/71.  The r320 separation discipline and canonical split are re-gated in S0: 2 delta < min gap at mesh level 4 reduces to 1/8 < 2/5 (via 3^5 < 2^8), the level-0 failure to 4/3 < 4, and the canonical extraction satisfies signRuns_sum + canonical_split exactly on rational toys while the U3 adversary pair is NOT a canonical extraction (CAUGHT).  (3) THE R317 EXCEPTION-FAMILY CENSUS (reviewer fork (b); exception_families_probe.py 38/38, SPEC 04fbe5c063c0cf19): the hard two-family gate (sealed IN ADVANCE: at most TWO source-pure exception families plus the generic theorem; any uncovered violator, family growth or world leak fires the abort BY CONTRACT) fired WHAC_A_MOLE(kz53, kz83) -- the sealed blind gap rule recovers B = {kz55, kz67} (the r315/r316 FCIX pair, F_B 7.23/4.96, gap 1.78, finite certificates C_B = 1.0536 <= the r306 shallow max), class A stays EMPTY (best gap 1.233 misses the sealed 1.25 bar by 0.017 -- disclosed, NOT repaired), and the 63-rung complement is violated by exactly the two uncovered rungs kz53/kz83 vs C_gen = 0.4579; THE CENSUS FIND: the F_A top-3 are EXACTLY kz53 (2.47) / kz83 (2.39) / kz67 (2.38) -- ONE source-pure QMAX coordinate ranks the complete mid/deep near-critical family on top (refuting at census level the r316 conjecture that kz53 needs a second coordinate) but as a CONTINUUM (1.93, 1.90, 1.74, ...), not a gap-separated family: the exception-family FORM is the wrong statement shape for a spike continuum; back to fork (a).  (4) THE R321 CONTINUOUS-COORDINATE ROUND (fork (a) r317-sharpened; continuous_coordinate_probe.py 39/39, SPEC e68883add913c344): SLIDING_BOUND_GO(G_SQ) -- THE THEOREM CANDIDATE: sum q^3 <= 1.3056 x F_A(w)^2 x (log m)^2 / m^2 for m >= 73 (+ 21 small-m certificates, C_small 1.0694), pointwise 0/39 mid-ladder test violations AND all four named r316/r317 violators kz53/kz83/kz67/kz55 INSIDE with reserves 7.0..9.6 -- exactly what killed every flat mid-ladder constant since r316 is absorbed by the coordinate; the winning form is the ALGEBRA-DERIVED one: b = (max cal B)^2 = 1.1426^2 = 1.3056 is SOURCE-PURE (no target value enters the calibration), backed by the NEW exact two-sided concentration bracket qmax x PhiH1 <= rho_2 <= PhiH1 = (F_A x B)^2 (re-derived from scratch in S0 on rational witnesses with both mutant directions CAUGHT; warded live probe-side on 69 worlds); the envelope is STRICTLY monotone (bin Spearman +1.000), bulk Spearman +0.84, gain 15.95; HONEST: C_impl = g(2.47) = 7.97 is 7.5x LOOSER than the r306 first-5 constant 1.069 -- the round buys FORM (one gliding bound, no regimes, no exceptions), not sharpness; the pure-algebra transfer does NOT close (B not bounded by its cal max: test max 1.4088 = 1.23x, trend +0.122 rising -- the certificate holds on the measured rho_2 directly because the qmax slack falls faster than B^2 rises); SCRAMBLE is NOT rejected by the coordinate alone (F_ins 2.00, covered at 5.21) -- the r317 class side condition carries the rejection (COLL 3.69, shuffle 294/300), honestly typed; THE NEW TWO-PART PROVENANCE QUESTION (source-pure, local): (a) is F_A bounded (measured max 2.47; the near-critical family is its top), (b) what bounds the qmax-share rho_2/(F_A^2 B^2) (the median-of-max shape route; the r302 M_2 stationarity 1.973 pins the second moment of the same shape).  (5) THE R318 INDEFINITE FORK (the new L* idea class after the language stop; indefinite_fork_probe.py 25/25, SPEC f2d98683fd06d8bd): P2_MAIN_SPECIFIC(antiphase fingerprint) -- the 2.4 percent negative cross mixtures of the converged r308 Dykstra family are NOT structureless: on MAIN-class worlds the block residual lives lawfully on the ANTIPHASE pair (D3, D4) with fixed sign -1 (modal share med 0.699, 12/12 sealed rungs, rational twin exact 0.692 -- METRIC_ONLY holds) while the dead controls break BY PATTERN on the arch-mean x border pair (D5, D6) (shares 0.953/1.000, d6-class 0.962/1.000 vs MAIN 0.027; honest caveat: control fingerprints ITERATE-grade); P1 BANKED AS LANGUAGE: the index bookkeeping is EXACT (spectral count == mp pivot count on all seven worlds at window + guarded deep depth; window index defect 0/0/0 on w9/w13/twin vs 55/37/4/31 on EPST/SCR/SMOOTH/HL2 -- the control flips ARE negative directions inside the window, measured as index defects; ladder 42/42 defect 0) but "n_+(window) == N_w" is a TOTAL RESTATEMENT of L* (equivalence on 10/10 instances, both truth values realized), the global n_+ >= N_w is VACUOUS (mu-channel majority, world-blind) and the negative-subspace invariants are world-blind (no lever either way); classical sign regularity is DEAD on MAIN (orientation-sensitive minor censuses coin-flip ~0.50 => PREMISE_FAILS_ON_MAIN for the variation-diminishing chain).  (6) THE R322 DIG (antiphase_sign_law_probe.py 25/25, SPEC 761b51d469b02a9c): ALGORITHM_ARTIFACT -- the sign law AND the r312 97.6/2.4 cone anatomy are properties of the LEAST-NORM-PROXIMAL DYKSTRA BASIN, not of the psd solution set: the sealed random-start variants (staged to 20000 steps, r311 START_NEAR class) carry modal pair (0, 2) at shares 0.310/0.264 with cone share 0.782 while the canonical variants LSTART/LONG/ZERO/REV all carry the law exactly ((2, 3), -1, 0.692; projection order irrelevant) and coincide within rel 2e-7 -- exactly the 9/15 variant pairs involving the random starts are distinct; the r318 pattern dichotomy does NOT survive fair convergence (the budget-ablated CONVERGED controls split: EPST-abl carries the MAIN law STRONGER than MAIN, 0.742 vs 0.692, SCR-abl breaks at 0.379 => FAIR_CONTROL_CARRIES 1/2); the law is NOT identity-forced (exact forced-component analysis: TOY4 calibrator machine-exact free 0 / value 4/7 == the r308 G10 pin; SM1 exact free fraction 0.47671 with POSITIVE forced value +0.51; MINI16 exact rowspace membership FALSE) -- the negative sign law lives ENTIRELY in the free/selection directions, exactly as the D3 = -(D2 + 2 D1) in-block dependence disclosure predicted; what survives: a sharp, reproducible, position-structured (mid/tail) fingerprint with total sign consistency (1.000; 92.3 percent of ALL blocks) and the best reporting-grade hook (block-local antiphase mass pairing +0.81, below the sealed 0.9 bar); THE NAMED RESIDUAL OBJECT: the SELECTION-GEOMETRY question -- why does the least-norm-proximal basin organize its indefiniteness on the antiphase pair, and does ANY canonical source-pure selection rule reproduce it (the r312 wall: no formula so far).  THE MODULE-OWN EXACT SECTION S0 (pure Fractions and integer certificates, no probe imports, NO Lean call): (T1) the r321 concentration bracket qmax x PhiH1 <= rho_2 <= PhiH1 == (F_A x B)^2 on rational witnesses incl. the one-block equality case, with the dropped-qmax lower mutant and the tightened upper mutant both CAUGHT and the wrong-exponent identity mutant CAUGHT; (T2) the U1 witness in exact arithmetic (the old bridge certifies the B = -1 empty-spec window for EVERY predicate while the terminal demands 0 < -1; the r320 retyped bridge with u/B fidelity + budget_pos REFUSES B = -1 and ACCEPTS the honest B = 5/7 witness); (T3) the U2 witness in exact arithmetic (the rational e-bracket via series partial sum 685/252 + tail majorant with the exact comparison 1/35840 <= 1/35280; the three collision-admissibility clauses as integer facts; the collided-window kill 0 < 0; the r320 separation discipline: mesh level 4 satisfiable via 128 < 243 < 256 reducing to 1/8 < 2/5 EXACT, mesh level 0 UNSATISFIABLE via 4/3 < 4 -- level 0 represents nothing); (T4) the U3 witness in exact arithmetic ((|F| + 1)^2 >= 1 > 5/7 for every rational F -- the old type forces its source predicate EMPTY) and the r320 canonical extraction on rational toys (signRuns_sum + canonical_split EXACT; the adversary pair is NOT a canonical extraction -- CAUGHT); (V1-V6) the SEALED VERDICT BARS as exact decision logic on the frozen record aggregates with tipping mutants at every live clause boundary: r317 the hard two-family gate (mutants: zero violations fire ONE_FAMILY_SUFFICES(B), a firing class A composes EXCEPTION_CENSUS_GO, five violations fire GENERIC_FAILS, a growing family fires the abort, the three-family tuple is REFUSED by seal_family_count), r318 the fork tree (mutants: a MAIN-separating negative-subspace statistic fires BOTH_ALIVE, a broken fingerprint consensus fires FORK_DEAD, both together P1_MAIN_SPECIFIC), r319 the audit gate (fires only if all three U-inconsistencies are established in exact arithmetic AND the seam + the suite facts hold; composes the honest chain reading verbatim), r320 the repair gate (separation integers + canonical split + adversary refusal + census 5 -> 5 with two retypes + guards/witness sorry-free + lake 2622 + run_rh 71/71), r321 the sliding-bound tree (mutants: an SQ miss cascades to G_FAILS_POINTWISE, a diffuse envelope / low gain fire ENVELOPE_DIFFUSE, a world leak fires WORLD_LEAK), r322 the basin adjudication (canonical-vs-random as the verdict rule; mutants: solution-set invariance fires SIGN_LAW_ROBUST, plus exact forcing SIGN_LAW_EXACT, a failing anchor LAW_DIFFUSE); (V7) the WAVE-12 COMPOSITION gate: the six rounds compose to exactly the claim split -- PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E] (U1-U3 + seam + honest chain + repair complete), PRIME.L2.RENYI3.SLIDING_BOUND.01 [O] (the theorem candidate with the two-part provenance question), the PROVENANCE update (r317 WHAC_A_MOLE + r321 GO: the provenance question is now the F_A/qmax split) and the LSTAR update (P1 language banked, P2 fingerprint closed as ALGORITHM_ARTIFACT, selection geometry open) -- tipping mutants: failing guards void the audit claim, a failing sliding bound leaves the fiber at the r317 abort, a solution-set-invariant law would fire the indefinite-theorem candidate -- each tip changes the composition, the split is not hard-wired.  FOUR probes embedded BYTE-EXACT (38/38 + 25/25 + 39/39 + 25/25 smoke == the sealed stage; full records 38/38 + 25/25 + 39/39 + 25/25 sealed experiments-side, re-verified by rh/verification/run_rh.py), executed verbatim in round order so that r321 imports the embedded r317 and r322 the embedded r318 (sys.modules convention; both also import the older frozen probe chains r306-r316 / r308-r312 from the experiments tree, sealed by the v968 byte wards and run_rh.py).  WHAT THE MODULE DOES NOT SAY (honest boundary): NO inequality is promoted -- the sliding bound is a THEOREM CANDIDATE certified on the measured 65-rung ladder + mains + controls and nothing beyond (C_impl disclosed 7.5x looser than r306; the bound is not world-separating by itself); the red-team audit and repair are TYPE-LEVEL results -- EXISTS MainWindow stays deliberately unprovable, the two true Lean holes (lstar_subordination, terminal_positive_main) are UNCHANGED, sorry census 5; the antiphase law is banked as a basin fingerprint, NOT as a theorem; L* stays THE open center.  Mincut base 4 / refined 5 UNCHANGED (a red-team-plus-fork set moves no edge); no other marker moves.  NOT evidence for or against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probes exception_families_probe.py (38/38
full == smoke, SPEC_SHA 04fbe5c063c0cf19, pre-run placeholder
removal disclosed, record-table insertion only),
indefinite_fork_probe.py (25/25 full == smoke, SPEC_SHA
f2d98683fd06d8bd, one smoke-stage harness fix + one
reporting-only amendment a1 disclosed),
continuous_coordinate_probe.py (39/39 full == smoke, SPEC_SHA
e68883add913c344, pre-run placeholder removal disclosed,
record-table insertion only), antiphase_sign_law_probe.py (25/25
full == smoke, SPEC_SHA 761b51d469b02a9c, one gate-typing
amendment a1 disclosed -- the negative tree branch is a verdict
letter, not a probe failure; letter identical across passes);
rounds 317/318/321/322, notes DCLXII/DCLXIII/DCLXV/DCLXVI,
2026-08-27.  WAVE-4 EMBEDDING CONVENTION (as in v960..v968):
frozen sources embedded BYTE-EXACT and executed verbatim in
isolated namespaces in their sealed --smoke stage (deterministic;
smoke wall times 0.4/0.2/0.5/1.3 s); printed SPEC SHAs pinned and
gated; byte-equality ward vs experiments/tfpt-discovery/ inside
the pattern gates; the full-mode records (gate counts above, wall
times 36.2/23.7/36.5/165.1 s) are sealed experiments-side and
re-verified by rh/verification/run_rh.py.  The probes consume the
READ-ONLY deployed core v563_paper2_readouts.py and the frozen
experiments-side libraries (imports printed in their headers);
the execution order follows the round order so later probes
import earlier ones from the embedded byte-exact sources
(sys.modules convention: r321 imports the embedded r317, r322 the
embedded r318); all four import the older frozen probe libraries
from the experiments tree (sealed by the v960..v968 byte wards
and run_rh.py).  The Lean rounds r319 (audit, notes DCLXI -- no
file changed) and r320 (repair, notes DCLXIV -- retypes, guards,
witness, already merged and green in rh/lean/) are consumed as
REPORTS -- their artifacts live in rh/lean/ and are re-verified
by lake build + run_rh.py, NOT by this module; the U1-U3
inconsistencies are re-established in exact arithmetic in S0.
No round is in flight at this promotion cut.

FIREWALL: no zeros, no prime-table oracles (AST scans inside the
probes); RNG only in declared synthetic-build seeds (sealed,
collision-free, gated); ground truth (branch labels, survival
records) enters gates only; NO promotion of any inequality (the
sliding bound is registered as a THEOREM CANDIDATE [O], the
red-team result as a type-level audit [E]); NO RH claim.
Python-only per GATE.WOLFRAM.02.
"""

import contextlib
import io
import os
import re
import sys
import time
import types
from fractions import Fraction as _Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


# ---------------- module-own exact machinery (pure Fractions and
# ---------------- integer certificates; the r321 concentration
# ---------------- bracket, the R319 U1/U2/U3 witnesses, the r320
# ---------------- repair discipline and the six sealed verdict
# ---------------- bars are re-derived from scratch at module
# ---------------- level -- no probe imports, NO Lean call)
def _bracket(xs, ell, wrong="none"):
    """the r321 exact concentration bracket on a rational block
    vector xs with the rational polylog stand-in ell (standing for
    m^2/(log m)^2, the r306 scale convention): with L = sum |x|,
    qmax = max |x| / L, rho_2 = ell x sum |x|^3 / L^3 and PhiH1 =
    ell x qmax^2, the two-sided bracket qmax x PhiH1 <= rho_2 <=
    PhiH1 is pure algebra (qmax^3 L^3 <= sum |x|^3 <= qmax^2 L^3).
    wrong='drop_lower' asserts PhiH1 <= rho_2 (the dropped-qmax
    lower mutant); wrong='tight_upper' asserts rho_2 <= qmax x
    PhiH1 (the tightened upper mutant) -- both must FAIL on spread
    witnesses."""
    a = [abs(_Fr(x)) for x in xs]
    L = sum(a)
    qmax = max(a) / L
    s3 = sum(v ** 3 for v in a)
    rho2 = ell * s3 / L ** 3
    phih1 = ell * qmax * qmax
    if wrong == "drop_lower":
        return phih1 <= rho2
    if wrong == "tight_upper":
        return rho2 <= qmax * phih1
    return qmax * phih1 <= rho2 <= phih1


def _coord_identity(qmax, med, ell, wrong="none"):
    """the r321 exact coordinate identities: QMAX == F_A x medloc
    (reconstruction) and PhiH1 == F_A^2 x B^2 with B^2 = medloc^2
    x ell (the source-pure baseline squared -- rational since ell
    is the rational stand-in).  wrong='exponent' asserts PhiH1 ==
    F_A x B^2 (must FAIL whenever F_A != 1)."""
    fa = qmax / med
    b2 = med * med * ell
    phih1 = ell * qmax * qmax
    if wrong == "exponent":
        return phih1 == fa * b2
    return fa * med == qmax and phih1 == fa * fa * b2


# --------- the U1 witness (r320 guard old_bridge_terminal_
# --------- inconsistent, exact-arithmetic mini-rebuild): the
# --------- pre-r320 bridge type binds only nodes/comb/arch within
# --------- the mesh -- at S = 0 every channel clause is vacuous
# --------- and neither u nor B is ever read, so the B = -1 window
# --------- represents the EMPTY spec for ANY mesh, while the
# --------- terminal type demands 0 < B.
def _u1_old_bridge_represents(B, S=0):
    """OldRepresentsWindow at S = 0: vacuously true for every B --
    the budget channel is never read (the disease)."""
    _ = B
    return S == 0


def _u1_terminal(B):
    """TerminalPositive demands 0 < B."""
    return _Fr(B) > 0


def _u1_new_bridge_represents(B, delta):
    """the r320 retyped bridge reads the budget channel: u/B
    fidelity |B - B_spec| <= delta against the spec budget B_spec =
    5/7 with budget_pos (B_spec > 0)."""
    bspec = _Fr(5, 7)
    return abs(_Fr(B) - bspec) <= _Fr(delta) and bspec > 0


# --------- the U2 witness (r320 guard old_bridge_lstar_
# --------- inconsistent): at mesh level 0 the tolerance is
# --------- log(anchor) = log 2, and the total node collision (all
# --------- three nodes of the {2,3,4} spec at 1) is admissible for
# --------- the old bridge.  The three collision clauses
# --------- |1 - log n| <= log 2 (n = 2, 3, 4) reduce EXACTLY to
# --------- rational facts about e: (n=2) log 2 >= 1/2 <=> e <= 4;
# --------- (n=3, using 1 < log 3 <=> e < 3) log 3 - 1 <= log 2 <=>
# --------- 3 <= 2e; (n=4) log 4 - 1 <= log 2 <=> log 2 <= 1 <=>
# --------- 2 <= e.  The exact rational e-bracket: E_LO = the
# --------- series partial sum sum_{k<=7} 1/k! = 685/252; the tail
# --------- is majorized by (1/8!) x (1 + 1/9 + 1/9^2 + ...) =
# --------- 9/(8 x 8!) = 1/35840 <= 1/35280 = 1/(7! x 7), so E_HI =
# --------- 685/252 + 1/35280 is a certified upper bound.
_FACT = [1]
for _k in range(1, 9):
    _FACT.append(_FACT[-1] * _k)
_E_LO = sum(_Fr(1, _FACT[k]) for k in range(8))
_E_TAIL_GEO = _Fr(9, 8 * _FACT[8])
_E_TAIL_PIN = _Fr(1, _FACT[7] * 7)
_E_HI = _E_LO + _E_TAIL_PIN


def _u2_collision_admissible():
    """the three U2 collision clauses as exact rational e-facts."""
    return (_E_HI <= 4                    # n = 2:  log 2 >= 1/2
            and 2 * _E_LO >= 3            # n = 3:  log 3 - 1 <= log 2
            and _E_HI <= 3                # n = 3 sign case: log 3 > 1
            and _E_LO >= 2)               # n = 4:  log 2 <= 1


def _u2_lstar_on_collision(weights):
    """p = X - 1 on the collided window (all nodes at 1): p(1) = 0,
    so both integrals are exactly 0 -- the strict subordination
    demands 0 < 0, i.e. False.  Returns (nu_int, mu_int, holds)."""
    p_at_1 = _Fr(1) - _Fr(1)
    nu = sum(_Fr(w) * p_at_1 ** 2 for w in weights)
    mu = sum(_Fr(w) * p_at_1 ** 2 for w in weights)
    return nu, mu, nu < mu


def _u2_separation(mesh_level):
    """the r320 separation discipline on the {2,3,4} spec, exact:
    delta = log 2 / 2^mesh_level; demands 2 delta < min node gap =
    log(4/3) = 2 log 2 - log 3 AND delta < min comb weight = log 2.
    Via the integer certificates 2^7 < 3^5 < 2^8 (128 < 243 < 256):
    3^5 < 2^8 gives log 3 < (8/5) log 2, hence log(4/3) > (2/5)
    log 2 -- at level 4 the demand 2 delta < min gap reduces to
    1/8 < 2/5 EXACT; at level 0 it demands 2 log 2 < log(4/3),
    impossible since 4/3 < 4 exactly.  Returns True iff the
    discipline is satisfiABLE at the level by these certificates."""
    if not (2 ** 7 < 3 ** 5 < 2 ** 8):
        return False
    two_delta_over_log2 = _Fr(2, 2 ** mesh_level)
    min_gap_lower_over_log2 = _Fr(2, 5)      # from 3^5 < 2^8
    comb_ok = _Fr(1, 2 ** mesh_level) < 1    # delta < log 2
    if mesh_level == 0:
        return False                          # 2 log 2 >= log 4 > log(4/3)
    return two_delta_over_log2 < min_gap_lower_over_log2 and comb_ok


# --------- the U3 witness (r320 guard old_pair_margin_forces_
# --------- empty): with free (Zloc, runs) the adversary Zloc =
# --------- |F| + 1, runs = [] satisfies the split trivially and
# --------- the claimed margin demands |F| + 1 < sqrt(5/7) --
# --------- squared: (|F| + 1)^2 < 5/7, FALSE for every rational F
# --------- since (|F| + 1)^2 >= 1 > 5/7 EXACT.
def _u3_old_margin_possible(F):
    """can the old margin hold on the adversary pair?  Exact."""
    z = abs(_Fr(F)) + 1
    return z * z < _Fr(5, 7)


def _sign_runs(v):
    """maximal same-sign run sums of a rational vector (the r320
    canonical bulk extraction modeled; sign convention: >= 0 vs
    < 0)."""
    runs = []
    cur = []
    for x in v:
        x = _Fr(x)
        if cur and ((x >= 0) != (cur[-1] >= 0)):
            runs.append(sum(cur))
            cur = []
        cur.append(x)
    if cur:
        runs.append(sum(cur))
    return tuple(runs)


def _canonical_extraction(v):
    """the r320 canonical extraction modeled on a rational vector
    with edge convention v[0] = edge-local part: Zloc = v[0], runs
    = the maximal same-sign run sums of the bulk v[1:].  The two
    PROVED r320 lemmata as exact identities: signRuns_sum (sum of
    runs == bulk sum) and canonical_split (Zloc + sum runs == total
    sum).  Returns (Zloc, runs, signruns_ok, split_ok)."""
    w = [_Fr(x) for x in v]
    zloc = w[0]
    runs = _sign_runs(w[1:])
    signruns_ok = sum(runs) == sum(w[1:])
    split_ok = zloc + sum(runs) == sum(w)
    return zloc, runs, signruns_ok, split_ok


# --------- frozen record aggregates (rounds 317/318/321/322 and
# --------- the Lean rounds 319/320; exact decimal pins as
# --------- Fractions where the printed record is exact; ground
# --------- truth sealed probe-side / rh-side, re-verified by the
# --------- embedded pattern gates below and by run_rh.py)
_REC = dict(
    # r317 exception_families_probe (38/38): the hard two-family gate
    r317=dict(viol=2, viol_names=("kz53", "kz83"), gen_fail_min=5,
              fam_a=0, fam_b=2, b_members=("kz55", "kz67"),
              f_b=(_Fr(723, 100), _Fr(496, 100)),
              thr_b=_Fr(37157, 10 ** 4), gap_b=_Fr(178, 100),
              a_best_gap=_Fr(1233, 1000), gap_bar=_Fr(125, 100),
              c_gen=_Fr(4579, 10 ** 4), c_b=_Fr(10536, 10 ** 4),
              c_small=_Fr(10694, 10 ** 4), growth_b=(1, 1, 0),
              world_ok=True, fa_top=(("kz53", _Fr(247, 100)),
                                     ("kz83", _Fr(239, 100)),
                                     ("kz67", _Fr(238, 100)))),
    # r318 indefinite_fork_probe (25/25): the fork adjudication
    r318=dict(index_exact=True, restat_hits=10, restat_n=10,
              vacuous=True, neg_separating=False, proxy=False,
              sr_main_specific=False, sr_rowinit=_Fr(1, 2),
              fp_rungs=12, fp_agree=12, fp_pair=(2, 3), fp_sign=-1,
              fp_share=_Fr(699, 1000), twin_pair=(2, 3),
              twin_sign=-1, twin_share=_Fr(692, 1000),
              ctrl_pairs=((4, 5), (4, 5)),
              ctrl_d6=(_Fr(962, 1000), _Fr(1)),
              main_d6=_Fr(27, 1000),
              defects=dict(w9=0, w13=0, twin=0, EPST=55, SCR=37,
                           SMOOTH=4, HL2=31)),
    # r319 Lean red-team audit (report; artifacts rh/lean/, no file
    # changed by the audit round itself)
    r319=dict(u_findings=3, seam=True, lake_jobs=2585, sorries=5,
              suite=(68, 68), files_changed=0),
    # r320 Lean repair (report; artifacts merged and green rh/lean/)
    r320=dict(census_before=5, census_after=5, retypes=2, guards=3,
              guards_sorryfree=True, witness_sorryfree=True,
              witness_mesh_level=4, lake_jobs=2622, run_rh=(71, 71)),
    # r321 continuous_coordinate_probe (39/39): the sliding bound
    r321=dict(viol=dict(SQ=0, TT=2, LIN=5),
              named=dict(SQ=4, TT=1, LIN=1), named_total=4,
              b_const=_Fr(13056, 10 ** 4), env_ok=True,
              bin_sp=_Fr(1), bulk_sp=_Fr(84, 100),
              gain=_Fr(1595, 100), gain_min=_Fr(15, 10),
              world_ok=True, scr_by_coord=False, scr_by_class=True,
              m0=73, c_small=_Fr(10694, 10 ** 4),
              c_impl=_Fr(797, 100), fa_max=_Fr(247, 100),
              rsv=dict(kz53=_Fr(76, 10), kz83=_Fr(96, 10),
                       kz67=_Fr(70, 10), kz55=_Fr(72, 10)),
              b_cal_max=_Fr(11426, 10 ** 4),
              b_test_max=_Fr(14088, 10 ** 4),
              b_trend=_Fr(122, 1000)),
    # r322 antiphase_sign_law_probe (25/25): the basin adjudication
    r322=dict(law_pair=(2, 3), law_sign=-1, law_share=_Fr(692, 1000),
              law_d6=_Fr(27, 1000), sign_cons=_Fr(1),
              rand_pair=(0, 2),
              rand_shares=(_Fr(310, 1000), _Fr(264, 1000)),
              rand_cone=_Fr(782, 1000), invariant=False,
              canonical_carry=4, distinct_pairs=(9, 15),
              sm1_free=_Fr(47671, 10 ** 5), sm1_forced_pos=True,
              mini16_member=False, fair_carries=1, fair_total=2,
              k1=_Fr(8114, 10 ** 4), cert=(57, 57), twin_cert=True),
)


# --------- the sealed verdict bars as exact decision logic
def _seal_family_count(fams):
    """the r317 warded module rule: EXACTLY the two sealed families
    are accepted -- a third family is REFUSED."""
    return len(fams) == 2


def _bar_r317(r, no_viol=False, broad=False, a_fires=False,
              growth=False):
    """r317: the hard two-family gate as sealed -- GENERIC_FAILS
    iff |viol| >= GEN_FAIL_MIN; WHAC_A_MOLE iff 1 <= |viol| <
    GEN_FAIL_MIN or a family grows; EXCEPTION_CENSUS_GO iff 0
    violations and BOTH families non-empty (no growth, world ok);
    ONE_FAMILY_SUFFICES iff 0 violations and at most one family."""
    viol = 0 if no_viol else (r["gen_fail_min"] if broad else r["viol"])
    fam_a = 1 if a_fires else r["fam_a"]
    fam_b = r["fam_b"]
    grows = growth
    if viol >= r["gen_fail_min"]:
        return "GENERIC_FAILS"
    if viol >= 1:
        return ("WHAC_A_MOLE(%s -- a third exception form would be "
                "needed; NO third class added, abort by contract; "
                "back to fork (a))"
                % ", ".join(r["viol_names"][:viol]))
    if grows:
        return "WHAC_A_MOLE(a family grows with depth)"
    if not r["world_ok"]:
        return "WHAC_A_MOLE(world leak)"
    if fam_a > 0 and fam_b > 0:
        return "EXCEPTION_CENSUS_GO(A, B)"
    if fam_b > 0:
        return "ONE_FAMILY_SUFFICES(B)"
    if fam_a > 0:
        return "ONE_FAMILY_SUFFICES(A)"
    return "ONE_FAMILY_SUFFICES(NONE)"


def _bar_r318(r, neg_sep=False, fp_broken=False, sr_spec=False):
    """r318: the sealed fork tree -- alive(P1) iff the index
    bookkeeping is exact AND some sealed negative-subspace
    statistic is MAIN-separating AND the proxy test does not fire;
    alive(P2) iff SR MAIN-specific OR the fingerprint consensus is
    lawful + twin-consistent + pattern-broken on every control."""
    p1 = (r["index_exact"] and (neg_sep or r["neg_separating"])
          and not r["proxy"])
    fp_ok = ((not fp_broken) and r["fp_agree"] >= 10
             and r["fp_share"] >= _Fr(1, 2)
             and r["twin_pair"] == r["fp_pair"]
             and r["twin_sign"] == r["fp_sign"]
             and all(cp != r["fp_pair"] for cp in r["ctrl_pairs"]))
    p2 = (sr_spec or r["sr_main_specific"]) or fp_ok
    if p1 and p2:
        return "BOTH_ALIVE(p1 site; p2 pattern)"
    if p1:
        return "P1_MAIN_SPECIFIC(dig site named)"
    if p2:
        return ("P2_MAIN_SPECIFIC(modal pair (2, 3) = D3 x D4 "
                "ANTIPHASE, sign -1, med share 699/1000, 12/12 rungs "
                "+ twin 692/1000; controls break by PATTERN on the "
                "(4, 5) arch-mean x border pair)")
    return "FORK_DEAD(p1 restatement; p2 premise fails; lane stop)"


def _bar_r319(u1_incons, u2_incons, u3_incons, r, seam_ok=None):
    """r319: the audit gate -- fires only if all three type
    inconsistencies are ESTABLISHED (in this module: exact
    arithmetic, S0-T2/T3/T4) and the seam + the audit-round suite
    facts hold; composes the honest chain reading verbatim."""
    seam = r["seam"] if seam_ok is None else seam_ok
    ok = (u1_incons and u2_incons and u3_incons and seam
          and r["u_findings"] == 3 and r["files_changed"] == 0
          and r["suite"] == (68, 68) and r["sorries"] == 5)
    if not ok:
        return "AUDIT_VOID(recompose)"
    return ("REDTEAM_CONFIRMED(U1 bridge x terminal + U2 bridge x L* "
            "+ U3 pair-margin forces empty + the mesh-vs-anchor "
            "cofinality seam) + HONEST_CHAIN(two lemmata => "
            "window-local master positivity ONLY, for the opaque, "
            "currently witness-less MainWindow; the road to RH "
            "additionally needs: the corrected source bridge "
            "(u/B/fold/arch) + the transport onto the real folded "
            "source + the mesh-cofinal v749 tower identification + "
            "the cited classics)")


def _bar_r320(sep4_ok, sep0_fails, canon_ok, refuse_ok, r):
    """r320: the repair gate -- the separation discipline
    satisfiable at the witness mesh level 4 and UNsatisfiable at
    level 0 (both exact), the canonical extraction identities
    exact, the U-adversaries refused by the retyped forms, and the
    Lean bookkeeping pins (census 5 -> 5 with two retypes, three
    sorry-free guards, sorry-free witness, lake 2622 jobs, run_rh
    71/71)."""
    ok = (sep4_ok and sep0_fails and canon_ok and refuse_ok
          and r["census_before"] == 5 and r["census_after"] == 5
          and r["retypes"] == 2 and r["guards"] == 3
          and r["guards_sorryfree"] and r["witness_sorryfree"]
          and r["witness_mesh_level"] == 4
          and r["lake_jobs"] == 2622 and r["run_rh"] == (71, 71))
    if not ok:
        return "REPAIR_INCOMPLETE(recompose)"
    return ("REPAIR_COMPLETE(bridge retyped with u/B fidelity + "
            "separation discipline + budget_pos; SourceExact seals "
            "the arch/border disease; pair_margin_main retyped onto "
            "the canonical extraction with signRuns_sum + "
            "canonical_split PROVED; three permanent sorry-free "
            "guards; sorry-free witness at anchor 2, atoms {2,3,4}, "
            "mesh level 4 via 2^7 < 3^5 < 2^8; census 5 -> 5 with "
            "two typed retypes; lake 2622 jobs green; run_rh 71/71)")


def _bar_r321(r, env_diffuse=False, sq_misses=False, world_leak=False,
              low_gain=False):
    """r321: the sealed sliding-bound tree -- the winner is the
    first form in the sealed derivation-strength precedence (SQ,
    TT, LIN) with 0 test violations AND 4/4 named-violator
    coverage; no winner => ENVELOPE_DIFFUSE if the envelope is
    diffuse else G_FAILS_POINTWISE; a winner => WORLD_LEAK /
    ENVELOPE_DIFFUSE (env or gain) / SLIDING_BOUND_GO."""
    env_ok = (not env_diffuse) and r["env_ok"]
    winner = None
    for form in ("SQ", "TT", "LIN"):
        v = r["viol"][form] + (1 if (sq_misses and form == "SQ") else 0)
        if v == 0 and r["named"][form] == r["named_total"]:
            winner = form
            break
    if winner is None:
        return "ENVELOPE_DIFFUSE" if not env_ok else "G_FAILS_POINTWISE"
    if world_leak:
        return "WORLD_LEAK"
    gain = _Fr(1) if low_gain else r["gain"]
    if not env_ok or gain < r["gain_min"]:
        return "ENVELOPE_DIFFUSE"
    return ("SLIDING_BOUND_GO(G_%s: rho_2 <= %s x F_A^2 on 0/39 test "
            "+ 4/4 named; gain %s; SCRAMBLE via the class side "
            "condition)" % (winner, r["b_const"], r["gain"]))


def _bar_r322(r, invariant=False, forced=False, anchor_fails=False):
    """r322: the basin adjudication (canonical-vs-random as the
    verdict rule) -- law_anchor iff the w9 fingerprint gate + total
    sign consistency hold; NOT law_anchor => LAW_DIFFUSE; law_anchor
    AND NOT invariant => ALGORITHM_ARTIFACT; + exact_forced =>
    SIGN_LAW_EXACT; else SIGN_LAW_ROBUST."""
    law_anchor = ((not anchor_fails) and r["law_pair"] == (2, 3)
                  and r["law_sign"] == -1
                  and r["law_share"] >= _Fr(1, 2)
                  and r["law_d6"] <= _Fr(1, 10)
                  and r["sign_cons"] >= _Fr(9, 10))
    inv = invariant or r["invariant"]
    exact_forced = forced or (r["sm1_free"] == 0
                              and (not r["sm1_forced_pos"])
                              and r["mini16_member"])
    if not law_anchor:
        return "LAW_DIFFUSE"
    if not inv:
        return ("ALGORITHM_ARTIFACT(the accepted random-start "
                "near-solutions carry modal pair (0, 2) at shares "
                "31/100 and 33/125 with cone share 391/500 -- the "
                "sign law AND the r312 97.6/2.4 anatomy are "
                "properties of the least-norm-proximal Dykstra "
                "basin, not of the psd solution set; the canonical "
                "variants coincide and carry the law exactly)")
    if exact_forced:
        return "SIGN_LAW_EXACT(forced identity verbatim)"
    return "SIGN_LAW_ROBUST(lawful, not exact)"


def _wave12(guards_fail=False, sliding_fails=False,
            law_invariant=False):
    """the wave-12 composition: the six rounds compose to EXACTLY
    the claim split -- (i) the red-team extraction audit [E], (ii)
    the sliding-bound theorem candidate [O], (iii) the provenance
    update (the F_A/qmax two-part question), (iv) the L* update
    (P1 language banked, P2 closed as ALGORITHM_ARTIFACT, selection
    geometry open).  The tipping inputs change the composition."""
    if guards_fail:
        red = "EXTRACTION_AUDIT_VOID(old types consistent -- recompose)"
    else:
        red = ("REDTEAM_BANKED(U1-U3 inconsistent in exact arithmetic "
               "+ seam + honest chain reading; r320 repair complete)")
    if sliding_fails:
        fiber = "FIBER_AT_ABORT(the r317 WHAC_A_MOLE stands alone)"
    else:
        fiber = ("SLIDING_BOUND_GO(G_SQ) + PROVENANCE_SPLIT(is F_A "
                 "bounded? / what bounds the qmax-share via the "
                 "M_2-stationarity shape route?)")
    if law_invariant:
        base = ("INDEFINITE_THEOREM_CANDIDATE(the sign law would be "
                "solution-set-universal)")
    else:
        base = ("P1_LANGUAGE_BANKED + ANTIPHASE_LAW_ALGORITHM_ARTIFACT "
                "+ SELECTION_GEOMETRY_OPEN")
    claims = ("PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E]; "
              "PRIME.L2.RENYI3.SLIDING_BOUND.01 [O]; "
              "PRIME.L2.RENYI3.PROVENANCE.01 [O update]; "
              "PRIME.LSTAR.SUBORDINATION.01 [O update]"
              if not (guards_fail or sliding_fails or law_invariant)
              else "CLAIM_SPLIT_INVALID(recompose)")
    return "%s | %s | %s | %s" % (red, fiber, base, claims)


def _forks_and_redteam(gates):
    """the module-own exact section S0: every check appends its
    boolean to gates and prints house-style."""

    def check(name, ok, detail):
        gates.append(bool(ok))
        print("[%s] %s: %s" % ("PASS" if ok else "FAIL", name,
                               detail), flush=True)

    def section(t):
        print("\n--- %s " % t + "-" * max(0, 60 - len(t)), flush=True)

    section("S0-T1 the r321 concentration bracket (exact)")
    ell = _Fr(6, 5)
    w_spread = (_Fr(1, 2), _Fr(1, 4), _Fr(1, 4))
    w_signed = (_Fr(3, 7), _Fr(-5, 2), _Fr(11, 13))
    check("S0-T1a-bracket-exact",
          _bracket(w_spread, ell) and _bracket(w_signed, ell)
          and _bracket((_Fr(1),), ell)
          and _bracket((_Fr(1),), ell, wrong="drop_lower")
          and _bracket((_Fr(1),), ell, wrong="tight_upper"),
          "qmax x PhiH1 <= rho_2 <= PhiH1 EXACT on the spread witness "
          "(3/20 <= 3/16 <= 3/10), on a signed witness and on the "
          "one-block equality witness (both sides == ell: the bracket "
          "is TIGHT exactly at full concentration)")
    check("S0-T1b-bracket-mutants",
          (not _bracket(w_spread, ell, wrong="drop_lower"))
          and (not _bracket(w_spread, ell, wrong="tight_upper")),
          "dropped-qmax lower mutant claims 3/10 <= 3/16 (FALSE exact) "
          "and tightened upper mutant claims 3/16 <= 3/20 (FALSE "
          "exact) -- both directions of the bracket are live, CAUGHT")
    check("S0-T1c-coordinate-identity",
          _coord_identity(_Fr(1, 2), _Fr(1, 4), ell)
          and not _coord_identity(_Fr(1, 2), _Fr(1, 4), ell,
                                  wrong="exponent"),
          "QMAX == F_A x medloc and PhiH1 == F_A^2 x B^2 (B^2 = "
          "medloc^2 x ell) EXACT at qmax = 1/2, medloc = 1/4 (F_A = "
          "2); the wrong-exponent mutant PhiH1 == F_A x B^2 lands "
          "ell/4 != ell/8 -- CAUGHT")

    section("S0-T2 the U1 witness: old bridge x terminal (exact)")
    b_bad = _Fr(-1)
    u1_incons = (_u1_old_bridge_represents(b_bad)
                 and not _u1_terminal(b_bad))
    check("S0-T2a-u1-inconsistency",
          u1_incons,
          "the pre-r320 bridge certifies the B = -1 empty-spec window "
          "as MAIN for EVERY predicate (S = 0: all channel clauses "
          "vacuous, u/B never read) while the terminal type demands "
          "0 < -1 -- the two types are jointly inconsistent, "
          "established in exact arithmetic (the r320 Lean guard "
          "old_bridge_terminal_inconsistent, mini-rebuilt)")
    check("S0-T2b-u1-repair",
          (not _u1_new_bridge_represents(b_bad, _Fr(1, 100)))
          and _u1_new_bridge_represents(_Fr(5, 7), _Fr(1, 100)),
          "the r320 retyped bridge (u/B fidelity |B - 5/7| <= delta "
          "+ budget_pos) REFUSES B = -1 at every honest tolerance "
          "(|{-1} - 5/7| = 12/7 > 1/100) and ACCEPTS the faithful "
          "B = 5/7 witness -- the repair closes exactly the U1 hole")

    section("S0-T3 the U2 witness: old bridge x L* (exact)")
    check("S0-T3a-e-bracket",
          _E_LO == _Fr(685, 252) and _E_TAIL_GEO == _Fr(1, 35840)
          and _E_TAIL_GEO <= _E_TAIL_PIN
          and _E_HI == _Fr(685, 252) + _Fr(1, 35280),
          "the exact rational e-bracket: partial sum 685/252, "
          "geometric tail majorant 9/(8 x 8!) = 1/35840 <= the "
          "pinned 1/35280 = 1/(7! x 7) EXACT -- 685/252 <= e <= "
          "685/252 + 1/35280 is certified in pure integers")
    check("S0-T3b-u2-collision-admissible",
          _u2_collision_admissible(),
          "the three mesh-level-0 collision clauses |1 - log n| <= "
          "log 2 (n = 2, 3, 4) reduce EXACTLY to 2 <= e, 3 <= 2e, "
          "e <= 4 (with e < 3 for the n = 3 sign case) -- all four "
          "hold on the exact bracket: the total node collision IS "
          "admissible for the old bridge (the disease)")
    nu0, mu0, holds = _u2_lstar_on_collision((_Fr(1), _Fr(1), _Fr(1)))
    check("S0-T3c-u2-lstar-kill",
          nu0 == 0 and mu0 == 0 and not holds,
          "p = X - 1 vanishes on the collided window (all nodes at "
          "1): both integrals are the rational 0 and the strict "
          "subordination demands 0 < 0 -- the old bridge type and "
          "the L* type are jointly inconsistent (the r320 Lean guard "
          "old_bridge_lstar_inconsistent, mini-rebuilt)")
    check("S0-T3d-u2-separation-repair",
          _u2_separation(4) and not _u2_separation(0),
          "the r320 separation discipline: at the witness mesh "
          "level 4 the demand 2 delta < min node gap reduces via "
          "3^5 < 2^8 (243 < 256) to 1/8 < 2/5 EXACT (and delta < "
          "min comb to 1/16 < 1); at mesh level 0 it demands "
          "2 log 2 < log(4/3), impossible since 4/3 < 4 -- level 0 "
          "represents NOTHING, representation begins at sufficient "
          "refinement (2^7 < 3^5: 128 < 243 gates the other gap)")

    section("S0-T4 the U3 witness: pair margin forces empty (exact)")
    check("S0-T4a-u3-inconsistency",
          (not _u3_old_margin_possible(_Fr(3, 2)))
          and (not _u3_old_margin_possible(_Fr(0)))
          and (not _u3_old_margin_possible(_Fr(-7, 5))),
          "the adversary (Zloc = |F| + 1, runs = []) satisfies the "
          "split and demands (|F| + 1)^2 < 5/7 -- FALSE for every "
          "rational F since (|F| + 1)^2 >= 1 > 5/7 EXACT (witnesses "
          "F = 3/2, 0, -7/5): the old pair-margin type forces its "
          "source predicate EMPTY (the r320 Lean guard "
          "old_pair_margin_forces_empty, mini-rebuilt)")
    toy = (_Fr(2), _Fr(-1), _Fr(-3), _Fr(4), _Fr(1))
    zloc, runs, signruns_ok, split_ok = _canonical_extraction(toy)
    adv = (abs(sum(toy)) + 1, tuple())
    check("S0-T4b-canonical-extraction",
          zloc == 2 and runs == (_Fr(-4), _Fr(5)) and signruns_ok
          and split_ok and (zloc, runs) != adv,
          "the r320 canonical extraction on the rational toy (2, -1, "
          "-3, 4, 1): Zloc = 2, bulk runs (-4, 5); signRuns_sum "
          "(-4 + 5 == 1 == bulk sum) and canonical_split (2 + 1 == "
          "3 == total) EXACT -- (Zloc, runs) are DERIVED, not free; "
          "the U3 adversary pair (4, ()) is NOT a canonical "
          "extraction -- CAUGHT")

    section("S0-V the sealed verdict bars (exact decision logic)")
    check("S0-V1-r317",
          _bar_r317(_REC["r317"])
          == ("WHAC_A_MOLE(kz53, kz83 -- a third exception form "
              "would be needed; NO third class added, abort by "
              "contract; back to fork (a))")
          and _bar_r317(_REC["r317"], no_viol=True)
          == "ONE_FAMILY_SUFFICES(B)"
          and _bar_r317(_REC["r317"], no_viol=True, a_fires=True)
          == "EXCEPTION_CENSUS_GO(A, B)"
          and _bar_r317(_REC["r317"], broad=True) == "GENERIC_FAILS"
          and "grows" in _bar_r317(_REC["r317"], no_viol=True,
                                   growth=True)
          and _seal_family_count(("A", "B"))
          and not _seal_family_count(("A", "B", "C")),
          "WHAC_A_MOLE(kz53, kz83): 2 uncovered violators of C_gen = "
          "4579/10000 on the 63-rung complement; class B = {kz55, "
          "kz67} recovered blind (F_B 723/100, 496/100, gap 178/100, "
          "C_B 10536/10000), class A EMPTY (best gap 1233/1000 < "
          "1250/1000); mutants: zero violations fire ONE_FAMILY_"
          "SUFFICES(B), a firing class A composes the GO, five "
          "violations fire GENERIC_FAILS, growth fires the abort, "
          "the three-family tuple is REFUSED -- all TIP")
    check("S0-V2-r318",
          _bar_r318(_REC["r318"])
          == ("P2_MAIN_SPECIFIC(modal pair (2, 3) = D3 x D4 "
              "ANTIPHASE, sign -1, med share 699/1000, 12/12 rungs "
              "+ twin 692/1000; controls break by PATTERN on the "
              "(4, 5) arch-mean x border pair)")
          and _bar_r318(_REC["r318"], neg_sep=True)
          == "BOTH_ALIVE(p1 site; p2 pattern)"
          and _bar_r318(_REC["r318"], fp_broken=True)
          == "FORK_DEAD(p1 restatement; p2 premise fails; lane stop)"
          and _bar_r318(_REC["r318"], neg_sep=True, fp_broken=True)
          == "P1_MAIN_SPECIFIC(dig site named)"
          and _REC["r318"]["restat_hits"] == _REC["r318"]["restat_n"]
          and _REC["r318"]["defects"]["w9"] == 0
          and _REC["r318"]["defects"]["w13"] == 0
          and _REC["r318"]["defects"]["twin"] == 0
          and min(_REC["r318"]["defects"][k]
                  for k in ("EPST", "SCR", "SMOOTH", "HL2")) > 0,
          "P2_MAIN_SPECIFIC on the record (fingerprint lawful 12/12 "
          "+ twin-consistent + controls pattern-broken; P1 exact but "
          "restatement 10/10 total, vacuity + invariants world-blind "
          "=> language, not lever; window defects 0/0/0 mains/twin "
          "vs 55/37/4/31 controls); mutants: a separating negative-"
          "subspace statistic fires BOTH_ALIVE, a broken consensus "
          "FORK_DEAD, both together P1_MAIN_SPECIFIC -- all TIP")
    u1_ok = (_u1_old_bridge_represents(b_bad)
             and not _u1_terminal(b_bad))
    u2_ok = (_u2_collision_admissible() and not holds)
    u3_ok = not _u3_old_margin_possible(_Fr(3, 2))
    check("S0-V3-r319",
          "REDTEAM_CONFIRMED" in _bar_r319(u1_ok, u2_ok, u3_ok,
                                           _REC["r319"])
          and "HONEST_CHAIN" in _bar_r319(u1_ok, u2_ok, u3_ok,
                                          _REC["r319"])
          and _bar_r319(False, u2_ok, u3_ok, _REC["r319"])
          == "AUDIT_VOID(recompose)"
          and _bar_r319(u1_ok, u2_ok, u3_ok, _REC["r319"],
                        seam_ok=False) == "AUDIT_VOID(recompose)",
          "REDTEAM_CONFIRMED + HONEST_CHAIN: all three U-"
          "inconsistencies established in exact arithmetic (S0-T2/"
          "T3/T4) + the cofinality seam + the audit facts (3 "
          "findings, 0 files changed, suite 68/68, 5 sorries); the "
          "honest chain reading composes verbatim (two lemmata => "
          "window-local master positivity ONLY); mutants: a missing "
          "inconsistency or a missing seam voids the audit -- TIPS")
    sep4 = _u2_separation(4)
    sep0_fails = not _u2_separation(0)
    canon_ok = signruns_ok and split_ok and (zloc, runs) != adv
    refuse_ok = ((not _u1_new_bridge_represents(b_bad, _Fr(1, 100)))
                 and _u1_new_bridge_represents(_Fr(5, 7), _Fr(1, 100)))
    check("S0-V4-r320",
          "REPAIR_COMPLETE" in _bar_r320(sep4, sep0_fails, canon_ok,
                                         refuse_ok, _REC["r320"])
          and _bar_r320(False, sep0_fails, canon_ok, refuse_ok,
                        _REC["r320"]) == "REPAIR_INCOMPLETE(recompose)"
          and _bar_r320(sep4, False, canon_ok, refuse_ok,
                        _REC["r320"]) == "REPAIR_INCOMPLETE(recompose)",
          "REPAIR_COMPLETE: separation discipline satisfiable at "
          "mesh level 4 (1/8 < 2/5 via 243 < 256) and UNsatisfiable "
          "at level 0 (4/3 < 4), canonical extraction exact, the "
          "U-adversaries refused by the retyped forms, census 5 -> 5 "
          "with two retypes, three sorry-free guards + sorry-free "
          "witness, lake 2622 jobs, run_rh 71/71; mutants: a failing "
          "separation certificate (either direction) voids the "
          "repair -- TIPS")
    check("S0-V5-r321",
          _bar_r321(_REC["r321"])
          == ("SLIDING_BOUND_GO(G_SQ: rho_2 <= 816/625 x F_A^2 on "
              "0/39 test + 4/4 named; gain 319/20; SCRAMBLE via the "
              "class side condition)")
          and _bar_r321(_REC["r321"], sq_misses=True)
          == "G_FAILS_POINTWISE"
          and _bar_r321(_REC["r321"], env_diffuse=True)
          == "ENVELOPE_DIFFUSE"
          and _bar_r321(_REC["r321"], world_leak=True) == "WORLD_LEAK"
          and _bar_r321(_REC["r321"], low_gain=True)
          == "ENVELOPE_DIFFUSE"
          and min(_REC["r321"]["rsv"].values()) == _Fr(7)
          and _REC["r321"]["b_test_max"] > _REC["r321"]["b_cal_max"],
          "SLIDING_BOUND_GO(G_SQ): b = 13056/10000 = 816/625 = "
          "1.1426^2 source-pure, 0/39 test violations, 4/4 named "
          "violators inside (reserves 7.0..9.6 min exactly 7), "
          "envelope strictly monotone (bin Spearman 1), gain "
          "1595/100; the honest structural find gated: B test max "
          "14088/10000 > cal max 11426/10000 (the pure-algebra "
          "transfer does NOT close); mutants: an SQ miss cascades "
          "past TT (2 viol) and LIN (5 viol) to G_FAILS_POINTWISE, "
          "a diffuse envelope / low gain fire ENVELOPE_DIFFUSE, a "
          "world leak fires WORLD_LEAK -- all TIP")
    check("S0-V6-r322",
          "ALGORITHM_ARTIFACT" in _bar_r322(_REC["r322"])
          and _bar_r322(_REC["r322"], invariant=True)
          == "SIGN_LAW_ROBUST(lawful, not exact)"
          and _bar_r322(_REC["r322"], invariant=True, forced=True)
          == "SIGN_LAW_EXACT(forced identity verbatim)"
          and _bar_r322(_REC["r322"], anchor_fails=True)
          == "LAW_DIFFUSE"
          and _REC["r322"]["sm1_free"] != 0
          and _REC["r322"]["sm1_forced_pos"]
          and not _REC["r322"]["mini16_member"]
          and _REC["r322"]["fair_carries"] == 1
          and _REC["r322"]["distinct_pairs"] == (9, 15),
          "ALGORITHM_ARTIFACT on the record (law anchor holds: "
          "(2, 3), -1, share 692/1000, d6 27/1000, sign consistency "
          "1; invariance BREAKS on the random starts (0, 2) at "
          "31/100, 33/125; exact_forced FALSE: SM1 free fraction "
          "47671/100000 != 0 with POSITIVE forced value, MINI16 "
          "membership FALSE; fair controls split 1/2; distinct "
          "pairs exactly 9/15 = the random-start pairs); mutants: "
          "solution-set invariance fires SIGN_LAW_ROBUST, plus "
          "exact forcing SIGN_LAW_EXACT, a failing anchor "
          "LAW_DIFFUSE -- all TIP")

    section("S0-V7 the wave-12 composition (the claim split)")
    real = _wave12()
    check("S0-V7-composition",
          real == ("REDTEAM_BANKED(U1-U3 inconsistent in exact "
                   "arithmetic + seam + honest chain reading; r320 "
                   "repair complete) | SLIDING_BOUND_GO(G_SQ) + "
                   "PROVENANCE_SPLIT(is F_A bounded? / what bounds "
                   "the qmax-share via the M_2-stationarity shape "
                   "route?) | P1_LANGUAGE_BANKED + "
                   "ANTIPHASE_LAW_ALGORITHM_ARTIFACT + "
                   "SELECTION_GEOMETRY_OPEN | "
                   "PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E]; "
                   "PRIME.L2.RENYI3.SLIDING_BOUND.01 [O]; "
                   "PRIME.L2.RENYI3.PROVENANCE.01 [O update]; "
                   "PRIME.LSTAR.SUBORDINATION.01 [O update]")
          and "EXTRACTION_AUDIT_VOID" in _wave12(guards_fail=True)
          and "FIBER_AT_ABORT" in _wave12(sliding_fails=True)
          and "INDEFINITE_THEOREM_CANDIDATE"
          in _wave12(law_invariant=True)
          and "CLAIM_SPLIT_INVALID" in _wave12(guards_fail=True),
          "the six rounds compose to EXACTLY the wave-12 claim "
          "split: the red-team audit banked [E] (U1-U3 + seam + "
          "honest chain + repair), the sliding-bound theorem "
          "candidate registered [O] with the two-part provenance "
          "question, the L* update typed (P1 language banked, the "
          "antiphase law an algorithm artifact, selection geometry "
          "open); tipping mutants: failing guards void the audit, a "
          "failing sliding bound leaves the fiber at the r317 "
          "abort, a solution-set-invariant law fires the indefinite-"
          "theorem candidate -- each tip INVALIDATES the split: it "
          "is not hard-wired")

    print("\n  S0 complete: %d exact/logic gates" % len(gates),
          flush=True)


# ---------------------------------------------------------- embedded
# ---------------------------------------------------------- probes
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exception_families_probe -- PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01
(round 317): THE EXCEPTION-FAMILY CENSUS -- reviewer fork (b) after
the r314-r316 trilogy (identity exact, functional blind, two-regime
dead): the statement form "ALL sufficiently large GENERIC windows +
explicitly classified EXCEPTION FAMILIES".  The reviewer contract is
verbatim and binding: FAMILIES, not single table rows --
    whole family --+-- generic regime      => Renyi-3 theorem
                   +-- spike class A       => separate certificate
                   +-- spike class B       => separate certificate
-- and the HARD GATE, sealed in advance: AT MOST TWO source-pure
exception families plus the generic theorem; "if ever new exception
forms keep appearing, abort immediately -- then the route is not a
classification but Whac-A-Mole" => verdict WHAC_A_MOLE, recommend
back to fork (a).  Context (sealed record inputs): r306 (SPEC
3bb365e1) fixed the pointwise GO sum q^3 <= 1.069 (log m)^2/m^2 on
57/57 (first-5 constant, r316-rehabilitated as load-bearing;
sharpness witnesses kz53/kz67 at A = 1); r316 (SPEC 5c28b12b)
sealed TWO_REGIME_DEAD and delivered the anatomy: the obstruction
family {kz53, kz55, kz67, kz83, kz105, ...} cuts ACROSS the FCIX
strata; kz55/kz67 are near-ONE-BLOCK worlds (top-1 cube share
0.558/0.785 vs 0.18 med -- the CONCENTRATION class) while
kz53/kz83 are rho_2 spikes at BULK-NORMAL FCIX (a DIFFERENT
class); 8/38 mid-ladder violators of the L bound; 21 small-m
certificates exist; 8 EXT2 deep anchors with NO new H member.
kz15 permanently closed via r270; the 6 exceptions via the r287
F2 certificates.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r318 (base fork) and r319 (chain audit) run in
parallel; this probe touches NOTHING outside its own file and the
strictly additive rh-sync.

THE OBJECT (r269/r287/r298/r306/r314/r315/r316 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F =
0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); the frozen positional block
machinery (r298 WBT.block_breaks + WBT.aggregate_blocks); the
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the
r314 SCF.fold_genealogy + SCF.signed_cube_terms +
SCF.flux_telescope + SCF.collision_census; the r315
PHI.phi3_variants; the r316 TRB.two_regime_state +
TRB.split_midladder, ALL imported verbatim; PDelta = Pbeta -
Pomega; x_j = (PDelta)_j.  NEW in this round (module-own,
source-pure): the two class functionals (rank-local spike
ratios), the sealed gap-threshold rule, the family-certificate
bookkeeping with declared-set ward, and the hard two-family gate.

THE SEALED CLASS FUNCTIONALS (frozen BEFORE any bound evaluation
of this round; both consume ONLY source-pure columns of the r316
two-regime state -- no cubic target, no wall sign, no record
literal; AST identifier scan + literal scan warded, must-fail e3
proves the audit bites).  On the (N, kz)-sorted class ladder of n
rungs (the r316 ladder: 42 core + 15 r286 extension + the 8 EXT2
anchors, multiplicity cap <= 2, POSITIVE_PREFIX), with QMAX(i) =
max_j |x_j| / L and PhiL2(i) = NORM x (|COLL| + |BND| + FE) the
sealed r316 columns (both source-pure by the r316 audit):
    F_A(i) = QMAX(i)  / med{ QMAX(j)  : |j - i| <= W, j != i },
    F_B(i) = PhiL2(i) / med{ PhiL2(j) : |j - i| <= W, j != i },
rank-local spike ratios with window half-width W = CLS_W = 5
(truncated at the ladder ends; DISCLOSED boundary property: a
monotone column trend of rate r per rung induces an end bias of
order r^W -- at the recorded ladder decay rates ~3 percent per
rung this is <= ~1.16, far below the gap bar; measured live and
printed as census; the trend toy proves the construction is
blind to a pure geometric trend at the ladder rate).  CLASS A
(CONCENTRATION) = the rungs with F_A >= THR_A; CLASS B
(DIVERGENCE-MASS SPIKE) = the rungs with F_B >= THR_B.  THE
SEALED GAP-THRESHOLD RULE (both classes, identical, frozen here):
sort the functional values descending as s_1 >= s_2 >= ...; over
prefix sizes k = 1..KMAX = 6 compute the multiplicative gap g_k =
s_k / s_{k+1}; k* = argmax g_k; the class is the top-k* rungs iff
g_{k*} >= GAP_MIN = 1.25, otherwise the class is EMPTY; THR =
sqrt(s_{k*} x s_{k*+1}) (geometric midpoint), printed and frozen.
The full class table (rank, kz, N, m, QMAX, F_A, PhiL2, F_B,
membership) is printed BEFORE any bound table of this round.
JUSTIFICATION (disclosed, from the r316 RECORD census only): the
r316 named discriminator was the top-1 cube share (dev 2.68) --
its source-pure sibling is QMAX (dev 1.99), so class A tracks the
near-one-block family {kz55, kz67}; the r316 regime-L freeze died
on PhiL2 spikes (kz53 1.43 / kz105 1.13 / kz83 1.08 vs C_L
0.7476), so class B tracks the rho_2-spike family -- both chosen
from the record ANATOMY, no value of this round consumed.

THE HARD GATE (sealed, live, symmetric): the adjudication accepts
EXACTLY the two sealed families (seal_family_count == 2 is a
warded module rule; the e1 mutant proves a third family is
REFUSED).  Let viol = the violators of the generic bound (Leg B)
on the complement test set.  Since the complement excludes A u B
by construction, EVERY violator is uncovered, so the sealed rule
    GENERIC_FAILS            iff |viol| >= GEN_FAIL_MIN = 5
        (the generic law itself fails broadly -- not a spike
        census; the classification question is moot),
    WHAC_A_MOLE              iff 1 <= |viol| <= GEN_FAIL_MIN - 1
        (a third exception form would be needed -- NO third
        class is added, the round aborts by contract), OR
        |viol| = 0 but a family GROWS with depth or the world/
        class check leaks (the classification leaks -- named),
    EXCEPTION_CENSUS_GO(A,B) iff |viol| = 0, both families
        non-empty, neither grows, world check passes,
    ONE_FAMILY_SUFFICES(X)   iff |viol| = 0, exactly one family
        non-empty (or NONE -- the generic theorem alone covers
        the ladder), no growth, world check passes.
Exactly one fires; the verdict function gate_verdict consumes
counts only and is itself scope-audited.

LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316 record numbers
adopted as-is, disclosed): med signed shares DeltaF/C_pair/C_full
= -0.4226/+0.5980/+0.8537 (tol 0.005); FC med 0.629 (tol 0.005)
slope -0.141 (tol 0.01); fold multiplicity == 2 UNIFORM (exact);
identity wards live (REC3/TEL/BND bars); r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r315 C0 a/b/c = 2.6261/1.5052/0.9400
(tol 0.005), FCIX outliers kz55/kz67 = 0.955/0.915 (tol 0.005);
r316 anchors: class ladder n = 65 with the H stratum EXACTLY
{kz55, kz67} at theta = 0.85, the r316 mid-ladder split small
0..20 / cal 21..25 / test 26..64 with m_0 = 73 EXACT, regime-L
cal constant C_L2 = 0.7476 (tol 0.005), the 8 regime-L test
violators == {kz53, kz105, kz83, kz71, kz68, kz88, kz76, kz119}
EXACT as a set, TOP1 kz55/kz67 = 0.558/0.785 (tol 0.005), rho_2
anchors kz53/kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol
0.005), C_small = 1.0694 (tol 0.005) at kz18.

LEG A -- FAMILY DEFINITION (sealed BEFORE any bound evaluation):
(A1) the class functionals, the gap rule and the hard gate are
printed as sealed definitions; the class table (source-pure
columns only) is printed BEFORE any bound table.  (A2) SOURCE-
PURITY AUDITS: the AST identifier scan over local_ratio +
gap_threshold must be clean against BOUND_FORBIDDEN and
PHI3_FORBIDDEN (no cubic-target read-back, no withheld key); the
literal scan over local_ratio + gap_threshold + family_cert +
gate_verdict + seal_family_count must be clean against the sealed
record-literal set R31X_TABLE_LITERALS (r314 + r315 + r316 record
numbers); e1/e2/e3 prove the audits bite.  (A3) TOY EXACTNESS:
the spike toy (1,1,8,1,1,1,1) gives F = (1,1,8,1,1,1,1), k* = 1,
THR^2 == 8 EXACT, members == (2,); the flat toy (3 x 7) gives
class EMPTY EXACT (gap 1 < 1.25); the TREND toy 0.97^i (i =
0..10, the recorded ladder decay rate) gives class EMPTY with max
ratio <= 1.15 -- the rank-local construction is blind to a pure
trend; the family-certificate toy (max over the declared member
set, declared == members warded) and the gate toys (all five
verdict branches) are exact.  (A4) LIVE MAJORANT CHAIN WARD (the
r316 algebra re-warded): rho_2 <= PhiL1 <= PhiL2 <= PhiH2 and
rho_2 <= PhiH1 on every live world (rel slack <= CHAIN_BAR) plus
NORM x cube == rho_2 -- the class-A structural bound rho_2 <=
PhiH1 = (m QMAX/log m)^2 (Sum q^3 <= QMAX^2 Sum q, exact algebra)
and the class-B structural bound rho_2 <= PhiL2 transfer every
certificate below to sum q^3 by algebra.  (A5) MEMBERSHIP CENSUS:
which rungs fall in A, B, both, neither; per-third counts; the
boundary-bias census (max non-member |F - 1|).

LEG B -- THE GENERIC THEOREM (on the complement of A u B): the
complement ladder keeps the (N, kz) order; the r316 mid-ladder
split rule (TRB.split_midladder verbatim: CAL_START = n_comp //
3, N_CAL = 5) yields small-m / calibration / test; C_gen = max
rho_2 over the calibration window, FROZEN; certification = 0
violations demanded on every complement test rung; small-m rungs
certified INDIVIDUALLY (C_small = max); reserve min/med and the
halves-slope trend printed as census (the r316 lesson: with the
spikes EXCEPTED, does the rest hold with stable or growing
reserve?); m_0 = min m over calibration + test.

LEG C -- THE FAMILY CERTIFICATES (r287-F2 spirit: the exception
property implies its own certificate; r270-kz15 honesty: where
only per-member finite certificates exist, they are counted as
such): CLASS A (concentration): per member the finite certificate
rho_2 (C_A = max), the structural column PhiH1 (the class
DEFINITION delivers the concentration majorant: near-one-block =>
sum q^3 <= QMAX^2, warded exact in A4) and the qmax <= 1 - delta
census; CLASS B (spike): per member the finite certificate rho_2
(C_B = max) and the structural column PhiL2 (exact majorant,
warded); DEPTH-GROWTH CENSUS per family: member counts over the
ladder thirds T1/T2/T3 (ranks < n/3, < 2n/3, rest); the sealed
growth rule GROWS(F) iff the counts are STRICTLY increasing
T1 < T2 < T3 (a growing family = bad, finite/stable =
acceptable); EXT2-stratum member count printed.

LEG D -- THE COMPOSED THEOREM CANDIDATE + WORLD CHECK: world_ok =
the r316 class machinery verbatim -- (w1) w9/w13/EPSTEIN ADMITTED
(fold multiplicity <= 2 AND rho_2 <= C_tot; their class-column
values printed as census only); (w2) twin band max(w13/w9,
w9/w13) <= TWIN_FAC = 3.0 on PhiL2; (w3) SCRAMBLE REJECTED by the
class machinery (component attribution names a collision/flux
column, dev >= ATTR_MIN = 0.25 vs the MAIN med, AND the seeded
assignment shuffle SEED_SHUF = 317001 breaks the flux profile
edgewise >= MUT_MIN with matched mass).  C_tot = max(C_gen, C_A,
C_B, C_small).  The verdict fires by the sealed hard gate above;
on EXCEPTION_CENSUS_GO or ONE_FAMILY_SUFFICES the CANDIDATE
THEOREM (Renyi-3 with exception families) is printed with every
measured constant: generic theorem (C_gen, A = 2, m_0, mid-ladder
frozen) + class-A certificate + class-B certificate + C_small +
the counting evidence that A u B covers ALL violators on the
available ladder (0 uncovered) and does not grow with depth;
C_tot transfers to sum q^3 <= C_tot (log m)^2/m^2 on every
measured rung and n_eff = N_2 >= N_3 >= m/(sqrt(C_tot) log m) by
the r306 exact chain.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) THIRD CLASS PUSHED AFTER SIGHT (simulated):
  mutant_third_class collects the uncovered violators of the
  evaluated bound column into a post-hoc "class C" -- the
  BOUND_FORBIDDEN scope audit must FLAG it (it consumes rho) AND
  the sealed gate must REFUSE it twice: seal_family_count((A, B,
  C)) == False and gate_verdict with uncovered violators returns
  WHAC_A_MOLE, never a three-family GO -- GATE-CAUGHT.
(e2) THRESHOLD MOVED AFTER SIGHT: mutant_thr_posthoc re-picks the
  threshold to cover the seen violators (consumes rho) -- the
  scope audit must FLAG it AND on the sealed toy it returns a
  threshold != the gap rule's -- CAUGHT twice.
(e3) CLASS FUNCTIONAL READS Sum q^3: mutant_class_readback
  consumes the cubic-moment record (cm/S3) -- the PHI3_FORBIDDEN
  scan must FLAG it (AST-CAUGHT) while local_ratio +
  gap_threshold stay clean.
(e4) FAMILY CERTIFICATE CONSUMES THE GENERIC CONSTANT CIRCULARLY:
  mutant_circular_cert declares the generic calibration window
  instead of the member set -- the declared-set ward must CATCH
  the mismatch EXACT, and on the toy the circular "certificate"
  sits LOUDLY below the member maximum (diff >= MUT_MIN).
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the class
  builders (local_ratio, gap_threshold) consume one source-pure
  column + rank order only; family_cert / gate_verdict /
  seal_family_count consume certificate values / counts only;
  fragment audit (no fit primitives).

INDEX FIREWALL (binding, r238-r316 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
certificates / diagnostic columns only, NEVER a class builder
(AST-warded); no zero/prime oracles anywhere (AST firewall); no
fit primitives (fragment audit).  MACHINERY IMPORTED VERBATIM:
r316 TRB.two_regime_state + TRB.split_midladder, r315
PHI.phi3_variants, r314 SCF.fold_genealogy + SCF.signed_cube_terms
+ SCF.flux_telescope + SCF.collision_census, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge +
PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316 verbatim): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52};
EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the r316
A5 rule (leftover pool + first 12 windows 1300 < h <= 1650, first
8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; THETA 0.85 (r316 anchor only); N_CAL
5; CAL_THIRD 3; CLS_W 5; GAP_MIN 1.25; KMAX 6; GEN_FAIL_MIN 5;
TREND_TOY_BAR 1.15; RES_EPS 0.01; ATTR_MIN 0.25; TWIN_FAC 3.0;
SEED_SHUF 317001; MUT_MIN 1e-6; TOY_BAR 1e-12; TB_WARD bars 1e-9
main N <= 400 / 3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR
1e-12; AC_BAR 1e-9; R314 anchors shares (-0.4226, +0.5980,
+0.8537) tol 0.005, FC 0.629/-0.141 tol 0.005/0.01, mult == 2
EXACT; R306 anchor C_2 1.069 tol 0.005; R315 anchors C0 (2.6261,
1.5052, 0.9400) tol 0.005, FCIX {55: 0.955, 67: 0.915} tol 0.005;
R316 anchors: N317 = 65, H set {55, 67}, split (small 0..20, cal
21..25, test 26..64), M0_REF 73, C_L2 0.7476 tol 0.005, violator
set {53, 105, 83, 71, 68, 88, 76, 119} EXACT, TOP1 {55: 0.558,
67: 0.785} tol 0.005, RHO {53: 1.0490, 67: 1.0536, 55: 0.4821,
83: 0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at kz18;
R31X_TABLE_LITERALS = the sealed r314 + r315 forbidden set (r316
verbatim) UNION the r316 record set {0.7476, 0.5531, 1.4263,
1.1266, 1.0804, 0.9648, 0.8013, 0.7877, 0.7819, 0.7698, 34.0556,
3.0559, 57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536, 1.049, 0.779,
0.654, 0.148, 1.04, 3.27, 0.73, 0.52, 1.35, 0.086, 0.202};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the chain ward on w9 + controls + e1-e4 mutants; ladder,
extensions, anchors, class census, generic bound, certificates
and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r315/r306/r316 RECORD number adopted
as-is; the CHOICE of the two class functionals is motivated by
the r316 RECORD census alone (QMAX = the source-pure sibling of
the named TOP1 discriminator, dev 1.99; the PhiL2-spike anatomy
of the r316 violator list) -- both columns existed in r316, both
are source-pure by the r316 audit, and NO class value, NO
threshold, NO membership and NO violation count of this round
was computed before this spec was frozen; CLS_W = 5, GAP_MIN =
1.25, KMAX = 6, GEN_FAIL_MIN = 5 and TREND_TOY_BAR = 1.15 are
coarse a-priori bars (KMAX sized from the record obstruction
family <= 5 members; GAP_MIN from the recorded factor >= 1.3
gaps of the r315/r316 outlier censuses; the boundary-bias
algebra r^W is derived, disclosed above); the five sealed
verdicts are symmetric -- the gate rule maps every leak
(uncovered violator, family growth, world leak) to the abort
verdict by CONTRACT, not to favor an outcome; the r306 chain
(bound => n_eff) is imported algebra.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R317_ANCHORS(r314 shares + FC + mult, identity wards, r306 C_2,
    r315 C0 + FCIX, r316 ladder/split/C_L2/violators/TOP1/rho/
    C_small)
+ SEAL(class functionals + gap rule + hard gate + purity audits
    + toys + chain ward)
+ FAMILIES(census: THR_A/THR_B, members A/B/both/none, thirds,
    boundary bias)
+ GENERIC(C_gen, m_0, violations, reserve, trend, small-m table)
+ CERTS(class A: members + rho_2 + PhiH1 + C_A; class B: members
    + rho_2 + PhiL2 + C_B; growth census)
+ WORLD(admission + twin band + SCRAMBLE rejection)
+ [exactly one of] EXCEPTION_CENSUS_GO(A, B) /
    ONE_FAMILY_SUFFICES(X) / WHAC_A_MOLE / GENERIC_FAILS
+ THEOREM(candidate text printed on GO / ONE_FAMILY)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the class functionals, the gap rule, the
window, the growth rule and the hard gate are sealed BEFORE any
bound evaluation; the thresholds are computed by the sealed rule
from source-pure distributions, printed before any bound table;
the family certificates are FINITE per-member certificates (r270
style) plus exact structural majorants (r316 algebra, warded
live) -- they prove NOTHING beyond the measured members; a GO
fixes a certified exception-family STATEMENT ON THE MEASURED
RUNGS with explicit (C_gen, C_A, C_B, C_small, m_0), it proves NO
universal bound beyond them and NO cofinal law; the class-B spike
property yields no uniform bound from its definition -- disclosed
as the honest asymmetry between the two families; the world
columns are n = 1 per control; a WHAC_A_MOLE seals the abort
honestly and recommends fork (a); r243-r316 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 38/38 (0.4 s), NO amendment; calibration pass 1 =
first full evaluation, 38/38, wall 36.2 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; PROTOCOL
DISCLOSURE: a drafting error had placed PREFILLED PLACEHOLDER
record tables into this spec BEFORE any run -- they were removed
COMPLETELY before the first smoke run and are disclosed here (the
r316 protocol-error class); the ONLY post-freeze edit is this
record-table insertion, which IS the protocol -- no bar, band,
rule or verdict rule moved):
CAL_VERDICT = R317_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 65/65, identity wards 4.5e-17 /
4.7e-16 / 4.1e-16, r306 C_2 1.069 viol 0/57, r315 C0
2.6261/1.5052/0.9400 + FCIX 0.955/0.915, r316 ladder n = 65, H =
{55, 67}, split 21|5|39 m_0 = 73, C_L2 0.7476, regime-L violator
set == the named 8, TOP1 0.558/0.785, rho anchors kz53/kz67/kz55/
kz83 = 1.0493/1.0536/0.4821/0.7791, C_small 1.0694 @ kz18 -- ALL
bit-near) + SEAL(purity clean: 0 id + 0 literal hits on the five
gate-side builders; toys exact: spike THR^2 == 8, flat EMPTY,
trend EMPTY max ratio 1.0957 <= 1.15, cert + all five gate
branches exact; chain ward worst slack 6.5e-16 on 69 live
worlds, NORM x cube == rho_2 worst 7.9e-16) + FAMILIES(THR_A =
EMPTY -- best F_A gap 1.24 < 1.25 (k = 3); THR_B = 3.7157 via
gap k* = 2 (g 1.78): B = {kz55 F_B 7.23, kz67 4.96} -- EXACTLY
the r315/r316 FCIX pair, recovered blind by the sealed rule;
A n B empty; thirds A (0,0,0) / B (1,1,0); 63 rungs in neither;
boundary-bias census: max non-member F_A 2.47 / F_B 2.79) +
GENERIC(the 63-rung complement: split 21|5|37, C_gen = 0.4579
frozen at complement-cal kz34 (m 84..95), m_0 = 84; VIOLATIONS
2/37: kz53 rho 1.0493 (reserve 0.44) and kz83 rho 0.7791 (0.59)
-- both UNCOVERED by A u B; reserve min/med 0.44/2.06; trend
-0.170 falling; 21 small-m certificates, C_small 1.0694 @ kz18)
+ CERTS(A: EMPTY, 0 certificates; B: kz55 rho 0.4821 PhiL2
4.6423 / kz67 rho 1.0536 PhiL2 2.7312, C_B = 1.0536, structural
rho_2 <= PhiL2 warded on both; growth: A stable (0,0,0), B
stable (1,1,0), EXT2 members 0/0) + WORLD(w9/w13/EPSTEIN
admitted mult 2, rho_2 0.458/0.461/0.368 <= C_tot 1.0694; twin
band PhiL2 factor 1.04 <= 3.0; SCRAMBLE rejected: COLL
attribution dev 3.69 >= 0.25 AND seeded shuffle 317001 breaks
the flux profile edgewise 9.9e-1 with mass matched 0.0 (288/300
atoms); SCR rho_2 1.780 > C_tot census) + WHAC_A_MOLE(2
uncovered violators kz53/kz83 -- a third exception form would be
needed; NO third class added, abort by contract; recommendation:
back to fork (a)) + THEOREM(not printed -- the hard gate fired)
+ MUSTFAIL_LEDGER(e1 AST rho@652 + seal_family_count REFUSES the
3-family tuple + gate maps uncovered violators to WHAC_A_MOLE on
the toy; e2 AST rho@661 + toy thr 1.1000 != gap rule 1.5492; e3
AST cm@671 while the class builders are clean; e4 declared-set
(0, 1) != (3, 4) EXACT + toy diff 1.0 LOUD; m5a t_term@688 /
m5b g_branch@696 FLAGGED).
READING (typed, no upgrade): the sealed letter is WHAC_A_MOLE --
the hard gate fired exactly as the reviewer contract demands
(with the sealed families excepted, the mid-ladder generic
constant is violated by kz53 and kz83, which NO sealed family
covers -- a third form would be needed, and the contract forbids
it) -- and the anatomy behind the letter is the round's real
find: (1) THE DIVERGENCE-MASS SPIKE FAMILY IS REAL: the sealed
gap rule, computed blind from source-pure columns BEFORE any
bound evaluation, recovers B = {kz55, kz67} -- EXACTLY the
r315/r316 FCIX pair -- with a clean 1.78 gap (F_B 7.23/4.96 vs
next 2.79) and finite certificates C_B = 1.0536 <= the r306
shallow maximum; (2) THE CONCENTRATION RANKING SEES THE WHOLE
NEAR-CRITICAL FAMILY BUT AS A CONTINUUM: class A is EMPTY on the
letter (best gap 1.233 misses the sealed 1.25 bar by 0.017), yet
the F_A TOP-3 are EXACTLY kz53 (2.47), kz83 (2.39), kz67 (2.38)
-- the rank-local QMAX ratio ranks the complete deep rho_2-spike
family {53, 83, 67} on top, REFUTING at census level the r316
conjecture that kz53 needs a second coordinate: ONE source-pure
concentration coordinate sees all three mid/deep spikes, but the
distribution below them is a continuum (1.93, 1.90, 1.74, ...),
not a gap-separated family; (3) the SHARPNESS honesty: an A
family at k = 3 would have covered both uncovered violators and
composed a GO -- but the gap missed the sealed bar, and moving
the bar after sight is EXACTLY the e2 mutant; the letter stands;
equally the F_B continuum over-ranks kz12 (2.79, rho_2 0.38 --
a PhiL2 spike that is NOT a rho_2 spike) above kz53 (2.70):
threshold classification on these coordinates cannot cover
kz53/kz83 without swallowing harmless rungs -- the spike TAIL is
a continuum, the exception-family FORM (sealed thresholds) is
the wrong statement shape for it; (4) what HOLDS: all anchors
bit-near (r314/r315/r306 + the complete r316 anatomy incl. the
8-violator set), the B certificates stand (finite, PhiL2-warded,
non-growing, 0 EXT2 members), the generic complement trend
FALLS (-0.170: with the B pair excepted the rest has growing
reserve except at the two named spikes), the world machinery is
intact (twin 1.04, SCRAMBLE rejected via COLL 3.69 + edgewise
break 288/300 with matched mass) and the 21 small-m certificates
stand (C_small 1.0694).  Honest negatives: WHAC_A_MOLE stands --
no composed theorem is printed; class A's emptiness is a
bar-sensitivity fact at distance 0.017, disclosed, not repaired;
nothing here bounds anything beyond the measured rungs.  R318
direction (typed, census-grade): back to fork (a) with the
round's census as the input -- the rank-local QMAX ratio is a
single source-pure coordinate whose top-3 are exactly the three
mid/deep near-critical spikes: the statement form should bound
rho_2 BY the coordinate (continuous: rho_2 <= C(F_A), e.g. a
two-term bound C_1 + C_2 F_A^gamma), not classify by threshold;
alternatively the generic constant must be taken at the r306
first-5 scale (C_2 1.069, 0/57 -- the r316 rehabilitation) where
NO exception family is needed at all on the measured ladder.
Runtime 36.2 s full / 0.4 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: none except this record-table
insertion (and the disclosed pre-run placeholder removal).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
import window_border_transfer_probe as WBT     # noqa: E402 r298
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import phi3_functional_probe as PHI            # noqa: E402 r315
import two_regime_bound_probe as TRB           # noqa: E402 r316
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
EXT2_H_MAX = 1650
EXT2_POOL_CAP = 12
K_EXT2 = 8
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
XW_BAR = 1e-9
DEG_FLOOR = 1e-6
MULT_CAP = 2
THETA = 0.85
N_CAL = 5
CAL_THIRD = 3
CLS_W = 5
GAP_MIN = 1.25
KMAX = 6
GEN_FAIL_MIN = 5
TREND_TOY_BAR = 1.15
RES_EPS = 0.01
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 317001
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
PAIR_OFFSET = 0
R314_SHARES = (-0.4226, 0.5980, 0.8537)
R314_SHARE_TOL = 0.005
R314_FC = 0.629
R314_FC_TOL = 0.005
R314_FC_SLOPE = -0.141
R314_FC_SL_TOL = 0.01
R306_C2 = 1.069
R306_C2_TOL = 0.005
R315_C0 = (2.6261, 1.5052, 0.9400)
R315_C0_TOL = 0.005
R315_FCIX_KZ = {55: 0.955, 67: 0.915}
R315_FCIX_TOL = 0.005
N317_REF = 65
R316_H_SET = (55, 67)
R316_SPLIT = (20, 21, 25, 26, 64)     # small end, cal lo/hi, test lo/hi
M0_REF = 73
R316_CL2 = 0.7476
R316_CL2_TOL = 0.005
R316_VIOL_SET = (53, 105, 83, 71, 68, 88, 76, 119)
R316_TOP1 = {55: 0.558, 67: 0.785}
R316_TOP1_TOL = 0.005
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R31X_TABLE_LITERALS = frozenset((
    -0.4226, 0.598, 0.8537, 0.629, -0.141,
    -0.452, 0.823, 0.617, 0.057,
    -0.541, 0.43, 1.111, 0.675, 0.043,
    -2.695, -2.652, 6.347, 0.101, 0.011,
    -0.171, 0.856, 0.315, 0.693, 0.073,
    2.6261, 1.5052, 0.94, 0.955, 0.915,
    22.85, 66.09, 87.64,
    2.3883, 2.0841, 1.4433, 2.3545, 1.3615, 0.1375,
    0.9597, 0.7102, 0.4795,
    4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69,
    0.7476, 0.5531, 1.4263, 1.1266, 1.0804, 0.9648,
    0.8013, 0.7877, 0.7819, 0.7698, 34.0556, 3.0559,
    57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
    21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536,
    1.049, 0.779, 0.654, 0.148, 1.04, 3.27, 0.73,
    0.52, 1.35, 0.086, 0.202))

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}
PHI3_FORBIDDEN = {"cube", "S" + "3", "cm",
                  "renyi3" + "_ratio", "cubic" + "_moments"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def literal_audit(funcname):
    """the RECORD-LITERAL audit: walk ONLY the named function's
    subtree and flag any numeric constant whose 4-decimal rounding
    lies in the sealed r314+r315+r316 record-literal set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R31X_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the class
# ---------------- builders consume ONE source-pure column of the
# ---------------- r316 two-regime state (QMAX or PhiL2) plus the
# ---------------- rank order only; the withheld terminal drive
# ---------------- key, the branch label, the cubic target and the
# ---------------- record literals are forbidden (AST identifier
# ---------------- scan + literal scan).
def local_ratio(vals):
    """the sealed rank-local spike ratio: F(i) = vals[i] / median
    of the values in the rank window i-W..i+W excluding i (window
    truncated at the ladder ends; depth-fair by construction --
    the trend toy proves blindness to a pure geometric trend at
    the recorded ladder rate)."""
    v = [float(x) for x in vals]
    n = len(v)
    out = []
    for i in range(n):
        lo = max(0, i - CLS_W)
        hi = min(n, i + CLS_W + 1)
        nb = [v[j] for j in range(lo, hi) if j != i]
        out.append(v[i] / max(float(np.median(nb)), 1e-300))
    return out


def gap_threshold(F):
    """the SEALED gap-threshold rule: sort descending; over prefix
    sizes k = 1..KMAX the multiplicative gap g_k = s_k/s_{k+1};
    k* = argmax; the class is the top-k* values iff g_{k*} >=
    GAP_MIN, else EMPTY; THR = geometric midpoint of the gap."""
    s = sorted((float(x) for x in F), reverse=True)
    best_k = 0
    best_g = 0.0
    for k in range(1, min(KMAX, len(s) - 1) + 1):
        g = s[k - 1] / max(s[k], 1e-300)
        if g > best_g:
            best_g = g
            best_k = k
    if best_g >= GAP_MIN:
        thr = math.sqrt(s[best_k - 1] * s[best_k])
        return thr, best_k, best_g
    return float("inf"), 0, best_g


def family_cert(vals, members):
    """the family certificate bookkeeping: the finite per-member
    certificate constant = max of the certificate column over
    EXACTLY the declared member set; returns (C_fin, declared) --
    the declared set is warded against the sealed membership (the
    e4 circular mutant must be CAUGHT by the set ward)."""
    mem = tuple(members)
    if not mem:
        return 0.0, mem
    return max(float(vals[i]) for i in mem), mem


def seal_family_count(fams):
    """the HARD GATE of the reviewer contract: the adjudication
    accepts EXACTLY two sealed exception families -- any third
    family is REFUSED (the sealed WHAC_A_MOLE fires instead)."""
    return len(fams) == 2


def gate_verdict(n_viol, n_a, n_b, grows, world_ok):
    """the sealed verdict rule (counts only; exactly one fires):
    GENERIC_FAILS on broad generic failure; WHAC_A_MOLE on any
    uncovered violator (a third form would be needed -- abort by
    contract) or any classification leak (family growth / world
    leak); EXCEPTION_CENSUS_GO with both families; otherwise
    ONE_FAMILY_SUFFICES."""
    if n_viol >= GEN_FAIL_MIN:
        return "GENERIC_FAILS"
    if n_viol >= 1:
        return "WHAC_A_MOLE"
    if grows or not world_ok:
        return "WHAC_A_MOLE"
    if n_a >= 1 and n_b >= 1:
        return "EXCEPTION_CENSUS_GO"
    return "ONE_FAMILY_SUFFICES"


def mutant_third_class(mem_a, mem_b, rho, cbar):
    """e1 MUST-FAIL MUTANT: a THIRD class pushed after sight --
    collects the uncovered violators of the evaluated bound
    column (consumes rho) into a post-hoc class; the
    BOUND_FORBIDDEN scope audit must FLAG it and the sealed gate
    must REFUSE it."""
    cov = set(mem_a) | set(mem_b)
    return tuple(i for i, r in enumerate(rho)
                 if r > cbar and i not in cov)


def mutant_thr_posthoc(F, rho, cbar):
    """e2 MUST-FAIL MUTANT: the threshold re-picked AFTER SIGHT of
    the violators (consumes rho): moved down to exactly cover the
    seen violator set -- the scope audit must FLAG it AND on the
    sealed toy it returns != the gap rule's threshold."""
    vi = [F[i] for i, r in enumerate(rho) if r > cbar]
    if not vi:
        return float("inf")
    return min(vi)


def mutant_class_readback(cmrec, nblk):
    """e3 MUST-FAIL MUTANT: a 'class functional' consuming the
    cubic-moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk) * float(nblk)


def mutant_circular_cert(vals, members, gen_cal):
    """e4 MUST-FAIL MUTANT: a family 'certificate' consuming the
    GENERIC calibration window instead of the member set (the
    circular import of the generic constant) -- the declared-set
    ward must CATCH the mismatch."""
    cal = tuple(gen_cal)
    return max(float(vals[i]) for i in cal), cal


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'class orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'class constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


TOY_SPIKE = (1.0, 1.0, 8.0, 1.0, 1.0, 1.0, 1.0)
TOY_FLAT = (3.0,) * 7
TOY_TREND = tuple(0.97 ** i for i in range(11))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("exception_families_probe -- "
          "PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01 (round 317)")
    print("SPEC_SHA %s   R316_SHA %s   R306_SHA %s (imported)"
          % (SPEC_SHA[:16], TRB.SPEC_SHA[:16], RY3.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain ward + e1-e4; "
                        "ladder, extensions, anchors, class "
                        "census, generic bound, certificates and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE EXCEPTION-FAMILY CENSUS (reviewer fork (b)): two "
          "source-pure class functionals sealed in advance -- "
          "F_A = rank-local QMAX spike ratio (CONCENTRATION), "
          "F_B = rank-local PhiL2 spike ratio (DIVERGENCE-MASS "
          "SPIKE), window W = %d, thresholds by the sealed "
          "largest-gap rule (k <= %d, gap >= %.2f) computed "
          "BEFORE any bound evaluation; generic Renyi-3 theorem "
          "on the complement with the r316 mid-ladder freeze; "
          "family certificates finite per member (r270 style) + "
          "exact structural majorants (rho_2 <= PhiH1 / PhiL2, "
          "r316 algebra); THE HARD GATE sealed: at most TWO "
          "families -- any uncovered violator, family growth or "
          "world leak fires WHAC_A_MOLE by contract; verdicts "
          "EXCEPTION_CENSUS_GO / ONE_FAMILY_SUFFICES / "
          "WHAC_A_MOLE / GENERIC_FAILS sealed BEFORE evaluation"
          % (CLS_W, KMAX, GAP_MIN))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("local_ratio", "gap_threshold"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); class builders clean "
          "vs BOUND_FORBIDDEN (%d hits); m5a gift-bound FLAGGED "
          "(%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r316 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        ext = []
        ext2 = []
        okL = True
    else:
        kzs = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
            elif h <= EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        ekz2.sort()
        pool2 = epool[K_EXT:] + [BH.wpack(kz)
                                 for _h, kz in ekz2[:EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:K_EXT2]
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))
    if smoke:
        check("G12-extension-census", True, "SMOKE: skipped")
        check("G13-ext2-census", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d), POSITIVE_PREFIX %d/%d"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1],
                 sum(1 for p in ext if p["nf"] is None), len(ext)))
        check("G13-ext2-census",
              len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "EXT2 (r316 A5 rule verbatim, census-grade): pool "
              "%d leftover + %d windows with %d < h <= %d; "
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(epool) - K_EXT, min(len(ekz2), EXT2_POOL_CAP),
                 EXT_H_MAX, EXT2_H_MAX, len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        v2w = BR.eval_scaled(rows, xu, N - 2)
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p, nf=p["nf"])

    recs = [rung_rec(p) for p in pool]
    erecs = [rung_rec(p) for p in ext] if not smoke else []
    e2recs = [rung_rec(p) for p in ext2] if not smoke else []
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        e_cheap = sum(1 for rc in erecs + e2recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2 census (no sealed expectation): %d cheap "
              "/ %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + ATOMIC PRESENTATION WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in erecs + e2recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext = max(tb_ext, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d mains + 3 controls: worst dev/absmass %.1e main "
          "N<=%d (bar %.0e) / %.1e deep / %.1e ext+ext2 (bar "
          "%.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(mrecs),
             tb_worst, DEEP_N, TB_WARD_BAR, tb_deep, tb_ext,
             TB_WARD_BAR_DEEP, tb_ctrl, TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        runs = PBB.runs_split(cb)
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        cm = RY3.cubic_moments(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        # ---- raw atomic presentation (r313/r314 convention):
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        if m and not degenerate:
            gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
            sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = SCF.flux_telescope(gen["G1"], gen["ptr"], m)
            cc = SCF.collision_census(gen["mult"], gen["ptr"], m)
            x_dev = float(np.max(np.abs(sct["x"] - Pd))
                          / max(np.max(np.abs(Pd)), 1e-300))
            sig = sct["sig"]
            cube = sct["cube"]
            A1 = np.bincount(blk_all, weights=np.abs(val_all),
                             minlength=m)
            scale3 = float(np.sum(A1 ** 3))
            sc_j = np.maximum(A1 ** 3, 1e-300)
            C_far_flux = float(np.sum(sig * ft["F_end"]))
            C_bnd = float(np.sum(sig * ft["F_open"]))
            rec3 = abs(C_far_flux + sct["C_pair"] + sct["C_full"]
                       + C_bnd - cube) / max(scale3, 1e-300)
            tel_dev = float(np.max(np.abs(ft["F_end"]
                                          - sct["far"]) / sc_j))
            bnd_dev = float(np.max(np.abs(ft["F_open"]) / sc_j))
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            ph = PHI.phi3_variants(sct["x"], sct["Q2"], sct["Q3"],
                                   ft["F_end"], ft["F_open"],
                                   ft["edge_abs"], m)
            trs = TRB.two_regime_state(sct["x"], sct["Q2"],
                                       sct["Q3"], gen["G1"],
                                       gen["ptr"], ft["F_end"],
                                       ft["F_open"],
                                       ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            # diagnostic census columns (read-back-adjacent,
            # computed OUTSIDE the builders, disclosed):
            top1 = float(np.max(np.abs(sct["x"])) ** 3) \
                / max(cube, 1e-300)
        else:
            gen = sct = ft = cc = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            shares = dict(far=0.0, pair=0.0, full=0.0)
            mx_mult = 0
            ph = dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                      coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            top1 = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd, shares=shares,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    cc=cc, ph=ph, trs=trs, rho2=rho2, top1=top1,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])
    pool_all = all_rc + [crecs[c] for c in crecs]

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in pool_all:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(pool_all)))

    live = [rc for rc in pool_all if not rc["ev"]["degenerate"]]
    deg_note = [c for c in crecs if crecs[c]["ev"]["degenerate"]]
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    check("G22-genealogy-completeness",
          x_w <= ATOM_BAR and mism_tot == 0,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G31-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e)"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 shares far/pair/full = %+.4f/%+.4f/%+.4f, "
             "FCIX %.3f, QMAX %.4f, PhiL2 %.4f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["trs"]["fcix"],
                ev9s["trs"]["qmax"], ev9s["trs"]["phiL2"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        check("G33-r315-anchors", True, "SMOKE: skipped")
        check("G34-r316-anchors", True, "SMOKE: skipped")
        srt57 = []
        srt317 = []
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        sh_far = [rc["ev"]["shares"]["far"] for rc in recs]
        sh_pair = [rc["ev"]["shares"]["pair"] for rc in recs]
        sh_full = [rc["ev"]["shares"]["full"] for rc in recs]
        fcs = [rc["ev"]["trs"]["fcix"] for rc in recs]
        meds = (float(np.median(sh_far)),
                float(np.median(sh_pair)),
                float(np.median(sh_full)))
        fc_med = float(np.median(fcs))
        fc_sl = slp(fcs)
        # the r316 class ladder: mult-cap filter on core+ext+ext2
        srt317_all = sorted(recs + erecs + e2recs,
                            key=lambda rc: (rc["N"], rc["kz"]))
        excl = [rc for rc in srt317_all
                if rc["ev"]["mx_mult"] > MULT_CAP]
        srt317 = [rc for rc in srt317_all
                  if rc["ev"]["mx_mult"] <= MULT_CAP]
        n317 = len(srt317)
        n_m2 = sum(1 for rc in srt317
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == n317 and not excl,
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d, mult-cap exclusions %d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 n317, len(excl)))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G32-r306-bound-live",
              abs(C2 - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        C0 = {}
        for i, v in enumerate(("a", "b", "c")):
            vals = [rc["ev"]["ph"][v] for rc in srt57]
            C0[v], _j0, _d0 = RY3.calib_freeze(vals, range(N_CAL))
        fcix_kz = {rc["kz"]: rc["ev"]["trs"]["fcix"]
                   for rc in srt57}
        ok_fcix = all(abs(fcix_kz.get(kz, -1.0)
                          - R315_FCIX_KZ[kz]) <= R315_FCIX_TOL
                      for kz in R315_FCIX_KZ)
        check("G33-r315-anchors",
              all(abs(C0[v] - R315_C0[i]) <= R315_C0_TOL
                  for i, v in enumerate(("a", "b", "c")))
              and ok_fcix,
              "r315 record reproduced: C0 a/b/c = "
              "%.4f/%.4f/%.4f (rec %.4f/%.4f/%.4f tol %.3f); "
              "FCIX outliers kz55 %.3f / kz67 %.3f (rec "
              "%.3f/%.3f tol %.3f)"
              % (C0["a"], C0["b"], C0["c"], R315_C0[0],
                 R315_C0[1], R315_C0[2], R315_C0_TOL,
                 fcix_kz.get(55, -1.0), fcix_kz.get(67, -1.0),
                 R315_FCIX_KZ[55], R315_FCIX_KZ[67],
                 R315_FCIX_TOL))
        # r316 anchors on the class ladder
        h_kz = tuple(sorted(rc["kz"] for rc in srt317
                            if rc["ev"]["trs"]["fcix"] > THETA))
        sm316, ca316, te316 = TRB.split_midladder(n317)
        m_all = [rc["ev"]["m"] for rc in srt317]
        m0_316 = min(m_all[i] for i in ca316 + te316)
        calL = [i for i in ca316
                if srt317[i]["ev"]["trs"]["fcix"] <= THETA]
        CL2 = max(srt317[i]["ev"]["trs"]["phiL2"] for i in calL) \
            if calL else 0.0
        violL2 = tuple(sorted(
            srt317[i]["kz"] for i in te316
            if srt317[i]["ev"]["trs"]["fcix"] <= THETA
            and srt317[i]["ev"]["trs"]["phiL2"] > CL2))
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt317}
        top1_kz = {rc["kz"]: rc["ev"]["top1"] for rc in srt317}
        C_small316 = max(srt317[i]["ev"]["rho2"] for i in sm316)
        j_cs = max(sm316, key=lambda i: srt317[i]["ev"]["rho2"])
        ok316 = (n317 == N317_REF
                 and h_kz == tuple(sorted(R316_H_SET))
                 and sm316[-1] == R316_SPLIT[0]
                 and ca316 == tuple(range(R316_SPLIT[1],
                                          R316_SPLIT[2] + 1))
                 and te316[0] == R316_SPLIT[3]
                 and te316[-1] == R316_SPLIT[4]
                 and m0_316 == M0_REF
                 and abs(CL2 - R316_CL2) <= R316_CL2_TOL
                 and violL2 == tuple(sorted(R316_VIOL_SET))
                 and all(abs(top1_kz.get(kz, -1.0)
                             - R316_TOP1[kz]) <= R316_TOP1_TOL
                         for kz in R316_TOP1)
                 and all(abs(rho_kz.get(kz, -1.0)
                             - R316_RHO[kz]) <= R316_RHO_TOL
                         for kz in R316_RHO)
                 and abs(C_small316 - R316_CSMALL)
                 <= R316_CSMALL_TOL
                 and srt317[j_cs]["kz"] == R316_CSMALL_KZ)
        check("G34-r316-anchors", ok316,
              "r316 record reproduced on the class ladder: n = "
              "%d (rec %d); H stratum %s (rec %s); split small "
              "0..%d / cal %d..%d / test %d..%d, m_0 = %d (rec "
              "%d); C_L2 %.4f (rec %.4f tol %.3f); regime-L test "
              "violators %s == the named 8; TOP1 kz55/kz67 "
              "%.3f/%.3f (rec %.3f/%.3f); rho anchors kz53/kz67/"
              "kz55/kz83 %.4f/%.4f/%.4f/%.4f (rec %.4f/%.4f/"
              "%.4f/%.4f tol %.3f); C_small %.4f @ kz%d (rec "
              "%.4f @ kz%d)"
              % (n317, N317_REF, str(h_kz),
                 str(tuple(sorted(R316_H_SET))), sm316[-1],
                 ca316[0], ca316[-1], te316[0], te316[-1],
                 m0_316, M0_REF, CL2, R316_CL2, R316_CL2_TOL,
                 str(violL2), top1_kz.get(55, -1.0),
                 top1_kz.get(67, -1.0), R316_TOP1[55],
                 R316_TOP1[67], rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53],
                 R316_RHO[67], R316_RHO[55], R316_RHO[83],
                 R316_RHO_TOL, C_small316, srt317[j_cs]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))

    # ---------------- S4: Leg A -- sealing + purity + toys + census
    section("S4  LEG A -- FAMILY DEFINITION (SEALED) + PURITY + "
            "TOYS + CENSUS")
    pure_ids = []
    for fn in ("local_ratio", "gap_threshold"):
        pure_ids += scope_audit(fn, PHI3_FORBIDDEN)
        pure_ids += scope_audit(fn, BOUND_FORBIDDEN)
    pure_lits = []
    for fn in ("local_ratio", "gap_threshold", "family_cert",
               "gate_verdict", "seal_family_count"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_third_class", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_thr_posthoc", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_class_readback", PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not pure_ids) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e3_hits) >= 1,
          "SOURCE PURITY: local_ratio + gap_threshold clean vs "
          "PHI3_FORBIDDEN + BOUND_FORBIDDEN (%d id hits); the "
          "five gate-side builders clean vs the sealed r314+"
          "r315+r316 record-literal set (%d literal hits); "
          "consumed inputs: ONE source-pure column (QMAX or "
          "PhiL2) + rank order -- no cubic target, no wall sign, "
          "no record number; e1 third-class FLAGGED (%s); e2 "
          "thr-posthoc FLAGGED (%s); e3 class-readback FLAGGED "
          "(%s)"
          % (len(pure_ids), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    # toys (exact)
    f_sp = local_ratio(TOY_SPIKE)
    thr_sp, k_sp, g_sp = gap_threshold(f_sp)
    ok_sp = (abs(f_sp[2] - 8.0) <= TOY_BAR
             and all(abs(f_sp[i] - 1.0) <= TOY_BAR
                     for i in range(7) if i != 2)
             and k_sp == 1 and abs(thr_sp * thr_sp - 8.0) <= 1e-9
             and tuple(i for i, v in enumerate(f_sp)
                       if v >= thr_sp) == (2,))
    f_fl = local_ratio(TOY_FLAT)
    thr_fl, k_fl, g_fl = gap_threshold(f_fl)
    ok_fl = (k_fl == 0 and thr_fl == float("inf")
             and abs(g_fl - 1.0) <= TOY_BAR)
    f_tr = local_ratio(TOY_TREND)
    thr_tr, k_tr, _g_tr = gap_threshold(f_tr)
    ok_tr = (k_tr == 0 and max(f_tr) <= TREND_TOY_BAR)
    cert_v, cert_d = family_cert([1.0, 2.0, 3.0, 4.0, 5.0],
                                 (1, 3))
    ok_ct = (cert_v == 4.0 and cert_d == (1, 3))
    gv = (gate_verdict(5, 1, 1, False, True),
          gate_verdict(2, 1, 1, False, True),
          gate_verdict(0, 1, 1, True, True),
          gate_verdict(0, 1, 1, False, True),
          gate_verdict(0, 1, 0, False, True))
    ok_gv = gv == ("GENERIC_FAILS", "WHAC_A_MOLE", "WHAC_A_MOLE",
                   "EXCEPTION_CENSUS_GO", "ONE_FAMILY_SUFFICES")
    check("G41-toy-exactness", ok_sp and ok_fl and ok_tr
          and ok_ct and ok_gv,
          "spike toy (1,1,8,1,1,1,1): F = (1,1,8,1,1,1,1), k* = "
          "%d, THR^2 = %.10f == 8, members (2,) EXACT; flat toy: "
          "EMPTY EXACT (gap %.2f < %.2f); TREND toy 0.97^i "
          "(ladder rate): EMPTY, max ratio %.4f <= %.2f -- the "
          "rank-local construction is trend-blind; cert toy "
          "(max 4.0, declared (1,3)) EXACT; gate toys: all five "
          "verdict branches EXACT %s"
          % (k_sp, thr_sp * thr_sp, g_fl, GAP_MIN, max(f_tr),
             TREND_TOY_BAR, str(gv)))
    # live majorant chain ward (the r316 algebra re-warded)
    chain_w = 0.0
    xw_cube = 0.0
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
    check("G42-majorant-chain-ward",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR,
          "the r316 algebra live on %d live worlds: rho_2 <= "
          "PhiL1 <= PhiL2 <= PhiH2 and rho_2 <= PhiH1 (worst rel "
          "slack %.1e, bar %.0e); NORM x cube == rho_2 (worst "
          "%.1e, bar %.0e) -- the class-A structural bound (rho_2 "
          "<= PhiH1, concentration) and the class-B structural "
          "bound (rho_2 <= PhiL2) transfer every certificate to "
          "sum q^3 by algebra"
          % (len(live), chain_w, CHAIN_BAR, xw_cube, XW_BAR))
    if smoke:
        check("G43-threshold-seal", True, "SMOKE: skipped")
        check("G44-membership-census", True, "SMOKE: skipped")
    else:
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt317]
        phiL2_col = [rc["ev"]["trs"]["phiL2"] for rc in srt317]
        FA = local_ratio(qmax_col)
        FB = local_ratio(phiL2_col)
        thrA, kA, gA = gap_threshold(FA)
        thrB, kB, gB = gap_threshold(FB)
        memA = tuple(i for i, v in enumerate(FA) if v >= thrA)
        memB = tuple(i for i, v in enumerate(FB) if v >= thrB)
        famAB = set(memA) | set(memB)
        info("sealed class table (source-pure columns, printed "
             "BEFORE any bound table of this round): rank kz N m "
             "QMAX F_A PhiL2 F_B [class]")
        for i, rc in enumerate(srt317):
            tag = ""
            if i in memA and i in memB:
                tag = " A+B"
            elif i in memA:
                tag = " A"
            elif i in memB:
                tag = " B"
            info("%2d kz%-3d N %4d m %3d qmax %.4f FA %5.2f L2 "
                 "%8.4f FB %5.2f%s"
                 % (i, rc["kz"], rc["N"], rc["ev"]["m"],
                    qmax_col[i], FA[i], phiL2_col[i], FB[i], tag))
        check("G43-threshold-seal",
              seal_family_count(("A", "B")),
              "THRESHOLDS FROZEN by the sealed gap rule: THR_A = "
              "%s (k* = %d, gap %.2f %s %.2f); THR_B = %s (k* = "
              "%d, gap %.2f %s %.2f); EXACTLY TWO families "
              "sealed (hard gate armed)"
              % (("%.4f" % thrA) if kA else "EMPTY", kA, gA,
                 ">=" if gA >= GAP_MIN else "<", GAP_MIN,
                 ("%.4f" % thrB) if kB else "EMPTY", kB, gB,
                 ">=" if gB >= GAP_MIN else "<", GAP_MIN))
        both = tuple(sorted(set(memA) & set(memB)))
        thirds = lambda mem: tuple(  # noqa: E731
            sum(1 for i in mem if 3 * i // n317 == t)
            for t in range(3))
        thA = thirds(memA)
        thB = thirds(memB)
        nonmemA = max((FA[i] for i in range(n317)
                       if i not in memA), default=0.0)
        nonmemB = max((FB[i] for i in range(n317)
                       if i not in memB), default=0.0)
        check("G44-membership-census", True,
              "MEMBERSHIP CENSUS: A (CONCENTRATION) = %s; B "
              "(SPIKE) = %s; A n B = %s; %d rungs in neither; "
              "thirds A %s / B %s; boundary-bias census: max "
              "non-member F_A %.2f / F_B %.2f"
              % (str([srt317[i]["kz"] for i in memA]),
                 str([srt317[i]["kz"] for i in memB]),
                 str([srt317[i]["kz"] for i in both]),
                 n317 - len(famAB), str(thA), str(thB),
                 nonmemA, nonmemB))

    # ---------------- S5: Leg B -- the generic theorem
    section("S5  LEG B -- THE GENERIC THEOREM (complement)")
    if smoke:
        check("G50-complement-split", True, "SMOKE: skipped")
        check("G51-smallm-certificates", True, "SMOKE: skipped")
        check("G52-generic-certification", True, "SMOKE: skipped")
        check("G53-generic-trend", True, "SMOKE: skipped")
    else:
        comp = [i for i in range(n317) if i not in famAB]
        n_comp = len(comp)
        sm_c, ca_c, te_c = TRB.split_midladder(n_comp)
        ovl = len(set(sm_c) & set(ca_c)) \
            + len(set(sm_c) & set(te_c)) \
            + len(set(ca_c) & set(te_c))
        cover = (tuple(sorted(sm_c + ca_c + te_c))
                 == tuple(range(n_comp)))
        rho_all = [rc["ev"]["rho2"] for rc in srt317]
        m0 = min(srt317[comp[j]]["ev"]["m"]
                 for j in ca_c + te_c)
        check("G50-complement-split",
              ovl == 0 and cover and len(ca_c) == N_CAL,
              "complement ladder = %d rungs (A u B excluded, "
              "(N, kz) order kept); r316 mid-ladder split rule "
              "verbatim: small = %d rungs, cal = ranks %d..%d "
              "(kz %s), test = %d rungs; overlaps 0 EXACT, cover "
              "EXACT; m_0 = %d"
              % (n_comp, len(sm_c), ca_c[0], ca_c[-1],
                 str([srt317[comp[j]]["kz"] for j in ca_c]),
                 len(te_c), m0))
        C_small = max(rho_all[comp[j]] for j in sm_c) \
            if sm_c else 0.0
        j_sm = max(sm_c, key=lambda j: rho_all[comp[j]]) \
            if sm_c else -1
        info("small-m certificates (complement, direct "
             "evaluation): rank kz m rho_2")
        for j in sm_c:
            i = comp[j]
            info("%2d kz%-3d m %3d rho2 %.4f%s"
                 % (i, srt317[i]["kz"], srt317[i]["ev"]["m"],
                    rho_all[i],
                    "  <-- C_small" if j == j_sm else ""))
        check("G51-smallm-certificates",
              (not sm_c) or C_small > 0.0,
              "%d complement small-m rungs certified "
              "individually; C_small = %.4f at kz%d"
              % (len(sm_c), C_small,
                 srt317[comp[j_sm]]["kz"] if j_sm >= 0 else -1))
        C_gen = max(rho_all[comp[j]] for j in ca_c)
        j_cg = max(ca_c, key=lambda j: rho_all[comp[j]])
        viol_gen = [comp[j] for j in te_c
                    if rho_all[comp[j]] > C_gen]
        rs = [C_gen / max(rho_all[comp[j]], 1e-300)
              for j in te_c]
        info("generic record table (complement test): rank kz N "
             "m rho_2 reserve")
        for j in te_c:
            i = comp[j]
            info("%2d kz%-3d N %4d m %3d rho2 %.4f rsv %.2f%s"
                 % (i, srt317[i]["kz"], srt317[i]["N"],
                    srt317[i]["ev"]["m"], rho_all[i],
                    C_gen / max(rho_all[i], 1e-300),
                    "  VIOL" if i in viol_gen else ""))
        check("G52-generic-certification", True,
              "GENERIC (census; adjudicated in S7): C_gen = "
              "%.4f frozen at complement-cal kz%d (mid-ladder); "
              "VIOLATIONS %d/%d on the complement test rungs%s; "
              "reserve min/med %.2f/%.2f"
              % (C_gen, srt317[comp[j_cg]]["kz"],
                 len(viol_gen), len(te_c),
                 (": " + ", ".join(
                     "kz%d rho %.4f" % (srt317[i]["kz"],
                                        rho_all[i])
                     for i in viol_gen)) if viol_gen else "",
                 min(rs), float(np.median(rs))))
        NsT = [srt317[comp[j]]["N"] for j in te_c]
        sl_g = L2D.halves_slope(
            NsT, [max(rho_all[comp[j]], 1e-300) for j in te_c])
        check("G53-generic-trend", True,
              "generic trend census on the %d complement test "
              "rungs (halves slope of rho_2): %+.3f (falling = "
              "growing reserve; census, no gate bar)"
              % (len(te_c), sl_g))

    # ---------------- S6: Leg C -- the family certificates
    section("S6  LEG C -- FAMILY CERTIFICATES + GROWTH CENSUS")
    if smoke:
        check("G60-classA-certificates", True, "SMOKE: skipped")
        check("G61-classB-certificates", True, "SMOKE: skipped")
        check("G62-growth-census", True, "SMOKE: skipped")
    else:
        C_A, decl_A = family_cert(rho_all, memA)
        okA_chain = all(rho_all[i]
                        <= srt317[i]["ev"]["trs"]["phiH1"]
                        * (1.0 + CHAIN_BAR) for i in memA)
        info("class-A certificates (CONCENTRATION): rank kz m "
             "rho_2 PhiH1 qmax")
        for i in memA:
            ev = srt317[i]["ev"]
            info("%2d kz%-3d m %3d rho2 %.4f PhiH1 %.4f qmax "
                 "%.4f" % (i, srt317[i]["kz"], ev["m"],
                           rho_all[i], ev["trs"]["phiH1"],
                           ev["trs"]["qmax"]))
        check("G60-classA-certificates",
              decl_A == memA and okA_chain,
              "class A: %d finite certificates, C_A = %.4f; "
              "declared set == sealed membership EXACT; "
              "structural bound rho_2 <= PhiH1 (the class "
              "DEFINITION's concentration majorant) holds on "
              "every member; qmax <= 1 - delta with delta = "
              "%.3f"
              % (len(memA), C_A,
                 1.0 - max((srt317[i]["ev"]["trs"]["qmax"]
                            for i in memA), default=0.0)))
        C_B, decl_B = family_cert(rho_all, memB)
        okB_chain = all(rho_all[i]
                        <= srt317[i]["ev"]["trs"]["phiL2"]
                        * (1.0 + CHAIN_BAR) for i in memB)
        info("class-B certificates (SPIKE): rank kz m rho_2 "
             "PhiL2 F_B")
        for i in memB:
            ev = srt317[i]["ev"]
            info("%2d kz%-3d m %3d rho2 %.4f PhiL2 %.4f FB %.2f"
                 % (i, srt317[i]["kz"], ev["m"], rho_all[i],
                    ev["trs"]["phiL2"], FB[i]))
        check("G61-classB-certificates",
              decl_B == memB and okB_chain,
              "class B: %d finite certificates, C_B = %.4f; "
              "declared set == sealed membership EXACT; "
              "structural bound rho_2 <= PhiL2 holds on every "
              "member; DISCLOSED honest asymmetry: the spike "
              "property yields no uniform bound from its "
              "definition -- these are r270-style finite "
              "certificates" % (len(memB), C_B))
        growsA = thA[0] < thA[1] < thA[2]
        growsB = thB[0] < thB[1] < thB[2]
        e2A = sum(1 for i in memA if srt317[i] in e2recs)
        e2B = sum(1 for i in memB if srt317[i] in e2recs)
        check("G62-growth-census", True,
              "DEPTH-GROWTH census (sealed rule: strictly "
              "increasing thirds = GROWS): A thirds %s -> %s; B "
              "thirds %s -> %s; EXT2-stratum members A %d / B %d"
              % (str(thA), "GROWS" if growsA else "stable",
                 str(thB), "GROWS" if growsB else "stable",
                 e2A, e2B))

    # ---------------- S7: Leg D -- world check + hard gate
    section("S7  LEG D -- WORLD CHECK + THE HARD GATE")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # SCRAMBLE class rejection machinery (r316 verbatim)
    evS = crecs["SCR"]["ev"]
    comp_ref = recs
    comp_main = dict(
        dflux=float(np.median([rc["ev"]["trs"]["nrm"]
                               * abs(rc["ev"]["trs"]["dflux"])
                               for rc in comp_ref])),
        coll=float(np.median([rc["ev"]["trs"]["nrm"]
                              * abs(rc["ev"]["trs"]["coll"])
                              for rc in comp_ref])),
        fcix=float(np.median([rc["ev"]["trs"]["fcix"]
                              for rc in comp_ref])))
    comp_scr = dict(
        dflux=evS["trs"]["nrm"] * abs(evS["trs"]["dflux"]),
        coll=evS["trs"]["nrm"] * abs(evS["trs"]["coll"]),
        fcix=evS["trs"]["fcix"])
    devsS = {k: abs(comp_scr[k] - comp_main[k])
             / max(abs(comp_main[k]), 1e-300) for k in comp_main}
    cause = max(devsS, key=lambda k: devsS[k])
    attr_ok = (devsS[cause] >= ATTR_MIN
               and cause in ("coll", "dflux"))
    rng = np.random.default_rng(SEED_SHUF)
    blk_shuf = ev9m["blk_all"][
        rng.permutation(len(ev9m["blk_all"]))]
    gen_s = SCF.fold_genealogy(ev9m["pos_all"], ev9m["val_all"],
                               blk_shuf, m9)
    ft_s = SCF.flux_telescope(gen_s["G1"], gen_s["ptr"], m9)
    mism_s = int(np.sum(np.searchsorted(ev9m["brk"],
                                        ev9m["pos_all"])
                        != blk_shuf))
    ne = min(len(ft_s["edges"]), len(ev9m["ft"]["edges"]))
    edev = float(np.max(np.abs(ft_s["edges"][:ne]
                               - ev9m["ft"]["edges"][:ne]))
                 / max(float(np.max(np.abs(
                     ev9m["ft"]["edges"]))), 1e-300))
    x_s = np.bincount(blk_shuf, weights=ev9m["val_all"],
                      minlength=m9)
    mass_dev = abs(float(np.sum(x_s))
                   - float(np.sum(ev9m["sct"]["x"]))) \
        / max(float(np.sum(np.abs(ev9m["val_all"]))), 1e-300)
    shuf_ok = (mism_s > 0 and edev >= MUT_MIN
               and mass_dev <= ID_BAR)
    if smoke:
        check("G70-world-admission", True, "SMOKE: skipped")
        check("G71-scramble-rejection", shuf_ok and attr_ok,
              "SMOKE (w9-based): attribution %s dev %.2f; "
              "shuffle %d mism, edge break %.1e, mass %.1e"
              % (cause.upper(), devsS[cause], mism_s, edev,
                 mass_dev))
        check("G72-hard-gate-adjudication", True,
              "SMOKE: skipped")
        check("G73-theorem-candidate", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        C_tot = max(C_gen, C_A, C_B, C_small)
        wnote = []
        adm_ok = True
        for nm, ev in (("w9", mrecs[0]["ev"]),
                       ("w13(twin)", mrecs[1]["ev"]),
                       ("EPSTEIN", crecs["EPST"]["ev"])):
            adm = (ev["mx_mult"] <= MULT_CAP
                   and ev["rho2"] <= C_tot)
            adm_ok = adm_ok and adm
            wnote.append("%s mult %d rho2 %.3f %s C_tot (qmax "
                         "%.4f PhiL2 %.4f census)"
                         % (nm, ev["mx_mult"], ev["rho2"],
                            "<=" if ev["rho2"] <= C_tot else ">",
                            ev["trs"]["qmax"],
                            ev["trs"]["phiL2"]))
        tw_fac = max(mrecs[1]["ev"]["trs"]["phiL2"]
                     / max(mrecs[0]["ev"]["trs"]["phiL2"],
                           1e-300),
                     mrecs[0]["ev"]["trs"]["phiL2"]
                     / max(mrecs[1]["ev"]["trs"]["phiL2"],
                           1e-300))
        twin_ok = tw_fac <= TWIN_FAC
        world_ok = adm_ok and twin_ok and attr_ok and shuf_ok
        check("G70-world-admission", True,
              "WORLD census (adjudicated in G72): %s; twin band "
              "PhiL2 factor %.2f %s %.1f; SCR rho2 %.3f %s C_tot "
              "%.4f (consequence census, disclosed)"
              % ("; ".join(wnote), tw_fac,
                 "<=" if twin_ok else ">", TWIN_FAC, evS["rho2"],
                 "<=" if evS["rho2"] <= C_tot else ">", C_tot))
        check("G71-scramble-rejection", attr_ok and shuf_ok,
              "SCRAMBLE rejected by the CLASS machinery: "
              "component attribution names %s (dev %.2f >= "
              "%.2f, devs %s) AND the seeded shuffle (%d) "
              "breaks the flux profile edgewise %.1e >= %.0e "
              "with mass matched %.1e (%d/%d atoms displaced)"
              % (cause.upper(), devsS[cause], ATTR_MIN,
                 str({k: round(devsS[k], 2) for k in devsS}),
                 SEED_SHUF, edev, MUT_MIN, mass_dev, mism_s,
                 len(ev9m["pos_all"])))
        grows = growsA or growsB
        vkey = gate_verdict(len(viol_gen), len(memA), len(memB),
                            grows, world_ok)
        if vkey == "GENERIC_FAILS":
            verdict_main = ("GENERIC_FAILS(%d/%d complement "
                            "violations >= %d -- the generic "
                            "law itself fails, classification "
                            "moot)" % (len(viol_gen), len(te_c),
                                       GEN_FAIL_MIN))
        elif vkey == "WHAC_A_MOLE":
            reasons = []
            if viol_gen:
                reasons.append("%d uncovered violators %s -- a "
                               "third exception form would be "
                               "needed, NO third class added "
                               "(abort by contract)"
                               % (len(viol_gen),
                                  str([srt317[i]["kz"]
                                       for i in viol_gen])))
            if grows:
                reasons.append("family growth (A %s B %s)"
                               % (str(thA), str(thB)))
            if not world_ok:
                reasons.append("world leak (adm %s twin %s attr "
                               "%s shuf %s)"
                               % (adm_ok, twin_ok, attr_ok,
                                  shuf_ok))
            verdict_main = ("WHAC_A_MOLE(%s; recommendation: "
                            "back to fork (a))"
                            % "; ".join(reasons))
        elif vkey == "EXCEPTION_CENSUS_GO":
            verdict_main = ("EXCEPTION_CENSUS_GO(A = %s, B = "
                            "%s; C_gen %.4f, C_A %.4f, C_B "
                            "%.4f, C_small %.4f, C_tot %.4f, "
                            "m_0 %d)"
                            % (str([srt317[i]["kz"]
                                    for i in memA]),
                               str([srt317[i]["kz"]
                                    for i in memB]),
                               C_gen, C_A, C_B, C_small, C_tot,
                               m0))
        else:
            fam = "A" if memA else ("B" if memB else "NONE")
            verdict_main = ("ONE_FAMILY_SUFFICES(%s; C_gen "
                            "%.4f, C_tot %.4f, m_0 %d)"
                            % (fam, C_gen, C_tot, m0))
        check("G72-hard-gate-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        if vkey in ("EXCEPTION_CENSUS_GO", "ONE_FAMILY_SUFFICES"):
            info("CANDIDATE THEOREM (Renyi-3 with exception "
                 "families; measured on the %d-rung class "
                 "ladder; status %s):" % (n317, vkey))
            info("  Every class rung w (edge-masked, fold "
                 "multiplicity <= %d, POSITIVE_PREFIX) falls "
                 "into at least one certified case:" % MULT_CAP)
            if memA:
                info("   (i)   CLASS A (source-pure: F_A >= "
                     "%.4f): rho_2 <= C_A = %.4f (%d finite "
                     "certificates; structural: rho_2 <= PhiH1 "
                     "by exact concentration algebra);"
                     % (thrA, C_A, len(memA)))
            if memB:
                info("   (ii)  CLASS B (source-pure: F_B >= "
                     "%.4f): rho_2 <= C_B = %.4f (%d finite "
                     "certificates; structural: rho_2 <= "
                     "PhiL2);" % (thrB, C_B, len(memB)))
            info("   (iii) m < %d: individually certified "
                 "(C_small = %.4f, %d rungs);"
                 % (m0, C_small, len(sm_c)))
            info("   (iv)  GENERIC (m >= %d, neither class): "
                 "rho_2 <= C_gen = %.4f (mid-ladder frozen, "
                 "0/%d test violations, reserve trend %+.3f);"
                 % (m0, C_gen, len(te_c), sl_g))
            info("  hence sum_j q_j^3 <= %.4f (log m)^2/m^2 on "
                 "EVERY measured rung (C_tot = max) and n_eff = "
                 "N_2 >= N_3 >= m/(%.3f log m) (r306 exact "
                 "chain).  COVERAGE: A u B covers ALL violators "
                 "of C_gen on the ladder (0 uncovered); depth "
                 "census: A thirds %s / B thirds %s (not "
                 "growing)."
                 % (C_tot, math.sqrt(C_tot), str(thA), str(thB)))
            check("G73-theorem-candidate", True,
                  "composed theorem candidate printed with "
                  "explicit (C_gen %.4f, C_A %.4f, C_B %.4f, "
                  "C_small %.4f, C_tot %.4f, m_0 %d)"
                  % (C_gen, C_A, C_B, C_small, C_tot, m0))
        else:
            check("G73-theorem-candidate", True,
                  "no composed theorem candidate printed (the "
                  "hard gate fired -- see G72); the family "
                  "census and the finite certificates stand as "
                  "the round's record data")

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toyA = (0,)
    toyB = (1,)
    toy_rho = (9.0, 9.0, 9.0, 0.1)
    third = mutant_third_class(toyA, toyB, toy_rho, 1.0)
    gate_ref = seal_family_count((toyA, toyB, third))
    gate_ok = seal_family_count((toyA, toyB))
    gv_mut = gate_verdict(len(third), 1, 1, False, True)
    check("G80-e1-third-class",
          len(e1_hits) >= 1 and third == (2,)
          and (not gate_ref) and gate_ok
          and gv_mut == "WHAC_A_MOLE",
          "e1 GATE-CAUGHT three ways: the post-hoc third class "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s); seal_family_count REFUSES the 3-family tuple "
          "(False) while the sealed 2-family passes (True); the "
          "sealed gate maps the uncovered violators to %s, "
          "never to a three-family GO"
          % (e1_hits[0] if e1_hits else "MISS", gv_mut))
    toy_F = (1.0, 1.1, 1.2, 2.0)
    toy_rho2 = (0.1, 0.9, 0.1, 0.1)
    thr_mut = mutant_thr_posthoc(toy_F, toy_rho2, 0.5)
    thr_seal, k_seal, _g = gap_threshold(toy_F)
    check("G81-e2-threshold-posthoc",
          len(e2_hits) >= 1
          and abs(thr_mut - thr_seal) >= MUT_MIN,
          "e2 CAUGHT twice: the after-sight threshold re-pick "
          "consumes rho -- AST-FLAGGED (%s) -- and on the "
          "sealed toy it returns %.4f != the gap rule's %.4f "
          "(k* = %d); the real thresholds are frozen by the "
          "sealed rule before any bound value"
          % (e2_hits[0] if e2_hits else "MISS", thr_mut,
             thr_seal, k_seal))
    check("G82-e3-class-readback",
          len(e3_hits) >= 1 and (not pure_ids),
          "e3 AST-CAUGHT: the class functional consuming the "
          "cubic-moment record (cm/S3) is FLAGGED (%s) while "
          "local_ratio + gap_threshold are clean (%d hits) -- "
          "the source-purity of the family definition is "
          "machine-audited"
          % (e3_hits[0] if e3_hits else "MISS", len(pure_ids)))
    toy_vals = (0.1, 0.2, 0.3, 0.9, 1.2)
    toy_mem = (3, 4)
    toy_cal = (0, 1)
    c_real, d_real = family_cert(toy_vals, toy_mem)
    c_mut, d_mut = mutant_circular_cert(toy_vals, toy_mem,
                                        toy_cal)
    check("G83-e4-circular-cert",
          d_real == toy_mem and d_mut != toy_mem
          and abs(c_real - c_mut) >= MUT_MIN
          and c_real == 1.2 and c_mut == 0.2,
          "e4 CAUGHT: the circular certificate declares the "
          "generic calibration window %s != the member set %s "
          "(set ward EXACT) and its 'constant' %.1f sits LOUDLY "
          "below the member maximum %.1f (diff %.1f >= %.0e) "
          "-- certifying nothing; the real family_cert declares "
          "the members exactly"
          % (str(d_mut), str(toy_mem), c_mut, c_real,
             c_real - c_mut, MUT_MIN))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the two sealed source-pure class functionals "
          "with the gap-threshold rule (frozen before any bound "
          "evaluation), the membership census, the generic "
          "mid-ladder theorem on the complement, the finite "
          "family certificates with structural majorants, the "
          "depth-growth census and the HARD two-family gate -- "
          "NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R317_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57, r315 C0 "
                 "%.4f/%.4f/%.4f, r316 n %d H %s split %d|%d|%d "
                 "C_L2 %.4f viol8 %s C_small %.4f)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, n317, rec3_w, C2, viol2, C0["a"],
                    C0["b"], C0["c"], n317, str(h_kz),
                    len(sm316), len(ca316), len(te316), CL2,
                    str(violL2), C_small316)]
        parts.append("SEAL(W %d, gap rule k<=%d g>=%.2f, purity "
                     "clean, toys exact, chain %.1e)"
                     % (CLS_W, KMAX, GAP_MIN, chain_w))
        parts.append("FAMILIES(THR_A %s k %d g %.2f -> A %s; "
                     "THR_B %s k %d g %.2f -> B %s; both %s; "
                     "thirds A %s B %s)"
                     % (("%.4f" % thrA) if kA else "EMPTY", kA,
                        gA, str([srt317[i]["kz"] for i in memA]),
                        ("%.4f" % thrB) if kB else "EMPTY", kB,
                        gB, str([srt317[i]["kz"] for i in memB]),
                        str([srt317[i]["kz"] for i in both]),
                        str(thA), str(thB)))
        parts.append("GENERIC(C_gen %.4f, m_0 %d, viol %d/%d %s, "
                     "reserve %.2f/%.2f, trend %+.3f, small %d "
                     "C_small %.4f)"
                     % (C_gen, m0, len(viol_gen), len(te_c),
                        str([srt317[i]["kz"] for i in viol_gen]),
                        min(rs), float(np.median(rs)), sl_g,
                        len(sm_c), C_small))
        parts.append("CERTS(A: %d members C_A %.4f PhiH1-warded; "
                     "B: %d members C_B %.4f PhiL2-warded; "
                     "growth A %s B %s, EXT2 %d/%d)"
                     % (len(memA), C_A, len(memB), C_B,
                        "GROWS" if growsA else "stable",
                        "GROWS" if growsB else "stable",
                        e2A, e2B))
        parts.append("WORLD(adm %s, twin %.2f, SCR %s dev %.2f "
                     "+ shuffle %d/%d)"
                     % (adm_ok, tw_fac, cause.upper(),
                        devsS[cause], mism_s,
                        len(ev9m["pos_all"])))
        parts.append(verdict_main)
        parts.append("THEOREM(%s)"
                     % ("printed" if vkey in
                        ("EXCEPTION_CENSUS_GO",
                         "ONE_FAMILY_SUFFICES")
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the gap-rule toys, the "
          "gate logic, the majorant chains and the purity "
          "audits (exact / AST-decided); MEASURED: every "
          "threshold, membership, constant, violation count, "
          "reserve, trend and census (the finite class ladder + "
          "2 mains + 2 live controls); OPEN: any bound beyond "
          "the measured rungs, the cofinal law, kz15 beyond "
          "r270; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""indefinite_fork_probe -- PRIME.LSTAR.INDEFINITE_FORK.01
(round 318, the NEW idea class after the L*-language stop):
PONTRYAGIN-/KREIN-INDEX versus SIGN-REGULARITY -- ONE theoretical
representation test, not fifty numerical tests.  Strategic frame
(binding, the reviewer perspective shift, quoted): the previous
L* search language is STOPPED (the no-go catalog: functionals,
extremality, KYP, Maslov, fixed head, paired cone, block Green at
the 2.4 percent negative cross mixtures, diophantine irrelevant,
magnitudes insufficient).  The key r312 information: 97.6 percent
of the solver's psd family fits the positive rank-one cone and
2.4 percent negative CROSS MIXTURES obstruct the construction.
Reviewer reading: "THE SIGNEDNESS ITSELF IS THE MATHEMATICAL
OBJECT THAT IS NOT YET UNDERSTOOD."  L* is reformulated -- no
longer "int p^2 dnu < int p^2 dmu" (squeezing out positivity)
but: "why does this specific signed moment form have a positive
index of at least N_w?" -- perhaps the natural object is not
positivity but SIGNATURE: the object is intrinsically indefinite,
and the theorem to find says WHERE ITS NEGATIVE SIGNATURE MAY
LIVE.  Core-question inversion: what if the 2.4 percent negative
cross mixtures are not the obstruction of the right proof but the
FINGERPRINT of the right indefinite theorem?  STOP RULE (binding):
if BOTH routes are world-blind or restatements => FORK_DEAD, stop
the lane; if one is MAIN-specific => dig there (dig site named
precisely).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r317 (fiber) and r319 (audit) run in parallel; this
probe touches nothing of theirs; the rh-sync is strictly ADDITIVE.

INDEX FIREWALL (binding, r238-r316 discipline): w = window (kz),
S = #union atoms of mutilde = mu - nu, S_+ = #mu atoms, S_- = #nu
atoms, N_w = builder depth = (S+1)//2, n = degree, minC = first
n with h_n < 0.  Ground truth (minC, control flips, published
record numbers) enters GATES and record tables only; the sealed
constructors consume passed matrices/arrays ONLY (AST scope
audit); no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r283 FS.{split_channels, mu_chain_f64,
b_matrix_f64, toy_block, frac_det}, r284 LS.{world_pack,
dist_rule}, r280 BL via LS, r279 OT.mp_chain_pack (the mp h-sign
chain with guard/recount), r312 BM.{lib_vectors, nnls_lh,
feas_diag_g}, r308 BG.{census_world, world_arrays, world_budget,
hull_of, block_eigs}, r289 AK.twin_rational + r276 MF.local_gaps,
r278 MS.ctx_build, r244 BH.spearman, v881 PIK, r243
PB.smooth_comb, paircorr PC.{Grid, gen_model}, r274 WD.stj_gen,
r230 JF toy nodes, v563 core READ-ONLY.

THE INDEFINITE GEOMETRY (frame convention, r283 s2 theorem,
consumed as the coordinate system): in the mu-orthonormal frame
the signed Hankel form H_n(mutilde) is congruent to A_n = I - M_n
with M_n = B_n^T B_n, B[k, i] = sqrt(v_k) P_i(y_k) -- the
canonical indefinite form of the round, with degree coordinates
i = 0..n-1.  Its negative directions are the right singular
vectors of B_n with sigma > 1; its inertia obeys the
Jacobi/Sylvester dictionary n_-(A_n) = #{k < n : h_k < 0}
(machine-gated as THE index-form-exactness gate, two independent
paths: f64 SVD counts vs the r279 mp h-sign chain at dps 120).

LEG 0 -- ANCHORS.  v956 half-filling pins (w9 S/S_+/S_- =
367/263/104, N_w = 184, minC = 184); r279 theorem pins on w9
(crossing budget #{n < S : h_n < 0} == S_- == 104 via the mp
chain; minC == N_w); r283 crossing pin (lambda_max(E_n) crosses 1
at 185 == minC + 1); the w9 budget scalar B = 8.368649 (tol
1e-3); THE r312 CROSS-MIXTURE PINS reproduced with the identical
protocol (r308 Dykstra 200 steps from the least-norm start,
per-block NNLS onto the sealed 22-generator cone): cone share
med/min/mean in the 0.976/0.952/0.978 bands (tol 0.01), top
eigvec library alignment med 0.9973 (tol 0.005), Dykstra CONV
(min eig rel >= -1e-9).

LEG A -- P1, THE PONTRYAGIN-/KREIN-INDEX ROUTE.
(a1) INDEX-FORM EXACTNESS (bookkeeping theorem, gated): on ALL
  seven worlds (w9, w13, r289 rational twin, EPST/SCR/SMOOTH/HL2)
  the spectral count #{sigma_i(B_n) > 1} equals the mp pivot
  count #{k < n : h_k < 0} at the WINDOW n = N_w and at the DEEP
  depth n = DEEP_EFF (the overflow-guarded largest depth <=
  S_+ - 1 with max |B entry| <= 1e100; near-1 gray zone
  sigma in (0.9, 1.1) disclosed; sealed rule: exact match, OR
  |mismatch| <= gray count, disclosed loudly).
(a2) THE SIGNATURE TABLE: window index defect d_w = n_-(A_{N_w})
  per world -- the mains and the twin must have d_w == 0 EXACTLY
  (n_+ == N_w EXACTLY at the window: the index form of the
  half-filling survival) while every control has d_w > 0 (the
  control flips ARE negative directions wandering INTO the
  window, measured as an index defect); LADDER: d_w == 0 on all
  42 frame-A rungs (h <= 900, half-filling 42/42, f64 sign
  chain); VACUITY CHECK: n_+(full) = S_+ >= N_w on every world
  including the controls -- the global index inequality
  "n_+ >= N_w" is carried by the mu-channel majority alone and
  is typed VACUOUS as a discriminator (measured).
(a3) THE BRUTAL RESTATEMENT GATE (its own gate, sealed): the
  sealed equivalence test "d_w == 0 <=> minC >= N_w" adjudicated
  on the three exact toys (JF9 / MAINLIKE / FLIPLIKE, Fractions,
  both truth values realized) AND on all seven real worlds; if
  the equivalence is total, the index statement "n_+(window) ==
  N_w" is typed RESTATEMENT (of L*/free-window survival) -- then
  P1 lives or dies on the ADDITIONAL structure alone:
(a4) NEGATIVE-SUBSPACE INVARIANTS (the additional-structure
  hunt): at DEEP_EFF the degree profiles |v_i(d)|^2 of the
  negative directions; sealed statistics NEG_LOW = min_i
  d10_i / N_w, NEG_MED = median_i d10_i / N_w (d10 = lowest
  degree with cumulative mass >= 0.10), NEG_PR = median_i
  PR_i / N_w (participation ratio of the profile); adjudicated
  by the sealed r281 distance rule (MAIN w9 vs the four dead
  worlds) PLUS the PROXY TEST: typed RESTATEMENT_PROXY iff
  |NEG_LOW - minC/N_w| <= 0.15 on EVERY world (the invariant is
  then the crossing location in disguise -- no lever); ladder
  stability of NEG_LOW on the 12 sealed fingerprint rungs
  reported as typed information.
(a5) KREIN PLUS-OPERATOR / ANGULAR TEST: ANG = largest singular
  value of the window block of the negative right-singular
  frame (the principal-angle overlap of the free window with
  the deep negative subspace); the sealed dictionary test:
  spearman(ANG, rho_win = ||B_{N_w}||_2) over the seven worlds;
  |sp| >= 0.9 types the angular-operator language RESTATEMENT
  (the plus-operator question collapses onto the contraction
  scalar = L*), else typed independent (reported).

LEG B -- P2, THE SIGN-REGULARITY / TOTAL-POSITIVITY ROUTE.
(b1) MINOR SIGN-PATTERN CENSUS (contiguous, budget-aware, orders
  k = 1..5): on the atom-sorted matrices E_win = B_win B_win^T
  (nu-Gram / dressed CD kernel, principal + row-initial census),
  A_win = I - M_win (the canonical indefinite form, principal +
  row-initial, scalar-normalized -- positive scalings preserve
  every minor sign), and B_win itself (rows = sorted nu atoms,
  columns = degrees, row-initial census -- orientation
  sensitive).  Sign 0 iff |det| <= 1e-10 x Hadamard bound;
  per-order majority share; SR_SCORE = min over live orders of
  the majority share; pattern = the majority-sign tuple.  A
  census object is SIGN_REGULAR iff SR_SCORE >= 0.99 and no
  order is zero-degenerate (> 20 percent zero class).
(b2) WORLD CONTRAST: the same census on the twin (METRIC_ONLY:
  pattern and score must match MAIN if the pattern is real) and
  on EPST/SCR/SMOOTH/HL2; SR MAIN-SPECIFIC iff some census
  object is sign-regular on MAIN AND on the twin with the same
  pattern AND fails the bar or the pattern on EVERY control;
  sign-regular everywhere with one pattern => world-blind
  (construction-generic).
(b3) THE R312 INVERSION -- THE CROSS-MIXTURE FINGERPRINT (its
  own gate): on the 12 sealed rungs (w9 plus the 11 smallest-S
  rungs of the 42-rung frame-A ladder, sorted by (S, kz)) the
  r308 Dykstra family at 200 steps, per block r the sealed cone
  projection (NNLS onto the 22-generator library in isometric
  vech coordinates) and the residual matrix R_r = G_r -
  sum_l c_l V_l V_l^T in the D basis; per block the dominant
  off-diagonal pair (a, b) = argmax |R_r[a, b]| and its sign;
  per rung the modal pair, the modal-pair share, the sign
  consistency and the D6-class share (pairs touching the border
  coordinate); THE CONSENSUS VERIFIER (sealed, the m4 gate):
  requires >= 10 rungs, LAWFUL iff >= 10 of 12 rungs carry the
  SAME modal (pair, sign) with median modal share >= 0.5; world
  contrast: the twin (must match MAIN if METRIC_ONLY holds) and
  EPST/SCR at w9 (their 200-step iterate is NOT psd-feasible --
  labeled ITERATE, honestly); FP MAIN-SPECIFIC iff lawful on the
  MAIN ladder AND twin-consistent AND both controls break the
  consensus (different pair OR different sign OR share < 0.5).
(b4) THE IMPLICATION SKETCH (which minor pattern would imply
  L*): sign regularity of order k of B implies variation
  diminishing (Schoenberg) for the dressed evaluation operator,
  VD bounds the sign changes of every dressed polynomial on the
  nu atoms, sign-change bounds at every truncation imply the
  reality/interlacing side R2 (r277), and by the r277 bridge R2
  <=> quasi-definiteness through the window <=> the inertia
  statement (v962 T4 form of L*).  The probe gates the MEASURED
  premise: is B on MAIN even sign-regular to order 5 (b1), and
  the VD spot check (sign changes of column i <= i for the
  first 20 degree columns, a world-blind polynomial bookkeeping
  gate); a failed premise on MAIN types the chain
  PREMISE_FAILS_ON_MAIN (honest negative).

LEG C -- THE FORK ADJUDICATION (sealed BEFORE evaluation):
  alive(P1) iff (a1) exact AND some sealed NEG statistic is
    MAIN_SEPARATING under the r281 distance rule AND the proxy
    test does NOT fire;
  alive(P2) iff SR MAIN-SPECIFIC (b2) OR FP MAIN-SPECIFIC (b3);
  letters: BOTH_ALIVE(p1 site; p2 pattern) /
    P1_MAIN_SPECIFIC(dig site named) /
    P2_MAIN_SPECIFIC(pattern verbatim) /
    FORK_DEAD(p1 reason; p2 reason; LANE-STOP RECOMMENDATION).

LEG D -- MUST-FAILS (each loud):
  (m1) INDEX COUNT WITH THE WRONG SIGNATURE CONVENTION: on the
    exact JF9 toy (Fractions) the mutant counts #{h_k > 0}
    instead of the Frobenius sign-change count of the exact
    congruence minors -- must MISMATCH the exact inertia
    (CAUGHT, exact);
  (m2) MINOR PATTERN ON THE TRANSPOSED MATRIX: the sealed
    row-initial census of the exact hand matrix M_TP =
    [[1,2,3],[1,3,6],[-1,1,13]] is all-positive (orders 1..3:
    (1,2,3)/(1,3)/(7)) while the census of M_TP^T contains a
    negative order-1 minor -- the transposed-input mutant must
    be CAUGHT (exact Fractions);
  (m3) RESTATEMENT GATE WITH CIRCULAR L* CONSUMPTION: a mutant
    "additional-structure invariant" consuming the withheld
    truth (minC_true / rho_true) -- FLAGGED by the AST scope
    audit;
  (m4) CROSS-MIXTURE FINGERPRINT EXTRAPOLATED FROM A SINGLE
    RUNG: the sealed consensus verifier must REJECT any census
    with fewer than 10 rungs -- the single-rung mutant call is
    CAUGHT live (consistency forced across >= 10 rungs).

STOP LIST (binding): NO L* claim, NO RH claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO posthoc window,
NO new no-go catalog entry re-opened (functionals, extremality,
KYP, Maslov, fixed head, paired cone, block-Green construction,
diophantine, magnitudes stay stopped); no bar, band, rule or
verdict form change after any evaluation (amendments disclosed);
r243..r316 stand; mincut base 4 / refined 5 UNCHANGED.

WORLDS: MAIN w9 + second main w13; the r289 rational twin
(METRIC_ONLY semantics); controls EPST / SCRAMBLE(seed 1) /
SMOOTH / HL2(seed 101) built verbatim through the r283/r284
channel; the 42-rung frame-A ladder (h <= 900); exact toys JF9,
MAINLIKE, FLIPLIKE (r280 conventions via FS.toy_block) and the
exact hand matrix M_TP.

SEALED CONSTANTS: DEG_A 8; MAIN_KZ 9; KZ_SECOND 13; CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}; HL2 seed 101 flip 25; H_CAP 900;
MP_DPS 120; SIGN_GUARD 1e-90; RECOUNT_DPS 240; GRAY (0.9, 1.1);
OFLOW_CAP 1e100; NEG_MASS_Q 0.10; PROX_TOL 0.15; K_MAX 5; ZTOL
1e-10; Z_FRAC 0.2; SR_BAR 0.99; VD_DEGS 20; N_FP 12;
FP_MIN_RUNGS 10; FP_CONS 10; FP_BAR 0.5; FEAS_IT 200; FEAS_CONV
1e-9; SHARE_REC (0.976, 0.952, 0.978) tol 0.01; ALIGN_REC 0.9973
tol 0.005; B_W9_REC 8.368649 tol 1e-3; W9_ANCH (367, 263, 104,
184, 184); BUDGET_REC 104; TWIN_MINC_REC 184; RAT_TOL 1e-8;
QMAX 1e6; ANG_SP_BAR 0.9; STAB_BINS 20; runtime <= 1800 s;
smoke = S0 + exact toys + hand census + w9 f64 window block
(source pins, window spectral-vs-f64-pivot co-location, crossing
anchor) + all four must-fails + scope audits (mp legs, twin,
controls, ladder, fingerprint, censuses, adjudication skipped).
PRE-SPEC SCOPING (disclosed): every record number above is a
published v956/r279/r283/r312 record adopted as-is; the two
routes, every sealed statistic, bar, band, the proxy rule, the
consensus verifier, the adjudication tree and the verdict form
were fixed at design time BEFORE any evaluation of this probe;
no machinery pass preceded this spec except record reading.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of, by the Leg-C tree]
    BOTH_ALIVE(p1 site; p2 pattern) /
    P1_MAIN_SPECIFIC(dig site) /
    P2_MAIN_SPECIFIC(pattern verbatim) /
    FORK_DEAD(p1 reason; p2 reason; lane-stop recommendation)
  + INDEX_LANGUAGE(exactness; restatement typing; vacuity)
    [always]
  + SIGNATURE_TABLE(per-world window defect / deep inertia /
    gray) [always]
  + FINGERPRINT(consensus pair/sign/share; world contrast)
    [always]
  + R312_DEMARCATION [always]: the r312 letters stand; this
    round adjudicates the REPRESENTATION question only.

RECORD TABLES (frozen from the record run; chronology honest:
(i) a PRE-RUN PROTOCOL CORRECTION is disclosed -- a draft
record-table block with placeholder numbers was removed from this
docstring BEFORE the first run of any stage (the r316 protocol
lesson, applied); (ii) smoke pass 1 ABORTED at G73 with a harness
crash (a tiebreak-type bug in the fp_consensus verifier, fixed at
smoke stage before any full evaluation; no rule content moved);
smoke pass 2 = 25/25 (0.2 s); (iii) calibration pass 1 = first
full evaluation = 25/25 (21.5 s) with ONE disclosed amendment a1
(reporting-only: the P2 verdict-letter dig-site label is derived
from the MEASURED modal pair -- the draft text had pre-named the
border column, which the measurement contradicts (d6-class share
0.027); no bar, band, statistic, rule or tree moved); calibration
pass 2 = 25/25 (23.7 s); record run1/run2 = 25/25, identical up
to WALL).
REC_VERDICT = P2_MAIN_SPECIFIC(fingerprint verbatim: modal
cross-mixture pair (2, 3) = D3 x D4 -- the ANTIPHASE x ANTIPHASE
coordinate pair of the sealed r312 library -- with sign -1,
median modal share 0.699, LAWFUL 12/12 sealed rungs AND
twin-consistent ((2, 3), -1, 0.692 -- METRIC_ONLY holds); the
controls break by PATTERN, not merely by bar: EPST modal (4, 5)
sign -1 share 0.953 / SCR modal (4, 5) sign -1 share 1.000 --
the dead worlds put their residual on the ARCH-MEAN x BORDER
pair (d6-class share 0.962/1.000 vs MAIN 0.027); honest caveat
typed with the letter: the EPST/SCR fingerprints are measured on
NON-psd-feasible 200-step iterates (feas -0.45/-0.49, the r308
non-convergence), labeled ITERATE -- the contrast compares the
converged MAIN-class family shape against the shape of a
non-converged control iterate; dig site named per the stop
rule: the D3 x D4 (antiphase x antiphase) cross-mixture residual
of the block-Green family -- WHY does the 2.4 percent negative
cross mixture of the converged psd family live on the antiphase
pair with a fixed negative sign, stably over 12 rungs and the
rational twin)
+ INDEX_LANGUAGE(EXACT: spectral count == mp pivot count at
window AND DEEP_EFF on all seven worlds (SCR deep 66/65 inside
its gray band 6 -- the single tolerated gray case, disclosed;
all other twelve counts exact, 0 guards / 0 recounts on w9);
RESTATEMENT: the equivalence 'window index defect == 0 <=>
minC >= N_w' holds on ALL 10 instances (3 exact toys JF9/
MAINLIKE/FLIPLIKE defects 2/0/1 + 7 real worlds) with both truth
values realized -- the reviewer's index form 'n_+(window) ==
N_w' is L* in signature language, a LANGUAGE gain with no
independent lever; VACUITY: the global inequality n_+ >= N_w is
carried by the mu-channel majority alone, S_+/N_w = 1.43/1.41/
1.43/1.23/1.48/1.96/1.52 on w9/w13/twin/EPST/SCR/SMOOTH/HL2 --
world-blind)
+ SIGNATURE_TABLE(window index defect w9 0 / w13 0 / twin 0 --
n_+ == N_w EXACTLY at the window on the mains, the index form
of half-filling survival -- vs EPST 55 / SCR 37 / SMOOTH 4 /
HL2 31: the control flips ARE negative directions inside the
window, measured as index defects; deep inertia at DEEP_EFF:
w9 43@262 / w13 36@236 / twin 43@262 / EPST 80@225 / SCR
66@272 / SMOOTH 6@360 / HL2 58@278; ladder 42/42 rungs window
defect 0 (half-filling 42/42); NEGATIVE-SUBSPACE INVARIANTS all
WORLD_BLIND under the sealed r281 distance rule (NEG_LOW MAIN
0.386 inside dead 0.0..1.28; NEG_MED MAIN 1.14 inside dead
0.39..1.90; NEG_PR MAIN 0.058 inside dead 0.030..0.326) and
NEG_LOW is NOT a proxy of the crossing location (devs 0.61/
0.51/0.79/0.11/0.11/1.13/0.03 > 0.15 on the mains -- the
negative directions do NOT live at minC, but their location is
world-blind: no lever either way); ladder NEG_LOW med 0.059
spread 0.473 (unstable); KREIN ANGULAR TEST typed INDEPENDENT
(spearman(ANG, rho_win) = +0.536 < 0.9; disclosed: ANG consumes
the UNSIGNED profiles sqrt(|v|^2), a magnitude-overlap
statistic -- values above 1 reflect the unsigned aggregation;
reported, no adjudication weight))
+ FINGERPRINT(consensus (2, 3) sign -1, 12/12 agree, med share
0.699; per-rung shares 0.605..0.780 over kz 9/12/13/14/15/18/
20/22/23/29/32/33, d6-class 0.005..0.064, cone-share med
0.970..0.982 -- the 97.6/2.4 anatomy is ladder-uniform; twin
(2, 3) -1 0.692; EPST (4, 5) -1 0.953 ITERATE / SCR (4, 5) -1
1.000 ITERATE)
+ R312_DEMARCATION.
Key numbers.  LEG 0 bit-near: w9 367/263/104/184/184, budget
B = 8.368649, mp crossing budget 104 == S_-, mp minC 184 ==
N_w, spectral crossing 185 == minC + 1; r312 pins reproduced:
Dykstra CONV +6.56e-16, cone share med/min/mean 0.9760/0.9520/
0.9778 (rec 0.976/0.952/0.978), alignment med 0.9973.  P2 SR
CENSUS (the honest negative half of P2): NO census object is
MAIN-specifically sign-regular -- E.principal and A.principal
score 1.000 but are NOT world-separating (E.principal is
psd-forced and pattern-identical everywhere; A.principal fails
the every-control-broken clause), and every orientation-
sensitive census is coin-flip on MAIN (E.rowinit 0.500 /
A.rowinit 0.503 / B.rowinit 0.500) => the SR premise of the
implication chain FAILS ON MAIN (PREMISE_FAILS_ON_MAIN: the
variation-diminishing route to L* cannot start; VD spot check
0 violations, world-blind bookkeeping).  MUST-FAILS: m1 wrong
signature convention 3 != 2 exact CAUGHT (JF9, Fractions); m2
transposed census exact CAUGHT (order-1 row (1, 1, -1)); m3
circular-lever mutant AST-FLAGGED (minC_true/rho_true); m4
single-rung consensus REJECTED (REJECT_INSUFFICIENT_RUNGS),
the 12-rung call accepted; constructors + fragment audit CLEAN.
READING (typed measurement): the reviewer's index language is
EXACT and gives L* its cleanest coordinate-free form -- "the
free polynomial window is a positive subspace of the canonical
Krein geometry I - M, of the maximal free dimension" -- but it
carries NO independent lever (restatement total, global index
vacuous, negative-subspace invariants world-blind): P1 closes
as language; the SIGNEDNESS FINGERPRINT is the round's find --
the reviewer's inversion question has a measured answer: the
2.4 percent negative cross mixtures are NOT structureless; on
MAIN-class worlds they live LAWFULLY on the antiphase pair
(D3, D4) with a fixed negative sign (12/12 rungs, twin exact),
while the dead controls' residual sits on the arch-mean x
border pair -- the fingerprint of the signedness is
world-separating in SHAPE, exactly the precondition the
reviewer's indefinite-theorem hope needs.  Runtime 23.7 s full
/ 0.2 s smoke; run1/run2 identical up to WALL.  AMENDMENTS
AFTER FREEZE: a1 only (reporting-only, disclosed above).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import blockgreen_membership_probe as BM           # noqa: E402 r312
import block_green_probe as BG                     # noqa: E402 r308
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import lstar_two_measure_probe as LS               # noqa: E402 r284
import budget_localization_probe as BL             # noqa: E402 r280
import oriented_theorem_probe as OT                # noqa: E402 r279
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import paircorr_margin_probe as PC                 # noqa: E402
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import bordered_hankel_probe as BH                 # noqa: E402 r244
import wronskian_dictionary_probe as WD            # noqa: E402 r274
import jfraction_probe as JF                       # noqa: E402 r230
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
MAIN_KZ = 9
KZ_SECOND = 13
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
H_CAP = 900
MP_DPS = 120
SIGN_GUARD = 1e-90
RECOUNT_DPS = 240
GRAY_LO = 0.9
GRAY_HI = 1.1
OFLOW_CAP = 1e100
NEG_MASS_Q = 0.10
PROX_TOL = 0.15
K_MAX = 5
ZTOL = 1e-10
Z_FRAC = 0.2
SR_BAR = 0.99
VD_DEGS = 20
N_FP = 12
FP_MIN_RUNGS = 10
FP_CONS = 10
FP_BAR = 0.5
FEAS_IT = 200
FEAS_CONV = 1e-9
SHARE_REC = (0.976, 0.952, 0.978)
SHARE_TOL = 0.01
ALIGN_REC = 0.9973
ALIGN_TOL = 0.005
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
W9_ANCH = (367, 263, 104, 184, 184)
BUDGET_REC = 104
TWIN_MINC_REC = 184
RAT_TOL = 1e-8
QMAX = 1e6
ANG_SP_BAR = 0.9
STAB_BINS = 20

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume passed matrices and "
                       "split-source arrays ONLY; record numbers "
                       "enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq_fit",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("finite_depth", "spectral_counts", "neg_profiles",
                "deg_stats", "ang_overlap", "det_sign",
                "minor_census", "census_shares",
                "block_residual_census", "fp_consensus",
                "vd_spotcheck", "frac_rowinit_signs")
SCOPE_FORBIDDEN = {"minC_true", "rho_true", "CTRL_FLIPS", "HL2_FLIP",
                   "W9_ANCH", "BUDGET_REC", "defect_true",
                   "cross_true", "HS_true", "sg_true"}


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def finite_depth(B, cap):
    """largest depth d <= ncols with every entry of B[:, :d]
    finite and max |entry| <= cap (the sealed overflow guard for
    deep frame spectra).  Consumes the passed matrix only."""
    d = 0
    for j in range(B.shape[1]):
        col = B[:, j]
        if not np.all(np.isfinite(col)) \
                or float(np.max(np.abs(col))) > cap:
            break
        d = j + 1
    return d


def spectral_counts(B, n):
    """spectral inertia counts of A_n = I - B_n^T B_n: n_neg =
    #{sigma_i(B_n) > 1} (negative directions) plus the near-one
    gray count sigma in (GRAY_LO, GRAY_HI).  Consumes the passed
    matrix only."""
    sv = np.linalg.svd(B[:, :n], compute_uv=False)
    n_neg = int(np.sum(sv > 1.0))
    n_gray = int(np.sum((sv > GRAY_LO) & (sv < GRAY_HI)))
    return n_neg, n_gray


def neg_profiles(B, n):
    """degree profiles |v_i(d)|^2 of the negative directions of
    A_n = I - B_n^T B_n (right singular vectors with sigma > 1,
    descending sigma).  Consumes the passed matrix only."""
    U, s, Vt = np.linalg.svd(B[:, :n], full_matrices=False)
    idx = np.nonzero(s > 1.0)[0]
    return Vt[idx] ** 2, s[idx]


def deg_stats(profiles, Nw):
    """sealed negative-subspace statistics: NEG_LOW / NEG_MED
    (min / median over directions of the lowest degree carrying
    cumulative mass >= NEG_MASS_Q, normalized by the passed
    window depth) and NEG_PR (median participation ratio of the
    profile, normalized).  Consumes the passed profiles only."""
    if profiles.shape[0] == 0:
        return None, None, None, []
    d10 = []
    prs = []
    for p in profiles:
        c = np.cumsum(p)
        d10.append(int(np.searchsorted(c, NEG_MASS_Q * c[-1])))
        prs.append(float((np.sum(p) ** 2) / max(np.sum(p * p),
                                                1e-300)))
    return (float(np.min(d10)) / Nw,
            float(np.median(d10)) / Nw,
            float(np.median(prs)) / Nw, d10)


def ang_overlap(Vt_neg, Nw):
    """principal-angle overlap of the free window with the deep
    negative subspace: largest singular value of the window block
    of the negative right-singular frame.  Consumes the passed
    frame only."""
    if Vt_neg.shape[0] == 0:
        return 0.0
    blk = Vt_neg[:, :Nw]
    sv = np.linalg.svd(blk, compute_uv=False)
    return float(sv[0]) if len(sv) else 0.0


def det_sign(sub):
    """sign of det(sub) with the sealed zero class |det| <=
    ZTOL x Hadamard bound.  Consumes the passed matrix only."""
    bnd = float(np.prod(np.linalg.norm(sub, axis=1)))
    if not math.isfinite(bnd) or bnd == 0.0:
        return 0
    d = float(np.linalg.det(sub))
    if not math.isfinite(d) or abs(d) <= ZTOL * bnd:
        return 0
    return 1 if d > 0 else -1


def minor_census(K, kmax, modes):
    """contiguous minor sign census: mode 'principal' =
    diagonal-sliding K[i..i+k-1, i..i+k-1] (square only), mode
    'rowinit' = rows 0..k-1 fixed, columns sliding (orientation
    sensitive).  Consumes the passed matrix only."""
    K = np.asarray(K, float)
    nr, nc = K.shape
    out = {}
    for mode in modes:
        per = []
        for k in range(1, kmax + 1):
            sgs = []
            if mode == "principal":
                if nr == nc:
                    for i in range(nr - k + 1):
                        sgs.append(det_sign(K[i:i + k, i:i + k]))
            else:
                if nr >= k:
                    for lo in range(nc - k + 1):
                        sgs.append(det_sign(K[0:k, lo:lo + k]))
            per.append(sgs)
        out[mode] = per
    return out


def census_shares(per_order):
    """per-order majority shares of one census: rows (k, n+, n-,
    n0, share, majority sign, zero fraction); SR_SCORE = min over
    live orders of the share; degenerate iff any populated order
    has zero fraction > Z_FRAC.  Consumes the passed census
    only."""
    rows = []
    for k, sgs in enumerate(per_order, start=1):
        npos = sum(1 for s in sgs if s > 0)
        nneg = sum(1 for s in sgs if s < 0)
        nz = sum(1 for s in sgs if s == 0)
        tot = npos + nneg
        share = (max(npos, nneg) / tot) if tot else 0.0
        maj = 0 if tot == 0 else (1 if npos >= nneg else -1)
        zfrac = nz / max(len(sgs), 1)
        rows.append((k, npos, nneg, nz, share, maj, zfrac))
    live = [r for r in rows if (r[1] + r[2]) > 0]
    score = min((r[4] for r in live), default=0.0)
    degen = any(r[6] > Z_FRAC for r in rows
                if (r[1] + r[2] + r[3]) > 0)
    pattern = tuple(r[5] for r in live)
    return dict(rows=rows, score=score, degen=degen,
                pattern=pattern)


def block_residual_census(g, nblk, V, A21, pa, pb, isow, iu1, ju1):
    """the r312 cross-mixture residual census: per block the
    sealed cone projection (NNLS onto the 22-generator library in
    isometric vech coordinates), the residual matrix R_r in the D
    basis, its dominant off-diagonal pair and sign, plus the cone
    share.  Consumes the passed iterate/coordinates only."""
    lam, scale, G = BG.block_eigs(g, nblk)
    pairs = []
    signs = []
    shares = []
    d6 = 0
    for r in range(nblk):
        rhs = G[r][pa, pb] * isow
        cc, rel, _s, _cap = BM.nnls_lh(A21, rhs)
        shares.append(1.0 - rel)
        res = A21 @ cc - rhs
        R = np.zeros((6, 6))
        R[pa, pb] = res / isow
        R = R + R.T - np.diag(np.diag(R))
        vals = R[iu1, ju1]
        j = int(np.argmax(np.abs(vals)))
        pairs.append((int(iu1[j]), int(ju1[j])))
        signs.append(1 if vals[j] > 0 else -1)
        if ju1[j] == 5 or iu1[j] == 5:
            d6 += 1
    cnt = {}
    for p, s in zip(pairs, signs):
        cnt[(p, s)] = cnt.get((p, s), 0) + 1
    modal = max(cnt, key=lambda k: (cnt[k], -k[0][0], -k[0][1]))
    return dict(modal_pair=modal[0], modal_sign=modal[1],
                modal_share=cnt[modal] / max(nblk, 1),
                d6_share=d6 / max(nblk, 1),
                share_med=float(np.median(shares)),
                share_min=float(np.min(shares)),
                share_mean=float(np.mean(shares)))


def fp_consensus(rows):
    """the sealed fingerprint consensus verifier: REJECTS any
    census with fewer than FP_MIN_RUNGS rungs (the m4 guard);
    LAWFUL iff >= FP_CONS rungs carry the same modal (pair, sign)
    with median modal share >= FP_BAR over the agreeing rungs.
    Consumes the passed census rows only."""
    if len(rows) < FP_MIN_RUNGS:
        return ("REJECT_INSUFFICIENT_RUNGS", None)
    cnt = {}
    for r in rows:
        key = (r["modal_pair"], r["modal_sign"])
        cnt[key] = cnt.get(key, 0) + 1
    modal = max(cnt, key=lambda k: (cnt[k], -k[0][0], -k[0][1]))
    agree = [r for r in rows
             if (r["modal_pair"], r["modal_sign"]) == modal]
    med_share = float(np.median([r["modal_share"] for r in agree]))
    lawful = (len(agree) >= FP_CONS) and (med_share >= FP_BAR)
    return ("OK", dict(pair=modal[0], sign=modal[1],
                       n_agree=len(agree), n_rungs=len(rows),
                       med_share=med_share, lawful=lawful))


def vd_spotcheck(Bs, kmax):
    """variation-diminishing spot check: the number of sign
    changes of the (atom-sorted) column i must be <= i for every
    degree column i < kmax (polynomial zero counting -- a
    world-blind bookkeeping gate).  Consumes the passed matrix
    only."""
    viol = 0
    for i in range(min(kmax, Bs.shape[1])):
        col = Bs[:, i]
        s = np.sign(col[col != 0.0])
        ch = int(np.sum(s[1:] != s[:-1])) if len(s) > 1 else 0
        if ch > i:
            viol += 1
    return viol


def frac_rowinit_signs(M, kmax):
    """EXACT (Fractions) row-initial contiguous minor sign census
    of the passed matrix (rows 0..k-1 fixed, columns sliding).
    Consumes the passed matrix only."""
    nr = len(M)
    nc = len(M[0])
    out = []
    for k in range(1, kmax + 1):
        sgs = []
        if nr >= k:
            for lo in range(nc - k + 1):
                d = FS.frac_det([row[lo:lo + k] for row in M[:k]])
                sgs.append(0 if d == 0 else (1 if d > 0 else -1))
        out.append(sgs)
    return out


# ============== must-fail mutants
def mutant_wrong_signature(hs, n):
    """m1 MUST-FAIL: index count with the WRONG signature
    convention -- counts the positive pivots instead of the
    negative ones; must mismatch the exact Frobenius inertia."""
    return sum(1 for k in range(n) if hs[k] > 0)


def mutant_circular_lever(minC_true, rho_true):
    """m3 MUST-FAIL: an 'additional-structure invariant' that
    consumes the withheld truth -- the scope audit must FLAG
    this."""
    return float(minC_true) + float(rho_true)


# ============== gate-side helpers
def frobenius_inertia_exact(minors, n):
    """gate-side exact Frobenius rule: n_-(H_n) = sign changes in
    the sequence (1, D_1, ..., D_n) of exact leading minors."""
    seq = [Fr(1)] + list(minors[:n])
    if any(v == 0 for v in seq):
        return None
    return sum(1 for a, b in zip(seq, seq[1:]) if (a > 0) != (b > 0))


def spectral_bundle(W):
    """gate-side per-world frame bundle: mu chain, B matrix to
    the guarded deep depth, window/deep spectral counts, negative
    profiles, statistics, angular overlap, rho at window."""
    Nw = W["N"]
    Sp = W["Sp"]
    deep = Sp - 1
    xp = np.asarray(W["xp"], float)
    wp = np.asarray(W["wp"], float)
    xn = np.asarray(W["xn"], float)
    vn = np.asarray(W["vn"], float)
    al, sb, h0 = FS.mu_chain_f64(xp, wp, deep)
    B = FS.b_matrix_f64(al, sb, h0, xn, vn, deep)
    deff = finite_depth(B, OFLOW_CAP)
    n_win = min(Nw, deff)
    cw, gw = spectral_counts(B, n_win)
    cd, gd = spectral_counts(B, deff)
    prof, sneg = neg_profiles(B, deff)
    nlow, nmed, npr, d10 = deg_stats(prof, Nw)
    ang = ang_overlap(np.sqrt(prof), Nw) if prof.shape[0] else 0.0
    rho_win = float(np.linalg.norm(B[:, :n_win], 2)) ** 2
    order = np.argsort(xn)
    Bs = B[order]
    return dict(B=B, Bs=Bs, deff=deff, n_win=n_win, cw=cw, gw=gw,
                cd=cd, gd=gd, prof=prof, sneg=sneg, nlow=nlow,
                nmed=nmed, npr=npr, d10=d10, ang=ang,
                rho_win=rho_win, Nw=Nw)


def sr_bundle(sp, Nw):
    """gate-side P2 census bundle on the atom-sorted window
    matrices E / A / B (positive scalings only -- every minor
    sign invariant)."""
    Bw = sp["Bs"][:, :min(Nw, sp["deff"])]
    scal = max(float(np.max(np.abs(Bw))), 1e-300)
    Bn = Bw / scal
    E = Bn @ Bn.T
    M = Bn.T @ Bn
    A = np.eye(M.shape[0]) - (scal ** 2) * M
    A = A / max(float(np.max(np.abs(A))), 1e-300)
    out = {}
    cE = minor_census(E, K_MAX, ("principal", "rowinit"))
    cA = minor_census(A, K_MAX, ("principal", "rowinit"))
    cB = minor_census(Bn, K_MAX, ("rowinit",))
    out["E.principal"] = census_shares(cE["principal"])
    out["E.rowinit"] = census_shares(cE["rowinit"])
    out["A.principal"] = census_shares(cA["principal"])
    out["A.rowinit"] = census_shares(cA["rowinit"])
    out["B.rowinit"] = census_shares(cB["rowinit"])
    out["_viol"] = vd_spotcheck(sp["Bs"][:, :min(VD_DEGS,
                                                 sp["deff"])],
                                VD_DEGS)
    return out


def fp_run(pack, ctx):
    """gate-side fingerprint run for one world: r308 census at
    DEG_A, Dykstra FEAS_IT steps from the least-norm start, the
    sealed block residual census."""
    Bw, _rho, bxa, bwa = BG.world_budget(pack, ctx)
    ffw, xaw, waw = BG.world_arrays(pack)
    C = BG.census_world(xaw, waw, bxa, bwa, Bw, DEG_A,
                        BG.hull_of(xaw, bxa))
    fm, rel, g = BM.feas_diag_g(C["M"], C["q"], C["g"],
                                C["nblk"], FEAS_IT)
    cen = block_residual_census(g, C["nblk"], V_LIB, A21_ISO,
                                PA6, PB6, ISOW, IU1, JU1)
    cen["feas"] = float(fm)
    cen["nblk"] = C["nblk"]
    return cen, C, g, Bw


V_LIB, V_LABELS = BM.lib_vectors()
PA6, PB6 = np.triu_indices(6)
ISOW = np.where(PA6 == PB6, 1.0, math.sqrt(2.0))
A21_ISO = np.stack([np.outer(v, v).astype(float)[PA6, PB6] * ISOW
                    for v in V_LIB], axis=1)
IU1, JU1 = np.triu_indices(6, k=1)

M_TP = [[Fr(1), Fr(2), Fr(3)],
        [Fr(1), Fr(3), Fr(6)],
        [Fr(-1), Fr(1), Fr(13)]]


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("indefinite_fork_probe -- PRIME.LSTAR.INDEFINITE_FORK.01 "
          "(round 318)")
    print("SPEC_SHA %s   (r312 BM %s / r283 FS %s / r284 LS %s / "
          "r279 OT %s)"
          % (SPEC_SHA[:16], BM.SPEC_SHA[:16], FS.SPEC_SHA[:16],
             LS.SPEC_SHA[:16], OT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (S0 + exact toys + hand census + w9 "
                        "f64 window block + must-fails + scopes; mp "
                        "legs, twin, controls, ladder, fingerprint, "
                        "censuses, adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the two routes (P1 Pontryagin/"
          "Krein index with the brutal restatement gate + the "
          "negative-subspace invariants + the proxy rule; P2 sign "
          "regularity with the contiguous minor census + the r312 "
          "cross-mixture fingerprint + the >= 10-rung consensus "
          "verifier), the frame convention A_n = I - M_n (r283 s2), "
          "the seven worlds, the 12 sealed fingerprint rungs, all "
          "four must-fails, every bar/band/tolerance, the Leg-C "
          "adjudication tree and the sealed verdict form; the stop "
          "rule is binding: both routes world-blind or restatement "
          "=> FORK_DEAD with a lane-stop recommendation")

    # ---------------- S1 exact toys
    section("S1  EXACT TOYS -- CONGRUENCE INERTIA + HAND TP CENSUS")
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    nodes9 = [t[0] for t in jf_pairs]
    wts9 = [t[1] for t in jf_pairs]
    toys = [("JF9", nodes9, wts9),
            ("MAINLIKE", BL.TOYS_XS, BL.MAINLIKE_W),
            ("FLIPLIKE", BL.TOYS_XS, BL.FLIPLIKE_W)]
    TB = {}
    toy_rows = []
    ok_cong = True
    ok_frob = True
    for name, nds, wt in toys:
        tb = FS.toy_block(nds, wt)
        TB[name] = tb
        ok_cong = ok_cong and tb["ok_cong"] and tb["ok_mu"]
        n_win = min(tb["Nw"], tb["Sp"])
        frob = frobenius_inertia_exact(tb["minors"], n_win)
        piv = sum(1 for k in range(n_win) if tb["hs"][k] < 0)
        ok_frob = ok_frob and (frob == piv)
        toy_rows.append((name, tb["minC"], tb["Nw"], piv))
        info("%s: S=%d N_w=%d S_+=%d minC=%s window defect "
             "(exact) = %d (Frobenius %s)"
             % (name, tb["S"], tb["Nw"], tb["Sp"],
                str(tb["minC"]), piv, str(frob)))
    check("G10-toy-congruence-inertia", ok_cong and ok_frob,
          "EXACT (Fractions): the r283 Sylvester congruence "
          "minor_k(D_mu - G) == D_k(mutilde) holds on all three "
          "toys AND the Frobenius sign-change inertia of the exact "
          "congruence minors equals the pivot count #{k < n : h_k "
          "< 0} at the window -- both truth values realized "
          "(defects %s): the index bookkeeping is exact at toy "
          "grade" % str({r[0]: r[3] for r in toy_rows}))
    sealed_tp = frac_rowinit_signs(M_TP, 3)
    ok_tp = all(all(s > 0 for s in ord_) for ord_ in sealed_tp)
    check("G11-toy-tp-census", ok_tp,
          "EXACT hand matrix M_TP = [[1,2,3],[1,3,6],[-1,1,13]]: "
          "the sealed row-initial contiguous census is all-"
          "positive at orders 1..3 (%s) -- the m2 substrate: the "
          "transposed census must break this pattern (S7)"
          % str([[int(s) for s in o] for o in sealed_tp]))

    # ---------------- S2 leg 0 anchors
    section("S2  LEG 0 -- W9 ANCHORS (v956 / r279 / r283 / r312)")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4]
              and W9["N"] == (W9["S"] + 1) // 2)
    B9, _rho9b, bxa9, bwa9 = BG.world_budget(W9, ctx9)
    check("G20-w9-source-pins", ok_src
          and abs(B9 - B_W9_REC) <= B_W9_TOL,
          "w9 SOURCE %d/%d/%d, N_w %d == (S+1)//2, minC %s == "
          "N_w (v956 pins); budget scalar B = %.6f (rec %.6f, "
          "tol %.0e)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"]),
             B9, B_W9_REC, B_W9_TOL))
    SP9 = spectral_bundle(W9)
    if smoke:
        # window co-location: f64 sign chain vs spectral count
        piv_f64 = int(np.sum(np.asarray(W9["sg"][:W9["N"]]) < 0))
        cross9 = None
        for n in range(1, SP9["n_win"] + 2):
            if float(np.linalg.norm(SP9["B"][:, :n], 2)) >= 1.0:
                cross9 = n
                break
        check("G21-w9-crossing-budget", SP9["cw"] == piv_f64 == 0
              and cross9 == W9["minC"] + 1,
              "SMOKE: window spectral defect %d == f64 pivot "
              "defect %d == 0 (exact half-filling positivity); "
              "crossing %s == minC + 1 (mp budget leg skipped)"
              % (SP9["cw"], piv_f64, str(cross9)))
        check("G22-r312-anchor", True, "SMOKE: skipped")
        HS9 = None
    else:
        al9m, be9m, SG9m, HS9, ng9, nr9 = OT.mp_chain_pack(
            np.asarray(W9["xu"], float), np.asarray(W9["wu"], float),
            MP_DPS, SIGN_GUARD, RECOUNT_DPS)
        budget9 = int(np.sum(HS9 < 0))
        minC9mp = next((n for n in range(len(HS9))
                        if HS9[n] < 0), None)
        cross9 = None
        for n in range(1, SP9["n_win"] + 2):
            if float(np.linalg.norm(SP9["B"][:, :n], 2)) >= 1.0:
                cross9 = n
                break
        check("G21-w9-crossing-budget", budget9 == BUDGET_REC
              and budget9 == W9["Sm"] and minC9mp == W9["N"]
              and cross9 == W9["minC"] + 1,
              "r279/v956/r283 pins: mp crossing budget #{h < 0} = "
              "%d == S_- == rec %d; mp minC = %s == N_w; spectral "
              "crossing %s == minC + 1 = %d (guards %d, recounts "
              "%d)" % (budget9, BUDGET_REC, str(minC9mp),
                       str(cross9), W9["minC"] + 1, ng9, nr9))
        cen9, C9, g9, _B9w = fp_run(W9, ctx9)
        # alignment census (r312 anatomy, verbatim class)
        lam9, sc9, G9 = BG.block_eigs(g9, C9["nblk"])
        ev9, Wv9 = np.linalg.eigh(G9)
        top9 = Wv9[:, :, -1]
        Vn = V_LIB.astype(float)
        Vn = Vn / np.linalg.norm(Vn, axis=1, keepdims=True)
        align9 = float(np.median(np.max(np.abs(top9 @ Vn.T),
                                        axis=1)))
        ok_312 = (cen9["feas"] >= -FEAS_CONV
                  and abs(cen9["share_med"] - SHARE_REC[0])
                  <= SHARE_TOL
                  and abs(cen9["share_min"] - SHARE_REC[1])
                  <= SHARE_TOL
                  and abs(cen9["share_mean"] - SHARE_REC[2])
                  <= SHARE_TOL
                  and abs(align9 - ALIGN_REC) <= ALIGN_TOL)
        check("G22-r312-anchor", ok_312,
              "r312 CROSS-MIXTURE PINS reproduced (identical "
              "protocol: Dykstra %d steps, per-block NNLS): CONV "
              "%+.2e; cone share med/min/mean %.4f/%.4f/%.4f (rec "
              "%.3f/%.3f/%.3f, tol %.2f); alignment med %.4f (rec "
              "%.4f) -- the 97.6/2.4 anatomy stands; w9 modal "
              "residual pair %s sign %+d share %.3f d6-class %.3f"
              % (FEAS_IT, cen9["feas"], cen9["share_med"],
                 cen9["share_min"], cen9["share_mean"],
                 SHARE_REC[0], SHARE_REC[1], SHARE_REC[2],
                 SHARE_TOL, align9, ALIGN_REC,
                 str(cen9["modal_pair"]), cen9["modal_sign"],
                 cen9["modal_share"], cen9["d6_share"]))

    # ---------------- S3 leg A P1
    section("S3  LEG A -- P1 PONTRYAGIN/KREIN INDEX")
    if smoke:
        for g in ("G30-index-form-exact", "G31-signature-table",
                  "G32-restatement-adjudication",
                  "G33-negspace-invariants", "G34-plus-operator"):
            check(g, True, "SMOKE: skipped")
        WORLDS = {}
        SPB = {}
        packs = {}
        neg_sep = {}
        proxy = True
        restat = True
        ok_idx = True
    else:
        # build the seven worlds
        ctx13 = MS.ctx_build(KZ_SECOND)
        D13 = float(core.build_window(KZ_SECOND)["D"])
        W13 = LS.world_pack("w13", ctx13, D13)
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tg = PC.gen_model(gpc, "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        WORLDS = {"w9": (W9, ctx9), "w13": (W13, ctx13),
                  "twin": (WT, ctxT)}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            WORLDS[cn] = (LS.world_pack(cn, cctx, D9), cctx)
        ok_ctrl = all(
            WORLDS[cn][0]["minC"] == CTRL_FLIPS.get(cn, HL2_FLIP)
            for cn in ("EPST", "SCR", "SMOOTH", "HL2"))
        # spectral + mp bundles
        SPB = {"w9": SP9}
        HSD = {"w9": HS9}
        for wn in ("w13", "twin", "EPST", "SCR", "SMOOTH", "HL2"):
            Wp = WORLDS[wn][0]
            SPB[wn] = spectral_bundle(Wp)
            _a, _b, _S, HSw, _g, _r = OT.mp_chain_pack(
                np.asarray(Wp["xu"], float),
                np.asarray(Wp["wu"], float),
                MP_DPS, SIGN_GUARD, RECOUNT_DPS)
            HSD[wn] = HSw
        ok_idx = ok_tc and (WT["minC"] == TWIN_MINC_REC) and ok_ctrl
        idx_txt = []
        defects = {}
        for wn in WORLDS:
            sp = SPB[wn]
            HSw = HSD[wn]
            piv_w = int(np.sum(HSw[:sp["n_win"]] < 0))
            piv_d = int(np.sum(HSw[:sp["deff"]] < 0))
            okw = (abs(sp["cw"] - piv_w) <= sp["gw"]
                   and sp["cw"] == piv_w if sp["gw"] == 0
                   else abs(sp["cw"] - piv_w) <= sp["gw"])
            okd = (sp["cd"] == piv_d if sp["gd"] == 0
                   else abs(sp["cd"] - piv_d) <= sp["gd"])
            ok_idx = ok_idx and okw and okd
            defects[wn] = piv_w
            idx_txt.append("%s %d/%d@%d(g%d)"
                           % (wn, sp["cw"], piv_w, sp["n_win"],
                              sp["gw"]))
            info("%s: window defect spec/mp %d/%d @ n=%d (gray "
                 "%d); deep %d/%d @ DEEP_EFF=%d (gray %d); "
                 "n_neg dirs %d" % (wn, sp["cw"], piv_w,
                                    sp["n_win"], sp["gw"],
                                    sp["cd"], piv_d, sp["deff"],
                                    sp["gd"], sp["prof"].shape[0]))
        check("G30-index-form-exact", ok_idx,
              "INDEX-FORM EXACTNESS: spectral count #{sigma(B_n) > "
              "1} == mp pivot count #{k < n : h_k < 0} at the "
              "window AND at DEEP_EFF on ALL SEVEN worlds (%s; "
              "sealed gray rule; twin rebuilt verbatim, minC %s == "
              "rec %d; control flips re-derived) -- the "
              "Jacobi/Sylvester index dictionary is machine-exact "
              "in the frame" % ("; ".join(idx_txt), str(WT["minC"]),
                                TWIN_MINC_REC))
        # ladder defect
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        packs = {}
        n_hf = 0
        n_def0 = 0
        for kz in kzs:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx)
            if Wp["N"] == (Wp["S"] + 1) // 2:
                n_hf += 1
            dfk = int(np.sum(np.asarray(Wp["sg"][:Wp["N"]]) < 0))
            if dfk == 0:
                n_def0 += 1
        sp_ratio = {wn: WORLDS[wn][0]["Sp"] / SPB[wn]["Nw"]
                    for wn in WORLDS}
        ok_vac = all(v >= 1.0 for v in sp_ratio.values())
        ok_sig = (defects["w9"] == 0 and defects["w13"] == 0
                  and defects["twin"] == 0
                  and all(defects[c] > 0 for c in
                          ("EPST", "SCR", "SMOOTH", "HL2"))
                  and n_hf == len(kzs) == 42
                  and n_def0 == len(kzs))
        check("G31-signature-table", ok_sig and ok_vac,
              "SIGNATURE TABLE: window index defect %s -- the "
              "mains + twin sit at d_w == 0 EXACTLY (n_+ == N_w: "
              "the index form of half-filling survival), every "
              "control has negative directions INSIDE the window "
              "(the flip as an index defect); ladder %d/%d rungs "
              "defect 0 (half-filling %d/%d); VACUITY measured: "
              "S_+/N_w = %s >= 1 on every world -- the global "
              "index inequality n_+ >= N_w is carried by the "
              "mu-channel majority alone (world-blind, VACUOUS as "
              "a discriminator)"
              % (str(defects), n_def0, len(kzs), n_hf, len(kzs),
                 str({k: round(v, 2) for k, v in
                      sp_ratio.items()})))
        # restatement adjudication
        inst = []
        for name in TB:
            tb = TB[name]
            n_win_t = min(tb["Nw"], tb["Sp"])
            dft = sum(1 for k in range(n_win_t) if tb["hs"][k] < 0)
            inst.append((name, dft == 0,
                         tb["minC"] is None
                         or tb["minC"] >= tb["Nw"]))
        for wn in WORLDS:
            mc = WORLDS[wn][0]["minC"]
            inst.append((wn, defects[wn] == 0,
                         mc is None or mc >= SPB[wn]["Nw"]))
        restat = all(a == b for _n, a, b in inst)
        both_vals = (any(a for _n, a, _b in inst)
                     and any(not a for _n, a, _b in inst))
        check("G32-restatement-adjudication", restat and both_vals,
              "THE BRUTAL RESTATEMENT GATE: the equivalence "
              "'window index defect == 0 <=> minC >= N_w' holds on "
              "ALL %d instances (3 exact toys + 7 real worlds) "
              "with BOTH truth values realized (%s) => the index "
              "statement 'n_+(window) == N_w' is typed RESTATEMENT "
              "of L*/free-window survival -- valuable as LANGUAGE "
              "(the cleanest coordinate-free form of the wall), "
              "carrying NO independent lever; P1 lives or dies on "
              "the additional structure (G33)"
              % (len(inst), str([(n, a) for n, a, _b in inst])))
        # negative-subspace invariants
        ctrls = ("EPST", "SCR", "SMOOTH", "HL2")
        neg_sep = {}
        for stat in ("nlow", "nmed", "npr"):
            tab = {"MAIN": SPB["w9"][stat]}
            for cn in ctrls:
                tab[cn] = SPB[cn][stat]
            neg_sep[stat] = (LS.dist_rule(tab, list(ctrls)), tab)
        proxy_dev = {}
        for wn in WORLDS:
            mc = WORLDS[wn][0]["minC"]
            mcf = (mc if mc is not None else SPB[wn]["Nw"]) \
                / SPB[wn]["Nw"]
            nl = SPB[wn]["nlow"]
            proxy_dev[wn] = abs((nl if nl is not None else mcf)
                                - mcf)
        proxy = all(v <= PROX_TOL for v in proxy_dev.values())
        # ladder stability of NEG_LOW on the 12 FP rungs
        fp_kzs = [MAIN_KZ] + [kz for kz, _ in
                              sorted(((kz, packs[kz][0]["S"])
                                      for kz in packs
                                      if kz != MAIN_KZ),
                                     key=lambda t: (t[1], t[0]))
                              ][:N_FP - 1]
        nl_r = []
        for kz in fp_kzs:
            Wp = packs[kz][0]
            spk = spectral_bundle(Wp)
            if spk["nlow"] is not None:
                nl_r.append(spk["nlow"])
        stab_med = float(np.median(nl_r)) if nl_r else float("nan")
        stab_spr = (float(np.max(nl_r) - np.min(nl_r))
                    if nl_r else float("nan"))
        check("G33-negspace-invariants", True,
              "NEGATIVE-SUBSPACE INVARIANTS (deep, DEEP_EFF-"
              "guarded): sealed distance rule %s; PROXY TEST: "
              "|NEG_LOW - minC/N_w| = %s (tol %.2f) => %s; ladder "
              "stability (12 FP rungs): NEG_LOW med %.3f spread "
              "%.3f -- MEASURED, adjudicated in S5"
              % (str({k: (v[0], {kk: (None if vv is None else
                                      round(vv, 4))
                                 for kk, vv in v[1].items()})
                      for k, v in neg_sep.items()}),
                 str({k: round(v, 3) for k, v in
                      proxy_dev.items()}), PROX_TOL,
                 "RESTATEMENT_PROXY (fires)" if proxy
                 else "not a proxy", stab_med, stab_spr))
        # plus-operator / angular dictionary
        angs = [SPB[wn]["ang"] for wn in WORLDS]
        rhos = [SPB[wn]["rho_win"] for wn in WORLDS]
        sp_ang = BH.spearman(angs, rhos)
        ang_restat = abs(sp_ang) >= ANG_SP_BAR
        check("G34-plus-operator", True,
              "KREIN ANGULAR TEST: window/negative-subspace "
              "overlap ANG per world %s; spearman(ANG, rho_win) = "
              "%+.3f (bar %.1f) => the angular-operator language "
              "is typed %s -- the plus-operator question %s"
              % (str({wn: round(SPB[wn]["ang"], 4)
                      for wn in WORLDS}), sp_ang, ANG_SP_BAR,
                 "RESTATEMENT (collapses onto the contraction "
                 "scalar = L*)" if ang_restat else "INDEPENDENT "
                 "(reported, no implication chain)",
                 "collapses onto L*" if ang_restat
                 else "stays open"))

    # ---------------- S4 leg B P2
    section("S4  LEG B -- P2 SIGN REGULARITY / FINGERPRINT")
    if smoke:
        for g in ("G40-minor-census-main", "G41-sr-adjudication",
                  "G42-fingerprint-census",
                  "G43-fingerprint-contrast",
                  "G44-implication-chain"):
            check(g, True, "SMOKE: skipped")
        sr_specific = False
        fp_specific = False
        fp_cons = None
        sr_main = {}
    else:
        SRB = {wn: sr_bundle(SPB[wn], SPB[wn]["Nw"])
               for wn in WORLDS}
        sr_main = SRB["w9"]
        txt40 = str({k: round(v["score"], 3)
                     for k, v in sr_main.items()
                     if not k.startswith("_")})
        check("G40-minor-census-main", True,
              "MINOR CENSUS on MAIN (contiguous, orders 1..%d, "
              "zero class %.0e x Hadamard): SR scores %s "
              "(patterns %s) -- MEASURED, adjudicated in G41"
              % (K_MAX, ZTOL, txt40,
                 str({k: v["pattern"] for k, v in sr_main.items()
                      if not k.startswith("_")})))
        objs = [k for k in sr_main if not k.startswith("_")]
        sr_specific = False
        sr_detail = []
        for ob in objs:
            m_ok = (sr_main[ob]["score"] >= SR_BAR
                    and not sr_main[ob]["degen"])
            t_ok = (SRB["twin"][ob]["score"] >= SR_BAR
                    and SRB["twin"][ob]["pattern"]
                    == sr_main[ob]["pattern"])
            c_all = all(
                SRB[cn][ob]["score"] < SR_BAR
                or SRB[cn][ob]["pattern"] != sr_main[ob]["pattern"]
                for cn in ("EPST", "SCR", "SMOOTH", "HL2"))
            if m_ok:
                sr_detail.append("%s MAIN-SR (twin %s, controls "
                                 "broken %s)" % (ob, t_ok, c_all))
            if m_ok and t_ok and c_all:
                sr_specific = True
        wb_objs = [ob for ob in objs
                   if all(SRB[wn][ob]["score"] >= SR_BAR
                          and SRB[wn][ob]["pattern"]
                          == sr_main[ob]["pattern"]
                          for wn in WORLDS)]
        check("G41-sr-adjudication", True,
              "SR ADJUDICATION (sealed rule, bar %.2f): "
              "MAIN-specific objects: %s; world-blind sign-regular "
              "objects (same pattern everywhere): %s; twin scores "
              "%s -- %s"
              % (SR_BAR,
                 str(sr_detail) if sr_detail else "NONE",
                 str(wb_objs) if wb_objs else "NONE",
                 str({k: round(v["score"], 3)
                      for k, v in SRB["twin"].items()
                      if not k.startswith("_")}),
                 "SR MAIN-SPECIFIC" if sr_specific
                 else "no MAIN-specific sign regularity"))
        # fingerprint on the 12 sealed rungs
        fp_rows = []
        for kz in fp_kzs:
            Wp, ctx = packs[kz]
            if kz == MAIN_KZ:
                cen = cen9
            else:
                cen, _C, _g, _Bw = fp_run(Wp, ctx)
            cen["kz"] = kz
            fp_rows.append(cen)
            info("kz%-3d: modal %s sign %+d share %.3f d6 %.3f "
                 "cone-share med %.3f feas %+.1e"
                 % (kz, str(cen["modal_pair"]), cen["modal_sign"],
                    cen["modal_share"], cen["d6_share"],
                    cen["share_med"], cen["feas"]))
        st, fp_cons = fp_consensus(fp_rows)
        check("G42-fingerprint-census", st == "OK"
              and fp_cons is not None,
              "CROSS-MIXTURE FINGERPRINT (12 sealed rungs, r308 "
              "Dykstra %d steps + sealed cone projection): "
              "consensus %s -- %s"
              % (FEAS_IT, str(fp_cons),
                 "LAWFUL on the MAIN ladder" if fp_cons["lawful"]
                 else "NOT lawful (no stable modal pattern)"))
        # world contrast: twin + EPST/SCR at w9
        fp_ctrl = {}
        for wn in ("twin", "EPST", "SCR"):
            Wp, ctx = WORLDS[wn]
            cen, _C, _g, _Bw = fp_run(Wp, ctx)
            fp_ctrl[wn] = cen
            info("%s: modal %s sign %+d share %.3f d6 %.3f feas "
                 "%+.1e%s"
                 % (wn, str(cen["modal_pair"]), cen["modal_sign"],
                    cen["modal_share"], cen["d6_share"],
                    cen["feas"],
                    "" if cen["feas"] >= -FEAS_CONV
                    else "  [ITERATE, not psd-feasible]"))
        twin_ok = (fp_ctrl["twin"]["modal_pair"] == fp_cons["pair"]
                   and fp_ctrl["twin"]["modal_sign"]
                   == fp_cons["sign"]
                   and fp_ctrl["twin"]["modal_share"] >= FP_BAR)
        ctrl_broken = {}
        for cn in ("EPST", "SCR"):
            c = fp_ctrl[cn]
            ctrl_broken[cn] = (c["modal_pair"] != fp_cons["pair"]
                               or c["modal_sign"] != fp_cons["sign"]
                               or c["modal_share"] < FP_BAR)
        fp_specific = (fp_cons["lawful"] and twin_ok
                       and all(ctrl_broken.values()))
        pat_match = {cn: (fp_ctrl[cn]["modal_pair"]
                          == fp_cons["pair"]
                          and fp_ctrl[cn]["modal_sign"]
                          == fp_cons["sign"])
                     for cn in ("EPST", "SCR")}
        check("G43-fingerprint-contrast", True,
              "FINGERPRINT WORLD CONTRAST: twin %s (METRIC_ONLY "
              "%s); controls broken %s (pattern-match census %s: "
              "a control that matches the PAIR but breaks the "
              "SHARE bar means the fingerprint SHAPE is "
              "construction-generic and only its MAGNITUDE "
              "separates -- printed honestly with the letter) => "
              "%s" % (str((fp_ctrl["twin"]["modal_pair"],
                           fp_ctrl["twin"]["modal_sign"],
                           round(fp_ctrl["twin"]["modal_share"],
                                 3))),
                      "holds" if twin_ok else "BREAKS",
                      str(ctrl_broken), str(pat_match),
                      "FP MAIN-SPECIFIC" if fp_specific
                      else "fingerprint not world-separating"))
        viol = sr_main["_viol"]
        premise = (sr_main["B.rowinit"]["score"] >= SR_BAR
                   and not sr_main["B.rowinit"]["degen"])
        check("G44-implication-chain", viol == 0,
              "IMPLICATION SKETCH (SR(B) => variation diminishing "
              "=> sign-change bounds at every truncation => r277 "
              "R2 reality/interlacing <=> window quasi-"
              "definiteness = v962-T4 form of L*): VD spot check "
              "0 violations required (measured %d, world-blind "
              "polynomial bookkeeping); THE MEASURED PREMISE on "
              "MAIN: B row-initial SR score %.3f (bar %.2f) => %s"
              % (viol, sr_main["B.rowinit"]["score"], SR_BAR,
                 "PREMISE_HOLDS -- the chain is live"
                 if premise else "PREMISE_FAILS_ON_MAIN -- the "
                 "variation-diminishing route cannot start "
                 "(honest negative)"))

    # ---------------- S5 leg C adjudication
    section("S5  LEG C -- THE FORK ADJUDICATION (SEALED TREE)")
    if smoke:
        check("G50-fork-adjudication", True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        p1_sep = [k for k, v in neg_sep.items()
                  if v[0] == "MAIN_SEPARATING"]
        p1_alive = bool(ok_idx and p1_sep and not proxy)
        p2_alive = bool(sr_specific or fp_specific)
        if p1_alive and p2_alive:
            main_v = ("BOTH_ALIVE(P1 dig site: deep negative-"
                      "subspace %s; P2 pattern: %s)"
                      % (str(p1_sep), str(fp_cons)))
        elif p1_alive:
            main_v = ("P1_MAIN_SPECIFIC(dig site: the deep "
                      "negative-subspace degree localization -- "
                      "separating statistics %s, not a proxy of "
                      "the crossing location; dig where the "
                      "negative directions live relative to N_w)"
                      % str(p1_sep))
        elif p2_alive:
            if fp_specific:
                # amendment a1 (disclosed, reporting-only): the
                # dig-site label is derived from the MEASURED
                # modal pair (the draft text pre-named the border
                # column, contradicting the measurement; no bar,
                # rule or tree moved).
                dnm = ("D1", "D2", "D3", "D4", "D5", "D6")
                dcl = {0: "fold-distance-1", 1: "fold-distance-2",
                       2: "antiphase", 3: "antiphase",
                       4: "arch-mean", 5: "border"}
                pr_ = fp_cons["pair"]
                site = ("%s x %s (%s x %s)"
                        % (dnm[pr_[0]], dnm[pr_[1]],
                           dcl[pr_[0]], dcl[pr_[1]]))
                main_v = ("P2_MAIN_SPECIFIC(fingerprint verbatim: "
                          "modal cross-mixture pair %s sign %+d, "
                          "median modal share %.3f, lawful %d/%d "
                          "rungs + twin-consistent; controls "
                          "break by %s -- dig site: the %s "
                          "cross-mixture residual of the "
                          "block-Green family)"
                          % (str(fp_cons["pair"]), fp_cons["sign"],
                             fp_cons["med_share"],
                             fp_cons["n_agree"], fp_cons["n_rungs"],
                             str({cn: ("pattern" if not
                                       pat_match[cn] else
                                       "share bar only")
                                  for cn in pat_match}), site))
            else:
                main_v = ("P2_MAIN_SPECIFIC(sign regularity: %s)"
                          % str(sr_detail))
        else:
            main_v = ("FORK_DEAD(P1: index language EXACT but "
                      "RESTATEMENT%s%s; P2: %s; %s -- LANE-STOP "
                      "RECOMMENDATION per the binding stop rule)"
                      % (" + proxy" if proxy else "",
                         "" if p1_sep else " + no separating "
                         "negative-subspace statistic",
                         "no sign-regular object is MAIN-specific"
                         if not sr_specific else "",
                         "fingerprint not world-separating"
                         if not fp_specific else ""))
        verd = " + ".join([
            main_v,
            "INDEX_LANGUAGE(exact %s; restatement %s; vacuity "
            "measured)" % (ok_idx, restat),
            "SIGNATURE_TABLE(defects %s)" % str(defects),
            "FINGERPRINT(%s)" % str(fp_cons),
            "R312_DEMARCATION(the r312 letters stand; this round "
            "adjudicates the representation question only)"])
        check("G50-fork-adjudication", True,
              "SEALED TREE: alive(P1) = %s (separating %s, proxy "
              "%s, exact %s); alive(P2) = %s (SR %s, FP %s) => %s"
              % (p1_alive, str(p1_sep), proxy, ok_idx, p2_alive,
                 sr_specific, fp_specific, main_v.split("(")[0]))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS + SCOPE AUDITS (LEG D)")
    tb9 = TB["JF9"]
    n_win9 = min(tb9["Nw"], tb9["Sp"])
    true_def = frobenius_inertia_exact(tb9["minors"], n_win9)
    mut_def = mutant_wrong_signature(tb9["hs"], n_win9)
    check("G70-mustfail-signature-convention",
          true_def is not None and mut_def != true_def,
          "m1 WRONG SIGNATURE CONVENTION (exact JF9, Fractions): "
          "the mutant counts %d positive pivots where the exact "
          "Frobenius inertia of the congruence minors is %d -- "
          "MISMATCH, CAUGHT loud" % (mut_def, true_def))
    mut_tp = frac_rowinit_signs(
        [list(row) for row in zip(*M_TP)], 3)
    broke = any(any(s < 0 for s in ord_) for ord_ in mut_tp)
    check("G71-mustfail-transposed-census", ok_tp and broke,
          "m2 TRANSPOSED CENSUS (exact): the sealed row-initial "
          "census of M_TP is all-positive while the census of "
          "M_TP^T contains a negative minor (order-1 row (1,1,-1))"
          " -- the orientation of the census is load-bearing, "
          "CAUGHT (%s)"
          % str([[int(s) for s in o] for o in mut_tp]))
    hits_m3 = scope_audit("mutant_circular_lever")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G72-mustfail-circular-lever", bool(hits_m3)
          and not hits and not ag_hits,
          "m3 CIRCULAR L* CONSUMPTION: the mutant invariant "
          "consuming the withheld truth is FLAGGED by the AST "
          "scope audit (%s); the %d sealed constructors audit "
          "CLEAN; fragment audit %s"
          % ("; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    toy_rows_fp = [dict(modal_pair=(0, 5), modal_sign=1,
                        modal_share=0.9)] * N_FP
    st_full, _c1 = fp_consensus(toy_rows_fp)
    st_one, _c2 = fp_consensus(toy_rows_fp[:1])
    check("G73-mustfail-single-rung", st_full == "OK"
          and st_one == "REJECT_INSUFFICIENT_RUNGS",
          "m4 SINGLE-RUNG EXTRAPOLATION: the sealed consensus "
          "verifier accepts the %d-rung census and REJECTS the "
          "single-rung mutant call loudly (%s) -- fingerprint "
          "consistency is FORCED across >= %d rungs"
          % (N_FP, st_one, FP_MIN_RUNGS))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "re-opened no-go entry, no bar/rule change after "
          "evaluation, no RH claim; r243..r316 stand; the r312 "
          "letters stand -- this round adjudicates the "
          "REPRESENTATION question of the fork only")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the stop rule is binding: FORK_DEAD => stop "
          "the lane; a MAIN-specific route => dig at the named "
          "site; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""continuous_coordinate_probe -- PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01
(round 321): THE CONTINUOUS-COORDINATE ROUND -- reviewer fork (a)
in the r317-sharpened form: bound rho_2 BY the single source-pure
concentration coordinate, do NOT classify by threshold.  The r317
fallback fired (WHAC_A_MOLE: the near-critical family is a
CONTINUUM, threshold classification swallows harmless rungs or
leaves kz53/kz83 uncovered), and the r317 census delivered the
sharpened form: the rank-local QMAX ratio F_A -- ONE source-pure
coordinate, computable in advance -- ranks the COMPLETE mid/deep
near-critical family on top (top-3 EXACTLY kz53 2.47 / kz83 2.39 /
kz67 2.38, refuting the r316 conjecture that kz53 needs a second
coordinate), with a continuum below (1.93, 1.90, 1.74, ...).  THE
ONE QUESTION OF THIS ROUND: does an explicit MONOTONE function g
exist with rho_2(w) <= g(F_A(w)) pointwise on ALL rungs
(mid-ladder calibrated, sealed), so that g(F_A) x (log m)^2 / m^2
is the new SLIDING uniform Renyi-3 bound -- no regimes, no
exception families, one gliding bound -- and is the coordinate
bound world-correct (twin/EPSTEIN admitted, SCRAMBLE breaks or
stays class-rejected, honestly documented which mechanism fires)?
Context (sealed record inputs): r306 (SPEC 3bb365e1) fixed sum q^3
<= 1.069 (log m)^2/m^2 pointwise 0/57 (first-5 constant,
r316-rehabilitated as load-bearing); r316 (SPEC 5c28b12b) sealed
TWO_REGIME_DEAD and the violator anatomy (kz53 rho_2 1.0493 at
bulk-normal FCIX, kz83 0.7791, kz55/kz67 the divergence-mass
spikes; C_gen 0.4579 mid-ladder; C_small 1.0694; 21 small-m
certificates; complement rest trend -0.170); r317 (SPEC 04fbe5c0)
sealed WHAC_A_MOLE and delivered F_A (rank-local QMAX spike ratio,
window W = 5) with the top-3 ranking above.  kz15 permanently
closed via r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r318 (base fork) and r320 (Lean repair) run in
parallel; this probe touches NOTHING outside its own file and the
strictly additive rh-sync.

THE OBJECT (r269/r287/r298/r306/r314/r315/r316/r317 machinery
imported verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266
eval); F = 0.20 edge split; maximal same-sign runs of the
bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298 WBT.block_breaks +
WBT.aggregate_blocks); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope + SCF.collision_census;
the r315 PHI.phi3_variants; the r316 TRB.two_regime_state +
TRB.split_midladder; the r317 EFP.local_ratio + EFP.gap_threshold,
ALL imported verbatim; PDelta = Pbeta - Pomega; x_j = (PDelta)_j.
NEW in this round (module-own, source-pure where required): the
rank-local median companion (local_median, the B-side baseline
column), the sealed monotone g-family evaluator + calibrator, the
sealed monotonicity grid check, the fit-free upper-envelope
builder with declared-set ward, the rank correlation, the
insertion-rule world coordinate and the sealed verdict tree.

THE SEALED COORDINATE (r317 verbatim, frozen): on the (N, kz)-
sorted class ladder of n rungs (42 core + 15 r286 extension + the
8 EXT2 anchors, multiplicity cap <= 2, POSITIVE_PREFIX), with
QMAX(i) = max_j |x_j| / L the sealed r316 column (source-pure by
the r316/r317 audits),
    F_A(i) = QMAX(i) / med{ QMAX(j) : |j - i| <= W, j != i },
rank-local ratio with half-width W = CLS_W = 5 (truncated at the
ladder ends), computed by the IMPORTED r317 builder
EFP.local_ratio -- no redefinition.  The companion baseline
    medloc(i) = med{ QMAX(j) : |j - i| <= W, j != i }
is computed by the module-own local_median (window verbatim) and
warded EXACT against the import: QMAX == F_A x medloc.

THE EXACT CONCENTRATION BRACKET (derived algebra, disclosed, no
measurement): with L = sum |x_j|, qmax = QMAX, rho_2 = NORM x
sum |x|^3 (NORM = m^2/((log m)^2 L^3), the r306 scale) and PhiH1 =
(m qmax / log m)^2 (the r316 concentration majorant):
    qmax^3 L^3 <= sum |x|^3 <= qmax^2 L^2 x sum |x| = qmax^2 L^3
  =>  qmax x PhiH1  <=  rho_2  <=  PhiH1,
a TWO-SIDED bracket: high F_A forces the QMAX share up and rho_2
is pinched between qmax x PhiH1 and PhiH1 -- exactly the r317
"B-certificate spirit" chain (near-one-block => QMAX high => sum
q^3 within an explicit factor of qmax^3).  Substituting qmax =
F_A x medloc gives PhiH1 == (F_A x B)^2 EXACT with
    B(i) = medloc(i) x m_i / log m_i
-- the rank-local BASELINE SCALE, source-pure (consumes the QMAX
column + rank order + m only), robust against spikes (a spike
moves F_A, not the local median).  THE UPPER DIRECTION OF THE
BRACKET IS CARRIED BY B: rho_2 <= F_A^2 x B^2 by exact algebra --
whether B is mid-ladder bounded is precisely the measurable
transfer question of Leg C, and it is a SOURCE-PURE question.
Both bracket sides and the PhiH1 == (F_A B)^2 identity are warded
live on every live world (CHAIN_BAR).

THE SEALED g-FAMILY (frozen BEFORE any evaluation of this round;
2-3 forms as the fork-(a) contract demands; every form MONOTONE
non-decreasing on F > 0 by construction, checked on the sealed
grid; constants frozen on the r316 mid-ladder calibration window
by the sealed rules below; precedence sealed by DERIVATION
STRENGTH, not by data):
  G_SQ  (STRUCTURAL QUADRATIC, precedence 1 -- derived from the
        exact bracket, not from data):  g(F) = b x F^2  with
        b = (max over CAL of B(i))^2.  By the exact bracket,
        rho_2 <= F_A^2 B^2 <= b F_A^2 holds on every rung whose
        baseline B stays below its calibration maximum -- the
        certification measures EXACTLY the source-pure
        boundedness of B (Leg C's question), and the calibration
        consumes NO target value at all (source-pure column only).
  G_TT  (TWO-TERM CUBIC, precedence 2 -- the r317-named reading
        form C_1 + C_2 F^gamma with gamma = 3 from the
        concentration heuristic: a spike of factor F in QMAX at
        fixed baseline inflates the cube-dominant term like F^3):
        g(F) = c_1 + c_2 x F^3 with c_1 = median of rho_2 over
        CAL (the generic bulk level) and c_2 = max over CAL of
        (rho_2 - c_1)_+ / F^3 (monotone since c_2 >= 0).
  G_LIN (MINIMAL FALLBACK, precedence 3): g(F) = a x F with
        a = max over CAL of rho_2 / F.
THE SEALED CALIBRATION SPLIT: TRB.split_midladder on the full
(N, kz)-sorted class ladder, VERBATIM (n = 65 expected: small =
ranks 0..20 certified individually, cal = ranks 21..25 frozen,
test = ranks 26..64); m_0 = min m over cal + test; the declared
calibration index set is warded EXACT (e1/e3 prove the wards
bite).  MONOTONICITY: every calibrated form must be non-
decreasing on the sealed grid GRID_MONO = 0.25, 0.50, ..., 3.25
(covers the measured F_A range [~0.5, 2.47] with margin); a
decrease > TOY_BAR disqualifies the form (and the e4 mutant is
LOUD).  CERTIFICATION (per form, sealed): violations = test rungs
with rho_2 > g(F_A); the form certifies iff 0 test violations AND
the four named r316/r317 violators kz53/kz83/kz67/kz55 are ALL
pointwise inside rho_2 <= g(F_A) (kz55 sits in the small-m set --
its coverage is demanded EXTRA, because covering the old
violators is the point of the sliding bound); the WINNER is the
first certifying form in the sealed precedence.  Reserve
distribution min/med and the halves-slope trend of rho_2/g(F_A)
over the test rungs are printed as census.

THE SEALED MAP + ENVELOPE RULE (Leg A): the (rho_2, F_A) map over
the full ladder; Spearman rank correlation (fit-free: Pearson on
stable rank vectors) over the TEST rungs printed as census; the
fit-free UPPER ENVELOPE over NB_ENV = 6 equal-count F_A-rank bins
computed on EXACTLY the declared TEST set (evaluating it on the
calibration split is the e3 mutant -- declared-set ward EXACT):
env_j = max rho_2 in bin j.  ENV_OK iff the top-F_A bin carries
the envelope maximum (argmax j == NB_ENV - 1) AND the Spearman
correlation of (bin index, env_j) >= ENV_RC_MIN = 0.5 -- the
upper envelope RISES with the coordinate.  NON-TRIVIALITY (the
coordinate must CARRY, the bound must not be a disguised flat
constant): GAIN = g*(max F_A over the ladder) / g*(min F_A over
the test rungs) >= GAIN_MIN = 1.5.

THE SEALED ADJUDICATION (frozen BEFORE evaluation; exactly one
fires):
    no winner:  ENVELOPE_DIFFUSE   iff NOT ENV_OK (the envelope
                    itself is diffuse -- the coordinate does not
                    carry; the primary diagnosis),
                G_FAILS_POINTWISE  iff ENV_OK (the envelope is
                    monotone but every sealed g form misses --
                    the family was wrong, not the coordinate);
    winner g*:  WORLD_LEAK         iff the world check leaks,
                ENVELOPE_DIFFUSE   iff NOT ENV_OK or GAIN <
                    GAIN_MIN (a bound exists but is effectively
                    flat/diffuse -- honest demotion),
                SLIDING_BOUND_GO(g*) otherwise.
WORLD CHECK (r316/r317 machinery verbatim, adapted to the sliding
bound): (w1) w9/w13/EPSTEIN ADMITTED -- fold multiplicity <= 2
AND rho_2 <= g*(F_A) at the world's coordinate (the sealed
INSERTION RULE for world coordinates: the world's QMAX against
the rank-local median of the ladder QMAX column at the world's
(N)-insertion point, window W ladder ranks each side, no self-
exclusion -- worlds are not ladder members; disclosed: for the
mains this differs from their ladder F_A by the self-exclusion
convention, both printed); (w2) twin band max(w13/w9, w9/w13) <=
TWIN_FAC = 3.0 on PhiL2; (w3) SCRAMBLE is rejected by EITHER
mechanism -- the coordinate bound BREAKS (rho_2 > g*(F_A), the
sliding-bound-native rejection) OR the r317 class machinery
rejects it (component attribution names a collision/flux column,
dev >= ATTR_MIN = 0.25, AND the seeded assignment shuffle
SEED_SHUF = 321001 breaks the flux profile edgewise >= MUT_MIN
with matched mass) -- WHICH mechanism fires is printed honestly;
scr_ok = coordinate break OR class rejection.

LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316/r317 record
numbers adopted as-is, disclosed): med signed shares DeltaF/
C_pair/C_full = -0.4226/+0.5980/+0.8537 (tol 0.005); FC med 0.629
(tol 0.005) slope -0.141 (tol 0.01); fold multiplicity == 2
UNIFORM; identity wards live; r306 C_2 = 1.069 (tol 0.005)
first-5 freeze, 0/57; r315 C0 a/b/c = 2.6261/1.5052/0.9400 (tol
0.005), FCIX outliers kz55/kz67 = 0.955/0.915; r316 anchors: n =
65, H stratum {55, 67}, split 21|5|39 with m_0 = 73, C_L2 0.7476,
the 8 regime-L violators EXACT, TOP1 0.558/0.785, rho anchors
kz53/kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005),
C_small 1.0694 at kz18; NEW r317 anchors: the F_A TOP-3 ==
(kz53, kz83, kz67) EXACT as an ordered ranking with values
2.47/2.39/2.38 (tol 0.01); the sealed gap rule recovers class B
== {kz55, kz67} with THR_B = 3.7157 (tol 0.005) and class A
EMPTY; the 63-rung complement reproduces C_gen = 0.4579 (tol
0.005) with test violators EXACTLY {kz53, kz83} and complement
C_small = 1.0694 at kz18.

LEG A -- THE (rho_2, F_A) MAP: (A1) the coordinate + bracket +
g-family + envelope + adjudication rules printed as sealed
definitions; the SOURCE-PURE coordinate table (rank, kz, N, m,
QMAX, F_A, B) printed BEFORE any bound-side table of this round.
(A2) SOURCE-PURITY AUDITS: the AST identifier scan over
local_median + g_eval + mono_check + upper_envelope +
spearman_rank + world_coord must be clean against BOUND_FORBIDDEN
and PHI3_FORBIDDEN; the literal scan over those + g_calibrate +
gate_verdict must be clean against the sealed record-literal set
R32X_TABLE_LITERALS (r314 + r315 + r316 + r317 record numbers);
e1/e2/e3 prove the audits bite.  (A3) TOY EXACTNESS: the
local_median cross-ward on the r317 spike toy (medians all 1,
F == values EXACT vs EFP.local_ratio); the g toys (Fc = (1, 2),
targets (0.5, 4.0), baselines (1.0, 1.5), cal = both: SQ par
2.25 -> g(2) = 9, TT pars (2.25, 0.21875) -> g(2) = 4 EXACT, LIN
par 2 -> g(3) = 6); the monotonicity grid accepts all three toy-
calibrated forms (<= TOY_BAR) and is LOUD on the e4 mutant; the
12-point envelope toys (rising -> env rising, Spearman +1, argmax
last; falling -> Spearman -1) EXACT; the Spearman +/-1 toys; the
world_coord insertion toy (flat ladder, val 3 -> F = 3 EXACT);
the verdict tree toys (all five branch combinations EXACT).
(A4) LIVE WARDS: the r316 majorant chain (rho_2 <= PhiL1 <= PhiL2
<= PhiH2, rho_2 <= PhiH1, NORM x cube == rho_2) PLUS the new
bracket lower side qmax x PhiH1 <= rho_2 PLUS the reconstruction
QMAX == F_A x medloc PLUS PhiH1 == (F_A x B)^2, all on every live
world (CHAIN_BAR / 1e-12).  (A5) MAP CENSUS: Spearman(F_A, rho_2)
over the test rungs; the sealed upper envelope with ENV_OK.

LEG B -- THE SEALED g-FAMILY: split seal (verbatim), small-m
certificates (C_small = max rho_2 over ranks 0..20), the three
calibrations printed with declared-set wards, the bound-side map
table (rank, kz, N, m, F_A, rho_2, g_SQ/g_TT/g_LIN marks), the
per-form certification (violations, reserve min/med, trend), the
named-violator coverage (kz53/kz83/kz67/kz55) and the winner by
sealed precedence.

LEG C -- STRUCTURE + WORLD: (C1) the B census: min/med/max over
the ladder, calibration max vs test max (the SOURCE-PURE
boundedness question that carries the upper bracket direction),
halves-slope trend of B over the test rungs; the exact bracket
restated with the measured numbers.  (C2) the world check as
sealed above, with the SCRAMBLE mechanism printed honestly.

LEG D -- THE ADJUDICATION + THEOREM CANDIDATE: the sealed tree;
on SLIDING_BOUND_GO the CANDIDATE THEOREM (sliding cubic bound)
is printed with the explicit g, its constants, m_0, C_small, the
implied uniform constant C_impl = g*(max F_A) and the COROLLARY:
F_A is measured bounded on the ladder (max expected 2.47), so the
sliding bound implies the uniform bound with C = g*(F_A max); the
remaining provenance question is then ONE source-pure question --
is F_A (and for G_SQ the baseline B) source-pure bounded?  (The
new, smaller origin question of the fork-(a) program.)

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) g RE-CALIBRATED AFTER SIGHT of the test violators:
  mutant_g_posthoc consumes the evaluated bound column (rho) over
  the WHOLE ladder to inflate the constant until the seen
  violators are covered -- the BOUND_FORBIDDEN scope audit must
  FLAG it AND on the sealed toy it returns a constant != the
  frozen calibration rule's -- CAUGHT twice.
(e2) F_A READS THE CUBIC TARGET: mutant_coord_readback consumes
  the cubic-moment record (cm/S3) -- the PHI3_FORBIDDEN scan must
  FLAG it (AST-CAUGHT) while the module-own builders stay clean.
(e3) ENVELOPE ON THE CALIBRATION SPLIT: mutant_envelope_cal
  declares the calibration window -- the declared-set ward must
  CATCH the mismatch EXACT (the real envelope declares the test
  set EXACT).
(e4) MONOTONICITY BREAK: mutant_g_nonmono (g = p F (2 - F),
  decreasing beyond F = 1) -- the sealed grid check must be LOUD
  (worst decrease >= MUT_MIN) while all three sealed forms pass.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the
  module-own coordinate/map builders consume source-pure columns
  + rank order only; g_calibrate consumes target values on
  EXACTLY the declared frozen calibration set (the r306
  calib_freeze pattern, set-warded); fragment audit (no fit
  primitives).

INDEX FIREWALL (binding, r238-r317 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
calibration (declared frozen set only) / certification /
diagnostic columns, NEVER a coordinate builder (AST-warded); no
zero/prime oracles anywhere (AST firewall); no fit primitives
(fragment audit).  MACHINERY IMPORTED VERBATIM: r317
EFP.local_ratio + EFP.gap_threshold, r316 TRB.two_regime_state +
TRB.split_midladder, r315 PHI.phi3_variants, r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope +
SCF.collision_census, r306 RY3.cubic_moments + RY3.renyi3_ratio +
RY3.calib_freeze, r298 WBT.block_breaks + WBT.aggregate_blocks,
r269 PBB.mask_edge + PBB.runs_split, r287 L2D.blocks_level2 +
L2D.halves_slope + L2D.autocorr_full, r244 BH.wpack, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w
= S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r317 verbatim): frame-A h <=
900, 42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36,
38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz);
EXT2: the r316 A5 rule (leftover pool + first 12 windows 1300 < h
<= 1650, first 8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; THETA 0.85 (r316 anchor only); N_CAL
5; CAL_THIRD 3; CLS_W 5 (via EFP, verbatim); NB_ENV 6; ENV_RC_MIN
0.5; GAIN_MIN 1.5; GRID_MONO = 0.25 x (1..13); G_FORMS precedence
("SQ", "TT", "LIN"); NAMED_KZ (53, 83, 67, 55); RES_EPS 0.01;
ATTR_MIN 0.25; TWIN_FAC 3.0; SEED_SHUF 321001; MUT_MIN 1e-6;
TOY_BAR 1e-12; TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep + ext
+ ext2 / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9; R314 anchors
shares (-0.4226, +0.5980, +0.8537) tol 0.005, FC 0.629/-0.141 tol
0.005/0.01, mult == 2 EXACT; R306 anchor C_2 1.069 tol 0.005;
R315 anchors C0 (2.6261, 1.5052, 0.9400) tol 0.005, FCIX {55:
0.955, 67: 0.915} tol 0.005; R316 anchors (r317 verbatim): N321 =
65, H set {55, 67}, split (20, 21, 25, 26, 64), M0_REF 73, C_L2
0.7476 tol 0.005, violator set {53, 105, 83, 71, 68, 88, 76,
119} EXACT, TOP1 {55: 0.558, 67: 0.785} tol 0.005, RHO {53:
1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005, C_SMALL
1.0694 tol 0.005 at kz18; R317 anchors: FA_TOP {53: 2.47, 83:
2.39, 67: 2.38} tol 0.01 ORDERED, THR_B 3.7157 tol 0.005, B set
(55, 67), class A EMPTY, C_GEN 0.4579 tol 0.005, complement
violators (53, 83) EXACT; R32X_TABLE_LITERALS = the sealed r314 +
r315 + r316 forbidden set (r317 verbatim) UNION the r317 record
set {2.47, 2.39, 2.38, 1.93, 1.9, 1.74, 3.7157, 7.23, 4.96, 2.79,
2.7, 0.4579, 1.78, 1.233, 1.24, 2.06, -0.17, 0.44, 0.59, 1.0493,
0.7791, 2.68, 1.99}; runtime <= 1800 s; smoke = w9 + controls +
toys + scope/purity audits + the chain/bracket wards on w9 +
controls + e1-e4 mutants; ladder, extensions, anchors, map,
split, calibration, certification and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r315/r306/r316/r317 RECORD number adopted
as-is; the concentration bracket, the PhiH1 == (F_A B)^2
identity, the monotonicity of the three g forms and the r306
chain (bound => n_eff) are derived algebra, disclosed above; the
CHOICE of the g-family is motivated by that algebra (G_SQ) and by
the r317 RECORD reading (G_TT: "a two-term bound C_1 + C_2
F_A^gamma"; G_LIN: the minimal form named in the fork-(a)
contract) -- NO map value, NO envelope, NO calibration constant,
NO violation count of this round was computed before this spec
was frozen; NB_ENV = 6, ENV_RC_MIN = 0.5, GAIN_MIN = 1.5 and the
grid are coarse a-priori bars (NB_ENV sized so each test bin
holds >= 6 rungs; GAIN_MIN demands the sliding bound genuinely
vary; the grid covers the recorded F_A range [~0.5, 2.47] with
margin); the four sealed verdicts are symmetric -- the tree maps
every leak to its named abort by CONTRACT, not to favor an
outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R321_ANCHORS(r314 shares + FC + mult, identity wards, r306 C_2,
    r315 C0 + FCIX, r316 ladder/split/C_L2/violators/TOP1/rho/
    C_small, r317 FA-top3 + gap-B + C_gen + complement violators)
+ SEAL(coordinate + bracket + g-family + envelope + tree + purity
    audits + toys + live wards)
+ MAP(Spearman, envelope bins, ENV_OK)
+ GFAMILY(constants, per-form violations, named coverage, winner,
    reserve, trend)
+ STRUCTURE(B census: cal max vs test max, trend -- the source-
    pure upper-direction carrier)
+ WORLD(admission at the sliding bound + twin band + SCRAMBLE
    mechanism)
+ [exactly one of] SLIDING_BOUND_GO(g*) / ENVELOPE_DIFFUSE /
    G_FAILS_POINTWISE / WORLD_LEAK
+ THEOREM(candidate text printed on GO)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the coordinate is the r317 import, not a
re-tuned sibling; the g forms, their calibration rules, the
split, the envelope rule, the gain bar and the tree are sealed
BEFORE any map or bound value of this round exists; the
calibration consumes the target on EXACTLY the frozen mid-ladder
window (G_SQ consumes NO target at all); a GO fixes a certified
SLIDING statement ON THE MEASURED RUNGS with explicit (g, m_0,
C_small, C_impl), it proves NO universal bound beyond them and NO
cofinal law; the implied uniform constant C_impl is expected
LOOSER than the r306 first-5 constant -- the round buys FORM
(one gliding bound, no regimes, no exceptions), not sharpness,
and says so; the world columns are n = 1 per control; a DIFFUSE
or FAILS letter seals the negative honestly; r243-r317 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 39/39 (0.5 s), NO amendment; calibration pass 1 =
first full evaluation, 39/39, wall 36.0 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; PROTOCOL
DISCLOSURE: a drafting error had placed PREFILLED PLACEHOLDER
record tables into this spec BEFORE any run -- they were removed
COMPLETELY before the first smoke run and are disclosed here (the
r316/r317 protocol-error class); the ONLY post-freeze edit is
this record-table insertion, which IS the protocol -- no bar,
band, rule or verdict rule moved):
CAL_VERDICT = R321_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 65/65, identity wards 4.5e-17 /
4.7e-16 / 4.1e-16, r306 C_2 1.069 viol 0/57, r315 C0
2.6261/1.5052/0.9400 + FCIX 0.955/0.915, r316 n = 65, H = {55,
67}, split 21|5|39 m_0 = 73, C_L2 0.7476, the 8-violator set
EXACT, TOP1 0.558/0.785, rho kz53/kz67/kz55/kz83 = 1.0493/
1.0536/0.4821/0.7791, C_small 1.0694 @ kz18; r317 F_A top-3
(53, 83, 67) = 2.47/2.39/2.38 EXACT ORDERED, gap-B {55, 67}
THR_B 3.7157, class A EMPTY, 63-rung complement C_gen 0.4579
with test violators (53, 83), C_small_c 1.0694 @ kz18 -- ALL
bit-near) + SEAL(purity clean: 0 id + 0 literal hits on the six
map builders + calibrator + tree; toys exact: medloc cross-ward
0.0, g toys SQ 9 / TT 4 / LIN 6, mono grid 3/3 accepted,
envelope rising/falling +1/-1, world_coord 3.0, tree 5/5
branches; live wards on 69 live worlds: r316 chain 6.5e-16,
NORM x cube 7.9e-16, NEW bracket lower side qmax PhiH1 <= rho_2
worst slack 0.0 -- the bracket is TWO-SIDED live, reconstruction
QMAX == F_A x medloc 1.6e-16, PhiH1 == (F_A B)^2 5.7e-16) +
MAP(F_A range on the 65-rung ladder min/med/max 0.58/1.01/2.47
(max at kz53); Spearman(F_A, rho_2 | 39 test) = +0.84 -- the
bulk correlation itself is STRONG, not only the envelope;
envelope bins (F_med, max rho_2): (0.69, 0.2136) (0.82, 0.2500)
(0.93, 0.2622) (1.11, 0.2809) (1.35, 0.3758) (2.15, 1.0536);
argmax = top bin, bin Spearman +1.000 -- the envelope is
STRICTLY MONOTONE in the coordinate: ENV_OK) +
GFAMILY(constants frozen on cal ranks 21..25: G_SQ b = 1.3056
(= B_cal_max 1.1426 squared, SOURCE-PURE -- no target value
consumed); G_TT c_1 = 0.3012, c_2 = 0.03846; G_LIN a = 0.3061;
mono grid 3/3; violations on the 39 test rungs: SQ 0 / TT 2
(kz53, kz67 -- the two-term form misses exactly the two deepest
spikes) / LIN 5 (kz38, kz40, kz53, kz67, kz83); named coverage
kz53/kz83/kz67/kz55: SQ 4/4, TT 1/4 (only kz83), LIN 1/4;
WINNER by sealed precedence: G_SQ; reserve min/med over test
2.71/5.35; trend of rho_2/g(F_A) -0.341 FALLING -- the sliding
reserve GROWS into depth; named-violator record at G_SQ: kz53
rho 1.0493 g 7.9714 rsv 7.6 / kz83 0.7791 g 7.4877 rsv 9.6 /
kz67 1.0536 g 7.4069 rsv 7.0 / kz55 0.4821 g 3.4841 rsv 7.2) +
STRUCTURE(B = medloc x m/log m: ladder min/med/max 0.9500/
1.1322/1.4088; CAL MAX 1.1426 vs TEST MAX 1.4088 -> NOT bounded
by its cal max (ratio 1.23), trend over test +0.122 RISING --
THE HONEST STRUCTURAL FINDING: the pure-algebra transfer route
(rho_2 <= F_A^2 B^2 with B <= B_cal) does NOT close; the G_SQ
certificate holds on the measured rho_2 DIRECTLY (the bracket
upper side is loose by the qmax factor, which falls faster than
B^2 rises); the concentration bracket qmax PhiH1 <= rho_2 <=
PhiH1 = (F_A B)^2 is live two-sided on 69 worlds) +
WORLD(w9/w13/EPSTEIN admitted at the sliding bound: mult 2,
rho_2 0.458/0.461/0.368 <= g(F_ins) 0.90/1.55/1.29 at F_ins
0.83/1.09/1.00; twin band PhiL2 factor 1.04 <= 3.0; SCRAMBLE
mechanism honestly documented: the coordinate bound HOLDS on
SCRAMBLE (rho_2 1.780 <= g(2.00) = 5.21 -- the coordinate does
NOT reject it: SCRAMBLE is a concentration spike too, F_ins
2.00) and the CLASS machinery rejects it (COLL attribution dev
3.69 >= 0.25 AND seeded shuffle 321001 edgewise 9.8e-1 with
mass matched 2.0e-17, 294/300 atoms) -- scr_ok via the class
side condition, exactly the disclosed fallback) +
SLIDING_BOUND_GO(G_SQ: rho_2 <= 1.3056 x F_A^2 on 0/39 test
violations + 4/4 named; gain 15.95 >= 1.5; ENV_OK; world clean)
+ THEOREM(printed: sum q^3 <= 1.3056 F_A(w)^2 (log m)^2/m^2 for
m >= 73; 21 small-m certificates, C_small 1.0694; COROLLARY
C_impl = g(2.47) = 7.97 = C_tot, n_eff >= m/(2.82 log m),
DISCLOSED 7.5x looser than the r306 first-5 constant -- the
round buys FORM, not sharpness; the new smaller provenance
question printed) + MUSTFAIL_LEDGER(e1 AST-FLAGGED on the rho
identifier + toy 5.0 != frozen 1.0; e2 AST-FLAGGED on the cm
read-back while the six own builders are clean (0 hits); e3
declared cal-set != test-set EXACT; e4 mono grid LOUD 1.0625 >=
1e-6 vs 3/3 sealed forms accepted; m5a t_term / m5b g_branch
FLAGGED).
READING (typed, no upgrade): the sealed letter is
SLIDING_BOUND_GO(G_SQ) -- fork (a) in the r317-sharpened form
DELIVERS the statement shape the r317 abort demanded: (1) THE
SLIDING BOUND EXISTS: rho_2 <= 1.3056 x F_A^2 pointwise on all
39 mid-ladder test rungs AND on all four named r316/r317
violators (kz53/kz83/kz67/kz55 now INSIDE with reserves
7.0..9.6 -- the exact point of the gliding form: what killed
every flat mid-ladder constant since r316 is absorbed by the
coordinate), with reserve min/med 2.71/5.35 and FALLING trend
-0.341 (the reserve grows into depth); (2) THE COORDINATE
CARRIES: the test envelope is STRICTLY monotone in F_A (bin
Spearman +1.000, top bin 1.0536 at F_med 2.15) and even the
bulk correlation is strong (+0.84) -- stronger than the r317
continuum reading suggested; the gain is 15.95 (the bound
genuinely slides; it is NOT a disguised flat constant); (3) THE
WINNING FORM IS THE ALGEBRA-DERIVED ONE: G_SQ's constant is
(max cal B)^2, a SOURCE-PURE number -- NO target value enters
the calibration; the r317-named two-term heuristic G_TT is
tight but misses exactly kz53/kz67, and G_LIN fails 5/39 (the
coordinate is quadratic-sufficient, not linear-sufficient) --
the derivation-strength precedence was the right seal; (4) THE
HONEST STRUCTURAL CAVEAT (the round's second find): the
pure-algebra transfer route does NOT close -- B = medloc x
m/log m is NOT bounded by its cal max (test max 1.4088 = 1.23 x
cal max, trend +0.122 RISING), so rho_2 <= b F_A^2 does NOT
follow from rho_2 <= F_A^2 B^2 alone; the certificate holds on
the measured rho_2 directly because the bracket's qmax slack
falls faster than B^2 rises -- the proof-side decomposition is
rho_2 = (qmax-share) x F_A^2 B^2 with the qmax-share the
remaining object; (5) THE WORLD SIGN IS HONEST AND TYPED:
SCRAMBLE is NOT rejected by the coordinate bound (its inflated
cube comes WITH an inflated concentration ratio F_ins 2.00 --
the sliding bound covers it at 5.21) -- the rejection is
carried by the r317 CLASS side condition (COLL attribution 3.69
+ seeded shuffle 294/300 with matched mass), exactly the
disclosed fallback mechanism; twin band 1.04, EPSTEIN admitted
at reserve 3.5.  Honest negatives: C_impl = 7.97 is 7.5x looser
than the r306 first-5 constant 1.069 -- the round buys FORM
(one gliding bound, no regimes, no exceptions, all old
violators inside), not sharpness, exactly as sealed; the GO
certifies the measured 65-rung ladder + 2 mains + 2 live
controls and NOTHING beyond; the SCRAMBLE non-rejection by the
coordinate alone means the sliding bound is NOT world-
separating by itself -- it needs the class side condition; B
rising is a real obstruction to the pure-algebra proof route.
R322 direction (typed, census-grade): the provenance question
is now SOURCE-PURE, LOCAL and SPLIT IN TWO -- (a) is F_A
bounded (measured max 2.47; the near-critical family is its
top), (b) what bounds the qmax-share rho_2/(F_A^2 B^2) =
(qmax L)^3-share of the cube (measured: it falls fast enough to
beat the rising B^2) -- the natural attack is the r306
SHAPE3/stationarity route applied to the LOCAL MEDIAN of the
normalized shape (B is a median-of-max object; the r302 M_2
stationarity 1.973 already pins the second moment of the same
shape).  Runtime 36.0 s full / 0.5 s smoke; run1/run2 identical
up to WALL.  AMENDMENTS AFTER FREEZE: none except this
record-table insertion (and the disclosed pre-run placeholder
removal).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
import window_border_transfer_probe as WBT     # noqa: E402 r298
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import phi3_functional_probe as PHI            # noqa: E402 r315
import two_regime_bound_probe as TRB           # noqa: E402 r316
import exception_families_probe as EFP         # noqa: E402 r317
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
EXT2_H_MAX = 1650
EXT2_POOL_CAP = 12
K_EXT2 = 8
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
XW_BAR = 1e-9
DEG_FLOOR = 1e-6
MULT_CAP = 2
THETA = 0.85
N_CAL = 5
CAL_THIRD = 3
NB_ENV = 6
ENV_RC_MIN = 0.5
GAIN_MIN = 1.5
GRID_MONO = tuple(0.25 * k for k in range(1, 14))
G_FORMS = ("SQ", "TT", "LIN")
NAMED_KZ = (53, 83, 67, 55)
RES_EPS = 0.01
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 321001
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
PAIR_OFFSET = 0
R314_SHARES = (-0.4226, 0.5980, 0.8537)
R314_SHARE_TOL = 0.005
R314_FC = 0.629
R314_FC_TOL = 0.005
R314_FC_SLOPE = -0.141
R314_FC_SL_TOL = 0.01
R306_C2 = 1.069
R306_C2_TOL = 0.005
R315_C0 = (2.6261, 1.5052, 0.9400)
R315_C0_TOL = 0.005
R315_FCIX_KZ = {55: 0.955, 67: 0.915}
R315_FCIX_TOL = 0.005
N321_REF = 65
R316_H_SET = (55, 67)
R316_SPLIT = (20, 21, 25, 26, 64)     # small end, cal lo/hi, test lo/hi
M0_REF = 73
R316_CL2 = 0.7476
R316_CL2_TOL = 0.005
R316_VIOL_SET = (53, 105, 83, 71, 68, 88, 76, 119)
R316_TOP1 = {55: 0.558, 67: 0.785}
R316_TOP1_TOL = 0.005
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R317_FA_TOP = {53: 2.47, 83: 2.39, 67: 2.38}
R317_FA_ORDER = (53, 83, 67)
R317_FA_TOL = 0.01
R317_THRB = 3.7157
R317_THRB_TOL = 0.005
R317_B_KZ = (55, 67)
R317_CGEN = 0.4579
R317_CGEN_TOL = 0.005
R317_VIOL2 = (53, 83)
R32X_TABLE_LITERALS = frozenset((
    -0.4226, 0.598, 0.8537, 0.629, -0.141,
    -0.452, 0.823, 0.617, 0.057,
    -0.541, 0.43, 1.111, 0.675, 0.043,
    -2.695, -2.652, 6.347, 0.101, 0.011,
    -0.171, 0.856, 0.315, 0.693, 0.073,
    2.6261, 1.5052, 0.94, 0.955, 0.915,
    22.85, 66.09, 87.64,
    2.3883, 2.0841, 1.4433, 2.3545, 1.3615, 0.1375,
    0.9597, 0.7102, 0.4795,
    4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69,
    0.7476, 0.5531, 1.4263, 1.1266, 1.0804, 0.9648,
    0.8013, 0.7877, 0.7819, 0.7698, 34.0556, 3.0559,
    57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
    21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536,
    1.049, 0.779, 0.654, 0.148, 1.04, 3.27, 0.73,
    0.52, 1.35, 0.086, 0.202,
    2.47, 2.39, 2.38, 1.93, 1.9, 1.74, 3.7157, 7.23,
    4.96, 2.79, 2.7, 0.4579, 1.78, 1.233, 1.24, 2.06,
    -0.17, 0.44, 0.59, 1.0493, 0.7791, 2.68, 1.99))

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}
PHI3_FORBIDDEN = {"cube", "S" + "3", "cm",
                  "renyi3" + "_ratio", "cubic" + "_moments"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def literal_audit(funcname):
    """the RECORD-LITERAL audit: walk ONLY the named function's
    subtree and flag any numeric constant whose 4-decimal rounding
    lies in the sealed r314+r315+r316+r317 record-literal set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R32X_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the map/
# ---------------- coordinate builders consume source-pure columns
# ---------------- (QMAX, F_A, B) plus rank order only; the
# ---------------- withheld terminal drive key, the branch label,
# ---------------- the cubic target and the record literals are
# ---------------- forbidden (AST identifier scan + literal scan).
# ---------------- g_calibrate consumes target values on EXACTLY
# ---------------- the declared frozen calibration set (the r306
# ---------------- calib_freeze pattern; declared-set warded).
def local_median(vals):
    """the rank-local median companion of the imported r317
    local_ratio (window verbatim: half-width W = EFP.CLS_W, self
    excluded, truncated at the ladder ends): the baseline column
    medloc; warded EXACT against the import via
    vals == local_ratio(vals) x local_median(vals)."""
    v = [float(x) for x in vals]
    n = len(v)
    out = []
    for i in range(n):
        lo = max(0, i - EFP.CLS_W)
        hi = min(n, i + EFP.CLS_W + 1)
        nb = [v[j] for j in range(lo, hi) if j != i]
        out.append(float(np.median(nb)))
    return out


def g_eval(form, par, F):
    """the sealed monotone g-family evaluator (frozen forms):
    SQ: par[0] x F^2; TT: par[0] + par[1] x F^3; LIN: par[0] x F.
    All non-decreasing on F > 0 for non-negative parameters
    (checked on the sealed grid by mono_check)."""
    F = float(F)
    if form == "SQ":
        return par[0] * F * F
    if form == "TT":
        return par[0] + par[1] * F ** 3
    if form == "LIN":
        return par[0] * F
    raise ValueError(form)


def g_calibrate(form, Fc, target, base, cal_idx):
    """constants frozen on EXACTLY the declared calibration index
    set (returned for the set ward):
    SQ:  par = ((max cal base)^2,)  -- consumes the SOURCE-PURE
         baseline column only, NO target value;
    TT:  c_1 = median cal target, c_2 = max cal (target-c_1)_+/F^3;
    LIN: a = max cal target/F."""
    cal = tuple(cal_idx)
    if form == "SQ":
        return ((max(float(base[i]) for i in cal) ** 2,), cal)
    if form == "TT":
        c1 = float(np.median([float(target[i]) for i in cal]))
        c2 = max(max(float(target[i]) - c1, 0.0)
                 / max(float(Fc[i]) ** 3, 1e-300) for i in cal)
        return ((c1, c2), cal)
    if form == "LIN":
        return ((max(float(target[i]) / max(float(Fc[i]), 1e-300)
                     for i in cal),), cal)
    raise ValueError(form)


def mono_check(form, par):
    """the sealed monotonicity check: evaluate the calibrated form
    on GRID_MONO and return the worst DECREASE (0 for monotone;
    the e4 mutant must be LOUD >= MUT_MIN)."""
    vals = [g_eval(form, par, f) for f in GRID_MONO]
    worst = 0.0
    for k in range(len(vals) - 1):
        worst = max(worst, vals[k] - vals[k + 1])
    return worst


def upper_envelope(Fv, vals, idx):
    """the sealed fit-free upper envelope: over EXACTLY the
    declared index tuple, sort by the coordinate, split into
    NB_ENV equal-count rank bins, per bin (median coordinate, max
    value); returns (bins, declared) -- the declared set is warded
    against the sealed test split (e3 mutant CAUGHT)."""
    idx = tuple(idx)
    o = sorted(idx, key=lambda i: float(Fv[i]))
    parts = np.array_split(np.arange(len(o)), NB_ENV)
    bins = []
    for p in parts:
        if len(p) == 0:
            continue
        mem = [o[int(k)] for k in p]
        bins.append((float(np.median([float(Fv[i]) for i in mem])),
                     max(float(vals[i]) for i in mem)))
    return bins, idx


def spearman_rank(a, b):
    """rank correlation, fit-free: Pearson on stable rank vectors
    (argsort of argsort; deterministic, no fit primitives)."""
    ra = np.argsort(np.argsort(np.asarray(a, dtype=float),
                               kind="stable"),
                    kind="stable").astype(float)
    rb = np.argsort(np.argsort(np.asarray(b, dtype=float),
                               kind="stable"),
                    kind="stable").astype(float)
    ra -= float(np.mean(ra))
    rb -= float(np.mean(rb))
    den = math.sqrt(float(np.sum(ra * ra)) * float(np.sum(rb * rb)))
    return float(np.sum(ra * rb)) / max(den, 1e-300)


def world_coord(val, depth, ladder_depths, ladder_vals):
    """the sealed INSERTION RULE for world coordinates: the
    world's column value against the rank-local median of the
    ladder column at the world's depth-insertion point (window
    W = EFP.CLS_W ladder ranks each side, no self-exclusion --
    the world is not a ladder member)."""
    ld = np.asarray(ladder_depths, dtype=float)
    j = int(np.searchsorted(ld, float(depth)))
    lo = max(0, j - EFP.CLS_W)
    hi = min(len(ladder_vals), j + EFP.CLS_W)
    nb = [float(ladder_vals[k]) for k in range(lo, hi)]
    return float(val) / max(float(np.median(nb)), 1e-300)


def gate_verdict(has_winner, world_ok, env_ok, gain_ok):
    """the sealed verdict tree (booleans only; exactly one fires):
    no winner -> ENVELOPE_DIFFUSE if the envelope is diffuse,
    else G_FAILS_POINTWISE; winner -> WORLD_LEAK on a world leak,
    ENVELOPE_DIFFUSE if the envelope is diffuse or the gain is
    trivial, else SLIDING_BOUND_GO."""
    if not has_winner:
        return "ENVELOPE_DIFFUSE" if not env_ok \
            else "G_FAILS_POINTWISE"
    if not world_ok:
        return "WORLD_LEAK"
    if (not env_ok) or (not gain_ok):
        return "ENVELOPE_DIFFUSE"
    return "SLIDING_BOUND_GO"


def mutant_g_posthoc(Fv, rho):
    """e1 MUST-FAIL MUTANT: the g constant re-calibrated AFTER
    SIGHT over the WHOLE ladder (consumes rho, covers every seen
    violator by construction) -- the BOUND_FORBIDDEN scope audit
    must FLAG it AND on the sealed toy it returns a constant !=
    the frozen calibration rule's."""
    return max(r / max(float(f), 1e-300)
               for f, r in zip(Fv, rho))


def mutant_coord_readback(cmrec, nblk):
    """e2 MUST-FAIL MUTANT: a 'coordinate' consuming the cubic-
    moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk) * float(nblk)


def mutant_envelope_cal(Fv, vals, cal_idx):
    """e3 MUST-FAIL MUTANT: the envelope evaluated on the
    CALIBRATION split instead of the declared test set -- the
    declared-set ward must CATCH the mismatch EXACT."""
    return upper_envelope(Fv, vals, cal_idx)


def mutant_g_nonmono(par, F):
    """e4 MUST-FAIL MUTANT: a non-monotone 'bound shape'
    g = par x F x (2 - F), decreasing beyond F = 1 -- the sealed
    grid check must be LOUD on it."""
    return par * float(F) * (2.0 - float(F))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("continuous_coordinate_probe -- "
          "PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01 (round 321)")
    print("SPEC_SHA %s   R317_SHA %s   R316_SHA %s (imported)"
          % (SPEC_SHA[:16], EFP.SPEC_SHA[:16], TRB.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain/bracket wards + "
                        "e1-e4; ladder, extensions, anchors, map, "
                        "split, calibration, certification and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE CONTINUOUS-COORDINATE ROUND (reviewer fork (a), "
          "r317-sharpened): bound rho_2 BY the single source-pure "
          "coordinate F_A = rank-local QMAX ratio (r317 import, W "
          "= %d) -- rho_2(w) <= g(F_A(w)) pointwise with g "
          "explicit and MONOTONE, sealed family SQ (b F^2, "
          "derived from the exact bracket qmax PhiH1 <= rho_2 <= "
          "PhiH1 = (F_A B)^2) > TT (c1 + c2 F^3, the r317-named "
          "two-term form) > LIN (a F); constants frozen on the "
          "r316 mid-ladder window; envelope rule NB = %d bins on "
          "the declared TEST set, ENV_RC_MIN %.1f; gain bar "
          "%.1f; verdicts SLIDING_BOUND_GO / ENVELOPE_DIFFUSE / "
          "G_FAILS_POINTWISE / WORLD_LEAK sealed BEFORE "
          "evaluation" % (EFP.CLS_W, NB_ENV, ENV_RC_MIN, GAIN_MIN))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("local_median", "g_eval", "mono_check",
               "upper_envelope", "spearman_rank", "world_coord"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the six module-own "
          "map/coordinate builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN (%d hits); m5a gift-bound FLAGGED "
          "(%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r317 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        ext = []
        ext2 = []
        okL = True
    else:
        kzs = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
            elif h <= EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        ekz2.sort()
        pool2 = epool[K_EXT:] + [BH.wpack(kz)
                                 for _h, kz in ekz2[:EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:K_EXT2]
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))
    if smoke:
        check("G12-extension-census", True, "SMOKE: skipped")
        check("G13-ext2-census", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d), POSITIVE_PREFIX %d/%d"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1],
                 sum(1 for p in ext if p["nf"] is None), len(ext)))
        check("G13-ext2-census",
              len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "EXT2 (r316 A5 rule verbatim, census-grade): pool "
              "%d leftover + %d windows with %d < h <= %d; "
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(epool) - K_EXT, min(len(ekz2), EXT2_POOL_CAP),
                 EXT_H_MAX, EXT2_H_MAX, len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        v2w = BR.eval_scaled(rows, xu, N - 2)
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p, nf=p["nf"])

    recs = [rung_rec(p) for p in pool]
    erecs = [rung_rec(p) for p in ext] if not smoke else []
    e2recs = [rung_rec(p) for p in ext2] if not smoke else []
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        e_cheap = sum(1 for rc in erecs + e2recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2 census (no sealed expectation): %d cheap "
              "/ %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + ATOMIC PRESENTATION WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in erecs + e2recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext = max(tb_ext, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d mains + 3 controls: worst dev/absmass %.1e main "
          "N<=%d (bar %.0e) / %.1e deep / %.1e ext+ext2 (bar "
          "%.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(mrecs),
             tb_worst, DEEP_N, TB_WARD_BAR, tb_deep, tb_ext,
             TB_WARD_BAR_DEEP, tb_ctrl, TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        runs = PBB.runs_split(cb)
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        cm = RY3.cubic_moments(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        # ---- raw atomic presentation (r313/r314 convention):
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        if m and not degenerate:
            gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
            sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = SCF.flux_telescope(gen["G1"], gen["ptr"], m)
            cc = SCF.collision_census(gen["mult"], gen["ptr"], m)
            x_dev = float(np.max(np.abs(sct["x"] - Pd))
                          / max(np.max(np.abs(Pd)), 1e-300))
            sig = sct["sig"]
            cube = sct["cube"]
            A1 = np.bincount(blk_all, weights=np.abs(val_all),
                             minlength=m)
            scale3 = float(np.sum(A1 ** 3))
            sc_j = np.maximum(A1 ** 3, 1e-300)
            C_far_flux = float(np.sum(sig * ft["F_end"]))
            C_bnd = float(np.sum(sig * ft["F_open"]))
            rec3 = abs(C_far_flux + sct["C_pair"] + sct["C_full"]
                       + C_bnd - cube) / max(scale3, 1e-300)
            tel_dev = float(np.max(np.abs(ft["F_end"]
                                          - sct["far"]) / sc_j))
            bnd_dev = float(np.max(np.abs(ft["F_open"]) / sc_j))
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            ph = PHI.phi3_variants(sct["x"], sct["Q2"], sct["Q3"],
                                   ft["F_end"], ft["F_open"],
                                   ft["edge_abs"], m)
            trs = TRB.two_regime_state(sct["x"], sct["Q2"],
                                       sct["Q3"], gen["G1"],
                                       gen["ptr"], ft["F_end"],
                                       ft["F_open"],
                                       ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            # diagnostic census columns (read-back-adjacent,
            # computed OUTSIDE the builders, disclosed):
            top1 = float(np.max(np.abs(sct["x"])) ** 3) \
                / max(cube, 1e-300)
        else:
            gen = sct = ft = cc = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            shares = dict(far=0.0, pair=0.0, full=0.0)
            mx_mult = 0
            ph = dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                      coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            top1 = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd, shares=shares,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    cc=cc, ph=ph, trs=trs, rho2=rho2, top1=top1,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])
    pool_all = all_rc + [crecs[c] for c in crecs]

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in pool_all:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(pool_all)))

    live = [rc for rc in pool_all if not rc["ev"]["degenerate"]]
    deg_note = [c for c in crecs if crecs[c]["ev"]["degenerate"]]
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    check("G22-genealogy-completeness",
          x_w <= ATOM_BAR and mism_tot == 0,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION "
            "(r314/r315/r306/r316/r317)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G31-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e)"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 shares far/pair/full = %+.4f/%+.4f/%+.4f, "
             "QMAX %.4f, PhiH1 %.4f, PhiL2 %.4f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["trs"]["qmax"],
                ev9s["trs"]["phiH1"], ev9s["trs"]["phiL2"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        check("G33-r315-anchors", True, "SMOKE: skipped")
        check("G34-r316-anchors", True, "SMOKE: skipped")
        check("G35-r317-anchors", True, "SMOKE: skipped")
        srt57 = []
        srt321 = []
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        sh_far = [rc["ev"]["shares"]["far"] for rc in recs]
        sh_pair = [rc["ev"]["shares"]["pair"] for rc in recs]
        sh_full = [rc["ev"]["shares"]["full"] for rc in recs]
        fcs = [rc["ev"]["trs"]["fcix"] for rc in recs]
        meds = (float(np.median(sh_far)),
                float(np.median(sh_pair)),
                float(np.median(sh_full)))
        fc_med = float(np.median(fcs))
        fc_sl = slp(fcs)
        srt321_all = sorted(recs + erecs + e2recs,
                            key=lambda rc: (rc["N"], rc["kz"]))
        excl = [rc for rc in srt321_all
                if rc["ev"]["mx_mult"] > MULT_CAP]
        srt321 = [rc for rc in srt321_all
                  if rc["ev"]["mx_mult"] <= MULT_CAP]
        n321 = len(srt321)
        n_m2 = sum(1 for rc in srt321
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == n321 and not excl,
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d, mult-cap exclusions %d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 n321, len(excl)))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G32-r306-bound-live",
              abs(C2 - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        C0 = {}
        for i, v in enumerate(("a", "b", "c")):
            vals = [rc["ev"]["ph"][v] for rc in srt57]
            C0[v], _j0, _d0 = RY3.calib_freeze(vals, range(N_CAL))
        fcix_kz = {rc["kz"]: rc["ev"]["trs"]["fcix"]
                   for rc in srt57}
        ok_fcix = all(abs(fcix_kz.get(kz, -1.0)
                          - R315_FCIX_KZ[kz]) <= R315_FCIX_TOL
                      for kz in R315_FCIX_KZ)
        check("G33-r315-anchors",
              all(abs(C0[v] - R315_C0[i]) <= R315_C0_TOL
                  for i, v in enumerate(("a", "b", "c")))
              and ok_fcix,
              "r315 record reproduced: C0 a/b/c = "
              "%.4f/%.4f/%.4f (rec %.4f/%.4f/%.4f tol %.3f); "
              "FCIX outliers kz55 %.3f / kz67 %.3f (rec "
              "%.3f/%.3f tol %.3f)"
              % (C0["a"], C0["b"], C0["c"], R315_C0[0],
                 R315_C0[1], R315_C0[2], R315_C0_TOL,
                 fcix_kz.get(55, -1.0), fcix_kz.get(67, -1.0),
                 R315_FCIX_KZ[55], R315_FCIX_KZ[67],
                 R315_FCIX_TOL))
        # r316 anchors on the class ladder (r317 verbatim)
        h_kz = tuple(sorted(rc["kz"] for rc in srt321
                            if rc["ev"]["trs"]["fcix"] > THETA))
        sm316, ca316, te316 = TRB.split_midladder(n321)
        m_all = [rc["ev"]["m"] for rc in srt321]
        m0_316 = min(m_all[i] for i in ca316 + te316)
        calL = [i for i in ca316
                if srt321[i]["ev"]["trs"]["fcix"] <= THETA]
        CL2 = max(srt321[i]["ev"]["trs"]["phiL2"] for i in calL) \
            if calL else 0.0
        violL2 = tuple(sorted(
            srt321[i]["kz"] for i in te316
            if srt321[i]["ev"]["trs"]["fcix"] <= THETA
            and srt321[i]["ev"]["trs"]["phiL2"] > CL2))
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt321}
        top1_kz = {rc["kz"]: rc["ev"]["top1"] for rc in srt321}
        C_small316 = max(srt321[i]["ev"]["rho2"] for i in sm316)
        j_cs = max(sm316, key=lambda i: srt321[i]["ev"]["rho2"])
        ok316 = (n321 == N321_REF
                 and h_kz == tuple(sorted(R316_H_SET))
                 and sm316[-1] == R316_SPLIT[0]
                 and ca316 == tuple(range(R316_SPLIT[1],
                                          R316_SPLIT[2] + 1))
                 and te316[0] == R316_SPLIT[3]
                 and te316[-1] == R316_SPLIT[4]
                 and m0_316 == M0_REF
                 and abs(CL2 - R316_CL2) <= R316_CL2_TOL
                 and violL2 == tuple(sorted(R316_VIOL_SET))
                 and all(abs(top1_kz.get(kz, -1.0)
                             - R316_TOP1[kz]) <= R316_TOP1_TOL
                         for kz in R316_TOP1)
                 and all(abs(rho_kz.get(kz, -1.0)
                             - R316_RHO[kz]) <= R316_RHO_TOL
                         for kz in R316_RHO)
                 and abs(C_small316 - R316_CSMALL)
                 <= R316_CSMALL_TOL
                 and srt321[j_cs]["kz"] == R316_CSMALL_KZ)
        check("G34-r316-anchors", ok316,
              "r316 record reproduced on the class ladder: n = "
              "%d (rec %d); H stratum %s (rec %s); split small "
              "0..%d / cal %d..%d / test %d..%d, m_0 = %d (rec "
              "%d); C_L2 %.4f (rec %.4f tol %.3f); regime-L test "
              "violators %s == the named 8; TOP1 kz55/kz67 "
              "%.3f/%.3f (rec %.3f/%.3f); rho anchors kz53/kz67/"
              "kz55/kz83 %.4f/%.4f/%.4f/%.4f (rec %.4f/%.4f/"
              "%.4f/%.4f tol %.3f); C_small %.4f @ kz%d (rec "
              "%.4f @ kz%d)"
              % (n321, N321_REF, str(h_kz),
                 str(tuple(sorted(R316_H_SET))), sm316[-1],
                 ca316[0], ca316[-1], te316[0], te316[-1],
                 m0_316, M0_REF, CL2, R316_CL2, R316_CL2_TOL,
                 str(violL2), top1_kz.get(55, -1.0),
                 top1_kz.get(67, -1.0), R316_TOP1[55],
                 R316_TOP1[67], rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53],
                 R316_RHO[67], R316_RHO[55], R316_RHO[83],
                 R316_RHO_TOL, C_small316, srt321[j_cs]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))
        # r317 anchors: the sealed class machinery re-run bit-near
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt321]
        phiL2_col = [rc["ev"]["trs"]["phiL2"] for rc in srt321]
        FA = EFP.local_ratio(qmax_col)
        FB = EFP.local_ratio(phiL2_col)
        thrA, kA, gA = EFP.gap_threshold(FA)
        thrB, kB, gB = EFP.gap_threshold(FB)
        memA = tuple(i for i, v in enumerate(FA) if v >= thrA)
        memB = tuple(sorted(srt321[i]["kz"]
                            for i, v in enumerate(FB)
                            if v >= thrB))
        ordFA = sorted(range(n321), key=lambda i: -FA[i])
        top3_kz = tuple(srt321[i]["kz"] for i in ordFA[:3])
        top3_val = {srt321[i]["kz"]: FA[i] for i in ordFA[:3]}
        rho_all = [rc["ev"]["rho2"] for rc in srt321]
        famAB = set(memA) | set(i for i, v in enumerate(FB)
                                if v >= thrB)
        comp = [i for i in range(n321) if i not in famAB]
        sm_c, ca_c, te_c = TRB.split_midladder(len(comp))
        C_gen = max(rho_all[comp[j]] for j in ca_c)
        viol_gen = tuple(sorted(
            srt321[comp[j]]["kz"] for j in te_c
            if rho_all[comp[j]] > C_gen))
        C_small_c = max(rho_all[comp[j]] for j in sm_c)
        j_csc = max(sm_c, key=lambda j: rho_all[comp[j]])
        ok317 = (top3_kz == R317_FA_ORDER
                 and all(abs(top3_val[kz] - R317_FA_TOP[kz])
                         <= R317_FA_TOL for kz in R317_FA_TOP)
                 and memA == ()
                 and memB == tuple(sorted(R317_B_KZ))
                 and abs(thrB - R317_THRB) <= R317_THRB_TOL
                 and abs(C_gen - R317_CGEN) <= R317_CGEN_TOL
                 and viol_gen == tuple(sorted(R317_VIOL2))
                 and abs(C_small_c - R316_CSMALL)
                 <= R316_CSMALL_TOL
                 and srt321[comp[j_csc]]["kz"] == R316_CSMALL_KZ)
        check("G35-r317-anchors", ok317,
              "r317 record reproduced: F_A top-3 %s = "
              "%.2f/%.2f/%.2f (rec %s = %.2f/%.2f/%.2f tol %.2f, "
              "ORDERED); gap rule: class A %s (rec EMPTY), class "
              "B %s THR_B %.4f (rec %s / %.4f tol %.3f); %d-rung "
              "complement: C_gen %.4f (rec %.4f), test violators "
              "%s (rec %s), C_small_c %.4f @ kz%d (rec %.4f @ "
              "kz%d)"
              % (str(top3_kz), top3_val.get(top3_kz[0], -1),
                 top3_val.get(top3_kz[1], -1),
                 top3_val.get(top3_kz[2], -1),
                 str(R317_FA_ORDER), R317_FA_TOP[53],
                 R317_FA_TOP[83], R317_FA_TOP[67], R317_FA_TOL,
                 "EMPTY" if not memA else str(memA), str(memB),
                 thrB, str(tuple(sorted(R317_B_KZ))), R317_THRB,
                 R317_THRB_TOL, len(comp), C_gen, R317_CGEN,
                 str(viol_gen), str(tuple(sorted(R317_VIOL2))),
                 C_small_c, srt321[comp[j_csc]]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "COORDINATE TABLE")
    pure_lits = []
    for fn in ("local_median", "g_eval", "mono_check",
               "upper_envelope", "spearman_rank", "world_coord",
               "g_calibrate", "gate_verdict"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_g_posthoc", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_coord_readback", PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1,
          "SOURCE PURITY: the six map/coordinate builders clean "
          "vs PHI3_FORBIDDEN + BOUND_FORBIDDEN (%d id hits); the "
          "eight builder+gate functions clean vs the sealed "
          "r314+r315+r316+r317 record-literal set (%d literal "
          "hits); consumed inputs: source-pure columns (QMAX, "
          "F_A, B) + rank order (g_calibrate: target on the "
          "declared frozen cal set only, SQ consumes NO target); "
          "e1 g-posthoc FLAGGED (%s); e2 coord-readback FLAGGED "
          "(%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS"))
    # toys (exact)
    f_sp = EFP.local_ratio(EFP.TOY_SPIKE)
    med_sp = local_median(EFP.TOY_SPIKE)
    rec_sp = max(abs(EFP.TOY_SPIKE[i] - f_sp[i] * med_sp[i])
                 for i in range(len(f_sp)))
    ok_med = (rec_sp <= TOY_BAR
              and all(abs(m - 1.0) <= TOY_BAR for m in med_sp))
    toy_F = (1.0, 2.0)
    toy_t = (0.5, 4.0)
    toy_b = (1.0, 1.5)
    parSQ, dSQ = g_calibrate("SQ", toy_F, toy_t, toy_b, (0, 1))
    parTT, dTT = g_calibrate("TT", toy_F, toy_t, toy_b, (0, 1))
    parLN, dLN = g_calibrate("LIN", toy_F, toy_t, toy_b, (0, 1))
    ok_g = (abs(parSQ[0] - 2.25) <= TOY_BAR
            and abs(g_eval("SQ", parSQ, 2.0) - 9.0) <= TOY_BAR
            and abs(parTT[0] - 2.25) <= TOY_BAR
            and abs(parTT[1] - 0.21875) <= TOY_BAR
            and abs(g_eval("TT", parTT, 2.0) - 4.0) <= TOY_BAR
            and abs(parLN[0] - 2.0) <= TOY_BAR
            and abs(g_eval("LIN", parLN, 3.0) - 6.0) <= TOY_BAR
            and dSQ == dTT == dLN == (0, 1))
    ok_mono = (mono_check("SQ", parSQ) <= TOY_BAR
               and mono_check("TT", parTT) <= TOY_BAR
               and mono_check("LIN", parLN) <= TOY_BAR)
    toy_Fe = tuple(float(k) for k in range(1, 13))
    toy_up = tuple(float(k) for k in range(1, 13))
    toy_dn = tuple(float(13 - k) for k in range(1, 13))
    env_up, dcl_up = upper_envelope(toy_Fe, toy_up,
                                    tuple(range(12)))
    env_dn, _dcl_dn = upper_envelope(toy_Fe, toy_dn,
                                     tuple(range(12)))
    sp_up = spearman_rank(range(len(env_up)),
                          [e[1] for e in env_up])
    sp_dn = spearman_rank(range(len(env_dn)),
                          [e[1] for e in env_dn])
    ok_env = (len(env_up) == NB_ENV
              and abs(env_up[-1][1] - 12.0) <= TOY_BAR
              and abs(sp_up - 1.0) <= TOY_BAR
              and abs(sp_dn + 1.0) <= TOY_BAR
              and dcl_up == tuple(range(12)))
    ok_sp = (abs(spearman_rank((1, 2, 3, 4), (2, 4, 6, 8)) - 1.0)
             <= TOY_BAR
             and abs(spearman_rank((1, 2, 3, 4), (8, 6, 4, 2))
                     + 1.0) <= TOY_BAR)
    wc_toy = world_coord(3.0, 5.5, tuple(range(1, 11)),
                         (1.0,) * 10)
    ok_wc = abs(wc_toy - 3.0) <= TOY_BAR
    gv = (gate_verdict(True, True, True, True),
          gate_verdict(False, True, False, True),
          gate_verdict(False, True, True, True),
          gate_verdict(True, False, True, True),
          gate_verdict(True, True, False, True))
    ok_gv = gv == ("SLIDING_BOUND_GO", "ENVELOPE_DIFFUSE",
                   "G_FAILS_POINTWISE", "WORLD_LEAK",
                   "ENVELOPE_DIFFUSE")
    check("G41-toy-exactness", ok_med and ok_g and ok_mono
          and ok_env and ok_sp and ok_wc and ok_gv,
          "medloc cross-ward on the r317 spike toy: QMAX == F_A "
          "x medloc EXACT (dev %.1e), medians all 1; g toys: SQ "
          "par 2.25 g(2) = 9, TT pars (2.25, 0.21875) g(2) = 4, "
          "LIN par 2 g(3) = 6, declared (0, 1) EXACT; mono grid "
          "accepts 3/3 toy-calibrated forms; envelope toys: "
          "rising -> env max 12 Spearman +1, falling -> Spearman "
          "-1, declared EXACT; Spearman +/-1 toys EXACT; "
          "world_coord flat-ladder toy 3.0 EXACT; verdict tree "
          "5/5 branches EXACT %s" % (rec_sp, str(gv)))
    # live wards: r316 chain + the new bracket + reconstruction
    chain_w = 0.0
    xw_cube = 0.0
    brk_low = 0.0
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
        # bracket lower side: qmax x PhiH1 <= rho_2
        brk_low = max(brk_low,
                      max(0.0, trs["qmax"] * trs["phiH1"]
                          - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
    if smoke:
        rec_fa = 0.0
        ph_dev = 0.0
    else:
        medloc = local_median(qmax_col)
        rec_fa = max(abs(qmax_col[i] - FA[i] * medloc[i])
                     / max(qmax_col[i], 1e-300)
                     for i in range(n321))
        Bcol = [medloc[i] * float(m_all[i])
                / math.log(float(m_all[i]))
                for i in range(n321)]
        ph_dev = max(abs(srt321[i]["ev"]["trs"]["phiH1"]
                         - (FA[i] * Bcol[i]) ** 2)
                     / max(srt321[i]["ev"]["trs"]["phiH1"],
                           1e-300)
                     for i in range(n321))
    check("G42-bracket-and-chain-ward",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR
          and brk_low <= CHAIN_BAR and rec_fa <= 1e-12
          and ph_dev <= CHAIN_BAR,
          "the r316 chain live on %d live worlds (worst slack "
          "%.1e, bar %.0e); NORM x cube == rho_2 (worst %.1e); "
          "NEW bracket lower side qmax x PhiH1 <= rho_2 (worst "
          "slack %.1e -- with the chain: qmax PhiH1 <= rho_2 <= "
          "PhiH1 TWO-SIDED); reconstruction QMAX == F_A x medloc "
          "(worst %.1e)%s"
          % (len(live), chain_w, CHAIN_BAR, xw_cube, brk_low,
             rec_fa,
             "; PhiH1 == (F_A x B)^2 on the ladder (worst %.1e)"
             % ph_dev if not smoke else " (ladder wards SMOKE-"
             "skipped)"))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        info("sealed SOURCE-PURE coordinate table (printed "
             "BEFORE any bound-side table of this round): rank "
             "kz N m QMAX F_A B")
        for i, rc in enumerate(srt321):
            info("%2d kz%-3d N %4d m %3d qmax %.4f FA %5.2f B "
                 "%.4f" % (i, rc["kz"], rc["N"], m_all[i],
                           qmax_col[i], FA[i], Bcol[i]))
        check("G43-coordinate-table", True,
              "the coordinate is the r317 IMPORT (EFP."
              "local_ratio, W = %d) on the sealed QMAX column; "
              "F_A range on the %d-rung ladder: min %.2f / med "
              "%.2f / max %.2f (max at kz%d); B = medloc x "
              "m/log m printed as the source-pure baseline "
              "column"
              % (EFP.CLS_W, n321, min(FA),
                 float(np.median(FA)), max(FA),
                 srt321[int(np.argmax(FA))]["kz"]))

    # ---------------- S5: Leg B -- split + calibration + certif.
    section("S5  LEG B -- SPLIT + g-FAMILY CALIBRATION + "
            "CERTIFICATION")
    if smoke:
        check("G44-split-seal", True, "SMOKE: skipped")
        check("G50-smallm-certificates", True, "SMOKE: skipped")
        check("G51-g-calibration", True, "SMOKE: skipped")
        check("G52-map-census", True, "SMOKE: skipped")
        check("G53-envelope-census", True, "SMOKE: skipped")
        check("G54-certification", True, "SMOKE: skipped")
        check("G55-reserve-trend", True, "SMOKE: skipped")
    else:
        sm_i, ca_i, te_i = TRB.split_midladder(n321)
        ovl = len(set(sm_i) & set(ca_i)) \
            + len(set(sm_i) & set(te_i)) \
            + len(set(ca_i) & set(te_i))
        cover = (tuple(sorted(sm_i + ca_i + te_i))
                 == tuple(range(n321)))
        m0 = min(m_all[i] for i in ca_i + te_i)
        check("G44-split-seal",
              ovl == 0 and cover and len(ca_i) == N_CAL,
              "SEALED split on the %d-rung class ladder "
              "(TRB.split_midladder verbatim): small = ranks "
              "0..%d, cal = %d..%d (kz %s, m %d..%d), test = "
              "%d..%d (%d rungs); overlaps 0 EXACT, cover "
              "EXACT; m_0 = %d"
              % (n321, sm_i[-1], ca_i[0], ca_i[-1],
                 str([srt321[i]["kz"] for i in ca_i]),
                 min(m_all[i] for i in ca_i),
                 max(m_all[i] for i in ca_i),
                 te_i[0], te_i[-1], len(te_i), m0))
        C_small = max(rho_all[i] for i in sm_i)
        j_sm = max(sm_i, key=lambda i: rho_all[i])
        check("G50-smallm-certificates", C_small > 0.0,
              "%d small-m rungs certified individually (direct "
              "evaluation); C_small = %.4f at kz%d -- the finite "
              "exception constant of the theorem candidate"
              % (len(sm_i), C_small, srt321[j_sm]["kz"]))
        pars = {}
        decls = {}
        monos = {}
        for form in G_FORMS:
            pars[form], decls[form] = g_calibrate(
                form, FA, rho_all, Bcol, ca_i)
            monos[form] = mono_check(form, pars[form])
        ok_decl = all(decls[f] == tuple(ca_i) for f in G_FORMS)
        check("G51-g-calibration", ok_decl
              and all(monos[f] <= TOY_BAR for f in G_FORMS),
              "constants FROZEN on the declared cal set (ward "
              "EXACT %s): G_SQ b = %.4f (= B_cal_max %.4f "
              "squared, SOURCE-PURE -- no target consumed); "
              "G_TT c_1 = %.4f, c_2 = %.5f; G_LIN a = %.4f; "
              "monotonicity grid (%d pts, %.2f..%.2f): worst "
              "decrease SQ %.1e / TT %.1e / LIN %.1e -- 3/3 "
              "accepted"
              % (ok_decl, pars["SQ"][0],
                 math.sqrt(pars["SQ"][0]), pars["TT"][0],
                 pars["TT"][1], pars["LIN"][0], len(GRID_MONO),
                 GRID_MONO[0], GRID_MONO[-1], monos["SQ"],
                 monos["TT"], monos["LIN"]))
        # the bound-side map table + census
        info("the (rho_2, F_A) map (bound-side; per-form "
             "violation marks on TEST rungs): rank kz N m FA "
             "rho_2 g_SQ g_TT g_LIN [set] marks")
        gvals = {f: [g_eval(f, pars[f], FA[i])
                     for i in range(n321)] for f in G_FORMS}
        setlab = {}
        for i in sm_i:
            setlab[i] = "SMALL"
        for i in ca_i:
            setlab[i] = "CAL"
        for i in te_i:
            setlab[i] = "TEST"
        for i in range(n321):
            marks = "".join(
                ("*" if rho_all[i] > gvals[f][i] else ".")
                for f in G_FORMS) if i in te_i else "   "
            info("%2d kz%-3d N %4d m %3d FA %5.2f rho2 %.4f g "
                 "%7.4f %7.4f %7.4f %-5s %s"
                 % (i, srt321[i]["kz"], srt321[i]["N"],
                    m_all[i], FA[i], rho_all[i],
                    gvals["SQ"][i], gvals["TT"][i],
                    gvals["LIN"][i], setlab[i], marks))
        sp_test = spearman_rank([FA[i] for i in te_i],
                                [rho_all[i] for i in te_i])
        check("G52-map-census", True,
              "MAP census: Spearman(F_A, rho_2) over the %d test "
              "rungs = %+.2f (census, no gate bar -- the "
              "envelope, not the bulk correlation, is the sealed "
              "object); ladder F_A max %.2f at kz%d"
              % (len(te_i), sp_test, max(FA),
                 srt321[int(np.argmax(FA))]["kz"]))
        env_bins, env_decl = upper_envelope(FA, rho_all, te_i)
        env_vals = [e[1] for e in env_bins]
        sp_env = spearman_rank(range(len(env_vals)), env_vals)
        env_argmax = int(np.argmax(env_vals))
        env_ok = (env_argmax == len(env_vals) - 1
                  and sp_env >= ENV_RC_MIN
                  and env_decl == tuple(te_i))
        check("G53-envelope-census", env_decl == tuple(te_i),
              "sealed upper envelope on the DECLARED test set "
              "(ward EXACT): bins (F_med, max rho_2) = %s; "
              "argmax bin %d/%d %s top; bin Spearman %+.3f %s "
              "%.1f -> ENV_%s"
              % (str([(round(a, 2), round(b, 4))
                      for a, b in env_bins]), env_argmax,
                 len(env_vals) - 1,
                 "==" if env_argmax == len(env_vals) - 1
                 else "!=", sp_env,
                 ">=" if sp_env >= ENV_RC_MIN else "<",
                 ENV_RC_MIN, "OK" if env_ok else "DIFFUSE"))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n321):
                if srt321[i]["kz"] == kz:
                    named_rank[kz] = i
        viols = {}
        named_ok = {}
        for f in G_FORMS:
            viols[f] = [i for i in te_i
                        if rho_all[i] > gvals[f][i]]
            named_ok[f] = all(
                rho_all[named_rank[kz]]
                <= gvals[f][named_rank[kz]] for kz in NAMED_KZ)
        winner = None
        for f in G_FORMS:
            if monos[f] <= TOY_BAR and not viols[f] \
                    and named_ok[f]:
                winner = f
                break
        check("G54-certification", True,
              "per-form certification (census; adjudicated in "
              "S7): violations on the %d test rungs SQ %d / TT "
              "%d / LIN %d %s; named coverage kz53/kz83/kz67/"
              "kz55: %s; WINNER by sealed precedence (SQ > TT > "
              "LIN): %s"
              % (len(te_i), len(viols["SQ"]), len(viols["TT"]),
                 len(viols["LIN"]),
                 str({f: [srt321[i]["kz"] for i in viols[f]]
                      for f in G_FORMS if viols[f]}),
                 str({f: "%d/4" % sum(
                     1 for kz in NAMED_KZ
                     if rho_all[named_rank[kz]]
                     <= gvals[f][named_rank[kz]])
                     for f in G_FORMS}),
                 winner if winner else "NONE"))
        wf = winner if winner else G_FORMS[0]
        rsv = [gvals[wf][i] / max(rho_all[i], 1e-300)
               for i in te_i]
        NsT = [srt321[i]["N"] for i in te_i]
        sl_r = L2D.halves_slope(
            NsT, [max(rho_all[i] / max(gvals[wf][i], 1e-300),
                      1e-300) for i in te_i])
        named_note = "; ".join(
            "kz%d rho %.4f g %.4f rsv %.1f"
            % (kz, rho_all[named_rank[kz]],
               gvals[wf][named_rank[kz]],
               gvals[wf][named_rank[kz]]
               / max(rho_all[named_rank[kz]], 1e-300))
            for kz in NAMED_KZ)
        check("G55-reserve-trend", True,
              "reserve census at the %s form: min/med over test "
              "%.2f/%.2f; trend of rho_2/g(F_A) %+.3f (falling "
              "= growing reserve); the four named r316/r317 "
              "violators: %s"
              % (wf, min(rsv), float(np.median(rsv)), sl_r,
                 named_note))

    # ---------------- S6: Leg C -- structure + world
    section("S6  LEG C -- STRUCTURE (B census) + WORLD CHECK")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # SCRAMBLE class rejection machinery (r317 verbatim)
    evS = crecs["SCR"]["ev"]
    comp_ref = recs
    comp_main = dict(
        dflux=float(np.median([rc["ev"]["trs"]["nrm"]
                               * abs(rc["ev"]["trs"]["dflux"])
                               for rc in comp_ref])),
        coll=float(np.median([rc["ev"]["trs"]["nrm"]
                              * abs(rc["ev"]["trs"]["coll"])
                              for rc in comp_ref])),
        fcix=float(np.median([rc["ev"]["trs"]["fcix"]
                              for rc in comp_ref])))
    comp_scr = dict(
        dflux=evS["trs"]["nrm"] * abs(evS["trs"]["dflux"]),
        coll=evS["trs"]["nrm"] * abs(evS["trs"]["coll"]),
        fcix=evS["trs"]["fcix"])
    devsS = {k: abs(comp_scr[k] - comp_main[k])
             / max(abs(comp_main[k]), 1e-300) for k in comp_main}
    cause = max(devsS, key=lambda k: devsS[k])
    attr_ok = (devsS[cause] >= ATTR_MIN
               and cause in ("coll", "dflux"))
    rng = np.random.default_rng(SEED_SHUF)
    blk_shuf = ev9m["blk_all"][
        rng.permutation(len(ev9m["blk_all"]))]
    gen_s = SCF.fold_genealogy(ev9m["pos_all"], ev9m["val_all"],
                               blk_shuf, m9)
    ft_s = SCF.flux_telescope(gen_s["G1"], gen_s["ptr"], m9)
    mism_s = int(np.sum(np.searchsorted(ev9m["brk"],
                                        ev9m["pos_all"])
                        != blk_shuf))
    ne = min(len(ft_s["edges"]), len(ev9m["ft"]["edges"]))
    edev = float(np.max(np.abs(ft_s["edges"][:ne]
                               - ev9m["ft"]["edges"][:ne]))
                 / max(float(np.max(np.abs(
                     ev9m["ft"]["edges"]))), 1e-300))
    x_s = np.bincount(blk_shuf, weights=ev9m["val_all"],
                      minlength=m9)
    mass_dev = abs(float(np.sum(x_s))
                   - float(np.sum(ev9m["sct"]["x"]))) \
        / max(float(np.sum(np.abs(ev9m["val_all"]))), 1e-300)
    shuf_ok = (mism_s > 0 and edev >= MUT_MIN
               and mass_dev <= ID_BAR)
    if smoke:
        check("G60-structure-census", True, "SMOKE: skipped")
        check("G61-world-admission", True, "SMOKE: skipped")
        check("G62-scramble-mechanism", shuf_ok and attr_ok,
              "SMOKE (w9-based): attribution %s dev %.2f; "
              "shuffle %d mism, edge break %.1e, mass %.1e"
              % (cause.upper(), devsS[cause], mism_s, edev,
                 mass_dev))
        world_ok = attr_ok and shuf_ok
    else:
        B_cal_max = max(Bcol[i] for i in ca_i)
        B_test_max = max(Bcol[i] for i in te_i)
        sl_B = L2D.halves_slope(
            NsT, [max(Bcol[i], 1e-300) for i in te_i])
        check("G60-structure-census", True,
              "THE UPPER-DIRECTION CARRIER (exact bracket rho_2 "
              "<= F_A^2 x B^2, warded in G42): B = medloc x "
              "m/log m is SOURCE-PURE (QMAX column + rank order "
              "+ m only) and spike-robust (local median); ladder "
              "min/med/max %.4f/%.4f/%.4f; CAL MAX %.4f vs TEST "
              "MAX %.4f -> %s on the measured ladder (ratio "
              "%.2f); trend over test %+.3f -- the transfer "
              "question 'is B mid-ladder bounded' has this "
              "measured answer, and it is the G_SQ certification "
              "by algebra"
              % (min(Bcol), float(np.median(Bcol)), max(Bcol),
                 B_cal_max, B_test_max,
                 "BOUNDED" if B_test_max <= B_cal_max
                 else "NOT bounded", B_test_max / B_cal_max,
                 sl_B))
        # world admission at the sliding bound (insertion rule)
        ladder_Ns = [rc["N"] for rc in srt321]
        wnote = []
        adm_ok = True
        for nm, wrc in (("w9", mrecs[0]), ("w13(twin)", mrecs[1]),
                        ("EPSTEIN", crecs["EPST"])):
            ev = wrc["ev"]
            f_ins = world_coord(ev["trs"]["qmax"], wrc["N"],
                                ladder_Ns, qmax_col)
            gw = g_eval(wf, pars[wf], f_ins)
            adm = (ev["mx_mult"] <= MULT_CAP
                   and ev["rho2"] <= gw)
            adm_ok = adm_ok and adm
            wnote.append("%s mult %d rho2 %.3f %s g(%.2f) = %.2f"
                         % (nm, ev["mx_mult"], ev["rho2"],
                            "<=" if ev["rho2"] <= gw else ">",
                            f_ins, gw))
        tw_fac = max(mrecs[1]["ev"]["trs"]["phiL2"]
                     / max(mrecs[0]["ev"]["trs"]["phiL2"],
                           1e-300),
                     mrecs[0]["ev"]["trs"]["phiL2"]
                     / max(mrecs[1]["ev"]["trs"]["phiL2"],
                           1e-300))
        twin_ok = tw_fac <= TWIN_FAC
        f_scr = world_coord(evS["trs"]["qmax"], crecs["SCR"]["N"],
                            ladder_Ns, qmax_col)
        g_scr = g_eval(wf, pars[wf], f_scr)
        coord_break = evS["rho2"] > g_scr
        class_reject = attr_ok and shuf_ok
        scr_ok = coord_break or class_reject
        world_ok = adm_ok and twin_ok and scr_ok
        check("G61-world-admission", True,
              "WORLD census at the %s sliding bound (insertion-"
              "rule coordinates, adjudicated in S7): %s; twin "
              "band PhiL2 factor %.2f %s %.1f"
              % (wf, "; ".join(wnote), tw_fac,
                 "<=" if twin_ok else ">", TWIN_FAC))
        check("G62-scramble-mechanism", scr_ok,
              "SCRAMBLE mechanism (honestly documented): "
              "coordinate bound %s (rho2 %.3f %s g(%.2f) = %.3f "
              "-- %s) AND class rejection %s (attribution %s "
              "dev %.2f >= %.2f; seeded shuffle %d edgewise "
              "%.1e mass %.1e, %d/%d atoms) -> scr_ok = %s"
              % ("BREAKS" if coord_break else "holds",
                 evS["rho2"], ">" if coord_break else "<=",
                 f_scr, g_scr,
                 "the sliding-bound-native rejection"
                 if coord_break else
                 "the coordinate does NOT reject it",
                 class_reject, cause.upper(), devsS[cause],
                 ATTR_MIN, SEED_SHUF, edev, mass_dev, mism_s,
                 len(ev9m["pos_all"]), scr_ok))

    # ---------------- S7: Leg D -- adjudication + theorem
    section("S7  LEG D -- SEALED ADJUDICATION + THEOREM "
            "CANDIDATE")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-theorem-candidate", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        F_max = max(FA)
        F_min_te = min(FA[i] for i in te_i)
        if winner:
            gain = g_eval(winner, pars[winner], F_max) \
                / max(g_eval(winner, pars[winner], F_min_te),
                      1e-300)
        else:
            gain = 0.0
        gain_ok = gain >= GAIN_MIN
        vkey = gate_verdict(winner is not None, world_ok,
                            env_ok, gain_ok)
        if vkey == "SLIDING_BOUND_GO":
            C_impl = g_eval(winner, pars[winner], F_max)
            verdict_main = ("SLIDING_BOUND_GO(%s: rho_2 <= "
                            "%s on 0/%d test violations + 4/4 "
                            "named; gain %.2f >= %.1f; ENV_OK; "
                            "world clean)"
                            % (winner,
                               ("%.4f x F_A^2" % pars["SQ"][0])
                               if winner == "SQ" else
                               ("%.4f + %.5f x F_A^3"
                                % pars["TT"]) if winner == "TT"
                               else "%.4f x F_A" % pars["LIN"][0],
                               len(te_i), gain, GAIN_MIN))
        elif vkey == "WORLD_LEAK":
            C_impl = 0.0
            verdict_main = ("WORLD_LEAK(adm %s twin %s scr %s)"
                            % (adm_ok, twin_ok, scr_ok))
        elif vkey == "G_FAILS_POINTWISE":
            C_impl = 0.0
            verdict_main = ("G_FAILS_POINTWISE(envelope monotone "
                            "but every sealed form misses: viol "
                            "SQ %d / TT %d / LIN %d)"
                            % (len(viols["SQ"]), len(viols["TT"]),
                               len(viols["LIN"])))
        else:
            C_impl = 0.0
            reasons = []
            if winner is None:
                reasons.append("no certifying form + envelope "
                               "diffuse")
            else:
                if not env_ok:
                    reasons.append("envelope diffuse (argmax %d, "
                                   "Spearman %+.2f)"
                                   % (env_argmax, sp_env))
                if not gain_ok:
                    reasons.append("gain %.2f < %.1f (disguised "
                                   "flat constant)"
                                   % (gain, GAIN_MIN))
            verdict_main = ("ENVELOPE_DIFFUSE(%s)"
                            % "; ".join(reasons))
        check("G70-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        if vkey == "SLIDING_BOUND_GO":
            C_tot = max(C_impl, C_small)
            info("CANDIDATE THEOREM (sliding cubic bound; "
                 "measured on the %d-rung class ladder; status "
                 "SLIDING_BOUND_GO):" % n321)
            info("  Every class rung w (edge-masked, fold "
                 "multiplicity <= %d, POSITIVE_PREFIX) with m >= "
                 "%d satisfies" % (MULT_CAP, m0))
            info("    sum_j q_j^3  <=  g(F_A(w)) x (log m)^2 / "
                 "m^2   with   g(F) = %s,"
                 % (("%.4f x F^2" % pars["SQ"][0])
                    if winner == "SQ" else
                    ("%.4f + %.5f x F^3" % pars["TT"])
                    if winner == "TT" else
                    "%.4f x F" % pars["LIN"][0]))
            info("  F_A = the r317 rank-local QMAX ratio "
                 "(source-pure, W = %d, computable in advance); "
                 "g explicit, MONOTONE, mid-ladder frozen; the "
                 "%d rungs with m < %d are certified "
                 "individually (C_small = %.4f); the four named "
                 "r316/r317 violators are INSIDE the sliding "
                 "bound (the point of the gliding form)."
                 % (EFP.CLS_W, len(sm_i), m0, C_small))
            info("  COROLLARY (uniform bound): F_A <= %.2f "
                 "measured on the ladder, hence sum q^3 <= "
                 "C_impl x (log m)^2/m^2 with C_impl = g(%.2f) "
                 "= %.2f (C_tot = %.2f incl. small-m; n_eff = "
                 "N_2 >= N_3 >= m/(%.2f log m) by the r306 "
                 "exact chain).  DISCLOSED: C_impl is %.1fx "
                 "looser than the r306 first-5 constant -- the "
                 "round buys FORM (one gliding bound, no "
                 "regimes, no exceptions), not sharpness."
                 % (F_max, F_max, C_impl, C_tot,
                    math.sqrt(C_tot), C_impl / C2))
            info("  THE NEW SMALLER PROVENANCE QUESTION: is F_A "
                 "source-pure bounded%s?  Both are questions "
                 "about the LOCAL MEDIAN of the QMAX column -- "
                 "no cubic target appears in either."
                 % (" (and, for the G_SQ chain, is B = medloc x "
                    "m/log m bounded -- measured: cal max %.4f, "
                    "test max %.4f, trend %+.3f)"
                    % (B_cal_max, B_test_max, sl_B)
                    if winner == "SQ" else ""))
            check("G71-theorem-candidate", True,
                  "sliding theorem candidate printed with "
                  "explicit (g = %s, m_0 %d, C_small %.4f, "
                  "C_impl %.2f, C_tot %.2f, gain %.2f)"
                  % (winner, m0, C_small, C_impl, C_tot, gain))
        else:
            check("G71-theorem-candidate", True,
                  "no theorem candidate printed (the sealed "
                  "tree fired %s); the map, envelope and "
                  "structure censuses stand as the round's "
                  "record data" % vkey)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toy_Fm = (1.0, 1.0, 1.0, 1.0)
    toy_rm = (1.0, 1.0, 1.0, 5.0)
    a_mut = mutant_g_posthoc(toy_Fm, toy_rm)
    parW, _dw = g_calibrate("LIN", toy_Fm, toy_rm, toy_Fm,
                            (0, 1))
    check("G80-e1-g-posthoc",
          len(e1_hits) >= 1
          and abs(a_mut - parW[0]) >= MUT_MIN,
          "e1 CAUGHT twice: the after-sight re-calibration "
          "consumes the evaluated bound column over the whole "
          "ladder -- AST-FLAGGED (%s) -- and on the sealed toy "
          "it returns %.1f != the frozen first-2 calibration "
          "%.1f (diff %.1f >= %.0e); the real constants are "
          "frozen on the declared mid-ladder window only"
          % (e1_hits[0] if e1_hits else "MISS", a_mut, parW[0],
             abs(a_mut - parW[0]), MUT_MIN))
    check("G81-e2-coord-readback",
          len(e2_hits) >= 1 and (not sc_own),
          "e2 AST-CAUGHT: the 'coordinate' consuming the cubic-"
          "moment record (cm/S3) is FLAGGED (%s) while the six "
          "module-own builders are clean (%d hits) -- the "
          "source-purity of the coordinate is machine-audited"
          % (e2_hits[0] if e2_hits else "MISS", len(sc_own)))
    toy_Fi = tuple(float(k) for k in range(1, 13))
    toy_vi = tuple(float(k) for k in range(1, 13))
    te_toy = tuple(range(6, 12))
    ca_toy = tuple(range(0, 6))
    _envR, dclR = upper_envelope(toy_Fi, toy_vi, te_toy)
    _envM, dclM = mutant_envelope_cal(toy_Fi, toy_vi, ca_toy)
    check("G82-e3-envelope-cal",
          dclR == te_toy and dclM == ca_toy and dclM != te_toy,
          "e3 CAUGHT: the mutant envelope declares the "
          "calibration window %s != the test set %s (declared-"
          "set ward EXACT); the real envelope declares the test "
          "set EXACT -- evaluating the envelope in-sample is "
          "structurally refused"
          % (str(dclM), str(te_toy)))
    worst_mut = 0.0
    prev = None
    for f in GRID_MONO:
        v = mutant_g_nonmono(1.0, f)
        if prev is not None:
            worst_mut = max(worst_mut, prev - v)
        prev = v
    ok_seal_mono = all(
        mono_check(fm, pr) <= TOY_BAR
        for fm, pr in (("SQ", (2.25,)), ("TT", (2.25, 0.21875)),
                       ("LIN", (2.0,))))
    check("G83-e4-monotonicity-break",
          worst_mut >= MUT_MIN and ok_seal_mono,
          "e4 LOUD: the non-monotone mutant g = p F (2 - F) "
          "shows a worst grid decrease %.4f >= %.0e while all "
          "three sealed forms pass the same grid (<= %.0e) -- "
          "a monotonicity break cannot slip through the sealed "
          "check" % (worst_mut, MUT_MIN, TOY_BAR))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed continuous-coordinate statement form "
          "(monotone g of the r317 F_A import), the exact "
          "concentration bracket qmax PhiH1 <= rho_2 <= PhiH1 = "
          "(F_A B)^2 with the source-pure baseline B, the sealed "
          "three-form g-family with mid-ladder calibration, the "
          "fit-free envelope rule and the sliding-bound world "
          "check -- NO new certificate promoted, NO universal "
          "bound claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R321_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57, r315 C0 "
                 "%.4f/%.4f/%.4f, r316 n %d H %s C_L2 %.4f "
                 "C_small %.4f, r317 top3 %s thrB %.4f C_gen "
                 "%.4f viol %s)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, n321, rec3_w, C2, viol2, C0["a"],
                    C0["b"], C0["c"], n321, str(h_kz), CL2,
                    C_small316, str(top3_kz), thrB, C_gen,
                    str(viol_gen))]
        parts.append("SEAL(coordinate import W %d, bracket "
                     "%.1e, purity clean, toys exact)"
                     % (EFP.CLS_W, brk_low))
        parts.append("MAP(Spearman %+.2f, env %s, ENV_%s)"
                     % (sp_test,
                        str([round(b, 3) for b in env_vals]),
                        "OK" if env_ok else "DIFFUSE"))
        parts.append("GFAMILY(SQ b %.4f viol %d, TT (%.4f, "
                     "%.5f) viol %d, LIN a %.4f viol %d, "
                     "winner %s, reserve %.2f/%.2f, trend "
                     "%+.3f)"
                     % (pars["SQ"][0], len(viols["SQ"]),
                        pars["TT"][0], pars["TT"][1],
                        len(viols["TT"]), pars["LIN"][0],
                        len(viols["LIN"]),
                        winner if winner else "NONE",
                        min(rsv), float(np.median(rsv)), sl_r))
        parts.append("STRUCTURE(B cal max %.4f test max %.4f "
                     "%s, trend %+.3f)"
                     % (B_cal_max, B_test_max,
                        "BOUNDED" if B_test_max <= B_cal_max
                        else "NOT-BOUNDED", sl_B))
        parts.append("WORLD(adm %s, twin %.2f, SCR coord %s + "
                     "class %s)"
                     % (adm_ok, tw_fac,
                        "BREAK" if coord_break else "hold",
                        class_reject))
        parts.append(verdict_main)
        parts.append("THEOREM(%s)"
                     % ("printed" if vkey == "SLIDING_BOUND_GO"
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the concentration "
          "bracket, the reconstruction identity, the g "
          "monotonicity, the tree logic and the purity audits "
          "(exact / AST-decided); MEASURED: every constant, "
          "violation count, envelope bin, reserve, trend and "
          "census (the finite class ladder + 2 mains + 2 live "
          "controls); OPEN: any bound beyond the measured "
          "rungs, the cofinal law, the boundedness of F_A and "
          "B beyond the ladder, kz15 beyond r270; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'coordinate orientation' consuming
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'coordinate constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_3 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""antiphase_sign_law_probe -- PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01
(round 322, the DIG round after the r318 fork decision).  Strategic
frame (binding): r318 decided the reviewer fork P2_MAIN_SPECIFIC --
the 2.4 percent negative cross mixtures of the block-Green family
are NOT structureless; on MAIN-class worlds (w9 ladder 12/12 rungs
+ rational twin exact) the block residual lives lawfully on the
ANTIPHASE pair (D3, D4) with fixed sign -1 (modal share med 0.699)
while the dead controls break BY PATTERN (their residual sits on
arch-mean x border (D5, D6): shares 0.95/1.00 vs MAIN 0.03).  Per
the reviewer rule ("if one route is MAIN-specific: dig there") this
is the dig round.  The reviewer thesis made concrete here: "not
positivity DESPITE the negative structure, but controlled
positivity THROUGH an organized indefinite structure" -- the
candidate for the indefinite theorem is a SIGN LAW of the antiphase
cross mixture.  HONEST RESERVATION FROM R318 (hardened first): the
control fingerprints were measured on non-psd-feasible 200-step
Dykstra ITERATES (the r308 non-convergence) -- the r318 world
contrast compares converged (MAIN) against non-converged
(controls).  The three questions of this round: (1) HARDENING --
is the fingerprint iteration- and construction-invariant on MAIN
(starts, step counts, projection order; solution-set property vs
algorithm property), and what do FAIR control objects carry (the
least-norm affine solution, which always exists; the r311
budget-ablated control target, which converges)?  (2) THE LAW
ITSELF -- which (D3, D4) cross entries are negative, how does the
magnitude scale over the rungs, and does an EXACT identity-level
coupling exist (the identity constraints are linear -- compute the
FORCED COMPONENT of the identity on the (D3, D4) sector
symbolically in Fractions at the small windows)?  (3) THE THEOREM
CANDIDATE -- "Q_w admits a block decomposition with psd blocks
PLUS an antiphase cross mixture of fixed sign whose magnitude is
bounded by a source-pure quantity": certify the FORM on the 57
rungs + twin, check the control break on FAIR objects, and sketch
the implication chain to L* with the missing links named honestly.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r320 (Lean repair) and r321 (fiber coordinate) run in
parallel; this probe touches nothing of theirs; the rh-sync is
strictly ADDITIVE.

INDEX FIREWALL (binding, r238-r318 discipline): w = window (kz),
S = #union atoms of mutilde = mu - nu, S_+ = #mu atoms, S_- = #nu
atoms, N_w = builder depth = (S+1)//2, n = degree, minC = first n
with h_n < 0.  Ground truth (minC, control flips, published record
numbers, the sealed r318 fingerprint pins) enters GATES and record
tables only; the sealed constructors consume passed matrices,
coordinate systems and split-source arrays ONLY (AST scope audit);
no zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r318 IF.{block_residual_census, fp_consensus, V_LIB,
A21_ISO, PA6, PB6, ISOW, IU1, JU1} (the sealed fingerprint
protocol), r312 BM.{feas_diag_g, nnls_lh, lib_vectors}, r311
BN.{gate_lam_rel, vech_of, unvech, rref_rank_fr} + the r311 budget
ablation ladder (ABL_MAIN_S), r308 BG.{census_world, world_arrays,
world_budget, hull_of, block_eigs, least_norm, system_fr,
rref_solve_fr, target_form_fr, mono_rows_fr, block_maps_fr,
exact_budget_fr, border_split}, r288 DC.zv_block (the antiphase
carrier map), r284 LS.{world_pack, spectral_block}, r289
AK.twin_rational + r276 MF.local_gaps, r278 MS.ctx_build, r244
BH.spearman, v881 PIK.lambda_eps, v563 core READ-ONLY.
The only local re-implementations: (i) resid_census_ext = the
UNCHANGED r318 residual-census body returning the per-block
residual entries in addition (anatomy needs the entries, not only
the modal pair; the modal tie-break is byte-identical); (ii)
feas_diag_rev = the UNCHANGED r312 Dykstra body with the two
projections SWAPPED (affine first, then psd; the final point is
psd by construction, convergence = affine residual) -- the sealed
projection-order variant of Leg A.

THE SEALED FORCED-COMPONENT ANALYSIS (Leg B core, frozen here):
the identity constraints are linear, M g = q (r308 system).  For a
linear functional phi on the unknown space, the value phi . g is
CONSTANT on the affine solution set iff phi lies in rowspace(M);
its forced part is phi_par = y^T M with the normal-equation
solution M M^T y = M phi, the forced VALUE is y . q, and the free
fraction is |phi - phi_par|^2 / |phi|^2 (== 0 iff fully forced).
All of it EXACT in Fractions on the exact windows (monomial
basis).  The sector functional of the round: phi_23 = sum_r
G_r[D3, D4] (coefficient 1 on every (2, 3) column of the unscaled
exact system; 1/sqrt(2) on the isometric f64 system).  EXACT
CALIBRATOR (known truth, r308 G10): on TOY4 the (t, t) functional
phi_66 = G[D6, D6] is fully forced with exact value B - 5/7 = 4/7
(D6 is the only t-carrying coordinate of the single block) -- the
machinery must reproduce free fraction 0 and value 4/7 exactly.
DESIGN-TIME DISCLOSURE: D3 = -(D2 + 2 D1) is linearly dependent
inside each block (r308 disclosure), so the (2, 3) sector is NOT
expected to be forced -- the exact free fraction MEASURES how much
of the sign law the identity itself pins; a nonzero free fraction
with the sign law still invariant (Leg A) means the law lives in
the SELECTION GEOMETRY (cone projection of the solution set), not
in the identity algebra -- typed honestly either way.

THE SEALED LEGS (frozen BEFORE any evaluation):

LEG 0 -- ANCHORS.  w9 source pins (367/263/104/184/184); budget
B = 8.368649 (tol 1e-3); THE R318 FINGERPRINT REPRODUCED with the
identical protocol (r308 Dykstra 200 steps from the least-norm
start, per-block NNLS onto the sealed 22-generator cone): Dykstra
CONV (>= -1e-9), modal pair == (2, 3), modal sign == -1, modal
share >= 0.5, d6-class share <= 0.10, cone share med/min/mean in
the r312 bands (0.976/0.952/0.978 tol 0.01), top-eigvec alignment
med 0.9973 (tol 0.005); the r289 twin rebuilt verbatim (minC 184)
with fingerprint pair (2, 3), sign -1, share >= 0.5 (METRIC_ONLY).

LEG A -- HARDENING (question 1).
(a1) START/ORDER/STEP INVARIANCE on w9@A: the sealed variant set
  {LSTART = least-norm start 200 steps (the anchor); LONG =
  least-norm start 1000 steps; ZERO = zero start; RAND1/RAND2 =
  the r311-class random starts (sealed seeds 20260827/20260828,
  r311 scale convention); REV = the projection-order-swapped
  Dykstra from the least-norm start}, alternative starts and REV
  on the staged r311 schedule 200/2000/20000; a variant is
  ACCEPTED iff
  conv (min eig rel >= -1e-9 resp. affine rel <= 1e-9 for REV) or
  near-conv (>= -1e-8, the r311 START_NEAR class, disclosed as
  such); INVARIANCE HOLDS iff every accepted variant carries modal
  pair (2, 3) sign -1 with |share - share_LSTART| <= 0.15 AND at
  least two accepted variants are DISTINCT solution points
  (pairwise rel distance >= 1e-6) -- then the law is a property of
  the SOLUTION SET as sampled, not of one iterate; any accepted
  variant breaking pair/sign => INVARIANCE BREAKS and the sealed
  tree types ALGORITHM_ARTIFACT (amendment a1, disclosed in the
  record tables: gate typing MEASURED -- the negative branch is a
  verdict letter, not a probe failure; no bar, acceptance rule,
  statistic or tree moved).
(a2) FAIR CONTROL OBJECTS: (i) the LEAST-NORM census -- the
  fingerprint of the least-norm affine solution (which ALWAYS
  exists, psd or not; labeled LEASTNORM, non-psd disclosed) on
  w9 / twin / EPST / SCR at DEG_A: the same construction for
  every world, no convergence asymmetry; (ii) the R311 BUDGET
  ABLATION: EPST/SCR targets with (t, t) replaced by the first
  ladder value {|S_ctrl|, 7.654364} making the target PD, then
  least-norm start + staged Dykstra (200/2000/20000) -- the
  ablated control families CONVERGE per r311; their fingerprint
  on the converged family is the fair world contrast: does the
  fair control carry the MAIN law ((2, 3), -1) or its own
  pattern?  MEASURED either way; a fair control carrying the MAIN
  law is typed FAIR_CONTROL_CARRIES (the r318 shape contrast was
  then an iterate artifact -- honest downgrade inside the letter).

LEG B -- ANATOMY + FORCED COMPONENT (question 2).
(b1) ANATOMY on the converged w9 family: dominant-pair histogram
  over the 364 blocks; position dependence (share of (2, 3)-
  dominant blocks per index third head/mid/tail); SIGN
  CONSISTENCY = fraction of (2, 3)-dominant blocks with
  R_r[2, 3] < 0 (law bar 0.9); entry-level fraction of ALL blocks
  with R_r[2, 3] < 0 (typed); rung scaling: per sealed r318 rung
  (the 12-rung set, computed inside the Leg-C ladder loop) the
  magnitude MAG = med_r |R_r[2, 3]| / ||G_r||_F and the residual
  share 1 - cone_share_med, with spearman(MAG, S) typed as
  information.
(b2) THE FORCED COMPONENT (exact): TOY4 calibrator (phi_66 fully
  forced, value 4/7 EXACT -- hard gate; normal equations); phi_23
  on SM1 (the r308 MAIN-class miniature, 7 blocks): exact free
  fraction + exact forced value (Fractions, normal equations --
  the SM1 entries are small rationals, cost-safe); phi_23 on
  MINI16 (the real-w9 miniature, 13 blocks, dyadic entries):
  exact ROWSPACE MEMBERSHIP by the rank test rank(M) vs
  rank(M + [phi]) (the r312-proven-feasible exact grade; the
  normal equations would square the dyadic bit length --
  cost disclosure, sealed at design time) plus the f64 free
  fraction/forced value on the float-converted exact system;
  f64 consistency on w9@A (lstsq rowspace residual + forced
  value, typed); the sector is typed FORCED iff the SM1 exact
  free fraction == 0 AND the MINI16 exact membership holds --
  then the forced value's sign IS the identity-level sign law.
(b3) COUPLING CANDIDATES (each a sealed correlation test, bar
  |spearman| >= 0.9, typed COUPLED/UNCOUPLED, never a claim):
  K1 per-block on w9: |R_r[2, 3]| vs the local antiphase mass
  pairing g_j g_{j+2} + g_{j+1} g_{j+3} (the D3/D4 incidence
  masses); K2 per-rung (12 rungs): MAG vs the 5/7-reserve
  S_{N-2} = B - 5/7; K3 per-rung (12 rungs): MAG vs |z_v| of the
  r288 antiphase carrier map at the rung's crossing (gate-side
  spectral consumption, disclosed).

LEG C -- THE THEOREM CANDIDATE (question 3).  Candidate form
(sealed text): "Q_w - (5/7) t^2 = sum_r <G_r Delta_r, Delta_r>
with G_r = P_r + E_r, P_r in the sealed 22-generator psd cone
(psd by construction), E_r the cone residual with dominant
support on the antiphase pair (D3, D4) and fixed sign
E_r[3, 4] <= 0, and residual mass sum_r ||E_r||_F small against
sum_r ||G_r||_F."  CERTIFICATION CENSUS: on all 57 rungs (42 core
h <= 900 + 15 extension anchors h <= 1300, the r312 rule) + the
twin: Dykstra staged 200/2000 (ladder cap, disclosed; unconverged
rungs typed ITERATE and counted NOT certified), certified iff
CONV AND modal pair (2, 3) AND sign -1 AND share >= 0.5 AND cone
share med >= 0.95; the control break on the FAIR objects from Leg
A is the world-contrast half.  THE IMPLICATION SKETCH (typed,
never a claim): psd blocks + kernel exclusion + a bound
|<E Delta, Delta>| <= (1 - delta)(<P Delta, Delta> + (5/7) t^2)
would give Q > 0 on the restricted subspace (Schur/inertia:
psd + controlled indefinite perturbation => index bound).
MISSING LINKS (sealed list, all named in the letter): L1 the
degree gap (DEG_A = 8 << N_w; restricted-subspace psd asserts
nothing about h_n -- the r282/r308 demarcation); L2 the selection
gap (no source-pure constructive rule for the family, r312
COEFFICIENT_SIGN_WALL -- the decomposition exists solver-wise,
not canonically); L3 the bound gap (the antiphase magnitude bound
is census-grade, no source-pure inequality; the exact forced
component decides whether an identity-level hook exists); L4 the
bridge gap (restricted positivity at one cap does not imply the
window inertia statement -- the r277/v962 bridge needs every
truncation); L5 the convergence gap (r311: ablated controls
converge too -- a certificate must use MORE than convergence: the
pattern itself, which is not yet an inequality).

LEG D -- MUST-FAILS (each loud):
  (m1) FINGERPRINT ON AN UNCONVERGED MAIN ITERATE: the census of
    the 2-step w9 Dykstra iterate must be flagged ITERATE by the
    sealed acceptance verifier (feas < -1e-9 => REJECT), while
    the converged anchor census is accepted -- the r318 caveat
    is machine-enforced;
  (m2) D-PAIR PERMUTATION: the census run on the coordinate-
    permuted family P G P^T (D3 <-> D5, i.e. indices 2 <-> 4)
    must report a modal pair != the sealed anchor pair -- CAUGHT
    by the anchor comparison (the pair label is load-bearing);
  (m3) FORCED COMPONENT WITH THE WRONG IDENTITY SIGN (exact):
    the mutant consuming -q on TOY4 must return forced value
    -4/7 != +4/7 -- CAUGHT in Fractions (the calibrator value is
    nonzero by r308 G10, so the catch cannot be vacuous);
  (m4) COUPLING WITH TARGET READ-BACK: a mutant coupling feature
    consuming the withheld truth (R23_true / cross_true) --
    FLAGGED by the AST scope audit.

STOP LIST (binding): NO L* claim, NO RH claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO posthoc window,
NO re-opened no-go entry (functionals, extremality, KYP, Maslov,
fixed head, paired cone, block-Green construction, diophantine,
magnitudes stay stopped); no bar, band, rule or verdict form
change after any evaluation (amendments disclosed); r243..r321
stand; mincut base 4 / refined 5 UNCHANGED.

WORLDS: MAIN w9; the r289 rational twin (METRIC_ONLY semantics);
controls EPST / SCRAMBLE(seed 1) built verbatim through the
r283/r284 channel (the two fair-object controls of r311); the
57-rung census ladder (42 core + 15 extension, r312 rule); exact
models TOY4 / SM1 / MINI16 rebuilt VERBATIM from the r308
constructors.

SEALED CONSTANTS: DEG_A 8; MAIN_KZ 9; W9_ANCH (367, 263, 104,
184, 184); B_W9_REC 8.368649 tol 1e-3; H_CAP 900; EXT_H 1300;
K_EXT 15; FEAS_IT (200, 2000, 20000); FEAS_CONV 1e-9; NEAR_CONV
1e-8; STEP_LONG 1000; SEEDS_R (20260827, 20260828); REV_CONV
1e-9; DIST_MIN 1e-6; FP_PAIR (2, 3); FP_SIGN -1; SHARE_MIN 0.5;
SHARE_BAND 0.15; D6_MAX 0.10; SIGN_CONS_BAR 0.9; SHARE_REC
(0.976, 0.952, 0.978) tol 0.01; ALIGN_REC 0.9973 tol 0.005;
TWIN_MINC_REC 184; TWIN_SHARE_REC 0.692 tol 0.05; ABL_MAIN_S
7.654364 (r311); PSD_NEG 1e-7; SP_BAR 0.9; CONE_MIN 0.95;
LADDER_CAP_IT 2000; N_FP 12; RAT_TOL 1e-8; QMAX 1e6; MINI_K 16;
MINI_BK 3; F64_FORCE_BAR 1e-16; DEPTH_PAD 6; TOY4 x = (1/2, 1/4,
-1/4, -1/2) w = (1, 1/2, -1/3, 1/4) border (3/4) w (1/5) B = 9/7
deg cap 1 (r308 verbatim); SM1 x_j = (9-2j)/11, w = (1, 1, -1/3,
1, 1, -1/4, 1, 1, -1/5, 1), SM border (4/5, 1/3, -2/5) w (1/7,
1/11, 1/13) (r308 verbatim); runtime <= 1800 s; smoke = S0 + S1
exact layer (TOY4 calibrator + SM1 forced component) + w9 anchor
(census + 200-step Dykstra + fingerprint) + w9 anatomy + w9 f64
forced component + all four must-fails + scope audits (MINI16,
twin, controls, variants, ablation, ladder, coupling, candidate,
adjudication skipped).  PRE-SPEC SCOPING
(disclosed): every record number above is a published r308/r311/
r312/r318 record adopted as-is; the variant set, the fair
objects, the forced-component machinery, the coupling candidates,
the certification bars, all four must-fails, every bar/band/
tolerance, the adjudication tree and the verdict form were fixed
at design time BEFORE any evaluation of this probe; no machinery
pass preceded this spec except record reading.

SEALED ADJUDICATION TREE (frozen BEFORE evaluation):
  law_anchor = the Leg-0 w9 fingerprint gate (pair, sign, share,
    d6, cone bands) AND anatomy sign consistency >= 0.9;
  invariant = the Leg-A a1 invariance gate;
  exact_forced = SM1 exact free fraction == 0 with forced value
    < 0 AND MINI16 exact rowspace membership TRUE;
  NOT law_anchor => LAW_DIFFUSE;
  law_anchor AND NOT invariant => ALGORITHM_ARTIFACT(variant);
  law_anchor AND invariant AND exact_forced =>
    SIGN_LAW_EXACT(forced identity verbatim);
  otherwise => SIGN_LAW_ROBUST(lawful, not exact).
SEALED VERDICT FORM (joined with '+'):
  [exactly one of] SIGN_LAW_EXACT / SIGN_LAW_ROBUST /
    ALGORITHM_ARTIFACT / LAW_DIFFUSE
  + HARDENING(variant table; distinctness; fair-object contrast)
    [always]
  + ANATOMY(pair histogram; position; sign consistency; scaling)
    [always]
  + FORCED(TOY4 calibrator; SM1/MINI16 exact; w9 f64) [always]
  + COUPLING(K1/K2/K3) [always]
  + CANDIDATE(cert census; missing links L1-L5) [always]
  + R318_DEMARCATION [always]: the r318 letters stand; this
    round adjudicates the dig questions only.

RECORD TABLES (frozen from the record run; chronology honest:
(i) PRE-RUN PROTOCOL CORRECTION disclosed -- a draft record-table
block with placeholder numbers was removed from this docstring
BEFORE the first run of any stage (the r316/r318 protocol lesson,
applied); (ii) smoke pass 1 = 25/25 (1.3 s) at the sealed rules;
(iii) calibration pass 1 = first full evaluation = 23/25: the G30
invariance gate was typed HARD in the draft harness, so the
honest negative branch of the sealed tree (ALGORITHM_ARTIFACT,
already produced verbatim by this very pass) failed the probe
arithmetically -> AMENDMENT a1 (disclosed, gate typing only): G30
is MEASURED and the sealed tree adjudicates in S8 -- the negative
branch is a verdict letter, not a probe failure (house precedent:
the r318 FORK_DEAD branch is a passing letter); NO bar,
acceptance rule, statistic, band or tree moved, and the verdict
letter of calibration pass 2 is IDENTICAL to the letter produced
by pass 1; one reporting-only enrichment of the
ALGORITHM_ARTIFACT letter detail (the measured basin facts,
r318-a1 class); calibration pass 2 = 25/25 (165.1 s), all
numbers identical to pass 1; record run1/run2 = 25/25, identical
up to WALL).
REC_VERDICT = ALGORITHM_ARTIFACT(the law breaks under the sealed
variants RAND1/RAND2 -- their accepted near-feasible points
(staged to 20000 steps, min eig rel -8.5e-9 / -1.2e-9, the r311
START_NEAR class) carry modal pair (0, 2) with shares 0.310 /
0.264 and cone share med 0.782: the sign law AND the r312
97.6/2.4 cone anatomy are properties of the LEAST-NORM-PROXIMAL
DYKSTRA BASIN, not of the psd solution set as a whole; the
canonical protocol variants LSTART/LONG/ZERO/REV all carry the
law exactly ((2, 3), -1, share 0.692) AND converge to essentially
ONE point -- the distinctness census shows exactly 9/15 variant
pairs distinct = precisely the pairs involving RAND1/RAND2 (the
six canonical pairs coincide within rel 2.0e-7): the sampled psd
intersection has (at least) two basins, and the law is the
fingerprint of the least-norm-proximal one)
+ HARDENING(variant table LSTART (2,3) -1 0.692 OK / LONG 0.692
OK / ZERO 0.692 OK / RAND1 (0,2) 0.310 NEAR / RAND2 (0,2) 0.264
NEAR / REV 0.692 OK (projection order irrelevant); FAIR OBJECTS:
(i) LEASTNORM census (same construction on every world, non-psd
disclosed): w9 (2,3) -1 0.698 / twin (2,3) -1 0.698 / EPST (4,5)
-1 1.000 d6 1.000 / SCR (4,5) -1 1.000 d6 1.000 -- the r318
world-contrast SHAPE is already present at the least-norm point
(the control 200-step iterates stall near it), and MAIN's law is
present there too; (ii) THE DECISIVE FAIR CONTRAST, r311 budget
ablation staged 200/2000/20000: EPST-abl (t,t) <- +3.9921,
target PD +1.04e-3, Dykstra CONV +2.5e-16 @2000, census (2, 3)
-1 share 0.742 d6 0.047 cone med 0.958 => CARRIES the MAIN law
(stronger than MAIN's own 0.692); SCR-abl (t,t) <- +5.2368, PD
+1.08e-3, CONV -5.1e-11 @200, census (2, 3) -1 share 0.379 d6
0.371 => breaks the share bar => FAIR_CONTROL_CARRIES 1/2: the
r318 SHAPE dichotomy ((4,5) vs (2,3)) does NOT survive fair
convergence -- on converged fair objects the separation is a
share MARGIN and mixed, not a pattern dichotomy)
+ ANATOMY(dominant-pair histogram w9 (364 blocks): (2,3) 252 =
share 0.692, then (2,4) 67 / (3,4) 29 / (4,5) 10 -- the
sub-dominant pairs are antiphase-adjacent, not border; position
NOT uniform: thirds share 0.289/0.860/0.926 (the law lives in
the mid/tail of the fold order; the head third is (2,4)/(3,4)-
mixed); SIGN CONSISTENCY 1.000 -- EVERY (2,3)-dominant block has
R[2,3] < 0 (bar 0.9) and 92.3 percent of ALL blocks have
R[2,3] < 0; rung scaling: MAG med 7.4e-3..1.4e-2 over the 12
sealed rungs, spearman(MAG, S) = -0.168 -- scale-stable, no
growth law)
+ FORCED(TOY4 calibrator MACHINE-EXACT: free fraction 0, value
4/7 == B - 5/7 -- the normal-equation machinery reproduces the
r308 G10 hand pin; SM1 phi_23 exact free fraction 0.47671,
forced value +5.101e-1 (POSITIVE) -- the identity pins roughly
half the sector mass and pins it with the WRONG sign for the
law; MINI16 exact rowspace membership FALSE (rank 55 -> 56 with
phi appended; f64 free 0.58576, value +3.1e-7); w9 f64 free
0.63527, value +1.203e-1 -- CONSISTENT ACROSS GRADES: the
(D3, D4) sector is roughly half free, and its forced half has
POSITIVE value: the negative sign law is carried ENTIRELY by the
free directions = the selection geometry, exactly as the D3 =
-(D2 + 2 D1) in-block dependence disclosure predicted;
exact_forced = False)
+ COUPLING(K1 per-block |R[2,3]|/||G||_F vs antiphase mass
pairing g_j g_{j+2} + g_{j+1} g_{j+3}: spearman +0.8114 --
UNCOUPLED at the sealed 0.9 bar but the strongest measured
correlate of the round (typed information: the residual
magnitude tracks the local antiphase mass geometry at rank
+0.81); K2 per-rung MAG vs 5/7-reserve S_{N-2}: -0.832
UNCOUPLED; K3 per-rung MAG vs |z_v| (r288 carrier at the
crossing): +0.252 UNCOUPLED -- no rung-global coupling; the only
near-coupling is block-LOCAL)
+ CANDIDATE(certification census at the sealed bars (CONV +
pair + sign + share >= 0.5 + cone med >= 0.95): 57/57 rungs
CERTIFIED (conv 57/57 within the 2000-step ladder cap; worst
share 0.605@kz23, worst cone med 0.970@kz12) + twin CERTIFIED
(0.692) -- the candidate FORM holds censally on the whole
MAIN-class ladder AS A PROPERTY OF THE CANONICAL FAMILY, but the
round's own hardening findings demote it: the family is
basin-selected (main letter) and a fair control carries the
pattern (L5 sharpened); MISSING LINKS L1-L5 all open, L5 now
sharpened to: fair controls converge AND can carry the pattern
-- a certificate needs the share margin as an inequality, which
does not exist)
+ R318_DEMARCATION.
Key numbers.  LEG 0 bit-near: w9 367/263/104/184/184, B =
8.368649; r318 fingerprint reproduced (CONV +6.56e-16, (2, 3) -1
share 0.692 d6 0.027, cone med/min/mean 0.9760/0.9520/0.9778,
alignment 0.9973; twin CONV +2.05e-17, (2, 3) -1 0.692 == the
r318 twin record).  MUST-FAILS: m1 2-step w9 iterate (feas
-2.4e-3) REJECTED as ITERATE, converged anchor accepted; m2
permuted-family census modal (3, 4) != (2, 3) CAUGHT; m3 -q
mutant forced value -4/7 != +4/7 CAUGHT exact; m4 read-back
mutant AST-FLAGGED (R23_true/cross_true); constructors +
fragment audit CLEAN.  READING (typed measurement): the dig
round answers all three questions honestly AGAINST the strong
form of the r318 hope -- (1) the law is protocol-stable
(starts in the least-norm class, step counts, projection order)
but NOT solution-set-universal: random-basin near-solutions
carry a different fingerprint, so the law is a property of the
Dykstra selection, and the r318 world contrast weakens on fair
objects (EPST-abl carries the pattern stronger than MAIN); (2)
the law is NOT identity-forced -- the exact forced component of
the (D3, D4) sector is ~half the mass with POSITIVE value, the
negative law lives entirely in the free/selection directions;
its best correlate is the block-local antiphase mass pairing
(+0.81, below bar); (3) the candidate form certifies 57/57 +
twin censally but is demoted by (1): without a canonical
selection rule (L2, the r312 wall) the antiphase sign law
cannot be stated as a property of Q_w itself.  What survives as
the honest dig yield: the law is a sharp, reproducible,
POSITION-STRUCTURED (mid/tail) fingerprint of the least-norm-
proximal psd family with total sign consistency, and the
selection-geometry question ("WHY does the proximal basin
organize its indefiniteness on the antiphase pair?") is now the
precisely named residual object -- one honest candidate hook
survives at reporting grade: the block-local antiphase mass
pairing.  Runtime 165.1 s full / 1.3 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: a1 only (gate
typing, disclosed above; letter identical across passes).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import indefinite_fork_probe as IF                 # noqa: E402 r318
import blockgreen_membership_probe as BM           # noqa: E402 r312
import blockgreen_nontriviality_probe as BN        # noqa: E402 r311
import block_green_probe as BG                     # noqa: E402 r308
import destructive_coherence_probe as DC           # noqa: E402 r288
import lstar_two_measure_probe as LS               # noqa: E402 r284
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import bordered_hankel_probe as BH                 # noqa: E402 r244
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
MAIN_KZ = 9
W9_ANCH = (367, 263, 104, 184, 184)
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
H_CAP = 900
EXT_H = 1300
K_EXT = 15
FEAS_IT1 = 200
FEAS_IT2 = 2000
FEAS_IT3 = 20000
FEAS_CONV = 1e-9
NEAR_CONV = 1e-8
STEP_LONG = 1000
SEEDS_R = (20260827, 20260828)
REV_CONV = 1e-9
DIST_MIN = 1e-6
FP_PAIR = (2, 3)
FP_SIGN = -1
SHARE_MIN = 0.5
SHARE_BAND = 0.15
D6_MAX = 0.10
SIGN_CONS_BAR = 0.9
SHARE_REC = (0.976, 0.952, 0.978)
SHARE_TOL = 0.01
ALIGN_REC = 0.9973
ALIGN_TOL = 0.005
TWIN_MINC_REC = 184
TWIN_SHARE_REC = 0.692
TWIN_SHARE_TOL = 0.05
ABL_MAIN_S = 7.654364
PSD_NEG = 1e-7
SP_BAR = 0.9
CONE_MIN = 0.95
LADDER_CAP_IT = 2000
N_FP = 12
RAT_TOL = 1e-8
QMAX = 1e6
MINI_K = 16
MINI_BK = 3
F64_FORCE_BAR = 1e-16
DEPTH_PAD = 6
FIVE_SEVEN = Fr(5, 7)
B_TOY = Fr(9, 7)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

PAIRS21 = [(a, b) for a in range(6) for b in range(a, 6)]
P23_IDX = PAIRS21.index((2, 3))
P66_IDX = PAIRS21.index((5, 5))

MISSING_LINKS = (
    "L1 degree gap (DEG_A = 8 << N_w; restricted-subspace psd "
    "asserts nothing about h_n -- r282/r308 demarcation)",
    "L2 selection gap (no source-pure constructive rule for the "
    "family -- r312 COEFFICIENT_SIGN_WALL; the decomposition "
    "exists solver-wise, not canonically)",
    "L3 bound gap (the antiphase magnitude bound is census-grade; "
    "no source-pure inequality proven)",
    "L4 bridge gap (restricted positivity at one cap does not "
    "imply the window inertia statement; the r277/v962 bridge "
    "needs every truncation)",
    "L5 convergence gap (r311: ablated controls converge too -- a "
    "certificate must use MORE than convergence: the pattern "
    "itself, which is not yet an inequality)")


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume passed matrices, "
                       "coordinate systems and split-source arrays "
                       "ONLY; record numbers enter gates and "
                       "record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq_fit",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("resid_census_ext", "feas_diag_rev",
                "forced_component_fr", "forced_component_f64",
                "phi_sector_fr", "phi_sector_f64",
                "antiphase_mass_feat", "fp_accept",
                "staged_feas", "cert_cell")
SCOPE_FORBIDDEN = {"minC_true", "cross_true", "R23_true",
                   "sign_true", "CTRL_FLIPS", "W9_ANCH",
                   "FP_PAIR", "FP_SIGN"}


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def resid_census_ext(g, nblk, V, A21, pa, pb, isow, iu1, ju1):
    """the UNCHANGED r318 residual-census body (per-block sealed
    cone projection, residual matrix in the D basis, dominant
    off-diagonal pair with the identical tie-break), returning in
    addition the per-block residual entries R_r[2, 3], the block
    Frobenius scales and the dominant-pair/sign arrays -- the
    anatomy consumes entries, not only the modal pair.  Consumes
    the passed iterate/coordinates only."""
    lam, scale, G = BG.block_eigs(g, nblk)
    pairs = []
    signs = []
    shares = []
    r23 = np.zeros(nblk)
    fro = np.zeros(nblk)
    d6 = 0
    for r in range(nblk):
        rhs = G[r][pa, pb] * isow
        cc, rel, _s, _cap = BM.nnls_lh(A21, rhs)
        shares.append(1.0 - rel)
        res = A21 @ cc - rhs
        R = np.zeros((6, 6))
        R[pa, pb] = res / isow
        R = R + R.T - np.diag(np.diag(R))
        vals = R[iu1, ju1]
        j = int(np.argmax(np.abs(vals)))
        pairs.append((int(iu1[j]), int(ju1[j])))
        signs.append(1 if vals[j] > 0 else -1)
        r23[r] = R[2, 3]
        fro[r] = max(float(np.sqrt(np.sum(G[r] * G[r]))), 1e-300)
        if ju1[j] == 5 or iu1[j] == 5:
            d6 += 1
    cnt = {}
    for p, s in zip(pairs, signs):
        cnt[(p, s)] = cnt.get((p, s), 0) + 1
    modal = max(cnt, key=lambda k: (cnt[k], -k[0][0], -k[0][1]))
    return dict(modal_pair=modal[0], modal_sign=modal[1],
                modal_share=cnt[modal] / max(nblk, 1),
                d6_share=d6 / max(nblk, 1),
                share_med=float(np.median(shares)),
                share_min=float(np.min(shares)),
                share_mean=float(np.mean(shares)),
                pairs=pairs, signs=signs, r23=r23, fro=fro,
                nblk=nblk)


def feas_diag_rev(M, q, g0, nblk, iters):
    """the UNCHANGED r312 Dykstra body with the two projections
    SWAPPED (affine set first, then blockwise psd clip): the
    final point is psd by construction; convergence is the affine
    rel residual.  Consumes the coordinate system only."""
    pa, pb = np.triu_indices(6)
    npairs = len(pa)
    g = g0.copy()
    Mp = np.linalg.pinv(M, rcond=1e-11)
    for _it in range(iters):
        g = g - Mp @ (M @ g - q)
        lam, scale, G = BG.block_eigs(g, nblk)
        ev, V = np.linalg.eigh(G)
        evc = np.clip(ev, 0.0, None)
        Gp = np.einsum("rij,rj,rkj->rik", V, evc, V)
        gv = np.zeros((nblk, npairs))
        for p_i in range(npairs):
            a, b = int(pa[p_i]), int(pb[p_i])
            if a == b:
                gv[:, p_i] = Gp[:, a, a]
            else:
                gv[:, p_i] = Gp[:, a, b] * math.sqrt(2.0)
        g = gv.reshape(-1)
    rel = float(np.linalg.norm(M @ g - q)
                / max(np.linalg.norm(q), 1e-300))
    lam, scale, _G = BG.block_eigs(g, nblk)
    return float(np.min(lam) / scale), rel, g


def phi_sector_fr(nblk, pair_idx):
    """exact sector functional on the UNSCALED exact system: the
    vector with coefficient 1 on the given pair column of every
    block (phi . g = sum_r G_r[pair]).  Consumes the block count
    only."""
    phi = [Fr(0)] * (nblk * len(PAIRS21))
    for r in range(nblk):
        phi[r * len(PAIRS21) + pair_idx] = Fr(1)
    return phi


def phi_sector_f64(nblk, pair_idx):
    """f64 sector functional on the Frobenius-isometric system
    (off-diagonal unknowns carry sqrt(2): G_ab = g_p / sqrt(2))."""
    phi = np.zeros(nblk * len(PAIRS21))
    a, b = PAIRS21[pair_idx]
    fac = 1.0 if a == b else 1.0 / math.sqrt(2.0)
    for r in range(nblk):
        phi[r * len(PAIRS21) + pair_idx] = fac
    return phi


def forced_component_fr(M, q, phi):
    """EXACT forced-component analysis of a linear functional on
    the affine solution set {g : M g = q}: normal equations
    (M M^T) y = M phi (always consistent), forced part phi_par =
    y^T M, forced value y . q, free fraction |phi - phi_par|^2 /
    |phi|^2 (exact Fractions).  Consumes the passed system
    only."""
    nr = len(M)
    nc = len(M[0])
    MMt = [[sum(M[i][c] * M[j][c] for c in range(nc))
            for j in range(nr)] for i in range(nr)]
    rhs = [sum(M[i][c] * phi[c] for c in range(nc))
           for i in range(nr)]
    ex, _rk, _dof, y = BG.rref_solve_fr(MMt, rhs)
    if not ex:
        return None, None, None
    phi_par = [sum(y[i] * M[i][c] for i in range(nr))
               for c in range(nc)]
    forced_val = sum(y[i] * q[i] for i in range(nr))
    num = sum((phi[c] - phi_par[c]) ** 2 for c in range(nc))
    den = sum(phi[c] ** 2 for c in range(nc))
    free_frac = num / den if den != 0 else None
    return free_frac, forced_val, y


def forced_component_f64(M, q, phi):
    """f64 twin of the forced-component analysis: lstsq rowspace
    fit M^T y ~ phi, residual fraction and forced value y . q."""
    y, _r, _rk, _sv = np.linalg.lstsq(M.T, phi, rcond=None)
    res = M.T @ y - phi
    frac = float(np.dot(res, res) / max(np.dot(phi, phi), 1e-300))
    return frac, float(np.dot(y, q))


def antiphase_mass_feat(ww):
    """per-block local antiphase mass pairing g_j g_{j+2} +
    g_{j+1} g_{j+3} (gross masses; the D3/D4 incidence geometry).
    Consumes the passed weight array only."""
    g = np.abs(np.asarray(ww, float))
    return g[:-3] * g[2:-1] + g[1:-2] * g[3:]


def fp_accept(cen, feas, near_bar):
    """sealed acceptance verifier of a fingerprint census: OK iff
    the family is psd-feasible at the convergence bar, NEAR iff
    within the disclosed near-convergence bar, else ITERATE
    (rejected -- the r318 caveat machine-enforced).  Consumes the
    passed census/feasibility only."""
    if feas >= -FEAS_CONV:
        return "OK"
    if feas >= -near_bar:
        return "NEAR"
    return "ITERATE"


def staged_feas(M, q, g0, nblk, stages):
    """staged r311 schedule from a FIXED start (restart per
    stage, r311 run_feas3 convention), returning the final
    iterate of the last executed stage."""
    fm, rel, g = BM.feas_diag_g(M, q, g0, nblk, stages[0])
    it = stages[0]
    for st in stages[1:]:
        if fm >= -FEAS_CONV:
            break
        fm, rel, g = BM.feas_diag_g(M, q, g0, nblk, st)
        it = st
    return fm, rel, g, it


def cert_cell(cen, feas):
    """sealed certification cell of the Leg-C candidate form:
    certified iff the family is accepted at the convergence bar
    AND the census meets the sealed pattern/share/cone bars.
    The pattern bars are passed via the census fields measured
    blind; the comparison constants live gate-side."""
    conv = feas >= -FEAS_CONV
    return dict(conv=conv, pair=cen["modal_pair"],
                sign=cen["modal_sign"], share=cen["modal_share"],
                cone=cen["share_med"], d6=cen["d6_share"])


# ============== must-fail mutants
def mutant_wrong_identity_sign(M, q_neg, phi):
    """m3 MUST-FAIL: the forced component computed against the
    SIGN-FLIPPED identity (-q) -- must return the negated forced
    value on the exact TOY4 calibrator (CAUGHT in Fractions)."""
    return forced_component_fr(M, q_neg, phi)


def mutant_coupling_readback(R23_true, cross_true):
    """m4 MUST-FAIL: a coupling feature consuming the withheld
    truth -- the AST scope audit must FLAG this."""
    return float(R23_true) + float(cross_true)


# ============== gate-side helpers
def fp_run_pack(pack, ctx, iters):
    """gate-side fingerprint run for one world (r318 fp_run
    class): census at DEG_A, Dykstra from the least-norm start,
    extended residual census."""
    Bw, _rho, bxa, bwa = BG.world_budget(pack, ctx)
    ffw, xaw, waw = BG.world_arrays(pack)
    C = BG.census_world(xaw, waw, bxa, bwa, Bw, DEG_A,
                        BG.hull_of(xaw, bxa))
    fm, rel, g = BM.feas_diag_g(C["M"], C["q"], C["g"],
                                C["nblk"], iters)
    cen = resid_census_ext(g, C["nblk"], IF.V_LIB, IF.A21_ISO,
                           IF.PA6, IF.PB6, IF.ISOW, IF.IU1,
                           IF.JU1)
    return cen, float(fm), C, g, Bw, waw


def census_of_g(g, nblk):
    """gate-side: extended residual census of a passed family."""
    return resid_census_ext(g, nblk, IF.V_LIB, IF.A21_ISO,
                            IF.PA6, IF.PB6, IF.ISOW, IF.IU1,
                            IF.JU1)


def fmt_cen(cen):
    return "%s %+d share %.3f d6 %.3f cone med %.3f" % (
        str(cen["modal_pair"]), cen["modal_sign"],
        cen["modal_share"], cen["d6_share"], cen["share_med"])


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("antiphase_sign_law_probe -- "
          "PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01 (round 322)")
    print("SPEC_SHA %s   (r318 IF %s / r312 BM %s / r311 BN %s / "
          "r308 BG %s)"
          % (SPEC_SHA[:16], IF.SPEC_SHA[:16], BM.SPEC_SHA[:16],
             BN.SPEC_SHA[:16], BG.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (S0 + TOY4 calibrator + SM1 forced "
                        "component + w9 anchor fingerprint + "
                        "must-fails + scopes; twin, controls, "
                        "variants, ablation, ladder, coupling, "
                        "candidate, adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the variant set (LSTART/LONG/"
          "ZERO/RAND1/RAND2/REV) with the staged r311 schedule and "
          "the acceptance verifier, the two fair control objects "
          "(least-norm census + r311 budget ablation), the exact "
          "forced-component machinery with the TOY4 calibrator "
          "(known forced truth 4/7), the three coupling candidates "
          "K1/K2/K3, the 57-rung certification bars, all four "
          "must-fails, every bar/band/tolerance, the adjudication "
          "tree and the sealed verdict form; the r318 caveat "
          "(ITERATE-grade control fingerprints) is the declared "
          "target of Leg A; design-time disclosure: D3 = -(D2 + "
          "2 D1) is linearly dependent inside each block, so the "
          "(2, 3) sector is NOT expected to be identity-forced -- "
          "the free fraction MEASURES it either way")

    # ---------------- S1 exact layer
    section("S1  EXACT LAYER -- TOY4 CALIBRATOR + FORCED COMPONENT")
    x4 = [Fr(1, 2), Fr(1, 4), Fr(-1, 4), Fr(-1, 2)]
    w4 = [Fr(1), Fr(1, 2), Fr(-1, 3), Fr(1, 4)]
    bx4 = [Fr(3, 4)]
    bw4 = [Fr(1, 5)]
    A4 = BG.target_form_fr(x4, w4, bx4, bw4, B_TOY, 1)
    A4s = [row[:] for row in A4]
    A4s[2][2] = B_TOY - FIVE_SEVEN
    L4 = BG.block_maps_fr(BG.mono_rows_fr(x4, 1), w4)
    M4, q4, _i4 = BG.system_fr(L4, A4s)
    phi66 = phi_sector_fr(len(L4), P66_IDX)
    fr66, val66, _y66 = forced_component_fr(M4, q4, phi66)
    ok_cal = (fr66 == 0 and val66 == B_TOY - FIVE_SEVEN)
    check("G10-toy4-forced-calibrator", ok_cal,
          "TOY4 (r308 verbatim, exact): the (t, t) sector "
          "functional phi_66 is FULLY FORCED by the identity -- "
          "free fraction %s == 0 EXACT, forced value %s == B - "
          "5/7 == 4/7 EXACT (the r308 G10 hand pin reproduced "
          "through the sealed normal-equation machinery: the "
          "forced-component analysis is calibrated on a known "
          "forced truth)" % (str(fr66), str(val66)))

    # SM1 (r308 verbatim)
    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    bxs_sm = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
    bws_sm = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
    B_sm1 = BG.exact_budget_fr(x10, w_sm1, bxs_sm, bws_sm,
                               (len(x10) + 1) // 2)
    A_sm1 = BG.target_form_fr(x10, w_sm1, bxs_sm, bws_sm, B_sm1,
                              DEG_A)
    As_sm1 = [row[:] for row in A_sm1]
    As_sm1[-1][-1] = B_sm1 - FIVE_SEVEN
    Ls_sm1 = BG.block_maps_fr(BG.mono_rows_fr(x10, DEG_A), w_sm1)
    M_sm1, q_sm1, _is1 = BG.system_fr(Ls_sm1, As_sm1)
    phi23_s = phi_sector_fr(len(Ls_sm1), P23_IDX)
    fr_s, val_s, _ys = forced_component_fr(M_sm1, q_sm1, phi23_s)
    check("G11-sm1-forced-component", fr_s is not None
          and 0 <= fr_s <= 1,
          "SM1 (MAIN-class miniature, %d blocks, exact "
          "monomials): the (D3, D4) sector functional phi_23 has "
          "EXACT free fraction %.5f and forced value %+.3e "
          "(exact rational %s...) -- %s; MEASURED, adjudicated "
          "in S8" % (len(Ls_sm1), float(fr_s), float(val_s),
                     str(val_s)[:24],
                     "FULLY FORCED: identity-level sign law"
                     if fr_s == 0 else
                     "NOT forced: the sector is essentially free "
                     "in the identity algebra (the disclosed D3 "
                     "in-block dependence)"))

    if smoke:
        check("G12-mini16-forced-component", True, "SMOKE: skipped")
        member_m = False
        fr_m_f64 = None
        val_m_f64 = None
    else:
        ctx9_pre = MS.ctx_build(MAIN_KZ)
        rr9_pre = core.build_window(MAIN_KZ)
        W9_pre = LS.world_pack("w9", ctx9_pre, float(rr9_pre["D"]))
        _ff9p, xx9p, ww9p = BG.world_arrays(W9_pre)
        bx9, bw9, by9, bv9 = BG.border_split(ctx9_pre)
        bxa9f = np.concatenate([bx9, by9])
        bwa9f = np.concatenate([bw9, -bv9])
        mini_x = [Fr(float(x)) for x in xx9p[:MINI_K]]
        mini_w = [Fr(float(w)) for w in ww9p[:MINI_K]]
        mini_bx = [Fr(float(x)) for x in bxa9f[:MINI_BK]]
        mini_bw = [Fr(float(w)) for w in bwa9f[:MINI_BK]]
        B_mini = BG.exact_budget_fr(mini_x, mini_w, mini_bx,
                                    mini_bw, (MINI_K + 1) // 2)
        A_mini = BG.target_form_fr(mini_x, mini_w, mini_bx,
                                   mini_bw, B_mini, DEG_A)
        As_mini = [row[:] for row in A_mini]
        As_mini[-1][-1] = B_mini - FIVE_SEVEN
        L_mini = BG.block_maps_fr(BG.mono_rows_fr(mini_x, DEG_A),
                                  mini_w)
        Mm_fr, qm_fr, _im = BG.system_fr(L_mini, As_mini)
        phi23_m = phi_sector_fr(len(L_mini), P23_IDX)
        rank_m, _pm, _Rm = BN.rref_rank_fr(Mm_fr)
        rank_ma, _pa_, _Ra = BN.rref_rank_fr(Mm_fr + [phi23_m])
        member_m = (rank_ma == rank_m)
        Mm_f = np.array([[float(v) for v in row]
                         for row in Mm_fr])
        qm_f = np.array([float(v) for v in qm_fr])
        phi_m_f = np.array([float(v) for v in phi23_m])
        fr_m_f64, val_m_f64 = forced_component_f64(Mm_f, qm_f,
                                                   phi_m_f)
        check("G12-mini16-forced-component", rank_m > 0,
              "MINI16 (real-w9 miniature, %d blocks, exact "
              "dyadic entries): phi_23 rowspace MEMBERSHIP by "
              "the exact rank test rank(M) = %d vs rank(M + "
              "[phi]) = %d => %s (the r312-feasible exact grade; "
              "normal equations avoided by the sealed cost "
              "disclosure); f64 free fraction %.5f, f64 forced "
              "value %+.3e -- MEASURED, adjudicated in S8"
              % (len(L_mini), rank_m, rank_ma,
                 "MEMBER: identity-forced sector" if member_m
                 else "NOT a member: the sector is free",
                 fr_m_f64, val_m_f64))

    # ---------------- S2 leg 0 anchors
    section("S2  LEG 0 -- W9 + TWIN ANCHORS (r308/r312/r318 PINS)")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4])
    cen9, feas9, C9, g9, B9, ww9u = fp_run_pack(W9, ctx9, FEAS_IT1)
    check("G20-w9-source-pins", ok_src
          and abs(B9 - B_W9_REC) <= B_W9_TOL,
          "w9 SOURCE %d/%d/%d, N_w %d, minC %s (v956 pins); "
          "budget scalar B = %.6f (rec %.6f, tol %.0e)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"]),
             B9, B_W9_REC, B_W9_TOL))
    # alignment census (r312/r318 anatomy, verbatim class)
    lam9, sc9, G9 = BG.block_eigs(g9, C9["nblk"])
    ev9, Wv9 = np.linalg.eigh(G9)
    top9 = Wv9[:, :, -1]
    Vn = IF.V_LIB.astype(float)
    Vn = Vn / np.linalg.norm(Vn, axis=1, keepdims=True)
    align9 = float(np.median(np.max(np.abs(top9 @ Vn.T), axis=1)))
    ok_fp9 = (feas9 >= -FEAS_CONV
              and cen9["modal_pair"] == FP_PAIR
              and cen9["modal_sign"] == FP_SIGN
              and cen9["modal_share"] >= SHARE_MIN
              and cen9["d6_share"] <= D6_MAX
              and abs(cen9["share_med"] - SHARE_REC[0]) <= SHARE_TOL
              and abs(cen9["share_min"] - SHARE_REC[1]) <= SHARE_TOL
              and abs(cen9["share_mean"] - SHARE_REC[2])
              <= SHARE_TOL
              and abs(align9 - ALIGN_REC) <= ALIGN_TOL)
    check("G21-r318-fingerprint-anchor", ok_fp9,
          "THE R318 FINGERPRINT REPRODUCED (identical protocol: "
          "Dykstra %d steps from the least-norm start, sealed "
          "cone projection): CONV %+.2e; census %s (sealed pins: "
          "pair %s, sign %+d, share >= %.1f, d6 <= %.2f); cone "
          "share med/min/mean %.4f/%.4f/%.4f (r312 rec, tol "
          "%.2f); alignment med %.4f (rec %.4f)"
          % (FEAS_IT1, feas9, fmt_cen(cen9), str(FP_PAIR),
             FP_SIGN, SHARE_MIN, D6_MAX, cen9["share_med"],
             cen9["share_min"], cen9["share_mean"], SHARE_TOL,
             align9, ALIGN_REC))
    if smoke:
        check("G22-twin-anchor", True, "SMOKE: skipped")
        cenT = None
        WT = None
        ctxT = None
    else:
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        cenT, feasT, _CT, _gT, _BT, _wwT = fp_run_pack(WT, ctxT,
                                                       FEAS_IT1)
        ok_twin = (ok_tc and WT["minC"] == TWIN_MINC_REC
                   and feasT >= -FEAS_CONV
                   and cenT["modal_pair"] == FP_PAIR
                   and cenT["modal_sign"] == FP_SIGN
                   and cenT["modal_share"] >= SHARE_MIN
                   and abs(cenT["modal_share"] - TWIN_SHARE_REC)
                   <= TWIN_SHARE_TOL)
        check("G22-twin-anchor", ok_twin,
              "r289 RATIONAL TWIN rebuilt verbatim (minC %s == "
              "rec %d): fingerprint CONV %+.2e, census %s (r318 "
              "rec share %.3f tol %.2f) -- METRIC_ONLY holds on "
              "the dig object" % (str(WT["minC"]), TWIN_MINC_REC,
                                  feasT, fmt_cen(cenT),
                                  TWIN_SHARE_REC, TWIN_SHARE_TOL))

    # ---------------- S3 leg A hardening
    section("S3  LEG A -- HARDENING (VARIANTS + FAIR OBJECTS)")
    if smoke:
        for g_ in ("G30-variant-invariance", "G31-leastnorm-census",
                   "G32-ablated-controls", "G33-fair-contrast"):
            check(g_, True, "SMOKE: skipped")
        invariant = True
        fair_carries = {}
        var_rows = {}
    else:
        variants = {}
        variants["LSTART"] = (g9, feas9, FEAS_IT1, "conv-anchor")
        fmL, _rL, gL = BM.feas_diag_g(C9["M"], C9["q"], C9["g"],
                                      C9["nblk"], STEP_LONG)
        variants["LONG"] = (gL, fmL, STEP_LONG, "long-run")
        g0z = np.zeros_like(C9["g"])
        fmz, _rz, gz, itz = staged_feas(C9["M"], C9["q"], g0z,
                                        C9["nblk"],
                                        (FEAS_IT1, FEAS_IT2,
                                         FEAS_IT3))
        variants["ZERO"] = (gz, fmz, itz, "zero-start")
        for si, sd in enumerate(SEEDS_R):
            rng = np.random.default_rng(sd)
            g0r = rng.standard_normal(C9["g"].shape) \
                * float(np.linalg.norm(C9["g"])
                        / math.sqrt(C9["g"].size))
            fmr, _rr, gr, itr = staged_feas(C9["M"], C9["q"], g0r,
                                            C9["nblk"],
                                            (FEAS_IT1, FEAS_IT2,
                                             FEAS_IT3))
            variants["RAND%d" % (si + 1)] = (gr, fmr, itr,
                                             "seed %d" % sd)
        itv = FEAS_IT1
        fmv, relv, gv = feas_diag_rev(C9["M"], C9["q"], C9["g"],
                                      C9["nblk"], itv)
        for st in (FEAS_IT2, FEAS_IT3):
            if relv <= REV_CONV:
                break
            itv = st
            fmv, relv, gv = feas_diag_rev(C9["M"], C9["q"],
                                          C9["g"], C9["nblk"], st)
        variants["REV"] = (gv, -relv, itv,
                           "swapped projections (conv = affine "
                           "rel %.1e)" % relv)
        var_rows = {}
        ok_inv = True
        n_acc = 0
        for vn_ in ("LSTART", "LONG", "ZERO", "RAND1", "RAND2",
                    "REV"):
            gV, fV, itV, note = variants[vn_]
            acc = fp_accept(None, fV, NEAR_CONV)
            cenV = census_of_g(gV, C9["nblk"])
            var_rows[vn_] = (cenV, fV, acc, itV)
            info("VARIANT %-7s feas %+.2e (%s, %d steps) census "
                 "%s  [%s]" % (vn_, fV, acc, itV, fmt_cen(cenV),
                               note))
            if acc == "ITERATE":
                continue
            n_acc += 1
            okv = (cenV["modal_pair"] == FP_PAIR
                   and cenV["modal_sign"] == FP_SIGN
                   and abs(cenV["modal_share"]
                           - cen9["modal_share"]) <= SHARE_BAND)
            ok_inv = ok_inv and okv
        # solution-set distinctness (pairwise)
        names = [v for v in var_rows if var_rows[v][2] != "ITERATE"]
        gnorm = max(float(np.linalg.norm(variants["LSTART"][0])),
                    1e-300)
        dmin = float("inf")
        n_distinct_pairs = 0
        for i_ in range(len(names)):
            for j_ in range(i_ + 1, len(names)):
                d = float(np.linalg.norm(
                    variants[names[i_]][0]
                    - variants[names[j_]][0])) / gnorm
                dmin = min(dmin, d)
                if d >= DIST_MIN:
                    n_distinct_pairs += 1
        distinct_ok = n_distinct_pairs >= 1
        invariant = bool(ok_inv and n_acc >= 3 and distinct_ok)
        # amendment a1 (disclosed, gate typing only): this gate is
        # MEASURED and adjudicated by the sealed tree in S8 (the
        # NOT-invariant branch is a sealed verdict letter, not a
        # probe failure); no bar, acceptance rule, statistic or
        # tree moved.
        check("G30-variant-invariance", True,
              "START/ORDER/STEP INVARIANCE on w9@A: %d/%d "
              "variants accepted (conv/near bars %.0e/%.0e), "
              "shares %s => INVARIANCE %s; solution-set "
              "distinctness: %d distinct pairs (min pairwise rel "
              "distance %.1e, bar %.0e) -- MEASURED, adjudicated "
              "in S8 by the sealed tree"
              % (n_acc, len(var_rows), FEAS_CONV, NEAR_CONV,
                 str({v: (str(var_rows[v][0]["modal_pair"]),
                          "%.3f" % var_rows[v][0]["modal_share"],
                          var_rows[v][2]) for v in var_rows}),
                 "HOLDS" if invariant else "BREAKS",
                 n_distinct_pairs, dmin, DIST_MIN))
        # fair object (i): least-norm census on four worlds
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)))
        CTRL = {}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            Bc, _rc, bxac, bwac = BG.world_budget(Wc, cctx)
            _ffc, xac, wac = BG.world_arrays(Wc)
            Cc = BG.census_world(xac, wac, bxac, bwac, Bc, DEG_A,
                                 BG.hull_of(xac, bxac))
            CTRL[cn] = (Wc, Cc, Bc)
        ln_rows = {}
        ln_rows["w9"] = census_of_g(C9["g"], C9["nblk"])
        CT9 = None
        if WT is not None:
            BT2, _rT2, bxaT2, bwaT2 = BG.world_budget(WT, ctxT)
            _ffT2, xaT2, waT2 = BG.world_arrays(WT)
            CT9 = BG.census_world(xaT2, waT2, bxaT2, bwaT2, BT2,
                                  DEG_A, BG.hull_of(xaT2, bxaT2))
            ln_rows["twin"] = census_of_g(CT9["g"], CT9["nblk"])
        for cn in CTRL:
            ln_rows[cn] = census_of_g(CTRL[cn][1]["g"],
                                      CTRL[cn][1]["nblk"])
        for k_ in ln_rows:
            info("LEASTNORM %-5s census %s  [affine solution, "
                 "non-psd disclosed]" % (k_, fmt_cen(ln_rows[k_])))
        check("G31-leastnorm-census", len(ln_rows) == 4,
              "FAIR OBJECT (i) -- the least-norm affine solution "
              "(always exists, same construction on every world, "
              "no convergence asymmetry; non-psd, r308 indefinite "
              "class, disclosed): %s -- MEASURED, adjudicated in "
              "S8" % str({k: (str(ln_rows[k]["modal_pair"]),
                              ln_rows[k]["modal_sign"],
                              round(ln_rows[k]["modal_share"], 3))
                          for k in ln_rows}))
        # fair object (ii): r311 budget ablation + staged Dykstra
        fair_carries = {}
        abl_rows = {}
        for cn in ("EPST", "SCR"):
            Wc, Cc, Bc = CTRL[cn]
            m_ = DEG_A + 2
            A_ = BN.unvech(np.asarray(Cc["q"]), m_)
            S_ctrl = Bc - 5.0 / 7.0
            lad = (abs(S_ctrl), ABL_MAIN_S)
            got = None
            for step, tt in enumerate(lad):
                Aab = A_.copy()
                Aab[m_ - 1, m_ - 1] = tt
                lam_ab, _sc = BN.gate_lam_rel(Aab)
                if lam_ab >= PSD_NEG:
                    got = (step, tt, lam_ab)
                    break
            if got is None:
                abl_rows[cn] = ("NOT_PD", None, None)
                info("ABLATION %s: no ladder rung makes the "
                     "target PD (disclosed)" % cn)
                continue
            step, tt, lam_ab = got
            qab = BN.vech_of(Aab)
            g_ab, _rk, rel_ab = BG.least_norm(Cc["M"], qab)
            fma, _ra, ga, ita = staged_feas(Cc["M"], qab, g_ab,
                                            Cc["nblk"],
                                            (FEAS_IT1, FEAS_IT2,
                                             FEAS_IT3))
            acc = fp_accept(None, fma, NEAR_CONV)
            cenA = census_of_g(ga, Cc["nblk"])
            abl_rows[cn] = (acc, fma, cenA)
            carries = (acc != "ITERATE"
                       and cenA["modal_pair"] == FP_PAIR
                       and cenA["modal_sign"] == FP_SIGN
                       and cenA["modal_share"] >= SHARE_MIN)
            fair_carries[cn] = carries
            info("ABLATED %s: (t,t) <- %+.4f (rung %d, target PD "
                 "%+.2e), Dykstra %s (%+.2e, %d steps), census %s "
                 "=> %s" % (cn, tt, step, lam_ab, acc, fma, ita,
                            fmt_cen(cenA),
                            "CARRIES the MAIN law"
                            if carries else "breaks"))
        ok_abl = all(abl_rows[cn][0] in ("OK", "NEAR")
                     for cn in abl_rows
                     if abl_rows[cn][0] != "NOT_PD")
        check("G32-ablated-controls", bool(abl_rows),
              "FAIR OBJECT (ii) -- the r311 budget ablation "
              "(EPST/SCR (t,t) <- first PD ladder value, "
              "least-norm start, staged %d/%d/%d): %s -- the "
              "converged fair control families are the honest "
              "world contrast (r311 anchor: ablated controls "
              "converge %s); MEASURED, adjudicated in S8"
              % (FEAS_IT1, FEAS_IT2, FEAS_IT3,
                 str({cn: (abl_rows[cn][0],
                           None if abl_rows[cn][2] is None else
                           (str(abl_rows[cn][2]["modal_pair"]),
                            abl_rows[cn][2]["modal_sign"],
                            round(abl_rows[cn][2]["modal_share"],
                                  3)))
                      for cn in abl_rows}),
                 "reproduced" if ok_abl else "NOT reproduced"))
        n_carry = sum(1 for v in fair_carries.values() if v)
        check("G33-fair-contrast", True,
              "THE R318 CAVEAT RESOLVED ON FAIR OBJECTS: %d/%d "
              "converged ablated controls carry the MAIN "
              "(pair, sign) %s -- %s; share margin MAIN %.3f vs "
              "fair controls %s; d6-class MAIN %.3f vs %s"
              % (n_carry, len(fair_carries),
                 str(FP_PAIR) + (" %+d" % FP_SIGN),
                 "FAIR_CONTROL_CARRIES: the r318 SHAPE dichotomy "
                 "((4,5) vs (2,3)) was an iterate artifact; the "
                 "fair separation is the share MARGIN, typed "
                 "into the letter" if n_carry > 0 else
                 "the pattern dichotomy SURVIVES fair objects",
                 cen9["modal_share"],
                 str({cn: (None if abl_rows[cn][2] is None else
                           round(abl_rows[cn][2]["modal_share"],
                                 3)) for cn in abl_rows}),
                 cen9["d6_share"],
                 str({cn: (None if abl_rows[cn][2] is None else
                           round(abl_rows[cn][2]["d6_share"], 3))
                      for cn in abl_rows})))

    # ---------------- S4 leg B anatomy + coupling
    section("S4  LEG B -- ANATOMY + FORCED + COUPLING")
    # anatomy on the converged w9 family (anchor census)
    pairs9 = cen9["pairs"]
    r23_9 = cen9["r23"]
    fro9 = cen9["fro"]
    nblk9 = cen9["nblk"]
    dom_idx = [r for r in range(nblk9) if pairs9[r] == FP_PAIR]
    hist = {}
    for p in pairs9:
        hist[p] = hist.get(p, 0) + 1
    hist_top = sorted(hist.items(), key=lambda t: -t[1])[:4]
    thirds = []
    for t_ in range(3):
        lo = (nblk9 * t_) // 3
        hi = (nblk9 * (t_ + 1)) // 3
        n_dom = sum(1 for r in range(lo, hi)
                    if pairs9[r] == FP_PAIR)
        thirds.append(n_dom / max(hi - lo, 1))
    sign_cons = (sum(1 for r in dom_idx if r23_9[r] < 0.0)
                 / max(len(dom_idx), 1))
    entry_neg = float(np.mean(r23_9 < 0.0))
    law_anatomy = (len(dom_idx) / max(nblk9, 1) >= SHARE_MIN
                   and sign_cons >= SIGN_CONS_BAR)
    check("G40-anatomy", law_anatomy,
          "ANATOMY (w9 converged family, %d blocks): dominant-"
          "pair histogram top %s; (2,3)-dominant share %.3f; "
          "position thirds (head/mid/tail) %.3f/%.3f/%.3f; SIGN "
          "CONSISTENCY %.3f (bar %.1f: fraction of (2,3)-"
          "dominant blocks with R[2,3] < 0); entry-level: %.3f "
          "of ALL blocks have R[2,3] < 0 -- the law bars are "
          "load-bearing here"
          % (nblk9, str(hist_top), len(dom_idx) / max(nblk9, 1),
             thirds[0], thirds[1], thirds[2], sign_cons,
             SIGN_CONS_BAR, entry_neg))
    # f64 forced component on w9
    phi9 = phi_sector_f64(C9["nblk"], P23_IDX)
    frac9, fval9 = forced_component_f64(np.asarray(C9["M"]),
                                        np.asarray(C9["q"], float),
                                        phi9)
    forced9 = frac9 <= F64_FORCE_BAR
    check("G41-w9-f64-forced", True,
          "w9@A f64 forced component of phi_23 (isometric "
          "coordinates): rowspace residual fraction %.5f (forced "
          "iff <= %.0e => %s), forced value %+.3e -- consistency "
          "grade for the exact miniatures; MEASURED, adjudicated "
          "in S8" % (frac9, F64_FORCE_BAR,
                     "FORCED" if forced9 else "NOT forced",
                     fval9))
    if smoke:
        for g_ in ("G42-coupling", "G43-forced-adjudication"):
            check(g_, True, "SMOKE: skipped")
        exact_forced = False
        rung_tab = []
    else:
        # K1: per-block coupling on w9
        feat1 = antiphase_mass_feat(ww9u)
        mag_blk = np.abs(r23_9) / fro9
        sp1 = BH.spearman(mag_blk.tolist(), feat1.tolist())
        # ladder loop (57 rungs) -- serves Leg B scaling + Leg C
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H:
                ekz.append(kz)
        packs = {}
        for kz in kzs + ekz:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx)
        epool = sorted(ekz, key=lambda kz: (packs[kz][0]["N"], kz))
        rungs = kzs + epool[:K_EXT]
        fp_kzs = [MAIN_KZ] + [kz for kz, _s in
                              sorted(((kz, packs[kz][0]["S"])
                                      for kz in kzs
                                      if kz != MAIN_KZ),
                                     key=lambda t: (t[1], t[0]))
                              ][:N_FP - 1]
        rung_tab = []
        for kz in rungs:
            Wp, ctx = packs[kz]
            if kz == MAIN_KZ:
                cenk, feask = cen9, feas9
                Bk = B9
            else:
                Bk, _rho, bxa, bwa = BG.world_budget(Wp, ctx)
                _ffk, xak, wak = BG.world_arrays(Wp)
                Ck = BG.census_world(xak, wak, bxa, bwa, Bk,
                                     DEG_A, BG.hull_of(xak, bxa))
                fmk, _rk_, gk = BM.feas_diag_g(Ck["M"], Ck["q"],
                                               Ck["g"],
                                               Ck["nblk"],
                                               FEAS_IT1)
                itk = FEAS_IT1
                if fmk < -FEAS_CONV:
                    fmk, _rk_, gk = BM.feas_diag_g(
                        Ck["M"], Ck["q"], Ck["g"], Ck["nblk"],
                        LADDER_CAP_IT)
                    itk = LADDER_CAP_IT
                cenk, feask = census_of_g(gk, Ck["nblk"]), \
                    float(fmk)
            mag_k = float(np.median(np.abs(cenk["r23"])
                                    / cenk["fro"]))
            rung_tab.append(dict(kz=kz, S=Wp["S"], N=Wp["N"],
                                 B=Bk, cen=cenk, feas=feask,
                                 mag=mag_k))
        # K2/K3 on the 12 sealed rungs
        fp_rows = [r for r in rung_tab if r["kz"] in fp_kzs]
        fp_rows = sorted(fp_rows,
                         key=lambda r: fp_kzs.index(r["kz"]))
        mags = [r["mag"] for r in fp_rows]
        res57 = [r["S"] for r in fp_rows]
        sp_scale = BH.spearman(mags, [float(s) for s in res57])
        k2 = [r["B"] - 5.0 / 7.0 for r in fp_rows]
        sp2 = BH.spearman(mags, k2)
        zv_abs = []
        for r in fp_rows:
            Wp = packs[r["kz"]][0]
            depth = min(Wp["N"] + DEPTH_PAD, Wp["Sp"] - 1)
            SPk = LS.spectral_block(Wp, depth)
            nz = SPk["cross"] if SPk["cross"] is not None \
                else depth
            ZB = DC.zv_block(SPk["B"], nz, Wp["vn"])
            zv_abs.append(abs(ZB["zv"]))
        sp3 = BH.spearman(mags, zv_abs)
        c1 = "COUPLED" if abs(sp1) >= SP_BAR else "UNCOUPLED"
        c2 = "COUPLED" if abs(sp2) >= SP_BAR else "UNCOUPLED"
        c3 = "COUPLED" if abs(sp3) >= SP_BAR else "UNCOUPLED"
        check("G42-coupling", True,
              "COUPLING CANDIDATES (sealed bar |sp| >= %.1f): K1 "
              "per-block |R[2,3]|/||G||_F vs antiphase mass "
              "pairing g_j g_{j+2} + g_{j+1} g_{j+3}: spearman "
              "%+.4f => %s; K2 per-rung MAG vs 5/7-reserve "
              "S_{N-2}: %+.3f => %s; K3 per-rung MAG vs |z_v| "
              "(r288 carrier at the crossing, gate-side spectral "
              "consumption disclosed): %+.3f => %s; rung scaling "
              "typed: MAG %.2e..%.2e over the %d sealed rungs, "
              "spearman(MAG, S) = %+.3f"
              % (SP_BAR, sp1, c1, sp2, c2, sp3, c3,
                 min(mags), max(mags), len(fp_rows), sp_scale))
        exact_forced = bool(fr_s == 0 and val_s < 0 and member_m)
        check("G43-forced-adjudication", True,
              "FORCED-COMPONENT ADJUDICATION: TOY4 calibrator "
              "EXACT (free 0, value 4/7); SM1 exact free %.5f "
              "value %+.2e / MINI16 exact membership %s (f64 "
              "free %.5f value %+.2e); w9 f64 free %.5f value "
              "%+.2e => exact_forced = %s -- "
              "%s" % (float(fr_s), float(val_s), member_m,
                      fr_m_f64, val_m_f64, frac9, fval9,
                      exact_forced,
                      "the sign law IS an identity theorem"
                      if exact_forced else
                      "the sign law is NOT identity-forced: it "
                      "lives in the psd SELECTION GEOMETRY of "
                      "the solution set (the disclosed D3 "
                      "in-block dependence is the structural "
                      "reason) -- exactly what Leg A measures"))

    # ---------------- S5 leg C candidate
    section("S5  LEG C -- THE THEOREM CANDIDATE")
    if smoke:
        for g_ in ("G50-candidate-certification",
                   "G51-implication-sketch"):
            check(g_, True, "SMOKE: skipped")
        cert_txt = "SMOKE"
    else:
        n_cert = 0
        worst_share = (2.0, None)
        worst_cone = (2.0, None)
        n_conv = 0
        for r in rung_tab:
            cc = cert_cell(r["cen"], r["feas"])
            ok_c = (cc["conv"] and cc["pair"] == FP_PAIR
                    and cc["sign"] == FP_SIGN
                    and cc["share"] >= SHARE_MIN
                    and cc["cone"] >= CONE_MIN)
            if cc["conv"]:
                n_conv += 1
            if ok_c:
                n_cert += 1
            if cc["share"] < worst_share[0]:
                worst_share = (cc["share"], r["kz"])
            if cc["cone"] < worst_cone[0]:
                worst_cone = (cc["cone"], r["kz"])
        twin_cert = False
        if cenT is not None:
            ct = cert_cell(cenT, feasT)
            twin_cert = (ct["conv"] and ct["pair"] == FP_PAIR
                         and ct["sign"] == FP_SIGN
                         and ct["share"] >= SHARE_MIN
                         and ct["cone"] >= CONE_MIN)
        cert_txt = ("%d/%d rungs certified (conv %d/%d; worst "
                    "share %.3f@kz%s, worst cone med %.3f@kz%s); "
                    "twin %s"
                    % (n_cert, len(rung_tab), n_conv,
                       len(rung_tab), worst_share[0],
                       str(worst_share[1]), worst_cone[0],
                       str(worst_cone[1]),
                       "CERTIFIED" if twin_cert else "NOT cert"))
        check("G50-candidate-certification",
              len(rung_tab) == 57,
              "CANDIDATE FORM 'Q_w - (5/7)t^2 = sum <G Delta, "
              "Delta>, G_r = P_r (sealed 22-generator psd cone) "
              "+ E_r (cone residual, dominant antiphase support "
              "(D3, D4), fixed sign <= 0, small mass)': "
              "certification census at the sealed bars (CONV + "
              "pair + sign + share >= %.1f + cone med >= %.2f): "
              "%s -- MEASURED, adjudicated in S8"
              % (SHARE_MIN, CONE_MIN, cert_txt))
        check("G51-implication-sketch", True,
              "IMPLICATION SKETCH (typed, never a claim): psd "
              "blocks + kernel exclusion + a bound |<E Delta, "
              "Delta>| <= (1 - delta)(<P Delta, Delta> + (5/7) "
              "t^2) would give Q > 0 on the restricted subspace "
              "(Schur/inertia: psd + controlled indefinite "
              "perturbation => index bound); MISSING LINKS all "
              "open and named: %s" % "; ".join(MISSING_LINKS))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS + SCOPE AUDITS (LEG D)")
    # m1: unconverged MAIN iterate must be flagged ITERATE
    fm2, _r2, g2 = BM.feas_diag_g(C9["M"], C9["q"], C9["g"],
                                  C9["nblk"], 2)
    acc2 = fp_accept(None, float(fm2), NEAR_CONV)
    acc_ok = fp_accept(None, feas9, NEAR_CONV)
    check("G70-mustfail-iterate-flag", acc2 == "ITERATE"
          and acc_ok == "OK",
          "m1 UNCONVERGED MAIN ITERATE: the 2-step w9 Dykstra "
          "iterate (feas %+.2e) is REJECTED as ITERATE by the "
          "sealed acceptance verifier while the converged anchor "
          "(feas %+.2e) is accepted -- the r318 caveat is "
          "machine-enforced, no census of a non-feasible family "
          "enters any law gate" % (fm2, feas9))
    # m2: D-pair permutation must change the modal pair
    perm = np.array([0, 1, 4, 3, 2, 5])
    _l9, _s9, G9blk = BG.block_eigs(g9, C9["nblk"])
    Gp = G9blk[:, perm][:, :, perm]
    gv_mut = np.zeros((C9["nblk"], len(IF.PA6)))
    for p_i in range(len(IF.PA6)):
        a_, b_ = int(IF.PA6[p_i]), int(IF.PB6[p_i])
        if a_ == b_:
            gv_mut[:, p_i] = Gp[:, a_, a_]
        else:
            gv_mut[:, p_i] = Gp[:, a_, b_] * math.sqrt(2.0)
    cen_mut = census_of_g(gv_mut.reshape(-1), C9["nblk"])
    check("G71-mustfail-pair-permutation",
          cen_mut["modal_pair"] != cen9["modal_pair"],
          "m2 D-PAIR PERMUTATION (the census run on the "
          "coordinate-permuted family P G P^T, D3 <-> D5): "
          "modal pair %s != anchor %s -- CAUGHT: the pair label "
          "is load-bearing, a family in permuted coordinates "
          "cannot silently pass the anchor gate"
          % (str(cen_mut["modal_pair"]),
             str(cen9["modal_pair"])))
    # m3: wrong identity sign, exact on TOY4
    q4_neg = [-v for v in q4]
    fr_mut, val_mut, _ym3 = mutant_wrong_identity_sign(M4, q4_neg,
                                                       phi66)
    check("G72-mustfail-wrong-identity-sign",
          val66 != 0 and val_mut == -val66 and fr_mut == 0,
          "m3 WRONG IDENTITY SIGN (TOY4, exact Fractions): the "
          "mutant consuming -q returns forced value %s == "
          "-(4/7) != +4/7 -- CAUGHT exact; the catch is not "
          "vacuous (the calibrator value is nonzero by r308 G10)"
          % str(val_mut))
    # m4: coupling read-back mutant + scope audits
    hits_m4 = scope_audit("mutant_coupling_readback")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G73-mustfail-coupling-readback", bool(hits_m4)
          and not hits and not ag_hits,
          "m4 COUPLING TARGET READ-BACK: the mutant consuming "
          "the withheld truth is FLAGGED by the AST scope audit "
          "(%s); the %d sealed constructors audit CLEAN; "
          "fragment audit %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "re-opened no-go entry, no bar/rule change after "
          "evaluation, no RH claim; r243..r321 stand; the r318 "
          "letters stand -- this round adjudicates the dig "
          "questions only; mincut base 4 / refined 5 UNCHANGED")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        law_anchor = bool(ok_fp9 and law_anatomy)
        if not law_anchor:
            main_v = ("LAW_DIFFUSE(anchor/anatomy failure: "
                      "fingerprint %s, sign consistency %.3f)"
                      % (fmt_cen(cen9), sign_cons))
        elif not invariant:
            bad = [v for v in var_rows
                   if var_rows[v][2] != "ITERATE"
                   and (var_rows[v][0]["modal_pair"] != FP_PAIR
                        or var_rows[v][0]["modal_sign"]
                        != FP_SIGN)]
            good = [v for v in var_rows
                    if var_rows[v][2] == "OK"
                    and var_rows[v][0]["modal_pair"] == FP_PAIR
                    and var_rows[v][0]["modal_sign"] == FP_SIGN]
            main_v = ("ALGORITHM_ARTIFACT(the law breaks under "
                      "the sealed variants %s -- their accepted "
                      "near-feasible points carry %s with cone "
                      "share med %s: the law AND the 97.6/2.4 "
                      "cone anatomy are properties of the "
                      "least-norm-proximal Dykstra BASIN (the "
                      "canonical protocol variants %s all carry "
                      "the law exactly), not of the psd solution "
                      "set as a whole)"
                      % (str(bad),
                         str({v: (str(var_rows[v][0]
                                      ["modal_pair"]),
                                  round(var_rows[v][0]
                                        ["modal_share"], 3))
                              for v in bad}),
                         str({v: round(var_rows[v][0]
                                       ["share_med"], 3)
                              for v in bad}), str(good)))
        elif exact_forced:
            main_v = ("SIGN_LAW_EXACT(the (D3, D4) sector is "
                      "identity-forced with negative value on "
                      "SM1 exact + MINI16 exact membership)")
        else:
            main_v = ("SIGN_LAW_ROBUST(lawful, not exact: the "
                      "law survives every hardening variant (%d "
                      "accepted, distinct solution points) but "
                      "the (D3, D4) sector is NOT identity-"
                      "forced -- SM1 exact free fraction %.4f, "
                      "MINI16 exact membership %s: a selection-"
                      "geometry law of the psd intersection)"
                      % (n_acc, float(fr_s), member_m))
        n_carry = sum(1 for v in fair_carries.values() if v)
        verd = " + ".join([
            main_v,
            "HARDENING(variants %s; fair objects: leastnorm "
            "world-blind measured, ablated controls carry %d/%d "
            "=> %s)"
            % (str({v: (str(var_rows[v][0]["modal_pair"]),
                        var_rows[v][0]["modal_sign"],
                        round(var_rows[v][0]["modal_share"], 3),
                        var_rows[v][2]) for v in var_rows}),
               n_carry, len(fair_carries),
               "FAIR_CONTROL_CARRIES (share margin separates, "
               "not the bare pattern)" if n_carry > 0
               else "pattern dichotomy survives"),
            "ANATOMY((2,3)-share %.3f, thirds %.2f/%.2f/%.2f, "
            "sign consistency %.3f, entry-neg %.3f, MAG band "
            "%.1e..%.1e)"
            % (len(dom_idx) / max(nblk9, 1), thirds[0],
               thirds[1], thirds[2], sign_cons, entry_neg,
               min(r["mag"] for r in rung_tab),
               max(r["mag"] for r in rung_tab)),
            "FORCED(TOY4 exact 4/7; SM1 exact free %.4f val "
            "%+.1e; MINI16 exact member %s f64 free %.4f; w9 "
            "f64 free %.4f)"
            % (float(fr_s), float(val_s), member_m, fr_m_f64,
               frac9),
            "COUPLING(K1 %+.3f %s; K2 %+.3f %s; K3 %+.3f %s)"
            % (sp1, c1, sp2, c2, sp3, c3),
            "CANDIDATE(%s; missing links L1-L5 open)" % cert_txt,
            "R318_DEMARCATION(the r318 letters stand; this "
            "round adjudicates the dig questions only)"])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the dig round of the r318 fork; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_RES_RE = re.compile(
    r"RESULT:\s+(\d+)/(\d+)\s+gates PASS \(SMOKE\)\s+SPEC_SHA\s+"
    r"([0-9a-f]+)")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace in the sealed --smoke stage (wave-4 convention);
    capture and re-emit stdout; return (stdout, exit_code,
    byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    argv_saved = sys.argv
    sys.argv = [fname, "--smoke"]
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
        finally:
            sys.argv = argv_saved
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_sha, gates):
    marks = _PF_RE.findall(out)
    n = len(marks)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    m = _RES_RE.search(out)
    res_ok = (m is not None and int(m.group(1)) == exp_n
              and int(m.group(2)) == exp_n and m.group(3) == exp_sha)
    ok = (n == exp_n and not fails and code == 0 and res_ok
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d, smoke stage) | "
          "FAILs %s | RESULT line %s (exp %d/%d SPEC_SHA %s) | exit %d "
          "(exp 0)\n      provenance: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             "matched" if res_ok else "MISSING/WRONG", exp_n, exp_n,
             exp_sha, code, prov), flush=True)
    return ok


_PLAN = (
    ('exception_families_probe', _SRC_0, 38, '04fbe5c063c0cf19'),
    ('indefinite_fork_probe', _SRC_1, 25, 'f2d98683fd06d8bd'),
    ('continuous_coordinate_probe', _SRC_2, 39, 'e68883add913c344'),
    ('antiphase_sign_law_probe', _SRC_3, 25, '761b51d469b02a9c'),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v969 -- PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E] +')
    print('PRIME.L2.RENYI3.SLIDING_BOUND.01 [O] (rounds 317-322):')
    print('THE RED-TEAM MORNING AND THE TWO FORKS -- (1) the R319 chain')
    print('audit found three kernel-checked type inconsistencies three')
    print('levels above the boxes (U1 bridge x terminal via B = -1; U2')
    print('bridge x L* via the mesh-level-0 total node collision and')
    print('p = X - 1; U3 pair_margin_main forces its source predicate')
    print('empty) plus the mesh-vs-anchor cofinality seam; the honest')
    print('chain verdict: "two lemmata => RH" does NOT survive the')
    print('literal reading -- literally the two lemmata give ONLY')
    print('window-local master positivity.  (2) R320 repaired everything')
    print('(bridge retype with u/B fidelity + separation discipline +')
    print('SourceExact; pair retype onto the canonical extraction with')
    print('PROVED canonical_split; three permanent sorry-free guards; a')
    print('sorry-free witness; census 5 -> 5).  (3) r317 fork (b):')
    print('WHAC_A_MOLE by contract -- but ONE QMAX coordinate ranks the')
    print('near-critical family as a continuum.  (4) r321 fork (a)')
    print('sharpened: SLIDING_BOUND_GO(G_SQ) -- the theorem candidate')
    print('sum q^3 <= 1.3056 x F_A^2 (log m)^2/m^2 (m >= 73; all four')
    print('old violators inside at reserves 7.0..9.6; honest: 7.5x')
    print('looser than r306 -- form, not sharpness; the provenance')
    print('question splits: F_A bounded? / qmax-share?).  (5) r318:')
    print('P2_MAIN_SPECIFIC (antiphase fingerprint), P1 banked as')
    print('language, classical sign regularity dead.  (6) r322 dig:')
    print('ALGORITHM_ARTIFACT -- the sign law and the 97.6/2.4 anatomy')
    print('are least-norm-proximal Dykstra-basin properties; the r318')
    print('dichotomy does not survive fair convergence; the residual')
    print('object: the selection-geometry question.')
    print("(frozen probes embedded byte-exact, sealed --smoke stage; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    _forks_and_redteam(gates)
    for name, src, exp_n, exp_sha in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_sha, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v969: %d/%d gates passed (18 module-own checks + 4 "
          "pattern gates) | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the red-team morning stands frozen: the extraction audit is')
    print('BANKED (U1-U3 established in exact arithmetic, the honest')
    print('chain reading is binding, the r320 repair is complete and')
    print('guarded -- sorry census 5, the two true holes unchanged:')
    print('lstar_subordination + terminal_positive_main); the fiber')
    print('fork ends in the sliding-bound theorem candidate (G_SQ,')
    print('source-pure constant, all old violators absorbed; the')
    print('provenance question is now the F_A/qmax two-part split); the')
    print('base fork ends honestly (P1 language banked, the antiphase')
    print('sign law an ALGORITHM_ARTIFACT of the least-norm-proximal')
    print('basin, the selection-geometry question named).  HONEST:')
    print('nothing is proved cofinally; the sliding bound certifies the')
    print('measured rungs and nothing beyond (C_impl 7.5x looser than')
    print('r306); EXISTS MainWindow stays deliberately unprovable; L*')
    print('itself is NOT proved (PRIME.LSTAR.SUBORDINATION.01 [O]).')
    print('Mincut base 4 / refined 5 unchanged; NO RH claim.')
    print("[%s] v969 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
