/-
RH/GaborHorizontalEdges.lean -- r557 brick: horizontal contour edges
for `(ζ′/ζ) ĥ_W` die along the Landau gap sequence.

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free decay of the two horizontal
sides of `[-1/16, 2] × [-T, T]`.  This file does not prove
`GaborExplicitFormula`.

The `ζ′/ζ` factor uses the glued Landau/sliver bound
`horizontalEdgeBound_glued` (valid on the gap sequence, including the
sliver `Re < 1/2`).  The hat factor uses the r555 Gaussian strip
bound, available for pure packets.  The general-quartic edge decay
is a named unasserted remainder, not a `sorry`.
-/
import RH.GaborHatAnalytic
import RH.GaborZeroSummable
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

namespace RH

open Complex Filter Function Set MeasureTheory
open scoped Topology Interval

/-- Horizontal edge of `(ζ′/ζ) ĥ_W` with a Gaussian hat majorant. -/
lemma norm_horizontal_logDeriv_gaborHat_integral_le
    (F : GaborWeilTest)
    {σ₁ σ₂ τ B C c : ℝ}
    (hσ : σ₁ ≤ σ₂) (hB : 0 ≤ B) (_hC0 : 0 ≤ C) (_hc : 0 ≤ c)
    (hne1 : ∀ σ, σ ∈ Icc σ₁ σ₂ → (σ : ℂ) + τ * I ≠ 1)
    (hnz : ∀ σ, σ ∈ Icc σ₁ σ₂ → riemannZeta ((σ : ℂ) + τ * I) ≠ 0)
    (hbd : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤ B)
    (hhat : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖gaborHat F ((σ : ℂ) + τ * I)‖ ≤ C * Real.exp (-c * τ ^ 2)) :
    ‖∫ x : ℝ in σ₁..σ₂,
        logDeriv riemannZeta ((x : ℂ) + τ * I) *
          gaborHat F ((x : ℂ) + τ * I)‖ ≤
      (σ₂ - σ₁) * B * C * Real.exp (-c * τ ^ 2) := by
  set f : ℝ → ℂ := fun x =>
    logDeriv riemannZeta ((x : ℂ) + τ * I) *
      gaborHat F ((x : ℂ) + τ * I)
  have hpathOn : ContinuousOn (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂) :=
    continuous_ofReal.continuousOn.add continuousOn_const
  have hlogOn : ContinuousOn (logDeriv riemannZeta)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := hz
    exact (analyticAt_logDeriv_riemannZeta (hne1 x hx)
      (hnz x hx)).continuousAt.continuousWithinAt
  have hFOn : ContinuousOn (gaborHat F)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    fun _ _ => (analyticAt_gaborHat F _).continuousAt.continuousWithinAt
  have hmaps : Set.MapsTo (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    Set.mapsTo_image _ _
  have hcont : ContinuousOn f (Icc σ₁ σ₂) :=
    (hlogOn.comp hpathOn hmaps).mul (hFOn.comp hpathOn hmaps)
  have hf : IntervalIntegrable f volume σ₁ σ₂ :=
    hcont.intervalIntegrable_of_Icc hσ
  have hbound : ∀ x, σ₁ ≤ x → x ≤ σ₂ →
      ‖f x‖ ≤ B * C * Real.exp (-c * τ ^ 2) := by
    intro x hx1 hx2
    have hx : x ∈ Icc σ₁ σ₂ := ⟨hx1, hx2⟩
    have hζ := hbd x hx
    have hh := hhat x hx
    dsimp [f]
    rw [norm_mul]
    have := mul_le_mul hζ hh (norm_nonneg _) hB
    simpa [mul_assoc] using this
  have hle := norm_intervalIntegral_le_length_mul hσ hf hbound
  have : (σ₂ - σ₁) * (B * C * Real.exp (-c * τ ^ 2)) =
      (σ₂ - σ₁) * B * C * Real.exp (-c * τ ^ 2) := by ring
  exact hle.trans_eq this

/-- `t² exp(-c t²) → 0` at `+∞`. -/
lemma tendsto_sq_mul_exp_neg_sq {c : ℝ} (hc : 0 < c) :
    Tendsto (fun t : ℝ => t ^ 2 * Real.exp (-c * t ^ 2))
      atTop (nhds 0) := by
  have hpow := Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero 1
  have hscale : Tendsto (fun t : ℝ => c * t ^ 2) atTop atTop :=
    (tendsto_pow_atTop (by norm_num : (2 : ℕ) ≠ 0)).const_mul_atTop hc
  have hcomp : Tendsto
      (fun t : ℝ => (c * t ^ 2) * Real.exp (-(c * t ^ 2)))
      atTop (nhds 0) := by
    convert hpow.comp hscale using 1
    ext t
    simp
  have hconst := hcomp.const_mul (1 / c)
  convert hconst using 1
  ext t
  field_simp [hc.ne']
  ring

lemma tendsto_exp_neg_sq {c : ℝ} (hc : 0 < c) :
    Tendsto (fun t : ℝ => Real.exp (-c * t ^ 2)) atTop (nhds 0) := by
  have hscale : Tendsto (fun t : ℝ => c * t ^ 2) atTop atTop :=
    (tendsto_pow_atTop (by norm_num : (2 : ℕ) ≠ 0)).const_mul_atTop hc
  convert Real.tendsto_exp_neg_atTop_nhds_zero.comp hscale using 1
  ext t
  simp

lemma tendsto_log_pow_mul_gauss {c : ℝ} (hc : 0 < c) :
    Tendsto (fun t : ℝ => (1 + Real.log t) ^ 3 * Real.exp (-c * t ^ 2))
      atTop (nhds 0) := by
  have hfrac := tendsto_one_add_log_cubed_div_one_add_sq
  have hsq := tendsto_sq_mul_exp_neg_sq hc
  have h1 := tendsto_exp_neg_sq hc
  have hprod := hfrac.mul (hsq.add h1)
  refine (hprod.congr' ?_).trans_eq (by simp)
  filter_upwards [eventually_gt_atTop (0 : ℝ)] with t ht
  have hden : 1 + t ^ 2 ≠ 0 := by positivity
  field_simp [hden]
  ring

/-- Horizontal edges of `(ζ′/ζ) ĥ_W` along the Landau gap sequence. -/
def GaborHorizontalEdgesTendstoZero : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 1 : ℕ) : ℝ) ≤ T k) ∧
      Tendsto T atTop atTop ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + T k * I) *
            gaborHat F ((x : ℂ) + T k * I)) atTop (nhds 0) ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
            gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0)

theorem gabor_horizontal_edges_tendsto_zero :
    GaborHorizontalEdgesTendstoZero := by
  intro F hFpure
  obtain ⟨T, hTbd, hgapP, _hgapN⟩ := exists_gap_sequence_landau
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hFpure (-1 / 16) 2
  set A : ℝ := ordinateGapConstLandau
  have hA : (1 : ℝ) ≤ A := ordinateGapConstLandau_one_le
  have hσ : (-1 / 16 : ℝ) ≤ (2 : ℝ) := by norm_num
  have hT2 : ∀ k, (2 : ℝ) ≤ T k := fun k =>
    le_trans (by norm_num : (2 : ℝ) ≤ 3)
      (le_trans (by exact_mod_cast
        (Nat.le_add_left 3 (2 * k) : 3 ≤ 2 * k + 3)) (hTbd k).1)
  have hTlo : ∀ k, ((2 * k + 1 : ℕ) : ℝ) ≤ T k := fun k =>
    le_trans (by exact_mod_cast
      (Nat.le_add_right (2 * k + 1) 2 : 2 * k + 1 ≤ 2 * k + 3))
      (hTbd k).1
  have hTtop : Tendsto T atTop atTop :=
    tendsto_atTop_mono (fun k =>
      le_trans (by exact_mod_cast (by omega : k ≤ 2 * k + 3)) (hTbd k).1)
      tendsto_natCast_atTop_atTop
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
  have hK0 : 0 ≤ K :=
    mul_nonneg (mul_nonneg (mul_nonneg (by norm_num)
      (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA)) sliverEdgeConst_nonneg) hC.le
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
  have hnorm {I : ℕ → ℂ}
      (hle : ∀ k, ‖I k‖ ≤ K * (L k ^ 3 * Real.exp (-c * T k ^ 2))) :
      Tendsto I atTop (nhds 0) :=
    tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero (fun _ => norm_nonneg _) hle (by
        convert hdecay.const_mul K
        rw [mul_zero]))
  refine ⟨T, hTlo, hTtop, hnorm hpos, hnorm hneg⟩

/-- Named remainder: the same horizontal vanishing for a general even
quartic, once the coefficient-dependent strip majorant is available.
Unasserted.  Not a `sorry`. -/
def GaborHatQuarticHorizontalEdgesRemainder : Prop :=
  ∀ F : GaborWeilTest,
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 1 : ℕ) : ℝ) ≤ T k) ∧
      Tendsto T atTop atTop ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + T k * I) *
            gaborHat F ((x : ℂ) + T k * I)) atTop (nhds 0) ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
            gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0)

end RH
