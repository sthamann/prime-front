/-
RH/Counterexamples.lean -- the r273 reviewer counterexamples, machine-checked.

PURPOSE (permanent guards).  Before r273 the pilot stated its three open
problems as universally quantified theorems over pure BOOKKEEPING
structures (`PairSplitFamily`, `WindowLadder`, an arbitrary `MainSource`
predicate).  The r273 reviewer adjudication observed that all three are
REFUTABLE in that form: the structures carry no arithmetic property from
which the claimed inequalities could ever follow, so trivial models
violate them.  This file makes the three refutations PERMANENT LEAN
THEOREMS, so that nobody can ever again "prove" an arithmetic margin
from pure bookkeeping: any attempt to close the old universal forms now
contradicts a proved theorem of this very library.

The three guards (verbatim the reviewer models):
  (G1) `pair_margin_not_universal`        -- M = 1, Z = Zloc = 2, runs = []:
       the H1-H4 split holds with equality, but the claimed margin would
       need 2 < 1.  H5 can NEVER follow from H1-H4.
  (G2) `terminal_crossratio_not_universal` -- h = 1, c = 1, F = 2, m = 1:
       every WindowLadder field is satisfied, yet q_N = 4.  q_N < 1 is
       not derivable from the ladder bookkeeping.
  (G3) `prefix_resummation_not_universal`  -- MainSource := fun _ => True
       and h_0 = -1: tau_1 = c_0^2 h_0 = -1.  An arbitrary source
       predicate carries no positivity.

The REPAIRED, truth-capable forms live in RH/Window.lean (structure
`VonMangoldtWindow`, opaque predicate `MainWindow`) and
RH/PairBound.lean (`pair_margin_main`); the master theorem
`augmented_prefix_positive` lives in RH/Closure.lean, where it is
PROVED (r305) from the two true holes.

r320 GUARDS (U1-U3, the R319 red-team audit -- same discipline): the
r310b source interface repeated the r273 mistake one layer up.  The
PRE-r320 statement TYPES (conserved verbatim below as local
definitions) are jointly inconsistent:
  (U1) `old_bridge_terminal_inconsistent`  -- the old bridge type
       (`RepresentsWindow` binding only nodes/comb/arch, never `u`/`B`)
       + the `terminal_positive_main` type refute each other: a window
       with `B = -1` represents the EMPTY spec.
  (U2) `old_bridge_lstar_inconsistent`     -- the old bridge type + the
       `lstar_subordination` type refute each other: at mesh level 0
       the tolerance is `log(anchor)`, so the total node collision
       (all nodes = 1) represents the {2,3,4} spec, and `p = X - 1`
       vanishes on the window at `cap = 2`.
  (U3) `old_pair_margin_forces_empty`      -- the old `pair_margin_main`
       type (free `(Zloc, runs)`, bound only by the split) forces its
       source predicate EMPTY: `Zloc = |F| + 1`, `runs = []` is
       adversarially admissible against any window.
All three quantify over an ARBITRARY predicate `P` (r273 G3 style): no
interpretation of the opaque `MainWindow` can satisfy the old types.
The REPAIRED forms live in RH/Source.lean (retyped `RepresentsWindow`
+ `SourceExact`) and RH/PairBound.lean (canonical extraction
`edgeLocal`/`bulkRuns`, r320).

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import RH.Open
import RH.PairBound
import RH.Inertia
import RH.Source
import RH.Closure
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

namespace RH

namespace Counterexamples

/-! ## (G1) the pair-margin law is not a consequence of the split
bookkeeping (pre-r273 `pair_margin_cofinal`, PairBound.lean) -/

/-- the reviewer model for G1: `M = 1`, `Z = Zloc = 2`, `runs = []` on
every rung.  The H1-H4 split `|Z| <= |Zloc| + |sum runs|` holds WITH
EQUALITY (`2 <= 2 + 0`), and `M > 0` holds -- every structure field is
satisfied. -/
def pairCE : PairBound.PairSplitFamily ℚ where
  Z := fun _ => 2
  Zloc := fun _ => 2
  runs := fun _ => []
  split := fun _ => by norm_num
  M := 1
  M_pos := one_pos

/-- **G1 (permanent guard): the old `pair_margin_cofinal` statement is
FALSE as a universal.**  In the reviewer model the claimed margin reads
`2 < 1`.  Moral: the margin H5 contains arithmetic content the
`PairSplitFamily` bookkeeping does not carry; it can never be proved
from H1-H4 alone.  The repaired form is `pair_margin_main`
(PairBound.lean), typed on `VonMangoldtWindow` + `MainWindow`. -/
theorem pair_margin_not_universal :
    ¬ ∀ (P : PairBound.PairSplitFamily ℚ) (i : ℕ),
        |P.Zloc i| + PairBound.pairBound (P.runs i) < P.M := by
  intro hall
  have h := hall pairCE 0
  norm_num [pairCE, PairBound.pairBound, PairBound.absSum,
    PairBound.blockSums] at h

/-! ## (G2) the terminal cross-ratio is not a consequence of the ladder
bookkeeping (pre-r273 `terminal_crossratio_cofinal`, Open.lean) -/

/-- the reviewer model for G2: `h_k = 1`, `c_k = 1`, `F_k = 2`, `m = 1`
on every rung (terminal degrees `N i = i + 1`, budgets fitted to the
r243 budget form: `rho_k = F^2/h = 4`, so `B_i = S_i(N_i - 1) + m =
4 i + 1`).  Positivity of the `h`-chain, the budget form, cofinality --
every `WindowLadder` field is satisfied. -/
def ladderCE : WindowLadder ℚ where
  data := fun i =>
    { c := fun _ => 1
      h := fun _ => 1
      F := fun _ => 2
      B := 4 * (i : ℚ) + 1 }
  N := fun i => i + 1
  m := 1
  m_pos := one_pos
  N_pos := fun i => Nat.succ_pos i
  cofinal := fun n => ⟨n, Nat.le_succ n⟩
  budget_form := by
    intro i
    simp [ChainData.S, ChainData.rho, Finset.sum_const, Finset.card_range,
      nsmul_eq_mul]
    norm_num
    ring
  wall := fun _ _ _ => one_pos
  cheb := fun _ _ _ => one_ne_zero

/-- **G2 (permanent guard): the old `terminal_crossratio_cofinal`
statement is FALSE as a universal.**  In the reviewer model the terminal
cross-ratio is `q_N = rho/m = (F^2/h)/m = 4` on every rung -- `q_N < 1`
is logically not derivable from the ladder's structure fields, because
NOTHING in them couples `F_k` to `h_k`.  The repaired form is
`terminal_crossratio_main` (Window.lean), a corollary of the master
theorem `augmented_prefix_positive`. -/
theorem terminal_crossratio_not_universal :
    ¬ ∀ (L : WindowLadder ℚ) (i : ℕ), L.q i < 1 := by
  intro hall
  have h := hall ladderCE 0
  norm_num [WindowLadder.q, ChainData.rho, ladderCE] at h

/-! ## (G3) prefix positivity is not a consequence of an arbitrary
source predicate (pre-r273 `prefix_resummation_positivity`, Open.lean) -/

/-- the reviewer model for G3: `c = 1`, `h_0 = -1` (any window with a
negative base-chain entry), `F = 0`, `B = 0`. -/
def chainCE : ChainData ℚ where
  c := fun _ => 1
  h := fun _ => -1
  F := fun _ => 0
  B := 0

/-- **G3 (permanent guard): the old `prefix_resummation_positivity`
statement is FALSE as a universal over arbitrary source predicates.**
With `MainSource := fun _ => True` every chain qualifies, and the model
gives `tau_1 = c_0^2 h_0 = -1`, refuting `0 < tau 1`.  Moral: the
problem is not the missing proof but the missing DEFINITION of what a
MAIN source is -- exactly what the opaque `MainWindow` predicate in
Window.lean now reserves.  The repaired form is
`prefix_chain_positive_main` (Window.lean). -/
theorem prefix_resummation_not_universal :
    ¬ ∀ (MainSource : ChainData ℚ → Prop) (d : ChainData ℚ),
        MainSource d → ∀ N : ℕ, ∀ n ≤ N, 0 < d.tau n := by
  intro hall
  have h := hall (fun _ => True) chainCE trivial 1 1 le_rfl
  rw [ChainData.tau_succ] at h
  norm_num [ChainData.tau_zero, ChainData.a, chainCE] at h

/-! ## (N1, wave 5) universal O(1) upper pinning is refuted by an exact
one-negative instance (r281 / v962; ledger
`PRIME.WALL.HALFFILLING_PINNING_THEORY.01` [E]).

The refuted expectation: "every genuinely signed measure spends its
first crossing inside the free window, `minC <= N_w`" (the world-blind
`C = 0` upper pinning).  The exact instance below is a GENUINE 4-atom
signed measure (not a bookkeeping model): its Hankel minors are computed
from the atoms, the Sylvester chain is the v962-derived exact pivot
chain `2999/1000, 5986/2999, 1962/2993, -4/109`, and the first crossing
sits at `3 = N_w + 1 > N_w = 2`.  The same instance is the v962 N2
witness (minC > N_w is attainable -- `N_w` is the free-window bound,
never an absolute maximum).  The r281 family fact (offset `= N_w - 2`,
i.e. `(S-3)/2`, for the one-negative measure at EVERY odd `S`, checked
exactly probe-side) enters Lean as the arithmetic escape
`o1_pinning_escape` below: no fixed `C` survives. -/

/-- the wave-5 one-negative toy (v962 N2 witness): 4 atoms `0, 1, 2, 3`
with weights `1, 1, 1, -1/1000` -- a genuinely signed measure. -/
noncomputable def onenegToy : SignedAtoms 4 where
  x := ![0, 1, 2, 3]
  w := ![1, 1, 1, -(1/1000)]

/-- its exact pivot chain (machine-derived in v962 S0; values beyond
degree 3 are irrelevant to the minors below). -/
noncomputable def onenegChain : ℕ → ℝ := fun n =>
  if n = 0 then 2999/1000 else if n = 1 then 5986/2999
  else if n = 2 then 1962/2993 else -4/109

theorem onenegToy_h1 :
    onenegToy.hankel 1 = !![2999/1000] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, onenegToy, Fin.sum_univ_four]
      norm_num

theorem onenegToy_h2 :
    onenegToy.hankel 2 = !![2999/1000, 2997/1000;
                            2997/1000, 4991/1000] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, onenegToy, Fin.sum_univ_four]
      norm_num

theorem onenegToy_h3 :
    onenegToy.hankel 3 = !![2999/1000, 2997/1000, 4991/1000;
                            2997/1000, 4991/1000, 8973/1000;
                            4991/1000, 8973/1000, 16919/1000] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, onenegToy, Fin.sum_univ_four]
      norm_num

theorem onenegToy_h4 :
    onenegToy.hankel 4 = !![2999/1000, 2997/1000, 4991/1000, 8973/1000;
                            2997/1000, 4991/1000, 8973/1000, 16919/1000;
                            4991/1000, 8973/1000, 16919/1000, 32757/1000;
                            8973/1000, 16919/1000, 32757/1000,
                            64271/1000] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, onenegToy, Fin.sum_univ_four]
      norm_num

/-- the Sylvester minor chain of the instance, exact: `det H_q =
prod_{i<q} h_i` for every `q <= 4` (the `q = 4` minor is NEGATIVE:
`-1962/13625 = V^2 prod w < 0`). -/
theorem onenegToy_minors : ∀ q ≤ 4,
    ((onenegToy.hankel q).det
      = ∏ i ∈ Finset.range q, onenegChain i) := by
  intro q hq
  interval_cases q
  · simp [Matrix.det_isEmpty]
  · rw [onenegToy_h1]
    norm_num [Matrix.det_fin_one, Finset.prod_range_succ, onenegChain]
  · rw [onenegToy_h2]
    norm_num [Matrix.det_fin_two, Finset.prod_range_succ, onenegChain]
  · rw [onenegToy_h3]
    norm_num [Matrix.det_fin_three, Matrix.cons_val_two,
      Matrix.tail_cons, Matrix.head_cons, Finset.prod_range_succ,
      onenegChain]
  · rw [onenegToy_h4, Matrix.det_succ_row_zero]
    set_option linter.unusedSimpArgs false in
    simp +decide only [Fin.sum_univ_succ, Fin.sum_univ_zero,
      Matrix.submatrix_apply, Fin.succAbove, Fin.castSucc, Fin.succ,
      Fin.castAdd, Fin.castLE, Fin.lt_def, Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.vecHead, Matrix.vecTail,
      Matrix.det_fin_three]
    norm_num [Finset.prod_range_succ, onenegChain]

/-- **N1 (permanent guard, wave 5): world-blind `C = 0` upper pinning is
FALSE.**  The exact one-negative instance has a nonvanishing Sylvester
chain with NO crossing at or below its half-filling cap `N_w = 2` (the
first crossing sits at `3 = N_w + 1`): "every genuinely signed measure
crosses inside its free window" is refuted by a genuine moment
computation, not a bookkeeping model.  Any O(1) upper pinning statement
must consume the comb structure (v962 N1; the arithmetic escape
`o1_pinning_escape` kills every fixed `C` for the family). -/
theorem upper_pinning_not_universal :
    ¬ ∀ (S : ℕ) (m : SignedAtoms S) (h : ℕ → ℝ),
        (∀ q ≤ S, ((m.hankel q).det = ∏ i ∈ Finset.range q, h i)) →
        (∃ j, m.w j < 0) →
        ∃ n ≤ (S + 1) / 2, h n < 0 := by
  intro hall
  obtain ⟨n, hn, hneg⟩ := hall 4 onenegToy onenegChain
    onenegToy_minors ⟨3, by simp [onenegToy]⟩
  interval_cases n <;> norm_num [onenegChain] at hneg

/-- the arithmetic escape (v962 N1, PROVED): the one-negative family has
offset `(S - 1) - N_w = (S - 3)/2`, UNBOUNDED in `S` -- no world-blind
constant `C` can upper-pin the first crossing at `N_w + C` (the family
fact `minC = S - 1` is machine-checked exactly in v962/r281; Lean
carries the `S = 4` instance above and this unboundedness). -/
theorem o1_pinning_escape (C : ℕ) :
    ∃ S : ℕ, 1 ≤ S ∧ (S - 1) - (S + 1) / 2 > C :=
  ⟨2 * C + 5, by omega, by omega⟩

/-! ## (U1-U3, r320) the R319 red-team guards: the pre-r320 statement
types of the source interface are jointly inconsistent

The pre-r320 `RepresentsWindow` (r310b) is CONSERVED VERBATIM below as
`OldRepresentsWindow`; the guards quantify over an arbitrary predicate
`P` in place of the opaque `MainWindow` (the r273 G3 discipline), so
they refute the statement TYPES themselves -- no interpretation of the
opaque marker can rescue the old forms.  All proofs are sorry-free. -/

open Polynomial

/-- the PRE-r320 window-level representation predicate (r310b),
conserved verbatim as the guard target: binds ONLY nodes/comb/arch
within the bare mesh width -- never `u`, never `B`, no separation. -/
def OldRepresentsWindow (w : VonMangoldtWindow) (v : PrimeWindow)
    (δ : ℝ) : Prop :=
  ∃ hS : w.S = v.S,
    (∀ j : Fin w.S,
      |((w.nodes j : ℚ) : ℝ) - v.nodes (Fin.cast hS j)| ≤ δ) ∧
    (∀ j : Fin w.S,
      |((w.combWeight j : ℚ) : ℝ) - v.combWeight (Fin.cast hS j)| ≤ δ) ∧
    (∀ j : Fin w.S,
      |((w.archWeight j : ℚ) : ℝ) - v.archWeight (Fin.cast hS j)| ≤ δ)

/-- the U1 spec: the EMPTY prime window spec (any budget -- the old
predicate never reads it). -/
noncomputable def guardSpec0 : PrimeWindowSpec where
  S := 0
  primePowers := fun j => j.elim0
  pp_isPrimePow := fun j => j.elim0
  pp_strictMono := by intro i _ _; exact i.elim0
  anchor := 2
  anchor_isPrimePow := Nat.prime_two.prime.isPrimePow
  meshLevel := 0
  pp_le := fun j => j.elim0
  archWeight := fun j => j.elim0
  arch_nonneg := fun j => j.elim0
  border := fun _ => 0
  budget := 5 / 7
  budget_pos := by norm_num

/-- the U1 window: empty support, budget `B = -1` -- the old predicate
does not see `B`, `TerminalPositive` demands `0 < B`. -/
def guardWindow0 : VonMangoldtWindow where
  S := 0
  nodes := fun j => j.elim0
  combWeight := fun j => j.elim0
  archWeight := fun j => j.elim0
  comb_nonneg := fun j => j.elim0
  arch_nonneg := fun j => j.elim0
  lo := 0
  hi := 0
  window_rule := fun j => j.elim0
  u := fun _ => 0
  B := -1

/-- **U1 (permanent guard, r320): the old bridge type and the terminal
type are jointly inconsistent** -- for EVERY predicate `P`.  The empty
spec is represented by the `B = -1` window (the old predicate binds
neither `u` nor `B`), so the old bridge certifies it as MAIN and the
terminal statement demands `0 < -1`.  The repaired form is the r320
`RepresentsWindow` (u/B-fidelity + `budget_pos`, RH/Source.lean). -/
theorem old_bridge_terminal_inconsistent :
    ¬ ∃ P : VonMangoldtWindow → Prop,
      (∀ w, P w ↔ ∃ s : PrimeWindowSpec,
        OldRepresentsWindow w (buildPrimeWindow s) s.mesh) ∧
      (∀ w, P w → TerminalPositive w) := by
  rintro ⟨P, hbridge, hterm⟩
  have hmain : P guardWindow0 :=
    (hbridge guardWindow0).mpr
      ⟨guardSpec0, rfl, fun j => j.elim0, fun j => j.elim0,
        fun j => j.elim0⟩
  have hB : (0 : ℝ) < ((-1 : ℚ) : ℝ) := (hterm guardWindow0 hmain).1
  norm_num at hB

/-- the U2 spec: the smallest full corpus window -- anchor 2, atoms
`{2, 3, 4}`, MESH LEVEL 0 (tolerance = the full half-window
`log 2`). -/
noncomputable def guardSpec3 : PrimeWindowSpec where
  S := 3
  primePowers := fun j => (j : ℕ) + 2
  pp_isPrimePow := by
    intro j
    fin_cases j
    · exact Nat.prime_two.prime.isPrimePow
    · exact Nat.prime_three.prime.isPrimePow
    · exact ⟨2, 2, Nat.prime_two.prime, two_pos, by norm_num⟩
  pp_strictMono := by
    intro i j hij
    simpa using Nat.add_lt_add_right (Fin.lt_def.mp hij) 2
  anchor := 2
  anchor_isPrimePow := Nat.prime_two.prime.isPrimePow
  meshLevel := 0
  pp_le := by intro j; have := j.isLt; simp; omega
  archWeight := fun _ => 0
  arch_nonneg := fun _ => le_refl 0
  border := fun _ => 0
  budget := 5 / 7
  budget_pos := by norm_num

/-- the U2 window: TOTAL NODE COLLISION -- all three nodes at `1`,
comb masses `1` (all within `log 2` of the true `log n` and `Λ(n)`:
the mesh-level-0 tolerance identifies the nodes). -/
def guardWindow3 : VonMangoldtWindow where
  S := 3
  nodes := fun _ => 1
  combWeight := fun _ => 1
  archWeight := fun _ => 0
  comb_nonneg := fun _ => by norm_num
  arch_nonneg := fun _ => le_refl 0
  lo := 1
  hi := 1
  window_rule := fun _ => ⟨le_refl 1, le_refl 1⟩
  u := fun _ => 0
  B := 1

theorem guard_coll2 : |(1 : ℝ) - Real.log 2| ≤ Real.log 2 := by
  have h := Real.log_two_gt_d9
  have h' := Real.log_two_lt_d9
  rw [abs_le]
  constructor <;> linarith

theorem guard_log3_bounds :
    Real.log 2 ≤ Real.log 3 ∧ Real.log 3 ≤ 2 * Real.log 2 := by
  constructor
  · exact Real.log_le_log (by norm_num) (by norm_num)
  · have h : Real.log 3 ≤ Real.log 4 :=
      Real.log_le_log (by norm_num) (by norm_num)
    have h4 : Real.log 4 = 2 * Real.log 2 := by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
      push_cast
      ring
    linarith

theorem guard_coll3 : |(1 : ℝ) - Real.log 3| ≤ Real.log 2 := by
  have h := Real.log_two_gt_d9
  have h' := Real.log_two_lt_d9
  obtain ⟨hl, hu⟩ := guard_log3_bounds
  rw [abs_le]
  constructor <;> linarith

theorem guard_coll4 : |(1 : ℝ) - Real.log 4| ≤ Real.log 2 := by
  have h := Real.log_two_gt_d9
  have h' := Real.log_two_lt_d9
  have h4 : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
    push_cast
    ring
  rw [abs_le]
  constructor <;> linarith

theorem guardSpec3_mesh : guardSpec3.mesh = Real.log 2 := by
  simp [PrimeWindowSpec.mesh, PrimeWindowSpec.alpha, guardSpec3]

/-- the collision window OLD-represents the built {2,3,4} window at
mesh level 0 (all three channel clauses within `log 2`). -/
theorem guardWindow3_old_represents :
    OldRepresentsWindow guardWindow3 (buildPrimeWindow guardSpec3)
      guardSpec3.mesh := by
  refine ⟨rfl, ?_, ?_, ?_⟩
  · intro j
    rw [guardSpec3_mesh]
    fin_cases j
    · show |((1 : ℚ) : ℝ) - Real.log ((2 : ℕ) : ℝ)| ≤ Real.log 2
      norm_num [guard_coll2]
    · show |((1 : ℚ) : ℝ) - Real.log ((3 : ℕ) : ℝ)| ≤ Real.log 2
      norm_num [guard_coll3]
    · show |((1 : ℚ) : ℝ) - Real.log ((4 : ℕ) : ℝ)| ≤ Real.log 2
      norm_num [guard_coll4]
  · intro j
    rw [guardSpec3_mesh]
    fin_cases j
    · show |((1 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 2|
        ≤ Real.log 2
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
      norm_num [guard_coll2]
    · show |((1 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 3|
        ≤ Real.log 2
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_three]
      norm_num [guard_coll3]
    · show |((1 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 4|
        ≤ Real.log 2
      rw [show (4 : ℕ) = 2 ^ 2 by norm_num,
        ArithmeticFunction.vonMangoldt_apply_pow (by norm_num),
        ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
      norm_num [guard_coll2]
  · intro j
    rw [guardSpec3_mesh]
    show |((0 : ℚ) : ℝ) - 0| ≤ Real.log 2
    have := Real.log_two_gt_d9
    rw [abs_le]
    constructor <;> push_cast <;> linarith

/-- **U2 (permanent guard, r320): the old bridge type and the L* type
are jointly inconsistent** -- for EVERY predicate `P`.  The collision
window is certified MAIN by the old bridge (mesh-level-0 tolerance),
and `p = X - 1` (degree `1 < cap = 2`) vanishes on the collided nodes,
so both integrals are `0` and the strict subordination demands
`0 < 0`.  The repaired form is the r320 separation discipline
(RH/Source.lean). -/
theorem old_bridge_lstar_inconsistent :
    ¬ ∃ P : VonMangoldtWindow → Prop,
      (∀ w, P w ↔ ∃ s : PrimeWindowSpec,
        OldRepresentsWindow w (buildPrimeWindow s) s.mesh) ∧
      (∀ w, P w → ∀ p : Polynomial ℝ, p ≠ 0 → p.natDegree < w.cap →
        w.nuSq p < w.muSq p) := by
  rintro ⟨P, hbridge, hlstar⟩
  have hmain : P guardWindow3 :=
    (hbridge guardWindow3).mpr ⟨guardSpec3, guardWindow3_old_represents⟩
  have hdeg : (X - C (1 : ℝ)).natDegree < guardWindow3.cap := by
    rw [Polynomial.natDegree_X_sub_C]
    show 1 < 2
    norm_num
  have hlt := hlstar guardWindow3 hmain (X - C 1)
    (Polynomial.X_sub_C_ne_zero 1) hdeg
  simp [VonMangoldtWindow.muSq, VonMangoldtWindow.nuSq,
    guardWindow3] at hlt

/-- **U3 (permanent guard, r320): the old pair-margin type forces its
source predicate EMPTY** -- for EVERY predicate `P`.  With free
`(Zloc, runs)` the adversarial instantiation `Zloc = |F| + 1`,
`runs = []` satisfies the split trivially, and the claimed margin
`|F| + 1 < sqrt(5/7) < 1` is absurd -- so ANY window in `P` yields
`False`: the old type is inconsistent with `∃ w, P w` (the r273
disease one level up).  The repaired form is the canonical extraction
(`edgeLocal`/`bulkRuns`, RH/PairBound.lean r320). -/
theorem old_pair_margin_forces_empty (P : VonMangoldtWindow → Prop)
    (hmargin : ∀ w, P w → ∀ {M : ℝ}, 0 < M → M ^ 2 = 5 / 7 →
      ∀ (Zloc : ℝ) (runs : List ℝ),
        |((w.F (w.cap - 1) : ℚ) : ℝ)| ≤ |Zloc| + |runs.sum| →
        |Zloc| + PairBound.pairBound runs < M) :
    ¬ ∃ w, P w := by
  rintro ⟨w, hw⟩
  have hM : (0 : ℝ) < Real.sqrt (5 / 7) := Real.sqrt_pos.mpr (by norm_num)
  have hM2 : Real.sqrt (5 / 7) ^ 2 = 5 / 7 := Real.sq_sqrt (by norm_num)
  have h0 : (0 : ℝ) ≤ abs ((w.F (w.cap - 1) : ℚ) : ℝ) + 1 := by positivity
  have habs : |((w.F (w.cap - 1) : ℚ) : ℝ)| ≤
      abs (abs ((w.F (w.cap - 1) : ℚ) : ℝ) + 1) + |([] : List ℝ).sum| := by
    rw [abs_of_nonneg h0, List.sum_nil, abs_zero]
    linarith [abs_nonneg ((w.F (w.cap - 1) : ℚ) : ℝ)]
  have h := hmargin w hw hM hM2
    (abs ((w.F (w.cap - 1) : ℚ) : ℝ) + 1) [] habs
  rw [abs_of_nonneg h0] at h
  have hpb : PairBound.pairBound ([] : List ℝ) = 0 := rfl
  rw [hpb] at h
  nlinarith [abs_nonneg ((w.F (w.cap - 1) : ℚ) : ℝ), hM, hM2, h]

end Counterexamples

end RH
