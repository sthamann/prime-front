/-
RH/GaborContourResidue.lean -- r557 brick: fixed-T residue identity
for `(ζ′/ζ) ĥ_W` on the rectangle `[-1/16, 2] × [-T, T]`.

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free punch-pole contour identity
for an entire multiplier.  This file does not prove
`GaborExplicitFormula` and does not take the `T → ∞` limit.

The compact-hat identity `contour_identity_fixed_T` hard-codes
`FullWeilTest.hat`.  The punch-pole machine
(`logDerivHatRemainderFilled`, `logDeriv_mul_eq_sum_add_filled`,
`rectangleIntegral_sum_simple_poles`) is already test-function
generic.  This file restates that argument for an arbitrary entire
multiplier and specialises to `gaborHat` (entire by r555).
-/
import RH.GaborHatAnalytic

namespace RH

open Complex Filter intervalIntegral MeasureTheory Set
open scoped Interval Topology

/-- Generic r517 identity: entire multiplier, left edge in `(-1/4, 0)`.
Trivial zeros lie at the negative even integers and are outside the
rectangle.  The pole residue of `ζ′/ζ` at `s = 1` is `-1`. -/
lemma contour_identity_fixed_T_of_entire
    (F : ℂ → ℂ) (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ T : ℝ} (hσlo : -1 / 4 < σ₁) (hσhi : σ₁ < 0) (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect σ₁ 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F ζ)
      ((σ₁ : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum F σ₁ 2 T - F 1) := by
  set z : ℂ := (σ₁ : ℂ) + (-T : ℝ) * I
  set w : ℂ := (((2 : ℝ) : ℂ) + (T : ℝ) * I)
  have hzre : z.re = σ₁ := by simp [z]
  have hwre : w.re = 2 := by simp [w]
  have hzim : z.im = -T := by simp [z]
  have hwim : w.im = T := by simp [w]
  have hre_le : σ₁ ≤ 2 :=
    le_trans (le_of_lt hσhi) (by norm_num : (0 : ℝ) ≤ 2)
  have him_le : -T ≤ T := neg_le_self hT.le
  have hrect :
      [[z.re, w.re]] ×ℂ [[z.im, w.im]] =
        zetaClosedRect σ₁ 2 T := by
    simp [zetaClosedRect, hzre, hwre, hzim, hwim,
      uIcc_of_le hre_le, uIcc_of_le him_le]
  let zeros := riemannZetaZerosOnClosedRect σ₁ 2 T
  let poles := contourPoles σ₁ 2 T
  let H := logDerivHatRemainderFilled hF σ₁ 2 T
  let r : ℂ → ℂ := fun p =>
    if p = 1 then -F 1
    else (riemannZetaMultiplicity p : ℂ) * F p
  have h1z : (1 : ℂ) ∉ zeros :=
    one_not_mem_riemannZetaZerosOnClosedRect σ₁ 2 T
  have hH : DifferentiableOn ℂ H ([[z.re, w.re]] ×ℂ [[z.im, w.im]]) := by
    rw [hrect]
    exact differentiableOn_logDerivHatRemainderFilled hF σ₁ 2 T
  have hp : ∀ p ∈ insert (1 : ℂ) zeros,
      z.re < p.re ∧ p.re < w.re ∧ z.im < p.im ∧ p.im < w.im := by
    intro p hp
    rw [hzre, hwre, hzim, hwim]
    rcases Finset.mem_insert.mp hp with hp1 | hpz
    · subst hp1
      refine ⟨lt_trans hσhi (by norm_num : (0 : ℝ) < 1), by norm_num,
        neg_lt_zero.mpr hT, hT⟩
    · have hmem := mem_riemannZetaZerosOnClosedRect.mp hpz
      have hQ := mem_zetaClosedRect.mp hmem.1
      have hre1 : σ₁ < p.re := lt_of_le_of_ne hQ.1 fun h =>
        (riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero
          (by rwa [← h]) (by rwa [← h])) hmem.2.1
      have hre2 : p.re < 2 := lt_of_le_of_ne hQ.2.1 fun h =>
        (riemannZeta_ne_zero_of_re_eq_two h) hmem.2.1
      have him : |p.im| < T := hord p hpz
      exact ⟨hre1, hre2, (abs_lt.mp him).1, (abs_lt.mp him).2⟩
  have hside : ∀ q : ℂ,
      q.re = σ₁ ∨ q.re = 2 ∨ q.im = -T ∨ q.im = T →
        q ∉ poles := by
    intro q hq hqp
    rw [mem_contourPoles] at hqp
    rcases hqp with hq1 | hqz
    · subst hq1
      rcases hq with hre | hre | him | him
      · have : σ₁ = 1 := hre.symm
        linarith [hσhi]
      · norm_num at hre
      · exact (neg_lt_zero.mpr hT).ne him.symm
      · exact hT.ne' him.symm
    · have hmem := mem_riemannZetaZerosOnClosedRect.mp hqz
      rcases hq with hre | hre | him | him
      · exact (riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero
          (by rwa [hre]) (by rwa [hre])) hmem.2.1
      · exact (riemannZeta_ne_zero_of_re_eq_two hre) hmem.2.1
      · have : |q.im| < T := hord q hqz
        rw [him, abs_neg, abs_of_nonneg hT.le] at this
        exact lt_irrefl T this
      · have : |q.im| < T := hord q hqz
        rw [him, abs_of_nonneg hT.le] at this
        exact lt_irrefl T this
  have hfun :
      rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F ζ) z w =
        rectangleIntegral
          (fun ζ => (∑ p ∈ insert (1 : ℂ) zeros, r p / (ζ - p)) + H ζ)
          z w := by
    refine rectangleIntegral_congr_sides _ _ z w ?bot ?top ?right ?left
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + z.im * I).im = -T := by simp [hzim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inl hq)))
      rw [logDeriv_mul_eq_sum_add_filled hF hnp,
        contour_sum_r_eq F σ₁ 2 T _ h1z]
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + w.im * I).im = T := by simp [hwim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inr hq)))
      rw [logDeriv_mul_eq_sum_add_filled hF hnp,
        contour_sum_r_eq F σ₁ 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((w.re : ℂ) + y * I).re = 2 := by simp [hwre]
      have hnp := hside _ (Or.inr (Or.inl hq))
      rw [logDeriv_mul_eq_sum_add_filled hF hnp,
        contour_sum_r_eq F σ₁ 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((z.re : ℂ) + y * I).re = σ₁ := by simp [hzre]
      have hnp := hside _ (Or.inl hq)
      rw [logDeriv_mul_eq_sum_add_filled hF hnp,
        contour_sum_r_eq F σ₁ 2 T _ h1z]
  have hcauchy :=
    rectangleIntegral_sum_simple_poles H z w (insert (1 : ℂ) zeros) r hH hp
  rw [hfun, hcauchy]
  have hsumr : ∑ p ∈ insert (1 : ℂ) zeros, r p =
      spectralPartialSum F σ₁ 2 T - F 1 := by
    have hr1 : r 1 = -F 1 := if_pos rfl
    have hrp : ∀ ρ ∈ zeros,
        r ρ = (riemannZetaMultiplicity ρ : ℂ) * F ρ :=
      fun ρ hρ => if_neg (mem_riemannZetaZerosOnClosedRect.mp hρ).2.2
    rw [Finset.sum_insert h1z, hr1, spectralPartialSum, sub_eq_add_neg,
      add_comm]
    congr 1
    exact Finset.sum_congr rfl fun ρ hρ => hrp ρ hρ
  rw [hsumr]

/-- Specialisation to the r522 contour `Re ∈ [-1/16, 2]`. -/
lemma contour_identity_fixed_T_neg_one_div_sixteen_entire
    (F : ℂ → ℂ) (hF : AnalyticOnNhd ℂ F univ)
    {T : ℝ} (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum F (-1 / 16) 2 T - F 1) :=
  contour_identity_fixed_T_of_entire F hF (by norm_num) (by norm_num) hT hord

/-- Fixed-`T` residue identity for a Gabor test (any even quartic:
`gaborHat` is entire).  Along a Landau gap height the hypothesis
`|ρ.im| < T` holds by `abs_im_lt_of_landau_gaps`. -/
theorem gabor_contour_identity_fixed_T
    (F : GaborWeilTest) {T : ℝ} (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum (gaborHat F) (-1 / 16) 2 T - gaborHat F 1) :=
  contour_identity_fixed_T_neg_one_div_sixteen_entire
    (gaborHat F) (analyticOnNhd_gaborHat F) hT hord

/-- Named remainder: the `T → ∞` spectral Finset exhaustion along a
Landau-gap height sequence.  Discharged r576 as
`gaborContourLimitRemainder_holds` (same sequence as
`gaborContourVerticalLimit_holds`); not a `sorry`. -/
def GaborContourLimitRemainder : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    ∃ T : ℕ → ℝ,
      Tendsto T atTop atTop ∧
        (∀ k, 0 < T k) ∧
        (∀ k, ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 (T k),
          |ρ.im| < T k) ∧
        Tendsto (fun k =>
          spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k))
          atTop
          (nhds
            (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ))

end RH
