/-
RH/GaborHatAnalytic.lean -- r555 analytic foundations of the Gabor
Weil-shifted transform `gaborHat`.

Brick 1 of the six-step scoping roadmap toward `GaborExplicitFormula`.
This file does not prove that identity.  It records entirety, the
functional-equation symmetry `ĥ_W(1-s) = ĥ_W(s)`, the pure three-lobe
bound, and Gaussian strip decay.

CLAIM BOUNDARY.  NO RH CLAIM.  Closed-form complex analysis of the
Gabor carrier only.  Sorry-free.

The live scaling tests (`scalingGaborTest`) are pure (`coeffs = ⟨1,0,0⟩`).
Entirety and FE-symmetry are proved for every even quartic.  The
three-lobe / strip bounds are proved for the pure specialization; the
quartic poly-in-t majorant `C(σ)·(1+|t|)^8·threeLobe` is the r587
theorem `gaborHatQuarticThreeLobeRemainder_holds`.
-/
import RH.GaborSeparation
import Mathlib.Analysis.Calculus.FDeriv.Add
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.Calculus.FDeriv.Pow
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

namespace RH

open Complex Set

/-! ## Holomorphic closed form of the pure packet -/

/-- Entire representative of `pureGaborHatDelta`: three complex
Gaussians, no `.re`/`.im` splitting. -/
noncomputable def pureGaborHatHolomorphic (a omega : ℝ) (δ : ℂ) : ℂ :=
  ((Real.pi / (4 * a) : ℝ) : ℂ) *
    (Complex.exp ((δ + Complex.I * omega) ^ 2 / (2 * a)) +
      Complex.exp ((δ - Complex.I * omega) ^ 2 / (2 * a)) +
      2 * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (δ ^ 2 / (2 * a)))

/-- Amplitude/phase expansion equals the entire representative. -/
theorem pureGaborHatHolomorphic_eq_delta
    (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    pureGaborHatHolomorphic a omega δ = pureGaborHatDelta a omega δ := by
  unfold pureGaborHatHolomorphic
  rw [cexp_square_shift_split a omega (ne_of_gt ha) δ]
  have hminus := cexp_square_shift_split a (-omega) (ne_of_gt ha) δ
  rw [show δ - Complex.I * (omega : ℂ) =
      δ + Complex.I * (-omega : ℝ) by push_cast; ring]
  rw [hminus]
  simp only [sub_eq_add_neg, Complex.ofReal_neg]
  rw [show
    2 * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (δ ^ 2 / (2 * a)) =
      2 * (Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (δ ^ 2 / (2 * a))) by ring]
  rw [cexp_neg_frequency_mul_square_split a omega (ne_of_gt ha) δ]
  unfold pureGaborHatDelta
  ring

theorem pureGaborHatDelta_eq_holomorphic
    (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    pureGaborHatDelta a omega δ = pureGaborHatHolomorphic a omega δ :=
  (pureGaborHatHolomorphic_eq_delta a omega ha δ).symm

theorem gaborHat_of_pure
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (s : ℂ) :
    gaborHat F s = pureGaborHatDelta F.a F.omega (s - (1 / 2 : ℂ)) := by
  unfold gaborHat
  simp [hF]

theorem gaborHat_of_not_pure
    {F : GaborWeilTest} (hF : F.coeffs ≠ ⟨1, 0, 0⟩) (s : ℂ) :
    gaborHat F s =
      gaborLaplace F (s - (1 / 2 : ℂ)) *
        gaborLaplace F (-(s - (1 / 2 : ℂ))) := by
  unfold gaborHat
  simp [hF]

theorem gaborHat_eq_pureHolomorphic
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (s : ℂ) :
    gaborHat F s =
      pureGaborHatHolomorphic F.a F.omega (s - (1 / 2 : ℂ)) := by
  rw [gaborHat_of_pure hF, pureGaborHatDelta_eq_holomorphic _ _ F.a_pos]

/-! ## Entirety -/

theorem differentiable_id_sub_half :
    Differentiable ℂ fun s : ℂ => s - (1 / 2 : ℂ) :=
  differentiable_id.sub (differentiable_const _)

@[fun_prop]
theorem differentiable_pureGaborHatHolomorphic
    (a omega : ℝ) (_ha : 0 < a) :
    Differentiable ℂ (pureGaborHatHolomorphic a omega) :=
  fun _ => by
    unfold pureGaborHatHolomorphic
    fun_prop

@[fun_prop]
theorem differentiable_gaussianPolynomialFactor
    (p : EvenQuartic) (a : ℝ) :
    Differentiable ℂ (gaussianPolynomialFactor p a) :=
  fun _ => by
    unfold gaussianPolynomialFactor
    fun_prop

@[fun_prop]
theorem differentiable_gaussianLaplace (p : EvenQuartic) (a : ℝ) :
    Differentiable ℂ (gaussianLaplace p a) :=
  fun _ => by
    unfold gaussianLaplace
    fun_prop

@[fun_prop]
theorem differentiable_gaborLaplace (F : GaborWeilTest) :
    Differentiable ℂ (gaborLaplace F) :=
  fun _ => by
    unfold gaborLaplace
    fun_prop

/-- `gaborHat F` is entire.  Pure packets use the three-exponential
closed form; general even quartics use the algebraic Laplace product. -/
theorem differentiable_gaborHat (F : GaborWeilTest) :
    Differentiable ℂ (gaborHat F) := by
  classical
  by_cases hF : F.coeffs = ⟨1, 0, 0⟩
  · have hfun :
        gaborHat F = fun s =>
          pureGaborHatHolomorphic F.a F.omega (s - (1 / 2 : ℂ)) := by
      funext s
      exact gaborHat_eq_pureHolomorphic hF s
    rw [hfun]
    exact (differentiable_pureGaborHatHolomorphic F.a F.omega F.a_pos).comp
      differentiable_id_sub_half
  · have hfun :
        gaborHat F = fun s =>
          gaborLaplace F (s - (1 / 2 : ℂ)) *
            gaborLaplace F (-(s - (1 / 2 : ℂ))) := by
      funext s
      exact gaborHat_of_not_pure hF s
    rw [hfun]
    refine (differentiable_gaborLaplace F).comp differentiable_id_sub_half
      |>.mul ?_
    exact (differentiable_gaborLaplace F).comp
      (differentiable_id_sub_half.neg)

theorem analyticOnNhd_gaborHat (F : GaborWeilTest) :
    AnalyticOnNhd ℂ (gaborHat F) univ :=
  analyticOnNhd_univ_iff_differentiable.mpr (differentiable_gaborHat F)

theorem analyticAt_gaborHat (F : GaborWeilTest) (s : ℂ) :
    AnalyticAt ℂ (gaborHat F) s :=
  analyticOnNhd_gaborHat F s (mem_univ s)

/-! ## Functional-equation symmetry `ĥ_W(1-s) = ĥ_W(s)` -/

theorem pureGaborHatHolomorphic_neg
    (a omega : ℝ) (δ : ℂ) :
    pureGaborHatHolomorphic a omega (-δ) =
      pureGaborHatHolomorphic a omega δ := by
  unfold pureGaborHatHolomorphic
  have hp : (-δ + Complex.I * omega) ^ 2 = (δ - Complex.I * omega) ^ 2 := by
    ring
  have hm : (-δ - Complex.I * omega) ^ 2 = (δ + Complex.I * omega) ^ 2 := by
    ring
  have hs : (-δ) ^ 2 = δ ^ 2 := by ring
  rw [hp, hm, hs]
  ring

theorem gaborHat_one_sub (F : GaborWeilTest) (s : ℂ) :
    gaborHat F (1 - s) = gaborHat F s := by
  classical
  have hδ : (1 - s) - (1 / 2 : ℂ) = -(s - (1 / 2 : ℂ)) := by ring
  by_cases hF : F.coeffs = ⟨1, 0, 0⟩
  · rw [gaborHat_eq_pureHolomorphic hF, gaborHat_eq_pureHolomorphic hF]
    rw [hδ, pureGaborHatHolomorphic_neg]
  · rw [gaborHat_of_not_pure hF, gaborHat_of_not_pure hF, hδ, neg_neg]
    rw [mul_comm]

lemma eq_pureGaborTest
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    F = pureGaborTest F.a F.omega F.a_pos := by
  rcases F with ⟨a, omega, coeffs, a_pos⟩
  subst hF
  rfl

/-- r600: critical-line nonnegativity for every pure packet
(`coeffs = ⟨1,0,0⟩`).  Quartic remainder is not needed by the
live separators (`scalingGaborTest` / `pureGaborTest`). -/
theorem gaborHat_criticalLine_nonneg
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (t : ℝ) :
    0 ≤ (gaborHat F ((1 / 2 : ℂ) + t * I)).re := by
  rw [eq_pureGaborTest hF]
  exact gaborHat_criticalLine_nonneg_pure F.a F.omega t F.a_pos

/-- r600: pole term `Re ĥ_W(1)` nonnegative for every pure packet. -/
theorem gaborHat_one_nonneg
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    0 ≤ (gaborHat F 1).re := by
  rw [eq_pureGaborTest hF]
  exact gaborHat_one_nonneg_pure F.a F.omega F.a_pos

/-! ## Three-lobe bound (pure specialization) -/

/-- The three nonnegative Gaussian lobes of a pure packet. -/
noncomputable def gaborThreeLobe (a omega t : ℝ) : ℝ :=
  Real.exp (-(t - omega) ^ 2 / (2 * a)) +
    Real.exp (-(t + omega) ^ 2 / (2 * a)) +
    2 * Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a))

/-- Explicit strip prefactor `C(a,σ) = (π/(4a)) exp((σ-1/2)²/(2a))`. -/
noncomputable def gaborHatThreeLobeConst (a σ : ℝ) : ℝ :=
  Real.pi / (4 * a) * Real.exp ((σ - 1 / 2) ^ 2 / (2 * a))

theorem gaborThreeLobe_nonneg (a omega t : ℝ) :
    0 ≤ gaborThreeLobe a omega t := by
  unfold gaborThreeLobe
  positivity

theorem gaborHatThreeLobeConst_nonneg (a σ : ℝ) (ha : 0 < a) :
    0 ≤ gaborHatThreeLobeConst a σ := by
  unfold gaborHatThreeLobeConst
  positivity

theorem norm_cexp_square_shift
    (a nu : ℝ) (ha : 0 < a) (z : ℂ) :
    ‖Complex.exp ((z + Complex.I * nu) ^ 2 / (2 * a))‖ =
      Real.exp ((z.re ^ 2 - (z.im + nu) ^ 2) / (2 * a)) := by
  rw [cexp_square_shift_split a nu (ne_of_gt ha) z, norm_mul]
  have hamp :
      ‖((Real.exp ((z.re ^ 2 - (z.im + nu) ^ 2) / (2 * a)) : ℝ) : ℂ)‖ =
        Real.exp ((z.re ^ 2 - (z.im + nu) ^ 2) / (2 * a)) :=
    Complex.norm_of_nonneg (Real.exp_pos _).le
  have hph :
      ‖Complex.exp (Complex.I * (z.re * (z.im + nu) / a))‖ = 1 := by
    rw [Complex.norm_exp]
    have : (Complex.I * (z.re * (z.im + nu) / a : ℂ)).re = 0 := by
      simp [mul_re, I_re, I_im]
    rw [this, Real.exp_zero]
  rw [hamp, hph, mul_one]

theorem norm_cexp_neg_frequency_mul_square
    (a omega : ℝ) (ha : 0 < a) (z : ℂ) :
    ‖Complex.exp (-(omega : ℂ) ^ 2 / (2 * a)) *
        Complex.exp (z ^ 2 / (2 * a))‖ =
      Real.exp ((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a)) := by
  rw [cexp_neg_frequency_mul_square_split a omega (ne_of_gt ha) z, norm_mul]
  have hamp :
      ‖((Real.exp ((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a)) : ℝ) : ℂ)‖ =
        Real.exp ((z.re ^ 2 - z.im ^ 2 - omega ^ 2) / (2 * a)) :=
    Complex.norm_of_nonneg (Real.exp_pos _).le
  have hph :
      ‖Complex.exp (Complex.I * (z.re * z.im / a))‖ = 1 := by
    rw [Complex.norm_exp]
    have : (Complex.I * (z.re * z.im / a : ℂ)).re = 0 := by
      simp [mul_re, I_re, I_im]
    rw [this, Real.exp_zero]
  rw [hamp, hph, mul_one]

theorem exp_re_sq_split (a x y : ℝ) (ha : 0 < a) :
    Real.exp ((x ^ 2 - y ^ 2) / (2 * a)) =
      Real.exp (x ^ 2 / (2 * a)) * Real.exp (-y ^ 2 / (2 * a)) := by
  rw [← Real.exp_add]
  congr 1
  field_simp [ne_of_gt ha]
  ring

theorem norm_pureGaborHatHolomorphic_le_three_lobe
    (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    ‖pureGaborHatHolomorphic a omega δ‖ ≤
      gaborHatThreeLobeConst a (δ.re + 1 / 2) * gaborThreeLobe a omega δ.im := by
  have hpre :
      gaborHatThreeLobeConst a (δ.re + 1 / 2) =
        Real.pi / (4 * a) * Real.exp (δ.re ^ 2 / (2 * a)) := by
    unfold gaborHatThreeLobeConst
    simp
  rw [hpre]
  unfold pureGaborHatHolomorphic
  set C : ℂ := ((Real.pi / (4 * a) : ℝ) : ℂ)
  have hC : ‖C‖ = Real.pi / (4 * a) := by
    change ‖((Real.pi / (4 * a) : ℝ) : ℂ)‖ = Real.pi / (4 * a)
    exact Complex.norm_of_nonneg (div_pos Real.pi_pos (by positivity)).le
  have hn1 := norm_cexp_square_shift a omega ha δ
  have hn2 : ‖Complex.exp ((δ - Complex.I * omega) ^ 2 / (2 * a))‖ =
      Real.exp ((δ.re ^ 2 - (δ.im - omega) ^ 2) / (2 * a)) := by
    have h := norm_cexp_square_shift a (-omega) ha δ
    have harg : δ - Complex.I * (omega : ℂ) =
        δ + Complex.I * (-omega : ℝ) := by push_cast; ring
    simpa [harg, sub_eq_add_neg, Complex.ofReal_neg] using h
  have hn3 := norm_cexp_neg_frequency_mul_square a omega ha δ
  set e1 := Complex.exp ((δ + Complex.I * omega) ^ 2 / (2 * a))
  set e2 := Complex.exp ((δ - Complex.I * omega) ^ 2 / (2 * a))
  set e3 := Complex.exp (-(omega : ℂ) ^ 2 / (2 * a))
  set e4 := Complex.exp (δ ^ 2 / (2 * a))
  have h2 : ‖(2 : ℂ)‖ = 2 := by norm_num
  have htri : ‖C * (e1 + e2 + 2 * e3 * e4)‖ ≤
      ‖C‖ * (‖e1‖ + ‖e2‖ + 2 * ‖e3 * e4‖) := by
    have hsum :
        ‖e1 + e2 + 2 * e3 * e4‖ ≤ ‖e1‖ + ‖e2‖ + ‖(2 : ℂ) * (e3 * e4)‖ := by
      calc
        ‖e1 + e2 + 2 * e3 * e4‖ ≤ ‖e1 + e2‖ + ‖2 * e3 * e4‖ :=
          norm_add_le _ _
        _ ≤ ‖e1‖ + ‖e2‖ + ‖2 * e3 * e4‖ :=
          add_le_add (norm_add_le e1 e2) le_rfl
        _ = ‖e1‖ + ‖e2‖ + ‖(2 : ℂ) * (e3 * e4)‖ := by
          rw [mul_assoc]
    have h2e : ‖(2 : ℂ) * (e3 * e4)‖ = 2 * ‖e3 * e4‖ := by
      rw [norm_mul, h2]
    calc
      ‖C * (e1 + e2 + 2 * e3 * e4)‖ = ‖C‖ * ‖e1 + e2 + 2 * e3 * e4‖ :=
        norm_mul _ _
      _ ≤ ‖C‖ * (‖e1‖ + ‖e2‖ + ‖(2 : ℂ) * (e3 * e4)‖) :=
        mul_le_mul_of_nonneg_left hsum (norm_nonneg _)
      _ = ‖C‖ * (‖e1‖ + ‖e2‖ + 2 * ‖e3 * e4‖) := by rw [h2e]
  refine htri.trans ?_
  rw [hC, hn1, hn2, hn3]
  rw [exp_re_sq_split a δ.re (δ.im + omega) ha,
    exp_re_sq_split a δ.re (δ.im - omega) ha]
  have hmid :
      Real.exp ((δ.re ^ 2 - δ.im ^ 2 - omega ^ 2) / (2 * a)) =
        Real.exp (δ.re ^ 2 / (2 * a)) *
          Real.exp (-(δ.im ^ 2 + omega ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [ne_of_gt ha]
    ring
  rw [hmid]
  unfold gaborThreeLobe
  have hE : 0 ≤ Real.exp (δ.re ^ 2 / (2 * a)) := (Real.exp_pos _).le
  nlinarith [Real.exp_pos (-(δ.im + omega) ^ 2 / (2 * a)),
    Real.exp_pos (-(δ.im - omega) ^ 2 / (2 * a)),
    Real.exp_pos (-(δ.im ^ 2 + omega ^ 2) / (2 * a))]

theorem norm_pureGaborHatDelta_le_three_lobe
    (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    ‖pureGaborHatDelta a omega δ‖ ≤
      gaborHatThreeLobeConst a (δ.re + 1 / 2) * gaborThreeLobe a omega δ.im := by
  rw [pureGaborHatDelta_eq_holomorphic a omega ha δ]
  exact norm_pureGaborHatHolomorphic_le_three_lobe a omega ha δ

/-- `|ĥ_W(σ+it)| ≤ C(a,σ) · (e^{-(t-ω)²/(2a)} + e^{-(t+ω)²/(2a)} +
2 e^{-(t²+ω²)/(2a)})` for every pure Gabor test. -/
theorem norm_gaborHat_le_three_lobe
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (s : ℂ) :
    ‖gaborHat F s‖ ≤
      gaborHatThreeLobeConst F.a s.re * gaborThreeLobe F.a F.omega s.im := by
  rw [gaborHat_of_pure hF]
  have hδre : (s - (1 / 2 : ℂ)).re + 1 / 2 = s.re := by
    simp [sub_re]
  have hδim : (s - (1 / 2 : ℂ)).im = s.im := by
    simp [sub_im]
  simpa [hδre, hδim] using
    norm_pureGaborHatDelta_le_three_lobe F.a F.omega F.a_pos (s - (1 / 2 : ℂ))

/-- Honest quartic three-lobe majorant: a t-independent C(σ) times
the three-lobe is too strong for degree-4 packets (the moment factor
is poly in t).  The form is C(σ)·(1+|t|)^8·threeLobe.  Discharged
by `gaborHatQuarticThreeLobeRemainder_holds`. -/
def GaborHatQuarticThreeLobeRemainder : Prop :=
  ∀ F : GaborWeilTest,
    ∃ C : ℝ → ℝ, (∀ σ : ℝ, 0 ≤ C σ) ∧
      ∀ s : ℂ, ‖gaborHat F s‖ ≤
        C s.re * (1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im

/-! ## Gaussian strip decay (pure; follows from the three-lobe bound) -/

theorem sq_sub_center_ge_half (t omega : ℝ) :
    t ^ 2 / 2 - omega ^ 2 ≤ (t - omega) ^ 2 := by
  have h : (t - omega) ^ 2 - (t ^ 2 / 2 - omega ^ 2) =
      (1 / 2) * (t - 2 * omega) ^ 2 := by ring
  have : 0 ≤ (1 / 2) * (t - 2 * omega) ^ 2 := by positivity
  linarith

theorem sq_add_center_ge_half (t omega : ℝ) :
    (t + omega) ^ 2 ≥ t ^ 2 / 2 - omega ^ 2 := by
  simpa [sub_eq_add_neg] using sq_sub_center_ge_half t (-omega)

theorem gaborThreeLobe_le_gaussian
    (a omega t : ℝ) (ha : 0 < a) :
    gaborThreeLobe a omega t ≤
      4 * Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) := by
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hden4 : 0 < 4 * a := mul_pos (by norm_num) ha
  have hminus :
      Real.exp (-(t - omega) ^ 2 / (2 * a)) ≤
        Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) := by
    have hge := sq_sub_center_ge_half t omega
    have hineq :
        -(t - omega) ^ 2 / (2 * a) ≤
          omega ^ 2 / (2 * a) + -t ^ 2 / (4 * a) := by
      have : (t - omega) ^ 2 ≥ t ^ 2 / 2 - omega ^ 2 := hge
      have := neg_le_neg this
      have hdiv := div_le_div_of_nonneg_right this hden.le
      -- `-(t²/2 - ω²)/(2a) = -t²/(4a) + ω²/(2a)`
      have hrew :
          -(t ^ 2 / 2 - omega ^ 2) / (2 * a) =
            omega ^ 2 / (2 * a) + -t ^ 2 / (4 * a) := by
        field_simp [ne_of_gt ha]
        ring
      calc
        -(t - omega) ^ 2 / (2 * a) ≤
            -(t ^ 2 / 2 - omega ^ 2) / (2 * a) := hdiv
        _ = _ := hrew
    rw [← Real.exp_add]
    exact Real.exp_le_exp.mpr hineq
  have hplus :
      Real.exp (-(t + omega) ^ 2 / (2 * a)) ≤
        Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) := by
    have hge := sq_add_center_ge_half t omega
    have hineq :
        -(t + omega) ^ 2 / (2 * a) ≤
          omega ^ 2 / (2 * a) + -t ^ 2 / (4 * a) := by
      have := neg_le_neg hge
      have hdiv := div_le_div_of_nonneg_right this hden.le
      have hrew :
          -(t ^ 2 / 2 - omega ^ 2) / (2 * a) =
            omega ^ 2 / (2 * a) + -t ^ 2 / (4 * a) := by
        field_simp [ne_of_gt ha]
        ring
      calc
        -(t + omega) ^ 2 / (2 * a) ≤
            -(t ^ 2 / 2 - omega ^ 2) / (2 * a) := hdiv
        _ = _ := hrew
    rw [← Real.exp_add]
    exact Real.exp_le_exp.mpr hineq
  have hmid :
      Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) ≤
        Real.exp (-t ^ 2 / (4 * a)) := by
    apply Real.exp_le_exp.mpr
    have : 0 ≤ omega ^ 2 / (2 * a) :=
      div_nonneg (sq_nonneg _) hden.le
    have : 0 ≤ t ^ 2 / (4 * a) :=
      div_nonneg (sq_nonneg _) hden4.le
    field_simp [ne_of_gt ha]
    nlinarith [sq_nonneg t, sq_nonneg omega, ha]
  unfold gaborThreeLobe
  have hω : 0 ≤ Real.exp (omega ^ 2 / (2 * a)) := (Real.exp_pos _).le
  have hg : 0 ≤ Real.exp (-t ^ 2 / (4 * a)) := (Real.exp_pos _).le
  have hone : (1 : ℝ) ≤ Real.exp (omega ^ 2 / (2 * a)) :=
    Real.one_le_exp (div_nonneg (sq_nonneg _) hden.le)
  calc
    Real.exp (-(t - omega) ^ 2 / (2 * a)) +
        Real.exp (-(t + omega) ^ 2 / (2 * a)) +
        2 * Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) ≤
      Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) +
        Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) +
        2 * Real.exp (-t ^ 2 / (4 * a)) := by
      gcongr
    _ = 2 * Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) +
        2 * Real.exp (-t ^ 2 / (4 * a)) := by ring
    _ ≤ 2 * Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) +
        2 * Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) := by
      have hside :
          2 * Real.exp (-t ^ 2 / (4 * a)) ≤
            2 * Real.exp (omega ^ 2 / (2 * a)) *
              Real.exp (-t ^ 2 / (4 * a)) := by
        nlinarith [mul_le_mul_of_nonneg_right hone hg]
      linarith
    _ = 4 * Real.exp (omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (4 * a)) := by
      ring

theorem abs_re_le_max_endpoints {σ σ₁ σ₂ : ℝ} (h1 : σ₁ ≤ σ) (h2 : σ ≤ σ₂) :
    |σ - 1 / 2| ≤ max |σ₁ - 1 / 2| |σ₂ - 1 / 2| := by
  cases le_total (σ - 1 / 2) 0 with
  | inl hnonpos =>
    rw [abs_of_nonpos hnonpos]
    have : -(σ - 1 / 2) ≤ -(σ₁ - 1 / 2) := by linarith
    exact this.trans ((neg_le_abs _).trans (le_max_left _ _))
  | inr hnonneg =>
    rw [abs_of_nonneg hnonneg]
    have : σ - 1 / 2 ≤ σ₂ - 1 / 2 := by linarith
    exact this.trans ((le_abs_self _).trans (le_max_right _ _))

/-- On every closed strip `σ ∈ [σ₁,σ₂]`, a pure Gabor transform decays
as a Gaussian in the imaginary direction.  Follows from
`norm_gaborHat_le_three_lobe`. -/
theorem norm_gaborHat_le_gaussian_strip
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (σ₁ σ₂ : ℝ) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ σ t : ℝ, σ₁ ≤ σ → σ ≤ σ₂ →
        ‖gaborHat F (σ + t * Complex.I)‖ ≤
          C * Real.exp (-c * t ^ 2) := by
  have ha : 0 < F.a := F.a_pos
  refine ⟨1 / (4 * F.a),
    (Real.pi / F.a) *
      Real.exp (((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 + F.omega ^ 2) /
        (2 * F.a)),
    div_pos (by norm_num) (mul_pos (by norm_num) ha),
    mul_pos (div_pos Real.pi_pos ha) (Real.exp_pos _), ?_⟩
  · intro σ t hσ1 hσ2
    have hs : ((σ : ℂ) + t * Complex.I).re = σ := by simp
    have ht : ((σ : ℂ) + t * Complex.I).im = t := by simp
    have hthree := norm_gaborHat_le_three_lobe (F := F) hF (σ + t * Complex.I)
    rw [hs, ht] at hthree
    have hM := abs_re_le_max_endpoints hσ1 hσ2
    have hconst :
        gaborHatThreeLobeConst F.a σ ≤
          Real.pi / (4 * F.a) *
            Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a)) := by
      unfold gaborHatThreeLobeConst
      have hexp :
          Real.exp ((σ - 1 / 2) ^ 2 / (2 * F.a)) ≤
            Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a)) := by
        apply Real.exp_le_exp.mpr
        refine div_le_div_of_nonneg_right ?_ (by positivity)
        have hmax : 0 ≤ max |σ₁ - 1 / 2| |σ₂ - 1 / 2| :=
          le_max_of_le_left (abs_nonneg _)
        exact sq_le_sq.mpr (hM.trans (by rw [abs_of_nonneg hmax]))
      exact mul_le_mul_of_nonneg_left hexp
        (div_nonneg Real.pi_pos.le (by positivity))
    have hlobe := gaborThreeLobe_le_gaussian F.a F.omega t ha
    have hCpos : 0 ≤ gaborHatThreeLobeConst F.a σ :=
      gaborHatThreeLobeConst_nonneg F.a σ ha
    have hlpos : 0 ≤ gaborThreeLobe F.a F.omega t :=
      gaborThreeLobe_nonneg F.a F.omega t
    have hprod :
        gaborHatThreeLobeConst F.a σ * gaborThreeLobe F.a F.omega t ≤
          (Real.pi / (4 * F.a) *
              Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a))) *
            (4 * Real.exp (F.omega ^ 2 / (2 * F.a)) *
              Real.exp (-t ^ 2 / (4 * F.a))) :=
      mul_le_mul hconst hlobe hlpos (by positivity)
    refine hthree.trans (hprod.trans ?_)
    have hrew :
        (Real.pi / (4 * F.a) *
            Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a))) *
          (4 * Real.exp (F.omega ^ 2 / (2 * F.a)) *
            Real.exp (-t ^ 2 / (4 * F.a))) =
          (Real.pi / F.a) *
            Real.exp (((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 + F.omega ^ 2) /
              (2 * F.a)) *
            Real.exp (-(1 / (4 * F.a)) * t ^ 2) := by
      have hexp :
          Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a)) *
              Real.exp (F.omega ^ 2 / (2 * F.a)) =
            Real.exp (((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 + F.omega ^ 2) /
              (2 * F.a)) := by
        rw [← Real.exp_add]
        congr 1
        field_simp [ne_of_gt ha]
      have hrate :
          Real.exp (-t ^ 2 / (4 * F.a)) =
            Real.exp (-(1 / (4 * F.a)) * t ^ 2) := by
        congr 1
        field_simp [ne_of_gt ha]
      calc
        (Real.pi / (4 * F.a) *
            Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a))) *
          (4 * Real.exp (F.omega ^ 2 / (2 * F.a)) *
            Real.exp (-t ^ 2 / (4 * F.a))) =
          (Real.pi / F.a) *
            (Real.exp ((max |σ₁ - 1 / 2| |σ₂ - 1 / 2|) ^ 2 / (2 * F.a)) *
              Real.exp (F.omega ^ 2 / (2 * F.a))) *
            Real.exp (-t ^ 2 / (4 * F.a)) := by
          field_simp [ne_of_gt ha]
        _ = _ := by rw [hexp, hrate]
    rw [hrew]

/-! ## r586: quartic Gaussian majorant (poly factor in t) -/

lemma norm_exp_sq_div_ofReal {a : ℝ} (ha : 0 < a) (z : ℂ) :
    ‖Complex.exp (z ^ 2 / (4 * a : ℂ))‖ =
      Real.exp ((z.re ^ 2 - z.im ^ 2) / (4 * a)) := by
  have hcoe : (4 * a : ℂ) = ((4 * a : ℝ) : ℂ) := by simp
  rw [hcoe, Complex.norm_exp, Complex.div_ofReal_re]
  have hsq : (z ^ 2).re = z.re ^ 2 - z.im ^ 2 := by
    simp [pow_two, Complex.mul_re]
  rw [hsq]

lemma one_add_abs_pow_mul_gauss {c : ℝ} (hc : 0 < c) (n : ℕ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ t : ℝ,
      (1 + |t|) ^ n * Real.exp (-c * t ^ 2) ≤
        K * Real.exp (-(c / 2) * t ^ 2) := by
  have hc2 : 0 < c / 2 := half_pos hc
  refine ⟨Real.exp ((n : ℝ) ^ 2 / (2 * c)), (Real.exp_pos _).le, fun t => ?_⟩
  have hlin : 1 + |t| ≤ Real.exp |t| := by
    have := Real.add_one_le_exp |t|
    simpa [add_comm] using this
  have hpow : (1 + |t|) ^ n ≤ Real.exp |t| ^ n :=
    pow_le_pow_left₀ (by positivity) hlin n
  have hexp : Real.exp |t| ^ n = Real.exp ((n : ℝ) * |t|) := by
    rw [← Real.exp_nat_mul]
  have hsplit : Real.exp (-c * t ^ 2) =
      Real.exp (-(c / 2) * t ^ 2) * Real.exp (-(c / 2) * t ^ 2) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have hquad : (n : ℝ) * |t| - (c / 2) * t ^ 2 ≤ (n : ℝ) ^ 2 / (2 * c) := by
    have hsq : t ^ 2 = |t| ^ 2 := (sq_abs t).symm
    rw [hsq]
    have : 0 ≤ (c / 2) * (|t| - (n : ℝ) / c) ^ 2 :=
      mul_nonneg hc2.le (sq_nonneg _)
    have hident : (c / 2) * (|t| - (n : ℝ) / c) ^ 2 =
        (c / 2) * |t| ^ 2 - (n : ℝ) * |t| + (n : ℝ) ^ 2 / (2 * c) := by
      have hc0 : c ≠ 0 := ne_of_gt hc
      field_simp [hc0]
      ring
    linarith
  have hmul : (1 + |t|) ^ n * Real.exp (-c * t ^ 2) ≤
      Real.exp ((n : ℝ) * |t|) * Real.exp (-c * t ^ 2) :=
    mul_le_mul_of_nonneg_right (hpow.trans_eq hexp) (Real.exp_pos _).le
  have hprod : Real.exp ((n : ℝ) * |t|) * Real.exp (-c * t ^ 2) =
      Real.exp ((n : ℝ) * |t| - (c / 2) * t ^ 2) *
        Real.exp (-(c / 2) * t ^ 2) := by
    rw [← Real.exp_add, ← Real.exp_add]
    congr 1
    ring
  rw [hprod] at hmul
  exact hmul.trans (mul_le_mul_of_nonneg_right
    (Real.exp_le_exp.mpr hquad) (Real.exp_pos _).le)

/-! ## r587: quartic poly-in-t three-lobe majorant -/

lemma one_add_add_le_mul {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    1 + x + y ≤ (1 + x) * (1 + y) := by
  nlinarith

lemma one_le_one_add_abs_pow (t : ℝ) (n : ℕ) :
    (1 : ℝ) ≤ (1 + |t|) ^ n :=
  one_le_pow₀ (le_add_of_nonneg_right (abs_nonneg t))

lemma norm_sq_le_one_add_pow_four (z : ℂ) :
    ‖z‖ ^ 2 ≤ (1 + ‖z‖) ^ 4 := by
  have h2 : ‖z‖ ^ 2 ≤ (1 + ‖z‖) ^ 2 := by
    nlinarith [norm_nonneg z]
  have h24 : (1 + ‖z‖) ^ 2 ≤ (1 + ‖z‖) ^ 4 :=
    pow_le_pow_right₀ (le_add_of_nonneg_right (norm_nonneg z)) (by norm_num)
  exact h2.trans h24

lemma norm_pow_four_le_one_add (z : ℂ) :
    ‖z‖ ^ 4 ≤ (1 + ‖z‖) ^ 4 :=
  pow_le_pow_left₀ (norm_nonneg z)
    (le_add_of_nonneg_left (by norm_num : (0 : ℝ) ≤ 1)) 4

lemma one_le_one_add_norm_pow_four (z : ℂ) :
    (1 : ℝ) ≤ (1 + ‖z‖) ^ 4 :=
  one_le_pow₀ (le_add_of_nonneg_right (norm_nonneg z))

noncomputable def gaussianPolynomialFactorBound (p : EvenQuartic) (a : ℝ) : ℝ :=
  |p.c0| + |p.c2| * (1 / (2 * a) + 1 / (4 * a ^ 2)) +
    |p.c4| * (3 / (4 * a ^ 2) + 3 / (4 * a ^ 3) + 1 / (16 * a ^ 4))

lemma gaussianPolynomialFactorBound_nonneg
    (p : EvenQuartic) (a : ℝ) (ha : 0 < a) :
    0 ≤ gaussianPolynomialFactorBound p a := by
  unfold gaussianPolynomialFactorBound
  positivity

lemma norm_coe_real (x : ℝ) : ‖(x : ℂ)‖ = |x| :=
  Complex.norm_real x

lemma norm_div_pos_real (z : ℂ) {c : ℝ} (hc : 0 < c) :
    ‖z / (c : ℂ)‖ = ‖z‖ / c := by
  rw [norm_div, norm_coe_real, abs_of_pos hc]

lemma norm_pow_div_ofReal (z : ℂ) (n : ℕ) {c : ℝ} (hc : 0 < c) :
    ‖z ^ n / (c : ℂ)‖ = ‖z‖ ^ n / c := by
  rw [norm_div_pos_real _ hc, norm_pow]

lemma gaussianPolynomialFactor_eq_ofReal
    (p : EvenQuartic) (a : ℝ) (z : ℂ) :
    gaussianPolynomialFactor p a z =
      (p.c0 : ℂ) +
        (p.c2 : ℂ) * ((1 : ℂ) / ((2 * a : ℝ) : ℂ) +
          z ^ 2 / ((4 * a ^ 2 : ℝ) : ℂ)) +
        (p.c4 : ℂ) * (((3 / (4 * a ^ 2) : ℝ) : ℂ) +
          ((3 : ℝ) : ℂ) * z ^ 2 / ((4 * a ^ 3 : ℝ) : ℂ) +
          z ^ 4 / ((16 * a ^ 4 : ℝ) : ℂ)) := by
  unfold gaussianPolynomialFactor
  push_cast
  ring

lemma norm_gaussianPolynomialFactor_le_moments
    (p : EvenQuartic) (a : ℝ) (ha : 0 < a) (z : ℂ) :
    ‖gaussianPolynomialFactor p a z‖ ≤
      |p.c0| + |p.c2| * (1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2)) +
        |p.c4| * (3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
          ‖z‖ ^ 4 / (16 * a ^ 4)) := by
  have ha2 : 0 < 2 * a := mul_pos (by norm_num) ha
  have ha4 : 0 < 4 * a ^ 2 := by positivity
  have ha43 : 0 < 4 * a ^ 3 := by positivity
  have ha16 : 0 < 16 * a ^ 4 := by positivity
  rw [gaussianPolynomialFactor_eq_ofReal]
  have hc0 : ‖(p.c0 : ℂ)‖ = |p.c0| := norm_coe_real _
  have hc2 : ‖(p.c2 : ℂ)‖ = |p.c2| := norm_coe_real _
  have hc4 : ‖(p.c4 : ℂ)‖ = |p.c4| := norm_coe_real _
  have h1 : ‖(1 : ℂ) / ((2 * a : ℝ) : ℂ)‖ = 1 / (2 * a) := by
    rw [norm_div_pos_real _ ha2, norm_one]
  have hz2 : ‖z ^ 2 / ((4 * a ^ 2 : ℝ) : ℂ)‖ = ‖z‖ ^ 2 / (4 * a ^ 2) :=
    norm_pow_div_ofReal z 2 ha4
  have hmid : ‖(1 : ℂ) / ((2 * a : ℝ) : ℂ) + z ^ 2 / ((4 * a ^ 2 : ℝ) : ℂ)‖ ≤
      1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2) := by
    refine (norm_add_le _ _).trans ?_
    rw [h1, hz2]
  have h3 : ‖((3 / (4 * a ^ 2) : ℝ) : ℂ)‖ = 3 / (4 * a ^ 2) :=
    Complex.norm_of_nonneg (div_nonneg (by norm_num) ha4.le)
  have hz2' :
      ‖((3 : ℝ) : ℂ) * z ^ 2 / ((4 * a ^ 3 : ℝ) : ℂ)‖ =
        3 * ‖z‖ ^ 2 / (4 * a ^ 3) := by
    rw [norm_div_pos_real _ ha43, norm_mul, norm_pow, norm_coe_real]
    simp [abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 3)]
  have hz4 : ‖z ^ 4 / ((16 * a ^ 4 : ℝ) : ℂ)‖ = ‖z‖ ^ 4 / (16 * a ^ 4) :=
    norm_pow_div_ofReal z 4 ha16
  have htail :
      ‖((3 / (4 * a ^ 2) : ℝ) : ℂ) +
            ((3 : ℝ) : ℂ) * z ^ 2 / ((4 * a ^ 3 : ℝ) : ℂ) +
          z ^ 4 / ((16 * a ^ 4 : ℝ) : ℂ)‖ ≤
        3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
          ‖z‖ ^ 4 / (16 * a ^ 4) := by
    refine (norm_add_le _ _).trans ?_
    refine add_le_add ?_ hz4.le
    refine (norm_add_le _ _).trans_eq ?_
    rw [h3, hz2']
  have hterm2 :
      ‖(p.c2 : ℂ) * ((1 : ℂ) / ((2 * a : ℝ) : ℂ) +
          z ^ 2 / ((4 * a ^ 2 : ℝ) : ℂ))‖ ≤
        |p.c2| * (1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2)) := by
    rw [norm_mul, hc2]
    exact mul_le_mul_of_nonneg_left hmid (abs_nonneg _)
  have hterm4 :
      ‖(p.c4 : ℂ) * (((3 / (4 * a ^ 2) : ℝ) : ℂ) +
          ((3 : ℝ) : ℂ) * z ^ 2 / ((4 * a ^ 3 : ℝ) : ℂ) +
          z ^ 4 / ((16 * a ^ 4 : ℝ) : ℂ))‖ ≤
        |p.c4| * (3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
          ‖z‖ ^ 4 / (16 * a ^ 4)) := by
    rw [norm_mul, hc4]
    exact mul_le_mul_of_nonneg_left htail (abs_nonneg _)
  refine (norm_add_le _ _).trans ?_
  refine add_le_add ?_ hterm4
  refine (norm_add_le _ _).trans ?_
  rw [hc0]
  exact add_le_add le_rfl hterm2

lemma moments_le_bound_mul_pow
    (p : EvenQuartic) (a : ℝ) (ha : 0 < a) (z : ℂ) :
    |p.c0| + |p.c2| * (1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2)) +
        |p.c4| * (3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
          ‖z‖ ^ 4 / (16 * a ^ 4)) ≤
      gaussianPolynomialFactorBound p a * (1 + ‖z‖) ^ 4 := by
  have h1 := one_le_one_add_norm_pow_four z
  have h2 := norm_sq_le_one_add_pow_four z
  have h4 := norm_pow_four_le_one_add z
  have ha2 : 0 < 2 * a := mul_pos (by norm_num) ha
  have ha4 : 0 < 4 * a ^ 2 := by positivity
  have ha43 : 0 < 4 * a ^ 3 := by positivity
  have ha16 : 0 < 16 * a ^ 4 := by positivity
  have hc0 : |p.c0| ≤ |p.c0| * (1 + ‖z‖) ^ 4 :=
    le_mul_of_one_le_right (abs_nonneg _) h1
  have hc2 :
      |p.c2| * (1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2)) ≤
        |p.c2| * (1 / (2 * a) + 1 / (4 * a ^ 2)) * (1 + ‖z‖) ^ 4 := by
    have hinner :
        1 / (2 * a) + ‖z‖ ^ 2 / (4 * a ^ 2) ≤
          (1 / (2 * a) + 1 / (4 * a ^ 2)) * (1 + ‖z‖) ^ 4 := by
      have hA : 1 / (2 * a) ≤ (1 / (2 * a)) * (1 + ‖z‖) ^ 4 :=
        le_mul_of_one_le_right (div_nonneg (by norm_num) ha2.le) h1
      have hB : ‖z‖ ^ 2 / (4 * a ^ 2) ≤ (1 / (4 * a ^ 2)) * (1 + ‖z‖) ^ 4 := by
        rw [div_eq_mul_inv, one_div]
        have : ‖z‖ ^ 2 * (4 * a ^ 2)⁻¹ ≤ (1 + ‖z‖) ^ 4 * (4 * a ^ 2)⁻¹ :=
          mul_le_mul_of_nonneg_right h2 (inv_nonneg.mpr ha4.le)
        simpa [mul_comm] using this
      linarith [hA, hB]
    simpa [mul_assoc] using
      mul_le_mul_of_nonneg_left hinner (abs_nonneg p.c2)
  have hc4 :
      |p.c4| * (3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
          ‖z‖ ^ 4 / (16 * a ^ 4)) ≤
        |p.c4| * (3 / (4 * a ^ 2) + 3 / (4 * a ^ 3) + 1 / (16 * a ^ 4)) *
          (1 + ‖z‖) ^ 4 := by
    have hinner :
        3 / (4 * a ^ 2) + 3 * ‖z‖ ^ 2 / (4 * a ^ 3) +
            ‖z‖ ^ 4 / (16 * a ^ 4) ≤
          (3 / (4 * a ^ 2) + 3 / (4 * a ^ 3) + 1 / (16 * a ^ 4)) *
            (1 + ‖z‖) ^ 4 := by
      have hA : 3 / (4 * a ^ 2) ≤ (3 / (4 * a ^ 2)) * (1 + ‖z‖) ^ 4 :=
        le_mul_of_one_le_right (div_nonneg (by norm_num) ha4.le) h1
      have hB : 3 * ‖z‖ ^ 2 / (4 * a ^ 3) ≤
          (3 / (4 * a ^ 3)) * (1 + ‖z‖) ^ 4 := by
        have : 3 * ‖z‖ ^ 2 / (4 * a ^ 3) = (3 / (4 * a ^ 3)) * ‖z‖ ^ 2 := by
          field_simp [ha.ne']
        rw [this]
        exact mul_le_mul_of_nonneg_left h2 (div_nonneg (by norm_num) ha43.le)
      have hC : ‖z‖ ^ 4 / (16 * a ^ 4) ≤
          (1 / (16 * a ^ 4)) * (1 + ‖z‖) ^ 4 := by
        rw [div_eq_mul_inv, one_div]
        have : ‖z‖ ^ 4 * (16 * a ^ 4)⁻¹ ≤ (1 + ‖z‖) ^ 4 * (16 * a ^ 4)⁻¹ :=
          mul_le_mul_of_nonneg_right h4 (inv_nonneg.mpr ha16.le)
        simpa [mul_comm] using this
      linarith [hA, hB, hC]
    simpa [mul_assoc] using
      mul_le_mul_of_nonneg_left hinner (abs_nonneg p.c4)
  unfold gaussianPolynomialFactorBound
  linarith [hc0, hc2, hc4]

lemma norm_gaussianPolynomialFactor_le
    (p : EvenQuartic) (a : ℝ) (ha : 0 < a) (z : ℂ) :
    ‖gaussianPolynomialFactor p a z‖ ≤
      gaussianPolynomialFactorBound p a * (1 + ‖z‖) ^ 4 :=
  (norm_gaussianPolynomialFactor_le_moments p a ha z).trans
    (moments_le_bound_mul_pow p a ha z)

lemma norm_add_I_omega_le (δ : ℂ) (omega : ℝ) :
    ‖δ + Complex.I * omega‖ ≤ |δ.re| + |δ.im| + |omega| := by
  have h := norm_le_abs_re_add_abs_im (δ + Complex.I * omega)
  have hre : (δ + Complex.I * omega).re = δ.re := by simp
  have him : (δ + Complex.I * omega).im = δ.im + omega := by simp
  rw [hre, him] at h
  linarith [h, abs_add_le δ.im omega]

lemma norm_sub_I_omega_le (δ : ℂ) (omega : ℝ) :
    ‖δ - Complex.I * omega‖ ≤ |δ.re| + |δ.im| + |omega| := by
  have h := norm_le_abs_re_add_abs_im (δ - Complex.I * omega)
  have hre : (δ - Complex.I * omega).re = δ.re := by simp
  have him : (δ - Complex.I * omega).im = δ.im - omega := by simp
  rw [hre, him] at h
  have : |δ.im - omega| ≤ |δ.im| + |omega| := by
    simpa [sub_eq_add_neg, abs_neg] using abs_add_le δ.im (-omega)
  linarith [h, this]

lemma one_add_norm_shift_le (δ : ℂ) (omega : ℝ) :
    1 + ‖δ + Complex.I * omega‖ ≤
      (1 + |δ.re| + |omega|) * (1 + |δ.im|) := by
  have h := norm_add_I_omega_le δ omega
  nlinarith [h, abs_nonneg δ.re, abs_nonneg δ.im, abs_nonneg omega]

lemma one_add_norm_shift_sub_le (δ : ℂ) (omega : ℝ) :
    1 + ‖δ - Complex.I * omega‖ ≤
      (1 + |δ.re| + |omega|) * (1 + |δ.im|) := by
  have h := norm_sub_I_omega_le δ omega
  nlinarith [h, abs_nonneg δ.re, abs_nonneg δ.im, abs_nonneg omega]

lemma norm_P_shift_le
    (p : EvenQuartic) (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    ‖gaussianPolynomialFactor p a (δ + Complex.I * omega)‖ ≤
      gaussianPolynomialFactorBound p a *
        (1 + |δ.re| + |omega|) ^ 4 * (1 + |δ.im|) ^ 4 := by
  have h := norm_gaussianPolynomialFactor_le p a ha (δ + Complex.I * omega)
  have hpow := pow_le_pow_left₀ (by positivity)
    (one_add_norm_shift_le δ omega) 4
  have hmul : (1 + ‖δ + Complex.I * omega‖) ^ 4 ≤
      (1 + |δ.re| + |omega|) ^ 4 * (1 + |δ.im|) ^ 4 := by
    simpa [mul_pow] using hpow
  simpa [mul_assoc] using
    h.trans (mul_le_mul_of_nonneg_left hmul
      (gaussianPolynomialFactorBound_nonneg p a ha))

lemma norm_P_shift_sub_le
    (p : EvenQuartic) (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    ‖gaussianPolynomialFactor p a (δ - Complex.I * omega)‖ ≤
      gaussianPolynomialFactorBound p a *
        (1 + |δ.re| + |omega|) ^ 4 * (1 + |δ.im|) ^ 4 := by
  have h := norm_gaussianPolynomialFactor_le p a ha (δ - Complex.I * omega)
  have hpow := pow_le_pow_left₀ (by positivity)
    (one_add_norm_shift_sub_le δ omega) 4
  have hmul : (1 + ‖δ - Complex.I * omega‖) ^ 4 ≤
      (1 + |δ.re| + |omega|) ^ 4 * (1 + |δ.im|) ^ 4 := by
    simpa [mul_pow] using hpow
  simpa [mul_assoc] using
    h.trans (mul_le_mul_of_nonneg_left hmul
      (gaussianPolynomialFactorBound_nonneg p a ha))

noncomputable def gaborHatQuarticPolyFac
    (p : EvenQuartic) (a omega : ℝ) (δ : ℂ) : ℝ :=
  gaussianPolynomialFactorBound p a *
    (1 + |δ.re| + |omega|) ^ 4 * (1 + |δ.im|) ^ 4

lemma gaborHatQuarticPolyFac_nonneg
    (p : EvenQuartic) (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    0 ≤ gaborHatQuarticPolyFac p a omega δ := by
  unfold gaborHatQuarticPolyFac
  exact mul_nonneg (mul_nonneg (gaussianPolynomialFactorBound_nonneg p a ha)
    (by positivity)) (by positivity)

lemma gaborHatQuarticPolyFac_sq
    (p : EvenQuartic) (a omega : ℝ) (δ : ℂ) :
    gaborHatQuarticPolyFac p a omega δ ^ 2 =
      gaussianPolynomialFactorBound p a ^ 2 *
        (1 + |δ.re| + |omega|) ^ 8 * (1 + |δ.im|) ^ 8 := by
  unfold gaborHatQuarticPolyFac
  ring

lemma norm_gaussianLaplace_le
    (p : EvenQuartic) (a : ℝ) (ha : 0 < a) (z : ℂ) :
    ‖gaussianLaplace p a z‖ ≤
      Real.sqrt (Real.pi / a) *
        Real.exp ((z.re ^ 2 - z.im ^ 2) / (4 * a)) *
          ‖gaussianPolynomialFactor p a z‖ := by
  unfold gaussianLaplace
  rw [norm_mul, norm_mul]
  have hsqrt : ‖((Real.sqrt (Real.pi / a) : ℝ) : ℂ)‖ =
      Real.sqrt (Real.pi / a) :=
    Complex.norm_of_nonneg (Real.sqrt_nonneg _)
  rw [hsqrt, norm_exp_sq_div_ofReal ha]

lemma norm_gaborLaplace_le (F : GaborWeilTest) (z : ℂ) :
    ‖gaborLaplace F z‖ ≤
      (1 / 2) * Real.sqrt (Real.pi / F.a) *
        (Real.exp ((z.re ^ 2 - (z.im + F.omega) ^ 2) / (4 * F.a)) *
            ‖gaussianPolynomialFactor F.coeffs F.a
              (z + Complex.I * F.omega)‖ +
          Real.exp ((z.re ^ 2 - (z.im - F.omega) ^ 2) / (4 * F.a)) *
            ‖gaussianPolynomialFactor F.coeffs F.a
              (z - Complex.I * F.omega)‖) := by
  have ha : 0 < F.a := F.a_pos
  unfold gaborLaplace
  have hhalf : ‖(1 / 2 : ℂ)‖ = (1 / 2 : ℝ) := by norm_num
  rw [norm_mul, hhalf]
  have hsum :=
    norm_add_le
      (gaussianLaplace F.coeffs F.a (z + Complex.I * F.omega))
      (gaussianLaplace F.coeffs F.a (z - Complex.I * F.omega))
  have hp :=
    norm_gaussianLaplace_le F.coeffs F.a ha (z + Complex.I * F.omega)
  have hm :=
    norm_gaussianLaplace_le F.coeffs F.a ha (z - Complex.I * F.omega)
  have hpre : (z + Complex.I * F.omega).re = z.re := by simp
  have hpre' : (z - Complex.I * F.omega).re = z.re := by simp
  have himp : (z + Complex.I * F.omega).im = z.im + F.omega := by simp
  have himm : (z - Complex.I * F.omega).im = z.im - F.omega := by simp
  have hp' :
      ‖gaussianLaplace F.coeffs F.a (z + Complex.I * F.omega)‖ ≤
        Real.sqrt (Real.pi / F.a) *
          Real.exp ((z.re ^ 2 - (z.im + F.omega) ^ 2) / (4 * F.a)) *
            ‖gaussianPolynomialFactor F.coeffs F.a
              (z + Complex.I * F.omega)‖ := by
    simpa [hpre, himp] using hp
  have hm' :
      ‖gaussianLaplace F.coeffs F.a (z - Complex.I * F.omega)‖ ≤
        Real.sqrt (Real.pi / F.a) *
          Real.exp ((z.re ^ 2 - (z.im - F.omega) ^ 2) / (4 * F.a)) *
            ‖gaussianPolynomialFactor F.coeffs F.a
              (z - Complex.I * F.omega)‖ := by
    simpa [hpre', himm] using hm
  have hfact :
      ‖gaussianLaplace F.coeffs F.a (z + Complex.I * F.omega)‖ +
          ‖gaussianLaplace F.coeffs F.a (z - Complex.I * F.omega)‖ ≤
        Real.sqrt (Real.pi / F.a) *
          (Real.exp ((z.re ^ 2 - (z.im + F.omega) ^ 2) / (4 * F.a)) *
              ‖gaussianPolynomialFactor F.coeffs F.a
                (z + Complex.I * F.omega)‖ +
            Real.exp ((z.re ^ 2 - (z.im - F.omega) ^ 2) / (4 * F.a)) *
              ‖gaussianPolynomialFactor F.coeffs F.a
                (z - Complex.I * F.omega)‖) := by
    have hsum' := add_le_add hp' hm'
    convert hsum' using 1
    ring
  have hmain := mul_le_mul_of_nonneg_left (hsum.trans hfact)
    (by norm_num : (0 : ℝ) ≤ 1 / 2)
  simpa [mul_assoc] using hmain

noncomputable def gaborHatQuarticThreeLobeConst (F : GaborWeilTest) (σ : ℝ) : ℝ :=
  gaborHatThreeLobeConst F.a σ *
    (1 + gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
      (1 + |σ - 1 / 2| + |F.omega|) ^ 8)

lemma gaborHatQuarticThreeLobeConst_nonneg (F : GaborWeilTest) (σ : ℝ) :
    0 ≤ gaborHatQuarticThreeLobeConst F σ := by
  have ha : 0 < F.a := F.a_pos
  unfold gaborHatQuarticThreeLobeConst
  exact mul_nonneg (gaborHatThreeLobeConst_nonneg F.a σ ha) (by positivity)

lemma exp_shift_sq_add (a x y omega : ℝ) (ha : 0 < a) :
    Real.exp ((x ^ 2 - (y + omega) ^ 2) / (4 * a)) *
        Real.exp ((x ^ 2 - (y - omega) ^ 2) / (4 * a)) =
      Real.exp ((x ^ 2 - y ^ 2 - omega ^ 2) / (2 * a)) := by
  rw [← Real.exp_add]
  congr 1
  have : (y + omega) ^ 2 + (y - omega) ^ 2 = 2 * y ^ 2 + 2 * omega ^ 2 := by
    ring
  field_simp [ha.ne']
  linarith

lemma exp_shift_sq_sq (a x y : ℝ) (ha : 0 < a) :
    Real.exp ((x ^ 2 - y ^ 2) / (4 * a)) ^ 2 =
      Real.exp ((x ^ 2 - y ^ 2) / (2 * a)) := by
  rw [← Real.exp_nat_mul]
  congr 1
  field_simp [ha.ne']
  ring

lemma threeLobe_from_half_rate (a omega t σ' : ℝ) (ha : 0 < a) :
    Real.exp ((σ' ^ 2 - (t + omega) ^ 2) / (4 * a)) ^ 2 +
        Real.exp ((σ' ^ 2 - (t - omega) ^ 2) / (4 * a)) ^ 2 +
        2 * (Real.exp ((σ' ^ 2 - (t + omega) ^ 2) / (4 * a)) *
          Real.exp ((σ' ^ 2 - (t - omega) ^ 2) / (4 * a))) =
      Real.exp (σ' ^ 2 / (2 * a)) * gaborThreeLobe a omega t := by
  have hA := exp_shift_sq_sq a σ' (t + omega) ha
  have hB := exp_shift_sq_sq a σ' (t - omega) ha
  have hAB := exp_shift_sq_add a σ' t omega ha
  have e1 := exp_re_sq_split a σ' (t + omega) ha
  have e2 := exp_re_sq_split a σ' (t - omega) ha
  have e3 :
      Real.exp ((σ' ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)) =
        Real.exp (σ' ^ 2 / (2 * a)) *
          Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [ha.ne']
    ring
  rw [hA, hB, hAB, e1, e2, e3]
  unfold gaborThreeLobe
  ring

lemma norm_gaborHat_le_poly_three_lobe_of_not_pure
    {F : GaborWeilTest} (hF : F.coeffs ≠ ⟨1, 0, 0⟩) (s : ℂ) :
    ‖gaborHat F s‖ ≤
      gaborHatThreeLobeConst F.a s.re *
        (gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
          (1 + |s.re - 1 / 2| + |F.omega|) ^ 8) *
        (1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im := by
  have ha : 0 < F.a := F.a_pos
  set δ : ℂ := s - (1 / 2 : ℂ)
  have hδre : δ.re = s.re - 1 / 2 := by simp [δ, sub_re]
  have hδim : δ.im = s.im := by simp [δ, sub_im]
  have hhat : ‖gaborHat F s‖ =
      ‖gaborLaplace F δ‖ * ‖gaborLaplace F (-δ)‖ := by
    rw [gaborHat_of_not_pure hF, norm_mul]
  set Q : ℝ := gaborHatQuarticPolyFac F.coeffs F.a F.omega δ
  have hQ0 : 0 ≤ Q := gaborHatQuarticPolyFac_nonneg F.coeffs F.a F.omega ha δ
  have hP1 : ‖gaussianPolynomialFactor F.coeffs F.a
      (δ + Complex.I * F.omega)‖ ≤ Q := by
    simpa [Q, gaborHatQuarticPolyFac] using
      norm_P_shift_le F.coeffs F.a F.omega ha δ
  have hP2 : ‖gaussianPolynomialFactor F.coeffs F.a
      (δ - Complex.I * F.omega)‖ ≤ Q := by
    simpa [Q, gaborHatQuarticPolyFac] using
      norm_P_shift_sub_le F.coeffs F.a F.omega ha δ
  have hP3 : ‖gaussianPolynomialFactor F.coeffs F.a
      (-δ + Complex.I * F.omega)‖ ≤ Q := by
    have h := norm_P_shift_le F.coeffs F.a F.omega ha (-δ)
    simpa [Q, gaborHatQuarticPolyFac, abs_neg] using h
  have hP4 : ‖gaussianPolynomialFactor F.coeffs F.a
      (-δ - Complex.I * F.omega)‖ ≤ Q := by
    have h := norm_P_shift_sub_le F.coeffs F.a F.omega ha (-δ)
    simpa [Q, gaborHatQuarticPolyFac, abs_neg] using h
  set A : ℝ :=
    Real.exp ((δ.re ^ 2 - (δ.im + F.omega) ^ 2) / (4 * F.a))
  set B : ℝ :=
    Real.exp ((δ.re ^ 2 - (δ.im - F.omega) ^ 2) / (4 * F.a))
  have hA0 : 0 ≤ A := (Real.exp_pos _).le
  have hB0 : 0 ≤ B := (Real.exp_pos _).le
  have hH : ‖gaborLaplace F δ‖ ≤
      (1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q := by
    have h0 := norm_gaborLaplace_le F δ
    have hsum :
        A * ‖gaussianPolynomialFactor F.coeffs F.a
              (δ + Complex.I * F.omega)‖ +
            B * ‖gaussianPolynomialFactor F.coeffs F.a
              (δ - Complex.I * F.omega)‖ ≤
          (A + B) * Q := by
      nlinarith [hP1, hP2, hA0, hB0, hQ0]
    have := (h0.trans (mul_le_mul_of_nonneg_left hsum (by positivity)))
    simpa [A, B, mul_assoc] using this
  have hAn : Real.exp (((-δ).re ^ 2 - ((-δ).im + F.omega) ^ 2) / (4 * F.a)) =
      B := by
    simp [B, abs_neg]
    congr 1
    ring
  have hBn : Real.exp (((-δ).re ^ 2 - ((-δ).im - F.omega) ^ 2) / (4 * F.a)) =
      A := by
    simp [A]
    congr 1
    ring
  have hHn : ‖gaborLaplace F (-δ)‖ ≤
      (1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q := by
    have h0 := norm_gaborLaplace_le F (-δ)
    have hsum :
        Real.exp (((-δ).re ^ 2 - ((-δ).im + F.omega) ^ 2) / (4 * F.a)) *
              ‖gaussianPolynomialFactor F.coeffs F.a
                (-δ + Complex.I * F.omega)‖ +
            Real.exp (((-δ).re ^ 2 - ((-δ).im - F.omega) ^ 2) / (4 * F.a)) *
              ‖gaussianPolynomialFactor F.coeffs F.a
                (-δ - Complex.I * F.omega)‖ ≤
          (A + B) * Q := by
      rw [hAn, hBn]
      nlinarith [hP3, hP4, hA0, hB0, hQ0]
    have := h0.trans (mul_le_mul_of_nonneg_left hsum (by positivity))
    simpa [mul_assoc] using this
  have hhalfs :
      ((1 / 2) * Real.sqrt (Real.pi / F.a)) *
          ((1 / 2) * Real.sqrt (Real.pi / F.a)) =
        Real.pi / (4 * F.a) := by
    have hs : Real.sqrt (Real.pi / F.a) * Real.sqrt (Real.pi / F.a) =
        Real.pi / F.a :=
      Real.mul_self_sqrt (div_nonneg Real.pi_pos.le ha.le)
    calc
      (1 / 2) * Real.sqrt (Real.pi / F.a) *
          ((1 / 2) * Real.sqrt (Real.pi / F.a)) =
        (1 / 4) * (Real.sqrt (Real.pi / F.a) * Real.sqrt (Real.pi / F.a)) := by
        ring
      _ = (1 / 4) * (Real.pi / F.a) := by rw [hs]
      _ = Real.pi / (4 * F.a) := by field_simp [ha.ne']
  have hprod :
      ‖gaborLaplace F δ‖ * ‖gaborLaplace F (-δ)‖ ≤
        (Real.pi / (4 * F.a)) * (A + B) ^ 2 * Q ^ 2 := by
    have hmul := mul_le_mul hH hHn (norm_nonneg _)
      (mul_nonneg (mul_nonneg (mul_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)
        (Real.sqrt_nonneg _)) (add_nonneg hA0 hB0)) hQ0)
    have hrhs :
        ((1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q) *
            ((1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q) =
          (Real.pi / (4 * F.a)) * (A + B) ^ 2 * Q ^ 2 := by
      calc
        ((1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q) *
            ((1 / 2) * Real.sqrt (Real.pi / F.a) * (A + B) * Q) =
          (((1 / 2) * Real.sqrt (Real.pi / F.a)) *
              ((1 / 2) * Real.sqrt (Real.pi / F.a))) *
            ((A + B) ^ 2 * Q ^ 2) := by
          ring
        _ = (Real.pi / (4 * F.a)) * ((A + B) ^ 2 * Q ^ 2) := by
          rw [hhalfs]
        _ = (Real.pi / (4 * F.a)) * (A + B) ^ 2 * Q ^ 2 := by
          ring
    exact hmul.trans_eq hrhs
  have hsq :
      (A + B) ^ 2 =
        Real.exp (δ.re ^ 2 / (2 * F.a)) * gaborThreeLobe F.a F.omega δ.im := by
    unfold A B
    have := threeLobe_from_half_rate F.a F.omega δ.im δ.re ha
    convert this using 1
    ring
  have hconst :
      gaborHatThreeLobeConst F.a s.re =
        Real.pi / (4 * F.a) * Real.exp (δ.re ^ 2 / (2 * F.a)) := by
    unfold gaborHatThreeLobeConst
    simp [hδre]
  have hQsq : Q ^ 2 =
      gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
        (1 + |δ.re| + |F.omega|) ^ 8 * (1 + |δ.im|) ^ 8 :=
    gaborHatQuarticPolyFac_sq F.coeffs F.a F.omega δ
  have hfin :
      (Real.pi / (4 * F.a)) * (A + B) ^ 2 * Q ^ 2 =
        gaborHatThreeLobeConst F.a s.re *
          (gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
            (1 + |s.re - 1 / 2| + |F.omega|) ^ 8) *
          (1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im := by
    rw [hsq, hconst, hQsq, hδre, hδim]
    ring
  exact hhat.trans_le (hprod.trans_eq hfin)

theorem norm_gaborHat_le_poly_three_lobe (F : GaborWeilTest) (s : ℂ) :
    ‖gaborHat F s‖ ≤
      gaborHatQuarticThreeLobeConst F s.re *
        (1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im := by
  classical
  have ha : 0 < F.a := F.a_pos
  have hpow : (1 : ℝ) ≤ (1 + |s.im|) ^ 8 :=
    one_le_one_add_abs_pow s.im 8
  have hl0 : 0 ≤ gaborThreeLobe F.a F.omega s.im :=
    gaborThreeLobe_nonneg F.a F.omega s.im
  have hC0 : 0 ≤ gaborHatThreeLobeConst F.a s.re :=
    gaborHatThreeLobeConst_nonneg F.a s.re ha
  by_cases hF : F.coeffs = ⟨1, 0, 0⟩
  · have hthree := norm_gaborHat_le_three_lobe (F := F) hF s
    have hscale :
        gaborHatThreeLobeConst F.a s.re * gaborThreeLobe F.a F.omega s.im ≤
          gaborHatThreeLobeConst F.a s.re * ((1 + |s.im|) ^ 8 *
            gaborThreeLobe F.a F.omega s.im) :=
      mul_le_mul_of_nonneg_left (le_mul_of_one_le_left hl0 hpow) hC0
    have : ‖gaborHat F s‖ ≤
        gaborHatThreeLobeConst F.a s.re * ((1 + |s.im|) ^ 8 *
          gaborThreeLobe F.a F.omega s.im) :=
      hthree.trans hscale
    have hle : gaborHatThreeLobeConst F.a s.re ≤
        gaborHatQuarticThreeLobeConst F s.re := by
      unfold gaborHatQuarticThreeLobeConst
      refine le_mul_of_one_le_right hC0 ?_
      exact le_add_of_nonneg_right (by positivity)
    have h2 :
        gaborHatThreeLobeConst F.a s.re * ((1 + |s.im|) ^ 8 *
            gaborThreeLobe F.a F.omega s.im) ≤
          gaborHatQuarticThreeLobeConst F s.re * ((1 + |s.im|) ^ 8 *
            gaborThreeLobe F.a F.omega s.im) :=
      mul_le_mul_of_nonneg_right hle (mul_nonneg (by positivity) hl0)
    exact (this.trans h2).trans_eq (by ring)
  · have hnp := norm_gaborHat_le_poly_three_lobe_of_not_pure hF s
    have hle :
        gaborHatThreeLobeConst F.a s.re *
            (gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
              (1 + |s.re - 1 / 2| + |F.omega|) ^ 8) ≤
          gaborHatQuarticThreeLobeConst F s.re := by
      unfold gaborHatQuarticThreeLobeConst
      have : gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
          (1 + |s.re - 1 / 2| + |F.omega|) ^ 8 ≤
            1 + gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
              (1 + |s.re - 1 / 2| + |F.omega|) ^ 8 :=
        le_add_of_nonneg_left (by norm_num)
      exact mul_le_mul_of_nonneg_left this hC0
    have h2 :
        gaborHatThreeLobeConst F.a s.re *
            (gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
              (1 + |s.re - 1 / 2| + |F.omega|) ^ 8) *
            ((1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im) ≤
          gaborHatQuarticThreeLobeConst F s.re *
            ((1 + |s.im|) ^ 8 * gaborThreeLobe F.a F.omega s.im) :=
      mul_le_mul_of_nonneg_right hle (mul_nonneg (by positivity) hl0)
    exact (hnp.trans (by simpa [mul_assoc] using h2)).trans_eq (by ring)

theorem gaborHatQuarticThreeLobeRemainder_holds :
    GaborHatQuarticThreeLobeRemainder :=
  fun F =>
    ⟨gaborHatQuarticThreeLobeConst F,
      fun σ => gaborHatQuarticThreeLobeConst_nonneg F σ,
      fun s => norm_gaborHat_le_poly_three_lobe F s⟩

#print axioms norm_exp_sq_div_ofReal
#print axioms one_add_abs_pow_mul_gauss
#print axioms gaborHatQuarticThreeLobeRemainder_holds
#print axioms norm_gaborHat_le_poly_three_lobe
#print axioms gaborHat_criticalLine_nonneg
#print axioms gaborHat_one_nonneg

end RH
