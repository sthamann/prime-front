/-
RH/GaborArchContour.lean -- r578 contour shift of χ′/χ from the
left edge Re = −1/16 onto the critical line.  r581: T→∞ glue.

CLAIM BOUNDARY.  NO RH CLAIM.  Rectangle/T→∞ glue for the
archimedean clamp: the unique strip singularity of χ′/χ on
−1/16 ≤ Re ≤ 1/2 is the simple pole at s = 0 coming from Γℝ(s)
(residue −1).  Γℝ(1−s) poles / cos-zeros sit at odd integers
Re ≥ 1, outside the strip.  Horizontal edges decay as Gauss×log.
-/
import RH.GaborArchDigamma
import RH.GaborVerticalLimit

namespace RH

open Complex Filter Function MeasureTheory Set
open scoped Topology Interval

/-! ## Holomorphic remainder after the pole at `s = 0` -/

noncomputable def zetaFEFactorLogDerivHol (s : ℂ) : ℂ :=
  -Complex.log (2 * (Real.pi : ℂ)) + digamma (s + 1)
    - ((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)

lemma logDeriv_zetaFEFactor_pole_split {s : ℂ}
    (hG : ∀ n : ℕ, s ≠ -n)
    (hcos : cos (Real.pi * s / 2) ≠ 0) :
    logDeriv zetaFEFactor s =
      -s⁻¹ + zetaFEFactorLogDerivHol s := by
  have hrec := digamma_apply_add_one s hG
  rw [logDeriv_zetaFEFactor hG hcos]
  unfold zetaFEFactorLogDerivHol
  rw [hrec]
  ring

noncomputable def zetaFEFactorLogDerivHatHol (F : GaborWeilTest) (s : ℂ) : ℂ :=
  zetaFEFactorLogDerivHol s * gaborHat F s - dslope (gaborHat F) 0 s

lemma logDeriv_zetaFEFactor_mul_hat_pole_split
    (F : GaborWeilTest) {s : ℂ}
    (hG : ∀ n : ℕ, s ≠ -n)
    (hcos : cos (Real.pi * s / 2) ≠ 0) :
    logDeriv zetaFEFactor s * gaborHat F s =
      (-gaborHat F 0) / s + zetaFEFactorLogDerivHatHol F s := by
  have h0 : s ≠ 0 := by
    simpa using hG 0
  have hsplit := logDeriv_zetaFEFactor_pole_split hG hcos
  have hslope : dslope (gaborHat F) 0 s =
      (gaborHat F s - gaborHat F 0) / s := by
    rw [dslope_of_ne (gaborHat F) h0]
    simp [slope, vsub_eq_sub, smul_eq_mul, sub_zero, div_eq_mul_inv, mul_comm]
  unfold zetaFEFactorLogDerivHatHol
  rw [hsplit, add_mul, hslope]
  field_simp [h0]
  ring

/-! ## Open strip containing the closed Gabor arch rectangle -/

def archStrip : Set ℂ :=
  {z : ℂ | (-1 / 8 : ℝ) < z.re ∧ z.re < (5 / 8 : ℝ)}

lemma isOpen_archStrip : IsOpen archStrip :=
  (isOpen_lt continuous_const continuous_re).inter
    (isOpen_lt continuous_re continuous_const)

lemma mem_archStrip_of_re_bounds {s : ℂ}
    (h1 : (-1 / 16 : ℝ) ≤ s.re) (h2 : s.re ≤ (1 / 2 : ℝ)) :
    s ∈ archStrip :=
  ⟨by linarith, by linarith⟩

lemma ne_neg_nat_of_mem_archStrip_ne_zero {s : ℂ}
    (hs : s ∈ archStrip) (h0 : s ≠ 0) (n : ℕ) : s ≠ -n := by
  cases n with
  | zero => simpa using h0
  | succ k =>
    intro h
    have hre : s.re = -((k + 1 : ℕ) : ℝ) := by
      simpa using congrArg Complex.re h
    have : (-1 / 8 : ℝ) < s.re := hs.1
    have : (1 : ℝ) ≤ (k + 1 : ℕ) := by exact_mod_cast Nat.succ_pos k
    linarith

lemma cos_pi_div_two_ne_zero_of_mem_archStrip {s : ℂ}
    (hs : s ∈ archStrip) :
    cos (Real.pi * s / 2) ≠ 0 := by
  intro hcos
  obtain ⟨n, hn⟩ := cos_eq_zero_iff.mp hcos
  have hπ : (Real.pi : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
  have hsodd : s = (2 * (n : ℂ) + 1) := by
    have := congrArg (fun z : ℂ => 2 * z / Real.pi) hn
    field_simp [hπ] at this
    exact this
  have hre : s.re = 2 * (n : ℝ) + 1 := by
    simp [hsodd]
  have h1 : (-1 / 8 : ℝ) < s.re := hs.1
  have h2 : s.re < (5 / 8 : ℝ) := hs.2
  cases lt_or_ge n (0 : ℤ) with
  | inl hlt =>
    have : n ≤ (-1 : ℤ) := Int.le_sub_one_of_lt hlt
    have : (n : ℝ) ≤ -1 := by exact_mod_cast this
    linarith
  | inr hge =>
    have : (0 : ℝ) ≤ n := by exact_mod_cast hge
    linarith

/-! ## Holomorphy of the remainder on the open strip -/

lemma re_add_one_pos_of_mem_archStrip {s : ℂ} (hs : s ∈ archStrip) :
    0 < (s + 1).re := by
  have : (-1 / 8 : ℝ) < s.re := hs.1
  simp [add_re]
  linarith

lemma differentiableOn_zetaFEFactorLogDerivHol :
    DifferentiableOn ℂ zetaFEFactorLogDerivHol archStrip := by
  intro s hs
  have hψ : DifferentiableAt ℂ (fun z : ℂ => digamma (z + 1)) s :=
    (analyticOnNhd_digamma_re_pos (s + 1)
      (re_add_one_pos_of_mem_archStrip hs)).differentiableAt.comp
      s (differentiableAt_id.add_const 1)
  have htan : DifferentiableAt ℂ (fun z : ℂ => tan (Real.pi * z / 2)) s := by
    change DifferentiableAt ℂ (tan ∘ fun w : ℂ => Real.pi * w / 2) s
    exact (differentiableAt_tan.mpr
        (cos_pi_div_two_ne_zero_of_mem_archStrip hs)).comp
      s (hasDerivAt_pi_mul_div_two s).differentiableAt
  have hconst :
      DifferentiableAt ℂ (fun _ : ℂ => -Complex.log (2 * (Real.pi : ℂ))) s :=
    differentiableAt_const _
  have hπ : DifferentiableAt ℂ
      (fun z : ℂ => ((Real.pi : ℂ) / 2) * tan (Real.pi * z / 2)) s :=
    (differentiableAt_const _).mul htan
  exact ((hconst.add hψ).sub hπ).differentiableWithinAt

lemma differentiableOn_zetaFEFactorLogDerivHatHol (F : GaborWeilTest) :
    DifferentiableOn ℂ (zetaFEFactorLogDerivHatHol F) archStrip :=
  (differentiableOn_zetaFEFactorLogDerivHol.mul
      ((differentiable_gaborHat F).differentiableOn.mono (subset_univ _))).sub
    (((Complex.differentiableOn_dslope (s := univ) univ_mem).mpr
        (differentiable_gaborHat F).differentiableOn).mono (subset_univ _))

lemma re_of_mem_reProdIm {z w s : ℂ}
    (hre : z.re ≤ w.re)
    (hs : s ∈ [[z.re, w.re]] ×ℂ [[z.im, w.im]]) :
    z.re ≤ s.re ∧ s.re ≤ w.re := by
  have hu : s.re ∈ [[z.re, w.re]] := (mem_reProdIm.mp hs).1
  simpa [uIcc_of_le hre] using hu

lemma differentiableOn_hatHol_rect (F : GaborWeilTest) (z w : ℂ)
    (hz : z ∈ archStrip) (hw : w ∈ archStrip)
    (hre : z.re ≤ w.re) :
    DifferentiableOn ℂ (zetaFEFactorLogDerivHatHol F)
      ([[z.re, w.re]] ×ℂ [[z.im, w.im]]) := by
  refine (differentiableOn_zetaFEFactorLogDerivHatHol F).mono ?_
  intro s hs
  obtain ⟨hre1, hre2⟩ := re_of_mem_reProdIm hre hs
  exact ⟨lt_of_lt_of_le hz.1 hre1, lt_of_le_of_lt hre2 hw.2⟩

/-! ## Fixed-`T` rectangle identity -/

lemma side_mem_archStrip_of_re {σ τ : ℝ}
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ (1 / 2 : ℝ)) :
    ((σ : ℂ) + τ * I) ∈ archStrip :=
  mem_archStrip_of_re_bounds (by simpa) (by simpa using hσ2)

lemma logDeriv_mul_hat_eq_pole_split_of_mem
    (F : GaborWeilTest) {s : ℂ}
    (hs : s ∈ archStrip) (h0 : s ≠ 0) :
    logDeriv zetaFEFactor s * gaborHat F s =
      (-gaborHat F 0) / s + zetaFEFactorLogDerivHatHol F s :=
  logDeriv_zetaFEFactor_mul_hat_pole_split F
    (ne_neg_nat_of_mem_archStrip_ne_zero hs h0)
    (cos_pi_div_two_ne_zero_of_mem_archStrip hs)

lemma rectangleIntegral_arch_fe_hat (F : GaborWeilTest) {T : ℝ}
    (hT : (0 : ℝ) < T) :
    rectangleIntegral
        (fun ζ => logDeriv zetaFEFactor ζ * gaborHat F ζ)
        (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
        (((1 / 2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) * (-gaborHat F 0) := by
  set z : ℂ := ((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I
  set w : ℂ := ((1 / 2 : ℝ) : ℂ) + (T : ℝ) * I
  have hzre : z.re = -1 / 16 := by simp [z]
  have hwre : w.re = 1 / 2 := by simp [w]
  have hzim : z.im = -T := by simp [z]
  have hwim : w.im = T := by simp [w]
  have hzS : z ∈ archStrip :=
    mem_archStrip_of_re_bounds (by simp [z]) (by
      have : z.re = -1 / 16 := by simp [z]
      rw [this]; norm_num)
  have hwS : w ∈ archStrip :=
    mem_archStrip_of_re_bounds (by
      have : w.re = 1 / 2 := by simp [w]
      rw [this]; norm_num) (by simp [w])
  have hre : z.re ≤ w.re := by simp [hzre, hwre]; norm_num
  have hh := differentiableOn_hatHol_rect F z w hzS hwS hre
  have hpole :=
    rectangleIntegral_simple_pole (zetaFEFactorLogDerivHatHol F) z w 0
      (-gaborHat F 0) hh
      (by have : z.re = -1 / 16 := hzre; rw [this]; norm_num)
      (by have : w.re = 1 / 2 := hwre; rw [this]; norm_num)
      (by
        have hz : z.im = -T := hzim
        have h0 : (0 : ℂ).im = 0 := rfl
        rw [hz, h0]; linarith)
      (by
        have hw : w.im = T := hwim
        have h0 : (0 : ℂ).im = 0 := rfl
        rw [hw, h0]; linarith)
  have hcongr :
      rectangleIntegral
          (fun ζ => logDeriv zetaFEFactor ζ * gaborHat F ζ) z w =
        rectangleIntegral
          (fun ζ => (-gaborHat F 0) / (ζ - 0) +
            zetaFEFactorLogDerivHatHol F ζ) z w := by
    refine rectangleIntegral_congr_sides _ _ z w ?bot ?top ?right ?left
    · intro x hx
      have hxI : x ∈ Icc z.re w.re := by simpa [uIcc_of_le hre] using hx
      have hmem := side_mem_archStrip_of_re (σ := x) (τ := z.im)
        (by linarith [hzre, hxI.1]) (by linarith [hwre, hxI.2])
      have h0 : (x : ℂ) + z.im * I ≠ 0 :=
        add_I_mul_ne_zero (by simp [hzim]; linarith)
      simpa [sub_zero] using logDeriv_mul_hat_eq_pole_split_of_mem F hmem h0
    · intro x hx
      have hxI : x ∈ Icc z.re w.re := by simpa [uIcc_of_le hre] using hx
      have hmem := side_mem_archStrip_of_re (σ := x) (τ := w.im)
        (by linarith [hzre, hxI.1]) (by linarith [hwre, hxI.2])
      have h0 : (x : ℂ) + w.im * I ≠ 0 :=
        add_I_mul_ne_zero (by simp [hwim]; linarith)
      simpa [sub_zero] using logDeriv_mul_hat_eq_pole_split_of_mem F hmem h0
    · intro y _hy
      have hmem : ((w.re : ℂ) + y * I) ∈ archStrip :=
        mem_archStrip_of_re_bounds
          (by have : w.re = 1 / 2 := hwre; rw [this]; norm_num)
          (by simp [hwre])
      have h0 : (w.re : ℂ) + y * I ≠ 0 := by
        intro h
        have hre0 : w.re = 0 := by simpa using congrArg Complex.re h
        have : (1 / 2 : ℝ) ≠ 0 := one_div_ne_zero two_ne_zero
        exact this (hwre ▸ hre0)
      simpa [sub_zero] using logDeriv_mul_hat_eq_pole_split_of_mem F hmem h0
    · intro y _hy
      have hmem : ((z.re : ℂ) + y * I) ∈ archStrip :=
        mem_archStrip_of_re_bounds (by simp [hzre])
          (by have : z.re = -1 / 16 := hzre; rw [this]; norm_num)
      have h0 : (z.re : ℂ) + y * I ≠ 0 := by
        intro h
        have hre0 : z.re = 0 := by simpa using congrArg Complex.re h
        have : (-1 / 16 : ℝ) ≠ 0 := by norm_num
        exact this (hzre ▸ hre0)
      simpa [sub_zero] using logDeriv_mul_hat_eq_pole_split_of_mem F hmem h0
  rw [hcongr, hpole]

lemma rectangleIntegral_arch_fe_hat_unfold (F : GaborWeilTest) (T : ℝ) :
    rectangleIntegral
        (fun ζ => logDeriv zetaFEFactor ζ * gaborHat F ζ)
        (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
        (((1 / 2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + (-T : ℝ) * I) *
            gaborHat F ((x : ℂ) + (-T : ℝ) * I)) -
      (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + (T : ℝ) * I) *
            gaborHat F ((x : ℂ) + (T : ℝ) * I)) +
      I • (∫ y : ℝ in (-T)..T,
          logDeriv zetaFEFactor (((1 / 2 : ℝ) : ℂ) + y * I) *
            gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I)) -
      I • (∫ y : ℝ in (-T)..T,
          logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + y * I) *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I)) := by
  unfold rectangleIntegral
  simp

#print axioms logDeriv_zetaFEFactor_pole_split
#print axioms rectangleIntegral_arch_fe_hat

/-! ## Holomorphy of `χ′/χ` on `|Im| ≥ 2` -/

lemma isOpen_im_ne_zero : IsOpen {z : ℂ | z.im ≠ 0} :=
  isOpen_compl_singleton.preimage continuous_im

lemma analyticOnNhd_zetaFEFactor_im_ne_zero :
    AnalyticOnNhd ℂ zetaFEFactor {z : ℂ | z.im ≠ 0} :=
  DifferentiableOn.analyticOnNhd
    (fun _w hw =>
      (differentiableAt_zetaFEFactor
        (ne_neg_nat_of_im_ne_zero hw)).differentiableWithinAt)
    isOpen_im_ne_zero

lemma analyticAt_zetaFEFactor_of_two_le_abs_im {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) :
    AnalyticAt ℂ zetaFEFactor s :=
  analyticOnNhd_zetaFEFactor_im_ne_zero s (by
    intro hz
    simp [hz] at h
    linarith)

lemma analyticAt_logDeriv_zetaFEFactor_of_two_le_abs_im {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) :
    AnalyticAt ℂ (logDeriv zetaFEFactor) s :=
  (analyticAt_zetaFEFactor_of_two_le_abs_im h).deriv.div
    (analyticAt_zetaFEFactor_of_two_le_abs_im h)
    (zetaFEFactor_ne_zero_of_two_le_abs_im h)

/-! ## Log-majorant of `χ′/χ` on the sliver `|Im| ≥ 2` -/

lemma norm_logDeriv_zetaFEFactor_of_sliver {s : ℂ}
    (hre1 : (-1 / 16 : ℝ) ≤ s.re) (hre2 : s.re ≤ (1 / 2 : ℝ))
    (him : (2 : ℝ) ≤ |s.im|) :
    ‖logDeriv zetaFEFactor s‖ ≤
      (6 + |Real.eulerMascheroniConstant|) * (1 + Real.log (2 + |s.im|)) +
        (Real.log (2 * Real.pi) + 1 / 2 +
          (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)) := by
  have hG : ∀ n : ℕ, s ≠ -n := ne_neg_nat_of_two_le_abs_im him
  have hcos := cos_pi_div_two_ne_zero_of_two_le_abs_im him
  have hFE := logDeriv_zetaFEFactor hG hcos
  have hψ := norm_digamma_le_log_of_sliver hre1 hre2 him
  have htan :=
    norm_tan_le_of_two_le_abs_im (z := Real.pi * s / 2)
      (two_le_abs_im_pi_div_two him)
  have hπtan : ‖((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ ≤
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2) := by
    have hπ : ‖(Real.pi : ℂ)‖ = Real.pi := by
      simp [Complex.norm_real, abs_of_pos Real.pi_pos]
    have h2 : ‖(2 : ℂ)‖ = 2 := by norm_num
    rw [norm_mul, norm_div, hπ, h2]
    exact mul_le_mul_of_nonneg_left htan
      (div_nonneg Real.pi_pos.le (by norm_num))
  rw [hFE]
  have hsplit :
      ‖-Complex.log (2 * (Real.pi : ℂ)) + digamma s
          - ((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ ≤
        ‖Complex.log (2 * (Real.pi : ℂ))‖ + ‖digamma s‖ +
          ‖((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ := by
    refine (norm_sub_le _ _).trans ?_
    gcongr
    simpa using
      norm_add_le (-Complex.log (2 * (Real.pi : ℂ))) (digamma s)
  refine hsplit.trans ?_
  rw [norm_log_two_pi]
  nlinarith [hψ, hπtan]

/-! ## Horizontal Gauss×log vanishing -/

lemma continuousOn_arch_horizontal_integrand
    (F : GaborWeilTest) {σ₁ σ₂ τ : ℝ} (hτ : (2 : ℝ) ≤ |τ|) :
    ContinuousOn (fun x : ℝ =>
      logDeriv zetaFEFactor ((x : ℂ) + τ * I) *
        gaborHat F ((x : ℂ) + τ * I)) (Icc σ₁ σ₂) := by
  have hpath : ContinuousOn (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂) :=
    continuous_ofReal.continuousOn.add continuousOn_const
  have hlog : ContinuousOn (logDeriv zetaFEFactor)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) := by
    intro z hz
    obtain ⟨x, _hx, rfl⟩ := hz
    have him : (2 : ℝ) ≤ |((x : ℂ) + τ * I).im| := by simpa
    exact (analyticAt_logDeriv_zetaFEFactor_of_two_le_abs_im him).continuousAt
      |>.continuousWithinAt
  have hFOn : ContinuousOn (gaborHat F)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    fun _ _ => (analyticAt_gaborHat F _).continuousAt.continuousWithinAt
  exact (hlog.comp hpath (Set.mapsTo_image _ _)).mul
    (hFOn.comp hpath (Set.mapsTo_image _ _))

lemma norm_arch_horizontal_edge_le
    (F : GaborWeilTest) {σ₁ σ₂ τ B C c : ℝ}
    (hσ : σ₁ ≤ σ₂) (hB : 0 ≤ B) (_hC0 : 0 ≤ C) (_hc : 0 ≤ c)
    (hbd : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖logDeriv zetaFEFactor ((σ : ℂ) + τ * I)‖ ≤ B)
    (hhat : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖gaborHat F ((σ : ℂ) + τ * I)‖ ≤ C * Real.exp (-c * τ ^ 2))
    (hτ : (2 : ℝ) ≤ |τ|) :
    ‖∫ x : ℝ in σ₁..σ₂,
        logDeriv zetaFEFactor ((x : ℂ) + τ * I) *
          gaborHat F ((x : ℂ) + τ * I)‖ ≤
      (σ₂ - σ₁) * B * C * Real.exp (-c * τ ^ 2) := by
  set f : ℝ → ℂ := fun x =>
    logDeriv zetaFEFactor ((x : ℂ) + τ * I) *
      gaborHat F ((x : ℂ) + τ * I)
  have hcont : ContinuousOn f (Icc σ₁ σ₂) :=
    continuousOn_arch_horizontal_integrand F hτ
  have hf : IntervalIntegrable f volume σ₁ σ₂ :=
    hcont.intervalIntegrable_of_Icc hσ
  have hbound : ∀ x, σ₁ ≤ x → x ≤ σ₂ →
      ‖f x‖ ≤ B * C * Real.exp (-c * τ ^ 2) := by
    intro x hx1 hx2
    have hx : x ∈ Icc σ₁ σ₂ := ⟨hx1, hx2⟩
    have := mul_le_mul (hbd x hx) (hhat x hx) (norm_nonneg _) hB
    simpa [f, norm_mul, mul_assoc] using this
  have hle := norm_intervalIntegral_le_length_mul hσ hf hbound
  have : (σ₂ - σ₁) * (B * C * Real.exp (-c * τ ^ 2)) =
      (σ₂ - σ₁) * B * C * Real.exp (-c * τ ^ 2) := by ring
  exact hle.trans_eq this

lemma tendsto_arch_horizontal_edges
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Tendsto (fun T : ℝ =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
        logDeriv zetaFEFactor ((x : ℂ) + T * I) *
          gaborHat F ((x : ℂ) + T * I)) atTop (nhds 0) ∧
    Tendsto (fun T : ℝ =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
        logDeriv zetaFEFactor ((x : ℂ) + (-T : ℝ) * I) *
          gaborHat F ((x : ℂ) + (-T : ℝ) * I)) atTop (nhds 0) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (-1 / 16) (1 / 2)
  have hσ : (-1 / 16 : ℝ) ≤ (1 / 2 : ℝ) := by norm_num
  have hlen : (1 / 2 : ℝ) - (-1 / 16) = 9 / 16 := by norm_num
  set Cψ : ℝ := 6 + |Real.eulerMascheroniConstant|
  set C0 : ℝ :=
    Real.log (2 * Real.pi) + 1 / 2 +
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)
  have hCψ0 : 0 ≤ Cψ := by unfold Cψ; positivity
  have hC00 : 0 ≤ C0 := by
    unfold C0
    have : 0 ≤ Real.log (2 * Real.pi) :=
      Real.log_nonneg (by nlinarith [Real.pi_gt_three])
    positivity
  set K : ℝ := (9 / 16 : ℝ) * (Cψ + C0) * C
  have hedge (τ : ℝ) (hτ : (2 : ℝ) ≤ |τ|) :
      ‖∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + τ * I) *
            gaborHat F ((x : ℂ) + τ * I)‖ ≤
        K * ((1 + Real.log (2 + |τ|)) * Real.exp (-c * τ ^ 2)) := by
    set B : ℝ := Cψ * (1 + Real.log (2 + |τ|)) + C0
    have hB0 : 0 ≤ B :=
      add_nonneg (mul_nonneg hCψ0 (add_nonneg (by norm_num)
        (Real.log_nonneg (by nlinarith [abs_nonneg τ])))) hC00
    have hbd : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) (1 / 2) →
        ‖logDeriv zetaFEFactor ((σ : ℂ) + τ * I)‖ ≤ B := by
      intro σ hσs
      have hre : ((σ : ℂ) + τ * I).re = σ := by simp
      have him : ((σ : ℂ) + τ * I).im = τ := by simp
      have hle :=
        norm_logDeriv_zetaFEFactor_of_sliver
          (s := (σ : ℂ) + τ * I)
          (by simpa [hre] using hσs.1)
          (by simpa [hre] using hσs.2)
          (by simpa [him] using hτ)
      simpa [B, Cψ, C0, him] using hle
    have hhatτ : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) (1 / 2) →
        ‖gaborHat F ((σ : ℂ) + τ * I)‖ ≤ C * Real.exp (-c * τ ^ 2) :=
      fun σ hσs => hhat σ τ hσs.1 hσs.2
    have hle :=
      norm_arch_horizontal_edge_le F hσ hB0 hC.le hc.le hbd hhatτ hτ
    have h1 : (1 : ℝ) ≤ 1 + Real.log (2 + |τ|) :=
      le_add_of_nonneg_right
        (Real.log_nonneg (by nlinarith [abs_nonneg τ]))
    have hpack : B ≤ (Cψ + C0) * (1 + Real.log (2 + |τ|)) := by
      unfold B
      have : C0 ≤ C0 * (1 + Real.log (2 + |τ|)) :=
        le_mul_of_one_le_right hC00 h1
      linarith
    have hmul : (9 / 16 : ℝ) * B * C * Real.exp (-c * τ ^ 2) ≤
        K * ((1 + Real.log (2 + |τ|)) * Real.exp (-c * τ ^ 2)) := by
      unfold K
      have hnn : 0 ≤ C * Real.exp (-c * τ ^ 2) :=
        mul_nonneg hC.le (Real.exp_pos _).le
      have := mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hpack (by norm_num : (0 : ℝ) ≤ 9 / 16)) hnn
      convert this using 1 <;> ring
    exact hle.trans (by rw [hlen]; exact hmul)
  have hdecay : Tendsto (fun T : ℝ =>
      (1 + Real.log (2 + T)) * Real.exp (-c * T ^ 2))
      atTop (nhds 0) := by
    have h :=
      tendsto_one_add_log_add_mul_gauss (c := c) (b := 2) hc (by norm_num)
    refine (h.congr' ?_).trans_eq rfl
    filter_upwards [eventually_ge_atTop (0 : ℝ)] with T _hT
    simp [add_comm]
  have hpos :
      Tendsto (fun T : ℝ =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + T * I) *
            gaborHat F ((x : ℂ) + T * I)) atTop (nhds 0) := by
    refine tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero' (Eventually.of_forall fun _ => norm_nonneg _) ?_
        (by convert hdecay.const_mul K; rw [mul_zero]))
    filter_upwards [eventually_ge_atTop (2 : ℝ)] with T hT
    have hle := hedge T (by simpa [abs_of_nonneg (le_trans
      (by norm_num : (0 : ℝ) ≤ 2) hT)] using hT)
    convert hle using 2
    simp [abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) hT)]
  have hneg :
      Tendsto (fun T : ℝ =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + (-T : ℝ) * I) *
            gaborHat F ((x : ℂ) + (-T : ℝ) * I)) atTop (nhds 0) := by
    refine tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero' (Eventually.of_forall fun _ => norm_nonneg _) ?_
        (by convert hdecay.const_mul K; rw [mul_zero]))
    filter_upwards [eventually_ge_atTop (2 : ℝ)] with T hT
    have hT0 : (0 : ℝ) ≤ T := le_trans (by norm_num : (0 : ℝ) ≤ 2) hT
    have hle := hedge (-T) (by simp [abs_neg, abs_of_nonneg hT0]; exact hT)
    convert hle using 2
    simp [abs_neg, abs_of_nonneg hT0]
  exact ⟨hpos, hneg⟩

/-! ## Interval → improper vertical edges -/

lemma arch_critical_fe_eq_density (F : GaborWeilTest) (y : ℝ) :
    logDeriv zetaFEFactor (((1 / 2 : ℝ) : ℂ) + y * I) *
      gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I) =
      (gaborArchDensity y : ℂ) *
        gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I) := by
  rw [← half_complex_ofReal, logDeriv_zetaFEFactor_criticalLine]

lemma tendsto_arch_right_edge_interval
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ y : ℝ in (-T k)..(T k),
        logDeriv zetaFEFactor (((1 / 2 : ℝ) : ℂ) + y * I) *
          gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I)) atTop
      (𝓝 (∫ t : ℝ, (gaborArchDensity t : ℂ) *
        gaborHat F ((1 / 2 : ℂ) + t * I))) := by
  have hf := integrable_arch_critical_integrand hF
  have hcast :
      (∫ t : ℝ, (gaborArchDensity t : ℂ) *
          gaborHat F ((1 / 2 : ℂ) + t * I)) =
        ∫ t : ℝ, (gaborArchDensity t : ℂ) *
          gaborHat F (((1 / 2 : ℝ) : ℂ) + t * I) :=
    integral_congr_ae (Eventually.of_forall fun t => by
      dsimp
      rw [gaborHat_critical_cast F t])
  rw [hcast]
  refine (tendsto_intervalIntegral_neg_to _ hf hT).congr fun k => ?_
  refine intervalIntegral.integral_congr fun y _hy => ?_
  exact (arch_critical_fe_eq_density F y).symm

lemma tendsto_arch_left_edge_interval
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ y : ℝ in (-T k)..(T k),
        logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + y * I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I)) atTop
      (𝓝 (gaborLeftEdgeArchIntegral F)) :=
  tendsto_intervalIntegral_neg_to _
    (integrable_gabor_left_edge_fe_integrand hF) hT

/-! ## Assembly: `GaborArchContourShift` -/

theorem gaborArchContourShift_holds : GaborArchContourShift := by
  intro F _hFadm hF
  set T : ℕ → ℝ := fun k => (k : ℝ) + 2
  have hT2 : ∀ k, (2 : ℝ) ≤ T k := fun k =>
    le_add_of_nonneg_left (Nat.cast_nonneg k)
  have hTpos : ∀ k, (0 : ℝ) < T k :=
    fun k => lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) (hT2 k)
  have hTtop : Tendsto T atTop atTop :=
    tendsto_atTop_mono (fun k =>
      le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 2))
      tendsto_natCast_atTop_atTop
  obtain ⟨hTop, hBot⟩ := tendsto_arch_horizontal_edges hF
  have hTop' : Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
        logDeriv zetaFEFactor ((x : ℂ) + T k * I) *
          gaborHat F ((x : ℂ) + T k * I)) atTop (nhds 0) :=
    hTop.comp hTtop
  have hBot' : Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
        logDeriv zetaFEFactor ((x : ℂ) + (-(T k) : ℝ) * I) *
          gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0) :=
    hBot.comp hTtop
  have hright := tendsto_arch_right_edge_interval hF hTtop
  have hleft := tendsto_arch_left_edge_interval hF hTtop
  set R : ℂ :=
    ∫ t : ℝ, (gaborArchDensity t : ℂ) *
      gaborHat F ((1 / 2 : ℂ) + t * I)
  set L : ℂ := gaborLeftEdgeArchIntegral F
  have hsides :
      Tendsto (fun k =>
        (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
            logDeriv zetaFEFactor ((x : ℂ) + (-(T k) : ℝ) * I) *
              gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) -
        (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
            logDeriv zetaFEFactor ((x : ℂ) + (T k : ℝ) * I) *
              gaborHat F ((x : ℂ) + (T k : ℝ) * I)) +
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv zetaFEFactor (((1 / 2 : ℝ) : ℂ) + y * I) *
              gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I)) -
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + y * I) *
              gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I))) atTop
        (𝓝 (I • R - I • L)) := by
    convert ((hBot'.sub hTop').add (hright.const_smul I)).sub
      (hleft.const_smul I) using 1
    simp [R, L]
  have heq : ∀ k,
      (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + (-(T k) : ℝ) * I) *
            gaborHat F ((x : ℂ) + (-(T k) : ℝ) * I)) -
      (∫ x : ℝ in (-1 / 16 : ℝ)..(1 / 2),
          logDeriv zetaFEFactor ((x : ℂ) + (T k : ℝ) * I) *
            gaborHat F ((x : ℂ) + (T k : ℝ) * I)) +
      I • (∫ y : ℝ in (-(T k))..(T k),
          logDeriv zetaFEFactor (((1 / 2 : ℝ) : ℂ) + y * I) *
            gaborHat F (((1 / 2 : ℝ) : ℂ) + y * I)) -
      I • (∫ y : ℝ in (-(T k))..(T k),
          logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + y * I) *
            gaborHat F (((-1 / 16 : ℝ) : ℂ) + y * I)) =
        (2 * (Real.pi : ℂ) * I) * (-gaborHat F 0) := fun k =>
    (rectangleIntegral_arch_fe_hat_unfold F (T k)).symm.trans
      (rectangleIntegral_arch_fe_hat F (hTpos k))
  have hlim := tendsto_nhds_unique (hsides.congr heq) tendsto_const_nhds
  have hI : I ≠ 0 := I_ne_zero
  have hπc : (2 * (Real.pi : ℂ)) = (2 * Real.pi : ℂ) := by
    norm_cast
  have halg : I * R - I * L = -((2 * Real.pi : ℂ) * I) * gaborHat F 0 := by
    simpa [smul_eq_mul, hπc, mul_neg] using hlim
  have hcancel : I * (R - L) = I * (-(2 * Real.pi : ℂ) * gaborHat F 0) := by
    convert halg using 1
    · ring
    · ring
  have hRL : R - L = -(2 * Real.pi : ℂ) * gaborHat F 0 :=
    mul_left_cancel₀ hI hcancel
  have hgoal : L = (2 * Real.pi : ℂ) * gaborHat F 0 + R := by
    linear_combination -hRL
  simpa [L, R] using hgoal

theorem gaborArchDigammaIdentification_holds :
    GaborArchDigammaIdentification :=
  gaborArchDigammaIdentification_of_parts
    gaborArchContourShift_holds gaborArchCriticalPairingReal_holds

#print axioms gaborArchContourShift_holds
#print axioms gaborArchDigammaIdentification_holds

end RH
