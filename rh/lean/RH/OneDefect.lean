/-
RH/OneDefect.lean -- r406: the general one-defect absorption theorems
as sorry-free finite real matrix algebra (DCCLXIX SATZ A/B/C).

Targets (reviewer R406; independent of the source-side R404/R405
probes):
  1. `indNeg_sub_rankOne_le_one` -- PROVED.  H ≻ 0 ⇒
     ind₋(H − ℓℓᵀ) ≤ 1.  Direct corollary of
     `rankOne_inertia_antitone` (RH/PivotCoordinate.lean) plus
     `indNeg_eq_zero_of_posDef`: rewrite H − ℓℓᵀ + ℓℓᵀ = H ≻ 0.
  2. `oneDefect_update_posDef_iff` -- PROVED.  H ≻ 0, J ≻ 0 ⇒
     (H − ℓℓᵀ + U J Uᵀ) ≻ 0 ⟺ 0 < Δ := 1 − ℓᵀH⁻¹ℓ + rᵀK⁻¹r,
     r = UᵀH⁻¹ℓ, K = J⁻¹ + UᵀH⁻¹U.  Kernel: the rank-1 Schur
     criterion `posDef_sub_rankOne_iff` (block det +
     `posDef_fromBlocks_border` / `fromBlocks₂₂`) plus the
     Woodbury identity `woodbury_inv`.  mathlib v4.29.1 has Schur
     complements, Weinstein–Aronszajn (`det_one_add_mul_comm`),
     the matrix-determinant lemma (`det_add_mul`), and
     `mul_inv_rev`; it does not name Woodbury.
  3. `posDef_of_contractive_lift` -- PROVED.  Vᵀ injective,
     ℓ = V c, ‖c‖² < 1 ⇒ (V Vᵀ − ℓℓᵀ) ≻ 0, by Cauchy–Schwarz
     (`Finset.sum_mul_sq_le_sq_mul_sq`).
  4. `cMin_normSq` / `posDef_gram_sub_rankOne_iff` -- PROVED.
     ‖c_min‖² = ℓᵀ(VVᵀ)⁻¹ℓ and (VVᵀ − ℓℓᵀ) ≻ 0 ⟺ 0 < 1 − ‖c_min‖²
     (the Gram-side Δ).

Does not assert (P1)/(P2), L*, or any window census.  Zero `sorry`.
Census of the pilot stays 5.  NO RH CLAIM.

Provenance: DCCLXIX reviewer re-adjudication; PRIME.LDAGGER.ONE_DEFECT_LEAN.01.
-/
import RH.PivotCoordinate
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.RowCol
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.StarOrdered

namespace RH

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ## Rank-one Gram bookkeeping -/

lemma isHermitian_sub_vecMulVec {H : Matrix n n ℝ} (hH : H.IsHermitian)
    (ℓ : n → ℝ) : (H - vecMulVec ℓ ℓ).IsHermitian :=
  hH.sub (isHermitian_vecMulVec_self ℓ)

lemma conjTranspose_replicateCol_real (ℓ : n → ℝ) :
    (replicateCol Unit ℓ)ᴴ = replicateRow Unit ℓ :=
  conjTranspose_replicateCol (ι := Unit) ℓ

lemma vecMulVec_eq_col_mul_row (ℓ : n → ℝ) :
    vecMulVec ℓ ℓ = replicateCol Unit ℓ * replicateRow Unit ℓ :=
  vecMulVec_eq Unit ℓ ℓ

lemma vecMulVec_eq_col_mul_conj (ℓ : n → ℝ) :
    vecMulVec ℓ ℓ = replicateCol Unit ℓ * (replicateCol Unit ℓ)ᴴ := by
  rw [vecMulVec_eq_col_mul_row, conjTranspose_replicateCol_real]

lemma sandwich_inv (M : Matrix n n ℝ) (ℓ : n → ℝ) :
    (replicateRow Unit ℓ * M * replicateCol Unit ℓ) () () = ℓ ⬝ᵥ (M *ᵥ ℓ) := by
  simp [Matrix.mul_apply, dotProduct, mulVec, replicateRow_apply,
    replicateCol_apply, Finset.sum_mul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun _ _ => ?_
  simp [Finset.mul_sum, mul_left_comm, mul_assoc]

/-- The rank-one border in the `Bᴴ` convention of `fromBlocks₂₂`. -/
def rankOneBorder (H : Matrix n n ℝ) (ℓ : n → ℝ) :
    Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ :=
  fromBlocks H (replicateCol Unit ℓ) (replicateCol Unit ℓ)ᴴ (1 : Matrix Unit Unit ℝ)

lemma rankOneBorder_eq_fun (H : Matrix n n ℝ) (ℓ : n → ℝ) :
    rankOneBorder H ℓ =
      fromBlocks H (fun i (_ : Unit) => ℓ i) (fun (_ : Unit) j => ℓ j)
        (fun _ _ => (1 : ℝ)) := by
  ext (i | ⟨⟩) (j | ⟨⟩)
  · rfl
  · rfl
  · simp [rankOneBorder, fromBlocks, conjTranspose_replicateCol_real,
      replicateRow_apply]
  · simp [rankOneBorder, fromBlocks, Matrix.one_apply]

lemma rankOneBorder_eq_row (H : Matrix n n ℝ) (ℓ : n → ℝ) :
    rankOneBorder H ℓ =
      fromBlocks H (replicateCol Unit ℓ) (replicateRow Unit ℓ)
        (1 : Matrix Unit Unit ℝ) := by
  simp only [rankOneBorder, conjTranspose_replicateCol_real]

lemma schur_rankOne_entry (H : Matrix n n ℝ) (ℓ : n → ℝ) [Invertible H] :
    ((1 : Matrix Unit Unit ℝ) - replicateRow Unit ℓ * H⁻¹ * replicateCol Unit ℓ) () () =
      1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) := by
  simp [Matrix.sub_apply, Matrix.one_apply, sandwich_inv]

lemma det_rankOne_border (H : Matrix n n ℝ) (ℓ : n → ℝ) [Invertible H] :
    (rankOneBorder H ℓ).det = H.det * (1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ)) := by
  rw [rankOneBorder_eq_row]
  have hdet :=
    det_fromBlocks₁₁ H (replicateCol Unit ℓ) (replicateRow Unit ℓ)
      (1 : Matrix Unit Unit ℝ)
  have hinv : ⅟H = H⁻¹ := invOf_eq_nonsing_inv H
  have h1x1 :
      ((1 : Matrix Unit Unit ℝ) - replicateRow Unit ℓ * ⅟H * replicateCol Unit ℓ).det =
        1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) := by
    rw [Matrix.det_unique, hinv, schur_rankOne_entry]
  rw [hdet, h1x1]

lemma schur_rankOne_block (H : Matrix n n ℝ) (ℓ : n → ℝ) :
    H - replicateCol Unit ℓ * (1 : Matrix Unit Unit ℝ)⁻¹ * (replicateCol Unit ℓ)ᴴ =
      H - vecMulVec ℓ ℓ := by
  rw [inv_one, Matrix.mul_one, vecMulVec_eq_col_mul_conj]

/-! ## Lemma 1: negative inertia of a rank-one downdate -/

/-- Positive definite matrices have vanishing negative inertia. -/
theorem indNeg_eq_zero_of_posDef {H : Matrix n n ℝ} (hH : H.PosDef) :
    indNeg H = 0 := by
  classical
  rw [indNeg, sigNeg_eq_ncard_neg_eigenvalues H hH.isHermitian]
  have hempty : {i : n | hH.isHermitian.eigenvalues i < 0} = ∅ := by
    ext i
    simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
    exact not_lt.mpr (hH.eigenvalues_pos i).le
  simp [hempty]

/-- **SATZ A** (DCCLXIX / r406; PROVED).  If `H ≻ 0`, then a rank-one
downdate drops at most one negative eigenvalue:
  `ind₋(H − ℓℓᵀ) ≤ 1`.
Rewrite `A := H − ℓℓᵀ`, so `A + ℓℓᵀ = H ≻ 0`, and apply the second
half of `rankOne_inertia_antitone`.  NO RH CLAIM. -/
theorem indNeg_sub_rankOne_le_one {H : Matrix n n ℝ} (hH : H.PosDef)
    (ℓ : n → ℝ) : indNeg (H - vecMulVec ℓ ℓ) ≤ 1 := by
  have hA : (H - vecMulVec ℓ ℓ).IsHermitian :=
    isHermitian_sub_vecMulVec hH.isHermitian ℓ
  have hsum : (H - vecMulVec ℓ ℓ) + vecMulVec ℓ ℓ = H := sub_add_cancel _ _
  have hanti := (rankOne_inertia_antitone (H - vecMulVec ℓ ℓ) ℓ hA).2
  have h0 : indNeg H = 0 := indNeg_eq_zero_of_posDef hH
  rw [hsum] at hanti
  linarith

/-! ## Rank-one Schur criterion (kernel of SATZ B) -/

lemma posDef_one_unit : (1 : Matrix Unit Unit ℝ).PosDef := PosDef.one

/-- **Rank-one Schur criterion.**  For `H ≻ 0`,
  `H − ℓℓᵀ ≻ 0` if and only if `ℓᵀ H⁻¹ ℓ < 1`.  NO RH CLAIM. -/
theorem posDef_sub_rankOne_iff {H : Matrix n n ℝ} (hH : H.PosDef)
    (ℓ : n → ℝ) :
    (H - vecMulVec ℓ ℓ).PosDef ↔ ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) < 1 := by
  classical
  haveI : Invertible H := hH.isUnit.invertible
  haveI : Invertible (1 : Matrix Unit Unit ℝ) := invertibleOne
  let Bcol : Matrix n Unit ℝ := replicateCol Unit ℓ
  let M : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ := rankOneBorder H ℓ
  have hMdef : M = fromBlocks H Bcol Bcolᴴ (1 : Matrix Unit Unit ℝ) := rfl
  have hschur :
      H - Bcol * (1 : Matrix Unit Unit ℝ)⁻¹ * Bcolᴴ = H - vecMulVec ℓ ℓ :=
    schur_rankOne_block H ℓ
  have hdetM : M.det = H.det * (1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ)) :=
    det_rankOne_border H ℓ
  have hHdet : 0 < H.det := hH.det_pos
  have hfun :
      fromBlocks H (fun i (_ : Unit) => ℓ i) (fun (_ : Unit) j => ℓ j)
          (fun _ _ => (1 : ℝ)) = M :=
    (rankOneBorder_eq_fun H ℓ).symm
  constructor
  · intro hA
    have hApsd : (H - vecMulVec ℓ ℓ).PosSemidef := hA.posSemidef
    have hMpsd : M.PosSemidef := by
      have hiff :=
        PosDef.fromBlocks₂₂ (A := H) Bcol (D := (1 : Matrix Unit Unit ℝ))
          posDef_one_unit
      rw [hMdef]
      exact hiff.mpr (by rwa [hschur])
    have hAdet : 0 < (H - vecMulVec ℓ ℓ).det := hA.det_pos
    have hMdet : M.det ≠ 0 := by
      have hdet22 := det_fromBlocks₂₂ H Bcol Bcolᴴ (1 : Matrix Unit Unit ℝ)
      have : M.det = (H - Bcol * ⅟(1 : Matrix Unit Unit ℝ) * Bcolᴴ).det := by
        rw [hMdef, hdet22, det_one, one_mul]
      rw [this, invOf_one, Matrix.mul_one]
      simpa [Bcol, vecMulVec_eq_col_mul_conj] using hAdet.ne'
    have hMpd : M.PosDef := posDef_of_posSemidef_det_ne_zero hMpsd hMdet
    have hprod := hMpd.det_pos
    rw [hdetM] at hprod
    rcases (mul_pos_iff.mp hprod) with ⟨_, hs⟩ | ⟨hneg, _⟩
    · linarith
    · exact (not_lt_of_gt hHdet hneg).elim
  · intro hη
    have hschur_pos : 0 < 1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) := sub_pos.mpr hη
    have hMdet_pos : 0 < M.det := by
      rw [hdetM]
      exact mul_pos hHdet hschur_pos
    have hMpd : M.PosDef := by
      have hborder := posDef_fromBlocks_border (A := H) (v := ℓ) (d := 1) hH
        (by rwa [hfun])
      rwa [← hfun]
    have hApsd : (H - vecMulVec ℓ ℓ).PosSemidef := by
      have hiff :=
        PosDef.fromBlocks₂₂ (A := H) Bcol (D := (1 : Matrix Unit Unit ℝ))
          posDef_one_unit
      have hMpsd : (fromBlocks H Bcol Bcolᴴ (1 : Matrix Unit Unit ℝ)).PosSemidef := by
        rw [← hMdef]
        exact hMpd.posSemidef
      have := hiff.mp hMpsd
      rwa [hschur] at this
    have hAdet : (H - vecMulVec ℓ ℓ).det ≠ 0 := by
      have hdet22 := det_fromBlocks₂₂ H Bcol Bcolᴴ (1 : Matrix Unit Unit ℝ)
      have : M.det = (H - Bcol * ⅟(1 : Matrix Unit Unit ℝ) * Bcolᴴ).det := by
        rw [hMdef, hdet22, det_one, one_mul]
      rw [this, invOf_one, Matrix.mul_one] at hMdet_pos
      simpa [Bcol, vecMulVec_eq_col_mul_conj] using hMdet_pos.ne'
    exact posDef_of_posSemidef_det_ne_zero hApsd hAdet

/-! ## Woodbury identity -/

variable {k : Type*} [Fintype k] [DecidableEq k]

/-- Gram `Uᵀ H⁻¹ U` is positive semidefinite when `H ≻ 0`. -/
lemma posSemidef_gram_inv {H : Matrix n n ℝ} (hH : H.PosDef)
    (U : Matrix n k ℝ) : (Uᵀ * H⁻¹ * U).PosSemidef := by
  have h := hH.inv.posSemidef.conjTranspose_mul_mul_same U
  rwa [conjTranspose_eq_transpose_of_trivial] at h

/-- `U J Uᵀ` is positive semidefinite when `J ≻ 0`. -/
lemma posSemidef_congruence_posDef {J : Matrix k k ℝ} (hJ : J.PosDef)
    (U : Matrix n k ℝ) : (U * J * Uᵀ).PosSemidef := by
  have h := hJ.posSemidef.mul_mul_conjTranspose_same U
  rwa [conjTranspose_eq_transpose_of_trivial] at h

/-- The Woodbury pivot `K = J⁻¹ + Uᵀ H⁻¹ U` is positive definite. -/
lemma oneDefectK_posDef {H : Matrix n n ℝ} {J : Matrix k k ℝ}
    (hH : H.PosDef) (hJ : J.PosDef) (U : Matrix n k ℝ) :
    (J⁻¹ + Uᵀ * H⁻¹ * U).PosDef :=
  hJ.inv.add_posSemidef (posSemidef_gram_inv hH U)

/-- `H + U J Uᵀ` is positive definite. -/
lemma posDef_add_congruence {H : Matrix n n ℝ} {J : Matrix k k ℝ}
    (hH : H.PosDef) (hJ : J.PosDef) (U : Matrix n k ℝ) :
    (H + U * J * Uᵀ).PosDef :=
  hH.add_posSemidef (posSemidef_congruence_posDef hJ U)

/-- **Woodbury identity.**  For `H ≻ 0`, `J ≻ 0`,
  `(H + U J Uᵀ)⁻¹ = H⁻¹ − H⁻¹ U K⁻¹ Uᵀ H⁻¹`,
  `K = J⁻¹ + Uᵀ H⁻¹ U`.  mathlib v4.29.1 does not name this. -/
theorem woodbury_inv {H : Matrix n n ℝ} {J : Matrix k k ℝ}
    (hH : H.PosDef) (hJ : J.PosDef) (U : Matrix n k ℝ) :
    (H + U * J * Uᵀ)⁻¹ =
      H⁻¹ - H⁻¹ * U * (J⁻¹ + Uᵀ * H⁻¹ * U)⁻¹ * Uᵀ * H⁻¹ := by
  set K : Matrix k k ℝ := J⁻¹ + Uᵀ * H⁻¹ * U
  have hK : K.PosDef := oneDefectK_posDef hH hJ U
  have hHunit : IsUnit H.det := (isUnit_iff_isUnit_det H).mp hH.isUnit
  have hKunit : IsUnit K.det := (isUnit_iff_isUnit_det K).mp hK.isUnit
  have hJunit : IsUnit J.det := (isUnit_iff_isUnit_det J).mp hJ.isUnit
  refine Matrix.inv_eq_right_inv ?_
  have hLeft :
      (H + U * J * Uᵀ) * H⁻¹ = 1 + U * J * Uᵀ * H⁻¹ := by
    rw [add_mul, mul_nonsing_inv H hHunit]
  have hRight :
      (H + U * J * Uᵀ) * (H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) =
        U * J * Uᵀ * H⁻¹ := by
    have hsplit :
        (H + U * J * Uᵀ) * (H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) =
          U * K⁻¹ * Uᵀ * H⁻¹ + U * J * (Uᵀ * H⁻¹ * U) * K⁻¹ * Uᵀ * H⁻¹ := by
      rw [add_mul]
      have h1 : H * (H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) = U * K⁻¹ * Uᵀ * H⁻¹ := by
        simp [← Matrix.mul_assoc, mul_nonsing_inv H hHunit]
      have h2 :
          (U * J * Uᵀ) * (H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) =
            U * J * (Uᵀ * H⁻¹ * U) * K⁻¹ * Uᵀ * H⁻¹ := by
        simp [Matrix.mul_assoc]
      rw [h1, h2]
    have hJK : (1 : Matrix k k ℝ) + J * (Uᵀ * H⁻¹ * U) = J * K := by
      simp only [K, Matrix.mul_add, mul_nonsing_inv J hJunit]
    have hsum :
        K⁻¹ + J * (Uᵀ * H⁻¹ * U) * K⁻¹ =
          ((1 : Matrix k k ℝ) + J * (Uᵀ * H⁻¹ * U)) * K⁻¹ := by
      simp [Matrix.add_mul, Matrix.mul_assoc]
    have hJKK : ((1 : Matrix k k ℝ) + J * (Uᵀ * H⁻¹ * U)) * K⁻¹ = J := by
      rw [hJK, Matrix.mul_assoc, mul_nonsing_inv K hKunit, Matrix.mul_one]
    have hfac :
        U * K⁻¹ * Uᵀ * H⁻¹ + U * J * (Uᵀ * H⁻¹ * U) * K⁻¹ * Uᵀ * H⁻¹ =
          U * J * Uᵀ * H⁻¹ := by
      calc U * K⁻¹ * Uᵀ * H⁻¹ + U * J * (Uᵀ * H⁻¹ * U) * K⁻¹ * Uᵀ * H⁻¹
          = U * K⁻¹ * Uᵀ * H⁻¹ +
              U * (J * (Uᵀ * H⁻¹ * U) * K⁻¹) * Uᵀ * H⁻¹ := by
                simp [Matrix.mul_assoc]
        _ = U * (K⁻¹ + J * (Uᵀ * H⁻¹ * U) * K⁻¹) * Uᵀ * H⁻¹ := by
              simp [Matrix.mul_add, Matrix.add_mul, Matrix.mul_assoc]
        _ = U * (((1 : Matrix k k ℝ) + J * (Uᵀ * H⁻¹ * U)) * K⁻¹) *
              Uᵀ * H⁻¹ := by rw [hsum]
        _ = U * J * Uᵀ * H⁻¹ := by rw [hJKK]
    rw [hsplit, hfac]
  calc (H + U * J * Uᵀ) * (H⁻¹ - H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹)
      = (H + U * J * Uᵀ) * H⁻¹ -
          (H + U * J * Uᵀ) * (H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) := mul_sub _ _ _
    _ = 1 + U * J * Uᵀ * H⁻¹ - U * J * Uᵀ * H⁻¹ := by rw [hLeft, hRight]
    _ = 1 := by simp

/-! ## Lemma 2: one-defect PosDef criterion -/

/-- The one-defect discriminant `Δ = 1 − η + rᵀ K⁻¹ r`. -/
noncomputable def oneDefectDelta (H : Matrix n n ℝ) (J : Matrix k k ℝ)
    (U : Matrix n k ℝ) (ℓ : n → ℝ) : ℝ :=
  let r := Uᵀ *ᵥ (H⁻¹ *ᵥ ℓ)
  let K := J⁻¹ + Uᵀ * H⁻¹ * U
  1 - ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) + r ⬝ᵥ (K⁻¹ *ᵥ r)

lemma herm_nonsingInv {H : Matrix n n ℝ} (hH : H.IsHermitian) :
    H⁻¹ᵀ = H⁻¹ := by
  simpa [conjTranspose_eq_transpose_of_trivial] using hH.inv.eq

lemma oneDefectDelta_eq_woodbury {H : Matrix n n ℝ} {J : Matrix k k ℝ}
    (hH : H.PosDef) (hJ : J.PosDef) (U : Matrix n k ℝ) (ℓ : n → ℝ) :
    oneDefectDelta H J U ℓ =
      1 - ℓ ⬝ᵥ ((H + U * J * Uᵀ)⁻¹ *ᵥ ℓ) := by
  have hW := woodbury_inv hH hJ U
  set r := Uᵀ *ᵥ (H⁻¹ *ᵥ ℓ)
  set K := J⁻¹ + Uᵀ * H⁻¹ * U
  have hAt : H⁻¹ᵀ = H⁻¹ := herm_nonsingInv hH.isHermitian
  have hform :
      ℓ ⬝ᵥ ((H⁻¹ - H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) *ᵥ ℓ) =
        ℓ ⬝ᵥ (H⁻¹ *ᵥ ℓ) - r ⬝ᵥ (K⁻¹ *ᵥ r) := by
    have hsub :
        (H⁻¹ - H⁻¹ * U * K⁻¹ * Uᵀ * H⁻¹) *ᵥ ℓ =
          H⁻¹ *ᵥ ℓ - H⁻¹ *ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) := by
      simp [sub_mulVec, mulVec_mulVec, r, Matrix.mul_assoc]
    rw [hsub, dotProduct_sub]
    have hsym :
        ℓ ⬝ᵥ (H⁻¹ *ᵥ (U *ᵥ (K⁻¹ *ᵥ r))) =
          (H⁻¹ *ᵥ ℓ) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) := by
      calc ℓ ⬝ᵥ (H⁻¹ *ᵥ (U *ᵥ (K⁻¹ *ᵥ r)))
          = (ℓ ᵥ* H⁻¹) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) := by
              rw [dotProduct_mulVec]
        _ = (H⁻¹ᵀ *ᵥ ℓ) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) := by
              rw [← mulVec_transpose]
        _ = (H⁻¹ *ᵥ ℓ) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) := by rw [hAt]
    have hU :
        (H⁻¹ *ᵥ ℓ) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r)) = r ⬝ᵥ (K⁻¹ *ᵥ r) := by
      calc (H⁻¹ *ᵥ ℓ) ⬝ᵥ (U *ᵥ (K⁻¹ *ᵥ r))
          = ((H⁻¹ *ᵥ ℓ) ᵥ* U) ⬝ᵥ (K⁻¹ *ᵥ r) := by
              rw [dotProduct_mulVec]
        _ = (Uᵀ *ᵥ (H⁻¹ *ᵥ ℓ)) ⬝ᵥ (K⁻¹ *ᵥ r) := by
              rw [← mulVec_transpose]
        _ = r ⬝ᵥ (K⁻¹ *ᵥ r) := rfl
    rw [hsym, hU]
  rw [oneDefectDelta, hW, hform]
  ring

/-- **SATZ B** (DCCLXIX / r406; PROVED).  For `H ≻ 0` and `J ≻ 0`,
  `(H − ℓℓᵀ + U J Uᵀ) ≻ 0` if and only if `0 < Δ`.  NO RH CLAIM. -/
theorem oneDefect_update_posDef_iff {H : Matrix n n ℝ} {J : Matrix k k ℝ}
    (hH : H.PosDef) (hJ : J.PosDef) (U : Matrix n k ℝ) (ℓ : n → ℝ) :
    (H - vecMulVec ℓ ℓ + U * J * Uᵀ).PosDef ↔
      0 < oneDefectDelta H J U ℓ := by
  have hB : (H + U * J * Uᵀ).PosDef := posDef_add_congruence hH hJ U
  have hrew : H - vecMulVec ℓ ℓ + U * J * Uᵀ =
      (H + U * J * Uᵀ) - vecMulVec ℓ ℓ := by
    abel
  rw [hrew, posDef_sub_rankOne_iff hB ℓ, oneDefectDelta_eq_woodbury hH hJ U ℓ]
  constructor <;> intro h <;> linarith

/-! ## Lemma 3: contractive Gram lift -/

lemma dotProduct_sq_le {ι : Type*} [Fintype ι] (x y : ι → ℝ) :
    (x ⬝ᵥ y) ^ 2 ≤ (x ⬝ᵥ x) * (y ⬝ᵥ y) := by
  have h := Finset.sum_mul_sq_le_sq_mul_sq (s := (Finset.univ : Finset ι)) x y
  simpa [dotProduct, pow_two] using h

lemma dotProduct_self_pos {ι : Type*} [Fintype ι] {x : ι → ℝ} (hx : x ≠ 0) :
    0 < x ⬝ᵥ x := by
  obtain ⟨i, hi⟩ := Function.ne_iff.mp hx
  have hterm : 0 < x i ^ 2 := sq_pos_of_ne_zero hi
  have hle : x i ^ 2 ≤ ∑ j, x j ^ 2 :=
    Finset.single_le_sum (fun j _ => sq_nonneg (x j)) (Finset.mem_univ i)
  have : (∑ j, x j ^ 2) = x ⬝ᵥ x := by simp [dotProduct, pow_two]
  exact lt_of_lt_of_le hterm (this ▸ hle)

lemma vecMul_eq_transpose_mulVec (V : Matrix n k ℝ) (x : n → ℝ) :
    x ᵥ* V = Vᵀ *ᵥ x :=
  (mulVec_transpose V x).symm

lemma injective_vecMul_of_transpose_mulVec {V : Matrix n k ℝ}
    (hV : Function.Injective Vᵀ.mulVec) : Function.Injective V.vecMul := by
  intro x y hxy
  apply hV
  simpa [vecMul_eq_transpose_mulVec] using hxy

lemma posDef_gram {V : Matrix n k ℝ}
    (hV : Function.Injective Vᵀ.mulVec) : (V * Vᵀ).PosDef := by
  have h := PosDef.mul_conjTranspose_self V
    (injective_vecMul_of_transpose_mulVec hV)
  rwa [conjTranspose_eq_transpose_of_trivial] at h

/-- **SATZ C** (DCCLXIX / r406; PROVED).  If `Vᵀ` is injective
and `ℓ = V c` with `‖c‖² < 1`, then `V Vᵀ − ℓℓᵀ ≻ 0`.  NO RH CLAIM. -/
theorem posDef_of_contractive_lift {V : Matrix n k ℝ}
    (hV : Function.Injective Vᵀ.mulVec) (c : k → ℝ) (hc : c ⬝ᵥ c < 1) :
    (V * Vᵀ - vecMulVec (V *ᵥ c) (V *ᵥ c)).PosDef := by
  refine PosDef.of_dotProduct_mulVec_pos ?_ ?_
  · exact (posDef_gram hV).isHermitian.sub (isHermitian_vecMulVec_self _)
  · intro x hx
    have hyne : Vᵀ *ᵥ x ≠ 0 := by
      intro h0
      have : Vᵀ *ᵥ x = Vᵀ *ᵥ 0 := by simpa using h0
      exact hx (hV this)
    set y := Vᵀ *ᵥ x
    have hform :
        star x ⬝ᵥ ((V * Vᵀ - vecMulVec (V *ᵥ c) (V *ᵥ c)) *ᵥ x) =
          y ⬝ᵥ y - (c ⬝ᵥ y) ^ 2 := by
      have hsub :
          (V * Vᵀ - vecMulVec (V *ᵥ c) (V *ᵥ c)) *ᵥ x =
            (V * Vᵀ) *ᵥ x - vecMulVec (V *ᵥ c) (V *ᵥ c) *ᵥ x :=
        sub_mulVec _ _ _
      rw [hsub, dotProduct_sub]
      have hGram : star x ⬝ᵥ ((V * Vᵀ) *ᵥ x) = y ⬝ᵥ y := by
        have : x ⬝ᵥ ((V * Vᵀ) *ᵥ x) = (Vᵀ *ᵥ x) ⬝ᵥ (Vᵀ *ᵥ x) := by
          calc x ⬝ᵥ ((V * Vᵀ) *ᵥ x)
              = x ⬝ᵥ (V *ᵥ (Vᵀ *ᵥ x)) := by rw [mulVec_mulVec]
            _ = (x ᵥ* V) ⬝ᵥ (Vᵀ *ᵥ x) := by rw [dotProduct_mulVec]
            _ = (Vᵀ *ᵥ x) ⬝ᵥ (Vᵀ *ᵥ x) := by rw [vecMul_eq_transpose_mulVec]
        simpa using this
      have hdot : (V *ᵥ c) ⬝ᵥ x = c ⬝ᵥ y := by
        calc (V *ᵥ c) ⬝ᵥ x
            = x ⬝ᵥ (V *ᵥ c) := dotProduct_comm _ _
          _ = (x ᵥ* V) ⬝ᵥ c := by rw [dotProduct_mulVec]
          _ = (Vᵀ *ᵥ x) ⬝ᵥ c := by rw [vecMul_eq_transpose_mulVec]
          _ = c ⬝ᵥ (Vᵀ *ᵥ x) := dotProduct_comm _ _
      have hrank :
          star x ⬝ᵥ (vecMulVec (V *ᵥ c) (V *ᵥ c) *ᵥ x) = (c ⬝ᵥ y) ^ 2 := by
        rw [mulVec_vecMulVec_self]
        have hsq : star x ⬝ᵥ ((V *ᵥ c ⬝ᵥ x) • (V *ᵥ c)) =
            (V *ᵥ c ⬝ᵥ x) ^ 2 := by
          simp [dotProduct_smul, smul_eq_mul, pow_two, dotProduct_comm]
        rw [hsq, hdot]
      simpa using congrArg₂ (fun a b => a - b) hGram hrank
    have hCS : (c ⬝ᵥ y) ^ 2 ≤ (c ⬝ᵥ c) * (y ⬝ᵥ y) := dotProduct_sq_le c y
    have hypos : 0 < y ⬝ᵥ y := dotProduct_self_pos hyne
    have hge : (1 - c ⬝ᵥ c) * (y ⬝ᵥ y) ≤ y ⬝ᵥ y - (c ⬝ᵥ y) ^ 2 := by
      linarith
    have hfac : 0 < (1 - c ⬝ᵥ c) * (y ⬝ᵥ y) :=
      mul_pos (sub_pos.mpr hc) hypos
    have : 0 < y ⬝ᵥ y - (c ⬝ᵥ y) ^ 2 := lt_of_lt_of_le hfac hge
    rwa [hform]

/-! ## Lemma 4: min-norm coefficient and Δ -/

/-- Min-norm coefficient `c_min = Vᵀ (V Vᵀ)⁻¹ ℓ`. -/
noncomputable def cMin (V : Matrix n k ℝ) (ℓ : n → ℝ) : k → ℝ :=
  Vᵀ *ᵥ ((V * Vᵀ)⁻¹ *ᵥ ℓ)

/-- **Min-norm identity.**  `‖c_min‖² = ℓᵀ (V Vᵀ)⁻¹ ℓ`. -/
theorem cMin_normSq {V : Matrix n k ℝ} (hV : Function.Injective Vᵀ.mulVec)
    (ℓ : n → ℝ) :
    cMin V ℓ ⬝ᵥ cMin V ℓ = ℓ ⬝ᵥ ((V * Vᵀ)⁻¹ *ᵥ ℓ) := by
  have hB : (V * Vᵀ).PosDef := posDef_gram hV
  have hunit : IsUnit (V * Vᵀ).det := (isUnit_iff_isUnit_det _).mp hB.isUnit
  set z := (V * Vᵀ)⁻¹ *ᵥ ℓ
  have hz : (V * Vᵀ) *ᵥ z = ℓ := by
    calc (V * Vᵀ) *ᵥ ((V * Vᵀ)⁻¹ *ᵥ ℓ)
        = ((V * Vᵀ) * (V * Vᵀ)⁻¹) *ᵥ ℓ := by rw [mulVec_mulVec]
      _ = (1 : Matrix n n ℝ) *ᵥ ℓ := by rw [mul_nonsing_inv _ hunit]
      _ = ℓ := one_mulVec _
  have hadj : (Vᵀ *ᵥ z) ⬝ᵥ (Vᵀ *ᵥ z) = z ⬝ᵥ ((V * Vᵀ) *ᵥ z) := by
    calc (Vᵀ *ᵥ z) ⬝ᵥ (Vᵀ *ᵥ z)
        = (z ᵥ* V) ⬝ᵥ (Vᵀ *ᵥ z) := by rw [vecMul_eq_transpose_mulVec]
      _ = z ⬝ᵥ (V *ᵥ (Vᵀ *ᵥ z)) := by rw [← dotProduct_mulVec]
      _ = z ⬝ᵥ ((V * Vᵀ) *ᵥ z) := by rw [mulVec_mulVec]
  calc cMin V ℓ ⬝ᵥ cMin V ℓ
      = (Vᵀ *ᵥ z) ⬝ᵥ (Vᵀ *ᵥ z) := rfl
    _ = z ⬝ᵥ ((V * Vᵀ) *ᵥ z) := hadj
    _ = z ⬝ᵥ ℓ := by rw [hz]
    _ = ℓ ⬝ᵥ z := dotProduct_comm _ _
    _ = ℓ ⬝ᵥ ((V * Vᵀ)⁻¹ *ᵥ ℓ) := rfl

/-- Gram-side Δ: `(V Vᵀ − ℓℓᵀ) ≻ 0` iff `0 < 1 − ‖c_min‖²`. -/
theorem posDef_gram_sub_rankOne_iff {V : Matrix n k ℝ}
    (hV : Function.Injective Vᵀ.mulVec) (ℓ : n → ℝ) :
    (V * Vᵀ - vecMulVec ℓ ℓ).PosDef ↔
      0 < 1 - cMin V ℓ ⬝ᵥ cMin V ℓ := by
  have hB := posDef_gram hV
  rw [posDef_sub_rankOne_iff hB ℓ, cMin_normSq hV ℓ]
  constructor <;> intro h <;> linarith

end RH
