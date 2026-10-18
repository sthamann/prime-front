/-
RH/GaborVertical.lean -- r564 vertical T→∞ identification for the
pure Gabor class.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not prove RH and does
not assert `GaborExplicitFormula`.  It proves the Gabor analogue of
the compact-class right-edge inversion (r532) and decomposes the
left edge / contour assembly into named remainders.  The monolithic
`gabor_vertical_arithmetic_remainder` sorry is replaced by a
sorry-free implication from those bricks.

`GaborVerticalArithmeticRemainder` is proved (r581)
(`gabor_vertical_arithmetic_remainder`, via
`gaborArchDigammaIdentification_holds`).  The remaining EF brick
for non-pure even quartics is `GaborHatQuarticExplicitRemainder`.
The numerical dictionary
`ψ(1/4) = −γ_EM − 3·log 2 − π/2` is recorded in the docstring
and is not a Mathlib theorem.  This file has no asserting `sorry`.
-/
import RH.GaborContourResidue
import RH.GaborHorizontalEdges
import Mathlib.Analysis.Fourier.FourierTransform
import Mathlib.Analysis.Fourier.Inversion
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace RH

open Complex Filter Function MeasureTheory
open scoped FourierTransform Topology RealInnerProductSpace LSeries.notation

/-! ## Closed-form packet -/

theorem pureGaborAutocorrelation_even (a omega u : ℝ) :
    pureGaborAutocorrelation a omega (-u) =
      pureGaborAutocorrelation a omega u := by
  unfold pureGaborAutocorrelation
  simp [mul_neg, Real.cos_neg]

theorem norm_pureGaborAutocorrelation_le
    (a omega u : ℝ) (ha : 0 < a) :
    |pureGaborAutocorrelation a omega u| ≤
      Real.sqrt (Real.pi / (2 * a)) / 2 *
        Real.exp (-a * u ^ 2 / 2) *
        (1 + Real.exp (-omega ^ 2 / (2 * a))) := by
  unfold pureGaborAutocorrelation
  have hpre : 0 ≤ Real.sqrt (Real.pi / (2 * a)) / 2 := by positivity
  have hexp : 0 ≤ Real.exp (-a * u ^ 2 / 2) := (Real.exp_pos _).le
  rw [abs_mul, abs_mul, abs_of_nonneg hpre, abs_of_nonneg hexp]
  refine mul_le_mul_of_nonneg_left ?_ (mul_nonneg hpre hexp)
  exact (abs_add_le _ _).trans
    (add_le_add (Real.abs_cos_le_one _)
      (le_of_eq (abs_of_nonneg (Real.exp_pos _).le)))

/-- The defining autocorrelation integral equals the closed form.
Classical Gaussian calculation (complete the square + product-to-sum).
Unasserted: the right-vertical inversion lands on the closed form,
which is already the unique L¹ function whose Weil-shifted transform
is `gaborHat` (r543).  Not a `sorry`. -/
def GaborAutocorrelationClosedForm : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    ∀ u : ℝ, gaborAutocorrelation F u =
      pureGaborAutocorrelation F.a F.omega u

/-! ## Weil-shifted Fourier slice -/

/-- Slice `u ↦ g_closed(u) e^{(σ−1/2)u}`. -/
noncomputable def gaborHatSlice (F : GaborWeilTest) (σ : ℝ) : ℝ → ℂ :=
  fun u => (pureGaborAutocorrelation F.a F.omega u : ℂ) *
    Complex.exp (((σ : ℂ) - (1 / 2 : ℂ)) * u)

theorem continuous_gaborHatSlice (F : GaborWeilTest) (σ : ℝ) :
    Continuous (gaborHatSlice F σ) := by
  unfold gaborHatSlice pureGaborAutocorrelation
  fun_prop

theorem abs_mul_le_sq_add {C a u : ℝ} (ha : 0 < a) :
    |C| * |u| ≤ C ^ 2 / a + a * u ^ 2 / 4 := by
  have h : 0 ≤ (|C| - a * |u| / 2) ^ 2 := sq_nonneg _
  have hexp : (|C| - a * |u| / 2) ^ 2 =
      C ^ 2 + a ^ 2 * u ^ 2 / 4 - |C| * a * |u| := by
    ring_nf
    simp [sq_abs]
    ring
  have : |C| * a * |u| ≤ C ^ 2 + a ^ 2 * u ^ 2 / 4 := by
    linarith [h, hexp]
  have := div_le_div_of_nonneg_right this ha.le
  convert this using 1 <;> field_simp [ha.ne'] <;> ring

theorem integrable_gaborHatSlice (F : GaborWeilTest) (σ : ℝ) :
    Integrable (gaborHatSlice F σ) := by
  have ha : 0 < F.a := F.a_pos
  set z : ℂ := ((σ : ℂ) - (1 / 2 : ℂ))
  have hp := integrable_cexp_neg_half_mul_sq_add F.a ha (z + Complex.I * F.omega)
  have hm := integrable_cexp_neg_half_mul_sq_add F.a ha (z - Complex.I * F.omega)
  have h0 := integrable_cexp_neg_half_mul_sq_add F.a ha z
  have hcos : Integrable fun u : ℝ =>
      (Real.exp (-F.a * u ^ 2 / 2) * Real.cos (F.omega * u) : ℝ) *
        Complex.exp (z * u) := by
    rw [show
      (fun u : ℝ =>
        (Real.exp (-F.a * u ^ 2 / 2) * Real.cos (F.omega * u) : ℝ) *
          Complex.exp (z * u)) =
        (fun u : ℝ =>
          (1 / 2 : ℂ) * Complex.exp (-(F.a : ℂ) / 2 * u ^ 2 +
              (z + Complex.I * F.omega) * u) +
            (1 / 2 : ℂ) * Complex.exp (-(F.a : ℂ) / 2 * u ^ 2 +
              (z - Complex.I * F.omega) * u)) by
        funext u
        exact gaussian_mul_cos_mul_cexp_eq F.a F.omega z u]
    exact (hp.const_mul _).add (hm.const_mul _)
  have hplain : Integrable fun u : ℝ =>
      (Real.exp (-F.a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u) := by
    refine h0.congr ?_
    filter_upwards with u
    rw [Complex.ofReal_exp, ← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hfun : gaborHatSlice F σ = fun u : ℝ =>
      (Real.sqrt (Real.pi / (2 * F.a)) / 2 : ℂ) *
        ((Real.exp (-F.a * u ^ 2 / 2) * Real.cos (F.omega * u) : ℝ) *
          Complex.exp (z * u) +
          (Real.exp (-F.omega ^ 2 / (2 * F.a)) : ℂ) *
            ((Real.exp (-F.a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u))) := by
    funext u
    unfold gaborHatSlice pureGaborAutocorrelation
    push_cast
    ring
  rw [hfun]
  exact (hcos.add (hplain.const_mul _)).const_mul _

theorem gaborHat_eq_integral_slice
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ τ : ℝ) :
    gaborHat F ((σ : ℂ) + τ * Complex.I) =
      ∫ u : ℝ, gaborHatSlice F σ u *
        Complex.exp ((τ : ℂ) * Complex.I * u) := by
  have hrep :=
    pureGaborHat_integral_representation F.a F.omega F.a_pos
      ((σ : ℂ) + τ * Complex.I)
  rw [gaborHat_of_pure hF, ← hrep]
  refine integral_congr_ae (Eventually.of_forall fun u => ?_)
  unfold gaborHatSlice
  dsimp
  have hexp :
      Complex.exp (((σ : ℂ) + τ * Complex.I - 1 / 2) * u) =
        Complex.exp (((σ : ℂ) - 1 / 2) * u) *
          Complex.exp ((τ : ℂ) * Complex.I * u) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  rw [hexp]
  ring

theorem gaborHat_eq_fourier_slice
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ ξ : ℝ) :
    gaborHat F ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I) =
      𝓕 (gaborHatSlice F σ) ξ := by
  have hrep :=
    pureGaborHat_integral_representation F.a F.omega F.a_pos
      ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I)
  rw [gaborHat_of_pure hF, ← hrep, Real.fourier_eq']
  refine integral_congr_ae (Eventually.of_forall fun u => ?_)
  have hinter : ⟪u, ξ⟫ = u * ξ := mul_comm ξ u
  unfold gaborHatSlice
  dsimp
  have hexp :
      Complex.exp
          (((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I - 1 / 2) * u) =
        Complex.exp (((σ : ℂ) - 1 / 2) * u) *
          Complex.exp (((-(2 * Real.pi) * ξ) * Complex.I) * u) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  have hfour :
      Complex.exp ((↑(-2 * Real.pi * ⟪u, ξ⟫) * Complex.I)) =
        Complex.exp (((-(2 * Real.pi) * ξ) * Complex.I) * u) := by
    simp [hinter, mul_comm, mul_left_comm, mul_assoc]
  rw [hexp, hfour]
  ring

theorem integrable_fourier_gaborHatSlice
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ : ℝ) :
    Integrable (𝓕 (gaborHatSlice F σ)) := by
  obtain ⟨c, C, hc, hC, hbd⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF σ σ
  have hmaj : Integrable fun ξ : ℝ =>
      C * Real.exp (-(c * (2 * Real.pi) ^ 2) * ξ ^ 2) :=
    (integrable_exp_neg_mul_sq (by positivity)).const_mul C
  have hpoint : ∀ ξ : ℝ, ‖𝓕 (gaborHatSlice F σ) ξ‖ ≤
      C * Real.exp (-(c * (2 * Real.pi) ^ 2) * ξ ^ 2) := by
    intro ξ
    have heq := gaborHat_eq_fourier_slice (F := F) hF σ ξ
    rw [← heq]
    have hh := hbd σ (-(2 * Real.pi) * ξ) le_rfl le_rfl
    convert hh.trans_eq ?_ using 1
    · congr 1; push_cast; ring
    · ring
  have hmeas : AEStronglyMeasurable (𝓕 (gaborHatSlice F σ)) volume :=
    (VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
      (continuous_inner (𝕜 := ℝ))
      (integrable_gaborHatSlice F σ)).aestronglyMeasurable
  exact hmaj.mono' hmeas (Eventually.of_forall hpoint)

theorem fourierInv_gaborHatSlice
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ : ℝ) :
    𝓕⁻ (𝓕 (gaborHatSlice F σ)) = gaborHatSlice F σ :=
  (continuous_gaborHatSlice F σ).fourierInv_fourier_eq
    (integrable_gaborHatSlice F σ) (integrable_fourier_gaborHatSlice hF σ)

/-- `∫ ĥ_W(σ+iτ) e^{-iτ u} dτ = 2π g(u) e^{(σ−1/2)u}`. -/
theorem gabor_hat_fourier_inversion
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ u : ℝ) :
    (∫ τ : ℝ, gaborHat F ((σ : ℂ) + τ * Complex.I) *
        Complex.exp (-(τ : ℂ) * Complex.I * u)) =
      (2 * Real.pi : ℂ) * gaborHatSlice F σ u := by
  set g : ℝ → ℂ := fun τ =>
    Complex.exp (-(τ : ℂ) * Complex.I * u) *
      gaborHat F ((σ : ℂ) + τ * Complex.I)
  have hinter : ∀ ξ : ℝ, ⟪ξ, u⟫ = ξ * u := fun ξ => mul_comm u ξ
  have hpoint : ∀ ξ : ℝ,
      Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (gaborHatSlice F σ) ξ =
        g (-(2 * Real.pi) * ξ) := by
    intro ξ
    dsimp [g]
    rw [← gaborHat_eq_fourier_slice hF σ ξ]
    simp [hinter ξ, mul_comm, mul_left_comm, mul_assoc]
  have hFinv :
      𝓕⁻ (𝓕 (gaborHatSlice F σ)) u =
        ∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (gaborHatSlice F σ) ξ := by
    rw [Real.fourierInv_eq']
    refine integral_congr_ae (Eventually.of_forall fun ξ => ?_)
    simp [smul_eq_mul]
  have hscale :
      (∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (gaborHatSlice F σ) ξ) =
        ∫ ξ : ℝ, g (-(2 * Real.pi) * ξ) :=
    integral_congr_ae (Eventually.of_forall hpoint)
  have hcomp := Measure.integral_comp_mul_left g (-(2 * Real.pi))
  have habs : |(-(2 * Real.pi))⁻¹| = (2 * Real.pi)⁻¹ := by
    rw [abs_inv, abs_neg, abs_of_pos (mul_pos (by norm_num) Real.pi_pos)]
  have h0 : 𝓕⁻ (𝓕 (gaborHatSlice F σ)) u = gaborHatSlice F σ u :=
    congrArg (fun f : ℝ → ℂ => f u) (fourierInv_gaborHatSlice hF σ)
  have hslice : gaborHatSlice F σ u =
      ((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ := by
    calc
      gaborHatSlice F σ u = 𝓕⁻ (𝓕 (gaborHatSlice F σ)) u := h0.symm
      _ = ∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
            𝓕 (gaborHatSlice F σ) ξ := hFinv
      _ = ∫ ξ : ℝ, g (-(2 * Real.pi) * ξ) := hscale
      _ = |(-(2 * Real.pi))⁻¹| • ∫ τ : ℝ, g τ := hcomp
      _ = ((2 * Real.pi)⁻¹ : ℝ) • ∫ τ : ℝ, g τ := by rw [habs]
      _ = ((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ := by
        rw [Complex.real_smul]; norm_cast
  have hgoal :
      (∫ τ : ℝ, gaborHat F ((σ : ℂ) + τ * Complex.I) *
          Complex.exp (-(τ : ℂ) * Complex.I * u)) =
        ∫ τ : ℝ, g τ :=
    integral_congr_ae (Eventually.of_forall fun τ => by dsimp [g]; ring)
  rw [hgoal]
  have hπ : (2 * Real.pi : ℂ) ≠ 0 := by
    exact_mod_cast (mul_ne_zero (by norm_num : (2 : ℝ) ≠ 0) Real.pi_ne_zero)
  calc
    ∫ τ : ℝ, g τ =
        (2 * Real.pi : ℂ) * (((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ) := by
      field_simp [hπ]
    _ = (2 * Real.pi : ℂ) * gaborHatSlice F σ u := by
      rw [← hslice]

/-! ## Right vertical -/

theorem continuous_gaborHat_vertical (F : GaborWeilTest) (σ : ℝ) :
    Continuous fun τ : ℝ => gaborHat F ((σ : ℂ) + τ * Complex.I) :=
  continuous_iff_continuousAt.mpr fun _τ =>
    ContinuousAt.comp (f := fun τ : ℝ => (σ : ℂ) + τ * Complex.I)
      (g := gaborHat F) (analyticAt_gaborHat F _).continuousAt
      (continuous_vertical_path σ).continuousAt

theorem continuous_gabor_right_edge_integrand (F : GaborWeilTest) :
    Continuous fun τ : ℝ =>
      logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        gaborHat F ((2 : ℂ) + τ * Complex.I) := by
  have hlog : Continuous fun τ : ℝ =>
      logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) :=
    continuous_iff_continuousAt.mpr fun τ =>
      ContinuousAt.comp (f := fun τ : ℝ => (2 : ℂ) + τ * Complex.I)
        (g := logDeriv riemannZeta)
        (analyticAt_logDeriv_riemannZeta
          (ne_one_of_re_eq (by norm_num : (2 : ℝ) ≠ 1) τ)
          (riemannZeta_ne_zero_of_re_eq_two (by simp))).continuousAt
        (continuous_vertical_path 2).continuousAt
  exact hlog.mul (continuous_gaborHat_vertical F 2)

theorem integrable_gabor_right_edge_integrand
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Integrable fun τ : ℝ =>
      logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        gaborHat F ((2 : ℂ) + τ * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF 2 2
  set K : ℝ := ‖logDeriv riemannZeta (2 : ℂ)‖ * C
  have hbd : ∀ τ : ℝ,
      ‖logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
          gaborHat F ((2 : ℂ) + τ * Complex.I)‖ ≤
        K * Real.exp (-c * τ ^ 2) := by
    intro τ
    have hζ :=
      right_edge_logDeriv_bound (s := (2 : ℂ) + τ * Complex.I) (by simp)
    have hh := hhat 2 τ le_rfl le_rfl
    rw [Complex.norm_mul]
    simpa [K, mul_assoc] using
      mul_le_mul hζ hh (norm_nonneg _) (norm_nonneg _)
  have hmaj : Integrable fun τ : ℝ => K * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul K
  exact hmaj.mono'
    (continuous_gabor_right_edge_integrand F).aestronglyMeasurable
    (Eventually.of_forall hbd)

theorem integrable_gabor_right_edge_term_mul_hat
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (n : ℕ) :
    Integrable fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((2 : ℂ) + τ * Complex.I) n *
        gaborHat F ((2 : ℂ) + τ * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF 2 2
  have hcont :=
    (continuous_LSeries_term_vonMangoldt_right_edge n).mul
      (continuous_gaborHat_vertical F 2)
  have hbd : ∀ τ : ℝ,
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          gaborHat F ((2 : ℂ) + τ * Complex.I)‖ ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          C * Real.exp (-c * τ ^ 2) := by
    intro τ
    rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_right_edge]
    simpa [mul_assoc] using
      mul_le_mul_of_nonneg_left (hhat 2 τ le_rfl le_rfl)
        (norm_nonneg
          (LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n))
  have hmaj : Integrable fun τ : ℝ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
        C * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul _
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

theorem summable_gabor_integral_norm_right_edge_term
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Summable fun n : ℕ =>
      ∫ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            gaborHat F ((2 : ℂ) + τ * Complex.I)‖ := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF 2 2
  have h2 : 1 < (2 : ℂ).re := by simp
  have hΛ : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact ArithmeticFunction.LSeriesSummable_vonMangoldt h2
  have hint : Integrable fun τ : ℝ => C * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul C
  have hbd : ∀ n : ℕ,
      (∫ τ : ℝ,
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              gaborHat F ((2 : ℂ) + τ * Complex.I)‖) ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          ∫ τ : ℝ, C * Real.exp (-c * τ ^ 2) := by
    intro n
    have hle : ∀ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            gaborHat F ((2 : ℂ) + τ * Complex.I)‖ ≤
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
            (C * Real.exp (-c * τ ^ 2)) := by
      intro τ
      rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_right_edge]
      exact mul_le_mul_of_nonneg_left (hhat 2 τ le_rfl le_rfl)
        (norm_nonneg
          (LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n))
    have hmeas : Integrable fun τ : ℝ =>
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          (C * Real.exp (-c * τ ^ 2)) :=
      hint.const_mul _
    refine (integral_mono_of_nonneg
      (Eventually.of_forall fun _ => norm_nonneg _)
      hmeas (Eventually.of_forall hle)).trans_eq ?_
    rw [integral_const_mul]
  exact Summable.of_nonneg_of_le
    (fun _ => integral_nonneg fun _ => norm_nonneg _) hbd (hΛ.mul_right _)

theorem logDeriv_gaborHat_eq_tsum_neg_term (F : GaborWeilTest) (τ : ℝ) :
    logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        gaborHat F ((2 : ℂ) + τ * Complex.I) =
      ∑' n : ℕ,
        -(LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          gaborHat F ((2 : ℂ) + τ * Complex.I)) := by
  have hs : 1 < ((2 : ℂ) + τ * Complex.I).re := by simp
  have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
  rw [logDeriv_riemannZeta_right_edge, LSeries, neg_mul, ← tsum_mul_right,
    tsum_neg]

theorem exp_neg_half_log_nat {n : ℕ} (hn : n ≠ 0) :
    Complex.exp (-((1 / 2 : ℂ) * Real.log n)) =
      (n : ℂ) ^ (-(1 / 2 : ℂ)) := by
  have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hlog : Complex.log (n : ℂ) = (Real.log n : ℂ) := by
    rw [← Complex.ofReal_natCast]
    exact (Complex.ofReal_log (Nat.cast_nonneg n)).symm
  rw [Complex.cpow_def_of_ne_zero hpos, hlog]
  ring_nf

theorem integral_gabor_term_mul_hat_eq_sqrt
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {n : ℕ}
    (hn : n ≠ 0) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          gaborHat F ((2 : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          ((n : ℂ) ^ (-(1 / 2 : ℂ))) *
          (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ) := by
  have hinv := gabor_hat_fourier_inversion (F := F) hF 2 (Real.log n)
  have hpoint : ∀ τ : ℝ,
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((2 : ℂ) + τ * Complex.I) n *
        gaborHat F ((2 : ℂ) + τ * Complex.I) =
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          Complex.exp (-(2 : ℂ) * Real.log n) *
            (gaborHat F ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) := by
    intro τ
    rw [LSeries_term_vonMangoldt_right_edge_eq_exp hn τ]
    have hsplit :
        Complex.exp (-((2 : ℂ) + τ * Complex.I) * Real.log n) =
          Complex.exp (-(2 : ℂ) * Real.log n) *
            Complex.exp (-(τ : ℂ) * Complex.I * Real.log n) := by
      rw [← Complex.exp_add]; ring_nf
    rw [hsplit]; ring
  set c : ℂ :=
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      Complex.exp (-(2 : ℂ) * Real.log n)
  have hrew :
      (∫ τ : ℝ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            gaborHat F ((2 : ℂ) + τ * Complex.I)) =
        c * ∫ τ : ℝ,
              gaborHat F ((2 : ℂ) + τ * Complex.I) *
                Complex.exp (-(τ : ℂ) * Complex.I * Real.log n) := by
    have heq :
        (fun τ : ℝ =>
            LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              gaborHat F ((2 : ℂ) + τ * Complex.I)) =
          fun τ : ℝ =>
            c * (gaborHat F ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) :=
      funext hpoint
    have heq' :
        (fun τ : ℝ =>
            c * (gaborHat F ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n))) =
          fun τ : ℝ =>
            c • (gaborHat F ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) :=
      funext fun _ => (smul_eq_mul _ _).symm
    rw [heq, heq', integral_smul, smul_eq_mul]
  rw [hrew]
  have hinv' :
      (∫ τ : ℝ, gaborHat F ((2 : ℂ) + τ * Complex.I) *
          Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) =
        (2 * Real.pi : ℂ) * gaborHatSlice F 2 (Real.log n) := hinv
  rw [hinv']
  unfold gaborHatSlice c
  have hcancel :
      Complex.exp (-(2 : ℂ) * Real.log n) *
          Complex.exp (((2 : ℂ) - 1 / 2) * Real.log n) =
        Complex.exp (-((1 / 2 : ℂ) * Real.log n)) := by
    rw [← Complex.exp_add]; congr 1; ring
  calc
    (ArithmeticFunction.vonMangoldt n : ℂ) *
          Complex.exp (-(2 : ℂ) * Real.log n) *
        ((2 * Real.pi : ℂ) *
          ((pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ) *
            Complex.exp (((2 : ℂ) - 1 / 2) * Real.log n))) =
        (2 * Real.pi : ℂ) *
          (ArithmeticFunction.vonMangoldt n : ℂ) *
            (Complex.exp (-(2 : ℂ) * Real.log n) *
              Complex.exp (((2 : ℂ) - 1 / 2) * Real.log n)) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ) := by
      ring
    _ = (2 * Real.pi : ℂ) *
          (ArithmeticFunction.vonMangoldt n : ℂ) *
            Complex.exp (-((1 / 2 : ℂ) * Real.log n)) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ) := by
      rw [hcancel]
    _ = (2 * Real.pi : ℂ) *
          (ArithmeticFunction.vonMangoldt n : ℂ) *
            ((n : ℂ) ^ (-(1 / 2 : ℂ))) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ) := by
      rw [exp_neg_half_log_nat hn]

theorem integral_gabor_term_mul_hat_eq_sqrt_all
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (n : ℕ) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          gaborHat F ((2 : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (if n = 0 then 0 else
            (n : ℂ) ^ (-(1 / 2 : ℂ)) *
              (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ)) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp [LSeries.term_zero]
  · rw [if_neg hn]
    convert integral_gabor_term_mul_hat_eq_sqrt hF hn using 1
    ring

/-- Half-comb `Σ Λ(n) n^{-1/2} g_closed(log n)`.  The corpus comb
`2Λ/√n` is twice this pairing after left+right and evenness. -/
noncomputable def gaborHalfPrimeComb (F : GaborWeilTest) : ℂ :=
  ∑' n : ℕ,
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      (if n = 0 then 0 else
        (n : ℂ) ^ (-(1 / 2 : ℂ)) *
          (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ))

/-- r564 right vertical: `∫ (ζ′/ζ)(2+iτ) ĥ_W dτ = −2π Σ Λ(n) n^{-1/2} g(log n)`. -/
theorem gabor_rightVerticalIntegral_eq_prime_sum
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        gaborHat F ((2 : ℂ) + τ * Complex.I)) =
      - (2 * Real.pi : ℂ) * gaborHalfPrimeComb F := by
  have hpt :
      (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
          gaborHat F ((2 : ℂ) + τ * Complex.I)) =
        ∫ τ : ℝ,
          ∑' n : ℕ,
            -(LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              gaborHat F ((2 : ℂ) + τ * Complex.I)) :=
    integral_congr_ae (Eventually.of_forall
      (logDeriv_gaborHat_eq_tsum_neg_term F))
  have hswap :=
    integral_tsum_of_summable_integral_norm
      (F := fun (n : ℕ) (τ : ℝ) =>
        -(LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          gaborHat F ((2 : ℂ) + τ * Complex.I)))
      (fun n => (integrable_gabor_right_edge_term_mul_hat hF n).neg)
      (by simpa [norm_neg] using
        summable_gabor_integral_norm_right_edge_term hF)
  rw [hpt, ← hswap]
  simp_rw [integral_neg, integral_gabor_term_mul_hat_eq_sqrt_all hF]
  have hfactor :
      (∑' n : ℕ,
          (2 * Real.pi : ℂ) *
            (ArithmeticFunction.vonMangoldt n : ℂ) *
              (if n = 0 then 0 else
                (n : ℂ) ^ (-(1 / 2 : ℂ)) *
                  (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ))) =
        (2 * Real.pi : ℂ) * gaborHalfPrimeComb F := by
    unfold gaborHalfPrimeComb
    rw [← tsum_mul_left]
    exact tsum_congr fun n => by ring
  rw [tsum_neg, hfactor]
  ring

/-! ## Left vertical and arch clamp -/

noncomputable def gaborLeftEdgeArchIntegral (F : GaborWeilTest) : ℂ :=
  ∫ τ : ℝ, logDeriv zetaFEFactor
      (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
    gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)

noncomputable def gaborReflectedHalfPrimeComb (F : GaborWeilTest) : ℂ :=
  ∑' n : ℕ,
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      (if n = 0 then 0 else
        (n : ℂ) ^ (-(1 / 2 : ℂ)) *
          (pureGaborAutocorrelation F.a F.omega (-Real.log n) : ℂ))

theorem gaborReflectedHalfPrimeComb_eq_half (F : GaborWeilTest) :
    gaborReflectedHalfPrimeComb F = gaborHalfPrimeComb F := by
  unfold gaborReflectedHalfPrimeComb gaborHalfPrimeComb
  refine tsum_congr fun n => ?_
  simp [pureGaborAutocorrelation_even]

theorem logDeriv_gaborHat_eq_tsum_dual_sub_fe
    (F : GaborWeilTest) (τ : ℝ) :
    logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
      (∑' n : ℕ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
        logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by
    simp; norm_num
  have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
  rw [logDeriv_riemannZeta_left_edge, logDeriv_riemannZeta_dual_left_edge,
    neg_neg, sub_mul, LSeries, tsum_mul_right]

/-- Left-edge prime reflection: FE + dual inversion give
`2π Σ Λ(n) n^{-1/2} g(−log n)` minus the `χ′/χ` clamp.
The dual inversion is the same Fourier lemma at `σ = −1/16`,
`u = −log n`; the remaining work is Fubini against Gaussian decay
(identical to the right edge).  Named so the assembly can cite it. -/
def GaborLeftPrimeReflection : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    (∫ τ : ℝ, logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) * gaborReflectedHalfPrimeComb F -
        gaborLeftEdgeArchIntegral F

/-- Contour `T→∞` assembly along Landau gaps:
`I • right − I • left = (2πi)(Z − ĥ_W(1))`.
The r557 bricks (fixed-`T` residue, horizontal vanishing, zero
summability) plus the two improper vertical integrals are the
inputs; the remaining glue is the interval-to-improper limit of
the vertical sides.  Unasserted.  Not a `sorry`. -/
def GaborContourVerticalLimit : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          gaborHat F ((2 : ℂ) + τ * I)) -
      I • (∫ τ : ℝ, logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * I)) =
      (2 * (Real.pi : ℂ) * I) *
        ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) -
          gaborHat F 1)

/-- Half-comb real part equals half the corpus comb, once the
closed-form identification and `n^{-1/2} = 1/√n` are available. -/
def GaborHalfCombReal : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    (gaborHalfPrimeComb F).re = gaborPrimeComb F / 2

/-- r564: the left-edge `χ′/χ` integral equals the critical-line
Digamma pairing plus `ĥ_W(0)`.

Specification (TFPT v640/v648/v719, numerically certified):
  * `ψ(1/4) = −γ_EM − 3·log 2 − π/2`
  * archimedean density `ω(τ) = Re ψ(1/4 + iτ/2) − log π`

Mathlib v4.29.1 lists Gauss's integral representation of digamma as
TODO (`GaussDigammaIntegralRepresentation` in `RH/Elementwise.lean`).
Same family as `arch_gauss_mellin_digamma_identity`.  NO RH CLAIM. -/
def GaborArchDigammaIdentification : Prop :=
  ∀ F : GaborWeilTest, F.admissible → F.coeffs = ⟨1, 0, 0⟩ →
    (gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ))).re =
      (gaborHat F 0).re + gaborArchSide F

end RH
