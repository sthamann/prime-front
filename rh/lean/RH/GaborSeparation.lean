/-
RH/GaborSeparation.lean -- r542 Gabor-wavepacket separation architecture.
r547: live counting input is the proved Path A increment
`GaborIncrementBound` / `gaborIncrementBound_holds`.  Trudgian is
inactive Path B.
r550: prime channel of `GaborExplicitFormula` is the classical
comb `2Λ(n) n^{-1/2} g(log n)` (`combMass`), not the compact
honest weight `Λ(n)(1+n⁻¹)` refuted for `ĥ_W` by r548.

CLAIM BOUNDARY.  This file makes NO RH claim.  It proves only closed-form
Gaussian identities and the logical reduction from two remaining named
analytic inputs.  The increment bound is discharged by the r546 theorem.

SORRY CENSUS (r612): this file has no asserting `sorry`.  The former
asserting theorem `gabor_separationForAllZeros` is retired: the Prop
`GaborSeparationForAllZeros` is OVERSPECIFIED (prescribed packet
`a = σ²/64`, `ω = γ − πa/σ` per zero), believed false by r605N T3
(C4-cluster sign flip), and superseded by the existential form in
`GaborExposedOrbit.lean`.  The Prop is retained unasserted for the
historical record.  `GaborSeparationPrecheck` is the finite r541
window (unasserted: a numeric probe can certify it; it is not a Lean
proof).  `GaborExplicitFormula` is no longer asserted here; r558 wires
it from the r557 bricks plus named remainders in
`RH/GaborExplicitFormula.lean`.
The former `trudgian_zeroDensityBound` sorry is retired; the Prop
`TrudgianZeroDensityBound` remains as documented Path B.

The carrier records an even polynomial of degree at most four.  Its transform
is defined algebraically through the polynomial Gaussian Laplace transform.
For the pure-Gabor specialization `p = 1`, `gaborHat` uses the equivalent
three-exponential expansion directly; this makes critical-line positivity and
phase/scaling identities finite real/complex algebra, independent of an
integral-normalization API.
-/
import RH.GaborIntegral
import RH.ZeroIncrement
import RH.GaborThetaBound
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv

namespace RH

set_option maxHeartbeats 800000

open MeasureTheory
open scoped Classical
open Complex Finset

/-- Coefficients of the even polynomial `c₀ + c₂ t² + c₄ t⁴`. -/
structure EvenQuartic where
  c0 : ℝ
  c2 : ℝ
  c4 : ℝ

/-- The degree-at-most-four even polynomial carried by a Gabor test. -/
def EvenQuartic.eval (p : EvenQuartic) (t : ℝ) : ℝ :=
  p.c0 + p.c2 * t ^ 2 + p.c4 * t ^ 4

theorem EvenQuartic.eval_neg (p : EvenQuartic) (t : ℝ) :
    p.eval (-t) = p.eval t := by
  unfold EvenQuartic.eval
  ring

/-- Noncompact Gabor test carrier.  Evenness, Gaussian decay and the
degree-`≤ 4` even polynomial are already encoded by the fields
(`a_pos`, `EvenQuartic`, `carrier`).  Those are the only side
conditions used by the five-step Guinand–Weil decomposition for this
class (entirety, three-lobe decay, Gaussian strips).  The analytic
gate `admissible` is therefore the tautology — see
`GaborWeilTest.admissible`. -/
structure GaborWeilTest where
  a : ℝ
  omega : ℝ
  coeffs : EvenQuartic
  a_pos : 0 < a

/-- `h(t) = p(t) exp(-a t²) cos(ωt)`. -/
noncomputable def GaborWeilTest.carrier (F : GaborWeilTest) (t : ℝ) : ℝ :=
  F.coeffs.eval t * Real.exp (-F.a * t ^ 2) * Real.cos (F.omega * t)

/-- Analytic gate for `GaborExplicitFormula`.  The carrier type already
contains `a > 0`, evenness and the even quartic envelope, so no extra
Schwartz/compact-support field remains.  r555 records this as `True`
rather than an unconstrained `Prop` placeholder. -/
def GaborWeilTest.admissible (_F : GaborWeilTest) : Prop := True

theorem GaborWeilTest.carrier_even (F : GaborWeilTest) :
    Function.Even F.carrier := by
  intro t
  simp [GaborWeilTest.carrier, EvenQuartic.eval_neg, Real.cos_neg]

/-- Concrete Gaussian envelope; the remaining polynomial factor is explicit. -/
theorem GaborWeilTest.abs_carrier_le (F : GaborWeilTest) (t : ℝ) :
    |F.carrier t| ≤
      |F.coeffs.eval t| * Real.exp (-F.a * t ^ 2) := by
  unfold GaborWeilTest.carrier
  rw [abs_mul, abs_mul, abs_of_pos (Real.exp_pos _)]
  exact mul_le_of_le_one_right
    (mul_nonneg (abs_nonneg _) (Real.exp_pos _).le) (Real.abs_cos_le_one _)

/-- Polynomial factor in the exact bilateral Gaussian Laplace transform.
It is the moment formula for `c₀+c₂t²+c₄t⁴`. -/
noncomputable def gaussianPolynomialFactor
    (p : EvenQuartic) (a : ℝ) (z : ℂ) : ℂ :=
  p.c0 +
    p.c2 * ((1 : ℂ) / (2 * a) + z ^ 2 / (4 * a ^ 2)) +
    p.c4 * (3 / (4 * a ^ 2) + 3 * z ^ 2 / (4 * a ^ 3) +
      z ^ 4 / (16 * a ^ 4))

/-- Closed Gaussian Laplace transform for the polynomial Gaussian. -/
noncomputable def gaussianLaplace
    (p : EvenQuartic) (a : ℝ) (z : ℂ) : ℂ :=
  (Real.sqrt (Real.pi / a) : ℂ) *
    Complex.exp (z ^ 2 / (4 * a)) * gaussianPolynomialFactor p a z

/-- Closed transform of `h`: the average of the two frequency shifts. -/
noncomputable def gaborLaplace (F : GaborWeilTest) (z : ℂ) : ℂ :=
  (1 / 2 : ℂ) *
    (gaussianLaplace F.coeffs F.a (z + Complex.I * F.omega) +
     gaussianLaplace F.coeffs F.a (z - Complex.I * F.omega))

/-- Pure-Gabor three-exponential transform as a function of
`δ = s - 1/2`.  This is the expanded product `H(δ)H(-δ)`. -/
noncomputable def pureGaborHatDelta (a omega : ℝ) (δ : ℂ) : ℂ :=
  let σ := δ.re
  let t := δ.im
  ((Real.pi / (4 * a) : ℝ) : ℂ) *
    (((Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) : ℝ) : ℂ) *
        Complex.exp (Complex.I * (σ * (t + omega) / a)) +
      ((Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) : ℝ) : ℂ) *
        Complex.exp (Complex.I * (σ * (t - omega) / a)) +
      2 * ((Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)) : ℝ) : ℂ) *
        Complex.exp (Complex.I * (σ * t / a)))

/-- Closed Weil-shifted transform.  The pure specialization is expanded
definitionally; all other quartics use `H(δ)H(-δ)`. -/
noncomputable def gaborHat (F : GaborWeilTest) (s : ℂ) : ℂ :=
  by
    classical
    let δ := s - (1 / 2 : ℂ)
    exact if F.coeffs = ⟨1, 0, 0⟩ then
      pureGaborHatDelta F.a F.omega δ
    else
      gaborLaplace F δ * gaborLaplace F (-δ)

/-- Pure Gabor test `p = 1`.  Admissibility is the tautology on this
carrier (`GaborWeilTest.admissible`). -/
def pureGaborTest (a omega : ℝ) (ha : 0 < a) : GaborWeilTest where
  a := a
  omega := omega
  coeffs := ⟨1, 0, 0⟩
  a_pos := ha

lemma pureGaborTest_coeffs (a omega : ℝ) (ha : 0 < a) :
    (pureGaborTest a omega ha).coeffs = ⟨1, 0, 0⟩ :=
  rfl

lemma pureGaborTest_admissible (a omega : ℝ) (ha : 0 < a) :
    (pureGaborTest a omega ha).admissible :=
  trivial

/-- Exact three-Gaussian real value on the critical line. -/
noncomputable def pureGaborOnLine (a omega t : ℝ) : ℝ :=
  Real.pi / (4 * a) *
    (Real.exp (-(t + omega) ^ 2 / (2 * a)) +
     Real.exp (-(t - omega) ^ 2 / (2 * a)) +
     2 * Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)))

/-- r542 hard core (a): exact critical-line evaluation. -/
theorem gaborHat_pure_criticalLine
    (a omega t : ℝ) (ha : 0 < a) :
    gaborHat (pureGaborTest a omega ha)
        ((1 / 2 : ℂ) + t * Complex.I) =
      (pureGaborOnLine a omega t : ℂ) := by
  simp [gaborHat, pureGaborTest, pureGaborHatDelta, pureGaborOnLine,
    ne_of_gt ha]
  ring

/-- r542 hard core (a): the exact three-Gaussian value is nonnegative. -/
theorem pureGaborOnLine_nonneg
    (a omega t : ℝ) (ha : 0 < a) :
    0 ≤ pureGaborOnLine a omega t := by
  unfold pureGaborOnLine
  positivity

/-- r600: the three-Gaussian line value is a literal square
`(π/(4a))(e^{-(t+ω)²/4a} + e^{-(t-ω)²/4a})²`. -/
theorem pureGaborOnLine_eq_square
    (a omega t : ℝ) :
    pureGaborOnLine a omega t =
      Real.pi / (4 * a) *
        (Real.exp (-(t + omega) ^ 2 / (4 * a)) +
          Real.exp (-(t - omega) ^ 2 / (4 * a))) ^ 2 := by
  set A := Real.exp (-(t + omega) ^ 2 / (4 * a))
  set B := Real.exp (-(t - omega) ^ 2 / (4 * a))
  have hA : A * A = Real.exp (-(t + omega) ^ 2 / (2 * a)) := by
    unfold A
    rw [← Real.exp_add]
    congr 1
    ring
  have hB : B * B = Real.exp (-(t - omega) ^ 2 / (2 * a)) := by
    unfold B
    rw [← Real.exp_add]
    congr 1
    ring
  have hAB : A * B = Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) := by
    unfold A B
    rw [← Real.exp_add]
    congr 1
    ring
  have hsq : (A + B) ^ 2 =
      Real.exp (-(t + omega) ^ 2 / (2 * a)) +
        Real.exp (-(t - omega) ^ 2 / (2 * a)) +
        2 * Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) := by
    rw [add_sq, pow_two, pow_two, hA, hB, mul_assoc, hAB]
    ring
  simp [pureGaborOnLine, A, B, hsq]

/-- r600: critical-line nonnegativity for a pure packet. -/
theorem gaborHat_criticalLine_nonneg_pure
    (a omega t : ℝ) (ha : 0 < a) :
    0 ≤ (gaborHat (pureGaborTest a omega ha)
        ((1 / 2 : ℂ) + t * Complex.I)).re := by
  rw [gaborHat_pure_criticalLine]
  simpa using pureGaborOnLine_nonneg a omega t ha

/-- Closed pole value `Re ĥ_W(1)` of a pure packet:
`(π/(4a)) e^{(1/4-ω²)/(2a)} (2+2cos(ω/(2a)))`. -/
noncomputable def pureGaborHatAtOne (a omega : ℝ) : ℝ :=
  Real.pi / (4 * a) *
    Real.exp ((1 / 4 - omega ^ 2) / (2 * a)) *
      (2 + 2 * Real.cos (omega / (2 * a)))

theorem pureGaborHatAtOne_nonneg
    (a omega : ℝ) (ha : 0 < a) :
    0 ≤ pureGaborHatAtOne a omega := by
  unfold pureGaborHatAtOne
  have hcos : -1 ≤ Real.cos (omega / (2 * a)) := Real.neg_one_le_cos _
  have : 0 ≤ 2 + 2 * Real.cos (omega / (2 * a)) := by linarith
  positivity

/-- Euler: `e^{iθ} + e^{-iθ} = 2 cos θ`. -/
lemma exp_I_add_exp_neg_I (θ : ℝ) :
    Complex.exp (Complex.I * (θ : ℂ)) +
      Complex.exp (-(Complex.I * (θ : ℂ))) =
      (2 * Real.cos θ : ℂ) := by
  simp_rw [mul_comm Complex.I]
  have hneg : -((θ : ℂ) * Complex.I) = ((-θ : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [hneg, Complex.exp_ofReal_mul_I, Complex.exp_ofReal_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  ring

/-- r600: exact evaluation of a pure packet at the pole `s = 1`. -/
theorem gaborHat_pure_one
    (a omega : ℝ) (ha : 0 < a) :
    gaborHat (pureGaborTest a omega ha) 1 =
      (pureGaborHatAtOne a omega : ℂ) := by
  have hδ : (1 : ℂ) - (2⁻¹ : ℂ) = (1 / 2 : ℂ) := by norm_num
  have hre : (1 / 2 : ℂ).re = (1 / 2 : ℝ) := by norm_num
  have him : (1 / 2 : ℂ).im = (0 : ℝ) := by norm_num
  unfold gaborHat
  simp [pureGaborTest]
  rw [hδ]
  dsimp [pureGaborHatDelta]
  rw [hre, him]
  have hamp :
      ((1 / 2 : ℝ) ^ 2 - (0 + omega) ^ 2) / (2 * a) =
        ((1 / 4 : ℝ) - omega ^ 2) / (2 * a) := by ring
  have hamp' :
      ((1 / 2 : ℝ) ^ 2 - (0 - omega) ^ 2) / (2 * a) =
        ((1 / 4 : ℝ) - omega ^ 2) / (2 * a) := by ring
  have hmid :
      ((1 / 2 : ℝ) ^ 2 - (0 : ℝ) ^ 2 - omega ^ 2) / (2 * a) =
        ((1 / 4 : ℝ) - omega ^ 2) / (2 * a) := by ring
  have hpC :
      ((1 / 2 : ℝ) : ℂ) * (((0 : ℝ) : ℂ) + (omega : ℂ)) / (a : ℂ) =
        (omega / (2 * a) : ℂ) := by
    push_cast; ring
  have hpC' :
      ((1 / 2 : ℝ) : ℂ) * (((0 : ℝ) : ℂ) - (omega : ℂ)) / (a : ℂ) =
        (-(omega / (2 * a) : ℝ) : ℂ) := by
    push_cast; ring
  have hp0C :
      ((1 / 2 : ℝ) : ℂ) * ((0 : ℝ) : ℂ) / (a : ℂ) = 0 := by
    push_cast; ring
  rw [hamp, hamp', hmid, hpC, hpC', hp0C, mul_zero, Complex.exp_zero, mul_one]
  unfold pureGaborHatAtOne
  have hph1 :
      (omega : ℂ) / (2 * (a : ℂ)) = ((omega / (2 * a) : ℝ) : ℂ) := by
    push_cast; ring
  have hph2 :
      Complex.I * -((omega / (2 * a) : ℝ) : ℂ) =
        -(Complex.I * ((omega / (2 * a) : ℝ) : ℂ)) := by
    ring
  rw [hph1, hph2]
  set E := Real.exp ((1 / 4 - omega ^ 2) / (2 * a))
  have hθ := exp_I_add_exp_neg_I (omega / (2 * a))
  have hpull :
      ((E : ℝ) : ℂ) *
            Complex.exp (Complex.I * ((omega / (2 * a) : ℝ) : ℂ)) +
          ((E : ℝ) : ℂ) *
            Complex.exp (-(Complex.I * ((omega / (2 * a) : ℝ) : ℂ))) +
          2 * ((E : ℝ) : ℂ) =
        ((E : ℝ) : ℂ) *
          (Complex.exp (Complex.I * ((omega / (2 * a) : ℝ) : ℂ)) +
            Complex.exp (-(Complex.I * ((omega / (2 * a) : ℝ) : ℂ))) +
            2) := by
    ring
  rw [hpull, hθ]
  push_cast
  ring

/-- r600: pole term of a pure packet is nonnegative. -/
theorem gaborHat_one_nonneg_pure
    (a omega : ℝ) (ha : 0 < a) :
    0 ≤ (gaborHat (pureGaborTest a omega ha) 1).re := by
  rw [gaborHat_pure_one, Complex.ofReal_re]
  exact pureGaborHatAtOne_nonneg a omega ha

/-- Specialization `a = 1`, `ω = 0`: `Re ĥ(1) = π e^{1/8}`. -/
theorem gaborHat_pure_one_zero
    (ha : 0 < (1 : ℝ)) :
    (gaborHat (pureGaborTest 1 0 ha) 1).re =
      Real.pi * Real.exp (1 / 8) := by
  rw [gaborHat_pure_one, Complex.ofReal_re]
  unfold pureGaborHatAtOne
  simp [Real.cos_zero]
  ring

/-- r610: `π e^{1/8} > 3`. -/
theorem gaborHat_pure_one_zero_gt_three
    (ha : 0 < (1 : ℝ)) :
    (3 : ℝ) < (gaborHat (pureGaborTest 1 0 ha) 1).re := by
  rw [gaborHat_pure_one_zero]
  have hπ : (3 : ℝ) < Real.pi := Real.pi_gt_three
  have hexp : (1 : ℝ) < Real.exp (1 / 8) :=
    Real.one_lt_exp_iff.mpr (by norm_num)
  have hpos : (0 : ℝ) < Real.pi := lt_trans (by norm_num) hπ
  have hmul :
      (3 : ℝ) * 1 < Real.pi * Real.exp (1 / 8) :=
    mul_lt_mul hπ hexp.le (by norm_num) hpos.le
  simpa using hmul

lemma gaborHat_pureGaborTest_eq
    (a omega : ℝ) (ha : 0 < a) (s : ℂ) :
    gaborHat (pureGaborTest a omega ha) s =
      pureGaborHatDelta a omega (s - (1 / 2 : ℂ)) := by
  unfold gaborHat
  simp [pureGaborTest]

lemma norm_cexp_I_mul_real (θ : ℝ) :
    ‖Complex.exp (Complex.I * (θ : ℂ))‖ = 1 := by
  rw [Complex.norm_exp]
  have hre : (Complex.I * (θ : ℂ)).re = 0 := by
    simp [mul_re, I_re, I_im]
  simp [hre]

/-- Exact three-lobe collapse at `a = 1`, `ω = 0`. -/
lemma pureGaborHatDelta_one_zero (δ : ℂ) :
    pureGaborHatDelta 1 0 δ =
      ((Real.pi : ℝ) : ℂ) *
        ((Real.exp ((δ.re ^ 2 - δ.im ^ 2) / 2) : ℝ) : ℂ) *
          Complex.exp (Complex.I * ((δ.re * δ.im : ℝ) : ℂ)) := by
  dsimp [pureGaborHatDelta]
  have hamp :
      ((δ.re ^ 2 - (δ.im + 0) ^ 2) / (2 * (1 : ℝ))) =
        (δ.re ^ 2 - δ.im ^ 2) / 2 := by ring
  have hamp' :
      ((δ.re ^ 2 - (δ.im - 0) ^ 2) / (2 * (1 : ℝ))) =
        (δ.re ^ 2 - δ.im ^ 2) / 2 := by ring
  have hmid :
      ((δ.re ^ 2 - δ.im ^ 2 - (0 : ℝ) ^ 2) / (2 * (1 : ℝ))) =
        (δ.re ^ 2 - δ.im ^ 2) / 2 := by ring
  have hph :
      δ.re * (δ.im + 0) / (1 : ℝ) = δ.re * δ.im := by ring
  have hph' :
      δ.re * (δ.im - 0) / (1 : ℝ) = δ.re * δ.im := by ring
  have hph0 :
      δ.re * δ.im / (1 : ℝ) = δ.re * δ.im := by ring
  simp [hamp, hamp', hmid, hph, hph', hph0]
  push_cast
  ring

lemma delta_re_im (s : ℂ) :
    (s - (1 / 2 : ℂ)).re = s.re - 1 / 2 ∧
      (s - (1 / 2 : ℂ)).im = s.im := by
  simp [sub_re, sub_im]

/-- `|ĥ_{F₀}(s)| = π exp(((Re s − 1/2)² − (Im s)²)/2)`. -/
theorem norm_gaborHat_pure_one_zero
    (ha : 0 < (1 : ℝ)) (s : ℂ) :
    ‖gaborHat (pureGaborTest 1 0 ha) s‖ =
      Real.pi * Real.exp (((s.re - 1 / 2) ^ 2 - s.im ^ 2) / 2) := by
  rw [gaborHat_pureGaborTest_eq, pureGaborHatDelta_one_zero]
  have hδ := delta_re_im s
  rw [hδ.1, hδ.2]
  have hπ : ‖((Real.pi : ℝ) : ℂ)‖ = Real.pi :=
    Complex.norm_of_nonneg Real.pi_pos.le
  have hE :
      ‖((Real.exp (((s.re - 1 / 2) ^ 2 - s.im ^ 2) / 2) : ℝ) : ℂ)‖ =
        Real.exp (((s.re - 1 / 2) ^ 2 - s.im ^ 2) / 2) :=
    Complex.norm_of_nonneg (Real.exp_pos _).le
  have hP :
      ‖Complex.exp (Complex.I * (((s.re - 1 / 2) * s.im : ℝ) : ℂ))‖ = 1 :=
    norm_cexp_I_mul_real _
  rw [norm_mul, norm_mul, hπ, hE, hP, mul_one]

lemma re_sub_half_sq_le_quarter {s : ℂ}
    (hs : IsCriticalStripZetaZero s) :
    (s.re - 1 / 2) ^ 2 ≤ (1 / 2 : ℝ) ^ 2 := by
  have habs : |s.re - 1 / 2| ≤ (1 / 2 : ℝ) :=
    abs_le.mpr ⟨by linarith [hs.2.1], by linarith [hs.2.2]⟩
  have hhalf : |(1 / 2 : ℝ)| = (1 / 2 : ℝ) := abs_of_nonneg (by norm_num)
  exact sq_le_sq.mpr (habs.trans_eq hhalf.symm)

/-- Strip majorant: `|ĥ_{F₀}(ρ)| ≤ π e^{1/8} e^{−(Im ρ)²/2}`. -/
theorem norm_gaborHat_pure_one_zero_strip
    (ha : 0 < (1 : ℝ)) {s : ℂ}
    (hs : IsCriticalStripZetaZero s) :
    ‖gaborHat (pureGaborTest 1 0 ha) s‖ ≤
      Real.pi * Real.exp (1 / 8) * Real.exp (-s.im ^ 2 / 2) := by
  rw [norm_gaborHat_pure_one_zero ha s]
  have hsplit :
      Real.exp (((s.re - 1 / 2) ^ 2 - s.im ^ 2) / 2) =
        Real.exp ((s.re - 1 / 2) ^ 2 / 2) *
          Real.exp (-s.im ^ 2 / 2) := by
    rw [← Real.exp_add]
    congr 1
    ring
  rw [hsplit, ← mul_assoc]
  have hE : 0 ≤ Real.exp (-s.im ^ 2 / 2) := (Real.exp_pos _).le
  have h8 : ((1 / 2 : ℝ) ^ 2) / 2 = (1 / 8 : ℝ) := by norm_num
  have hdiv :
      ((s.re - 1 / 2) ^ 2) / 2 ≤ ((1 / 2 : ℝ) ^ 2) / 2 :=
    div_le_div_of_nonneg_right (re_sub_half_sq_le_quarter hs)
      (show (0 : ℝ) ≤ 2 by norm_num)
  have hre :
      Real.exp ((s.re - 1 / 2) ^ 2 / 2) ≤ Real.exp (1 / 8) :=
    Real.exp_le_exp.mpr (hdiv.trans_eq h8)
  have hπ :
      Real.pi * Real.exp ((s.re - 1 / 2) ^ 2 / 2) ≤
        Real.pi * Real.exp (1 / 8) :=
    mul_le_mul_of_nonneg_left hre Real.pi_pos.le
  exact mul_le_mul_of_nonneg_right hπ hE

/-- r610 threshold: Path-A increment times `e^{-T₀²/2}` drops below 1
at `T₀ = 4`.  Classically the first strip zero sits at 14.1347. -/
def gaborF0LowHeight : ℝ := 4

/-- Classically true (first zero at 14.1347), not in Mathlib. -/
def GaborLowHeightZeroFree (T₀ : ℝ) : Prop :=
  ∀ s : ℂ, IsCriticalStripZetaZero s → T₀ ≤ |s.im|

/-- Unit-bin Gaussian used by the F₀ tail: `0` on bins that cannot
meet `|Im| ≥ T₀`, otherwise `exp(−d²/2)` with
`d = max(T₀, left endpoint)`. -/
noncomputable def gaborF0BinGauss (T₀ : ℝ) (k : ℤ) : ℝ :=
  if T₀ ≤ (k : ℝ) + 1 ∨ (k : ℝ) < -T₀ then
    Real.exp
      (-(max T₀ (if 0 ≤ k then (k : ℝ) else |((k : ℝ) + 1)|)) ^ 2 / 2)
  else
    0

lemma gaborF0BinGauss_nonneg (T₀ : ℝ) (k : ℤ) :
    0 ≤ gaborF0BinGauss T₀ k := by
  unfold gaborF0BinGauss
  apply ite_nonneg
  · exact le_of_lt (Real.exp_pos _)
  · exact le_rfl

lemma gaborF0BinGauss_le_exp_neg_eight (k : ℤ) :
    gaborF0BinGauss 4 k ≤ Real.exp (-(4 : ℝ) ^ 2 / 2) := by
  unfold gaborF0BinGauss
  by_cases h : (4 : ℝ) ≤ (k : ℝ) + 1 ∨ (k : ℝ) < -4
  · rw [if_pos h]
    set d := max (4 : ℝ) (if 0 ≤ k then (k : ℝ) else |((k : ℝ) + 1)|)
    have hd : (4 : ℝ) ≤ d := le_max_left _ _
    have hd0 : (0 : ℝ) ≤ d := le_trans (by norm_num) hd
    have hsq : (4 : ℝ) ^ 2 ≤ d ^ 2 :=
      sq_le_sq.mpr (by
        rw [abs_of_nonneg (by norm_num : (0 : ℝ) ≤ (4 : ℝ)), abs_of_nonneg hd0]
        exact hd)
    exact Real.exp_le_exp.mpr
      (div_le_div_of_nonneg_right (neg_le_neg hsq) (by norm_num))
  · rw [if_neg h]
    exact (Real.exp_pos _).le

lemma log_add_three_nonneg (k : ℤ) :
    0 ≤ 1 + Real.log ((|k| : ℝ) + 3) := by
  have : (1 : ℝ) ≤ (|k| : ℝ) + 3 := by nlinarith [abs_nonneg (k : ℝ)]
  exact add_nonneg (by norm_num) (Real.log_nonneg this)

lemma one_add_log_le_four_of_le_ten {k : ℤ}
    (hk : |k| ≤ 10) :
    1 + Real.log ((|k| : ℝ) + 3) ≤ 4 := by
  have hx : (0 : ℝ) < (|k| : ℝ) + 3 := by nlinarith [abs_nonneg (k : ℝ)]
  have hle : (|k| : ℝ) + 3 ≤ 13 := by
    have : (|k| : ℝ) ≤ 10 := by exact_mod_cast hk
    linarith
  have hlog := Real.log_le_log hx hle
  have h13 : Real.log (13 : ℝ) ≤ Real.log (16 : ℝ) :=
    Real.log_le_log (by norm_num) (by norm_num)
  have h16 : Real.log (16 : ℝ) = Real.log ((2 : ℝ) ^ 4) := by norm_num
  have hpow : Real.log ((2 : ℝ) ^ 4) = 4 * Real.log 2 :=
    Real.log_pow 2 4
  have h2 : Real.log 2 < (7 / 10 : ℝ) :=
    lt_trans Real.log_two_lt_d9 (by norm_num)
  have : 4 * Real.log 2 < 4 * (7 / 10 : ℝ) :=
    mul_lt_mul_of_pos_left h2 (by norm_num)
  have : 4 * (7 / 10 : ℝ) < (3 : ℝ) := by norm_num
  linarith [hlog, h13, h16, hpow]

lemma rpow_neg_nine_eighths_le_mvt {n : ℕ} (hn : 1 ≤ n) :
    ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) ≤
      8 * ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
        ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) := by
  have ha : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (Nat.succ_le_iff.mp hn)
  have hab : (n : ℝ) < (n : ℝ) + 1 := lt_add_one _
  have hnb : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by exact_mod_cast rfl
  set f : ℝ → ℝ := fun t => t ^ (-(1 / 8 : ℝ))
  have hcont : ContinuousOn f (Set.Icc (n : ℝ) ((n : ℝ) + 1)) := by
    apply ContinuousOn.rpow_const continuousOn_id
    intro t ht
    exact Or.inl (ne_of_gt (lt_of_lt_of_le ha ht.1))
  have hder : ∀ t ∈ Set.Ioo (n : ℝ) ((n : ℝ) + 1),
      HasDerivAt f ((-(1 / 8 : ℝ)) * t ^ (-(1 / 8 : ℝ) - 1)) t := by
    intro t ht
    have ht0 : t ≠ 0 := ne_of_gt (lt_trans ha ht.1)
    dsimp [f]
    exact Real.hasDerivAt_rpow_const (p := -(1 / 8 : ℝ)) (Or.inl ht0)
  obtain ⟨c, hc, hslope⟩ :=
    exists_hasDerivAt_eq_slope f
      (fun t => (-(1 / 8 : ℝ)) * t ^ (-(1 / 8 : ℝ) - 1)) hab hcont hder
  have hp : -(1 / 8 : ℝ) - 1 = -(9 / 8 : ℝ) := by ring
  have hdiv :
      (f ((n : ℝ) + 1) - f (n : ℝ)) /
          (((n : ℝ) + 1) - (n : ℝ)) =
        f ((n : ℝ) + 1) - f (n : ℝ) := by
    have : ((n : ℝ) + 1) - (n : ℝ) = 1 := by ring
    simp [this]
  have hfeq :
      (-(1 / 8 : ℝ)) * c ^ (-(1 / 8 : ℝ) - 1) =
        f ((n : ℝ) + 1) - f (n : ℝ) := by
    simpa [hdiv] using hslope
  have hfeq' :
      (-(1 / 8 : ℝ)) * c ^ (-(9 / 8 : ℝ)) =
        f ((n : ℝ) + 1) - f (n : ℝ) := by
    rw [← hp]
    exact hfeq
  have hdiff :
      f (n : ℝ) - f ((n : ℝ) + 1) =
        (1 / 8 : ℝ) * c ^ (-(9 / 8 : ℝ)) := by
    linarith [hfeq']
  have hcpos : (0 : ℝ) < c := lt_trans ha hc.1
  have hmono :
      ((n : ℝ) + 1) ^ (-(9 / 8 : ℝ)) ≤ c ^ (-(9 / 8 : ℝ)) :=
    Real.rpow_le_rpow_of_exponent_nonpos hcpos hc.2.le (by norm_num)
  have hc8 :
      c ^ (-(9 / 8 : ℝ)) = 8 * (f (n : ℝ) - f ((n : ℝ) + 1)) := by
    rw [hdiff]; ring
  have : ((n : ℝ) + 1) ^ (-(9 / 8 : ℝ)) ≤
      8 * (f (n : ℝ) - f ((n : ℝ) + 1)) := by
    rwa [← hc8]
  simpa [f, hnb] using this

lemma telescope_rpow_one_eight (N : ℕ) :
    ∑ n ∈ Icc 1 N,
        ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
          ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) =
      (1 : ℝ) ^ (-(1 / 8 : ℝ)) -
        ((N + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ)) := by
  induction N with
  | zero =>
    have hempty : (Icc 1 0 : Finset ℕ) = ∅ :=
      Icc_eq_empty_of_lt (by norm_num)
    simp [hempty]
  | succ N ih =>
    have hnot : N + 1 ∉ Icc 1 N := by
      intro h
      exact Nat.not_succ_le_self N (mem_Icc.mp h).2
    have hunion : Icc 1 (N + 1) = insert (N + 1) (Icc 1 N) := by
      ext x
      simp only [mem_Icc, mem_insert]
      omega
    rw [hunion, sum_insert hnot, ih]
    ring

lemma zetaFractCellMajorant_one_div_eight_le_nine :
    zetaFractCellMajorant (1 / 8) ≤ 9 := by
  refine Real.tsum_le_of_sum_le
      (fun _ => Real.rpow_nonneg (Nat.cast_nonneg _) _) ?_
  intro S
  let Spos := S.filter (fun n : ℕ => 1 ≤ n)
  have h0 :
      ∑ n ∈ S.filter (fun n : ℕ => n = 0),
          ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) ≤ 1 := by
    have hsub : S.filter (fun n : ℕ => n = 0) ⊆ ({0} : Finset ℕ) := by
      intro n hn
      simp only [mem_filter, mem_singleton] at hn ⊢
      exact hn.2
    have hle :=
      sum_le_sum_of_subset_of_nonneg
        (f := fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ))) hsub
        (fun _ _ _ => Real.rpow_nonneg (Nat.cast_nonneg _) _)
    have hone :
        ∑ n ∈ ({0} : Finset ℕ),
            ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) = 1 := by
      simp [Real.one_rpow]
    exact hle.trans_eq hone
  have hpos :
      ∑ n ∈ Spos, ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) ≤ 8 := by
    by_cases hne : Spos.Nonempty
    · let N := Spos.sup id
      have hsub : Spos ⊆ Icc 1 N := by
        intro n hn
        exact mem_Icc.mpr ⟨(mem_filter.mp hn).2, Finset.le_sup (f := id) hn⟩
      have hmvt : ∀ n ∈ Spos,
          ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) ≤
            8 * ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
              ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) :=
        fun n hn => rpow_neg_nine_eighths_le_mvt (mem_filter.mp hn).2
      have hsum := sum_le_sum hmvt
      have htel :
          ∑ n ∈ Spos,
              ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
                ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) ≤
            ∑ n ∈ Icc 1 N,
                ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
                  ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) :=
        sum_le_sum_of_subset_of_nonneg hsub fun n hn _ => by
          have hn1 : 1 ≤ n := (mem_Icc.mp hn).1
          have hn0 : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (Nat.succ_le_iff.mp hn1)
          have hxy : (n : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by exact_mod_cast Nat.le_succ n
          have hmono :=
            Real.rpow_le_rpow_of_exponent_nonpos hn0 hxy
              (by norm_num : -(1 / 8 : ℝ) ≤ 0)
          linarith
      have hval := telescope_rpow_one_eight N
      have hone : (1 : ℝ) ^ (-(1 / 8 : ℝ)) = 1 := Real.one_rpow _
      have htail :
          (0 : ℝ) ≤ ((N + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ)) :=
        Real.rpow_nonneg (Nat.cast_nonneg _) _
      have htel' :
          ∑ n ∈ Icc 1 N,
              ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
                ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) ≤ 1 := by
        rw [hval, hone]
        linarith [htail]
      have h8 :
          ∑ n ∈ Spos, 8 * ((n : ℝ) ^ (-(1 / 8 : ℝ)) -
              ((n + 1 : ℕ) : ℝ) ^ (-(1 / 8 : ℝ))) ≤ 8 := by
        rw [← mul_sum]
        nlinarith [htel.trans htel']
      exact hsum.trans h8
    · simp [Finset.not_nonempty_iff_eq_empty.mp hne]
  have hsplit :
      ∑ n ∈ S, ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) =
        ∑ n ∈ S.filter (fun n : ℕ => n = 0),
            ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) +
          ∑ n ∈ Spos, ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)) := by
    have hnot : S.filter (fun n : ℕ => ¬ n = 0) = Spos := by
      ext n
      constructor
      · intro hn
        exact mem_filter.mpr ⟨(mem_filter.mp hn).1,
          Nat.succ_le_iff.mpr (Nat.pos_of_ne_zero (mem_filter.mp hn).2)⟩
      · intro hn
        exact mem_filter.mpr ⟨(mem_filter.mp hn).1,
          ne_of_gt (Nat.succ_le_iff.mp (mem_filter.mp hn).2)⟩
    rw [← sum_filter_add_sum_filter_not
        (f := fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-(9 / 8 : ℝ)))
        S (fun n : ℕ => n = 0), hnot]
  linarith [hsplit, h0, hpos]

lemma jensenSphereMajorantCoeff_le_fifty_six :
    jensenSphereMajorantCoeff ≤ 56 := by
  unfold jensenSphereMajorantCoeff
  have hCI := zetaFractCellMajorant_one_div_eight_le_nine
  have h6 : (6 : ℝ) * zetaFractCellMajorant (1 / 8) ≤ 54 := by
    nlinarith [zetaFractCellMajorant_nonneg (δ := 1 / 8), hCI]
  linarith

lemma log_fourteen_over_thirteen_ge_one_div_fourteen :
    (1 / 14 : ℝ) ≤ Real.log (14 / 13) := by
  have hx : (0 : ℝ) < 14 / 13 := by norm_num
  have hexp :=
    Real.exp_bound_div_one_sub_of_interval
      (by norm_num : (0 : ℝ) ≤ 1 / 14)
      (by norm_num : (1 / 14 : ℝ) < 1)
  have hfrac : 1 / (1 - (1 / 14 : ℝ)) = (14 / 13 : ℝ) := by norm_num
  have : Real.exp (1 / 14) ≤ 14 / 13 := by
    rwa [hfrac] at hexp
  exact (Real.le_log_iff_exp_le hx).mpr this

lemma zetaZerosInDiskCardBoundInner_lt_one_hundred_twenty :
    zetaZerosInDiskCardBoundInner < 120 := by
  have hK : jensenSphereMajorantCoeff ≤ (2 : ℝ) ^ (6 : ℕ) :=
    le_trans jensenSphereMajorantCoeff_le_fifty_six (by norm_num)
  have hKpos : (0 : ℝ) < jensenSphereMajorantCoeff :=
    jensenSphereMajorantCoeff_pos
  have hlogK : Real.log jensenSphereMajorantCoeff ≤ 6 * Real.log 2 := by
    have := Real.log_le_log hKpos hK
    have hpow : Real.log ((2 : ℝ) ^ (6 : ℕ)) = (6 : ℕ) * Real.log 2 :=
      Real.log_pow 2 6
    have hcast : ((6 : ℕ) : ℝ) * Real.log 2 = 6 * Real.log 2 := by norm_cast
    linarith
  have hζ : ‖riemannZeta 2‖ < 3 := by
    rw [norm_riemannZeta_two]
    have hsq : Real.pi ^ 2 < (4 : ℝ) ^ 2 :=
      sq_lt_sq.mpr (by
        rw [abs_of_pos Real.pi_pos, abs_of_pos (by norm_num : (0 : ℝ) < 4)]
        exact Real.pi_lt_four)
    have : Real.pi ^ 2 / 6 < 16 / 6 := by
      have h16 : (4 : ℝ) ^ 2 = 16 := by norm_num
      exact div_lt_div_of_pos_right (h16 ▸ hsq) (by norm_num)
    linarith
  have hζpos : (0 : ℝ) < ‖riemannZeta 2‖ :=
    lt_trans (by norm_num) one_lt_norm_riemannZeta_two
  have hlogζ : Real.log ‖riemannZeta 2‖ < 2 * Real.log 2 := by
    have h3 : Real.log ‖riemannZeta 2‖ < Real.log 3 :=
      Real.log_lt_log hζpos hζ
    have h4 : Real.log (3 : ℝ) < Real.log 4 :=
      Real.log_lt_log (by norm_num) (by norm_num)
    have hpow : Real.log (4 : ℝ) = 2 * Real.log 2 := by
      rw [show (4 : ℝ) = (2 : ℝ) ^ (2 : ℕ) by norm_num, Real.log_pow]
      norm_cast
    linarith
  have h2 : Real.log 2 < (7 / 10 : ℝ) :=
    lt_trans Real.log_two_lt_d9 (by norm_num)
  have hnum :
      Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2 < 8 := by
    have : 6 * Real.log 2 + 2 * Real.log 2 + 2 < 8 := by
      nlinarith [h2]
    linarith [hlogK, hlogζ]
  have hden := log_fourteen_over_thirteen_ge_one_div_fourteen
  have hdenpos : (0 : ℝ) < Real.log (14 / 13) :=
    lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1 / 14) hden
  unfold zetaZerosInDiskCardBoundInner
  have hlt : (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) /
        Real.log (14 / 13) < 8 / Real.log (14 / 13) :=
    div_lt_div_of_pos_right hnum hdenpos
  have hle : 8 / Real.log (14 / 13) ≤ 8 / (1 / 14 : ℝ) :=
    div_le_div_of_nonneg_left (by norm_num) (by norm_num) hden
  have h814 : (8 : ℝ) / (1 / 14) = 112 := by norm_num
  linarith [hlt, hle, h814]

lemma exp_eight_gt_2800 : (2800 : ℝ) < Real.exp 8 := by
  have he : (27 / 10 : ℝ) < Real.exp 1 :=
    lt_trans (by norm_num) Real.exp_one_gt_d9
  have hpow : ((27 / 10 : ℝ) ^ 8) < Real.exp 1 ^ 8 :=
    pow_lt_pow_left₀ he (by norm_num) (Nat.succ_ne_zero 7)
  have hexp : Real.exp 1 ^ 8 = Real.exp 8 := by
    rw [← Real.exp_nat_mul]
    norm_num
  have hnum : (2800 : ℝ) < (27 / 10 : ℝ) ^ 8 := by norm_num
  linarith

lemma exp_four_gt_fifty : (50 : ℝ) < Real.exp 4 := by
  have he : (27 / 10 : ℝ) < Real.exp 1 :=
    lt_trans (by norm_num) Real.exp_one_gt_d9
  have hpow : ((27 / 10 : ℝ) ^ 4) < Real.exp 1 ^ 4 :=
    pow_lt_pow_left₀ he (by norm_num) (Nat.succ_ne_zero 3)
  have hexp : Real.exp 1 ^ 4 = Real.exp 4 := by
    rw [← Real.exp_nat_mul]
    norm_num
  have hnum : (50 : ℝ) < (27 / 10 : ℝ) ^ 4 := by norm_num
  linarith

lemma exp_eighteen_gt :
    (7800000 : ℝ) < Real.exp 18 := by
  have h8 := exp_eight_gt_2800
  have h2 : (7 : ℝ) < Real.exp 2 := by
    have he : (27 / 10 : ℝ) < Real.exp 1 :=
      lt_trans (by norm_num) Real.exp_one_gt_d9
    have hpow : ((27 / 10 : ℝ) ^ 2) < Real.exp 1 ^ 2 :=
      pow_lt_pow_left₀ he (by norm_num) (Nat.succ_ne_zero 1)
    have hexp : Real.exp 1 ^ 2 = Real.exp 2 := by
      rw [← Real.exp_nat_mul]
      norm_num
    have hnum : (7 : ℝ) < (27 / 10 : ℝ) ^ 2 := by norm_num
    linarith
  have : Real.exp 18 = Real.exp 8 * Real.exp 8 * Real.exp 2 := by
    have h18 : (18 : ℝ) = 8 + 8 + 2 := by norm_num
    rw [h18, add_assoc, Real.exp_add, Real.exp_add]
    ring
  nlinarith [h8, h2, Real.exp_pos 8, Real.exp_pos 2]

lemma one_add_log_le_sixteen_div_five {k : ℤ} (hk : |k| ≤ 5) :
    1 + Real.log ((|k| : ℝ) + 3) ≤ 16 / 5 := by
  have hx : (0 : ℝ) < (|k| : ℝ) + 3 := by nlinarith [abs_nonneg (k : ℝ)]
  have hle : (|k| : ℝ) + 3 ≤ 8 := by
    have : (|k| : ℝ) ≤ 5 := by exact_mod_cast hk
    linarith
  have hlog := Real.log_le_log hx hle
  have h8 : Real.log (8 : ℝ) = 3 * Real.log 2 := by
    rw [show (8 : ℝ) = (2 : ℝ) ^ (3 : ℕ) by norm_num, Real.log_pow]
    norm_cast
  have h2 : Real.log 2 < (7 / 10 : ℝ) :=
    lt_trans Real.log_two_lt_d9 (by norm_num)
  nlinarith [hlog, h8, h2]



noncomputable def gaborF0BinCount (k : ℤ) : ℝ :=
  2 * zetaZerosInDiskCardBoundInner * (1 + Real.log ((|k| : ℝ) + 3))

lemma gaborF0BinCount_nonneg (k : ℤ) : 0 ≤ gaborF0BinCount k :=
  mul_nonneg (mul_nonneg (by norm_num) (le_of_lt zetaZerosInDiskCardBoundInner_pos))
    (log_add_three_nonneg k)

lemma log_disk_center_le_int (k : ℤ) :
    1 + Real.log (2 + |((k : ℝ) + 1 / 2)|) ≤
      1 + Real.log ((|k| : ℝ) + 3) := by
  have habs : |((k : ℝ) + 1 / 2)| ≤ (|k| : ℝ) + 1 := by
    have := abs_add_le (k : ℝ) (1 / 2)
    have : |(1 / 2 : ℝ)| = (1 / 2 : ℝ) := abs_of_pos (by norm_num)
    linarith
  have hx : (0 : ℝ) < 2 + |((k : ℝ) + 1 / 2)| := by positivity
  have hle : 2 + |((k : ℝ) + 1 / 2)| ≤ (|k| : ℝ) + 3 := by linarith
  exact add_le_add_right (Real.log_le_log hx hle) 1

lemma log_disk_center_neg_le_int (k : ℤ) :
    1 + Real.log (2 + |(-(k : ℝ) - 1 + 1 / 2)|) ≤
      1 + Real.log ((|k| : ℝ) + 3) := by
  have hτ : |(-(k : ℝ) - 1 + 1 / 2)| = |((k : ℝ) + 1 / 2)| := by
    have : -(k : ℝ) - 1 + (1 / 2 : ℝ) = -((k : ℝ) + 1 / 2) := by ring
    rw [this, abs_neg]
  rw [hτ]
  exact log_disk_center_le_int k

lemma gaborF0_bin_if_of_height {t : ℝ} {k : ℤ}
    (hbin : (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)
    (hT : (4 : ℝ) ≤ |t|) :
    (4 : ℝ) ≤ (k : ℝ) + 1 ∨ (k : ℝ) < -4 := by
  cases lt_or_ge t 0 with
  | inl ht0 =>
    refine Or.inr ?_
    have : t ≤ -4 := by
      have : |t| = -t := abs_of_neg ht0
      linarith
    linarith [hbin.1]
  | inr ht0 =>
    refine Or.inl ?_
    have : (4 : ℝ) ≤ t := by rwa [abs_of_nonneg ht0] at hT
    exact le_trans this hbin.2

lemma exp_neg_im_sq_le_binGauss {t : ℝ} {k : ℤ}
    (hbin : (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)
    (hT : (4 : ℝ) ≤ |t|) :
    Real.exp (-t ^ 2 / 2) ≤ gaborF0BinGauss 4 k := by
  have hif := gaborF0_bin_if_of_height hbin hT
  set d := max (4 : ℝ) (if 0 ≤ k then (k : ℝ) else |((k : ℝ) + 1)|)
  have hd4 : (4 : ℝ) ≤ d := le_max_left _ _
  have hd0 : (0 : ℝ) ≤ d := le_trans (by norm_num) hd4
  have hd_le : d ≤ |t| := by
    refine max_le hT ?_
    by_cases hk : 0 ≤ k
    · simp only [hk, ↓reduceIte]
      have ht0 : (0 : ℝ) ≤ t := le_trans (by exact_mod_cast hk) hbin.1.le
      rw [abs_of_nonneg ht0]
      exact hbin.1.le
    · simp only [hk, ↓reduceIte]
      have hk0 : k < 0 := lt_of_not_ge hk
      have hk1z : k + 1 ≤ 0 := (Int.lt_iff_add_one_le).mp hk0
      have hk1 : (k : ℝ) + 1 ≤ 0 := by exact_mod_cast hk1z
      have htnonpos : t ≤ 0 := le_trans hbin.2 hk1
      rw [abs_of_nonpos htnonpos, abs_of_nonpos hk1]
      linarith [hbin.2]
  have hsq : d ^ 2 ≤ t ^ 2 :=
    sq_le_sq.mpr (by rwa [abs_of_nonneg hd0])
  unfold gaborF0BinGauss
  rw [if_pos hif]
  exact Real.exp_le_exp.mpr
    (div_le_div_of_nonneg_right (neg_le_neg hsq) (by norm_num))

lemma gaborF0_bin_re_ge_subset
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) (k : ℤ) :
    ((S.filter (fun ρ =>
        ordinateBin ρ.val.im = k ∧ (1 / 2 : ℝ) ≤ ρ.val.re)).image
      Subtype.val) ⊆ landauInnerDisk ((k : ℝ) + 1 / 2) := by
  intro w hw
  obtain ⟨ρ, hρ, rfl⟩ := mem_image.mp hw
  have hρf := mem_filter.mp hρ
  have hbin := mem_ordinateBin ρ.val.im
  rw [hρf.2.1] at hbin
  have hre : (1 / 2 : ℝ) ≤ ρ.val.re := hρf.2.2
  have hre1 : ρ.val.re ≤ 1 := le_of_lt ρ.property.2.2
  have him : (k : ℝ) ≤ ρ.val.im ∧ ρ.val.im ≤ (k : ℝ) + 1 :=
    ⟨hbin.1.le, hbin.2⟩
  refine mem_riemannZetaZerosInClosedDisk.mpr
    ⟨?_, ρ.property.1, isCriticalStripZetaZero_ne_one ρ.property⟩
  simpa [landauInnerDisk] using mem_unit_height_inner_disk hre hre1 him

lemma gaborF0_bin_re_lt_image_subset
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) (k : ℤ) :
    ((S.filter (fun ρ =>
        ordinateBin ρ.val.im = k ∧ ρ.val.re < (1 / 2 : ℝ))).image
      (fun ρ => (1 : ℂ) - ρ.val)) ⊆
      landauInnerDisk (-(k : ℝ) - 1 + 1 / 2) := by
  intro w hw
  obtain ⟨ρ, hρ, rfl⟩ := mem_image.mp hw
  have hρf := mem_filter.mp hρ
  have hbin := mem_ordinateBin ρ.val.im
  rw [hρf.2.1] at hbin
  have hre_ge : (1 / 2 : ℝ) ≤ ((1 : ℂ) - ρ.val).re := by
    simp only [sub_re, one_re]; linarith [hρf.2.2]
  have hre_le : ((1 : ℂ) - ρ.val).re ≤ 1 := by
    simp only [sub_re, one_re]; linarith [ρ.property.2.1]
  have him : (-(k : ℝ) - 1) ≤ ((1 : ℂ) - ρ.val).im ∧
      ((1 : ℂ) - ρ.val).im ≤ (-(k : ℝ) - 1 + 1) := by
    simp only [sub_im, one_im]
    constructor <;> linarith [hbin.1, hbin.2]
  have h1z := isCriticalStrip_one_sub ρ.property
  refine mem_riemannZetaZerosInClosedDisk.mpr
    ⟨?_, h1z.1, isCriticalStripZetaZero_ne_one h1z⟩
  simpa [landauInnerDisk] using
    mem_unit_height_inner_disk (N := -(k : ℝ) - 1) hre_ge hre_le him

lemma gaborF0_sum_mult_bin_le
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) (k : ℤ)
    (hT : ∀ ρ ∈ S, (2 : ℝ) ≤ |ρ.val.im|) :
    (S.filter (fun ρ => ordinateBin ρ.val.im = k)).sum
        (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) ≤
      gaborF0BinCount k := by
  set Sk := S.filter (fun ρ => ordinateBin ρ.val.im = k)
  set Sge := Sk.filter (fun ρ => (1 / 2 : ℝ) ≤ ρ.val.re)
  set Slt := Sk.filter (fun ρ => ρ.val.re < (1 / 2 : ℝ))
  have hunion : Sge ∪ Slt = Sk := by
    ext ρ
    constructor
    · intro h
      rcases mem_union.mp h with h | h
      · exact (mem_filter.mp h).1
      · exact (mem_filter.mp h).1
    · intro h
      by_cases hre : (1 / 2 : ℝ) ≤ ρ.val.re
      · exact mem_union.mpr (Or.inl (mem_filter.mpr ⟨h, hre⟩))
      · exact mem_union.mpr (Or.inr (mem_filter.mpr ⟨h, lt_of_not_ge hre⟩))
  have hdisj : Disjoint Sge Slt := by
    refine disjoint_left.mpr ?_
    intro ρ hge hlt
    exact (not_lt_of_ge (mem_filter.mp hge).2) (mem_filter.mp hlt).2
  have hpart :
      Sk.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) =
        Sge.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) +
          Slt.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) := by
    rw [← hunion, sum_union hdisj]
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hge :
      Sge.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) ≤
        zetaZerosInDiskCardBoundInner *
          (1 + Real.log (2 + |((k : ℝ) + 1 / 2)|)) := by
    have hSge :
        Sge = S.filter (fun ρ =>
          ordinateBin ρ.val.im = k ∧ (1 / 2 : ℝ) ≤ ρ.val.re) := by
      ext ρ
      simp [Sge, Sk, mem_filter, and_assoc]
    have hinj : Set.InjOn (Subtype.val :
        {z : ℂ // IsCriticalStripZetaZero z} → ℂ) Sge :=
      fun _ _ _ _ h => Subtype.ext h
    have hsum :
        Sge.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) =
          (Sge.image Subtype.val).sum
            (fun z => (riemannZetaMultiplicity z : ℝ)) :=
      (sum_image (g := Subtype.val)
        (f := fun z => (riemannZetaMultiplicity z : ℝ)) hinj).symm
    have hsub : Sge.image Subtype.val ⊆ landauInnerDisk ((k : ℝ) + 1 / 2) := by
      rw [hSge]; exact gaborF0_bin_re_ge_subset S k
    have hle := sum_le_sum_of_subset_of_nonneg
        (f := fun z : ℂ => (riemannZetaMultiplicity z : ℝ)) hsub
        (fun _ _ _ => Nat.cast_nonneg _)
    exact (hsum.trans_le hle).trans
      (sum_multiplicity_landauInnerDisk_le ((k : ℝ) + 1 / 2))
  have hlt :
      Slt.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) ≤
        zetaZerosInDiskCardBoundInner *
          (1 + Real.log (2 + |(-(k : ℝ) - 1 + 1 / 2)|)) := by
    have hSlt :
        Slt = S.filter (fun ρ =>
          ordinateBin ρ.val.im = k ∧ ρ.val.re < (1 / 2 : ℝ)) := by
      ext ρ
      simp [Slt, Sk, mem_filter, and_assoc]
    have hinj : Set.InjOn
        (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} => (1 : ℂ) - ρ.val)
        Slt :=
      fun _ _ _ _ h => Subtype.ext (sub_right_inj.mp h)
    have hm : ∀ ρ ∈ Slt,
        riemannZetaMultiplicity ρ.val =
          riemannZetaMultiplicity ((1 : ℂ) - ρ.val) := by
      intro ρ hρ
      have hS : ρ ∈ S := (mem_filter.mp ((mem_filter.mp hρ).1)).1
      exact riemannZetaMultiplicity_eq_one_sub ρ.property (hT ρ hS)
    have hsum :
        Slt.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) =
          (Slt.image (fun ρ => (1 : ℂ) - ρ.val)).sum
            (fun z => (riemannZetaMultiplicity z : ℝ)) := by
      have hcongr :
          Slt.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) =
            Slt.sum (fun ρ =>
              (riemannZetaMultiplicity ((1 : ℂ) - ρ.val) : ℝ)) :=
        sum_congr rfl fun ρ hρ => by exact_mod_cast (hm ρ hρ)
      have himg :=
        sum_image (g := fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
            (1 : ℂ) - ρ.val)
          (f := fun z : ℂ => (riemannZetaMultiplicity z : ℝ)) hinj
      exact hcongr.trans himg.symm
    have hsub : Slt.image (fun ρ => (1 : ℂ) - ρ.val) ⊆
        landauInnerDisk (-(k : ℝ) - 1 + 1 / 2) := by
      rw [hSlt]; exact gaborF0_bin_re_lt_image_subset S k
    have hle := sum_le_sum_of_subset_of_nonneg
        (f := fun z : ℂ => (riemannZetaMultiplicity z : ℝ)) hsub
        (fun _ _ _ => Nat.cast_nonneg _)
    exact (hsum.trans_le hle).trans
      (sum_multiplicity_landauInnerDisk_le (-(k : ℝ) - 1 + 1 / 2))
  have hp := hge.trans (mul_le_mul_of_nonneg_left (log_disk_center_le_int k) hC0)
  have hm := hlt.trans
    (mul_le_mul_of_nonneg_left (log_disk_center_neg_le_int k) hC0)
  unfold gaborF0BinCount
  rw [hpart]
  linarith [hp, hm]

lemma one_add_log_le_add_three (k : ℤ) :
    1 + Real.log ((|k| : ℝ) + 3) ≤ (|k| : ℝ) + 3 := by
  have hx : (0 : ℝ) < (|k| : ℝ) + 3 := by nlinarith [abs_nonneg (k : ℝ)]
  have hy : ((|k| : ℝ) + 3) ≤ Real.exp ((|k| : ℝ) + 2) := by
    have := Real.add_one_le_exp ((|k| : ℝ) + 2)
    linarith
  have hlog : Real.log ((|k| : ℝ) + 3) ≤ (|k| : ℝ) + 2 :=
    (Real.log_le_iff_le_exp hx).mpr hy
  linarith

lemma gaborF0_count_le_two_forty_mul (k : ℤ) :
    gaborF0BinCount k ≤ 240 * (1 + Real.log ((|k| : ℝ) + 3)) := by
  unfold gaborF0BinCount
  have hC : zetaZerosInDiskCardBoundInner ≤ 120 :=
    le_of_lt zetaZerosInDiskCardBoundInner_lt_one_hundred_twenty
  have hlog := log_add_three_nonneg k
  have h2 : (2 : ℝ) * zetaZerosInDiskCardBoundInner ≤ 240 := by
    nlinarith [hC]
  exact mul_le_mul_of_nonneg_right h2 hlog

lemma half_geom_sum_le (N : ℕ) :
    ∑ m ∈ range N, ((1 / 2 : ℝ) ^ m) ≤ 2 := by
  have hr : (1 / 2 : ℝ) ≠ 1 := by norm_num
  have h := geom_sum_eq hr N
  have hp : (0 : ℝ) ≤ ((1 / 2 : ℝ) ^ N) := by positivity
  have heq : ∑ m ∈ range N, ((1 / 2 : ℝ) ^ m) =
      2 * (1 - (1 / 2 : ℝ) ^ N) := by
    rw [h]
    field_simp
    ring
  have : 2 * (1 - (1 / 2 : ℝ) ^ N) ≤ 2 := by nlinarith [hp]
  exact heq.le.trans this

lemma exp_neg_two_le_half : Real.exp (-2) ≤ (1 / 2 : ℝ) := by
  have h2 : (2 : ℝ) ≤ Real.exp 2 :=
    le_trans (by norm_num) (Real.add_one_le_exp 2)
  have hpos : (0 : ℝ) < Real.exp 2 := Real.exp_pos _
  have hinv : Real.exp (-2) = 1 / Real.exp 2 := by
    rw [eq_div_iff hpos.ne', ← Real.exp_add]
    simp
  rw [hinv]
  exact div_le_div_of_nonneg_left (by norm_num) (by norm_num) h2

lemma gaborF0_near_term_le {k : ℤ} (hk : k = 3 ∨ k = 4 ∨ k = -5) :
    gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      2 * 120 * (16 / 5) * Real.exp (-8) := by
  have habs : |k| ≤ 5 := by
    rcases hk with rfl | rfl | rfl <;> norm_num
  have hlog := one_add_log_le_sixteen_div_five habs
  have hG := gaborF0BinGauss_le_exp_neg_eight k
  have h8 : Real.exp (-(4 : ℝ) ^ 2 / 2) = Real.exp (-8) := by norm_num
  rw [h8] at hG
  have hC : zetaZerosInDiskCardBoundInner ≤ 120 :=
    le_of_lt zetaZerosInDiskCardBoundInner_lt_one_hundred_twenty
  have hnn1 := gaborF0BinGauss_nonneg (4 : ℝ) k
  have hnn2 := log_add_three_nonneg k
  unfold gaborF0BinCount
  have h1 : (2 : ℝ) * zetaZerosInDiskCardBoundInner *
      (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k ≤
        2 * 120 * (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k :=
    mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hC (by norm_num)) hnn2) hnn1
  have h2 : 2 * 120 * (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k ≤
      2 * 120 * (16 / 5) * gaborF0BinGauss 4 k :=
    mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left hlog (by positivity)) hnn1
  have h3 : 2 * 120 * (16 / 5) * gaborF0BinGauss 4 k ≤
      2 * 120 * (16 / 5) * Real.exp (-8) :=
    mul_le_mul_of_nonneg_left hG (by positivity)
  exact h1.trans (h2.trans h3)

lemma gaborF0BinGauss_mid {k : ℤ} (hk : k = 5 ∨ k = -6) :
    gaborF0BinGauss 4 k ≤ Real.exp (-(25 / 2)) := by
  unfold gaborF0BinGauss
  have hif : (4 : ℝ) ≤ (k : ℝ) + 1 ∨ (k : ℝ) < -4 := by
    rcases hk with rfl | rfl <;> norm_num
  rw [if_pos hif]
  have hd : max (4 : ℝ) (if 0 ≤ k then (k : ℝ) else |((k : ℝ) + 1)|) = 5 := by
    rcases hk with rfl | rfl <;> norm_num
  rw [hd]
  have : -((5 : ℝ) ^ 2) / 2 = -(25 / 2) := by norm_num
  rw [this]

lemma gaborF0_mid_term_le {k : ℤ} (hk : k = 5 ∨ k = -6) :
    gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      2 * 120 * 4 * Real.exp (-(25 / 2)) := by
  have habs : |k| ≤ 10 := by
    rcases hk with rfl | rfl <;> norm_num
  have hlog := one_add_log_le_four_of_le_ten habs
  have hG := gaborF0BinGauss_mid hk
  have hC : zetaZerosInDiskCardBoundInner ≤ 120 :=
    le_of_lt zetaZerosInDiskCardBoundInner_lt_one_hundred_twenty
  have hnn1 := gaborF0BinGauss_nonneg (4 : ℝ) k
  have hnn2 := log_add_three_nonneg k
  unfold gaborF0BinCount
  have h1 : (2 : ℝ) * zetaZerosInDiskCardBoundInner *
      (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k ≤
        2 * 120 * (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k :=
    mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hC (by norm_num)) hnn2) hnn1
  have h2 : 2 * 120 * (1 + Real.log ((|k| : ℝ) + 3)) * gaborF0BinGauss 4 k ≤
      2 * 120 * 4 * gaborF0BinGauss 4 k :=
    mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left hlog (by positivity)) hnn1
  have h3 : 2 * 120 * 4 * gaborF0BinGauss 4 k ≤
      2 * 120 * 4 * Real.exp (-(25 / 2)) :=
    mul_le_mul_of_nonneg_left hG (by positivity)
  exact h1.trans (h2.trans h3)

lemma gaborF0BinGauss_of_ge_six {k : ℤ} (hk : 6 ≤ k) :
    gaborF0BinGauss 4 k = Real.exp (-(k : ℝ) ^ 2 / 2) := by
  have hk0 : 0 ≤ k := le_trans (by norm_num : (0 : ℤ) ≤ 6) hk
  have hif : (4 : ℝ) ≤ (k : ℝ) + 1 := by
    exact_mod_cast (le_trans (by norm_num : (4 : ℤ) ≤ 7) (by omega : (7 : ℤ) ≤ k + 1))
  have h4 : (4 : ℝ) ≤ (k : ℝ) := by
    exact_mod_cast (le_trans (by norm_num : (4 : ℤ) ≤ 6) hk)
  unfold gaborF0BinGauss
  rw [if_pos (Or.inl hif)]
  simp [hk0, max_eq_right h4]

lemma gaborF0_farP_term_le {k : ℤ} (hk : 6 ≤ k) :
    gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((k - 6).toNat)) := by
  have hk0 : (0 : ℤ) ≤ k - 6 := sub_nonneg.mpr hk
  have hcast : ((k - 6).toNat : ℝ) = (k : ℝ) - 6 := by
    exact_mod_cast Int.toNat_of_nonneg hk0
  rw [gaborF0BinGauss_of_ge_six hk]
  have hkR : (6 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hsq : 3 * (k : ℝ) ≤ (k : ℝ) ^ 2 / 2 := by nlinarith
  have hG : Real.exp (-((k : ℝ) ^ 2 / 2)) ≤ Real.exp (-(3 * (k : ℝ))) :=
    Real.exp_le_exp.mpr (neg_le_neg hsq)
  have hG' : Real.exp (-(k : ℝ) ^ 2 / 2) ≤ Real.exp (-3 * (k : ℝ)) := by
    have hL : -(k : ℝ) ^ 2 / 2 = -((k : ℝ) ^ 2 / 2) := by ring
    have hR : -3 * (k : ℝ) = -(3 * (k : ℝ)) := by ring
    rw [hL, hR]
    exact hG
  have hlog := one_add_log_le_add_three k
  have habs : |k| = k := abs_of_nonneg (le_trans (by norm_num : (0 : ℤ) ≤ 6) hk)
  have hcount : gaborF0BinCount k ≤ 240 * ((k : ℝ) + 3) := by
    have hle := gaborF0_count_le_two_forty_mul k
    have hkR0 : (0 : ℝ) ≤ (k : ℝ) := by
      exact_mod_cast (le_trans (by norm_num : (0 : ℤ) ≤ 6) hk)
    have hlog' := one_add_log_le_add_three k
    rw [abs_of_nonneg hkR0] at hle hlog'
    have hnn := log_add_three_nonneg k
    nlinarith [hle, hlog', hnn]
  have hk2 : (k : ℝ) + 3 ≤ 2 * (k : ℝ) := by nlinarith
  have hkexp : (k : ℝ) ≤ Real.exp (k : ℝ) := by
    have := Real.add_one_le_exp (k : ℝ)
    linarith
  have hprod :
      ((k : ℝ) + 3) * Real.exp (-(k : ℝ) ^ 2 / 2) ≤
        2 * Real.exp (-2 * (k : ℝ)) := by
    have h1 := mul_le_mul hk2 hG' (Real.exp_pos _).le (by nlinarith)
    have h2 :
        2 * (k : ℝ) * Real.exp (-3 * (k : ℝ)) ≤
          2 * Real.exp (k : ℝ) * Real.exp (-3 * (k : ℝ)) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hkexp (by norm_num)) (Real.exp_pos _).le
    have h3 : 2 * Real.exp (k : ℝ) * Real.exp (-3 * (k : ℝ)) =
        2 * Real.exp (-2 * (k : ℝ)) := by
      rw [mul_assoc, ← Real.exp_add]
      congr 2
      ring
    nlinarith [h1, h2, h3]
  have hshift : Real.exp (-2 * (k : ℝ)) =
      Real.exp (-12) * Real.exp (-2 * ((k : ℝ) - 6)) := by
    rw [← Real.exp_add]; congr 1; ring
  have hpow : Real.exp (-2 * ((k : ℝ) - 6)) ≤
      (1 / 2 : ℝ) ^ ((k - 6).toNat) := by
    have heq : Real.exp (-2 * ((k : ℝ) - 6)) =
        Real.exp (-2) ^ ((k - 6).toNat) := by
      rw [← hcast]
      have hmul : -2 * ((k - 6).toNat : ℝ) =
          ((k - 6).toNat : ℝ) * (-2) := by ring
      rw [hmul, Real.exp_nat_mul]
    rw [heq]
    exact pow_le_pow_left₀ (Real.exp_pos _).le exp_neg_two_le_half _
  have hnnC := gaborF0BinCount_nonneg k
  have hnnG : (0 : ℝ) ≤ Real.exp (-(k : ℝ) ^ 2 / 2) := (Real.exp_pos _).le
  nlinarith [hcount, hprod, hshift, hpow, hnnC, hnnG, Real.exp_pos (-12)]

lemma gaborF0BinGauss_of_le_neg_seven {k : ℤ} (hk : k ≤ -7) :
    gaborF0BinGauss 4 k = Real.exp (-(|((k : ℝ) + 1)|) ^ 2 / 2) := by
  have hneg : k < 0 := lt_of_le_of_lt hk (by decide : (-7 : ℤ) < 0)
  have hif : (k : ℝ) < -4 := by
    have : k < -4 := lt_of_le_of_lt hk (by decide : (-7 : ℤ) < -4)
    exact_mod_cast this
  have hk0 : ¬ 0 ≤ k := not_le.mpr hneg
  unfold gaborF0BinGauss
  rw [if_pos (Or.inr hif)]
  simp [hk0]
  have h4 : (4 : ℝ) ≤ |((k : ℝ) + 1)| := by
    have : (k : ℝ) + 1 ≤ -6 := by exact_mod_cast (by omega : k + 1 ≤ -6)
    have habs : |((k : ℝ) + 1)| = -((k : ℝ) + 1) := abs_of_nonpos (by linarith)
    linarith
  rw [max_eq_right h4]
  rw [sq_abs]

lemma gaborF0_farN_term_le {k : ℤ} (hk : k ≤ -7) :
    gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) := by
  rw [gaborF0BinGauss_of_le_neg_seven hk]
  have hd : |((k : ℝ) + 1)| = -((k : ℝ) + 1) := by
    have : (k : ℝ) + 1 ≤ 0 := by exact_mod_cast (by omega : k + 1 ≤ 0)
    exact abs_of_nonpos this
  have ht : (6 : ℝ) ≤ -((k : ℝ) + 1) := by
    exact_mod_cast (by omega : (6 : ℤ) ≤ -(k + 1))
  rw [hd]
  set t := -((k : ℝ) + 1)
  have hsq : 3 * t ≤ t ^ 2 / 2 := by
    have : (6 : ℝ) ≤ t := ht
    nlinarith
  have hG : Real.exp (-(t ^ 2 / 2)) ≤ Real.exp (-(3 * t)) :=
    Real.exp_le_exp.mpr (neg_le_neg hsq)
  have hG' : Real.exp (-t ^ 2 / 2) ≤ Real.exp (-3 * t) := by
    have hL : -t ^ 2 / 2 = -(t ^ 2 / 2) := by ring
    have hR : -3 * t = -(3 * t) := by ring
    rw [hL, hR]
    exact hG
  have hlog := one_add_log_le_add_three k
  have habs : |k| = -k := abs_of_neg (lt_of_le_of_lt hk (by decide : (-7 : ℤ) < 0))
  have hcount : gaborF0BinCount k ≤ 240 * ((|k| : ℝ) + 3) := by
    have hlt := gaborF0_count_le_two_forty_mul k
    nlinarith [hlt, hlog, log_add_three_nonneg k]
  have hkt : (|k| : ℝ) + 3 = t + 4 := by
    have habsR : (|k| : ℝ) = -(k : ℝ) := by exact_mod_cast habs
    simp [t, habsR]
    ring
  have hcount' : gaborF0BinCount k ≤ 240 * (t + 4) := by
    rwa [← hkt]
  have ht2 : t + 4 ≤ 2 * t := by nlinarith [ht]
  have htexp : t ≤ Real.exp t := by
    have := Real.add_one_le_exp t
    linarith
  have hprod : (t + 4) * Real.exp (-t ^ 2 / 2) ≤ 2 * Real.exp (-2 * t) := by
    have h1 := mul_le_mul ht2 hG' (Real.exp_pos _).le (by nlinarith [ht])
    have h2 : 2 * t * Real.exp (-3 * t) ≤ 2 * Real.exp t * Real.exp (-3 * t) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left htexp (by norm_num)) (Real.exp_pos _).le
    have h3 : 2 * Real.exp t * Real.exp (-3 * t) = 2 * Real.exp (-2 * t) := by
      rw [mul_assoc, ← Real.exp_add]; congr 2; ring
    nlinarith [h1, h2, h3]
  have hshift : Real.exp (-2 * t) =
      Real.exp (-12) * Real.exp (-2 * (t - 6)) := by
    rw [← Real.exp_add]; congr 1; ring
  have hcast : ((-k - 7).toNat : ℝ) = t - 6 := by
    have hnn : (0 : ℤ) ≤ -k - 7 := by omega
    have hc : ((-k - 7).toNat : ℝ) = (-k - 7 : ℤ) := by
      exact_mod_cast Int.toNat_of_nonneg hnn
    simp [t] at hc ⊢
    linarith
  have hpow : Real.exp (-2 * (t - 6)) ≤ (1 / 2 : ℝ) ^ ((-k - 7).toNat) := by
    have heq : Real.exp (-2 * (t - 6)) = Real.exp (-2) ^ ((-k - 7).toNat) := by
      rw [← hcast]
      have hmul : -2 * ((-k - 7).toNat : ℝ) =
          ((-k - 7).toNat : ℝ) * (-2) := by ring
      rw [hmul, Real.exp_nat_mul]
    rw [heq]
    exact pow_le_pow_left₀ (Real.exp_pos _).le exp_neg_two_le_half _
  have hnnC := gaborF0BinCount_nonneg k
  have hnnG : (0 : ℝ) ≤ Real.exp (-t ^ 2 / 2) := (Real.exp_pos _).le
  have hmul :
      gaborF0BinCount k * Real.exp (-t ^ 2 / 2) ≤
        240 * (t + 4) * Real.exp (-t ^ 2 / 2) :=
    mul_le_mul_of_nonneg_right hcount' hnnG
  nlinarith [hmul, hprod, hshift, hpow, hnnC, hnnG, Real.exp_pos (-12)]

lemma gaborF0_term_nonneg (k : ℤ) :
    0 ≤ gaborF0BinCount k * gaborF0BinGauss 4 k :=
  mul_nonneg (gaborF0BinCount_nonneg k) (gaborF0BinGauss_nonneg 4 k)

lemma gaborF0_exp_neg_eight_inv :
    Real.exp (-8) = 1 / Real.exp 8 := by
  have hpos : (0 : ℝ) < Real.exp 8 := Real.exp_pos _
  rw [eq_div_iff hpos.ne', ← Real.exp_add]
  simp

lemma gaborF0_exp_neg_twelve_inv :
    Real.exp (-12) = 1 / Real.exp 12 := by
  have hpos : (0 : ℝ) < Real.exp 12 := Real.exp_pos _
  rw [eq_div_iff hpos.ne', ← Real.exp_add]
  simp

lemma gaborF0_exp_twelve_eq : Real.exp 12 = Real.exp 8 * Real.exp 4 := by
  rw [← Real.exp_add]
  norm_num

lemma gaborF0_near_budget :
    (3 : ℝ) * (2 * 120 * (16 / 5) * Real.exp (-8)) < (5 / 6 : ℝ) := by
  have h2800 := exp_eight_gt_2800
  have hnum : (3 : ℝ) * (2 * 120 * (16 / 5)) = 2304 := by norm_num
  have hrew : (3 : ℝ) * (2 * 120 * (16 / 5) * Real.exp (-8)) =
      2304 * Real.exp (-8) := by
    rw [← hnum]; ring
  rw [hrew, gaborF0_exp_neg_eight_inv, ← div_eq_mul_one_div]
  have hfrac : (2304 : ℝ) / 2800 < 5 / 6 := by norm_num
  have hlt : (2304 : ℝ) / Real.exp 8 < 2304 / 2800 :=
    div_lt_div_of_pos_left (by norm_num) (by norm_num) h2800
  linarith

lemma gaborF0_far_budget :
    (1920 : ℝ) * Real.exp (-12) < (1 / 50 : ℝ) := by
  have h8 := exp_eight_gt_2800
  have h4 := exp_four_gt_fifty
  have hprod : (140000 : ℝ) < Real.exp 8 * Real.exp 4 := by nlinarith
  rw [gaborF0_exp_neg_twelve_inv, gaborF0_exp_twelve_eq, ← div_eq_mul_one_div]
  have hlt : (1920 : ℝ) / (Real.exp 8 * Real.exp 4) < 1920 / 140000 :=
    div_lt_div_of_pos_left (by norm_num) (by positivity) hprod
  have : (1920 : ℝ) / 140000 < 1 / 50 := by norm_num
  linarith

lemma gaborF0_mid_budget :
    (2 : ℝ) * (2 * 120 * 4 * Real.exp (-(25 / 2))) < (1 / 50 : ℝ) := by
  have hle : Real.exp (-(25 / 2)) ≤ Real.exp (-12) :=
    Real.exp_le_exp.mpr (by norm_num)
  have hmul :
      (2 : ℝ) * (2 * 120 * 4 * Real.exp (-(25 / 2))) ≤
        1920 * Real.exp (-12) := by
    have hnum : (2 : ℝ) * (2 * 120 * 4) = 1920 := by norm_num
    have h1 :
        (2 : ℝ) * (2 * 120 * 4 * Real.exp (-(25 / 2))) =
          1920 * Real.exp (-(25 / 2)) := by
      rw [← hnum]; ring
    rw [h1]
    exact mul_le_mul_of_nonneg_left hle (by norm_num)
  exact lt_of_le_of_lt hmul gaborF0_far_budget

lemma gaborF0_term_eq_zero_of_inactive {k : ℤ}
    (h3 : ¬ (k = 3 ∨ k = 4 ∨ k = -5))
    (h5 : ¬ (k = 5 ∨ k = -6))
    (h6 : ¬ 6 ≤ k)
    (h7 : ¬ k ≤ -7) :
    gaborF0BinCount k * gaborF0BinGauss 4 k = 0 := by
  have hif : ¬ ((4 : ℝ) ≤ (k : ℝ) + 1 ∨ (k : ℝ) < -4) := by
    refine not_or.mpr ⟨?_, ?_⟩
    · intro hle
      have : (4 : ℤ) ≤ k + 1 := by exact_mod_cast hle
      omega
    · intro hlt
      have : k < (-4 : ℤ) := by exact_mod_cast hlt
      omega
  unfold gaborF0BinGauss
  rw [if_neg hif, mul_zero]

lemma gaborF0_near_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k = 3 ∨ k = 4 ∨ k = -5),
        gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      3 * (2 * 120 * (16 / 5) * Real.exp (-8)) := by
  set s := K.filter (fun k => k = 3 ∨ k = 4 ∨ k = -5)
  set b := 2 * 120 * (16 / 5) * Real.exp (-8)
  have hf : ∀ k ∈ s, gaborF0BinCount k * gaborF0BinGauss 4 k ≤ b :=
    fun k hk => gaborF0_near_term_le (mem_filter.mp hk).2
  have hsub : s ⊆ ({(3 : ℤ), 4, -5} : Finset ℤ) := by
    intro k hk
    rcases (mem_filter.mp hk).2 with h | h | h <;> simp [h]
  have hcard : (s.card : ℝ) ≤ 3 := by
    have : s.card ≤ 3 := (card_le_card hsub).trans (by decide)
    exact_mod_cast this
  have hsum : ∑ k ∈ s, gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      ∑ k ∈ s, b := sum_le_sum hf
  have hconst : ∑ k ∈ s, b = (s.card : ℝ) * b := by
    simp [sum_const, nsmul_eq_mul]
  exact (hsum.trans_eq hconst).trans
    (mul_le_mul_of_nonneg_right hcard (by positivity))

lemma gaborF0_mid_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k = 5 ∨ k = -6),
        gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      2 * (2 * 120 * 4 * Real.exp (-(25 / 2))) := by
  set s := K.filter (fun k => k = 5 ∨ k = -6)
  set b := 2 * 120 * 4 * Real.exp (-(25 / 2))
  have hf : ∀ k ∈ s, gaborF0BinCount k * gaborF0BinGauss 4 k ≤ b :=
    fun k hk => gaborF0_mid_term_le (mem_filter.mp hk).2
  have hsub : s ⊆ ({(5 : ℤ), -6} : Finset ℤ) := by
    intro k hk
    rcases (mem_filter.mp hk).2 with h | h <;> simp [h]
  have hcard : (s.card : ℝ) ≤ 2 := by
    have : s.card ≤ 2 := (card_le_card hsub).trans (by decide)
    exact_mod_cast this
  have hsum : ∑ k ∈ s, gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      ∑ k ∈ s, b := sum_le_sum hf
  have hconst : ∑ k ∈ s, b = (s.card : ℝ) * b := by
    simp [sum_const, nsmul_eq_mul]
  exact (hsum.trans_eq hconst).trans
    (mul_le_mul_of_nonneg_right hcard (by positivity))

lemma gaborF0_farP_pow_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => 6 ≤ k),
        ((1 / 2 : ℝ) ^ ((k - 6).toNat)) ≤ 2 := by
  set FP := K.filter (fun k => 6 ≤ k)
  let f : ℤ → ℕ := fun k => (k - 6).toNat
  have hinj : Set.InjOn f FP := by
    intro a ha b hb heq
    have ha6 : 6 ≤ a := (mem_filter.mp ha).2
    have hb6 : 6 ≤ b := (mem_filter.mp hb).2
    have hab : (a - 6 : ℤ) = b - 6 := by
      rw [← Int.toNat_of_nonneg (sub_nonneg.mpr ha6),
          ← Int.toNat_of_nonneg (sub_nonneg.mpr hb6)]
      exact_mod_cast heq
    linarith
  have himg :=
    sum_image (g := f) (f := fun n : ℕ => (1 / 2 : ℝ) ^ n) hinj
  have hsub : FP.image f ⊆ range (Finset.sup (FP.image f) id + 1) := by
    intro n hn
    exact mem_range.mpr (Nat.lt_succ_of_le (Finset.le_sup (f := id) hn))
  have hle :=
    sum_le_sum_of_subset_of_nonneg (f := fun n : ℕ => (1 / 2 : ℝ) ^ n)
      hsub fun _ _ _ => by positivity
  exact himg.symm.trans_le (hle.trans (half_geom_sum_le _))

lemma gaborF0_farP_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => 6 ≤ k),
        gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      960 * Real.exp (-12) := by
  set FP := K.filter (fun k => 6 ≤ k)
  have hterm : ∀ k ∈ FP,
      gaborF0BinCount k * gaborF0BinGauss 4 k ≤
        480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((k - 6).toNat)) :=
    fun k hk => gaborF0_farP_term_le (mem_filter.mp hk).2
  have hsum := sum_le_sum hterm
  have hfac :
      ∑ k ∈ FP, 480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((k - 6).toNat)) =
        480 * Real.exp (-12) *
          ∑ k ∈ FP, ((1 / 2 : ℝ) ^ ((k - 6).toNat)) := by
    exact (mul_sum (s := FP)
      (f := fun k : ℤ => ((1 / 2 : ℝ) ^ ((k - 6).toNat)))
      (a := (480 : ℝ) * Real.exp (-12))).symm
  have hpow := gaborF0_farP_pow_sum_le K
  have hnn : (0 : ℝ) ≤ 480 * Real.exp (-12) := by positivity
  have hmul :
      480 * Real.exp (-12) *
          ∑ k ∈ FP, ((1 / 2 : ℝ) ^ ((k - 6).toNat)) ≤
        480 * Real.exp (-12) * 2 :=
    mul_le_mul_of_nonneg_left (by simpa [FP] using hpow) hnn
  have h960 : 480 * Real.exp (-12) * 2 = 960 * Real.exp (-12) := by ring
  exact (hsum.trans_eq hfac).trans (hmul.trans_eq h960)

lemma gaborF0_farN_pow_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k ≤ -7),
        ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) ≤ 2 := by
  set FN := K.filter (fun k => k ≤ -7)
  let f : ℤ → ℕ := fun k => (-k - 7).toNat
  have hinj : Set.InjOn f FN := by
    intro a ha b hb heq
    have ha7 : a ≤ -7 := (mem_filter.mp ha).2
    have hb7 : b ≤ -7 := (mem_filter.mp hb).2
    have hab : (-a - 7 : ℤ) = -b - 7 := by
      rw [← Int.toNat_of_nonneg (by omega : (0 : ℤ) ≤ -a - 7),
          ← Int.toNat_of_nonneg (by omega : (0 : ℤ) ≤ -b - 7)]
      exact_mod_cast heq
    linarith
  have himg :=
    sum_image (g := f) (f := fun n : ℕ => (1 / 2 : ℝ) ^ n) hinj
  have hsub : FN.image f ⊆ range (Finset.sup (FN.image f) id + 1) := by
    intro n hn
    exact mem_range.mpr (Nat.lt_succ_of_le (Finset.le_sup (f := id) hn))
  have hle :=
    sum_le_sum_of_subset_of_nonneg (f := fun n : ℕ => (1 / 2 : ℝ) ^ n)
      hsub fun _ _ _ => by positivity
  exact himg.symm.trans_le (hle.trans (half_geom_sum_le _))

lemma gaborF0_farN_sum_le (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k ≤ -7),
        gaborF0BinCount k * gaborF0BinGauss 4 k ≤
      960 * Real.exp (-12) := by
  set FN := K.filter (fun k => k ≤ -7)
  have hterm : ∀ k ∈ FN,
      gaborF0BinCount k * gaborF0BinGauss 4 k ≤
        480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) :=
    fun k hk => gaborF0_farN_term_le (mem_filter.mp hk).2
  have hsum := sum_le_sum hterm
  have hfac :
      ∑ k ∈ FN, 480 * Real.exp (-12) * ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) =
        480 * Real.exp (-12) *
          ∑ k ∈ FN, ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) := by
    exact (mul_sum (s := FN)
      (f := fun k : ℤ => ((1 / 2 : ℝ) ^ ((-k - 7).toNat)))
      (a := (480 : ℝ) * Real.exp (-12))).symm
  have hpow := gaborF0_farN_pow_sum_le K
  have hnn : (0 : ℝ) ≤ 480 * Real.exp (-12) := by positivity
  have hmul :
      480 * Real.exp (-12) *
          ∑ k ∈ FN, ((1 / 2 : ℝ) ^ ((-k - 7).toNat)) ≤
        480 * Real.exp (-12) * 2 :=
    mul_le_mul_of_nonneg_left (by simpa [FN] using hpow) hnn
  have h960 : 480 * Real.exp (-12) * 2 = 960 * Real.exp (-12) := by ring
  exact (hsum.trans_eq hfac).trans (hmul.trans_eq h960)

lemma gaborF0_bin_majorant_finset_le (K : Finset ℤ) :
    ∑ k ∈ K, gaborF0BinCount k * gaborF0BinGauss 4 k ≤ (19 / 20 : ℝ) := by
  set f := fun k : ℤ => gaborF0BinCount k * gaborF0BinGauss 4 k
  have hpt : ∀ k ∈ K,
      f k ≤
        (if 6 ≤ k then f k else 0) +
          (if k ≤ -7 then f k else 0) +
            (if k = 3 ∨ k = 4 ∨ k = -5 then f k else 0) +
              (if k = 5 ∨ k = -6 then f k else 0) := by
    intro k _hk
    by_cases h6 : 6 ≤ k
    · have h7 : ¬ k ≤ -7 := by omega
      have h3 : ¬ (k = 3 ∨ k = 4 ∨ k = -5) := by omega
      have h5 : ¬ (k = 5 ∨ k = -6) := by omega
      simp [h6, h7, h3, h5]
    · by_cases h7 : k ≤ -7
      · have h3 : ¬ (k = 3 ∨ k = 4 ∨ k = -5) := by omega
        have h5 : ¬ (k = 5 ∨ k = -6) := by omega
        simp [h6, h7, h3, h5]
      · by_cases h3 : k = 3 ∨ k = 4 ∨ k = -5
        · have h5 : ¬ (k = 5 ∨ k = -6) := by omega
          simp [h6, h7, h3, h5]
        · by_cases h5 : k = 5 ∨ k = -6
          · simp [h6, h7, h3, h5]
          · have hz : f k = 0 :=
              gaborF0_term_eq_zero_of_inactive h3 h5 h6 h7
            simp [h6, h7, h3, h5, hz]
  have hle := sum_le_sum hpt
  simp_rw [sum_add_distrib] at hle
  have h6s :
      ∑ k ∈ K, (if 6 ≤ k then f k else 0) =
        ∑ k ∈ K.filter (fun k => 6 ≤ k), f k :=
    (sum_filter (p := fun k => 6 ≤ k) (s := K) f).symm
  have h7s :
      ∑ k ∈ K, (if k ≤ -7 then f k else 0) =
        ∑ k ∈ K.filter (fun k => k ≤ -7), f k :=
    (sum_filter (p := fun k => k ≤ -7) (s := K) f).symm
  have h3s :
      ∑ k ∈ K, (if k = 3 ∨ k = 4 ∨ k = -5 then f k else 0) =
        ∑ k ∈ K.filter (fun k => k = 3 ∨ k = 4 ∨ k = -5), f k :=
    (sum_filter (p := fun k => k = 3 ∨ k = 4 ∨ k = -5) (s := K) f).symm
  have h5s :
      ∑ k ∈ K, (if k = 5 ∨ k = -6 then f k else 0) =
        ∑ k ∈ K.filter (fun k => k = 5 ∨ k = -6), f k :=
    (sum_filter (p := fun k => k = 5 ∨ k = -6) (s := K) f).symm
  rw [h6s, h7s, h3s, h5s] at hle
  have htot :
      960 * Real.exp (-12) + 960 * Real.exp (-12) +
          3 * (2 * 120 * (16 / 5) * Real.exp (-8)) +
            2 * (2 * 120 * 4 * Real.exp (-(25 / 2))) <
        (19 / 20 : ℝ) := by
    nlinarith [gaborF0_near_budget, gaborF0_mid_budget, gaborF0_far_budget]
  linarith [hle, gaborF0_farP_sum_le K, gaborF0_farN_sum_le K,
    gaborF0_near_sum_le K, gaborF0_mid_sum_le K, htot]

lemma gaborF0_sum_fiber_weight
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (μ : {z : ℂ // IsCriticalStripZetaZero z} → ℝ)
    (M : ℤ → ℝ) :
    S.sum (fun ρ => μ ρ * M (ordinateBin ρ.val.im)) =
      ∑ k ∈ S.image (fun ρ => ordinateBin ρ.val.im),
        (S.filter (fun ρ => ordinateBin ρ.val.im = k)).sum μ * M k := by
  classical
  let g : {z : ℂ // IsCriticalStripZetaZero z} → ℤ :=
    fun ρ => ordinateBin ρ.val.im
  let bins := S.image g
  have hmaps : ∀ x ∈ S, g x ∈ bins := fun x hx => mem_image_of_mem g hx
  have hinner : ∀ k ∈ bins,
      (S.filter (fun x => g x = k)).sum (fun x => μ x * M (g x)) =
        (S.filter (fun x => g x = k)).sum μ * M k := by
    intro k _hk
    have : ∀ x ∈ S.filter (fun x => g x = k),
        μ x * M (g x) = μ x * M k := by
      intro x hx
      rw [(mem_filter.mp hx).2]
    rw [sum_congr rfl this, ← sum_mul]
  have hS :=
    disjiUnion_filter_eq_of_maps_to (s := S) (t := bins) (f := g) hmaps
  conv_lhs => rw [← hS]
  rw [sum_disjiUnion]
  exact sum_congr rfl hinner

/-- Tail-bound lemma: under `|Im ρ| ≥ 4`, the multiplicity-weighted
Gaussian mass on any finite zero set is `< 1` (in fact `≤ 19/20`). -/
lemma gaborF0_zero_mass_finset_le
    (hT : GaborLowHeightZeroFree gaborF0LowHeight)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) :
    S.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ) *
      Real.exp (-ρ.val.im ^ 2 / 2)) ≤ (19 / 20 : ℝ) := by
  have h4 : ∀ ρ ∈ S, (4 : ℝ) ≤ |ρ.val.im| :=
    fun ρ _hρ => hT ρ.val ρ.property
  have h2 : ∀ ρ ∈ S, (2 : ℝ) ≤ |ρ.val.im| :=
    fun ρ hρ => le_trans (by norm_num) (h4 ρ hρ)
  have hpt : ∀ ρ ∈ S,
      (riemannZetaMultiplicity ρ.val : ℝ) *
          Real.exp (-ρ.val.im ^ 2 / 2) ≤
        (riemannZetaMultiplicity ρ.val : ℝ) *
          gaborF0BinGauss 4 (ordinateBin ρ.val.im) := by
    intro ρ hρ
    refine mul_le_mul_of_nonneg_left ?_ (Nat.cast_nonneg _)
    exact exp_neg_im_sq_le_binGauss (mem_ordinateBin ρ.val.im) (h4 ρ hρ)
  have hsum := sum_le_sum hpt
  have hfib :=
    gaborF0_sum_fiber_weight S
      (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ))
      (gaborF0BinGauss 4)
  have hfib_le :
      ∑ k ∈ S.image (fun ρ => ordinateBin ρ.val.im),
          (S.filter (fun ρ => ordinateBin ρ.val.im = k)).sum
            (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) *
            gaborF0BinGauss 4 k ≤
        ∑ k ∈ S.image (fun ρ => ordinateBin ρ.val.im),
          gaborF0BinCount k * gaborF0BinGauss 4 k := by
    refine sum_le_sum fun k _hk => ?_
    exact mul_le_mul_of_nonneg_right
      (gaborF0_sum_mult_bin_le S k h2)
      (gaborF0BinGauss_nonneg 4 k)
  exact (hsum.trans_eq hfib).trans
    (hfib_le.trans (gaborF0_bin_majorant_finset_le _))

lemma gaborF0_zero_mass_tsum_le
    (hT : GaborLowHeightZeroFree gaborF0LowHeight) :
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity ρ.val : ℝ) *
        Real.exp (-ρ.val.im ^ 2 / 2)) ≤ (19 / 20 : ℝ) :=
  Real.tsum_le_of_sum_le
    (fun _ => mul_nonneg (Nat.cast_nonneg _) (le_of_lt (Real.exp_pos _)))
    (fun S => gaborF0_zero_mass_finset_le hT S)

/-- r542 hard core (b): phase tuning sends the leading cosine phase to `π`. -/
theorem gabor_phase_tuning
    (a sigma gamma : ℝ) (ha : a ≠ 0) (hsigma : sigma ≠ 0) :
    Real.cos
        (sigma * (gamma - (gamma - Real.pi * a / sigma)) / a) = -1 := by
  have hphase :
      sigma * (gamma - (gamma - Real.pi * a / sigma)) / a = Real.pi := by
    field_simp
    ring
  rw [hphase, Real.cos_pi]

/-- r542 hard core (c): `a = σ²/64` gives the exact enhancement `exp 32`. -/
theorem gabor_enhancement_scaling (sigma : ℝ) (hsigma : sigma ≠ 0) :
    Real.exp (sigma ^ 2 / (2 * (sigma ^ 2 / 64))) = Real.exp 32 := by
  congr 1
  field_simp [pow_ne_zero 2 hsigma]
  ring

/-- Pure autocorrelation closed form from r541:
`sqrt(π/(2a))/2 exp(-au²/2)(cos(ωu)+exp(-ω²/(2a)))`. -/
noncomputable def pureGaborAutocorrelation (a omega u : ℝ) : ℝ :=
  Real.sqrt (Real.pi / (2 * a)) / 2 *
    Real.exp (-a * u ^ 2 / 2) *
    (Real.cos (omega * u) + Real.exp (-omega ^ 2 / (2 * a)))

/-- Optional r542 integral seam.  Mathlib v4.29.1 exposes Fourier Gaussian
lemmas in normalization-specific form, but no directly matching bilateral
complex Laplace lemma for this shifted autocorrelation.  Backlog r543:
derive that lemma by completing the square, then discharge this statement. -/
theorem pureGaborHat_integral_representation
    (a omega : ℝ) (ha : 0 < a) (s : ℂ) :
    (∫ u : ℝ, (pureGaborAutocorrelation a omega u : ℂ) *
        Complex.exp ((s - (1 / 2 : ℂ)) * u)) =
      pureGaborHatDelta a omega (s - (1 / 2 : ℂ)) := by
  simpa [pureGaborAutocorrelation, pureGaborHatDelta] using
    pureGabor_integral_closed_form a omega ha (s - (1 / 2 : ℂ))

noncomputable def trudgianTheta (T : ℝ) : ℝ :=
  T / (2 * Real.pi) * Real.log (T / (2 * Real.pi * Real.exp 1)) + 7 / 8

noncomputable def trudgianError (T : ℝ) : ℝ :=
  0.111 * Real.log T + 0.275 * Real.log (Real.log T) + 2.450 + 0.2 / T

/-- PATH B (inactive, r547).  Explicit Trudgian zero-count error bound,
in the exact constants used by r541.  Not a premise of the live Gabor
reduction: Path A increment `GaborIncrementBound` is proved and is the
weaker counting input actually consumed.  Kept because
`TrudgianGaussianMeasureTransfer` documents the same classical bound.
Reference: T. Trudgian, J. Number Theory 134 (2014), 280--292,
Theorem 1 and Corollary 1.  No asserting `sorry`. -/
def TrudgianZeroDensityBound : Prop :=
  ∀ T : ℝ, Real.exp 1 ≤ T →
    |(gaborZeroCount T : ℝ) - trudgianTheta T| ≤ trudgianError T

/-- Closed spectral side for the Gabor class:
`Re(Σ_ρ m_ρ ĥ_W(ρ) − ĥ_W(1))`.

r600: this is **not** the Weil functional.  The pole subtraction
makes the quantity negative on `pureGaborTest 1 0` as soon as the
zero-side tail is smaller than `Re ĥ(1) = π e^{1/8}`.  The live
object is `gaborZeroSide`. -/
noncomputable def gaborSpectralFormula (F : GaborWeilTest) : ℝ :=
  ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) -
    gaborHat F 1).re

/-- Zero side of the classical Guinand–Weil identity:
`Z = Re Σ_ρ ĥ_W(ρ)` (nontrivial zeros, both signs). -/
noncomputable def gaborZeroSide (F : GaborWeilTest) : ℝ :=
  (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ).re

/-- Algebraic split: the subtracted pole is exactly `Re ĥ_W(1)`. -/
theorem gaborSpectralFormula_eq (F : GaborWeilTest) :
    gaborSpectralFormula F = gaborZeroSide F - (gaborHat F 1).re := by
  unfold gaborSpectralFormula gaborZeroSide
  rw [Complex.sub_re]

/-- If the zero-side is strictly smaller than the pole term, the
pole-subtracted formula is negative.  Refutation of spectral
nonnegativity modulo a tail bound; numerically `3·10⁻⁴³` vs
`3.5599` on `pureGaborTest 1 0`. -/
theorem gaborSpectralFormula_neg_of_small_zero_side
    {F : GaborWeilTest}
    (h : gaborZeroSide F < (gaborHat F 1).re) :
    gaborSpectralFormula F < 0 := by
  rw [gaborSpectralFormula_eq]
  linarith

/-- r600: `hpos` on `gaborSpectralFormula` is false as soon as the
zero-side of `pureGaborTest 1 0` is smaller than `π e^{1/8}`.
Kept as the bound-form; r610 discharges the bound from
`GaborLowHeightZeroFree 4`.  No `sorry`. -/
theorem gaborSpectralFormula_refuted_of_bound
    (h : gaborZeroSide (pureGaborTest 1 0 (by norm_num)) <
      (gaborHat (pureGaborTest 1 0 (by norm_num)) 1).re) :
    ¬ (∀ F : GaborWeilTest, F.admissible →
        0 ≤ gaborSpectralFormula F) := by
  intro hpos
  have hnn := hpos (pureGaborTest 1 0 (by norm_num)) trivial
  exact (not_le_of_gt (gaborSpectralFormula_neg_of_small_zero_side h)) hnn

lemma gaborF0_weighted_hat_norm_finset_le
    (ha : 0 < (1 : ℝ))
    (hT : GaborLowHeightZeroFree gaborF0LowHeight)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) :
    S.sum (fun ρ => ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
        gaborHat (pureGaborTest 1 0 ha) ρ‖) ≤
      Real.pi * Real.exp (1 / 8) * (19 / 20) := by
  have hle :
      S.sum (fun ρ => ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
          gaborHat (pureGaborTest 1 0 ha) ρ‖) ≤
        S.sum (fun ρ => Real.pi * Real.exp (1 / 8) *
          ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            Real.exp (-(ρ : ℂ).im ^ 2 / 2))) := by
    refine sum_le_sum fun ρ _hρ => ?_
    have hmul :
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat (pureGaborTest 1 0 ha) ρ‖ =
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            ‖gaborHat (pureGaborTest 1 0 ha) ρ‖ := by
      rw [norm_mul, Complex.norm_natCast]
    rw [hmul]
    have hst := norm_gaborHat_pure_one_zero_strip ha ρ.property
    have hm : (0 : ℝ) ≤ (riemannZetaMultiplicity (ρ : ℂ) : ℝ) :=
      Nat.cast_nonneg _
    calc
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            ‖gaborHat (pureGaborTest 1 0 ha) ρ‖ ≤
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            (Real.pi * Real.exp (1 / 8) *
              Real.exp (-(ρ : ℂ).im ^ 2 / 2)) :=
        mul_le_mul_of_nonneg_left hst hm
      _ = Real.pi * Real.exp (1 / 8) *
            ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              Real.exp (-(ρ : ℂ).im ^ 2 / 2)) := by
        ring
  have hfac :
      S.sum (fun ρ => Real.pi * Real.exp (1 / 8) *
          ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            Real.exp (-(ρ : ℂ).im ^ 2 / 2))) =
        Real.pi * Real.exp (1 / 8) *
          S.sum (fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            Real.exp (-(ρ : ℂ).im ^ 2 / 2)) :=
    (mul_sum (s := S)
      (f := fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          Real.exp (-(ρ : ℂ).im ^ 2 / 2))
      (a := Real.pi * Real.exp (1 / 8))).symm
  have hmass := gaborF0_zero_mass_finset_le hT S
  have hnn : (0 : ℝ) ≤ Real.pi * Real.exp (1 / 8) := by positivity
  have hmass' :
      S.sum (fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          Real.exp (-(ρ : ℂ).im ^ 2 / 2)) ≤ (19 / 20 : ℝ) := by
    simpa using hmass
  exact hle.trans (hfac.trans_le (mul_le_mul_of_nonneg_left hmass' hnn))

lemma gaborZeroSide_pure_one_zero_le_mass
    (ha : 0 < (1 : ℝ))
    (hT : GaborLowHeightZeroFree gaborF0LowHeight) :
    gaborZeroSide (pureGaborTest 1 0 ha) ≤
      Real.pi * Real.exp (1 / 8) * (19 / 20) := by
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
      gaborHat (pureGaborTest 1 0 ha) ρ
  unfold gaborZeroSide
  by_cases hsm : Summable f
  · have hn : Summable (fun ρ => ‖f ρ‖) := by
      rw [summable_norm_iff]; exact hsm
    have hre : (∑' ρ, f ρ).re ≤ ‖∑' ρ, f ρ‖ :=
      (le_abs_self _).trans (abs_re_le_norm _)
    have hts := norm_tsum_le_tsum_norm hn
    have hbound :=
      Real.tsum_le_of_sum_le (fun ρ => norm_nonneg (f ρ))
        (fun S => gaborF0_weighted_hat_norm_finset_le ha hT S)
    exact hre.trans (hts.trans hbound)
  · have hz : (∑' ρ, f ρ) = 0 := tsum_eq_zero_of_not_summable hsm
    simp [f, hz]
    positivity

/-- r610 rung (b): `Z(F₀) < Re ĥ(F₀,1)` from the named low-height
hypothesis `GaborLowHeightZeroFree 4`.  Classically true (first zero
at 14.1347), not in Mathlib. -/
theorem gaborZeroSide_pure_one_zero_lt_hat_of_lowHeight
    (hT : GaborLowHeightZeroFree gaborF0LowHeight) :
    gaborZeroSide (pureGaborTest 1 0 (by norm_num)) <
      (gaborHat (pureGaborTest 1 0 (by norm_num)) 1).re := by
  have ha : 0 < (1 : ℝ) := by norm_num
  rw [gaborHat_pure_one_zero ha]
  have hle := gaborZeroSide_pure_one_zero_le_mass ha hT
  have hlt : Real.pi * Real.exp (1 / 8) * (19 / 20) <
      Real.pi * Real.exp (1 / 8) := by
    have hpos : (0 : ℝ) < Real.pi * Real.exp (1 / 8) :=
      mul_pos Real.pi_pos (Real.exp_pos _)
    nlinarith
  exact lt_of_le_of_lt hle hlt

/-- r610: spectral nonnegativity of `gaborSpectralFormula` is false
once every strip zero satisfies `|Im| ≥ 4`.  Classically true
(first zero at 14.1347), not in Mathlib.  Unasserted Prop, no `sorry`. -/
theorem gaborSpectralFormula_refuted_of_lowHeight
    (hT : GaborLowHeightZeroFree gaborF0LowHeight) :
    ¬ (∀ F : GaborWeilTest, F.admissible →
        0 ≤ gaborSpectralFormula F) :=
  gaborSpectralFormula_refuted_of_bound
    (gaborZeroSide_pure_one_zero_lt_hat_of_lowHeight hT)

/-- Autocorrelation represented directly by its defining integral.
This is the even test function `g` whose Weil-shifted transform is
`gaborHat`. -/
noncomputable def gaborAutocorrelation (F : GaborWeilTest) (u : ℝ) : ℝ :=
  ∫ t : ℝ, F.carrier t * F.carrier (t - u)

/-- Classical Weil prime comb `2 Λ(n) n^{-1/2} g(log n)`, in the
corpus gauge `combMass`.  The r542 contour weight `Λ(n)(1+n⁻¹)`
was removed: r548 refutes it as an identity for `ĥ_W`. -/
noncomputable def gaborPrimeComb (F : GaborWeilTest) : ℝ :=
  ∑' n : ℕ, combMass n * gaborAutocorrelation F (Real.log n)

/-- Classical pole channel `ĥ_W(0) + ĥ_W(1)`. -/
noncomputable def gaborPoleSide (F : GaborWeilTest) : ℝ :=
  (gaborHat F 0 + gaborHat F 1).re

/-- Weil archimedean channel on the critical line:
`(1/2π) ∫ ĥ_W(1/2+it) (Re ψ(1/4+it/2) − log π) dt`. -/
noncomputable def gaborArchSide (F : GaborWeilTest) : ℝ :=
  (1 / (2 * Real.pi)) *
    ∫ t : ℝ, (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re *
      ((Complex.digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * Complex.I)).re -
        Real.log Real.pi)

/-- Two-edge contour of `(ζ'/ζ) ĥ_W` along `Re = 2` and
`Re = -1/16`, divided by `2π`.  Intermediate in the residue-theorem
step of `GaborExplicitFormula`; not the arithmetic landing site. -/
noncomputable def gaborContourFormula (F : GaborWeilTest) : ℝ :=
  ((∫ t : ℝ,
      logDeriv riemannZeta ((2 : ℂ) + t * Complex.I) *
          gaborHat F ((2 : ℂ) + t * Complex.I) -
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + t * Complex.I) *
          gaborHat F (((-1 / 16 : ℝ) : ℂ) + t * Complex.I)) /
    (2 * Real.pi)).re

/-- Three-channel arithmetic form equivalent to `Z − ĥ_W(1)`:
`Arch − Prime_comb + ĥ_W(0)`. -/
noncomputable def gaborArithmeticFormula (F : GaborWeilTest) : ℝ :=
  gaborArchSide F - gaborPrimeComb F + (gaborHat F 0).re

/-- r550: classical Guinand–Weil identity for the Weil-shifted
Gabor transform `gaborHat` (= `ĥ_W`):

    Z = Pole − Prime_comb + Arch

with `Z = Re Σ_ρ ĥ_W(ρ)`, `Pole = Re(ĥ_W(0)+ĥ_W(1))`,
`Prime_comb = Σ_n (2Λ(n)/√n) g(log n)`, and `Arch` the critical-line
Digamma pairing.  Numerically confirmed by the sealed probe r548
(`weil_gabor_explicit_formula_probe`, VERDICT EF_CONFIRMED, 36/36)
on the comb normalization `2Λ/√n`.  The r542 weight `Λ(n)(1+1/n)`
fails on every sharp test cell as an identity for `ĥ_W`.

Proof decomposition (no new density theorem, no RH circle):
  (1) Entirety + Gaussian decay of `gaborHat` (algebraic, GaborIntegral);
  (2) Horizontal edges → 0 via `|ζ'/ζ| ≪ log²|t|` against Gaussian decay;
  (3) Residue theorem in the strip `-1/16 < Re s < 2`
      (nontrivial zeros + pole at 1, `res ζ'/ζ = -1` ⇒ `-ĥ_W(1)`;
      trivial zeros lie outside);
  (4) Convergence of the zero sum via the proved `GaborIncrementBound`
      (ZeroIncrement.lean);
  (5) Right edge → comb `2Λ/√n` by Schwartz Fourier inversion;
      left edge → Digamma via `logDeriv_zetaFEFactor_left_edge`
      plus the reflected prime sum. -/
def GaborExplicitFormula : Prop :=
  ∀ F : GaborWeilTest, F.admissible →
    gaborZeroSide F =
      gaborPoleSide F - gaborPrimeComb F + gaborArchSide F

/- CLASSICAL INPUT r542, backlog after r558: contour/convergence
proof along the five-step decomposition above.  The asserting
`sorry` was retired.  The r557 bricks plus the remaining vertical
identification live in `RH/GaborExplicitFormula.lean`
(`gabor_explicitFormula_of_remainders`).  The arithmetic landing
site is the classical comb, not the compact honest `(1+1/n)`
pairing. -/

/-- Algebraic rearrangement of identity A:
`Z − ĥ_W(1) = ĥ_W(0) − Prime_comb + Arch`.  Sorry-free. -/
theorem gabor_explicitFormula_to_spectral
    {F : GaborWeilTest} (hF : F.admissible)
    (hexp : GaborExplicitFormula) :
    gaborArithmeticFormula F = gaborSpectralFormula F := by
  have hid := hexp F hF
  have hZ := gaborSpectralFormula_eq F
  have hP :
      gaborPoleSide F =
        (gaborHat F 0).re + (gaborHat F 1).re := by
    unfold gaborPoleSide
    rw [Complex.add_re]
  unfold gaborArithmeticFormula
  rw [hZ, hid, hP]
  ring

/-- r600 pole-sign lemma, NOT RH-core.  Under EF,
`Arch − Prime + ĥ(0) = Z − Re ĥ(1)`.  If `Z < 0` and
`Re ĥ(1) ≥ 0` then the arithmetic form is negative. -/
theorem gaborArithmeticFormula_neg_of_zeroSide_neg
    {F : GaborWeilTest} (hF : F.admissible)
    (hexp : GaborExplicitFormula)
    (h1 : 0 ≤ (gaborHat F 1).re)
    (hZ : gaborZeroSide F < 0) :
    gaborArithmeticFormula F < 0 := by
  have hsp := gabor_explicitFormula_to_spectral hF hexp
  have heq := gaborSpectralFormula_eq F
  have : gaborArithmeticFormula F =
      gaborZeroSide F - (gaborHat F 1).re := by
    rw [hsp, heq]
  linarith

/-- The scaling-law test selected for an off-critical point. -/
noncomputable def scalingGaborTest (beta gamma : ℝ)
    (hbeta : beta ≠ 1 / 2) : GaborWeilTest :=
  let sigma := beta - 1 / 2
  let a := sigma ^ 2 / 64
  pureGaborTest a (gamma - Real.pi * a / sigma)
    (div_pos (sq_pos_of_ne_zero (sub_ne_zero.mpr hbeta)) (by norm_num))

/-- The live scaling tests are pure (`coeffs = ⟨1,0,0⟩`). -/
theorem scalingGaborTest_coeffs (beta gamma : ℝ)
    (hbeta : beta ≠ 1 / 2) :
    (scalingGaborTest beta gamma hbeta).coeffs = ⟨1, 0, 0⟩ :=
  rfl

/-- Finite certified window, not a statement about the zero set.

Quantifier: `∀ β,γ` in the compact rectangle
`β ∈ [0.51, 0.95]`, `|γ| ∈ [5, 10⁴]`, with explicit margin
`gaborArithmeticFormula ≤ -3.56`.  This is exactly the r541
42/42 table.  A numeric probe can certify every cell; the
statement does not quantify over `IsNontrivialRiemannZetaZero`.
Unasserted (not a `sorry`): Lean does not contain that table. -/
def GaborSeparationPrecheck : Prop :=
  ∀ beta gamma : ℝ, 0.51 ≤ beta → beta ≤ 0.95 →
    5 ≤ |gamma| → |gamma| ≤ 10000 →
    ∀ hcritical : beta ≠ 1 / 2,
    gaborArithmeticFormula (scalingGaborTest beta gamma hcritical) ≤
      -3.56

/-- Full `∀`-over-zeros separation, the load-bearing conjunct of the
former mixed `GaborSeparationInequality`.

OVERSPECIFIED (r605A/r612): prescribed packet per zero
`a = σ²/64`, `ω = γ − πa/σ`.  Believed false by r605N T3 (C4-cluster
sign flip of the prescribed packet).  Superseded by the existential
form in `GaborExposedOrbit.lean`
(`gabor_zeroSide_pure_criterion_iff_rh_unconditional`).  Retained
unasserted for the historical record only.  Not a `sorry`.

Quantifier: `∀ s, IsNontrivialRiemannZetaZero s → Re s ≠ 1/2 →
gaborArithmeticFormula (scalingGaborTest (Re s) (Im s)) < 0`.
Strictly larger than `GaborSeparationPrecheck`: unbounded `|γ|`,
every off-critical `β`, and a strict sign rather than a numeric
margin on a compact window.  Historical input of
`gabor_separation_of_inputs` / `gabor_inputs_to_mathlib_rh`
(now an explicit hypothesis, never asserted). -/
def GaborSeparationForAllZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s →
    ∀ hcritical : s.re ≠ 1 / 2,
    gaborArithmeticFormula
      (scalingGaborTest s.re s.im hcritical) < 0

/-- Historical package: Path A increment (already proved) plus both
quantifier-distinct conjuncts.  Definitionally
`GaborIncrementBound → GaborSeparationForAllZeros ∧ GaborSeparationPrecheck`.
The endpoint no longer takes this package; it takes
`GaborSeparationForAllZeros` directly. -/
def GaborSeparationInequality : Prop :=
  GaborIncrementBound →
    GaborSeparationForAllZeros ∧ GaborSeparationPrecheck

/-- Sorry-free unpacking: the old package still yields the `∀`-zeros
statement once the proved increment is discharged. -/
theorem gaborSeparationForAllZeros_of_inequality
    (hineq : GaborSeparationInequality) :
    GaborSeparationForAllZeros :=
  (hineq gaborIncrementBound_holds).1

/-- Sorry-free unpacking of the finite window. -/
theorem gaborSeparationPrecheck_of_inequality
    (hineq : GaborSeparationInequality) :
    GaborSeparationPrecheck :=
  (hineq gaborIncrementBound_holds).2

/-- Sorry-free reassembly of the historical package. -/
theorem gabor_separationInequality_of_parts
    (hall : GaborSeparationForAllZeros)
    (hpre : GaborSeparationPrecheck) :
    GaborSeparationInequality :=
  fun _ => ⟨hall, hpre⟩

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail.  Gabor-class analogue of
`FullWeilSeparatesOffCriticalZeros` on the pole-subtracted formula. -/
def GaborSeparatesOffCriticalZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s → s.re ≠ 1 / 2 →
    ∃ F : GaborWeilTest, F.admissible ∧ gaborSpectralFormula F < 0

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail.  r558 reduction: explicit formula plus the
`∀`-zeros inequality imply Gabor separation on the pole-subtracted
formula.  Path A increment is already discharged and is not a
hypothesis of `GaborSeparationForAllZeros`.  Pure logic. -/
theorem gabor_separation_of_inputs :
    GaborExplicitFormula →
    GaborSeparationForAllZeros →
    GaborSeparatesOffCriticalZeros := by
  intro hexp hineq s hs hcritical
  let F := scalingGaborTest s.re s.im hcritical
  refine ⟨F, trivial, ?_⟩
  have harith : gaborArithmeticFormula F < 0 :=
    hineq s hs hcritical
  rw [gabor_explicitFormula_to_spectral trivial hexp] at harith
  exact harith

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail. -/
theorem gabor_separation_of_inequality :
    GaborExplicitFormula →
    GaborSeparationInequality →
    GaborSeparatesOffCriticalZeros :=
  fun hexp hineq =>
    gabor_separation_of_inputs hexp
      (gaborSeparationForAllZeros_of_inequality hineq)

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail.  Gabor criterion on the pole-subtracted
formula. -/
def GaborCriterionToMathlibRH : Prop :=
  (∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborSpectralFormula F) →
    RiemannHypothesis

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail. -/
theorem gabor_criterion_to_mathlib_rh
    (hseparate : GaborSeparatesOffCriticalZeros) :
    GaborCriterionToMathlibRH := by
  intro hpos s hz htrivial hpole
  by_contra hcritical
  obtain ⟨F, hF, hneg⟩ :=
    hseparate s ⟨hz, htrivial, hpole⟩ hcritical
  exact (not_lt_of_ge (hpos F hF)) hneg

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail. -/
theorem gabor_inputs_to_mathlib_rh
    (hexp : GaborExplicitFormula)
    (hineq : GaborSeparationForAllZeros)
    (hpos : ∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborSpectralFormula F) :
    RiemannHypothesis :=
  gabor_criterion_to_mathlib_rh
    (gabor_separation_of_inputs hexp hineq) hpos

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted_of_lowHeight`;
kept for audit trail. -/
theorem gabor_inputs_to_mathlib_rh_of_inequality
    (hexp : GaborExplicitFormula)
    (hineq : GaborSeparationInequality)
    (hpos : ∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborSpectralFormula F) :
    RiemannHypothesis :=
  gabor_inputs_to_mathlib_rh hexp
    (gaborSeparationForAllZeros_of_inequality hineq) hpos

/-! ## r600 live zero-side interface -/

/-- `∀`-zeros negativity of the classical zero-side `Z = Re Σ ĥ_W(ρ)`
on the scaling packet.  Parallel of `GaborSeparationForAllZeros`.
Unasserted.  Not a `sorry`.

OVERSPECIFIED (r605): prescribed-packet pointwise form; superseded by
the existential separator in `GaborExposedOrbit.lean`. -/
def GaborZeroSideForAllZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s →
    ∀ hcritical : s.re ≠ 1 / 2,
    gaborZeroSide (scalingGaborTest s.re s.im hcritical) < 0

/-- Existential zero-side separator: every nontrivial off-critical
zero is witnessed by some admissible Gabor test with `Z < 0`. -/
def GaborZeroSideSeparatesOffCriticalZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s → s.re ≠ 1 / 2 →
    ∃ F : GaborWeilTest, F.admissible ∧ gaborZeroSide F < 0

/-- Live Gabor criterion: nonnegativity of the zero-side for every
admissible test implies Mathlib `RiemannHypothesis`. -/
def GaborZeroSideCriterionToMathlibRH : Prop :=
  (∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborZeroSide F) →
    RiemannHypothesis

theorem gabor_zeroSide_separation_of_inputs :
    GaborZeroSideForAllZeros →
    GaborZeroSideSeparatesOffCriticalZeros := by
  intro hineq s hs hcritical
  let F := scalingGaborTest s.re s.im hcritical
  refine ⟨F, trivial, ?_⟩
  exact hineq s hs hcritical

theorem gabor_zeroSide_criterion_to_mathlib_rh
    (hseparate : GaborZeroSideSeparatesOffCriticalZeros) :
    GaborZeroSideCriterionToMathlibRH := by
  intro hpos s hz htrivial hpole
  by_contra hcritical
  obtain ⟨F, hF, hneg⟩ :=
    hseparate s ⟨hz, htrivial, hpole⟩ hcritical
  exact (not_lt_of_ge (hpos F hF)) hneg

/-- Parallel of `gabor_inputs_to_mathlib_rh` on the live object
`gaborZeroSide`.  Explicit formula is not required: the `∀`-zeros
input already names `Z`. -/
theorem gabor_zeroSide_inputs_to_mathlib_rh
    (hineq : GaborZeroSideForAllZeros)
    (hpos : ∀ F : GaborWeilTest, F.admissible → 0 ≤ gaborZeroSide F) :
    RiemannHypothesis :=
  gabor_zeroSide_criterion_to_mathlib_rh
    (gabor_zeroSide_separation_of_inputs hineq) hpos

#print axioms gaborHat_criticalLine_nonneg_pure
#print axioms gaborHat_one_nonneg_pure
#print axioms gaborHat_pure_one
#print axioms gaborHat_pure_one_zero
#print axioms gaborHat_pure_one_zero_gt_three
#print axioms gaborSpectralFormula_eq
#print axioms gaborSpectralFormula_neg_of_small_zero_side
#print axioms gaborSpectralFormula_refuted_of_bound
#print axioms gaborZeroSide_pure_one_zero_lt_hat_of_lowHeight
#print axioms gaborSpectralFormula_refuted_of_lowHeight
#print axioms gaborArithmeticFormula_neg_of_zeroSide_neg
#print axioms gabor_zeroSide_criterion_to_mathlib_rh
#print axioms gabor_zeroSide_inputs_to_mathlib_rh

end RH
