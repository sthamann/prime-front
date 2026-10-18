/-
  DeltaOneNoGo — the δ₁ no-go: pin finiteness ⇏ strict section
  positivity.
  ================================================================

  Lean seam of round 93 (PRIME.SCREW.VERBLUNSKY.INVARIANT.01, V0b):
  numeric counterpart `experiments/tfpt-discovery/vbk_invariant_probe.py`
  (23/23 gates) and note CCCXCIII.  The no-go there: for the point
  measure μ = δ₁ on the circle, the Carathéodory function
  F(w) = (1+w)/(1-w) is finite with positive real part for 0 < w < 1,
  while EVERY n×n moment Toeplitz section is the all-ones matrix J_n —
  PSD but singular (det J_n = 0, rank 1) for n ≥ 2.  Consequently
  convergence/positivity of PIN VALUES cannot prove the STRICT section
  positivity needed to construct the Verblunsky/Schur carrier: the
  carrier cannot supply its own existence premise.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`) — the two component facts and their conjunction:

    (1) `toeplitz_deltaOneMoment` — the δ₁ moment sequence (every
        moment = 1; the measure-theoretic evaluation ∫ z^{-k} dδ₁ = 1
        is definitional bookkeeping recorded here as a definition, NOT
        formalized measure theory) has all its Toeplitz sections equal
        to the all-ones matrix.

    (2) `allOnes_posSemidef` — J_n IS PSD (the form is (Σc)², so δ₁ is
        an honest nonnegative measure), `allOnes_det_eq_zero` —
        det J_n = 0 for n ≥ 2, `allOnes_mulVec_eq_zero` — the explicit
        kernel vector e₀ − e₁ ≠ 0, `allOnes_not_posDef` — J_n is NOT
        positive definite for n ≥ 2 (via det_pos).  So strict section
        positivity FAILS at every size ≥ 2.

    (3) `caratheodoryDeltaOne_pos` — the pin side: F(w) = (1+w)/(1-w)
        is (finite and) strictly positive on 0 < w < 1.

    (4) `delta_one_no_go` — the packaged conjunction: positive pin
        values coexist with singular, non-PD sections at every size
        n ≥ 2.

  THE HONEST BOUNDARY.  This is a COUNTEREXAMPLE PACKAGE, not a
  general impossibility theorem: it exhibits one measure whose pin
  values are finite and positive while no Toeplitz section of size ≥ 2
  is strictly positive.  The moral drawn in V0b — "any (SV) ⇒ RH route
  through strict section positivity must obtain strictness from an
  input BEYOND pin finiteness/positivity" — is the correct reading of
  this counterexample; a general quantified no-go over all
  back-inference schemes is NOT stated and NOT claimed.  That F is the
  Herglotz/Carathéodory transform of δ₁ and that the all-ones matrices
  are its moment sections is classical bookkeeping cited from V0b, not
  re-derived from a formal measure integral.  No RH claim.
-/
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Tactic

namespace TfptCarrier
namespace DeltaOneNoGo

open Matrix

/-! ### (1) The δ₁ moment sequence and its Toeplitz sections -/

/-- The moment sequence of μ = δ₁ on the circle: every trigonometric
moment equals 1.  (The evaluation ∫ z^{-k} dδ₁(z) = 1 is definitional;
no measure theory is formalized — see module docstring.) -/
def deltaOneMoment : ℤ → ℝ := fun _ => 1

/-- The n×n Toeplitz section of a moment sequence c: entry (j,k) is
c(j−k). -/
def toeplitz (c : ℤ → ℝ) (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun j k => c ((j : ℤ) - (k : ℤ))

/-- The all-ones matrix J. -/
def allOnes (m : Type*) : Matrix m m ℝ :=
  Matrix.of fun _ _ => 1

/-- **Every Toeplitz section of δ₁ is the all-ones matrix** — the
moment side of the no-go, at every section size. -/
theorem toeplitz_deltaOneMoment (n : ℕ) :
    toeplitz deltaOneMoment n = allOnes (Fin n) :=
  rfl

/-! ### (2) The section side: PSD, singular, not PD -/

/-- J is PSD — the quadratic form is the perfect square (Σ_j c_j)²,
as befits the moment matrix of a nonnegative measure. -/
theorem allOnes_posSemidef (m : Type*) [Fintype m] :
    (allOnes m).PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ fun x => ?_
  · ext j k
    simp [allOnes]
  · have expand : x ⬝ᵥ (allOnes m *ᵥ x) = (∑ j, x j) ^ 2 := by
      simp only [allOnes, Matrix.mulVec, dotProduct, Matrix.of_apply,
        one_mul, sq]
      rw [← Finset.sum_mul]
    rw [star_trivial, expand]
    positivity

/-- **det J_n = 0 for n ≥ 2** — two equal rows.  Strict positivity of
the section fails at the determinant. -/
theorem allOnes_det_eq_zero {n : ℕ} (hn : 2 ≤ n) :
    (allOnes (Fin n)).det = 0 := by
  have h01 : (⟨0, by omega⟩ : Fin n) ≠ ⟨1, by omega⟩ := by
    simp [Fin.ext_iff]
  exact Matrix.det_zero_of_row_eq h01 rfl

/-- The explicit kernel vector: e₀ − e₁ is nonzero and J_n kills it
(each entry of J_n *ᵥ v is Σ_k v_k = 1 − 1 = 0). -/
theorem allOnes_mulVec_eq_zero {n : ℕ} (hn : 2 ≤ n) :
    ∃ v : Fin n → ℝ, v ≠ 0 ∧ allOnes (Fin n) *ᵥ v = 0 := by
  have h01 : (⟨0, by omega⟩ : Fin n) ≠ ⟨1, by omega⟩ := by
    simp [Fin.ext_iff]
  refine ⟨Pi.single ⟨0, by omega⟩ 1 - Pi.single ⟨1, by omega⟩ 1, ?_, ?_⟩
  · intro hv
    have h0 := congrFun hv ⟨0, by omega⟩
    simp at h0
  · funext j
    simp [allOnes, Matrix.mulVec, dotProduct, Pi.single_apply,
      Finset.sum_sub_distrib]

/-- **J_n is NOT positive definite for n ≥ 2**: positive definiteness
forces a positive determinant, but det J_n = 0. -/
theorem allOnes_not_posDef {n : ℕ} (hn : 2 ≤ n) :
    ¬ (allOnes (Fin n)).PosDef := fun h =>
  absurd (allOnes_det_eq_zero hn) (ne_of_gt h.det_pos)

/-! ### (3) The pin side: the Carathéodory value is finite and positive -/

/-- The Carathéodory function of μ = δ₁ evaluated at w ∈ (0,1):
F(w) = (1+w)/(1−w) (the Herglotz transform (z+w)/(z−w) at z = 1). -/
noncomputable def caratheodoryDeltaOne (w : ℝ) : ℝ :=
  (1 + w) / (1 - w)

/-- **The pin values are strictly positive** (and, being real numbers,
finite) on the whole pin range 0 < w < 1. -/
theorem caratheodoryDeltaOne_pos {w : ℝ} (hw0 : 0 < w) (hw1 : w < 1) :
    0 < caratheodoryDeltaOne w := by
  unfold caratheodoryDeltaOne
  have h1 : (0 : ℝ) < 1 + w := by linarith
  have h2 : (0 : ℝ) < 1 - w := by linarith
  positivity

/-! ### (4) The packaged no-go -/

/-- **THE δ₁ NO-GO** (packaged conjunction, V0b): for every pin
w ∈ (0,1) and every section size n ≥ 2 simultaneously —

  * the pin value F(w) is strictly positive (and finite),
  * the δ₁ Toeplitz section IS the all-ones matrix,
  * that section is PSD,
  * yet its determinant vanishes and it is NOT positive definite,
    with an explicit nonzero kernel vector.

Reading (see module docstring for the honest scope): pin finiteness
and positivity of a Carathéodory function do NOT imply the strict
positivity of its moment Toeplitz sections — the property a
Verblunsky/Schur carrier construction needs as its existence premise.
One counterexample suffices for the no-go; no general impossibility
over all schemes is claimed. -/
theorem delta_one_no_go {n : ℕ} (hn : 2 ≤ n) {w : ℝ}
    (hw0 : 0 < w) (hw1 : w < 1) :
    0 < caratheodoryDeltaOne w ∧
    toeplitz deltaOneMoment n = allOnes (Fin n) ∧
    (allOnes (Fin n)).PosSemidef ∧
    (allOnes (Fin n)).det = 0 ∧
    ¬ (allOnes (Fin n)).PosDef ∧
    ∃ v : Fin n → ℝ, v ≠ 0 ∧ allOnes (Fin n) *ᵥ v = 0 :=
  ⟨caratheodoryDeltaOne_pos hw0 hw1, toeplitz_deltaOneMoment n,
    allOnes_posSemidef (Fin n), allOnes_det_eq_zero hn,
    allOnes_not_posDef hn, allOnes_mulVec_eq_zero hn⟩

end DeltaOneNoGo
end TfptCarrier
