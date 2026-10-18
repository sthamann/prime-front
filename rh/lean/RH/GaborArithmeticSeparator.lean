/-
RH/GaborArithmeticSeparator.lean -- r590 existential arithmetic
separator, parallel to the scaling-test `∀`-zeros chain.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r600: the live Mathlib interface is the zero-side pair
(`GaborZeroSideSeparatesOffCriticalZeros`,
`gabor_zeroSide_criterion_to_mathlib_rh`).  The older spectral
interface (`GaborSeparatesOffCriticalZeros`,
`gabor_criterion_to_mathlib_rh`) is VACUOUS: its positivity
premise is refuted by `gaborSpectralFormula_refuted`.  Kept for
audit trail.

No asserting `sorry`.  Census unchanged.
-/
import RH.GaborSeparation
import RH.GaborSpectralBridge

namespace RH

/-- Existential arithmetic separator: every nontrivial off-critical
zero is witnessed by some admissible Gabor test with negative
three-channel arithmetic form.  Does not pin the test to
`scalingGaborTest`.  Unasserted.  Not a `sorry`. -/
def GaborArithmeticSeparatesOffCriticalZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s → s.re ≠ 1 / 2 →
    ∃ F : GaborWeilTest, F.admissible ∧ gaborArithmeticFormula F < 0

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted`;
kept for audit trail.  Sorry-free: explicit formula turns an
arithmetic separator into the pole-subtracted spectral separator. -/
theorem gabor_separation_of_arithmetic_separators :
    GaborExplicitFormula →
    GaborArithmeticSeparatesOffCriticalZeros →
    GaborSeparatesOffCriticalZeros := by
  intro hexp harith s hs hoff
  obtain ⟨F, hF, hneg⟩ := harith s hs hoff
  refine ⟨F, hF, ?_⟩
  rwa [← gabor_explicitFormula_to_spectral hF hexp]

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted`;
kept for audit trail. -/
theorem gabor_arithmetic_inputs_to_mathlib_rh
    (hexp : GaborExplicitFormula)
    (hsep : GaborArithmeticSeparatesOffCriticalZeros)
    (hpos : ∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborSpectralFormula F) :
    RiemannHypothesis :=
  gabor_criterion_to_mathlib_rh
    (gabor_separation_of_arithmetic_separators hexp hsep) hpos

/-- Zero-side separator plus EF plus pole sign yields an arithmetic
separator.  The conversion `Z < 0 → Arch−Prime+ĥ(0) < 0` is the
r600 pole-sign lemma, not RH-core. -/
theorem gabor_arithmetic_separator_of_zeroSide
    (hexp : GaborExplicitFormula)
    (h1 : ∀ F : GaborWeilTest, 0 ≤ (gaborHat F 1).re)
    (hsep : GaborZeroSideSeparatesOffCriticalZeros) :
    GaborArithmeticSeparatesOffCriticalZeros := by
  intro s hs hoff
  obtain ⟨F, hF, hneg⟩ := hsep s hs hoff
  refine ⟨F, hF, ?_⟩
  exact gaborArithmeticFormula_neg_of_zeroSide_neg hF hexp (h1 F) hneg

/-- Live Mathlib endpoint on the zero-side.  Parallel of the
vacuous `gabor_arithmetic_inputs_to_mathlib_rh`. -/
theorem gabor_arithmetic_zeroSide_inputs_to_mathlib_rh
    (hsep : GaborZeroSideSeparatesOffCriticalZeros)
    (hpos : ∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborZeroSide F) :
    RiemannHypothesis :=
  gabor_zeroSide_criterion_to_mathlib_rh hsep hpos

/-- Non-circular kernel checkpoint (L2 adjudication r589).

A single *fixed* packet `(a, ω)` scores every sufficiently large
weighted FD window by a uniform margin `δ > 0`.  Distinct from
window-retuned isolation (`GaborWeightedTruncationNegLog`,
BoundLog2) and from the unweighted `GaborTruncationUniformNeg`.
Unasserted.  Not a `sorry`. -/
def GaborFixedPacketCofinalNegAt : Prop :=
  ∃ a omega δ : ℝ, 0 < δ ∧
    ∃ T0 : ℝ, ∀ T : ℝ, T0 ≤ T →
      gaborHonestWeil a omega
        (gaborWeightedTruncationConfig T) gaborCInc ≤ -δ

/-- Named implication, not a theorem: cofinal negativity of one
fixed packet on weighted FD windows does not by itself produce
per-zero arithmetic separators (localization of the packet to an
off-critical zero, and the arithmetic identification, remain).
Unasserted.  Not a `sorry`. -/
def gabor_arithmetic_separator_of_cofinal_neg : Prop :=
  GaborFixedPacketCofinalNegAt → GaborArithmeticSeparatesOffCriticalZeros

/-! ## r600: RH ⇒ zero-side nonnegativity (pure packets) -/

lemma isCriticalStrip_re_eq_half_of_RH
    (hRH : RiemannHypothesis) {s : ℂ}
    (hs : IsCriticalStripZetaZero s) :
    s.re = 1 / 2 := by
  have hnt : ¬∃ n : ℕ, s = -2 * (n + 1) := by
    rintro ⟨n, hn⟩
    have hre : s.re ≤ 0 := by
      have hval : s.re = -2 * ((n : ℝ) + 1) := by
        simp [hn]
      have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg _
      linarith [hval, hn0]
    linarith [hs.2.1]
  exact hRH s hs.1 hnt (isCriticalStripZetaZero_ne_one hs)

lemma gaborHat_eq_onLine {ρ : ℂ} (hre : ρ.re = 1 / 2) :
    ρ = (1 / 2 : ℂ) + ρ.im * Complex.I := by
  apply Complex.ext
  · simp [hre]
  · simp

lemma re_mult_gaborHat_eq (F : GaborWeilTest) (ρ : ℂ) :
    ((riemannZetaMultiplicity ρ : ℂ) * gaborHat F ρ).re =
      (riemannZetaMultiplicity ρ : ℝ) * (gaborHat F ρ).re := by
  rw [Complex.mul_re]
  simp

lemma gaborHat_mult_re_nonneg_of_onLine_aux
    (hline : ∀ (F : GaborWeilTest) (t : ℝ),
      0 ≤ (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re)
    (F : GaborWeilTest) {ρ : ℂ} (hre : ρ.re = 1 / 2) :
    0 ≤ ((riemannZetaMultiplicity ρ : ℂ) * gaborHat F ρ).re := by
  rw [re_mult_gaborHat_eq]
  have hz : 0 ≤ (gaborHat F ρ).re := by
    rw [gaborHat_eq_onLine hre]
    exact hline F ρ.im
  exact mul_nonneg (Nat.cast_nonneg _) hz

lemma gaborHat_mult_re_nonneg_of_onLine
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {ρ : ℂ}
    (hre : ρ.re = 1 / 2) :
    0 ≤ ((riemannZetaMultiplicity ρ : ℂ) * gaborHat F ρ).re := by
  rw [re_mult_gaborHat_eq]
  have hz : 0 ≤ (gaborHat F ρ).re := by
    rw [gaborHat_eq_onLine hre]
    exact gaborHat_criticalLine_nonneg hF ρ.im
  exact mul_nonneg (Nat.cast_nonneg _) hz

/-- Under Mathlib `RiemannHypothesis` every strip zero lies on
`Re = 1/2`, so a pure packet has nonnegative zero-side. -/
theorem rh_implies_gaborZeroSide_nonneg
    (hRH : RiemannHypothesis)
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    0 ≤ gaborZeroSide F := by
  have hsm := gaborMultiplicityWeightedHatSummable F hF
  unfold gaborZeroSide
  rw [Complex.re_tsum hsm]
  exact tsum_nonneg fun ρ =>
    gaborHat_mult_re_nonneg_of_onLine hF
      (isCriticalStrip_re_eq_half_of_RH hRH ρ.property)

/-- Reverse direction for every even quartic, modulo on-line
nonnegativity (proved for the pure family only). -/
theorem rh_implies_gaborZeroSide_nonneg_of_onLine
    (hRH : RiemannHypothesis)
    (hline : ∀ (F : GaborWeilTest) (t : ℝ),
      0 ≤ (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re)
    (F : GaborWeilTest) :
    0 ≤ gaborZeroSide F := by
  have hsm := gaborMultiplicityWeightedHatSummableQuartic_holds F
  unfold gaborZeroSide
  rw [Complex.re_tsum hsm]
  exact tsum_nonneg fun ρ =>
    gaborHat_mult_re_nonneg_of_onLine_aux hline F
      (isCriticalStrip_re_eq_half_of_RH hRH ρ.property)

/-- Scaling tests are pure, so `GaborZeroSideForAllZeros` plus
pure zero-side nonnegativity reach Mathlib RH. -/
theorem gabor_zeroSide_pure_inputs_to_mathlib_rh
    (hineq : GaborZeroSideForAllZeros)
    (hpos : ∀ (a omega : ℝ) (ha : 0 < a),
      0 ≤ gaborZeroSide (pureGaborTest a omega ha)) :
    RiemannHypothesis := by
  intro s hz htrivial hpole
  by_contra hcritical
  have hneg := hineq s ⟨hz, htrivial, hpole⟩ hcritical
  set F := scalingGaborTest s.re s.im hcritical
  have heq : F = pureGaborTest F.a F.omega F.a_pos :=
    eq_pureGaborTest (scalingGaborTest_coeffs s.re s.im hcritical)
  have hposF : 0 ≤ gaborZeroSide F := by
    rw [heq]
    exact hpos F.a F.omega F.a_pos
  exact (not_lt_of_ge hposF) hneg

/-- Fully discharged iff on the live pure family.  Separator
premise is `GaborZeroSideForAllZeros` (scaling packet).

OVERSPECIFIED (r605): prescribed-packet pointwise form; superseded by
the existential separator in `GaborExposedOrbit.lean`. -/
theorem gabor_zeroSide_pure_criterion_iff_rh
    (hsep : GaborZeroSideForAllZeros) :
    (∀ (a omega : ℝ) (ha : 0 < a),
      0 ≤ gaborZeroSide (pureGaborTest a omega ha)) ↔
      RiemannHypothesis :=
  ⟨gabor_zeroSide_pure_inputs_to_mathlib_rh hsep,
   fun hRH _a _omega _ha => rh_implies_gaborZeroSide_nonneg hRH rfl⟩

/-- Conditional iff matching the existential separator.  On-line
nonnegativity is an explicit extra premise: it is a theorem for
`coeffs = ⟨1,0,0⟩` and is not proved for a general even quartic. -/
theorem gabor_zeroSide_criterion_iff_rh
    (hsep : GaborZeroSideSeparatesOffCriticalZeros)
    (hline : ∀ (F : GaborWeilTest) (t : ℝ),
      0 ≤ (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re) :
    (∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborZeroSide F) ↔
      RiemannHypothesis :=
  ⟨gabor_zeroSide_criterion_to_mathlib_rh hsep,
   fun hRH F _hF => rh_implies_gaborZeroSide_nonneg_of_onLine hRH hline F⟩

#print axioms gabor_separation_of_arithmetic_separators
#print axioms gabor_arithmetic_inputs_to_mathlib_rh
#print axioms gabor_arithmetic_separator_of_zeroSide
#print axioms gabor_arithmetic_zeroSide_inputs_to_mathlib_rh
#print axioms rh_implies_gaborZeroSide_nonneg
#print axioms rh_implies_gaborZeroSide_nonneg_of_onLine
#print axioms gabor_zeroSide_pure_inputs_to_mathlib_rh
#print axioms gabor_zeroSide_pure_criterion_iff_rh
#print axioms gabor_zeroSide_criterion_iff_rh

end RH
