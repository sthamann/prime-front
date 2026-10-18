/-
RH/GaborCountableCriterion.lean -- r612C countable (rational) pure-Gabor
zero-side criterion.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not assert RH or anti-RH
and does not assert `GaborSeparationForAllZeros`.

Continuity of `Z(a,ω) := gaborZeroSide (pureGaborTest a ω _)` on
`{a > 0} × ℝ` is the theorem `gaborZeroSideContinuous_holds`
(`GaborZeroSideContinuous` remains the named Prop, now asserted).
Local uniform majorant of `‖pureGaborHatHolomorphic‖` on a compact box,
then Mathlib `continuousOn_tsum`; density of `ℚ₊ × ℚ` upgrades
rational-packet nonnegativity to the real family; the real-packet iff is
`gabor_zeroSide_pure_criterion_iff_rh_unconditional`.  The rational iff
is now unconditional as
`gabor_zeroSide_rational_criterion_iff_rh_unconditional`.

Rung (a): the dominated-convergence/continuity lemma is proved.
Named-open list shrinks by one (`GaborZeroSideContinuous` is asserted);
census of `sorry` declarations stays 7 (no `Open.lean` edit here).
`←` is on-line positivity (`rh_implies_gaborZeroSide_nonneg`).  `→`
consumes the asserted Prop and the exposed-orbit iff.  No `sorry`.

No new axioms beyond `propext` / `Classical.choice` / `Quot.sound`.
-/
import RH.GaborExposedOrbit
import RH.GaborHatAnalytic
import RH.GaborExplicitFormula
import Mathlib.Analysis.Normed.Group.FunctionSeries
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Data.Real.Archimedean
import Mathlib.Topology.MetricSpace.Basic

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical Topology
open Complex Filter Set

/-! ## Extension of the pure zero-side to `ℝ × ℝ` -/

/-- Zero-side of the pure packet, extended by `0` for non-positive `a`. -/
noncomputable def gaborZeroSidePureExt (p : ℝ × ℝ) : ℝ :=
  if h : 0 < p.1 then gaborZeroSide (pureGaborTest p.1 p.2 h) else 0

lemma gaborZeroSidePureExt_pos {a omega : ℝ} (ha : 0 < a) :
    gaborZeroSidePureExt (a, omega) =
      gaborZeroSide (pureGaborTest a omega ha) :=
  dif_pos ha

/-- Continuity of `Z(a,ω)` on `{a > 0} × ℝ`, as `ContinuousAt` of
`gaborZeroSidePureExt` at every `(a,ω)` with `a > 0`.

Proved as `gaborZeroSideContinuous_holds` by a local uniform majorant
of `‖pureGaborHatHolomorphic a ω (ρ − 1/2)‖` on the compact box
`[a/2, 2a] × [−(|ω|+1), |ω|+1]`:
`‖ĥ‖ ≤ (π/a₀) exp((1/8 + ω₁²/2)/a₀) exp(−(Im ρ)²/(4 a₁))`
(`gaborHatThreeLobeConst` × `gaborThreeLobe_le_gaussian`, worst
constants over the box), then `continuousOn_tsum`.  Summability of the
multiplicity-weighted Gaussian is `summable_gauss_over_zeros` plus
`riemannZetaMultiplicity_le_log_all_local` /
`one_add_log_mul_gauss_le_local`. -/
def GaborZeroSideContinuous : Prop :=
  ∀ (a omega : ℝ), 0 < a →
    ContinuousAt gaborZeroSidePureExt (a, omega)

/-! ## Local continuity of the holomorphic closed form -/

lemma continuousOn_pureGaborHatHolomorphic (δ : ℂ) :
    ContinuousOn (fun p : ℝ × ℝ => pureGaborHatHolomorphic p.1 p.2 δ)
      {p | 0 < p.1} := by
  simp only [pureGaborHatHolomorphic]
  refine ContinuousOn.mul ?_ ?_
  · exact Complex.continuous_ofReal.comp_continuousOn
      (continuousOn_const.div (continuousOn_const.mul continuousOn_fst)
        (fun p hp => mul_ne_zero (by norm_num : (4 : ℝ) ≠ 0) (ne_of_gt hp)))
  · have hden :
        ContinuousOn (fun p : ℝ × ℝ => (2 : ℂ) * (p.1 : ℂ))
          {p | 0 < p.1} :=
      continuousOn_const.mul
        (Complex.continuous_ofReal.comp_continuousOn continuousOn_fst)
    have hden0 : ∀ p : ℝ × ℝ, 0 < p.1 → (2 : ℂ) * (p.1 : ℂ) ≠ 0 :=
      fun p hp => mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr (ne_of_gt hp))
    have hω : ContinuousOn (fun p : ℝ × ℝ => (p.2 : ℂ)) {p | 0 < p.1} :=
      Complex.continuous_ofReal.comp_continuousOn continuousOn_snd
    refine ContinuousOn.add (ContinuousOn.add ?_ ?_) ?_
    · refine Complex.continuous_exp.comp_continuousOn ?_
      refine ContinuousOn.div (ContinuousOn.pow ?_ 2) hden hden0
      exact continuousOn_const.add (continuousOn_const.mul hω)
    · refine Complex.continuous_exp.comp_continuousOn ?_
      refine ContinuousOn.div (ContinuousOn.pow ?_ 2) hden hden0
      exact continuousOn_const.sub (continuousOn_const.mul hω)
    · refine ContinuousOn.mul (ContinuousOn.mul continuousOn_const ?_) ?_
      · refine Complex.continuous_exp.comp_continuousOn ?_
        refine ContinuousOn.div ?_ hden hden0
        exact (ContinuousOn.pow hω 2).neg
      · refine Complex.continuous_exp.comp_continuousOn ?_
        exact continuousOn_const.div hden hden0

noncomputable def gaborZeroSideHolomorphicTerm
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) (p : ℝ × ℝ) : ℂ :=
  (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
    pureGaborHatHolomorphic p.1 p.2 ((ρ : ℂ) - (1 / 2 : ℂ))

lemma continuousOn_gaborZeroSideHolomorphicTerm
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ContinuousOn (gaborZeroSideHolomorphicTerm ρ) {p | 0 < p.1} :=
  continuousOn_const.mul (continuousOn_pureGaborHatHolomorphic _)

lemma gaborZeroSidePureExt_eq_tsum_holomorphic {p : ℝ × ℝ} (hp : 0 < p.1) :
    gaborZeroSidePureExt p =
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        gaborZeroSideHolomorphicTerm ρ p).re := by
  cases p with
  | mk a omega =>
    rw [gaborZeroSidePureExt_pos hp]
    unfold gaborZeroSide gaborZeroSideHolomorphicTerm
    refine congrArg Complex.re (tsum_congr fun ρ => ?_)
    have hF : (pureGaborTest a omega hp).coeffs = ⟨1, 0, 0⟩ := rfl
    simpa [pureGaborTest] using
      congrArg (fun z => (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * z)
        (gaborHat_eq_pureHolomorphic (F := pureGaborTest a omega hp) hF (ρ : ℂ))

/-! ## Uniform Gaussian majorant on a compact box -/

lemma gaborHatThreeLobeConst_le_box
    {a0 a : ℝ} (ha0 : 0 < a0) (ha : a0 ≤ a) {σ : ℝ} (hσ : |σ| ≤ 1 / 2) :
    gaborHatThreeLobeConst a (σ + 1 / 2) ≤
      Real.pi / (4 * a0) * Real.exp ((1 / 4 : ℝ) / (2 * a0)) := by
  have ha_pos : 0 < a := lt_of_lt_of_le ha0 ha
  rw [gaborHatThreeLobeConst_add_half]
  have hpre : Real.pi / (4 * a) ≤ Real.pi / (4 * a0) :=
    div_le_div_of_nonneg_left Real.pi_pos.le (by positivity)
      (mul_le_mul_of_nonneg_left ha (by norm_num))
  have hsq : σ ^ 2 ≤ (1 / 4 : ℝ) := by
    have hhalf : |σ| ≤ |(1 / 2 : ℝ)| := by
      simpa [abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)] using hσ
    have hpow : σ ^ 2 ≤ (1 / 2 : ℝ) ^ 2 := sq_le_sq.mpr hhalf
    have : (1 / 2 : ℝ) ^ 2 = (1 / 4 : ℝ) := by norm_num
    rwa [this] at hpow
  have hexp :
      Real.exp (σ ^ 2 / (2 * a)) ≤ Real.exp ((1 / 4 : ℝ) / (2 * a0)) := by
    refine Real.exp_le_exp.mpr ?_
    have h1 : σ ^ 2 / (2 * a) ≤ (1 / 4 : ℝ) / (2 * a) :=
      div_le_div_of_nonneg_right hsq (by positivity)
    have h2 : (1 / 4 : ℝ) / (2 * a) ≤ (1 / 4 : ℝ) / (2 * a0) :=
      div_le_div_of_nonneg_left (by norm_num) (by positivity)
        (mul_le_mul_of_nonneg_left ha (by norm_num))
    exact h1.trans h2
  exact mul_le_mul hpre hexp (Real.exp_pos _).le (by positivity)

lemma gaborThreeLobe_le_box
    {a0 a1 ω1 a omega t : ℝ} (ha0 : 0 < a0) (ha : a0 ≤ a) (ha1 : a ≤ a1)
    (hω : |omega| ≤ ω1) :
    gaborThreeLobe a omega t ≤
      4 * Real.exp (ω1 ^ 2 / (2 * a0)) *
        Real.exp (-t ^ 2 / (4 * a1)) := by
  have ha_pos : 0 < a := lt_of_lt_of_le ha0 ha
  have ha1_pos : 0 < a1 := lt_of_lt_of_le ha0 (ha.trans ha1)
  have hω0 : 0 ≤ ω1 := le_trans (abs_nonneg omega) hω
  have hbase := gaborThreeLobe_le_gaussian a omega t ha_pos
  refine hbase.trans ?_
  have hωexp :
      Real.exp (omega ^ 2 / (2 * a)) ≤ Real.exp (ω1 ^ 2 / (2 * a0)) := by
    refine Real.exp_le_exp.mpr ?_
    have hωsq : omega ^ 2 ≤ ω1 ^ 2 :=
      sq_le_sq.mpr (by rwa [abs_of_nonneg hω0])
    have h1 : omega ^ 2 / (2 * a) ≤ ω1 ^ 2 / (2 * a) :=
      div_le_div_of_nonneg_right hωsq (by positivity)
    have h2 : ω1 ^ 2 / (2 * a) ≤ ω1 ^ 2 / (2 * a0) :=
      div_le_div_of_nonneg_left (sq_nonneg _) (by positivity)
        (mul_le_mul_of_nonneg_left ha (by norm_num))
    exact h1.trans h2
  have hg :
      Real.exp (-t ^ 2 / (4 * a)) ≤ Real.exp (-t ^ 2 / (4 * a1)) := by
    refine Real.exp_le_exp.mpr ?_
    have : t ^ 2 / (4 * a1) ≤ t ^ 2 / (4 * a) :=
      div_le_div_of_nonneg_left (sq_nonneg _) (by positivity)
        (mul_le_mul_of_nonneg_left ha1 (by norm_num))
    rw [neg_div, neg_div]
    exact neg_le_neg this
  have hmul1 :
      4 * Real.exp (omega ^ 2 / (2 * a)) ≤
        4 * Real.exp (ω1 ^ 2 / (2 * a0)) :=
    mul_le_mul_of_nonneg_left hωexp (by norm_num)
  exact mul_le_mul hmul1 hg (Real.exp_pos _).le (by positivity)

lemma exp_one_div_eight_eq {a0 : ℝ} (ha0 : 0 < a0) :
    Real.exp ((1 / 4 : ℝ) / (2 * a0)) = Real.exp ((1 / 8 : ℝ) / a0) := by
  congr 1
  field_simp [ha0.ne']
  ring

lemma box_prefactor_mul {a0 ω1 : ℝ} (ha0 : a0 ≠ 0) :
    Real.pi / (4 * a0) * 4 * Real.exp ((1 / 8 : ℝ) / a0) *
        Real.exp (ω1 ^ 2 / (2 * a0)) =
      (Real.pi / a0) *
        Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) := by
  have h4 : Real.pi / (4 * a0) * 4 = Real.pi / a0 := by
    field_simp [ha0]
  have hexp :
      Real.exp ((1 / 8 : ℝ) / a0) * Real.exp (ω1 ^ 2 / (2 * a0)) =
        Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [ha0]
  calc
    Real.pi / (4 * a0) * 4 * Real.exp ((1 / 8 : ℝ) / a0) *
        Real.exp (ω1 ^ 2 / (2 * a0)) =
      (Real.pi / (4 * a0) * 4) *
        (Real.exp ((1 / 8 : ℝ) / a0) * Real.exp (ω1 ^ 2 / (2 * a0))) := by
      ring
    _ = (Real.pi / a0) *
        (Real.exp ((1 / 8 : ℝ) / a0) * Real.exp (ω1 ^ 2 / (2 * a0))) := by
      rw [h4]
    _ = (Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) := by
      rw [hexp]

lemma norm_pureGaborHatHolomorphic_le_box
    {a0 a1 ω1 a omega : ℝ} (ha0 : 0 < a0) (ha : a0 ≤ a) (ha1 : a ≤ a1)
    (hω : |omega| ≤ ω1) (δ : ℂ) (hδ : |δ.re| ≤ 1 / 2) :
    ‖pureGaborHatHolomorphic a omega δ‖ ≤
      (Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) *
        Real.exp (-δ.im ^ 2 / (4 * a1)) := by
  have ha_pos : 0 < a := lt_of_lt_of_le ha0 ha
  have hthree :=
    norm_pureGaborHatHolomorphic_le_three_lobe a omega ha_pos δ
  have hC := gaborHatThreeLobeConst_le_box ha0 ha hδ
  have hL := gaborThreeLobe_le_box (t := δ.im) ha0 ha ha1 hω
  have hC0 : 0 ≤ gaborHatThreeLobeConst a (δ.re + 1 / 2) :=
    gaborHatThreeLobeConst_nonneg a (δ.re + 1 / 2) ha_pos
  have hL0 : 0 ≤ gaborThreeLobe a omega δ.im :=
    gaborThreeLobe_nonneg a omega δ.im
  have hprod := mul_le_mul hC hL hL0 (by positivity)
  refine hthree.trans (hprod.trans ?_)
  have hrew :
      Real.pi / (4 * a0) * Real.exp ((1 / 4 : ℝ) / (2 * a0)) *
          (4 * Real.exp (ω1 ^ 2 / (2 * a0)) *
            Real.exp (-δ.im ^ 2 / (4 * a1))) =
        (Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) *
          Real.exp (-δ.im ^ 2 / (4 * a1)) := by
    rw [exp_one_div_eight_eq ha0]
    have hpf := box_prefactor_mul (ω1 := ω1) ha0.ne'
    calc
      Real.pi / (4 * a0) * Real.exp ((1 / 8 : ℝ) / a0) *
          (4 * Real.exp (ω1 ^ 2 / (2 * a0)) *
            Real.exp (-δ.im ^ 2 / (4 * a1))) =
        (Real.pi / (4 * a0) * 4 * Real.exp ((1 / 8 : ℝ) / a0) *
          Real.exp (ω1 ^ 2 / (2 * a0))) *
          Real.exp (-δ.im ^ 2 / (4 * a1)) := by
        ring
      _ = ((Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0)) *
          Real.exp (-δ.im ^ 2 / (4 * a1)) := by
        rw [hpf]
      _ = (Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0) *
          Real.exp (-δ.im ^ 2 / (4 * a1)) := by
        ring
  exact le_of_eq hrew

lemma abs_delta_re_le_half
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    |((ρ : ℂ) - (1 / 2 : ℂ)).re| ≤ 1 / 2 := by
  simpa [sub_re] using (abs_re_sub_half_lt_half_of_strip ρ).le

lemma gaborContBox_a_pos {a omega : ℝ} (ha : 0 < a)
    {p : ℝ × ℝ}
    (hp : p ∈ Icc (a / 2) (2 * a) ×ˢ Icc (-(|omega| + 1)) (|omega| + 1)) :
    0 < p.1 :=
  lt_of_lt_of_le (half_pos ha) (mem_prod.mp hp).1.1

/-- Uniform box majorant
`(π/a₀) exp((1/8 + ω₁²/2)/a₀) exp(−t²/(4 a₁))`. -/
noncomputable def gaborZeroSideBoxC (a0 ω1 : ℝ) : ℝ :=
  (Real.pi / a0) * Real.exp ((1 / 8 + ω1 ^ 2 / 2) / a0)

lemma gaborZeroSideBoxC_nonneg {a0 ω1 : ℝ} (ha0 : 0 < a0) :
    0 ≤ gaborZeroSideBoxC a0 ω1 := by
  unfold gaborZeroSideBoxC
  positivity

lemma gaborZeroSideBoxC_pos {a0 ω1 : ℝ} (ha0 : 0 < a0) :
    0 < gaborZeroSideBoxC a0 ω1 := by
  unfold gaborZeroSideBoxC
  positivity

lemma norm_gaborZeroSideHolomorphicTerm_le_box
    {a0 a1 ω1 : ℝ} (ha0 : 0 < a0)
    {p : ℝ × ℝ} (ha : a0 ≤ p.1) (ha1 : p.1 ≤ a1) (hω : |p.2| ≤ ω1)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ‖gaborZeroSideHolomorphicTerm ρ p‖ ≤
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
        gaborZeroSideBoxC a0 ω1 *
          Real.exp (-(ρ : ℂ).im ^ 2 / (4 * a1)) := by
  unfold gaborZeroSideHolomorphicTerm
  have hnorm :
      ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
          pureGaborHatHolomorphic p.1 p.2 ((ρ : ℂ) - (1 / 2 : ℂ))‖ =
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          ‖pureGaborHatHolomorphic p.1 p.2 ((ρ : ℂ) - (1 / 2 : ℂ))‖ := by
    rw [norm_mul, Complex.norm_natCast]
  rw [hnorm]
  have hhat :=
    norm_pureGaborHatHolomorphic_le_box ha0 ha ha1 hω
      ((ρ : ℂ) - (1 / 2 : ℂ)) (abs_delta_re_le_half ρ)
  have him : ((ρ : ℂ) - (1 / 2 : ℂ)).im = (ρ : ℂ).im := by simp [sub_im]
  rw [him] at hhat
  have hm0 : (0 : ℝ) ≤ (riemannZetaMultiplicity (ρ : ℂ) : ℝ) :=
    Nat.cast_nonneg _
  have := mul_le_mul_of_nonneg_left hhat hm0
  simpa [gaborZeroSideBoxC, mul_assoc] using this

lemma summable_gaborZeroSideBoxMajorant
    {a0 a1 ω1 : ℝ} (ha0 : 0 < a0) (ha1 : 0 < a1) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * gaborZeroSideBoxC a0 ω1 *
        Real.exp (-(1 / (4 * a1)) * (ρ : ℂ).im ^ 2) := by
  set c : ℝ := 1 / (4 * a1)
  have hc : 0 < c :=
    div_pos (by norm_num) (mul_pos (by norm_num) ha1)
  obtain ⟨K, hK0, hK⟩ := one_add_log_mul_gauss_le_local hc
  set Cm : ℝ :=
    zetaZerosInDiskCardBoundInner +
      ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
        (riemannZetaMultiplicity ρ : ℝ)
  have hCm0 : 0 < Cm :=
    lt_of_lt_of_le zetaZerosInDiskCardBoundInner_pos
      (le_add_of_nonneg_right
        (Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _))
  have hC0 := gaborZeroSideBoxC_nonneg (ω1 := ω1) ha0
  have hbd : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * gaborZeroSideBoxC a0 ω1 *
          Real.exp (-c * (ρ : ℂ).im ^ 2) ≤
        (Cm * gaborZeroSideBoxC a0 ω1 * K) *
          Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) := by
    intro ρ
    have hm := riemannZetaMultiplicity_le_log_all_local ρ.property
    have hexp : 0 ≤ Real.exp (-c * (ρ : ℂ).im ^ 2) := (Real.exp_pos _).le
    have h1 :
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            Real.exp (-c * (ρ : ℂ).im ^ 2) ≤
          Cm * (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
            Real.exp (-c * (ρ : ℂ).im ^ 2) :=
      mul_le_mul_of_nonneg_right hm hexp
    have h2 := mul_le_mul_of_nonneg_left (hK (ρ : ℂ).im) (le_of_lt hCm0)
    have hlog :
        Cm * (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
            Real.exp (-c * (ρ : ℂ).im ^ 2) ≤
          Cm * K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) := by
      simpa [mul_assoc] using h2
    have hmass :
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            Real.exp (-c * (ρ : ℂ).im ^ 2) ≤
          Cm * K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) :=
      h1.trans hlog
    have hmul := mul_le_mul_of_nonneg_left hmass hC0
    simpa [mul_assoc, mul_left_comm, mul_comm] using hmul
  refine Summable.of_nonneg_of_le
    (fun _ => mul_nonneg (mul_nonneg (Nat.cast_nonneg _) hC0)
      (Real.exp_pos _).le)
    (fun ρ => by
      have : Real.exp (-(ρ : ℂ).im ^ 2 / (4 * a1)) =
          Real.exp (-c * (ρ : ℂ).im ^ 2) := by
        unfold c; congr 1; field_simp [ha1.ne']
      simpa [this] using hbd ρ)
    ((summable_gauss_over_zeros (half_pos hc)).mul_left
      (Cm * gaborZeroSideBoxC a0 ω1 * K))

lemma continuousOn_gaborZeroSidePureExt_box
    {a omega : ℝ} (ha : 0 < a) :
    ContinuousOn gaborZeroSidePureExt
      (Icc (a / 2) (2 * a) ×ˢ Icc (-(|omega| + 1)) (|omega| + 1)) := by
  set a0 : ℝ := a / 2
  set a1 : ℝ := 2 * a
  set ω1 : ℝ := |omega| + 1
  set K : Set (ℝ × ℝ) := Icc a0 a1 ×ˢ Icc (-ω1) ω1
  have ha0 : 0 < a0 := half_pos ha
  have ha1 : 0 < a1 := mul_pos (by norm_num) ha
  have hKsub : K ⊆ {p : ℝ × ℝ | 0 < p.1} :=
    fun p hp => gaborContBox_a_pos ha (by simpa [K, a0, a1, ω1] using hp)
  have hf : ∀ ρ, ContinuousOn (gaborZeroSideHolomorphicTerm ρ) K :=
    fun ρ => (continuousOn_gaborZeroSideHolomorphicTerm ρ).mono hKsub
  set u : {z : ℂ // IsCriticalStripZetaZero z} → ℝ := fun ρ =>
    (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * gaborZeroSideBoxC a0 ω1 *
      Real.exp (-(1 / (4 * a1)) * (ρ : ℂ).im ^ 2)
  have hu : Summable u :=
    summable_gaborZeroSideBoxMajorant (ω1 := ω1) ha0 ha1
  have hfu : ∀ ρ p, p ∈ K → ‖gaborZeroSideHolomorphicTerm ρ p‖ ≤ u ρ := by
    intro ρ p hp
    have hp' := mem_prod.mp hp
    have ha_le : a0 ≤ p.1 := hp'.1.1
    have ha_ge : p.1 ≤ a1 := hp'.1.2
    have hω : |p.2| ≤ ω1 := abs_le.mpr (mem_Icc.mp hp'.2)
    have hterm :=
      norm_gaborZeroSideHolomorphicTerm_le_box ha0 ha_le ha_ge hω ρ
    have hexp : Real.exp (-(ρ : ℂ).im ^ 2 / (4 * a1)) =
        Real.exp (-(1 / (4 * a1)) * (ρ : ℂ).im ^ 2) := by
      congr 1
      field_simp [ha1.ne']
    simpa [u, hexp] using hterm
  have htsum :
      ContinuousOn (fun p =>
        ∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          gaborZeroSideHolomorphicTerm ρ p) K :=
    continuousOn_tsum hf hu hfu
  have hre :
      ContinuousOn (fun p =>
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          gaborZeroSideHolomorphicTerm ρ p).re) K :=
    Complex.continuous_re.comp_continuousOn htsum
  refine hre.congr ?_
  intro p hp
  exact gaborZeroSidePureExt_eq_tsum_holomorphic (hKsub hp)

theorem gaborZeroSideContinuous_holds : GaborZeroSideContinuous := by
  intro a omega ha
  set a0 : ℝ := a / 2
  set a1 : ℝ := 2 * a
  set ω1 : ℝ := |omega| + 1
  set K : Set (ℝ × ℝ) := Icc a0 a1 ×ˢ Icc (-ω1) ω1
  have ha0_lt : a0 < a := half_lt_self ha
  have ha_lt : a < a1 := lt_mul_of_one_lt_left ha (by norm_num)
  have hωlo : -ω1 < omega := by
    have : -(|omega| + 1) < -|omega| := by linarith
    exact this.trans_le (neg_abs_le omega)
  have hωhi : omega < ω1 :=
    lt_of_le_of_lt (le_abs_self omega) (lt_add_one _)
  have hKnhds : K ∈ 𝓝 (a, omega) :=
    prod_mem_nhds
      (mem_of_superset (isOpen_Ioo.mem_nhds ⟨ha0_lt, ha_lt⟩)
        Ioo_subset_Icc_self)
      (mem_of_superset (isOpen_Ioo.mem_nhds ⟨hωlo, hωhi⟩)
        Ioo_subset_Icc_self)
  exact (continuousOn_gaborZeroSidePureExt_box ha).continuousAt hKnhds

/-! ## Density of positive rationals -/

lemma exists_pos_rat_close (a : ℝ) (ha : 0 < a) {ε : ℝ} (hε : 0 < ε) :
    ∃ q : ℚ, 0 < (q : ℝ) ∧ |(q : ℝ) - a| < ε := by
  have hlt : max (a / 2) (a - ε) < a + ε := by
    refine max_lt ?_ ?_
    · linarith
    · linarith
  obtain ⟨q, hqL, hqR⟩ := exists_rat_btwn hlt
  have hqpos : 0 < (q : ℝ) :=
    lt_trans (lt_of_lt_of_le (half_pos ha) (le_max_left _ _)) hqL
  have hqa : (q : ℝ) - a < ε := by linarith
  have haq : a - (q : ℝ) < ε := by
    have : a - ε < (q : ℝ) :=
      lt_of_le_of_lt (le_max_right (a / 2) (a - ε)) hqL
    linarith
  exact ⟨q, hqpos, abs_sub_lt_iff.mpr ⟨hqa, haq⟩⟩

lemma exists_rat_close' (x : ℝ) {ε : ℝ} (hε : 0 < ε) :
    ∃ q : ℚ, |(q : ℝ) - x| < ε := by
  obtain ⟨q, hq1, hq2⟩ := exists_rat_btwn (sub_lt_self x hε)
  exact ⟨q, abs_sub_lt_iff.mpr ⟨by linarith, by linarith⟩⟩

lemma tendsto_of_abs_lt_one_div {f : ℕ → ℝ} {x : ℝ}
    (hf : ∀ n, |f n - x| < (1 : ℝ) / (n + 1)) :
    Tendsto f atTop (𝓝 x) := by
  refine Metric.tendsto_atTop.mpr fun ε hε => ?_
  obtain ⟨N, hN⟩ := exists_nat_gt (1 / ε)
  refine ⟨N, fun n hn => ?_⟩
  have hgt : (1 / ε : ℝ) < n + 1 := by
    have : (1 / ε : ℝ) < N := hN
    have hnN : (N : ℝ) ≤ n := Nat.cast_le.mpr hn
    linarith
  have hsmall : (1 : ℝ) / (n + 1) < ε := by
    have hn1 : (0 : ℝ) < n + 1 := by positivity
    rw [div_lt_iff₀ hn1]
    have := (div_lt_iff₀ hε).mp hgt
    simpa [mul_comm] using this
  have : dist (f n) x < ε := by
    simpa [Real.dist_eq] using (hf n).trans hsmall
  exact this

/-! ## Rational family ⇒ real family, given continuity -/

theorem gabor_zeroSide_nonneg_of_rational
    (hcont : GaborZeroSideContinuous)
    (hQ : ∀ (a : ℚ) (ω : ℚ) (ha : 0 < (a : ℝ)),
      0 ≤ gaborZeroSide (pureGaborTest a ω ha))
    (a omega : ℝ) (ha : 0 < a) :
    0 ≤ gaborZeroSide (pureGaborTest a omega ha) := by
  have hseq :
      ∀ n : ℕ, ∃ (q r : ℚ) (hq : 0 < (q : ℝ)),
        |(q : ℝ) - a| < 1 / (n + 1) ∧
          |(r : ℝ) - omega| < 1 / (n + 1) := by
    intro n
    have ε : 0 < (1 : ℝ) / (n + 1) := by positivity
    obtain ⟨q, hqpos, hqa⟩ := exists_pos_rat_close a ha ε
    obtain ⟨r, hr⟩ := exists_rat_close' omega ε
    exact ⟨q, r, hqpos, hqa, hr⟩
  choose q r hq hqa hr using hseq
  have hq_td : Tendsto (fun n : ℕ => ((q n : ℝ))) atTop (𝓝 a) :=
    tendsto_of_abs_lt_one_div (fun n => hqa n)
  have hr_td : Tendsto (fun n : ℕ => ((r n : ℝ))) atTop (𝓝 omega) :=
    tendsto_of_abs_lt_one_div (fun n => hr n)
  have hp_td :
      Tendsto (fun n : ℕ => ((q n : ℝ), (r n : ℝ))) atTop
        (𝓝 (a, omega)) :=
    hq_td.prodMk_nhds hr_td
  have hZ :
      Tendsto (fun n : ℕ => gaborZeroSidePureExt (q n, r n)) atTop
        (𝓝 (gaborZeroSidePureExt (a, omega))) :=
    (hcont a omega ha).tendsto.comp hp_td
  have hnn : ∀ n, 0 ≤ gaborZeroSidePureExt (q n, r n) := by
    intro n
    rw [gaborZeroSidePureExt_pos (hq n)]
    exact hQ (q n) (r n) (hq n)
  have hz0 : 0 ≤ gaborZeroSidePureExt (a, omega) :=
    ge_of_tendsto hZ (Eventually.of_forall hnn)
  rwa [gaborZeroSidePureExt_pos ha] at hz0

/-! ## The countable criterion -/

/-- `←` is on-line positivity of the pure family (no continuity). -/
theorem gabor_zeroSide_rational_of_rh
    (hRH : RiemannHypothesis) (a ω : ℚ) (ha : 0 < (a : ℝ)) :
    0 ≤ gaborZeroSide (pureGaborTest a ω ha) :=
  rh_implies_gaborZeroSide_nonneg hRH rfl

/-- Superseded by the unconditional version, kept for the historical
record. -/
theorem gabor_zeroSide_rational_criterion_iff_rh
    (hcont : GaborZeroSideContinuous) :
    (∀ (a : ℚ) (ω : ℚ) (ha : 0 < (a : ℝ)),
      0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔
      RiemannHypothesis := by
  constructor
  · intro hQ
    exact (gabor_zeroSide_pure_criterion_iff_rh_unconditional).1
      (gabor_zeroSide_nonneg_of_rational hcont hQ)
  · intro hRH a ω ha
    exact gabor_zeroSide_rational_of_rh hRH a ω ha

/-- Unconditional rational-packet criterion: continuity of `Z` is
`gaborZeroSideContinuous_holds`. -/
theorem gabor_zeroSide_rational_criterion_iff_rh_unconditional :
    (∀ (a ω : ℚ) (ha : 0 < (a : ℝ)),
      0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔
      RiemannHypothesis :=
  gabor_zeroSide_rational_criterion_iff_rh gaborZeroSideContinuous_holds

/-- RH ⇔ nonnegativity of the explicit prime/archimedean side
POLE − PRIME + ARCH of the pure Gabor packet at all rational
`(a, ω)`, `a > 0`.  Fully prime-side Π₁ form; unconditional.
No RH claim. -/
theorem gabor_primeSide_rational_criterion_iff_rh :
    (∀ (a ω : ℚ) (ha : 0 < (a : ℝ)),
      0 ≤ gaborPoleSide (pureGaborTest a ω ha) -
        gaborPrimeComb (pureGaborTest a ω ha) +
        gaborArchSide (pureGaborTest a ω ha)) ↔
      RiemannHypothesis := by
  refine Iff.trans ?_ gabor_zeroSide_rational_criterion_iff_rh_unconditional
  refine forall_congr' fun a => forall_congr' fun ω => forall_congr' fun ha => ?_
  rw [gabor_explicitFormula_pure (pureGaborTest_admissible a ω ha)
    (pureGaborTest_coeffs a ω ha)]

#print axioms gabor_zeroSide_rational_of_rh
#print axioms gabor_zeroSide_nonneg_of_rational
#print axioms gabor_zeroSide_rational_criterion_iff_rh
#print axioms gaborZeroSideContinuous_holds
#print axioms gabor_zeroSide_rational_criterion_iff_rh_unconditional
#print axioms gabor_primeSide_rational_criterion_iff_rh

end RH
