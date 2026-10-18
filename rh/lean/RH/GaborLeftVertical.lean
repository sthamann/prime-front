/-
RH/GaborLeftVertical.lean -- r570 left-edge prime reflection.

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free FE + dual inversion for
the Gabor left vertical.  Digamma identification stays parked.
-/
import RH.GaborVertical

namespace RH

open Complex Filter Function MeasureTheory Set
open scoped FourierTransform Topology RealInnerProductSpace LSeries.notation

/-! ## Digamma specification (unasserted; parked) -/

def GaborDigammaQuarterValue : Prop :=
  Complex.digamma (1 / 4 : ℂ) =
    (-Real.eulerMascheroniConstant - 3 * Real.log 2 - Real.pi / 2 : ℂ)

noncomputable def gaborArchDensity (τ : ℝ) : ℝ :=
  (Complex.digamma ((1 / 4 : ℂ) + (τ / 2 : ℝ) * Complex.I)).re -
    Real.log Real.pi

theorem gaborArchSide_eq_density_pairing (F : GaborWeilTest) :
    gaborArchSide F =
      (1 / (2 * Real.pi)) *
        ∫ t : ℝ, (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re *
          gaborArchDensity t := rfl

def GaborArchDigammaIdentificationSpec : Prop :=
  ∀ F : GaborWeilTest, F.admissible → F.coeffs = ⟨1, 0, 0⟩ →
    (gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ))).re =
      (gaborHat F 0).re +
        (1 / (2 * Real.pi)) *
          ∫ t : ℝ, (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re *
            gaborArchDensity t

theorem GaborArchDigammaIdentificationSpec_iff :
    GaborArchDigammaIdentificationSpec ↔ GaborArchDigammaIdentification :=
  Iff.rfl

/-! ## Continuity and termwise Gaussian integrability -/

theorem continuous_gabor_left_edge_integrand (F : GaborWeilTest) :
    Continuous fun τ : ℝ =>
      logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  have hlog : Continuous fun τ : ℝ =>
      logDeriv riemannZeta
        (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) :=
    continuous_iff_continuousAt.mpr fun τ =>
      ContinuousAt.comp
        (f := fun τ : ℝ => ((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)
        (g := logDeriv riemannZeta)
        (analyticAt_logDeriv_riemannZeta
          (ne_one_of_re_eq (by norm_num : (-1 / 16 : ℝ) ≠ 1) τ)
          (riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen
            (by simp))).continuousAt
        (continuous_vertical_path (-1 / 16)).continuousAt
  exact hlog.mul (continuous_gaborHat_vertical F (-1 / 16))

theorem integrable_gabor_left_edge_term_mul_hat
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (n : ℕ) :
    Integrable fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) (-1 / 16)
  have hcont :=
    (continuous_LSeries_term_vonMangoldt_dual_left_edge n).mul
      (continuous_gaborHat_vertical F (-1 / 16))
  have hbd : ∀ τ : ℝ,
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ *
          C * Real.exp (-c * τ ^ 2) := by
    intro τ
    rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_dual_left_edge]
    simpa [mul_assoc] using
      mul_le_mul_of_nonneg_left (hhat (-1 / 16) τ le_rfl le_rfl)
        (norm_nonneg
          (LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((17 / 16 : ℝ) : ℂ) n))
  have hmaj : Integrable fun τ : ℝ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ * C * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul _
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

theorem summable_gabor_integral_norm_left_edge_term
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Summable fun n : ℕ =>
      ∫ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) (-1 / 16)
  have hσ : 1 < (((17 / 16 : ℝ) : ℂ).re) := by simp; norm_num
  have hΛ : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact ArithmeticFunction.LSeriesSummable_vonMangoldt hσ
  have hint : Integrable fun τ : ℝ => C * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul C
  have hbd : ∀ n : ℕ,
      (∫ τ : ℝ,
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖) ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ *
          ∫ τ : ℝ, C * Real.exp (-c * τ ^ 2) := by
    intro n
    have hle : ∀ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((17 / 16 : ℝ) : ℂ) n‖ *
            (C * Real.exp (-c * τ ^ 2)) := by
      intro τ
      rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_dual_left_edge]
      exact mul_le_mul_of_nonneg_left (hhat (-1 / 16) τ le_rfl le_rfl)
        (norm_nonneg
          (LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((17 / 16 : ℝ) : ℂ) n))
    have hmeas : Integrable fun τ : ℝ =>
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ * (C * Real.exp (-c * τ ^ 2)) :=
      hint.const_mul _
    refine (integral_mono_of_nonneg
      (Eventually.of_forall fun _ => norm_nonneg _)
      hmeas (Eventually.of_forall hle)).trans_eq ?_
    rw [integral_const_mul]
  exact Summable.of_nonneg_of_le
    (fun _ => integral_nonneg fun _ => norm_nonneg _) hbd (hΛ.mul_right _)

/-! ## Termwise dual inversion at `σ = -1/16`, `u = -log n` -/

theorem integral_gabor_dual_term_mul_hat_eq_sqrt
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {n : ℕ}
    (hn : n ≠ 0) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          ((n : ℂ) ^ (-(1 / 2 : ℂ))) *
          (pureGaborAutocorrelation F.a F.omega (-Real.log n) : ℂ) := by
  set u : ℝ := -Real.log n
  have hinv := gabor_hat_fourier_inversion (F := F) hF (-1 / 16) u
  have hpoint : ∀ τ : ℝ,
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
            (gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) := by
    intro τ
    rw [LSeries_term_vonMangoldt_dual_left_edge_eq_exp hn τ]
    have hsplit :
        Complex.exp (-(((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            Real.log n) =
          Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
            Complex.exp (-(τ : ℂ) * Complex.I * u) := by
      rw [← Complex.exp_add]
      congr 1
      unfold u
      push_cast
      ring
    rw [hsplit]
    ring
  set c : ℂ :=
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      Complex.exp (-((17 / 16 : ℂ) * Real.log n))
  have hrew :
      (∫ τ : ℝ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
        c * ∫ τ : ℝ,
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
                Complex.exp (-(τ : ℂ) * Complex.I * u) := by
    have heq :
        (fun τ : ℝ =>
            LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
          fun τ : ℝ =>
            c * (gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) :=
      funext hpoint
    have heq' :
        (fun τ : ℝ =>
            c * (gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u))) =
          fun τ : ℝ =>
            c • (gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) :=
      funext fun _ => (smul_eq_mul _ _).symm
    rw [heq, heq', integral_smul, smul_eq_mul]
  rw [hrew, hinv]
  have hcancel :
      Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
          Complex.exp (((-1 / 16 : ℂ) - 1 / 2) * u) =
        Complex.exp (-((1 / 2 : ℂ) * Real.log n)) := by
    rw [← Complex.exp_add]
    congr 1
    unfold u
    push_cast
    ring
  have hmul :
      c * ((2 * Real.pi : ℂ) * gaborHatSlice F (-1 / 16) u) =
        (2 * Real.pi : ℂ) *
          (ArithmeticFunction.vonMangoldt n : ℂ) *
            (Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
              Complex.exp (((-1 / 16 : ℂ) - 1 / 2) * u)) *
            (pureGaborAutocorrelation F.a F.omega u : ℂ) := by
    unfold gaborHatSlice c
    ring_nf
    congr 1
    congr 1
    push_cast
    ring
  -- After the `rw [hrew, hinv]` the goal is `c * (2π * slice) = ...`
  -- Re-state from `hmul`.
  have hgoal :
      c * ((2 * Real.pi : ℂ) * gaborHatSlice F (-1 / 16) u) =
        (2 * Real.pi : ℂ) *
          (ArithmeticFunction.vonMangoldt n : ℂ) *
            ((n : ℂ) ^ (-(1 / 2 : ℂ))) *
            (pureGaborAutocorrelation F.a F.omega u : ℂ) := by
    rw [hmul, hcancel, exp_neg_half_log_nat hn]
  exact hgoal

theorem integral_gabor_dual_term_mul_hat_eq_sqrt_all
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (n : ℕ) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (if n = 0 then 0 else
            (n : ℂ) ^ (-(1 / 2 : ℂ)) *
              (pureGaborAutocorrelation F.a F.omega (-Real.log n) : ℂ)) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp [LSeries.term_zero]
  · rw [if_neg hn]
    convert integral_gabor_dual_term_mul_hat_eq_sqrt hF hn using 1
    ring

/-! ## Full left-edge channels -/

theorem integrable_gabor_LSeries_hat_left_edge
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Integrable fun τ : ℝ =>
      L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) (-1 / 16)
  have hL : Continuous fun τ : ℝ =>
      L ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) := by
    convert continuous_logDeriv_dual_left_edge.neg using 1
    funext τ
    rw [logDeriv_riemannZeta_dual_left_edge, neg_neg]
  have hcont := hL.mul (continuous_gaborHat_vertical F (-1 / 16))
  have hbd : ∀ τ : ℝ,
      ‖L ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
        ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ *
          C * Real.exp (-c * τ ^ 2) := by
    intro τ
    have hζ :=
      norm_logDeriv_riemannZeta_le_at_seventeen_sixteen
        (s := ((17 / 16 : ℝ) : ℂ) - τ * Complex.I) (by simp)
    have hLnorm : ‖L ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ ≤
        ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ := by
      have hnorm :
          ‖L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ =
            ‖logDeriv riemannZeta
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ := by
        rw [logDeriv_riemannZeta_dual_left_edge, norm_neg]
      rw [hnorm]
      exact hζ
    rw [Complex.norm_mul]
    simpa [mul_assoc] using
      mul_le_mul hLnorm (hhat (-1 / 16) τ le_rfl le_rfl)
        (norm_nonneg _) (norm_nonneg _)
  have hmaj : Integrable fun τ : ℝ =>
      ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ *
        C * Real.exp (-c * τ ^ 2) :=
    (integrable_exp_neg_mul_sq hc).const_mul _
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

theorem integrable_one_add_abs_mul_gaussian
    {c : ℝ} (hc : 0 < c) :
    Integrable fun τ : ℝ =>
      (1 + |τ|) * Real.exp (-c * τ ^ 2) := by
  have h0 : Integrable fun τ : ℝ => Real.exp (-c * τ ^ 2) :=
    integrable_exp_neg_mul_sq hc
  have hsq : Integrable fun τ : ℝ =>
      τ ^ 2 * Real.exp (-c * τ ^ 2) := by
    have hhalf := integrable_exp_neg_mul_sq (half_pos hc)
    have hbd : ∀ τ : ℝ,
        |τ ^ 2 * Real.exp (-c * τ ^ 2)| ≤
          (2 / c) * Real.exp (-(c / 2) * τ ^ 2) := by
      intro τ
      have hx : (c / 2) * τ ^ 2 ≤ Real.exp ((c / 2) * τ ^ 2) :=
        (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1)).trans
          (Real.add_one_le_exp ((c / 2) * τ ^ 2))
      have hτ2 : τ ^ 2 ≤ (2 / c) * Real.exp ((c / 2) * τ ^ 2) := by
        have := mul_le_mul_of_nonneg_left hx (by positivity : (0 : ℝ) ≤ 2 / c)
        have hrew : (2 / c) * ((c / 2) * τ ^ 2) = τ ^ 2 := by
          field_simp [hc.ne']
        linarith [this, hrew]
      have hmul := mul_le_mul_of_nonneg_right hτ2 (Real.exp_pos (-c * τ ^ 2)).le
      have hsimp :
          (2 / c) * Real.exp ((c / 2) * τ ^ 2) * Real.exp (-c * τ ^ 2) =
            (2 / c) * Real.exp (-(c / 2) * τ ^ 2) := by
        rw [mul_assoc, ← Real.exp_add]
        congr 2
        ring
      rw [abs_mul, abs_of_nonneg (sq_nonneg τ),
        abs_of_nonneg (Real.exp_pos _).le]
      rwa [hsimp] at hmul
    exact (hhalf.const_mul (2 / c)).mono'
      (Continuous.aestronglyMeasurable (by fun_prop))
      (Eventually.of_forall fun τ => by
        simpa [Real.norm_eq_abs] using hbd τ)
  have habs : Integrable fun τ : ℝ => |τ| * Real.exp (-c * τ ^ 2) := by
    have hsum : Integrable fun τ : ℝ =>
        (1 + τ ^ 2) * Real.exp (-c * τ ^ 2) := by
      have hfun :
          (fun τ : ℝ => (1 + τ ^ 2) * Real.exp (-c * τ ^ 2)) =
            (fun τ : ℝ => Real.exp (-c * τ ^ 2) +
              τ ^ 2 * Real.exp (-c * τ ^ 2)) := by
        funext τ; ring
      rw [hfun]
      exact h0.add hsq
    refine hsum.mono' (Continuous.aestronglyMeasurable (by fun_prop))
      (Eventually.of_forall fun τ => ?_)
    have hle : |τ| ≤ 1 + τ ^ 2 := by nlinarith [sq_abs τ, abs_nonneg τ]
    rw [Real.norm_eq_abs, abs_mul, abs_abs,
      abs_of_nonneg (Real.exp_pos _).le]
    exact mul_le_mul_of_nonneg_right hle (Real.exp_pos _).le
  have hfun :
      (fun τ : ℝ => (1 + |τ|) * Real.exp (-c * τ ^ 2)) =
        (fun τ : ℝ => Real.exp (-c * τ ^ 2) +
          |τ| * Real.exp (-c * τ ^ 2)) := by
    funext τ; ring
  rw [hfun]
  exact h0.add habs

theorem exists_gabor_left_edge_compact_bound (F : GaborWeilTest) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ τ : ℝ, |τ| ≤ 2 →
      ‖logDeriv riemannZeta
            (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤ M := by
  set f : ℝ → ℂ := fun τ =>
    logDeriv riemannZeta
        (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
      gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)
  have hOn : ContinuousOn f (Icc (-2 : ℝ) 2) :=
    (continuous_gabor_left_edge_integrand F).continuousOn
  obtain ⟨M, hM⟩ := isCompact_Icc.exists_bound_of_continuousOn hOn
  refine ⟨M, ?_, ?_⟩
  · exact le_trans (norm_nonneg (f 0)) (hM 0 ⟨by norm_num, by norm_num⟩)
  · intro τ hτ
    exact hM τ (abs_le.mp hτ)

theorem integrable_gabor_left_edge_integrand
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Integrable fun τ : ℝ =>
      logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) (-1 / 16)
  obtain ⟨M, hM0, hM⟩ := exists_gabor_left_edge_compact_bound F
  set f : ℝ → ℂ := fun τ =>
    logDeriv riemannZeta
        (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
      gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)
  set K : ℝ := 2 * leftEdgeConst * C
  have hK0 : 0 ≤ K :=
    mul_nonneg (mul_nonneg (by norm_num : (0 : ℝ) ≤ 2) leftEdgeConst_nonneg)
      hC.le
  set g : ℝ → ℝ := fun τ =>
    Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ +
      K * ((1 + |τ|) * Real.exp (-c * τ ^ 2))
  have hind : Integrable
      (Set.indicator (Icc (-2 : ℝ) 2) (fun _ : ℝ => M)) :=
    (continuousOn_const.integrableOn_compact isCompact_Icc).integrable_indicator
      measurableSet_Icc
  have hlog :=
    (integrable_one_add_abs_mul_gaussian hc).const_mul K
  have hmaj : Integrable g := hind.add hlog
  have hbd : ∀ τ, ‖f τ‖ ≤ g τ := by
    intro τ
    have hlognn : 0 ≤ K * ((1 + |τ|) * Real.exp (-c * τ ^ 2)) :=
      mul_nonneg hK0
        (mul_nonneg (add_nonneg (by norm_num) (abs_nonneg _))
          (Real.exp_pos _).le)
    have hindnn : 0 ≤
        Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ :=
      Set.indicator_apply_nonneg (fun _ => hM0)
    by_cases hτ : |τ| ≤ 2
    · have hmem : τ ∈ Icc (-2 : ℝ) 2 := abs_le.mp hτ
      have : Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ = M :=
        Set.indicator_of_mem hmem (fun _ => M)
      have hf : ‖f τ‖ ≤ M := hM τ hτ
      simpa [g, this] using le_add_of_le_of_nonneg hf hlognn
    · have hge : (2 : ℝ) ≤ |τ| := le_of_lt (lt_of_not_ge hτ)
      have hζ := left_edge_logDeriv_bound
        (s := ((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)
        (by simp) (by simpa using hge)
      have hh := hhat (-1 / 16) τ le_rfl le_rfl
      have hnot : τ ∉ Icc (-2 : ℝ) 2 := fun h => hτ (abs_le.mpr h)
      have : Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ = 0 :=
        Set.indicator_of_notMem hnot (fun _ => M)
      have him : (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).im = τ := by
        simp
      have hζ' : ‖logDeriv riemannZeta
            (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
          leftEdgeConst * (1 + Real.log (2 + |τ|)) := by
        simpa [him] using hζ
      have hlognn' : 0 ≤ 1 + Real.log (2 + |τ|) :=
        add_nonneg (by norm_num)
          (Real.log_nonneg
            (le_add_of_le_of_nonneg (by norm_num : (1 : ℝ) ≤ 2)
              (abs_nonneg τ)))
      have hf : ‖f τ‖ ≤
          (leftEdgeConst * (1 + Real.log (2 + |τ|))) *
            (C * Real.exp (-c * τ ^ 2)) := by
        rw [Complex.norm_mul]
        exact mul_le_mul hζ' hh (norm_nonneg _)
          (mul_nonneg leftEdgeConst_nonneg hlognn')
      have hlogle : 1 + Real.log (2 + |τ|) ≤ 2 + |τ| := by
        have hpos : 0 < 2 + |τ| := by positivity
        have := Real.log_le_sub_one_of_pos hpos
        linarith
      have hf' : ‖f τ‖ ≤ K * ((1 + |τ|) * Real.exp (-c * τ ^ 2)) := by
        refine hf.trans ?_
        unfold K
        have h2 : 2 + |τ| ≤ 2 * (1 + |τ|) := by nlinarith [abs_nonneg τ]
        have hle : 1 + Real.log (2 + |τ|) ≤ 2 * (1 + |τ|) :=
          hlogle.trans h2
        have := mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hle
            (mul_nonneg leftEdgeConst_nonneg hC.le))
          (Real.exp_pos (-c * τ ^ 2)).le
        simpa [mul_assoc, mul_left_comm, mul_comm] using this
      simpa [g, this] using le_add_of_nonneg_of_le hindnn hf'
  exact hmaj.mono' (continuous_gabor_left_edge_integrand F).aestronglyMeasurable
    (Eventually.of_forall hbd)

theorem integrable_gabor_left_edge_fe_integrand
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Integrable fun τ : ℝ =>
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  have hpt : (fun τ : ℝ =>
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
    (fun τ : ℝ =>
      L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
    (fun τ : ℝ =>
      logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) := by
    funext τ
    have h := logDeriv_gaborHat_eq_tsum_dual_sub_fe F τ
    have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by
      simp; norm_num
    have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
    have htsum :
        (∑' n : ℕ,
            LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
          L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
      rw [LSeries, tsum_mul_right]
    rw [htsum] at h
    calc
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
          L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
          (L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
            logDeriv zetaFEFactor
                (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) := by
        ring
      _ = L ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
        logDeriv riemannZeta
            (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
        rw [← h]
  rw [hpt]
  exact (integrable_gabor_LSeries_hat_left_edge hF).sub
    (integrable_gabor_left_edge_integrand hF)

/-- r570: left vertical equals the reflected half-comb minus the
`χ′/χ` clamp.  Digamma identification of the clamp is not claimed. -/
theorem gabor_leftVerticalIntegral_eq_reflected_prime_sub_arch
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    (∫ τ : ℝ, logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) * gaborReflectedHalfPrimeComb F -
        gaborLeftEdgeArchIntegral F := by
  have hpt :
      (∫ τ : ℝ, logDeriv riemannZeta
            (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
        ∫ τ : ℝ,
          (∑' n : ℕ,
              LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
            logDeriv zetaFEFactor
              (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) :=
    integral_congr_ae (Eventually.of_forall
      (logDeriv_gaborHat_eq_tsum_dual_sub_fe F))
  have hA := integrable_gabor_LSeries_hat_left_edge hF
  have hB := integrable_gabor_left_edge_fe_integrand hF
  have hA' : Integrable fun τ : ℝ =>
      ∑' n : ℕ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
    convert hA using 1
    funext τ
    have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by
      simp; norm_num
    have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
    rw [LSeries, tsum_mul_right]
  have hsplit := integral_sub hA' hB
  rw [hpt, hsplit]
  have hswap :=
    integral_tsum_of_summable_integral_norm
      (F := fun (n : ℕ) (τ : ℝ) =>
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I))
      (integrable_gabor_left_edge_term_mul_hat hF)
      (summable_gabor_integral_norm_left_edge_term hF)
  rw [← hswap]
  simp_rw [integral_gabor_dual_term_mul_hat_eq_sqrt_all hF]
  have hfactor :
      (∑' n : ℕ,
          (2 * Real.pi : ℂ) *
            (ArithmeticFunction.vonMangoldt n : ℂ) *
              (if n = 0 then 0 else
                (n : ℂ) ^ (-(1 / 2 : ℂ)) *
                  (pureGaborAutocorrelation F.a F.omega (-Real.log n) : ℂ))) =
        (2 * Real.pi : ℂ) * gaborReflectedHalfPrimeComb F := by
    unfold gaborReflectedHalfPrimeComb
    rw [← tsum_mul_left]
    exact tsum_congr fun n => by ring
  rw [hfactor]
  rfl

theorem gaborLeftPrimeReflection_holds : GaborLeftPrimeReflection :=
  fun _ hF => gabor_leftVerticalIntegral_eq_reflected_prime_sub_arch hF

#print axioms gabor_leftVerticalIntegral_eq_reflected_prime_sub_arch
#print axioms gaborLeftPrimeReflection_holds
#print axioms GaborArchDigammaIdentificationSpec_iff

end RH
