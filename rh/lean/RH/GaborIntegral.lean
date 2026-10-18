import RH.ExternalBridges
import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform

/-
RH/GaborIntegral.lean -- r543 bilateral Gaussian integral for the pure Gabor test.

This module contains only the analytic identity needed by
`RH.GaborSeparation`.  It makes no statement about zeta zeros or RH.
-/

namespace RH

open MeasureTheory

/-- Bilateral complex Gaussian Laplace transform in the real-positive gauge
used by the pure Gabor autocorrelation. -/
theorem integral_cexp_neg_half_mul_sq_add
    (a : ℝ) (ha : 0 < a) (z : ℂ) :
    (∫ u : ℝ, Complex.exp (-(a : ℂ) / 2 * u ^ 2 + z * u)) =
      (Real.sqrt (2 * Real.pi / a) : ℂ) *
        Complex.exp (z ^ 2 / (2 * a)) := by
  have hb : (-(a : ℂ) / 2).re < 0 := by
    norm_num
    linarith
  have hquad := integral_cexp_quadratic
    (b := -(a : ℂ) / 2) hb z 0
  simp only [add_zero] at hquad
  rw [hquad]
  have harg : 0 ≤ 2 * Real.pi / a := (div_pos (mul_pos (by norm_num) Real.pi_pos) ha).le
  have hcoeff :
      (Real.pi : ℂ) / -(-(a : ℂ) / 2) = (2 * Real.pi / a : ℝ) := by
    push_cast
    field_simp [ne_of_gt ha]
  have hexponent :
      0 - z ^ 2 / (4 * (-(a : ℂ) / 2)) = z ^ 2 / (2 * a) := by
    field_simp [ne_of_gt ha]
    ring
  rw [hcoeff, hexponent]
  have hhalf : (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) := by norm_num
  rw [hhalf]
  rw [← Complex.ofReal_cpow harg, ← Real.sqrt_eq_rpow]

/-- The Gaussian-with-linear-term integrand is Bochner integrable. -/
theorem integrable_cexp_neg_half_mul_sq_add
    (a : ℝ) (ha : 0 < a) (z : ℂ) :
    Integrable (fun u : ℝ =>
      Complex.exp (-(a : ℂ) / 2 * u ^ 2 + z * u)) := by
  have hb : 0 < ((a : ℂ) / 2).re := by
    norm_num
    linarith
  convert (integrable_cexp_quadratic (b := (a : ℂ) / 2) hb z 0) using 1
  ext u
  congr 1
  ring

/-- Euler expansion of a real cosine, in the coercion used below. -/
theorem ofReal_cos_eq_half_exp_add_exp_neg (x : ℝ) :
    (Real.cos x : ℂ) =
      (1 / 2 : ℂ) *
        (Complex.exp ((x : ℂ) * Complex.I) +
          Complex.exp (-(x : ℂ) * Complex.I)) := by
  rw [Complex.exp_ofReal_mul_I]
  rw [show -(x : ℂ) * Complex.I = ((-x : ℝ) : ℂ) * Complex.I by push_cast; ring]
  rw [Complex.exp_ofReal_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  ring

/-- Pointwise Euler decomposition of the modulated Gaussian. -/
theorem gaussian_mul_cos_mul_cexp_eq
    (a omega : ℝ) (z : ℂ) (u : ℝ) :
    (Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
        Complex.exp (z * u) =
      (1 / 2 : ℂ) * Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
            (z + Complex.I * omega) * u) +
        (1 / 2 : ℂ) * Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
            (z - Complex.I * omega) * u) := by
  rw [Complex.ofReal_mul, Complex.ofReal_exp, ofReal_cos_eq_half_exp_add_exp_neg]
  simp only [Complex.ofReal_neg, Complex.ofReal_mul, Complex.ofReal_div,
    Complex.ofReal_pow, Complex.ofReal_ofNat]
  calc
    Complex.exp (-↑a * ↑u ^ 2 / 2) *
          (1 / 2 *
            (Complex.exp (↑omega * ↑u * Complex.I) +
              Complex.exp (-(↑omega * ↑u) * Complex.I))) *
          Complex.exp (z * ↑u) =
        1 / 2 *
            (Complex.exp (-↑a * ↑u ^ 2 / 2) *
              Complex.exp (↑omega * ↑u * Complex.I) *
              Complex.exp (z * ↑u)) +
          1 / 2 *
            (Complex.exp (-↑a * ↑u ^ 2 / 2) *
              Complex.exp (-(↑omega * ↑u) * Complex.I) *
              Complex.exp (z * ↑u)) := by ring
    _ = _ := by
      have hp :
          Complex.exp (-↑a * ↑u ^ 2 / 2) *
              Complex.exp (↑omega * ↑u * Complex.I) *
              Complex.exp (z * ↑u) =
            Complex.exp (-↑a / 2 * ↑u ^ 2 +
              (z + Complex.I * ↑omega) * ↑u) := by
        rw [← Complex.exp_add, ← Complex.exp_add]
        congr 1
        ring
      have hm :
          Complex.exp (-↑a * ↑u ^ 2 / 2) *
              Complex.exp (-(↑omega * ↑u) * Complex.I) *
              Complex.exp (z * ↑u) =
            Complex.exp (-↑a / 2 * ↑u ^ 2 +
              (z - Complex.I * ↑omega) * ↑u) := by
        rw [← Complex.exp_add, ← Complex.exp_add]
        congr 1
        ring
      rw [hp, hm]

/-- Bilateral Gaussian Laplace transform with a cosine modulation. -/
theorem integral_gaussian_mul_cos_mul_cexp
    (a omega : ℝ) (ha : 0 < a) (z : ℂ) :
    (∫ u : ℝ,
        (Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
          Complex.exp (z * u)) =
      (Real.sqrt (2 * Real.pi / a) : ℂ) / 2 *
        (Complex.exp ((z + Complex.I * omega) ^ 2 / (2 * a)) +
          Complex.exp ((z - Complex.I * omega) ^ 2 / (2 * a))) := by
  have hplus := integrable_cexp_neg_half_mul_sq_add a ha (z + Complex.I * omega)
  have hminus := integrable_cexp_neg_half_mul_sq_add a ha (z - Complex.I * omega)
  simp_rw [gaussian_mul_cos_mul_cexp_eq a omega z]
  rw [MeasureTheory.integral_add (hplus.const_mul _) (hminus.const_mul _)]
  have hiPlus :
      (∫ u : ℝ, (1 / 2 : ℂ) *
        Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
          (z + Complex.I * omega) * u)) =
        (1 / 2 : ℂ) * ∫ u : ℝ,
          Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
            (z + Complex.I * omega) * u) :=
    MeasureTheory.integral_const_mul _ _
  have hiMinus :
      (∫ u : ℝ, (1 / 2 : ℂ) *
        Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
          (z - Complex.I * omega) * u)) =
        (1 / 2 : ℂ) * ∫ u : ℝ,
          Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
            (z - Complex.I * omega) * u) :=
    MeasureTheory.integral_const_mul _ _
  rw [hiPlus, hiMinus]
  rw [integral_cexp_neg_half_mul_sq_add a ha,
    integral_cexp_neg_half_mul_sq_add a ha]
  ring

/-- Closed bilateral transform of the pure-Gabor autocorrelation, before
splitting complex exponentials into real amplitude and phase. -/
theorem pureGabor_integral_compact
    (a omega : ℝ) (ha : 0 < a) (z : ℂ) :
    (∫ u : ℝ,
      ((Real.sqrt (Real.pi / (2 * a)) / 2 *
          Real.exp (-a * u ^ 2 / 2) *
          (Real.cos (omega * u) + Real.exp (-omega ^ 2 / (2 * a))) : ℝ) : ℂ) *
        Complex.exp (z * u)) =
      ((Real.pi / (4 * a) : ℝ) : ℂ) *
        (Complex.exp ((z + Complex.I * omega) ^ 2 / (2 * a)) +
          Complex.exp ((z - Complex.I * omega) ^ 2 / (2 * a)) +
          2 * Complex.exp (-omega ^ 2 / (2 * a)) *
            Complex.exp (z ^ 2 / (2 * a))) := by
  have hcos := integral_gaussian_mul_cos_mul_cexp a omega ha z
  have hgauss := integral_cexp_neg_half_mul_sq_add a ha z
  have hgaussInt := integrable_cexp_neg_half_mul_sq_add a ha z
  have hgaussPoint (u : ℝ) :
      (Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u) =
        Complex.exp (-(a : ℂ) / 2 * u ^ 2 + z * u) := by
    rw [Complex.ofReal_exp, ← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hcosInt :
      Integrable (fun u : ℝ =>
        (Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
          Complex.exp (z * u)) := by
    have hp := integrable_cexp_neg_half_mul_sq_add a ha (z + Complex.I * omega)
    have hm := integrable_cexp_neg_half_mul_sq_add a ha (z - Complex.I * omega)
    rw [show
      (fun u : ℝ =>
        (Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
          Complex.exp (z * u)) =
        (fun u : ℝ =>
          (1 / 2 : ℂ) * Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
              (z + Complex.I * omega) * u) +
            (1 / 2 : ℂ) * Complex.exp (-(a : ℂ) / 2 * u ^ 2 +
              (z - Complex.I * omega) * u)) by
        funext u
        exact gaussian_mul_cos_mul_cexp_eq a omega z u]
    exact (hp.const_mul _).add (hm.const_mul _)
  have hrealGaussInt :
      Integrable (fun u : ℝ =>
        (Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u)) := by
    rw [show
      (fun u : ℝ =>
        (Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u)) =
        (fun u : ℝ =>
          Complex.exp (-(a : ℂ) / 2 * u ^ 2 + z * u)) by
        funext u
        exact hgaussPoint u]
    exact hgaussInt
  have hpoint (u : ℝ) :
      ((Real.sqrt (Real.pi / (2 * a)) / 2 *
          Real.exp (-a * u ^ 2 / 2) *
          (Real.cos (omega * u) + Real.exp (-omega ^ 2 / (2 * a))) : ℝ) : ℂ) *
          Complex.exp (z * u) =
        (Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          ((Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
            Complex.exp (z * u)) +
        (Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          (Real.exp (-omega ^ 2 / (2 * a)) : ℂ) *
          ((Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u)) := by
    push_cast
    ring
  simp_rw [hpoint]
  rw [MeasureTheory.integral_add
    (hcosInt.const_mul _)
    (hrealGaussInt.const_mul
      ((Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
        (Real.exp (-omega ^ 2 / (2 * a)) : ℂ)))]
  have hIntCos :
      (∫ u : ℝ,
        (Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          ((Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
            Complex.exp (z * u))) =
        (Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          ∫ u : ℝ,
            (Real.exp (-a * u ^ 2 / 2) * Real.cos (omega * u) : ℝ) *
              Complex.exp (z * u) :=
    MeasureTheory.integral_const_mul _ _
  have hIntGauss :
      (∫ u : ℝ,
        (Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          (Real.exp (-omega ^ 2 / (2 * a)) : ℂ) *
          ((Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u))) =
        ((Real.sqrt (Real.pi / (2 * a)) / 2 : ℂ) *
          (Real.exp (-omega ^ 2 / (2 * a)) : ℂ)) *
          ∫ u : ℝ,
            (Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u) :=
    MeasureTheory.integral_const_mul _ _
  rw [hIntCos, hIntGauss]
  rw [hcos, show
      (∫ u : ℝ,
        (Real.exp (-a * u ^ 2 / 2) : ℂ) * Complex.exp (z * u)) =
          (Real.sqrt (2 * Real.pi / a) : ℂ) *
            Complex.exp (z ^ 2 / (2 * a)) by
        simp_rw [hgaussPoint]
        exact hgauss]
  have hpa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hsqrtProduct :
      Real.sqrt (Real.pi / (2 * a)) *
          Real.sqrt (2 * Real.pi / a) = Real.pi / a := by
    rw [← Real.sqrt_mul (by positivity : 0 ≤ Real.pi / (2 * a))]
    have hinside :
        (Real.pi / (2 * a)) * (2 * Real.pi / a) =
          (Real.pi / a) ^ 2 := by
      field_simp [ne_of_gt ha]
    rw [hinside, Real.sqrt_sq_eq_abs, abs_of_pos hpa]
  have hsqrtProductC :
      (Real.sqrt (Real.pi / (2 * a)) : ℂ) *
          (Real.sqrt (2 * Real.pi / a) : ℂ) =
        ((Real.pi / a : ℝ) : ℂ) := by
    exact_mod_cast hsqrtProduct
  have hExpOmega :
      (Real.exp (-omega ^ 2 / (2 * a)) : ℂ) =
        Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) := by
    rw [Complex.ofReal_exp]
    congr 1
    push_cast
    rfl
  rw [hExpOmega]
  calc
    (Real.sqrt (Real.pi / (2 * a)) : ℂ) / 2 *
          ((Real.sqrt (2 * Real.pi / a) : ℂ) / 2 *
            (Complex.exp ((z + Complex.I * omega) ^ 2 / (2 * a)) +
              Complex.exp ((z - Complex.I * omega) ^ 2 / (2 * a)))) +
        ((Real.sqrt (Real.pi / (2 * a)) : ℂ) / 2 *
          Complex.exp (-(omega : ℂ) ^ 2 / (2 * a))) *
          ((Real.sqrt (2 * Real.pi / a) : ℂ) *
            Complex.exp (z ^ 2 / (2 * a))) =
      ((Real.sqrt (Real.pi / (2 * a)) : ℂ) *
          (Real.sqrt (2 * Real.pi / a) : ℂ)) / 4 *
        (Complex.exp ((z + Complex.I * omega) ^ 2 / (2 * a)) +
          Complex.exp ((z - Complex.I * omega) ^ 2 / (2 * a)) +
          2 * Complex.exp (-omega ^ 2 / (2 * a)) *
            Complex.exp (z ^ 2 / (2 * a))) := by ring
    _ = _ := by
      rw [hsqrtProductC]
      push_cast
      ring

/-- Real-amplitude/phase split for a frequency-shifted complex Gaussian. -/
theorem cexp_square_shift_split
    (a nu : ℝ) (ha : a ≠ 0) (z : ℂ) :
    Complex.exp ((z + Complex.I * nu) ^ 2 / (2 * a)) =
      (Real.exp ((z.re ^ 2 - (z.im + nu) ^ 2) / (2 * a)) : ℂ) *
        Complex.exp
          (Complex.I * (z.re * (z.im + nu) / a)) := by
  have hexponent :
      (z + Complex.I * nu) ^ 2 / (2 * a) =
        (((z.re ^ 2 - (z.im + nu) ^ 2) / (2 * a) : ℝ) : ℂ) +
          Complex.I * (z.re * (z.im + nu) / a) := by
    have hz : z = (z.re : ℂ) + (z.im : ℂ) * Complex.I :=
      (Complex.re_add_im z).symm
    nth_rewrite 1 [hz]
    push_cast
    field_simp [ha]
    ring_nf
    rw [Complex.I_sq]
    ring
  rw [hexponent, Complex.exp_add, ← Complex.ofReal_exp]

/-- Real-amplitude/phase split for the unshifted square with the carrier
damping factor included. -/
theorem cexp_neg_frequency_mul_square_split
    (a omega : ℝ) (ha : a ≠ 0) (z : ℂ) :
    Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (z ^ 2 / (2 * a)) =
      (Real.exp ((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a)) : ℂ) *
        Complex.exp (Complex.I * (z.re * z.im / a)) := by
  rw [← Complex.exp_add]
  have hexponent :
      -(omega : ℂ) ^ 2 / (2 * a) + z ^ 2 / (2 * a) =
        (((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a) : ℝ) : ℂ) +
          Complex.I * (z.re * z.im / a) := by
    have hz : z = (z.re : ℂ) + (z.im : ℂ) * Complex.I :=
      (Complex.re_add_im z).symm
    nth_rewrite 1 [hz]
    push_cast
    field_simp [ha]
    ring_nf
    rw [Complex.I_sq]
    ring
  rw [hexponent, Complex.exp_add, ← Complex.ofReal_exp]

/-- Exact pure-Gabor integral in the expanded amplitude/phase convention of
`pureGaborHatDelta`. -/
theorem pureGabor_integral_closed_form
    (a omega : ℝ) (ha : 0 < a) (z : ℂ) :
    (∫ u : ℝ,
      ((Real.sqrt (Real.pi / (2 * a)) / 2 *
          Real.exp (-a * u ^ 2 / 2) *
          (Real.cos (omega * u) + Real.exp (-omega ^ 2 / (2 * a))) : ℝ) : ℂ) *
        Complex.exp (z * u)) =
      ((Real.pi / (4 * a) : ℝ) : ℂ) *
        (((Real.exp ((z.re ^ 2 - (z.im + omega) ^ 2) / (2 * a)) : ℝ) : ℂ) *
            Complex.exp (Complex.I * (z.re * (z.im + omega) / a)) +
          ((Real.exp ((z.re ^ 2 - (z.im - omega) ^ 2) / (2 * a)) : ℝ) : ℂ) *
            Complex.exp (Complex.I * (z.re * (z.im - omega) / a)) +
          2 * ((Real.exp ((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a)) : ℝ) : ℂ) *
            Complex.exp (Complex.I * (z.re * z.im / a))) := by
  rw [pureGabor_integral_compact a omega ha z]
  rw [cexp_square_shift_split a omega (ne_of_gt ha) z]
  have hminus := cexp_square_shift_split a (-omega) (ne_of_gt ha) z
  rw [show z - Complex.I * (omega : ℂ) =
      z + Complex.I * (-omega : ℝ) by push_cast; ring]
  rw [hminus]
  simp only [sub_eq_add_neg, Complex.ofReal_neg]
  rw [show
    2 * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (z ^ 2 / (2 * a)) =
      2 * (Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (z ^ 2 / (2 * a))) by ring]
  rw [cexp_neg_frequency_mul_square_split a omega (ne_of_gt ha) z]
  ring

end RH
