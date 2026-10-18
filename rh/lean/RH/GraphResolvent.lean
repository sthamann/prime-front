/-
RH/GraphResolvent.lean -- r412: the graph-resolvent dictionary as
sorry-free finite real matrix algebra (R407/R409/R411 consolidation).

Abstract forms only (no window / source objects).  Targets:

  (a) For `C ≻ 0`, the graph resolvent `R := C(I+C)⁻¹` is well-defined,
      `0 ≺ R ≺ I`, and the half-shift identity
        `R − ½I = ½ (I+C)⁻¹ (C − I)`.
      Inertia: `ind₋(R − ½I) = ind₋(C − I)` (Sylvester: `(I+C)⁻¹` is
      PD; the spectral theorem is the simultaneous eigenbasis).
  (b) Möbius: `ind₋(C − I) = ind₋(I − C⁻¹)` for `C ≻ 0`.  The
      factorization `I − C⁻¹ = C⁻¹(C − I)` is not a congruence; the
      true sandwich is `C⁻¹ (C−I) C⁻¹`, and the spectral form
      `C^{-1/2}(C−I)C^{-1/2}` has the same signs because `C ≻ 0`.
  (c) Energy split: if `𝔗ᵀ 𝔗 = C⁻¹`, then Euclidean contraction
      `∀ x, ‖𝔗 x‖ ≤ ‖x‖` iff `C ⪰ I`, and
      `ind₋(I − 𝔗ᵀ𝔗) ≤ 1` iff `ind₋(C − I) ≤ 1`.
  (d) Composition with the R† layer: the *zero-defect* face
      `C ≻ I` plus `q† < 1` implies `R† ≻ ½I` (A3+A5, proved).
      The one-defect lift at the cap (depth gap `N-3` vs cap, CD
      identification of `C`) is the named Prop
      `GraphResolventIsLEnsembleInv`; same class as `P1EqCapInertia`.

Does not assert (P1)/(P2), L*, or any window census.  Zero `sorry`.
Census of the pilot stays 5.  NO RH CLAIM.

Provenance: r407 dual intertwiner; r409 Borodin–Birkhoff graph
identity; r411 energy split.  PRIME.LDAGGER.GRAPH_RESOLVENT_LEAN.01.
-/
import RH.OneDefect
import RH.DualResolvent
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.QuadraticForm.Signature
import Mathlib.Tactic.FieldSimp

namespace RH

open Matrix QuadraticMap QuadraticForm Unitary

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ## Graph resolvent -/

/-- Graph resolvent `R := C(I+C)⁻¹`.  Alias of the L-ensemble
transform of `RH/DualResolvent.lean`. -/
noncomputable def graphResolvent (C : Matrix n n ℝ) : Matrix n n ℝ :=
  lEnsemble C

lemma graphResolvent_eq (C : Matrix n n ℝ) :
    graphResolvent C = C * (1 + C)⁻¹ :=
  rfl

lemma one_add_posDef {C : Matrix n n ℝ} (hC : C.PosDef) :
    (1 + C).PosDef :=
  posDef_one_add_of_posSemidef hC.posSemidef

lemma one_add_det_isUnit {C : Matrix n n ℝ} (hC : C.PosDef) :
    IsUnit (1 + C).det :=
  (isUnit_iff_isUnit_det _).mp (one_add_posDef hC).isUnit

/-- `R = I − (I+C)⁻¹`. -/
theorem graphResolvent_eq_one_sub_inv {C : Matrix n n ℝ} (hC : C.PosDef) :
    graphResolvent C = 1 - (1 + C)⁻¹ := by
  have h := dualResolvent_eq_one_sub_lEnsemble C (one_add_det_isUnit hC)
  simp only [dualResolvent] at h
  unfold graphResolvent
  rw [h, sub_sub_cancel]

lemma commute_mul_one_add_inv {C : Matrix n n ℝ} (hC : C.PosDef) :
    C * (1 + C)⁻¹ = (1 + C)⁻¹ * C := by
  have hunit := one_add_det_isUnit hC
  have hleft : C * (1 + C)⁻¹ = 1 - (1 + C)⁻¹ :=
    graphResolvent_eq_one_sub_inv hC
  have hright : (1 + C)⁻¹ * C = 1 - (1 + C)⁻¹ := by
    calc (1 + C)⁻¹ * C
        = (1 + C)⁻¹ * ((1 + C) - (1 : Matrix n n ℝ)) := by
            congr 1
            abel
      _ = (1 + C)⁻¹ * (1 + C) - (1 + C)⁻¹ * 1 := mul_sub _ _ _
      _ = 1 - (1 + C)⁻¹ := by rw [nonsing_inv_mul _ hunit, Matrix.mul_one]
  rw [hleft, hright]

/-- `I + C⁻¹ = C⁻¹(I+C)`. -/
theorem one_add_inv_factor {C : Matrix n n ℝ} (hC : C.PosDef) :
    (1 + C⁻¹ : Matrix n n ℝ) = C⁻¹ * (1 + C) := by
  have hunit : IsUnit C.det := (isUnit_iff_isUnit_det _).mp hC.isUnit
  calc (1 : Matrix n n ℝ) + C⁻¹
      = C⁻¹ * C + C⁻¹ := by rw [nonsing_inv_mul C hunit]
    _ = C⁻¹ * (C + 1) := by rw [mul_add, mul_one]
    _ = C⁻¹ * (1 + C) := by rw [add_comm]

/-- **r407/r409 dictionary.**  `C(I+C)⁻¹ = (I + C⁻¹)⁻¹`. -/
theorem graphResolvent_eq_dualResolvent_inv {C : Matrix n n ℝ}
    (hC : C.PosDef) : graphResolvent C = dualResolvent C⁻¹ := by
  haveI : Invertible C := hC.isUnit.invertible
  unfold graphResolvent lEnsemble dualResolvent
  rw [one_add_inv_factor hC, Matrix.mul_inv_rev, inv_inv_of_invertible]
  exact commute_mul_one_add_inv hC

/-- `R ≺ I`: `I − R = (I+C)⁻¹ ≻ 0`. -/
theorem graphResolvent_lt_one {C : Matrix n n ℝ} (hC : C.PosDef) :
    ((1 : Matrix n n ℝ) - graphResolvent C).PosDef := by
  rw [graphResolvent_eq_one_sub_inv hC, sub_sub_cancel]
  exact (one_add_posDef hC).inv

/-! ## Spectral forms -/

lemma conj_add (U : Matrix.unitaryGroup n ℝ) (A B : Matrix n n ℝ) :
    (U : Matrix n n ℝ) * A * star (U : Matrix n n ℝ) +
      (U : Matrix n n ℝ) * B * star (U : Matrix n n ℝ) =
    (U : Matrix n n ℝ) * (A + B) * star (U : Matrix n n ℝ) := by
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_add]
  congr 1
  rw [← Matrix.add_mul]

lemma conj_sub (U : Matrix.unitaryGroup n ℝ) (A B : Matrix n n ℝ) :
    (U : Matrix n n ℝ) * A * star (U : Matrix n n ℝ) -
      (U : Matrix n n ℝ) * B * star (U : Matrix n n ℝ) =
    (U : Matrix n n ℝ) * (A - B) * star (U : Matrix n n ℝ) := by
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_sub]
  congr 1
  rw [← Matrix.sub_mul]

lemma one_add_spectral {C : Matrix n n ℝ} (hC : C.IsHermitian) :
    1 + C =
      (hC.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => 1 + hC.eigenvalues i) *
        star (hC.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.eigenvectorUnitary with hU
  set lam := hC.eigenvalues with hlam
  have hCform : C =
      (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
    simpa [U, lam, conjStarAlgAut_apply, Function.comp_def] using hC.spectral_theorem
  have h1 : (1 : Matrix n n ℝ) =
      (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) := by
    simpa using (conj_unitary_smul_one U 1).symm
  have hadd :
      (1 : Matrix n n ℝ) + diagonal lam = diagonal fun i => 1 + lam i := by
    ext i j
    by_cases hij : i = j <;> simp [diagonal, Matrix.one_apply, hij, add_comm]
  calc (1 : Matrix n n ℝ) + C
      = (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) + C := by
          conv_lhs => rw [h1]
    _ = (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) +
          (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
            rw [hCform]
    _ = (U : Matrix n n ℝ) * (1 + diagonal lam) * star (U : Matrix n n ℝ) :=
          conj_add U 1 (diagonal lam)
    _ = (U : Matrix n n ℝ) * diagonal (fun i => 1 + lam i) *
          star (U : Matrix n n ℝ) := by rw [hadd]

lemma sub_one_spectral {C : Matrix n n ℝ} (hC : C.IsHermitian) :
    C - 1 =
      (hC.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => hC.eigenvalues i - 1) *
        star (hC.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.eigenvectorUnitary with hU
  set lam := hC.eigenvalues with hlam
  have hCform : C =
      (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
    simpa [U, lam, conjStarAlgAut_apply, Function.comp_def] using hC.spectral_theorem
  have h1 : (1 : Matrix n n ℝ) =
      (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) := by
    simpa using (conj_unitary_smul_one U 1).symm
  have hsub : diagonal lam - (1 : Matrix n n ℝ) =
      diagonal fun i => lam i - 1 := by
    simpa using diagonal_sub_smul_one lam 1
  calc C - 1
      = (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) - 1 := by
          rw [hCform]
    _ = (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) -
          (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) := by
            conv_lhs => rw [h1]
    _ = (U : Matrix n n ℝ) * (diagonal lam - 1) * star (U : Matrix n n ℝ) :=
          conj_sub U (diagonal lam) 1
    _ = (U : Matrix n n ℝ) * diagonal (fun i => lam i - 1) *
          star (U : Matrix n n ℝ) := by rw [hsub]

/-- `R = U diag(λ/(1+λ)) U*`. -/
theorem graphResolvent_spectral {C : Matrix n n ℝ} (hC : C.PosDef) :
    graphResolvent C =
      (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => hC.isHermitian.eigenvalues i /
          (1 + hC.isHermitian.eigenvalues i)) *
        star (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  have hlam1 : ∀ i, 0 < 1 + lam i := fun i => add_pos (by norm_num) (hlam i)
  have h1C := one_add_spectral hC.isHermitian
  have hDdet : IsUnit (diagonal fun i => 1 + lam i).det := by
    rw [det_diagonal, IsUnit.prod_univ_iff]
    intro i
    exact (hlam1 i).ne'.isUnit
  have h1Cinv :
      (1 + C)⁻¹ =
        (U : Matrix n n ℝ) * (diagonal fun i => 1 + lam i)⁻¹ *
          star (U : Matrix n n ℝ) := by
    rw [show 1 + C =
          (U : Matrix n n ℝ) * diagonal (fun i => 1 + lam i) *
            star (U : Matrix n n ℝ) by simpa [U, lam] using h1C]
    exact inv_conj_unitary U (diagonal fun i => 1 + lam i) hDdet
  have hDinv := inv_diagonal_pos (n := n) hlam1
  have hCform : C =
      (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
    simpa [U, lam, conjStarAlgAut_apply, Function.comp_def] using
      hC.isHermitian.spectral_theorem
  unfold graphResolvent lEnsemble
  rw [h1Cinv, hDinv, hCform]
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (star (U : Matrix n n ℝ)) (U : Matrix n n ℝ),
    unitary_star_mul_self U, Matrix.one_mul]
  rw [← Matrix.mul_assoc (diagonal lam) (diagonal fun i => (1 + lam i)⁻¹),
    diagonal_mul_diagonal]
  simp [div_eq_mul_inv]

/-- `C⁻¹ = U diag(1/λ) U*`. -/
theorem inv_spectral {C : Matrix n n ℝ} (hC : C.PosDef) :
    C⁻¹ =
      (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => (hC.isHermitian.eigenvalues i)⁻¹) *
        star (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  have hDdet : IsUnit (diagonal lam).det := by
    rw [det_diagonal, IsUnit.prod_univ_iff]
    intro i
    exact (hlam i).ne'.isUnit
  have hCform : C =
      (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := by
    simpa [U, lam, conjStarAlgAut_apply, Function.comp_def] using
      hC.isHermitian.spectral_theorem
  rw [hCform, inv_conj_unitary U (diagonal lam) hDdet, inv_diagonal_pos hlam]

/-- `0 ≺ R`. -/
theorem graphResolvent_posDef {C : Matrix n n ℝ} (hC : C.PosDef) :
    (graphResolvent C).PosDef := by
  classical
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  have hUunit : IsUnit (U : Matrix n n ℝ) := isUnit_coe
  rw [graphResolvent_spectral hC, hUunit.posDef_star_right_conjugate_iff,
    posDef_diagonal_iff]
  intro i
  exact div_pos (hlam i) (add_pos (by norm_num) (hlam i))

lemma one_sub_half_smul :
    (1 : Matrix n n ℝ) - (1 / 2 : ℝ) • 1 = (1 / 2 : ℝ) • 1 := by
  ext i j
  simp [Matrix.one_apply, Matrix.smul_apply]
  split_ifs <;> ring

/-- **Half-shift identity** (the cleanest form).
  `R − ½I = ½ (I+C)⁻¹ (C − I)`. -/
theorem graphResolvent_sub_half_eq {C : Matrix n n ℝ} (hC : C.PosDef) :
    graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ) =
      (1 / 2 : ℝ) • ((1 + C)⁻¹ * (C - 1)) := by
  have hunit := one_add_det_isUnit hC
  have hL :
      graphResolvent C - (1 / 2 : ℝ) • 1 =
        (1 / 2 : ℝ) • 1 - (1 + C)⁻¹ := by
    calc graphResolvent C - (1 / 2 : ℝ) • 1
        = (1 - (1 + C)⁻¹) - (1 / 2 : ℝ) • 1 := by
            rw [graphResolvent_eq_one_sub_inv hC]
      _ = (1 - (1 / 2 : ℝ) • 1) - (1 + C)⁻¹ := by abel
      _ = (1 / 2 : ℝ) • 1 - (1 + C)⁻¹ := by rw [one_sub_half_smul]
  have hR :
      (1 / 2 : ℝ) • ((1 + C)⁻¹ * (C - 1)) =
        (1 / 2 : ℝ) • 1 - (1 + C)⁻¹ := by
    have hC' : C - 1 = (1 + C) - (2 : ℝ) • 1 := by
      ext i j
      simp [two_smul, Matrix.one_apply, Matrix.sub_apply, Matrix.add_apply]
    calc (1 / 2 : ℝ) • ((1 + C)⁻¹ * (C - 1))
        = (1 / 2 : ℝ) • ((1 + C)⁻¹ * ((1 + C) - (2 : ℝ) • 1)) := by
            rw [hC']
      _ = (1 / 2 : ℝ) • (1 - (1 + C)⁻¹ * ((2 : ℝ) • 1)) := by
            rw [mul_sub, nonsing_inv_mul _ hunit]
      _ = (1 / 2 : ℝ) • (1 - (2 : ℝ) • (1 + C)⁻¹) := by
            simp
      _ = (1 / 2 : ℝ) • 1 - ((1 / 2 : ℝ) * 2) • (1 + C)⁻¹ := by
            rw [smul_sub, smul_smul]
      _ = (1 / 2 : ℝ) • 1 - (1 : ℝ) • (1 + C)⁻¹ := by
            congr 2
            norm_num
      _ = (1 / 2 : ℝ) • 1 - (1 + C)⁻¹ := by rw [one_smul]
  rw [hL, hR]

/-! ## Inertia: Sylvester sandwich -/

lemma indNeg_unitary_conj (U : Matrix.unitaryGroup n ℝ) (d : n → ℝ) :
    indNeg ((U : Matrix n n ℝ) * diagonal d * star (U : Matrix n n ℝ)) =
      {i : n | d i < 0}.ncard := by
  classical
  set P := (U : Matrix n n ℝ)
  have hdiag : Pᵀ * (P * diagonal d * star P) * P = diagonal d := by
    rw [transpose_eq_star]
    simp only [Matrix.mul_assoc]
    rw [unitary_star_mul_self U, Matrix.mul_one]
    rw [← Matrix.mul_assoc, unitary_star_mul_self U, Matrix.one_mul]
  have hE : Equivalent
      (P * diagonal d * star P).toQuadraticMap' (weightedSumSquares ℝ d) := by
    have hc := equivalent_toQuadraticMap'_congruence_index
      (P * diagonal d * star P) P (unitary_det_isUnit U)
    rw [hdiag, toQuadraticMap'_diagonal_index] at hc
    exact hc.symm
  rw [indNeg, sigNeg_of_equiv_weightedSumSquares hE]

lemma mobius_frac {t : ℝ} (ht : 0 < t) :
    t / (1 + t) - (1 / 2 : ℝ) = (t - 1) / (2 * (1 + t)) := by
  have hden : 1 + t ≠ 0 := (add_pos (by norm_num : (0 : ℝ) < 1) ht).ne'
  field_simp [hden]
  ring

lemma mobius_sign {t : ℝ} (ht : 0 < t) :
    t / (1 + t) - (1 / 2 : ℝ) < 0 ↔ t - 1 < 0 := by
  have hden : 0 < 2 * (1 + t) :=
    mul_pos (by norm_num) (add_pos (by norm_num) ht)
  rw [mobius_frac ht, div_lt_iff₀ hden, zero_mul]

lemma inv_frac {t : ℝ} (ht : 0 < t) :
    1 - t⁻¹ = (t - 1) / t := by
  field_simp [ht.ne']

lemma inv_sign {t : ℝ} (ht : 0 < t) :
    1 - t⁻¹ < 0 ↔ t - 1 < 0 := by
  rw [inv_frac ht, div_lt_iff₀ ht, zero_mul]

lemma inv_pos_sign {t : ℝ} (ht : 0 < t) :
    0 < 1 - t⁻¹ ↔ 0 < t - 1 := by
  rw [inv_frac ht, div_pos_iff_of_pos_right ht]

lemma inv_nonneg_sign {t : ℝ} (ht : 0 < t) :
    0 ≤ 1 - t⁻¹ ↔ 0 ≤ t - 1 := by
  rw [inv_frac ht, le_div_iff₀ ht, zero_mul]

lemma graphResolvent_sub_half_spectral {C : Matrix n n ℝ} (hC : C.PosDef) :
    graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ) =
      (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => hC.isHermitian.eigenvalues i /
          (1 + hC.isHermitian.eigenvalues i) - 1 / 2) *
        star (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.isHermitian.eigenvectorUnitary with hU
  set lam := hC.isHermitian.eigenvalues with hlam
  have hR : graphResolvent C =
      (U : Matrix n n ℝ) * diagonal (fun i => lam i / (1 + lam i)) *
        star (U : Matrix n n ℝ) := by
    simpa [U, lam] using graphResolvent_spectral hC
  have hcI : (1 / 2 : ℝ) • (1 : Matrix n n ℝ) =
      (U : Matrix n n ℝ) * ((1 / 2 : ℝ) • 1) *
        star (U : Matrix n n ℝ) :=
    (conj_unitary_smul_one U (1 / 2)).symm
  rw [hR, hcI, conj_sub]
  congr 2
  exact diagonal_sub_smul_one (fun i => lam i / (1 + lam i)) (1 / 2)

/-- True Sylvester sandwich: `(I+C)⁻¹` is PD, so
  `In((I+C)⁻¹ (C−I) (I+C)⁻¹) = In(C−I)`. -/
theorem indNeg_one_add_inv_congruence {C : Matrix n n ℝ} (hC : C.PosDef) :
    indNeg ((1 + C)⁻¹ * (C - 1) * (1 + C)⁻¹) = indNeg (C - 1) := by
  have hS := one_add_posDef hC
  have hP : IsUnit (1 + C)⁻¹.det :=
    (isUnit_iff_isUnit_det _).mp hS.inv.isUnit
  have hAt : ((1 + C)⁻¹)ᵀ = (1 + C)⁻¹ := by
    simpa [conjTranspose_eq_transpose_of_trivial] using hS.inv.isHermitian.eq
  simp only [indNeg]
  simpa [hAt] using sigNeg_congruence (C - 1) (1 + C)⁻¹ hP

/-- True Sylvester sandwich for the Möbius side:
  `In(C⁻¹ (C−I) C⁻¹) = In(C−I)`. -/
theorem indNeg_inv_congruence {C : Matrix n n ℝ} (hC : C.PosDef) :
    indNeg (C⁻¹ * (C - 1) * C⁻¹) = indNeg (C - 1) := by
  have hP : IsUnit C⁻¹.det := (isUnit_iff_isUnit_det _).mp hC.inv.isUnit
  have hAt : (C⁻¹)ᵀ = C⁻¹ := by
    simpa [conjTranspose_eq_transpose_of_trivial] using hC.inv.isHermitian.eq
  simp only [indNeg]
  simpa [hAt] using sigNeg_congruence (C - 1) C⁻¹ hP

/-- **(a) Spectral bridge.**  `ind₋(R − ½I) = ind₋(C − I)`.
The commuting sandwich `R − ½I = ½ (I+C)⁻¹ (C − I)` has the same
inertia as `C − I` because `(I+C)⁻¹ ≻ 0`. -/
theorem indNeg_graphResolvent_sub_half {C : Matrix n n ℝ} (hC : C.PosDef) :
    indNeg (graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)) =
      indNeg (C - 1) := by
  classical
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  rw [graphResolvent_sub_half_spectral hC, sub_one_spectral hC.isHermitian]
  rw [indNeg_unitary_conj U, indNeg_unitary_conj U]
  refine congrArg Set.ncard ?_
  ext i
  simp only [Set.mem_setOf_eq]
  exact mobius_sign (hlam i)

lemma one_sub_inv_spectral {C : Matrix n n ℝ} (hC : C.PosDef) :
    (1 : Matrix n n ℝ) - C⁻¹ =
      (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) *
        diagonal (fun i => 1 - (hC.isHermitian.eigenvalues i)⁻¹) *
        star (hC.isHermitian.eigenvectorUnitary : Matrix n n ℝ) := by
  set U := hC.isHermitian.eigenvectorUnitary with hU
  set lam := hC.isHermitian.eigenvalues with hlam
  have h1 : (1 : Matrix n n ℝ) =
      (U : Matrix n n ℝ) * 1 * star (U : Matrix n n ℝ) := by
    simpa using (conj_unitary_smul_one U 1).symm
  have hinv : C⁻¹ =
      (U : Matrix n n ℝ) * diagonal (fun i => (lam i)⁻¹) *
        star (U : Matrix n n ℝ) := by
    simpa [U, lam] using inv_spectral hC
  have hsub :
      (1 : Matrix n n ℝ) - diagonal (fun i => (lam i)⁻¹) =
        diagonal fun i => 1 - (lam i)⁻¹ := by
    ext i j
    by_cases hij : i = j <;> simp [diagonal, Matrix.one_apply, hij]
  rw [h1, hinv, conj_sub, hsub]

/-- **(b) Möbius inertia.**  `ind₋(C − I) = ind₋(I − C⁻¹)`. -/
theorem indNeg_mobius {C : Matrix n n ℝ} (hC : C.PosDef) :
    indNeg (C - 1) = indNeg ((1 : Matrix n n ℝ) - C⁻¹) := by
  classical
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  rw [sub_one_spectral hC.isHermitian, one_sub_inv_spectral hC]
  rw [indNeg_unitary_conj U, indNeg_unitary_conj U]
  refine congrArg Set.ncard ?_
  ext i
  simp only [Set.mem_setOf_eq]
  exact (inv_sign (hlam i)).symm

/-- Möbius, PosDef face: `I − C⁻¹ ≻ 0` iff `C ≻ I`. -/
theorem posDef_one_sub_inv_iff {C : Matrix n n ℝ} (hC : C.PosDef) :
    ((1 : Matrix n n ℝ) - C⁻¹).PosDef ↔ (C - 1).PosDef := by
  classical
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  have hUunit : IsUnit (U : Matrix n n ℝ) := isUnit_coe
  rw [one_sub_inv_spectral hC, sub_one_spectral hC.isHermitian]
  rw [hUunit.posDef_star_right_conjugate_iff,
    hUunit.posDef_star_right_conjugate_iff, posDef_diagonal_iff,
    posDef_diagonal_iff]
  constructor
  · intro h i
    exact (inv_pos_sign (hlam i)).mp (h i)
  · intro h i
    exact (inv_pos_sign (hlam i)).mpr (h i)

/-- Möbius, Loewner face: `I − C⁻¹ ⪰ 0` iff `C ⪰ I`. -/
theorem posSemidef_one_sub_inv_iff {C : Matrix n n ℝ} (hC : C.PosDef) :
    ((1 : Matrix n n ℝ) - C⁻¹).PosSemidef ↔ (C - 1).PosSemidef := by
  classical
  set U := hC.isHermitian.eigenvectorUnitary
  set lam := hC.isHermitian.eigenvalues
  have hlam : ∀ i, 0 < lam i := hC.eigenvalues_pos
  have hUunit : IsUnit (U : Matrix n n ℝ) := isUnit_coe
  rw [one_sub_inv_spectral hC, sub_one_spectral hC.isHermitian]
  rw [hUunit.posSemidef_star_right_conjugate_iff,
    hUunit.posSemidef_star_right_conjugate_iff, posSemidef_diagonal_iff,
    posSemidef_diagonal_iff]
  constructor
  · intro h i
    exact (inv_nonneg_sign (hlam i)).mp (h i)
  · intro h i
    exact (inv_nonneg_sign (hlam i)).mpr (h i)

/-- Zero-defect face of (a)+(b): `R ≻ ½I` iff `C ≻ I`. -/
theorem graphResolvent_gt_half_iff {C : Matrix n n ℝ} (hC : C.PosDef) :
    (graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)).PosDef ↔
      (C - 1).PosDef := by
  have hS : (1 + C⁻¹).PosDef :=
    posDef_one_add_of_posSemidef hC.inv.posSemidef
  rw [graphResolvent_eq_dualResolvent_inv hC]
  rw [← posDef_one_sub_iff_dualResolvent_gt_half hS]
  exact posDef_one_sub_inv_iff hC

/-- Loewner face of (a)+(b) (r430): `R ⪰ ½I` iff `C ⪰ I`. -/
theorem graphResolvent_ge_half_iff {C : Matrix n n ℝ} (hC : C.PosDef) :
    (graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)).PosSemidef ↔
      (C - 1).PosSemidef := by
  have hS : (1 + C⁻¹).PosDef :=
    posDef_one_add_of_posSemidef hC.inv.posSemidef
  rw [graphResolvent_eq_dualResolvent_inv hC]
  rw [← posSemidef_one_sub_iff_dualResolvent_ge_half hS]
  exact posSemidef_one_sub_inv_iff hC

/-! ## Energy split -/

variable {m : Type*} [Fintype m] [DecidableEq m]

lemma gram_quadratic (T : Matrix m n ℝ) (x : n → ℝ) :
    x ⬝ᵥ ((Tᵀ * T) *ᵥ x) = (T *ᵥ x) ⬝ᵥ (T *ᵥ x) := by
  calc x ⬝ᵥ ((Tᵀ * T) *ᵥ x)
      = x ⬝ᵥ (Tᵀ *ᵥ (T *ᵥ x)) := by rw [mulVec_mulVec]
    _ = (x ᵥ* Tᵀ) ⬝ᵥ (T *ᵥ x) := by rw [dotProduct_mulVec]
    _ = (Tᵀᵀ *ᵥ x) ⬝ᵥ (T *ᵥ x) := by rw [vecMul_eq_transpose_mulVec]
    _ = (T *ᵥ x) ⬝ᵥ (T *ᵥ x) := by rw [transpose_transpose]

lemma isHermitian_gram (T : Matrix m n ℝ) : (Tᵀ * T).IsHermitian := by
  simpa [conjTranspose_eq_transpose_of_trivial] using
    isHermitian_conjTranspose_mul_self T

/-- Euclidean operator-norm bound `∀ x, ‖𝔗 x‖ ≤ ‖x‖` as a quadratic
form: equivalent to `I − 𝔗ᵀ𝔗 ⪰ 0`. -/
theorem contractive_iff_gram_le_one (T : Matrix m n ℝ) :
    (∀ x : n → ℝ, (T *ᵥ x) ⬝ᵥ (T *ᵥ x) ≤ x ⬝ᵥ x) ↔
      ((1 : Matrix n n ℝ) - Tᵀ * T).PosSemidef := by
  have hform (x : n → ℝ) :
      x ⬝ᵥ (((1 : Matrix n n ℝ) - Tᵀ * T) *ᵥ x) =
        x ⬝ᵥ x - (T *ᵥ x) ⬝ᵥ (T *ᵥ x) := by
    rw [sub_mulVec, dotProduct_sub, one_mulVec, gram_quadratic]
  constructor
  · intro h
    refine PosSemidef.of_dotProduct_mulVec_nonneg
      (isHermitian_one.sub (isHermitian_gram T)) ?_
    intro x
    have hx : 0 ≤ x ⬝ᵥ x - (T *ᵥ x) ⬝ᵥ (T *ᵥ x) := sub_nonneg.mpr (h x)
    simpa [← hform x] using hx
  · intro h x
    have hx := h.dotProduct_mulVec_nonneg x
    have : 0 ≤ x ⬝ᵥ x - (T *ᵥ x) ⬝ᵥ (T *ᵥ x) := by
      simpa [hform x] using hx
    linarith

/-- **(c) Energy split, contraction.**  For `𝔗ᵀ 𝔗 = C⁻¹`,
  `∀ x, ‖𝔗 x‖ ≤ ‖x‖` iff `C ⪰ I`. -/
theorem energy_split_contractive {T : Matrix m n ℝ} {C : Matrix n n ℝ}
    (hC : C.PosDef) (hT : Tᵀ * T = C⁻¹) :
    (∀ x : n → ℝ, (T *ᵥ x) ⬝ᵥ (T *ᵥ x) ≤ x ⬝ᵥ x) ↔
      (C - 1).PosSemidef := by
  rw [contractive_iff_gram_le_one, hT]
  exact posSemidef_one_sub_inv_iff hC

/-- **(c) Energy split, one excess singular value.**
  `ind₋(I − 𝔗ᵀ𝔗) ≤ 1` iff `ind₋(C − I) ≤ 1`. -/
theorem energy_split_at_most_one {T : Matrix m n ℝ} {C : Matrix n n ℝ}
    (hC : C.PosDef) (hT : Tᵀ * T = C⁻¹) :
    indNeg ((1 : Matrix n n ℝ) - Tᵀ * T) ≤ 1 ↔
      indNeg (C - 1) ≤ 1 := by
  rw [hT, ← indNeg_mobius hC]

/-- P1 in the graph-resolvent coordinate: `ind₋(R − ½I) ≤ 1`
iff `ind₋(C − I) ≤ 1`. -/
theorem p1_coord_graphResolvent {C : Matrix n n ℝ} (hC : C.PosDef) :
    indNeg (graphResolvent C - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)) ≤ 1 ↔
      indNeg (C - 1) ≤ 1 := by
  rw [indNeg_graphResolvent_sub_half hC]

/-! ## Composition with the R† layer -/

/-- **(d) Zero-defect composition** (PROVED).  If `C ≻ I` and the
A5 Schur `q† < 1` holds on the L-ensemble kernel `E = C⁻¹`, then
`R† ≻ ½I`.  This is A3+A5 of `RH/DualResolvent.lean` after the
r407 dictionary `E = C⁻¹`.  The one-defect branch cannot be lifted
at the *same* depth (A7-min contrapose) and is the named remainder
below. -/
theorem augDualResolvent_gt_half_of_C_gt_one
    {C : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hC : C.PosDef) (hCgt : (C - 1).PosDef)
    (hZ : (dualZ C⁻¹ v γ).PosDef)
    (hq : 0 < 1 - qDagger C⁻¹ v γ) :
    (augDualResolvent C⁻¹ v γ
      - (1 / 2 : ℝ) •
        (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosDef := by
  have hE : ((1 : Matrix n n ℝ) - C⁻¹).PosDef :=
    (posDef_one_sub_inv_iff hC).mpr hCgt
  exact (augDualResolvent_gt_half_iff_qDagger hZ hE).mpr hq

/-- **Named remainder** (not a `sorry`).  The dual CD Gram `C` on
the hole set of a window is the inverse of the L-ensemble kernel
`E` of some μ-ONB transcription.  Census-grade in r407
(`R = C(I+C)⁻¹ = (I+E)⁻¹`); not a finite-algebra identity over
`VonMangoldtWindow` (needs the Borodin/CD construction; same class
as `CauchyInterlace` / `P1EqCapInertia`).  Once `E = C⁻¹`, the
identity `graphResolvent C = dualResolvent E` is the theorem
`graphResolvent_eq_dualResolvent_inv`.  The one-defect lift of
`indNeg(C−I) ≤ 1` plus a strictly positive r406 discriminant of
the *cap* border to the r430 mincut
`frequently_selected_augDualResolvent_ge_half` consumes this identification
and the depth gap `N-3` vs cap. -/
def GraphResolventIsLEnsembleInv : Prop :=
  ∀ (w : VonMangoldtWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ),
    RepresentsLEnsemble w n E v γ →
    ∃ C : Matrix (Fin n) (Fin n) ℝ, C.PosDef ∧ E = C⁻¹

end RH
