/-
RH/GaborAutocorrelation.lean -- r572 closed form of the pure Gabor ACF
and the half-comb real-part identification.

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free Gaussian calculation:
the defining autocorrelation integral equals the closed packet
`pureGaborAutocorrelation`, and the right half-comb is the real
half of the corpus comb.  This file does not prove
`GaborExplicitFormula` and does not close the vertical T to inf
contour glue.
-/
import RH.GaborVertical
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.Topology.Algebra.InfiniteSum.Module

namespace RH

open Complex Filter MeasureTheory
open scoped Topology LSeries.notation

/-! ## Pointwise Euler / Gaussian identities -/

theorem gabor_carrier_of_pure
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (t : ℝ) :
    F.carrier t = Real.exp (-F.a * t ^ 2) * Real.cos (F.omega * t) := by
  unfold GaborWeilTest.carrier EvenQuartic.eval
  simp [hF]

theorem ofReal_cos_mul_cos_four (x y : ℝ) :
    ((Real.cos x * Real.cos y : ℝ) : ℂ) =
      (1 / 4 : ℂ) *
        (Complex.exp (((x + y : ℝ) : ℂ) * Complex.I) +
          Complex.exp (((x - y : ℝ) : ℂ) * Complex.I) +
          Complex.exp (((-x + y : ℝ) : ℂ) * Complex.I) +
          Complex.exp (((-x - y : ℝ) : ℂ) * Complex.I)) := by
  rw [Complex.ofReal_mul, ofReal_cos_eq_half_exp_add_exp_neg,
    ofReal_cos_eq_half_exp_add_exp_neg]
  have hxpy :
      Complex.exp ((x : ℂ) * Complex.I) * Complex.exp ((y : ℂ) * Complex.I) =
        Complex.exp (((x + y : ℝ) : ℂ) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hxmy :
      Complex.exp ((x : ℂ) * Complex.I) * Complex.exp (-(y : ℂ) * Complex.I) =
        Complex.exp (((x - y : ℝ) : ℂ) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hmxpy :
      Complex.exp (-(x : ℂ) * Complex.I) * Complex.exp ((y : ℂ) * Complex.I) =
        Complex.exp (((-x + y : ℝ) : ℂ) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hmxmy :
      Complex.exp (-(x : ℂ) * Complex.I) * Complex.exp (-(y : ℂ) * Complex.I) =
        Complex.exp (((-x - y : ℝ) : ℂ) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  calc
    (1 / 2 : ℂ) *
          (Complex.exp ((x : ℂ) * Complex.I) +
            Complex.exp (-(x : ℂ) * Complex.I)) *
        ((1 / 2 : ℂ) *
          (Complex.exp ((y : ℂ) * Complex.I) +
            Complex.exp (-(y : ℂ) * Complex.I))) =
      (1 / 4 : ℂ) *
        (Complex.exp ((x : ℂ) * Complex.I) * Complex.exp ((y : ℂ) * Complex.I) +
          Complex.exp ((x : ℂ) * Complex.I) * Complex.exp (-(y : ℂ) * Complex.I) +
          Complex.exp (-(x : ℂ) * Complex.I) * Complex.exp ((y : ℂ) * Complex.I) +
          Complex.exp (-(x : ℂ) * Complex.I) *
            Complex.exp (-(y : ℂ) * Complex.I)) := by
      ring
    _ = _ := by rw [hxpy, hxmy, hmxpy, hmxmy]

theorem ofReal_gabor_gauss_product (a u t : ℝ) :
    ((Real.exp (-a * t ^ 2) * Real.exp (-a * (t - u) ^ 2) : ℝ) : ℂ) =
      Complex.exp
        (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) := by
  rw [Complex.ofReal_mul, Complex.ofReal_exp, Complex.ofReal_exp, ← Complex.exp_add]
  congr 1
  push_cast
  ring

/-- Four-term Euler expansion of the pure ACF integrand, after `ofReal`. -/
theorem gabor_acf_integrand_four_cexp (a omega u t : ℝ) :
    ((Real.exp (-a * t ^ 2) * Real.cos (omega * t) *
        Real.exp (-a * (t - u) ^ 2) * Real.cos (omega * (t - u)) : ℝ) : ℂ) =
      (1 / 4 : ℂ) *
        (Complex.exp
            (-(2 * a : ℂ) * t ^ 2 +
              ((2 * a * u : ℂ) + (2 : ℂ) * Complex.I * omega) * t +
              (-(a * u ^ 2 : ℂ) - Complex.I * omega * u)) +
          Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t +
              (-(a * u ^ 2 : ℂ) + Complex.I * omega * u)) +
          Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t +
              (-(a * u ^ 2 : ℂ) - Complex.I * omega * u)) +
          Complex.exp
            (-(2 * a : ℂ) * t ^ 2 +
              ((2 * a * u : ℂ) - (2 : ℂ) * Complex.I * omega) * t +
              (-(a * u ^ 2 : ℂ) + Complex.I * omega * u))) := by
  have hsplit :
      ((Real.exp (-a * t ^ 2) * Real.cos (omega * t) *
            Real.exp (-a * (t - u) ^ 2) * Real.cos (omega * (t - u)) : ℝ) : ℂ) =
        ((Real.exp (-a * t ^ 2) * Real.exp (-a * (t - u) ^ 2) : ℝ) : ℂ) *
          ((Real.cos (omega * t) * Real.cos (omega * (t - u)) : ℝ) : ℂ) := by
    push_cast
    ring
  rw [hsplit, ofReal_gabor_gauss_product, ofReal_cos_mul_cos_four]
  have hw2 : (omega * t + omega * (t - u) : ℝ) = omega * (2 * t - u) := by ring
  have hw0 : (omega * t - omega * (t - u) : ℝ) = omega * u := by ring
  have hw0' : (-(omega * t) + omega * (t - u) : ℝ) = -(omega * u) := by ring
  have hw2' : (-(omega * t) - omega * (t - u) : ℝ) = -(omega * (2 * t - u)) := by
    ring
  simp_rw [hw2, hw0, hw0', hw2']
  have hpp :
      Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
          Complex.exp (((omega * (2 * t - u) : ℝ) : ℂ) * Complex.I) =
        Complex.exp
          (-(2 * a : ℂ) * t ^ 2 +
            ((2 * a * u : ℂ) + (2 : ℂ) * Complex.I * omega) * t +
            (-(a * u ^ 2 : ℂ) - Complex.I * omega * u)) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hp0 :
      Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
          Complex.exp (((omega * u : ℝ) : ℂ) * Complex.I) =
        Complex.exp
          (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t +
            (-(a * u ^ 2 : ℂ) + Complex.I * omega * u)) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hm0 :
      Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
          Complex.exp (((-(omega * u) : ℝ) : ℂ) * Complex.I) =
        Complex.exp
          (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t +
            (-(a * u ^ 2 : ℂ) - Complex.I * omega * u)) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hmm :
      Complex.exp
            (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
          Complex.exp (((-(omega * (2 * t - u)) : ℝ) : ℂ) * Complex.I) =
        Complex.exp
          (-(2 * a : ℂ) * t ^ 2 +
            ((2 * a * u : ℂ) - (2 : ℂ) * Complex.I * omega) * t +
            (-(a * u ^ 2 : ℂ) + Complex.I * omega * u)) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  calc
    Complex.exp
          (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
        ((1 / 4 : ℂ) *
          (Complex.exp (((omega * (2 * t - u) : ℝ) : ℂ) * Complex.I) +
            Complex.exp (((omega * u : ℝ) : ℂ) * Complex.I) +
            Complex.exp (((-(omega * u) : ℝ) : ℂ) * Complex.I) +
            Complex.exp (((-(omega * (2 * t - u)) : ℝ) : ℂ) * Complex.I))) =
      (1 / 4 : ℂ) *
        (Complex.exp
              (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
            Complex.exp (((omega * (2 * t - u) : ℝ) : ℂ) * Complex.I) +
          Complex.exp
              (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
            Complex.exp (((omega * u : ℝ) : ℂ) * Complex.I) +
          Complex.exp
              (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
            Complex.exp (((-(omega * u) : ℝ) : ℂ) * Complex.I) +
          Complex.exp
              (-(2 * a : ℂ) * t ^ 2 + (2 * a * u : ℂ) * t - (a * u ^ 2 : ℂ)) *
            Complex.exp (((-(omega * (2 * t - u)) : ℝ) : ℂ) * Complex.I)) := by
      ring
    _ = _ := by rw [hpp, hp0, hm0, hmm]

/-! ## Bilateral Gaussian with linear + constant term -/

theorem integral_cexp_neg_two_a_sq_add
    (a : ℝ) (ha : 0 < a) (z d : ℂ) :
    (∫ t : ℝ, Complex.exp (-(2 * a : ℂ) * t ^ 2 + z * t + d)) =
      (Real.sqrt (Real.pi / (2 * a)) : ℂ) *
        Complex.exp (d + z ^ 2 / (8 * a)) := by
  have h4 : 0 < 4 * a := mul_pos (by norm_num) ha
  have hfun :
      (fun t : ℝ => Complex.exp (-(2 * a : ℂ) * t ^ 2 + z * t + d)) =
        fun t : ℝ =>
          Complex.exp d *
            Complex.exp (-((4 * a : ℂ) / 2) * t ^ 2 + z * t) := by
    funext t
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  rw [hfun]
  have hI :
      (∫ t : ℝ,
          Complex.exp d *
            Complex.exp (-((4 * a : ℂ) / 2) * t ^ 2 + z * t)) =
        Complex.exp d *
          ∫ t : ℝ, Complex.exp (-((4 * a : ℂ) / 2) * t ^ 2 + z * t) :=
    MeasureTheory.integral_const_mul _ _
  rw [hI]
  have hgauss :
      (∫ t : ℝ, Complex.exp (-((4 * a : ℂ) / 2) * t ^ 2 + z * t)) =
        (Real.sqrt (2 * Real.pi / (4 * a)) : ℂ) *
          Complex.exp (z ^ 2 / (2 * (4 * a))) := by
    convert integral_cexp_neg_half_mul_sq_add (4 * a) h4 z using 2
    · ext t
      congr 1
      push_cast
      ring
    · push_cast
      ring
  rw [hgauss]
  have hsqrt :
      (Real.sqrt (2 * Real.pi / (4 * a)) : ℂ) =
        (Real.sqrt (Real.pi / (2 * a)) : ℂ) := by
    congr 1
    have : 2 * Real.pi / (4 * a) = Real.pi / (2 * a) := by
      field_simp [ha.ne']
      ring
    rw [this]
  have hz : z ^ 2 / (2 * (4 * a)) = z ^ 2 / (8 * a) := by
    field_simp [ha.ne']
    ring
  rw [hsqrt, hz]
  calc
    Complex.exp d *
        ((Real.sqrt (Real.pi / (2 * a)) : ℂ) * Complex.exp (z ^ 2 / (8 * a))) =
      (Real.sqrt (Real.pi / (2 * a)) : ℂ) *
        (Complex.exp d * Complex.exp (z ^ 2 / (8 * a))) := by
      ring
    _ = (Real.sqrt (Real.pi / (2 * a)) : ℂ) *
        Complex.exp (d + z ^ 2 / (8 * a)) := by
      rw [← Complex.exp_add]

theorem integrable_cexp_neg_two_a_sq_add
    (a : ℝ) (ha : 0 < a) (z d : ℂ) :
    Integrable fun t : ℝ =>
      Complex.exp (-(2 * a : ℂ) * t ^ 2 + z * t + d) := by
  have h4 : 0 < 4 * a := mul_pos (by norm_num) ha
  have hfun :
      (fun t : ℝ => Complex.exp (-(2 * a : ℂ) * t ^ 2 + z * t + d)) =
        fun t : ℝ =>
          Complex.exp d *
            Complex.exp (-((4 * a : ℂ) / 2) * t ^ 2 + z * t) := by
    funext t
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  rw [hfun]
  convert (integrable_cexp_neg_half_mul_sq_add (4 * a) h4 z).const_mul (Complex.exp d) using 1
  ext t
  congr 1
  push_cast
  ring

/-! ## Completing the square on the four frequencies -/

theorem gabor_acf_phase_pp (a omega u : ℝ) (ha : a ≠ 0) :
    (-(a * u ^ 2 : ℂ) - Complex.I * omega * u) +
        ((2 * a * u : ℂ) + (2 : ℂ) * Complex.I * omega) ^ 2 / (8 * a) =
      (-(a : ℂ) * u ^ 2 / 2) - (omega : ℂ) ^ 2 / (2 * a) := by
  field_simp [ha]
  ring_nf
  simp [Complex.I_sq]
  ring

theorem gabor_acf_phase_p0 (a omega u : ℝ) (ha : a ≠ 0) :
    (-(a * u ^ 2 : ℂ) + Complex.I * omega * u) +
        (2 * a * u : ℂ) ^ 2 / (8 * a) =
      (-(a : ℂ) * u ^ 2 / 2) + Complex.I * omega * u := by
  field_simp [ha]
  ring

theorem gabor_acf_phase_m0 (a omega u : ℝ) (ha : a ≠ 0) :
    (-(a * u ^ 2 : ℂ) - Complex.I * omega * u) +
        (2 * a * u : ℂ) ^ 2 / (8 * a) =
      (-(a : ℂ) * u ^ 2 / 2) - Complex.I * omega * u := by
  field_simp [ha]
  ring

theorem gabor_acf_phase_mm (a omega u : ℝ) (ha : a ≠ 0) :
    (-(a * u ^ 2 : ℂ) + Complex.I * omega * u) +
        ((2 * a * u : ℂ) - (2 : ℂ) * Complex.I * omega) ^ 2 / (8 * a) =
      (-(a : ℂ) * u ^ 2 / 2) - (omega : ℂ) ^ 2 / (2 * a) := by
  field_simp [ha]
  ring_nf
  simp [Complex.I_sq]
  ring

/-! ## Integrability of the real ACF integrand -/

theorem integrable_gabor_acf
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (u : ℝ) :
    Integrable fun t : ℝ => F.carrier t * F.carrier (t - u) := by
  have ha : 0 < F.a := F.a_pos
  have hmajC :=
    integrable_cexp_neg_two_a_sq_add F.a ha (2 * F.a * u : ℂ) (-(F.a * u ^ 2 : ℂ))
  have hmaj : Integrable fun t : ℝ =>
      ‖Complex.exp
        (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
          (-(F.a * u ^ 2 : ℂ)))‖ :=
    hmajC.norm
  have hbd : ∀ t : ℝ,
      ‖(F.carrier t * F.carrier (t - u) : ℝ)‖ ≤
        ‖Complex.exp
          (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
            (-(F.a * u ^ 2 : ℂ)))‖ := by
    intro t
    have hle : |F.carrier t * F.carrier (t - u)| ≤
        Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) := by
      have hc1 := gabor_carrier_of_pure hF t
      have hc2 := gabor_carrier_of_pure hF (t - u)
      have h1 : |F.carrier t| ≤ Real.exp (-F.a * t ^ 2) := by
        rw [hc1, abs_mul, abs_of_pos (Real.exp_pos _)]
        exact mul_le_of_le_one_right (Real.exp_pos _).le (Real.abs_cos_le_one _)
      have h2 : |F.carrier (t - u)| ≤ Real.exp (-F.a * (t - u) ^ 2) := by
        rw [hc2, abs_mul, abs_of_pos (Real.exp_pos _)]
        exact mul_le_of_le_one_right (Real.exp_pos _).le (Real.abs_cos_le_one _)
      rw [abs_mul]
      exact mul_le_mul h1 h2 (abs_nonneg _) (Real.exp_pos _).le
    have hre :
        Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) =
          ‖Complex.exp
            (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
              (-(F.a * u ^ 2 : ℂ)))‖ := by
      have hc := ofReal_gabor_gauss_product F.a u t
      have hsub :
          (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t - (F.a * u ^ 2 : ℂ)) =
            (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
              (-(F.a * u ^ 2 : ℂ))) := by
        ring
      have hz : ((Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) : ℝ) : ℂ) =
          Complex.exp
            (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
              (-(F.a * u ^ 2 : ℂ))) := by
        rw [hc, hsub]
      have hpos : 0 <
          Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) :=
        mul_pos (Real.exp_pos _) (Real.exp_pos _)
      calc
        Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) =
            |Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2)| :=
          (abs_of_pos hpos).symm
        _ = ‖((Real.exp (-F.a * t ^ 2) * Real.exp (-F.a * (t - u) ^ 2) : ℝ) : ℂ)‖ :=
          (Complex.norm_real _).symm
        _ = ‖Complex.exp
              (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
                (-(F.a * u ^ 2 : ℂ)))‖ :=
          congrArg (fun z : ℂ => ‖z‖) hz
    simpa [Real.norm_eq_abs] using hle.trans_eq hre
  exact hmaj.mono'
    (Continuous.aestronglyMeasurable (by
      simp_rw [gabor_carrier_of_pure hF]
      fun_prop))
    (Eventually.of_forall hbd)


theorem integral_add4 {f g h k : ℝ → ℂ}
    (hf : Integrable f) (hg : Integrable g) (hh : Integrable h) (hk : Integrable k) :
    (∫ x : ℝ, f x + g x + h x + k x) =
      (∫ x, f x) + (∫ x, g x) + (∫ x, h x) + (∫ x, k x) := by
  have hfg : Integrable (f + g) := hf.add hg
  have hfgh : Integrable (f + g + h) := hfg.add hh
  have h4 : (fun x : ℝ => f x + g x + h x + k x) =
      fun x => (f + g + h) x + k x := rfl
  have h3 : (fun x : ℝ => (f + g + h) x) =
      fun x => (f + g) x + h x := rfl
  have h2 : (fun x : ℝ => (f + g) x) = fun x => f x + g x := rfl
  rw [h4, integral_add hfgh hk, h3, integral_add hfg hh, h2, integral_add hf hg]

/-! ## Closed form via ofReal / four Gaussians -/

theorem gabor_autocorrelation_eq_pure_complex
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (u : ℝ) :
    (gaborAutocorrelation F u : ℂ) =
      (pureGaborAutocorrelation F.a F.omega u : ℂ) := by
  have ha : 0 < F.a := F.a_pos
  have ha0 : F.a ≠ 0 := ne_of_gt ha
  have hlift :
      (gaborAutocorrelation F u : ℂ) =
        ∫ t : ℝ, ((F.carrier t * F.carrier (t - u) : ℝ) : ℂ) := by
    unfold gaborAutocorrelation
    exact (integral_ofReal (f := fun t : ℝ => F.carrier t * F.carrier (t - u))).symm
  have hpt : ∀ t : ℝ,
      ((F.carrier t * F.carrier (t - u) : ℝ) : ℂ) =
        ((Real.exp (-F.a * t ^ 2) * Real.cos (F.omega * t) *
            Real.exp (-F.a * (t - u) ^ 2) * Real.cos (F.omega * (t - u)) : ℝ) : ℂ) := by
    intro t
    simp [gabor_carrier_of_pure hF, mul_assoc]
  rw [hlift, integral_congr_ae (Eventually.of_forall hpt)]
  simp_rw [gabor_acf_integrand_four_cexp F.a F.omega u]
  set zpp : ℂ := (2 * F.a * u : ℂ) + (2 : ℂ) * Complex.I * F.omega
  set zmm : ℂ := (2 * F.a * u : ℂ) - (2 : ℂ) * Complex.I * F.omega
  set z0 : ℂ := (2 * F.a * u : ℂ)
  set dpp : ℂ := -(F.a * u ^ 2 : ℂ) - Complex.I * F.omega * u
  set dp0 : ℂ := -(F.a * u ^ 2 : ℂ) + Complex.I * F.omega * u
  set dm0 : ℂ := -(F.a * u ^ 2 : ℂ) - Complex.I * F.omega * u
  set dmm : ℂ := -(F.a * u ^ 2 : ℂ) + Complex.I * F.omega * u
  have hpp := integrable_cexp_neg_two_a_sq_add F.a ha zpp dpp
  have hp0 := integrable_cexp_neg_two_a_sq_add F.a ha z0 dp0
  have hm0 := integrable_cexp_neg_two_a_sq_add F.a ha z0 dm0
  have hmm := integrable_cexp_neg_two_a_sq_add F.a ha zmm dmm
  have hfun :
      (fun t : ℝ =>
          (1 / 4 : ℂ) *
            (Complex.exp (-(2 * F.a : ℂ) * t ^ 2 +
                ((2 * F.a * u : ℂ) + (2 : ℂ) * Complex.I * F.omega) * t +
                (-(F.a * u ^ 2 : ℂ) - Complex.I * F.omega * u)) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
                (-(F.a * u ^ 2 : ℂ) + Complex.I * F.omega * u)) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + (2 * F.a * u : ℂ) * t +
                (-(F.a * u ^ 2 : ℂ) - Complex.I * F.omega * u)) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 +
                ((2 * F.a * u : ℂ) - (2 : ℂ) * Complex.I * F.omega) * t +
                (-(F.a * u ^ 2 : ℂ) + Complex.I * F.omega * u)))) =
        fun t : ℝ =>
          (1 / 4 : ℂ) *
            (Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zmm * t + dmm)) := by
    funext t
    dsimp [zpp, zmm, z0, dpp, dp0, dm0, dmm]
  rw [hfun]
  have h123 : Integrable fun t : ℝ =>
      Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp) +
        Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0) +
        Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0) :=
    (hpp.add hp0).add hm0
  have hsplit :
      (∫ t : ℝ,
          (1 / 4 : ℂ) *
            (Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0) +
              Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zmm * t + dmm))) =
        (1 / 4 : ℂ) *
          ((∫ t : ℝ, Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp)) +
            (∫ t : ℝ, Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0)) +
            (∫ t : ℝ, Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0)) +
            (∫ t : ℝ, Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zmm * t + dmm))) := by
    have hI :
        (∫ t : ℝ,
            (1 / 4 : ℂ) *
              (Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zmm * t + dmm))) =
          (1 / 4 : ℂ) *
            ∫ t : ℝ,
              (Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zpp * t + dpp) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dp0) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + z0 * t + dm0) +
                Complex.exp (-(2 * F.a : ℂ) * t ^ 2 + zmm * t + dmm)) :=
      MeasureTheory.integral_const_mul (μ := volume) (1 / 4 : ℂ) _
    rw [hI, integral_add4 hpp hp0 hm0 hmm]
  rw [hsplit, integral_cexp_neg_two_a_sq_add F.a ha zpp dpp,
    integral_cexp_neg_two_a_sq_add F.a ha z0 dp0,
    integral_cexp_neg_two_a_sq_add F.a ha z0 dm0,
    integral_cexp_neg_two_a_sq_add F.a ha zmm dmm]
  have hsum :
      Complex.exp (dpp + zpp ^ 2 / (8 * F.a)) +
          Complex.exp (dp0 + z0 ^ 2 / (8 * F.a)) +
          Complex.exp (dm0 + z0 ^ 2 / (8 * F.a)) +
          Complex.exp (dmm + zmm ^ 2 / (8 * F.a)) =
        Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - (F.omega : ℂ) ^ 2 / (2 * F.a)) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) + Complex.I * F.omega * u) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - Complex.I * F.omega * u) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - (F.omega : ℂ) ^ 2 / (2 * F.a)) := by
    dsimp [zpp, zmm, z0, dpp, dp0, dm0, dmm]
    rw [gabor_acf_phase_pp F.a F.omega u ha0, gabor_acf_phase_p0 F.a F.omega u ha0,
      gabor_acf_phase_m0 F.a F.omega u ha0, gabor_acf_phase_mm F.a F.omega u ha0]
  have hfactor :
      (1 / 4 : ℂ) *
          ((Real.sqrt (Real.pi / (2 * F.a)) : ℂ) *
              Complex.exp (dpp + zpp ^ 2 / (8 * F.a)) +
            (Real.sqrt (Real.pi / (2 * F.a)) : ℂ) *
              Complex.exp (dp0 + z0 ^ 2 / (8 * F.a)) +
            (Real.sqrt (Real.pi / (2 * F.a)) : ℂ) *
              Complex.exp (dm0 + z0 ^ 2 / (8 * F.a)) +
            (Real.sqrt (Real.pi / (2 * F.a)) : ℂ) *
              Complex.exp (dmm + zmm ^ 2 / (8 * F.a))) =
        (Real.sqrt (Real.pi / (2 * F.a)) : ℂ) / 4 *
          (Complex.exp (dpp + zpp ^ 2 / (8 * F.a)) +
            Complex.exp (dp0 + z0 ^ 2 / (8 * F.a)) +
            Complex.exp (dm0 + z0 ^ 2 / (8 * F.a)) +
            Complex.exp (dmm + zmm ^ 2 / (8 * F.a))) := by
    ring
  rw [hfactor, hsum]
  have hw :
      Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - (F.omega : ℂ) ^ 2 / (2 * F.a)) =
        Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
          Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) := by
    rw [sub_eq_add_neg, Complex.exp_add]
    congr 2
    ring
  have hcos :
      Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) + Complex.I * F.omega * u) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - Complex.I * F.omega * u) =
        Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
          (Complex.exp (Complex.I * F.omega * u) +
            Complex.exp (-(Complex.I * F.omega * u))) := by
    rw [sub_eq_add_neg, Complex.exp_add, Complex.exp_add]
    ring
  have hsum' :
      Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - (F.omega : ℂ) ^ 2 / (2 * F.a)) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) + Complex.I * F.omega * u) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - Complex.I * F.omega * u) +
          Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - (F.omega : ℂ) ^ 2 / (2 * F.a)) =
        Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
          (2 * Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) +
            Complex.exp (Complex.I * F.omega * u) +
            Complex.exp (-(Complex.I * F.omega * u))) := by
    rw [hw]
    have hrearr :
        Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
              Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) +
            Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) + Complex.I * F.omega * u) +
            Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - Complex.I * F.omega * u) +
            Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
              Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) =
          (Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) + Complex.I * F.omega * u) +
              Complex.exp ((-(F.a : ℂ) * u ^ 2 / 2) - Complex.I * F.omega * u)) +
            2 * (Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) *
              Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a))) := by
      ring
    rw [hrearr, hcos]
    ring
  rw [hsum']
  have hcosR :
      Complex.exp (Complex.I * F.omega * u) +
          Complex.exp (-(Complex.I * F.omega * u)) =
        (2 : ℂ) * (Real.cos (F.omega * u) : ℂ) := by
    have h := ofReal_cos_eq_half_exp_add_exp_neg (F.omega * u)
    have hI :
        ((F.omega * u : ℝ) : ℂ) * Complex.I = Complex.I * F.omega * u := by
      push_cast
      ring
    have hI' :
        -((F.omega * u : ℝ) : ℂ) * Complex.I = -(Complex.I * F.omega * u) := by
      push_cast
      ring
    rw [hI, hI'] at h
    rw [h]
    ring
  have hinner :
      2 * Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) +
          Complex.exp (Complex.I * F.omega * u) +
          Complex.exp (-(Complex.I * F.omega * u)) =
        2 * Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) +
          (2 : ℂ) * (Real.cos (F.omega * u) : ℂ) := by
    rw [add_assoc, hcosR]
  rw [hinner]
  have hwR :
      Complex.exp (-(F.omega : ℂ) ^ 2 / (2 * F.a)) =
        (Real.exp (-F.omega ^ 2 / (2 * F.a)) : ℂ) := by
    rw [Complex.ofReal_exp]
    congr 1
    push_cast
    ring
  have huR :
      Complex.exp (-(F.a : ℂ) * u ^ 2 / 2) =
        (Real.exp (-F.a * u ^ 2 / 2) : ℂ) := by
    rw [Complex.ofReal_exp]
    congr 1
    push_cast
    ring
  rw [hwR, huR]
  unfold pureGaborAutocorrelation
  push_cast
  ring

theorem gabor_autocorrelation_eq_pure
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (u : ℝ) :
    gaborAutocorrelation F u = pureGaborAutocorrelation F.a F.omega u :=
  Complex.ofReal_injective (gabor_autocorrelation_eq_pure_complex hF u)

theorem gaborAutocorrelationClosedForm_holds : GaborAutocorrelationClosedForm :=
  fun _F hF u => gabor_autocorrelation_eq_pure hF u


/-! ## `n^{-1/2} = 1/√n` and half-comb real part -/

theorem nat_cpow_neg_half {n : ℕ} (hn : n ≠ 0) :
    (n : ℂ) ^ (-(1 / 2 : ℂ)) = ((1 / Real.sqrt n : ℝ) : ℂ) := by
  have hn0 : 0 < (n : ℝ) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn)
  rw [← exp_neg_half_log_nat hn]
  have hmul : -((1 / 2 : ℂ) * (Real.log n : ℂ)) =
      ((-(1 / 2 : ℝ) * Real.log n : ℝ) : ℂ) := by
    have hhalf : (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) := by norm_num
    rw [hhalf, neg_mul]
    push_cast
    ring
  rw [hmul, ← Complex.ofReal_exp]
  have hr : Real.exp (-(1 / 2) * Real.log n) = 1 / Real.sqrt n := by
    have hneg : (n : ℝ) ^ (-(1 / 2 : ℝ)) = 1 / Real.sqrt n := by
      rw [Real.rpow_neg hn0.le, ← Real.sqrt_eq_rpow, inv_eq_one_div]
    rw [← hneg, Real.rpow_def_of_pos hn0]
    congr 1
    ring
  rw [hr]

theorem gabor_halfPrimeComb_term_re
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (n : ℕ) :
    ((ArithmeticFunction.vonMangoldt n : ℂ) *
        (if n = 0 then 0 else
          (n : ℂ) ^ (-(1 / 2 : ℂ)) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ))).re =
      combMass n * gaborAutocorrelation F (Real.log n) / 2 := by
  rw [gabor_autocorrelation_eq_pure hF]
  rcases eq_or_ne n 0 with rfl | hn
  · simp [combMass]
  · rw [if_neg hn, nat_cpow_neg_half hn]
    have hmul :
        (ArithmeticFunction.vonMangoldt n : ℂ) *
            (((1 / Real.sqrt n : ℝ) : ℂ) *
              (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ)) =
          (((ArithmeticFunction.vonMangoldt n * (1 / Real.sqrt n) *
              pureGaborAutocorrelation F.a F.omega (Real.log n) : ℝ) : ℂ)) := by
      push_cast
      ring
    rw [hmul, Complex.ofReal_re]
    unfold combMass
    have hsqrt : Real.sqrt n ≠ 0 := (Real.sqrt_pos.mpr
      (Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn))).ne'
    field_simp [hsqrt]

/-- `x √x exp(-a (log x)² / 2) ≤ exp(9/(8a))` by completing the square. -/
theorem sqrt_cube_mul_gauss_le (a : ℝ) (ha : 0 < a) {x : ℝ} (hx : 0 < x) :
    x * Real.sqrt x * Real.exp (-a * (Real.log x) ^ 2 / 2) ≤
      Real.exp (9 / (8 * a)) := by
  have hxlog : x = Real.exp (Real.log x) := (Real.exp_log hx).symm
  have hsqrt : Real.sqrt x = Real.exp (Real.log x / 2) := by
    rw [Real.sqrt_eq_rpow, Real.rpow_def_of_pos hx]
    ring_nf
  rw [hsqrt, hxlog, Real.log_exp]
  rw [← Real.exp_add, ← Real.exp_add]
  refine Real.exp_le_exp.mpr ?_
  have hdiff :
      9 / (8 * a) - (Real.log x + Real.log x / 2 + -a * (Real.log x) ^ 2 / 2) =
        (2 * a * Real.log x - 3) ^ 2 / (8 * a) := by
    field_simp [ha.ne']
    ring
  refine le_of_sub_nonneg ?_
  rw [hdiff]
  exact div_nonneg (sq_nonneg _) (mul_nonneg (by norm_num) ha.le)

theorem norm_LSeries_term_vonMangoldt_two (n : ℕ) :
    ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ =
      if n = 0 then 0 else
        ArithmeticFunction.vonMangoldt n / (n : ℝ) ^ 2 := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    have hn0 : 0 < (n : ℝ) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn)
    have hden : (0 : ℝ) < (n : ℝ) ^ 2 := pow_pos hn0 2
    have key :
        ‖(ArithmeticFunction.vonMangoldt n : ℂ) / (n : ℂ) ^ 2‖ =
          ArithmeticFunction.vonMangoldt n / (n : ℝ) ^ 2 := by
      rw [← Complex.ofReal_natCast, ← Complex.ofReal_pow, ← Complex.ofReal_div,
        Complex.norm_real, Real.norm_eq_abs,
        abs_of_nonneg (div_nonneg hΛ hden.le)]
    rw [if_neg hn]
    simpa [LSeries.term_of_ne_zero hn] using key

theorem norm_gabor_halfPrimeComb_term_le_LSeries
    (F : GaborWeilTest) (n : ℕ) :
    ‖(ArithmeticFunction.vonMangoldt n : ℂ) *
        (if n = 0 then 0 else
          (n : ℂ) ^ (-(1 / 2 : ℂ)) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ))‖ ≤
      (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
          (1 + Real.exp (-F.omega ^ 2 / (2 * F.a))) *
          Real.exp (9 / (8 * F.a))) *
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have ha : 0 < F.a := F.a_pos
    have hn0 : 0 < (n : ℝ) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn)
    have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    have hK :
        0 ≤ Real.sqrt (Real.pi / (2 * F.a)) / 2 *
          (1 + Real.exp (-F.omega ^ 2 / (2 * F.a))) := by positivity
    have hg :=
      norm_pureGaborAutocorrelation_le F.a F.omega (Real.log n) ha
    rw [if_neg hn, nat_cpow_neg_half hn, Complex.norm_mul, Complex.norm_mul,
      Complex.norm_real, Complex.norm_real, Real.norm_eq_abs, Real.norm_eq_abs,
      abs_of_nonneg hΛ,
      abs_of_nonneg (div_nonneg (by norm_num : (0 : ℝ) ≤ 1) (Real.sqrt_nonneg _))]
    rw [norm_LSeries_term_vonMangoldt_two, if_neg hn]
    have hLHS :
        ArithmeticFunction.vonMangoldt n *
            (1 / Real.sqrt n *
              ‖(pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ)‖) =
          ArithmeticFunction.vonMangoldt n / Real.sqrt n *
            |pureGaborAutocorrelation F.a F.omega (Real.log n)| := by
      rw [Complex.norm_real, Real.norm_eq_abs]
      ring
    rw [hLHS]
    have hcube := sqrt_cube_mul_gauss_le F.a ha hn0
    have hsqrt : Real.sqrt n ≠ 0 := (Real.sqrt_pos.mpr hn0).ne'
    have hn2 : (n : ℝ) ≠ 0 := hn0.ne'
    have hrat : (n : ℝ) ^ 2 / Real.sqrt n = (n : ℝ) * Real.sqrt n := by
      have hsq : Real.sqrt n * Real.sqrt n = (n : ℝ) :=
        Real.mul_self_sqrt hn0.le
      calc (n : ℝ) ^ 2 / Real.sqrt n
          = ((n : ℝ) * (n : ℝ)) / Real.sqrt n := by ring
          _ = ((n : ℝ) * (Real.sqrt n * Real.sqrt n)) / Real.sqrt n := by
              rw [hsq]
          _ = (n : ℝ) * Real.sqrt n * (Real.sqrt n / Real.sqrt n) := by ring
          _ = (n : ℝ) * Real.sqrt n * 1 := by rw [div_self hsqrt]
          _ = (n : ℝ) * Real.sqrt n := by ring
    have hstep :
        ArithmeticFunction.vonMangoldt n / Real.sqrt n *
            |pureGaborAutocorrelation F.a F.omega (Real.log n)| ≤
          ArithmeticFunction.vonMangoldt n / Real.sqrt n *
            (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
              Real.exp (-F.a * (Real.log n) ^ 2 / 2) *
              (1 + Real.exp (-F.omega ^ 2 / (2 * F.a)))) :=
      mul_le_mul_of_nonneg_left hg (div_nonneg hΛ (Real.sqrt_nonneg _))
    refine hstep.trans ?_
    have hcmp :
        Real.exp (-F.a * (Real.log n) ^ 2 / 2) / Real.sqrt n ≤
          Real.exp (9 / (8 * F.a)) / (n : ℝ) ^ 2 := by
      have hdecomp : (n : ℝ) ^ 2 =
          Real.sqrt n * ((n : ℝ) * Real.sqrt n) := by
        calc (n : ℝ) ^ 2
            = Real.sqrt n * ((n : ℝ) ^ 2 / Real.sqrt n) := by
                field_simp [hsqrt]
            _ = Real.sqrt n * ((n : ℝ) * Real.sqrt n) := by rw [hrat]
      have hmul :
          (n : ℝ) ^ 2 * Real.exp (-F.a * (Real.log n) ^ 2 / 2) ≤
            Real.sqrt n * Real.exp (9 / (8 * F.a)) := by
        rw [hdecomp, mul_assoc]
        exact mul_le_mul_of_nonneg_left hcube (Real.sqrt_nonneg _)
      rw [div_le_div_iff₀ (Real.sqrt_pos.mpr hn0) (pow_pos hn0 2)]
      convert hmul using 1 <;> ring
    have hA :
        0 ≤ Real.sqrt (Real.pi / (2 * F.a)) / 2 := by positivity
    have hB :
        0 ≤ 1 + Real.exp (-F.omega ^ 2 / (2 * F.a)) := by positivity
    have hE : 0 ≤ Real.exp (9 / (8 * F.a)) := (Real.exp_pos _).le
    have hscale :
        ArithmeticFunction.vonMangoldt n / Real.sqrt n *
            (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
              Real.exp (-F.a * (Real.log n) ^ 2 / 2) *
              (1 + Real.exp (-F.omega ^ 2 / (2 * F.a)))) ≤
          (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
              (1 + Real.exp (-F.omega ^ 2 / (2 * F.a))) *
              Real.exp (9 / (8 * F.a))) *
            (ArithmeticFunction.vonMangoldt n / (n : ℝ) ^ 2) := by
      have hleft :
          ArithmeticFunction.vonMangoldt n / Real.sqrt n *
              (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
                Real.exp (-F.a * (Real.log n) ^ 2 / 2) *
                (1 + Real.exp (-F.omega ^ 2 / (2 * F.a)))) =
            (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
                (1 + Real.exp (-F.omega ^ 2 / (2 * F.a)))) *
              (ArithmeticFunction.vonMangoldt n *
                (Real.exp (-F.a * (Real.log n) ^ 2 / 2) / Real.sqrt n)) := by
        ring
      have hright :
          (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
              (1 + Real.exp (-F.omega ^ 2 / (2 * F.a))) *
              Real.exp (9 / (8 * F.a))) *
            (ArithmeticFunction.vonMangoldt n / (n : ℝ) ^ 2) =
            (Real.sqrt (Real.pi / (2 * F.a)) / 2 *
                (1 + Real.exp (-F.omega ^ 2 / (2 * F.a)))) *
              (ArithmeticFunction.vonMangoldt n *
                (Real.exp (9 / (8 * F.a)) / (n : ℝ) ^ 2)) := by
        ring
      rw [hleft, hright]
      refine mul_le_mul_of_nonneg_left ?_ (mul_nonneg hA hB)
      exact mul_le_mul_of_nonneg_left hcmp hΛ
    exact hscale

theorem summable_gabor_halfPrimeComb
    {F : GaborWeilTest} (_hF : F.coeffs = ⟨1, 0, 0⟩) :
    Summable fun n : ℕ =>
      (ArithmeticFunction.vonMangoldt n : ℂ) *
        (if n = 0 then 0 else
          (n : ℂ) ^ (-(1 / 2 : ℂ)) *
            (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ)) := by
  have h2 : 1 < (2 : ℂ).re := by simp
  have hΛ : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact ArithmeticFunction.LSeriesSummable_vonMangoldt h2
  set C : ℝ :=
    Real.sqrt (Real.pi / (2 * F.a)) / 2 *
      (1 + Real.exp (-F.omega ^ 2 / (2 * F.a))) *
      Real.exp (9 / (8 * F.a))
  refine Summable.of_norm_bounded (hΛ.mul_left C) ?_
  intro n
  simpa [C] using norm_gabor_halfPrimeComb_term_le_LSeries F n

theorem gabor_halfPrimeComb_re
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    (gaborHalfPrimeComb F).re = gaborPrimeComb F / 2 := by
  have hsum := summable_gabor_halfPrimeComb (F := F) hF
  unfold gaborHalfPrimeComb gaborPrimeComb
  rw [Complex.re_tsum hsum]
  set f : ℕ → ℂ := fun n =>
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      (if n = 0 then 0 else
        (n : ℂ) ^ (-(1 / 2 : ℂ)) *
          (pureGaborAutocorrelation F.a F.omega (Real.log n) : ℂ))
  have hsumRe : Summable fun n : ℕ => (f n).re := by
    change Summable (Complex.reCLM ∘ f)
    exact Complex.reCLM.summable hsum
  have hsumComb : Summable fun n : ℕ =>
      combMass n * gaborAutocorrelation F (Real.log n) := by
    refine (hsumRe.mul_right (2 : ℝ)).congr fun n => ?_
    change (f n).re * 2 = _
    rw [gabor_halfPrimeComb_term_re hF]
    ring
  have heq : (fun n : ℕ => (f n).re) =
      fun n : ℕ =>
        (combMass n * gaborAutocorrelation F (Real.log n)) * (1 / 2) := by
    ext n
    change (f n).re = _
    rw [gabor_halfPrimeComb_term_re hF]
    ring
  rw [heq, hsumComb.tsum_mul_right]
  ring

theorem gaborHalfCombReal_holds : GaborHalfCombReal :=
  fun _F hF => gabor_halfPrimeComb_re hF

#print axioms gaborAutocorrelationClosedForm_holds
#print axioms gaborHalfCombReal_holds
#print axioms gabor_autocorrelation_eq_pure
#print axioms gabor_halfPrimeComb_re

end RH
