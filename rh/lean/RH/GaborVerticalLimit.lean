/-
RH/GaborVerticalLimit.lean -- r576 Landau-gap T→∞ glue for the
Gabor contour.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not prove
`GaborExplicitFormula`.  It proves `GaborContourVerticalLimit`:
along a Landau gap height the fixed-`T` residue identity, the
horizontal vanishing, the interval→improper vertical limits
(Gaussian decay of ĥ_W), and the spectral Finset exhaustion
pass to the improper identity
`I • ∫_right − I • ∫_left = (2πi)(∑ m_ρ ĥ_W(ρ) − ĥ_W(1))`.

The remaining EF remainder after this cut is
`GaborArchDigammaIdentification` (Mathlib v4.29.1 has no Gauss
integral for ψ).  No asserting `sorry`.
-/
import RH.GaborLeftVertical
import RH.GaborHorizontalEdges

namespace RH

open Complex Filter Function MeasureTheory Set
open scoped Topology Interval

/-! ## Multiplicity-weighted zero summability -/

lemma tendsto_one_add_log_add_mul_gauss {c b : ℝ}
    (hc : 0 < c) (hb : 0 ≤ b) :
    Tendsto (fun t : ℝ =>
      (1 + Real.log (t + b)) * Real.exp (-c * t ^ 2))
      atTop (nhds 0) := by
  have h3 := tendsto_log_pow_mul_gauss hc
  have h2 : Tendsto (fun t : ℝ =>
      2 * ((1 + Real.log t) ^ 3 * Real.exp (-c * t ^ 2)))
      atTop (nhds 0) := by
    convert h3.const_mul (2 : ℝ)
    rw [mul_zero]
  refine squeeze_zero' ?nonneg ?le h2
  · filter_upwards [eventually_ge_atTop (1 : ℝ)] with t ht
    have : (1 : ℝ) ≤ t + b := by linarith
    exact mul_nonneg (add_nonneg (by norm_num) (Real.log_nonneg this))
      (Real.exp_pos _).le
  · filter_upwards [eventually_ge_atTop (max (1 : ℝ) b)] with t ht
    have ht1 : (1 : ℝ) ≤ t := le_trans (le_max_left _ _) ht
    have htb : b ≤ t := le_trans (le_max_right _ _) ht
    have h2t : t + b ≤ 2 * t := by linarith
    have hlog2t : Real.log (t + b) ≤ Real.log (2 * t) :=
      Real.log_le_log (by linarith) h2t
    have hlog2 : Real.log (2 * t) = Real.log 2 + Real.log t :=
      Real.log_mul (by norm_num) (by linarith)
    have hlogt : (0 : ℝ) ≤ Real.log t := Real.log_nonneg ht1
    have hstep : 1 + Real.log (t + b) ≤ 2 * (1 + Real.log t) := by
      have : 1 + Real.log (t + b) ≤ 1 + Real.log 2 + Real.log t := by
        linarith [hlog2t, hlog2]
      have h2lt : Real.log 2 ≤ 1 :=
        (Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2)).trans
          (by norm_num)
      linarith [hlogt, h2lt]
    have h1 : (1 : ℝ) ≤ 1 + Real.log t := by linarith [hlogt]
    have hpow : 1 + Real.log t ≤ (1 + Real.log t) ^ 3 := by
      nlinarith [h1, sq_nonneg (1 + Real.log t),
        sq_nonneg (1 + Real.log t - 1)]
    have hexp : (0 : ℝ) ≤ Real.exp (-c * t ^ 2) := (Real.exp_pos _).le
    calc
      (1 + Real.log (t + b)) * Real.exp (-c * t ^ 2) ≤
          (2 * (1 + Real.log t)) * Real.exp (-c * t ^ 2) :=
        mul_le_mul_of_nonneg_right hstep hexp
      _ ≤ (2 * (1 + Real.log t) ^ 3) * Real.exp (-c * t ^ 2) :=
        mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hpow (by norm_num : (0 : ℝ) ≤ 2))
          hexp
      _ = 2 * ((1 + Real.log t) ^ 3 * Real.exp (-c * t ^ 2)) := by
        ring

lemma le_B_of_neg_max (R B : ℝ) (hR : max (-B) 0 ≤ R) : -R ≤ B := by
  have h2 : -R ≤ -max (-B) 0 := neg_le_neg hR
  have h3 : -max (-B) 0 ≤ B := by
    rcases le_total (-B) 0 with h | h
    · rw [max_eq_right h]; linarith
    · rw [max_eq_left h]; linarith
  exact h2.trans h3

lemma one_add_log_im_mul_gauss_le {c : ℝ} (hc : 0 < c) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ t : ℝ,
      (1 + Real.log (2 + |t| + 5 / 4)) * Real.exp (-c * t ^ 2) ≤
        K * Real.exp (-(c / 2) * t ^ 2) := by
  have hc2 : 0 < c / 2 := half_pos hc
  set f : ℝ → ℝ := fun t =>
    (1 + Real.log (2 + |t| + 5 / 4)) * Real.exp (-(c / 2) * t ^ 2)
  have hcont : Continuous f := by
    have harg : Continuous fun t : ℝ => 2 + |t| + 5 / 4 := by
      continuity
    have hne : ∀ t : ℝ, 2 + |t| + 5 / 4 ≠ 0 := fun t =>
      ne_of_gt (by nlinarith [abs_nonneg t])
    have hlog : Continuous fun t : ℝ => Real.log (2 + |t| + 5 / 4) :=
      harg.log hne
    have hexp : Continuous fun t : ℝ => Real.exp (-(c / 2) * t ^ 2) := by
      fun_prop
    exact (continuous_const.add hlog).mul hexp
  have htop : Tendsto f atTop (nhds 0) := by
    have h :=
      tendsto_one_add_log_add_mul_gauss (c := c / 2) (b := 13 / 4)
        hc2 (by norm_num)
    refine (h.congr' ?_).trans_eq rfl
    filter_upwards [eventually_ge_atTop (0 : ℝ)] with t ht
    have : 2 + |t| + 5 / 4 = t + 13 / 4 := by
      rw [abs_of_nonneg ht]; ring
    simp [f, this]
  have hbot : Tendsto f atBot (nhds 0) := by
    have h :=
      tendsto_one_add_log_add_mul_gauss (c := c / 2) (b := 13 / 4)
        hc2 (by norm_num)
    have hneg : Tendsto (fun t : ℝ => f (-t)) atTop (nhds 0) := by
      refine (h.congr' ?_).trans_eq rfl
      filter_upwards [eventually_ge_atTop (0 : ℝ)] with t ht
      have : 2 + |t| + 5 / 4 = t + 13 / 4 := by
        rw [abs_of_nonneg ht]; ring
      simp [f, this]
    exact (hneg.comp tendsto_neg_atBot_atTop).congr fun t => by simp [f]
  have hltTop : ∀ᶠ t in atTop, f t < 1 :=
    htop.eventually (Iio_mem_nhds (by norm_num : (0 : ℝ) < 1))
  have hltBot : ∀ᶠ t in atBot, f t < 1 :=
    hbot.eventually (Iio_mem_nhds (by norm_num : (0 : ℝ) < 1))
  obtain ⟨A, hA⟩ := eventually_atTop.mp hltTop
  obtain ⟨B, hB⟩ := eventually_atBot.mp hltBot
  set R : ℝ := max (max A 0) (max (-B) 0)
  obtain ⟨M, hM⟩ :=
    isCompact_Icc.exists_bound_of_continuousOn
      (hcont.continuousOn : ContinuousOn f (Icc (-R) R))
  set K : ℝ := max 1 (|M|)
  have hK0 : 0 ≤ K := le_trans (by norm_num : (0 : ℝ) ≤ 1) (le_max_left _ _)
  refine ⟨K, hK0, fun t => ?_⟩
  have hgoal : f t ≤ K := by
    by_cases ht : |t| ≤ R
    · have htI : t ∈ Icc (-R) R := abs_le.mp ht
      have hfM : |f t| ≤ M := by
        simpa [Real.norm_eq_abs] using hM t htI
      have hMK : M ≤ |M| := le_abs_self M
      have habsK : |M| ≤ K := le_max_right 1 (|M|)
      exact (le_abs_self (f t)).trans (hfM.trans (hMK.trans habsK))
    · have htR : R < |t| := lt_of_not_ge ht
      have hf1 : f t < 1 := by
        rcases le_total t 0 with htn | htp
        · have htneg : t < -R := by
            rw [abs_of_nonpos htn] at htR
            linarith
          exact hB t (htneg.le.trans (le_B_of_neg_max R B (le_max_right _ _)))
        · have htpos : R < t := by
            rwa [abs_of_nonneg htp] at htR
          have hAR : A ≤ R :=
            (le_max_left A 0).trans (le_max_left _ _)
          exact hA t (hAR.trans htpos.le)
      exact hf1.le.trans (le_max_left _ _)
  have hsplit : Real.exp (-c * t ^ 2) =
      Real.exp (-(c / 2) * t ^ 2) * Real.exp (-(c / 2) * t ^ 2) := by
    rw [← Real.exp_add]
    congr 1
    ring
  calc
    (1 + Real.log (2 + |t| + 5 / 4)) * Real.exp (-c * t ^ 2) =
        f t * Real.exp (-(c / 2) * t ^ 2) := by
      unfold f
      rw [hsplit, mul_assoc]
    _ ≤ K * Real.exp (-(c / 2) * t ^ 2) :=
      mul_le_mul_of_nonneg_right hgoal (Real.exp_pos _).le

/-- `m_ρ` is log-bounded on the whole critical strip: the `|Im|≥2`
or `Re≥1/2` case is `riemannZetaMultiplicity_le_log`; the compact
remainder is absorbed into the constant. -/
lemma riemannZetaMultiplicity_le_log_all {z : ℂ}
    (hz : IsCriticalStripZetaZero z) :
    (riemannZetaMultiplicity z : ℝ) ≤
      (zetaZerosInDiskCardBoundInner +
        ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
          (riemannZetaMultiplicity ρ : ℝ)) *
        (1 + Real.log (2 + |z.im| + 5 / 4)) := by
  set S := riemannZetaZerosOnClosedRect 0 1 2
  set M : ℝ := ∑ ρ ∈ S, (riemannZetaMultiplicity ρ : ℝ)
  set C : ℝ := zetaZerosInDiskCardBoundInner + M
  have hM0 : 0 ≤ M :=
    Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _
  have hC0 : 0 ≤ C :=
    add_nonneg (le_of_lt zetaZerosInDiskCardBoundInner_pos) hM0
  have hlog : (1 : ℝ) ≤ 1 + Real.log (2 + |z.im| + 5 / 4) :=
    le_add_of_nonneg_right
      (Real.log_nonneg (by nlinarith [abs_nonneg z.im]))
  by_cases him : (2 : ℝ) ≤ |z.im| ∨ (1 / 2 : ℝ) ≤ z.re
  · have hle := riemannZetaMultiplicity_le_log hz him
    have hC : zetaZerosInDiskCardBoundInner ≤ C :=
      le_add_of_nonneg_right hM0
    exact hle.trans (mul_le_mul_of_nonneg_right hC
      (add_nonneg (by norm_num)
        (Real.log_nonneg (by nlinarith [abs_nonneg z.im]))))
  · have himlt : |z.im| < 2 := by
      rw [not_or] at him
      exact lt_of_not_ge him.1
    have hzS : z ∈ S :=
      mem_rect_of_criticalStrip hz (le_of_lt himlt)
    have hterm : (riemannZetaMultiplicity z : ℝ) ≤ M :=
      Finset.single_le_sum (fun _ _ => Nat.cast_nonneg _) hzS
    have hMC : M ≤ C := le_add_of_nonneg_left
      (le_of_lt zetaZerosInDiskCardBoundInner_pos)
    exact hterm.trans (hMC.trans (le_mul_of_one_le_right hC0 hlog))

lemma exists_mult_gaborHat_gauss_bound
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ ≤
          C * Real.exp (-c * (ρ : ℂ).im ^ 2) := by
  obtain ⟨c, Chat, hc, hChat, hhat⟩ := norm_gaborHat_le_gauss_critical hF
  obtain ⟨K, hK0, hK⟩ := one_add_log_im_mul_gauss_le hc
  set Cm : ℝ :=
    zetaZerosInDiskCardBoundInner +
      ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
        (riemannZetaMultiplicity ρ : ℝ)
  have hCm0 : 0 < Cm :=
    lt_of_lt_of_le zetaZerosInDiskCardBoundInner_pos
      (le_add_of_nonneg_right
        (Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _))
  refine ⟨c / 2, Cm * Chat * K + 1, half_pos hc, by positivity, ?_⟩
  intro ρ
  have hnorm :
      ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ =
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖gaborHat F ρ‖ := by
    rw [norm_mul]
    simp
  have hm := riemannZetaMultiplicity_le_log_all ρ.property
  have hh := hhat ρ ρ.property
  have hlogg := hK (ρ : ℂ).im
  have hprod :
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖gaborHat F ρ‖ ≤
        Cm * Chat * K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) := by
    have h1 := mul_le_mul hm hh (norm_nonneg _)
      (mul_nonneg (le_of_lt hCm0)
        (add_nonneg (by norm_num)
          (Real.log_nonneg (by nlinarith [abs_nonneg (ρ : ℂ).im]))))
    have h2 :
        Cm * (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
            (Chat * Real.exp (-c * (ρ : ℂ).im ^ 2)) =
          Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) := by
      ring
    have h3 :
        Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) ≤
          Cm * Chat * (K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2)) :=
      mul_le_mul_of_nonneg_left hlogg
        (mul_nonneg (le_of_lt hCm0) hChat.le)
    have := (h1.trans_eq h2).trans h3
    simpa [mul_assoc] using this
  have hC :
      Cm * Chat * K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) ≤
        (Cm * Chat * K + 1) * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) :=
    mul_le_mul_of_nonneg_right (le_add_of_nonneg_right (by norm_num))
      (Real.exp_pos _).le
  rw [hnorm]
  exact hprod.trans hC

theorem summable_gaborHat_mult_over_zeros
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ := by
  obtain ⟨c, C, hc, _hC, hbd⟩ := exists_mult_gaborHat_gauss_bound hF
  refine Summable.of_norm
    (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hbd
      ((summable_gauss_over_zeros hc).mul_left C))

/-! ## Interval → improper vertical edges -/

lemma tendsto_gabor_right_edge_interval
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ τ : ℝ in (-T k)..(T k),
        logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          gaborHat F ((2 : ℂ) + τ * I)) atTop
      (𝓝 (∫ τ : ℝ,
        logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          gaborHat F ((2 : ℂ) + τ * I))) :=
  tendsto_intervalIntegral_neg_to _
    (integrable_gabor_right_edge_integrand hF) hT

lemma tendsto_gabor_left_edge_interval
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ τ : ℝ in (-T k)..(T k),
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * I)) atTop
      (𝓝 (∫ τ : ℝ,
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * I))) :=
  tendsto_intervalIntegral_neg_to _
    (integrable_gabor_left_edge_integrand hF) hT

/-! ## Spectral Finset exhaustion along Landau heights -/

lemma tendsto_gabor_spectralPartialSum_tsum
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Tendsto (fun k =>
      spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k)) atTop
      (𝓝 (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ)) := by
  have hsum := (summable_gaborHat_mult_over_zeros hF).hasSum
  have hfin := tendsto_stripZerosBelow_landau hTbd
  have hsub :
      Tendsto (fun k =>
        ∑ ρ ∈ stripZerosBelow (T k),
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) atTop
        (𝓝 (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ)) :=
    hsum.comp hfin
  refine hsub.congr fun k => ?_
  rw [spectralPartialSum_eq_critical (gaborHat F) (by norm_num) (by norm_num),
    spectralPartialSum_eq_subtype]

/-! ## Horizontal vanishing on a fixed Landau sequence -/

lemma gabor_horizontal_edges_along_landau
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1)
    (hgapP : ∀ k : ℕ, ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (ordinateGapConstLandau * (1 + Real.log (T k))) ≤
        |ρ.im - T k|) :
    Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + T k * I) *
          gaborHat F ((x : ℂ) + T k * I)) atTop (nhds 0) ∧
    Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
          gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) 2
  set A : ℝ := ordinateGapConstLandau
  have hA : (1 : ℝ) ≤ A := ordinateGapConstLandau_one_le
  have hσ : (-1 / 16 : ℝ) ≤ (2 : ℝ) := by norm_num
  have hT2 : ∀ k, (2 : ℝ) ≤ T k := landau_gap_T_two_le hTbd
  have hTtop : Tendsto T atTop atTop := landau_gap_T_tendsto hTbd
  set L : ℕ → ℝ := fun k => 1 + Real.log (T k)
  set B : ℕ → ℝ := fun k => A * sliverEdgeConst * L k ^ 3
  have hB0 : ∀ k, 0 ≤ B k := fun k => by
    have hLk : 0 ≤ L k :=
      add_nonneg (by norm_num)
        (Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) (hT2 k)))
    exact mul_nonneg (mul_nonneg
      (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA) sliverEdgeConst_nonneg)
      (pow_nonneg hLk 3)
  set K : ℝ := (2 + 1 / 16 : ℝ) * A * sliverEdgeConst * C
  have hlen : (2 : ℝ) - (-1 / 16) = 2 + 1 / 16 := by ring
  have hedge (τ : ℕ → ℝ) (hτ : ∀ k, |τ k| = T k) (k : ℕ) :
      ‖∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + τ k * I) *
            gaborHat F ((x : ℂ) + τ k * I)‖ ≤
        K * (L k ^ 3 * Real.exp (-c * T k ^ 2)) := by
    have hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (A * (1 + Real.log (T k))) ≤ |ρ.im - T k| := hgapP k
    have hbdζ : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
        ‖logDeriv riemannZeta ((σ : ℂ) + τ k * I)‖ ≤ B k :=
      fun σ hσs => horizontalEdgeBound_glued hA (hT2 k) hgap
        hσs.1 hσs.2 (hτ k)
    have hnz : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
        riemannZeta ((σ : ℂ) + τ k * I) ≠ 0 :=
      fun σ hσs => riemannZeta_ne_zero_of_glued_gap hA (hT2 k) hgap
        hσs.1 hσs.2 (hτ k)
    have hne1 : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
        (σ : ℂ) + τ k * I ≠ 1 :=
      fun _ _ => horizontal_ne_one_of_abs (hT2 k) (hτ k)
    have hhatτ : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
        ‖gaborHat F ((σ : ℂ) + τ k * I)‖ ≤
          C * Real.exp (-c * τ k ^ 2) :=
      fun σ hσs => hhat σ (τ k) hσs.1 hσs.2
    have hle :=
      norm_horizontal_logDeriv_gaborHat_integral_le F hσ (hB0 k)
        hC.le hc.le hne1 hnz hbdζ hhatτ
    have hsq : τ k ^ 2 = T k ^ 2 := by
      have : |τ k| ^ 2 = T k ^ 2 := by simp [hτ]
      simpa [sq_abs] using this
    convert hle using 1
    unfold B L K
    rw [hsq, hlen]
    ring
  have hdecay : Tendsto
      (fun k => L k ^ 3 * Real.exp (-c * T k ^ 2)) atTop (nhds 0) :=
    (tendsto_log_pow_mul_gauss hc).comp hTtop
  have hpos := hedge (fun k => T k)
    (fun k => abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k)))
  have hneg := hedge (fun k => -(T k)) (fun k => by
    simp [abs_neg, abs_of_nonneg
      (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k))])
  have hnorm {Iint : ℕ → ℂ}
      (hle : ∀ k, ‖Iint k‖ ≤ K * (L k ^ 3 * Real.exp (-c * T k ^ 2))) :
      Tendsto Iint atTop (nhds 0) :=
    tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero (fun _ => norm_nonneg _) hle (by
        convert hdecay.const_mul K
        rw [mul_zero]))
  exact ⟨hnorm hpos, hnorm hneg⟩

/-! ## Rectangle unfolding -/

lemma rectangleIntegral_logDeriv_gaborHat (F : GaborWeilTest) (T : ℝ) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
    (∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (-T : ℝ) * I) *
          gaborHat F ((x : ℂ) + (-T : ℝ) * I)) -
    (∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (T : ℝ) * I) *
          gaborHat F ((x : ℂ) + (T : ℝ) * I)) +
    I • (∫ y : ℝ in (-T)..T,
        logDeriv riemannZeta ((2 : ℂ) + y * I) *
          gaborHat F ((2 : ℂ) + y * I)) -
    I • (∫ y : ℝ in (-T)..T,
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + y * I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I)) := by
  unfold rectangleIntegral
  simp

/-! ## Assembly -/

/-- r576: the Gabor contour identity along Landau gaps.  The
statement of `GaborContourVerticalLimit` is the same improper
identity as the compact-class `ContourIdentityLimitAlongGaps`;
no reordering of limits is required. -/
theorem gaborContourVerticalLimit_holds :
    GaborContourVerticalLimit := by
  intro F hF
  obtain ⟨T, hTbd, hgapP, hgapN⟩ := exists_gap_sequence_landau
  obtain ⟨hTop, hBot⟩ :=
    gabor_horizontal_edges_along_landau hF hTbd hgapP
  have hT2 := landau_gap_T_two_le hTbd
  have hTpos : ∀ k, (0 : ℝ) < T k :=
    fun k => lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) (hT2 k)
  have hTtop := landau_gap_T_tendsto hTbd
  have hA0 : (0 : ℝ) < ordinateGapConstLandau :=
    lt_of_lt_of_le (by norm_num) ordinateGapConstLandau_one_le
  have hord : ∀ k, ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 (T k),
      |ρ.im| < T k :=
    fun k ρ hρ =>
      abs_im_lt_of_landau_gaps hA0 (hT2 k) (hgapP k) (hgapN k) hρ
  have hid : ∀ k,
      rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
        (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
        (((2 : ℝ) : ℂ) + (T k : ℝ) * I) =
        (2 * (Real.pi : ℂ) * I) *
          (spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k) -
            gaborHat F 1) :=
    fun k => gabor_contour_identity_fixed_T F (hTpos k) (hord k)
  have hright := tendsto_gabor_right_edge_interval hF hTtop
  have hleft := tendsto_gabor_left_edge_interval hF hTtop
  have hspec := tendsto_gabor_spectralPartialSum_tsum hF hTbd
  have hsides :
      Tendsto (fun k =>
        (∫ x : ℝ in (-1 / 16 : ℝ)..2,
            logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
              gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) -
        (∫ x : ℝ in (-1 / 16 : ℝ)..2,
            logDeriv riemannZeta ((x : ℂ) + (T k : ℝ) * I) *
              gaborHat F ((x : ℂ) + (T k : ℝ) * I)) +
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv riemannZeta ((2 : ℂ) + y * I) *
              gaborHat F ((2 : ℂ) + y * I)) -
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + y * I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I))) atTop
        (𝓝 (I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
              gaborHat F ((2 : ℂ) + τ * I)) -
            I • (∫ τ : ℝ, logDeriv riemannZeta
              (((-1 / 16 : ℝ) : ℂ) + τ * I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * I)))) := by
    convert ((hBot.sub hTop).add (hright.const_smul I)).sub
      (hleft.const_smul I) using 1
    simp
  have hrect :
      Tendsto (fun k =>
        rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
          (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
          (((2 : ℝ) : ℂ) + (T k : ℝ) * I)) atTop
        (𝓝 (I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
              gaborHat F ((2 : ℂ) + τ * I)) -
            I • (∫ τ : ℝ, logDeriv riemannZeta
              (((-1 / 16 : ℝ) : ℂ) + τ * I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + τ * I)))) :=
    hsides.congr fun k => (rectangleIntegral_logDeriv_gaborHat F (T k)).symm
  have hspec' :
      Tendsto (fun k =>
        (2 * (Real.pi : ℂ) * I) *
          (spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k) -
            gaborHat F 1)) atTop
        (𝓝 ((2 * (Real.pi : ℂ) * I) *
          ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) -
            gaborHat F 1))) :=
    (hspec.sub tendsto_const_nhds).const_mul _
  exact tendsto_nhds_unique (hrect.congr hid) hspec'

/-- The r557 named remainder is the same Landau exhaustion. -/
theorem gaborContourLimitRemainder_holds :
    GaborContourLimitRemainder := by
  intro F hF
  obtain ⟨T, hTbd, hgapP, hgapN⟩ := exists_gap_sequence_landau
  have hT2 := landau_gap_T_two_le hTbd
  have hTpos : ∀ k, (0 : ℝ) < T k :=
    fun k => lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) (hT2 k)
  have hTtop := landau_gap_T_tendsto hTbd
  have hA0 : (0 : ℝ) < ordinateGapConstLandau :=
    lt_of_lt_of_le (by norm_num) ordinateGapConstLandau_one_le
  have hord : ∀ k, ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 (T k),
      |ρ.im| < T k :=
    fun k ρ hρ =>
      abs_im_lt_of_landau_gaps hA0 (hT2 k) (hgapP k) (hgapN k) hρ
  exact ⟨T, hTtop, hTpos, hord,
    tendsto_gabor_spectralPartialSum_tsum hF hTbd⟩

#print axioms gaborContourVerticalLimit_holds
#print axioms gaborContourLimitRemainder_holds
#print axioms summable_gaborHat_mult_over_zeros

end RH
