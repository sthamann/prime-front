/-
RH/Window.lean -- the retyped window structure and THE MASTER THEOREM
(r273 reviewer repair).

WHY THIS FILE EXISTS.  The three former open statements
  * `terminal_crossratio_cofinal`   (pre-r273 Open.lean),
  * `prefix_resummation_positivity` (pre-r273 Open.lean),
  * `pair_margin_cofinal`           (pre-r273 PairBound.lean)
were quantified UNIVERSALLY over pure bookkeeping structures
(`WindowLadder`, an arbitrary `MainSource` predicate, `PairSplitFamily`)
and are therefore REFUTABLE by trivial models -- the explicit refutations
are machine-checked in RH/Counterexamples.lean.  The problem was never the
`sorry`; it was the missing definition of what a MAIN window IS.  This
file supplies
  (a) the concrete window structure `VonMangoldtWindow` that the real
      measured windows instantiate (exact rationals, as in the corpus),
  (b) the derived objects (moments, Hankel matrices `H_n`, chain `h_k`,
      border readouts `F_k`, Schur margins `D_n`, terminal cross-ratio
      `q`) as DEFINITIONS from the structure -- not as free fields,
  (c) the honestly-open source predicate `MainWindow` (opaque -- its
      mathematical content IS the open problem), and
  (d) the master theorem `augmented_prefix_positive`, from which BOTH
      former edges follow by finite matrix algebra.
      r305 UPDATE (wave 10): the master theorem and its corollaries
      MOVED to RH/Closure.lean, where the master is PROVED from the two
      true holes (`lstar_subordination` below + `terminal_positive_main`
      there) via the reconstruction theorem
      `lstar_terminal_implies_master` -- it is no longer an independent
      `sorry` of this file.

INSTANCE DATA (what the real windows would supply -- corpus dictionary):
  * `nodes`      -- the window node positions: the rescaled prime-power
                    abscissas `log p^k` of the von-Mangoldt double zone,
                    clipped to the window (probe coupledtau_probe.py,
                    r257, SPEC_SHA 73d8247f6de36a2b; frozen window spec).
                    NOTE: real abscissas are irrational; the corpus works
                    with the exact-rational frozen window data (f64 atoms
                    exactly converted, cf. r270 interval certificate).
  * `combWeight` -- the nonnegative von-Mangoldt comb masses (the mu side
                    of the signed defect measure mutilde = mu - nu).
  * `archWeight` -- the nonnegative archimedean/smooth subtraction (the
                    nu side; v955 window object, r224-r226).
  * `lo/hi/window_rule` -- the window rule: all nodes confined to the
                    frozen window interval (the Galerkin localization).
  * `u`          -- the border source vector (border column `t` of the
                    bordered RHP dictionary, v958 r244-r253; the r264
                    dictionary reads the terminal drive from it).
  * `B`          -- the budget scalar (r243 form: B = S_{N-2} + 5/7).
The half-filling cap is DERIVED: `cap = ceil(S/2) = (S+1)/2` (v956
half-filling law, r228-r229; counting half proved in RH/Inertia.lean as
`window_cap_arith`).

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Data.Matrix.Block
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace RH

open Matrix

/-- **The concrete window structure** (r273 retype).  One window of the
von-Mangoldt double zone: `S` atoms with exact-rational positions and a
signed defect decomposition `weight = combWeight - archWeight`, a window
rule confining the nodes, and the border source (border vector `u`,
budget `B`).  The corpus instantiates exact rationals throughout (the
frozen window data of the probes); the toy instance below is an exact
miniature. -/
structure VonMangoldtWindow where
  /-- support size of the signed defect measure `mutilde = mu - nu`. -/
  S : ℕ
  /-- node positions (corpus: rescaled `log p^k` abscissas, frozen). -/
  nodes : Fin S → ℚ
  /-- nonnegative von-Mangoldt comb masses (the `mu` side). -/
  combWeight : Fin S → ℚ
  /-- nonnegative archimedean/smooth part (the `nu` side). -/
  archWeight : Fin S → ℚ
  comb_nonneg : ∀ j, 0 ≤ combWeight j
  arch_nonneg : ∀ j, 0 ≤ archWeight j
  /-- window rule: lower edge of the frozen window. -/
  lo : ℚ
  /-- window rule: upper edge of the frozen window. -/
  hi : ℚ
  /-- the window rule: every node lies in `[lo, hi]` (Galerkin locality). -/
  window_rule : ∀ j, lo ≤ nodes j ∧ nodes j ≤ hi
  /-- border source vector (border column `t` of the bordered RHP, v958;
  entries beyond the cap are unused). -/
  u : ℕ → ℚ
  /-- budget scalar (r243 form `B = S_{N-2} + 5/7`). -/
  B : ℚ

namespace VonMangoldtWindow

variable (w : VonMangoldtWindow)

/-- the signed defect weight `w_j = mu_j - nu_j` (v955 window object). -/
def weight (j : Fin w.S) : ℚ := w.combWeight j - w.archWeight j

/-- **the half-filling cap** `N = ceil(S/2) = (S+1)/2` (v956 law,
r228-r229; the counting half is `window_cap_arith` in RH/Inertia.lean).
DERIVED, not a free field -- no model can decouple it from `S`. -/
def cap : ℕ := (w.S + 1) / 2

/-- the `n`-th signed moment `m_n = sum_j w_j x_j^n` (exact rational). -/
def mom (n : ℕ) : ℚ := ∑ j, w.weight j * w.nodes j ^ n

/-- **the Hankel moment matrix** `H_n(i,k) = m_{i+k}` -- DERIVED from the
structure (over ℝ so that the mathlib `Matrix.PosDef` API applies; the
entries are exact-rational casts). -/
def hankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => ((w.mom ((i : ℕ) + (k : ℕ)) : ℚ) : ℝ)

/-- comb-channel moments `Σ_j μ_j x_j^n` (the μ-Gram generating function). -/
def combMom (n : ℕ) : ℚ := ∑ j, w.combWeight j * w.nodes j ^ n

/-- arch-channel moments `Σ_j ν_j x_j^n` (the ν-Gram generating function). -/
def archMom (n : ℕ) : ℚ := ∑ j, w.archWeight j * w.nodes j ^ n

/-- μ-Hankel (comb Gram in the monomial basis). -/
def combHankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => ((w.combMom ((i : ℕ) + (k : ℕ)) : ℚ) : ℝ)

/-- ν-Hankel (arch Gram in the monomial basis). -/
def archHankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => ((w.archMom ((i : ℕ) + (k : ℕ)) : ℚ) : ℝ)

/-- node-evaluation matrix: row `j` (node), column `i` (power `x_j^i`).
The finite evaluation map `ℝ[x]_{<n} → ℝ^S`. -/
def nodeVand (n : ℕ) : Matrix (Fin w.S) (Fin n) ℝ :=
  fun j i => ((w.nodes j : ℚ) : ℝ) ^ (i : ℕ)

theorem mom_eq_comb_sub_arch (n : ℕ) :
    w.mom n = w.combMom n - w.archMom n := by
  simp [mom, combMom, archMom, weight, sub_mul, Finset.sum_sub_distrib]

theorem hankel_eq_comb_sub_arch (n : ℕ) :
    w.hankel n = w.combHankel n - w.archHankel n := by
  ext i k
  simp [hankel, combHankel, archHankel, mom_eq_comb_sub_arch]

theorem combHankel_eq_vand (n : ℕ) :
    w.combHankel n =
      (w.nodeVand n)ᵀ * diagonal (fun j => ((w.combWeight j : ℚ) : ℝ)) *
        w.nodeVand n := by
  ext i k
  rw [Matrix.mul_apply]
  simp only [Matrix.mul_diagonal, Matrix.transpose_apply, nodeVand, combHankel,
    combMom]
  push_cast
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [pow_add]
  ring

theorem archHankel_eq_vand (n : ℕ) :
    w.archHankel n =
      (w.nodeVand n)ᵀ * diagonal (fun j => ((w.archWeight j : ℚ) : ℝ)) *
        w.nodeVand n := by
  ext i k
  rw [Matrix.mul_apply]
  simp only [Matrix.mul_diagonal, Matrix.transpose_apply, nodeVand, archHankel,
    archMom]
  push_cast
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [pow_add]
  ring

/-- the border Cauchy readout `F_k` (corpus: the border column expressed
in the monic orthogonal-polynomial basis of the window; the structure
carries it as the border vector `u`). -/
def F (k : ℕ) : ℚ := w.u k

/-- the border vector as a real vector of length `n`. -/
def borderVec (n : ℕ) : Fin n → ℝ := fun i => ((w.u i : ℚ) : ℝ)

/-- **the augmented matrix** `A_{w,n} = [[H_n, u_n], [u_n^T, B]]` -- the
bordered object of the master theorem (v958 bordered PSD dictionary:
bordered PSD = wall + budget). -/
def A (n : ℕ) : Matrix (Fin n ⊕ Unit) (Fin n ⊕ Unit) ℝ :=
  Matrix.fromBlocks (w.hankel n)
    (fun i _ => ((w.u i : ℚ) : ℝ))
    (fun _ k => ((w.u k : ℚ) : ℝ))
    (fun _ _ => ((w.B : ℚ) : ℝ))

/-- **the chain `h_k`** as the exact Sylvester ratio of consecutive
leading principal minors, `h_k = det H_{k+1} / det H_k` (v959 S0.5:
`det H_p = prod_{i<p} h_i`; `det H_0 = 1`).  DERIVED, not a free field --
this is what the pre-r273 skeletons were missing. -/
noncomputable def h (k : ℕ) : ℝ :=
  (w.hankel (k + 1)).det / (w.hankel k).det

/-- **the Schur margin** `D_n = det A_n / det H_n` -- the determinant form
of the Schur complement `B - u^T H_n^{-1} u` (see `D_eq_schur` below);
`D_cap` is the terminal fiber margin of the corpus. -/
noncomputable def D (n : ℕ) : ℝ := (w.A n).det / (w.hankel n).det

/-- **the terminal cross-ratio** `q = (B - D_cap)/B = u^T H^{-1} u / B` --
the r258 TERMINAL_Q_LAW object at the half-filling terminal. -/
noncomputable def q : ℝ :=
  (((w.B : ℚ) : ℝ) - w.D w.cap) / ((w.B : ℚ) : ℝ)

/-- the Hankel matrices are symmetric, hence Hermitian over ℝ. -/
theorem hankel_isHermitian (n : ℕ) : (w.hankel n).IsHermitian := by
  ext i k
  simp [hankel, Nat.add_comm (i : ℕ) (k : ℕ)]

/-- the top-left block of the augmented matrix is the Hankel matrix. -/
theorem A_submatrix_inl (n : ℕ) :
    (w.A n).submatrix Sum.inl Sum.inl = w.hankel n := rfl

end VonMangoldtWindow

/-! ## The honest open predicate -/

/-- **`MainWindow` -- the honestly-open source predicate** (r273 retype).

This predicate is deliberately `opaque`: its mathematical content IS the
open problem.  What it must eventually say (the arithmetic properties any
proof of the master theorem has to consume):

  * the nodes/weights are the ACTUAL von-Mangoldt double comb of the
    window (`combWeight = Lambda(p^k)`-masses at `nodes = log p^k`
    rescaled, `archWeight` = the explicit archimedean density) -- i.e.
    genuine prime arithmetic, not just any nonneg-minus-nonneg split;
  * the border source `u` and budget `B` are the v958/r243 bordered-RHP
    data OF that comb (budget form `B = S_{N-2} + 5/7`);
  * whatever quantitative arithmetic input the wall needs: the measured
    content is quasi-definiteness of the signed defect measure exactly
    through half-filling (v956, r228-r229) and the coherent-cancellation
    depth of the ensemble (r259-r272).

What provably does NOT suffice (the measured kill lists, see
RH/Open.lean headers): every structural/bookkeeping consequence of the
fields above (Counterexamples.lean shows universality over the bare
structure is FALSE); mass majorants (r258); the bordered spectral bound
(r257/r265); saddle dominance / k-swap truncation (r259); subtraction-
free positivity, block involutions, transfer cones (r261); naive and
IIKS s-coordinates (r265); eventual-triangle asymptotics (r263); blind
level-2 pairing beyond 5/7 exception rungs (r270-r272).

Because `MainWindow` is opaque, no theorem conditioned on it can be
refuted by a toy model (truth-capability restored), and none can be
proved without supplying the arithmetic -- exactly the honest state.

C1 STATUS NOTE (the reviewer final-domain contract): since block C1
the LOAD-BEARING chain (the two true holes, the master theorem and
all its corollaries) no longer runs over this predicate -- it runs
over the constructive `CanonicalWindow` predicate of
RH/Canonical.lean (the completed canonical prime-window family; only
the kernel-channel VALUES stay opaque there, as the named constant
`canonicalCompletion`).  `MainWindow` remains as the r273 historical
interface: it is consumed only by the opacity bridge
`mainWindow_iff_builtFromPrimeSource` (RH/Source.lean) and documented
by the permanent guards. -/
opaque MainWindow : VonMangoldtWindow → Prop

/-! ## The master theorem (the new north star)

r305 MOVE (wave 10): the master theorem `augmented_prefix_positive`
(r273 target form -- for a MAIN window every augmented matrix
`A_{w,n} = [[H_n, u_n], [u_n^T, B]]` through the half-filling cap is
positive definite) now lives in RH/Closure.lean, where it is PROVED
from L* (`lstar_subordination` below) and the terminal statement
(`terminal_positive_main` there) via the reconstruction theorem
`lstar_terminal_implies_master`.  It carries NO `sorry` of its own
anymore: the open content is exactly the two true holes.  The `_main`
corollaries (`prefix_chain_positive_main`,
`terminal_margin_positive_main`, `terminal_crossratio_main`) moved
with it, proofs verbatim. -/

/-! ## Finite matrix algebra: everything derivable from the master
conclusion is proved here against the mathlib `Matrix.PosDef` API.
These lemmas take the PosDef conclusion as a hypothesis, so they are
unconditional finite algebra (no `sorry`); the `_main` corollaries
in RH/Closure.lean compose them with the master theorem. -/

namespace VonMangoldtWindow

variable (w : VonMangoldtWindow)

/-- **block extraction**: if the augmented matrix is PosDef, so is its
Hankel principal block (restrict the quadratic form to vectors vanishing
on the border coordinate).  Pure finite algebra, PROVED. -/
theorem hankel_posDef_of_augmented {n : ℕ} (hA : (w.A n).PosDef) :
    (w.hankel n).PosDef := by
  refine Matrix.PosDef.of_dotProduct_mulVec_pos (w.hankel_isHermitian n)
    fun x hx => ?_
  have hx' : (Sum.elim x (fun _ => (0 : ℝ)) : Fin n ⊕ Unit → ℝ) ≠ 0 := by
    intro h0
    apply hx
    funext i
    simpa using congrFun h0 (Sum.inl i)
  have hform := hA.dotProduct_mulVec_pos hx'
  have key : star (Sum.elim x (fun _ => (0 : ℝ))) ⬝ᵥ
      (w.A n *ᵥ Sum.elim x (fun _ => (0 : ℝ)))
      = star x ⬝ᵥ (w.hankel n *ᵥ x) := by
    simp [A, dotProduct, Matrix.mulVec, Fintype.sum_sum_type,
      Matrix.fromBlocks_apply₁₁, Matrix.fromBlocks_apply₂₁]
  rw [← key]
  exact hform

/-- **corner extraction**: if any augmented matrix is PosDef, the budget
is positive (test vector `(0, 1)`).  Pure finite algebra, PROVED. -/
theorem budget_pos_of_augmented {n : ℕ} (hA : (w.A n).PosDef) :
    (0 : ℝ) < ((w.B : ℚ) : ℝ) := by
  have hx : (Sum.elim (fun _ => (0 : ℝ)) (fun _ => (1 : ℝ)) :
      Fin n ⊕ Unit → ℝ) ≠ 0 := by
    intro h0
    simpa using congrFun h0 (Sum.inr ())
  have hform := hA.dotProduct_mulVec_pos hx
  have key : star (Sum.elim (fun _ => (0 : ℝ)) (fun _ => (1 : ℝ)) :
      Fin n ⊕ Unit → ℝ) ⬝ᵥ
      (w.A n *ᵥ Sum.elim (fun _ => (0 : ℝ)) (fun _ => (1 : ℝ)))
      = ((w.B : ℚ) : ℝ) := by
    simp [A, dotProduct, Matrix.mulVec, Fintype.sum_sum_type,
      Matrix.fromBlocks_apply₁₂, Matrix.fromBlocks_apply₂₂]
  rw [key] at hform
  exact hform

/-- PosDef of the Hankel block gives positive leading principal minors
(mathlib `Matrix.PosDef.det_pos`). -/
theorem hankelDet_pos {n : ℕ} (hH : (w.hankel n).PosDef) :
    0 < (w.hankel n).det := hH.det_pos

/-- **the Sylvester step**: consecutive PosDef Hankel blocks make the
chain element positive, `h_k = det H_{k+1}/det H_k > 0`.  PROVED. -/
theorem h_pos_of_posDef {k : ℕ} (h1 : (w.hankel k).PosDef)
    (h2 : (w.hankel (k + 1)).PosDef) : 0 < w.h k :=
  div_pos h2.det_pos h1.det_pos

/-- **the Schur-margin step**: PosDef of the augmented matrix and of its
Hankel block make the Schur margin positive, `D_n = det A_n/det H_n > 0`.
PROVED. -/
theorem D_pos_of_augmented {n : ℕ} (hA : (w.A n).PosDef)
    (hH : (w.hankel n).PosDef) : 0 < w.D n :=
  div_pos hA.det_pos hH.det_pos

/-- **the terminal gate**: positive budget + positive terminal Schur
margin give the terminal cross-ratio inequality `q < 1`.  PROVED (pure
ordered-field algebra; cf. `terminal_equiv` in RH/Recursion.lean). -/
theorem q_lt_one_of_pos (hB : (0 : ℝ) < ((w.B : ℚ) : ℝ))
    (hD : 0 < w.D w.cap) : w.q < 1 := by
  rw [q, div_lt_one hB]
  linarith

/-- **the Schur-complement identity** `D_n = B - u^T H_n^{-1} u`
(the determinant margin IS the bordered Schur complement; v958 S0
bordered dictionary: `[[G,u],[u^T,B]]` PSD iff `B >= u^T G^{-1} u`).
Proved against mathlib's `Matrix.det_fromBlocks₁₁`. -/
theorem D_eq_schur {n : ℕ} (hH : (w.hankel n).PosDef) :
    w.D n = ((w.B : ℚ) : ℝ)
      - w.borderVec n ⬝ᵥ ((w.hankel n)⁻¹ *ᵥ w.borderVec n) := by
  have hdet : (w.hankel n).det ≠ 0 := hH.det_pos.ne'
  have hinv : Invertible (w.hankel n) :=
    (w.hankel n).invertibleOfIsUnitDet (isUnit_iff_ne_zero.mpr hdet)
  have hA : (w.A n).det = (w.hankel n).det *
      (((w.B : ℚ) : ℝ)
        - w.borderVec n ⬝ᵥ ((w.hankel n)⁻¹ *ᵥ w.borderVec n)) := by
    rw [show w.A n = Matrix.fromBlocks (w.hankel n)
        (fun i _ => ((w.u i : ℚ) : ℝ))
        (fun _ k => ((w.u k : ℚ) : ℝ))
        (fun _ _ => ((w.B : ℚ) : ℝ)) from rfl,
      Matrix.det_fromBlocks₁₁]
    congr 1
    rw [Matrix.det_unique, Matrix.invOf_eq_nonsing_inv]
    simp only [Matrix.sub_apply, Matrix.mul_apply, borderVec, dotProduct,
      Matrix.mulVec, Finset.sum_mul, Finset.mul_sum]
    congr 1
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
    ring
  rw [D, hA, mul_div_cancel_left₀ _ hdet]

end VonMangoldtWindow

/-! ## The retyped edges as corollaries of the master theorem --
MOVED to RH/Closure.lean (r305): `prefix_chain_positive_main`,
`terminal_margin_positive_main`, `terminal_crossratio_main` are proved
there from the reconstructed master theorem, proofs verbatim. -/

open VonMangoldtWindow

/-! ## Wave 5 (rounds 279-281, v962): the fog-free central hole

The v962 theory set (`PRIME.WALL.HALFFILLING_PINNING_THEORY.01` [E],
module verification/v962_halffilling_pinning_theory.py) reduces the wall
to ONE placement question:
  * T1 (moment counting, r281 -- PROVED in RH/Inertia.lean as
    `moment_counting_free_pivots`): the free pivots are exactly
    `h_0 .. h_{cap-1}` -- half-filling is the end of the free moment
    space ("why half-filling" is answered by counting, no secret);
  * T2 (crossing budget, r279 -- stated in RH/Inertia.lean as
    `crossing_budget`, certified exactly in v962): the number of negative
    pivots over the full continuation is the negative-atom count `S_-`,
    world-blindly (Jacobi/Sylvester);
  * T4 (main window reduction -- `main_window_reduction` below, PROVED):
    "no crossing before the cap" is EXACTLY free-window positivity.
Hence nothing about the wall is open except WHERE the fixed budget is
spent, and that statement is `free_window_positivity` below. -/

/-! **THE FOG-FREE CENTRAL HOLE** (wave 5; the r279 b3 gap statement =
the v962 T4 reinstform; ledger
`PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` [O]): the statement
`free_window_positivity` is PROVED as a corollary of L* since wave 10
(r305) -- since C1 it lives in RH/Canonical.lean on the final domain
(`CanonicalWindow`), proved from `lstar_canonical`.  The v962
reduction chain (T1 counting + T2 budget + T4 equivalence) and the
refutation set N1-N4 are unchanged. -/

/-- the master conclusion implies free-window positivity by pure finite
algebra (block extraction + the Sylvester ratio) -- hypothesis form,
PROVED: the fog-free hole is (at most) the base half of the master
`sorry`. -/
theorem master_implies_free_window (w : VonMangoldtWindow)
    (hA : ∀ n ≤ w.cap, (w.A n).PosDef) : ∀ n < w.cap, 0 < w.h n := by
  intro n hn
  have h1 := w.hankel_posDef_of_augmented (hA n (Nat.le_of_lt hn))
  have h2 := w.hankel_posDef_of_augmented (hA (n + 1) hn)
  exact w.h_pos_of_posDef h1 h2

/-- **T4, the main window reduction** (v962, PROVED): on a chain with no
vanishing pivot below the cap, free-window positivity is EXACTLY the
localization statement "no crossing before the cap" -- with T2 fixing
the total budget, the entire open content of the wall is this placement
question. -/
theorem main_window_reduction (h : ℕ → ℝ) (N : ℕ)
    (hnz : ∀ n < N, h n ≠ 0) :
    (∀ n < N, 0 < h n) ↔ ∀ n < N, ¬ h n < 0 := by
  constructor
  · intro hp n hn hneg
    exact absurd (hp n hn) (not_lt.mpr hneg.le)
  · intro hnc n hn
    rcases lt_trichotomy (h n) 0 with hlt | heq | hgt
    · exact absurd hlt (hnc n hn)
    · exact absurd heq (hnz n hn)
    · exact hgt

/-! ## Wave 6 (rounds 282-285, v963): the canonical form -- lemma L*

The r283 A2 chain (v963, `PRIME.LSTAR.REDUCTION_DICTIONARY.01` [E],
module verification/v963_lstar_reduction_dictionary.py) reduces the
free-window question to ONE two-measure subordination scalar, the
missing lemma L*: on a MAIN window, for every real polynomial `p != 0`
with `deg p < cap`,

    int p^2 dnu  <  int p^2 dmu

(equivalently `lambda_max(E_cap) < 1` for the nu-dressed mu-CD kernel;
the frame congruence `minor_k(D_mu - G) = D_k(mutilde)` and the
contraction equivalence are machine-certified exact-rationally in
v963).  Ledger: `PRIME.LSTAR.SUBORDINATION.01` [O]; the fully
standalone problem statement lives in rh/problem/lstar_problem.tex.

The direction L* => free-window positivity is PROVED below
(`lstar_implies_free_window`, via `lstar_implies_hankel_posDef`): the
subordination makes every Hankel block through the cap positive
definite (the quadratic form of the signed defect measure evaluated at
the coefficient polynomial), hence every Sylvester ratio `h_k` is
positive -- pure finite algebra, no `sorry`.  The statement itself is
the open center in canonical form and carries the honest `sorry` --
since C1 as `lstar_canonical` in RH/Canonical.lean (the final-domain
retype: quantified over the canonical construction, no longer over the
opaque `MainWindow`).  NO RH CLAIM. -/

namespace VonMangoldtWindow

open Polynomial

variable (w : VonMangoldtWindow)

/-- the discrete `mu`-integral of `p^2` (real): `int p^2 dmu` over the
nonnegative von-Mangoldt comb channel. -/
noncomputable def muSq (p : Polynomial ℝ) : ℝ :=
  ∑ j, ((w.combWeight j : ℚ) : ℝ) * p.eval ((w.nodes j : ℚ) : ℝ) ^ 2

/-- the discrete `nu`-integral of `p^2` (real): `int p^2 dnu` over the
nonnegative archimedean/smooth channel. -/
noncomputable def nuSq (p : Polynomial ℝ) : ℝ :=
  ∑ j, ((w.archWeight j : ℚ) : ℝ) * p.eval ((w.nodes j : ℚ) : ℝ) ^ 2

/-- the coefficient polynomial of a vector `x : Fin n -> R`. -/
noncomputable def coeffPoly {n : ℕ} (x : Fin n → ℝ) : Polynomial ℝ :=
  ∑ i : Fin n, Polynomial.C (x i) * Polynomial.X ^ (i : ℕ)

theorem coeffPoly_eval {n : ℕ} (x : Fin n → ℝ) (t : ℝ) :
    (coeffPoly x).eval t = ∑ i : Fin n, x i * t ^ (i : ℕ) := by
  simp [coeffPoly, Polynomial.eval_finset_sum]

theorem coeffPoly_coeff {n : ℕ} (x : Fin n → ℝ) (i0 : Fin n) :
    (coeffPoly x).coeff (i0 : ℕ) = x i0 := by
  classical
  rw [coeffPoly, Polynomial.finset_sum_coeff]
  rw [Finset.sum_eq_single i0]
  · simp
  · intro i _ hne
    have hik : ((i0 : ℕ) ≠ (i : ℕ)) := fun h => hne (Fin.ext h.symm)
    simp [Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, hik]
  · intro h
    exact absurd (Finset.mem_univ i0) h

theorem coeffPoly_ne_zero {n : ℕ} {x : Fin n → ℝ} (hx : x ≠ 0) :
    coeffPoly x ≠ 0 := by
  obtain ⟨i0, hi0⟩ : ∃ i, x i ≠ 0 := Function.ne_iff.mp hx
  intro h0
  apply hi0
  have := coeffPoly_coeff x i0
  rw [h0] at this
  simpa using this.symm

theorem coeffPoly_natDegree_lt {n : ℕ} (hn : 0 < n) (x : Fin n → ℝ) :
    (coeffPoly x).natDegree < n := by
  rcases eq_or_ne (coeffPoly x) 0 with h0 | h0
  · simpa [h0] using hn
  · have hdeg : (coeffPoly x).degree < (n : ℕ) := by
      apply lt_of_le_of_lt (Polynomial.degree_sum_le _ _)
      rw [Finset.sup_lt_iff (by exact_mod_cast WithBot.bot_lt_coe n)]
      intro i _
      exact lt_of_le_of_lt (Polynomial.degree_C_mul_X_pow_le _ _)
        (by exact_mod_cast i.isLt)
    exact (Polynomial.natDegree_lt_iff_degree_lt h0).mpr hdeg

/-- **the quadratic-form dictionary** (finite algebra, PROVED): the
Hankel quadratic form of the signed defect measure evaluated at `x` is
the signed integral `int p_x^2 d(mu - nu)` of the coefficient
polynomial. -/
theorem hankel_quadform (n : ℕ) (x : Fin n → ℝ) :
    x ⬝ᵥ (w.hankel n *ᵥ x) = w.muSq (coeffPoly x) - w.nuSq (coeffPoly x) := by
  classical
  have hmom : ∀ m : ℕ, ((w.mom m : ℚ) : ℝ)
      = ∑ j, ((w.weight j : ℚ) : ℝ) * ((w.nodes j : ℚ) : ℝ) ^ m := by
    intro m
    rw [mom]
    push_cast
    rfl
  have hsplit : w.muSq (coeffPoly x) - w.nuSq (coeffPoly x)
      = ∑ j, ((w.weight j : ℚ) : ℝ)
          * ((coeffPoly x).eval ((w.nodes j : ℚ) : ℝ)) ^ 2 := by
    rw [muSq, nuSq, ← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [weight]
    push_cast
    ring
  rw [hsplit]
  have hrhs : ∀ j : Fin w.S,
      ((w.weight j : ℚ) : ℝ) * ((coeffPoly x).eval ((w.nodes j : ℚ) : ℝ)) ^ 2
      = ∑ i : Fin n, ∑ k : Fin n, x i * x k
          * (((w.weight j : ℚ) : ℝ) * ((w.nodes j : ℚ) : ℝ) ^ ((i : ℕ) + (k : ℕ))) := by
    intro j
    rw [coeffPoly_eval, sq, Finset.sum_mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [pow_add]
    ring
  calc x ⬝ᵥ (w.hankel n *ᵥ x)
      = ∑ i : Fin n, ∑ k : Fin n, x i * x k * ((w.mom ((i : ℕ) + (k : ℕ)) : ℚ) : ℝ) := by
        simp only [dotProduct, Matrix.mulVec, hankel, dotProduct]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun k _ => ?_
        ring
    _ = ∑ i : Fin n, ∑ k : Fin n, ∑ j, x i * x k
          * (((w.weight j : ℚ) : ℝ) * ((w.nodes j : ℚ) : ℝ) ^ ((i : ℕ) + (k : ℕ))) := by
        refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun k _ => ?_
        rw [hmom, Finset.mul_sum]
    _ = ∑ i : Fin n, ∑ j, ∑ k : Fin n, x i * x k
          * (((w.weight j : ℚ) : ℝ) * ((w.nodes j : ℚ) : ℝ) ^ ((i : ℕ) + (k : ℕ))) :=
        Finset.sum_congr rfl fun i _ => Finset.sum_comm
    _ = ∑ j, ∑ i : Fin n, ∑ k : Fin n, x i * x k
          * (((w.weight j : ℚ) : ℝ) * ((w.nodes j : ℚ) : ℝ) ^ ((i : ℕ) + (k : ℕ))) :=
        Finset.sum_comm
    _ = ∑ j, ((w.weight j : ℚ) : ℝ)
          * ((coeffPoly x).eval ((w.nodes j : ℚ) : ℝ)) ^ 2 := by
        refine Finset.sum_congr rfl fun j _ => (hrhs j).symm

end VonMangoldtWindow

open VonMangoldtWindow

/-! **THE CANONICAL FORM OF THE OPEN CENTER: lemma L*** -- C1 MOVE
(the reviewer final-domain contract): the open statement formerly
carried here as `lstar_subordination : MainWindow w → ...` is RETYPED
onto the canonical construction and now lives in RH/Canonical.lean as
`lstar_canonical : CanonicalWindow w → LStar w` (same mathematical
content -- the wave-6 / r283 / v963 subordination, ledger
`PRIME.LSTAR.SUBORDINATION.01` [O], standalone statement
rh/problem/lstar_problem.tex -- with the quantifier domain now the
actual completed prime-window construction instead of the fully
opaque `MainWindow` marker; retype justification at the statement).
The finite-algebra machinery below is hypothesis-form and unchanged. -/

/-- L* makes every Hankel block through the cap positive definite --
hypothesis form, PROVED (finite algebra via the quadratic-form
dictionary `hankel_quadform`). -/
theorem lstar_implies_hankel_posDef (w : VonMangoldtWindow)
    (hL : ∀ p : Polynomial ℝ, p ≠ 0 → p.natDegree < w.cap →
      w.nuSq p < w.muSq p) :
    ∀ n ≤ w.cap, 0 < n → (w.hankel n).PosDef := by
  intro n hn hpos
  refine Matrix.PosDef.of_dotProduct_mulVec_pos (w.hankel_isHermitian n)
    fun x hx => ?_
  have hform := w.hankel_quadform n x
  have hne := coeffPoly_ne_zero hx
  have hdeg : (coeffPoly x).natDegree < w.cap :=
    lt_of_lt_of_le (coeffPoly_natDegree_lt hpos x) hn
  have hlt := hL (coeffPoly x) hne hdeg
  have : (0 : ℝ) < w.muSq (coeffPoly x) - w.nuSq (coeffPoly x) := by
    linarith
  simpa [hform] using this

/-- **the proved direction: L* implies free-window positivity**
(hypothesis form, PROVED -- the wave-6 finite-algebra corollary tying
the canonical form to the fog-free hole: given the subordination, the
whole pivot chain through the cap is positive via the Sylvester
ratio). -/
theorem lstar_implies_free_window (w : VonMangoldtWindow)
    (hL : ∀ p : Polynomial ℝ, p ≠ 0 → p.natDegree < w.cap →
      w.nuSq p < w.muSq p) :
    ∀ n < w.cap, 0 < w.h n := by
  intro n hn
  have h1 : (w.hankel n).PosDef ∨ n = 0 := by
    rcases Nat.eq_zero_or_pos n with h0 | hpos
    · exact Or.inr h0
    · exact Or.inl (lstar_implies_hankel_posDef w hL n
        (Nat.le_of_lt hn) hpos)
  have h2 : (w.hankel (n + 1)).PosDef :=
    lstar_implies_hankel_posDef w hL (n + 1) hn (Nat.succ_pos n)
  rcases h1 with hpd | h0
  · exact w.h_pos_of_posDef hpd h2
  · subst h0
    have hdet0 : (w.hankel 0).det = 1 := Matrix.det_fin_zero
    have := h2.det_pos
    rw [VonMangoldtWindow.h, hdet0, div_one]
    exact this

/-! the composed corollaries on the final domain --
`lstar_free_window_main` and `free_window_positivity` (the wave-5
fog-free statement, ledger
`PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` [O]) MOVED to
RH/Canonical.lean with the C1 domain retype (`CanonicalWindow` in
place of the opaque `MainWindow`); proofs verbatim through
`lstar_implies_free_window` above. -/

/-! ## Toy instance: an exact rational miniature window
(S = 3 atoms, cap = 2) -- the definitions are TESTED against it below
by exact computation.  It instantiates the STRUCTURE, not `MainWindow`
(it is not a von-Mangoldt comb; nothing about `MainWindow` can or should
be provable for it -- that is the point of the r273 retype). -/

/-- toy window: nodes `0, 1, 2`, comb masses `1, 1, 1`, archimedean part
`0, 0, 3/4` (so the signed weights are `1, 1, 1/4`), border vector
constant `1/2`, budget `1`. -/
def toyWindow : VonMangoldtWindow where
  S := 3
  nodes := fun j => ((j : ℕ) : ℚ)
  combWeight := fun _ => 1
  archWeight := fun j => if (j : ℕ) = 2 then 3/4 else 0
  comb_nonneg := by intro j; norm_num
  arch_nonneg := by intro j; split <;> norm_num
  lo := 0
  hi := 2
  window_rule := by
    intro j
    refine ⟨Nat.cast_nonneg _, ?_⟩
    exact_mod_cast Nat.lt_succ_iff.mp j.isLt
  u := fun _ => 1/2
  B := 1

-- the half-filling cap is derived: `ceil(3/2) = 2`.
example : toyWindow.cap = 2 := rfl

-- structural projections (pure `rfl`, no arithmetic).
theorem toyWindow_comb (j : Fin 3) : toyWindow.combWeight j = 1 := rfl
theorem toyWindow_arch (j : Fin 3) :
    toyWindow.archWeight j = if (j : ℕ) = 2 then 3/4 else 0 := rfl
theorem toyWindow_nodes (j : Fin 3) : toyWindow.nodes j = ((j : ℕ) : ℚ) :=
  rfl
theorem toyWindow_u (k : ℕ) : toyWindow.u k = 1/2 := rfl
theorem toyWindow_B : toyWindow.B = 1 := rfl

-- exact signed moments: `m_0 = 9/4`, `m_1 = 3/2`, `m_2 = 2` (exact
-- rational computations from the structure).
example : toyWindow.mom 0 = 9/4 := by
  show ∑ j : Fin 3, toyWindow.weight j * toyWindow.nodes j ^ 0 = 9/4
  norm_num [VonMangoldtWindow.weight, toyWindow_comb, toyWindow_arch,
    toyWindow_nodes, Fin.sum_univ_three, Fin.val_zero, Fin.val_one,
    Fin.val_ofNat]
example : toyWindow.mom 1 = 3/2 := by
  show ∑ j : Fin 3, toyWindow.weight j * toyWindow.nodes j ^ 1 = 3/2
  norm_num [VonMangoldtWindow.weight, toyWindow_comb, toyWindow_arch,
    toyWindow_nodes, Fin.sum_univ_three, Fin.val_zero, Fin.val_one,
    Fin.val_ofNat]
example : toyWindow.mom 2 = 2 := by
  show ∑ j : Fin 3, toyWindow.weight j * toyWindow.nodes j ^ 2 = 2
  norm_num [VonMangoldtWindow.weight, toyWindow_comb, toyWindow_arch,
    toyWindow_nodes, Fin.sum_univ_three, Fin.val_zero, Fin.val_one,
    Fin.val_ofNat]

-- the chain head is the first minor ratio: `h_0 = m_0 / 1 = 9/4`.
example : toyWindow.h 0 = 9/4 := by
  have hm : toyWindow.mom 0 = 9/4 := by
    show ∑ j : Fin 3, toyWindow.weight j * toyWindow.nodes j ^ 0 = 9/4
    norm_num [VonMangoldtWindow.weight, toyWindow_comb, toyWindow_arch,
      toyWindow_nodes, Fin.sum_univ_three, Fin.val_zero, Fin.val_one,
      Fin.val_ofNat]
  rw [VonMangoldtWindow.h, Matrix.det_fin_one, Matrix.det_fin_zero]
  norm_num [VonMangoldtWindow.hankel, hm]

-- augmented-matrix entries: border and budget corners.
example : toyWindow.A 1 (Sum.inl 0) (Sum.inr ()) = 1/2 := by
  norm_num [VonMangoldtWindow.A, toyWindow_u, Matrix.fromBlocks_apply₁₂]
example : toyWindow.A 1 (Sum.inr ()) (Sum.inr ()) = 1 := by
  norm_num [VonMangoldtWindow.A, toyWindow_B, Matrix.fromBlocks_apply₂₂]

end RH
