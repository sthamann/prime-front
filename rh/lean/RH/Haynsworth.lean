/-
RH/Haynsworth.lean -- THE R373 TRANSCRIPTION (reviewer goal 1):
Haynsworth inertia additivity as a proved finite-matrix theorem,
plus the r367 two-rank cut (J = I₂) and the r369 mixed J-form.

Provenance:
  * r367 `final_two_rank_inertia_probe.py` (LEAN FORMALIZATION FORM
    of `haynsworth_two_rank`; implication is SATZ, premises P1/P2
    are census-grade arithmetic and are NOT theorems here);
  * r369 `mixed_haynsworth_probe.py` (general invertible symmetric
    J).  Both probes live in experiments/ and are NOT consumed as
    RH claims.

Finite real linear algebra only.  Does not assert P1/P2 on any
window.  NO RH CLAIM.
-/
import RH.Inertia
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Data.Matrix.Block
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.LinearAlgebra.QuadraticForm.Signature
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic.FinCases

namespace RH

open Matrix QuadraticMap QuadraticForm Unitary

/-! ## Quadratic-form bookkeeping -/

theorem toQuadraticMap'_apply_index {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n ℝ) (x : n → ℝ) :
    M.toQuadraticMap' x = x ⬝ᵥ (M *ᵥ x) :=
  Matrix.toLinearMap₂'_apply' M x x

theorem toQuadraticMap'_diagonal_index {n : Type*} [Fintype n] [DecidableEq n]
    (d : n → ℝ) :
    (diagonal d).toQuadraticMap' = weightedSumSquares ℝ d := by
  ext x
  simp [toQuadraticMap'_apply_index, weightedSumSquares_apply, dotProduct,
    Matrix.mulVec_diagonal]
  exact Finset.sum_congr rfl fun _ _ => by ring

theorem equivalent_toQuadraticMap'_congruence_index {n : Type*}
    [Fintype n] [DecidableEq n]
    (M P : Matrix n n ℝ) (hP : IsUnit P.det) :
    Equivalent (Pᵀ * M * P).toQuadraticMap' M.toQuadraticMap' := by
  haveI : Invertible P := P.invertibleOfIsUnitDet hP
  refine ⟨{ P.toLinearEquiv' ‹_› with map_app' := fun x => ?_ }⟩
  show M.toQuadraticMap' (Matrix.toLin' P x) = _
  rw [Matrix.toLin'_apply, toQuadraticMap'_apply_index,
    toQuadraticMap'_apply_index]
  rw [show (Pᵀ * M * P) *ᵥ x = Pᵀ *ᵥ (M *ᵥ (P *ᵥ x)) by
    rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, Matrix.mul_assoc]]
  conv_rhs => rw [Matrix.dotProduct_mulVec, Matrix.vecMul_transpose]

lemma isHermitian_eq_conj_diagonal {n : Type*} [Fintype n] [DecidableEq n]
    {A : Matrix n n ℝ} (hA : A.IsHermitian) :
    A = (hA.eigenvectorUnitary : Matrix n n ℝ) *
      diagonal hA.eigenvalues *
      star (hA.eigenvectorUnitary : Matrix n n ℝ) := by
  simpa [conjStarAlgAut_apply, Function.comp_def] using hA.spectral_theorem

lemma transpose_eq_star {n : Type*} (U : Matrix n n ℝ) : Uᵀ = star U := by
  simp [star_eq_conjTranspose, conjTranspose_eq_transpose_of_trivial]

lemma unitary_det_isUnit {n : Type*} [Fintype n] [DecidableEq n]
    (U : Matrix.unitaryGroup n ℝ) :
    IsUnit (U : Matrix n n ℝ).det :=
  (isUnit_iff_isUnit_det (U : Matrix n n ℝ)).mp isUnit_coe

/-- `sigNeg` of a real Hermitian matrix is the number of strictly
negative eigenvalues. -/
theorem sigNeg_eq_ncard_neg_eigenvalues {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    sigNeg A.toQuadraticMap' = {i : n | hA.eigenvalues i < 0}.ncard := by
  classical
  set U := hA.eigenvectorUnitary
  generalize hlam : hA.eigenvalues = lam
  have hform : A =
      (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
    simpa [U, hlam] using isHermitian_eq_conj_diagonal hA
  have hdiag : (U : Matrix n n ℝ)ᵀ * A * (U : Matrix n n ℝ) = diagonal lam := by
    rw [transpose_eq_star, hform]
    simp only [Matrix.mul_assoc, Matrix.mul_one]
    rw [← Matrix.mul_assoc (star (U : Matrix n n ℝ)),
      Unitary.coe_star_mul_self U, Matrix.one_mul, Matrix.mul_one]
  have hE : Equivalent A.toQuadraticMap' (weightedSumSquares ℝ lam) := by
    have hc := equivalent_toQuadraticMap'_congruence_index A
      (U : Matrix n n ℝ) (unitary_det_isUnit U)
    rw [hdiag, toQuadraticMap'_diagonal_index] at hc
    exact hc.symm
  simpa [hlam] using sigNeg_of_equiv_weightedSumSquares hE

lemma fromBlocks_diagonal_elim {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l] (d : n → ℝ) (e : l → ℝ) :
    fromBlocks (diagonal d) 0 0 (diagonal e) = diagonal (Sum.elim d e) := by
  ext i j
  cases i <;> cases j <;> simp [fromBlocks, diagonal]

lemma ncard_neg_sumElim {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l] (f : n → ℝ) (g : l → ℝ) :
    {i : n ⊕ l | Sum.elim f g i < 0}.ncard
      = {i : n | f i < 0}.ncard + {i : l | g i < 0}.ncard := by
  classical
  let e : {i : n ⊕ l // Sum.elim f g i < 0} ≃
      {i : n // f i < 0} ⊕ {i : l // g i < 0} :=
    { toFun := fun x =>
        match x with
        | ⟨.inl a, ha⟩ => .inl ⟨a, ha⟩
        | ⟨.inr b, hb⟩ => .inr ⟨b, hb⟩
      invFun := fun x =>
        match x with
        | .inl ⟨a, ha⟩ => ⟨.inl a, ha⟩
        | .inr ⟨b, hb⟩ => ⟨.inr b, hb⟩
      left_inv := fun ⟨x, _⟩ => by cases x <;> rfl
      right_inv := fun x => by cases x <;> rfl }
  have hcard := Fintype.card_congr e
  rw [Fintype.card_sum] at hcard
  simp_rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf, ← Fintype.card_subtype]
  exact hcard

lemma sigNeg_fromBlocks_diagonal {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (S : Matrix l l ℝ)
    (hA : A.IsHermitian) (hS : S.IsHermitian) :
    sigNeg (fromBlocks A (0 : Matrix n l ℝ) (0 : Matrix l n ℝ) S).toQuadraticMap'
      = sigNeg A.toQuadraticMap' + sigNeg S.toQuadraticMap' := by
  classical
  set UA := hA.eigenvectorUnitary
  set US := hS.eigenvectorUnitary
  generalize hlamA : hA.eigenvalues = lamA
  generalize hlamS : hS.eigenvalues = lamS
  set P : Matrix (n ⊕ l) (n ⊕ l) ℝ :=
    fromBlocks (UA : Matrix n n ℝ) 0 0 (US : Matrix l l ℝ)
  have hAform : A =
      (UA : Matrix n n ℝ) * diagonal lamA * star (UA : Matrix n n ℝ) := by
    simpa [UA, hlamA] using isHermitian_eq_conj_diagonal hA
  have hSform : S =
      (US : Matrix l l ℝ) * diagonal lamS * star (US : Matrix l l ℝ) := by
    simpa [US, hlamS] using isHermitian_eq_conj_diagonal hS
  have hPstar : Pᵀ =
      fromBlocks ((UA : Matrix n n ℝ)ᵀ) 0 0 ((US : Matrix l l ℝ)ᵀ) := by
    simp [P, fromBlocks_transpose]
  have hPstar' : Pᵀ =
      fromBlocks (star (UA : Matrix n n ℝ)) 0 0 (star (US : Matrix l l ℝ)) := by
    simpa [transpose_eq_star] using hPstar
  have hM :
      fromBlocks A (0 : Matrix n l ℝ) 0 S =
        P * fromBlocks (diagonal lamA) 0 0 (diagonal lamS) * Pᵀ := by
    have hstep :
        fromBlocks (UA : Matrix n n ℝ) 0 0 (US : Matrix l l ℝ) *
            fromBlocks (diagonal lamA) 0 0 (diagonal lamS) =
          fromBlocks ((UA : Matrix n n ℝ) * diagonal lamA) 0 0
            ((US : Matrix l l ℝ) * diagonal lamS) := by
      simp only [fromBlocks_multiply, Matrix.mul_zero, Matrix.zero_mul, add_zero,
        zero_add]
    rw [hAform, hSform, hPstar']
    simp only [P]
    rw [hstep]
    simp only [fromBlocks_multiply, Matrix.mul_zero, Matrix.zero_mul, add_zero,
      zero_add, Matrix.mul_assoc]
  have hPTP : Pᵀ * P = 1 := by
    rw [hPstar']
    simp only [P, fromBlocks_multiply, Matrix.mul_zero, Matrix.zero_mul, add_zero,
      zero_add]
    rw [Unitary.coe_star_mul_self UA, Unitary.coe_star_mul_self US, fromBlocks_one]
  have hdiag :
      Pᵀ * fromBlocks A (0 : Matrix n l ℝ) 0 S * P =
        diagonal (Sum.elim lamA lamS) := by
    rw [hM]
    simp only [Matrix.mul_assoc, Matrix.mul_one]
    rw [← Matrix.mul_assoc Pᵀ, hPTP, Matrix.one_mul, fromBlocks_diagonal_elim,
      Matrix.mul_one]
  have hPunit : IsUnit P.det := by
    have : P.det = (UA : Matrix n n ℝ).det * (US : Matrix l l ℝ).det :=
      det_fromBlocks_zero₂₁ _ 0 _
    rw [this]
    exact (unitary_det_isUnit UA).mul (unitary_det_isUnit US)
  have hE : Equivalent
      (fromBlocks A (0 : Matrix n l ℝ) 0 S).toQuadraticMap'
      (weightedSumSquares ℝ (Sum.elim lamA lamS)) := by
    have hc := equivalent_toQuadraticMap'_congruence_index
      (fromBlocks A (0 : Matrix n l ℝ) 0 S) P hPunit
    rw [hdiag, toQuadraticMap'_diagonal_index] at hc
    exact hc.symm
  have hcount := ncard_neg_sumElim lamA lamS
  rw [sigNeg_of_equiv_weightedSumSquares hE, hcount]
  simp [hlamA, hlamS, sigNeg_eq_ncard_neg_eigenvalues A hA,
    sigNeg_eq_ncard_neg_eigenvalues S hS]

/-! ## Schur congruence -/

theorem schur_elim_congruence {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (B : Matrix n l ℝ) (D : Matrix l l ℝ)
    (hA : A.IsHermitian) [Invertible A] :
    let T : Matrix (n ⊕ l) (n ⊕ l) ℝ := fromBlocks 1 (-(A⁻¹ * B)) 0 1
    let S : Matrix l l ℝ := D - Bᵀ * (A⁻¹ * B)
    T.det = 1 ∧
      Tᵀ * fromBlocks A B Bᵀ D * T = fromBlocks A 0 0 S := by
  intro T S
  have hAsymm : Aᵀ = A := by
    simpa [conjTranspose_eq_transpose_of_trivial] using hA.eq
  have hAunit : IsUnit A.det := isUnit_det_of_invertible A
  have hAAinv : A * A⁻¹ = 1 := Matrix.mul_nonsing_inv A hAunit
  have hAinvA : A⁻¹ * A = 1 := Matrix.nonsing_inv_mul A hAunit
  have hAinvT : (A⁻¹)ᵀ = A⁻¹ := by rw [Matrix.transpose_nonsing_inv, hAsymm]
  refine ⟨?_, ?_⟩
  · rw [det_fromBlocks_zero₂₁]; simp
  · have hXT : fromBlocks A B Bᵀ D * T = fromBlocks A 0 Bᵀ S := by
      simp only [T, fromBlocks_multiply]
      congr 1
      · simp
      · simp [Matrix.mul_neg, ← Matrix.mul_assoc, hAAinv]
      · simp
      · simp [S, Matrix.mul_neg, Matrix.mul_one, neg_add_eq_sub]
    rw [Matrix.mul_assoc, hXT]
    simp only [T, fromBlocks_transpose, transpose_one, transpose_zero,
      transpose_neg, Matrix.transpose_mul, hAinvT]
    rw [fromBlocks_multiply]
    congr 1
    · simp
    · simp
    · simp [Matrix.neg_mul, Matrix.mul_assoc, hAinvA]
    · simp

/-- Bottom-right Schur face via the mathlib LDU factorization. -/
theorem schur_elim_congruence₂₂ {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (B : Matrix n l ℝ) (D : Matrix l l ℝ)
    (hD : D.IsHermitian) [Invertible D] :
    let T : Matrix (n ⊕ l) (n ⊕ l) ℝ := fromBlocks 1 0 (-(D⁻¹ * Bᵀ)) 1
    let S : Matrix n n ℝ := A - B * (D⁻¹ * Bᵀ)
    T.det = 1 ∧
      Tᵀ * fromBlocks A B Bᵀ D * T = fromBlocks S 0 0 D := by
  intro T S
  have hDsymm : Dᵀ = D := by
    simpa [conjTranspose_eq_transpose_of_trivial] using hD.eq
  have hDunit : IsUnit D.det := isUnit_det_of_invertible D
  have hDinvT : (D⁻¹)ᵀ = D⁻¹ := by rw [Matrix.transpose_nonsing_inv, hDsymm]
  have hinvOf : ⅟D = D⁻¹ := invOf_eq_nonsing_inv D
  refine ⟨?_, ?_⟩
  · rw [det_fromBlocks_zero₁₂]; simp
  · set Umat : Matrix (n ⊕ l) (n ⊕ l) ℝ :=
      fromBlocks 1 0 (⅟D * Bᵀ) 1
    set Δ : Matrix (n ⊕ l) (n ⊕ l) ℝ :=
      fromBlocks (A - B * ⅟D * Bᵀ) 0 0 D
    have hLDU := fromBlocks_eq_of_invertible₂₂ (A := A) (B := B)
      (C := Bᵀ) (D := D)
    have hLeq : fromBlocks (1 : Matrix n n ℝ) (B * ⅟D) 0 1 = Umatᵀ := by
      simp [Umat, fromBlocks_transpose, Matrix.transpose_mul, hDinvT, hinvOf]
    have hM : fromBlocks A B Bᵀ D = Umatᵀ * Δ * Umat := by
      rw [hLDU, hLeq]
    have hSΔ : Δ = fromBlocks S 0 0 D := by
      simp [Δ, S, hinvOf, Matrix.mul_assoc]
    have hUT : Umat * T = 1 := by
      simp [Umat, T, fromBlocks_multiply, hinvOf, Matrix.mul_neg, fromBlocks_one]
    have hconj : Tᵀ * (Umatᵀ * Δ * Umat) * T = Δ := by
      calc Tᵀ * (Umatᵀ * Δ * Umat) * T
          = (Umat * T)ᵀ * Δ * (Umat * T) := by
            simp [Matrix.transpose_mul, Matrix.mul_assoc]
        _ = (1 : Matrix (n ⊕ l) (n ⊕ l) ℝ)ᵀ * Δ * 1 := by rw [hUT]
        _ = Δ := by simp
    rw [hM, hconj, hSΔ]

theorem sigNeg_congruence {n : Type*} [Fintype n] [DecidableEq n]
    (M P : Matrix n n ℝ) (hP : IsUnit P.det) :
    sigNeg (Pᵀ * M * P).toQuadraticMap' = sigNeg M.toQuadraticMap' :=
  (equivalent_toQuadraticMap'_congruence_index M P hP).sigNeg_eq

/-- Haynsworth additivity, top-left invertible. -/
theorem haynsworth_sigNeg_₁₁ {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (B : Matrix n l ℝ) (D : Matrix l l ℝ)
    (hA : A.IsHermitian) (hD : D.IsHermitian) [Invertible A]
    (hH : (fromBlocks A B Bᵀ D).IsHermitian) :
    sigNeg (fromBlocks A B Bᵀ D).toQuadraticMap'
      = sigNeg A.toQuadraticMap'
        + sigNeg (D - Bᵀ * A⁻¹ * B).toQuadraticMap' := by
  classical
  obtain ⟨hTdet, hstep⟩ := schur_elim_congruence (A := A) (B := B) (D := D) hA
  set T : Matrix (n ⊕ l) (n ⊕ l) ℝ := fromBlocks 1 (-(A⁻¹ * B)) 0 1
  have hTunit : IsUnit T.det := isUnit_iff_ne_zero.mpr (by simp [hTdet])
  have hS : (D - Bᵀ * A⁻¹ * B).IsHermitian := by
    have hiff :=
      (IsHermitian.fromBlocks₁₁ (A := A) B D hA).mp
        (by simpa [conjTranspose_eq_transpose_of_trivial] using hH)
    simpa [conjTranspose_eq_transpose_of_trivial, invOf_eq_nonsing_inv] using hiff
  have hstep' : Tᵀ * fromBlocks A B Bᵀ D * T
      = fromBlocks A 0 0 (D - Bᵀ * A⁻¹ * B) :=
    hstep.trans (by simp [Matrix.mul_assoc])
  rw [← sigNeg_congruence (fromBlocks A B Bᵀ D) T hTunit, hstep']
  exact sigNeg_fromBlocks_diagonal A (D - Bᵀ * A⁻¹ * B) hA hS

/-- Haynsworth additivity, bottom-right invertible. -/
theorem haynsworth_sigNeg_₂₂ {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (B : Matrix n l ℝ) (D : Matrix l l ℝ)
    (hA : A.IsHermitian) (hD : D.IsHermitian) [Invertible D]
    (hH : (fromBlocks A B Bᵀ D).IsHermitian) :
    sigNeg (fromBlocks A B Bᵀ D).toQuadraticMap'
      = sigNeg (A - B * D⁻¹ * Bᵀ).toQuadraticMap'
        + sigNeg D.toQuadraticMap' := by
  classical
  obtain ⟨hTdet, hstep⟩ := schur_elim_congruence₂₂ (A := A) (B := B) (D := D) hD
  set T : Matrix (n ⊕ l) (n ⊕ l) ℝ := fromBlocks 1 0 (-(D⁻¹ * Bᵀ)) 1
  have hTunit : IsUnit T.det := isUnit_iff_ne_zero.mpr (by simp [hTdet])
  have hS : (A - B * D⁻¹ * Bᵀ).IsHermitian := by
    have hiff :=
      (IsHermitian.fromBlocks₂₂ (D := D) A B hD).mp
        (by simpa [conjTranspose_eq_transpose_of_trivial] using hH)
    simpa [conjTranspose_eq_transpose_of_trivial, invOf_eq_nonsing_inv] using hiff
  have hstep' : Tᵀ * fromBlocks A B Bᵀ D * T
      = fromBlocks (A - B * D⁻¹ * Bᵀ) 0 0 D :=
    hstep.trans (by simp [Matrix.mul_assoc])
  rw [← sigNeg_congruence (fromBlocks A B Bᵀ D) T hTunit, hstep']
  exact sigNeg_fromBlocks_diagonal (A - B * D⁻¹ * Bᵀ) D hS hD

/-! ## 2×2 mixed signature and the two-rank cut -/

lemma ncard_fin2_neg_of_lt_gt {lam : Fin 2 → ℝ} (h0 : lam 0 < 0) (h1 : 0 < lam 1) :
    {i : Fin 2 | lam i < 0}.ncard = 1 := by
  rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf]
  have : Finset.univ.filter (fun i : Fin 2 => lam i < 0) = {0} := by
    ext i; fin_cases i <;> simp [h0, not_lt.mpr h1.le]
  simp [this]

lemma ncard_fin2_neg_of_gt_lt {lam : Fin 2 → ℝ} (h0 : 0 < lam 0) (h1 : lam 1 < 0) :
    {i : Fin 2 | lam i < 0}.ncard = 1 := by
  rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf]
  have : Finset.univ.filter (fun i : Fin 2 => lam i < 0) = {1} := by
    ext i; fin_cases i <;> simp [h1, not_lt.mpr h0.le]
  simp [this]

lemma ncard_fin2_pos_of_lt_gt {lam : Fin 2 → ℝ} (h0 : lam 0 < 0) (h1 : 0 < lam 1) :
    {i : Fin 2 | 0 < lam i}.ncard = 1 := by
  rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf]
  have : Finset.univ.filter (fun i : Fin 2 => 0 < lam i) = {1} := by
    ext i; fin_cases i <;> simp [h1, not_lt.mpr h0.le]
  simp [this]

lemma ncard_fin2_pos_of_gt_lt {lam : Fin 2 → ℝ} (h0 : 0 < lam 0) (h1 : lam 1 < 0) :
    {i : Fin 2 | 0 < lam i}.ncard = 1 := by
  rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf]
  have : Finset.univ.filter (fun i : Fin 2 => 0 < lam i) = {0} := by
    ext i; fin_cases i <;> simp [h0, not_lt.mpr h1.le]
  simp [this]

lemma prod_eigenvalues_fin2 {M : Matrix (Fin 2) (Fin 2) ℝ} (hM : M.IsHermitian) :
    M.det = hM.eigenvalues 0 * hM.eigenvalues 1 := by
  rw [hM.det_eq_prod_eigenvalues, Fin.prod_univ_two]
  simp

theorem sigNeg_eq_one_of_det_neg_fin2 {M : Matrix (Fin 2) (Fin 2) ℝ}
    (hM : M.IsHermitian) (hdet : M.det < 0) :
    sigNeg M.toQuadraticMap' = 1 := by
  classical
  have hlam : hM.eigenvalues 0 * hM.eigenvalues 1 < 0 := by
    rwa [← prod_eigenvalues_fin2 hM]
  have hcount : {i : Fin 2 | hM.eigenvalues i < 0}.ncard = 1 := by
    rcases (mul_neg_iff.mp hlam) with ⟨h0, h1⟩ | ⟨h0, h1⟩
    · exact ncard_fin2_neg_of_gt_lt h0 h1
    · exact ncard_fin2_neg_of_lt_gt h0 h1
  rwa [sigNeg_eq_ncard_neg_eigenvalues M hM]

lemma isHermitian_one_real {n : Type*} [Fintype n] [DecidableEq n] :
    (1 : Matrix n n ℝ).IsHermitian := isHermitian_one

lemma sigNeg_neg_one_fin2 :
    sigNeg (-(1 : Matrix (Fin 2) (Fin 2) ℝ)).toQuadraticMap' = 2 := by
  classical
  have hdiag : -(1 : Matrix (Fin 2) (Fin 2) ℝ) =
      diagonal fun _ : Fin 2 => (-1 : ℝ) := by
    ext i j
    by_cases hij : i = j <;> simp [hij, diagonal, Matrix.one_apply, Matrix.neg_apply]
  have hE : Equivalent (-(1 : Matrix (Fin 2) (Fin 2) ℝ)).toQuadraticMap'
      (weightedSumSquares ℝ fun _ : Fin 2 => (-1 : ℝ)) := by
    rw [hdiag, toQuadraticMap'_diagonal_index]
    rfl
  rw [sigNeg_of_equiv_weightedSumSquares hE]
  simp [Set.ncard_univ]

lemma isHermitian_U_sandwich {n l : Type*} [Fintype n] [Fintype l]
    [DecidableEq n] [DecidableEq l]
    (A : Matrix n n ℝ) (U : Matrix n l ℝ) (hA : A.IsHermitian) [Invertible A] :
    (Uᵀ * A⁻¹ * U).IsHermitian := by
  simpa [conjTranspose_eq_transpose_of_trivial] using
    (isHermitian_conjTranspose_mul_mul (B := U) hA.inv)

lemma inv_neg_one_fin2 :
    (-(1 : Matrix (Fin 2) (Fin 2) ℝ))⁻¹ = -(1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  apply Matrix.inv_eq_left_inv
  ext i j
  simp [Matrix.mul_apply, Matrix.neg_apply, Matrix.one_apply]

@[implicit_reducible]
def invertible_neg_one_fin2 :
    Invertible (-(1 : Matrix (Fin 2) (Fin 2) ℝ)) :=
  invertibleOfLeftInverse _ (-(1 : Matrix (Fin 2) (Fin 2) ℝ)) <| by
    ext i j
    simp [Matrix.mul_apply, Matrix.neg_apply, Matrix.one_apply]

/-- **THE r367 TWO-RANK THEOREM** (J = I₂; PROVED).  If a real
Hermitian `A0` is invertible with exactly one negative inertia
direction and the 2×2 Schur matrix `K₂ = I + Uᵀ A0⁻¹ U` has negative
determinant, then `A0 + U Uᵀ` is positive definite.

Finite algebra only.  Does not assert the r367 census premises P1/P2
on any window.  NO RH CLAIM. -/
theorem haynsworth_two_rank {n : ℕ} (A0 : Matrix (Fin n) (Fin n) ℝ)
    (U : Matrix (Fin n) (Fin 2) ℝ)
    (hSym : A0.IsHermitian) [Invertible A0]
    (hP1 : sigNeg A0.toQuadraticMap' = 1)
    (hP2 : ((1 : Matrix (Fin 2) (Fin 2) ℝ) + Uᵀ * A0⁻¹ * U).det < 0) :
    (A0 + U * Uᵀ).PosDef := by
  classical
  letI := invertible_neg_one_fin2
  set K2 : Matrix (Fin 2) (Fin 2) ℝ := 1 + Uᵀ * A0⁻¹ * U
  set H : Matrix (Fin n ⊕ Fin 2) (Fin n ⊕ Fin 2) ℝ :=
    fromBlocks A0 U Uᵀ (-(1 : Matrix (Fin 2) (Fin 2) ℝ))
  have hIherm : (-(1 : Matrix (Fin 2) (Fin 2) ℝ)).IsHermitian :=
    isHermitian_one_real.neg
  have hH : H.IsHermitian :=
    IsHermitian.fromBlocks hSym
      (by simp [conjTranspose_eq_transpose_of_trivial]) hIherm
  have hK2herm : K2.IsHermitian :=
    isHermitian_one_real.add (isHermitian_U_sandwich A0 U hSym)
  have hschur11 :
      (-(1 : Matrix (Fin 2) (Fin 2) ℝ)) - Uᵀ * A0⁻¹ * U = -K2 := by
    simp [K2, sub_eq_add_neg, add_comm, add_left_comm, add_assoc, neg_add]
  have hschur22 :
      A0 - U * (-(1 : Matrix (Fin 2) (Fin 2) ℝ))⁻¹ * Uᵀ = A0 + U * Uᵀ := by
    rw [inv_neg_one_fin2]
    simp [Matrix.mul_neg, sub_neg_eq_add]
  have h11 := haynsworth_sigNeg_₁₁ A0 U (-(1 : Matrix (Fin 2) (Fin 2) ℝ))
    hSym hIherm hH
  have h22 := haynsworth_sigNeg_₂₂ A0 U (-(1 : Matrix (Fin 2) (Fin 2) ℝ))
    hSym hIherm hH
  have hK2neg : sigNeg K2.toQuadraticMap' = 1 :=
    sigNeg_eq_one_of_det_neg_fin2 hK2herm hP2
  have hnegK2 : sigNeg (-K2).toQuadraticMap' = 1 := by
    have hKH : (-K2).IsHermitian := hK2herm.neg
    generalize hlam : hK2herm.eigenvalues = lam
    have hform : K2 =
        (hK2herm.eigenvectorUnitary : Matrix (Fin 2) (Fin 2) ℝ) *
          diagonal lam *
          star (hK2herm.eigenvectorUnitary : Matrix (Fin 2) (Fin 2) ℝ) := by
      simpa [hlam] using isHermitian_eq_conj_diagonal hK2herm
    set UK := hK2herm.eigenvectorUnitary
    have hnegform : -K2 =
        (UK : Matrix (Fin 2) (Fin 2) ℝ) *
          diagonal (fun i => -lam i) *
          star (UK : Matrix (Fin 2) (Fin 2) ℝ) := by
      have hD : -(diagonal lam) = diagonal fun i => -lam i := by
        ext i j; by_cases hij : i = j <;> simp [hij, diagonal, Matrix.neg_apply]
      have hmid : ∀ (A D B : Matrix (Fin 2) (Fin 2) ℝ),
          -(A * D * B) = A * (-D) * B := fun A D B => by
        calc -(A * D * B)
            = -(A * (D * B)) := by rw [Matrix.mul_assoc]
          _ = A * (-(D * B)) := by rw [← Matrix.mul_neg]
          _ = A * ((-D) * B) := by rw [Matrix.neg_mul]
          _ = A * (-D) * B := by rw [← Matrix.mul_assoc]
      calc -K2
          = -((UK : Matrix (Fin 2) (Fin 2) ℝ) * diagonal lam *
              star (UK : Matrix (Fin 2) (Fin 2) ℝ)) := by rw [hform]
        _ = (UK : Matrix (Fin 2) (Fin 2) ℝ) * (-diagonal lam) *
              star (UK : Matrix (Fin 2) (Fin 2) ℝ) := hmid _ _ _
        _ = (UK : Matrix (Fin 2) (Fin 2) ℝ) * diagonal (fun i => -lam i) *
              star (UK : Matrix (Fin 2) (Fin 2) ℝ) := by rw [hD]
    have hdiag : (UK : Matrix (Fin 2) (Fin 2) ℝ)ᵀ * (-K2) *
        (UK : Matrix (Fin 2) (Fin 2) ℝ) = diagonal fun i => -lam i := by
      rw [hnegform, transpose_eq_star]
      simp only [Matrix.mul_assoc, Matrix.mul_one]
      rw [← Matrix.mul_assoc (star (UK : Matrix (Fin 2) (Fin 2) ℝ)),
        Unitary.coe_star_mul_self UK, Matrix.one_mul, Matrix.mul_one]
    have hE : Equivalent (-K2).toQuadraticMap'
        (weightedSumSquares ℝ fun i => -lam i) := by
      have hc := equivalent_toQuadraticMap'_congruence_index (-K2)
        (UK : Matrix (Fin 2) (Fin 2) ℝ) (unitary_det_isUnit UK)
      rw [hdiag, toQuadraticMap'_diagonal_index] at hc
      exact hc.symm
    have hprod : lam 0 * lam 1 < 0 := by
      have hprod0 := prod_eigenvalues_fin2 hK2herm
      rw [hlam] at hprod0
      have : K2.det < 0 := hP2
      linarith
    have hcard : {i : Fin 2 | -lam i < 0}.ncard = 1 := by
      have : {i : Fin 2 | -lam i < 0} = {i : Fin 2 | 0 < lam i} := by
        ext i; simp [neg_lt_zero]
      rw [this]
      have hne0 : lam 0 ≠ 0 := fun h => by simp [h] at hprod
      rcases (mul_neg_iff.mp hprod) with ⟨h0, h1⟩ | ⟨h0, h1⟩
      · exact ncard_fin2_pos_of_gt_lt h0 h1
      · exact ncard_fin2_pos_of_lt_gt h0 h1
    rw [sigNeg_of_equiv_weightedSumSquares hE]
    simpa using hcard
  have hnegM : sigNeg (A0 + U * Uᵀ).toQuadraticMap' = 0 := by
    have hL : sigNeg H.toQuadraticMap' = 2 := by
      rw [h11, hP1, hschur11, hnegK2]
    have hR : sigNeg H.toQuadraticMap'
        = sigNeg (A0 + U * Uᵀ).toQuadraticMap' + 2 := by
      rw [h22, hschur22, sigNeg_neg_one_fin2]
    omega
  have hAunit : IsUnit A0.det := isUnit_det_of_invertible A0
  have hdet : (A0 + U * Uᵀ).det ≠ 0 := by
    rw [det_add_mul U Uᵀ hAunit]
    have hK2ne : K2.det ≠ 0 := hP2.ne
    exact mul_ne_zero hAunit.ne_zero (by simpa [K2] using hK2ne)
  have hMh : (A0 + U * Uᵀ).IsHermitian :=
    hSym.add (by
      simpa [conjTranspose_eq_transpose_of_trivial] using
        isHermitian_mul_conjTranspose_self U)
  rw [hMh.posDef_iff_eigenvalues_pos]
  intro i
  have hne : hMh.eigenvalues i ≠ 0 := by
    intro hz
    apply hdet
    rw [hMh.det_eq_prod_eigenvalues]
    exact Finset.prod_eq_zero (Finset.mem_univ i) (by simpa using hz)
  have hncard := sigNeg_eq_ncard_neg_eigenvalues (A0 + U * Uᵀ) hMh
  rw [hnegM] at hncard
  have hnotneg : ¬ hMh.eigenvalues i < 0 := by
    intro hlt
    have : {j | hMh.eigenvalues j < 0}.Nonempty := ⟨i, hlt⟩
    have : 0 < {j | hMh.eigenvalues j < 0}.ncard := this.ncard_pos
    omega
  exact lt_of_le_of_ne (not_lt.mp hnotneg) (Ne.symm hne)

lemma inv_neg_nonsingInv {l : Type*} [Fintype l] [DecidableEq l]
    (J : Matrix l l ℝ) [Invertible J] :
    (-J⁻¹)⁻¹ = -J := by
  apply Matrix.inv_eq_left_inv
  rw [neg_mul_neg]
  exact Matrix.mul_nonsing_inv J (isUnit_det_of_invertible J)

/-- **Generalized Haynsworth** (r369 mixed form; PROVED).  For
invertible Hermitian `A`, `J` and rectangular `U`,
  `In [[A, U], [Uᵀ, −J⁻¹]] = In(A) + In(−Φ) = In(−J⁻¹) + In(A + U J Uᵀ)`
with `Φ = J⁻¹ + Uᵀ A⁻¹ U`.  The r367 two-rank theorem is `J = I₂`.
NO RH CLAIM. -/
theorem haynsworth_mixed {n k : Type*} [Fintype n] [Fintype k]
    [DecidableEq n] [DecidableEq k]
    (A : Matrix n n ℝ) (U : Matrix n k ℝ) (J : Matrix k k ℝ)
    (hA : A.IsHermitian) (hJ : J.IsHermitian)
    [Invertible A] [Invertible J] :
    let Φ := J⁻¹ + Uᵀ * A⁻¹ * U
    let H := fromBlocks A U Uᵀ (-J⁻¹)
    let M := A + U * J * Uᵀ
    sigNeg H.toQuadraticMap'
        = sigNeg A.toQuadraticMap' + sigNeg (-Φ).toQuadraticMap'
      ∧ sigNeg H.toQuadraticMap'
        = sigNeg M.toQuadraticMap' + sigNeg (-J⁻¹).toQuadraticMap' := by
  intro Φ H M
  have hnegJH : (-J⁻¹).IsHermitian := hJ.inv.neg
  have hH : H.IsHermitian :=
    IsHermitian.fromBlocks hA
      (by simp [conjTranspose_eq_transpose_of_trivial]) hnegJH
  haveI : Invertible (-J⁻¹) :=
    invertibleOfLeftInverse _ (-J) <| by
      rw [neg_mul_neg]
      exact Matrix.mul_nonsing_inv J (isUnit_det_of_invertible J)
  have h11eq : (-J⁻¹) - Uᵀ * A⁻¹ * U = -Φ := by
    simp [Φ, sub_eq_add_neg, add_comm, add_left_comm, add_assoc, neg_add]
  have h22eq : A - U * (-J⁻¹)⁻¹ * Uᵀ = M := by
    rw [inv_neg_nonsingInv J]
    simp [M, Matrix.mul_neg, sub_neg_eq_add]
  constructor
  · have h := haynsworth_sigNeg_₁₁ A U (-J⁻¹) hA hnegJH hH
    simpa [H, h11eq] using h
  · have h := haynsworth_sigNeg_₂₂ A U (-J⁻¹) hA hnegJH hH
    simpa [H, M, h22eq] using h

end RH
