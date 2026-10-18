import RH.InnerBridges

/-!
# Classical quadrature component of the selected arch error

This file isolates the ordinary analysis in
`SelectedArchErrorQuadraticRate` from the corpus-specific transcription.

Paper proof of the local estimate: on a cell `[a,b]`, Taylor's theorem
with `|f''| ≤ M` bounds the difference between `f` and its affine chord by
`(M / 2) (x-a)(b-x)`.  Integrating this quadratic envelope gives
`M (b-a)^3 / 12`.  Summing cells of common width `Δ` gives the composite
bound `(M / 12) (b-a) Δ^2`.

The exact missing transcription would identify `selectedArchError k f`
with the absolute weighted integral of `I_Δ(f.toFun) - f.toFun`, once the
selected grid covers the support; the near-cell regularization cancels
the common value at zero.  The endpoint-kink theorem below shows why this
does not prove the stated corpus bound: for a one-step test of support
`d`, the terminal cell contributes asymptotically
`weilArchUWeight d * θ(1-θ) * Δ² / 2`.  This is of order `Δ²/d`, whereas
the fixed `archRateConst` remains bounded as `d → 0`.
-/

namespace RH

open MeasureTheory
open Filter
open scoped Topology

/-- Piecewise-affine interpolation of `f.toFun` on the selected
equal-spacing arch grid. -/
noncomputable def selectedArchLinearInterpolant
    (k : ℕ) (f : GridElement) (u : ℝ) : ℝ :=
  let Δ := selectedDelta k
  let n := ⌊u / Δ⌋₊
  f.toFun ((n : ℝ) * Δ) +
    (u / Δ - n) *
      (f.toFun (((n + 1 : ℕ) : ℝ) * Δ) - f.toFun ((n : ℝ) * Δ))

/-- Right endpoint of the last selected cell meeting the native support.
The selected interpolant can remain nonzero between `supportBound` and
this node, even though `f.toFun` already vanishes there. -/
noncomputable def selectedArchGridEndpoint
    (k : ℕ) (f : GridElement) : ℝ :=
  let Δ := selectedDelta k
  ((⌊f.supportBound / Δ⌋₊ + 1 : ℕ) : ℝ) * Δ

/-- Corrected rate interface: every fixed grid autocorrelation admits
some finite quadratic-rate constant.  Unlike the r475 interface, this
does not prescribe a support-uniform formula for that constant. -/
def SelectedArchErrorQuadraticRateExists : Prop :=
  ∀ f : GridElement, ∃ C : ℝ,
    ∀ᶠ k : ℕ in atTop,
      selectedArchError k f ≤ C * selectedDelta k ^ 2

/-- Exact missing analytic lemma.  It bundles the near/far
`productionArchLag` transcription with the finite piecewise-linear
weighted interpolation estimate. -/
def SelectedArchWeightedInterpolationEstimate : Prop :=
  ∀ f : GridElement, ∃ C : ℝ,
    ∀ᶠ k : ℕ in atTop,
      selectedArchError k f =
          |intervalIntegral
            (fun u => weilArchUWeight u *
              (f.toFun u - selectedArchLinearInterpolant k f u))
            0 (selectedArchGridEndpoint k f) volume| ∧
        |intervalIntegral
            (fun u => weilArchUWeight u *
              (f.toFun u - selectedArchLinearInterpolant k f u))
            0 (selectedArchGridEndpoint k f) volume|
          ≤ C * selectedDelta k ^ 2

/-- The exact weighted interpolation estimate discharges the corrected
existential-constant rate interface. -/
theorem selectedArchErrorQuadraticRateExists_of_weightedInterpolationEstimate
    (hestimate : SelectedArchWeightedInterpolationEstimate) :
    SelectedArchErrorQuadraticRateExists := by
  intro f
  obtain ⟨C, hC⟩ := hestimate f
  refine ⟨C, ?_⟩
  filter_upwards [hC] with k hk
  rw [hk.1]
  exact hk.2

/-- The only downstream use of the r475 rate needs merely an
element-dependent constant: the selected arch error tends to zero. -/
theorem selectedArchError_tendsto_zero_of_rateExists
    (hrate : SelectedArchErrorQuadraticRateExists) (f : GridElement) :
    Tendsto (fun k : ℕ => selectedArchError k f) atTop (nhds 0) := by
  obtain ⟨C, hbound⟩ := hrate f
  have hΔ2 : Tendsto (fun k : ℕ => selectedDelta k ^ 2) atTop (nhds 0) := by
    simpa [pow_two] using selectedDelta_tendsto_zero.mul selectedDelta_tendsto_zero
  have hC : Tendsto (fun k : ℕ => C * selectedDelta k ^ 2)
      atTop (nhds 0) := by
    convert hΔ2.const_mul C using 1
    ring
  refine squeeze_zero' (Eventually.of_forall fun _ => abs_nonneg _) ?_ hC
  filter_upwards [hbound] with k hk
  exact hk

/-- Compatibility: the stronger fixed-constant r475 interface implies
the corrected existential-constant interface. -/
theorem selectedArchErrorQuadraticRateExists_of_fixed
    (hrate : SelectedArchErrorQuadraticRate) :
    SelectedArchErrorQuadraticRateExists := by
  intro f
  obtain ⟨k0, hbound⟩ := hrate f
  refine ⟨archRateConst f, ?_⟩
  filter_upwards [eventually_ge_atTop k0,
    selected_covers f.elementAnchor f.meshExp] with k hk0 hcover
  exact hbound k hk0 hcover.1 hcover.2.2 hcover.2.1

/-- The integrated quadratic interpolation envelope has the classical
`1 / 12` constant.  The Taylor remainder is supplied pointwise so this
lemma also applies to piecewise-smooth functions after a cell split. -/
theorem intervalIntegral_affineInterpolation_error_le_one_twelfth
    {f q : ℝ → ℝ} {a b M : ℝ}
    (hab : a ≤ b)
    (hpoint : ∀ x ∈ Set.Icc a b,
      |f x - q x| ≤ (M / 2) * (x - a) * (b - x)) :
    |intervalIntegral (fun x => f x - q x) a b volume|
      ≤ M * (b - a) ^ 3 / 12 := by
  let envelope : ℝ → ℝ := fun x => (M / 2) * (x - a) * (b - x)
  let primitive : ℝ → ℝ := fun x =>
    (M / 2) * (-x ^ 3 / 3 + (a + b) * x ^ 2 / 2 - a * b * x)
  have henvelope : IntervalIntegrable envelope volume a b :=
    Continuous.intervalIntegrable (by fun_prop) a b
  have hnorm :
      ‖intervalIntegral (fun x => f x - q x) a b volume‖
        ≤ intervalIntegral envelope a b volume := by
    apply intervalIntegral.norm_integral_le_of_norm_le hab
    · filter_upwards [] with x hx
      rw [Real.norm_eq_abs]
      exact hpoint x ⟨le_of_lt hx.1, hx.2⟩
    · exact henvelope
  have hintegral :
      intervalIntegral envelope a b volume = M * (b - a) ^ 3 / 12 := by
    calc
      intervalIntegral envelope a b volume = primitive b - primitive a := by
        apply intervalIntegral.integral_eq_sub_of_hasDerivAt
        · intro x _
          dsimp [primitive, envelope]
          convert
            (((((hasDerivAt_id x).pow 3).neg.div_const 3).add
              (((hasDerivAt_const x (a + b)).mul
                ((hasDerivAt_id x).pow 2)).div_const 2)).sub
              (((hasDerivAt_const x (a * b)).mul (hasDerivAt_id x)))).const_mul
                (M / 2) using 1
          all_goals simp only [id_eq]
          all_goals ring
        · exact henvelope
      _ = M * (b - a) ^ 3 / 12 := by
        dsimp [primitive]
        ring
  rw [Real.norm_eq_abs] at hnorm
  exact hnorm.trans_eq hintegral

/-- Exact unweighted defect on the cell containing the support endpoint.
In normalized cell coordinates the true ramp is `θ - t` up to `t = θ`
and zero afterwards, while the nodal interpolant is `θ (1 - t)`.
The signed cell integral is therefore `-θ(1-θ)/2`. -/
theorem endpointKink_cell_integral_defect (θ : ℝ) :
    intervalIntegral
        (fun t => (θ - t) - θ * (1 - t)) 0 θ volume
      + intervalIntegral (fun t => -θ * (1 - t)) θ 1 volume
      = -θ * (1 - θ) / 2 := by
  have hleft :
      intervalIntegral
          (fun t => (θ - t) - θ * (1 - t)) 0 θ volume
        = ((θ - 1) * θ ^ 2 / 2) := by
    let primitive : ℝ → ℝ := fun t => (θ - 1) * t ^ 2 / 2
    calc
      intervalIntegral
          (fun t => (θ - t) - θ * (1 - t)) 0 θ volume
          = primitive θ - primitive 0 := by
              apply intervalIntegral.integral_eq_sub_of_hasDerivAt
              · intro t _
                dsimp [primitive]
                convert
                  (((hasDerivAt_const t (θ - 1)).mul
                    ((hasDerivAt_id t).pow 2)).div_const 2) using 1
                · simp only [id_eq]
                  ring
              · exact Continuous.intervalIntegrable (by fun_prop) 0 θ
      _ = (θ - 1) * θ ^ 2 / 2 := by
        dsimp [primitive]
        ring
  have hright :
      intervalIntegral (fun t => -θ * (1 - t)) θ 1 volume
        = (-θ / 2) - (-θ * θ + θ * θ ^ 2 / 2) := by
    let primitive : ℝ → ℝ := fun t => -θ * t + θ * t ^ 2 / 2
    calc
      intervalIntegral (fun t => -θ * (1 - t)) θ 1 volume
          = primitive 1 - primitive θ := by
              apply intervalIntegral.integral_eq_sub_of_hasDerivAt
              · intro t _
                dsimp [primitive]
                convert
                  ((hasDerivAt_const t (-θ)).mul (hasDerivAt_id t)).add
                    (((hasDerivAt_const t θ).mul
                      ((hasDerivAt_id t).pow 2)).div_const 2) using 1
                · simp only [id_eq]
                  ring
              · exact Continuous.intervalIntegrable (by fun_prop) θ 1
      _ = (-θ / 2) - (-θ * θ + θ * θ ^ 2 / 2) := by
        dsimp [primitive]
        ring
  rw [hleft, hright]
  ring

/-- Arithmetic gap exposed by the endpoint cell at native width `1/64`.
The lower phase coefficient `6` already exceeds the fixed corpus
majorant `4(1+1/64)^2 = 4.1259765625`. -/
theorem meshSix_endpointCoefficient_exceeds_archRateConst :
    4 * (1 + (1 / 64 : ℝ)) ^ 2 < 64 * (3 / 16 : ℝ) / 2 := by
  norm_num

/-- Hypothesis-form closure of the corpus Prop.  A cellwise quadrature
proof may use a sharper constant `C`; it suffices to dominate that
constant by the predefined `archRateConst`. -/
theorem selectedArchErrorQuadraticRate_holds
    (hquadrature :
      ∀ f : GridElement, ∃ k0 : ℕ, ∃ C : ℝ,
        C ≤ archRateConst f ∧
          ∀ k : ℕ, k0 ≤ k → ∀ _hk : 0 < k,
            f.meshExp ≤ selectedMesh k →
            f.elementAnchor ≤ selectedAnchor k →
              selectedArchError k f ≤ C * selectedDelta k ^ 2) :
    SelectedArchErrorQuadraticRate := by
  intro f
  obtain ⟨k0, C, hC, hquad⟩ := hquadrature f
  refine ⟨k0, fun k hk0 _hk hm ha => ?_⟩
  have hlocal := hquad k hk0 _hk hm ha
  have hsq : 0 ≤ selectedDelta k ^ 2 := sq_nonneg _
  nlinarith

end RH
