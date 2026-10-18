/-
RH/DualResolvent.lean -- THE R362 DUALITY (reviewer priority 2):
L† ⟺ R† ≻ ½I as a kernel-checked finite-matrix identity.

FORMULATION.  Abstract finite linear algebra over ℝ.  The Borodin
OP-construction of R from the dual ensemble is outside the kernel
graph -- the spectral object is the L-ensemble transform

  R  := (I + E)⁻¹
  G† := [[E, v], [vᵀ, γ]]
  Z  := I + G†
  R† := Z⁻¹

(D = I gauge: the probe's sign matrix is a signature conjugation and
does not change the PosDef cone).  Provenance: r356 dual-hole probe,
r362 `augmented_borodin_duality_probe.py`.

PROVED (sorry-free):
  (r356-A / A2) I − E ≻ 0 ⟺ R ≻ ½I, given I+E ≻ 0
  (r430 Loewner) I − E ⪰ 0 ⟺ R ⪰ ½I, given I+E ≻ 0
  (A3)          I − G† ≻ 0 ⟺ R† ≻ ½I, given I+G† ≻ 0
  (r430 A3-PSD) I − G† ⪰ 0 ⟺ R† ⪰ ½I, given I+G† ≻ 0
                (`Rdagger_ge_half_iff_augmented_posSemidef`)
  (A4)          Y-block of R† is the Sherman–Morrison rank-1 update
                (mathlib `invOf_fromBlocks₁₁_eq` specialized)
  (A5)          I − G† ≻ 0 ⟺ q† < 1, given I−E ≻ 0
  (A7-min)      R† ≻ αI ⟹ R ≻ αI
  (r373 bridge) L† ⟺ R† ≻ ½I under the μ-ONB whitening
                `RepresentsLEnsemble`
  (r434 Loewner) PosSemidef congruence both directions
                (`posSemidef_congruence_iff`); the real-window
                dock lives in RH/FrequentlySelected.lean
                (`masterCap_posSemidef_iff_Rdagger_ge_half`)

NAMED, NOT ASSERTED: `CauchyInterlace` (classical A7; mathlib v4.29.1
has no min-max / interlacing lemma).

r373: `RepresentsLEnsemble` is the μ-ONB Gram transcription (not an
opaque marker): `E = Qᵀ ν Q` in a frame with `Qᵀ μ Q = I`,
`v = −Qᵀ u / √B`, `γ = 0`, size `n = cap`.  The bridge
`augmentedSubordination_iff_dualResolvent` is PROVED as finite
algebra (congruence of `A_cap` onto `I − G†`, then A3).  R319: the
Prop is the whitening equations, not the cone-iff itself.

Claim boundary: research documentation.  NO RH CLAIM.
-/
import RH.Augmented
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Data.Matrix.Block
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Data.Real.StarOrdered
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace RH

open Matrix Unitary

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ## Block helpers -/

def borderCol (v : n → ℝ) : Matrix n Unit ℝ := fun i _ => v i
def borderRow (v : n → ℝ) : Matrix Unit n ℝ := fun _ j => v j
def borderCorner (γ : ℝ) : Matrix Unit Unit ℝ := fun _ _ => γ

lemma borderRow_eq_conjTranspose (v : n → ℝ) :
    (borderCol (n := n) v)ᴴ = borderRow v := by
  ext ⟨⟩ j; simp [borderCol, borderRow, Matrix.conjTranspose_apply]

lemma one_fromBlocks :
    (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) =
      fromBlocks (1 : Matrix n n ℝ) 0 0 (1 : Matrix Unit Unit ℝ) := by
  ext (i | ⟨⟩) (j | ⟨⟩) <;> simp [Matrix.one_apply, fromBlocks]

lemma border_sandwich (M : Matrix n n ℝ) (v : n → ℝ) :
    (borderRow v * M * borderCol v) () () = v ⬝ᵥ (M *ᵥ v) := by
  simp [borderRow, borderCol, Matrix.mul_apply, dotProduct, mulVec, Finset.sum_mul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun i _ => ?_
  simp [Finset.mul_sum, mul_left_comm, mul_assoc]

lemma borderCorner_add (a b : ℝ) :
    borderCorner (a + b) = borderCorner a + borderCorner b := by
  ext ⟨⟩ ⟨⟩; simp [borderCorner, Matrix.add_apply]

lemma borderCorner_one : (1 : Matrix Unit Unit ℝ) = borderCorner 1 := by
  ext ⟨⟩ ⟨⟩; simp [borderCorner, Matrix.one_apply]

lemma inv_borderCorner {d : ℝ} (hd : d ≠ 0) :
    (borderCorner d)⁻¹ = borderCorner d⁻¹ := by
  have : IsUnit d := isUnit_iff_ne_zero.mpr hd
  rw [inv_subsingleton]
  ext ⟨⟩ ⟨⟩
  simp [borderCorner, diagonal, Ring.inverse_eq_inv]

/-! ## Unaugmented dual resolvent -/

/-- `R := (I+E)⁻¹`.  Spectral object of the r356 L-ensemble transform. -/
noncomputable def dualResolvent (E : Matrix n n ℝ) : Matrix n n ℝ :=
  (1 + E)⁻¹

/-- `Q := E(I+E)⁻¹`. -/
noncomputable def lEnsemble (E : Matrix n n ℝ) : Matrix n n ℝ :=
  E * (1 + E)⁻¹

theorem dualResolvent_eq_one_sub_lEnsemble (E : Matrix n n ℝ)
    (h : IsUnit (1 + E).det) :
    dualResolvent E = 1 - lEnsemble E := by
  unfold dualResolvent lEnsemble
  have h1E : (1 + E : Matrix n n ℝ) - E = 1 := by
    simp [sub_eq_add_neg, add_assoc, add_neg_cancel]
  calc
    (1 + E)⁻¹ = ((1 + E) - E) * (1 + E)⁻¹ := by rw [h1E, Matrix.one_mul]
    _ = (1 + E) * (1 + E)⁻¹ - E * (1 + E)⁻¹ := sub_mul _ _ _
    _ = 1 - E * (1 + E)⁻¹ := by rw [Matrix.mul_nonsing_inv _ h]

theorem posDef_one_add_of_posSemidef {E : Matrix n n ℝ} (hE : E.PosSemidef) :
    (1 + E).PosDef :=
  Matrix.PosDef.one.add_posSemidef hE

/-- Hermitian form of the spectral theorem over `ℝ`. -/
lemma isHermitian_eq_conj_diagonal {S : Matrix n n ℝ} (hS : S.IsHermitian) :
    S = (hS.eigenvectorUnitary : Matrix n n ℝ) *
      diagonal hS.eigenvalues *
      star (hS.eigenvectorUnitary : Matrix n n ℝ) := by
  simpa [conjStarAlgAut_apply, Function.comp_def] using hS.spectral_theorem

lemma unitary_mul_star_self (U : Matrix.unitaryGroup n ℝ) :
    (U : Matrix n n ℝ) * star (U : Matrix n n ℝ) = 1 :=
  Unitary.coe_mul_star_self U

lemma unitary_star_mul_self (U : Matrix.unitaryGroup n ℝ) :
    star (U : Matrix n n ℝ) * (U : Matrix n n ℝ) = 1 :=
  Unitary.coe_star_mul_self U

/-- Inverse of a unitary conjugation: `(U D U*)⁻¹ = U D⁻¹ U*`. -/
lemma inv_conj_unitary (U : Matrix.unitaryGroup n ℝ) (D : Matrix n n ℝ)
    (hD : IsUnit D.det) :
    ((U : Matrix n n ℝ) * D * star (U : Matrix n n ℝ))⁻¹ =
      (U : Matrix n n ℝ) * D⁻¹ * star (U : Matrix n n ℝ) := by
  apply Matrix.inv_eq_left_inv
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (star (U : Matrix n n ℝ)) (U : Matrix n n ℝ)]
  rw [unitary_star_mul_self U, Matrix.one_mul]
  rw [← Matrix.mul_assoc D⁻¹ D]
  rw [Matrix.nonsing_inv_mul _ hD, Matrix.one_mul]
  exact unitary_mul_star_self U

lemma conj_unitary_smul_one (U : Matrix.unitaryGroup n ℝ) (c : ℝ) :
    (U : Matrix n n ℝ) * (c • (1 : Matrix n n ℝ)) * star (U : Matrix n n ℝ) =
      c • (1 : Matrix n n ℝ) := by
  simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one]
  rw [unitary_mul_star_self U]

lemma inv_diagonal_pos {lam : n → ℝ} (hlam : ∀ i, 0 < lam i) :
    (diagonal lam)⁻¹ = diagonal fun i => (lam i)⁻¹ := by
  apply Matrix.inv_eq_left_inv
  ext i j
  simp only [Matrix.mul_apply, diagonal, Matrix.one_apply]
  by_cases hij : i = j
  · subst hij
    simp [inv_mul_cancel₀ (hlam i).ne']
  · simp [hij]

lemma diagonal_sub_smul_one (lam : n → ℝ) (c : ℝ) :
    diagonal lam - c • (1 : Matrix n n ℝ) = diagonal fun i => lam i - c := by
  ext i j
  by_cases hij : i = j
  · subst hij
    simp [diagonal, Matrix.one_apply, Matrix.smul_apply]
  · simp [diagonal, Matrix.one_apply, Matrix.smul_apply, hij]

/-- **the spectral comparison**: for `S ≻ 0` and `c > 0`,
`S⁻¹ ≻ c I` ⟺ `c⁻¹ I ≻ S`. -/
theorem posDef_nonsingInv_sub_smul_iff {S : Matrix n n ℝ}
    (hS : S.PosDef) {c : ℝ} (hc : 0 < c) :
    (S⁻¹ - c • (1 : Matrix n n ℝ)).PosDef ↔
      (c⁻¹ • (1 : Matrix n n ℝ) - S).PosDef := by
  classical
  set U := hS.isHermitian.eigenvectorUnitary
  set lam := hS.isHermitian.eigenvalues
  have hform := isHermitian_eq_conj_diagonal hS.isHermitian
  have hlam : ∀ i, 0 < lam i := hS.eigenvalues_pos
  have hDdet : IsUnit (diagonal lam).det := by
    rw [det_diagonal, IsUnit.prod_univ_iff]
    intro i
    exact (hlam i).ne'.isUnit
  have hSform : S = (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := hform
  have hSinv :
      S⁻¹ = (U : Matrix n n ℝ) * (diagonal lam)⁻¹ * star (U : Matrix n n ℝ) := by
    rw [hSform, inv_conj_unitary U (diagonal lam) hDdet]
  have hDinv := inv_diagonal_pos (n := n) hlam
  have hUunit : IsUnit (U : Matrix n n ℝ) := isUnit_coe
  have hL :
      S⁻¹ - c • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) *
          (diagonal (fun i => (lam i)⁻¹ - c)) *
          star (U : Matrix n n ℝ) := by
    have hcI : c • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) * (c • 1) * star (U : Matrix n n ℝ) :=
      (conj_unitary_smul_one U c).symm
    rw [hSinv, hDinv, hcI]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_sub, ← Matrix.sub_mul]
    congr 2
    simpa using (diagonal_sub_smul_one (fun i => (lam i)⁻¹) c)
  have hR :
      c⁻¹ • (1 : Matrix n n ℝ) - S =
        (U : Matrix n n ℝ) *
          (diagonal (fun i => c⁻¹ - lam i)) *
          star (U : Matrix n n ℝ) := by
    have hcI : c⁻¹ • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) * (c⁻¹ • 1) * star (U : Matrix n n ℝ) :=
      (conj_unitary_smul_one U c⁻¹).symm
    rw [hSform, hcI]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_sub, ← Matrix.sub_mul]
    congr 2
    ext i j
    by_cases hij : i = j
    · subst hij
      simp [diagonal, Matrix.one_apply, Matrix.smul_apply]
    · simp [diagonal, Matrix.one_apply, Matrix.smul_apply, hij]
  have hLiff : (S⁻¹ - c • (1 : Matrix n n ℝ)).PosDef ↔
      ∀ i, 0 < (lam i)⁻¹ - c := by
    rw [hL, hUunit.posDef_star_right_conjugate_iff, posDef_diagonal_iff]
  have hRiff : (c⁻¹ • (1 : Matrix n n ℝ) - S).PosDef ↔
      ∀ i, 0 < c⁻¹ - lam i := by
    rw [hR, hUunit.posDef_star_right_conjugate_iff, posDef_diagonal_iff]
  rw [hLiff, hRiff]
  constructor
  · intro h i
    exact sub_pos.mpr ((lt_inv_comm₀ hc (hlam i)).mp (sub_pos.mp (h i)))
  · intro h i
    exact sub_pos.mpr ((lt_inv_comm₀ hc (hlam i)).mpr (sub_pos.mp (h i)))

/-- **the spectral comparison, Loewner face** (r430): for `S ≻ 0`
and `c > 0`, `S⁻¹ ⪰ c I` ⟺ `c⁻¹ I ⪰ S`.  Same eigenbasis as
`posDef_nonsingInv_sub_smul_iff`; eigenvalues compared by `≤`. -/
theorem posSemidef_nonsingInv_sub_smul_iff {S : Matrix n n ℝ}
    (hS : S.PosDef) {c : ℝ} (hc : 0 < c) :
    (S⁻¹ - c • (1 : Matrix n n ℝ)).PosSemidef ↔
      (c⁻¹ • (1 : Matrix n n ℝ) - S).PosSemidef := by
  classical
  set U := hS.isHermitian.eigenvectorUnitary
  set lam := hS.isHermitian.eigenvalues
  have hform := isHermitian_eq_conj_diagonal hS.isHermitian
  have hlam : ∀ i, 0 < lam i := hS.eigenvalues_pos
  have hDdet : IsUnit (diagonal lam).det := by
    rw [det_diagonal, IsUnit.prod_univ_iff]
    intro i
    exact (hlam i).ne'.isUnit
  have hSform : S = (U : Matrix n n ℝ) * diagonal lam * star (U : Matrix n n ℝ) := hform
  have hSinv :
      S⁻¹ = (U : Matrix n n ℝ) * (diagonal lam)⁻¹ * star (U : Matrix n n ℝ) := by
    rw [hSform, inv_conj_unitary U (diagonal lam) hDdet]
  have hDinv := inv_diagonal_pos (n := n) hlam
  have hUunit : IsUnit (U : Matrix n n ℝ) := isUnit_coe
  have hL :
      S⁻¹ - c • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) *
          (diagonal (fun i => (lam i)⁻¹ - c)) *
          star (U : Matrix n n ℝ) := by
    have hcI : c • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) * (c • 1) * star (U : Matrix n n ℝ) :=
      (conj_unitary_smul_one U c).symm
    rw [hSinv, hDinv, hcI]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_sub, ← Matrix.sub_mul]
    congr 2
    simpa using (diagonal_sub_smul_one (fun i => (lam i)⁻¹) c)
  have hR :
      c⁻¹ • (1 : Matrix n n ℝ) - S =
        (U : Matrix n n ℝ) *
          (diagonal (fun i => c⁻¹ - lam i)) *
          star (U : Matrix n n ℝ) := by
    have hcI : c⁻¹ • (1 : Matrix n n ℝ) =
        (U : Matrix n n ℝ) * (c⁻¹ • 1) * star (U : Matrix n n ℝ) :=
      (conj_unitary_smul_one U c⁻¹).symm
    rw [hSform, hcI]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_sub, ← Matrix.sub_mul]
    congr 2
    ext i j
    by_cases hij : i = j
    · subst hij
      simp [diagonal, Matrix.one_apply, Matrix.smul_apply]
    · simp [diagonal, Matrix.one_apply, Matrix.smul_apply, hij]
  have hLiff : (S⁻¹ - c • (1 : Matrix n n ℝ)).PosSemidef ↔
      ∀ i, 0 ≤ (lam i)⁻¹ - c := by
    rw [hL, hUunit.posSemidef_star_right_conjugate_iff, posSemidef_diagonal_iff]
  have hRiff : (c⁻¹ • (1 : Matrix n n ℝ) - S).PosSemidef ↔
      ∀ i, 0 ≤ c⁻¹ - lam i := by
    rw [hR, hUunit.posSemidef_star_right_conjugate_iff, posSemidef_diagonal_iff]
  rw [hLiff, hRiff]
  constructor
  · intro h i
    exact sub_nonneg.mpr ((le_inv_comm₀ hc (hlam i)).mp (sub_nonneg.mp (h i)))
  · intro h i
    exact sub_nonneg.mpr ((le_inv_comm₀ hc (hlam i)).mpr (sub_nonneg.mp (h i)))

lemma one_sub_eq_two_sub_one_add (E : Matrix n n ℝ) :
    (1 : Matrix n n ℝ) - E = (2 : ℝ) • 1 - (1 + E) := by
  simp [two_smul, sub_eq_add_neg, add_assoc, add_left_comm, add_comm]

/-- **r356-A / (A2)** (PROVED): `I − E ≻ 0` ⟺ `R ≻ ½I`, given `I+E ≻ 0`. -/
theorem posDef_one_sub_iff_dualResolvent_gt_half {E : Matrix n n ℝ}
    (hS : (1 + E).PosDef) :
    ((1 : Matrix n n ℝ) - E).PosDef ↔
      (dualResolvent E - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)).PosDef := by
  have hc : (0 : ℝ) < 1 / 2 := by norm_num
  have hinv : (1 / 2 : ℝ)⁻¹ = (2 : ℝ) := by norm_num
  have hcmp := posDef_nonsingInv_sub_smul_iff (S := 1 + E) hS hc
  unfold dualResolvent
  rw [hcmp, hinv, ← one_sub_eq_two_sub_one_add]

/-! ## Bordered dual resolvent -/

def borderedGram (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ :=
  fromBlocks E (borderCol v) (borderRow v) (borderCorner γ)

def dualZ (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ :=
  1 + borderedGram E v γ

noncomputable def augDualResolvent (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ :=
  (dualZ E v γ)⁻¹

lemma dualZ_fromBlocks (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    dualZ E v γ =
      fromBlocks (1 + E) (borderCol v) (borderRow v) (borderCorner (1 + γ)) := by
  ext x y
  rcases x with i | ⟨⟩ <;> rcases y with j | ⟨⟩
  · simp [dualZ, borderedGram, fromBlocks, Matrix.one_apply, Matrix.add_apply]
  · simp [dualZ, borderedGram, fromBlocks, Matrix.one_apply, Matrix.add_apply, borderCol]
  · simp [dualZ, borderedGram, fromBlocks, Matrix.one_apply, Matrix.add_apply, borderRow]
  · simp [dualZ, borderedGram, fromBlocks, Matrix.one_apply, Matrix.add_apply,
      borderCorner, add_comm]

lemma dualZ_toBlocks₁₁ (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    (dualZ E v γ).toBlocks₁₁ = 1 + E := by
  rw [dualZ_fromBlocks]; rfl

/-- **(A3)** (PROVED): `I − G† ≻ 0` ⟺ `R† ≻ ½I`, given `Z ≻ 0`. -/
theorem posDef_one_sub_borderedGram_iff_augDualResolvent
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hZ : (dualZ E v γ).PosDef) :
    ((1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) - borderedGram E v γ).PosDef ↔
      (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosDef := by
  have hS' : ((1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) + borderedGram E v γ).PosDef := by
    simpa [dualZ] using hZ
  simpa [dualZ, augDualResolvent] using
    posDef_one_sub_iff_dualResolvent_gt_half (E := borderedGram E v γ) hS'

/-- **r356-A Loewner face** (r430; PROVED): `I − E ⪰ 0` ⟺ `R ⪰ ½I`,
given `I+E ≻ 0`.  Inverse still needs `Z ≻ 0`; the cone on `R−½I`
is semidefinite. -/
theorem posSemidef_one_sub_iff_dualResolvent_ge_half {E : Matrix n n ℝ}
    (hS : (1 + E).PosDef) :
    ((1 : Matrix n n ℝ) - E).PosSemidef ↔
      (dualResolvent E - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)).PosSemidef := by
  have hc : (0 : ℝ) < 1 / 2 := by norm_num
  have hinv : (1 / 2 : ℝ)⁻¹ = (2 : ℝ) := by norm_num
  have hcmp := posSemidef_nonsingInv_sub_smul_iff (S := 1 + E) hS hc
  unfold dualResolvent
  rw [hcmp, hinv, ← one_sub_eq_two_sub_one_add]

/-- **(A3) Loewner face** (r430; PROVED): `I − G† ⪰ 0` ⟺ `R† ⪰ ½I`,
given `Z ≻ 0`.  Elementwise extraction needs this cone, not the
strict window margin.  NO RH CLAIM. -/
theorem Rdagger_ge_half_iff_augmented_posSemidef
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hZ : (dualZ E v γ).PosDef) :
    ((1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) - borderedGram E v γ).PosSemidef ↔
      (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosSemidef := by
  have hS' : ((1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) + borderedGram E v γ).PosDef := by
    simpa [dualZ] using hZ
  simpa [dualZ, augDualResolvent] using
    posSemidef_one_sub_iff_dualResolvent_ge_half (E := borderedGram E v γ) hS'

noncomputable def shermanDenom (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) : ℝ :=
  1 + γ - v ⬝ᵥ (dualResolvent E *ᵥ v)

noncomputable def qDagger (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) : ℝ :=
  γ + v ⬝ᵥ ((1 - E)⁻¹ *ᵥ v)

lemma one_sub_borderedGram_fromBlocks (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) - borderedGram E v γ =
      fromBlocks ((1 : Matrix n n ℝ) - E) (borderCol (fun i => -v i))
        (borderRow (fun i => -v i)) (borderCorner (1 - γ)) := by
  ext x y
  rcases x with i | ⟨⟩ <;> rcases y with j | ⟨⟩
  · simp [borderedGram, fromBlocks, Matrix.one_apply, borderCol]
  · simp [borderedGram, fromBlocks, Matrix.one_apply, borderCol]
  · simp [borderedGram, fromBlocks, Matrix.one_apply, borderRow]
  · simp [borderedGram, fromBlocks, Matrix.one_apply, borderCorner]

lemma schur_one_sub_eq_qDagger {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ} :
    (borderCorner (1 - γ)
      - borderRow (fun i => -v i) * ((1 : Matrix n n ℝ) - E)⁻¹ *
        borderCol (fun i => -v i)) () () =
      1 - qDagger E v γ := by
  have h := border_sandwich ((1 : Matrix n n ℝ) - E)⁻¹ (fun i => -v i)
  have hv : (fun i => -v i) ⬝ᵥ (((1 : Matrix n n ℝ) - E)⁻¹ *ᵥ fun i => -v i) =
      v ⬝ᵥ (((1 : Matrix n n ℝ) - E)⁻¹ *ᵥ v) := by
    simp [dotProduct, mulVec]
  simp [borderCorner, h, hv, qDagger]
  ring

/-- **(A5)** (PROVED): given `I−E ≻ 0`, the bordered cone is the
terminal Schur `q† < 1`. -/
theorem posDef_one_sub_borderedGram_iff_qDagger
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hE : ((1 : Matrix n n ℝ) - E).PosDef) :
    ((1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ) - borderedGram E v γ).PosDef ↔
      0 < 1 - qDagger E v γ := by
  classical
  rw [one_sub_borderedGram_fromBlocks]
  set A := (1 : Matrix n n ℝ) - E
  set vn : n → ℝ := fun i => -v i
  haveI : Invertible A :=
    A.invertibleOfIsUnitDet (isUnit_iff_ne_zero.mpr hE.det_pos.ne')
  have hdet_eq :
      (fromBlocks A (borderCol vn) (borderRow vn) (borderCorner (1 - γ))).det =
        A.det * (borderCorner (1 - γ) - borderRow vn * ⅟A * borderCol vn).det :=
    det_fromBlocks₁₁ _ _ _ _
  have hschur :
      (borderCorner (1 - γ) - borderRow vn * A⁻¹ * borderCol vn) () () =
        1 - qDagger E v γ := by
    simpa [vn, A] using (schur_one_sub_eq_qDagger (E := E) (v := v) (γ := γ))
  have hdet1x1 :
      (borderCorner (1 - γ) - borderRow vn * A⁻¹ * borderCol vn).det =
        (borderCorner (1 - γ) - borderRow vn * A⁻¹ * borderCol vn) () () :=
    Matrix.det_unique _
  constructor
  · intro hG
    have hdet := hG.det_pos
    rw [hdet_eq, invOf_eq_nonsing_inv, hdet1x1, hschur] at hdet
    rcases mul_pos_iff.mp hdet with ⟨_, hs⟩ | ⟨hneg, _⟩
    · exact hs
    · exact absurd hE.det_pos (not_lt.mpr hneg.le)
  · intro hq
    have hdet :
        0 < (fromBlocks A (borderCol vn) (borderRow vn)
          (borderCorner (1 - γ))).det := by
      rw [hdet_eq, invOf_eq_nonsing_inv, hdet1x1, hschur]
      exact mul_pos hE.det_pos hq
    exact posDef_fromBlocks_border (v := vn) (d := 1 - γ) hE hdet

/-- **(A5)+(A3)** (PROVED). -/
theorem augDualResolvent_gt_half_iff_qDagger
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hZ : (dualZ E v γ).PosDef)
    (hE : ((1 : Matrix n n ℝ) - E).PosDef) :
    (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosDef ↔
      0 < 1 - qDagger E v γ := by
  rw [← posDef_one_sub_borderedGram_iff_augDualResolvent hZ]
  exact posDef_one_sub_borderedGram_iff_qDagger hE

lemma dualZ_submatrix_inl (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    (dualZ E v γ).submatrix Sum.inl Sum.inl = 1 + E := by
  rw [dualZ_fromBlocks]
  ext i j
  simp [Matrix.submatrix, fromBlocks]

/-- **(A7-min)** (PROVED): `R† ≻ αI` implies `R ≻ αI`. -/
theorem augDualResolvent_gt_smul_implies_dualResolvent
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ} {α : ℝ}
    (hZ : (dualZ E v γ).PosDef) (hα : 0 < α)
    (hRdag : (augDualResolvent E v γ
        - α • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosDef) :
    (dualResolvent E - α • (1 : Matrix n n ℝ)).PosDef := by
  have hinj : Function.Injective (Sum.inl : n → n ⊕ Unit) := Sum.inl_injective
  have hS : (1 + E).PosDef := by
    have hsub := posDef_submatrix_of_injective hZ hinj
    rwa [dualZ_submatrix_inl] at hsub
  have hZupper : (α⁻¹ • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)
      - dualZ E v γ).PosDef := by
    simpa [augDualResolvent] using
      (posDef_nonsingInv_sub_smul_iff hZ hα).mp hRdag
  have hRinvUpper : (α⁻¹ • (1 : Matrix n n ℝ) - (1 + E)).PosDef := by
    have hsub := posDef_submatrix_of_injective hZupper hinj
    have hblk : (α⁻¹ • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)
        - dualZ E v γ).submatrix Sum.inl Sum.inl
        = α⁻¹ • (1 : Matrix n n ℝ) - (1 + E) := by
      rw [dualZ_fromBlocks]
      ext i j
      simp [Matrix.submatrix, fromBlocks, Matrix.one_apply, Matrix.smul_apply]
    rwa [hblk] at hsub
  exact (posDef_nonsingInv_sub_smul_iff hS hα).mpr hRinvUpper

theorem augDualResolvent_gt_half_implies_dualResolvent_gt_half
    {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hZ : (dualZ E v γ).PosDef)
    (hRdag : (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (n ⊕ Unit) (n ⊕ Unit) ℝ)).PosDef) :
    (dualResolvent E - (1 / 2 : ℝ) • (1 : Matrix n n ℝ)).PosDef :=
  augDualResolvent_gt_smul_implies_dualResolvent hZ (by norm_num) hRdag

lemma schur_dualZ_eq_shermanDenom (E : Matrix n n ℝ) (v : n → ℝ) (γ : ℝ) :
    borderCorner (1 + γ) - borderRow v * (1 + E)⁻¹ * borderCol v =
      borderCorner (shermanDenom E v γ) := by
  ext ⟨⟩ ⟨⟩
  simp [borderCorner, shermanDenom, dualResolvent, border_sandwich]

/-- **(A4)** (PROVED): block inverse of `Z`.  The Y-block is the
Sherman–Morrison rank-1 update of `R`. -/
theorem augDualResolvent_fromBlocks {E : Matrix n n ℝ} {v : n → ℝ} {γ : ℝ}
    (hS : (1 + E).PosDef) (hden : shermanDenom E v γ ≠ 0) :
    augDualResolvent E v γ =
      fromBlocks
        (dualResolvent E + dualResolvent E * borderCol v *
          borderCorner (shermanDenom E v γ)⁻¹ * borderRow v * dualResolvent E)
        (-(dualResolvent E * borderCol v *
          borderCorner (shermanDenom E v γ)⁻¹))
        (-(borderCorner (shermanDenom E v γ)⁻¹ * borderRow v *
          dualResolvent E))
        (borderCorner (shermanDenom E v γ)⁻¹) := by
  classical
  haveI : Invertible (1 + E) :=
    (1 + E).invertibleOfIsUnitDet (isUnit_iff_ne_zero.mpr hS.det_pos.ne')
  have hschur :
      borderCorner (1 + γ) - borderRow v * ⅟(1 + E) * borderCol v =
        borderCorner (shermanDenom E v γ) := by
    rw [invOf_eq_nonsing_inv]
    exact schur_dualZ_eq_shermanDenom E v γ
  haveI : Invertible
      (borderCorner (1 + γ) - borderRow v * ⅟(1 + E) * borderCol v) := by
    rw [hschur]
    refine (borderCorner (shermanDenom E v γ)).invertibleOfIsUnitDet ?_
    simpa [borderCorner, Matrix.det_unique] using isUnit_iff_ne_zero.mpr hden
  haveI := fromBlocks₁₁Invertible (1 + E) (borderCol v) (borderRow v)
    (borderCorner (1 + γ))
  unfold augDualResolvent
  rw [dualZ_fromBlocks, ← invOf_eq_nonsing_inv, invOf_fromBlocks₁₁_eq]
  simp only [invOf_eq_nonsing_inv, dualResolvent]
  rw [schur_dualZ_eq_shermanDenom, inv_borderCorner hden]

/-! ## Cauchy interlacing -- named classical, never asserted -/

/-- **Cauchy interlacing** (classical, A7).  mathlib v4.29.1 has the
spectral theorem and `eigenvalues₀_antitone` but no min-max principle
and no interlacing lemma.  Named Prop, never a `sorry`, never silently
consumed.  The cone consequence is `augDualResolvent_gt_smul_implies_
dualResolvent`, proved above. -/
def CauchyInterlace : Prop :=
  ∀ (p : ℕ) (A : Matrix (Fin (p + 1)) (Fin (p + 1)) ℝ)
    (hA : A.IsHermitian) (k : Fin p),
    let hP := hA.submatrix (Fin.castSucc : Fin p → Fin (p + 1))
    hA.eigenvalues₀ (Fin.cast (Fintype.card_fin (p + 1)).symm k.castSucc) ≥
      hP.eigenvalues₀ (Fin.cast (Fintype.card_fin p).symm k) ∧
    hP.eigenvalues₀ (Fin.cast (Fintype.card_fin p).symm k) ≥
      hA.eigenvalues₀ (Fin.cast (Fintype.card_fin (p + 1)).symm k.succ)

/-! ## Congruence invariance of PosDef (both directions) -/

lemma posDef_congruence_iff (S P : Matrix n n ℝ) (hP : IsUnit P.det) :
    S.PosDef ↔ (Pᵀ * S * P).PosDef := by
  have hinj : Function.Injective P.mulVec :=
    P.mulVec_injective_iff_isUnit.mpr ((isUnit_iff_isUnit_det P).mpr hP)
  constructor
  · intro hS
    have hpd := hS.conjTranspose_mul_mul_same hinj
    rwa [conjTranspose_eq_transpose_of_trivial] at hpd
  · intro hPAP
    haveI : Invertible P := P.invertibleOfIsUnitDet hP
    haveI : Invertible P⁻¹ := Invertible.copy (invertibleInvOf (a := P)) P⁻¹
      (by rw [invOf_eq_nonsing_inv])
    have hinj' : Function.Injective P⁻¹.mulVec :=
      P⁻¹.mulVec_injective_iff_isUnit.mpr
        ((isUnit_iff_isUnit_det _).mpr (isUnit_det_of_invertible P⁻¹))
    have hPP : P * P⁻¹ = 1 := Matrix.mul_nonsing_inv P hP
    have hrew : (P⁻¹)ᵀ * (Pᵀ * S * P) * P⁻¹ = S := by
      calc (P⁻¹)ᵀ * (Pᵀ * S * P) * P⁻¹
          = ((P⁻¹)ᵀ * Pᵀ) * S * (P * P⁻¹) := by simp [mul_assoc]
        _ = (P * P⁻¹)ᵀ * S * (P * P⁻¹) := by rw [transpose_mul]
        _ = (1 : Matrix n n ℝ)ᵀ * S * 1 := by rw [hPP]
        _ = S := by simp
    rw [← hrew]
    have hpd := hPAP.conjTranspose_mul_mul_same hinj'
    rwa [conjTranspose_eq_transpose_of_trivial] at hpd

/-- Congruence invariance of `PosSemidef` (both directions).
Injectivity is not required for the forward map; invertibility
of `P` gives the converse.  r434: the real-window Loewner face. -/
lemma posSemidef_congruence_iff (S P : Matrix n n ℝ) (hP : IsUnit P.det) :
    S.PosSemidef ↔ (Pᵀ * S * P).PosSemidef := by
  constructor
  · intro hS
    have hpd := hS.conjTranspose_mul_mul_same P
    rwa [conjTranspose_eq_transpose_of_trivial] at hpd
  · intro hPAP
    haveI : Invertible P := P.invertibleOfIsUnitDet hP
    haveI : Invertible P⁻¹ := Invertible.copy (invertibleInvOf (a := P)) P⁻¹
      (by rw [invOf_eq_nonsing_inv])
    have hPP : P * P⁻¹ = 1 := Matrix.mul_nonsing_inv P hP
    have hrew : (P⁻¹)ᵀ * (Pᵀ * S * P) * P⁻¹ = S := by
      calc (P⁻¹)ᵀ * (Pᵀ * S * P) * P⁻¹
          = ((P⁻¹)ᵀ * Pᵀ) * S * (P * P⁻¹) := by simp [mul_assoc]
        _ = (P * P⁻¹)ᵀ * S * (P * P⁻¹) := by rw [transpose_mul]
        _ = (1 : Matrix n n ℝ)ᵀ * S * 1 := by rw [hPP]
        _ = S := by simp
    rw [← hrew]
    have hpd := hPAP.conjTranspose_mul_mul_same P⁻¹
    rwa [conjTranspose_eq_transpose_of_trivial] at hpd

/-! ## The window bridge -- μ-ONB Gram transcription (r373, PROVED) -/

/-- `(E, v, γ)` is the node-side L-ensemble / CD transcription of the
window `w` in a μ-orthonormal monomial frame of size `n = cap`
(r356 `dual_rung` + r362 `aug_rung` + r373 transcription round).

R319: this is the whitening *equations*, not the cone-iff.  `Q` is a
μ-ONB change of basis (`Qᵀ (combHankel n) Q = I`); `E` is the ν-Gram
in that frame; the border is D=I gauged by `1/√B`; `γ = 0`. -/
def RepresentsLEnsemble (w : VonMangoldtWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ) : Prop :=
  n = w.cap ∧
    0 < ((w.B : ℚ) : ℝ) ∧
    ∃ Q : Matrix (Fin n) (Fin n) ℝ, IsUnit Q.det ∧
      Qᵀ * w.combHankel n * Q = 1 ∧
      E = Qᵀ * w.archHankel n * Q ∧
      v = -((1 / Real.sqrt ((w.B : ℚ) : ℝ)) • (Qᵀ *ᵥ w.borderVec n)) ∧
      γ = 0

lemma transpose_borderCorner (γ : ℝ) :
    (borderCorner γ)ᵀ = borderCorner γ := by
  ext ⟨⟩ ⟨⟩; rfl

lemma A_eq_bordered (w : VonMangoldtWindow) (p : ℕ) :
    w.A p = fromBlocks (w.hankel p)
      (borderCol (n := Fin p) (w.borderVec p))
      (borderRow (n := Fin p) (w.borderVec p))
      (borderCorner ((w.B : ℚ) : ℝ)) :=
  rfl

lemma mul_borderCol {p : ℕ} (M : Matrix (Fin p) (Fin p) ℝ) (x : Fin p → ℝ) :
    M * borderCol (n := Fin p) x = borderCol (n := Fin p) (M *ᵥ x) := by
  ext i ⟨⟩
  simp [borderCol, mulVec, Matrix.mul_apply, dotProduct]

lemma borderCol_mul_corner {p : ℕ} (x : Fin p → ℝ) (σ : ℝ) :
    borderCol (n := Fin p) x * borderCorner σ =
      borderCol (n := Fin p) (σ • x) := by
  ext i ⟨⟩
  simp [borderCol, borderCorner, Matrix.mul_apply, smul_eq_mul, mul_comm]

lemma muWhiteningBlock_transpose {p : ℕ}
    (Q : Matrix (Fin p) (Fin p) ℝ) (σ : ℝ) :
    (fromBlocks Q (0 : Matrix (Fin p) Unit ℝ) (0 : Matrix Unit (Fin p) ℝ)
      (borderCorner σ))ᵀ =
      fromBlocks Qᵀ (0 : Matrix (Fin p) Unit ℝ) (0 : Matrix Unit (Fin p) ℝ)
        (borderCorner σ) := by
  rw [fromBlocks_transpose, transpose_zero, transpose_zero,
    transpose_borderCorner]

lemma muWhiteningBlock_det {p : ℕ}
    (Q : Matrix (Fin p) (Fin p) ℝ) (σ : ℝ) :
    (fromBlocks Q (0 : Matrix (Fin p) Unit ℝ) (0 : Matrix Unit (Fin p) ℝ)
      (borderCorner σ)).det = Q.det * σ := by
  rw [det_fromBlocks_zero₂₁]
  simp [borderCorner, Matrix.det_unique]

/-- The μ-ONB block `S = diag(Q, σ)` conjugates `A_n` onto `I − G†`. -/
lemma muWhitening_congruence {p : ℕ}
    (w : VonMangoldtWindow) (Q : Matrix (Fin p) (Fin p) ℝ) (σ : ℝ)
    (hQ : Qᵀ * w.combHankel p * Q = 1)
    (hσB : σ * σ * ((w.B : ℚ) : ℝ) = 1) :
    let E := Qᵀ * w.archHankel p * Q
    let vv : Fin p → ℝ := -(σ • (Qᵀ *ᵥ w.borderVec p))
    let S := fromBlocks Q (0 : Matrix (Fin p) Unit ℝ)
      (0 : Matrix Unit (Fin p) ℝ) (borderCorner σ)
    Sᵀ * w.A p * S =
      (1 : Matrix (Fin p ⊕ Unit) (Fin p ⊕ Unit) ℝ) -
        borderedGram (n := Fin p) E vv 0 := by
  intro E vv S
  have hH : Qᵀ * w.hankel p * Q = (1 : Matrix (Fin p) (Fin p) ℝ) - E := by
    simp only [E]
    rw [w.hankel_eq_comb_sub_arch, Matrix.mul_sub, Matrix.sub_mul, hQ]
  have hcol :
      Qᵀ * borderCol (n := Fin p) (w.borderVec p) * borderCorner σ =
        borderCol (n := Fin p) (-vv) := by
    rw [mul_borderCol, borderCol_mul_corner]
    simp [vv]
  have hrow :
      borderCorner σ * borderRow (n := Fin p) (w.borderVec p) * Q =
        borderRow (n := Fin p) (-vv) := by
    ext ⟨⟩ j
    simp [borderRow, borderCorner, vv, Matrix.mul_apply, mulVec, smul_eq_mul,
      dotProduct, mul_left_comm, mul_comm, Finset.mul_sum]
  have hcorner :
      borderCorner σ * borderCorner ((w.B : ℚ) : ℝ) * borderCorner σ =
        (1 : Matrix Unit Unit ℝ) := by
    ext ⟨⟩ ⟨⟩
    simp [borderCorner, Matrix.mul_apply, Matrix.one_apply]
    linarith
  have hSTAS :
      Sᵀ * w.A p * S =
        fromBlocks (Qᵀ * w.hankel p * Q)
          (Qᵀ * borderCol (n := Fin p) (w.borderVec p) * borderCorner σ)
          (borderCorner σ * borderRow (n := Fin p) (w.borderVec p) * Q)
          (borderCorner σ * borderCorner ((w.B : ℚ) : ℝ) * borderCorner σ) := by
    rw [muWhiteningBlock_transpose, A_eq_bordered]
    simp only [S]
    rw [fromBlocks_multiply]
    simp [fromBlocks_multiply]
  have h1 : (1 : Matrix Unit Unit ℝ) = borderCorner (1 - (0 : ℝ)) := by
    ext ⟨⟩ ⟨⟩
    simp [borderCorner, Matrix.one_apply]
  have hnegv :
      borderCol (n := Fin p) (-vv) = borderCol (n := Fin p) (fun i => -vv i) ∧
      borderRow (n := Fin p) (-vv) = borderRow (n := Fin p) (fun i => -vv i) := by
    constructor <;> (ext x y; simp [borderCol, borderRow, Pi.neg_apply])
  rw [hSTAS, hH, hcol, hrow, hcorner, one_sub_borderedGram_fromBlocks, h1,
    hnegv.1, hnegv.2]

lemma augmentedSubordination_iff_A_cap (w : VonMangoldtWindow) :
    AugmentedSubordination w ↔ (w.A w.cap).PosDef := by
  rw [augmentedSubordination_iff_masterCap]
  constructor
  · intro h; exact h w.cap le_rfl
  · intro hAcap p hp
    rw [A_eq_submatrix_A_cap w hp]
    exact posDef_submatrix_of_injective hAcap
      ((Fin.castLE_injective hp).sumMap Function.injective_id)

/-- **THE r362/r373 BRIDGE** (PROVED): on a window whose node Gram is
the transcribed `(E, v, γ)`, L† is the dual-resolvent cone `R† ≻ ½I`.

The finite-algebra identity `I − G† ≻ 0 ↔ R† ≻ ½I` is
`posDef_one_sub_borderedGram_iff_augDualResolvent` (PROVED).  L† ↔
`A_cap ≻ 0` is `augmentedSubordination_iff_masterCap` (PROVED).  The
identification of the window's L† quadratic form with `I − G†` in the
μ-orthonormal frame is the `RepresentsLEnsemble` whitening (the
evaluation-Gram / Vandermonde factorization is
`combHankel_eq_vand` / `archHankel_eq_vand` in `RH/Window.lean`).
NO RH CLAIM. -/
theorem augmentedSubordination_iff_dualResolvent
    (w : VonMangoldtWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ)
    (hrep : RepresentsLEnsemble w n E v γ)
    (hZ : (dualZ E v γ).PosDef) :
    AugmentedSubordination w ↔
      (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (Fin n ⊕ Unit) (Fin n ⊕ Unit) ℝ)).PosDef := by
  rcases hrep with ⟨hncap, hB, Q, hQunit, hQμ, hE, hv, hγ⟩
  subst hncap
  subst hγ
  subst hE
  subst hv
  set σ : ℝ := 1 / Real.sqrt ((w.B : ℚ) : ℝ)
  have hσpos : 0 < σ := by
    unfold σ
    positivity
  have hσB : σ * σ * ((w.B : ℚ) : ℝ) = 1 := by
    unfold σ
    have hne : Real.sqrt ((w.B : ℚ) : ℝ) ≠ 0 :=
      (Real.sqrt_pos.mpr hB).ne'
    field_simp [hne]
    exact (Real.sq_sqrt hB.le).symm
  set S := fromBlocks Q (0 : Matrix (Fin w.cap) Unit ℝ)
    (0 : Matrix Unit (Fin w.cap) ℝ) (borderCorner σ)
  have hcong := muWhitening_congruence (p := w.cap) w Q σ hQμ hσB
  have hSunit : IsUnit S.det := by
    rw [muWhiteningBlock_det]
    exact hQunit.mul (isUnit_iff_ne_zero.mpr hσpos.ne')
  have hAiff :
      (w.A w.cap).PosDef ↔
        ((1 : Matrix (Fin w.cap ⊕ Unit) (Fin w.cap ⊕ Unit) ℝ) -
          borderedGram (n := Fin w.cap) (Qᵀ * w.archHankel w.cap * Q)
            (-(σ • (Qᵀ *ᵥ w.borderVec w.cap))) 0).PosDef := by
    rw [posDef_congruence_iff (n := Fin w.cap ⊕ Unit) (w.A w.cap) S hSunit]
    rw [hcong]
  rw [augmentedSubordination_iff_A_cap, hAiff,
    posDef_one_sub_borderedGram_iff_augDualResolvent (n := Fin w.cap) hZ]

end RH
