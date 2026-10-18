/-
RH/ExternalBridges.lean -- THE THREE EXTERNAL BRIDGES MISSING AT r462
(r463, PRIME.RDAGGER.LEAN_FIDELITY_REPAIR.01).

r638L: the honest-contour dictionary is proved; the
gauge-mismatched corpus identification is retained only as an
unasserted historical contract; the sole asserting sorry in this
file is compact off-critical separation.

  internal GridElement positivity
    -> full Weil test-class positivity
    -> standard explicit-formula positivity
    -> Mathlib.NumberTheory.LSeries.RiemannZeta.RiemannHypothesis.

Nothing in this file is an RH claim.  The endpoint in
`FrequentlySelected.lean` is named `_internal` until the remaining
arrow is proved without `sorry`.
-/
import RH.Elementwise
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.NumberTheory.LSeries.Nonvanishing
import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.NumberTheory.LSeries.HurwitzZetaValues
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.Analytic.Order
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Normed.Module.Connected
import Mathlib.LinearAlgebra.Complex.FiniteDimensional
import Mathlib.Topology.Order.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.MeasureTheory.Function.LocallyIntegrable
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Topology.DiscreteSubset
import Mathlib.Analysis.Complex.RemovableSingularity
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.PSeriesComplex
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.Calculus.ParametricIntervalIntegral
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Complex.Convex
import Mathlib.Analysis.Complex.JensenFormula
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.MeasureTheory.Integral.CircleAverage
import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.ENNReal
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Arctan
import Mathlib.Analysis.Complex.BorelCaratheodory
import Mathlib.Analysis.Complex.HasPrimitives
import Mathlib.Analysis.Complex.AbsMax
import Mathlib.Analysis.Fourier.Inversion

namespace RH

/-- Carrier for the fixed-support real Weil autocorrelation class.

The test is continuous, even, compactly supported in
`[-supportRadius, supportRadius]`, and carries an explicit real
autorrelation witness `g(u)=∫ h(t)h(t+u)dt`.  Further strip/transform
conditions needed by a chosen Guinand--Weil theorem remain in the
`admissible` field; they are no longer conflated with density. -/
structure FullWeilTest where
  toFun : ℝ → ℝ
  supportRadius : ℝ
  supportRadius_nonneg : 0 ≤ supportRadius
  continuous_toFun : Continuous toFun
  even_toFun : Function.Even toFun
  support_toFun : ∀ u : ℝ, supportRadius < |u| → toFun u = 0
  autocorrelation : ∃ h : ℝ → ℝ,
    MeasureTheory.MemLp h 2 MeasureTheory.volume ∧
    HasCompactSupport h ∧
    (∃ K : NNReal, LipschitzWith K h) ∧
    (∃ a : ℝ, ∀ t : ℝ, t < a ∨ a + supportRadius < t → h t = 0) ∧
    ∀ u : ℝ, toFun u =
      ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume
  admissible : Prop

/-- The actual half-open step function represented by a
`GridElement`: value `x i` on the dyadic cell `[iD,(i+1)D)` and zero
off the finite cell range. -/
noncomputable def GridElement.toStepFun (f : GridElement) (t : ℝ) : ℝ :=
  if ht : 0 ≤ t ∧ ⌊t / f.D0⌋₊ < f.steps then
    f.x ⟨⌊t / f.D0⌋₊, ht.2⟩
  else 0

/-- Explicit left-sampled dyadic grid element for a witness supported
in `[a,a+R]`.  Values are arbitrary reals; no value-grid rounding is
part of `GridElement`. -/
noncomputable def dyadicSampleGrid
    (h : ℝ → ℝ) (a R : ℝ) (m : ℕ) : GridElement where
  steps := Nat.floor (R * (2 : ℝ) ^ m)
  meshExp := m
  x i := h (a + (i : ℕ) * meshWidth m)

/-- Flooring the number of cells makes the sampled grid support fit
inside the declared target support. -/
theorem dyadicSampleGrid_supportBound_le
    (h : ℝ → ℝ) (a R : ℝ) (m : ℕ) (hR : 0 ≤ R) :
    (dyadicSampleGrid h a R m).supportBound ≤ R := by
  unfold dyadicSampleGrid GridElement.supportBound GridElement.D0
  dsimp
  have hpow : 0 < (2 : ℝ) ^ m := by positivity
  have hfloor :
      ((Nat.floor (R * (2 : ℝ) ^ m) : ℕ) : ℝ) ≤
        R * (2 : ℝ) ^ m :=
    Nat.floor_le (mul_nonneg hR hpow.le)
  calc
    ((Nat.floor (R * (2 : ℝ) ^ m) : ℕ) : ℝ) *
        (1 / (2 : ℝ) ^ m) ≤
      (R * (2 : ℝ) ^ m) * (1 / (2 : ℝ) ^ m) :=
        mul_le_mul_of_nonneg_right hfloor (by positivity)
    _ = R := by field_simp

/-- `D(m) = 2^{-m} → 0`.  Mesh of the r491 left-sampled grid. -/
lemma meshWidth_tendsto_zero :
    Filter.Tendsto meshWidth Filter.atTop (nhds 0) := by
  have h : Filter.Tendsto (fun m : ℕ => ((1 : ℝ) / 2) ^ m)
      Filter.atTop (nhds 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by positivity) (by norm_num)
  convert h using 1
  funext m
  unfold meshWidth
  exact (one_div_pow (2 : ℝ) m).symm

/-- Compactly supported continuous functions on `ℝ` are uniformly
continuous (Heine on a 1-neighbourhood of the support, both sides
vanish outside). -/
lemma FullWeilTest.uniformContinuous_toFun (F : FullWeilTest) :
    UniformContinuous F.toFun := by
  rw [Metric.uniformContinuous_iff]
  intro ε hε
  have hcpt :
      IsCompact (Set.Icc (-(F.supportRadius + 1)) (F.supportRadius + 1)) :=
    isCompact_Icc
  have hUC :=
    hcpt.uniformContinuousOn_of_continuous F.continuous_toFun.continuousOn
  rw [Metric.uniformContinuousOn_iff] at hUC
  obtain ⟨δ', hδ', hδu⟩ := hUC ε hε
  refine ⟨min δ' 1, lt_min hδ' (by norm_num), fun x y hdxy => ?_⟩
  have hd1 : dist x y < 1 := lt_of_lt_of_le hdxy (min_le_right _ _)
  have hdδ : dist x y < δ' := lt_of_lt_of_le hdxy (min_le_left _ _)
  have hmem {z : ℝ} (hz : |z| ≤ F.supportRadius + 1) :
      z ∈ Set.Icc (-(F.supportRadius + 1)) (F.supportRadius + 1) :=
    abs_le.mp hz
  by_cases hx : |x| ≤ F.supportRadius + 1
  · by_cases hy : |y| ≤ F.supportRadius + 1
    · exact hδu x (hmem hx) y (hmem hy) hdδ
    · have hyR : F.supportRadius < |y| :=
        lt_of_lt_of_le' (not_le.mp hy)
          (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1))
      have hxR : F.supportRadius < |x| := by
        have habs : |(|y| - |x|)| ≤ dist y x := abs_abs_sub_abs_le_abs_sub y x
        have : |(|y| - |x|)| < 1 :=
          lt_of_le_of_lt habs (by rwa [dist_comm, Real.dist_eq] at hd1)
        rw [abs_lt] at this
        linarith
      rw [F.support_toFun x hxR, F.support_toFun y hyR, dist_self]
      exact hε
  · have hxR : F.supportRadius < |x| :=
      lt_of_lt_of_le' (not_le.mp hx)
        (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1))
    have hyR : F.supportRadius < |y| := by
      have habs : |(|x| - |y|)| ≤ dist x y := abs_abs_sub_abs_le_abs_sub x y
      have : |(|x| - |y|)| < 1 :=
        lt_of_le_of_lt habs (by rwa [Real.dist_eq] at hd1)
      rw [abs_lt] at this
      linarith
    rw [F.support_toFun x hxR, F.support_toFun y hyR, dist_self]
    exact hε

lemma FullWeilTest.toFun_zero_at_radius (F : FullWeilTest) :
    F.toFun F.supportRadius = 0 := by
  have hs : Filter.Tendsto (fun n : ℕ => F.supportRadius + 1 / (n + 1 : ℝ))
      Filter.atTop (nhds F.supportRadius) := by
    simpa using
      (tendsto_const_nhds (x := F.supportRadius)).add
        tendsto_one_div_add_atTop_nhds_zero_nat
  have hval : ∀ n : ℕ, F.toFun (F.supportRadius + 1 / (n + 1 : ℝ)) = 0 :=
    fun n => by
      apply F.support_toFun
      rw [abs_of_nonneg
        (add_nonneg F.supportRadius_nonneg (by positivity))]
      exact lt_add_of_pos_right _ (by positivity)
  have hseq : Filter.Tendsto
      (fun n : ℕ => F.toFun (F.supportRadius + 1 / (n + 1 : ℝ)))
      Filter.atTop (nhds 0) := by
    have : (fun n : ℕ => F.toFun (F.supportRadius + 1 / (n + 1 : ℝ))) =
        fun _ => (0 : ℝ) := funext hval
    rw [this]
    exact tendsto_const_nhds
  exact tendsto_nhds_unique
    ((F.continuous_toFun.tendsto F.supportRadius).comp hs) hseq

lemma lipschitz_witness_zero_left {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0) :
    h a = 0 := by
  have hs : Filter.Tendsto (fun n : ℕ => a - 1 / (n + 1 : ℝ))
      Filter.atTop (nhds a) := by
    simpa using
      (tendsto_const_nhds (x := a)).sub tendsto_one_div_add_atTop_nhds_zero_nat
  have hval : ∀ n : ℕ, h (a - 1 / (n + 1 : ℝ)) = 0 := fun n =>
    hsupp _ (Or.inl (sub_lt_self a (by positivity)))
  have hseq : Filter.Tendsto (fun n : ℕ => h (a - 1 / (n + 1 : ℝ)))
      Filter.atTop (nhds 0) := by
    have : (fun n : ℕ => h (a - 1 / (n + 1 : ℝ))) = fun _ => (0 : ℝ) :=
      funext hval
    rw [this]
    exact tendsto_const_nhds
  exact tendsto_nhds_unique ((hK.continuous.tendsto a).comp hs) hseq

lemma lipschitz_witness_zero_right {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0) :
    h (a + R) = 0 := by
  have hs : Filter.Tendsto (fun n : ℕ => a + R + 1 / (n + 1 : ℝ))
      Filter.atTop (nhds (a + R)) := by
    simpa using
      (tendsto_const_nhds (x := a + R)).add tendsto_one_div_add_atTop_nhds_zero_nat
  have hval : ∀ n : ℕ, h (a + R + 1 / (n + 1 : ℝ)) = 0 := fun n =>
    hsupp _ (Or.inr (lt_add_of_pos_right _ (by positivity)))
  have hseq : Filter.Tendsto (fun n : ℕ => h (a + R + 1 / (n + 1 : ℝ)))
      Filter.atTop (nhds 0) := by
    have : (fun n : ℕ => h (a + R + 1 / (n + 1 : ℝ))) = fun _ => (0 : ℝ) :=
      funext hval
    rw [this]
    exact tendsto_const_nhds
  exact tendsto_nhds_unique ((hK.continuous.tendsto (a + R)).comp hs) hseq

lemma lipschitz_witness_abs_le {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (t : ℝ) :
    |h t| ≤ K * R := by
  rcases lt_or_ge t a with hlt | hge
  · rw [hsupp t (Or.inl hlt), abs_zero]
    exact mul_nonneg (NNReal.coe_nonneg _) hR
  rcases lt_or_ge (a + R) t with hgt | _hle
  · rw [hsupp t (Or.inr hgt), abs_zero]
    exact mul_nonneg (NNReal.coe_nonneg _) hR
  · have ha : h a = 0 := lipschitz_witness_zero_left hK hsupp
    have hdist := hK.dist_le_mul t a
    rw [Real.dist_eq, Real.dist_eq, ha, sub_zero] at hdist
    have ht : t - a ≤ R := by linarith
    have ht0 : 0 ≤ t - a := sub_nonneg.mpr hge
    rw [abs_of_nonneg ht0] at hdist
    exact le_trans hdist (mul_le_mul_of_nonneg_left ht (NNReal.coe_nonneg _))

lemma autocorrelation_eq_intervalIntegral
    {h : ℝ → ℝ} {a R u : ℝ}
    (hc : Continuous h) (hs : HasCompactSupport h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) :
    ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume =
      intervalIntegral (fun t : ℝ => h t * h (t + u))
        a (a + R) MeasureTheory.volume := by
  set φ : ℝ → ℝ := fun t => h t * h (t + u)
  have _hint :
      MeasureTheory.Integrable φ MeasureTheory.volume :=
    (hc.mul (hc.comp (by fun_prop))).integrable_of_hasCompactSupport
      (by simpa [φ, Pi.mul_apply] using
        hs.mul_right (f' := fun t => h (t + u)))
  have h0 : ∀ t : ℝ, t ∉ Set.Icc a (a + R) → φ t = 0 := fun t ht => by
    have hout : t < a ∨ a + R < t := by
      rw [Set.mem_Icc, not_and_or] at ht
      rcases ht with hta | htR
      · exact Or.inl (lt_of_not_ge hta)
      · exact Or.inr (lt_of_not_ge htR)
    change h t * h (t + u) = 0
    rw [hsupp t hout, zero_mul]
  have hab : a ≤ a + R := le_add_of_nonneg_right hR
  rw [← MeasureTheory.setIntegral_eq_integral_of_forall_compl_eq_zero h0]
  rw [MeasureTheory.integral_Icc_eq_integral_Ioc]
  exact (intervalIntegral.integral_of_le hab).symm

lemma autocorrelation_integrand_abs_le
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (t u : ℝ) :
    |h t * h (t + u)| ≤ (K * R) ^ 2 := by
  have hb := lipschitz_witness_abs_le hK hsupp hR
  have hKR : 0 ≤ (K : ℝ) * R :=
    mul_nonneg (NNReal.coe_nonneg _) hR
  calc
    |h t * h (t + u)| = |h t| * |h (t + u)| := abs_mul _ _
    _ ≤ (K * R) * (K * R) :=
      mul_le_mul (hb t) (hb (t + u)) (abs_nonneg _) hKR
    _ = (K * R) ^ 2 := by ring

lemma autocorrelation_integrand_lip
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (u x y : ℝ) :
    |h x * h (x + u) - h y * h (y + u)| ≤
      (2 * (K : ℝ) * K * R) * |x - y| := by
  have hb := lipschitz_witness_abs_le hK hsupp hR
  have hdx := hK.dist_le_mul x y
  have hdu := hK.dist_le_mul (x + u) (y + u)
  rw [Real.dist_eq, Real.dist_eq] at hdx
  rw [Real.dist_eq, Real.dist_eq, add_sub_add_right_eq_sub] at hdu
  have hKR : 0 ≤ (K : ℝ) * R :=
    mul_nonneg (NNReal.coe_nonneg _) hR
  have hK0 : 0 ≤ (K : ℝ) := NNReal.coe_nonneg _
  calc
    |h x * h (x + u) - h y * h (y + u)| =
        |(h x - h y) * h (x + u) + h y * (h (x + u) - h (y + u))| := by
      congr 1
      ring
    _ ≤ |(h x - h y) * h (x + u)| + |h y * (h (x + u) - h (y + u))| :=
      abs_add_le _ _
    _ = |h x - h y| * |h (x + u)| + |h y| * |h (x + u) - h (y + u)| := by
      rw [abs_mul, abs_mul]
    _ ≤ (K * |x - y|) * (K * R) + (K * R) * (K * |x - y|) :=
      add_le_add
        (mul_le_mul hdx (hb (x + u)) (abs_nonneg _) (mul_nonneg hK0 (abs_nonneg _)))
        (mul_le_mul (hb y) hdu (abs_nonneg _) hKR)
    _ = (2 * (K : ℝ) * K * R) * |x - y| := by ring

lemma intervalIntegral_lipschitz_left_riemann
    {φ : ℝ → ℝ} {L D α : ℝ}
    (hL : ∀ x y : ℝ, |φ x - φ y| ≤ L * |x - y|)
    (hL0 : 0 ≤ L) (hD : 0 ≤ D)
    (hint : IntervalIntegrable φ MeasureTheory.volume α (α + D)) :
    |intervalIntegral φ α (α + D) MeasureTheory.volume - φ α * D| ≤
      L * D ^ 2 := by
  have hα : α ≤ α + D := le_add_of_nonneg_right hD
  have hconst : IntervalIntegrable (fun _ : ℝ => φ α)
      MeasureTheory.volume α (α + D) :=
    intervalIntegrable_const
  have hsub := intervalIntegral.integral_sub hint hconst
  have hφconst :
      intervalIntegral (fun _ : ℝ => φ α) α (α + D)
        MeasureTheory.volume = φ α * D := by
    rw [intervalIntegral.integral_const, smul_eq_mul]
    ring
  have hrew :
      intervalIntegral φ α (α + D) MeasureTheory.volume - φ α * D =
        intervalIntegral (fun t : ℝ => φ t - φ α) α (α + D)
          MeasureTheory.volume := by
    rw [← hφconst, hsub]
  rw [hrew]
  have habs :=
    intervalIntegral.abs_integral_le_integral_abs
      (f := fun t : ℝ => φ t - φ α) (μ := MeasureTheory.volume) hα
  refine le_trans habs ?_
  have hbound : ∀ t ∈ Set.uIcc α (α + D),
      |(φ t - φ α)| ≤ L * D := by
    intro t ht
    rw [Set.uIcc_of_le hα] at ht
    have htα : |t - α| ≤ D := by
      have h1 : α ≤ t := ht.1
      have h2 : t ≤ α + D := ht.2
      rw [abs_of_nonneg (sub_nonneg.mpr h1)]
      linarith
    exact le_trans (hL t α) (mul_le_mul_of_nonneg_left htα hL0)
  have hintabs : IntervalIntegrable (fun t : ℝ => |φ t - φ α|)
      MeasureTheory.volume α (α + D) :=
    (hint.sub hconst).abs
  have hmono :=
    intervalIntegral.integral_mono_on hα hintabs
      (intervalIntegrable_const (c := L * D))
      (fun t ht => by
        have : t ∈ Set.uIcc α (α + D) := by
          rw [Set.uIcc_of_le hα]
          exact ht
        exact hbound t this)
  refine le_trans hmono ?_
  rw [intervalIntegral.integral_const, smul_eq_mul]
  ring_nf
  nlinarith

lemma dyadicSampleGrid_D0_eq (h : ℝ → ℝ) (a R : ℝ) (m : ℕ) :
    (dyadicSampleGrid h a R m).D0 = meshWidth m := rfl

lemma dyadicSampleGrid_supportBound_tail_lt
    (h : ℝ → ℝ) (a R : ℝ) (m : ℕ) (hR : 0 ≤ R) :
    R - (dyadicSampleGrid h a R m).supportBound < meshWidth m := by
  unfold dyadicSampleGrid GridElement.supportBound GridElement.D0
  dsimp
  have hpow : 0 < (2 : ℝ) ^ m := by positivity
  have hlt : R * (2 : ℝ) ^ m <
      ((Nat.floor (R * (2 : ℝ) ^ m) : ℕ) : ℝ) + 1 :=
    Nat.lt_floor_add_one _
  have : R - ((Nat.floor (R * (2 : ℝ) ^ m) : ℕ) : ℝ) * (1 / (2 : ℝ) ^ m) <
      1 / (2 : ℝ) ^ m := by
    have hgoal : R < ((Nat.floor (R * (2 : ℝ) ^ m) : ℕ) : ℝ) *
        (1 / (2 : ℝ) ^ m) + 1 / (2 : ℝ) ^ m := by
      field_simp
      linarith
    linarith
  simpa [meshWidth] using this

lemma lipschitz_witness_abs_le_mesh
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ} {m i : ℕ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R)
    (hi : (dyadicSampleGrid h a R m).steps ≤ i) :
    |h (a + (i : ℝ) * meshWidth m)| ≤ K * meshWidth m := by
  set D := meshWidth m
  set n := (dyadicSampleGrid h a R m).steps
  have hD : 0 < D := meshWidth_pos m
  have hnR : (n : ℝ) * D ≤ R := by
    simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
      dyadicSampleGrid_supportBound_le h a R m hR
  have htail : R - (n : ℝ) * D ≤ D :=
    le_of_lt (by
      simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
        dyadicSampleGrid_supportBound_tail_lt h a R m hR)
  have haR : h (a + R) = 0 := lipschitz_witness_zero_right hK hsupp
  rcases le_or_gt ((i : ℝ) * D) R with hle | hgt
  · have hdist := hK.dist_le_mul (a + (i : ℝ) * D) (a + R)
    rw [Real.dist_eq, Real.dist_eq, haR, sub_zero, add_sub_add_left_eq_sub] at hdist
    have hid : 0 ≤ R - (i : ℝ) * D := sub_nonneg.mpr hle
    rw [abs_sub_comm, abs_of_nonneg hid] at hdist
    have hile : (n : ℝ) * D ≤ (i : ℝ) * D :=
      mul_le_mul_of_nonneg_right (Nat.cast_le.mpr hi) hD.le
    have hrest : R - (i : ℝ) * D ≤ R - (n : ℝ) * D := by linarith
    exact le_trans hdist
      (mul_le_mul_of_nonneg_left (le_trans hrest htail) (NNReal.coe_nonneg _))
  · rw [hsupp _ (Or.inr (by linarith)), abs_zero]
    exact mul_nonneg (NNReal.coe_nonneg _) hD.le

lemma dyadicSampleGrid_acf_eq
    (h : ℝ → ℝ) (a R : ℝ) (m d : ℕ) :
    (dyadicSampleGrid h a R m).acf d =
      meshWidth m *
        ∑ i : Fin (dyadicSampleGrid h a R m).steps,
          if hi : (i : ℕ) + d < (dyadicSampleGrid h a R m).steps then
            h (a + (i : ℕ) * meshWidth m) *
              h (a + (i : ℕ) * meshWidth m + (d : ℝ) * meshWidth m)
          else 0 := by
  unfold GridElement.acf
  rw [dyadicSampleGrid_D0_eq]
  congr 1
  refine Finset.sum_congr rfl fun i _ => ?_
  dsimp [dyadicSampleGrid]
  split_ifs with hi
  · have harg : a + ((↑i + d : ℕ) : ℝ) * meshWidth m =
        a + (i : ℕ) * meshWidth m + (d : ℝ) * meshWidth m := by
      have hcast : ((↑i + d : ℕ) : ℝ) = (i : ℕ) + (d : ℝ) :=
        Nat.cast_add (i : ℕ) d
      rw [hcast]
      ring
    rw [harg]
  · rfl

lemma dyadicSampleGrid_acf_riemann_gap
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (m d : ℕ) :
    let D := meshWidth m
    let n := (dyadicSampleGrid h a R m).steps
    let φ : ℝ → ℝ := fun t => h t * h (t + (d : ℝ) * D)
    |D * ∑ i : Fin n,
          (if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
        D * ∑ i : Fin n, φ (a + (i : ℕ) * D)| ≤
      ((K : ℝ) * R) ^ 2 * D := by
  intro D n φ
  have hD : 0 < D := meshWidth_pos m
  have hK0 : 0 ≤ (K : ℝ) := NNReal.coe_nonneg _
  have hKR : 0 ≤ (K : ℝ) * R := mul_nonneg hK0 hR
  have hnR : (n : ℝ) * D ≤ R := by
    simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
      dyadicSampleGrid_supportBound_le h a R m hR
  have hfac :
      |D * ∑ i : Fin n,
            (if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
          D * ∑ i : Fin n, φ (a + (i : ℕ) * D)| =
        D * |∑ i : Fin n,
            ((if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
              φ (a + (i : ℕ) * D))| := by
    rw [← mul_sub, abs_mul, abs_of_pos hD]
    congr 2
    exact (Finset.sum_sub_distrib (s := Finset.univ)
      (f := fun i : Fin n =>
        if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0)
      (g := fun i : Fin n => φ (a + (i : ℕ) * D))).symm
  rw [hfac]
  have hterm (i : Fin n) :
      |(if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
          φ (a + (i : ℕ) * D)| ≤ (K * R) * (K * D) := by
    by_cases hi : (i : ℕ) + d < n
    · rw [dif_pos hi, sub_self, abs_zero]
      exact mul_nonneg hKR (mul_nonneg hK0 hD.le)
    · rw [dif_neg hi, zero_sub, abs_neg]
      have hge : n ≤ (i : ℕ) + d := Nat.le_of_not_gt hi
      have htailv :=
        lipschitz_witness_abs_le_mesh (m := m) (i := (i : ℕ) + d)
          hK hsupp hR (by simpa [n] using hge)
      have hb := lipschitz_witness_abs_le hK hsupp hR (a + (i : ℕ) * D)
      have hφ : |φ (a + (i : ℕ) * D)| =
          |h (a + (i : ℕ) * D)| *
            |h (a + (i : ℕ) * D + (d : ℝ) * D)| := by
        simp [φ, abs_mul]
      have harg : a + (i : ℕ) * D + (d : ℝ) * D =
          a + ((↑i + d : ℕ) : ℝ) * D := by
        have hcast : ((↑i + d : ℕ) : ℝ) = (i : ℕ) + (d : ℝ) :=
          Nat.cast_add (i : ℕ) d
        rw [hcast]
        ring
      rw [hφ, harg]
      exact mul_le_mul hb htailv (abs_nonneg _) hKR
  have hsumle :=
    Finset.abs_sum_le_sum_abs
      (s := (Finset.univ : Finset (Fin n)))
      (f := fun i : Fin n =>
        (if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
          φ (a + (i : ℕ) * D))
  refine le_trans (mul_le_mul_of_nonneg_left hsumle hD.le) ?_
  have hsumb :
      ∑ i : Fin n,
          |(if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0) -
            φ (a + (i : ℕ) * D)| ≤
        (n : ℝ) * ((K * R) * (K * D)) := by
    refine le_trans (Finset.sum_le_sum fun i _ => hterm i) ?_
    simp [Finset.sum_const, nsmul_eq_mul]
  refine le_trans (mul_le_mul_of_nonneg_left hsumb hD.le) ?_
  calc
    D * ((n : ℝ) * ((K * R) * (K * D))) =
        ((n : ℝ) * D) * ((K * R) * (K * D)) := by ring
    _ ≤ R * ((K * R) * (K * D)) :=
      mul_le_mul_of_nonneg_right hnR (mul_nonneg hKR (mul_nonneg hK0 hD.le))
    _ = ((K : ℝ) * R) ^ 2 * D := by ring

lemma dyadicSampleGrid_riemann_cell_error
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (m d : ℕ) :
    let D := meshWidth m
    let n := (dyadicSampleGrid h a R m).steps
    let φ : ℝ → ℝ := fun t => h t * h (t + (d : ℝ) * D)
    |D * ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) -
        intervalIntegral φ a (a + (n : ℝ) * D)
          MeasureTheory.volume| ≤
      2 * ((K : ℝ) * R) ^ 2 * D := by
  intro D n φ
  have hD : 0 < D := meshWidth_pos m
  have hK0 : 0 ≤ (K : ℝ) := NNReal.coe_nonneg _
  have hL0 : 0 ≤ 2 * (K : ℝ) * K * R := by positivity
  have hnR : (n : ℝ) * D ≤ R := by
    simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
      dyadicSampleGrid_supportBound_le h a R m hR
  have hφc : Continuous φ :=
    hK.continuous.mul (hK.continuous.comp (by fun_prop))
  have hφint (b c : ℝ) : IntervalIntegrable φ MeasureTheory.volume b c :=
    hφc.intervalIntegrable _ _
  have hφlip (x y : ℝ) :
      |φ x - φ y| ≤ (2 * (K : ℝ) * K * R) * |x - y| :=
    autocorrelation_integrand_lip hK hsupp hR ((d : ℝ) * D) x y
  have hadj :=
    intervalIntegral.sum_integral_adjacent_intervals
      (f := φ) (μ := MeasureTheory.volume) (n := n)
      (a := fun k : ℕ => a + (k : ℝ) * D)
      (fun k _ => hφint _ _)
  have hadj' :
      ∑ k ∈ Finset.range n,
          intervalIntegral φ (a + (k : ℝ) * D)
            (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume =
        intervalIntegral φ a (a + (n : ℝ) * D)
          MeasureTheory.volume := by
    convert hadj
    · simp
  have hcell (k : ℕ) (_hk : k ∈ Finset.range n) :
      |intervalIntegral φ (a + (k : ℝ) * D)
          (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume -
        φ (a + (k : ℝ) * D) * D| ≤
        (2 * (K : ℝ) * K * R) * D ^ 2 := by
    have hcell' : a + ((k + 1 : ℕ) : ℝ) * D = (a + (k : ℝ) * D) + D := by
      rw [Nat.cast_succ]
      ring
    rw [hcell']
    exact intervalIntegral_lipschitz_left_riemann hφlip hL0 hD.le (hφint _ _)
  have hsumcells :
      |∑ k ∈ Finset.range n,
            intervalIntegral φ (a + (k : ℝ) * D)
              (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume -
          ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) * D| ≤
        ∑ k ∈ Finset.range n, (2 * (K : ℝ) * K * R) * D ^ 2 := by
    have hsub :
        ∑ k ∈ Finset.range n,
              intervalIntegral φ (a + (k : ℝ) * D)
                (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume -
            ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) * D =
          ∑ k ∈ Finset.range n,
            (intervalIntegral φ (a + (k : ℝ) * D)
              (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume -
              φ (a + (k : ℝ) * D) * D) :=
      (Finset.sum_sub_distrib
        (s := Finset.range n)
        (fun k => intervalIntegral φ (a + (k : ℝ) * D)
          (a + ((k + 1 : ℕ) : ℝ) * D) MeasureTheory.volume)
        (fun k => φ (a + (k : ℝ) * D) * D)).symm
    rw [hsub]
    exact le_trans (Finset.abs_sum_le_sum_abs _ _)
      (Finset.sum_le_sum fun k hk => hcell k hk)
  have hrewsum :
      ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) * D =
        D * ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) := by
    simp [mul_comm, Finset.mul_sum]
  rw [hadj', hrewsum, abs_sub_comm] at hsumcells
  refine le_trans hsumcells ?_
  have hcard :
      ∑ _k ∈ Finset.range n, (2 * (K : ℝ) * K * R) * D ^ 2 =
        (n : ℝ) * ((2 * (K : ℝ) * K * R) * D ^ 2) := by
    simp [Finset.sum_const, nsmul_eq_mul]
  rw [hcard]
  calc
    (n : ℝ) * ((2 * (K : ℝ) * K * R) * D ^ 2) =
        ((n : ℝ) * D) * (2 * (K : ℝ) * K * R) * D := by ring
    _ ≤ R * (2 * (K : ℝ) * K * R) * D :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_right hnR (by positivity)) hD.le
    _ = 2 * ((K : ℝ) * R) ^ 2 * D := by ring

lemma dyadicSampleGrid_tail_integral_le
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (m d : ℕ) :
    let D := meshWidth m
    let n := (dyadicSampleGrid h a R m).steps
    let φ : ℝ → ℝ := fun t => h t * h (t + (d : ℝ) * D)
    |intervalIntegral φ a (a + (n : ℝ) * D) MeasureTheory.volume -
        intervalIntegral φ a (a + R) MeasureTheory.volume| ≤
      ((K : ℝ) * R) ^ 2 * D := by
  intro D n φ
  have hD : 0 < D := meshWidth_pos m
  have hnR : (n : ℝ) * D ≤ R := by
    simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
      dyadicSampleGrid_supportBound_le h a R m hR
  have htail : R - (n : ℝ) * D < D := by
    simpa [GridElement.supportBound, dyadicSampleGrid_D0_eq] using
      dyadicSampleGrid_supportBound_tail_lt h a R m hR
  have hφc : Continuous φ :=
    hK.continuous.mul (hK.continuous.comp (by fun_prop))
  have hφint (b c : ℝ) : IntervalIntegrable φ MeasureTheory.volume b c :=
    hφc.intervalIntegrable _ _
  have hsplit :=
    intervalIntegral.integral_add_adjacent_intervals
      (hφint a (a + (n : ℝ) * D)) (hφint (a + (n : ℝ) * D) (a + R))
  have hrew :
      intervalIntegral φ a (a + R) MeasureTheory.volume -
          intervalIntegral φ a (a + (n : ℝ) * D) MeasureTheory.volume =
        intervalIntegral φ (a + (n : ℝ) * D) (a + R)
          MeasureTheory.volume := by
    linarith [hsplit]
  rw [abs_sub_comm, hrew]
  have hle : a + (n : ℝ) * D ≤ a + R := by linarith
  have habs :=
    intervalIntegral.abs_integral_le_integral_abs
      (f := φ) (μ := MeasureTheory.volume) hle
  refine le_trans habs ?_
  have hmono :=
    intervalIntegral.integral_mono_on hle
      (hφint (a + (n : ℝ) * D) (a + R)).abs
      (intervalIntegrable_const (c := (K * R) ^ 2))
      (fun t _ht =>
        autocorrelation_integrand_abs_le hK hsupp hR t ((d : ℝ) * D))
  refine le_trans hmono ?_
  rw [intervalIntegral.integral_const, smul_eq_mul]
  have hlen : (a + R) - (a + (n : ℝ) * D) = R - (n : ℝ) * D := by ring
  rw [hlen, mul_comm]
  exact mul_le_mul_of_nonneg_left (le_of_lt htail) (sq_nonneg _)

lemma dyadicSampleGrid_sum_sample_eq
    (h : ℝ → ℝ) (a : ℝ) (m d n : ℕ) :
    let D := meshWidth m
    let φ : ℝ → ℝ := fun t => h t * h (t + (d : ℝ) * D)
    ∑ i : Fin n, φ (a + (i : ℕ) * D) =
      ∑ k ∈ Finset.range n, φ (a + (k : ℝ) * D) := by
  intro D φ
  rw [Finset.sum_fin_eq_sum_range]
  refine Finset.sum_congr rfl fun k hk => ?_
  rw [dif_pos (Finset.mem_range.mp hk)]

lemma dyadicSampleGrid_acf_sub_toFun_le
    {F : FullWeilTest} {h : ℝ → ℝ} {K : NNReal} {a : ℝ}
    (hK : LipschitzWith K h) (hhKs : HasCompactSupport h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + F.supportRadius < t → h t = 0)
    (hac : ∀ u : ℝ, F.toFun u =
      ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume)
    (m d : ℕ) :
    |(dyadicSampleGrid h a F.supportRadius m).acf d -
        F.toFun ((d : ℝ) * meshWidth m)| ≤
      4 * ((K : ℝ) * F.supportRadius) ^ 2 * meshWidth m := by
  set R := F.supportRadius
  set D := meshWidth m
  set n := (dyadicSampleGrid h a R m).steps
  set φ : ℝ → ℝ := fun t => h t * h (t + (d : ℝ) * D)
  have hR : 0 ≤ R := F.supportRadius_nonneg
  have hD : 0 < D := meshWidth_pos m
  rw [dyadicSampleGrid_acf_eq, hac,
    autocorrelation_eq_intervalIntegral hK.continuous hhKs hsupp hR]
  have hgap := dyadicSampleGrid_acf_riemann_gap hK hsupp hR m d
  have hsum := dyadicSampleGrid_sum_sample_eq h a m d n
  have hcells := dyadicSampleGrid_riemann_cell_error hK hsupp hR m d
  have htailI := dyadicSampleGrid_tail_integral_le hK hsupp hR m d
  have hmid :
      |D * ∑ i : Fin n, φ (a + (i : ℕ) * D) -
          intervalIntegral φ a (a + (n : ℝ) * D)
            MeasureTheory.volume| ≤
        2 * ((K : ℝ) * R) ^ 2 * D := by
    simp only [D, φ] at hsum hcells ⊢
    rw [hsum]
    exact hcells
  refine le_trans
    (abs_sub_le (D * ∑ i : Fin n,
        (if hi : (i : ℕ) + d < n then φ (a + (i : ℕ) * D) else 0))
      (D * ∑ i : Fin n, φ (a + (i : ℕ) * D))
      (intervalIntegral φ a (a + R) MeasureTheory.volume)) ?_
  refine le_trans (add_le_add hgap
      (le_trans
        (abs_sub_le (D * ∑ i : Fin n, φ (a + (i : ℕ) * D))
          (intervalIntegral φ a (a + (n : ℝ) * D) MeasureTheory.volume)
          (intervalIntegral φ a (a + R) MeasureTheory.volume))
        (add_le_add hmid htailI))) ?_
  ring_nf
  nlinarith [sq_nonneg ((K : ℝ) * R), hD.le]

lemma dyadicSampleGrid_toFun_uniform
    {F : FullWeilTest} {h : ℝ → ℝ} {K : NNReal} {a : ℝ}
    (hK : LipschitzWith K h) (hhKs : HasCompactSupport h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + F.supportRadius < t → h t = 0)
    (hac : ∀ u : ℝ, F.toFun u =
      ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume)
    {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ m in Filter.atTop, ∀ u : ℝ, |u| ≤ F.supportRadius →
      |(dyadicSampleGrid h a F.supportRadius m).toFun u - F.toFun u| < ε := by
  have hUC := F.uniformContinuous_toFun
  rw [Metric.uniformContinuous_iff] at hUC
  obtain ⟨δ, hδ, hδu⟩ := hUC (ε / 6) (by positivity)
  have hDδ : ∀ᶠ m in Filter.atTop, meshWidth m < δ := by
    have h := meshWidth_tendsto_zero
    rw [Metric.tendsto_atTop] at h
    obtain ⟨N, hN⟩ := h δ hδ
    refine Filter.eventually_atTop.2 ⟨N, fun m hm => ?_⟩
    have := hN m hm
    rwa [Real.dist_eq, sub_zero, abs_of_nonneg (meshWidth_pos m).le] at this
  have hknot : ∀ᶠ m in Filter.atTop,
      4 * ((K : ℝ) * F.supportRadius) ^ 2 * meshWidth m < ε / 6 := by
    have htend :
        Filter.Tendsto
          (fun m : ℕ => 4 * ((K : ℝ) * F.supportRadius) ^ 2 * meshWidth m)
          Filter.atTop (nhds 0) := by
      simpa using meshWidth_tendsto_zero.const_mul
        (4 * ((K : ℝ) * F.supportRadius) ^ 2)
    rw [Metric.tendsto_atTop] at htend
    obtain ⟨N, hN⟩ := htend (ε / 6) (by positivity)
    refine Filter.eventually_atTop.2 ⟨N, fun m hm => ?_⟩
    have := hN m hm
    have hnn : 0 ≤ 4 * ((K : ℝ) * F.supportRadius) ^ 2 * meshWidth m :=
      mul_nonneg (mul_nonneg (by norm_num) (sq_nonneg _))
        (meshWidth_pos m).le
    rwa [Real.dist_eq, sub_zero, abs_of_nonneg hnn] at this
  filter_upwards [hDδ, hknot] with m hDm hkm
  intro u hu
  set R := F.supportRadius
  set D := meshWidth m
  set f := dyadicSampleGrid h a R m
  have hD : 0 < D := meshWidth_pos m
  have hR : 0 ≤ R := F.supportRadius_nonneg
  have hFeven : F.toFun u = F.toFun |u| := by
    rcases le_total 0 u with hu0 | hu0
    · rw [abs_of_nonneg hu0]
    · rw [abs_of_nonpos hu0, F.even_toFun]
  have hω {x y : ℝ} (hxy : dist x y < δ) :
      |F.toFun x - F.toFun y| < ε / 6 := by
    have := hδu hxy
    rwa [Real.dist_eq] at this
  have hknotu (k : ℕ) :
      |f.acf k - F.toFun ((k : ℝ) * D)| < ε / 6 :=
    lt_of_le_of_lt (dyadicSampleGrid_acf_sub_toFun_le hK hhKs hsupp hac m k) hkm
  set q : ℕ := ⌊|u| / D⌋₊
  have hqle : (q : ℝ) ≤ |u| / D := Nat.floor_le (div_nonneg (abs_nonneg _) hD.le)
  have hqt : |u| / D < (q : ℝ) + 1 := Nat.lt_floor_add_one _
  have hqD : (q : ℝ) * D ≤ |u| := (le_div_iff₀ hD).mp hqle
  have hqD' : |u| < ((q + 1 : ℕ) : ℝ) * D := by
    have : |u| / D < ((q + 1 : ℕ) : ℝ) := by
      rw [Nat.cast_succ]
      exact hqt
    exact (div_lt_iff₀ hD).mp this
  have hqd : dist ((q : ℝ) * D) |u| < δ := by
    rw [Real.dist_eq, abs_sub_comm, abs_of_nonneg (sub_nonneg.mpr hqD)]
    have : |u| - (q : ℝ) * D < D := by
      have hsucc : ((q + 1 : ℕ) : ℝ) = (q : ℝ) + 1 := Nat.cast_succ q
      have hqD'' := hqD'
      rw [hsucc] at hqD''
      linarith
    exact lt_trans this hDm
  have hFe : |F.toFun ((q : ℝ) * D) - F.toFun u| < ε / 6 := by
    rw [hFeven]
    exact hω hqd
  by_cases hq : q < f.steps
  · have hθ : 0 ≤ |u| / D - q := sub_nonneg.mpr hqle
    have hθ1 : |u| / D - q < 1 := by linarith
    have hD0 : f.D0 = D := dyadicSampleGrid_D0_eq h a R m
    have hto : f.toFun u =
        f.acf q + (|u| / D - q) * (f.acf (q + 1) - f.acf q) := by
      unfold GridElement.toFun
      rw [hD0]
    rw [hto]
    have hconv :
        f.acf q + (|u| / D - q) * (f.acf (q + 1) - f.acf q) =
          (1 - (|u| / D - q)) * f.acf q + (|u| / D - q) * f.acf (q + 1) := by
      ring
    rw [hconv]
    have hqd1 : dist (((q + 1 : ℕ) : ℝ) * D) |u| < δ := by
      rw [Real.dist_eq, abs_of_nonneg (sub_nonneg.mpr hqD'.le)]
      have : ((q + 1 : ℕ) : ℝ) * D - |u| ≤ D := by
        have : |u| ≥ (q : ℝ) * D := hqD
        have hsucc : ((q + 1 : ℕ) : ℝ) = (q : ℝ) + 1 := Nat.cast_succ q
        rw [hsucc]
        linarith
      exact lt_of_le_of_lt this hDm
    have hFe1 : |F.toFun (((q + 1 : ℕ) : ℝ) * D) - F.toFun u| < ε / 6 := by
      rw [hFeven]
      exact hω hqd1
    set θ := |u| / D - (q : ℝ)
    have hθ01 : 0 ≤ θ := hθ
    have hθle : θ ≤ 1 := le_of_lt hθ1
    have habs :
        |(1 - θ) * f.acf q + θ * f.acf (q + 1) - F.toFun u| ≤
          (1 - θ) * |f.acf q - F.toFun u| + θ * |f.acf (q + 1) - F.toFun u| := by
      have : (1 - θ) * f.acf q + θ * f.acf (q + 1) - F.toFun u =
          (1 - θ) * (f.acf q - F.toFun u) + θ * (f.acf (q + 1) - F.toFun u) := by
        ring
      rw [this]
      refine le_trans (abs_add_le _ _) ?_
      rw [abs_mul, abs_mul, abs_of_nonneg (sub_nonneg.mpr hθle), abs_of_nonneg hθ01]
    refine lt_of_le_of_lt habs ?_
    have h0 : |f.acf q - F.toFun u| < ε / 3 :=
      lt_of_le_of_lt
        (abs_sub_le (f.acf q) (F.toFun ((q : ℝ) * D)) (F.toFun u))
        (by linarith [hknotu q, hFe])
    have h1 : |f.acf (q + 1) - F.toFun u| < ε / 3 :=
      lt_of_le_of_lt
        (abs_sub_le (f.acf (q + 1))
          (F.toFun (((q + 1 : ℕ) : ℝ) * D)) (F.toFun u))
        (by linarith [hknotu (q + 1), hFe1])
    have hcomb :
        (1 - θ) * |f.acf q - F.toFun u| +
            θ * |f.acf (q + 1) - F.toFun u| ≤ ε / 3 := by
      have := add_le_add
        (mul_le_mul_of_nonneg_left (le_of_lt h0) (sub_nonneg.mpr hθle))
        (mul_le_mul_of_nonneg_left (le_of_lt h1) hθ01)
      refine le_trans this ?_
      ring_nf
      linarith
    exact lt_of_le_of_lt hcomb (by linarith)
  · have hsup : f.supportBound ≤ |u| := by
      have hqge : f.steps ≤ q := Nat.le_of_not_gt hq
      have : (f.steps : ℝ) * D ≤ (q : ℝ) * D :=
        mul_le_mul_of_nonneg_right (Nat.cast_le.mpr hqge) hD.le
      unfold GridElement.supportBound
      rw [dyadicSampleGrid_D0_eq]
      exact le_trans this hqD
    rw [f.toFun_eq_zero_of_supportBound_le hsup, zero_sub, abs_neg]
    have hFR : F.toFun R = 0 := F.toFun_zero_at_radius
    have hRu : dist |u| R < δ := by
      rw [Real.dist_eq, abs_sub_comm, abs_of_nonneg (sub_nonneg.mpr hu)]
      have htail : R - f.supportBound < D :=
        dyadicSampleGrid_supportBound_tail_lt h a R m hR
      have : R - |u| ≤ R - f.supportBound := by linarith
      exact lt_of_le_of_lt this (lt_trans htail hDm)
    have : |F.toFun u| < ε / 6 := by
      have hωu : |F.toFun |u| - F.toFun R| < ε / 6 := hω hRu
      rw [hFR, sub_zero] at hωu
      rwa [hFeven]
    linarith

lemma dyadicSampleGrid_l1_tendsto
    {F : FullWeilTest} {h : ℝ → ℝ} {K : NNReal} {a : ℝ}
    (hK : LipschitzWith K h) (hhKs : HasCompactSupport h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + F.supportRadius < t → h t = 0)
    (hac : ∀ u : ℝ, F.toFun u =
      ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume) :
    Filter.Tendsto
      (fun m => intervalIntegral
        (fun u : ℝ =>
          |(dyadicSampleGrid h a F.supportRadius m).toFun u - F.toFun u|)
        (-F.supportRadius) F.supportRadius MeasureTheory.volume)
      Filter.atTop (nhds 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  have hR : 0 ≤ F.supportRadius := F.supportRadius_nonneg
  have hε' : 0 < ε / (2 * F.supportRadius + 1) := by positivity
  have huni :=
    dyadicSampleGrid_toFun_uniform hK hhKs hsupp hac hε'
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1 huni
  refine ⟨N, fun m hm => ?_⟩
  have hpt := hN m hm
  have hgrid :
      IntervalIntegrable
        (dyadicSampleGrid h a F.supportRadius m).toFun
        MeasureTheory.volume (-F.supportRadius) F.supportRadius :=
    (dyadicSampleGrid h a F.supportRadius m).intervalIntegrable_toFun _ _
  have hFint : IntervalIntegrable F.toFun MeasureTheory.volume
      (-F.supportRadius) F.supportRadius :=
    F.continuous_toFun.intervalIntegrable _ _
  have habs :
      IntervalIntegrable
        (fun u =>
          |(dyadicSampleGrid h a F.supportRadius m).toFun u - F.toFun u|)
        MeasureTheory.volume (-F.supportRadius) F.supportRadius :=
    (hgrid.sub hFint).abs
  have hle : -F.supportRadius ≤ F.supportRadius := neg_le_self hR
  have hmono :=
    intervalIntegral.integral_mono_on hle habs
      (intervalIntegrable_const (c := ε / (2 * F.supportRadius + 1)))
      (fun u hu => by
        have huabs : |u| ≤ F.supportRadius := abs_le.mpr ⟨hu.1, hu.2⟩
        exact le_of_lt (hpt u huabs))
  have hbound :
      intervalIntegral
          (fun _ : ℝ => ε / (2 * F.supportRadius + 1))
          (-F.supportRadius) F.supportRadius MeasureTheory.volume =
        (2 * F.supportRadius) * (ε / (2 * F.supportRadius + 1)) := by
    rw [intervalIntegral.integral_const, smul_eq_mul]
    ring
  rw [Real.dist_eq, sub_zero]
  have hnn : 0 ≤ intervalIntegral
      (fun u : ℝ =>
        |(dyadicSampleGrid h a F.supportRadius m).toFun u - F.toFun u|)
      (-F.supportRadius) F.supportRadius MeasureTheory.volume :=
    intervalIntegral.integral_nonneg hle fun u hu => abs_nonneg _
  rw [abs_of_nonneg hnn]
  refine lt_of_le_of_lt (le_trans hmono (le_of_eq hbound)) ?_
  have hden : 0 < 2 * F.supportRadius + 1 := by positivity
  have : (2 * F.supportRadius) * (ε / (2 * F.supportRadius + 1)) < ε := by
    rw [mul_div_assoc']
    exact (div_lt_iff₀ hden).2 (by linarith)
  exact this

/-- Full-class regularized u-space arch integrand, with the same
normalization as r475 `weilArchUIntegrand`. -/
noncomputable def fullWeilArchUIntegrand
    (F : FullWeilTest) (u : ℝ) : ℝ :=
  if u = 0 then 0
  else weilArchUWeight u *
    (Real.exp (-(3 / 2 : ℝ) * u) * F.toFun 0 - F.toFun u)

/-- Full-class archimedean channel, concretely the r475 u-space
pairing at the declared support radius. -/
noncomputable def fullWeilArchSide (F : FullWeilTest) : ℝ :=
  if 0 < F.supportRadius then
    let b := F.supportRadius
    let g0 := F.toFun 0
    let Cb := -(Real.eulerMascheroniConstant + Real.log Real.pi)
      - Real.log (1 - Real.exp (-2 * b))
    Cb * g0 +
      intervalIntegral (fullWeilArchUIntegrand F)
        0 b MeasureTheory.volume
  else 0

/-- Common finite anchor determined by the target support. -/
noncomputable def FullWeilTest.fullAnchor (F : FullWeilTest) : ℕ :=
  max 1 (Nat.ceil (Real.exp F.supportRadius))

/-- Full-class prime channel.  The support anchor makes the
von-Mangoldt pairing visibly finite. -/
noncomputable def fullWeilCombSide (F : FullWeilTest) : ℝ :=
  ∑ n ∈ windowAtoms F.fullAnchor, combMass n * F.toFun (Real.log n)

/-- Standard polar weight.  Since `Π''(u) = -2 cosh(u/2)` for the
r376 potential `Π = polePotential` and `polePairingZ` has an outer
minus sign, the integral weight is `+2 cosh(u/2)`.  This is
equivalently the two evaluations of the bilateral transform at
`±1/2`. -/
noncomputable def fullWeilPoleWeight (u : ℝ) : ℝ :=
  2 * Real.cosh (u / 2)

/-- Full-class pole channel as the bounded-weight integral on the
fixed support. -/
noncomputable def fullWeilPoleSide (F : FullWeilTest) : ℝ :=
  intervalIntegral (fun u : ℝ => fullWeilPoleWeight u * F.toFun u)
    (-F.supportRadius) F.supportRadius MeasureTheory.volume

/-- The continuation of the internal three-channel pairing to the full
Weil test class, now visibly decomposed by channel. -/
noncomputable def fullWeilForm (F : FullWeilTest) : ℝ :=
  fullWeilArchSide F - fullWeilCombSide F + fullWeilPoleSide F

/- The standard Weil explicit-formula quadratic form is defined after
the r530 spectral sum: `Re(∑ m_ρ ĥ(ρ) − ĥ(1))`.  The r463 opaque is
retired; the three-channel identification remains open. -/

/-- Fixed-support approximation data.  `grid n` never exceeds the
target support, converges uniformly there, and converges in `L¹` on
that fixed compact interval.  Uniform convergence supplies every
point evaluation in the finite prime channel; `L¹` controls bounded
integral weights such as the standard polar `cosh` functional.
The last conjunct is the common Dini / Lipschitz majorant required
by the `1/u` arch weight: every approximating PL interpolant shares
one Lipschitz constant (dyadic ACF knots give this uniformly). -/
def FullWeilTest.FixedSupportGridApproximation
    (F : FullWeilTest) (grid : ℕ → GridElement) : Prop :=
  (∀ n, (grid n).supportBound ≤ F.supportRadius) ∧
  (∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop,
    ∀ u : ℝ, |u| ≤ F.supportRadius →
      |(grid n).toFun u - F.toFun u| < ε) ∧
  (∀ n, IntervalIntegrable (grid n).toFun MeasureTheory.volume
    (-F.supportRadius) F.supportRadius) ∧
  Filter.Tendsto
    (fun n => intervalIntegral
      (fun u : ℝ => |(grid n).toFun u - F.toFun u|)
      (-F.supportRadius) F.supportRadius MeasureTheory.volume)
    Filter.atTop (nhds 0) ∧
  ∃ Kgrid : NNReal, ∀ n, LipschitzWith Kgrid (grid n).toFun

/-- Uniform-on-support convergence plus the common support bound gives
pointwise convergence on all of `ℝ` (both functions vanish outside). -/
theorem FullWeilTest.FixedSupportGridApproximation.tendsto_toFun
    {F : FullWeilTest} {grid : ℕ → GridElement}
    (happrox : F.FixedSupportGridApproximation grid) (u : ℝ) :
    Filter.Tendsto (fun n => (grid n).toFun u)
      Filter.atTop (nhds (F.toFun u)) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ :=
    Filter.eventually_atTop.1 (happrox.2.1 ε hε)
  refine ⟨N, fun n hn => ?_⟩
  rw [Real.dist_eq]
  by_cases hu : |u| ≤ F.supportRadius
  · exact hN n hn u hu
  · have hRu : F.supportRadius < |u| := lt_of_not_ge hu
    rw [F.support_toFun u hRu]
    rw [(grid n).toFun_eq_zero_of_lt_abs
      (lt_of_le_of_lt (happrox.1 n) hRu)]
    simpa using hε

/-- Every approximating grid support fits below the target's common
finite prime anchor. -/
theorem GridElement.elementAnchor_le_fullAnchor
    {F : FullWeilTest} {f : GridElement}
    (hsupport : f.supportBound ≤ F.supportRadius) :
    f.elementAnchor ≤ F.fullAnchor := by
  unfold GridElement.elementAnchor FullWeilTest.fullAnchor
  exact max_le_max_left 1
    (Nat.ceil_mono ((Real.exp_le_exp).2 hsupport))

/-- The native prime side equals the target-anchor finite sum whenever
the native support lies in the target support. -/
theorem weilCombSide_eq_fullAnchor
    {F : FullWeilTest} {f : GridElement}
    (hsupport : f.supportBound ≤ F.supportRadius) :
    weilCombSide f =
      ∑ n ∈ windowAtoms F.fullAnchor,
        combMass n * f.toFun (Real.log n) := by
  symm
  exact comb_elementwise_stabilization f
    (f.elementAnchor_le_fullAnchor hsupport)

/-- **Comb continuity (r489, PROVED).**  Fixed support turns the prime
channel into one common finite sum, and uniform convergence supplies
the finitely many point evaluations. -/
theorem fullWeilCombSide_tendsto
    {F : FullWeilTest} {grid : ℕ → GridElement}
    (happrox : F.FixedSupportGridApproximation grid) :
    Filter.Tendsto (fun n => weilCombSide (grid n))
      Filter.atTop (nhds (fullWeilCombSide F)) := by
  unfold fullWeilCombSide
  have heq : (fun k => weilCombSide (grid k)) =
      (fun k => ∑ n ∈ windowAtoms F.fullAnchor,
        combMass n * (grid k).toFun (Real.log n)) := by
    funext k
    exact weilCombSide_eq_fullAnchor (happrox.1 k)
  rw [heq]
  exact tendsto_finset_sum (windowAtoms F.fullAnchor) fun n _ =>
    (happrox.tendsto_toFun (Real.log n)).const_mul (combMass n)

/-- The standard polar integral is continuous for the chosen
fixed-support topology.  This is the analytic rank-two continuity
statement; identifying r376's native-mesh second-difference read with
this integral is recorded separately below. -/
theorem fullWeilPoleIntegral_tendsto
    {F : FullWeilTest} {grid : ℕ → GridElement}
    (happrox : F.FixedSupportGridApproximation grid) :
    Filter.Tendsto
      (fun n => intervalIntegral
        (fun u : ℝ => fullWeilPoleWeight u * (grid n).toFun u)
        (-F.supportRadius) F.supportRadius MeasureTheory.volume)
      Filter.atTop (nhds (fullWeilPoleSide F)) := by
  rw [tendsto_iff_norm_sub_tendsto_zero]
  unfold fullWeilPoleSide
  let C : ℝ := 2 * Real.cosh (F.supportRadius / 2)
  let err : ℕ → ℝ := fun n => intervalIntegral
    (fun u : ℝ => |(grid n).toFun u - F.toFun u|)
    (-F.supportRadius) F.supportRadius MeasureTheory.volume
  have hFint : IntervalIntegrable F.toFun MeasureTheory.volume
      (-F.supportRadius) F.supportRadius :=
    F.continuous_toFun.intervalIntegrable _ _
  have hweight : Continuous fullWeilPoleWeight := by
    unfold fullWeilPoleWeight
    fun_prop
  have hC : Filter.Tendsto (fun n => C * err n)
      Filter.atTop (nhds 0) := by
    simpa only [err, mul_zero] using happrox.2.2.2.1.const_mul C
  refine squeeze_zero' (Filter.Eventually.of_forall fun _ => norm_nonneg _) ?_ hC
  filter_upwards [] with n
  have hgridInt := happrox.2.2.1 n
  have hgridWeighted :=
    hgridInt.continuousOn_mul hweight.continuousOn
  have hFWeighted :=
    hFint.continuousOn_mul hweight.continuousOn
  rw [← intervalIntegral.integral_sub hgridWeighted hFWeighted]
  have hintegrand :
      (fun u : ℝ => fullWeilPoleWeight u * (grid n).toFun u -
        fullWeilPoleWeight u * F.toFun u) =
      (fun u : ℝ => fullWeilPoleWeight u *
        ((grid n).toFun u - F.toFun u)) := by
    funext u
    ring
  rw [hintegrand]
  change ‖intervalIntegral
    (fun u : ℝ => fullWeilPoleWeight u *
      ((grid n).toFun u - F.toFun u))
    (-F.supportRadius) F.supportRadius MeasureTheory.volume‖ ≤ C * err n
  calc
    _ ≤ intervalIntegral
        (fun u : ℝ => C * |(grid n).toFun u - F.toFun u|)
        (-F.supportRadius) F.supportRadius MeasureTheory.volume := by
      apply intervalIntegral.norm_integral_le_of_norm_le
        (neg_le_self F.supportRadius_nonneg)
      · filter_upwards [] with u hu
        have huabs : |u| ≤ F.supportRadius := by
          exact abs_le.mpr ⟨hu.1.le, hu.2⟩
        have hhalf : |u / 2| ≤ |F.supportRadius / 2| := by
          rw [abs_div, abs_div, abs_of_nonneg F.supportRadius_nonneg]
          exact div_le_div_of_nonneg_right huabs (by norm_num)
        have hcosh : Real.cosh (u / 2) ≤
            Real.cosh (F.supportRadius / 2) := by
          exact (Real.cosh_le_cosh).2 hhalf
        simp only [norm_mul, Real.norm_eq_abs, fullWeilPoleWeight]
        rw [abs_of_pos (by norm_num : (0 : ℝ) < 2),
          abs_of_pos (Real.cosh_pos _)]
        dsimp [C]
        exact mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hcosh (by norm_num))
          (abs_nonneg ((grid n).toFun u - F.toFun u))
      · exact ((hgridInt.sub hFint).norm.const_mul C)
    _ = C * err n := by
      rw [intervalIntegral.integral_const_mul]

/-- Density brick: every admissible fixed-support autocorrelation has
a dyadic `GridElement` autocorrelation approximation with the same
support bound.  Classical route: compactly supported `L²` step
approximation of the autocorrelation witness, then dyadic PL
interpolation. -/
def FullWeilFixedSupportGridDensity : Prop :=
  ∀ F : FullWeilTest, F.admissible →
    ∃ grid : ℕ → GridElement, F.FixedSupportGridApproximation grid

/-- Exact dyadic-density target after r491: the approximating sequence
is no longer existentially anonymous, but the explicit left-sampled
`dyadicSampleGrid h a R`.  The remaining proof must establish its
uniform autocorrelation and `L¹` convergence from the support and
Lipschitz contracts. -/
def FullWeilDyadicSampleConvergence : Prop :=
  ∀ F : FullWeilTest, F.admissible →
    ∃ (h : ℝ → ℝ) (K : NNReal) (a : ℝ),
      MeasureTheory.MemLp h 2 MeasureTheory.volume ∧
      HasCompactSupport h ∧
      LipschitzWith K h ∧
      (∀ t : ℝ, t < a ∨ a + F.supportRadius < t → h t = 0) ∧
      (∀ u : ℝ, F.toFun u =
        ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume) ∧
      F.FixedSupportGridApproximation
        (fun m => dyadicSampleGrid h a F.supportRadius m)

/-- Cell slopes vanish past the last ACF knot. -/
lemma GridElement.cellSlope_eq_zero_of_steps_le (f : GridElement) {d : ℕ}
    (hd : f.steps ≤ d) : f.cellSlope d = 0 := by
  unfold GridElement.cellSlope
  rw [f.acf_eq_zero hd, f.acf_eq_zero (le_trans hd (Nat.le_succ _)),
    sub_zero, zero_div]

/-- Even PL interpolant depends only on `|u|`. -/
lemma GridElement.toFun_eq_toFun_abs (f : GridElement) (u : ℝ) :
    f.toFun u = f.toFun |u| := by
  rcases le_or_gt 0 u with hu | hu
  · rw [abs_of_nonneg hu]
  · rw [abs_of_neg hu, f.toFun_even]

/-- Same-cell increment of the nonnegative PL interpolant. -/
lemma GridElement.toFun_sub_le_of_mem_cell (f : GridElement) (d : ℕ)
    {L x y : ℝ} (hL : ∀ k : ℕ, |f.cellSlope k| ≤ L)
    (hx : (d : ℝ) * f.D0 ≤ x) (hxy : x ≤ y)
    (hy : y ≤ ((d : ℝ) + 1) * f.D0) :
    |f.toFun y - f.toFun x| ≤ L * (y - x) := by
  have hylo : (d : ℝ) * f.D0 ≤ y := le_trans hx hxy
  have hx0 : 0 ≤ x :=
    le_trans (mul_nonneg (Nat.cast_nonneg _) f.D0_pos.le) hx
  have hy0 : 0 ≤ y := le_trans hx0 hxy
  rw [f.toFun_eq_affine_on_nonneg_cell d hx (le_trans hxy hy),
    f.toFun_eq_affine_on_nonneg_cell d hylo hy]
  have hdiff :
      f.cellIntercept d + f.cellSlope d * y -
        (f.cellIntercept d + f.cellSlope d * x) =
      f.cellSlope d * (y - x) := by ring
  rw [hdiff, abs_mul, abs_of_nonneg (sub_nonneg.mpr hxy)]
  exact mul_le_mul_of_nonneg_right (hL d) (sub_nonneg.mpr hxy)

/-- Telescoping ACF increments from knot `i` across `n` cells. -/
lemma GridElement.acf_sub_eq_sum_cell (f : GridElement) (i n : ℕ) :
    f.acf (i + n) - f.acf i =
      ∑ k ∈ Finset.range n, (f.acf (i + k + 1) - f.acf (i + k)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ← ih]
    ring

/-- Nonnegative restriction of the PL interpolant is Lipschitz. -/
lemma GridElement.toFun_nonneg_lip (f : GridElement) {L s t : ℝ}
    (hL : ∀ d : ℕ, |f.cellSlope d| ≤ L) (hs : 0 ≤ s) (hst : s ≤ t) :
    |f.toFun t - f.toFun s| ≤ L * (t - s) := by
  have hs0 : 0 ≤ s / f.D0 := div_nonneg hs f.D0_pos.le
  have htD : 0 ≤ t / f.D0 := div_nonneg (le_trans hs hst) f.D0_pos.le
  let i : ℕ := ⌊s / f.D0⌋₊
  let j : ℕ := ⌊t / f.D0⌋₊
  have hi : i = ⌊s / f.D0⌋₊ := rfl
  have hj : j = ⌊t / f.D0⌋₊ := rfl
  have hilo : (i : ℝ) * f.D0 ≤ s :=
    (le_div_iff₀ f.D0_pos).mp (Nat.floor_le hs0)
  have hjlo : (j : ℝ) * f.D0 ≤ t :=
    (le_div_iff₀ f.D0_pos).mp (Nat.floor_le htD)
  have hihi : s ≤ ((i : ℝ) + 1) * f.D0 := by
    have := Nat.lt_succ_floor (s / f.D0)
    rw [← hi, Nat.cast_succ] at this
    exact (div_le_iff₀ f.D0_pos).mp (le_of_lt this)
  have hjhi : t ≤ ((j : ℝ) + 1) * f.D0 := by
    have := Nat.lt_succ_floor (t / f.D0)
    rw [← hj, Nat.cast_succ] at this
    exact (div_le_iff₀ f.D0_pos).mp (le_of_lt this)
  have hij : i ≤ j := Nat.floor_le_floor
    (div_le_div_of_nonneg_right hst f.D0_pos.le)
  rcases eq_or_lt_of_le hij with hijeq | hijlt
  · rw [hijeq] at hilo hihi
    simpa [abs_sub_comm, hijeq] using
      f.toFun_sub_le_of_mem_cell (x := s) (y := t) j hL hilo hst hjhi
  · have hle : i + 1 ≤ j := Nat.succ_le_of_lt hijlt
    have h1 : |f.toFun t - f.toFun ((j : ℝ) * f.D0)| ≤
        L * (t - (j : ℝ) * f.D0) :=
      f.toFun_sub_le_of_mem_cell (x := (j : ℝ) * f.D0) (y := t) j hL
        le_rfl hjlo hjhi
    have h3 : |f.toFun (((i : ℝ) + 1) * f.D0) - f.toFun s| ≤
        L * (((i : ℝ) + 1) * f.D0 - s) := by
      simpa [abs_sub_comm] using
        f.toFun_sub_le_of_mem_cell (x := s) (y := ((i : ℝ) + 1) * f.D0)
          i hL hilo hihi le_rfl
    have h2 : |f.toFun ((j : ℝ) * f.D0) -
        f.toFun (((i : ℝ) + 1) * f.D0)| ≤
          L * ((j : ℝ) * f.D0 - ((i : ℝ) + 1) * f.D0) := by
      have hjk : f.toFun ((j : ℝ) * f.D0) = f.acf j :=
        f.toFun_nat_mul_D0 j
      have hik : f.toFun (((i : ℝ) + 1) * f.D0) = f.acf (i + 1) := by
        simpa [Nat.cast_succ] using f.toFun_nat_mul_D0 (i + 1)
      rw [hjk, hik]
      have hsum := f.acf_sub_eq_sum_cell (i + 1) (j - (i + 1))
      have hji : i + 1 + (j - (i + 1)) = j := by omega
      rw [hji] at hsum
      rw [hsum]
      refine le_trans (Finset.abs_sum_le_sum_abs _ _) ?_
      have hterm : ∀ k ∈ Finset.range (j - (i + 1)),
          |f.acf (i + 1 + k + 1) - f.acf (i + 1 + k)| ≤ L * f.D0 := by
        intro k _
        have hslope := hL (i + 1 + k)
        unfold GridElement.cellSlope at hslope
        rw [abs_div, abs_of_pos f.D0_pos] at hslope
        exact (div_le_iff₀ f.D0_pos).mp hslope
      refine le_trans (Finset.sum_le_sum hterm) ?_
      simp only [Finset.sum_const, nsmul_eq_mul, Finset.card_range]
      have hcast :
          ((j : ℝ) - ((i : ℝ) + 1)) * f.D0 =
            ((j - (i + 1) : ℕ) : ℝ) * f.D0 := by
        have : (j : ℝ) - ((i : ℝ) + 1) = ((j - (i + 1) : ℕ) : ℝ) := by
          rw [Nat.cast_sub hle, Nat.cast_add, Nat.cast_one]
        rw [this]
      have hspan :
          (j : ℝ) * f.D0 - ((i : ℝ) + 1) * f.D0 =
            ((j : ℝ) - ((i : ℝ) + 1)) * f.D0 := by ring
      rw [hspan, hcast]
      linarith
    have htri :=
      abs_sub_le (f.toFun t) (f.toFun ((j : ℝ) * f.D0)) (f.toFun s)
    have htri2 :=
      abs_sub_le (f.toFun ((j : ℝ) * f.D0))
        (f.toFun (((i : ℝ) + 1) * f.D0)) (f.toFun s)
    nlinarith [h1, h2, h3, htri, htri2]

/-- A uniform cell-slope bound is a Lipschitz constant for `toFun`. -/
lemma GridElement.lipschitz_toFun_of_slope_bound (f : GridElement) {L : ℝ}
    (hL0 : 0 ≤ L) (hL : ∀ d : ℕ, |f.cellSlope d| ≤ L) :
    LipschitzWith ⟨L, hL0⟩ f.toFun := by
  refine LipschitzWith.of_dist_le_mul fun x y => ?_
  rw [Real.dist_eq, Real.dist_eq]
  change |f.toFun x - f.toFun y| ≤ L * |x - y|
  rw [f.toFun_eq_toFun_abs x, f.toFun_eq_toFun_abs y]
  have habs : |(|x| - |y|)| ≤ |x - y| := abs_abs_sub_abs_le_abs_sub _ _
  refine le_trans ?_ (mul_le_mul_of_nonneg_left habs hL0)
  rcases le_total |x| |y| with hst | hts
  · have hlip := f.toFun_nonneg_lip hL (abs_nonneg x) hst
    rw [abs_sub_comm] at hlip
    convert hlip using 1
    rw [abs_sub_comm (|x|) (|y|), abs_of_nonneg (sub_nonneg.mpr hst)]
  · have hlip := f.toFun_nonneg_lip hL (abs_nonneg y) hts
    convert hlip using 1
    rw [abs_of_nonneg (sub_nonneg.mpr hts)]

/-- Autocorrelation of a Lipschitz compactly-supported witness is
itself Lipschitz, with constant `K² R²`. -/
lemma FullWeilTest.lipschitz_toFun (F : FullWeilTest) :
    ∃ K : NNReal, LipschitzWith K F.toFun := by
  obtain ⟨h, _, hhKs, hhLip, hhSupp, hac⟩ := F.autocorrelation
  obtain ⟨K, hK⟩ := hhLip
  obtain ⟨a, hsupp⟩ := hhSupp
  set R := F.supportRadius
  have hR : 0 ≤ R := F.supportRadius_nonneg
  have hc : Continuous h := hK.continuous
  refine ⟨⟨(K : ℝ) * K * R * R, by positivity⟩, ?_⟩
  refine LipschitzWith.of_dist_le_mul fun u v => ?_
  rw [Real.dist_eq, Real.dist_eq, hac u, hac v]
  rw [autocorrelation_eq_intervalIntegral hc hhKs hsupp hR,
    autocorrelation_eq_intervalIntegral hc hhKs hsupp hR]
  have hφu :
      IntervalIntegrable (fun t : ℝ => h t * h (t + u))
        MeasureTheory.volume a (a + R) :=
    (hc.mul (hc.comp (continuous_add_right u))).intervalIntegrable _ _
  have hφv :
      IntervalIntegrable (fun t : ℝ => h t * h (t + v))
        MeasureTheory.volume a (a + R) :=
    (hc.mul (hc.comp (continuous_add_right v))).intervalIntegrable _ _
  rw [← intervalIntegral.integral_sub hφu hφv]
  have hrew :
      (fun t : ℝ => h t * h (t + u) - h t * h (t + v)) =
        fun t : ℝ => h t * (h (t + u) - h (t + v)) := by
    funext t
    ring
  rw [hrew]
  have hab : a ≤ a + R := le_add_of_nonneg_right hR
  have hpt : ∀ t : ℝ,
      |h t * (h (t + u) - h (t + v))| ≤
        ((K : ℝ) * R) * (K : ℝ) * |u - v| := fun t => by
    rw [abs_mul]
    have hb := lipschitz_witness_abs_le hK hsupp hR t
    have hdu := hK.dist_le_mul (t + u) (t + v)
    rw [Real.dist_eq, Real.dist_eq] at hdu
    have hspan : |t + u - (t + v)| = |u - v| := by
      congr 1
      ring
    rw [hspan] at hdu
    have h1 : |h t| * |h (t + u) - h (t + v)| ≤
        ((K : ℝ) * R) * |h (t + u) - h (t + v)| :=
      mul_le_mul_of_nonneg_right hb (abs_nonneg _)
    have h2 : ((K : ℝ) * R) * |h (t + u) - h (t + v)| ≤
        ((K : ℝ) * R) * ((K : ℝ) * |u - v|) :=
      mul_le_mul_of_nonneg_left hdu (by positivity)
    linarith
  have hconst :
      intervalIntegral
          (fun _ : ℝ => ((K : ℝ) * R) * (K : ℝ) * |u - v|)
          a (a + R) MeasureTheory.volume =
        ((K : ℝ) * K * R * R) * |u - v| := by
    rw [intervalIntegral.integral_const, smul_eq_mul]
    ring
  rw [← Real.norm_eq_abs]
  refine le_trans
    (intervalIntegral.norm_integral_le_of_norm_le hab
      (by
        filter_upwards [] with t _ht
        simpa [Real.norm_eq_abs] using hpt t)
      intervalIntegrable_const)
    (le_of_eq hconst)

/-- `w(u) e^{-3u/2} = 2 e^{-2u}/(1-e^{-2u})` for `u ≠ 0`. -/
lemma weilArchUWeight_mul_exp {u : ℝ} (hu : u ≠ 0) :
    weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u) =
      2 * Real.exp (-2 * u) / (1 - Real.exp (-2 * u)) := by
  unfold weilArchUWeight
  have hden : 1 - Real.exp (-2 * u) ≠ 0 := by
    intro h
    have hexp : Real.exp (-2 * u) = 1 := (sub_eq_zero.mp h).symm
    have hu2 : -2 * u = 0 := by
      rwa [← Real.exp_eq_one_iff]
    exact hu (by nlinarith [hu2])
  field_simp [hden]
  rw [← Real.exp_add]
  ring_nf

/-- The regularized weight is positive on `(0, ∞)`. -/
lemma weilArchUWeight_pos {u : ℝ} (hu : 0 < u) : 0 < weilArchUWeight u := by
  unfold weilArchUWeight
  have hnum : 0 < 2 * Real.exp (-u / 2) := by positivity
  have hden : 0 < 1 - Real.exp (-2 * u) :=
    sub_pos.mpr (Real.exp_lt_one_iff.2 (by linarith))
  positivity

/-- Dini majorant: `w(u)·u ≤ e^{3u/2}` on `(0, ∞)`. -/
lemma weilArchUWeight_mul_id_le {u : ℝ} (hu : 0 < u) :
    weilArchUWeight u * u ≤ Real.exp ((3 / 2 : ℝ) * u) := by
  have hden : 0 < 1 - Real.exp (-2 * u) :=
    sub_pos.mpr (Real.exp_lt_one_iff.2 (by linarith))
  have hge : (2 * u) * Real.exp (-2 * u) ≤ 1 - Real.exp (-2 * u) := by
    have hexp := Real.add_one_le_exp (2 * u)
    have hmul := mul_le_mul_of_nonneg_right hexp (Real.exp_pos (-2 * u)).le
    rw [add_mul, ← Real.exp_add, one_mul] at hmul
    have hsum : (2 * u) + (-2 * u) = 0 := by ring
    rw [hsum, Real.exp_zero] at hmul
    linarith
  unfold weilArchUWeight
  have hpos : 0 < 2 * u * Real.exp (-2 * u) := by positivity
  have hnum0 : 0 ≤ 2 * Real.exp (-u / 2) * u := by positivity
  have hw :
      2 * Real.exp (-u / 2) / (1 - Real.exp (-2 * u)) * u =
        2 * Real.exp (-u / 2) * u / (1 - Real.exp (-2 * u)) := by
    ring
  rw [hw]
  have hquot :
      2 * Real.exp (-u / 2) * u / (1 - Real.exp (-2 * u)) ≤
        2 * Real.exp (-u / 2) * u / (2 * u * Real.exp (-2 * u)) :=
    div_le_div_of_nonneg_left hnum0 hpos hge
  refine le_trans hquot ?_
  have hu0 : u ≠ 0 := hu.ne'
  have hne : Real.exp (-2 * u) ≠ 0 := (Real.exp_pos _).ne'
  have hsimp :
      2 * Real.exp (-u / 2) * u / (2 * u * Real.exp (-2 * u)) =
        Real.exp ((3 / 2 : ℝ) * u) := by
    field_simp [hu0, hne]
    rw [← Real.exp_add]
    congr 1
    ring
  exact le_of_eq hsimp

/-- Lipschitz increment against the tilted constant term. -/
lemma archDiff_le_of_lipschitz {g : ℝ → ℝ} {K : NNReal} {u : ℝ}
    (hK : LipschitzWith K g) (hu : 0 ≤ u) :
    |Real.exp (-(3 / 2 : ℝ) * u) * g 0 - g u| ≤
      ((3 / 2 : ℝ) * |g 0| + (K : ℝ)) * u := by
  have hexp : |Real.exp (-(3 / 2 : ℝ) * u) - 1| ≤ (3 / 2 : ℝ) * u := by
    have ha : 0 ≤ (3 / 2 : ℝ) * u := by positivity
    have hle : -((3 / 2 : ℝ) * u) + 1 ≤ Real.exp (-((3 / 2 : ℝ) * u)) :=
      Real.add_one_le_exp (-((3 / 2 : ℝ) * u))
    have hnp : Real.exp (-(3 / 2 : ℝ) * u) ≤ 1 := by
      refine Real.exp_le_one_iff.2 ?_
      nlinarith [ha]
    have hrew : Real.exp (-(3 / 2 : ℝ) * u) = Real.exp (-((3 / 2 : ℝ) * u)) := by
      ring_nf
    rw [hrew] at hnp ⊢
    rw [abs_of_nonpos (sub_nonpos.mpr hnp), neg_sub]
    linarith
  have hLip := hK.dist_le_mul 0 u
  rw [Real.dist_eq, Real.dist_eq, zero_sub, abs_neg, abs_of_nonneg hu] at hLip
  have hrew :
      Real.exp (-(3 / 2 : ℝ) * u) * g 0 - g u =
        (Real.exp (-(3 / 2 : ℝ) * u) - 1) * g 0 + (g 0 - g u) := by
    ring
  rw [hrew]
  refine le_trans (abs_add_le _ _) ?_
  rw [abs_mul]
  have h1 : |Real.exp (-(3 / 2 : ℝ) * u) - 1| * |g 0| ≤
      ((3 / 2 : ℝ) * u) * |g 0| :=
    mul_le_mul_of_nonneg_right hexp (abs_nonneg _)
  linarith [h1, hLip]

/-- Pointwise Dini bound for a Lipschitz test against the r475 weight. -/
lemma archIntegrand_dini_bound {g : ℝ → ℝ} {K : NNReal} {u b : ℝ}
    (hK : LipschitzWith K g) (hu : 0 < u) (hub : u ≤ b) :
    |weilArchUWeight u * (Real.exp (-(3 / 2 : ℝ) * u) * g 0 - g u)| ≤
      Real.exp ((3 / 2 : ℝ) * b) *
        ((3 / 2 : ℝ) * |g 0| + (K : ℝ)) := by
  have hw0 : 0 ≤ weilArchUWeight u := (weilArchUWeight_pos hu).le
  have hwu := weilArchUWeight_mul_id_le hu
  have hdiff := archDiff_le_of_lipschitz hK hu.le
  have hexp : Real.exp ((3 / 2 : ℝ) * u) ≤ Real.exp ((3 / 2 : ℝ) * b) :=
    Real.exp_le_exp.2 (by linarith)
  calc
    |weilArchUWeight u * (Real.exp (-(3 / 2 : ℝ) * u) * g 0 - g u)|
        = weilArchUWeight u *
            |Real.exp (-(3 / 2 : ℝ) * u) * g 0 - g u| := by
          rw [abs_mul, abs_of_nonneg hw0]
      _ ≤ weilArchUWeight u * (((3 / 2 : ℝ) * |g 0| + (K : ℝ)) * u) :=
          mul_le_mul_of_nonneg_left hdiff hw0
      _ = (weilArchUWeight u * u) * ((3 / 2 : ℝ) * |g 0| + (K : ℝ)) := by
          ring
      _ ≤ Real.exp ((3 / 2 : ℝ) * u) *
            ((3 / 2 : ℝ) * |g 0| + (K : ℝ)) :=
          mul_le_mul_of_nonneg_right hwu (by positivity)
      _ ≤ Real.exp ((3 / 2 : ℝ) * b) *
            ((3 / 2 : ℝ) * |g 0| + (K : ℝ)) :=
          mul_le_mul_of_nonneg_right hexp (by positivity)

/-- Dyadic sampled ACF interpolants share one Lipschitz constant. -/
lemma dyadicSampleGrid_uniform_lipschitz
    {F : FullWeilTest} {h : ℝ → ℝ} {K : NNReal} {a : ℝ}
    (hK : LipschitzWith K h) (hhKs : HasCompactSupport h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + F.supportRadius < t → h t = 0)
    (hac : ∀ u : ℝ, F.toFun u =
      ∫ t : ℝ, h t * h (t + u) ∂MeasureTheory.volume) :
    ∃ Kgrid : NNReal, ∀ m,
      LipschitzWith Kgrid
        (dyadicSampleGrid h a F.supportRadius m).toFun := by
  obtain ⟨KF, hKF⟩ := F.lipschitz_toFun
  set R := F.supportRadius
  let L : ℝ := (KF : ℝ) + 8 * ((K : ℝ) * R) ^ 2
  have hL0 : 0 ≤ L := by positivity
  refine ⟨⟨L, hL0⟩, fun m => ?_⟩
  refine GridElement.lipschitz_toFun_of_slope_bound _ hL0 fun d => ?_
  set f := dyadicSampleGrid h a R m
  have hD : 0 < f.D0 := f.D0_pos
  by_cases hd : f.steps ≤ d
  · rw [f.cellSlope_eq_zero_of_steps_le hd, abs_zero]
    exact hL0
  · have h1 := dyadicSampleGrid_acf_sub_toFun_le hK hhKs hsupp hac m d
    have h2 := dyadicSampleGrid_acf_sub_toFun_le hK hhKs hsupp hac m (d + 1)
    have hF := hKF.dist_le_mul (((d : ℝ) + 1) * f.D0) ((d : ℝ) * f.D0)
    rw [Real.dist_eq, Real.dist_eq] at hF
    have hspan : |(((d : ℝ) + 1) * f.D0) - ((d : ℝ) * f.D0)| = f.D0 := by
      rw [add_mul, one_mul, add_sub_cancel_left, abs_of_pos hD]
    rw [hspan] at hF
    unfold GridElement.cellSlope
    rw [abs_div, abs_of_pos hD]
    have hDmesh : f.D0 = meshWidth m := rfl
    have h1' : |f.acf d - F.toFun ((d : ℝ) * f.D0)| ≤
        4 * ((K : ℝ) * R) ^ 2 * f.D0 := by
      simpa [f, hDmesh, R] using h1
    have h2' : |f.acf (d + 1) - F.toFun (((d : ℝ) + 1) * f.D0)| ≤
        4 * ((K : ℝ) * R) ^ 2 * f.D0 := by
      simpa [f, hDmesh, R, Nat.cast_succ] using h2
    have h1c : |F.toFun ((d : ℝ) * f.D0) - f.acf d| ≤
        4 * ((K : ℝ) * R) ^ 2 * f.D0 := by
      rw [abs_sub_comm]
      exact h1'
    have htri1 :=
      abs_sub_le (f.acf (d + 1)) (F.toFun (((d : ℝ) + 1) * f.D0)) (f.acf d)
    have htri2 :=
      abs_sub_le (F.toFun (((d : ℝ) + 1) * f.D0))
        (F.toFun ((d : ℝ) * f.D0)) (f.acf d)
    have hdiff : |f.acf (d + 1) - f.acf d| ≤ L * f.D0 := by
      have hsum :
          |f.acf (d + 1) - f.acf d| ≤
            |f.acf (d + 1) - F.toFun (((d : ℝ) + 1) * f.D0)| +
              |F.toFun (((d : ℝ) + 1) * f.D0) - F.toFun ((d : ℝ) * f.D0)| +
                |F.toFun ((d : ℝ) * f.D0) - f.acf d| := by
        linarith [htri1, htri2]
      have hnum :
          |f.acf (d + 1) - F.toFun (((d : ℝ) + 1) * f.D0)| +
            |F.toFun (((d : ℝ) + 1) * f.D0) - F.toFun ((d : ℝ) * f.D0)| +
              |F.toFun ((d : ℝ) * f.D0) - f.acf d| ≤
            8 * ((K : ℝ) * R) ^ 2 * f.D0 + (KF : ℝ) * f.D0 := by
        linarith [h2', hF, h1c]
      have hLrw : 8 * ((K : ℝ) * R) ^ 2 * f.D0 + (KF : ℝ) * f.D0 = L * f.D0 := by
        simp only [L]
        ring
      linarith [hsum, hnum, hLrw]
    exact (div_le_iff₀ hD).mpr hdiff

/-- r493d: the explicit left-sampled grid converges uniformly in the
autocorrelation and in `L¹` on the fixed support.  The witness is
already Lipschitz with interval support, so Heine plus a Lipschitz
Riemann-sum comparison of the ACF knots close both limits. -/
theorem fullWeil_dyadic_sample_convergence :
    FullWeilDyadicSampleConvergence := by
  intro F _hF
  obtain ⟨h, hhLp, hhKs, hhLip, hhSupp, hac⟩ := F.autocorrelation
  obtain ⟨K, hK⟩ := hhLip
  obtain ⟨a, hsupp⟩ := hhSupp
  refine ⟨h, K, a, hhLp, hhKs, hK, hsupp, hac, ?_⟩
  refine ⟨fun m =>
      dyadicSampleGrid_supportBound_le h a F.supportRadius m
        F.supportRadius_nonneg,
    ?unif, fun m =>
      (dyadicSampleGrid h a F.supportRadius m).intervalIntegrable_toFun
        (-F.supportRadius) F.supportRadius,
    ?l1, ?lip⟩
  · intro ε hε
    exact dyadicSampleGrid_toFun_uniform hK hhKs hsupp hac hε
  · exact dyadicSampleGrid_l1_tendsto hK hhKs hsupp hac
  · exact dyadicSampleGrid_uniform_lipschitz hK hhKs hsupp hac

/-- The explicit sampled-grid convergence target implies the
existential fixed-support density interface. -/
theorem fullWeilFixedSupportGridDensity_of_dyadicSample
    (hdyadic : FullWeilDyadicSampleConvergence) :
    FullWeilFixedSupportGridDensity := by
  intro F hF
  obtain ⟨h, K, a, hhLp, hhcompact, hhLip, hhsupport, hac, happrox⟩ :=
    hdyadic F hF
  exact ⟨fun m => dyadicSampleGrid h a F.supportRadius m, happrox⟩

/-- Existing r376 finite-element seam, now placed exactly: the
native-mesh second-difference pole read equals the compact-support
`+2 cosh(u/2)` integral.  Once this dictionary holds, pole continuity
is the proved `fullWeilPoleIntegral_tendsto`. -/
def GridPoleIntegralIdentification : Prop :=
  ∀ (F : FullWeilTest) (grid : ℕ → GridElement), F.admissible →
    F.FixedSupportGridApproximation grid →
      ∀ n, weilPoleSide (grid n) =
        intervalIntegral
          (fun u : ℝ => fullWeilPoleWeight u * (grid n).toFun u)
          (-F.supportRadius) F.supportRadius MeasureTheory.volume

/-- Exact finite-element identity needed for the r376 pole seam.
Each `GridElement.toFun` is the finite hat expansion of its ACF
samples; integrating a hat against `-polePotential'' = 2 cosh(u/2)`
gives the second difference in `polePairingZ`.  The larger interval
causes no change because `toFun` vanishes outside its support. -/
def GridPoleHatIntegralIdentity : Prop :=
  ∀ (f : GridElement) (R : ℝ), f.supportBound ≤ R →
    weilPoleSide f =
      intervalIntegral
        (fun u : ℝ => fullWeilPoleWeight u * f.toFun u)
        (-R) R MeasureTheory.volume

/-- r493c1: evenness split plus dyadic cell decomposition.  The two-sided
pole-density integral equals twice the sum of the nonnegative cell
integrals.  Each cell is the r493b affine integrand on
`[d D0, (d+1) D0]` via `toFun_eq_affine_on_nonneg_cell`. -/
theorem gridPoleIntegral_eq_two_mul_sum_cell
    (f : GridElement) {R : ℝ} (hR : f.supportBound ≤ R) :
    intervalIntegral
        (fun u : ℝ => fullWeilPoleWeight u * f.toFun u)
        (-R) R MeasureTheory.volume =
      2 * ∑ d ∈ Finset.range f.steps,
        intervalIntegral
          (fun u : ℝ => fullWeilPoleWeight u * f.toFun u)
          ((d : ℝ) * f.D0) (((d : ℝ) + 1) * f.D0)
          MeasureTheory.volume := by
  have hswap (a b : ℝ) :
      intervalIntegral
          (fun u : ℝ => fullWeilPoleWeight u * f.toFun u)
          a b MeasureTheory.volume =
        intervalIntegral
          (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
          a b MeasureTheory.volume := by
    refine intervalIntegral.integral_congr fun u _ => ?_
    unfold fullWeilPoleWeight
    ring
  simp_rw [hswap]
  exact f.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_cell hR

/-- r493c2: the native-mesh pole pairing equals the two-sided
`2 cosh(u/2)` integral.  Each cell evaluates to an
`affineCoshPrimitive` increment; the increments telescope against
`poleΔ` after the even one-sided rewrite of `polePairingZ`. -/
theorem gridPoleHatIntegralIdentity : GridPoleHatIntegralIdentity := by
  intro f R hR
  have hswap (a b : ℝ) :
      intervalIntegral
          (fun u : ℝ => fullWeilPoleWeight u * f.toFun u)
          a b MeasureTheory.volume =
        intervalIntegral
          (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
          a b MeasureTheory.volume := by
    refine intervalIntegral.integral_congr fun u _ => ?_
    unfold fullWeilPoleWeight
    ring
  rw [hswap, f.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_increment hR]
  exact weilPoleSide_eq_two_mul_sum_cellCoshIncrement f

/-- The pointwise hat identity supplies the sequence-level pole
dictionary used by channel continuity. -/
theorem gridPoleIntegralIdentification_of_hat
    (hhat : GridPoleHatIntegralIdentity) :
    GridPoleIntegralIdentification := by
  intro F grid _ happrox n
  exact hhat (grid n) F.supportRadius (happrox.1 n)

/-- `w` is continuous on any set that avoids the origin. -/
lemma continuousOn_weilArchUWeight {s : Set ℝ}
    (hs : ∀ x ∈ s, x ≠ 0) : ContinuousOn weilArchUWeight s := by
  unfold weilArchUWeight
  refine ContinuousOn.div (by fun_prop) (by fun_prop) ?_
  intro x hx
  have hx0 : x ≠ 0 := hs x hx
  have hexp : Real.exp (-2 * x) ≠ 1 := by
    intro h
    have : -2 * x = 0 := by
      rwa [← Real.exp_eq_one_iff]
    exact hx0 (by nlinarith [this])
  exact sub_ne_zero.2 hexp.symm

/-- The tilted weight is continuous away from the origin. -/
lemma continuousOn_weilArchUWeight_mul_exp {s : Set ℝ}
    (hs : ∀ x ∈ s, x ≠ 0) :
    ContinuousOn
      (fun u : ℝ => weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u)) s :=
  (continuousOn_weilArchUWeight hs).mul (by fun_prop)

/-- Measurability of the regularized integrand of a measurable test. -/
lemma measurable_weilArchUIntegrand_of_measurable {f : ℝ → ℝ}
    (hf : Measurable f) :
    Measurable (fun u : ℝ =>
      if u = 0 then (0 : ℝ)
      else weilArchUWeight u *
        (Real.exp (-(3 / 2 : ℝ) * u) * f 0 - f u)) := by
  refine Measurable.ite (measurableSet_singleton (0 : ℝ))
    measurable_const ?_
  unfold weilArchUWeight
  fun_prop

/-- Derivative of `log(1-e^{-2u})` is the tilted r475 weight. -/
lemma hasDerivAt_log_one_sub_exp_neg_two {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun t : ℝ => Real.log (1 - Real.exp (-2 * t)))
      (weilArchUWeight x * Real.exp (-(3 / 2 : ℝ) * x)) x := by
  have harg : 0 < 1 - Real.exp (-2 * x) :=
    sub_pos.mpr (Real.exp_lt_one_iff.2 (by linarith))
  have hder : HasDerivAt (fun t : ℝ => 1 - Real.exp (-2 * t))
      (2 * Real.exp (-2 * x)) x := by
    convert (hasDerivAt_const x (1 : ℝ)).sub
      ((Real.hasDerivAt_exp (-2 * x)).comp x
        ((hasDerivAt_id x).const_mul (-2))) using 1
    ring
  have hlog := (Real.hasDerivAt_log (ne_of_gt harg)).comp x hder
  convert hlog using 1
  · rw [weilArchUWeight_mul_exp hx.ne']
    field_simp [harg.ne']

/-- Antiderivative of the tilted weight on a compact interval away from `0`. -/
lemma weilArch_weight_exp_integral {b R : ℝ} (hb : 0 < b) (hle : b ≤ R) :
    intervalIntegral
        (fun u : ℝ =>
          weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u))
        b R MeasureTheory.volume =
      Real.log (1 - Real.exp (-2 * R)) -
        Real.log (1 - Real.exp (-2 * b)) := by
  have hcont :
      ContinuousOn
        (fun u : ℝ =>
          weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u))
        (Set.uIcc b R) := by
    refine continuousOn_weilArchUWeight_mul_exp ?_
    intro x hx
    rw [Set.uIcc_of_le hle] at hx
    exact (lt_of_lt_of_le hb hx.1).ne'
  apply intervalIntegral.integral_eq_sub_of_hasDerivAt
  · intro x hx
    have hxpos : 0 < x := by
      rw [Set.uIcc_of_le hle] at hx
      exact lt_of_lt_of_le hb hx.1
    exact hasDerivAt_log_one_sub_exp_neg_two hxpos
  · exact hcont.intervalIntegrable

/-- The r475 integrand of a Lipschitz test is interval-integrable
on any compact subinterval of `[0, ∞)`. -/
lemma intervalIntegrable_weilArchUIntegrand
    {f : ℝ → ℝ} {K : NNReal} {a b : ℝ}
    (hf : LipschitzWith K f) (ha : 0 ≤ a) (hab : a ≤ b) :
    IntervalIntegrable
      (fun u : ℝ =>
        if u = 0 then (0 : ℝ)
        else weilArchUWeight u *
          (Real.exp (-(3 / 2 : ℝ) * u) * f 0 - f u))
      MeasureTheory.volume a b := by
  let g : ℝ → ℝ := fun _ =>
    Real.exp ((3 / 2 : ℝ) * b) * ((3 / 2 : ℝ) * |f 0| + (K : ℝ))
  refine IntervalIntegrable.mono_fun' (g := g) intervalIntegrable_const ?meas ?bound
  · exact (measurable_weilArchUIntegrand_of_measurable
      hf.continuous.measurable).aestronglyMeasurable
  · refine (MeasureTheory.ae_restrict_iff' measurableSet_uIoc).2 ?_
    refine Filter.Eventually.of_forall fun u hu => ?_
    have huI : u ∈ Set.uIcc a b := Set.uIoc_subset_uIcc hu
    have hu0 : 0 ≤ u := by
      rw [Set.uIcc_of_le hab] at huI
      exact le_trans ha huI.1
    have hub : u ≤ b := by
      rw [Set.uIcc_of_le hab] at huI
      exact huI.2
    by_cases h0 : u = 0
    · simp [h0, g, Real.norm_eq_abs]
      positivity
    · have hupos : 0 < u := lt_of_le_of_ne hu0 (Ne.symm h0)
      simpa [h0, g, Real.norm_eq_abs] using
        archIntegrand_dini_bound hf hupos hub

/-- Cutoff invariance: if `toFun` vanishes past `supportBound ≤ R`,
the pairing at `supportBound` equals the pairing at `R`. -/
lemma weilArchSide_eq_cutoff (f : GridElement) {R : ℝ} {K : NNReal}
    (hR : 0 < R) (hsupp : f.supportBound ≤ R)
    (hK : LipschitzWith K f.toFun) :
    weilArchSide f =
      (-(Real.eulerMascheroniConstant + Real.log Real.pi)
        - Real.log (1 - Real.exp (-2 * R))) * f.toFun 0 +
        intervalIntegral (weilArchUIntegrand f) 0 R
          MeasureTheory.volume := by
  by_cases hb0 : 0 < f.supportBound
  · set b := f.supportBound
    have hbR : b ≤ R := hsupp
    have hI0b : IntervalIntegrable (weilArchUIntegrand f)
        MeasureTheory.volume 0 b :=
      intervalIntegrable_weilArchUIntegrand hK le_rfl f.supportBound_nonneg
    have hIbR : IntervalIntegrable (weilArchUIntegrand f)
        MeasureTheory.volume b R :=
      intervalIntegrable_weilArchUIntegrand hK hb0.le hbR
    have hadd :
        intervalIntegral (weilArchUIntegrand f) 0 R
            MeasureTheory.volume =
          intervalIntegral (weilArchUIntegrand f) 0 b
            MeasureTheory.volume +
          intervalIntegral (weilArchUIntegrand f) b R
            MeasureTheory.volume :=
      (intervalIntegral.integral_add_adjacent_intervals hI0b hIbR).symm
    have htail :
        intervalIntegral (weilArchUIntegrand f) b R
            MeasureTheory.volume =
          f.toFun 0 *
            intervalIntegral
              (fun u : ℝ =>
                weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u))
              b R MeasureTheory.volume := by
      have heq : Set.EqOn (weilArchUIntegrand f)
          (fun u : ℝ =>
            weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u) * f.toFun 0)
          (Set.uIcc b R) := by
        intro u hu
        have hu0 : u ≠ 0 := by
          rw [Set.uIcc_of_le hbR] at hu
          exact (lt_of_lt_of_le hb0 hu.1).ne'
        unfold weilArchUIntegrand
        rw [if_neg hu0]
        have htu : f.toFun u = 0 := by
          rw [Set.uIcc_of_le hbR] at hu
          exact f.toFun_eq_zero_of_supportBound_le
            (le_trans hu.1 (le_abs_self u))
        rw [htu, sub_zero]
        ring
      have hcongr :=
        intervalIntegral.integral_congr (μ := MeasureTheory.volume) heq
      have hmul :
          (fun u : ℝ =>
            weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u) * f.toFun 0) =
            fun u : ℝ =>
              f.toFun 0 *
                (weilArchUWeight u * Real.exp (-(3 / 2 : ℝ) * u)) := by
        funext u
        ring
      rw [hcongr, hmul, intervalIntegral.integral_const_mul]
    unfold weilArchSide
    rw [if_pos (by simpa [b] using hb0)]
    rw [hadd, htail, weilArch_weight_exp_integral hb0 hbR]
    ring
  · have hb : f.supportBound = 0 :=
      le_antisymm (not_lt.mp hb0) f.supportBound_nonneg
    unfold weilArchSide
    rw [if_neg hb0]
    have hto0 : f.toFun 0 = 0 := by
      exact f.toFun_eq_zero_of_supportBound_le (by simpa [hb] using abs_nonneg (0 : ℝ))
    have hI0 : intervalIntegral (weilArchUIntegrand f) 0 R
        MeasureTheory.volume = 0 := by
      have heq : Set.EqOn (weilArchUIntegrand f) (fun _ => (0 : ℝ))
          (Set.uIcc 0 R) := by
        intro u hu
        unfold weilArchUIntegrand
        split_ifs with h0
        · rfl
        · have htu : f.toFun u = 0 :=
            f.toFun_eq_zero_of_supportBound_le (by simpa [hb] using abs_nonneg u)
          have ht00 : f.toFun 0 = 0 := hto0
          rw [ht00, htu]
          ring
      rw [intervalIntegral.integral_congr (μ := MeasureTheory.volume) heq,
        intervalIntegral.integral_zero]
    rw [hto0, hI0]
    ring

/-- r493e: the r475 u-space pairing is continuous along a fixed-support
approximation that carries a common Lipschitz / Dini majorant. -/
theorem fullWeil_arch_side_tendsto
    (F : FullWeilTest) (grid : ℕ → GridElement) :
    F.admissible → F.FixedSupportGridApproximation grid →
      Filter.Tendsto (fun n => weilArchSide (grid n))
        Filter.atTop (nhds (fullWeilArchSide F)) := by
  intro _hF happrox
  obtain ⟨KF, hKF⟩ := F.lipschitz_toFun
  obtain ⟨Kgrid, hKgrid⟩ := happrox.2.2.2.2
  set R := F.supportRadius
  have hR0 : 0 ≤ R := F.supportRadius_nonneg
  by_cases hRz : R = 0
  · have hF0 : fullWeilArchSide F = 0 := by
      unfold fullWeilArchSide
      have : ¬0 < F.supportRadius := by
        simpa [hRz, R] using (lt_irrefl (0 : ℝ))
      simp [this]
    have hn0 : ∀ n, weilArchSide (grid n) = 0 := fun n => by
      unfold weilArchSide
      have : ¬0 < (grid n).supportBound :=
        not_lt.mpr (le_trans (happrox.1 n) (le_of_eq hRz))
      simp [this]
    simpa [hF0, funext hn0] using tendsto_const_nhds (x := (0 : ℝ))
  have hRpos : 0 < R := lt_of_le_of_ne hR0 (Ne.symm hRz)
  have hFeq :
      fullWeilArchSide F =
        (-(Real.eulerMascheroniConstant + Real.log Real.pi)
          - Real.log (1 - Real.exp (-2 * R))) * F.toFun 0 +
          intervalIntegral (fullWeilArchUIntegrand F) 0 R
            MeasureTheory.volume := by
    unfold fullWeilArchSide
    rw [if_pos (by simpa [R] using hRpos)]
  have hgeq : ∀ n,
      weilArchSide (grid n) =
        (-(Real.eulerMascheroniConstant + Real.log Real.pi)
          - Real.log (1 - Real.exp (-2 * R))) * (grid n).toFun 0 +
          intervalIntegral (weilArchUIntegrand (grid n)) 0 R
            MeasureTheory.volume :=
    fun n => weilArchSide_eq_cutoff (grid n) hRpos (happrox.1 n) (hKgrid n)
  have hfun :
      (fun n => weilArchSide (grid n)) =
        fun n =>
          (-(Real.eulerMascheroniConstant + Real.log Real.pi)
            - Real.log (1 - Real.exp (-2 * R))) * (grid n).toFun 0 +
            intervalIntegral (weilArchUIntegrand (grid n)) 0 R
              MeasureTheory.volume := funext hgeq
  rw [hfun, hFeq]
  refine Filter.Tendsto.add ?_ ?_
  · exact tendsto_const_nhds.mul (happrox.tendsto_toFun 0)
  · let C : ℝ :=
      Real.exp ((3 / 2 : ℝ) * R) *
        ((3 / 2 : ℝ) * (|F.toFun 0| + 1) + max (KF : ℝ) (Kgrid : ℝ))
    let bound : ℝ → ℝ := fun _ => C
    have hg0 : ∀ᶠ n in Filter.atTop,
        |(grid n).toFun 0| ≤ |F.toFun 0| + 1 := by
      have htend := Metric.tendsto_nhds.1 (happrox.tendsto_toFun 0) 1
        (by norm_num)
      filter_upwards [htend] with n hn
      have hlt : |(grid n).toFun 0 - F.toFun 0| < 1 := by
        simpa [Real.dist_eq] using hn
      have htri : |(grid n).toFun 0| ≤
          |F.toFun 0| + |(grid n).toFun 0 - F.toFun 0| := by
        have := abs_add_le ((grid n).toFun 0 - F.toFun 0) (F.toFun 0)
        convert this using 1 <;> ring
      exact le_trans htri (add_le_add_right hlt.le _)
    have hIgrid (n : ℕ) :
        IntervalIntegrable (weilArchUIntegrand (grid n))
          MeasureTheory.volume 0 R :=
      intervalIntegrable_weilArchUIntegrand (hKgrid n) le_rfl hR0
    have hIF :
        IntervalIntegrable (fullWeilArchUIntegrand F)
          MeasureTheory.volume 0 R :=
      intervalIntegrable_weilArchUIntegrand hKF le_rfl hR0
    have heq_int (φ : ℝ → ℝ) :
        intervalIntegral φ 0 R MeasureTheory.volume =
          ∫ u in Set.Ioc (0 : ℝ) R, φ u :=
      intervalIntegral.integral_of_le hR0
    simp_rw [heq_int]
    have hbound_int :
        MeasureTheory.Integrable bound
          (MeasureTheory.volume.restrict (Set.Ioc (0 : ℝ) R)) :=
      (intervalIntegrable_const (c := C)).1
    refine MeasureTheory.tendsto_integral_filter_of_dominated_convergence
      (μ := MeasureTheory.volume.restrict (Set.Ioc (0 : ℝ) R))
      bound ?meas ?dom hbound_int ?lim
    · filter_upwards with n
      exact (measurable_weilArchUIntegrand_of_measurable
        (hKgrid n).continuous.measurable).aestronglyMeasurable
    · filter_upwards [hg0] with n hn
      rw [MeasureTheory.ae_restrict_iff' measurableSet_Ioc]
      refine Filter.Eventually.of_forall fun u hu => ?_
      have hupos : 0 < u := hu.1
      have hub : u ≤ R := hu.2
      rw [Real.norm_eq_abs]
      have hpt := archIntegrand_dini_bound (hKgrid n) hupos hub
      have hIeq : weilArchUIntegrand (grid n) u =
          weilArchUWeight u *
            (Real.exp (-(3 / 2 : ℝ) * u) * (grid n).toFun 0 -
              (grid n).toFun u) := by
        unfold weilArchUIntegrand
        rw [if_neg hupos.ne']
      rw [hIeq]
      refine le_trans hpt ?_
      refine mul_le_mul_of_nonneg_left ?_ (Real.exp_pos _).le
      refine add_le_add ?_ (le_max_right _ _)
      exact mul_le_mul_of_nonneg_left hn (by norm_num)
    · rw [MeasureTheory.ae_restrict_iff' measurableSet_Ioc]
      refine Filter.Eventually.of_forall fun u hu => ?_
      have hu0 : u ≠ 0 := hu.1.ne'
      simp only [weilArchUIntegrand, fullWeilArchUIntegrand, hu0, ↓reduceIte]
      exact ((tendsto_const_nhds.mul (happrox.tendsto_toFun 0)).sub
        (happrox.tendsto_toFun u)).const_mul _

def FullWeilArchContinuity : Prop :=
  ∀ (F : FullWeilTest) (grid : ℕ → GridElement), F.admissible →
    F.FixedSupportGridApproximation grid →
      Filter.Tendsto (fun n => weilArchSide (grid n))
        Filter.atTop (nhds (fullWeilArchSide F))

theorem fullWeil_arch_continuity : FullWeilArchContinuity :=
  fullWeil_arch_side_tendsto

/-- Channel-continuity brick along the fixed-support approximation.
The arch component is dominated/L¹ convergence (r475 supplies the
u-space kernel and selected `Δ²` model); the comb component is a
finite sum of point evaluations; the pole component is finite-rank. -/
def FullWeilChannelContinuity : Prop :=
  ∀ (F : FullWeilTest) (grid : ℕ → GridElement), F.admissible →
    F.FixedSupportGridApproximation grid →
      Filter.Tendsto (fun n => weilArchSide (grid n))
        Filter.atTop (nhds (fullWeilArchSide F)) ∧
      Filter.Tendsto (fun n => weilCombSide (grid n))
        Filter.atTop (nhds (fullWeilCombSide F)) ∧
      Filter.Tendsto (fun n => weilPoleSide (grid n))
        Filter.atTop (nhds (fullWeilPoleSide F))

/-- The three channel limits follow from the remaining arch component
and the native-grid pole dictionary.  Comb continuity and standard
polar-integral continuity are proved above. -/
theorem fullWeilChannelContinuity_of_components
    (harch : FullWeilArchContinuity)
    (hpole : GridPoleIntegralIdentification) :
    FullWeilChannelContinuity := by
  intro F grid hF happrox
  refine ⟨harch F grid hF happrox, fullWeilCombSide_tendsto happrox, ?_⟩
  have heq : (fun n => weilPoleSide (grid n)) =
      (fun n => intervalIntegral
        (fun u : ℝ => fullWeilPoleWeight u * (grid n).toFun u)
        (-F.supportRadius) F.supportRadius MeasureTheory.volume) := by
    funext n
    exact hpole F grid hF happrox n
  rw [heq]
  exact fullWeilPoleIntegral_tendsto happrox

/-- **Single remaining dense-completion package (r493d shrink).**

The r376 pole hat dictionary and the r493d dyadic sampled-grid
`L²`/ACF transfer are proved theorems.  The remaining component is
r475 u-space / Dini arch continuity. -/
def FullWeilFixedSupportCompletion : Prop :=
  FullWeilArchContinuity

/-- Form convergence assembled from the three channel limits. -/
theorem fullWeilForm_tendsto_of_channels
    {F : FullWeilTest} {grid : ℕ → GridElement}
    (hchannels :
      Filter.Tendsto (fun n => weilArchSide (grid n))
        Filter.atTop (nhds (fullWeilArchSide F)) ∧
      Filter.Tendsto (fun n => weilCombSide (grid n))
        Filter.atTop (nhds (fullWeilCombSide F)) ∧
      Filter.Tendsto (fun n => weilPoleSide (grid n))
        Filter.atTop (nhds (fullWeilPoleSide F))) :
    Filter.Tendsto (fun n => weilForm (grid n))
      Filter.atTop (nhds (fullWeilForm F)) := by
  unfold weilForm fullWeilForm
  exact hchannels.1.sub hchannels.2.1 |>.add hchannels.2.2

/-- Positivity is closed under the form limit. -/
theorem fullWeilForm_nonneg_of_tendsto
    {F : FullWeilTest} {grid : ℕ → GridElement}
    (hpos : ∀ f : GridElement, 0 ≤ weilForm f)
    (hlim : Filter.Tendsto (fun n => weilForm (grid n))
      Filter.atTop (nhds (fullWeilForm F))) :
    0 ≤ fullWeilForm F :=
  ge_of_tendsto hlim (Filter.Eventually.of_forall fun n => hpos (grid n))

/-- Missing bridge 1: density/continuity from the native dyadic
`GridElement` class to the complete Weil test class. -/
def GridDenseExtension : Prop :=
  (∀ f : GridElement, 0 ≤ weilForm f) →
    ∀ F : FullWeilTest, F.admissible → 0 ≤ fullWeilForm F

/-- The logical dense-extension bridge is proved once the two precise
fixed-support bricks are supplied. -/
theorem grid_dense_extension_of_fixedSupport
    (hdense : FullWeilFixedSupportGridDensity)
    (hcontinuous : FullWeilChannelContinuity) :
    GridDenseExtension := by
  intro hpos F hF
  obtain ⟨grid, hgrid⟩ := hdense F hF
  exact fullWeilForm_nonneg_of_tendsto hpos
    (fullWeilForm_tendsto_of_channels (hcontinuous F grid hF hgrid))

/-- r493e: the remaining dense-completion package is the proved
Dini / u-space arch continuity. -/
theorem fullWeil_fixedSupport_completion :
    FullWeilFixedSupportCompletion :=
  fullWeil_arch_continuity

/-- Grid density is the proved r493d dyadic sampled-grid transfer.
Formerly the first projection `fullWeil_fixedSupport_completion.1`. -/
theorem fullWeil_fixedSupport_grid_density :
    FullWeilFixedSupportGridDensity :=
  fullWeilFixedSupportGridDensity_of_dyadicSample
    fullWeil_dyadic_sample_convergence

/-- All channel limits follow from the remaining arch completion
component, the proved pole hat identity, and the proved comb and
polar-integral continuity theorems. -/
theorem fullWeil_channel_continuity :
    FullWeilChannelContinuity :=
  fullWeilChannelContinuity_of_components
    fullWeil_fixedSupport_completion
    (gridPoleIntegralIdentification_of_hat gridPoleHatIntegralIdentity)

/-- Bridge 1 now consumes exactly the two named bricks above; its
positivity-transfer algebra is sorry-free. -/
theorem grid_dense_extension : GridDenseExtension :=
  grid_dense_extension_of_fixedSupport
    fullWeil_fixedSupport_grid_density fullWeil_channel_continuity

/-! ### r497: multiplicity API for `riemannZeta` (bridge [2], first brick)

Lane decision: prove the explicit-formula identification **before**
off-critical separation.  `FullWeilSeparatesOffCriticalZeros` is
stated against the opaque `standardExplicitFormula`.  That value
cannot be shown negative without an identification (bridge [2]) or a
spectral-side definition, which is the same work.  Mathlib's
`RiemannHypothesis` is the quantified zero statement
`ζ(s)=0 ∧ nontrivial ∧ s≠1 → Re s = 1/2`; the logical wrapper
`standard_weil_criterion_to_mathlib_rh_of_separation` is already
proved.  A contour/Mellin argument for one test family is a
special case of Guinand--Weil, not a bypass of [2].

Named remainder of [2] after this brick:
  [2b] meromorphic `ζ'/ζ` (simple poles, residue = order);
  [2c] local finiteness of zeros and absolute convergence of the
      spectral pairing for admissible tests;
  [2d] contour evaluation = the three-channel form
      (`standard_explicit_formula_identification`).
-/

/-- `ζ` is holomorphic on `ℂ \ {1}`. -/
lemma differentiableOn_riemannZeta_compl_one :
    DifferentiableOn ℂ riemannZeta ({1}ᶜ) :=
  fun _z hz => (differentiableAt_riemannZeta hz).differentiableWithinAt

/-- Analyticity on a neighbourhood of every point of `ℂ \ {1}`. -/
lemma analyticOnNhd_riemannZeta_compl_one :
    AnalyticOnNhd ℂ riemannZeta ({1}ᶜ) :=
  differentiableOn_riemannZeta_compl_one.analyticOnNhd isOpen_compl_singleton

/-- Pointwise analyticity of `ζ` away from the pole. -/
lemma analyticAt_riemannZeta {s : ℂ} (hs : s ≠ 1) :
    AnalyticAt ℂ riemannZeta s :=
  analyticOnNhd_riemannZeta_compl_one s hs

/-- `ℂ \ {1}` is connected (real rank of `ℂ` is 2). -/
lemma isConnected_compl_one : IsConnected ({1}ᶜ : Set ℂ) :=
  isConnected_compl_singleton_of_one_lt_rank
      (Complex.rank_real_complex ▸ Nat.one_lt_ofNat) (1 : ℂ)

/-- `ℂ \ {1}` is preconnected (real rank of `ℂ` is 2). -/
lemma isPreconnected_compl_one : IsPreconnected ({1}ᶜ : Set ℂ) :=
  isConnected_compl_one.isPreconnected

/-- Identity theorem: `ζ` is not eventually zero at any non-polar
point, because `ζ(0) = -1/2 ≠ 0` and `ℂ \ {1}` is preconnected. -/
lemma analyticOrderAt_riemannZeta_ne_top {s : ℂ} (hs : s ≠ 1) :
    analyticOrderAt riemannZeta s ≠ ⊤ := by
  have h0 : (0 : ℂ) ≠ 1 := by norm_num
  have hord0 : analyticOrderAt riemannZeta 0 ≠ ⊤ := by
    have hz0 : riemannZeta 0 ≠ 0 := by
      rw [riemannZeta_zero]
      norm_num
    have hord :
        analyticOrderAt riemannZeta 0 = 0 :=
      (analyticAt_riemannZeta h0).analyticOrderAt_eq_zero.2 hz0
    simp [hord]
  exact analyticOnNhd_riemannZeta_compl_one.analyticOrderAt_ne_top_of_isPreconnected
    isPreconnected_compl_one h0 hs hord0

/-- A genuine zero (away from the pole) has positive order. -/
lemma analyticOrderAt_riemannZeta_ne_zero {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1) :
    analyticOrderAt riemannZeta s ≠ 0 :=
  (analyticAt_riemannZeta hs).analyticOrderAt_ne_zero.2 hz

/-- **r497 brick [2a].**  At every non-polar zero the analytic order
of `riemannZeta` is a positive finite `ℕ∞` (neither `0` nor `⊤`).
This is the multiplicity number that a future spectral sum must
carry.  Mathlib v4.29.1 has `analyticOrderAt` but no `ZetaZero`
enumeration. -/
lemma riemannZeta_analyticOrderAt_finite_pos {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1) :
    analyticOrderAt riemannZeta s ≠ 0 ∧
      analyticOrderAt riemannZeta s ≠ ⊤ :=
  ⟨analyticOrderAt_riemannZeta_ne_zero hz hs,
    analyticOrderAt_riemannZeta_ne_top hs⟩

/-- Local multiplicity as a natural number (junk `0` at the pole). -/
noncomputable def riemannZetaMultiplicity (s : ℂ) : ℕ :=
  analyticOrderNatAt riemannZeta s

lemma riemannZetaMultiplicity_pos {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1) :
    0 < riemannZetaMultiplicity s := by
  have hfin := riemannZeta_analyticOrderAt_finite_pos hz hs
  unfold riemannZetaMultiplicity analyticOrderNatAt
  refine Nat.pos_of_ne_zero ?_
  intro h0
  exact (not_or.mpr ⟨hfin.1, hfin.2⟩) (ENat.toNat_eq_zero.mp h0)

/-! ### r498: meromorphic `ζ'/ζ` at non-polar zeros (bridge [2b], first cut)

Standard local calculus, specialised to `riemannZeta`.  If `f` is
analytic of finite order `m` at `s`, then
`f'/f = m/(z-s) + analytic` on a punctured neighbourhood.  At a
genuine non-polar zero this is a simple pole whose residue equals
`riemannZetaMultiplicity`.  The polar point `s = 1` (intended
residue `-1`) is not in this cut.  Meromorphy on `ℂ \ {1}` is the
carrier a later contour ([2d]) will restrict to a strip rectangle.
-/

section LogDerivZeta

open Filter

open scoped Topology

/-- Logarithmic derivative of a translated monomial.  Used only on
`z ≠ s`; the identity is algebraic. -/
lemma logDeriv_sub_const_pow (s : ℂ) (n : ℕ) (z : ℂ) :
    logDeriv (fun w : ℂ => (w - s) ^ n) z = n / (z - s) := by
  have hcomp :
      (fun w : ℂ => (w - s) ^ n) =
        (fun y : ℂ => y ^ n) ∘ fun w : ℂ => w - s := rfl
  rw [hcomp, logDeriv_comp (by fun_prop) (by fun_prop)]
  simp [logDeriv_pow]

/-- Local factorization of the logarithmic derivative of a
non-identically-vanishing analytic germ: finite order `m` gives
`f'/f = m/(z-s) + h` with `h` analytic at `s`.  Harmless at regular
points (`m = 0`). -/
lemma exists_analytic_logDeriv_eq_order_div
    {f : ℂ → ℂ} {s : ℂ} (hf : AnalyticAt ℂ f s)
    (hfin : analyticOrderAt f s ≠ ⊤) :
    ∃ h : ℂ → ℂ, AnalyticAt ℂ h s ∧
      ∀ᶠ z in 𝓝[≠] s,
        logDeriv f z = (analyticOrderNatAt f s : ℂ) / (z - s) + h z := by
  obtain ⟨g, hg_an, hg_ne, hg_eq⟩ := hf.analyticOrderAt_ne_top.mp hfin
  set m := analyticOrderNatAt f s
  have hg_log : AnalyticAt ℂ (logDeriv g) s :=
    (hg_an.deriv).div hg_an hg_ne
  refine ⟨logDeriv g, hg_log, ?_⟩
  have hg_nz : ∀ᶠ z in 𝓝 s, g z ≠ 0 :=
    hg_an.continuousAt.preimage_mem_nhds
      (isOpen_compl_singleton.mem_nhds hg_ne)
  have hprod : f =ᶠ[𝓝 s] fun z => (z - s) ^ m * g z := by
    filter_upwards [hg_eq] with z hz
    simpa [smul_eq_mul] using hz
  obtain ⟨r, hr, hball⟩ := hg_an.exists_ball_analyticOnNhd
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hprod.eventually_nhds, hg_nz,
    Metric.ball_mem_nhds s hr] with z hf_nhds hgz hzball hzne
  have hz : z ≠ s := hzne
  have hf_eq : f =ᶠ[𝓝 z] fun w => (w - s) ^ m * g w := hf_nhds
  have hpow_ne : (z - s) ^ m ≠ 0 :=
    pow_ne_zero _ (sub_ne_zero.mpr hz)
  have hlog :
      logDeriv f z = logDeriv (fun w => (w - s) ^ m * g w) z := by
    simp [logDeriv_apply, hf_eq.deriv_eq, hf_eq.eq_of_nhds]
  have hdf : DifferentiableAt ℂ (fun w : ℂ => (w - s) ^ m) z := by
    fun_prop
  have hdg : DifferentiableAt ℂ g z :=
    (hball z hzball).differentiableAt
  rw [hlog, logDeriv_mul z hpow_ne hgz hdf hdg,
    logDeriv_sub_const_pow s m z]

/-- **r498 brick [2b], lemma (1).**  At a non-polar zero,
`ζ'/ζ = m/(z-s) + analytic`, with `m = riemannZetaMultiplicity s`. -/
lemma logDeriv_riemannZeta_eq_multiplicity_div_add_analytic {s : ℂ}
    (_hz : riemannZeta s = 0) (hs : s ≠ 1) :
    ∃ h : ℂ → ℂ, AnalyticAt ℂ h s ∧
      ∀ᶠ z in 𝓝[≠] s,
        logDeriv riemannZeta z =
          (riemannZetaMultiplicity s : ℂ) / (z - s) + h z :=
  exists_analytic_logDeriv_eq_order_div
    (analyticAt_riemannZeta hs) (analyticOrderAt_riemannZeta_ne_top hs)

/-- The logarithmic derivative is meromorphic at every non-polar
point (zeros and regular points of `ζ`). -/
lemma meromorphicAt_logDeriv_riemannZeta {s : ℂ} (hs : s ≠ 1) :
    MeromorphicAt (logDeriv riemannZeta) s := by
  obtain ⟨h, hh, heq⟩ :=
    exists_analytic_logDeriv_eq_order_div
      (analyticAt_riemannZeta hs) (analyticOrderAt_riemannZeta_ne_top hs)
  refine MeromorphicAt.iff_eventuallyEq_zpow_smul_analyticAt.mpr ?_
  refine ⟨-1,
    fun z => (analyticOrderNatAt riemannZeta s : ℂ) + (z - s) * h z,
    by fun_prop, ?_⟩
  filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
  have hz0 : z - s ≠ 0 := sub_ne_zero.mpr hzne
  rw [hz, zpow_neg_one, smul_eq_mul]
  field_simp [hz0]

/-- Carrier for a later strip-rectangle contour: `ζ'/ζ` is meromorphic
on `ℂ \ {1}`. -/
lemma meromorphicOn_logDeriv_riemannZeta_compl_one :
    MeromorphicOn (logDeriv riemannZeta) ({1}ᶜ) :=
  fun _s hs => meromorphicAt_logDeriv_riemannZeta hs

/-- At a genuine non-polar zero the meromorphic order of `ζ'/ζ` is
exactly `-1` (simple pole). -/
lemma meromorphicOrderAt_logDeriv_riemannZeta {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1) :
    meromorphicOrderAt (logDeriv riemannZeta) s = (-1 : ℤ) := by
  have hm : 0 < riemannZetaMultiplicity s :=
    riemannZetaMultiplicity_pos hz hs
  obtain ⟨h, hh, heq⟩ :=
    logDeriv_riemannZeta_eq_multiplicity_div_add_analytic hz hs
  set G : ℂ → ℂ :=
    fun z => (riemannZetaMultiplicity s : ℂ) + (z - s) * h z
  have hGan : AnalyticAt ℂ G s := by fun_prop
  have hGne : G s ≠ 0 := by
    simp [G]
    exact_mod_cast hm.ne'
  have hfmer : MeromorphicAt (logDeriv riemannZeta) s :=
    meromorphicAt_logDeriv_riemannZeta hs
  rw [meromorphicOrderAt_eq_int_iff hfmer]
  refine ⟨G, hGan, hGne, ?_⟩
  filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
  have hz0 : z - s ≠ 0 := sub_ne_zero.mpr hzne
  rw [hz, zpow_neg_one, smul_eq_mul]
  field_simp [hz0]
  rfl

/-- Residue form of lemma (1): `(z-s)·ζ'/ζ → m` at a non-polar zero. -/
lemma tendsto_mul_logDeriv_riemannZeta {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1) :
    Tendsto (fun z => (z - s) * logDeriv riemannZeta z)
      (𝓝[≠] s) (𝓝 (riemannZetaMultiplicity s : ℂ)) := by
  obtain ⟨h, hh, heq⟩ :=
    logDeriv_riemannZeta_eq_multiplicity_div_add_analytic hz hs
  set G : ℂ → ℂ :=
    fun z => (riemannZetaMultiplicity s : ℂ) + (z - s) * h z
  have hagree :
      (fun z => (z - s) * logDeriv riemannZeta z) =ᶠ[𝓝[≠] s] G := by
    filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
    have hz0 : z - s ≠ 0 := sub_ne_zero.mpr hzne
    rw [hz]
    field_simp [hz0]
    rfl
  have hcont : ContinuousAt G s := by
    unfold G
    exact continuousAt_const.add
      ((continuousAt_id.sub continuousAt_const).mul hh.continuousAt)
  have hGs : G s = (riemannZetaMultiplicity s : ℂ) := by simp [G]
  rw [← hGs]
  exact Tendsto.congr' (EventuallyEq.symm hagree)
    (hcont.tendsto.mono_left nhdsWithin_le_nhds)

end LogDerivZeta

/-! ### r500: holomorphic part of `ζ'/ζ` at the pole `s = 1` ([2b] remainder)

Mathlib v4.29.1 has no `riemannZeta = 1/(s-1) + holomorphic` lemma.
It supplies `riemannZeta_residue_one` (`(s-1)ζ(s) → 1`) and
`differentiableAt_hurwitzZetaEven_sub_one_div` (`ζ - 1/((s-1)Γ_ℝ)`
differentiable at 1).  The logDeriv-convenient form is the removable
singularity of `(s-1)ζ(s)`: fill in the value `1` at `s = 1`.  Then
`ζ = g/(s-1)` with `g(1) = 1 ≠ 0`, so
`ζ'/ζ = -1/(s-1) + g'/g`.  This completes [2b]: `ζ'/ζ` is meromorphic
on all of `ℂ`.
-/

section LogDerivZetaPole

open Filter Function Set

open scoped Topology Asymptotics

/-- Holomorphic filling of `(s-1)ζ(s)` at the pole (value `1`). -/
noncomputable def riemannZetaMulSubOne : ℂ → ℂ :=
  update (fun s => (s - 1) * riemannZeta s) 1 1

lemma riemannZetaMulSubOne_apply_of_ne {s : ℂ} (hs : s ≠ 1) :
    riemannZetaMulSubOne s = (s - 1) * riemannZeta s :=
  update_of_ne hs _ _

lemma riemannZetaMulSubOne_one : riemannZetaMulSubOne 1 = 1 :=
  update_self ..

/-- Off the pole, the filling agrees with `(s-1)ζ(s)` on a
neighbourhood, so it is analytic wherever `ζ` is. -/
lemma riemannZetaMulSubOne_eq_mul {s : ℂ} (hs : s ≠ 1) :
    riemannZetaMulSubOne =ᶠ[𝓝 s] fun z => (z - 1) * riemannZeta z := by
  have hU : ({1}ᶜ : Set ℂ) ∈ 𝓝 s := isOpen_compl_singleton.mem_nhds hs
  filter_upwards [hU] with z hz
  exact riemannZetaMulSubOne_apply_of_ne hz

lemma analyticAt_riemannZetaMulSubOne (s : ℂ) :
    AnalyticAt ℂ riemannZetaMulSubOne s := by
  rcases eq_or_ne s 1 with rfl | hs
  · refine Complex.analyticAt_of_differentiable_on_punctured_nhds_of_continuousAt
      ?_ (continuousAt_update_same.mpr riemannZeta_residue_one)
    filter_upwards [self_mem_nhdsWithin] with z hz
    exact ((differentiableAt_id.sub (differentiableAt_const 1)).mul
      (differentiableAt_riemannZeta hz)).congr_of_eventuallyEq
      (riemannZetaMulSubOne_eq_mul hz)
  · exact ((analyticAt_id.sub analyticAt_const).mul
      (analyticAt_riemannZeta hs)).congr
      (riemannZetaMulSubOne_eq_mul hs).symm

/-- **r500 brick [2b], lemma (1).**  `(s-1)ζ(s)` extends to an entire
function with value `1` at `s = 1`. -/
lemma analyticOnNhd_riemannZetaMulSubOne :
    AnalyticOnNhd ℂ riemannZetaMulSubOne univ :=
  fun s _ => analyticAt_riemannZetaMulSubOne s

lemma riemannZetaMulSubOne_one_ne_zero : riemannZetaMulSubOne 1 ≠ 0 := by
  rw [riemannZetaMulSubOne_one]
  norm_num

/-- On a punctured neighbourhood of `1`, `ζ(s) = 1/(s-1) + H(s)` with
`H` analytic at `1`. -/
lemma exists_analytic_riemannZeta_eq_one_div_add :
    ∃ H : ℂ → ℂ, AnalyticAt ℂ H 1 ∧
      ∀ᶠ z in 𝓝[≠] 1, riemannZeta z = 1 / (z - 1) + H z := by
  have hds : AnalyticAt ℂ (dslope riemannZetaMulSubOne 1) 1 := by
    have hdiff : DifferentiableOn ℂ riemannZetaMulSubOne univ :=
      fun s _ => (analyticAt_riemannZetaMulSubOne s).differentiableAt.differentiableWithinAt
    have hdslope : DifferentiableOn ℂ (dslope riemannZetaMulSubOne 1) univ :=
      (Complex.differentiableOn_dslope (s := univ) univ_mem).mpr hdiff
    exact (hdslope.analyticOnNhd isOpen_univ) 1 (mem_univ _)
  refine ⟨dslope riemannZetaMulSubOne 1, hds, ?_⟩
  filter_upwards [self_mem_nhdsWithin] with z hz
  have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hz
  have hne : z ≠ 1 := hz
  rw [dslope_of_ne riemannZetaMulSubOne hne]
  have hslope :
      slope riemannZetaMulSubOne 1 z =
        (z - 1)⁻¹ * (riemannZetaMulSubOne z - riemannZetaMulSubOne 1) := rfl
  rw [hslope, riemannZetaMulSubOne_apply_of_ne hne, riemannZetaMulSubOne_one]
  field_simp [hz0]
  ring

/-- **r500 brick [2b], lemma (2).**  At the pole,
`ζ'/ζ = -1/(s-1) + analytic`. -/
lemma logDeriv_riemannZeta_eq_neg_one_div_add_analytic :
    ∃ h : ℂ → ℂ, AnalyticAt ℂ h 1 ∧
      ∀ᶠ z in 𝓝[≠] 1,
        logDeriv riemannZeta z = -1 / (z - 1) + h z := by
  have hg : AnalyticAt ℂ riemannZetaMulSubOne 1 :=
    analyticAt_riemannZetaMulSubOne 1
  have hg0 : riemannZetaMulSubOne 1 ≠ 0 :=
    riemannZetaMulSubOne_one_ne_zero
  have hg_log : AnalyticAt ℂ (logDeriv riemannZetaMulSubOne) 1 :=
    (hg.deriv).div hg hg0
  refine ⟨logDeriv riemannZetaMulSubOne, hg_log, ?_⟩
  have hg_nz : ∀ᶠ z in 𝓝 1, riemannZetaMulSubOne z ≠ 0 :=
    hg.continuousAt.preimage_mem_nhds (isOpen_compl_singleton.mem_nhds hg0)
  obtain ⟨r, hr, hball⟩ := hg.exists_ball_analyticOnNhd
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hg_nz, Metric.ball_mem_nhds (1 : ℂ) hr] with z hgz hzball hzne
  have hz : z ≠ 1 := hzne
  have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hz
  have hf_eq :
      riemannZeta =ᶠ[𝓝 z] fun w => riemannZetaMulSubOne w / (w - 1) := by
    have hopen : ({1}ᶜ : Set ℂ) ∈ 𝓝 z := isOpen_compl_singleton.mem_nhds hz
    filter_upwards [hopen] with w hw
    have hw0 : w - 1 ≠ 0 := sub_ne_zero.mpr hw
    rw [riemannZetaMulSubOne_apply_of_ne hw]
    field_simp [hw0]
  have hlog :
      logDeriv riemannZeta z =
        logDeriv (fun w => riemannZetaMulSubOne w / (w - 1)) z := by
    simp [logDeriv_apply, hf_eq.deriv_eq, hf_eq.eq_of_nhds]
  have hdg : DifferentiableAt ℂ riemannZetaMulSubOne z :=
    (hball z hzball).differentiableAt
  have hdd : DifferentiableAt ℂ (fun w : ℂ => w - 1) z := by fun_prop
  have hlin :
      (fun w : ℂ => w - 1) = fun w => (w - 1) ^ 1 := by
    ext w; rw [pow_one]
  rw [hlog, logDeriv_div z hgz hz0 hdg hdd, hlin,
    logDeriv_sub_const_pow 1 1 z]
  ring

/-- Residue of `ζ'/ζ` at the pole is `-1`. -/
lemma tendsto_mul_logDeriv_riemannZeta_one :
    Tendsto (fun z => (z - 1) * logDeriv riemannZeta z) (𝓝[≠] 1) (𝓝 (-1)) := by
  obtain ⟨h, hh, heq⟩ := logDeriv_riemannZeta_eq_neg_one_div_add_analytic
  set G : ℂ → ℂ := fun z => (-1 : ℂ) + (z - 1) * h z
  have hagree :
      (fun z => (z - 1) * logDeriv riemannZeta z) =ᶠ[𝓝[≠] 1] G := by
    filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
    have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hzne
    rw [hz]
    field_simp [hz0]
    rfl
  have hGs : G 1 = (-1 : ℂ) := by simp [G]
  have hcont : ContinuousAt G 1 := by
    unfold G
    exact continuousAt_const.add
      ((continuousAt_id.sub continuousAt_const).mul hh.continuousAt)
  rw [← hGs]
  exact Tendsto.congr' (EventuallyEq.symm hagree)
    (hcont.tendsto.mono_left nhdsWithin_le_nhds)

/-- `ζ'/ζ` is meromorphic at the pole. -/
lemma meromorphicAt_logDeriv_riemannZeta_one :
    MeromorphicAt (logDeriv riemannZeta) 1 := by
  obtain ⟨h, hh, heq⟩ := logDeriv_riemannZeta_eq_neg_one_div_add_analytic
  refine MeromorphicAt.iff_eventuallyEq_zpow_smul_analyticAt.mpr ?_
  refine ⟨-1, fun z => (-1 : ℂ) + (z - 1) * h z, by fun_prop, ?_⟩
  filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
  have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hzne
  rw [hz, zpow_neg_one, smul_eq_mul]
  field_simp [hz0]

/-- Simple pole of `ζ'/ζ` at `s = 1`. -/
lemma meromorphicOrderAt_logDeriv_riemannZeta_one :
    meromorphicOrderAt (logDeriv riemannZeta) 1 = (-1 : ℤ) := by
  obtain ⟨h, hh, heq⟩ := logDeriv_riemannZeta_eq_neg_one_div_add_analytic
  set G : ℂ → ℂ := fun z => (-1 : ℂ) + (z - 1) * h z
  have hGan : AnalyticAt ℂ G 1 := by fun_prop
  have hGne : G 1 ≠ 0 := by simp [G]
  have hfmer : MeromorphicAt (logDeriv riemannZeta) 1 :=
    meromorphicAt_logDeriv_riemannZeta_one
  rw [meromorphicOrderAt_eq_int_iff hfmer]
  refine ⟨G, hGan, hGne, ?_⟩
  filter_upwards [heq, self_mem_nhdsWithin] with z hz hzne
  have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hzne
  rw [hz, zpow_neg_one, smul_eq_mul]
  field_simp [hz0]
  rfl

/-- **r500 brick [2b], lemma (3).**  `ζ'/ζ` is meromorphic on all of
`ℂ` (zeros: r498; pole: this cut). -/
lemma meromorphicAt_logDeriv_riemannZeta_univ (s : ℂ) :
    MeromorphicAt (logDeriv riemannZeta) s := by
  rcases eq_or_ne s 1 with rfl | hs
  · exact meromorphicAt_logDeriv_riemannZeta_one
  · exact meromorphicAt_logDeriv_riemannZeta hs

lemma meromorphicOn_logDeriv_riemannZeta :
    MeromorphicOn (logDeriv riemannZeta) univ :=
  fun s _ => meromorphicAt_logDeriv_riemannZeta_univ s

end LogDerivZetaPole

/-! ### r499: local finiteness of `ζ`-zeros (bridge [2c], first cut)

The identity theorem ([2a]) isolates zeros on `ℂ \ {1}`.  Combined
with Mathlib's `codiscreteWithin` / locally-finite complement, every
compact `K ⊆ ℂ \ {1}` meets the zero set finitely often.  The residue
at `s = 1` excludes zeros from a punctured neighbourhood of the pole,
so the same finiteness holds on every compact in `ℂ` (a closed strip
rectangle may contain `1`).  A residue sum of `ζ'/ζ` over such a
rectangle is therefore a finite sum, using the r498 residue lemma.
The absolute-convergence half of [2c] is not in this cut.
-/

section ZetaZeroFiniteness

open Filter Set

open scoped Topology

/-- Isolation: away from the pole, `ζ` is not identically zero, so it
is non-vanishing on a punctured neighbourhood. -/
lemma riemannZeta_eventually_ne_zero_punctured {s : ℂ} (hs : s ≠ 1) :
    ∀ᶠ z in 𝓝[≠] s, riemannZeta z ≠ 0 :=
  (analyticAt_riemannZeta hs).eventually_eq_zero_or_eventually_ne_zero.resolve_left
    fun h => analyticOrderAt_riemannZeta_ne_top hs (analyticOrderAt_eq_top.mpr h)

/-- The residue ` (s-1)ζ(s) → 1 ` forbids zeros in a punctured
neighbourhood of the pole. -/
lemma riemannZeta_eventually_ne_zero_nhdsNE_one :
    ∀ᶠ s in 𝓝[≠] 1, riemannZeta s ≠ 0 := by
  have h := riemannZeta_residue_one.eventually
    (isOpen_compl_singleton.mem_nhds (by norm_num : (1 : ℂ) ≠ 0))
  filter_upwards [h] with s hs
  exact right_ne_zero_of_mul hs

/-- Non-polar zeros of `ζ` are a discrete subset of `ℂ`. -/
lemma isDiscrete_riemannZeta_zeros_compl_one :
    IsDiscrete (riemannZeta ⁻¹' {0} ∩ ({1}ᶜ : Set ℂ)) :=
  isDiscrete_of_codiscreteWithin (s := riemannZeta ⁻¹' {0})
    (analyticOnNhd_riemannZeta_compl_one.preimage_zero_mem_codiscreteWithin
      (by
        rw [riemannZeta_zero]
        norm_num)
      (by norm_num : (0 : ℂ) ≠ 1) isConnected_compl_one)

/-- Local finiteness on `ℂ \ {1}`: every point has a neighbourhood
meeting only finitely many zeros. -/
lemma riemannZeta_zeros_locallyFinite_compl_one :
    ∀ z ∈ ({1}ᶜ : Set ℂ), ∃ t ∈ 𝓝 z,
      (t ∩ {w : ℂ | w ≠ 1 ∧ riemannZeta w = 0}).Finite := by
  have hcod :
      riemannZeta ⁻¹' {0}ᶜ ∈ codiscreteWithin ({1}ᶜ : Set ℂ) :=
    analyticOnNhd_riemannZeta_compl_one.preimage_zero_mem_codiscreteWithin
      (by
        rw [riemannZeta_zero]
        norm_num)
      (by norm_num : (0 : ℂ) ≠ 1) isConnected_compl_one
  rw [codiscreteWithin_iff_locallyFiniteComplementWithin] at hcod
  intro z hz
  obtain ⟨t, ht, hfin⟩ := hcod z hz
  refine ⟨t, ht, hfin.subset fun w hw => ?_⟩
  simp only [mem_inter_iff, mem_diff, mem_preimage, mem_compl_iff,
    mem_singleton_iff, mem_setOf_eq] at hw ⊢
  exact ⟨hw.1, hw.2.1, not_not.mpr hw.2.2⟩

/-- **r499 brick [2c], lemma (1).**  On every compact `K ⊆ ℂ \ {1}`
the zero set of `ζ` is finite. -/
lemma finite_riemannZeta_zeros_of_isCompact {K : Set ℂ}
    (hK : IsCompact K) (hK1 : K ⊆ ({1}ᶜ : Set ℂ)) :
    {z ∈ K | riemannZeta z = 0}.Finite := by
  choose! t ht_nhds ht_fin using fun z (hz : z ∈ K) =>
    riemannZeta_zeros_locallyFinite_compl_one z (hK1 hz)
  obtain ⟨F, hFmem, hFcov⟩ := hK.elim_nhds_subcover t (fun z hz => ht_nhds z hz)
  have hunion :
      {z ∈ K | riemannZeta z = 0} ⊆
        ⋃ z ∈ F, t z ∩ {w : ℂ | w ≠ 1 ∧ riemannZeta w = 0} := by
    intro w hw
    obtain ⟨z, hzF, hwt⟩ := mem_iUnion₂.mp (hFcov hw.1)
    exact mem_iUnion₂.mpr ⟨z, hzF, hwt, hK1 hw.1, hw.2⟩
  exact ((F.finite_toSet).biUnion fun z hz =>
    ht_fin z (hFmem z (Finset.mem_coe.mp hz))).subset hunion

/-- The same finiteness on every compact in `ℂ`: zeros cannot
accumulate at the pole. -/
lemma finite_riemannZeta_zeros_of_isCompact_ne_one {K : Set ℂ}
    (hK : IsCompact K) :
    {z ∈ K | riemannZeta z = 0 ∧ z ≠ 1}.Finite := by
  have hnear := riemannZeta_eventually_ne_zero_nhdsNE_one
  rw [eventually_nhdsWithin_iff, eventually_nhds_iff] at hnear
  obtain ⟨U, hU, hUopen, h1U⟩ := hnear
  have hKc : IsCompact (K \ U) := hK.diff hUopen
  have hK1 : K \ U ⊆ ({1}ᶜ : Set ℂ) := by
    intro z hz h1
    exact hz.2 (h1 ▸ h1U)
  have hfin := finite_riemannZeta_zeros_of_isCompact hKc hK1
  refine hfin.subset ?_
  intro z hz
  refine ⟨⟨hz.1, fun hzU => ?_⟩, hz.2.1⟩
  exact hU z hzU hz.2.2 hz.2.1

/-- Closed strip rectangle `[σ₁, σ₂] × [-T, T]`. -/
def zetaClosedRect (σ₁ σ₂ T : ℝ) : Set ℂ :=
  Icc σ₁ σ₂ ×ℂ Icc (-T) T

lemma isCompact_zetaClosedRect (σ₁ σ₂ T : ℝ) :
    IsCompact (zetaClosedRect σ₁ σ₂ T) :=
  isCompact_Icc.reProdIm isCompact_Icc

/-- **r499 brick [2c], lemma (2).**  Only finitely many zeros of `ζ`
lie in a closed strip rectangle (the [2d] contour support). -/
lemma finite_riemannZeta_zeros_on_closedRect (σ₁ σ₂ T : ℝ) :
    {z ∈ zetaClosedRect σ₁ σ₂ T | riemannZeta z = 0 ∧ z ≠ 1}.Finite :=
  finite_riemannZeta_zeros_of_isCompact_ne_one (isCompact_zetaClosedRect σ₁ σ₂ T)

/-- [2c] cut 2 interface: the r499 finite-zero witness as a
`Finset`.  No convergence claim. -/
noncomputable def riemannZetaZerosOnClosedRect (σ₁ σ₂ T : ℝ) : Finset ℂ :=
  (finite_riemannZeta_zeros_on_closedRect σ₁ σ₂ T).toFinset

lemma mem_riemannZetaZerosOnClosedRect {σ₁ σ₂ T : ℝ} {z : ℂ} :
    z ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T ↔
      z ∈ zetaClosedRect σ₁ σ₂ T ∧ riemannZeta z = 0 ∧ z ≠ 1 :=
  Set.Finite.mem_toFinset _

/-- Indexed spectral partial sum on a closed rectangle.
Interface only: no `T → ∞` or absolute-convergence claim. -/
noncomputable def spectralPartialSum (F : ℂ → ℂ) (σ₁ σ₂ T : ℝ) : ℂ :=
  (riemannZetaZerosOnClosedRect σ₁ σ₂ T).sum fun ρ =>
    (riemannZetaMultiplicity ρ : ℂ) * F ρ

end ZetaZeroFiniteness

/-! ### r501: spectral kernel growth of a `FullWeilTest` ([2c] analysis)

The test `g = toFun` is even, continuous, supported in `[-R,R]`, and
an autocorrelation of a Lipschitz compactly-supported witness `h`.
Mathlib's Fourier-convolution identity is Schwartz-only, so
Bochner `ĝ = |ĥ|²` is not in this class without approximation; it
is not needed for absolute convergence.

This cut defines the spectral kernel and proves the compact-support
exponential-type envelope.  Lipschitz of `g` classically gives a
first-difference `1/t` strip bound; Lipschitz of the witness `h`
classically gives an autocorrelation second difference `O(δ²)` and
hence `1/t²`.  Those decay lemmas are the next cut.
-/

section WeilHatGrowth

open MeasureTheory Complex Filter Set Function

open scoped Topology

/-- Two-sided Laplace transform of the even compactly-supported
Weil test.  Spectral kernel for [2c] cut 3. -/
noncomputable def FullWeilTest.hat (F : FullWeilTest) (s : ℂ) : ℂ :=
  ∫ t : ℝ, (F.toFun t : ℂ) * exp (s * t)

lemma FullWeilTest.support_subset_Icc (F : FullWeilTest) :
    support F.toFun ⊆ Icc (-F.supportRadius) F.supportRadius := by
  intro t ht
  exact abs_le.mp (le_of_not_gt fun h =>
    (mem_support.mp ht) (F.support_toFun t h))

lemma FullWeilTest.hasCompactSupport_toFun (F : FullWeilTest) :
    HasCompactSupport F.toFun :=
  HasCompactSupport.of_support_subset_isCompact isCompact_Icc
    F.support_subset_Icc

lemma FullWeilTest.abs_toFun_le (F : FullWeilTest) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ t : ℝ, |F.toFun t| ≤ M := by
  obtain ⟨K, hK⟩ := F.lipschitz_toFun
  set R := F.supportRadius
  have hR : 0 ≤ R := F.supportRadius_nonneg
  refine ⟨(K : ℝ) * (2 * R + 1), by positivity, fun t => ?_⟩
  by_cases ht : R < |t|
  · rw [F.support_toFun t ht, abs_zero]
    positivity
  · have hz : F.toFun (R + 1) = 0 :=
      F.support_toFun _ (by
        rw [abs_of_nonneg (add_nonneg hR (by positivity : (0 : ℝ) ≤ 1))]
        exact lt_add_of_pos_right _ (by positivity))
    have hdist := hK.dist_le_mul t (R + 1)
    rw [Real.dist_eq, Real.dist_eq, hz, sub_zero] at hdist
    have hlen : |t - (R + 1)| ≤ 2 * R + 1 := by
      have htri := abs_sub_le t 0 (R + 1)
      have htR : |t| ≤ R := le_of_not_gt ht
      have hRp : |0 - (R + 1)| = R + 1 := by
        rw [zero_sub, abs_neg, abs_of_nonneg (add_nonneg hR (by positivity))]
      rw [sub_zero] at htri
      linarith
    exact le_trans hdist (mul_le_mul_of_nonneg_left hlen (NNReal.coe_nonneg _))

lemma FullWeilTest.not_mem_Icc_radius {F : FullWeilTest} {t : ℝ}
    (ht : t ∉ Icc (-(F.supportRadius + 1)) (F.supportRadius + 1)) :
    F.supportRadius < |t| := by
  have hI : ¬ (-(F.supportRadius + 1) ≤ t ∧ t ≤ F.supportRadius + 1) :=
    mt mem_Icc.mpr ht
  rw [not_and_or] at hI
  rcases hI with hlt | hgt
  · have htneg : t < 0 :=
      lt_of_not_ge (fun h0 => hlt (le_trans (neg_nonpos.mpr
        (add_nonneg F.supportRadius_nonneg (by positivity : (0 : ℝ) ≤ 1))) h0))
    rw [abs_of_neg htneg]
    linarith [F.supportRadius_nonneg]
  · have htpos : 0 < t :=
      lt_of_not_ge (fun h0 => hgt (le_trans h0
        (add_nonneg F.supportRadius_nonneg (by positivity : (0 : ℝ) ≤ 1))))
    rw [abs_of_pos htpos]
    linarith [F.supportRadius_nonneg]

lemma FullWeilTest.hat_eq_setIntegral (F : FullWeilTest) (s : ℂ) :
    F.hat s =
      ∫ t in Icc (-(F.supportRadius + 1)) (F.supportRadius + 1),
        (F.toFun t : ℂ) * exp (s * t) := by
  have h0 : ∀ t : ℝ, t ∉ Icc (-(F.supportRadius + 1)) (F.supportRadius + 1) →
      (F.toFun t : ℂ) * exp (s * t) = 0 := by
    intro t ht
    rw [F.support_toFun t (F.not_mem_Icc_radius ht), ofReal_zero, zero_mul]
  exact (setIntegral_eq_integral_of_forall_compl_eq_zero h0).symm

lemma FullWeilTest.integrable_hat_integrand (F : FullWeilTest) (s : ℂ) :
    Integrable (fun t : ℝ => (F.toFun t : ℂ) * exp (s * t)) := by
  have hc : Continuous fun t : ℝ => (F.toFun t : ℂ) * exp (s * t) :=
    (continuous_ofReal.comp F.continuous_toFun).mul
      (continuous_exp.comp (continuous_const.mul continuous_ofReal))
  have hsupp :
      HasCompactSupport fun t : ℝ => (F.toFun t : ℂ) * exp (s * t) :=
    HasCompactSupport.of_support_subset_isCompact isCompact_Icc
      (fun t ht => F.support_subset_Icc (by
        refine mem_support.mpr ?_
        intro hg
        have : (F.toFun t : ℂ) * exp (s * t) = 0 := by simp [hg]
        exact (mem_support.mp ht) this))
  exact hc.integrable_of_hasCompactSupport hsupp

/-- Crude Paley--Wiener envelope (exponential type `R+1`). -/
lemma FullWeilTest.norm_hat_le_exp (F : FullWeilTest) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s : ℂ,
      ‖F.hat s‖ ≤ C * Real.exp ((F.supportRadius + 1) * |s.re|) := by
  obtain ⟨M, hM0, hM⟩ := F.abs_toFun_le
  set R := F.supportRadius
  have hR : 0 ≤ R := F.supportRadius_nonneg
  refine ⟨M * (2 * R + 2), by nlinarith, fun s => ?_⟩
  have hpt : ∀ t ∈ Icc (-(R + 1)) (R + 1),
      ‖(F.toFun t : ℂ) * exp (s * t)‖ ≤
        M * Real.exp ((R + 1) * |s.re|) := by
    intro t ht
    rw [norm_mul, norm_exp, norm_real]
    have hre : (s * (t : ℂ)).re = s.re * t := by simp
    rw [hre]
    have hexp : Real.exp (s.re * t) ≤ Real.exp ((R + 1) * |s.re|) := by
      apply Real.exp_le_exp.mpr
      have htabs : |t| ≤ R + 1 := abs_le.mpr ⟨ht.1, ht.2⟩
      calc s.re * t ≤ |s.re * t| := le_abs_self _
        _ = |s.re| * |t| := abs_mul _ _
        _ ≤ |s.re| * (R + 1) :=
          mul_le_mul_of_nonneg_left htabs (abs_nonneg _)
        _ = (R + 1) * |s.re| := mul_comm _ _
    exact mul_le_mul (hM t) hexp (Real.exp_nonneg _) hM0
  have hμ : volume (Icc (-(R + 1)) (R + 1)) < ⊤ :=
    isCompact_Icc.measure_lt_top
  have hvol : volume.real (Icc (-(R + 1)) (R + 1)) = 2 * R + 2 := by
    have hle : -(R + 1) ≤ R + 1 := by linarith
    rw [Measure.real, Real.volume_Icc, sub_neg_eq_add, ENNReal.toReal_ofReal (by linarith)]
    ring
  rw [F.hat_eq_setIntegral s]
  refine (norm_setIntegral_le_of_norm_le_const (μ := volume) hμ hpt).trans ?_
  rw [hvol]
  ring_nf
  rfl

/-- Pair `h(·+α) h(·+β)` is integrable: continuous, compact support. -/
lemma autocorrelation_pair_integrable
    {h : ℝ → ℝ} (hc : Continuous h) (hs : HasCompactSupport h) (α β : ℝ) :
    Integrable fun t : ℝ => h (t + α) * h (t + β) :=
  ((hc.comp (continuous_add_const α)).mul
    (hc.comp (continuous_add_const β))).integrable_of_hasCompactSupport
    ((hs.comp_homeomorph (Homeomorph.addRight α)).mul_right
      (f' := fun t => h (t + β)))

/-- Translation invariance of the autocorrelation integral. -/
lemma autocorrelation_integral_shift
    {h : ℝ → ℝ} (_hc : Continuous h) (_hs : HasCompactSupport h) (w ε : ℝ) :
    ∫ t : ℝ, h (t + (-ε)) * h (t + (-ε) + w) = ∫ t : ℝ, h t * h (t + w) :=
  integral_add_right_eq_self (fun t : ℝ => h t * h (t + w)) (-ε)

/-- Second difference of an autocorrelation:
`Δ²_δ I(u) = -∫ (h-τ_δ h)(τ_{u-δ}h - τ_{u-2δ}h)`. -/
lemma autocorrelation_second_diff_eq
    {h : ℝ → ℝ} (hc : Continuous h) (hs : HasCompactSupport h)
    (u δ : ℝ) :
    (∫ t : ℝ, h t * h (t + u))
        - 2 * (∫ t : ℝ, h t * h (t + (u - δ)))
        + (∫ t : ℝ, h t * h (t + (u - 2 * δ)))
      = -∫ t : ℝ,
          (h t - h (t + (-δ))) *
            (h (t + (u - δ)) - h (t + (u - 2 * δ))) := by
  have I : ∀ α β : ℝ, Integrable fun t : ℝ => h (t + α) * h (t + β) :=
    fun α β => autocorrelation_pair_integrable hc hs α β
  have hA : Integrable fun t : ℝ => h t * h (t + (u - δ)) := by
    simpa using I 0 (u - δ)
  have hB : Integrable fun t : ℝ => h t * h (t + (u - 2 * δ)) := by
    simpa using I 0 (u - 2 * δ)
  have hC : Integrable fun t : ℝ => h (t + (-δ)) * h (t + (u - δ)) :=
    I (-δ) (u - δ)
  have hD : Integrable fun t : ℝ => h (t + (-δ)) * h (t + (u - 2 * δ)) :=
    I (-δ) (u - 2 * δ)
  set f1 : ℝ → ℝ := fun t => h t * h (t + (u - δ))
  set f2 : ℝ → ℝ := fun t => h t * h (t + (u - 2 * δ))
  set f3 : ℝ → ℝ := fun t => h (t + (-δ)) * h (t + (u - δ))
  set f4 : ℝ → ℝ := fun t => h (t + (-δ)) * h (t + (u - 2 * δ))
  have hφ :
      (fun t : ℝ =>
        (h t - h (t + (-δ))) * (h (t + (u - δ)) - h (t + (u - 2 * δ)))) =
        ((f1 - f2) - (f3 - f4)) := by
    ext t
    simp [f1, f2, f3, f4, Pi.sub_apply]
    ring
  have hAB : Integrable (f1 - f2) := hA.sub hB
  have hCD : Integrable (f3 - f4) := hC.sub hD
  have hshift1 :
      ∫ t : ℝ, h (t + (-δ)) * h (t + (u - δ)) =
        ∫ t : ℝ, h t * h (t + u) := by
    have hpt : ∀ t : ℝ,
        h (t + (-δ)) * h (t + (u - δ)) =
          h (t + (-δ)) * h (t + (-δ) + u) := fun t => by ring
    simp_rw [hpt]
    exact autocorrelation_integral_shift hc hs u δ
  have hshift2 :
      ∫ t : ℝ, h (t + (-δ)) * h (t + (u - 2 * δ)) =
        ∫ t : ℝ, h t * h (t + (u - δ)) := by
    have hpt : ∀ t : ℝ,
        h (t + (-δ)) * h (t + (u - 2 * δ)) =
          h (t + (-δ)) * h (t + (-δ) + (u - δ)) := fun t => by ring
    simp_rw [hpt]
    exact autocorrelation_integral_shift hc hs (u - δ) δ
  have hRHS :
      ∫ t : ℝ,
          (h t - h (t + (-δ))) *
            (h (t + (u - δ)) - h (t + (u - 2 * δ))) =
        (∫ t : ℝ, h t * h (t + (u - δ)))
          - (∫ t : ℝ, h t * h (t + (u - 2 * δ)))
          - ((∫ t : ℝ, h (t + (-δ)) * h (t + (u - δ)))
            - ∫ t : ℝ, h (t + (-δ)) * h (t + (u - 2 * δ))) := by
    rw [hφ]
    refine (integral_sub hAB hCD).trans ?_
    simp_rw [Pi.sub_apply]
    rw [integral_sub hA hB, integral_sub hC hD]
  rw [hRHS, hshift1, hshift2]
  ring

/-- **r503 brick [2c], Δ² lemma.**  Lipschitz of the witness gives
`|Δ²_δ g(u)| ≤ K² δ² (R + 2|δ|)`. -/
lemma autocorrelation_second_diff_le
    {h : ℝ → ℝ} {K : NNReal} {a R : ℝ}
    (hc : Continuous h) (hs : HasCompactSupport h)
    (hK : LipschitzWith K h)
    (hsupp : ∀ t : ℝ, t < a ∨ a + R < t → h t = 0)
    (hR : 0 ≤ R) (u δ : ℝ) :
    |(∫ t : ℝ, h t * h (t + u))
        - 2 * (∫ t : ℝ, h t * h (t + (u - δ)))
        + (∫ t : ℝ, h t * h (t + (u - 2 * δ)))|
      ≤ (K : ℝ) ^ 2 * δ ^ 2 * (R + 2 * |δ|) := by
  have heq := autocorrelation_second_diff_eq hc hs u δ
  rw [heq, abs_neg]
  set φ : ℝ → ℝ := fun t =>
    (h t - h (t + (-δ))) * (h (t + (u - δ)) - h (t + (u - 2 * δ)))
  set S := Icc (a - |δ|) (a + R + |δ|)
  have h0 : ∀ t : ℝ, t ∉ S → φ t = 0 := by
    intro t ht
    have hI : ¬ (a - |δ| ≤ t ∧ t ≤ a + R + |δ|) := mt mem_Icc.mpr ht
    rw [not_and_or] at hI
    rcases hI with hlt | hgt
    · have ht0 : t < a := by linarith [abs_nonneg δ]
      have ht1 : t + (-δ) < a := by linarith [neg_le_abs δ]
      change (h t - h (t + (-δ))) *
        (h (t + (u - δ)) - h (t + (u - 2 * δ))) = 0
      rw [hsupp t (Or.inl ht0), hsupp (t + (-δ)) (Or.inl ht1),
        sub_zero, zero_mul]
    · have ht0 : a + R < t := by linarith [abs_nonneg δ]
      have ht1 : a + R < t + (-δ) := by linarith [le_abs_self δ]
      change (h t - h (t + (-δ))) *
        (h (t + (u - δ)) - h (t + (u - 2 * δ))) = 0
      rw [hsupp t (Or.inr ht0), hsupp (t + (-δ)) (Or.inr ht1),
        sub_zero, zero_mul]
  have hIeq :
      ∫ t : ℝ, φ t = ∫ t in S, φ t :=
    (setIntegral_eq_integral_of_forall_compl_eq_zero (μ := volume) h0).symm
  have hμ : volume S < ⊤ := isCompact_Icc.measure_lt_top
  have hC : ∀ t ∈ S, ‖φ t‖ ≤ (K : ℝ) ^ 2 * δ ^ 2 := by
    intro t _ht
    change ‖(h t - h (t + (-δ))) *
      (h (t + (u - δ)) - h (t + (u - 2 * δ)))‖ ≤ _
    rw [Real.norm_eq_abs, abs_mul]
    have h1 : |h t - h (t + (-δ))| ≤ (K : ℝ) * |δ| := by
      simpa [Real.dist_eq, abs_sub_comm, sub_eq_add_neg] using
        hK.dist_le_mul t (t + (-δ))
    have h2 : |h (t + (u - δ)) - h (t + (u - 2 * δ))| ≤ (K : ℝ) * |δ| := by
      have hd := hK.dist_le_mul (t + (u - δ)) (t + (u - 2 * δ))
      rw [Real.dist_eq, Real.dist_eq] at hd
      have hlen : |(t + (u - δ)) - (t + (u - 2 * δ))| = |δ| := by
        ring_nf
      rwa [hlen] at hd
    have hmul := mul_le_mul h1 h2 (abs_nonneg _) (by positivity)
    have hsq : ((K : ℝ) * |δ|) * ((K : ℝ) * |δ|) = (K : ℝ) ^ 2 * δ ^ 2 :=
      calc (K : ℝ) * |δ| * ((K : ℝ) * |δ|)
          = (K : ℝ) ^ 2 * (|δ| ^ 2) := by ring
        _ = (K : ℝ) ^ 2 * δ ^ 2 := by rw [sq_abs]
    rwa [hsq] at hmul
  have hvol : volume.real S = R + 2 * |δ| := by
    have hle : a - |δ| ≤ a + R + |δ| := by linarith [hR, abs_nonneg δ]
    rw [Measure.real, Real.volume_Icc,
      ENNReal.toReal_ofReal (by linarith [hR, abs_nonneg δ])]
    ring
  have hle :=
    norm_setIntegral_le_of_norm_le_const (μ := volume) hμ hC
  rw [← hIeq, Real.norm_eq_abs, hvol] at hle
  exact hle

lemma FullWeilTest.abs_second_diff_le (F : FullWeilTest) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ u δ : ℝ,
      |F.toFun u - 2 * F.toFun (u - δ) + F.toFun (u - 2 * δ)| ≤
        K * δ ^ 2 * (F.supportRadius + 2 * |δ|) := by
  obtain ⟨h, _, hcs, ⟨Kh, hKh⟩, ⟨a, hsupp⟩, hac⟩ := F.autocorrelation
  refine ⟨(Kh : ℝ) ^ 2, by positivity, fun u δ => ?_⟩
  have hc : Continuous h := hKh.continuous
  have hΔ :=
    autocorrelation_second_diff_le hc hcs hKh hsupp F.supportRadius_nonneg u δ
  rw [hac u, hac (u - δ), hac (u - 2 * δ)]
  exact hΔ

lemma FullWeilTest.hat_comp_sub (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    ∫ t : ℝ, (F.toFun (t + (-δ)) : ℂ) * exp (s * t) =
      exp (s * δ) * F.hat s := by
  have hφ :
      (fun t : ℝ => (F.toFun (t + (-δ)) : ℂ) * exp (s * t)) =
        fun t =>
          (fun u : ℝ => (F.toFun u : ℂ) * exp (s * (u + δ))) (t + (-δ)) := by
    ext t
    simp
  rw [hφ, integral_add_right_eq_self
      (fun u : ℝ => (F.toFun u : ℂ) * exp (s * (u + δ))) (-δ)]
  have hmul :
      (fun u : ℝ => (F.toFun u : ℂ) * exp (s * (u + δ))) =
        fun u => exp (s * δ) • ((F.toFun u : ℂ) * exp (s * u)) := by
    ext u
    have hadd : s * ((u : ℂ) + (δ : ℂ)) = s * u + s * δ := mul_add _ _ _
    rw [hadd, exp_add, smul_eq_mul]
    ring
  rw [hmul, integral_smul]
  rfl

lemma FullWeilTest.integrable_hat_comp_sub (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    Integrable fun t : ℝ => (F.toFun (t + (-δ)) : ℂ) * exp (s * t) := by
  have hc : Continuous fun t : ℝ => (F.toFun (t + (-δ)) : ℂ) * exp (s * t) :=
    (continuous_ofReal.comp
      (F.continuous_toFun.comp (continuous_add_const (-δ)))).mul
      (continuous_exp.comp (continuous_const.mul continuous_ofReal))
  refine hc.integrable_of_hasCompactSupport ?_
  refine HasCompactSupport.of_support_subset_isCompact
      (isCompact_Icc : IsCompact
        (Icc (-(F.supportRadius + |δ| + 1)) (F.supportRadius + |δ| + 1)))
      (fun t ht => ?_)
  have hg : F.toFun (t + (-δ)) ≠ 0 := by
    intro h0
    apply mem_support.mp ht
    change (F.toFun (t + (-δ)) : ℂ) * exp (s * t) = 0
    rw [h0, ofReal_zero, zero_mul]
  have hm := F.support_subset_Icc (mem_support.mpr hg)
  constructor
  · linarith [hm.1, neg_le_abs δ, F.supportRadius_nonneg]
  · linarith [hm.2, le_abs_self δ, F.supportRadius_nonneg]

/-- Two one-step translations: no `2δ` coercion. -/
lemma FullWeilTest.hat_comp_sub_twice (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    ∫ t : ℝ, (F.toFun (t + (-δ) + (-δ)) : ℂ) * exp (s * t) =
      exp (s * δ) * exp (s * δ) * F.hat s := by
  have hφ :
      (fun t : ℝ => (F.toFun (t + (-δ) + (-δ)) : ℂ) * exp (s * t)) =
        fun t =>
          (fun u : ℝ => (F.toFun (u + (-δ)) : ℂ) * exp (s * (u + δ)))
            (t + (-δ)) := by
    ext t
    simp
  rw [hφ, integral_add_right_eq_self
      (fun u : ℝ => (F.toFun (u + (-δ)) : ℂ) * exp (s * (u + δ))) (-δ)]
  have hmul :
      (fun u : ℝ => (F.toFun (u + (-δ)) : ℂ) * exp (s * (u + δ))) =
        fun u => exp (s * δ) • ((F.toFun (u + (-δ)) : ℂ) * exp (s * u)) := by
    ext u
    have hadd : s * ((u : ℂ) + (δ : ℂ)) = s * u + s * δ := mul_add _ _ _
    rw [hadd, exp_add, smul_eq_mul]
    ring
  rw [hmul, integral_smul, F.hat_comp_sub s δ, smul_eq_mul]
  ring

lemma FullWeilTest.integrable_hat_comp_sub_twice
    (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    Integrable fun t : ℝ =>
      (F.toFun (t + (-δ) + (-δ)) : ℂ) * exp (s * t) := by
  have hpt : ∀ t : ℝ,
      F.toFun (t + (-δ) + (-δ)) = F.toFun (t + (-(2 * δ))) :=
    fun t => by ring
  simp_rw [hpt]
  exact F.integrable_hat_comp_sub s (2 * δ)

/-- Pointwise integrand equality first, then Bochner split. -/
lemma FullWeilTest.hat_mul_weierstrass (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    F.hat s * (1 - exp (s * δ)) ^ 2 =
      ∫ t : ℝ,
        ((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
          + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t) := by
  set g0 : ℝ → ℂ := fun t => (F.toFun t : ℂ) * exp (s * t)
  set gδ : ℝ → ℂ := fun t => (F.toFun (t + (-δ)) : ℂ) * exp (s * t)
  set g2 : ℝ → ℂ := fun t => (F.toFun (t + (-δ) + (-δ)) : ℂ) * exp (s * t)
  set φ : ℝ → ℂ := fun t =>
    ((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
      + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t)
  set f2 : ℝ → ℂ := fun t => (2 : ℂ) * gδ t
  have hφ : φ = (g0 - f2) + g2 := by
    ext t
    simp only [φ, g0, gδ, g2, f2, Pi.add_apply, Pi.sub_apply]
    ring
  have hI0 : Integrable g0 := F.integrable_hat_integrand s
  have hIδ : Integrable gδ := F.integrable_hat_comp_sub s δ
  have hI2 : Integrable g2 := F.integrable_hat_comp_sub_twice s δ
  have hIf2 : Integrable f2 := by
    simpa [f2] using hIδ.const_mul (2 : ℂ)
  have hsub : Integrable (g0 - f2) := hI0.sub hIf2
  change _ = ∫ t, φ t
  rw [hφ]
  simp_rw [Pi.add_apply]
  rw [integral_add hsub hI2]
  simp_rw [Pi.sub_apply]
  rw [integral_sub hI0 hIf2]
  have hf2I : ∫ t, f2 t = (2 : ℂ) * ∫ t, gδ t := by
    simp only [f2]
    exact integral_const_mul (2 : ℂ) gδ
  rw [hf2I]
  change F.hat s * (1 - exp (s * δ)) ^ 2 =
    (∫ t, g0 t) - (2 : ℂ) * (∫ t, gδ t) + ∫ t, g2 t
  simp only [g0, gδ, g2]
  have hg0 : ∫ t, (F.toFun t : ℂ) * exp (s * t) = F.hat s := rfl
  rw [hg0, F.hat_comp_sub s δ, F.hat_comp_sub_twice s δ]
  ring

/-- On the strip, `δ = π/|Im s|` sends `e^{sδ}` to `-e^{σδ}`. -/
lemma exp_mul_pi_div_abs_im {s : ℂ} (hτ : s.im ≠ 0) :
    exp (s * (Real.pi / |s.im| : ℝ)) =
      -exp (s.re * (Real.pi / |s.im|) : ℝ) := by
  set δ : ℝ := Real.pi / |s.im|
  set z : ℂ := s * (δ : ℂ)
  have hre : z.re = s.re * δ := by
    simp [z, mul_re]
  have him : z.im = s.im * δ := by
    simp [z, mul_im]
  have hexp : exp z = exp (z.re : ℂ) * exp ((z.im : ℂ) * I) := by
    conv_lhs => rw [← re_add_im z]
    exact exp_add _ _
  have himabs : exp ((z.im : ℂ) * I) = -1 := by
    rcases lt_trichotomy s.im 0 with hneg | h0 | hpos
    · have himn : z.im = -Real.pi := by
        have habs : |s.im| = -s.im := abs_of_neg hneg
        have hne : s.im ≠ 0 := ne_of_lt hneg
        have hδeq : δ = Real.pi / |s.im| := rfl
        rw [him, hδeq, habs]
        field_simp [hne]
      rw [himn, ofReal_neg, neg_mul, exp_neg, exp_pi_mul_I]
      norm_num
    · exact (hτ h0).elim
    · have himp : z.im = Real.pi := by
        have habs : |s.im| = s.im := abs_of_pos hpos
        have hne : s.im ≠ 0 := ne_of_gt hpos
        have hδeq : δ = Real.pi / |s.im| := rfl
        rw [him, hδeq, habs]
        field_simp [hne]
      rw [himp]
      exact exp_pi_mul_I
  rw [hexp, himabs]
  simp [hre]

lemma FullWeilTest.not_mem_Icc_wide {F : FullWeilTest} {t r : ℝ}
    (hr : 0 ≤ r)
    (ht : t ∉ Icc (-(F.supportRadius + r)) (F.supportRadius + r)) :
    F.supportRadius < |t| := by
  have hI : ¬ (-(F.supportRadius + r) ≤ t ∧ t ≤ F.supportRadius + r) :=
    mt mem_Icc.mpr ht
  rw [not_and_or] at hI
  rcases hI with hlt | hgt
  · have htneg : t < 0 :=
      lt_of_not_ge (fun h0 => hlt (le_trans (neg_nonpos.mpr
        (add_nonneg F.supportRadius_nonneg hr)) h0))
    rw [abs_of_neg htneg]
    linarith [F.supportRadius_nonneg]
  · have htpos : 0 < t :=
      lt_of_not_ge (fun h0 => hgt (le_trans h0
        (add_nonneg F.supportRadius_nonneg hr)))
    rw [abs_of_pos htpos]
    linarith [F.supportRadius_nonneg]

lemma one_add_exp_re_pi_ge_two {s : ℂ} (hσ : 0 ≤ s.re) (hτ : s.im ≠ 0) :
    2 ≤ 1 + Real.exp (s.re * (Real.pi / |s.im|)) := by
  have hx : 0 ≤ s.re * (Real.pi / |s.im|) :=
    mul_nonneg hσ (div_nonneg Real.pi_pos.le (abs_nonneg _))
  linarith [Real.one_le_exp hx]

lemma norm_one_sub_exp_pi {s : ℂ} (hτ : s.im ≠ 0) :
    ‖(1 : ℂ) - exp (s * (Real.pi / |s.im| : ℝ))‖ =
      1 + Real.exp (s.re * (Real.pi / |s.im|)) := by
  set δ : ℝ := Real.pi / |s.im|
  have h1 : (1 : ℂ) - exp (s * (δ : ℝ)) =
      ((1 + Real.exp (s.re * δ) : ℝ) : ℂ) := by
    rw [exp_mul_pi_div_abs_im hτ, sub_neg_eq_add, ← ofReal_exp,
      ← ofReal_one, ← ofReal_add]
  rw [h1]
  rw [norm_real]
  exact abs_of_nonneg (add_nonneg (zero_le_one : (0 : ℝ) ≤ 1) (Real.exp_nonneg _))

/-- Sharp complement: `t ∉ [-R-r, R+r]` is `|t| > R+r`. -/
lemma FullWeilTest.not_mem_Icc_abs {F : FullWeilTest} {t r : ℝ}
    (ht : t ∉ Icc (-(F.supportRadius + r)) (F.supportRadius + r)) :
    F.supportRadius + r < |t| :=
  not_le.mp (mt (fun h => mem_Icc.mpr (abs_le.mp h)) ht)

/-- Real Δ² of `g` vanishes outside the wide window: each of the
three copies `g(t)`, `g(t-δ)`, `g(t-2δ)` has its own shifted
support in `[-R,R]`. -/
lemma FullWeilTest.second_diff_eq_zero_of_wide (F : FullWeilTest)
    {t δ : ℝ} (ht : F.supportRadius + 2 * |δ| < |t|) :
    F.toFun t - 2 * F.toFun (t - δ) + F.toFun (t - 2 * δ) = 0 := by
  have ht0 : F.supportRadius < |t| := by linarith [abs_nonneg δ]
  have ht1 : F.supportRadius < |t - δ| := by
    have htri : |t| ≤ |t - δ| + |δ| := by
      have : |t| = |(t - δ) + δ| := by ring
      rw [this]
      exact abs_add_le (t - δ) δ
    linarith
  have ht2 : F.supportRadius < |t - 2 * δ| := by
    have htri : |t| ≤ |t - 2 * δ| + |2 * δ| := by
      have : |t| = |(t - 2 * δ) + (2 * δ)| := by ring
      rw [this]
      exact abs_add_le (t - 2 * δ) (2 * δ)
    have habs : |2 * δ| = 2 * |δ| := by
      rw [abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ 2)]
    linarith [habs]
  rw [F.support_toFun t ht0, F.support_toFun (t - δ) ht1,
    F.support_toFun (t - 2 * δ) ht2]
  ring

/-- ofReal: the ℂ-linear combination is the coercion of the real Δ².
The `t + (-δ) + (-δ)` form is rewritten as `t - 2δ` on ℝ, then
lifted. -/
lemma FullWeilTest.ofReal_second_diff (F : FullWeilTest) (t δ : ℝ) :
    (F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
      + (F.toFun (t + (-δ) + (-δ)) : ℂ)
    = ((F.toFun t - 2 * F.toFun (t - δ)
        + F.toFun (t - 2 * δ) : ℝ) : ℂ) := by
  have h1 : t + (-δ) = t - δ := by ring
  have h2 : t + (-δ) + (-δ) = t - 2 * δ := by ring
  rw [h2, h1]
  have h2c : (2 : ℂ) = ((2 : ℝ) : ℂ) := by norm_num
  rw [h2c, ← ofReal_mul, ← ofReal_sub, ← ofReal_add]

lemma FullWeilTest.weierstrass_integrand_eq_zero_of_not_mem
    (F : FullWeilTest) (s : ℂ) {t δ : ℝ}
    (ht : t ∉ Icc (-(F.supportRadius + 2 * |δ|))
      (F.supportRadius + 2 * |δ|)) :
    ((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
      + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t) = 0 := by
  have hwide := F.not_mem_Icc_abs (r := 2 * |δ|) ht
  rw [F.ofReal_second_diff, F.second_diff_eq_zero_of_wide hwide,
    ofReal_zero, zero_mul]

lemma FullWeilTest.hat_mul_weierstrass_eq_setIntegral
    (F : FullWeilTest) (s : ℂ) (δ : ℝ) :
    F.hat s * (1 - exp (s * δ)) ^ 2 =
      ∫ t in Icc (-(F.supportRadius + 2 * |δ|))
        (F.supportRadius + 2 * |δ|),
        ((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
          + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t) := by
  rw [F.hat_mul_weierstrass s δ]
  exact (setIntegral_eq_integral_of_forall_compl_eq_zero
    (fun t ht => F.weierstrass_integrand_eq_zero_of_not_mem s ht)).symm

/-- Pointwise envelope of the Weierstrass integrand on the wide
window: `|Δ²g(t)| e^{σ t} ≤ K δ² W e^{|σ| W}`. -/
lemma FullWeilTest.norm_weierstrass_integrand_le (F : FullWeilTest)
    {K : ℝ} (hK0 : 0 ≤ K)
    (hK : ∀ u δ : ℝ,
      |F.toFun u - 2 * F.toFun (u - δ) + F.toFun (u - 2 * δ)| ≤
        K * δ ^ 2 * (F.supportRadius + 2 * |δ|))
    (s : ℂ) {t δ : ℝ}
    (ht : t ∈ Icc (-(F.supportRadius + 2 * |δ|))
      (F.supportRadius + 2 * |δ|)) :
    ‖((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
      + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t)‖ ≤
      K * δ ^ 2 * (F.supportRadius + 2 * |δ|) *
        Real.exp (|s.re| * (F.supportRadius + 2 * |δ|)) := by
  set W := F.supportRadius + 2 * |δ|
  have hW : 0 ≤ W :=
    add_nonneg F.supportRadius_nonneg (by positivity)
  rw [norm_mul, F.ofReal_second_diff, norm_real, Real.norm_eq_abs,
    norm_exp]
  have hre : (s * (t : ℂ)).re = s.re * t := by simp
  rw [hre]
  have hexp : Real.exp (s.re * t) ≤ Real.exp (|s.re| * W) := by
    apply Real.exp_le_exp.mpr
    have htabs : |t| ≤ W := abs_le.mpr ⟨ht.1, ht.2⟩
    calc s.re * t ≤ |s.re * t| := le_abs_self _
      _ = |s.re| * |t| := abs_mul _ _
      _ ≤ |s.re| * W := mul_le_mul_of_nonneg_left htabs (abs_nonneg _)
  have hΔ := hK t δ
  have hC0 : 0 ≤ K * δ ^ 2 * W :=
    mul_nonneg (mul_nonneg hK0 (sq_nonneg _)) hW
  exact mul_le_mul hΔ hexp (Real.exp_nonneg _) hC0

lemma FullWeilTest.norm_hat_mul_weierstrass_le (F : FullWeilTest)
    {K : ℝ} (hK0 : 0 ≤ K)
    (hK : ∀ u δ : ℝ,
      |F.toFun u - 2 * F.toFun (u - δ) + F.toFun (u - 2 * δ)| ≤
        K * δ ^ 2 * (F.supportRadius + 2 * |δ|))
    (s : ℂ) (δ : ℝ) :
    ‖F.hat s * (1 - exp (s * δ)) ^ 2‖ ≤
      2 * K * δ ^ 2 * (F.supportRadius + 2 * |δ|) ^ 2 *
        Real.exp (|s.re| * (F.supportRadius + 2 * |δ|)) := by
  set W := F.supportRadius + 2 * |δ|
  have hW : 0 ≤ W :=
    add_nonneg F.supportRadius_nonneg (by positivity)
  have hμ : volume (Icc (-W) W) < ⊤ := isCompact_Icc.measure_lt_top
  have hvol : volume.real (Icc (-W) W) = 2 * W := by
    rw [Measure.real, Real.volume_Icc, sub_neg_eq_add,
      ENNReal.toReal_ofReal (by linarith [hW])]
    ring
  have hpt : ∀ t ∈ Icc (-W) W,
      ‖((F.toFun t : ℂ) - (2 : ℂ) * (F.toFun (t + (-δ)) : ℂ)
        + (F.toFun (t + (-δ) + (-δ)) : ℂ)) * exp (s * t)‖ ≤
        K * δ ^ 2 * W * Real.exp (|s.re| * W) :=
    fun t ht => F.norm_weierstrass_integrand_le hK0 hK s ht
  rw [F.hat_mul_weierstrass_eq_setIntegral s δ]
  have hbound :=
    norm_setIntegral_le_of_norm_le_const (μ := volume) hμ hpt
  refine hbound.trans ?_
  rw [hvol]
  ring_nf
  rfl

/-- Target 1/t² strip bound. Weierstrass identity and
`e^{sδ} = -e^{σδ}` (with `|1-e^{sδ}| ≥ 2`) are in. -/
def FullWeilTest.NormHatLeInvSq (F : FullWeilTest) : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ s : ℂ, s.re ∈ Icc (0 : ℝ) 1 →
    ‖F.hat s‖ ≤ C / (1 + s.im ^ 2)

/-- **r506, ĥ-side of [2c] complete.**  `‖hat s‖ ≤ C/(1+τ²)` on the
closed strip `0 ≤ Re s ≤ 1`.  `|τ| ≤ 1` from the Paley–Wiener
envelope; `|τ| > 1` from Weierstrass + `|1-e^{sδ}| ≥ 2` at
`δ = π/|τ|`. -/
lemma FullWeilTest.norm_hat_le_inv_sq (F : FullWeilTest) :
    F.NormHatLeInvSq := by
  unfold FullWeilTest.NormHatLeInvSq
  obtain ⟨Cexp, hCexp0, hCexp⟩ := F.norm_hat_le_exp
  obtain ⟨K, hK0, hK⟩ := F.abs_second_diff_le
  set R := F.supportRadius
  have hR : 0 ≤ R := F.supportRadius_nonneg
  set C : ℝ :=
    2 * Cexp * Real.exp (R + 1)
      + K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2
        * Real.exp (R + 2 * Real.pi)
  have hC0 : 0 ≤ C :=
    add_nonneg (by positivity) (by positivity)
  refine ⟨C, hC0, fun s hs => ?_⟩
  have hσ0 : 0 ≤ s.re := hs.1
  have hσ1 : s.re ≤ 1 := hs.2
  have hdenpos : 0 < 1 + s.im ^ 2 := by nlinarith [sq_nonneg s.im]
  by_cases hτle : |s.im| ≤ 1
  · have hexp :
        Real.exp ((R + 1) * |s.re|) ≤ Real.exp (R + 1) := by
      apply Real.exp_le_exp.mpr
      rw [abs_of_nonneg hσ0]
      nlinarith [hR, hσ1]
    have hhat : ‖F.hat s‖ ≤ Cexp * Real.exp (R + 1) :=
      (hCexp s).trans (mul_le_mul_of_nonneg_left hexp hCexp0)
    have hτsq : s.im ^ 2 ≤ 1 := by
      have : |s.im| ^ 2 ≤ (1 : ℝ) ^ 2 :=
        sq_le_sq.mpr (by simpa [abs_one] using hτle)
      rwa [sq_abs, one_pow] at this
    have hden : 1 + s.im ^ 2 ≤ 2 := by linarith
    have hprod : ‖F.hat s‖ * (1 + s.im ^ 2)
        ≤ 2 * Cexp * Real.exp (R + 1) := by
      have := mul_le_mul hhat hden (by nlinarith [sq_nonneg s.im])
        (by positivity)
      nlinarith
    have hCpart : 2 * Cexp * Real.exp (R + 1) ≤ C := by
      dsimp [C]
      exact le_add_of_nonneg_right (by positivity)
    exact (le_div_iff₀ hdenpos).mpr (hprod.trans hCpart)
  · have hτgt : 1 < |s.im| := not_le.mp hτle
    have hτne : s.im ≠ 0 := fun h0 => by
      rw [h0, abs_zero] at hτgt
      linarith
    set δ : ℝ := Real.pi / |s.im|
    have hδpos : 0 < δ :=
      div_pos Real.pi_pos (abs_pos.mpr hτne)
    have hδleπ : δ ≤ Real.pi :=
      div_le_self Real.pi_pos.le (le_of_lt hτgt)
    have hWle : R + 2 * |δ| ≤ R + 2 * Real.pi := by
      rw [abs_of_pos hδpos]
      linarith
    have hI := F.norm_hat_mul_weierstrass_le hK0 hK s δ
    have hfac :
        ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ =
          1 + Real.exp (s.re * δ) := by
      simpa [δ] using norm_one_sub_exp_pi hτne
    have hge : (2 : ℝ) ≤ ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ := by
      rw [hfac]
      simpa [δ] using one_add_exp_re_pi_ge_two hσ0 hτne
    have hpow : ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ =
        ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ ^ 2 :=
      norm_pow _ 2
    have hge4 : (4 : ℝ) ≤ ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := by
      rw [hpow]
      nlinarith [hge]
    have hmul : ‖F.hat s * ((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ =
        ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ :=
      norm_mul _ _
    have hhat4 : ‖F.hat s‖ * 4 ≤
        2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
          Real.exp (|s.re| * (R + 2 * |δ|)) := by
      have hleft : ‖F.hat s‖ * 4
          ≤ ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ :=
        mul_le_mul_of_nonneg_left hge4 (norm_nonneg _)
      calc ‖F.hat s‖ * 4
          ≤ ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := hleft
        _ = ‖F.hat s * ((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := hmul.symm
        _ ≤ _ := hI
    have hhat : ‖F.hat s‖ ≤
        (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
          Real.exp (|s.re| * (R + 2 * |δ|)) := by
      have hdiv := (le_div_iff₀ (by norm_num : (0 : ℝ) < 4)).mpr hhat4
      have hrearr :
          (2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
            Real.exp (|s.re| * (R + 2 * |δ|))) / 4
          = (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
            Real.exp (|s.re| * (R + 2 * |δ|)) := by ring
      rwa [hrearr] at hdiv
    have hexp : Real.exp (|s.re| * (R + 2 * |δ|))
        ≤ Real.exp (R + 2 * Real.pi) := by
      apply Real.exp_le_exp.mpr
      have habsσ : |s.re| ≤ 1 := by
        rwa [abs_of_nonneg hσ0]
      have : |s.re| * (R + 2 * |δ|) ≤ 1 * (R + 2 * Real.pi) :=
        mul_le_mul habsσ hWle
          (add_nonneg hR (by positivity)) (by positivity)
      linarith
    have hWsq : (R + 2 * |δ|) ^ 2 ≤ (R + 2 * Real.pi) ^ 2 :=
      pow_le_pow_left₀ (add_nonneg hR (by positivity)) hWle 2
    have hδsq : δ ^ 2 = Real.pi ^ 2 / s.im ^ 2 := by
      have hne : |s.im| ≠ 0 := abs_ne_zero.mpr hτne
      rw [div_pow, sq_abs]
    have hτsq : 1 ≤ s.im ^ 2 := by
      have h1 : (1 : ℝ) ≤ |s.im| := le_of_lt hτgt
      have : (1 : ℝ) ^ 2 ≤ |s.im| ^ 2 :=
        pow_le_pow_left₀ (by positivity) h1 2
      rwa [one_pow, sq_abs] at this
    have hcomp : 1 / s.im ^ 2 ≤ 2 / (1 + s.im ^ 2) := by
      have hpos1 : 0 < s.im ^ 2 := by nlinarith
      rw [div_le_div_iff₀ hpos1 hdenpos]
      nlinarith
    have hδbound : δ ^ 2 ≤ 2 * Real.pi ^ 2 / (1 + s.im ^ 2) := by
      rw [hδsq, div_eq_mul_inv, show 2 * Real.pi ^ 2 / (1 + s.im ^ 2) =
          Real.pi ^ 2 * (2 / (1 + s.im ^ 2)) from by ring]
      exact mul_le_mul_of_nonneg_left
        (by simpa [one_div] using hcomp) (by positivity)
    have hnnK : 0 ≤ (1 / 2 : ℝ) * K := by positivity
    have hnnδ : 0 ≤ δ ^ 2 := sq_nonneg _
    have hnnW : 0 ≤ (R + 2 * |δ|) ^ 2 := sq_nonneg _
    have hnnE : 0 ≤ Real.exp (|s.re| * (R + 2 * |δ|)) :=
      Real.exp_nonneg _
    have hstep1 : ‖F.hat s‖ ≤
        (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * Real.pi) ^ 2 *
          Real.exp (R + 2 * Real.pi) := by
      refine hhat.trans ?_
      have hmid : (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
            Real.exp (|s.re| * (R + 2 * |δ|))
          ≤ (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * Real.pi) ^ 2 *
            Real.exp (|s.re| * (R + 2 * |δ|)) :=
        mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hWsq (mul_nonneg hnnK hnnδ))
          hnnE
      refine hmid.trans ?_
      exact mul_le_mul_of_nonneg_left hexp (by positivity)
    have hnnRest : 0 ≤ (1 / 2 : ℝ) * K * (R + 2 * Real.pi) ^ 2 *
        Real.exp (R + 2 * Real.pi) := by positivity
    have hstep2 : ‖F.hat s‖ ≤
        (1 / 2 : ℝ) * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
          (R + 2 * Real.pi) ^ 2 * Real.exp (R + 2 * Real.pi) := by
      refine hstep1.trans ?_
      have hrearr1 :
          (1 / 2 : ℝ) * K * δ ^ 2 * (R + 2 * Real.pi) ^ 2 *
            Real.exp (R + 2 * Real.pi)
          = δ ^ 2 * ((1 / 2 : ℝ) * K * (R + 2 * Real.pi) ^ 2 *
            Real.exp (R + 2 * Real.pi)) := by ring
      have hrearr2 :
          (1 / 2 : ℝ) * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * Real.pi) ^ 2 * Real.exp (R + 2 * Real.pi)
          = (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            ((1 / 2 : ℝ) * K * (R + 2 * Real.pi) ^ 2 *
              Real.exp (R + 2 * Real.pi)) := by ring
      rw [hrearr1, hrearr2]
      exact mul_le_mul_of_nonneg_right hδbound hnnRest
    have hsimp :
        (1 / 2 : ℝ) * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
          (R + 2 * Real.pi) ^ 2 * Real.exp (R + 2 * Real.pi)
        = (K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2 *
            Real.exp (R + 2 * Real.pi)) / (1 + s.im ^ 2) := by
      field_simp
      try ring
    rw [hsimp] at hstep2
    have hCpart : K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2 *
        Real.exp (R + 2 * Real.pi) ≤ C := by
      dsimp [C]
      exact le_add_of_nonneg_left (by positivity)
    have hdiv : (K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2 *
          Real.exp (R + 2 * Real.pi)) / (1 + s.im ^ 2)
        ≤ C / (1 + s.im ^ 2) :=
      div_le_div_of_nonneg_right hCpart hdenpos.le
    exact hstep2.trans hdiv

end WeilHatGrowth

section ZetaHalfPlaneBounds

open Complex Set
open scoped ArithmeticFunction.Moebius LSeries.notation

lemma nat_succ_coe_complex (n : ℕ) : (n + 1 : ℂ) = ((n + 1 : ℕ) : ℂ) := by
  simp

lemma norm_one_div_nat_succ_cpow (n : ℕ) (s : ℂ) :
    ‖(1 : ℂ) / (n + 1 : ℂ) ^ s‖ = ((n + 1 : ℕ) : ℝ) ^ (-s.re) := by
  rw [nat_succ_coe_complex, norm_div, norm_one,
    norm_natCast_cpow_of_pos (Nat.succ_pos n)]
  have hn : (0 : ℝ) < n.succ := Nat.cast_pos.mpr (Nat.succ_pos n)
  rw [one_div, ← Real.rpow_neg hn.le, Nat.cast_succ]

lemma riemannZeta_two_ofReal :
    riemannZeta 2 = ((Real.pi ^ 2 / 6 : ℝ) : ℂ) := by
  rw [riemannZeta_two]
  simp [ofReal_div, ofReal_pow, ofReal_ofNat]

lemma norm_riemannZeta_two : ‖riemannZeta 2‖ = Real.pi ^ 2 / 6 := by
  rw [riemannZeta_two_ofReal]
  exact (norm_real _).trans (abs_of_nonneg (by positivity))

lemma norm_one_div_nat_succ_cpow_le_two {s : ℂ} (hs : 2 ≤ s.re) (n : ℕ) :
    ‖(1 : ℂ) / (n + 1 : ℂ) ^ s‖ ≤
      ‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ := by
  have hb : (1 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by
    exact_mod_cast (Nat.succ_le_succ (Nat.zero_le n))
  rw [norm_one_div_nat_succ_cpow, norm_one_div_nat_succ_cpow]
  have h2 : (2 : ℂ).re = (2 : ℝ) := by simp
  rw [h2]
  exact Real.rpow_le_rpow_of_exponent_le hb (neg_le_neg hs)

/-- Same summand as `zeta_eq_tsum_one_div_nat_add_one_cpow`.
The `n+1` is the ℂ-addition `(n : ℂ) + 1`, converted from the
`summable_nat_add_iff` index `(n+1 : ℕ)` by `nat_succ_coe_complex`. -/
lemma summable_one_div_nat_add_one_cpow {s : ℂ} (hs : 1 < s.re) :
    Summable fun n : ℕ => (1 : ℂ) / (n + 1 : ℂ) ^ s := by
  have h := (Complex.summable_one_div_nat_cpow (p := s)).mpr hs
  have hshift :=
    (summable_nat_add_iff
      (f := fun n : ℕ => (1 : ℂ) / (n : ℂ) ^ s) 1).mpr h
  refine (summable_congr fun n => ?_).mp hshift
  rw [nat_succ_coe_complex]

lemma one_div_nat_succ_cpow_two_eq_ofReal (n : ℕ) :
    (1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ) =
      ((((n + 1 : ℕ) : ℝ) ^ (-(2 : ℝ)) : ℝ) : ℂ) := by
  have hn : 0 ≤ ((n + 1 : ℕ) : ℝ) := Nat.cast_nonneg _
  rw [nat_succ_coe_complex, ← ofReal_natCast]
  have h2 : (2 : ℂ) = ((2 : ℝ) : ℂ) := by norm_num
  rw [h2, ← ofReal_cpow hn, ← ofReal_one, ← ofReal_div]
  congr 1
  rw [Real.rpow_neg hn, one_div]

lemma tsum_norm_one_div_nat_succ_two :
    (∑' n : ℕ, ‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖) =
      ‖∑' n : ℕ, (1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ := by
  have heq : ∀ n : ℕ, (1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ) =
      (‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ : ℂ) := fun n => by
    rw [one_div_nat_succ_cpow_two_eq_ofReal]
    rw [Complex.norm_of_nonneg (Real.rpow_nonneg (Nat.cast_nonneg _) _)]
  rw [tsum_congr heq, ← ofReal_tsum,
    Complex.norm_of_nonneg (tsum_nonneg fun _ => norm_nonneg _)]

/-- Dirichlet majorant `|ζ(s)| ≤ |ζ(2)|` on `Re s ≥ 2`. -/
def NormRiemannZetaLeZetaTwo : Prop :=
  ∀ s : ℂ, 2 ≤ s.re → ‖riemannZeta s‖ ≤ ‖riemannZeta 2‖

/-- **r506, ζ-side cut.**  `|ζ(s)| ≤ |ζ(2)|` on `Re s ≥ 2`, using
Mathlib's `zeta_eq_tsum_one_div_nat_add_one_cpow` summand shape
verbatim (no reindex). -/
lemma normRiemannZetaLeZetaTwo : NormRiemannZetaLeZetaTwo := by
  intro s hs
  have hs1 : 1 < s.re := by linarith
  have h2 : 1 < (2 : ℂ).re := by simp
  rw [zeta_eq_tsum_one_div_nat_add_one_cpow hs1,
    zeta_eq_tsum_one_div_nat_add_one_cpow h2]
  have hsum_n : Summable fun n : ℕ =>
      ‖(1 : ℂ) / (n + 1 : ℂ) ^ s‖ := by
    rw [summable_norm_iff]
    exact summable_one_div_nat_add_one_cpow hs1
  have hsum_2 : Summable fun n : ℕ =>
      ‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ := by
    rw [summable_norm_iff]
    exact summable_one_div_nat_add_one_cpow h2
  refine (norm_tsum_le_tsum_norm hsum_n).trans ?_
  refine (hsum_n.tsum_le_tsum
    (fun n => norm_one_div_nat_succ_cpow_le_two hs n) hsum_2).trans ?_
  exact (tsum_norm_one_div_nat_succ_two).le

/-- Möbius inversion on `Re s > 1`: `1/ζ(s) = L(μ, s)`. -/
lemma inv_riemannZeta_eq_LSeries_moebius {s : ℂ} (hs : 1 < s.re) :
    (riemannZeta s)⁻¹ = L ↗ArithmeticFunction.moebius s := by
  have hprod := ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius hs
  rw [ArithmeticFunction.LSeries_zeta_eq_riemannZeta hs] at hprod
  exact inv_eq_of_mul_eq_one_right hprod

lemma norm_moebius_le_one (n : ℕ) :
    ‖(ArithmeticFunction.moebius n : ℂ)‖ ≤ ‖((1 : ℕ → ℂ) n)‖ := by
  rw [Complex.norm_intCast, ← Int.cast_abs]
  simp only [Pi.one_apply, norm_one]
  exact_mod_cast ArithmeticFunction.abs_moebius_le_one (n := n)

lemma tsum_norm_term_one_two :
    (∑' n : ℕ, ‖LSeries.term (1 : ℕ → ℂ) (2 : ℂ) n‖) = ‖riemannZeta 2‖ := by
  have h2 : 1 < (2 : ℂ).re := by simp
  have hn2 : Summable fun n : ℕ => ‖LSeries.term (1 : ℕ → ℂ) (2 : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact LSeriesSummable_one_iff.mpr h2
  have hshift := Summable.tsum_eq_zero_add hn2
  have h0 : ‖LSeries.term (1 : ℕ → ℂ) (2 : ℂ) 0‖ = 0 := by
    simp [LSeries.term_zero]
  have htail :
      (∑' n : ℕ, ‖LSeries.term (1 : ℕ → ℂ) (2 : ℂ) (n + 1)‖) =
        ∑' n : ℕ, ‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ := by
    refine tsum_congr fun n => ?_
    have hn : n + 1 ≠ 0 := Nat.succ_ne_zero n
    rw [LSeries.term_of_ne_zero hn, Pi.one_apply, ← nat_succ_coe_complex]
  rw [hshift, h0, zero_add, htail, tsum_norm_one_div_nat_succ_two,
    ← zeta_eq_tsum_one_div_nat_add_one_cpow h2]

/-- Polynomial bound on a vertical strip via FE + `Gamma` growth.
Mathlib v4.29.1 has `riemannZeta_one_sub` and factorial Stirling,
but no vertical `Complex.Gamma` bound. -/
def RiemannZetaStripPolyBound : Prop :=
  ∀ σ₁ σ₂ : ℝ, σ₁ ≤ σ₂ → ∃ A B : ℝ, 0 ≤ A ∧ 0 ≤ B ∧
    ∀ s : ℂ, s.re ∈ Icc σ₁ σ₂ →
      ‖riemannZeta s‖ ≤ A * (1 + |s.im|) ^ B

/-- `|1/ζ(s)| ≤ |ζ(2)|` on `Re s ≥ 2`. -/
def NormInvRiemannZetaLeZetaTwo : Prop :=
  ∀ s : ℂ, 2 ≤ s.re → ‖(riemannZeta s)⁻¹‖ ≤ ‖riemannZeta 2‖

/-- **r506, ζ-side inverse.**  `|1/ζ(s)| ≤ |ζ(2)|` on `Re s ≥ 2` via
`|μ(n)| ≤ 1` and `LSeries.norm_term_le`. -/
lemma normInvRiemannZetaLeZetaTwo : NormInvRiemannZetaLeZetaTwo := by
  intro s hs
  have hs1 : 1 < s.re := by linarith
  have h2 : 1 < (2 : ℂ).re := by simp
  rw [inv_riemannZeta_eq_LSeries_moebius hs1]
  have hμ : LSeriesSummable ↗ArithmeticFunction.moebius s :=
    ArithmeticFunction.LSeriesSummable_moebius_iff.mpr hs1
  have h1s : LSeriesSummable (1 : ℕ → ℂ) s :=
    LSeriesSummable_one_iff.mpr hs1
  have hnμ : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.moebius s n‖ := by
    rw [summable_norm_iff]; exact hμ
  have hn1 : Summable fun n =>
      ‖LSeries.term (1 : ℕ → ℂ) s n‖ := by
    rw [summable_norm_iff]; exact h1s
  have hn2 : Summable fun n =>
      ‖LSeries.term (1 : ℕ → ℂ) (2 : ℂ) n‖ := by
    rw [summable_norm_iff]; exact LSeriesSummable_one_iff.mpr h2
  have hre : (2 : ℂ).re ≤ s.re := by simpa using hs
  refine (norm_tsum_le_tsum_norm hnμ).trans ?_
  refine (hnμ.tsum_le_tsum (fun n => LSeries.norm_term_le s (norm_moebius_le_one n))
    hn1).trans ?_
  refine (hn1.tsum_le_tsum
    (fun n => LSeries.norm_term_le_of_re_le_re (1 : ℕ → ℂ) hre n)
    hn2).trans ?_
  exact (tsum_norm_term_one_two).le

/-- `ζ'/ζ = -L(Λ)` on `Re s > 1`. -/
lemma logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt {s : ℂ}
    (hs : 1 < s.re) :
    logDeriv riemannZeta s = - L ↗ArithmeticFunction.vonMangoldt s := by
  rw [logDeriv_apply, ArithmeticFunction.LSeries_vonMangoldt_eq_deriv_riemannZeta_div hs]
  ring

lemma term_vonMangoldt_two_eq_ofReal_norm (n : ℕ) :
    LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n =
      (‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ : ℂ) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    have hden : (0 : ℝ) < (n : ℝ) ^ 2 :=
      pow_pos (Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn)) 2
    have key :
        (ArithmeticFunction.vonMangoldt n : ℂ) / (n : ℂ) ^ 2 =
          (‖(ArithmeticFunction.vonMangoldt n : ℂ) / (n : ℂ) ^ 2‖ : ℂ) := by
      rw [← ofReal_natCast, ← ofReal_pow, ← ofReal_div]
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (div_nonneg hΛ hden.le)]
    simpa [LSeries.term_of_ne_zero hn] using key

lemma tsum_norm_term_vonMangoldt_two :
    (∑' n, ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖) =
      ‖L ↗ArithmeticFunction.vonMangoldt (2 : ℂ)‖ := by
  have h2 : 1 < (2 : ℂ).re := by simp
  have hsum := ArithmeticFunction.LSeriesSummable_vonMangoldt h2
  have hn : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
    rw [summable_norm_iff]; exact hsum
  have heq := term_vonMangoldt_two_eq_ofReal_norm
  rw [LSeries, tsum_congr heq, ← ofReal_tsum,
    Complex.norm_of_nonneg (tsum_nonneg fun _ => norm_nonneg _)]

/-- On `Re s ≥ 2`, `|ζ'/ζ(s)| ≤ Σ Λ(n) n^{-2} = -ζ'(2)/ζ(2) = |ζ'/ζ(2)|`. -/
lemma norm_logDeriv_riemannZeta_le_at_two {s : ℂ} (hs : 2 ≤ s.re) :
    ‖logDeriv riemannZeta s‖ ≤ ‖logDeriv riemannZeta (2 : ℂ)‖ := by
  have hs1 : 1 < s.re := by linarith
  have h2 : 1 < (2 : ℂ).re := by simp
  rw [logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt hs1,
    logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt h2, norm_neg, norm_neg]
  have hΛs : LSeriesSummable ↗ArithmeticFunction.vonMangoldt s :=
    ArithmeticFunction.LSeriesSummable_vonMangoldt hs1
  have hΛ2 : LSeriesSummable ↗ArithmeticFunction.vonMangoldt (2 : ℂ) :=
    ArithmeticFunction.LSeriesSummable_vonMangoldt h2
  have hns : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt s n‖ := by
    rw [summable_norm_iff]; exact hΛs
  have hn2 : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
    rw [summable_norm_iff]; exact hΛ2
  have hre : (2 : ℂ).re ≤ s.re := by simpa using hs
  refine (norm_tsum_le_tsum_norm hns).trans ?_
  refine (hns.tsum_le_tsum
    (fun n => LSeries.norm_term_le_of_re_le_re
      (↗ArithmeticFunction.vonMangoldt) hre n) hn2).trans ?_
  exact (tsum_norm_term_vonMangoldt_two).le

end ZetaHalfPlaneBounds

/-! ### r507: Γ-free counting path — FE pairing + N=1 Euler–Maclaurin

Mathlib scoping (v4.29.1):
* `riemannZeta_one_sub` uses **cos(π s / 2)** (not sin) and needs
  `∀ n, s ≠ -n` plus `s ≠ 1`.  No growth bound.
* `Complex.Gamma_ne_zero` / `Gamma_ne_zero_of_re_pos` exist; pairing
  does not need them (the FE is a product, so `ζ(s) = 0` forces
  `ζ(1-s) = 0` whenever the identity applies).
* `ZetaAsymptotics` (`Harmonic/ZetaAsymp`) is only the `s → 1`
  Euler–Mascheroni limit.  Its real auxiliary
  `term n s = ∫_n^{n+1} (x-n)/x^{s+1}` is the real-s>1 shadow of
  the `{x}`-cell, not a complex `Re s > 0` representation.
* No EulerMacLaurin zeta module and no `{x} x^{-s-1}` formula
  for complex `s`.  We build the N=1 form from FTC + telescoping.
-/

section ZetaFunctionalEquationPairing

open Complex

/-- On the open strip `0 < Re s < 1` the FE hypotheses hold:
`s` is not a non-positive integer and `s ≠ 1`. -/
lemma riemannZeta_one_sub_hypotheses {s : ℂ} (h0 : 0 < s.re) (h1 : s.re < 1) :
    (∀ n : ℕ, s ≠ -n) ∧ s ≠ 1 := by
  refine ⟨fun n h => ?_, fun h => ?_⟩
  · have hre : s.re = - (n : ℝ) := by
      rw [h, neg_re, natCast_re]
    have : (0 : ℝ) ≤ n := Nat.cast_nonneg _
    linarith
  · have : s.re = 1 := by rw [h]; simp
    linarith

/-- **r507 (a).**  Functional-equation pairing on the open strip:
`ζ(s) = 0` and `0 < Re s < 1` imply `ζ(1-s) = 0`.  Prefactors of
`riemannZeta_one_sub` are finite on this strip, so no Γ-growth
and no `Gamma_ne_zero` is required. -/
lemma riemannZeta_one_sub_eq_zero_of {s : ℂ}
    (h0 : 0 < s.re) (h1 : s.re < 1) (hz : riemannZeta s = 0) :
    riemannZeta (1 - s) = 0 := by
  obtain ⟨hs_neg, hs1⟩ := riemannZeta_one_sub_hypotheses h0 h1
  rw [riemannZeta_one_sub hs_neg hs1, hz, mul_zero]

lemma re_one_sub {s : ℂ} : (1 - s).re = 1 - s.re := by
  simp [sub_re]

/-- Pairing is an equivalence: apply the one-sided lemma twice. -/
lemma riemannZeta_zero_iff_one_sub {s : ℂ}
    (h0 : 0 < s.re) (h1 : s.re < 1) :
    riemannZeta s = 0 ↔ riemannZeta (1 - s) = 0 := by
  constructor
  · exact riemannZeta_one_sub_eq_zero_of h0 h1
  · intro hz
    have h0' : 0 < (1 - s).re := by rw [re_one_sub]; linarith
    have h1' : (1 - s).re < 1 := by rw [re_one_sub]; linarith
    simpa [sub_sub_cancel] using
      riemannZeta_one_sub_eq_zero_of h0' h1' hz

end ZetaFunctionalEquationPairing

section ZetaEulerMaclaurin

open Complex Set MeasureTheory Filter Topology
open scoped Interval

/-- `{x} = x - n` on the half-open cell `[n, n+1)`. -/
lemma fract_eq_sub_of_mem_Ico {n : ℕ} {x : ℝ}
    (hx : x ∈ Ico (n : ℝ) (n + 1)) : Int.fract x = x - n := by
  have hfloor : ⌊x⌋ = (n : ℤ) :=
    Int.floor_eq_on_Ico (n : ℤ) x (by
      refine ⟨?_, ?_⟩
      · exact_mod_cast hx.1
      · exact_mod_cast hx.2)
  simp [Int.fract, hfloor]

lemma continuousOn_ofReal_cpow_Icc {a b : ℝ} (ha : 0 < a) (_hab : a ≤ b) (z : ℂ) :
    ContinuousOn (fun x : ℝ => (x : ℂ) ^ z) (Icc a b) := by
  intro x hx
  have hx0 : x ≠ 0 := (ha.trans_le hx.1).ne'
  exact (continuousAt_ofReal_cpow_const x z (Or.inr hx0)).continuousWithinAt

lemma intervalIntegrable_ofReal_cpow {n : ℕ} (hn : 0 < n) (z : ℂ) :
    IntervalIntegrable (fun x : ℝ => (x : ℂ) ^ z) volume (n : ℝ) (n + 1 : ℝ) := by
  refine ContinuousOn.intervalIntegrable_of_Icc (by linarith) ?_
  exact continuousOn_ofReal_cpow_Icc (Nat.cast_pos.mpr hn) (by linarith) z

/-- FTC for `x ↦ x^r` on a cell `[n, n+1]` with `n ≥ 1`. -/
lemma intervalIntegral_ofReal_cpow_deriv {n : ℕ} (hn : 0 < n) {r : ℂ}
    (hr : r ≠ 0) :
    ∫ x in (n : ℝ)..(n + 1), r * (x : ℂ) ^ (r - 1) =
      ((n + 1 : ℝ) : ℂ) ^ r - (n : ℂ) ^ r := by
  have hderiv : ∀ x ∈ uIcc (n : ℝ) (n + 1),
      HasDerivAt (fun y : ℝ => (y : ℂ) ^ r) (r * (x : ℂ) ^ (r - 1)) x := by
    intro x hx
    have hx0 : x ≠ 0 := by
      rw [uIcc_of_le (by linarith)] at hx
      exact ((Nat.cast_pos.mpr hn).trans_le hx.1).ne'
    exact hasDerivAt_ofReal_cpow_const hx0 hr
  have hint : IntervalIntegrable (fun x : ℝ => r * (x : ℂ) ^ (r - 1))
      volume (n : ℝ) (n + 1 : ℝ) :=
    (intervalIntegrable_ofReal_cpow hn (r - 1)).const_mul r
  simpa using intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint

/-- Cell identity: `∫_n^{n+1} x^{-s-1} dx = (n^{-s} - (n+1)^{-s}) / s`. -/
lemma intervalIntegral_cpow_neg_succ {n : ℕ} (hn : 0 < n) {s : ℂ}
    (hs : s ≠ 0) :
    ∫ x in (n : ℝ)..(n + 1), (x : ℂ) ^ (-s - 1) =
      ((n : ℂ) ^ (-s) - ((n + 1 : ℕ) : ℂ) ^ (-s)) / s := by
  have hr : (-s) ≠ 0 := neg_ne_zero.mpr hs
  have hFTC := intervalIntegral_ofReal_cpow_deriv hn hr
  have hI :
      (-s) * (∫ x in (n : ℝ)..(n + 1), (x : ℂ) ^ (-s - 1)) =
        ((n + 1 : ℝ) : ℂ) ^ (-s) - (n : ℂ) ^ (-s) := by
    trans ∫ x in (n : ℝ)..(n + 1), (-s) * (x : ℂ) ^ (-s - 1)
    · exact (intervalIntegral.integral_const_mul
        (r := -s) (fun x : ℝ => (x : ℂ) ^ (-s - 1))).symm
    · convert hFTC using 1
  have hcast : ((n + 1 : ℝ) : ℂ) = ((n + 1 : ℕ) : ℂ) := by simp
  rw [hcast] at hI
  rw [eq_div_iff hs]
  linear_combination -(hI)

/-- Discrete telescoping: `∑_{k=1}^N k (k^{-s}-(k+1)^{-s}) = ∑ k^{-s} - N(N+1)^{-s}`. -/
lemma sum_succ_mul_sub_cpow (N : ℕ) (s : ℂ) :
    ∑ n ∈ Finset.range N,
        (n + 1 : ℂ) * ((n + 1 : ℂ) ^ (-s) - (n + 2 : ℂ) ^ (-s)) =
      (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) -
        (N : ℂ) * (N + 1 : ℂ) ^ (-s) := by
  induction N with
  | zero => simp
  | succ N ih =>
    have hstep :
        (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) -
            (N : ℂ) * (N + 1 : ℂ) ^ (-s) +
            (N + 1 : ℂ) * ((N + 1 : ℂ) ^ (-s) - (N + 2 : ℂ) ^ (-s)) =
          (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) +
            (N + 1 : ℂ) ^ (-s) -
            (N + 1 : ℂ) * (N + 2 : ℂ) ^ (-s) := by
      have hN : (N + 1 : ℂ) - (N : ℂ) = 1 := by ring
      calc
        (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) -
            (N : ℂ) * (N + 1 : ℂ) ^ (-s) +
            (N + 1 : ℂ) * ((N + 1 : ℂ) ^ (-s) - (N + 2 : ℂ) ^ (-s))
            = (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) +
              ((N + 1 : ℂ) - (N : ℂ)) * (N + 1 : ℂ) ^ (-s) -
              (N + 1 : ℂ) * (N + 2 : ℂ) ^ (-s) := by ring
        _ = (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) +
              (N + 1 : ℂ) ^ (-s) -
              (N + 1 : ℂ) * (N + 2 : ℂ) ^ (-s) := by
          rw [hN, one_mul]
    calc
      ∑ n ∈ Finset.range (N + 1),
          (n + 1 : ℂ) * ((n + 1 : ℂ) ^ (-s) - (n + 2 : ℂ) ^ (-s))
          = (∑ n ∈ Finset.range N,
              (n + 1 : ℂ) * ((n + 1 : ℂ) ^ (-s) - (n + 2 : ℂ) ^ (-s))) +
            (N + 1 : ℂ) * ((N + 1 : ℂ) ^ (-s) - (N + 2 : ℂ) ^ (-s)) :=
        Finset.sum_range_succ _ _
      _ = (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) -
            (N : ℂ) * (N + 1 : ℂ) ^ (-s) +
            (N + 1 : ℂ) * ((N + 1 : ℂ) ^ (-s) - (N + 2 : ℂ) ^ (-s)) := by
        rw [ih]
      _ = (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) +
            (N + 1 : ℂ) ^ (-s) -
            (N + 1 : ℂ) * (N + 2 : ℂ) ^ (-s) := hstep
      _ = (∑ n ∈ Finset.range (N + 1), (n + 1 : ℂ) ^ (-s)) -
            ((N + 1 : ℕ) : ℂ) * (((N + 1 : ℕ) : ℂ) + 1) ^ (-s) := by
        rw [Finset.sum_range_succ, Nat.cast_succ, add_assoc]
        simp only [one_add_one_eq_two]

/-- `{x}`-cell integrand on `[n+1, n+2)` (equals `Int.fract` there). -/
noncomputable def zetaFractCellIntegrand (n : ℕ) (s : ℂ) (x : ℝ) : ℂ :=
  ((x - (n + 1 : ℝ) : ℝ) : ℂ) * (x : ℂ) ^ (-s - 1)

noncomputable def zetaFractCell (n : ℕ) (s : ℂ) : ℂ :=
  ∫ x in ((n + 1 : ℝ))..(n + 2), zetaFractCellIntegrand n s x

/-- N=1 fractional-part integral as a cell series (equals `∫_1^∞ {x} x^{-s-1} dx`
whenever the improper integral exists). -/
noncomputable def zetaFractIntegral (s : ℂ) : ℂ :=
  ∑' n : ℕ, zetaFractCell n s

lemma continuousOn_zetaFractCellIntegrand (n : ℕ) (s : ℂ) :
    ContinuousOn (zetaFractCellIntegrand n s) (Icc (n + 1 : ℝ) (n + 2)) := by
  have hpos : (0 : ℝ) < n + 1 := by exact_mod_cast Nat.succ_pos n
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  unfold zetaFractCellIntegrand
  refine ContinuousOn.mul ?_ (continuousOn_ofReal_cpow_Icc hpos hle (-s - 1))
  exact (continuous_ofReal.comp (continuous_sub_right (n + 1 : ℝ))).continuousOn

lemma intervalIntegrable_zetaFractCellIntegrand (n : ℕ) (s : ℂ) :
    IntervalIntegrable (zetaFractCellIntegrand n s) volume
      (n + 1 : ℝ) (n + 2) :=
  (continuousOn_zetaFractCellIntegrand n s).intervalIntegrable_of_Icc (by linarith)

lemma intervalIntegrable_id_mul_cpow {n : ℕ} (hn : 0 < n) (z : ℂ) :
    IntervalIntegrable (fun x : ℝ => (x : ℂ) * (x : ℂ) ^ z) volume
      (n : ℝ) (n + 1 : ℝ) := by
  refine ContinuousOn.intervalIntegrable_of_Icc (by linarith) ?_
  exact ContinuousOn.mul continuous_ofReal.continuousOn
    (continuousOn_ofReal_cpow_Icc (Nat.cast_pos.mpr hn) (by linarith) z)

/-- Rearrangement of the cell FTC: `n^{-s}-(n+1)^{-s} = s ∫_n^{n+1} x^{-s-1}`. -/
lemma sub_cpow_eq_s_mul_intervalIntegral {n : ℕ} (hn : 0 < n) {s : ℂ}
    (hs : s ≠ 0) :
    (n : ℂ) ^ (-s) - ((n + 1 : ℕ) : ℂ) ^ (-s) =
      s * ∫ x in (n : ℝ)..(n + 1), (x : ℂ) ^ (-s - 1) := by
  rw [intervalIntegral_cpow_neg_succ hn hs, mul_div_cancel₀ _ hs]

lemma one_div_natCast_cpow_eq_cpow_neg {n : ℕ} (s : ℂ) :
    (1 : ℂ) / (n : ℂ) ^ s = (n : ℂ) ^ (-s) := by
  rw [cpow_neg, inv_eq_one_div]

/-- On a cell, `|{x} x^{-s-1}| ≤ x^{-Re s - 1}`. -/
lemma norm_zetaFractCellIntegrand_le (n : ℕ) (s : ℂ) {x : ℝ}
    (hx : x ∈ Icc (n + 1 : ℝ) (n + 2)) :
    ‖zetaFractCellIntegrand n s x‖ ≤ x ^ (-s.re - 1) := by
  have hxpos : 0 < x :=
    (show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le hx.1
  have hfrac : |x - (n + 1)| ≤ 1 := by
    have h0 : 0 ≤ x - (n + 1) := sub_nonneg.mpr hx.1
    have h1 : x - (n + 1) ≤ 1 := by linarith [hx.2]
    rw [abs_of_nonneg h0]
    exact h1
  unfold zetaFractCellIntegrand
  rw [norm_mul, Complex.norm_real, norm_cpow_eq_rpow_re_of_pos hxpos]
  simp only [sub_re, neg_re, one_re]
  exact mul_le_of_le_one_left (Real.rpow_nonneg hxpos.le _) hfrac

/-- Cell majorant: `|∫_{n+1}^{n+2} {x} x^{-s-1}| ≤ ∫_{n+1}^{n+2} x^{-σ-1}`. -/
lemma norm_zetaFractCell_le (n : ℕ) (s : ℂ) :
    ‖zetaFractCell n s‖ ≤
      ∫ x in (n + 1 : ℝ)..(n + 2), (x : ℝ) ^ (-s.re - 1) := by
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  refine (intervalIntegral.norm_integral_le_integral_norm hle).trans ?_
  refine intervalIntegral.integral_mono_on hle
    ((continuousOn_zetaFractCellIntegrand n s).norm.intervalIntegrable_of_Icc hle)
    (ContinuousOn.intervalIntegrable_of_Icc hle
      (continuousOn_id.rpow_const (fun x hx => Or.inl
        ((show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le hx.1).ne')))
    (fun x hx => norm_zetaFractCellIntegrand_le n s hx)

/-! ### r508: assemble N=1 Euler–Maclaurin on `Re s > 1` -/

lemma ofReal_mul_cpow_neg_succ {x : ℝ} (hx : 0 < x) (s : ℂ) :
    (x : ℂ) * (x : ℂ) ^ (-s - 1) = (x : ℂ) ^ (-s) := by
  have hx0 : (x : ℂ) ≠ 0 := ofReal_ne_zero.mpr hx.ne'
  calc
    (x : ℂ) * (x : ℂ) ^ (-s - 1)
        = (x : ℂ) ^ (1 : ℂ) * (x : ℂ) ^ (-s - 1) := by rw [cpow_one]
    _ = (x : ℂ) ^ ((1 : ℂ) + (-s - 1)) := (cpow_add _ _ hx0).symm
    _ = (x : ℂ) ^ (-s) := by
      congr 1
      ring

lemma intervalIntegrable_ofReal_cpow_neg (n : ℕ) (s : ℂ) :
    IntervalIntegrable (fun x : ℝ => (x : ℂ) ^ (-s)) volume
      (n + 1 : ℝ) (n + 2) := by
  refine ContinuousOn.intervalIntegrable_of_Icc (by linarith) ?_
  exact continuousOn_ofReal_cpow_Icc (by exact_mod_cast Nat.succ_pos n)
    (by linarith) (-s)

/-- FTC on a compact interval away from `0`. -/
lemma intervalIntegral_ofReal_cpow_deriv_of_le {a b : ℝ}
    (ha : 0 < a) (hab : a ≤ b) {r : ℂ} (hr : r ≠ 0) :
    ∫ x in a..b, r * (x : ℂ) ^ (r - 1) = (b : ℂ) ^ r - (a : ℂ) ^ r := by
  have hderiv : ∀ x ∈ uIcc a b,
      HasDerivAt (fun y : ℝ => (y : ℂ) ^ r) (r * (x : ℂ) ^ (r - 1)) x := by
    intro x hx
    have hx0 : x ≠ 0 := by
      rw [uIcc_of_le hab] at hx
      exact (ha.trans_le hx.1).ne'
    exact hasDerivAt_ofReal_cpow_const hx0 hr
  have hint : IntervalIntegrable (fun x : ℝ => r * (x : ℂ) ^ (r - 1)) volume a b :=
    (ContinuousOn.intervalIntegrable_of_Icc hab
      (continuousOn_ofReal_cpow_Icc ha hab (r - 1))).const_mul r
  simpa using intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint

lemma intervalIntegral_cpow_neg_of_le {a b : ℝ} (ha : 0 < a) (hab : a ≤ b)
    {s : ℂ} (hs : s ≠ 1) :
    ∫ x in a..b, (x : ℂ) ^ (-s) =
      ((b : ℂ) ^ (1 - s) - (a : ℂ) ^ (1 - s)) / (1 - s) := by
  have hr : (1 - s) ≠ 0 := sub_ne_zero.mpr fun h => hs (by linear_combination -h)
  have hFTC := intervalIntegral_ofReal_cpow_deriv_of_le ha hab hr
  have hI :
      (1 - s) * (∫ x in a..b, (x : ℂ) ^ (-s)) =
        (b : ℂ) ^ (1 - s) - (a : ℂ) ^ (1 - s) := by
    trans ∫ x in a..b, (1 - s) * (x : ℂ) ^ (-s)
    · exact (intervalIntegral.integral_const_mul
        (r := 1 - s) (fun x : ℝ => (x : ℂ) ^ (-s))).symm
    · have hFTC' := hFTC
      rw [show (1 - s) - (1 : ℂ) = -s from by ring] at hFTC'
      exact hFTC'
  rw [eq_div_iff hr]
  linear_combination hI

lemma intervalIntegral_cpow_neg_one_to_succ (N : ℕ) {s : ℂ} (hs : s ≠ 1) :
    ∫ x in (1 : ℝ)..(N + 1 : ℝ), (x : ℂ) ^ (-s) =
      ((((N + 1 : ℕ) : ℂ) ^ (1 - s) - 1) / (1 - s)) := by
  have h := intervalIntegral_cpow_neg_of_le (a := (1 : ℝ)) (b := (N + 1 : ℝ))
    (by positivity) (le_add_of_nonneg_left (Nat.cast_nonneg N)) hs
  have h1 : ((1 : ℝ) : ℂ) ^ (1 - s) = 1 := by
    rw [ofReal_one, one_cpow]
  have hN : ((N + 1 : ℝ) : ℂ) = ((N + 1 : ℕ) : ℂ) := by simp
  rw [h, h1, hN]

lemma succ_mul_sub_cpow_eq_s_mul_integral (n : ℕ) {s : ℂ} (hs : s ≠ 0) :
    (n + 1 : ℂ) * ((n + 1 : ℂ) ^ (-s) - (n + 2 : ℂ) ^ (-s)) =
      s * ∫ x in (n + 1 : ℝ)..(n + 2),
        (n + 1 : ℂ) * (x : ℂ) ^ (-s - 1) := by
  have hn : 0 < n + 1 := Nat.succ_pos n
  have hsub := sub_cpow_eq_s_mul_intervalIntegral (n := n + 1) hn hs
  have hcast : ((n + 2 : ℕ) : ℂ) = (n + 2 : ℂ) := by simp
  have hcast1 : ((n + 1 : ℕ) : ℂ) = (n + 1 : ℂ) := by simp
  rw [hcast1, hcast] at hsub
  have hab : ((n + 1 : ℕ) : ℝ) = (n + 1 : ℝ) := by simp
  have hab' : (n + 1 : ℝ) + 1 = (n + 2 : ℝ) := by ring
  rw [hab] at hsub
  rw [hab'] at hsub
  have hint :=
    intervalIntegral.integral_const_mul (μ := volume) (a := (n + 1 : ℝ))
      (b := (n + 2 : ℝ)) (r := (n + 1 : ℂ))
      (fun x : ℝ => (x : ℂ) ^ (-s - 1))
  rw [hsub, mul_left_comm]
  congr 1
  exact hint.symm

lemma succ_mul_cpow_eq_sub_cell_integrand (n : ℕ) (s : ℂ) {x : ℝ}
    (hx : 0 < x) :
    (n + 1 : ℂ) * (x : ℂ) ^ (-s - 1) =
      (x : ℂ) ^ (-s) - zetaFractCellIntegrand n s x := by
  unfold zetaFractCellIntegrand
  have hsplit :
      ((x - (n + 1 : ℝ) : ℝ) : ℂ) * (x : ℂ) ^ (-s - 1) +
          (n + 1 : ℂ) * (x : ℂ) ^ (-s - 1) =
        (x : ℂ) * (x : ℂ) ^ (-s - 1) := by
    have hx' : ((x - (n + 1 : ℝ) : ℝ) : ℂ) = (x : ℂ) - (n + 1 : ℂ) := by
      simp
    rw [hx']
    ring
  rw [eq_sub_iff_add_eq, add_comm, hsplit, ofReal_mul_cpow_neg_succ hx]

set_option maxHeartbeats 800000 in
lemma intervalIntegral_succ_mul_eq_sub_cell (n : ℕ) (s : ℂ) :
    ∫ x in (n + 1 : ℝ)..(n + 2), (n + 1 : ℂ) * (x : ℂ) ^ (-s - 1) =
      (∫ x in (n + 1 : ℝ)..(n + 2), (x : ℂ) ^ (-s)) - zetaFractCell n s := by
  have hpos : ∀ x ∈ uIcc (n + 1 : ℝ) (n + 2), 0 < x := by
    intro x hx
    rw [uIcc_of_le (by linarith)] at hx
    exact (show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le hx.1
  have hcongr :
      ∫ x in (n + 1 : ℝ)..(n + 2), (n + 1 : ℂ) * (x : ℂ) ^ (-s - 1) =
        ∫ x in (n + 1 : ℝ)..(n + 2),
          (x : ℂ) ^ (-s) - zetaFractCellIntegrand n s x := by
    apply intervalIntegral.integral_congr
    intro x hx
    exact succ_mul_cpow_eq_sub_cell_integrand n s (hpos x hx)
  rw [hcongr, intervalIntegral.integral_sub]
  · rfl
  · exact intervalIntegrable_ofReal_cpow_neg n s
  · exact intervalIntegrable_zetaFractCellIntegrand n s

lemma sum_intervalIntegral_cpow_neg (N : ℕ) (s : ℂ) :
    ∑ n ∈ Finset.range N,
        ∫ x in (n + 1 : ℝ)..(n + 2), (x : ℂ) ^ (-s) =
      ∫ x in (1 : ℝ)..(N + 1 : ℝ), (x : ℂ) ^ (-s) := by
  have hint : ∀ k < N,
      IntervalIntegrable (fun x : ℝ => (x : ℂ) ^ (-s)) volume
        ((k + 1 : ℕ) : ℝ) ((k + 2 : ℕ) : ℝ) := by
    intro k _
    convert intervalIntegrable_ofReal_cpow_neg k s <;> simp
  have hadj :=
    intervalIntegral.sum_integral_adjacent_intervals
      (μ := volume) (f := fun x : ℝ => (x : ℂ) ^ (-s))
      (a := fun k : ℕ => ((k + 1 : ℕ) : ℝ)) (n := N) hint
  have hsum :
      ∑ n ∈ Finset.range N,
          ∫ x in (n + 1 : ℝ)..(n + 2), (x : ℂ) ^ (-s) =
        ∑ k ∈ Finset.range N,
          ∫ x in ((k + 1 : ℕ) : ℝ)..((k + 2 : ℕ) : ℝ), (x : ℂ) ^ (-s) := by
    apply Finset.sum_congr rfl
    intro n _
    congr 1 <;> simp
  rw [hsum, hadj]
  congr 1 <;> simp

/-- **r508 (1).** Finite-N Euler–Maclaurin identity. -/
lemma finite_N_euler_maclaurin {N : ℕ} {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) =
      s / (s - 1) * (1 - ((N + 1 : ℕ) : ℂ) ^ (1 - s)) -
        s * ∑ n ∈ Finset.range N, zetaFractCell n s +
        (N : ℂ) * (N + 1 : ℂ) ^ (-s) := by
  have htel := sum_succ_mul_sub_cpow N s
  have hterm : ∀ n ∈ Finset.range N,
      (n + 1 : ℂ) * ((n + 1 : ℂ) ^ (-s) - (n + 2 : ℂ) ^ (-s)) =
        s * ((∫ x in (n + 1 : ℝ)..(n + 2), (x : ℂ) ^ (-s)) -
          zetaFractCell n s) := by
    intro n _
    rw [succ_mul_sub_cpow_eq_s_mul_integral n hs0,
      intervalIntegral_succ_mul_eq_sub_cell]
  have hsum := Finset.sum_congr rfl hterm
  rw [htel, ← Finset.mul_sum] at hsum
  have hsum' :
      s * ∑ n ∈ Finset.range N,
          ((∫ x in (n + 1 : ℝ)..(n + 2), (x : ℂ) ^ (-s)) - zetaFractCell n s) =
        (∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) -
          (N : ℂ) * (N + 1 : ℂ) ^ (-s) := hsum.symm
  rw [Finset.sum_sub_distrib, mul_sub, sum_intervalIntegral_cpow_neg,
    intervalIntegral_cpow_neg_one_to_succ N hs1] at hsum'
  have hdiv :
      s * ((((N + 1 : ℕ) : ℂ) ^ (1 - s) - 1) / (1 - s)) =
        s / (s - 1) * (1 - ((N + 1 : ℕ) : ℂ) ^ (1 - s)) := by
    have hneg : (1 - s) = -(s - 1) := by ring
    rw [hneg, div_neg, neg_sub]
    ring
  rw [hdiv] at hsum'
  have hadd := congrArg
    (fun z => z + (N : ℂ) * (N + 1 : ℂ) ^ (-s)) hsum'
  simpa [sub_add_cancel, add_comm] using hadd.symm

lemma tendsto_nat_succ_cpow_neg {s : ℂ} (hs : 0 < s.re) :
    Tendsto (fun N : ℕ => ((N + 1 : ℕ) : ℂ) ^ (-s)) atTop (𝓝 0) := by
  rw [tendsto_zero_iff_norm_tendsto_zero]
  simp_rw [norm_natCast_cpow_of_pos (Nat.succ_pos _), neg_re]
  exact (tendsto_rpow_neg_atTop hs).comp
    (tendsto_natCast_atTop_atTop.comp (tendsto_add_atTop_nat 1))

lemma tendsto_nat_succ_cpow_one_sub {s : ℂ} (hs : 1 < s.re) :
    Tendsto (fun N : ℕ => ((N + 1 : ℕ) : ℂ) ^ (1 - s)) atTop (𝓝 0) := by
  rw [tendsto_zero_iff_norm_tendsto_zero]
  simp_rw [norm_natCast_cpow_of_pos (Nat.succ_pos _), sub_re, one_re]
  have hpos : 0 < s.re - 1 := sub_pos.mpr hs
  have hpow : (fun N : ℕ => ((N + 1 : ℕ) : ℝ) ^ (1 - s.re)) =
      fun N => ((N + 1 : ℕ) : ℝ) ^ (-(s.re - 1)) := by
    ext N
    congr 1
    ring
  rw [hpow]
  exact (tendsto_rpow_neg_atTop hpos).comp
    (tendsto_natCast_atTop_atTop.comp (tendsto_add_atTop_nat 1))

lemma tendsto_nat_mul_succ_cpow_neg {s : ℂ} (hs : 1 < s.re) :
    Tendsto (fun N : ℕ => (N : ℂ) * (N + 1 : ℂ) ^ (-s)) atTop (𝓝 0) := by
  have hbound : ∀ N : ℕ,
      ‖(N : ℂ) * (N + 1 : ℂ) ^ (-s)‖ ≤
        ((N + 1 : ℕ) : ℝ) ^ (1 - s.re) := by
    intro N
    rw [norm_mul, Complex.norm_natCast]
    have hcast : (N + 1 : ℂ) = ((N + 1 : ℕ) : ℂ) := by simp
    rw [hcast, norm_natCast_cpow_of_pos (Nat.succ_pos N), neg_re]
    have hN : (N : ℝ) ≤ ((N + 1 : ℕ) : ℝ) := by exact_mod_cast Nat.le_succ N
    have hpow : 0 ≤ ((N + 1 : ℕ) : ℝ) ^ (-s.re) :=
      Real.rpow_nonneg (Nat.cast_nonneg _) _
    refine (mul_le_mul_of_nonneg_right hN hpow).trans ?_
    have hpos : (0 : ℝ) < ((N + 1 : ℕ) : ℝ) := by exact_mod_cast Nat.succ_pos N
    rw [mul_comm, ← Real.rpow_add_one hpos.ne']
    refine le_of_eq ?_
    congr 1
    ring
  have htend : Tendsto (fun N : ℕ => ((N + 1 : ℕ) : ℝ) ^ (1 - s.re))
      atTop (𝓝 0) := by
    have hpos : 0 < s.re - 1 := sub_pos.mpr hs
    have hpow : (fun N : ℕ => ((N + 1 : ℕ) : ℝ) ^ (1 - s.re)) =
        fun N => ((N + 1 : ℕ) : ℝ) ^ (-(s.re - 1)) := by
      ext N
      congr 1
      ring
    rw [hpow]
    exact (tendsto_rpow_neg_atTop hpos).comp
      (tendsto_natCast_atTop_atTop.comp (tendsto_add_atTop_nat 1))
  exact squeeze_zero_norm hbound htend

lemma norm_zetaFractCell_le_rpow (n : ℕ) {s : ℂ} (hs : -1 < s.re) :
    ‖zetaFractCell n s‖ ≤ ((n + 1 : ℕ) : ℝ) ^ (-s.re - 1) := by
  refine (norm_zetaFractCell_le n s).trans ?_
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  have hpos : (0 : ℝ) < n + 1 := by exact_mod_cast Nat.succ_pos n
  have hmono : ∀ x ∈ Icc (n + 1 : ℝ) (n + 2),
      x ^ (-s.re - 1) ≤ ((n + 1 : ℕ) : ℝ) ^ (-s.re - 1) := by
    intro x hx
    have hx0 : 0 < x := hpos.trans_le hx.1
    have hbase : (n + 1 : ℝ) ≤ x := hx.1
    have hexp : -s.re - 1 ≤ 0 := by linarith
    simpa using Real.rpow_le_rpow_of_nonpos hpos hbase hexp
  have hint : IntervalIntegrable (fun x : ℝ => x ^ (-s.re - 1)) volume
      (n + 1 : ℝ) (n + 2) :=
    ContinuousOn.intervalIntegrable_of_Icc hle
      (continuousOn_id.rpow_const fun x hx =>
        Or.inl (hpos.trans_le hx.1).ne')
  refine (intervalIntegral.integral_mono_on hle hint
    (intervalIntegrable_const (c := ((n + 1 : ℕ) : ℝ) ^ (-s.re - 1)))
    hmono).trans ?_
  simp [intervalIntegral.integral_const]
  ring_nf
  exact le_rfl

lemma summable_one_div_nat_succ_rpow {p : ℝ} (hp : 1 < p) :
    Summable fun n : ℕ => (1 : ℝ) / ((n + 1 : ℕ) : ℝ) ^ p := by
  have h := (Real.summable_one_div_nat_rpow (p := p)).mpr hp
  exact (summable_nat_add_iff
    (f := fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ p) 1).mpr h

lemma summable_rpow_neg_succ {p : ℝ} (hp : 1 < p) :
    Summable fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-p) := by
  refine (summable_congr fun n : ℕ => ?_).mp (summable_one_div_nat_succ_rpow hp)
  have hn : (0 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := Nat.cast_nonneg _
  rw [one_div]
  exact (Real.rpow_neg hn p).symm

lemma summable_zetaFractCell {s : ℂ} (hs : 0 < s.re) :
    Summable fun n : ℕ => zetaFractCell n s := by
  refine Summable.of_norm ?_
  refine Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
    (fun n => norm_zetaFractCell_le_rpow n (by linarith)) ?_
  have hp : 1 < s.re + 1 := by linarith
  refine (summable_congr fun n : ℕ => ?_).mp (summable_rpow_neg_succ hp)
  congr 1
  ring

lemma one_div_nat_succ_cpow_eq_cpow_neg (n : ℕ) (s : ℂ) :
    (1 : ℂ) / (n + 1 : ℂ) ^ s = (n + 1 : ℂ) ^ (-s) := by
  rw [nat_succ_coe_complex, one_div_natCast_cpow_eq_cpow_neg]

lemma summable_rpow_neg_succ_two :
    Summable fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-(2 : ℝ)) :=
  summable_rpow_neg_succ (p := (2 : ℝ)) (by norm_num)

/-- **r508 (2).** N=1 formula on `Re s > 1`:
`ζ(s) = s/(s-1) - s · zetaFractIntegral s`. -/
lemma riemannZeta_eq_s_div_sub_s_mul_fractIntegral {s : ℂ}
    (hs : 1 < s.re) :
    riemannZeta s = s / (s - 1) - s * zetaFractIntegral s := by
  have hs1 : 1 < s.re := hs
  have hs0 : s ≠ 0 := by
    intro h
    have : s.re = 0 := by rw [h]; simp
    linarith
  have hs_ne1 : s ≠ 1 := by
    intro h
    have : s.re = 1 := by rw [h]; simp
    linarith
  have hsummable_cell := summable_zetaFractCell (by linarith : 0 < s.re)
  have hζ := zeta_eq_tsum_one_div_nat_add_one_cpow hs1
  have hterm : (fun n : ℕ => (1 : ℂ) / (n + 1 : ℂ) ^ s) =
      (fun n : ℕ => (n + 1 : ℂ) ^ (-s)) :=
    funext fun n : ℕ => one_div_nat_succ_cpow_eq_cpow_neg n s
  rw [hterm] at hζ
  have hpartial := (summable_one_div_nat_add_one_cpow hs1).hasSum.tendsto_sum_nat
  rw [hterm] at hpartial
  rw [← hζ] at hpartial
  have hid N := finite_N_euler_maclaurin (N := N) hs0 hs_ne1
  have hlim :
      Tendsto (fun N : ℕ =>
        s / (s - 1) * (1 - ((N + 1 : ℕ) : ℂ) ^ (1 - s)) -
          s * ∑ n ∈ Finset.range N, zetaFractCell n s +
          (N : ℂ) * (N + 1 : ℂ) ^ (-s)) atTop
        (𝓝 (s / (s - 1) - s * zetaFractIntegral s)) := by
    have h1 : Tendsto (fun N : ℕ =>
        s / (s - 1) * (1 - ((N + 1 : ℕ) : ℂ) ^ (1 - s))) atTop
        (𝓝 (s / (s - 1) * (1 - 0))) :=
      tendsto_const_nhds.mul <| tendsto_const_nhds.sub (tendsto_nat_succ_cpow_one_sub hs)
    have h2 : Tendsto (fun N : ℕ =>
        s * ∑ n ∈ Finset.range N, zetaFractCell n s) atTop
        (𝓝 (s * zetaFractIntegral s)) :=
      tendsto_const_nhds.mul hsummable_cell.hasSum.tendsto_sum_nat
    have h3 := tendsto_nat_mul_succ_cpow_neg hs
    have heq : s / (s - 1) * (1 - 0) - s * zetaFractIntegral s + 0 =
        s / (s - 1) - s * zetaFractIntegral s := by ring
    rw [← heq]
    exact (h1.sub h2).add h3
  have hlim' : Tendsto (fun N : ℕ =>
      ∑ n ∈ Finset.range N, (n + 1 : ℂ) ^ (-s)) atTop
      (𝓝 (s / (s - 1) - s * zetaFractIntegral s)) := by
    convert hlim using 1
    exact funext hid
  exact tendsto_nhds_unique hpartial hlim'

set_option maxHeartbeats 800000 in
lemma norm_zetaFractIntegral_le_zeta_two {s : ℂ} (hs : 1 < s.re) :
    ‖zetaFractIntegral s‖ ≤ ‖riemannZeta 2‖ := by
  have hle : ∀ n, ‖zetaFractCell n s‖ ≤ ((n + 1 : ℕ) : ℝ) ^ (-(2 : ℝ)) :=
    fun n => (norm_zetaFractCell_le_rpow n (by linarith)).trans <| by
      have hb : (1 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by
        exact_mod_cast Nat.succ_le_succ (Nat.zero_le n)
      exact Real.rpow_le_rpow_of_exponent_le hb
        (by linarith : -s.re - 1 ≤ -(2 : ℝ))
  have hnorm : Summable fun n : ℕ => ‖zetaFractCell n s‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hle
      summable_rpow_neg_succ_two
  refine (norm_tsum_le_tsum_norm (f := fun n => zetaFractCell n s) hnorm).trans ?_
  refine (hnorm.tsum_mono summable_rpow_neg_succ_two hle).trans ?_
  have hn : ∀ n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-(2 : ℝ)) =
      ‖(1 : ℂ) / (n + 1 : ℂ) ^ (2 : ℂ)‖ := fun n => by
    rw [norm_one_div_nat_succ_cpow]
    simp
  rw [tsum_congr hn, tsum_norm_one_div_nat_succ_two]
  have h2c : 1 < (2 : ℂ).re := by norm_num
  rw [← zeta_eq_tsum_one_div_nat_add_one_cpow h2c]

/-- **r508 (4), Re s > 1 cut.**  Γ-free polynomial bound on
`{Re s > 1} ∩ {|s-1| ≥ 1/2}`.  Constant `2 + |ζ(2)|`. -/
lemma norm_riemannZeta_le_of_re_gt_one {s : ℂ} (hs : 1 < s.re)
    (hsep : (1 / 2 : ℝ) ≤ ‖s - 1‖) :
    ‖riemannZeta s‖ ≤ (2 + ‖riemannZeta 2‖) * (1 + ‖s‖) := by
  have hform := riemannZeta_eq_s_div_sub_s_mul_fractIntegral hs
  rw [hform]
  have hI := norm_zetaFractIntegral_le_zeta_two hs
  have hleft : ‖s / (s - 1)‖ ≤ 2 * ‖s‖ := by
    rw [norm_div]
    refine (div_le_div_of_nonneg_left (norm_nonneg s)
      (by positivity : (0 : ℝ) < 1 / 2) hsep).trans ?_
    field_simp
    exact le_rfl
  have hright : ‖s * zetaFractIntegral s‖ ≤ ‖s‖ * ‖riemannZeta 2‖ := by
    rw [norm_mul]
    exact mul_le_mul_of_nonneg_left hI (norm_nonneg s)
  refine (norm_sub_le _ _).trans ?_
  refine (add_le_add hleft hright).trans ?_
  nlinarith [norm_nonneg s, norm_nonneg (riemannZeta 2)]

/-- **r509 (a).** `s ↦ x^{-s-1}` is entire for `x > 0`. -/
lemma hasDerivAt_ofReal_cpow_neg_succ {x : ℝ} (hx : 0 < x) (s : ℂ) :
    HasDerivAt (fun z : ℂ => (x : ℂ) ^ (-z - 1))
      (-Complex.log (x : ℂ) * (x : ℂ) ^ (-s - 1)) s := by
  have hx0 : (x : ℂ) ≠ 0 := ofReal_ne_zero.mpr hx.ne'
  simpa [mul_comm, mul_neg, sub_eq_add_neg] using
    (((hasDerivAt_id' s).neg).sub_const (1 : ℂ)).const_cpow (Or.inl hx0)

lemma hasDerivAt_zetaFractCellIntegrand (n : ℕ) {x : ℝ} (hx : 0 < x)
    (s : ℂ) :
    HasDerivAt (fun z : ℂ => zetaFractCellIntegrand n z x)
      (-Complex.log (x : ℂ) * zetaFractCellIntegrand n s x) s := by
  simpa [zetaFractCellIntegrand, mul_comm, mul_left_comm, mul_neg] using
    (hasDerivAt_ofReal_cpow_neg_succ hx s).const_mul ((x - (n + 1 : ℝ) : ℂ))

lemma norm_log_ofReal_of_one_le {x : ℝ} (hx : 1 ≤ x) :
    ‖Complex.log (x : ℂ)‖ = Real.log x := by
  have hx0 : 0 < x := zero_lt_one.trans_le hx
  rw [← ofReal_log hx0.le, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.log_nonneg hx)]

/-- Integrand derivative majorant on a cell: `|∂_s cellIntegrand| ≤ log x · x^{-σ-1}`. -/
lemma norm_hasDeriv_zetaFractCellIntegrand (n : ℕ) (s : ℂ) {x : ℝ}
    (hx : x ∈ Icc (n + 1 : ℝ) (n + 2)) :
    ‖-Complex.log (x : ℂ) * zetaFractCellIntegrand n s x‖ ≤
      Real.log x * x ^ (-s.re - 1) := by
  have hx1 : 1 ≤ x := by
    have : (1 : ℝ) ≤ n + 1 := by exact_mod_cast Nat.succ_le_succ (Nat.zero_le n)
    exact this.trans hx.1
  rw [norm_mul, norm_neg, norm_log_ofReal_of_one_le hx1]
  exact mul_le_mul_of_nonneg_left (norm_zetaFractCellIntegrand_le n s hx)
    (Real.log_nonneg hx1)

lemma intervalIntegrable_log_rpow (n : ℕ) (p : ℝ) :
    IntervalIntegrable (fun x : ℝ => Real.log x * x ^ (-p - 1)) volume
      (n + 1 : ℝ) (n + 2) := by
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  have hpos : (0 : ℝ) < n + 1 := by exact_mod_cast Nat.succ_pos n
  refine ContinuousOn.intervalIntegrable_of_Icc hle ?_
  refine ContinuousOn.mul ?_
    (continuousOn_id.rpow_const fun x hx => Or.inl (hpos.trans_le hx.1).ne')
  exact Real.continuousOn_log.mono fun x hx => (hpos.trans_le hx.1).ne'

lemma mem_Icc_of_mem_uIoc {n : ℕ} {t : ℝ}
    (ht : t ∈ Ι (n + 1 : ℝ) (n + 2)) : t ∈ Icc (n + 1 : ℝ) (n + 2) := by
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  exact Ioc_subset_Icc_self (by rwa [uIoc_of_le hle] at ht)

/-- **r509 (a).** Parametric FTC: each cell is entire. -/
lemma hasDerivAt_zetaFractCell (n : ℕ) (s₀ : ℂ) :
    HasDerivAt (zetaFractCell n)
      (∫ x in (n + 1 : ℝ)..(n + 2),
        -Complex.log (x : ℂ) * zetaFractCellIntegrand n s₀ x) s₀ := by
  let δ : ℝ := s₀.re - 1
  let r : ℝ := (1 : ℝ) / 2
  have hr : 0 < r := by norm_num
  have hs : Metric.ball s₀ r ∈ 𝓝 s₀ := Metric.ball_mem_nhds s₀ hr
  have hF_meas : ∀ᶠ z in 𝓝 s₀,
      AEStronglyMeasurable (zetaFractCellIntegrand n z)
        (volume.restrict (Ι (n + 1 : ℝ) (n + 2))) :=
    Filter.Eventually.of_forall fun z =>
      (intervalIntegrable_zetaFractCellIntegrand n z).aestronglyMeasurable_restrict_uIoc
  have hF_int := intervalIntegrable_zetaFractCellIntegrand n s₀
  have hF'_meas :
      AEStronglyMeasurable
        (fun x : ℝ => -Complex.log (x : ℂ) * zetaFractCellIntegrand n s₀ x)
        (volume.restrict (Ι (n + 1 : ℝ) (n + 2))) := by
    have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
    have hpos : (0 : ℝ) < n + 1 := by exact_mod_cast Nat.succ_pos n
    have hcont : ContinuousOn
        (fun x : ℝ => -Complex.log (x : ℂ) * zetaFractCellIntegrand n s₀ x)
        (Icc (n + 1 : ℝ) (n + 2)) := by
      refine ContinuousOn.mul ?_ (continuousOn_zetaFractCellIntegrand n s₀)
      refine ContinuousOn.neg ?_
      refine ContinuousOn.congr
        (continuous_ofReal.comp_continuousOn
          (Real.continuousOn_log.mono fun x hx =>
            (hpos.trans_le hx.1).ne'))
        fun x hx => (ofReal_log (hpos.trans_le hx.1).le).symm
    exact (hcont.intervalIntegrable_of_Icc hle).aestronglyMeasurable_restrict_uIoc
  have h_bound : ∀ᵐ t ∂volume, t ∈ Ι (n + 1 : ℝ) (n + 2) →
      ∀ z ∈ Metric.ball s₀ r,
        ‖-Complex.log (t : ℂ) * zetaFractCellIntegrand n z t‖ ≤
          Real.log t * t ^ (-δ - 1) := by
    refine Filter.Eventually.of_forall ?_
    intro t ht z hz
    have hIcc := mem_Icc_of_mem_uIoc ht
    refine (norm_hasDeriv_zetaFractCellIntegrand n z hIcc).trans ?_
    have hx1 : 1 ≤ t := by
      have : (1 : ℝ) ≤ n + 1 := by exact_mod_cast Nat.succ_le_succ (Nat.zero_le n)
      exact this.trans hIcc.1
    have hzball : ‖z - s₀‖ < r := by
      simpa [dist_eq_norm] using Metric.mem_ball.mp hz
    have habs : |z.re - s₀.re| < r :=
      (abs_re_le_norm (z - s₀)).trans_lt hzball
    have hre : δ < z.re := by
      have : s₀.re - r < z.re := by linarith [(abs_lt.mp habs).1]
      dsimp [δ, r] at *
      linarith
    exact mul_le_mul_of_nonneg_left
      (Real.rpow_le_rpow_of_exponent_le hx1 (by linarith : -z.re - 1 ≤ -δ - 1))
      (Real.log_nonneg hx1)
  have bound_int := intervalIntegrable_log_rpow n δ
  have h_diff : ∀ᵐ t ∂volume, t ∈ Ι (n + 1 : ℝ) (n + 2) →
      ∀ z ∈ Metric.ball s₀ r,
        HasDerivAt (fun w : ℂ => zetaFractCellIntegrand n w t)
          (-Complex.log (t : ℂ) * zetaFractCellIntegrand n z t) z := by
    refine Filter.Eventually.of_forall ?_
    intro t ht z _hz
    have hx0 : 0 < t :=
      (show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le
        (mem_Icc_of_mem_uIoc ht).1
    exact hasDerivAt_zetaFractCellIntegrand n hx0 z
  exact (intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le
    hs hF_meas hF_int hF'_meas h_bound bound_int h_diff).2

lemma differentiable_zetaFractCell (n : ℕ) : Differentiable ℂ (zetaFractCell n) :=
  fun s => (hasDerivAt_zetaFractCell n s).differentiableAt

lemma isOpen_re_gt (δ : ℝ) : IsOpen {s : ℂ | δ < s.re} :=
  isOpen_lt continuous_const continuous_re

lemma norm_zetaFractCell_le_rpow_of_re_gt (n : ℕ) {s : ℂ} {δ : ℝ}
    (hδ : 0 < δ) (hs : δ < s.re) :
    ‖zetaFractCell n s‖ ≤ ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) :=
  (norm_zetaFractCell_le_rpow n (by linarith : -1 < s.re)).trans <| by
    have hb : (1 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by
      exact_mod_cast Nat.succ_le_succ (Nat.zero_le n)
    exact Real.rpow_le_rpow_of_exponent_le hb (by linarith : -s.re - 1 ≤ -δ - 1)

/-- **r509 (b).** Weierstrass M-test: `zetaFractIntegral` is holomorphic on `{Re > δ}`. -/
lemma differentiableOn_zetaFractIntegral_re_gt {δ : ℝ} (hδ : 0 < δ) :
    DifferentiableOn ℂ zetaFractIntegral {s | δ < s.re} := by
  have hu := summable_rpow_neg_succ (p := δ + 1) (by linarith)
  have hu' : Summable fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
    refine (summable_congr fun n => ?_).mp hu
    congr 1
    ring
  refine differentiableOn_tsum_of_summable_norm hu'
    (fun n => (differentiable_zetaFractCell n).differentiableOn)
    (isOpen_re_gt δ) ?_
  intro n s hs
  exact norm_zetaFractCell_le_rpow_of_re_gt n hδ hs

lemma differentiableOn_zetaFractIntegral_re_pos :
    DifferentiableOn ℂ zetaFractIntegral {s | 0 < s.re} := by
  intro s hs
  have hδ : 0 < s.re / 2 := half_pos hs
  have hsU : s.re / 2 < s.re := half_lt_self hs
  exact ((differentiableOn_zetaFractIntegral_re_gt hδ).differentiableAt
    ((isOpen_re_gt (s.re / 2)).mem_nhds hsU)).differentiableWithinAt

/-- Convex open charts that avoid the pole `s = 1`. -/
lemma isOpen_re_gt_im_pos (δ : ℝ) :
    IsOpen ({s : ℂ | δ < s.re} ∩ {s | (0 : ℝ) < s.im}) :=
  (isOpen_re_gt δ).inter (isOpen_lt continuous_const continuous_im)

lemma isOpen_re_gt_im_neg (δ : ℝ) :
    IsOpen ({s : ℂ | δ < s.re} ∩ {s | s.im < (0 : ℝ)}) :=
  (isOpen_re_gt δ).inter (isOpen_lt continuous_im continuous_const)

lemma isOpen_re_mem_Ioo (δ : ℝ) :
    IsOpen {s : ℂ | δ < s.re ∧ s.re < (1 : ℝ)} :=
  (isOpen_re_gt δ).inter (isOpen_lt continuous_re continuous_const)

noncomputable def zetaNOneRHS (s : ℂ) : ℂ :=
  s / (s - 1) - s * zetaFractIntegral s

lemma differentiableOn_zetaNOneRHS_re_gt {δ : ℝ} (hδ : 0 < δ)
    {U : Set ℂ} (hU : U ⊆ {s | δ < s.re}) (h1 : 1 ∉ U) :
    DifferentiableOn ℂ zetaNOneRHS U := by
  have hI := (differentiableOn_zetaFractIntegral_re_gt hδ).mono hU
  refine DifferentiableOn.sub ?_ ?_
  · intro s hs
    have hs1 : s ≠ 1 := fun h => h1 (h ▸ hs)
    exact ((differentiableAt_id (x := s)).div
      (differentiableAt_id.sub_const (1 : ℂ))
      (sub_ne_zero.mpr hs1)).differentiableWithinAt
  · exact differentiable_id.differentiableOn.mul hI

/-- Identity on the upper open half of `{Re > δ}`. -/
lemma riemannZeta_eq_zetaNOneRHS_of_re_gt_im_pos {δ : ℝ} (hδ : 0 < δ)
    {s : ℂ} (hs : δ < s.re) (him : 0 < s.im) :
    riemannZeta s = zetaNOneRHS s := by
  let U : Set ℂ := {z | δ < z.re} ∩ {z | (0 : ℝ) < z.im}
  have hUo : IsOpen U := isOpen_re_gt_im_pos δ
  have hUc : IsPreconnected U :=
    ((convex_halfSpace_re_gt δ).inter (convex_halfSpace_im_gt (0 : ℝ))).isPreconnected
  have h1 : (1 : ℂ) ∉ U := by intro h; simp [U] at h
  have hz0 : ((δ + 2 : ℝ) : ℂ) + I ∈ U := by
    simp [U, add_re, add_im, I_re, I_im]
  have heq : riemannZeta =ᶠ[𝓝 (((δ + 2 : ℝ) : ℂ) + I)] zetaNOneRHS := by
    have hopen : IsOpen {z : ℂ | (1 : ℝ) < z.re} := isOpen_re_gt 1
    have hmem : (1 : ℝ) < (((δ + 2 : ℝ) : ℂ) + I).re := by
      simp [add_re, I_re]; linarith
    refine eventually_of_mem (hopen.mem_nhds hmem) ?_
    intro z hz
    simpa [zetaNOneRHS] using riemannZeta_eq_s_div_sub_s_mul_fractIntegral hz
  have hf : AnalyticOnNhd ℂ riemannZeta U :=
    analyticOnNhd_riemannZeta_compl_one.mono fun z hz => by
      intro h; exact h1 (h ▸ hz)
  have hg : AnalyticOnNhd ℂ zetaNOneRHS U :=
    (differentiableOn_zetaNOneRHS_re_gt hδ (fun z hz => hz.1) h1).analyticOnNhd hUo
  exact hf.eqOn_of_preconnected_of_eventuallyEq hg hUc hz0 heq ⟨hs, him⟩

/-- Identity on the lower open half of `{Re > δ}`. -/
lemma riemannZeta_eq_zetaNOneRHS_of_re_gt_im_neg {δ : ℝ} (hδ : 0 < δ)
    {s : ℂ} (hs : δ < s.re) (him : s.im < 0) :
    riemannZeta s = zetaNOneRHS s := by
  let U : Set ℂ := {z | δ < z.re} ∩ {z | z.im < (0 : ℝ)}
  have hUo : IsOpen U := isOpen_re_gt_im_neg δ
  have hUc : IsPreconnected U :=
    ((convex_halfSpace_re_gt δ).inter (convex_halfSpace_im_lt (0 : ℝ))).isPreconnected
  have h1 : (1 : ℂ) ∉ U := by intro h; simp [U] at h
  have hz0 : ((δ + 2 : ℝ) : ℂ) - I ∈ U := by
    simp [U, sub_re, sub_im, I_re, I_im]
  have heq : riemannZeta =ᶠ[𝓝 (((δ + 2 : ℝ) : ℂ) - I)] zetaNOneRHS := by
    have hopen : IsOpen {z : ℂ | (1 : ℝ) < z.re} := isOpen_re_gt 1
    have hmem : (1 : ℝ) < (((δ + 2 : ℝ) : ℂ) - I).re := by
      simp [sub_re, I_re]; linarith
    refine eventually_of_mem (hopen.mem_nhds hmem) ?_
    intro z hz
    simpa [zetaNOneRHS] using riemannZeta_eq_s_div_sub_s_mul_fractIntegral hz
  have hf : AnalyticOnNhd ℂ riemannZeta U :=
    analyticOnNhd_riemannZeta_compl_one.mono fun z hz => by
      intro h; exact h1 (h ▸ hz)
  have hg : AnalyticOnNhd ℂ zetaNOneRHS U :=
    (differentiableOn_zetaNOneRHS_re_gt hδ (fun z hz => hz.1) h1).analyticOnNhd hUo
  exact hf.eqOn_of_preconnected_of_eventuallyEq hg hUc hz0 heq ⟨hs, him⟩

/-- Identity on the open strip `{δ < Re s < 1}` (no pole). -/
lemma riemannZeta_eq_zetaNOneRHS_of_re_Ioo {δ : ℝ} (hδ : 0 < δ) (hδ1 : δ < 1)
    {s : ℂ} (hs : δ < s.re) (hs1 : s.re < 1) :
    riemannZeta s = zetaNOneRHS s := by
  let U : Set ℂ := {z | δ < z.re ∧ z.re < (1 : ℝ)}
  have hUo : IsOpen U := isOpen_re_mem_Ioo δ
  have hUc : IsPreconnected U :=
    ((convex_halfSpace_re_gt δ).inter (convex_halfSpace_re_lt (1 : ℝ))).isPreconnected
  have h1 : (1 : ℂ) ∉ U := by intro h; simp [U] at h
  have hz0 : (((δ + 1) / 2 : ℝ) : ℂ) + I ∈ U := by
    refine ⟨?_, ?_⟩
    · simp; linarith
    · simp; linarith
  have hr : 0 < min (min ((δ + 1) / 2 - δ) (1 - (δ + 1) / 2)) (1 / 2 : ℝ) := by
    refine lt_min (lt_min ?_ ?_) (by norm_num) <;> linarith
  let r := min (min ((δ + 1) / 2 - δ) (1 - (δ + 1) / 2)) (1 / 2 : ℝ)
  have heq : riemannZeta =ᶠ[𝓝 ((((δ + 1) / 2 : ℝ) : ℂ) + I)] zetaNOneRHS := by
    have hball : Metric.ball ((((δ + 1) / 2 : ℝ) : ℂ) + I) r ⊆
        {z | δ < z.re} ∩ {z | (0 : ℝ) < z.im} := by
      intro z hz
      have hd : ‖z - ((((δ + 1) / 2 : ℝ) : ℂ) + I)‖ < r := by
        simpa [dist_eq_norm] using Metric.mem_ball.mp hz
      have hre' : |(z - ((((δ + 1) / 2 : ℝ) : ℂ) + I)).re| < r :=
        (abs_re_le_norm _).trans_lt hd
      have him' : |(z - ((((δ + 1) / 2 : ℝ) : ℂ) + I)).im| < r :=
        (abs_im_le_norm _).trans_lt hd
      have hre : |z.re - (δ + 1) / 2| < r := by
        simpa [sub_re, add_re, I_re] using hre'
      have him : |z.im - 1| < r := by
        simpa [sub_im, add_im, I_im] using him'
      constructor
      · have hzre : (δ + 1) / 2 - r < z.re := by linarith [(abs_lt.mp hre).1]
        have hrle : r ≤ (δ + 1) / 2 - δ :=
          (min_le_left (min ((δ + 1) / 2 - δ) (1 - (δ + 1) / 2)) (1 / 2 : ℝ)).trans
            (min_le_left _ _)
        have hδle : δ ≤ (δ + 1) / 2 - r := by linarith
        exact hδle.trans_lt hzre
      · have hzim : 1 - r < z.im := by linarith [(abs_lt.mp him).1]
        have hrle : r ≤ (1 / 2 : ℝ) :=
          min_le_right (min ((δ + 1) / 2 - δ) (1 - (δ + 1) / 2)) (1 / 2 : ℝ)
        have hpos : (0 : ℝ) < 1 - r := by linarith
        exact hpos.trans hzim
    refine eventually_of_mem (Metric.isOpen_ball.mem_nhds (Metric.mem_ball_self hr)) ?_
    intro z hz
    have hz' := hball hz
    exact riemannZeta_eq_zetaNOneRHS_of_re_gt_im_pos hδ hz'.1 hz'.2
  have hf : AnalyticOnNhd ℂ riemannZeta U :=
    analyticOnNhd_riemannZeta_compl_one.mono fun z hz => by
      intro h; exact h1 (h ▸ hz)
  have hg : AnalyticOnNhd ℂ zetaNOneRHS U :=
    (differentiableOn_zetaNOneRHS_re_gt hδ (fun z hz => hz.1) h1).analyticOnNhd hUo
  exact hf.eqOn_of_preconnected_of_eventuallyEq hg hUc hz0 heq ⟨hs, hs1⟩

lemma riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos
    {s : ℂ} (hs : 0 < s.re) (h1 : s ≠ 1) :
    riemannZeta s = s / (s - 1) - s * zetaFractIntegral s := by
  by_cases hgt : 1 < s.re
  · exact riemannZeta_eq_s_div_sub_s_mul_fractIntegral hgt
  · have hδ : 0 < s.re / 2 := half_pos hs
    have hδ1 : s.re / 2 < 1 := by
      have : s.re ≤ 1 := le_of_not_gt hgt
      linarith
    have hs' : s.re / 2 < s.re := half_lt_self hs
    by_cases him : 0 < s.im
    · simpa [zetaNOneRHS] using
        riemannZeta_eq_zetaNOneRHS_of_re_gt_im_pos hδ hs' him
    · by_cases himn : s.im < 0
      · simpa [zetaNOneRHS] using
          riemannZeta_eq_zetaNOneRHS_of_re_gt_im_neg hδ hs' himn
      · have him0 : s.im = 0 := le_antisymm (not_lt.mp him) (not_lt.mp himn)
        have hs1 : s.re < 1 := lt_of_le_of_ne (not_lt.mp hgt) ?_
        · simpa [zetaNOneRHS] using
            riemannZeta_eq_zetaNOneRHS_of_re_Ioo hδ hδ1 hs' hs1
        · intro hre
          exact h1 (Complex.ext hre him0)

lemma norm_zetaFractIntegral_le_of_re_gt {δ : ℝ} (hδ : 0 < δ) {s : ℂ}
    (hs : δ < s.re) :
    ‖zetaFractIntegral s‖ ≤ ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
  have hle : ∀ n, ‖zetaFractCell n s‖ ≤ ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) :=
    fun n => norm_zetaFractCell_le_rpow_of_re_gt n hδ hs
  have hu : Summable fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
    refine (summable_congr fun n => ?_).mp
      (summable_rpow_neg_succ (p := δ + 1) (by linarith))
    congr 1
    ring
  have hnorm : Summable fun n : ℕ => ‖zetaFractCell n s‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hle hu
  refine (norm_tsum_le_tsum_norm (f := fun n => zetaFractCell n s) hnorm).trans ?_
  exact hnorm.tsum_mono hu hle

/-- **r509 (4).** Γ-free polynomial bound on `{Re s > δ} ∩ {|s-1| ≥ 1/2}`. -/
lemma norm_riemannZeta_le_of_re_gt {δ : ℝ} (hδ : 0 < δ) {s : ℂ}
    (hs : δ < s.re) (h1 : s ≠ 1)
    (hsep : (1 / 2 : ℝ) ≤ ‖s - 1‖) :
    ‖riemannZeta s‖ ≤
      (2 + ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1)) * (1 + ‖s‖) := by
  have hform := riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos
    (lt_trans hδ hs) h1
  rw [hform]
  have hI := norm_zetaFractIntegral_le_of_re_gt hδ hs
  have hleft : ‖s / (s - 1)‖ ≤ 2 * ‖s‖ := by
    rw [norm_div]
    refine (div_le_div_of_nonneg_left (norm_nonneg s)
      (by positivity : (0 : ℝ) < 1 / 2) hsep).trans ?_
    field_simp
    exact le_rfl
  have hright : ‖s * zetaFractIntegral s‖ ≤
      ‖s‖ * ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
    rw [norm_mul]
    exact mul_le_mul_of_nonneg_left hI (norm_nonneg s)
  refine (norm_sub_le _ _).trans ?_
  refine (add_le_add hleft hright).trans ?_
  have hz : 0 ≤ ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) :=
    tsum_nonneg fun _ => Real.rpow_nonneg (Nat.cast_nonneg _) _
  nlinarith [norm_nonneg s]

/-- **r510.** Filling bound without `|s-1| ≥ 1/2`:
`|(s-1)ζ(s)| = |s - s(s-1)I(s)|` on `Re s > δ`. -/
lemma norm_riemannZetaMulSubOne_le_of_re_gt {δ : ℝ} (hδ : 0 < δ) {s : ℂ}
    (hs : δ < s.re) :
    ‖riemannZetaMulSubOne s‖ ≤
      ‖s‖ + ‖s‖ * (‖s‖ + 1) *
        ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
  let C := ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1)
  have hC : 0 ≤ C :=
    tsum_nonneg fun _ => Real.rpow_nonneg (Nat.cast_nonneg _) _
  by_cases h1 : s = 1
  · subst h1
    rw [riemannZetaMulSubOne_one, norm_one]
    nlinarith [norm_nonneg (1 : ℂ)]
  · have hform :=
      riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos (lt_trans hδ hs) h1
    have halg :
        (s - 1) * (s / (s - 1) - s * zetaFractIntegral s) =
          s - s * (s - 1) * zetaFractIntegral s := by
      have hne : s - 1 ≠ 0 := sub_ne_zero.mpr h1
      field_simp [hne]
    rw [riemannZetaMulSubOne_apply_of_ne h1, hform, halg]
    have hI : ‖zetaFractIntegral s‖ ≤ C :=
      norm_zetaFractIntegral_le_of_re_gt hδ hs
    refine (norm_sub_le _ _).trans ?_
    have hright :
        ‖s * (s - 1) * zetaFractIntegral s‖ ≤ ‖s‖ * (‖s‖ + 1) * C := by
      have hsm1 : ‖s - 1‖ ≤ ‖s‖ + 1 :=
        (norm_sub_le s 1).trans (by simp)
      rw [mul_assoc, norm_mul, norm_mul, mul_assoc]
      refine mul_le_mul_of_nonneg_left ?_ (norm_nonneg s)
      exact mul_le_mul hsm1 hI (norm_nonneg _)
        (add_nonneg (norm_nonneg s) zero_le_one)
    exact add_le_add le_rfl hright

/-- **r510.** Centre lower bound: `|F(2+iT)| ≥ 1/|ζ(2)|`. -/
lemma norm_riemannZetaMulSubOne_center_ge (T : ℝ) :
    ‖riemannZeta 2‖⁻¹ ≤ ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ := by
  set c := (2 : ℂ) + T * I
  have hc : c ≠ 1 := by
    intro h
    have : c.re = (1 : ℂ).re := congrArg Complex.re h
    simp [c] at this
  have hre : (2 : ℝ) ≤ c.re := by simp [c]
  have hz : riemannZeta c ≠ 0 :=
    riemannZeta_ne_zero_of_one_lt_re (by simp [c])
  have hinv : ‖riemannZeta c‖⁻¹ ≤ ‖riemannZeta 2‖ := by
    simpa [norm_inv] using normInvRiemannZetaLeZetaTwo c hre
  have hζ2pos : 0 < ‖riemannZeta 2‖ := by
    rw [norm_riemannZeta_two]; positivity
  have hζpos : 0 < ‖riemannZeta c‖ := norm_pos_iff.mpr hz
  have hζ : ‖riemannZeta 2‖⁻¹ ≤ ‖riemannZeta c‖ := by
    rw [inv_le_iff_one_le_mul₀ hζpos] at hinv
    exact (inv_le_iff_one_le_mul₀ hζ2pos).mpr (by rwa [mul_comm] at hinv)
  rw [riemannZetaMulSubOne_apply_of_ne hc, norm_mul]
  have hfac : (1 : ℝ) ≤ ‖c - 1‖ := by
    have heq : ‖c - 1‖ = Real.sqrt (1 + T ^ 2) := by
      rw [Complex.norm_eq_sqrt_sq_add_sq]
      simp [c, add_re, add_im, sub_re, sub_im, mul_re, mul_im, I_re, I_im]
      ring_nf
    rw [heq]
    exact (Real.le_sqrt (by norm_num) (by positivity)).mpr
      (by nlinarith [sq_nonneg T])
  nlinarith [hζ, norm_nonneg (riemannZeta c),
    inv_nonneg.mpr (norm_nonneg (riemannZeta 2))]

/-- r499 witness restricted to a closed disk. -/
noncomputable def riemannZetaZerosInClosedDisk (c : ℂ) (r : ℝ) : Finset ℂ :=
  (finite_riemannZeta_zeros_of_isCompact_ne_one
    (isCompact_closedBall c |r|)).toFinset

lemma mem_riemannZetaZerosInClosedDisk {c : ℂ} {r : ℝ} {z : ℂ} :
    z ∈ riemannZetaZerosInClosedDisk c r ↔
      z ∈ Metric.closedBall c |r| ∧ riemannZeta z = 0 ∧ z ≠ 1 :=
  Set.Finite.mem_toFinset _

lemma riemannZetaMulSubOne_eq_zero_iff {z : ℂ} :
    riemannZetaMulSubOne z = 0 ↔ riemannZeta z = 0 ∧ z ≠ 1 := by
  by_cases h1 : z = 1
  · subst h1
    simp [riemannZetaMulSubOne_one]
  · rw [riemannZetaMulSubOne_apply_of_ne h1, mul_eq_zero]
    constructor
    · intro h
      rcases h with h | h
      · exact absurd (sub_eq_zero.mp h) h1
      · exact ⟨h, h1⟩
    · exact fun h => Or.inr h.1

lemma riemannZetaMulSubOne_meromorphicOrderAt_ne_top (z : ℂ) :
    meromorphicOrderAt riemannZetaMulSubOne z ≠ ⊤ := by
  intro htop
  have hAn := analyticAt_riemannZetaMulSubOne z
  have hANtop : analyticOrderAt riemannZetaMulSubOne z = ⊤ := by
    rw [hAn.meromorphicOrderAt_eq] at htop
    exact ENat.map_eq_top_iff.mp htop
  have heq : riemannZetaMulSubOne =ᶠ[𝓝 z] 0 :=
    analyticOrderAt_eq_top.mp hANtop
  have heqOn :=
    analyticOnNhd_riemannZetaMulSubOne.eqOn_of_preconnected_of_eventuallyEq
      analyticOnNhd_const isPreconnected_univ (mem_univ z) heq
      (mem_univ (2 : ℂ))
  have h2 : riemannZetaMulSubOne 2 = 0 := heqOn
  rw [riemannZetaMulSubOne_apply_of_ne (by norm_num : (2 : ℂ) ≠ 1),
    mul_eq_zero] at h2
  rcases h2 with h2 | h2
  · exact (by norm_num : (2 : ℂ) - 1 ≠ 0) h2
  · exact riemannZeta_ne_zero_of_one_lt_re (by norm_num) h2

lemma riemannZetaMulSubOne_divisor_ge_one_of_zero {z : ℂ}
    (hz : riemannZetaMulSubOne z = 0) {U : Set ℂ}
    (hU : MeromorphicOn riemannZetaMulSubOne U) (hzU : z ∈ U) :
    (1 : ℤ) ≤ MeromorphicOn.divisor riemannZetaMulSubOne U z := by
  have hAn := analyticAt_riemannZetaMulSubOne z
  have hAnNe : analyticOrderAt riemannZetaMulSubOne z ≠ ⊤ := by
    intro htop
    exact riemannZetaMulSubOne_meromorphicOrderAt_ne_top z (by
      rw [hAn.meromorphicOrderAt_eq, htop]; simp)
  obtain ⟨n, hn⟩ := ENat.ne_top_iff_exists.mp hAnNe
  have hn0 : n ≠ 0 := by
    intro h0
    have : analyticOrderAt riemannZetaMulSubOne z = 0 := by
      rw [← hn]; simp [h0]
    exact (hAn.analyticOrderAt_eq_zero.mp this) hz
  rw [MeromorphicOn.divisor_apply hU hzU, hAn.meromorphicOrderAt_eq, ← hn]
  simp
  exact Nat.one_le_iff_ne_zero.mpr hn0

noncomputable def zetaFractCellMajorant (δ : ℝ) : ℝ :=
  ∑' n : ℕ, ((n + 1 : ℕ) : ℝ) ^ (-δ - 1)

lemma summable_zetaFractCellMajorant {δ : ℝ} (hδ : 0 < δ) :
    Summable fun n : ℕ => ((n + 1 : ℕ) : ℝ) ^ (-δ - 1) := by
  refine (summable_congr fun n => ?_).mp
    (summable_rpow_neg_succ (p := δ + 1) (by linarith))
  congr 1
  ring

lemma zetaFractCellMajorant_nonneg {δ : ℝ} :
    0 ≤ zetaFractCellMajorant δ :=
  tsum_nonneg fun _ => Real.rpow_nonneg (Nat.cast_nonneg _) _

/-- **r511 geometry.** On `|z-(2+iT)|=7/4` one has `Re z ≥ 1/4 > 1/8`. -/
lemma re_gt_one_div_eight_of_mem_jensen_sphere {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.sphere ((2 : ℂ) + T * I) (7 / 4)) :
    (1 / 8 : ℝ) < z.re := by
  have hdist : ‖z - ((2 : ℂ) + T * I)‖ = (7 / 4 : ℝ) := by
    simpa [dist_eq_norm] using Metric.mem_sphere.mp hz
  have hre : |z.re - 2| ≤ (7 / 4 : ℝ) := by
    have h := abs_re_le_norm (z - ((2 : ℂ) + T * I))
    have hre' : (z - ((2 : ℂ) + T * I)).re = z.re - 2 := by
      simp [sub_re, add_re, mul_re, I_re]
    rwa [hre', hdist] at h
  have : (1 / 4 : ℝ) ≤ z.re := by
    have := (abs_le.mp hre).1
    linarith
  linarith

/-- **r511 geometry.** On `|z-(2+iT)|=7/4` one has `|z| ≤ 4+|T|`. -/
lemma norm_le_four_add_abs_of_mem_jensen_sphere {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.sphere ((2 : ℂ) + T * I) (7 / 4)) :
    ‖z‖ ≤ 4 + |T| := by
  set c := (2 : ℂ) + T * I
  have hdist : ‖z - c‖ = (7 / 4 : ℝ) := by
    simpa [dist_eq_norm, c] using Metric.mem_sphere.mp hz
  have hzc : ‖z‖ ≤ ‖c‖ + 7 / 4 := by
    have hzeq : z = c + (z - c) := by rw [add_comm, sub_add_cancel]
    rw [hzeq]
    calc
      ‖c + (z - c)‖ ≤ ‖c‖ + ‖z - c‖ := norm_add_le _ _
      _ = ‖c‖ + 7 / 4 := by rw [hdist]
  have hc : ‖c‖ ≤ 2 + |T| := by
    calc
      ‖c‖ ≤ ‖(2 : ℂ)‖ + ‖T * I‖ := norm_add_le _ _
      _ = 2 + |T| := by simp [c, norm_mul, Complex.norm_I]
  nlinarith

/-- **r511.** Filling bound on the Jensen circle; `δ = 1/8` (the
leftmost point has `Re = 1/4`, so the strict `δ < Re` of r510
forbids `δ = 1/4`). -/
lemma norm_riemannZetaMulSubOne_le_on_jensen_sphere (T : ℝ) {z : ℂ}
    (hz : z ∈ Metric.sphere ((2 : ℂ) + T * I) (7 / 4)) :
    ‖riemannZetaMulSubOne z‖ ≤
      (4 + |T|) + (4 + |T|) * (5 + |T|) * zetaFractCellMajorant (1 / 8) := by
  have hδ : (0 : ℝ) < 1 / 8 := by norm_num
  have hre := re_gt_one_div_eight_of_mem_jensen_sphere hz
  have hnorm := norm_le_four_add_abs_of_mem_jensen_sphere hz
  have hbound := norm_riemannZetaMulSubOne_le_of_re_gt hδ hre
  have hCI : 0 ≤ zetaFractCellMajorant (1 / 8) := zetaFractCellMajorant_nonneg
  have hz1 : ‖z‖ + 1 ≤ (4 + |T|) + 1 := by linarith [hnorm]
  have h51 : (4 + |T|) + 1 = 5 + |T| := by ring
  have hbound' : ‖riemannZetaMulSubOne z‖ ≤
      ‖z‖ + ‖z‖ * (‖z‖ + 1) * zetaFractCellMajorant (1 / 8) := by
    simpa [zetaFractCellMajorant] using hbound
  have hprod : ‖z‖ * (‖z‖ + 1) * zetaFractCellMajorant (1 / 8) ≤
      (4 + |T|) * (5 + |T|) * zetaFractCellMajorant (1 / 8) := by
    rw [← h51]
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul hnorm hz1 (add_nonneg (norm_nonneg z) zero_le_one)
        (add_nonneg (by norm_num : (0 : ℝ) ≤ 4) (abs_nonneg T)))
      hCI
  exact hbound'.trans (add_le_add hnorm hprod)

noncomputable def jensenSphereMajorant (T : ℝ) : ℝ :=
  max 1 ((4 + |T|) + (4 + |T|) * (5 + |T|) * zetaFractCellMajorant (1 / 8))

lemma one_le_jensenSphereMajorant (T : ℝ) : 1 ≤ jensenSphereMajorant T :=
  le_max_left _ _

lemma norm_riemannZetaMulSubOne_le_jensenSphereMajorant (T : ℝ) {z : ℂ}
    (hz : z ∈ Metric.sphere ((2 : ℂ) + T * I) (7 / 4)) :
    ‖riemannZetaMulSubOne z‖ ≤ jensenSphereMajorant T :=
  (norm_riemannZetaMulSubOne_le_on_jensen_sphere T hz).trans (le_max_right _ _)

lemma riemannZetaMulSubOne_center_ne_zero (T : ℝ) :
    riemannZetaMulSubOne ((2 : ℂ) + T * I) ≠ 0 := by
  have hζ2 : 0 < ‖riemannZeta 2‖ := by
    rw [norm_riemannZeta_two]; positivity
  exact norm_pos_iff.mp
    (lt_of_lt_of_le (inv_pos.mpr hζ2) (norm_riemannZetaMulSubOne_center_ge T))

lemma riemannZetaMulSubOne_meromorphicOn_closedBall (c : ℂ) (R : ℝ) :
    MeromorphicOn riemannZetaMulSubOne (Metric.closedBall c |R|) :=
  (AnalyticOnNhd.mono analyticOnNhd_riemannZetaMulSubOne
    (Set.subset_univ _)).meromorphicOn

lemma riemannZetaMulSubOne_divisor_center
    (T : ℝ) :
    MeromorphicOn.divisor riemannZetaMulSubOne
        (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|)
        ((2 : ℂ) + T * I) = 0 := by
  set c := (2 : ℂ) + T * I
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hcmem : c ∈ Metric.closedBall c |7 / 4| :=
    Metric.mem_closedBall_self (abs_nonneg _)
  have hfc := riemannZetaMulSubOne_center_ne_zero T
  rw [MeromorphicOn.divisor_apply hmer hcmem,
    (analyticAt_riemannZetaMulSubOne c).meromorphicOrderAt_eq,
    (analyticAt_riemannZetaMulSubOne c).analyticOrderAt_eq_zero.mpr hfc]
  simp

/-- **r511 (i).** Jensen identity for the filling on `D(2+iT, 7/4)`. -/
lemma riemannZetaMulSubOne_jensen_identity (T : ℝ) :
    Real.circleAverage (fun z => Real.log ‖riemannZetaMulSubOne z‖)
        ((2 : ℂ) + T * I) (7 / 4) =
      ∑ᶠ u, (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) *
        Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) +
      Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ := by
  set c := (2 : ℂ) + T * I
  have hR : (7 / 4 : ℝ) ≠ 0 := by norm_num
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hj := MeromorphicOn.circleAverage_log_norm (c := c) (R := (7 / 4 : ℝ))
    hR hmer
  have htrail :
      meromorphicTrailingCoeffAt riemannZetaMulSubOne c =
        riemannZetaMulSubOne c :=
    (analyticAt_riemannZetaMulSubOne c).meromorphicTrailingCoeffAt_of_ne_zero
      (riemannZetaMulSubOne_center_ne_zero T)
  have hDc := riemannZetaMulSubOne_divisor_center T
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  simpa [c, htrail, hDc, hRabs, Int.cast_zero, zero_mul, add_zero] using hj

lemma riemannZetaMulSubOne_circleIntegrable_log (T : ℝ) :
    CircleIntegrable (fun z => Real.log ‖riemannZetaMulSubOne z‖)
      ((2 : ℂ) + T * I) (7 / 4) := by
  set c := (2 : ℂ) + T * I
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  exact circleIntegrable_log_norm_meromorphicOn
    (hmer.mono_set (by rw [hRabs]; exact Metric.sphere_subset_closedBall))

/-- **r511 (i).** `circleAverage log‖F‖ ≤ log M` via the constant function. -/
lemma riemannZetaMulSubOne_jensen_avg_le (T : ℝ) :
    Real.circleAverage (fun z => Real.log ‖riemannZetaMulSubOne z‖)
        ((2 : ℂ) + T * I) (7 / 4) ≤
      Real.log (jensenSphereMajorant T) := by
  refine Real.circleAverage_mono_on_of_le_circle
    (riemannZetaMulSubOne_circleIntegrable_log T) ?_
  intro z hz
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hz' : z ∈ Metric.sphere ((2 : ℂ) + T * I) (7 / 4) := by
    simpa [hRabs] using hz
  by_cases hfz : riemannZetaMulSubOne z = 0
  · rw [hfz, norm_zero, Real.log_zero]
    exact Real.log_nonneg (one_le_jensenSphereMajorant T)
  · exact Real.log_le_log (norm_pos_iff.mpr hfz)
      (norm_riemannZetaMulSubOne_le_jensenSphereMajorant T hz')

lemma riemannZetaMulSubOne_jensen_sum_le (T : ℝ) :
    ∑ᶠ u, (MeromorphicOn.divisor riemannZetaMulSubOne
        (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) *
      Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) ≤
      Real.log (jensenSphereMajorant T) -
        Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ := by
  have hid := riemannZetaMulSubOne_jensen_identity T
  have havg := riemannZetaMulSubOne_jensen_avg_le T
  linarith

lemma riemannZetaMulSubOne_divisor_nonneg (T : ℝ) (u : ℂ) :
    0 ≤ (MeromorphicOn.divisor riemannZetaMulSubOne
      (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) := by
  set c := (2 : ℂ) + T * I
  set U := Metric.closedBall c |7 / 4|
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  by_cases hu : u ∈ U
  · by_cases hz : riemannZetaMulSubOne u = 0
    · have hge := riemannZetaMulSubOne_divisor_ge_one_of_zero hz hmer hu
      exact_mod_cast (le_trans (by norm_num : (0 : ℤ) ≤ 1) hge)
    · have hAn := analyticAt_riemannZetaMulSubOne u
      rw [MeromorphicOn.divisor_apply hmer hu, hAn.meromorphicOrderAt_eq,
        hAn.analyticOrderAt_eq_zero.mpr hz]
      simp
  · have : MeromorphicOn.divisor riemannZetaMulSubOne U u = 0 := by
      simp [MeromorphicOn.divisor_def, hu]
    simp [this]

lemma jensen_log_weight_nonneg (T : ℝ) {u : ℂ}
    (hu : u ∈ Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) :
    0 ≤ Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) := by
  set c := (2 : ℂ) + T * I
  by_cases h : c = u
  · subst h
    simp
  · have hpos : 0 < ‖c - u‖ := norm_pos_iff.mpr (sub_ne_zero.mpr h)
    have hle : ‖c - u‖ ≤ (7 / 4 : ℝ) := by
      have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
      have : ‖u - c‖ ≤ (7 / 4 : ℝ) := by
        simpa [dist_eq_norm, c, hRabs] using Metric.mem_closedBall.mp hu
      rwa [norm_sub_rev] at this
    apply Real.log_nonneg
    rw [← div_eq_mul_inv, le_div_iff₀ hpos]
    simpa [mul_one] using hle

lemma mem_jensen_support_of_mem_disk {T : ℝ} {z : ℂ}
    (hz : z ∈ riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)) :
    z ∈ (MeromorphicOn.divisor riemannZetaMulSubOne
      (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|)).support := by
  set c := (2 : ℂ) + T * I
  have hz' := mem_riemannZetaZerosInClosedDisk.mp hz
  have hrabs : |(3 / 2 : ℝ)| = (3 / 2 : ℝ) := abs_of_pos (by norm_num)
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hzF : riemannZetaMulSubOne z = 0 :=
    riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
  have hzB : z ∈ Metric.closedBall c |7 / 4| := by
    have : (3 / 2 : ℝ) ≤ (7 / 4 : ℝ) := by norm_num
    have hzball : z ∈ Metric.closedBall c (3 / 2) := by
      simpa [c, hrabs] using hz'.1
    exact Metric.closedBall_subset_closedBall (by simpa [hRabs] using this) hzball
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hge := riemannZetaMulSubOne_divisor_ge_one_of_zero hzF hmer hzB
  exact fun h0 => by linarith [hge, h0]

/-- **r511 (ii)+(iii).** Inner zeros contribute at least `log(7/6)` each. -/
lemma zetaZerosInDisk_card_mul_log_le (T : ℝ) :
    ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)).card : ℝ) *
        Real.log (7 / 6 : ℝ) ≤
      ∑ᶠ u, (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) *
        Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) := by
  set c := (2 : ℂ) + T * I
  set D := MeromorphicOn.divisor riemannZetaMulSubOne (Metric.closedBall c |7 / 4|)
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hfin : D.support.Finite :=
    D.finiteSupport (isCompact_closedBall c |7 / 4|)
  set s := hfin.toFinset
  set Z := riemannZetaZerosInClosedDisk c (3 / 2)
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hrabs : |(3 / 2 : ℝ)| = (3 / 2 : ℝ) := abs_of_pos (by norm_num)
  have hZsub : Z ⊆ s := by
    intro z hz
    exact hfin.mem_toFinset.mpr (mem_jensen_support_of_mem_disk (by simpa [Z, c] using hz))
  have htermnn : ∀ u ∈ s, 0 ≤ (D u : ℝ) *
      Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := by
    intro u hu
    have huB : u ∈ Metric.closedBall c |7 / 4| :=
      D.supportWithinDomain (hfin.mem_toFinset.mp hu)
    exact mul_nonneg (riemannZetaMulSubOne_divisor_nonneg T u)
      (jensen_log_weight_nonneg T huB)
  have hsupp :
      (fun u => (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹)).support ⊆ s := by
    intro u hu
    have : D u ≠ 0 := by
      intro h0
      simp [h0] at hu
    exact hfin.mem_toFinset.mpr this
  have hleft :
      ∑ z ∈ Z, Real.log (7 / 6 : ℝ) ≤
        ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
    refine Finset.sum_le_sum ?_
    intro z hz
    have hz' := mem_riemannZetaZerosInClosedDisk.mp (by simpa [Z, c] using hz)
    have hzF : riemannZetaMulSubOne z = 0 :=
      riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
    have hzB : z ∈ Metric.closedBall c |7 / 4| := by
      have : (3 / 2 : ℝ) ≤ (7 / 4 : ℝ) := by norm_num
      have hzball : z ∈ Metric.closedBall c (3 / 2) := by
        simpa [c, hrabs] using hz'.1
      exact Metric.closedBall_subset_closedBall (by simpa [hRabs] using this) hzball
    have hge : (1 : ℝ) ≤ (D z : ℝ) := by
      exact_mod_cast (riemannZetaMulSubOne_divisor_ge_one_of_zero hzF hmer hzB)
    have hzc : z ≠ c := by
      intro h
      exact riemannZetaMulSubOne_center_ne_zero T (by simpa [c, h] using hzF)
    have hpos : 0 < ‖c - z‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hzc.symm)
    have hle : ‖c - z‖ ≤ (3 / 2 : ℝ) := by
      have : dist z c ≤ (3 / 2 : ℝ) := by
        simpa [c, hrabs, Metric.mem_closedBall] using hz'.1
      simpa [dist_eq_norm, norm_sub_rev] using this
    have hlogle : Real.log (7 / 6 : ℝ) ≤
        Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
      apply Real.log_le_log (by positivity)
      rw [← div_eq_mul_inv, div_le_div_iff₀ (by positivity) hpos]
      nlinarith
    have hlogpos : 0 ≤ Real.log (7 / 6 : ℝ) :=
      le_of_lt (Real.log_pos (by norm_num))
    nlinarith [riemannZetaMulSubOne_divisor_nonneg T z]
  have hmid :
      ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) ≤
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    Finset.sum_le_sum_of_subset_of_nonneg hZsub fun u hu _ => htermnn u hu
  have hcard : ∑ z ∈ Z, Real.log (7 / 6 : ℝ) =
      (Z.card : ℝ) * Real.log (7 / 6 : ℝ) := by simp
  have hfinsum :
      ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) =
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    finsum_eq_sum_of_support_subset _ hsupp
  calc
    (Z.card : ℝ) * Real.log (7 / 6 : ℝ) = ∑ z ∈ Z, Real.log (7 / 6 : ℝ) := hcard.symm
    _ ≤ ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
      hleft.trans hmid
    _ = ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := hfinsum.symm

noncomputable def jensenSphereMajorantCoeff : ℝ :=
  2 + 6 * zetaFractCellMajorant (1 / 8)

lemma jensenSphereMajorantCoeff_pos : 0 < jensenSphereMajorantCoeff := by
  have hCI : 0 ≤ zetaFractCellMajorant (1 / 8) :=
    zetaFractCellMajorant_nonneg
  unfold jensenSphereMajorantCoeff
  linarith

lemma jensenSphereMajorant_le_coeff_mul_sq (T : ℝ) :
    jensenSphereMajorant T ≤
      jensenSphereMajorantCoeff * (2 + |T|) ^ 2 := by
  set s := (2 : ℝ) + |T|
  set CI := zetaFractCellMajorant (1 / 8)
  have hs : (1 : ℝ) ≤ s := by nlinarith [abs_nonneg T]
  have h4 : 4 + |T| ≤ 2 * s := by nlinarith [abs_nonneg T]
  have h5 : 5 + |T| ≤ 3 * s := by nlinarith [abs_nonneg T]
  have hCI : 0 ≤ CI := zetaFractCellMajorant_nonneg
  have hpoly :
      (4 + |T|) + (4 + |T|) * (5 + |T|) * CI ≤ 2 * s + (2 * s) * (3 * s) * CI := by
    have ha : 0 ≤ 4 + |T| := add_nonneg (by norm_num) (abs_nonneg T)
    have hb : 0 ≤ 5 + |T| := add_nonneg (by norm_num) (abs_nonneg T)
    have hprod1 : (4 + |T|) * (5 + |T|) ≤ (2 * s) * (3 * s) :=
      mul_le_mul h4 h5 hb (mul_nonneg (by norm_num) (le_trans zero_le_one hs))
    have hprod : (4 + |T|) * (5 + |T|) * CI ≤ (2 * s) * (3 * s) * CI :=
      mul_le_mul_of_nonneg_right hprod1 hCI
    linarith
  have hsimp : 2 * s + (2 * s) * (3 * s) * CI ≤ (2 + 6 * CI) * s ^ 2 := by
    have hs2 : s ≤ s ^ 2 :=
      calc
        s = s * 1 := (mul_one s).symm
        _ ≤ s * s := mul_le_mul_of_nonneg_left hs (le_trans zero_le_one hs)
        _ = s ^ 2 := (sq s).symm
    nlinarith [hCI]
  have hpoly' : (4 + |T|) + (4 + |T|) * (5 + |T|) * CI ≤
      jensenSphereMajorantCoeff * s ^ 2 := by
    unfold jensenSphereMajorantCoeff
    exact hpoly.trans hsimp
  have h1 : (1 : ℝ) ≤ jensenSphereMajorantCoeff * s ^ 2 := by
    have hs2 : (1 : ℝ) ≤ s ^ 2 := one_le_pow₀ hs
    nlinarith [jensenSphereMajorantCoeff_pos]
  unfold jensenSphereMajorant
  exact (max_le h1 hpoly').trans_eq (by rfl)

lemma log_jensenSphereMajorant_le (T : ℝ) :
    Real.log (jensenSphereMajorant T) ≤
      Real.log jensenSphereMajorantCoeff + 2 * Real.log (2 + |T|) := by
  have hK : 0 < jensenSphereMajorantCoeff := jensenSphereMajorantCoeff_pos
  have hs : 0 < 2 + |T| := by positivity
  have hMpos : 0 < jensenSphereMajorant T :=
    lt_of_lt_of_le zero_lt_one (one_le_jensenSphereMajorant T)
  have hle := jensenSphereMajorant_le_coeff_mul_sq T
  have := Real.log_le_log hMpos hle
  rwa [Real.log_mul (ne_of_gt hK) (pow_ne_zero 2 (ne_of_gt hs)),
    Real.log_pow] at this

lemma log_center_neg_le (T : ℝ) :
    -Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ ≤
      Real.log ‖riemannZeta 2‖ := by
  have hζ2 : 0 < ‖riemannZeta 2‖ := by
    rw [norm_riemannZeta_two]; positivity
  have hge := norm_riemannZetaMulSubOne_center_ge T
  have hlog : Real.log ‖riemannZeta 2‖⁻¹ ≤
      Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ :=
    Real.log_le_log (inv_pos.mpr hζ2) hge
  rw [Real.log_inv] at hlog
  linarith [hlog]

/-- Explicit Jensen disk-card constant:
`C = (log K + log‖ζ(2)‖ + 2) / log(7/6)` with
`K = 2 + 6·∑(n+1)^{-9/8}`. -/
noncomputable def zetaZerosInDiskCardBound : ℝ :=
  (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) /
    Real.log (7 / 6 : ℝ)

lemma one_lt_jensenSphereMajorantCoeff :
    (1 : ℝ) < jensenSphereMajorantCoeff := by
  have h2 : (2 : ℝ) ≤ jensenSphereMajorantCoeff := by
    unfold jensenSphereMajorantCoeff
    linarith [zetaFractCellMajorant_nonneg (δ := 1 / 8)]
  exact lt_of_lt_of_le (by norm_num : (1 : ℝ) < 2) h2

lemma one_lt_norm_riemannZeta_two : (1 : ℝ) < ‖riemannZeta 2‖ := by
  rw [norm_riemannZeta_two]
  have hπ : (3 : ℝ) < Real.pi := Real.pi_gt_three
  nlinarith

lemma zetaZerosInDiskCardBound_pos : 0 < zetaZerosInDiskCardBound := by
  have hnum : 0 < Real.log jensenSphereMajorantCoeff +
      Real.log ‖riemannZeta 2‖ + 2 := by
    have h1 : 0 < Real.log jensenSphereMajorantCoeff :=
      Real.log_pos one_lt_jensenSphereMajorantCoeff
    have h2 : 0 < Real.log ‖riemannZeta 2‖ :=
      Real.log_pos one_lt_norm_riemannZeta_two
    linarith
  have hden : 0 < Real.log (7 / 6 : ℝ) := Real.log_pos (by norm_num)
  unfold zetaZerosInDiskCardBound
  exact div_pos hnum hden

/-- **r511.** Disk zero count: `card ≤ C · (1 + log(2+|T|))`. -/
lemma zetaZerosInDisk_card_le (T : ℝ) :
    (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)).card ≤
      zetaZerosInDiskCardBound * (1 + Real.log (2 + |T|)) := by
  have hlog76 : 0 < Real.log (7 / 6 : ℝ) := Real.log_pos (by norm_num)
  have hL : 0 ≤ Real.log (2 + |T|) :=
    Real.log_nonneg (by nlinarith [abs_nonneg T])
  have hchain :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)).card : ℝ) *
          Real.log (7 / 6 : ℝ) ≤
        Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ :=
    (zetaZerosInDisk_card_mul_log_le T).trans
      (riemannZetaMulSubOne_jensen_sum_le T)
  have hnum :
      Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ ≤
        Real.log jensenSphereMajorantCoeff +
          Real.log ‖riemannZeta 2‖ + 2 * Real.log (2 + |T|) := by
    linarith [log_jensenSphereMajorant_le T, log_center_neg_le T]
  have hA :
      0 ≤ Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ := by
    have h1 : 0 ≤ Real.log jensenSphereMajorantCoeff :=
      le_of_lt (Real.log_pos one_lt_jensenSphereMajorantCoeff)
    have h2 : 0 ≤ Real.log ‖riemannZeta 2‖ :=
      le_of_lt (Real.log_pos one_lt_norm_riemannZeta_two)
    linarith
  have hpack :
      Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ +
          2 * Real.log (2 + |T|) ≤
        (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) *
          (1 + Real.log (2 + |T|)) := by
    nlinarith [hL, hA]
  have hdiv :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)).card : ℝ) ≤
        zetaZerosInDiskCardBound * (1 + Real.log (2 + |T|)) := by
    have hle := hchain.trans (hnum.trans hpack)
    unfold zetaZerosInDiskCardBound
    rw [div_mul_eq_mul_div]
    exact (le_div_iff₀ hlog76).mpr (by simpa [mul_comm] using hle)
  exact_mod_cast hdiv

/-- Disk form of the r509 landing site. -/
def JensenDiskZeroCountBound : Prop :=
  ∃ C : ℝ, 0 < C ∧
    ∀ T : ℝ,
      (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (3 / 2)).card ≤
        C * (1 + Real.log (2 + |T|))

theorem jensenDiskZeroCountBound : JensenDiskZeroCountBound :=
  ⟨zetaZerosInDiskCardBound, zetaZerosInDiskCardBound_pos,
    zetaZerosInDisk_card_le⟩

lemma mem_zetaClosedRect {s1 s2 T : ℝ} {z : ℂ} :
    z ∈ zetaClosedRect s1 s2 T ↔
      s1 ≤ z.re ∧ z.re ≤ s2 ∧ -T ≤ z.im ∧ z.im ≤ T := by
  simp [zetaClosedRect, mem_reProdIm, mem_Icc, and_assoc]

lemma riemannZeta_ne_zero_of_re_eq_zero {s : ℂ} (hs : s.re = 0) :
    riemannZeta s ≠ 0 := by
  by_cases h0 : s = 0
  · subst h0
    rw [riemannZeta_zero]
    norm_num
  · intro hz
    have hneg : ∀ n : ℕ, s ≠ -n := by
      intro n hn
      have hre : s.re = -(n : ℝ) := by rw [hn]; simp
      have hn0 : n = 0 := by
        have : (n : ℝ) = 0 := by linarith [hs, hre]
        exact Nat.cast_eq_zero.mp this
      exact h0 (by simpa [hn0] using hn)
    have hs1 : s ≠ 1 := by
      intro h
      have : s.re = 1 := by rw [h]; simp
      linarith
    have hz1 : riemannZeta (1 - s) = 0 := by
      rw [riemannZeta_one_sub hneg hs1, hz, mul_zero]
    have hre1 : (1 : ℝ) ≤ (1 - s).re := by
      rw [re_one_sub, hs]; norm_num
    exact riemannZeta_ne_zero_of_one_le_re hre1 hz1

lemma mem_jensen_support_of_mem_disk_radius {T r : ℝ} {z : ℂ}
    (hr : 0 < r) (hrR : r ≤ (7 / 4 : ℝ))
    (hz : z ∈ riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) r) :
    z ∈ (MeromorphicOn.divisor riemannZetaMulSubOne
      (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|)).support := by
  set c := (2 : ℂ) + T * I
  have hz' := mem_riemannZetaZerosInClosedDisk.mp hz
  have hrabs : |r| = r := abs_of_pos hr
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hzF : riemannZetaMulSubOne z = 0 :=
    riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
  have hzB : z ∈ Metric.closedBall c |7 / 4| := by
    have hzball : z ∈ Metric.closedBall c r := by
      simpa [c, hrabs] using hz'.1
    exact Metric.closedBall_subset_closedBall (by simpa [hRabs] using hrR) hzball
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hge := riemannZetaMulSubOne_divisor_ge_one_of_zero hzF hmer hzB
  exact fun h00 => by linarith [hge, h00]

/-- Inner radius `13/8` sits strictly inside the r511 Jensen circle
`R = 7/4`.  For `β ≥ 1/2` this gives a genuine height window
`w = 5/8`. -/
lemma zetaZerosInDisk_card_mul_log_le_inner (T : ℝ) :
    ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card : ℝ) *
        Real.log (14 / 13 : ℝ) ≤
      ∑ᶠ u, (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) *
        Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) := by
  set c := (2 : ℂ) + T * I
  set D := MeromorphicOn.divisor riemannZetaMulSubOne (Metric.closedBall c |7 / 4|)
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hfin : D.support.Finite :=
    D.finiteSupport (isCompact_closedBall c |7 / 4|)
  set s := hfin.toFinset
  set Z := riemannZetaZerosInClosedDisk c (13 / 8)
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hrabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) := abs_of_pos (by norm_num)
  have hZsub : Z ⊆ s := by
    intro z hz
    exact hfin.mem_toFinset.mpr
      (mem_jensen_support_of_mem_disk_radius (by norm_num : (0 : ℝ) < 13 / 8)
        (by norm_num) (by simpa [Z, c] using hz))
  have htermnn : ∀ u ∈ s, 0 ≤ (D u : ℝ) *
      Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := by
    intro u hu
    have huB : u ∈ Metric.closedBall c |7 / 4| :=
      D.supportWithinDomain (hfin.mem_toFinset.mp hu)
    exact mul_nonneg (riemannZetaMulSubOne_divisor_nonneg T u)
      (jensen_log_weight_nonneg T huB)
  have hsupp :
      (fun u => (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹)).support ⊆ s := by
    intro u hu
    have : D u ≠ 0 := by
      intro h00
      simp [h00] at hu
    exact hfin.mem_toFinset.mpr this
  have hleft :
      ∑ z ∈ Z, Real.log (14 / 13 : ℝ) ≤
        ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
    refine Finset.sum_le_sum ?_
    intro z hz
    have hz' := mem_riemannZetaZerosInClosedDisk.mp (by simpa [Z, c] using hz)
    have hzF : riemannZetaMulSubOne z = 0 :=
      riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
    have hzB : z ∈ Metric.closedBall c |7 / 4| := by
      have : (13 / 8 : ℝ) ≤ (7 / 4 : ℝ) := by norm_num
      have hzball : z ∈ Metric.closedBall c (13 / 8) := by
        simpa [c, hrabs] using hz'.1
      exact Metric.closedBall_subset_closedBall (by simpa [hRabs] using this) hzball
    have hge : (1 : ℝ) ≤ (D z : ℝ) := by
      exact_mod_cast (riemannZetaMulSubOne_divisor_ge_one_of_zero hzF hmer hzB)
    have hzc : z ≠ c := by
      intro h
      exact riemannZetaMulSubOne_center_ne_zero T (by simpa [c, h] using hzF)
    have hpos : 0 < ‖c - z‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hzc.symm)
    have hle : ‖c - z‖ ≤ (13 / 8 : ℝ) := by
      have : dist z c ≤ (13 / 8 : ℝ) := by
        simpa [c, hrabs, Metric.mem_closedBall] using hz'.1
      simpa [dist_eq_norm, norm_sub_rev] using this
    have hlogle : Real.log (14 / 13 : ℝ) ≤
        Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
      apply Real.log_le_log (by positivity)
      rw [← div_eq_mul_inv, div_le_div_iff₀ (by positivity) hpos]
      nlinarith
    have hlogpos : 0 ≤ Real.log (14 / 13 : ℝ) :=
      le_of_lt (Real.log_pos (by norm_num))
    nlinarith [riemannZetaMulSubOne_divisor_nonneg T z]
  have hmid :
      ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) ≤
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    Finset.sum_le_sum_of_subset_of_nonneg hZsub fun u hu _ => htermnn u hu
  have hcard : ∑ z ∈ Z, Real.log (14 / 13 : ℝ) =
      (Z.card : ℝ) * Real.log (14 / 13 : ℝ) := by simp
  have hfinsum :
      ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) =
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    finsum_eq_sum_of_support_subset _ hsupp
  calc
    (Z.card : ℝ) * Real.log (14 / 13 : ℝ) = ∑ z ∈ Z, Real.log (14 / 13 : ℝ) :=
      hcard.symm
    _ ≤ ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
      hleft.trans hmid
    _ = ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := hfinsum.symm

noncomputable def zetaZerosInDiskCardBoundInner : ℝ :=
  (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) /
    Real.log (14 / 13 : ℝ)

lemma zetaZerosInDiskCardBoundInner_pos : 0 < zetaZerosInDiskCardBoundInner := by
  have hnum : 0 < Real.log jensenSphereMajorantCoeff +
      Real.log ‖riemannZeta 2‖ + 2 := by
    have h1 : 0 < Real.log jensenSphereMajorantCoeff :=
      Real.log_pos one_lt_jensenSphereMajorantCoeff
    have h2 : 0 < Real.log ‖riemannZeta 2‖ :=
      Real.log_pos one_lt_norm_riemannZeta_two
    linarith
  have hden : 0 < Real.log (14 / 13 : ℝ) := Real.log_pos (by norm_num)
  unfold zetaZerosInDiskCardBoundInner
  exact div_pos hnum hden

lemma zetaZerosInDisk_card_le_inner (T : ℝ) :
    (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card ≤
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|)) := by
  have hlog : 0 < Real.log (14 / 13 : ℝ) := Real.log_pos (by norm_num)
  have hL : 0 ≤ Real.log (2 + |T|) :=
    Real.log_nonneg (by nlinarith [abs_nonneg T])
  have hchain :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card : ℝ) *
          Real.log (14 / 13 : ℝ) ≤
        Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ :=
    (zetaZerosInDisk_card_mul_log_le_inner T).trans
      (riemannZetaMulSubOne_jensen_sum_le T)
  have hnum :
      Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ ≤
        Real.log jensenSphereMajorantCoeff +
          Real.log ‖riemannZeta 2‖ + 2 * Real.log (2 + |T|) := by
    linarith [log_jensenSphereMajorant_le T, log_center_neg_le T]
  have hA :
      0 ≤ Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ := by
    have h1 : 0 ≤ Real.log jensenSphereMajorantCoeff :=
      le_of_lt (Real.log_pos one_lt_jensenSphereMajorantCoeff)
    have h2 : 0 ≤ Real.log ‖riemannZeta 2‖ :=
      le_of_lt (Real.log_pos one_lt_norm_riemannZeta_two)
    linarith
  have hpack :
      Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ +
          2 * Real.log (2 + |T|) ≤
        (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) *
          (1 + Real.log (2 + |T|)) := by
    nlinarith [hL, hA]
  have hdiv :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|)) := by
    have hle := hchain.trans (hnum.trans hpack)
    unfold zetaZerosInDiskCardBoundInner
    rw [div_mul_eq_mul_div]
    exact (le_div_iff₀ hlog).mpr (by simpa [mul_comm] using hle)
  exact_mod_cast hdiv

/-- Height-count on the critical-strip rectangle `[0, 1] × [-X, X]`. -/
def ZetaZeroCountUpToXBound : Prop :=
  ∃ C : ℝ, 0 < C ∧
    ∀ X : ℝ, 0 ≤ X →
      (riemannZetaZerosOnClosedRect 0 1 X).card ≤
        C * (1 + X) * (1 + Real.log (2 + X))

lemma mem_closedDisk_of_re_ge_half {T : ℝ} {z : ℂ}
    (hre : (1 / 2 : ℝ) ≤ z.re) (hre1 : z.re ≤ 1)
    (him : |z.im - T| ≤ (5 / 8 : ℝ)) :
    z ∈ Metric.closedBall ((2 : ℂ) + T * I) |(13 / 8 : ℝ)| := by
  have hRabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) := abs_of_pos (by norm_num)
  set c := (2 : ℂ) + T * I
  have hre_c : (z - c).re = z.re - 2 := by
    simp [c, sub_re, add_re, mul_re, I_re]
  have him_c : (z - c).im = z.im - T := by
    simp [c, sub_im, add_im, mul_im, I_re, I_im]
  have hsq : ‖z - c‖ ^ 2 = (z.re - 2) ^ 2 + (z.im - T) ^ 2 := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, hre_c, him_c]
    ring
  have habsre : |z.re - 2| ≤ (3 / 2 : ℝ) := by
    have hnn : 0 ≤ 2 - z.re := by linarith [hre1]
    have hup : 2 - z.re ≤ (3 / 2 : ℝ) := by linarith [hre]
    rwa [abs_sub_comm, abs_of_nonneg hnn]
  have hsqle : (z.re - 2) ^ 2 + (z.im - T) ^ 2 ≤ (13 / 8 : ℝ) ^ 2 := by
    have h1 : (z.re - 2) ^ 2 ≤ (3 / 2 : ℝ) ^ 2 :=
      sq_le_sq.mpr (by simpa [abs_of_pos (by norm_num : (0 : ℝ) < 3 / 2)] using habsre)
    have h2 : (z.im - T) ^ 2 ≤ (5 / 8 : ℝ) ^ 2 :=
      sq_le_sq.mpr (by simpa [abs_of_pos (by norm_num : (0 : ℝ) < 5 / 8)] using him)
    nlinarith
  have hnorm : ‖z - c‖ ≤ (13 / 8 : ℝ) := by
    have hnn : 0 ≤ ‖z - c‖ := norm_nonneg _
    have hR : 0 ≤ (13 / 8 : ℝ) := by norm_num
    exact (sq_le_sq₀ hnn hR).mp (by rwa [hsq])
  simpa [c, dist_eq_norm, hRabs] using hnorm

lemma abs_int_floor_le (y : ℝ) : |(Int.floor y : ℝ)| ≤ |y| + 1 := by
  have h1 := Int.floor_le y
  have h2 := Int.lt_floor_add_one y
  refine abs_le.mpr ⟨?_, ?_⟩
  · exact le_of_lt (by linarith [neg_le_abs y, h2])
  · linarith [le_abs_self y, h1]

noncomputable def zetaZeroHeightCenterBound (X : ℝ) : ℕ :=
  Nat.ceil ((8 : ℝ) * X / 5) + 1

noncomputable def zetaZeroHeightCenters (X : ℝ) : Finset ℝ :=
  (Finset.Icc (-(zetaZeroHeightCenterBound X : ℤ))
      (zetaZeroHeightCenterBound X : ℤ)).image
    fun k : ℤ => (k : ℝ) * (5 / 8)

lemma mem_zetaZeroHeightCenters {X : ℝ} {k : ℤ}
    (hk : |k| ≤ (zetaZeroHeightCenterBound X : ℤ)) :
    (k : ℝ) * (5 / 8) ∈ zetaZeroHeightCenters X := by
  refine Finset.mem_image.mpr ⟨k, ?_, rfl⟩
  exact Finset.mem_Icc.mpr (abs_le.mp hk)

lemma exists_zetaZeroHeightCenter {X γ : ℝ}
    (hX : 0 ≤ X) (hγ : |γ| ≤ X) :
    ∃ T ∈ zetaZeroHeightCenters X, |γ - T| ≤ (5 / 8 : ℝ) := by
  set w := (5 / 8 : ℝ)
  have hw : 0 < w := by norm_num
  set k := Int.floor (γ / w)
  have hlo : (k : ℝ) ≤ γ / w := Int.floor_le _
  have hhi : γ / w < (k : ℝ) + 1 := Int.lt_floor_add_one _
  have hcancel : (γ / w) * w = γ := by field_simp [hw.ne']
  have hdiff0 : 0 ≤ γ - (k : ℝ) * w := by
    have hmul := mul_le_mul_of_nonneg_right hlo (le_of_lt hw)
    rw [hcancel] at hmul
    linarith
  have hdiff1 : γ - (k : ℝ) * w < w := by
    have hmul := mul_lt_mul_of_pos_right hhi hw
    rw [hcancel, add_mul, one_mul] at hmul
    linarith
  have hwin : |γ - (k : ℝ) * w| ≤ w := by
    have : |γ - (k : ℝ) * w| = γ - (k : ℝ) * w := abs_of_nonneg hdiff0
    linarith [hdiff1]
  have hn : |k| ≤ (zetaZeroHeightCenterBound X : ℤ) := by
    have hkR : |(k : ℝ)| ≤ (8 : ℝ) * X / 5 + 1 := by
      have := abs_int_floor_le (γ / w)
      have hdiv : |γ / w| ≤ X / w := by
        rw [abs_div, abs_of_pos hw]
        exact div_le_div_of_nonneg_right hγ (le_of_lt hw)
      have hwX : X / w = (8 : ℝ) * X / 5 := by
        field_simp [w]; ring
      linarith
    have hceil : ((8 : ℝ) * X / 5 : ℝ) ≤
        (Nat.ceil ((8 : ℝ) * X / 5) : ℝ) := Nat.le_ceil _
    have hnR : |(k : ℝ)| ≤ (zetaZeroHeightCenterBound X : ℝ) := by
      have hnval : (zetaZeroHeightCenterBound X : ℝ) =
          (Nat.ceil ((8 : ℝ) * X / 5) : ℝ) + 1 := by
        unfold zetaZeroHeightCenterBound
        exact_mod_cast rfl
      linarith [hkR, hceil, hnval]
    exact_mod_cast hnR
  refine ⟨(k : ℝ) * w, mem_zetaZeroHeightCenters hn, ?_⟩
  simpa [w] using hwin

lemma mem_disk_of_half_strip {X : ℝ} {z : ℂ} (hX : 0 ≤ X)
    (hz : z ∈ riemannZetaZerosOnClosedRect 0 1 X)
    (hre : (1 / 2 : ℝ) ≤ z.re) :
    ∃ T ∈ zetaZeroHeightCenters X,
      z ∈ riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8) := by
  have hz' := mem_riemannZetaZerosOnClosedRect.mp hz
  have hrect := mem_zetaClosedRect.mp hz'.1
  obtain ⟨T, hT, him⟩ := exists_zetaZeroHeightCenter hX
    (abs_le.mpr ⟨hrect.2.2.1, hrect.2.2.2⟩)
  refine ⟨T, hT, ?_⟩
  refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hz'.2.1, hz'.2.2⟩
  exact mem_closedDisk_of_re_ge_half hre hrect.2.1 him

lemma one_sub_mem_closedRect {X : ℝ} {z : ℂ}
    (hz : z ∈ riemannZetaZerosOnClosedRect 0 1 X)
    (h0 : 0 < z.re) (h1 : z.re < 1) :
    1 - z ∈ riemannZetaZerosOnClosedRect 0 1 X := by
  have hz' := mem_riemannZetaZerosOnClosedRect.mp hz
  have hrect := mem_zetaClosedRect.mp hz'.1
  have hz1 : riemannZeta (1 - z) = 0 :=
    riemannZeta_one_sub_eq_zero_of h0 h1 hz'.2.1
  have hre : 0 ≤ (1 - z).re ∧ (1 - z).re ≤ 1 := by
    rw [re_one_sub]
    constructor <;> linarith [hrect.1, hrect.2.1]
  have him : -(X) ≤ (1 - z).im ∧ (1 - z).im ≤ X := by
    have : (1 - z).im = -z.im := by simp [sub_im]
    rw [this]
    constructor <;> linarith [hrect.2.2.1, hrect.2.2.2]
  have hne : 1 - z ≠ 1 := by
    intro h
    have : z = 0 := by linear_combination -(h)
    exact (ne_of_gt h0) (by simpa [this] using this)
  refine mem_riemannZetaZerosOnClosedRect.mpr ⟨?_, hz1, hne⟩
  exact mem_zetaClosedRect.mpr ⟨hre.1, hre.2, him.1, him.2⟩

lemma zetaZeroHeightCenters_card_le (X : ℝ) (hX : 0 ≤ X) :
    (zetaZeroHeightCenters X).card ≤
      2 * zetaZeroHeightCenterBound X + 1 := by
  refine (Finset.card_image_le).trans ?_
  have hIcc :
      (Finset.Icc (-(zetaZeroHeightCenterBound X : ℤ))
        (zetaZeroHeightCenterBound X : ℤ)).card =
        2 * zetaZeroHeightCenterBound X + 1 := by
    rw [Int.card_Icc]
    set n := zetaZeroHeightCenterBound X
    have : ((n : ℤ) + 1 - - (n : ℤ)) = ((2 * n + 1 : ℕ) : ℤ) := by
      push_cast; ring
    rw [this, Int.toNat_natCast]
  exact_mod_cast hIcc.le

lemma zetaZeroHeightCenterBound_cast_le (X : ℝ) (hX : 0 ≤ X) :
    (zetaZeroHeightCenterBound X : ℝ) ≤ (8 : ℝ) * X / 5 + 2 := by
  have hpos : 0 ≤ (8 : ℝ) * X / 5 := by positivity
  have hlt := Nat.ceil_lt_add_one hpos
  unfold zetaZeroHeightCenterBound
  exact_mod_cast (by linarith : (Nat.ceil ((8 : ℝ) * X / 5) : ℝ) + 1 ≤
    (8 : ℝ) * X / 5 + 2)

lemma abs_heightCenter_le (X : ℝ) {T : ℝ}
    (hT : T ∈ zetaZeroHeightCenters X) :
    |T| ≤ (zetaZeroHeightCenterBound X : ℝ) * (5 / 8) := by
  obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp hT
  have hkI := Finset.mem_Icc.mp hk
  have habs : |k| ≤ (zetaZeroHeightCenterBound X : ℤ) := abs_le.mpr hkI
  have : |(k : ℝ)| ≤ (zetaZeroHeightCenterBound X : ℝ) := by exact_mod_cast habs
  have hw : 0 ≤ (5 / 8 : ℝ) := by norm_num
  simpa [abs_mul, abs_of_nonneg hw] using mul_le_mul_of_nonneg_right this hw

lemma card_half_strip_le (X : ℝ) (hX : 0 ≤ X) :
    ((riemannZetaZerosOnClosedRect 0 1 X).filter
        fun z => (1 / 2 : ℝ) ≤ z.re).card ≤
      (zetaZeroHeightCenters X).card *
        (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) := by
  set S := (riemannZetaZerosOnClosedRect 0 1 X).filter
    fun z => (1 / 2 : ℝ) ≤ z.re
  set Cts := zetaZeroHeightCenters X
  have hcover :
      S ⊆ Cts.biUnion fun T =>
        riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8) := by
    intro z hz
    obtain ⟨hzS, hre⟩ := Finset.mem_filter.mp hz
    obtain ⟨T, hT, hzD⟩ := mem_disk_of_half_strip hX hzS hre
    exact Finset.mem_biUnion.mpr ⟨T, hT, hzD⟩
  have hbu :
      (Cts.biUnion fun T =>
          riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card ≤
        ∑ T ∈ Cts,
          (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card :=
    Finset.card_biUnion_le
  have hnat : S.card ≤
      ∑ T ∈ Cts,
        (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)).card :=
    (Finset.card_le_card hcover).trans hbu
  have h1 : (S.card : ℝ) ≤
      ∑ T ∈ Cts, ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I)
        (13 / 8)).card : ℝ) := by
    have hcast :
        (↑(∑ T ∈ Cts, (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I)
            (13 / 8)).card) : ℝ) =
          ∑ T ∈ Cts, (↑(riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I)
            (13 / 8)).card : ℝ) :=
      map_sum (Nat.castAddMonoidHom ℝ)
        (fun T : ℝ => (riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I)
          (13 / 8)).card) Cts
    exact (Nat.cast_le.mpr hnat).trans_eq hcast
  have h3 :
      ∑ T ∈ Cts, ((riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I)
          (13 / 8)).card : ℝ) ≤
        ∑ T ∈ Cts, zetaZerosInDiskCardBoundInner *
          (1 + Real.log (2 + X + 5 / 4)) := by
    refine Finset.sum_le_sum ?_
    intro T hT
    have hn := zetaZeroHeightCenterBound_cast_le X hX
    have habsT : |T| ≤ X + 5 / 4 := by
      have := mul_le_mul_of_nonneg_right hn (by norm_num : (0 : ℝ) ≤ 5 / 8)
      have hsimp : ((8 : ℝ) * X / 5 + 2) * (5 / 8) = X + 5 / 4 := by ring
      linarith [abs_heightCenter_le X hT]
    have hlog : 1 + Real.log (2 + |T|) ≤
        1 + Real.log (2 + X + 5 / 4) := by
      have hpos : 0 < 2 + |T| := by positivity
      have hle : 2 + |T| ≤ 2 + X + 5 / 4 := by linarith [abs_nonneg T]
      exact add_le_add le_rfl (Real.log_le_log hpos hle)
    have hdisk := zetaZerosInDisk_card_le_inner T
    exact_mod_cast (hdisk.trans (mul_le_mul_of_nonneg_left hlog
      (le_of_lt zetaZerosInDiskCardBoundInner_pos)))
  have h4 :
      ∑ T ∈ Cts, zetaZerosInDiskCardBoundInner *
          (1 + Real.log (2 + X + 5 / 4)) =
        (Cts.card : ℝ) * (zetaZerosInDiskCardBoundInner *
          (1 + Real.log (2 + X + 5 / 4))) := by
    simp [Finset.sum_const, nsmul_eq_mul]
  exact (h1.trans h3).trans_eq h4

lemma card_critical_le_two_mul_half (X : ℝ) (_hX : 0 ≤ X) :
    (riemannZetaZerosOnClosedRect 0 1 X).card ≤
      2 * ((riemannZetaZerosOnClosedRect 0 1 X).filter
        fun z => (1 / 2 : ℝ) ≤ z.re).card := by
  set S := riemannZetaZerosOnClosedRect 0 1 X
  set Sge := S.filter fun z => (1 / 2 : ℝ) ≤ z.re
  set Slt := S.filter fun z => z.re < (1 / 2 : ℝ)
  have hunion : Sge ∪ Slt = S := by
    ext z
    simp [Sge, Slt, Finset.mem_union, Finset.mem_filter]
    constructor
    · rintro (⟨h, _⟩ | ⟨h, _⟩) <;> exact h
    · intro hz
      by_cases hre : (1 / 2 : ℝ) ≤ z.re
      · exact Or.inl ⟨hz, by simpa using hre⟩
      · exact Or.inr ⟨hz, by simpa using lt_of_not_ge hre⟩
  have hdisj : Disjoint Sge Slt := by
    refine Finset.disjoint_left.mpr ?_
    intro z hzge hzlt
    have := (Finset.mem_filter.mp hzge).2
    have := (Finset.mem_filter.mp hzlt).2
    linarith
  have hpart : S.card = Slt.card + Sge.card := by
    rw [← hunion, Finset.card_union_of_disjoint hdisj, add_comm]
  have hinj : Function.Injective fun z : ℂ => 1 - z :=
    fun a b h => sub_right_inj.mp h
  have himage : Slt.image (fun z => 1 - z) ⊆ Sge := by
    intro w hw
    obtain ⟨z, hzlt, rfl⟩ := Finset.mem_image.mp hw
    have hz := (Finset.mem_filter.mp hzlt).1
    have hre_lt := (Finset.mem_filter.mp hzlt).2
    have hz' := mem_riemannZetaZerosOnClosedRect.mp hz
    have hrect := mem_zetaClosedRect.mp hz'.1
    have hre0 : 0 < z.re :=
      lt_of_le_of_ne hrect.1 fun h0 =>
        riemannZeta_ne_zero_of_re_eq_zero h0.symm hz'.2.1
    have hre1 : z.re < 1 := lt_of_lt_of_le hre_lt (by norm_num)
    have hwmem := one_sub_mem_closedRect hz hre0 hre1
    have hre_ge : (1 / 2 : ℝ) ≤ (1 - z).re := by
      rw [re_one_sub]; linarith
    exact Finset.mem_filter.mpr ⟨hwmem, hre_ge⟩
  have hle : Slt.card ≤ Sge.card :=
    (Finset.card_image_of_injective Slt hinj).symm.trans_le
      (Finset.card_le_card himage)
  linarith [hpart, hle]

noncomputable def zetaZeroCountUpToXBoundConst : ℝ :=
  2 * (16 / 5 + 5) * zetaZerosInDiskCardBoundInner * (9 / 4)

lemma zetaZeroCountUpToXBoundConst_pos :
    0 < zetaZeroCountUpToXBoundConst := by
  have hC := zetaZerosInDiskCardBoundInner_pos
  unfold zetaZeroCountUpToXBoundConst
  positivity

lemma log_height_pack (X : ℝ) (hX : 0 ≤ X) :
    1 + Real.log (2 + X + 5 / 4) ≤
      (9 / 4) * (1 + Real.log (2 + X)) := by
  have hpos : 0 < 2 + X := by positivity
  have h1 : 0 < 1 + (5 / 4 : ℝ) / (2 + X) := by positivity
  have hsplit : 2 + X + 5 / 4 = (2 + X) * (1 + (5 / 4) / (2 + X)) := by
    field_simp
  have hlog : Real.log (2 + X + 5 / 4) ≤ Real.log (2 + X) + 5 / 4 := by
    have hsum : Real.log (2 + X + 5 / 4) =
        Real.log (2 + X) + Real.log (1 + (5 / 4) / (2 + X)) := by
      rw [hsplit, Real.log_mul hpos.ne' h1.ne']
    have hlog1 : Real.log (1 + (5 / 4) / (2 + X)) ≤
        (5 / 4 : ℝ) / (2 + X) := by
      have := Real.log_le_sub_one_of_pos h1
      linarith
    have hdiv : (5 / 4 : ℝ) / (2 + X) ≤ 5 / 4 :=
      (div_le_iff₀ hpos).mpr (by nlinarith [hX])
    linarith [hsum, hlog1, hdiv]
  have hL : 0 ≤ Real.log (2 + X) := Real.log_nonneg (by linarith)
  nlinarith [hlog, hL]

lemma heightCenters_card_cast_le (X : ℝ) (hX : 0 ≤ X) :
    ((zetaZeroHeightCenters X).card : ℝ) ≤ (16 / 5 : ℝ) * X + 5 := by
  have hcts := zetaZeroHeightCenters_card_le X hX
  have hn := zetaZeroHeightCenterBound_cast_le X hX
  have hcard : ((zetaZeroHeightCenters X).card : ℝ) ≤
      (2 * zetaZeroHeightCenterBound X + 1 : ℝ) := by exact_mod_cast hcts
  have hlin : (2 * zetaZeroHeightCenterBound X + 1 : ℝ) ≤
      2 * ((8 : ℝ) * X / 5 + 2) + 1 := by
    linarith [hn]
  have hsimp : 2 * ((8 : ℝ) * X / 5 + 2) + 1 = (16 / 5 : ℝ) * X + 5 := by ring
  linarith

lemma card_zeros_le (X : ℝ) (hX : 0 ≤ X) :
    ((riemannZetaZerosOnClosedRect 0 1 X).card : ℝ) ≤
      zetaZeroCountUpToXBoundConst * (1 + X) * (1 + Real.log (2 + X)) := by
    have hhalf := card_half_strip_le X hX
    have htwo := card_critical_le_two_mul_half X hX
    have hctsR := heightCenters_card_cast_le X hX
    have hpack := log_height_pack X hX
    have hCpos := le_of_lt zetaZerosInDiskCardBoundInner_pos
    have hR : ((riemannZetaZerosOnClosedRect 0 1 X).card : ℝ) ≤
        2 * ((zetaZeroHeightCenters X).card : ℝ) *
          (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) := by
      have hge : (((riemannZetaZerosOnClosedRect 0 1 X).filter
          fun z => (1 / 2 : ℝ) ≤ z.re).card : ℝ) ≤
          ((zetaZeroHeightCenters X).card : ℝ) *
            (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) :=
        hhalf
      have h2R : ((riemannZetaZerosOnClosedRect 0 1 X).card : ℝ) ≤
          2 * (((riemannZetaZerosOnClosedRect 0 1 X).filter
            fun z => (1 / 2 : ℝ) ≤ z.re).card : ℝ) := by exact_mod_cast htwo
      nlinarith [h2R, hge, hCpos]
    have hcts1 : ((zetaZeroHeightCenters X).card : ℝ) ≤
        (16 / 5 + 5 : ℝ) * (1 + X) := by nlinarith [hctsR, hX]
    have hL1pos : 0 ≤ 1 + Real.log (2 + X + 5 / 4) :=
      add_nonneg (by norm_num)
        (Real.log_nonneg (by nlinarith [hX] : (1 : ℝ) ≤ 2 + X + 5 / 4))
    have hL2pos : 0 ≤ 1 + Real.log (2 + X) :=
      add_nonneg (by norm_num) (Real.log_nonneg (by linarith : (1 : ℝ) ≤ 2 + X))
    have hXpos : 0 ≤ 1 + X := by linarith
    have hstep1 :
        2 * ((zetaZeroHeightCenters X).card : ℝ) *
            (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) ≤
          2 * ((16 / 5 + 5 : ℝ) * (1 + X)) *
            (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hcts1 (by norm_num))
        (mul_nonneg hCpos hL1pos)
    have hstep2 :
        2 * ((16 / 5 + 5 : ℝ) * (1 + X)) *
            (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + X + 5 / 4))) ≤
          2 * ((16 / 5 + 5 : ℝ) * (1 + X)) *
            (zetaZerosInDiskCardBoundInner * ((9 / 4) * (1 + Real.log (2 + X)))) :=
      mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_left hpack hCpos)
        (mul_nonneg (by norm_num) (mul_nonneg (by norm_num) hXpos))
    have hrewrit :
        2 * ((16 / 5 + 5 : ℝ) * (1 + X)) *
            (zetaZerosInDiskCardBoundInner * ((9 / 4) * (1 + Real.log (2 + X)))) =
          zetaZeroCountUpToXBoundConst * (1 + X) * (1 + Real.log (2 + X)) := by
      unfold zetaZeroCountUpToXBoundConst; ring
    exact (hR.trans (hstep1.trans hstep2)).trans_eq hrewrit

theorem zetaZeroCountUpToXBound : ZetaZeroCountUpToXBound :=
  ⟨zetaZeroCountUpToXBoundConst, zetaZeroCountUpToXBoundConst_pos, fun X hX => by
    exact_mod_cast (card_zeros_le X hX)⟩

end ZetaEulerMaclaurin

/-! ### r513: ∑ 1/|ρ|² via dyadic blocks ([2c] counting complete)

`zetaZeroCountUpToXBound` estimates Finset.card of the rectangle
zeros (unweighted).  Jensen's divisor already carries multiplicity;
the same disk constant therefore bounds `riemannZetaMultiplicity`
pointwise by `O(log(2+|γ|))`, which is enough for the weighted
[2d] series `∑ m_ρ/|ρ|²`.  Block geometry: compact `|Im|<1`
(finite by r499) plus `B_j = {2^j ≤ |Im| < 2^{j+1}}`.
-/

section ZetaZeroInvSq

open Complex Classical
open scoped ENNReal

def IsCriticalStripZetaZero (s : ℂ) : Prop :=
  riemannZeta s = 0 ∧ 0 < s.re ∧ s.re < 1

lemma isCriticalStripZetaZero_ne_zero {s : ℂ}
    (hs : IsCriticalStripZetaZero s) : s ≠ 0 :=
  fun h => (ne_of_gt hs.2.1) (by simp [h])

lemma isCriticalStripZetaZero_norm_pos {s : ℂ}
    (hs : IsCriticalStripZetaZero s) : 0 < ‖s‖ :=
  norm_pos_iff.mpr (isCriticalStripZetaZero_ne_zero hs)

lemma isCriticalStripZetaZero_ne_one {s : ℂ}
    (hs : IsCriticalStripZetaZero s) : s ≠ 1 :=
  fun h => (lt_irrefl (1 : ℝ)) (by
    have : s.re = 1 := by simp [h]
    linarith [hs.2.2, this])

lemma mem_rect_of_criticalStrip {X : ℝ} {z : ℂ}
    (hz : IsCriticalStripZetaZero z) (him : |z.im| ≤ X) :
    z ∈ riemannZetaZerosOnClosedRect 0 1 X := by
  refine mem_riemannZetaZerosOnClosedRect.mpr ⟨?_, hz.1,
    isCriticalStripZetaZero_ne_one hz⟩
  exact mem_zetaClosedRect.mpr ⟨le_of_lt hz.2.1, le_of_lt hz.2.2,
    (abs_le.mp him).1, (abs_le.mp him).2⟩

lemma isCriticalStrip_of_mem_rect {X : ℝ} {z : ℂ}
    (hz : z ∈ riemannZetaZerosOnClosedRect 0 1 X) :
    IsCriticalStripZetaZero z := by
  have hz' := mem_riemannZetaZerosOnClosedRect.mp hz
  have hrect := mem_zetaClosedRect.mp hz'.1
  have h0 : 0 < z.re :=
    lt_of_le_of_ne hrect.1 fun h0 =>
      riemannZeta_ne_zero_of_re_eq_zero h0.symm hz'.2.1
  have h1 : z.re < 1 :=
    lt_of_le_of_ne hrect.2.1 fun h1 =>
      riemannZeta_ne_zero_of_one_le_re (le_of_eq h1.symm) hz'.2.1
  exact ⟨hz'.2.1, h0, h1⟩

lemma exists_dyadic_index {x : ℝ} (hx : 1 ≤ x) :
    ∃ j : ℕ, (2 : ℝ) ^ j ≤ x ∧ x < (2 : ℝ) ^ (j + 1) := by
  have hx0 : 0 ≤ x := le_trans (by norm_num : (0 : ℝ) ≤ 1) hx
  set n := Nat.floor x
  have hn_le : (n : ℝ) ≤ x := Nat.floor_le hx0
  have hx_lt : x < (n : ℝ) + 1 := Nat.lt_floor_add_one x
  have hn1 : 1 ≤ n := (Nat.le_floor_iff hx0).mpr (by exact_mod_cast hx)
  have hn0 : n ≠ 0 := Nat.pos_iff_ne_zero.mp (Nat.succ_le_iff.mp hn1)
  refine ⟨Nat.log 2 n, ?_, ?_⟩
  · have hnat : (2 : ℕ) ^ Nat.log 2 n ≤ n := Nat.pow_log_le_self 2 hn0
    have : (2 : ℝ) ^ Nat.log 2 n ≤ (n : ℝ) := by exact_mod_cast hnat
    linarith
  · have hlt := Nat.lt_pow_succ_log_self (by norm_num : (1 : ℕ) < 2) n
    have hnat : n + 1 ≤ 2 ^ (Nat.log 2 n + 1) := Nat.succ_le_of_lt hlt
    have : (n : ℝ) + 1 ≤ (2 : ℝ) ^ (Nat.log 2 n + 1) := by exact_mod_cast hnat
    linarith

noncomputable def zetaZeroCompactBlock : Finset ℂ :=
  (riemannZetaZerosOnClosedRect 0 1 1).filter fun z => |z.im| < 1

noncomputable def zetaZeroDyadicBlock (j : ℕ) : Finset ℂ :=
  (riemannZetaZerosOnClosedRect 0 1 ((2 : ℝ) ^ (j + 1))).filter fun z =>
    (2 : ℝ) ^ j ≤ |z.im| ∧ |z.im| < (2 : ℝ) ^ (j + 1)

lemma mem_compactBlock {z : ℂ} :
    z ∈ zetaZeroCompactBlock ↔
      z ∈ riemannZetaZerosOnClosedRect 0 1 1 ∧ |z.im| < 1 :=
  Finset.mem_filter

lemma mem_dyadicBlock {j : ℕ} {z : ℂ} :
    z ∈ zetaZeroDyadicBlock j ↔
      z ∈ riemannZetaZerosOnClosedRect 0 1 ((2 : ℝ) ^ (j + 1)) ∧
        (2 : ℝ) ^ j ≤ |z.im| ∧ |z.im| < (2 : ℝ) ^ (j + 1) :=
  Finset.mem_filter

lemma isCritical_of_mem_compact {z : ℂ} (hz : z ∈ zetaZeroCompactBlock) :
    IsCriticalStripZetaZero z :=
  isCriticalStrip_of_mem_rect (mem_compactBlock.mp hz).1

lemma isCritical_of_mem_dyadic {j : ℕ} {z : ℂ}
    (hz : z ∈ zetaZeroDyadicBlock j) :
    IsCriticalStripZetaZero z :=
  isCriticalStrip_of_mem_rect (mem_dyadicBlock.mp hz).1

lemma mem_compact_or_dyadic {z : ℂ} (hz : IsCriticalStripZetaZero z) :
    z ∈ zetaZeroCompactBlock ∨ ∃ j : ℕ, z ∈ zetaZeroDyadicBlock j := by
  by_cases h : |z.im| < 1
  · refine Or.inl (mem_compactBlock.mpr ⟨?_, h⟩)
    exact mem_rect_of_criticalStrip hz (le_of_lt h)
  · have h1 : 1 ≤ |z.im| := le_of_not_gt h
    obtain ⟨j, hj0, hj1⟩ := exists_dyadic_index h1
    refine Or.inr ⟨j, mem_dyadicBlock.mpr ⟨?_, hj0, hj1⟩⟩
    exact mem_rect_of_criticalStrip hz (le_of_lt hj1)

lemma stripZeros_eq_blocks :
    {z : ℂ | IsCriticalStripZetaZero z} =
      (zetaZeroCompactBlock : Set ℂ) ∪
        ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ) := by
  ext z
  constructor
  · intro hz
    rcases mem_compact_or_dyadic hz with h | ⟨j, hj⟩
    · exact Or.inl h
    · exact Or.inr ⟨zetaZeroDyadicBlock j, ⟨j, rfl⟩, hj⟩
  · intro hz
    rcases hz with h | h
    · exact isCritical_of_mem_compact h
    · obtain ⟨s, ⟨j, rfl⟩, hzj⟩ := h
      exact isCritical_of_mem_dyadic hzj

lemma dyadicBlock_norm_ge {j : ℕ} {z : ℂ}
    (hz : z ∈ zetaZeroDyadicBlock j) :
    (2 : ℝ) ^ j ≤ ‖z‖ := by
  have him := (mem_dyadicBlock.mp hz).2.1
  exact le_trans him (Complex.abs_im_le_norm z)

lemma inv_sq_le_dyadic {j : ℕ} {z : ℂ}
    (hz : z ∈ zetaZeroDyadicBlock j) :
    (‖z‖ ^ 2)⁻¹ ≤ ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
  have hpos : 0 < ‖z‖ :=
    isCriticalStripZetaZero_norm_pos (isCritical_of_mem_dyadic hz)
  have hge := dyadicBlock_norm_ge hz
  have h2 : 0 < (2 : ℝ) ^ j := pow_pos (by norm_num) _
  have hsq : ((2 : ℝ) ^ j) ^ 2 ≤ ‖z‖ ^ 2 :=
    sq_le_sq.mpr (by simpa [abs_of_pos h2, abs_of_pos hpos] using hge)
  have hinv : (‖z‖ ^ 2)⁻¹ ≤ (((2 : ℝ) ^ j) ^ 2)⁻¹ :=
    (inv_le_inv₀ (sq_pos_of_pos hpos) (sq_pos_of_pos h2)).mpr hsq
  have hrew : (((2 : ℝ) ^ j) ^ 2)⁻¹ = ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
    simp [inv_pow]
  exact hinv.trans_eq hrew

lemma two_pow_cast (j : ℕ) : ((2 : ℕ) : ℝ) ^ j = (2 : ℝ) ^ j := by
  simp

lemma log_dyadic_height_le (j : ℕ) :
    1 + Real.log (2 + (2 : ℝ) ^ (j + 1)) ≤ 2 * ((j : ℝ) + 2) := by
  have h2 : (2 : ℝ) + (2 : ℝ) ^ (j + 1) ≤ (2 : ℝ) ^ (j + 2) := by
    have hpow : (2 : ℝ) ^ (j + 2) = 2 * (2 : ℝ) ^ (j + 1) := by ring
    have hone : (1 : ℝ) ≤ (2 : ℝ) ^ j := one_le_pow₀ (by norm_num)
    have hge : (2 : ℝ) ≤ (2 : ℝ) ^ (j + 1) := by
      have : (2 : ℝ) ^ (j + 1) = 2 * (2 : ℝ) ^ j := by ring
      nlinarith [this, hone]
    nlinarith [hpow, hge]
  have hpos : 0 < 2 + (2 : ℝ) ^ (j + 1) := by positivity
  have hlog : Real.log (2 + (2 : ℝ) ^ (j + 1)) ≤
      Real.log ((2 : ℝ) ^ (j + 2)) :=
    Real.log_le_log hpos h2
  have hlogpow : Real.log ((2 : ℝ) ^ (j + 2)) = (j + 2 : ℝ) * Real.log 2 := by
    simpa [Nat.cast_add, Nat.cast_ofNat] using Real.log_pow (2 : ℝ) (j + 2)
  have hlog2 : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2)
    linarith
  nlinarith [hlog, hlogpow, hlog2]

lemma dyadic_count_factor_le (j : ℕ) :
    (1 + (2 : ℝ) ^ (j + 1)) * (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) *
      ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤ 8 * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by
  have ha : 0 < (2 : ℝ) ^ j := pow_pos (by norm_num) _
  have ha1 : (1 : ℝ) ≤ (2 : ℝ) ^ j := one_le_pow₀ (by norm_num)
  have h2j : (2 : ℝ) ^ (j + 1) = 2 * (2 : ℝ) ^ j := by ring
  have hinv : ((2 : ℝ) ^ j)⁻¹ = (2 : ℝ)⁻¹ ^ j := (inv_pow (2 : ℝ) j).symm
  have hrew : (1 + (2 : ℝ) ^ (j + 1)) * ((2 : ℝ) ^ j)⁻¹ ^ 2 =
      ((2 : ℝ) ^ j)⁻¹ ^ 2 + 2 * ((2 : ℝ) ^ j)⁻¹ := by
    rw [h2j]
    have hA : (2 * (2 : ℝ) ^ j) * ((2 : ℝ) ^ j)⁻¹ ^ 2 =
        2 * ((2 : ℝ) ^ j)⁻¹ := by
      field_simp [ha.ne']
    rw [add_mul, one_mul, hA]
  have hsmall : ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤ ((2 : ℝ) ^ j)⁻¹ := by
    rw [pow_two]
    exact mul_le_of_le_one_left (inv_nonneg.mpr (le_of_lt ha))
      (inv_le_one_of_one_le₀ ha1)
  have hprod : (1 + (2 : ℝ) ^ (j + 1)) * ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤
      4 * (2 : ℝ)⁻¹ ^ j := by
    rw [hrew, hinv]
    nlinarith [hsmall]
  have hlog := log_dyadic_height_le j
  have hnnL : 0 ≤ 1 + Real.log (2 + (2 : ℝ) ^ (j + 1)) := by
    have : (1 : ℝ) ≤ 2 + (2 : ℝ) ^ (j + 1) := by
      nlinarith [pow_nonneg (by norm_num : (0 : ℝ) ≤ 2) (j + 1)]
    exact add_nonneg (by norm_num) (Real.log_nonneg this)
  have hmul' :
      ((1 + (2 : ℝ) ^ (j + 1)) * ((2 : ℝ) ^ j)⁻¹ ^ 2) *
          (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) ≤
        (4 * (2 : ℝ)⁻¹ ^ j) * (2 * ((j : ℝ) + 2)) :=
    mul_le_mul hprod hlog hnnL (mul_nonneg (by norm_num) (by positivity))
  have hassoc :
      (1 + (2 : ℝ) ^ (j + 1)) * (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) *
          ((2 : ℝ) ^ j)⁻¹ ^ 2 =
        ((1 + (2 : ℝ) ^ (j + 1)) * ((2 : ℝ) ^ j)⁻¹ ^ 2) *
          (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) := by ring
  have h8 : (4 * (2 : ℝ)⁻¹ ^ j) * (2 * ((j : ℝ) + 2)) =
      8 * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by ring
  rw [hassoc]
  exact hmul'.trans_eq h8

noncomputable def zetaZeroInvSqBlockBound : ℝ :=
  8 * zetaZeroCountUpToXBoundConst

lemma zetaZeroInvSqBlockBound_nonneg : 0 ≤ zetaZeroInvSqBlockBound :=
  mul_nonneg (by norm_num) (le_of_lt zetaZeroCountUpToXBoundConst_pos)

lemma dyadicBlock_inv_sq_sum_le (j : ℕ) :
    ∑ z ∈ zetaZeroDyadicBlock j, (‖z‖ ^ 2)⁻¹ ≤
      zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by
  set B := zetaZeroDyadicBlock j
  have hX : 0 ≤ (2 : ℝ) ^ (j + 1) := pow_nonneg (by norm_num) _
  have hcard := card_zeros_le ((2 : ℝ) ^ (j + 1)) hX
  have hBcard : (B.card : ℝ) ≤
      ((riemannZetaZerosOnClosedRect 0 1 ((2 : ℝ) ^ (j + 1))).card : ℝ) :=
    Nat.cast_le.mpr (Finset.card_le_card (Finset.filter_subset _ _))
  have hterm : ∀ z ∈ B, (‖z‖ ^ 2)⁻¹ ≤ ((2 : ℝ) ^ j)⁻¹ ^ 2 :=
    fun z hz => inv_sq_le_dyadic hz
  have hsum : ∑ z ∈ B, (‖z‖ ^ 2)⁻¹ ≤
      (B.card : ℝ) * ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
    have := Finset.sum_le_card_nsmul B (fun z => (‖z‖ ^ 2)⁻¹)
      (((2 : ℝ) ^ j)⁻¹ ^ 2) hterm
    simpa [nsmul_eq_mul] using this
  have hC := le_of_lt zetaZeroCountUpToXBoundConst_pos
  have hL : 0 ≤ 1 + Real.log (2 + (2 : ℝ) ^ (j + 1)) := by
    have : (1 : ℝ) ≤ 2 + (2 : ℝ) ^ (j + 1) := by
      nlinarith [pow_nonneg (by norm_num : (0 : ℝ) ≤ 2) (j + 1)]
    exact add_nonneg (by norm_num) (Real.log_nonneg this)
  have hpack : (B.card : ℝ) * ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤
      zetaZeroCountUpToXBoundConst * (1 + (2 : ℝ) ^ (j + 1)) *
        (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) * ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
    have h1 := hBcard.trans hcard
    exact mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
  have hfac := dyadic_count_factor_le j
  have hfin :
      zetaZeroCountUpToXBoundConst * (1 + (2 : ℝ) ^ (j + 1)) *
          (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) * ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤
        zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by
    have := mul_le_mul_of_nonneg_left hfac hC
    unfold zetaZeroInvSqBlockBound
    nlinarith [this]
  exact hsum.trans (hpack.trans hfin)

lemma summable_nat_succ_mul_two_pow_neg :
    Summable fun j : ℕ => ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by
  have hr : ‖(2 : ℝ)⁻¹‖ < 1 := by norm_num
  have hpow : Summable fun n : ℕ => (n : ℝ) ^ 1 * (2 : ℝ)⁻¹ ^ n :=
    summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have hgeo : Summable fun n : ℕ => (2 : ℝ)⁻¹ ^ n :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  have h1 : Summable fun n : ℕ => (n : ℝ) * (2 : ℝ)⁻¹ ^ n := by
    simpa using hpow
  have h2 : Summable fun n : ℕ => (2 : ℝ) * (2 : ℝ)⁻¹ ^ n :=
    hgeo.mul_left 2
  convert h1.add h2 using 1
  ext j
  ring

lemma summable_dyadic_block_majorant :
    Summable fun j : ℕ =>
      zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j := by
  convert (summable_nat_succ_mul_two_pow_neg).mul_left zetaZeroInvSqBlockBound using 1
  ext j
  ring

lemma inv_sq_nonneg (z : ℂ) : 0 ≤ (‖z‖ ^ 2)⁻¹ :=
  inv_nonneg.mpr (sq_nonneg _)

noncomputable def invSqStripZero (z : ℂ) : ℝ≥0∞ :=
  if IsCriticalStripZetaZero z then ENNReal.ofReal (‖z‖ ^ 2)⁻¹ else 0

lemma invSqStripZero_eq_ofReal {z : ℂ} (hz : IsCriticalStripZetaZero z) :
    invSqStripZero z = ENNReal.ofReal (‖z‖ ^ 2)⁻¹ :=
  if_pos hz

lemma invSqStripZero_eq_zero {z : ℂ} (hz : ¬ IsCriticalStripZetaZero z) :
    invSqStripZero z = 0 :=
  if_neg hz

lemma tsum_invSq_compact :
    ∑' z : (zetaZeroCompactBlock : Set ℂ), invSqStripZero z =
      ∑ z ∈ zetaZeroCompactBlock, invSqStripZero z := by
  rw [← Finset.tsum_subtype zetaZeroCompactBlock invSqStripZero]
  rfl

lemma tsum_invSq_dyadic (j : ℕ) :
    ∑' z : (zetaZeroDyadicBlock j : Set ℂ), invSqStripZero z =
      ∑ z ∈ zetaZeroDyadicBlock j, invSqStripZero z := by
  rw [← Finset.tsum_subtype (zetaZeroDyadicBlock j) invSqStripZero]
  rfl

lemma sum_invSq_eq_ofReal (s : Finset ℂ)
    (hs : ∀ z ∈ s, IsCriticalStripZetaZero z) :
    ∑ z ∈ s, invSqStripZero z =
      ENNReal.ofReal (∑ z ∈ s, (‖z‖ ^ 2)⁻¹) := by
  have hcongr : ∑ z ∈ s, invSqStripZero z =
      ∑ z ∈ s, ENNReal.ofReal (‖z‖ ^ 2)⁻¹ :=
    Finset.sum_congr rfl fun z hz => invSqStripZero_eq_ofReal (hs z hz)
  rw [hcongr, ENNReal.ofReal_sum_of_nonneg fun z _ => inv_sq_nonneg z]

lemma sum_invSq_compact_ne_top :
    (∑ z ∈ zetaZeroCompactBlock, invSqStripZero z) ≠ ∞ := by
  rw [sum_invSq_eq_ofReal _ fun z hz => isCritical_of_mem_compact hz]
  exact ENNReal.ofReal_ne_top

lemma sum_invSq_dyadic_le (j : ℕ) :
    ∑ z ∈ zetaZeroDyadicBlock j, invSqStripZero z ≤
      ENNReal.ofReal (zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j) := by
  rw [sum_invSq_eq_ofReal _ fun z hz => isCritical_of_mem_dyadic hz]
  exact ENNReal.ofReal_le_ofReal (dyadicBlock_inv_sq_sum_le j)

lemma tsum_invSq_strip_le :
    ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, invSqStripZero z ≤
      ∑ z ∈ zetaZeroCompactBlock, invSqStripZero z +
        ∑' j : ℕ, ENNReal.ofReal
          (zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j) := by
  have hunion := stripZeros_eq_blocks
  have h1 :
      ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, invSqStripZero z =
        ∑' z : ↥((zetaZeroCompactBlock : Set ℂ) ∪
            ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ)), invSqStripZero z :=
    tsum_congr_set_coe _ hunion
  have h2 := ENNReal.tsum_union_le invSqStripZero
    (zetaZeroCompactBlock : Set ℂ)
    (⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ))
  have h3 := ENNReal.tsum_iUnion_le_tsum invSqStripZero
    fun j : ℕ => (zetaZeroDyadicBlock j : Set ℂ)
  have hcomp : ∑' z : (zetaZeroCompactBlock : Set ℂ), invSqStripZero z =
      ∑ z ∈ zetaZeroCompactBlock, invSqStripZero z := tsum_invSq_compact
  have hdy : ∑' j : ℕ, ∑' z : (zetaZeroDyadicBlock j : Set ℂ), invSqStripZero z ≤
      ∑' j : ℕ, ENNReal.ofReal
        (zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j) := by
    refine ENNReal.tsum_le_tsum fun j => ?_
    rw [tsum_invSq_dyadic]
    exact sum_invSq_dyadic_le j
  calc
    ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, invSqStripZero z =
        ∑' z : ↥((zetaZeroCompactBlock : Set ℂ) ∪
            ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ)), invSqStripZero z := h1
    _ ≤ ∑' z : (zetaZeroCompactBlock : Set ℂ), invSqStripZero z +
          ∑' z : ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ), invSqStripZero z := h2
    _ ≤ ∑ z ∈ zetaZeroCompactBlock, invSqStripZero z +
          ∑' j : ℕ, ∑' z : (zetaZeroDyadicBlock j : Set ℂ), invSqStripZero z := by
        rw [hcomp]; exact add_le_add le_rfl h3
    _ ≤ ∑ z ∈ zetaZeroCompactBlock, invSqStripZero z +
          ∑' j : ℕ, ENNReal.ofReal
            (zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j) :=
        add_le_add le_rfl hdy

lemma tsum_dyadic_majorant_ne_top :
    (∑' j : ℕ, ENNReal.ofReal
        (zetaZeroInvSqBlockBound * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j)) ≠ ∞ := by
  have hf : ∀ n : ℕ, 0 ≤
      zetaZeroInvSqBlockBound * ((n : ℝ) + 2) * (2 : ℝ)⁻¹ ^ n := fun n =>
    mul_nonneg (mul_nonneg zetaZeroInvSqBlockBound_nonneg (by nlinarith))
      (pow_nonneg (by norm_num) _)
  rw [← ENNReal.ofReal_tsum_of_nonneg hf summable_dyadic_block_majorant]
  exact ENNReal.ofReal_ne_top

lemma tsum_invSq_strip_ne_top :
    (∑' z : {z : ℂ | IsCriticalStripZetaZero z}, invSqStripZero z) ≠ ∞ := by
  have hle := tsum_invSq_strip_le
  have h1 := sum_invSq_compact_ne_top
  have h2 := tsum_dyadic_majorant_ne_top
  exact ne_top_of_le_ne_top (ENNReal.add_ne_top.mpr ⟨h1, h2⟩) hle

lemma tsum_ofReal_inv_sq_ne_top :
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      ENNReal.ofReal (‖(ρ : ℂ)‖ ^ 2)⁻¹) ≠ ∞ := by
  have heq :
      (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
        ENNReal.ofReal (‖(ρ : ℂ)‖ ^ 2)⁻¹) =
        fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
          invSqStripZero ρ.val :=
    funext fun ρ => (invSqStripZero_eq_ofReal ρ.property).symm
  rw [heq]
  exact tsum_invSq_strip_ne_top

lemma summable_inv_sq_zetaZeros :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (‖(ρ : ℂ)‖ ^ 2)⁻¹ := by
  have htop := tsum_ofReal_inv_sq_ne_top
  have hNN := ENNReal.summable_toNNReal_of_tsum_ne_top htop
  refine (summable_congr fun ρ => ?_).mpr (NNReal.summable_coe.mpr hNN)
  refine Eq.trans (ENNReal.toReal_ofReal (inv_sq_nonneg (ρ : ℂ))).symm ?_
  rfl

end ZetaZeroInvSq

/-! ### r514: rectangle contour, one simple pole ([2d] entry)

Mathlib scoping (A): Cauchy-Goursat on rectangles is
`Complex.integral_boundary_rect_eq_zero_of_differentiableOn`
(four interval integrals, no `RectangleIntegral` type). Residues
live on circles (`circleIntegral.integral_sub_inv_of_mem_ball`,
Cauchy formula). There is no meromorphic residue theorem on
rectangles. Cheapest formalism: keep Mathlib's four-side sum,
punch the pole by the r498 split `f = r/(z-p)+h`, apply rectangle
Cauchy to `h`, and compute the rectangle integral of `1/(z-p)`
as `2πi` by an elementary arctan/log primitive
(no winding-number library).

[2d] contour design (C): rectangle `[-1/4, 2] × [-T, T]`.
Right edge `Re = 2` uses the Dirichlet series `ζ'/ζ = -Σ Λ(n)n^{-s}`.
Left edge `Re = -1/4` is folded by the functional equation onto
`Re = 5/4 > 1` (same Dirichlet bound) plus an explicit `χ'/χ`
(digamma). Keeping the left edge at `Re > 0` would miss
`0 < β < ε` zeros; pairing of test-function hats does not replace
enclosure. Horizontal edges die from `ĥ` decay (r506) times a
log-type `ζ'/ζ` bound. The residue identity on `Q_T` is
`∮ (ζ'/ζ) ĥ = spectralPartialSum ĥ - ĥ(1)`.
-/

section RectangleContour

open Complex intervalIntegral MeasureTheory Set
open scoped Interval

/-- Four-side rectangle contour, Mathlib Cauchy-Goursat convention
(bottom − top + `I`·right − `I`·left). -/
noncomputable def rectangleIntegral (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
  (∫ x : ℝ in z.re..w.re, f (x + z.im * I)) -
    (∫ x : ℝ in z.re..w.re, f (x + w.im * I)) +
    I • (∫ y : ℝ in z.im..w.im, f (w.re + y * I)) -
    I • (∫ y : ℝ in z.im..w.im, f (z.re + y * I))

lemma rectangleIntegral_eq_zero_of_differentiableOn
    (f : ℂ → ℂ) (z w : ℂ)
    (hf : DifferentiableOn ℂ f ([[z.re, w.re]] ×ℂ [[z.im, w.im]])) :
    rectangleIntegral f z w = 0 :=
  integral_boundary_rect_eq_zero_of_differentiableOn f z w hf

lemma add_I_mul_ne_zero {x γ : ℝ} (hγ : γ ≠ 0) :
    (x : ℂ) + γ * I ≠ 0 := by
  intro h
  apply hγ
  simpa using congrArg Complex.im h

lemma inv_add_I_mul {x γ : ℝ} (hγ : γ ≠ 0) :
    ((x : ℂ) + γ * I)⁻¹ =
      ((x : ℂ) - γ * I) / (x ^ 2 + γ ^ 2) := by
  have hden : (x ^ 2 + γ ^ 2 : ℝ) ≠ 0 :=
    (add_pos_of_nonneg_of_pos (sq_nonneg x) (sq_pos_of_ne_zero hγ)).ne'
  have hmul : ((x : ℂ) + γ * I) * ((x : ℂ) - γ * I) = ↑(x ^ 2 + γ ^ 2) := by
    calc ((x : ℂ) + γ * I) * ((x : ℂ) - γ * I)
        = (x : ℂ) ^ 2 - (γ : ℂ) ^ 2 * I ^ 2 := by ring
      _ = (x : ℂ) ^ 2 - (γ : ℂ) ^ 2 * (-1) := by rw [I_sq]
      _ = (x : ℂ) ^ 2 + (γ : ℂ) ^ 2 := by ring
      _ = ↑(x ^ 2 + γ ^ 2) := by norm_cast
  have hdenC : (x : ℂ) ^ 2 + (γ : ℂ) ^ 2 ≠ 0 := by exact_mod_cast hden
  rw [eq_div_iff hdenC, inv_mul_eq_iff_eq_mul₀ (add_I_mul_ne_zero hγ)]
  exact (hmul.trans (by norm_cast)).symm

lemma inv_add_I_mul' {x γ : ℝ} (hγ : γ ≠ 0) :
    ((x : ℂ) + γ * I)⁻¹ =
      (↑(x / (x ^ 2 + γ ^ 2)) : ℂ) - I * ↑(γ / (x ^ 2 + γ ^ 2)) := by
  calc ((x : ℂ) + γ * I)⁻¹
      = ((x : ℂ) - γ * I) / (x ^ 2 + γ ^ 2) := inv_add_I_mul hγ
    _ = (x : ℂ) / (x ^ 2 + γ ^ 2) - (γ : ℂ) * I / (x ^ 2 + γ ^ 2) :=
        sub_div _ _ _
    _ = ↑(x / (x ^ 2 + γ ^ 2)) - I * ↑(γ / (x ^ 2 + γ ^ 2)) := by
        rw [ofReal_div, ofReal_div]
        congr 1
        · norm_cast
        · rw [mul_comm (γ : ℂ) I, mul_div_assoc]
          congr 1
          norm_cast

lemma hasDerivAt_log_sq_add {γ : ℝ} (hγ : γ ≠ 0) (x : ℝ) :
    HasDerivAt (fun t : ℝ => Real.log (t ^ 2 + γ ^ 2))
      (2 * x / (x ^ 2 + γ ^ 2)) x := by
  have hpos : 0 < x ^ 2 + γ ^ 2 :=
    add_pos_of_nonneg_of_pos (sq_nonneg _) (sq_pos_of_ne_zero hγ)
  have hsq : HasDerivAt (fun t : ℝ => t ^ 2 + γ ^ 2) (2 * x) x := by
    simpa using (hasDerivAt_pow 2 x).add_const (γ ^ 2)
  convert (Real.hasDerivAt_log hpos.ne').comp x hsq using 1
  field_simp [hpos.ne']

lemma integral_x_div_sq_add (a b γ : ℝ) (hγ : γ ≠ 0) :
    ∫ x : ℝ in a..b, x / (x ^ 2 + γ ^ 2) =
      (1 / 2) * (Real.log (b ^ 2 + γ ^ 2) - Real.log (a ^ 2 + γ ^ 2)) := by
  have hpos : ∀ x : ℝ, x ^ 2 + γ ^ 2 ≠ 0 := fun x =>
    (add_pos_of_nonneg_of_pos (sq_nonneg x) (sq_pos_of_ne_zero hγ)).ne'
  have hderiv : ∀ x : ℝ,
      HasDerivAt (fun t : ℝ => (1 / 2) * Real.log (t ^ 2 + γ ^ 2))
        (x / (x ^ 2 + γ ^ 2)) x := by
    intro x
    convert (hasDerivAt_log_sq_add hγ x).const_mul (1 / 2) using 1
    ring
  have hcont : Continuous fun x : ℝ => x / (x ^ 2 + γ ^ 2) :=
    continuous_id.div ((continuous_pow 2).add continuous_const) hpos
  have hFTC :=
    integral_eq_sub_of_hasDerivAt (fun x (_ : x ∈ [[a, b]]) => hderiv x)
      (hcont.intervalIntegrable a b)
  convert hFTC using 1
  ring

lemma continuous_x_div_sq_add {γ : ℝ} (hγ : γ ≠ 0) :
    Continuous fun x : ℝ => x / (x ^ 2 + γ ^ 2) :=
  continuous_id.div ((continuous_pow 2).add continuous_const) fun x =>
    (add_pos_of_nonneg_of_pos (sq_nonneg x) (sq_pos_of_ne_zero hγ)).ne'

lemma continuous_const_div_sq_add (γ : ℝ) (hγ : γ ≠ 0) :
    Continuous fun x : ℝ => γ / (x ^ 2 + γ ^ 2) :=
  continuous_const.div ((continuous_pow 2).add continuous_const) fun x =>
    (add_pos_of_nonneg_of_pos (sq_nonneg x) (sq_pos_of_ne_zero hγ)).ne'

lemma continuous_inv_add_I_mul {γ : ℝ} (hγ : γ ≠ 0) :
    Continuous fun x : ℝ => ((x : ℂ) + γ * I)⁻¹ := by
  refine Continuous.congr ?_ fun x => (inv_add_I_mul' (x := x) hγ).symm
  exact (continuous_ofReal.comp (continuous_x_div_sq_add hγ)).sub
    (continuous_const.mul
      (continuous_ofReal.comp (continuous_const_div_sq_add γ hγ)))

lemma re_inv_add_I_mul {x γ : ℝ} (hγ : γ ≠ 0) :
    (((x : ℂ) + γ * I)⁻¹).re = x / (x ^ 2 + γ ^ 2) := by
  rw [inv_add_I_mul' hγ, sub_re, mul_re, I_re, I_im, ofReal_re, ofReal_im]
  ring

lemma im_inv_add_I_mul {x γ : ℝ} (hγ : γ ≠ 0) :
    (((x : ℂ) + γ * I)⁻¹).im = -(γ / (x ^ 2 + γ ^ 2)) := by
  rw [inv_add_I_mul' hγ, sub_im, mul_im, I_re, I_im, ofReal_re, ofReal_im]
  ring

lemma intervalIntegral_re {f : ℝ → ℂ} {a b : ℝ}
    (hf : IntervalIntegrable f volume a b) :
    (∫ x in a..b, f x).re = ∫ x in a..b, (f x).re :=
  (Complex.reCLM.intervalIntegral_comp_comm hf).symm

lemma intervalIntegral_im {f : ℝ → ℂ} {a b : ℝ}
    (hf : IntervalIntegrable f volume a b) :
    (∫ x in a..b, f x).im = ∫ x in a..b, (f x).im :=
  (Complex.imCLM.intervalIntegral_comp_comm hf).symm

lemma integral_inv_add_I_mul (a b γ : ℝ) (hγ : γ ≠ 0) :
    ∫ x : ℝ in a..b, ((x : ℂ) + γ * I)⁻¹ =
      ((1 : ℂ) / 2) * ↑(Real.log (b ^ 2 + γ ^ 2) - Real.log (a ^ 2 + γ ^ 2)) -
        I * ↑(Real.arctan (b / γ) - Real.arctan (a / γ)) := by
  have hf : IntervalIntegrable (fun x : ℝ => ((x : ℂ) + γ * I)⁻¹) volume a b :=
    (continuous_inv_add_I_mul hγ).intervalIntegrable a b
  have hsame : (fun x : ℝ => γ / (x ^ 2 + γ ^ 2)) =
      fun x : ℝ => γ / (γ ^ 2 + x ^ 2) :=
    funext fun x => by ring
  apply Complex.ext
  · rw [intervalIntegral_re hf]
    simp_rw [re_inv_add_I_mul hγ]
    rw [integral_x_div_sq_add a b γ hγ]
    simp [sub_re, mul_re, ofReal_re, I_re, I_im]
  · rw [intervalIntegral_im hf]
    simp_rw [im_inv_add_I_mul hγ]
    rw [intervalIntegral.integral_neg, hsame, integral_div_sq_add_sq]
    simp [sub_im, mul_im, ofReal_im, ofReal_re, I_re, I_im]

lemma inv_re_add_mul_I {σ y : ℝ} (hσ : σ ≠ 0) :
    ((σ : ℂ) + y * I)⁻¹ = -I * ((y : ℂ) + (-σ) * I)⁻¹ := by
  have hI : (σ : ℂ) + y * I = I * ((y : ℂ) + (-σ) * I) := by
    calc (σ : ℂ) + y * I
        = -(σ : ℂ) * I * I + y * I := by
          rw [mul_assoc, I_mul_I, mul_neg_one, neg_neg]
      _ = I * ((y : ℂ) + (-σ) * I) := by ring
  rw [hI, mul_inv_rev, inv_I]
  ring

lemma inv_re_add_mul_I_div' {σ y : ℝ} (hσ : σ ≠ 0) :
    ((σ : ℂ) + y * I)⁻¹ =
      (↑(σ / (σ ^ 2 + y ^ 2)) : ℂ) - I * ↑(y / (σ ^ 2 + y ^ 2)) := by
  calc ((σ : ℂ) + y * I)⁻¹
      = -I * ((y : ℂ) + (-σ) * I)⁻¹ := inv_re_add_mul_I hσ
    _ = -I * ((y : ℂ) + ↑(-σ) * I)⁻¹ := by simp
    _ = -I * (↑(y / (y ^ 2 + (-σ) ^ 2)) -
          I * ↑((-σ) / (y ^ 2 + (-σ) ^ 2))) := by
        rw [inv_add_I_mul' (neg_ne_zero.mpr hσ)]
    _ = -I * (↑(y / (y ^ 2 + σ ^ 2)) - I * ↑((-σ) / (y ^ 2 + σ ^ 2))) := by
        rw [neg_sq]
    _ = -I * ↑(y / (y ^ 2 + σ ^ 2)) + (I * I) * ↑((-σ) / (y ^ 2 + σ ^ 2)) := by
        rw [mul_sub]; ring
    _ = -I * ↑(y / (y ^ 2 + σ ^ 2)) + (-1) * ↑((-σ) / (y ^ 2 + σ ^ 2)) := by
        rw [I_mul_I]
    _ = ↑(σ / (σ ^ 2 + y ^ 2)) - I * ↑(y / (σ ^ 2 + y ^ 2)) := by
        simp [neg_div, ofReal_neg, add_comm]
        ring

lemma continuous_inv_re_add_mul_I {σ : ℝ} (hσ : σ ≠ 0) :
    Continuous fun y : ℝ => ((σ : ℂ) + y * I)⁻¹ := by
  have hcongr :
      (fun y : ℝ => ((σ : ℂ) + y * I)⁻¹) =
        fun y : ℝ =>
          (↑(σ / (σ ^ 2 + y ^ 2)) : ℂ) - I * ↑(y / (σ ^ 2 + y ^ 2)) :=
    funext fun y => inv_re_add_mul_I_div' hσ
  rw [hcongr]
  refine (continuous_ofReal.comp ?_).sub
      (continuous_const.mul (continuous_ofReal.comp ?_))
  · exact (continuous_const_div_sq_add σ hσ).congr fun y => by ring
  · exact (continuous_x_div_sq_add hσ).congr fun y => by ring

lemma re_inv_re_add_mul_I {σ y : ℝ} (hσ : σ ≠ 0) :
    (((σ : ℂ) + y * I)⁻¹).re = σ / (σ ^ 2 + y ^ 2) := by
  rw [inv_re_add_mul_I_div' hσ, sub_re, mul_re, I_re, I_im, ofReal_re, ofReal_im]
  ring

lemma im_inv_re_add_mul_I {σ y : ℝ} (hσ : σ ≠ 0) :
    (((σ : ℂ) + y * I)⁻¹).im = -(y / (σ ^ 2 + y ^ 2)) := by
  rw [inv_re_add_mul_I_div' hσ, sub_im, mul_im, I_re, I_im, ofReal_re, ofReal_im]
  ring

lemma integral_inv_re_add_mul_I (σ a b : ℝ) (hσ : σ ≠ 0) :
    ∫ y : ℝ in a..b, ((σ : ℂ) + y * I)⁻¹ =
      ↑(Real.arctan (b / σ) - Real.arctan (a / σ)) -
        I * ((1 / 2 : ℂ) *
          ↑(Real.log (σ ^ 2 + b ^ 2) - Real.log (σ ^ 2 + a ^ 2))) := by
  have hf : IntervalIntegrable (fun y : ℝ => ((σ : ℂ) + y * I)⁻¹) volume a b :=
    (continuous_inv_re_add_mul_I hσ).intervalIntegrable a b
  have hsame : (fun y : ℝ => y / (σ ^ 2 + y ^ 2)) =
      fun y : ℝ => y / (y ^ 2 + σ ^ 2) :=
    funext fun y => by ring
  apply Complex.ext
  · rw [intervalIntegral_re hf]
    simp_rw [re_inv_re_add_mul_I hσ]
    rw [integral_div_sq_add_sq]
    simp [sub_re, mul_re, ofReal_re, I_re, I_im]
  · rw [intervalIntegral_im hf]
    simp_rw [im_inv_re_add_mul_I hσ]
    rw [intervalIntegral.integral_neg, hsame, integral_x_div_sq_add a b σ hσ]
    simp [sub_im, mul_im, ofReal_im, ofReal_re, I_re, I_im, add_comm]

lemma arctan_add_inv_pos {x : ℝ} (hx : 0 < x) :
    Real.arctan x + Real.arctan x⁻¹ = Real.pi / 2 := by
  rw [Real.arctan_inv_of_pos hx]
  ring

lemma arctan_add_inv_neg {x : ℝ} (hx : x < 0) :
    Real.arctan x + Real.arctan x⁻¹ = -(Real.pi / 2) := by
  rw [Real.arctan_inv_of_neg hx]
  ring

lemma rectangle_inv_arctan_sum
    {α β γ Γ : ℝ} (hα : α < 0) (hβ : 0 < β) (hγ : γ < 0) (hΓ : 0 < Γ) :
    -(Real.arctan (β / γ) - Real.arctan (α / γ))
      + (Real.arctan (β / Γ) - Real.arctan (α / Γ))
      + (Real.arctan (Γ / β) - Real.arctan (γ / β))
      - (Real.arctan (Γ / α) - Real.arctan (γ / α))
    = 2 * Real.pi := by
  have hTR : Real.arctan (β / Γ) + Real.arctan (Γ / β) = Real.pi / 2 := by
    have := arctan_add_inv_pos (div_pos hβ hΓ)
    rwa [inv_div] at this
  have hBR : -(Real.arctan (β / γ) + Real.arctan (γ / β)) = Real.pi / 2 := by
    have := arctan_add_inv_neg (div_neg_of_pos_of_neg hβ hγ)
    rw [inv_div] at this
    linarith
  have hTL : -(Real.arctan (α / Γ) + Real.arctan (Γ / α)) = Real.pi / 2 := by
    have := arctan_add_inv_neg (div_neg_of_neg_of_pos hα hΓ)
    rw [inv_div] at this
    linarith
  have hBL : Real.arctan (α / γ) + Real.arctan (γ / α) = Real.pi / 2 := by
    have := arctan_add_inv_pos (div_pos_of_neg_of_neg hα hγ)
    rwa [inv_div] at this
  calc
      -(Real.arctan (β / γ) - Real.arctan (α / γ))
        + (Real.arctan (β / Γ) - Real.arctan (α / Γ))
        + (Real.arctan (Γ / β) - Real.arctan (γ / β))
        - (Real.arctan (Γ / α) - Real.arctan (γ / α))
      = (Real.arctan (β / Γ) + Real.arctan (Γ / β))
          + (-(Real.arctan (β / γ) + Real.arctan (γ / β)))
          + (-(Real.arctan (α / Γ) + Real.arctan (Γ / α)))
          + (Real.arctan (α / γ) + Real.arctan (γ / α)) := by ring
    _ = Real.pi / 2 + Real.pi / 2 + Real.pi / 2 + Real.pi / 2 := by
        rw [hTR, hBR, hTL, hBL]
    _ = 2 * Real.pi := by ring

lemma sub_side_eq (p : ℂ) (x im : ℝ) :
    (x + im * I) - p = ((x - p.re : ℝ) : ℂ) + (im - p.im) * I := by
  apply Complex.ext <;> simp

lemma rectangleIntegral_inv_of_zero_mem (z w : ℂ)
    (hre : z.re < 0) (hre' : 0 < w.re)
    (him : z.im < 0) (him' : 0 < w.im) :
    rectangleIntegral (fun ζ => ζ⁻¹) z w = 2 * (Real.pi : ℂ) * I := by
  have hzre : z.re ≠ 0 := hre.ne
  have hwre : w.re ≠ 0 := hre'.ne'
  have hzim : z.im ≠ 0 := him.ne
  have hwim : w.im ≠ 0 := him'.ne'
  have hsum := rectangle_inv_arctan_sum hre hre' him him'
  simp only [rectangleIntegral]
  rw [integral_inv_add_I_mul z.re w.re z.im hzim,
    integral_inv_add_I_mul z.re w.re w.im hwim,
    integral_inv_re_add_mul_I w.re z.im w.im hwre,
    integral_inv_re_add_mul_I z.re z.im w.im hzre]
  apply Complex.ext
  · simp [smul_eq_mul, sub_re, mul_re, add_re, ofReal_re, I_re, I_im]
    ring
  · simp [smul_eq_mul, sub_im, mul_im, add_im, ofReal_im, ofReal_re, I_re, I_im]
    linarith [hsum]


/-- Horizontal side after a complex translation: only `p.re` shifts the
real parameter. -/
lemma add_horiz_shift (p : ℂ) (x im : ℝ) :
    ((x : ℂ) + ↑(im - p.im) * I) + p = ((x + p.re : ℝ) : ℂ) + im * I := by
  apply Complex.ext
  · simp [add_re, mul_re, I_re, I_im]
  · simp [add_im, mul_im, I_re, I_im]

/-- Vertical side after a complex translation: only `p.im` shifts the
real parameter. -/
lemma add_vert_shift (p : ℂ) (σ y : ℝ) :
    (↑(σ - p.re) : ℂ) + y * I + p = (σ : ℂ) + ↑(y + p.im) * I := by
  apply Complex.ext
  · simp [add_re, mul_re, I_re, I_im]
  · simp [add_im, mul_im, I_re, I_im]

lemma intervalIntegral_horiz_shift (f : ℂ → ℂ) (a b im : ℝ) (p : ℂ) :
    (∫ x : ℝ in (a - p.re)..(b - p.re),
        f (((x : ℂ) + ↑(im - p.im) * I) + p)) =
      ∫ x : ℝ in a..b, f ((x : ℂ) + im * I) := by
  simp_rw [add_horiz_shift]
  exact (intervalIntegral.integral_comp_add_right
      (fun t : ℝ => f ((t : ℂ) + im * I)) p.re).trans
    (by simp [sub_add_cancel])

lemma intervalIntegral_vert_shift (f : ℂ → ℂ) (σ a b : ℝ) (p : ℂ) :
    (∫ y : ℝ in (a - p.im)..(b - p.im),
        f ((↑(σ - p.re) : ℂ) + y * I + p)) =
      ∫ y : ℝ in a..b, f ((σ : ℂ) + y * I) := by
  simp_rw [add_vert_shift]
  exact (intervalIntegral.integral_comp_add_right
      (fun t : ℝ => f ((σ : ℂ) + t * I)) p.im).trans
    (by simp [sub_add_cancel])

/-- Substitution `g(ζ) = f(ζ + p)`: the four-side rectangle integral
is invariant.  Horizontal sides use `p.re`; vertical sides use `p.im`. -/
lemma rectangleIntegral_comp_add (f : ℂ → ℂ) (z w p : ℂ) :
    rectangleIntegral (fun ζ => f (ζ + p)) (z - p) (w - p) =
      rectangleIntegral f z w := by
  simp only [rectangleIntegral, sub_re, sub_im]
  rw [intervalIntegral_horiz_shift f z.re w.re z.im p,
    intervalIntegral_horiz_shift f z.re w.re w.im p,
    intervalIntegral_vert_shift f w.re z.im w.im p,
    intervalIntegral_vert_shift f z.re z.im w.im p]

lemma rectangleIntegral_comp_sub (f : ℂ → ℂ) (z w p : ℂ) :
    rectangleIntegral (fun ζ => f (ζ - p)) z w =
      rectangleIntegral f (z - p) (w - p) := by
  simpa [sub_eq_add_neg, add_comm, sub_neg_eq_add] using
    rectangleIntegral_comp_add f (z - p) (w - p) (-p)

lemma rectangleIntegral_inv_of_mem (z w p : ℂ)
    (hre : z.re < p.re) (hre' : p.re < w.re)
    (him : z.im < p.im) (him' : p.im < w.im) :
    rectangleIntegral (fun ζ => (ζ - p)⁻¹) z w = 2 * (Real.pi : ℂ) * I := by
  rw [rectangleIntegral_comp_sub (fun ξ => ξ⁻¹) z w p]
  refine rectangleIntegral_inv_of_zero_mem (z - p) (w - p) ?_ ?_ ?_ ?_
  · simpa [sub_re] using sub_neg.mpr hre
  · simpa [sub_re] using sub_pos.mpr hre'
  · simpa [sub_im] using sub_neg.mpr him
  · simpa [sub_im] using sub_pos.mpr him'

lemma rectangleIntegral_const_mul (c : ℂ) (f : ℂ → ℂ) (z w : ℂ) :
    rectangleIntegral (fun ζ => c * f ζ) z w = c * rectangleIntegral f z w := by
  simp only [rectangleIntegral]
  simp_rw [← smul_eq_mul, intervalIntegral.integral_smul]
  simp [smul_add, smul_comm c I]
  ring

lemma rectangleIntegral_add (f g : ℂ → ℂ) (z w : ℂ)
    (hfb : IntervalIntegrable (fun x : ℝ => f ((x : ℂ) + z.im * I)) volume z.re w.re)
    (hft : IntervalIntegrable (fun x : ℝ => f ((x : ℂ) + w.im * I)) volume z.re w.re)
    (hfr : IntervalIntegrable (fun y : ℝ => f ((w.re : ℂ) + y * I)) volume z.im w.im)
    (hfl : IntervalIntegrable (fun y : ℝ => f ((z.re : ℂ) + y * I)) volume z.im w.im)
    (hgb : IntervalIntegrable (fun x : ℝ => g ((x : ℂ) + z.im * I)) volume z.re w.re)
    (hgt : IntervalIntegrable (fun x : ℝ => g ((x : ℂ) + w.im * I)) volume z.re w.re)
    (hgr : IntervalIntegrable (fun y : ℝ => g ((w.re : ℂ) + y * I)) volume z.im w.im)
    (hgl : IntervalIntegrable (fun y : ℝ => g ((z.re : ℂ) + y * I)) volume z.im w.im) :
    rectangleIntegral (fun ζ => f ζ + g ζ) z w =
      rectangleIntegral f z w + rectangleIntegral g z w := by
  simp only [rectangleIntegral]
  rw [intervalIntegral.integral_add hfb hgb, intervalIntegral.integral_add hft hgt,
    intervalIntegral.integral_add hfr hgr, intervalIntegral.integral_add hfl hgl]
  simp [smul_eq_mul, mul_add, sub_eq_add_neg]
  ring

lemma continuous_side_inv_sub_horiz (p : ℂ) {im : ℝ} (him : im ≠ p.im) :
    Continuous fun x : ℝ => ((x : ℂ) + im * I - p)⁻¹ :=
  ((continuous_ofReal.add continuous_const).sub continuous_const).inv₀ fun _ => by
    intro h
    apply him
    exact sub_eq_zero.mp (by simpa [sub_im] using congrArg Complex.im h)

lemma continuous_side_inv_sub_vert (p : ℂ) {σ : ℝ} (hσ : σ ≠ p.re) :
    Continuous fun y : ℝ => ((σ : ℂ) + y * I - p)⁻¹ :=
  ((continuous_const.add (continuous_ofReal.mul continuous_const)).sub
      continuous_const).inv₀ fun _ => by
    intro h
    apply hσ
    exact sub_eq_zero.mp (by simpa [sub_re] using congrArg Complex.re h)

lemma mem_closedRect_horiz {z w : ℂ} {im x : ℝ}
    (hx : x ∈ [[z.re, w.re]]) (him : im ∈ [[z.im, w.im]]) :
    (x : ℂ) + im * I ∈ [[z.re, w.re]] ×ℂ [[z.im, w.im]] := by
  refine mem_reProdIm.mpr ⟨?_, ?_⟩
  · simpa [add_re, mul_re, I_re, I_im, ofReal_re] using hx
  · simpa [add_im, mul_im, I_re, I_im, ofReal_im] using him

lemma mem_closedRect_vert {z w : ℂ} {σ y : ℝ}
    (hσ : σ ∈ [[z.re, w.re]]) (hy : y ∈ [[z.im, w.im]]) :
    (σ : ℂ) + y * I ∈ [[z.re, w.re]] ×ℂ [[z.im, w.im]] := by
  refine mem_reProdIm.mpr ⟨?_, ?_⟩
  · simpa [add_re, mul_re, I_re, I_im, ofReal_re] using hσ
  · simpa [add_im, mul_im, I_re, I_im, ofReal_im] using hy

lemma intervalIntegrable_holomorphic_horiz (h : ℂ → ℂ) (z w : ℂ) {im : ℝ}
    (hh : ContinuousOn h ([[z.re, w.re]] ×ℂ [[z.im, w.im]]))
    (him : im ∈ [[z.im, w.im]]) :
    IntervalIntegrable (fun x : ℝ => h ((x : ℂ) + im * I)) volume z.re w.re :=
  (hh.comp (continuous_ofReal.add continuous_const).continuousOn
      fun _ hx => mem_closedRect_horiz hx him).intervalIntegrable

lemma intervalIntegrable_holomorphic_vert (h : ℂ → ℂ) (z w : ℂ) {σ : ℝ}
    (hh : ContinuousOn h ([[z.re, w.re]] ×ℂ [[z.im, w.im]]))
    (hσ : σ ∈ [[z.re, w.re]]) :
    IntervalIntegrable (fun y : ℝ => h ((σ : ℂ) + y * I)) volume z.im w.im :=
  (hh.comp (continuous_const.add (continuous_ofReal.mul continuous_const)).continuousOn
      fun _ hy => mem_closedRect_vert hσ hy).intervalIntegrable

/-- One simple pole in the open rectangle, with holomorphic remainder
already extended to the closed rectangle (the r498 split). -/
lemma rectangleIntegral_simple_pole (h : ℂ → ℂ) (z w p r : ℂ)
    (hh : DifferentiableOn ℂ h ([[z.re, w.re]] ×ℂ [[z.im, w.im]]))
    (hre : z.re < p.re) (hre' : p.re < w.re)
    (him : z.im < p.im) (him' : p.im < w.im) :
    rectangleIntegral (fun ζ => r / (ζ - p) + h ζ) z w =
      (2 * (Real.pi : ℂ) * I) * r := by
  have hhol := rectangleIntegral_eq_zero_of_differentiableOn h z w hh
  have hwind := rectangleIntegral_inv_of_mem z w p hre hre' him him'
  have hcont := hh.continuousOn
  have hhb := intervalIntegrable_holomorphic_horiz h z w hcont left_mem_uIcc
  have hht := intervalIntegrable_holomorphic_horiz h z w hcont right_mem_uIcc
  have hhr := intervalIntegrable_holomorphic_vert h z w hcont right_mem_uIcc
  have hhl := intervalIntegrable_holomorphic_vert h z w hcont left_mem_uIcc
  have hfb : IntervalIntegrable
      (fun x : ℝ => r * (((x : ℂ) + z.im * I - p)⁻¹)) volume z.re w.re :=
    (continuous_const.mul (continuous_side_inv_sub_horiz p him.ne)).intervalIntegrable _ _
  have hft : IntervalIntegrable
      (fun x : ℝ => r * (((x : ℂ) + w.im * I - p)⁻¹)) volume z.re w.re :=
    (continuous_const.mul (continuous_side_inv_sub_horiz p him'.ne')).intervalIntegrable _ _
  have hfr : IntervalIntegrable
      (fun y : ℝ => r * (((w.re : ℂ) + y * I - p)⁻¹)) volume z.im w.im :=
    (continuous_const.mul (continuous_side_inv_sub_vert p hre'.ne')).intervalIntegrable _ _
  have hfl : IntervalIntegrable
      (fun y : ℝ => r * (((z.re : ℂ) + y * I - p)⁻¹)) volume z.im w.im :=
    (continuous_const.mul (continuous_side_inv_sub_vert p hre.ne)).intervalIntegrable _ _
  have hadd :=
    rectangleIntegral_add (fun ζ => r * (ζ - p)⁻¹) h z w
      hfb hft hfr hfl hhb hht hhr hhl
  have hdiv : (fun ζ : ℂ => r / (ζ - p) + h ζ) =
      fun ζ => r * (ζ - p)⁻¹ + h ζ :=
    funext fun ζ => by rw [div_eq_mul_inv]
  rw [hdiv, hadd, rectangleIntegral_const_mul, hhol, hwind]
  ring

lemma rectangleIntegral_div_sub (z w p r : ℂ)
    (hre : z.re < p.re) (hre' : p.re < w.re)
    (him : z.im < p.im) (him' : p.im < w.im) :
    rectangleIntegral (fun ζ => r / (ζ - p)) z w =
      (2 * (Real.pi : ℂ) * I) * r := by
  have h0 :
      (fun ζ : ℂ => r / (ζ - p) + (0 : ℂ)) = fun ζ => r / (ζ - p) := by
    funext ζ; simp
  rw [← h0]
  exact rectangleIntegral_simple_pole (fun _ => 0) z w p r
    (differentiableOn_const 0) hre hre' him him'

lemma intervalIntegrable_div_sub_horiz (p r : ℂ) (a b im : ℝ)
    (him : im ≠ p.im) :
    IntervalIntegrable (fun x : ℝ => r / ((x : ℂ) + im * I - p)) volume a b := by
  have hfun :
      (fun x : ℝ => r / ((x : ℂ) + im * I - p)) =
        fun x : ℝ => r * ((x : ℂ) + im * I - p)⁻¹ :=
    funext fun _ => div_eq_mul_inv _ _
  rw [hfun]
  exact (continuous_const.mul (continuous_side_inv_sub_horiz p him)).intervalIntegrable a b

lemma intervalIntegrable_div_sub_vert (p r : ℂ) (σ a b : ℝ)
    (hσ : σ ≠ p.re) :
    IntervalIntegrable (fun y : ℝ => r / ((σ : ℂ) + y * I - p)) volume a b := by
  have hfun :
      (fun y : ℝ => r / ((σ : ℂ) + y * I - p)) =
        fun y : ℝ => r * ((σ : ℂ) + y * I - p)⁻¹ :=
    funext fun _ => div_eq_mul_inv _ _
  rw [hfun]
  exact (continuous_const.mul (continuous_side_inv_sub_vert p hσ)).intervalIntegrable a b

lemma intervalIntegrable_sum_div_horiz (s : Finset ℂ) (r : ℂ → ℂ)
    (a b im : ℝ) (him : ∀ p ∈ s, im ≠ p.im) :
    IntervalIntegrable
      (fun x : ℝ => ∑ p ∈ s, r p / ((x : ℂ) + im * I - p)) volume a b := by
  have hfun :
      (fun x : ℝ => ∑ p ∈ s, r p / ((x : ℂ) + im * I - p)) =
        fun x : ℝ => ∑ p ∈ s, r p * ((x : ℂ) + im * I - p)⁻¹ :=
    funext fun _ => by simp_rw [div_eq_mul_inv]
  rw [hfun]
  exact (continuous_finset_sum s fun p hp =>
      continuous_const.mul (continuous_side_inv_sub_horiz p (him p hp))).intervalIntegrable a b

lemma intervalIntegrable_sum_div_vert (s : Finset ℂ) (r : ℂ → ℂ)
    (σ a b : ℝ) (hσ : ∀ p ∈ s, σ ≠ p.re) :
    IntervalIntegrable
      (fun y : ℝ => ∑ p ∈ s, r p / ((σ : ℂ) + y * I - p)) volume a b := by
  have hfun :
      (fun y : ℝ => ∑ p ∈ s, r p / ((σ : ℂ) + y * I - p)) =
        fun y : ℝ => ∑ p ∈ s, r p * ((σ : ℂ) + y * I - p)⁻¹ :=
    funext fun _ => by simp_rw [div_eq_mul_inv]
  rw [hfun]
  exact (continuous_finset_sum s fun p hp =>
      continuous_const.mul (continuous_side_inv_sub_vert p (hσ p hp))).intervalIntegrable a b

/-- Finite simple-pole sum, no remainder.  Interior poles make every
side miss every pole, so each summand is continuous on the side. -/
lemma rectangleIntegral_sum_div (s : Finset ℂ) (r : ℂ → ℂ) (z w : ℂ)
    (hp : ∀ p ∈ s, z.re < p.re ∧ p.re < w.re ∧ z.im < p.im ∧ p.im < w.im) :
    rectangleIntegral (fun ζ => ∑ p ∈ s, r p / (ζ - p)) z w =
      (2 * (Real.pi : ℂ) * I) * ∑ p ∈ s, r p := by
  classical
  revert hp
  refine Finset.induction_on s ?empty ?insert
  · intro _hp
    simp [rectangleIntegral]
  · intro p s hps ih hp
    have hp' := hp p (Finset.mem_insert_self p s)
    have hs : ∀ q ∈ s,
        z.re < q.re ∧ q.re < w.re ∧ z.im < q.im ∧ q.im < w.im :=
      fun q hq => hp q (Finset.mem_insert_of_mem hq)
    have hadd := rectangleIntegral_add
      (fun ζ => r p / (ζ - p))
      (fun ζ => ∑ q ∈ s, r q / (ζ - q)) z w
      (intervalIntegrable_div_sub_horiz p (r p) z.re w.re z.im hp'.2.2.1.ne)
      (intervalIntegrable_div_sub_horiz p (r p) z.re w.re w.im hp'.2.2.2.ne.symm)
      (intervalIntegrable_div_sub_vert p (r p) w.re z.im w.im hp'.2.1.ne.symm)
      (intervalIntegrable_div_sub_vert p (r p) z.re z.im w.im hp'.1.ne)
      (intervalIntegrable_sum_div_horiz s r z.re w.re z.im
        fun q hq => (hs q hq).2.2.1.ne)
      (intervalIntegrable_sum_div_horiz s r z.re w.re w.im
        fun q hq => (hs q hq).2.2.2.ne.symm)
      (intervalIntegrable_sum_div_vert s r w.re z.im w.im
        fun q hq => (hs q hq).2.1.ne.symm)
      (intervalIntegrable_sum_div_vert s r z.re z.im w.im
        fun q hq => (hs q hq).1.ne)
    have hfun :
        (fun ζ : ℂ => ∑ q ∈ insert p s, r q / (ζ - q)) =
          fun ζ => r p / (ζ - p) + ∑ q ∈ s, r q / (ζ - q) := by
      funext ζ
      exact Finset.sum_insert hps
    rw [hfun, hadd, rectangleIntegral_div_sub z w p (r p)
      hp'.1 hp'.2.1 hp'.2.2.1 hp'.2.2.2, ih hs, Finset.sum_insert hps]
    ring

/-- r498-style Finset punch: `f = Σ r_p/(·-p) + h` with `h` holomorphic
on the closed rectangle.  One Cauchy call on `h`. -/
lemma rectangleIntegral_sum_simple_poles (h : ℂ → ℂ) (z w : ℂ)
    (s : Finset ℂ) (r : ℂ → ℂ)
    (hh : DifferentiableOn ℂ h ([[z.re, w.re]] ×ℂ [[z.im, w.im]]))
    (hp : ∀ p ∈ s, z.re < p.re ∧ p.re < w.re ∧ z.im < p.im ∧ p.im < w.im) :
    rectangleIntegral (fun ζ => (∑ p ∈ s, r p / (ζ - p)) + h ζ) z w =
      (2 * (Real.pi : ℂ) * I) * ∑ p ∈ s, r p := by
  have hhol := rectangleIntegral_eq_zero_of_differentiableOn h z w hh
  have hc := hh.continuousOn
  have hadd := rectangleIntegral_add
    (fun ζ => ∑ p ∈ s, r p / (ζ - p)) h z w
    (intervalIntegrable_sum_div_horiz s r z.re w.re z.im
      fun p hp' => (hp p hp').2.2.1.ne)
    (intervalIntegrable_sum_div_horiz s r z.re w.re w.im
      fun p hp' => (hp p hp').2.2.2.ne.symm)
    (intervalIntegrable_sum_div_vert s r w.re z.im w.im
      fun p hp' => (hp p hp').2.1.ne.symm)
    (intervalIntegrable_sum_div_vert s r z.re z.im w.im
      fun p hp' => (hp p hp').1.ne)
    (intervalIntegrable_holomorphic_horiz h z w hc left_mem_uIcc)
    (intervalIntegrable_holomorphic_horiz h z w hc right_mem_uIcc)
    (intervalIntegrable_holomorphic_vert h z w hc right_mem_uIcc)
    (intervalIntegrable_holomorphic_vert h z w hc left_mem_uIcc)
  rw [hadd, rectangleIntegral_sum_div s r z w hp, hhol]
  ring


end RectangleContour

/-! ### r516: residue identity on a fixed rectangle ([2d] assembly)

The remainder `f − Σ r_p/(·−p)` of `(ζ′/ζ)·ĥ` is meromorphic of
nonnegative order at every point of the closed rectangle (local
r498/r500 split times an analytic factor, then cancel the principal
part).  Mathlib fills a nonnegative-order germ by `update`.
-/

section ContourRemainder

open Complex Filter Function Set
open scoped Topology

/-- Nonnegative meromorphic order is a removable singularity:
updating the value at the point yields an analytic germ
(the r500 `update` pattern, abstracted). -/
lemma exists_analyticAt_update_of_meromorphicOrderAt_nonneg
    {f : ℂ → ℂ} {x : ℂ}
    (hf : MeromorphicAt f x) (ho : 0 ≤ meromorphicOrderAt f x) :
    ∃ c : ℂ, AnalyticAt ℂ (update f x c) x := by
  obtain ⟨c, hc⟩ := tendsto_nhds_of_meromorphicOrderAt_nonneg hf ho
  refine ⟨c, ?_⟩
  have hcont : ContinuousAt (update f x c) x :=
    continuousAt_update_same.mpr hc
  have hmer : MeromorphicAt (update f x c) x :=
    hf.congr (by
      filter_upwards [self_mem_nhdsWithin] with z hz
      exact (update_of_ne hz _ _).symm)
  exact hmer.analyticAt hcont

/-- `dslope` of an analytic germ is analytic (open-ball form of
`Complex.differentiableOn_dslope`). -/
lemma analyticAt_dslope {F : ℂ → ℂ} {s : ℂ} (hF : AnalyticAt ℂ F s) :
    AnalyticAt ℂ (dslope F s) s := by
  obtain ⟨r, hr, hball⟩ := hF.exists_ball_analyticOnNhd
  have hU : Metric.ball s r ∈ 𝓝 s := Metric.ball_mem_nhds s hr
  have hdiff : DifferentiableOn ℂ F (Metric.ball s r) :=
    fun z hz => (hball z hz).differentiableAt.differentiableWithinAt
  have hds : DifferentiableOn ℂ (dslope F s) (Metric.ball s r) :=
    (Complex.differentiableOn_dslope (s := Metric.ball s r) hU).mpr hdiff
  exact hds.analyticAt hU

/-- r498 × analytic factor: at a non-polar zero the principal part of
`(ζ′/ζ)·F` is `m_s·F(s)/(z−s)`, with analytic remainder.  If `F s = 0`
the principal part vanishes and the product is already analytic. -/
lemma exists_analytic_logDeriv_mul_sub {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1)
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F s) :
    ∃ H : ℂ → ℂ, AnalyticAt ℂ H s ∧
      ∀ᶠ z in 𝓝[≠] s,
        logDeriv riemannZeta z * F z =
          (riemannZetaMultiplicity s : ℂ) * F s / (z - s) + H z := by
  obtain ⟨h, hh, heq⟩ :=
    logDeriv_riemannZeta_eq_multiplicity_div_add_analytic hz hs
  refine ⟨fun z =>
      (riemannZetaMultiplicity s : ℂ) * dslope F s z + h z * F z, ?_, ?_⟩
  · exact ((analyticAt_const.mul (analyticAt_dslope hF)).add
      (hh.mul hF))
  · filter_upwards [heq, self_mem_nhdsWithin] with z hzlog hzne
    have hz0 : z - s ≠ 0 := sub_ne_zero.mpr hzne
    rw [hzlog, dslope_of_ne F hzne]
    have hslope :
        slope F s z = (z - s)⁻¹ * (F z - F s) := rfl
    rw [hslope]
    field_simp [hz0]
    ring

/-- r500 × analytic factor: at `s = 1` the principal part of
`(ζ′/ζ)·F` is `−F(1)/(z−1)`. -/
lemma exists_analytic_logDeriv_mul_sub_one
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F 1) :
    ∃ H : ℂ → ℂ, AnalyticAt ℂ H 1 ∧
      ∀ᶠ z in 𝓝[≠] 1,
        logDeriv riemannZeta z * F z = -F 1 / (z - 1) + H z := by
  obtain ⟨h, hh, heq⟩ := logDeriv_riemannZeta_eq_neg_one_div_add_analytic
  refine ⟨fun z => -dslope F 1 z + h z * F z, ?_, ?_⟩
  · exact ((analyticAt_dslope hF).neg.add (hh.mul hF))
  · filter_upwards [heq, self_mem_nhdsWithin] with z hzlog hzne
    have hz0 : z - 1 ≠ 0 := sub_ne_zero.mpr hzne
    rw [hzlog, dslope_of_ne F hzne]
    have hslope :
        slope F 1 z = (z - 1)⁻¹ * (F z - F 1) := rfl
    rw [hslope]
    field_simp [hz0]
    ring

/-- The punched product has nonnegative meromorphic order at a
non-polar zero (principal parts cancel). -/
lemma meromorphicOrderAt_logDeriv_mul_sub_nonneg {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1)
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F s) :
    0 ≤ meromorphicOrderAt
      (fun z => logDeriv riemannZeta z * F z
        - (riemannZetaMultiplicity s : ℂ) * F s / (z - s)) s := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDeriv_mul_sub hz hs hF
  have hcong :
      (fun z => logDeriv riemannZeta z * F z
        - (riemannZetaMultiplicity s : ℂ) * F s / (z - s))
        =ᶠ[𝓝[≠] s] H := by
    filter_upwards [heq] with z hz
    rw [hz, add_comm, add_sub_cancel_right]
  rw [meromorphicOrderAt_congr hcong]
  exact hH.meromorphicOrderAt_nonneg

/-- The punched product has nonnegative meromorphic order at `s = 1`. -/
lemma meromorphicOrderAt_logDeriv_mul_sub_one_nonneg
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F 1) :
    0 ≤ meromorphicOrderAt
      (fun z => logDeriv riemannZeta z * F z - (-F 1) / (z - 1)) 1 := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDeriv_mul_sub_one hF
  have hcong :
      (fun z => logDeriv riemannZeta z * F z - (-F 1) / (z - 1))
        =ᶠ[𝓝[≠] 1] H := by
    filter_upwards [heq] with z hz
    rw [hz, add_comm, add_sub_cancel_right]
  rw [meromorphicOrderAt_congr hcong]
  exact hH.meromorphicOrderAt_nonneg

/-- Analytic filling of the punched product at a non-polar zero. -/
lemma exists_analyticAt_update_logDeriv_mul_sub {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1)
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F s) :
    ∃ c : ℂ, AnalyticAt ℂ
      (update (fun z => logDeriv riemannZeta z * F z
        - (riemannZetaMultiplicity s : ℂ) * F s / (z - s)) s c) s := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDeriv_mul_sub hz hs hF
  have hf : MeromorphicAt
      (fun z => logDeriv riemannZeta z * F z
        - (riemannZetaMultiplicity s : ℂ) * F s / (z - s)) s :=
    hH.meromorphicAt.congr (by
      filter_upwards [heq] with z hz
      rw [hz, add_comm, add_sub_cancel_right])
  exact exists_analyticAt_update_of_meromorphicOrderAt_nonneg hf
    (meromorphicOrderAt_logDeriv_mul_sub_nonneg hz hs hF)

/-- Product rule: a non-vanishing analytic factor does not change
the meromorphic order of `ζ'/ζ`. -/
lemma meromorphicOrderAt_logDeriv_mul_of_ne_zero {s : ℂ}
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F s) (hFne : F s ≠ 0) :
    meromorphicOrderAt (fun z => logDeriv riemannZeta z * F z) s =
      meromorphicOrderAt (logDeriv riemannZeta) s := by
  have hmul :=
    meromorphicOrderAt_mul_of_ne_zero (f := logDeriv riemannZeta) hF hFne
  refine (meromorphicOrderAt_congr ?_).trans hmul
  filter_upwards with z
  exact mul_comm _ _

/-- If the analytic factor vanishes, `(ζ'/ζ)·F` has nonnegative order
at a non-polar zero (the pole is cancelled). -/
lemma meromorphicOrderAt_logDeriv_mul_of_eq_zero {s : ℂ}
    (hz : riemannZeta s = 0) (hs : s ≠ 1)
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F s) (hF0 : F s = 0) :
    0 ≤ meromorphicOrderAt (fun z => logDeriv riemannZeta z * F z) s := by
  simpa [hF0, div_zero] using
    meromorphicOrderAt_logDeriv_mul_sub_nonneg hz hs hF

/-- Analytic filling of the punched product at `s = 1`. -/
lemma exists_analyticAt_update_logDeriv_mul_sub_one
    {F : ℂ → ℂ} (hF : AnalyticAt ℂ F 1) :
    ∃ c : ℂ, AnalyticAt ℂ
      (update (fun z => logDeriv riemannZeta z * F z - (-F 1) / (z - 1)) 1 c) 1 := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDeriv_mul_sub_one hF
  have hf : MeromorphicAt
      (fun z => logDeriv riemannZeta z * F z - (-F 1) / (z - 1)) 1 :=
    hH.meromorphicAt.congr (by
      filter_upwards [heq] with z hz
      rw [hz, add_comm, add_sub_cancel_right])
  exact exists_analyticAt_update_of_meromorphicOrderAt_nonneg hf
    (meromorphicOrderAt_logDeriv_mul_sub_one_nonneg hF)

/-- Punched integrand on a closed strip rectangle. -/
noncomputable def logDerivHatRemainder (F : ℂ → ℂ) (σ₁ σ₂ T : ℝ) : ℂ → ℂ :=
  fun z => logDeriv riemannZeta z * F z
    - ∑ ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T,
        (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ)
    - (-F 1) / (z - 1)

lemma analyticAt_inv_sub {s p : ℂ} (hp : p ≠ s) :
    AnalyticAt ℂ (fun z => (z - p)⁻¹) s :=
  ((analyticAt_id.sub analyticAt_const).inv (sub_ne_zero.mpr hp.symm))

lemma analyticAt_sum_inv_sub (s : Finset ℂ) (r : ℂ → ℂ) {x : ℂ}
    (hx : ∀ p ∈ s, p ≠ x) :
    AnalyticAt ℂ (fun z => ∑ p ∈ s, r p / (z - p)) x := by
  classical
  revert hx
  refine s.induction_on ?empty ?insert
  · intro _hx
    simp; exact analyticAt_const
  · intro p s hps ih hx
    have hp : p ≠ x := hx p (Finset.mem_insert_self p s)
    have hs : ∀ q ∈ s, q ≠ x :=
      fun q hq => hx q (Finset.mem_insert_of_mem hq)
    simp_rw [Finset.sum_insert hps]
    exact ((analyticAt_const.mul (analyticAt_inv_sub hp)).add (ih hs))

lemma exists_analytic_logDerivHatRemainder_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    ∃ H : ℂ → ℂ, AnalyticAt ℂ H s ∧
      logDerivHatRemainder F σ₁ σ₂ T =ᶠ[𝓝[≠] s] H := by
  have hs' := mem_riemannZetaZerosOnClosedRect.mp hs
  obtain ⟨H0, hH0, heq⟩ :=
    exists_analytic_logDeriv_mul_sub hs'.2.1 hs'.2.2 (hF s (mem_univ s))
  let zeros := riemannZetaZerosOnClosedRect σ₁ σ₂ T
  have hrest : AnalyticAt ℂ
      (fun z =>
        ∑ ρ ∈ zeros.erase s,
            (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ)
          + (-F 1) / (z - 1)) s :=
    (analyticAt_sum_inv_sub (zeros.erase s)
        (fun ρ => (riemannZetaMultiplicity ρ : ℂ) * F ρ)
        (fun ρ hρ => Finset.ne_of_mem_erase hρ)).add
      (analyticAt_const.mul (analyticAt_inv_sub hs'.2.2.symm))
  refine ⟨fun z => H0 z -
      (∑ ρ ∈ zeros.erase s,
          (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ)
        + (-F 1) / (z - 1)), hH0.sub hrest, ?_⟩
  filter_upwards [heq] with z hz
  unfold logDerivHatRemainder
  have hsum := Finset.sum_erase_add (s := zeros) (f := fun ρ : ℂ =>
      (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ)) hs
  rw [← hsum, hz]
  ring

lemma meromorphicOrderAt_logDerivHatRemainder_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    0 ≤ meromorphicOrderAt (logDerivHatRemainder F σ₁ σ₂ T) s := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDerivHatRemainder_at_zero hF hs
  rw [meromorphicOrderAt_congr heq]
  exact hH.meromorphicOrderAt_nonneg

lemma exists_analytic_logDerivHatRemainder_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    (σ₁ σ₂ T : ℝ) :
    ∃ H : ℂ → ℂ, AnalyticAt ℂ H 1 ∧
      logDerivHatRemainder F σ₁ σ₂ T =ᶠ[𝓝[≠] 1] H := by
  obtain ⟨H0, hH0, heq⟩ :=
    exists_analytic_logDeriv_mul_sub_one (hF 1 (mem_univ 1))
  let zeros := riemannZetaZerosOnClosedRect σ₁ σ₂ T
  have hrest : AnalyticAt ℂ
      (fun z => ∑ ρ ∈ zeros,
          (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ)) 1 :=
    analyticAt_sum_inv_sub zeros
      (fun ρ => (riemannZetaMultiplicity ρ : ℂ) * F ρ)
      (fun ρ hρ => (mem_riemannZetaZerosOnClosedRect.mp hρ).2.2)
  refine ⟨fun z => H0 z -
      ∑ ρ ∈ zeros, (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ),
      hH0.sub hrest, ?_⟩
  filter_upwards [heq] with z hz
  unfold logDerivHatRemainder
  rw [hz]
  ring

lemma meromorphicOrderAt_logDerivHatRemainder_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    (σ₁ σ₂ T : ℝ) :
    0 ≤ meromorphicOrderAt (logDerivHatRemainder F σ₁ σ₂ T) 1 := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDerivHatRemainder_at_one hF σ₁ σ₂ T
  rw [meromorphicOrderAt_congr heq]
  exact hH.meromorphicOrderAt_nonneg

lemma exists_analyticAt_update_logDerivHatRemainder_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    ∃ c : ℂ, AnalyticAt ℂ
      (update (logDerivHatRemainder F σ₁ σ₂ T) s c) s := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDerivHatRemainder_at_zero hF hs
  exact exists_analyticAt_update_of_meromorphicOrderAt_nonneg
    (hH.meromorphicAt.congr (by
      filter_upwards [heq] with z hz
      exact hz.symm))
    (meromorphicOrderAt_logDerivHatRemainder_at_zero hF hs)

lemma exists_analyticAt_update_logDerivHatRemainder_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F Set.univ)
    (σ₁ σ₂ T : ℝ) :
    ∃ c : ℂ, AnalyticAt ℂ
      (update (logDerivHatRemainder F σ₁ σ₂ T) 1 c) 1 := by
  obtain ⟨H, hH, heq⟩ := exists_analytic_logDerivHatRemainder_at_one hF σ₁ σ₂ T
  exact exists_analyticAt_update_of_meromorphicOrderAt_nonneg
    (hH.meromorphicAt.congr (by
      filter_upwards [heq] with z hz
      exact hz.symm))
    (meromorphicOrderAt_logDerivHatRemainder_at_one hF σ₁ σ₂ T)

end ContourRemainder

/-! ### r517: `ĥ` entire, filled remainder, fixed-T residue identity -/

section ContourIdentity

open Complex Filter Function Set MeasureTheory
open scoped Topology Interval

lemma hasDerivAt_hat_integrand (g : ℝ → ℝ) (t : ℝ) (s : ℂ) :
    HasDerivAt (fun z : ℂ => (g t : ℂ) * exp (z * t))
      ((g t : ℂ) * t * exp (s * t)) s := by
  have h := ((hasDerivAt_id' s).mul_const (t : ℂ)).cexp
  convert h.const_mul (g t : ℂ) using 1
  ring

lemma FullWeilTest.hasDerivAt_hat (F : FullWeilTest) (s₀ : ℂ) :
    HasDerivAt F.hat
      (∫ t : ℝ, (F.toFun t : ℂ) * (t : ℂ) * exp (s₀ * t)) s₀ := by
  let r : ℝ := 1
  have hr : (0 : ℝ) < r := by norm_num
  have hs : Metric.ball s₀ r ∈ 𝓝 s₀ := Metric.ball_mem_nhds s₀ hr
  let Fint : ℂ → ℝ → ℂ := fun z t => (F.toFun t : ℂ) * exp (z * t)
  let F' : ℂ → ℝ → ℂ := fun z t => (F.toFun t : ℂ) * (t : ℂ) * exp (z * t)
  have hF_meas : ∀ᶠ z in 𝓝 s₀, AEStronglyMeasurable (Fint z) volume :=
    Filter.Eventually.of_forall fun z =>
      ((continuous_ofReal.comp F.continuous_toFun).mul
        (continuous_exp.comp (continuous_const.mul continuous_ofReal))).aestronglyMeasurable
  have hF_int := F.integrable_hat_integrand s₀
  have hF'_meas : AEStronglyMeasurable (F' s₀) volume := by
    have hc : Continuous fun t : ℝ =>
        (F.toFun t : ℂ) * (t : ℂ) * exp (s₀ * t) :=
      ((continuous_ofReal.comp F.continuous_toFun).mul
        (continuous_ofReal.comp continuous_id)).mul
        (continuous_exp.comp (continuous_const.mul continuous_ofReal))
    exact hc.aestronglyMeasurable
  let bound : ℝ → ℝ := fun t =>
    |F.toFun t| * |t| * Real.exp ((‖s₀‖ + 1) * |t|)
  have hbound_int : Integrable bound := by
    have hc : Continuous bound :=
      ((continuous_abs.comp F.continuous_toFun).mul continuous_abs).mul
        (Real.continuous_exp.comp (continuous_const.mul continuous_abs))
    have hsupp : HasCompactSupport bound :=
      HasCompactSupport.of_support_subset_isCompact isCompact_Icc
        (fun t ht => F.support_subset_Icc (by
          refine mem_support.mpr ?_
          intro hg
          have : bound t = 0 := by simp [bound, hg]
          exact (mem_support.mp ht) this))
    exact hc.integrable_of_hasCompactSupport hsupp
  have h_bound : ∀ᵐ t ∂volume, ∀ z ∈ Metric.ball s₀ r, ‖F' z t‖ ≤ bound t := by
    refine Filter.Eventually.of_forall ?_
    intro t z hz
    have hzball : ‖z - s₀‖ < (1 : ℝ) := by
      simpa [dist_eq_norm, r] using Metric.mem_ball.mp hz
    have hzle : ‖z‖ ≤ ‖s₀‖ + 1 := by
      have htri : ‖z‖ ≤ ‖s₀‖ + ‖z - s₀‖ := by
        calc ‖z‖ = ‖s₀ + (z - s₀)‖ := by simp
          _ ≤ ‖s₀‖ + ‖z - s₀‖ := norm_add_le _ _
      linarith [htri, hzball.le]
    have hre : |z.re| ≤ ‖s₀‖ + 1 :=
      (abs_re_le_norm z).trans hzle
    rw [norm_mul, norm_mul, norm_real, norm_real, norm_exp]
    have hrezt : (z * (t : ℂ)).re = z.re * t := by simp
    rw [hrezt]
    have hexp : Real.exp (z.re * t) ≤ Real.exp ((‖s₀‖ + 1) * |t|) := by
      apply Real.exp_le_exp.mpr
      calc z.re * t ≤ |z.re * t| := le_abs_self _
        _ = |z.re| * |t| := abs_mul _ _
        _ ≤ (‖s₀‖ + 1) * |t| :=
          mul_le_mul_of_nonneg_right hre (abs_nonneg _)
    exact mul_le_mul_of_nonneg_left hexp (mul_nonneg (abs_nonneg _) (abs_nonneg _))
  have h_diff : ∀ᵐ t ∂volume, ∀ z ∈ Metric.ball s₀ r,
      HasDerivAt (fun w : ℂ => Fint w t) (F' z t) z :=
    Filter.Eventually.of_forall fun t z _ => hasDerivAt_hat_integrand F.toFun t z
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le
    hs hF_meas hF_int hF'_meas h_bound hbound_int h_diff).2

lemma FullWeilTest.differentiable_hat (F : FullWeilTest) :
    Differentiable ℂ F.hat :=
  fun s => (F.hasDerivAt_hat s).differentiableAt

lemma FullWeilTest.analyticOnNhd_hat (F : FullWeilTest) :
    AnalyticOnNhd ℂ F.hat univ :=
  analyticOnNhd_univ_iff_differentiable.mpr F.differentiable_hat

lemma FullWeilTest.analyticAt_hat (F : FullWeilTest) (s : ℂ) :
    AnalyticAt ℂ F.hat s :=
  F.analyticOnNhd_hat s (mem_univ s)

/-- Poles of `(ζ′/ζ)·F` on the closed strip rectangle: the r499
zeros together with the simple pole at `1`. -/
noncomputable def contourPoles (σ₁ σ₂ T : ℝ) : Finset ℂ :=
  insert (1 : ℂ) (riemannZetaZerosOnClosedRect σ₁ σ₂ T)

lemma one_not_mem_riemannZetaZerosOnClosedRect (σ₁ σ₂ T : ℝ) :
    (1 : ℂ) ∉ riemannZetaZerosOnClosedRect σ₁ σ₂ T :=
  fun h => (mem_riemannZetaZerosOnClosedRect.mp h).2.2 rfl

lemma mem_contourPoles {σ₁ σ₂ T : ℝ} {z : ℂ} :
    z ∈ contourPoles σ₁ σ₂ T ↔
      z = 1 ∨ z ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T :=
  Finset.mem_insert

lemma analyticAt_logDeriv_riemannZeta {s : ℂ}
    (hs : s ≠ 1) (hz : riemannZeta s ≠ 0) :
    AnalyticAt ℂ (logDeriv riemannZeta) s :=
  (analyticAt_riemannZeta hs).deriv.div (analyticAt_riemannZeta hs) hz

lemma analyticAt_logDerivHatRemainder_of_mem_rect_not_pole
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hQ : s ∈ zetaClosedRect σ₁ σ₂ T)
    (hs1 : s ≠ 1)
    (hsz : s ∉ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    AnalyticAt ℂ (logDerivHatRemainder F σ₁ σ₂ T) s := by
  have hz : riemannZeta s ≠ 0 := fun h =>
    hsz (mem_riemannZetaZerosOnClosedRect.mpr ⟨hQ, h, hs1⟩)
  have hx : ∀ ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T, ρ ≠ s :=
    fun ρ hρ hps => hsz (by simpa [hps] using hρ)
  have hsum := analyticAt_sum_inv_sub
    (riemannZetaZerosOnClosedRect σ₁ σ₂ T)
    (fun ρ => (riemannZetaMultiplicity ρ : ℂ) * F ρ) hx
  unfold logDerivHatRemainder
  exact (((analyticAt_logDeriv_riemannZeta hs1 hz).mul
      (hF s (mem_univ s))).sub hsum).sub
    (analyticAt_const.mul (analyticAt_inv_sub hs1.symm))

noncomputable def logDerivHatRemainderFillAtZero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) : ℂ :=
  Classical.choose
    (exists_analyticAt_update_logDerivHatRemainder_at_zero hF hs)

lemma analyticAt_update_logDerivHatRemainder_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    AnalyticAt ℂ
      (update (logDerivHatRemainder F σ₁ σ₂ T) s
        (logDerivHatRemainderFillAtZero hF hs)) s :=
  Classical.choose_spec
    (exists_analyticAt_update_logDerivHatRemainder_at_zero hF hs)

noncomputable def logDerivHatRemainderFillAtOne
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ) (σ₁ σ₂ T : ℝ) : ℂ :=
  Classical.choose
    (exists_analyticAt_update_logDerivHatRemainder_at_one hF σ₁ σ₂ T)

lemma analyticAt_update_logDerivHatRemainder_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ) (σ₁ σ₂ T : ℝ) :
    AnalyticAt ℂ
      (update (logDerivHatRemainder F σ₁ σ₂ T) 1
        (logDerivHatRemainderFillAtOne hF σ₁ σ₂ T)) 1 :=
  Classical.choose_spec
    (exists_analyticAt_update_logDerivHatRemainder_at_one hF σ₁ σ₂ T)

noncomputable def logDerivHatRemainderFilled
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ) (σ₁ σ₂ T : ℝ) : ℂ → ℂ :=
  fun z =>
    if hz : z ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T then
      logDerivHatRemainderFillAtZero hF hz
    else if z = 1 then
      logDerivHatRemainderFillAtOne hF σ₁ σ₂ T
    else
      logDerivHatRemainder F σ₁ σ₂ T z

lemma logDerivHatRemainderFilled_of_not_mem
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {z : ℂ}
    (hz : z ∉ contourPoles σ₁ σ₂ T) :
    logDerivHatRemainderFilled hF σ₁ σ₂ T z =
      logDerivHatRemainder F σ₁ σ₂ T z := by
  have hz' : z ∉ riemannZetaZerosOnClosedRect σ₁ σ₂ T ∧ z ≠ 1 := by
    rw [mem_contourPoles, not_or] at hz
    exact ⟨hz.2, hz.1⟩
  simp [logDerivHatRemainderFilled, hz'.1, hz'.2]

lemma eventuallyEq_filled_of_not_mem
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∉ contourPoles σ₁ σ₂ T) :
    logDerivHatRemainderFilled hF σ₁ σ₂ T
      =ᶠ[𝓝 s] logDerivHatRemainder F σ₁ σ₂ T := by
  have hnhds : (contourPoles σ₁ σ₂ T : Set ℂ)ᶜ ∈ 𝓝 s :=
    (Finset.isClosed (contourPoles σ₁ σ₂ T)).isOpen_compl.mem_nhds
      (mem_compl hs)
  filter_upwards [hnhds] with z hz
  exact logDerivHatRemainderFilled_of_not_mem hF hz

lemma eventuallyEq_filled_update_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    logDerivHatRemainderFilled hF σ₁ σ₂ T
      =ᶠ[𝓝 s]
        update (logDerivHatRemainder F σ₁ σ₂ T) s
          (logDerivHatRemainderFillAtZero hF hs) := by
  have hnhds :
      ((contourPoles σ₁ σ₂ T).erase s : Set ℂ)ᶜ ∈ 𝓝 s :=
    ((contourPoles σ₁ σ₂ T).erase s).isClosed.isOpen_compl.mem_nhds
      (by simp)
  filter_upwards [hnhds] with z hz
  by_cases hzs : z = s
  · subst hzs
    simp [logDerivHatRemainderFilled, hs, update_self]
  · have hzp : z ∉ contourPoles σ₁ σ₂ T := fun h =>
      hz (Finset.mem_erase.mpr ⟨hzs, h⟩)
    rw [update_of_ne hzs, logDerivHatRemainderFilled_of_not_mem hF hzp]

lemma eventuallyEq_filled_update_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ) (σ₁ σ₂ T : ℝ) :
    logDerivHatRemainderFilled hF σ₁ σ₂ T
      =ᶠ[𝓝 (1 : ℂ)]
        update (logDerivHatRemainder F σ₁ σ₂ T) 1
          (logDerivHatRemainderFillAtOne hF σ₁ σ₂ T) := by
  have h1z : (1 : ℂ) ∉ riemannZetaZerosOnClosedRect σ₁ σ₂ T :=
    one_not_mem_riemannZetaZerosOnClosedRect σ₁ σ₂ T
  have hnhds :
      (riemannZetaZerosOnClosedRect σ₁ σ₂ T : Set ℂ)ᶜ ∈ 𝓝 (1 : ℂ) :=
    (riemannZetaZerosOnClosedRect σ₁ σ₂ T).isClosed.isOpen_compl.mem_nhds
      (mem_compl h1z)
  filter_upwards [hnhds] with z hz
  by_cases hz1 : z = 1
  · subst hz1
    simp [logDerivHatRemainderFilled, h1z, update_self]
  · have hzp : z ∉ contourPoles σ₁ σ₂ T := fun h => by
      rw [mem_contourPoles] at h
      exact h.elim hz1 hz
    rw [update_of_ne hz1, logDerivHatRemainderFilled_of_not_mem hF hzp]

lemma analyticAt_logDerivHatRemainderFilled_at_zero
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hs : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    AnalyticAt ℂ (logDerivHatRemainderFilled hF σ₁ σ₂ T) s :=
  (analyticAt_update_logDerivHatRemainder_at_zero hF hs).congr
    (eventuallyEq_filled_update_at_zero hF hs).symm

lemma analyticAt_logDerivHatRemainderFilled_at_one
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ) (σ₁ σ₂ T : ℝ) :
    AnalyticAt ℂ (logDerivHatRemainderFilled hF σ₁ σ₂ T) 1 :=
  (analyticAt_update_logDerivHatRemainder_at_one hF σ₁ σ₂ T).congr
    (eventuallyEq_filled_update_at_one hF σ₁ σ₂ T).symm

lemma analyticAt_logDerivHatRemainderFilled
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {s : ℂ}
    (hQ : s ∈ zetaClosedRect σ₁ σ₂ T) :
    AnalyticAt ℂ (logDerivHatRemainderFilled hF σ₁ σ₂ T) s := by
  by_cases hsz : s ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T
  · exact analyticAt_logDerivHatRemainderFilled_at_zero hF hsz
  · by_cases hs1 : s = 1
    · subst hs1
      exact analyticAt_logDerivHatRemainderFilled_at_one hF σ₁ σ₂ T
    · have hs : s ∉ contourPoles σ₁ σ₂ T := by
        rw [mem_contourPoles]; exact fun h => h.elim hs1 hsz
      exact (analyticAt_logDerivHatRemainder_of_mem_rect_not_pole
          hF hQ hs1 hsz).congr
        (eventuallyEq_filled_of_not_mem hF hs).symm

lemma differentiableOn_logDerivHatRemainderFilled
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    (σ₁ σ₂ T : ℝ) :
    DifferentiableOn ℂ (logDerivHatRemainderFilled hF σ₁ σ₂ T)
      (zetaClosedRect σ₁ σ₂ T) :=
  fun _s hs =>
    (analyticAt_logDerivHatRemainderFilled hF hs).differentiableWithinAt

lemma logDeriv_mul_eq_sum_add_remainder (F : ℂ → ℂ) (σ₁ σ₂ T : ℝ)
    (z : ℂ) :
    logDeriv riemannZeta z * F z =
      (∑ ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T,
          (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ))
      + (-F 1) / (z - 1)
      + logDerivHatRemainder F σ₁ σ₂ T z := by
  unfold logDerivHatRemainder
  ring

lemma logDeriv_mul_eq_sum_add_filled
    {F : ℂ → ℂ} (hF : AnalyticOnNhd ℂ F univ)
    {σ₁ σ₂ T : ℝ} {z : ℂ}
    (hz : z ∉ contourPoles σ₁ σ₂ T) :
    logDeriv riemannZeta z * F z =
      (∑ ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T,
          (riemannZetaMultiplicity ρ : ℂ) * F ρ / (z - ρ))
      + (-F 1) / (z - 1)
      + logDerivHatRemainderFilled hF σ₁ σ₂ T z := by
  rw [logDeriv_mul_eq_sum_add_remainder,
    logDerivHatRemainderFilled_of_not_mem hF hz]

lemma riemannZeta_ne_zero_of_re_eq_neg_one_div_four {s : ℂ}
    (hs : s.re = -1 / 4) : riemannZeta s ≠ 0 := by
  intro hz
  have hneg : ∀ n : ℕ, s ≠ -n := by
    intro n hn
    have hre : s.re = -(n : ℝ) := by rw [hn]; simp
    have hnval : (n : ℝ) = 1 / 4 := by linarith [hs, hre]
    have h4 : (4 : ℝ) * n = 1 := by linarith [hnval]
    norm_cast at h4
    omega
  have hs1 : s ≠ 1 := by
    intro h
    have : s.re = 1 := by rw [h]; simp
    linarith
  have hz1 : riemannZeta (1 - s) = 0 := by
    rw [riemannZeta_one_sub hneg hs1, hz, mul_zero]
  have hre1 : (1 : ℝ) ≤ (1 - s).re := by
    rw [re_one_sub, hs]; norm_num
  exact riemannZeta_ne_zero_of_one_le_re hre1 hz1

lemma riemannZeta_ne_zero_of_re_eq_two {s : ℂ} (hs : s.re = 2) :
    riemannZeta s ≠ 0 :=
  riemannZeta_ne_zero_of_one_le_re (by simp [hs] : (1 : ℝ) ≤ s.re)

lemma rectangleIntegral_congr_sides (f g : ℂ → ℂ) (z w : ℂ)
    (hbot : EqOn (fun x : ℝ => f ((x : ℂ) + z.im * I))
      (fun x : ℝ => g ((x : ℂ) + z.im * I)) [[z.re, w.re]])
    (htop : EqOn (fun x : ℝ => f ((x : ℂ) + w.im * I))
      (fun x : ℝ => g ((x : ℂ) + w.im * I)) [[z.re, w.re]])
    (hright : EqOn (fun y : ℝ => f ((w.re : ℂ) + y * I))
      (fun y : ℝ => g ((w.re : ℂ) + y * I)) [[z.im, w.im]])
    (hleft : EqOn (fun y : ℝ => f ((z.re : ℂ) + y * I))
      (fun y : ℝ => g ((z.re : ℂ) + y * I)) [[z.im, w.im]]) :
    rectangleIntegral f z w = rectangleIntegral g z w := by
  simp only [rectangleIntegral]
  rw [intervalIntegral.integral_congr hbot,
    intervalIntegral.integral_congr htop,
    intervalIntegral.integral_congr hright,
    intervalIntegral.integral_congr hleft]

lemma contour_sum_r_eq (F : ℂ → ℂ) (σ₁ σ₂ T : ℝ) (ζ : ℂ)
    (h1z : (1 : ℂ) ∉ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    ∑ p ∈ insert (1 : ℂ) (riemannZetaZerosOnClosedRect σ₁ σ₂ T),
        (if p = 1 then -F 1
          else (riemannZetaMultiplicity p : ℂ) * F p) / (ζ - p) =
      (∑ ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T,
          (riemannZetaMultiplicity ρ : ℂ) * F ρ / (ζ - ρ))
      + (-F 1) / (ζ - 1) := by
  set zeros := riemannZetaZerosOnClosedRect σ₁ σ₂ T
  set r : ℂ → ℂ := fun p =>
    if p = 1 then -F 1 else (riemannZetaMultiplicity p : ℂ) * F p
  have hr1 : r 1 = -F 1 := if_pos rfl
  have hrp : ∀ ρ ∈ zeros,
      r ρ = (riemannZetaMultiplicity ρ : ℂ) * F ρ :=
    fun ρ hρ => if_neg (mem_riemannZetaZerosOnClosedRect.mp hρ).2.2
  change ∑ p ∈ insert (1 : ℂ) zeros, r p / (ζ - p) = _
  rw [Finset.sum_insert h1z, hr1, add_comm]
  congr 1
  exact Finset.sum_congr rfl fun ρ hρ => by rw [hrp ρ hρ]

lemma contour_identity_fixed_T (F : FullWeilTest) {T : ℝ}
    (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 4) 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
      (((-1 / 4 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum F.hat (-1 / 4) 2 T - F.hat 1) := by
  set z : ℂ := (((-1 / 4 : ℝ) : ℂ) + (-T : ℝ) * I)
  set w : ℂ := (((2 : ℝ) : ℂ) + (T : ℝ) * I)
  have hzre : z.re = -1 / 4 := by simp [z]
  have hwre : w.re = 2 := by simp [w]
  have hzim : z.im = -T := by simp [z]
  have hwim : w.im = T := by simp [w]
  have hre_le : (-1 / 4 : ℝ) ≤ 2 := by norm_num
  have him_le : -T ≤ T := neg_le_self hT.le
  have hrect :
      [[z.re, w.re]] ×ℂ [[z.im, w.im]] =
        zetaClosedRect (-1 / 4) 2 T := by
    simp [zetaClosedRect, hzre, hwre, hzim, hwim,
      uIcc_of_le hre_le, uIcc_of_le him_le]
  let zeros := riemannZetaZerosOnClosedRect (-1 / 4) 2 T
  let poles := contourPoles (-1 / 4) 2 T
  let H := logDerivHatRemainderFilled F.analyticOnNhd_hat (-1 / 4) 2 T
  let r : ℂ → ℂ := fun p =>
    if p = 1 then -F.hat 1
    else (riemannZetaMultiplicity p : ℂ) * F.hat p
  have h1z : (1 : ℂ) ∉ zeros :=
    one_not_mem_riemannZetaZerosOnClosedRect (-1 / 4) 2 T
  have hH : DifferentiableOn ℂ H ([[z.re, w.re]] ×ℂ [[z.im, w.im]]) := by
    rw [hrect]
    exact differentiableOn_logDerivHatRemainderFilled
      F.analyticOnNhd_hat (-1 / 4) 2 T
  have hp : ∀ p ∈ insert (1 : ℂ) zeros,
      z.re < p.re ∧ p.re < w.re ∧ z.im < p.im ∧ p.im < w.im := by
    intro p hp
    rw [hzre, hwre, hzim, hwim]
    rcases Finset.mem_insert.mp hp with hp1 | hpz
    · subst hp1
      refine ⟨by norm_num, by norm_num, neg_lt_zero.mpr hT, hT⟩
    · have hmem := mem_riemannZetaZerosOnClosedRect.mp hpz
      have hQ := mem_zetaClosedRect.mp hmem.1
      have hre1 : -1 / 4 < p.re := lt_of_le_of_ne hQ.1 fun h =>
        (riemannZeta_ne_zero_of_re_eq_neg_one_div_four h.symm) hmem.2.1
      have hre2 : p.re < 2 := lt_of_le_of_ne hQ.2.1 fun h =>
        (riemannZeta_ne_zero_of_re_eq_two h) hmem.2.1
      have him : |p.im| < T := hord p hpz
      exact ⟨hre1, hre2, (abs_lt.mp him).1, (abs_lt.mp him).2⟩
  have hside : ∀ q : ℂ,
      q.re = -1 / 4 ∨ q.re = 2 ∨ q.im = -T ∨ q.im = T →
        q ∉ poles := by
    intro q hq hqp
    rw [mem_contourPoles] at hqp
    rcases hqp with hq1 | hqz
    · subst hq1
      rcases hq with hre | hre | him | him
      · norm_num at hre
      · norm_num at hre
      · exact (neg_lt_zero.mpr hT).ne him.symm
      · exact hT.ne' him.symm
    · have hmem := mem_riemannZetaZerosOnClosedRect.mp hqz
      rcases hq with hre | hre | him | him
      · exact (riemannZeta_ne_zero_of_re_eq_neg_one_div_four hre) hmem.2.1
      · exact (riemannZeta_ne_zero_of_re_eq_two hre) hmem.2.1
      · have : |q.im| < T := hord q hqz
        rw [him, abs_neg, abs_of_nonneg hT.le] at this
        exact lt_irrefl T this
      · have : |q.im| < T := hord q hqz
        rw [him, abs_of_nonneg hT.le] at this
        exact lt_irrefl T this
  have hfun :
      rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ) z w =
        rectangleIntegral
          (fun ζ => (∑ p ∈ insert (1 : ℂ) zeros, r p / (ζ - p)) + H ζ)
          z w := by
    refine rectangleIntegral_congr_sides _ _ z w ?bot ?top ?right ?left
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + z.im * I).im = -T := by simp [hzim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inl hq)))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat (-1 / 4) 2 T _ h1z]
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + w.im * I).im = T := by simp [hwim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inr hq)))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat (-1 / 4) 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((w.re : ℂ) + y * I).re = 2 := by simp [hwre]
      have hnp := hside _ (Or.inr (Or.inl hq))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat (-1 / 4) 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((z.re : ℂ) + y * I).re = -1 / 4 := by simp [hzre]
      have hnp := hside _ (Or.inl hq)
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat (-1 / 4) 2 T _ h1z]
  have hcauchy :=
    rectangleIntegral_sum_simple_poles H z w (insert (1 : ℂ) zeros) r hH hp
  rw [hfun, hcauchy]
  have hsumr : ∑ p ∈ insert (1 : ℂ) zeros, r p =
      spectralPartialSum F.hat (-1 / 4) 2 T - F.hat 1 := by
    have hr1 : r 1 = -F.hat 1 := if_pos rfl
    have hrp : ∀ ρ ∈ zeros,
        r ρ = (riemannZetaMultiplicity ρ : ℂ) * F.hat ρ :=
      fun ρ hρ => if_neg (mem_riemannZetaZerosOnClosedRect.mp hρ).2.2
    rw [Finset.sum_insert h1z, hr1, spectralPartialSum, sub_eq_add_neg,
      add_comm]
    congr 1
    exact Finset.sum_congr rfl fun ρ hρ => hrp ρ hρ
  rw [hsumr]

end ContourIdentity

/-! ### r518: edge bounds and T→∞ entry ([2d] decay) -/

section ContourEdges

open Complex Filter Function Set MeasureTheory
open scoped Topology Interval ComplexConjugate

/-- Weierstrass factor: on `|τ| ≥ 1` and `|Re s| ≤ M`,
`1 + e^{σδ} ≥ 1 + e^{-Mπ}`. -/
lemma one_add_exp_re_delta_ge_of_abs_re_le {s : ℂ} {M : ℝ}
    (hM : 0 ≤ M) (hσ : |s.re| ≤ M) (hτ : 1 ≤ |s.im|) :
    1 + Real.exp (-M * Real.pi) ≤
      1 + Real.exp (s.re * (Real.pi / |s.im|)) := by
  have hτpos : 0 < |s.im| :=
    lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hτ
  have hδle : Real.pi / |s.im| ≤ Real.pi :=
    div_le_self Real.pi_pos.le hτ
  have hδpos : 0 ≤ Real.pi / |s.im| :=
    div_nonneg Real.pi_pos.le (abs_nonneg _)
  have hre : -M ≤ s.re := (abs_le.mp hσ).1
  have hmul : -M * Real.pi ≤ s.re * (Real.pi / |s.im|) := by
    by_cases hpos : 0 ≤ s.re
    · have : 0 ≤ s.re * (Real.pi / |s.im|) := mul_nonneg hpos hδpos
      linarith [mul_nonneg hM Real.pi_pos.le]
    · have hneg : s.re ≤ 0 := le_of_not_ge hpos
      have h1 : s.re * Real.pi ≤ s.re * (Real.pi / |s.im|) :=
        mul_le_mul_of_nonpos_left hδle hneg
      have h2 : -M * Real.pi ≤ s.re * Real.pi :=
        mul_le_mul_of_nonneg_right hre Real.pi_pos.le
      exact h2.trans h1
  exact add_le_add_right (Real.exp_le_exp.mpr hmul) 1

/-- r506 extended: `‖ĥ s‖ ≤ C/(1+τ²)` on any compact real interval. -/
lemma FullWeilTest.norm_hat_le_inv_sq_of_abs_re_le (F : FullWeilTest)
    (M : ℝ) (hM : 0 ≤ M) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s : ℂ, |s.re| ≤ M →
      ‖F.hat s‖ ≤ C / (1 + s.im ^ 2) := by
  obtain ⟨Cexp, hCexp0, hCexp⟩ := F.norm_hat_le_exp
  obtain ⟨K, hK0, hK⟩ := F.abs_second_diff_le
  set R := F.supportRadius
  have hR : 0 ≤ R := F.supportRadius_nonneg
  set c0 : ℝ := 1 + Real.exp (-M * Real.pi)
  have hc0 : 0 < c0 := by
    dsimp [c0]; positivity
  set C : ℝ :=
    2 * Cexp * Real.exp ((R + 1) * M)
      + (4 * K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2
          * Real.exp (M * (R + 2 * Real.pi))) / c0 ^ 2
  have hC0 : 0 ≤ C := by
    dsimp [C]
    exact add_nonneg (by positivity) (by positivity)
  refine ⟨C, hC0, fun s hs => ?_⟩
  have hdenpos : 0 < 1 + s.im ^ 2 := by nlinarith [sq_nonneg s.im]
  by_cases hτle : |s.im| ≤ 1
  · have hexp :
        Real.exp ((R + 1) * |s.re|) ≤ Real.exp ((R + 1) * M) :=
      Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_left hs (by positivity))
    have hhat : ‖F.hat s‖ ≤ Cexp * Real.exp ((R + 1) * M) :=
      (hCexp s).trans (mul_le_mul_of_nonneg_left hexp hCexp0)
    have hτsq : s.im ^ 2 ≤ 1 := by
      have : |s.im| ^ 2 ≤ (1 : ℝ) ^ 2 :=
        sq_le_sq.mpr (by simpa [abs_one] using hτle)
      rwa [sq_abs, one_pow] at this
    have hden : 1 + s.im ^ 2 ≤ 2 := by linarith
    have hprod : ‖F.hat s‖ * (1 + s.im ^ 2)
        ≤ 2 * Cexp * Real.exp ((R + 1) * M) := by
      have := mul_le_mul hhat hden (by nlinarith [sq_nonneg s.im])
        (by positivity)
      nlinarith
    have hCpart : 2 * Cexp * Real.exp ((R + 1) * M) ≤ C := by
      dsimp [C]
      exact le_add_of_nonneg_right (by positivity)
    exact (le_div_iff₀ hdenpos).mpr (hprod.trans hCpart)
  · have hτgt : 1 < |s.im| := not_le.mp hτle
    have hτne : s.im ≠ 0 := fun h0 => by
      rw [h0, abs_zero] at hτgt
      linarith
    set δ : ℝ := Real.pi / |s.im|
    have hδpos : 0 < δ :=
      div_pos Real.pi_pos (abs_pos.mpr hτne)
    have hδleπ : δ ≤ Real.pi :=
      div_le_self Real.pi_pos.le (le_of_lt hτgt)
    have hWle : R + 2 * |δ| ≤ R + 2 * Real.pi := by
      rw [abs_of_pos hδpos]
      linarith
    have hI := F.norm_hat_mul_weierstrass_le hK0 hK s δ
    have hfac :
        ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ =
          1 + Real.exp (s.re * δ) := by
      simpa [δ] using norm_one_sub_exp_pi hτne
    have hge : c0 ≤ ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ := by
      rw [hfac]
      simpa [δ, c0] using
        one_add_exp_re_delta_ge_of_abs_re_le hM hs (le_of_lt hτgt)
    have hpow : ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ =
        ‖(1 : ℂ) - exp (s * (δ : ℝ))‖ ^ 2 :=
      norm_pow _ 2
    have hge2 : c0 ^ 2 ≤ ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := by
      rw [hpow]
      exact pow_le_pow_left₀ hc0.le hge 2
    have hmul : ‖F.hat s * ((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ =
        ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ :=
      norm_mul _ _
    have hhatW : ‖F.hat s‖ * c0 ^ 2 ≤
        2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
          Real.exp (|s.re| * (R + 2 * |δ|)) := by
      have hleft : ‖F.hat s‖ * c0 ^ 2
          ≤ ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ :=
        mul_le_mul_of_nonneg_left hge2 (norm_nonneg _)
      calc ‖F.hat s‖ * c0 ^ 2
          ≤ ‖F.hat s‖ * ‖((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := hleft
        _ = ‖F.hat s * ((1 : ℂ) - exp (s * (δ : ℝ))) ^ 2‖ := hmul.symm
        _ ≤ _ := hI
    have hhat : ‖F.hat s‖ ≤
        (2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
          Real.exp (|s.re| * (R + 2 * |δ|))) / c0 ^ 2 :=
      (le_div_iff₀ (sq_pos_of_pos hc0)).mpr hhatW
    have hexp : Real.exp (|s.re| * (R + 2 * |δ|))
        ≤ Real.exp (M * (R + 2 * Real.pi)) := by
      apply Real.exp_le_exp.mpr
      have : |s.re| * (R + 2 * |δ|) ≤ M * (R + 2 * Real.pi) :=
        mul_le_mul hs hWle (add_nonneg hR (by positivity)) hM
      exact this
    have hWsq : (R + 2 * |δ|) ^ 2 ≤ (R + 2 * Real.pi) ^ 2 :=
      pow_le_pow_left₀ (add_nonneg hR (by positivity)) hWle 2
    have hδsq : δ ^ 2 = Real.pi ^ 2 / s.im ^ 2 := by
      have hne : |s.im| ≠ 0 := abs_ne_zero.mpr hτne
      rw [div_pow, sq_abs]
    have hcomp : 1 / s.im ^ 2 ≤ 2 / (1 + s.im ^ 2) := by
      have hpos1 : 0 < s.im ^ 2 := sq_pos_of_ne_zero hτne
      have hτsq : 1 ≤ s.im ^ 2 := by
        have h1 : (1 : ℝ) ≤ |s.im| := le_of_lt hτgt
        have : (1 : ℝ) ^ 2 ≤ |s.im| ^ 2 :=
          pow_le_pow_left₀ (by positivity) h1 2
        rwa [one_pow, sq_abs] at this
      rw [div_le_div_iff₀ hpos1 hdenpos]
      nlinarith
    have hδbound : δ ^ 2 ≤ 2 * Real.pi ^ 2 / (1 + s.im ^ 2) := by
      rw [hδsq]
      have : Real.pi ^ 2 / s.im ^ 2 =
          Real.pi ^ 2 * (1 / s.im ^ 2) := by ring
      rw [this]
      have : Real.pi ^ 2 * (1 / s.im ^ 2) ≤
          Real.pi ^ 2 * (2 / (1 + s.im ^ 2)) :=
        mul_le_mul_of_nonneg_left hcomp (sq_nonneg _)
      convert this using 1
      ring
    have hnum : 2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
          Real.exp (|s.re| * (R + 2 * |δ|))
        ≤ 2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * Real.pi) ^ 2 * Real.exp (M * (R + 2 * Real.pi)) := by
      have hnn2K : 0 ≤ 2 * K := by positivity
      have hstep1 : 2 * K * δ ^ 2 * (R + 2 * |δ|) ^ 2 *
            Real.exp (|s.re| * (R + 2 * |δ|))
          ≤ 2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * |δ|) ^ 2 * Real.exp (|s.re| * (R + 2 * |δ|)) := by
        refine mul_le_mul_of_nonneg_right ?_ (Real.exp_nonneg _)
        exact mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hδbound hnn2K) (sq_nonneg _)
      refine hstep1.trans ?_
      have hstep2 : 2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * |δ|) ^ 2 * Real.exp (|s.re| * (R + 2 * |δ|))
          ≤ 2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * Real.pi) ^ 2 * Real.exp (|s.re| * (R + 2 * |δ|)) :=
        mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hWsq (by positivity))
          (Real.exp_nonneg _)
      refine hstep2.trans ?_
      exact mul_le_mul_of_nonneg_left hexp (by positivity)
    have hfin : (2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
          (R + 2 * Real.pi) ^ 2 * Real.exp (M * (R + 2 * Real.pi))) / c0 ^ 2
        ≤ C / (1 + s.im ^ 2) := by
      have hrearr :
          (2 * K * (2 * Real.pi ^ 2 / (1 + s.im ^ 2)) *
            (R + 2 * Real.pi) ^ 2 * Real.exp (M * (R + 2 * Real.pi))) / c0 ^ 2
          = ((4 * K * Real.pi ^ 2 * (R + 2 * Real.pi) ^ 2 *
              Real.exp (M * (R + 2 * Real.pi))) / c0 ^ 2)
            / (1 + s.im ^ 2) := by
        field_simp [hc0.ne']
        ring
      rw [hrearr]
      exact div_le_div_of_nonneg_right (by
        dsimp [C]
        exact le_add_of_nonneg_left (by positivity)) hdenpos.le
    exact hhat.trans ((div_le_div_of_nonneg_right hnum (sq_nonneg c0)).trans hfin)

lemma FullWeilTest.norm_hat_le_inv_sq_on_Icc (F : FullWeilTest)
    (σ₁ σ₂ : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s : ℂ, s.re ∈ Icc σ₁ σ₂ →
      ‖F.hat s‖ ≤ C / (1 + s.im ^ 2) := by
  set M : ℝ := |σ₁| ⊔ |σ₂|
  have hM : 0 ≤ M := le_max_of_le_left (abs_nonneg _)
  obtain ⟨C, hC0, hC⟩ := F.norm_hat_le_inv_sq_of_abs_re_le M hM
  refine ⟨C, hC0, fun s hs => hC s ?_⟩
  have h1 : |s.re| ≤ |σ₁| ⊔ |σ₂| := by
    have : σ₁ ≤ s.re ∧ s.re ≤ σ₂ := mem_Icc.mp hs
    exact abs_le_max_abs_abs this.1 this.2
  simpa [M] using h1

lemma FullWeilTest.norm_hat_le_inv_sq_on_contour (F : FullWeilTest) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s : ℂ,
      s.re ∈ Icc (-1 / 4 : ℝ) 2 →
        ‖F.hat s‖ ≤ C / (1 + s.im ^ 2) :=
  F.norm_hat_le_inv_sq_on_Icc (-1 / 4) 2

section DirichletHalfPlane
open scoped ArithmeticFunction.Moebius LSeries.notation

lemma term_vonMangoldt_real_eq_ofReal_norm {σ : ℝ} (_hσ : 1 < σ)
    (n : ℕ) :
    LSeries.term ↗ArithmeticFunction.vonMangoldt (σ : ℂ) n =
      (‖LSeries.term ↗ArithmeticFunction.vonMangoldt (σ : ℂ) n‖ : ℂ) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have hΛ : 0 ≤ ArithmeticFunction.vonMangoldt n :=
      ArithmeticFunction.vonMangoldt_nonneg
    have hnpos : 0 < (n : ℝ) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero hn)
    have hden : (0 : ℝ) < Real.rpow (n : ℝ) σ :=
      Real.rpow_pos_of_pos hnpos _
    have hpow : ((n : ℝ) : ℂ) ^ (σ : ℂ) = (Real.rpow (n : ℝ) σ : ℂ) := by
      rw [Real.rpow_eq_pow]
      exact (ofReal_cpow hnpos.le σ).symm
    have key :
        (ArithmeticFunction.vonMangoldt n : ℂ) / (n : ℂ) ^ (σ : ℂ) =
          (‖(ArithmeticFunction.vonMangoldt n : ℂ) /
            (n : ℂ) ^ (σ : ℂ)‖ : ℂ) := by
      rw [← ofReal_natCast, hpow, ← ofReal_div]
      rw [Complex.norm_real, Real.norm_eq_abs,
        abs_of_nonneg (div_nonneg hΛ hden.le)]
    simpa [LSeries.term_of_ne_zero hn] using key

lemma tsum_norm_term_vonMangoldt_real {σ : ℝ} (hσ : 1 < σ) :
    (∑' n, ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (σ : ℂ) n‖) =
      ‖L ↗ArithmeticFunction.vonMangoldt (σ : ℂ)‖ := by
  have hs : 1 < (σ : ℂ).re := by simpa
  have hsum := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
  have hn : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (σ : ℂ) n‖ := by
    rw [summable_norm_iff]; exact hsum
  have heq := term_vonMangoldt_real_eq_ofReal_norm hσ
  rw [LSeries, tsum_congr heq, ← ofReal_tsum,
    Complex.norm_of_nonneg (tsum_nonneg fun _ => norm_nonneg _)]

lemma norm_logDeriv_riemannZeta_le_of_re_ge {s : ℂ} {σ : ℝ}
    (hσ : 1 < σ) (hs : σ ≤ s.re) :
    ‖logDeriv riemannZeta s‖ ≤ ‖logDeriv riemannZeta (σ : ℂ)‖ := by
  have hs1 : 1 < s.re := lt_of_lt_of_le hσ hs
  have hσc : 1 < (σ : ℂ).re := by simpa
  rw [logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt hs1,
    logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt hσc,
    norm_neg, norm_neg]
  have hΛs : LSeriesSummable ↗ArithmeticFunction.vonMangoldt s :=
    ArithmeticFunction.LSeriesSummable_vonMangoldt hs1
  have hΛσ : LSeriesSummable ↗ArithmeticFunction.vonMangoldt (σ : ℂ) :=
    ArithmeticFunction.LSeriesSummable_vonMangoldt hσc
  have hns : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt s n‖ := by
    rw [summable_norm_iff]; exact hΛs
  have hnσ : Summable fun n =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (σ : ℂ) n‖ := by
    rw [summable_norm_iff]; exact hΛσ
  have hre : (σ : ℂ).re ≤ s.re := by simpa using hs
  refine (norm_tsum_le_tsum_norm hns).trans ?_
  refine (hns.tsum_le_tsum
    (fun n => LSeries.norm_term_le_of_re_le_re
      (↗ArithmeticFunction.vonMangoldt) hre n) hnσ).trans ?_
  exact (tsum_norm_term_vonMangoldt_real hσ).le

lemma norm_logDeriv_riemannZeta_le_at_five_four {s : ℂ}
    (hs : (5 / 4 : ℝ) ≤ s.re) :
    ‖logDeriv riemannZeta s‖ ≤
      ‖logDeriv riemannZeta ((5 / 4 : ℝ) : ℂ)‖ :=
  norm_logDeriv_riemannZeta_le_of_re_ge (by norm_num : (1 : ℝ) < 5 / 4) hs

end DirichletHalfPlane

lemma riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero {s : ℂ}
    (hlo : -1 / 4 < s.re) (hhi : s.re < 0) :
    riemannZeta s ≠ 0 := by
  intro hz
  have hneg : ∀ n : ℕ, s ≠ -n := by
    intro n hn
    have hre : s.re = -(n : ℝ) := by rw [hn]; simp
    rcases n.eq_zero_or_pos with rfl | hnpos
    · have : s.re = 0 := by simpa using hre
      linarith
    · have : (1 : ℝ) ≤ n := Nat.one_le_cast.mpr hnpos
      linarith
  have hs1 : s ≠ 1 := by
    intro h
    have : s.re = 1 := by rw [h]; simp
    linarith
  have hz1 : riemannZeta (1 - s) = 0 := by
    rw [riemannZeta_one_sub hneg hs1, hz, mul_zero]
  have hre1 : (1 : ℝ) ≤ (1 - s).re := by
    rw [re_one_sub]
    linarith
  exact riemannZeta_ne_zero_of_one_le_re hre1 hz1

lemma riemannZeta_ne_zero_of_neg_quarter_lt_re_le_zero {s : ℂ}
    (hlo : -1 / 4 < s.re) (hhi : s.re ≤ 0) :
    riemannZeta s ≠ 0 := by
  rcases lt_or_eq_of_le hhi with hlt | heq
  · exact riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero hlo hlt
  · exact riemannZeta_ne_zero_of_re_eq_zero heq

/-- r499 Finset bridge: zeros in `Q_T(σ₁,2)` for `σ₁ ∈ (-1/4, 0)`
are exactly the critical-strip zeros in `[0,1] × [-T,T]`.
The open strip `(-1/4, 0)` and the line `Re = 0` are zero-free,
and `Re ≥ 1` is zero-free except the pole (excluded). -/
lemma riemannZetaZerosOnClosedRect_eq_critical
    {σ₁ T : ℝ} (hlo : -1 / 4 < σ₁) (hhi : σ₁ < 0) :
    riemannZetaZerosOnClosedRect σ₁ 2 T =
      riemannZetaZerosOnClosedRect 0 1 T := by
  ext z
  constructor
  · intro hz
    have hmem := mem_riemannZetaZerosOnClosedRect.mp hz
    have hQ := mem_zetaClosedRect.mp hmem.1
    have hre0 : 0 ≤ z.re := by
      have hnot : ¬ z.re ≤ 0 := fun hle =>
        (riemannZeta_ne_zero_of_neg_quarter_lt_re_le_zero
          (lt_of_lt_of_le hlo hQ.1) hle) hmem.2.1
      exact le_of_not_ge hnot
    have hre1 : z.re ≤ 1 := by
      have hnot : ¬ (1 : ℝ) ≤ z.re := fun hge =>
        riemannZeta_ne_zero_of_one_le_re hge hmem.2.1
      exact le_of_lt (lt_of_not_ge hnot)
    exact mem_riemannZetaZerosOnClosedRect.mpr
      ⟨mem_zetaClosedRect.mpr ⟨hre0, hre1, hQ.2.2.1, hQ.2.2.2⟩,
        hmem.2.1, hmem.2.2⟩
  · intro hz
    have hmem := mem_riemannZetaZerosOnClosedRect.mp hz
    have hQ := mem_zetaClosedRect.mp hmem.1
    have hσ : σ₁ ≤ z.re := (le_of_lt hhi).trans hQ.1
    have h2 : z.re ≤ 2 := hQ.2.1.trans (by norm_num : (1 : ℝ) ≤ 2)
    exact mem_riemannZetaZerosOnClosedRect.mpr
      ⟨mem_zetaClosedRect.mpr ⟨hσ, h2, hQ.2.2.1, hQ.2.2.2⟩,
        hmem.2.1, hmem.2.2⟩

lemma riemannZetaZerosOnClosedRect_eq_of_neg_quarter
    {σ₁ σ₁' T : ℝ}
    (hlo : -1 / 4 < σ₁) (hhi : σ₁ < 0)
    (hlo' : -1 / 4 < σ₁') (hhi' : σ₁' < 0) :
    riemannZetaZerosOnClosedRect σ₁ 2 T =
      riemannZetaZerosOnClosedRect σ₁' 2 T := by
  rw [riemannZetaZerosOnClosedRect_eq_critical hlo hhi,
    riemannZetaZerosOnClosedRect_eq_critical hlo' hhi']

lemma spectralPartialSum_eq_critical
    (F : ℂ → ℂ) {σ₁ T : ℝ} (hlo : -1 / 4 < σ₁) (hhi : σ₁ < 0) :
    spectralPartialSum F σ₁ 2 T = spectralPartialSum F 0 1 T := by
  simp [spectralPartialSum,
    riemannZetaZerosOnClosedRect_eq_critical hlo hhi]

lemma hord_iff_critical {σ₁ T : ℝ}
    (hlo : -1 / 4 < σ₁) (hhi : σ₁ < 0) :
    (∀ ρ ∈ riemannZetaZerosOnClosedRect σ₁ 2 T, |ρ.im| < T) ↔
      (∀ ρ ∈ riemannZetaZerosOnClosedRect 0 1 T, |ρ.im| < T) := by
  constructor <;> intro h ρ hρ
  · exact h ρ (by simpa [riemannZetaZerosOnClosedRect_eq_critical hlo hhi]
      using hρ)
  · exact h ρ (by simpa [riemannZetaZerosOnClosedRect_eq_critical hlo hhi]
      using hρ)

/-- Parametric r517 identity on every left edge `σ₁ ∈ (-1/4, 0)`.
The r517 argument is symmetric: left-edge cleanliness is the r518
zero-free strip, which holds for every such `σ₁`.  The r499 Finset
is the critical-strip Finset (`riemannZetaZerosOnClosedRect_eq_critical`). -/
lemma contour_identity_fixed_T_of (F : FullWeilTest) {σ₁ T : ℝ}
    (hσlo : -1 / 4 < σ₁) (hσhi : σ₁ < 0) (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect σ₁ 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
      ((σ₁ : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum F.hat σ₁ 2 T - F.hat 1) := by
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
  let H := logDerivHatRemainderFilled F.analyticOnNhd_hat σ₁ 2 T
  let r : ℂ → ℂ := fun p =>
    if p = 1 then -F.hat 1
    else (riemannZetaMultiplicity p : ℂ) * F.hat p
  have h1z : (1 : ℂ) ∉ zeros :=
    one_not_mem_riemannZetaZerosOnClosedRect σ₁ 2 T
  have hH : DifferentiableOn ℂ H ([[z.re, w.re]] ×ℂ [[z.im, w.im]]) := by
    rw [hrect]
    exact differentiableOn_logDerivHatRemainderFilled
      F.analyticOnNhd_hat σ₁ 2 T
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
      rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ) z w =
        rectangleIntegral
          (fun ζ => (∑ p ∈ insert (1 : ℂ) zeros, r p / (ζ - p)) + H ζ)
          z w := by
    refine rectangleIntegral_congr_sides _ _ z w ?bot ?top ?right ?left
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + z.im * I).im = -T := by simp [hzim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inl hq)))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat σ₁ 2 T _ h1z]
    · intro x _hx
      dsimp
      have hq : ((x : ℂ) + w.im * I).im = T := by simp [hwim]
      have hnp := hside _ (Or.inr (Or.inr (Or.inr hq)))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat σ₁ 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((w.re : ℂ) + y * I).re = 2 := by simp [hwre]
      have hnp := hside _ (Or.inr (Or.inl hq))
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat σ₁ 2 T _ h1z]
    · intro y _hy
      dsimp
      have hq : ((z.re : ℂ) + y * I).re = σ₁ := by simp [hzre]
      have hnp := hside _ (Or.inl hq)
      rw [logDeriv_mul_eq_sum_add_filled F.analyticOnNhd_hat hnp,
        contour_sum_r_eq F.hat σ₁ 2 T _ h1z]
  have hcauchy :=
    rectangleIntegral_sum_simple_poles H z w (insert (1 : ℂ) zeros) r hH hp
  rw [hfun, hcauchy]
  have hsumr : ∑ p ∈ insert (1 : ℂ) zeros, r p =
      spectralPartialSum F.hat σ₁ 2 T - F.hat 1 := by
    have hr1 : r 1 = -F.hat 1 := if_pos rfl
    have hrp : ∀ ρ ∈ zeros,
        r ρ = (riemannZetaMultiplicity ρ : ℂ) * F.hat ρ :=
      fun ρ hρ => if_neg (mem_riemannZetaZerosOnClosedRect.mp hρ).2.2
    rw [Finset.sum_insert h1z, hr1, spectralPartialSum, sub_eq_add_neg,
      add_comm]
    congr 1
    exact Finset.sum_congr rfl fun ρ hρ => hrp ρ hρ
  rw [hsumr]

lemma contour_identity_fixed_T_neg_one_div_sixteen
    (F : FullWeilTest) {T : ℝ} (hT : 0 < T)
    (hord : ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 T,
      |ρ.im| < T) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum F.hat (-1 / 16) 2 T - F.hat 1) :=
  contour_identity_fixed_T_of F (by norm_num) (by norm_num) hT hord

set_option maxHeartbeats 800000 in
lemma exists_point_far_from_finset (s : Finset ℝ) {a b : ℝ}
    (hab : a ≤ b) (_hs : ∀ x ∈ s, a ≤ x ∧ x ≤ b) :
    ∃ t, a ≤ t ∧ t ≤ b ∧
      ∀ x ∈ s, (b - a) / (2 * (s.card + 1 : ℝ)) ≤ |t - x| := by
  classical
  rcases eq_or_lt_of_le hab with heq | hlt
  · refine ⟨a, le_rfl, heq ▸ le_rfl, ?_⟩
    intro x hx
    have : (b - a) / (2 * (s.card + 1 : ℝ)) = 0 := by
      simp [heq]
    rw [this]
    exact abs_nonneg _
  set n := s.card
  set δ := (b - a) / (n + 1 : ℝ)
  have hnpos : (0 : ℝ) < n + 1 := by positivity
  have hδpos : 0 < δ := div_pos (sub_pos.mpr hlt) hnpos
  have hδhalf : δ / 2 = (b - a) / (2 * (n + 1 : ℝ)) := by
    unfold δ
    field_simp
  by_contra h
  push Not at h
  have hf : ∀ k : Fin (n + 1),
      ∃ x ∈ s, |a + (k.val + (1 / 2 : ℝ)) * δ - x| < δ / 2 := by
    intro k
    have hk : (k.val : ℝ) ≤ n :=
      Nat.cast_le.mpr (Nat.lt_succ_iff.mp k.isLt)
    have hhalf : (0 : ℝ) ≤ k.val + 1 / 2 := by
      have : (0 : ℝ) ≤ k.val := Nat.cast_nonneg _
      linarith
    have ht1 : a ≤ a + (k.val + 1 / 2) * δ :=
      le_add_of_nonneg_right (mul_nonneg hhalf hδpos.le)
    have hδid : (n + 1 : ℝ) * δ = b - a := by
      unfold δ
      field_simp
    have ht2 : a + (k.val + 1 / 2) * δ ≤ b := by
      have hkle : k.val + (1 / 2 : ℝ) ≤ n + 1 / 2 := by linarith
      have hle :
          a + (k.val + 1 / 2) * δ ≤ a + (n + 1 / 2) * δ :=
        add_le_add_right (mul_le_mul_of_nonneg_right hkle hδpos.le) a
      have hmid : a + (n + 1 / 2) * δ = b - δ / 2 := by
        have : (n + 1 / 2 : ℝ) * δ = (n + 1 : ℝ) * δ - δ / 2 := by ring
        linarith [hδid]
      linarith [hle, hmid, hδpos.le]
    obtain ⟨x, hx, hlt'⟩ := h _ ht1 ht2
    refine ⟨x, hx, ?_⟩
    simpa [hδhalf] using hlt'
  choose f hfmem hdist using hf
  have hinj : Function.Injective f := by
    intro k1 k2 heq
    set t1 := a + (k1.val + (1 / 2 : ℝ)) * δ
    set t2 := a + (k2.val + (1 / 2 : ℝ)) * δ
    have hsum : |t1 - t2| < δ := by
      have hsplit : t1 - t2 = (t1 - f k1) + (f k1 - t2) := by
        abel
      have hre : |t1 - t2| ≤ |t1 - f k1| + |t2 - f k2| := by
        rw [hsplit]
        refine (abs_add_le _ _).trans_eq ?_
        rw [heq, abs_sub_comm (f k2) t2]
      have hlt12 : |t1 - f k1| + |t2 - f k2| < δ := by
        have := add_lt_add (hdist k1) (hdist k2)
        simpa [t1, t2] using this
      exact lt_of_le_of_lt hre hlt12
    have htri :
        |(k1.val + (1 / 2 : ℝ)) * δ - (k2.val + (1 / 2 : ℝ)) * δ| < δ := by
      simpa [t1, t2, add_sub_add_left_eq_sub] using hsum
    have habs : |(k1.val : ℝ) - k2.val| < 1 := by
      have hmul : |(k1.val : ℝ) - k2.val| * δ < δ := by
        convert htri using 1
        rw [← sub_mul, abs_mul, abs_of_pos hδpos]
        ring
      exact (mul_lt_iff_lt_one_left hδpos).mp hmul
    have hval : k1.val = k2.val := by
      have h1 : (k1.val : ℝ) < (k2.val : ℝ) + 1 := by
        linarith [(abs_lt.mp habs).2]
      have h2 : (k2.val : ℝ) < (k1.val : ℝ) + 1 := by
        linarith [(abs_lt.mp habs).1]
      have h1n : k1.val < k2.val + 1 := Nat.cast_lt.mp (by simpa using h1)
      have h2n : k2.val < k1.val + 1 := Nat.cast_lt.mp (by simpa using h2)
      omega
    exact Fin.ext hval
  have hcard : n + 1 ≤ n := by
    have himg : (Finset.univ.image f).card = n + 1 := by
      rw [Finset.card_image_of_injective _ hinj, Finset.card_univ,
        Fintype.card_fin]
    have hsub : Finset.univ.image f ⊆ s := by
      intro x hx
      obtain ⟨k, _, rfl⟩ := Finset.mem_image.mp hx
      exact hfmem k
    have := Finset.card_le_card hsub
    linarith [this, himg]
  exact (Nat.not_succ_le_self n) hcard

lemma exists_point_far_from_finset_any (s : Finset ℝ) {a b : ℝ}
    (hab : a ≤ b) :
    ∃ t, a ≤ t ∧ t ≤ b ∧
      ∀ x ∈ s, (b - a) / (2 * (s.card + 1 : ℝ)) ≤ |t - x| := by
  classical
  let s' := s.image fun x : ℝ => min b (max a x)
  have hs' : ∀ x ∈ s', a ≤ x ∧ x ≤ b := by
    intro x hx
    obtain ⟨y, _, rfl⟩ := Finset.mem_image.mp hx
    exact ⟨le_min hab (le_max_left a y), min_le_left _ _⟩
  obtain ⟨t, ht1, ht2, hfar⟩ := exists_point_far_from_finset s' hab hs'
  refine ⟨t, ht1, ht2, ?_⟩
  intro x hx
  have hclamp : min b (max a x) ∈ s' :=
    Finset.mem_image.mpr ⟨x, hx, rfl⟩
  have hfar' := hfar _ hclamp
  have hcard : (s'.card : ℝ) ≤ s.card :=
    Nat.cast_le.mpr Finset.card_image_le
  have hfrac : (b - a) / (2 * (s.card + 1 : ℝ)) ≤
      (b - a) / (2 * (s'.card + 1 : ℝ)) := by
    have hden : 0 < 2 * (s.card + 1 : ℝ) := by positivity
    have hden' : 0 < 2 * (s'.card + 1 : ℝ) := by positivity
    exact div_le_div_of_nonneg_left (sub_nonneg.mpr hab) hden'
      (by nlinarith [hcard])
  have hproj : |t - min b (max a x)| ≤ |t - x| := by
    rcases le_total x a with hxa | hax
    · have hmin : min b (max a x) = a := by
        rw [max_eq_left hxa, min_eq_right hab]
      rw [hmin]
      have hx_le_t : x ≤ t := hxa.trans ht1
      have habs_ta : |t - a| = t - a := abs_of_nonneg (sub_nonneg.mpr ht1)
      have habs_tx : |t - x| = t - x := abs_of_nonneg (sub_nonneg.mpr hx_le_t)
      rw [habs_ta, habs_tx]
      linarith
    · rcases le_total x b with hxb | hbx
      · have heq : min b (max a x) = x := by
          rw [max_eq_right hax, min_eq_right hxb]
        simp [heq]
      · have hmin : min b (max a x) = b := by
          rw [max_eq_right hax, min_eq_left hbx]
        rw [hmin]
        have ht_le_x : t ≤ x := ht2.trans hbx
        rw [abs_sub_comm t x, abs_of_nonneg (sub_nonneg.mpr ht_le_x),
          abs_sub_comm t b, abs_of_nonneg (sub_nonneg.mpr ht2)]
        linarith
  exact hfrac.trans (hfar'.trans hproj)

lemma mem_unit_height_inner_disk {N : ℝ} {z : ℂ}
    (hre : (1 / 2 : ℝ) ≤ z.re) (hre1 : z.re ≤ 1)
    (him : N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)) :
    z ∈ Metric.closedBall ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) |(13 / 8 : ℝ)| := by
  have him0 : |z.im - (N + (1 / 2 : ℝ))| ≤ (5 / 8 : ℝ) :=
    le_trans (abs_le.mpr ⟨by linarith [him.1], by linarith [him.2]⟩)
      (by norm_num : (1 / 2 : ℝ) ≤ 5 / 8)
  exact mem_closedDisk_of_re_ge_half (T := N + (1 / 2 : ℝ)) hre hre1 him0

lemma card_zeros_re_ge_half_unit (N : ℝ) :
    ((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => (1 / 2 : ℝ) ≤ z.re ∧ N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ))).card
      ≤ (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  refine Finset.card_le_card ?_
  intro z hz
  have hzf := Finset.mem_filter.mp hz
  have hzR := mem_riemannZetaZerosOnClosedRect.mp hzf.1
  have hrect := mem_zetaClosedRect.mp hzR.1
  refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hzR.2.1, hzR.2.2⟩
  exact mem_unit_height_inner_disk hzf.2.1 hrect.2.1 hzf.2.2

lemma card_zeros_re_lt_half_unit (N : ℝ) :
    ((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => z.re < (1 / 2 : ℝ) ∧ N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ))).card
      ≤ (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  set Slt := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => z.re < (1 / 2 : ℝ) ∧ N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  set D := riemannZetaZerosInClosedDisk
    ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)
  have hinj : Function.Injective fun z : ℂ => 1 - z :=
    fun a b h => sub_right_inj.mp h
  have himage : Slt.image (fun z => 1 - z) ⊆ D := by
    intro w hw
    obtain ⟨z, hzlt, rfl⟩ := Finset.mem_image.mp hw
    have hzf := Finset.mem_filter.mp hzlt
    have hzR := mem_riemannZetaZerosOnClosedRect.mp hzf.1
    have hrect := mem_zetaClosedRect.mp hzR.1
    have hre0 : 0 < z.re :=
      lt_of_le_of_ne hrect.1 fun h0 =>
        riemannZeta_ne_zero_of_re_eq_zero h0.symm hzR.2.1
    have hre1 : z.re < 1 := lt_of_lt_of_le hzf.2.1 (by norm_num)
    have hwz := one_sub_mem_closedRect hzf.1 hre0 hre1
    have hwR := mem_riemannZetaZerosOnClosedRect.mp hwz
    have hre_ge : (1 / 2 : ℝ) ≤ (1 - z).re := by
      rw [re_one_sub]; linarith [hzf.2.1]
    have hre_le : (1 - z).re ≤ 1 := by
      rw [re_one_sub]; linarith [hrect.1]
    have him : -(N + 1 : ℝ) ≤ (1 - z).im ∧
        (1 - z).im ≤ (-(N + 1 : ℝ) + 1) := by
      have himz : (1 - z).im = -z.im := by simp [sub_im]
      rw [himz]
      constructor <;> linarith [hzf.2.2.1, hzf.2.2.2]
    refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hwR.2.1, hwR.2.2⟩
    exact mem_unit_height_inner_disk (N := -(N + 1 : ℝ))
      hre_ge hre_le him
  exact (Finset.card_image_of_injective Slt hinj).symm.trans_le
    (Finset.card_le_card himage)

lemma card_window_zeros_unit (N : ℝ) :
    ((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ))).card
      ≤ (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card +
        (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  set S := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  set Sge := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => (1 / 2 : ℝ) ≤ z.re ∧ N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  set Slt := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => z.re < (1 / 2 : ℝ) ∧ N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  have hunion : Sge ∪ Slt = S := by
    ext z
    constructor
    · intro hz
      rcases Finset.mem_union.mp hz with h | h
      · exact Finset.mem_filter.mpr ⟨(Finset.mem_filter.mp h).1,
          (Finset.mem_filter.mp h).2.2⟩
      · exact Finset.mem_filter.mpr ⟨(Finset.mem_filter.mp h).1,
          (Finset.mem_filter.mp h).2.2⟩
    · intro hz
      have hz' := Finset.mem_filter.mp hz
      by_cases hre : (1 / 2 : ℝ) ≤ z.re
      · exact Finset.mem_union.mpr
          (Or.inl (Finset.mem_filter.mpr ⟨hz'.1, hre, hz'.2⟩))
      · exact Finset.mem_union.mpr
          (Or.inr (Finset.mem_filter.mpr ⟨hz'.1, lt_of_not_ge hre, hz'.2⟩))
  have hdisj : Disjoint Sge Slt := by
    refine Finset.disjoint_left.mpr ?_
    intro z hzge hzlt
    have := (Finset.mem_filter.mp hzge).2.1
    have := (Finset.mem_filter.mp hzlt).2.1
    linarith
  have hpart : S.card = Sge.card + Slt.card := by
    rw [← hunion, Finset.card_union_of_disjoint hdisj]
  linarith [hpart, card_zeros_re_ge_half_unit N, card_zeros_re_lt_half_unit N]

noncomputable def ordinateGapConst : ℝ :=
  4 * zetaZerosInDiskCardBoundInner + 2

lemma ordinateGapConst_pos : 0 < ordinateGapConst := by
  have hC := zetaZerosInDiskCardBoundInner_pos
  unfold ordinateGapConst
  positivity

lemma card_window_zeros_unit_le (N : ℝ) (hN : 1 ≤ N) :
    (((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ))).card : ℝ)
      ≤ 2 * zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + N + 1)) := by
  have hnat := card_window_zeros_unit N
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  set τp : ℝ := N + (1 / 2 : ℝ)
  set τm : ℝ := -(N + 1 : ℝ) + (1 / 2 : ℝ)
  have hDp := zetaZerosInDisk_card_le_inner τp
  have hDm := zetaZerosInDisk_card_le_inner τm
  have hτp : 0 ≤ τp := by unfold τp; linarith [hN]
  have hτpeq : |τp| = τp := abs_of_nonneg hτp
  have hτmeq : |τm| = τp := by
    have : τm = -τp := by unfold τp τm; ring
    rw [this, abs_neg, hτpeq]
  have hlogp : 1 + Real.log (2 + |τp|) ≤ 1 + Real.log (2 + N + 1) := by
    have hle : 2 + |τp| ≤ 2 + N + 1 := by
      rw [hτpeq]; unfold τp; linarith
    have hx : 0 < 2 + |τp| := by
      rw [hτpeq]; unfold τp; linarith [hN]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hlogm : 1 + Real.log (2 + |τm|) ≤ 1 + Real.log (2 + N + 1) := by
    have hle : 2 + |τm| ≤ 2 + N + 1 := by
      rw [hτmeq]; unfold τp; linarith
    have hx : 0 < 2 + |τm| := by
      rw [hτmeq]; unfold τp; linarith [hN]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hp :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τp * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    hDp.trans (mul_le_mul_of_nonneg_left hlogp hC0)
  have hm :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τm * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    hDm.trans (mul_le_mul_of_nonneg_left hlogm hC0)
  have hcast :
      (((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
          (fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ))).card : ℝ)
        ≤ ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τp * I) (13 / 8)).card : ℝ) +
          ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τm * I) (13 / 8)).card : ℝ) := by
    have h0 : (N + 1 / 2 : ℝ) = τp := by unfold τp; ring
    have h1 : (-(N + 1 : ℝ) + 1 / 2 : ℝ) = τm := by unfold τm; ring
    have h :=
      (Nat.cast_le (α := ℝ)).mpr hnat
    have hadd :
        (((riemannZetaZerosInClosedDisk
            ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card +
          (riemannZetaZerosInClosedDisk
            ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card : ℕ) : ℝ) =
          ((riemannZetaZerosInClosedDisk
            ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card : ℝ) +
          ((riemannZetaZerosInClosedDisk
            ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card : ℝ) :=
      Nat.cast_add _ _
    simpa [h0, h1, hadd] using h
  have hsum := add_le_add hp hm
  have h2 : zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) +
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) =
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) := by
    ring
  exact hcast.trans (hsum.trans_eq h2)

lemma exists_gap_height (N : ℝ) (hN : 1 ≤ N) :
    ∃ T : ℝ, N ≤ T ∧ T ≤ (N + 1 : ℝ) ∧
      ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ),
        N ≤ z.im → z.im ≤ (N + 1 : ℝ) →
          1 / (ordinateGapConst * (1 + Real.log (2 + N + 1))) ≤ |z.im - T| := by
  set W := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  set s := W.image Complex.im
  have hs : ∀ x ∈ s, N ≤ x ∧ x ≤ (N + 1 : ℝ) := by
    intro x hx
    obtain ⟨z, hz, rfl⟩ := Finset.mem_image.mp hx
    exact (Finset.mem_filter.mp hz).2
  obtain ⟨T, hTlo, hThi, hfar⟩ :=
    exists_point_far_from_finset s
      (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1)) hs
  refine ⟨T, hTlo, hThi, ?_⟩
  intro z hz himlo himhi
  have hzW : z ∈ W := Finset.mem_filter.mpr ⟨hz, himlo, himhi⟩
  have hims : z.im ∈ s := Finset.mem_image.mpr ⟨z, hzW, rfl⟩
  have hdist := hfar z.im hims
  have hL : (1 : ℝ) ≤ 1 + Real.log (2 + N + 1) :=
    le_add_of_nonneg_right (Real.log_nonneg (by linarith [hN] : (1 : ℝ) ≤ 2 + N + 1))
  have hsc : (s.card : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    (Nat.cast_le.mpr Finset.card_image_le).trans (card_window_zeros_unit_le N hN)
  have hC := le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hstep : (s.card : ℝ) + 1 ≤
      (2 * zetaZerosInDiskCardBoundInner + 1) * (1 + Real.log (2 + N + 1)) := by
    nlinarith [hsc, hC, hL]
  have hconst : ordinateGapConst =
      2 * (2 * zetaZerosInDiskCardBoundInner + 1) := by
    unfold ordinateGapConst; ring
  have hden : 2 * (s.card + 1 : ℝ) ≤
      ordinateGapConst * (1 + Real.log (2 + N + 1)) := by
    rw [hconst, mul_assoc]
    exact mul_le_mul_of_nonneg_left hstep (by norm_num : (0 : ℝ) ≤ 2)
  have hB : 0 < 2 * (s.card + 1 : ℝ) := by positivity
  have hA : 0 < ordinateGapConst * (1 + Real.log (2 + N + 1)) :=
    mul_pos ordinateGapConst_pos (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hL)
  have hinv :
      1 / (ordinateGapConst * (1 + Real.log (2 + N + 1))) ≤
        1 / (2 * (s.card + 1 : ℝ)) :=
    (one_div_le_one_div hA hB).mpr hden
  have hlen : ((N + 1 : ℝ) - N) / (2 * (s.card + 1 : ℝ)) =
      1 / (2 * (s.card + 1 : ℝ)) := by ring
  have hdist' : 1 / (2 * (s.card + 1 : ℝ)) ≤ |z.im - T| := by
    simpa [hlen, abs_sub_comm T z.im] using hdist
  exact le_trans hinv hdist'

lemma exists_gap_sequence :
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 1 : ℕ) : ℝ) ≤ T k ∧
        T k ≤ ((2 * k + 1 : ℕ) : ℝ) + 1) ∧
      (∀ k : ℕ, ∀ z ∈ riemannZetaZerosOnClosedRect 0 1
          (((2 * k + 1 : ℕ) : ℝ) + 1),
        ((2 * k + 1 : ℕ) : ℝ) ≤ z.im →
          z.im ≤ ((2 * k + 1 : ℕ) : ℝ) + 1 →
            1 / (ordinateGapConst *
              (1 + Real.log (2 + ((2 * k + 1 : ℕ) : ℝ) + 1))) ≤
              |z.im - T k|) := by
  have hN : ∀ k : ℕ, (1 : ℝ) ≤ (2 * k + 1 : ℕ) := by
    intro k
    exact_mod_cast (Nat.le_add_left 1 (2 * k) : 1 ≤ 2 * k + 1)
  choose T hT using fun k : ℕ =>
    exists_gap_height ((2 * k + 1 : ℕ) : ℝ) (hN k)
  exact ⟨T, fun k => ⟨(hT k).1, (hT k).2.1⟩,
    fun k z hz hlo hhi => (hT k).2.2 z hz hlo hhi⟩

/-- Two-sided unit window: pigeonhole against `|Im ρ| ∈ [N, N+1]`.
A gap `| |ρ.im| - T | ≥ δ` is `|ρ.im - T| ≥ δ` on the positive
side and `|ρ.im + T| ≥ δ` on the negative side, so the FE fold
`Im ↦ -Im` stays on a gap edge. -/
noncomputable def ordinateGapConstAbs : ℝ :=
  2 * ordinateGapConst

lemma ordinateGapConstAbs_pos : 0 < ordinateGapConstAbs :=
  mul_pos (by norm_num : (0 : ℝ) < 2) ordinateGapConst_pos

lemma card_window_zeros_neg_unit (N : ℝ) :
    ((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ -N)).card
      ≤ (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + ((-(N + 1 : ℝ) + (1 / 2 : ℝ)) : ℝ) * I) (13 / 8)).card +
        (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  set R := riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)
  set S := R.filter fun z => -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ -N
  set Sge := R.filter fun z =>
    (1 / 2 : ℝ) ≤ z.re ∧ -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ -N
  set Slt := R.filter fun z =>
    z.re < (1 / 2 : ℝ) ∧ -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ -N
  have hunion : Sge ∪ Slt = S := by
    ext z
    constructor
    · intro hz
      rcases Finset.mem_union.mp hz with h | h
      · exact Finset.mem_filter.mpr ⟨(Finset.mem_filter.mp h).1,
          (Finset.mem_filter.mp h).2.2⟩
      · exact Finset.mem_filter.mpr ⟨(Finset.mem_filter.mp h).1,
          (Finset.mem_filter.mp h).2.2⟩
    · intro hz
      have hz' := Finset.mem_filter.mp hz
      by_cases hre : (1 / 2 : ℝ) ≤ z.re
      · exact Finset.mem_union.mpr
          (Or.inl (Finset.mem_filter.mpr ⟨hz'.1, hre, hz'.2⟩))
      · exact Finset.mem_union.mpr
          (Or.inr (Finset.mem_filter.mpr ⟨hz'.1, lt_of_not_ge hre, hz'.2⟩))
  have hdisj : Disjoint Sge Slt := by
    refine Finset.disjoint_left.mpr ?_
    intro z hzge hzlt
    have := (Finset.mem_filter.mp hzge).2.1
    have := (Finset.mem_filter.mp hzlt).2.1
    linarith
  have hpart : S.card = Sge.card + Slt.card := by
    rw [← hunion, Finset.card_union_of_disjoint hdisj]
  have hge : Sge.card ≤
      (riemannZetaZerosInClosedDisk
        ((2 : ℂ) + ((-(N + 1 : ℝ) + (1 / 2 : ℝ)) : ℝ) * I) (13 / 8)).card := by
    refine Finset.card_le_card ?_
    intro z hz
    have hzf := Finset.mem_filter.mp hz
    have hzR := mem_riemannZetaZerosOnClosedRect.mp hzf.1
    have hrect := mem_zetaClosedRect.mp hzR.1
    refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hzR.2.1, hzR.2.2⟩
    have him : -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ (-(N + 1 : ℝ) + 1) :=
      ⟨hzf.2.2.1, by linarith [hzf.2.2.2]⟩
    exact mem_unit_height_inner_disk (N := -(N + 1 : ℝ))
      hzf.2.1 hrect.2.1 him
  have hlt : Slt.card ≤
      (riemannZetaZerosInClosedDisk
        ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card := by
    have hinj : Function.Injective fun z : ℂ => 1 - z :=
      fun a b h => sub_right_inj.mp h
    have himage : Slt.image (fun z => 1 - z) ⊆
        riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8) := by
      intro w hw
      obtain ⟨z, hzlt, rfl⟩ := Finset.mem_image.mp hw
      have hzf := Finset.mem_filter.mp hzlt
      have hzR := mem_riemannZetaZerosOnClosedRect.mp hzf.1
      have hrect := mem_zetaClosedRect.mp hzR.1
      have hre0 : 0 < z.re :=
        lt_of_le_of_ne hrect.1 fun h0 =>
          riemannZeta_ne_zero_of_re_eq_zero h0.symm hzR.2.1
      have hre1 : z.re < 1 := lt_of_lt_of_le hzf.2.1 (by norm_num)
      have hwz := one_sub_mem_closedRect hzf.1 hre0 hre1
      have hwR := mem_riemannZetaZerosOnClosedRect.mp hwz
      have hre_ge : (1 / 2 : ℝ) ≤ (1 - z).re := by
        rw [re_one_sub]; linarith [hzf.2.1]
      have hre_le : (1 - z).re ≤ 1 := by
        rw [re_one_sub]; linarith [hrect.1]
      have him : N ≤ (1 - z).im ∧ (1 - z).im ≤ (N + 1 : ℝ) := by
        have himz : (1 - z).im = -z.im := by simp [sub_im]
        rw [himz]
        constructor <;> linarith [hzf.2.2.1, hzf.2.2.2]
      refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hwR.2.1, hwR.2.2⟩
      exact mem_unit_height_inner_disk hre_ge hre_le him
    exact (Finset.card_image_of_injective Slt hinj).symm.trans_le
      (Finset.card_le_card himage)
  linarith [hpart, hge, hlt]

lemma card_window_zeros_abs_le (N : ℝ) (hN : 1 ≤ N) :
    (((riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
        (fun z => N ≤ |z.im| ∧ |z.im| ≤ (N + 1 : ℝ))).card : ℝ)
      ≤ 4 * zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + N + 1)) := by
  set R := riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)
  set W := R.filter fun z => N ≤ |z.im| ∧ |z.im| ≤ (N + 1 : ℝ)
  set Wp := R.filter fun z => N ≤ z.im ∧ z.im ≤ (N + 1 : ℝ)
  set Wm := R.filter fun z => -(N + 1 : ℝ) ≤ z.im ∧ z.im ≤ -N
  have hsub : W ⊆ Wp ∪ Wm := by
    intro z hz
    have hzf := Finset.mem_filter.mp hz
    rcases le_total 0 z.im with hpos | hneg
    · have habs : |z.im| = z.im := abs_of_nonneg hpos
      exact Finset.mem_union.mpr (Or.inl
        (Finset.mem_filter.mpr ⟨hzf.1, by simpa [habs] using hzf.2⟩))
    · have habs : |z.im| = -z.im := abs_of_nonpos hneg
      refine Finset.mem_union.mpr (Or.inr
        (Finset.mem_filter.mpr ⟨hzf.1, ?_, ?_⟩))
      · linarith [hzf.2.1, habs]
      · linarith [hzf.2.2, habs]
  have hcard : (W.card : ℝ) ≤ (Wp.card : ℝ) + (Wm.card : ℝ) := by
    have h1 : W.card ≤ (Wp ∪ Wm).card := Finset.card_le_card hsub
    have h2 : (Wp ∪ Wm).card ≤ Wp.card + Wm.card :=
      Finset.card_union_le Wp Wm
    exact (Nat.cast_le.mpr (h1.trans h2)).trans_eq (Nat.cast_add _ _)
  have hp := card_window_zeros_unit_le N hN
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hnat := card_window_zeros_neg_unit N
  set τp : ℝ := N + (1 / 2 : ℝ)
  set τm : ℝ := -(N + 1 : ℝ) + (1 / 2 : ℝ)
  have hτp0 : 0 ≤ τp := by unfold τp; linarith [hN]
  have hτpabs : |τp| = τp := abs_of_nonneg hτp0
  have hτmabs : |τm| = τp := by
    have : τm = -τp := by unfold τp τm; ring
    rw [this, abs_neg, hτpabs]
  have hlogp : 1 + Real.log (2 + |τp|) ≤ 1 + Real.log (2 + N + 1) := by
    have hle : 2 + |τp| ≤ 2 + N + 1 := by
      rw [hτpabs]; unfold τp; linarith
    have hx : 0 < 2 + |τp| := by
      rw [hτpabs]; unfold τp; linarith [hN]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hlogm : 1 + Real.log (2 + |τm|) ≤ 1 + Real.log (2 + N + 1) := by
    have hle : 2 + |τm| ≤ 2 + N + 1 := by
      rw [hτmabs]; unfold τp; linarith
    have hx : 0 < 2 + |τm| := by
      rw [hτmabs]; unfold τp; linarith [hN]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hDp := zetaZerosInDisk_card_le_inner τp
  have hDm := zetaZerosInDisk_card_le_inner τm
  have hpD :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τp * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    hDp.trans (mul_le_mul_of_nonneg_left hlogp hC0)
  have hmD :
      ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τm * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    hDm.trans (mul_le_mul_of_nonneg_left hlogm hC0)
  have hm : (Wm.card : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) := by
    set τm' : ℝ := (-(N + 1 : ℝ) + (1 / 2 : ℝ) : ℝ)
    set τp' : ℝ := (N + 1 / 2 : ℝ)
    have hcast : (Wm.card : ℝ) ≤
        ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τm' * I) (13 / 8)).card : ℝ) +
          ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τp' * I) (13 / 8)).card : ℝ) :=
      (Nat.cast_le.mpr hnat).trans_eq (Nat.cast_add _ _)
    have hDm' := zetaZerosInDisk_card_le_inner τm'
    have hDp' := zetaZerosInDisk_card_le_inner τp'
    have hlogm' : 1 + Real.log (2 + |τm'|) ≤ 1 + Real.log (2 + N + 1) := by
      have : τm' = τm := by unfold τm' τm; rfl
      simpa [this] using hlogm
    have hlogp' : 1 + Real.log (2 + |τp'|) ≤ 1 + Real.log (2 + N + 1) := by
      have : τp' = τp := by unfold τp' τp; rfl
      simpa [this] using hlogp
    have hm1 :
        ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τm' * I) (13 / 8)).card : ℝ) ≤
          zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
      hDm'.trans (mul_le_mul_of_nonneg_left hlogm' hC0)
    have hp1 :
        ((riemannZetaZerosInClosedDisk ((2 : ℂ) + τp' * I) (13 / 8)).card : ℝ) ≤
          zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
      hDp'.trans (mul_le_mul_of_nonneg_left hlogp' hC0)
    exact hcast.trans ((add_le_add hm1 hp1).trans_eq (by ring))
  have hsum := add_le_add hp hm
  have h4 :
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) +
        2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) =
        4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) := by
    ring
  exact hcard.trans (hsum.trans_eq h4)

lemma exists_gap_height_abs (N : ℝ) (hN : 1 ≤ N) :
    ∃ T : ℝ, N ≤ T ∧ T ≤ (N + 1 : ℝ) ∧
      ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ),
        N ≤ |z.im| → |z.im| ≤ (N + 1 : ℝ) →
          1 / (ordinateGapConstAbs * (1 + Real.log (2 + N + 1))) ≤
            |(|z.im| - T)| := by
  set W := (riemannZetaZerosOnClosedRect 0 1 (N + 1 : ℝ)).filter
    fun z => N ≤ |z.im| ∧ |z.im| ≤ (N + 1 : ℝ)
  set s := W.image fun z : ℂ => |z.im|
  have hs : ∀ x ∈ s, N ≤ x ∧ x ≤ (N + 1 : ℝ) := by
    intro x hx
    obtain ⟨z, hz, rfl⟩ := Finset.mem_image.mp hx
    exact (Finset.mem_filter.mp hz).2
  obtain ⟨T, hTlo, hThi, hfar⟩ :=
    exists_point_far_from_finset s
      (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1)) hs
  refine ⟨T, hTlo, hThi, ?_⟩
  intro z hz himlo himhi
  have hzW : z ∈ W := Finset.mem_filter.mpr ⟨hz, himlo, himhi⟩
  have hims : |z.im| ∈ s := Finset.mem_image.mpr ⟨z, hzW, rfl⟩
  have hdist := hfar |z.im| hims
  have hL : (1 : ℝ) ≤ 1 + Real.log (2 + N + 1) :=
    le_add_of_nonneg_right (Real.log_nonneg
      (by linarith [hN] : (1 : ℝ) ≤ 2 + N + 1))
  have hsc : (s.card : ℝ) ≤
      4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 1)) :=
    (Nat.cast_le.mpr Finset.card_image_le).trans (card_window_zeros_abs_le N hN)
  have hC := le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hstep : (s.card : ℝ) + 1 ≤
      (4 * zetaZerosInDiskCardBoundInner + 1) * (1 + Real.log (2 + N + 1)) := by
    nlinarith [hsc, hC, hL]
  have hconst : ordinateGapConstAbs =
      2 * (4 * zetaZerosInDiskCardBoundInner + 2) := by
    unfold ordinateGapConstAbs ordinateGapConst; ring
  have hstep' : (s.card : ℝ) + 1 ≤
      (4 * zetaZerosInDiskCardBoundInner + 2) *
        (1 + Real.log (2 + N + 1)) := by
    nlinarith [hstep, hC, hL]
  have hden : 2 * (s.card + 1 : ℝ) ≤
      ordinateGapConstAbs * (1 + Real.log (2 + N + 1)) := by
    rw [hconst, mul_assoc]
    exact mul_le_mul_of_nonneg_left hstep' (by norm_num : (0 : ℝ) ≤ 2)
  have hB : 0 < 2 * (s.card + 1 : ℝ) := by positivity
  have hA : 0 < ordinateGapConstAbs * (1 + Real.log (2 + N + 1)) :=
    mul_pos ordinateGapConstAbs_pos
      (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hL)
  have hinv :
      1 / (ordinateGapConstAbs * (1 + Real.log (2 + N + 1))) ≤
        1 / (2 * (s.card + 1 : ℝ)) :=
    (one_div_le_one_div hA hB).mpr hden
  have hlen : ((N + 1 : ℝ) - N) / (2 * (s.card + 1 : ℝ)) =
      1 / (2 * (s.card + 1 : ℝ)) := by ring
  have hdist' : 1 / (2 * (s.card + 1 : ℝ)) ≤ |(|z.im| - T)| := by
    simpa [hlen, abs_sub_comm T |z.im|] using hdist
  exact le_trans hinv hdist'

lemma exists_gap_sequence_abs :
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 1 : ℕ) : ℝ) ≤ T k ∧
        T k ≤ ((2 * k + 1 : ℕ) : ℝ) + 1) ∧
      (∀ k : ℕ, ∀ z ∈ riemannZetaZerosOnClosedRect 0 1
          (((2 * k + 1 : ℕ) : ℝ) + 1),
        ((2 * k + 1 : ℕ) : ℝ) ≤ |z.im| →
          |z.im| ≤ ((2 * k + 1 : ℕ) : ℝ) + 1 →
            1 / (ordinateGapConstAbs *
              (1 + Real.log (2 + ((2 * k + 1 : ℕ) : ℝ) + 1))) ≤
              |(|z.im| - T k)|) := by
  have hN : ∀ k : ℕ, (1 : ℝ) ≤ (2 * k + 1 : ℕ) := by
    intro k
    exact_mod_cast (Nat.le_add_left 1 (2 * k) : 1 ≤ 2 * k + 1)
  choose T hT using fun k : ℕ =>
    exists_gap_height_abs ((2 * k + 1 : ℕ) : ℝ) (hN k)
  exact ⟨T, fun k => ⟨(hT k).1, (hT k).2.1⟩,
    fun k z hz hlo hhi => (hT k).2.2 z hz hlo hhi⟩


/-- Landau inner disk `D(2+iT, 13/8)` sees ordinates in
`[T-13/8, T+13/8]`.  For `T ∈ [N, N+1]` this sits in `[N-2, N+3]`.
Five unit `|Im|` windows, same two r511 disks each; the extra
factor `6` absorbs `1+log(N+5) ≤ 3(1+log T)` for `T ≥ N ≥ 3`. -/
noncomputable def ordinateGapConstLandau : ℝ :=
  6 * (20 * zetaZerosInDiskCardBoundInner + 2)

lemma ordinateGapConstLandau_pos : 0 < ordinateGapConstLandau := by
  have hC := zetaZerosInDiskCardBoundInner_pos
  unfold ordinateGapConstLandau
  positivity

lemma ordinateGapConstLandau_one_le : (1 : ℝ) ≤ ordinateGapConstLandau := by
  unfold ordinateGapConstLandau
  have hC := zetaZerosInDiskCardBoundInner_pos
  nlinarith

lemma log_three_lt_two : Real.log 3 < 2 := by
  have hlt : Real.log 3 < Real.log 4 :=
    Real.log_lt_log (by norm_num : (0 : ℝ) < 3) (by norm_num)
  have h4 : Real.log (4 : ℝ) = 2 * Real.log 2 := by
    have : (4 : ℝ) = 2 ^ 2 := by norm_num
    rw [this, Real.log_pow]
    norm_num
  have h2 : Real.log 2 < 1 :=
    lt_trans Real.log_two_lt_d9 (by norm_num)
  linarith [hlt, h4, h2]

lemma card_window_zeros_abs_filter_large_le (N M : ℝ)
    (hM : 1 ≤ M) (hMN : M + 1 ≤ N + 3) :
    (((riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ)).filter
        (fun z => M ≤ |z.im| ∧ |z.im| ≤ M + 1)).card : ℝ)
      ≤ 4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + M + 1)) := by
  set RL := riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ)
  set RS := riemannZetaZerosOnClosedRect 0 1 (M + 1 : ℝ)
  set WL := RL.filter fun z => M ≤ |z.im| ∧ |z.im| ≤ M + 1
  set WS := RS.filter fun z => M ≤ |z.im| ∧ |z.im| ≤ M + 1
  have hsub : WL ⊆ WS := by
    intro z hz
    have hzf := Finset.mem_filter.mp hz
    have hmem := mem_riemannZetaZerosOnClosedRect.mp hzf.1
    have hQ := mem_zetaClosedRect.mp hmem.1
    have him : (-(M + 1 : ℝ)) ≤ z.im ∧ z.im ≤ (M + 1 : ℝ) :=
      abs_le.mp hzf.2.2
    have hrect : z ∈ RS :=
      mem_riemannZetaZerosOnClosedRect.mpr
        ⟨mem_zetaClosedRect.mpr ⟨hQ.1, hQ.2.1, him.1, him.2⟩,
          hmem.2.1, hmem.2.2⟩
    exact Finset.mem_filter.mpr ⟨hrect, hzf.2.1, hzf.2.2⟩
  exact (Nat.cast_le.mpr (Finset.card_le_card hsub)).trans
    (card_window_zeros_abs_le M hM)

lemma card_window_zeros_abs_wide_le (N : ℝ) (hN : 3 ≤ N) :
    (((riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ)).filter
        (fun z => N - 2 ≤ |z.im| ∧ |z.im| ≤ N + 3)).card : ℝ)
      ≤ 20 * zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + N + 3)) := by
  set R := riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ)
  set W := R.filter fun z => N - 2 ≤ |z.im| ∧ |z.im| ≤ N + 3
  set W0 := R.filter fun z => N - 2 ≤ |z.im| ∧ |z.im| ≤ (N - 2) + 1
  set W1 := R.filter fun z => N - 1 ≤ |z.im| ∧ |z.im| ≤ (N - 1) + 1
  set W2 := R.filter fun z => N ≤ |z.im| ∧ |z.im| ≤ N + 1
  set W3 := R.filter fun z => N + 1 ≤ |z.im| ∧ |z.im| ≤ (N + 1) + 1
  set W4 := R.filter fun z => N + 2 ≤ |z.im| ∧ |z.im| ≤ (N + 2) + 1
  have hsub : W ⊆ W0 ∪ W1 ∪ W2 ∪ W3 ∪ W4 := by
    intro z hz
    have hzf := Finset.mem_filter.mp hz
    have hlo := hzf.2.1
    have hhi := hzf.2.2
    have hzR := hzf.1
    by_cases h0 : |z.im| ≤ (N - 2) + 1
    · exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
        (Or.inl (Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
          (Or.inl (Finset.mem_filter.mpr ⟨hzR, hlo, h0⟩))))))))
    · by_cases h1 : |z.im| ≤ (N - 1) + 1
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
          (Or.inl (Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
            (Or.inr (Finset.mem_filter.mpr
              ⟨hzR, by linarith [h0], h1⟩))))))))
      · by_cases h2 : |z.im| ≤ N + 1
        · exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
            (Or.inl (Finset.mem_union.mpr (Or.inr
              (Finset.mem_filter.mpr ⟨hzR, by linarith [h1], h2⟩))))))
        · by_cases h3 : |z.im| ≤ (N + 1) + 1
          · exact Finset.mem_union.mpr (Or.inl (Finset.mem_union.mpr
              (Or.inr (Finset.mem_filter.mpr
                ⟨hzR, by linarith [h2], h3⟩))))
          · exact Finset.mem_union.mpr (Or.inr
              (Finset.mem_filter.mpr ⟨hzR, by linarith [h3],
                by linarith [hhi]⟩))
  have hunion : (W.card : ℝ) ≤
      (W0.card : ℝ) + (W1.card : ℝ) + (W2.card : ℝ) +
        (W3.card : ℝ) + (W4.card : ℝ) := by
    have hnat : W.card ≤
        W0.card + W1.card + W2.card + W3.card + W4.card := by
      linarith [Finset.card_le_card hsub,
        Finset.card_union_le (W0 ∪ W1 ∪ W2 ∪ W3) W4,
        Finset.card_union_le (W0 ∪ W1 ∪ W2) W3,
        Finset.card_union_le (W0 ∪ W1) W2,
        Finset.card_union_le W0 W1]
    exact_mod_cast hnat
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hlogle : ∀ {M : ℝ}, 1 ≤ M → M ≤ N + 2 →
      1 + Real.log (2 + M + 1) ≤ 1 + Real.log (2 + N + 3) := by
    intro M hM1 hM2
    have hx : 0 < 2 + M + 1 := by linarith [hM1]
    have hle : 2 + M + 1 ≤ 2 + N + 3 := by linarith
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have unit : ∀ (a : ℝ) (ha1 : 1 ≤ a) (ha2 : a ≤ N + 2),
      (((R.filter fun z => a ≤ |z.im| ∧ |z.im| ≤ a + 1).card : ℝ)) ≤
        4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) := by
    intro a ha1 ha2
    have hle := card_window_zeros_abs_filter_large_le N a ha1
      (by linarith [ha2])
    exact hle.trans (mul_le_mul_of_nonneg_left (hlogle ha1 ha2)
      (by positivity))
  have b0 := unit (N - 2) (by linarith [hN]) (by linarith)
  have b1 := unit (N - 1) (by linarith [hN]) (by linarith)
  have b2 := unit N (by linarith [hN]) (by linarith)
  have b3 := unit (N + 1) (by linarith [hN]) (by linarith)
  have b4 := unit (N + 2) (by linarith [hN]) (by linarith)
  have h5 : (W0.card : ℝ) + (W1.card : ℝ) + (W2.card : ℝ) +
      (W3.card : ℝ) + (W4.card : ℝ) ≤
      20 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) := by
    have hsum := add_le_add (add_le_add (add_le_add (add_le_add b0 b1) b2) b3) b4
    have heq :
        4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) +
          4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) +
          4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) +
          4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) +
          4 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) =
          20 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) := by
      ring
    exact hsum.trans_eq heq
  exact hunion.trans h5

lemma exists_gap_height_landau (N : ℝ) (hN : 3 ≤ N) :
    ∃ T : ℝ, N ≤ T ∧ T ≤ (N + 1 : ℝ) ∧
      ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ),
        N - 2 ≤ |z.im| → |z.im| ≤ N + 3 →
          1 / (ordinateGapConstLandau * (1 + Real.log T)) ≤
            |(|z.im| - T)| := by
  set W := (riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ)).filter
    fun z => N - 2 ≤ |z.im| ∧ |z.im| ≤ N + 3
  set s := W.image fun z : ℂ => |z.im|
  obtain ⟨T, hTlo, hThi, hfar⟩ :=
    exists_point_far_from_finset_any s
      (le_add_of_nonneg_right (by norm_num : (0 : ℝ) ≤ 1))
  refine ⟨T, hTlo, hThi, ?_⟩
  intro z hz himlo himhi
  have hzW : z ∈ W := Finset.mem_filter.mpr ⟨hz, himlo, himhi⟩
  have hims : |z.im| ∈ s := Finset.mem_image.mpr ⟨z, hzW, rfl⟩
  have hdist := hfar |z.im| hims
  have hTpos : (3 : ℝ) ≤ T := hN.trans hTlo
  have hL : (1 : ℝ) ≤ 1 + Real.log T :=
    le_add_of_nonneg_right (Real.log_nonneg
      (le_trans (by norm_num : (1 : ℝ) ≤ 3) hTpos))
  have hLN : (1 : ℝ) ≤ 1 + Real.log (2 + N + 3) :=
    le_add_of_nonneg_right (Real.log_nonneg (by linarith [hN]))
  have hsc : (s.card : ℝ) ≤
      20 * zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + N + 3)) :=
    (Nat.cast_le.mpr Finset.card_image_le).trans
      (card_window_zeros_abs_wide_le N hN)
  have hC := le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hstep : (s.card : ℝ) + 1 ≤
      (20 * zetaZerosInDiskCardBoundInner + 1) *
        (1 + Real.log (2 + N + 3)) := by
    nlinarith [hsc, hC, hLN]
  have hstep' : (s.card : ℝ) + 1 ≤
      (20 * zetaZerosInDiskCardBoundInner + 2) *
        (1 + Real.log (2 + N + 3)) := by
    nlinarith [hstep, hC, hLN]
  have hdenN : 2 * (s.card + 1 : ℝ) ≤
      2 * ((20 * zetaZerosInDiskCardBoundInner + 2) *
        (1 + Real.log (2 + N + 3))) :=
    mul_le_mul_of_nonneg_left hstep' (by norm_num : (0 : ℝ) ≤ 2)
  have hLN_le : 1 + Real.log (2 + N + 3) ≤ 3 * (1 + Real.log T) := by
    have hx : 0 < 2 + N + 3 := by linarith [hN]
    have hle : 2 + N + 3 ≤ 3 * T := by nlinarith [hTpos, hTlo]
    have hlog := Real.log_le_log hx hle
    have hmul : Real.log (3 * T) = Real.log 3 + Real.log T :=
      Real.log_mul (by norm_num)
        (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 3) hTpos).ne'
    linarith [hlog, hmul, log_three_lt_two]
  have hden : 2 * (s.card + 1 : ℝ) ≤
      ordinateGapConstLandau * (1 + Real.log T) := by
    have : 2 * (20 * zetaZerosInDiskCardBoundInner + 2) *
        (1 + Real.log (2 + N + 3)) ≤
        6 * (20 * zetaZerosInDiskCardBoundInner + 2) *
          (1 + Real.log T) := by
      have hcoef : 0 ≤ 2 * (20 * zetaZerosInDiskCardBoundInner + 2) := by
        positivity
      have := mul_le_mul_of_nonneg_left hLN_le hcoef
      nlinarith [this, hC]
    unfold ordinateGapConstLandau
    have hdenN' : 2 * (s.card + 1 : ℝ) ≤
        2 * (20 * zetaZerosInDiskCardBoundInner + 2) *
          (1 + Real.log (2 + N + 3)) := by
      simpa [mul_assoc] using hdenN
    exact hdenN'.trans this
  have hB : 0 < 2 * (s.card + 1 : ℝ) := by positivity
  have hA : 0 < ordinateGapConstLandau * (1 + Real.log T) :=
    mul_pos ordinateGapConstLandau_pos
      (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hL)
  have hinv :
      1 / (ordinateGapConstLandau * (1 + Real.log T)) ≤
        1 / (2 * (s.card + 1 : ℝ)) :=
    (one_div_le_one_div hA hB).mpr hden
  have hlen : ((N + 1 : ℝ) - N) / (2 * (s.card + 1 : ℝ)) =
      1 / (2 * (s.card + 1 : ℝ)) := by ring
  have hdist' : 1 / (2 * (s.card + 1 : ℝ)) ≤ |(|z.im| - T)| := by
    simpa [hlen, abs_sub_comm T |z.im|] using hdist
  exact le_trans hinv hdist'

lemma riemannZeta_eq_zero_im_eq_zero_of_re_lt_zero {ρ : ℂ}
    (hre : ρ.re < 0) (hz : riemannZeta ρ = 0) :
    ρ.im = 0 := by
  by_contra him
  have hneg : ∀ n : ℕ, ρ ≠ -n := by
    intro n hn
    exact him (by rw [hn]; simp)
  have hs1 : ρ ≠ 1 := by
    intro h
    have : ρ.re = 1 := by rw [h]; simp
    linarith
  have hz1 : riemannZeta (1 - ρ) = 0 := by
    rw [riemannZeta_one_sub hneg hs1, hz, mul_zero]
  have hre1 : (1 : ℝ) ≤ (1 - ρ).re := by
    rw [re_one_sub]; linarith
  exact riemannZeta_ne_zero_of_one_le_re hre1 hz1


lemma landau_abs_gap_of_wide_window {N T A : ℝ}
    (hN : 3 ≤ N) (hTlo : N ≤ T) (hThi : T ≤ N + 1)
    (hA1 : (1 : ℝ) ≤ A)
    (hwin : ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ),
      N - 2 ≤ |z.im| → |z.im| ≤ N + 3 →
        1 / (A * (1 + Real.log T)) ≤ |(|z.im| - T)|) :
    ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |(|ρ.im| - T)| := by
  intro ρ hz hs1
  have hTpos : (3 : ℝ) ≤ T := hN.trans hTlo
  have hL : (1 : ℝ) ≤ 1 + Real.log T :=
    le_add_of_nonneg_right (Real.log_nonneg
      (le_trans (by norm_num : (1 : ℝ) ≤ 3) hTpos))
  have hδ2 : 1 / (A * (1 + Real.log T)) ≤ 2 := by
    have hAL : (1 : ℝ) ≤ A * (1 + Real.log T) := by
      simpa using mul_le_mul hA1 hL (by norm_num : (0 : ℝ) ≤ 1)
        (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA1)
    have : 1 / (A * (1 + Real.log T)) ≤ 1 := by
      simpa [one_div] using inv_le_one_of_one_le₀ hAL
    linarith
  by_cases hhi : N + 3 < |ρ.im|
  · have : 2 ≤ |(|ρ.im| - T)| := by
      have : |ρ.im| - T ≥ (N + 3) - (N + 1) := by linarith [hhi.le, hThi]
      have hpos : 0 ≤ |ρ.im| - T := by linarith [hTpos]
      rw [abs_of_nonneg hpos]; linarith
    exact hδ2.trans this
  · by_cases hlo : |ρ.im| < N - 2
    · have : 2 ≤ |(|ρ.im| - T)| := by
        have : T - |ρ.im| ≥ N - (N - 2) := by linarith [hlo.le, hTlo]
        have hpos : 0 ≤ T - |ρ.im| := by linarith [hTpos]
        rw [abs_sub_comm, abs_of_nonneg hpos]; linarith
      exact hδ2.trans this
    · have himlo : N - 2 ≤ |ρ.im| := le_of_not_gt hlo
      have himhi : |ρ.im| ≤ N + 3 := le_of_not_gt hhi
      have hre1 : ρ.re < 1 := by
        by_contra hge
        exact riemannZeta_ne_zero_of_one_le_re (le_of_not_gt hge) hz
      have hre0 : 0 ≤ ρ.re := by
        by_contra hneg
        have him0 := riemannZeta_eq_zero_im_eq_zero_of_re_lt_zero
          (lt_of_not_ge hneg) hz
        have : |ρ.im| = 0 := by simp [him0]
        linarith [this, himlo, hN]
      have himB : (-(N + 3 : ℝ)) ≤ ρ.im ∧ ρ.im ≤ (N + 3 : ℝ) :=
        abs_le.mp himhi
      have hrect : ρ ∈ riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ) :=
        mem_riemannZetaZerosOnClosedRect.mpr
          ⟨mem_zetaClosedRect.mpr ⟨hre0, le_of_lt hre1, himB.1, himB.2⟩,
            hz, hs1⟩
      exact hwin ρ hrect himlo himhi

lemma landau_gap_of_wide_window {N T A : ℝ}
    (hN : 3 ≤ N) (hTlo : N ≤ T) (hThi : T ≤ N + 1)
    (hA1 : (1 : ℝ) ≤ A)
    (hwin : ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ),
      N - 2 ≤ |z.im| → |z.im| ≤ N + 3 →
        1 / (A * (1 + Real.log T)) ≤ |(|z.im| - T)|) :
    ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T| := by
  intro ρ hz hs1
  have hT0 : (0 : ℝ) ≤ T :=
    le_trans (by norm_num : (0 : ℝ) ≤ 3) (hN.trans hTlo)
  have habs : |(|ρ.im| - T)| ≤ |ρ.im - T| := by
    simpa [abs_of_nonneg hT0] using abs_abs_sub_abs_le_abs_sub ρ.im T
  exact (landau_abs_gap_of_wide_window hN hTlo hThi hA1 hwin ρ hz hs1).trans habs

lemma landau_gap_neg_of_wide_window {N T A : ℝ}
    (hN : 3 ≤ N) (hTlo : N ≤ T) (hThi : T ≤ N + 1)
    (hA1 : (1 : ℝ) ≤ A) (hT0 : 0 ≤ T)
    (hwin : ∀ z ∈ riemannZetaZerosOnClosedRect 0 1 (N + 3 : ℝ),
      N - 2 ≤ |z.im| → |z.im| ≤ N + 3 →
        1 / (A * (1 + Real.log T)) ≤ |(|z.im| - T)|) :
    ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im + T| := by
  intro ρ hz hs1
  have h := landau_abs_gap_of_wide_window hN hTlo hThi hA1 hwin ρ hz hs1
  have hle : |(|ρ.im| - T)| ≤ |ρ.im + T| :=
    calc |(|ρ.im| - T)|
        = |(|ρ.im| - |-(T)|)| := by simp [abs_neg, abs_of_nonneg hT0]
      _ ≤ |ρ.im - (-T)| := abs_abs_sub_abs_le_abs_sub _ _
      _ = |ρ.im + T| := by simp
  exact h.trans hle

lemma exists_gap_sequence_landau :
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
        T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) ∧
      (∀ k : ℕ, ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (ordinateGapConstLandau * (1 + Real.log (T k))) ≤
          |ρ.im - T k|) ∧
      (∀ k : ℕ, ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (ordinateGapConstLandau * (1 + Real.log (T k))) ≤
          |ρ.im + T k|) := by
  have hN : ∀ k : ℕ, (3 : ℝ) ≤ (2 * k + 3 : ℕ) := by
    intro k
    exact_mod_cast (Nat.le_add_left 3 (2 * k) : 3 ≤ 2 * k + 3)
  choose T hT using fun k : ℕ =>
    exists_gap_height_landau ((2 * k + 3 : ℕ) : ℝ) (hN k)
  have hA1 : (1 : ℝ) ≤ ordinateGapConstLandau := by
    unfold ordinateGapConstLandau
    have hC := zetaZerosInDiskCardBoundInner_pos
    nlinarith
  refine ⟨T, fun k => ⟨(hT k).1, (hT k).2.1⟩, ?_, ?_⟩
  · intro k ρ hz hs1
    exact landau_gap_of_wide_window (hN k) (hT k).1 (hT k).2.1 hA1
      (hT k).2.2 ρ hz hs1
  · intro k ρ hz hs1
    have hT0 : (0 : ℝ) ≤ T k :=
      le_trans (by norm_num : (0 : ℝ) ≤ 3) ((hN k).trans (hT k).1)
    exact landau_gap_neg_of_wide_window (hN k) (hT k).1 (hT k).2.1
      hA1 hT0 (hT k).2.2 ρ hz hs1


lemma borelCaratheodory_ball {f : ℂ → ℂ} {c : ℂ} {M R : ℝ} {z : ℂ}
    (hM : 0 < M) (hR : 0 < R)
    (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hRe : ∀ w ∈ Metric.ball c R, (f w).re ≤ M)
    (hz : z ∈ Metric.ball c R) :
    ‖f z‖ ≤
      2 * M * ‖z - c‖ / (R - ‖z - c‖) +
        ‖f c‖ * (R + ‖z - c‖) / (R - ‖z - c‖) := by
  set g : ℂ → ℂ := fun w => f (w + c)
  have hmaps : MapsTo (fun w : ℂ => w + c) (Metric.ball (0 : ℂ) R)
      (Metric.ball c R) := by
    intro w hw
    simp only [Metric.mem_ball, dist_eq_norm, add_sub_cancel_right, sub_zero] at hw ⊢
    exact hw
  have hg : DifferentiableOn ℂ g (Metric.ball (0 : ℂ) R) :=
    hf.comp (differentiableOn_id.add (differentiableOn_const c)) hmaps
  have hRe' : MapsTo g (Metric.ball (0 : ℂ) R) {w : ℂ | w.re ≤ M} := by
    intro w hw
    exact hRe (w + c) (hmaps hw)
  have hz' : z - c ∈ Metric.ball (0 : ℂ) R := by
    simpa [Metric.mem_ball, dist_eq_norm] using hz
  have hbc := Complex.borelCaratheodory hM hg hRe' hR hz'
  have hg0 : g 0 = f c := by simp [g]
  have hgz : g (z - c) = f z := by simp [g, sub_add_cancel]
  simpa [hg0, hgz, dist_eq_norm] using hbc

lemma borelCaratheodory_ball_zero {f : ℂ → ℂ} {c : ℂ} {M R : ℝ} {z : ℂ}
    (hM : 0 < M) (hR : 0 < R)
    (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hRe : ∀ w ∈ Metric.ball c R, (f w).re ≤ M)
    (hf0 : f c = 0) (hz : z ∈ Metric.ball c R) :
    ‖f z‖ ≤ 2 * M * ‖z - c‖ / (R - ‖z - c‖) := by
  have h := borelCaratheodory_ball hM hR hf hRe hz
  simpa [hf0] using h

lemma borelCaratheodory_closedBall_zero {f : ℂ → ℂ} {c : ℂ} {M R r : ℝ}
    {z : ℂ} (hM : 0 < M) (hR : 0 < R) (hr : 0 ≤ r) (hrR : r < R)
    (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hRe : ∀ w ∈ Metric.ball c R, (f w).re ≤ M)
    (hf0 : f c = 0) (hz : z ∈ Metric.closedBall c r) :
    ‖f z‖ ≤ 2 * M * r / (R - r) := by
  have hzR : z ∈ Metric.ball c R :=
    (Metric.closedBall_subset_ball hrR) hz
  have h0 := borelCaratheodory_ball_zero hM hR hf hRe hf0 hzR
  have hnc : ‖z - c‖ ≤ r := by
    simpa [Metric.mem_closedBall, dist_eq_norm] using hz
  have hmono : 2 * M * ‖z - c‖ / (R - ‖z - c‖) ≤ 2 * M * r / (R - r) := by
    have hnum : 0 ≤ 2 * M := by positivity
    have hdenpos : 0 < R - r := sub_pos.mpr hrR
    have hle : ‖z - c‖ / (R - ‖z - c‖) ≤ r / (R - r) := by
      have hzn : 0 ≤ ‖z - c‖ := norm_nonneg _
      have hzr : ‖z - c‖ < R := by
        simpa [Metric.mem_ball, dist_eq_norm] using hzR
      have h1 : 0 < R - ‖z - c‖ := sub_pos.mpr hzr
      rw [div_le_div_iff₀ h1 hdenpos]
      nlinarith [hzn, hr]
    simpa [mul_div_assoc] using (mul_le_mul_of_nonneg_left hle hnum)
  exact h0.trans hmono

lemma differentiableOn_logDeriv_of_ne {f : ℂ → ℂ} {s : Set ℂ}
    (hs : IsOpen s) (hf : DifferentiableOn ℂ f s)
    (hne : ∀ z ∈ s, f z ≠ 0) :
    DifferentiableOn ℂ (logDeriv f) s := by
  intro z hz
  have hdf : DifferentiableAt ℂ f z :=
    hf.differentiableAt (hs.mem_nhds hz)
  have hder : DifferentiableAt ℂ (deriv f) z :=
    (hf.deriv hs z hz).differentiableAt (hs.mem_nhds hz)
  exact (hder.div hdf (hne z hz)).differentiableWithinAt

lemma exists_logDeriv_primitive {f : ℂ → ℂ} {c : ℂ} {R : ℝ}
    (_hR : 0 < R) (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hne : ∀ z ∈ Metric.ball c R, f z ≠ 0) :
    ∃ h : ℂ → ℂ, h c = 0 ∧
      ∀ z ∈ Metric.ball c R, HasDerivAt h (logDeriv f z) z := by
  have hld : DifferentiableOn ℂ (logDeriv f) (Metric.ball c R) :=
    differentiableOn_logDeriv_of_ne Metric.isOpen_ball hf hne
  exact hld.isExactOn_ball.with_val_at c 0

lemma hasDerivAt_exp_div {f h : ℂ → ℂ} {z : ℂ}
    (hh : HasDerivAt h (logDeriv f z) z)
    (hf : DifferentiableAt ℂ f z) (hfz : f z ≠ 0) :
    HasDerivAt (fun w => Complex.exp (h w) / f w) 0 z := by
  have hexp : HasDerivAt (fun w => Complex.exp (h w))
      (Complex.exp (h z) * logDeriv f z) z :=
    hh.cexp
  have hdiv := hexp.div hf.hasDerivAt hfz
  have hval :
      (Complex.exp (h z) * logDeriv f z * f z -
        Complex.exp (h z) * deriv f z) / f z ^ 2 = 0 := by
    rw [logDeriv_apply]
    field_simp [hfz]
    ring
  exact hval ▸ hdiv

lemma re_logDeriv_primitive_eq {f h : ℂ → ℂ} {c : ℂ} {R : ℝ}
    (hR : 0 < R) (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hne : ∀ z ∈ Metric.ball c R, f z ≠ 0)
    (hh0 : h c = 0)
    (hh : ∀ z ∈ Metric.ball c R, HasDerivAt h (logDeriv f z) z)
    {z : ℂ} (hz : z ∈ Metric.ball c R) :
    (h z).re = Real.log ‖f z‖ - Real.log ‖f c‖ := by
  have hc : c ∈ Metric.ball c R := Metric.mem_ball_self hR
  have hF : DifferentiableOn ℂ (fun w => Complex.exp (h w) / f w)
      (Metric.ball c R) := by
    intro w hw
    have hfw : DifferentiableAt ℂ f w :=
      hf.differentiableAt (Metric.isOpen_ball.mem_nhds hw)
    exact (hasDerivAt_exp_div (hh w hw) hfw (hne w hw)).differentiableAt.differentiableWithinAt
  have hder0 : EqOn (deriv (fun w => Complex.exp (h w) / f w)) 0
      (Metric.ball c R) := by
    intro w hw
    have hfw : DifferentiableAt ℂ f w :=
      hf.differentiableAt (Metric.isOpen_ball.mem_nhds hw)
    exact (hasDerivAt_exp_div (hh w hw) hfw (hne w hw)).deriv
  have hconst :=
    Metric.isOpen_ball.is_const_of_deriv_eq_zero Metric.isPreconnected_ball hF hder0 hz hc
  have hval : Complex.exp (h z) / f z = Complex.exp (h c) / f c := hconst
  have hexp0 : Complex.exp (h c) = 1 := by simp [hh0]
  have hratio : Complex.exp (h z) / f z = 1 / f c := by
    simpa [hexp0] using hval
  have hne0 : f c ≠ 0 := hne c hc
  have hnez : f z ≠ 0 := hne z hz
  have heq : Complex.exp (h z) = f z / f c := by
    have hratio' : Complex.exp (h z) / f z = (f c)⁻¹ := by
      simpa using hratio
    rw [div_eq_iff hnez] at hratio'
    have hmul : Complex.exp (h z) * f c = f z := by
      rw [hratio']
      calc
        (f c)⁻¹ * f z * f c = (f c)⁻¹ * f c * f z := by ring
        _ = f z := by rw [inv_mul_cancel₀ hne0, one_mul]
    exact (eq_div_iff_mul_eq hne0).mpr hmul
  have hn : ‖Complex.exp (h z)‖ = ‖f z‖ / ‖f c‖ := by
    rw [heq, norm_div]
  have hfcpos : 0 < ‖f c‖ := norm_pos_iff.mpr hne0
  have hfzpos : 0 < ‖f z‖ := norm_pos_iff.mpr (hne z hz)
  have : Real.exp (h z).re = ‖f z‖ / ‖f c‖ := by
    simpa [Complex.norm_exp] using hn
  have hlog : (h z).re = Real.log (‖f z‖ / ‖f c‖) := by
    apply Real.exp_injective
    rw [Real.exp_log (div_pos hfzpos hfcpos), this]
  rwa [Real.log_div hfzpos.ne' hfcpos.ne'] at hlog

lemma norm_logDeriv_le_of_log_norm_le {f : ℂ → ℂ} {c : ℂ} {M R r : ℝ}
    (hR : 0 < R) (hr : 0 < r) (hrR : r < R)
    (hf : DifferentiableOn ℂ f (Metric.ball c R))
    (hne : ∀ z ∈ Metric.ball c R, f z ≠ 0)
    (hlog : ∀ z ∈ Metric.ball c R, Real.log ‖f z‖ ≤ M)
    {z : ℂ} (hz : z ∈ Metric.closedBall c r) :
    ‖logDeriv f z‖ ≤
      4 * max (M - Real.log ‖f c‖) (1 : ℝ) * (R + r) / (R - r) ^ 2 := by
  obtain ⟨h, hh0, hh⟩ := exists_logDeriv_primitive hR hf hne
  have hzR : z ∈ Metric.ball c R :=
    (Metric.closedBall_subset_ball hrR) hz
  have hc : c ∈ Metric.ball c R := Metric.mem_ball_self hR
  have hdh : DifferentiableOn ℂ h (Metric.ball c R) :=
    fun w hw => (hh w hw).differentiableAt.differentiableWithinAt
  have hRe : ∀ w ∈ Metric.ball c R, (h w).re ≤ max (M - Real.log ‖f c‖) (1 : ℝ) := by
    intro w hw
    have hre := re_logDeriv_primitive_eq hR hf hne hh0 hh hw
    have : (h w).re ≤ M - Real.log ‖f c‖ := by
      rw [hre]
      linarith [hlog w hw]
    exact this.trans (le_max_left _ _)
  set K : ℝ := max (M - Real.log ‖f c‖) (1 : ℝ)
  have hK : 0 < K := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) (le_max_right _ _)
  set δ : ℝ := (R - r) / 2
  have hδpos : 0 < δ := by
    have : 0 < R - r := sub_pos.mpr hrR
    positivity
  have hcl : Metric.closedBall z δ ⊆ Metric.ball c R := by
    intro w hw
    have htri : dist w c ≤ dist w z + dist z c := dist_triangle w z c
    have hwz : dist w z ≤ δ := Metric.mem_closedBall.mp hw
    have hzc : dist z c ≤ r := Metric.mem_closedBall.mp hz
    have hsum : dist w c ≤ δ + r := le_trans htri (add_le_add hwz hzc)
    have hδr : δ + r = (R + r) / 2 := by
      unfold δ
      ring
    have hlt : (R + r) / 2 < R := by
      have : r < R := hrR
      linarith
    exact (hsum.trans_eq hδr).trans_lt hlt
  have hsub : Metric.ball z δ ⊆ Metric.ball c R :=
    (Metric.ball_subset_closedBall).trans hcl
  have hcl' : closure (Metric.ball z δ) ⊆ Metric.ball c R :=
    Metric.closure_ball_subset_closedBall.trans hcl
  have hdc : DiffContOnCl ℂ h (Metric.ball z δ) :=
    ⟨hdh.mono hsub, hdh.continuousOn.mono hcl'⟩
  have hC : ∀ w ∈ Metric.sphere z δ, ‖h w‖ ≤
      2 * K * (R + r) / (R - r) := by
    intro w hw
    have hwR : w ∈ Metric.ball c R := hcl (Metric.sphere_subset_closedBall hw)
    have hbc := borelCaratheodory_ball_zero hK hR hdh hRe hh0 hwR
    have hwc : ‖w - c‖ ≤ r + δ := by
      have h1 : dist w z = δ := Metric.mem_sphere.mp hw
      have h2 : dist z c ≤ r := Metric.mem_closedBall.mp hz
      have : dist w c ≤ δ + r :=
        (dist_triangle w z c).trans (add_le_add (le_of_eq h1) h2)
      simpa [dist_eq_norm, add_comm] using this
    have hwcR : ‖w - c‖ < R := by
      simpa [Metric.mem_ball, dist_eq_norm] using hwR
    have hmono : 2 * K * ‖w - c‖ / (R - ‖w - c‖) ≤ 2 * K * (r + δ) / (R - (r + δ)) := by
      have hnum : 0 ≤ 2 * K := by positivity
      have hden1 : 0 < R - ‖w - c‖ := sub_pos.mpr hwcR
      have hrd : r + δ = (R + r) / 2 := by unfold δ; ring
      have hden2 : 0 < R - (r + δ) := by
        rw [hrd]; linarith
      have hfrac : ‖w - c‖ / (R - ‖w - c‖) ≤ (r + δ) / (R - (r + δ)) := by
        rw [div_le_div_iff₀ hden1 hden2]
        nlinarith [norm_nonneg (w - c), hwc]
      simpa [mul_div_assoc] using mul_le_mul_of_nonneg_left hfrac hnum
    have hsimp : 2 * K * (r + δ) / (R - (r + δ)) = 2 * K * (R + r) / (R - r) := by
      unfold δ
      field_simp
      ring
    exact (hbc.trans hmono).trans_eq hsimp
  have hcauchy :=
    Complex.norm_deriv_le_of_forall_mem_sphere_norm_le hδpos hdc hC
  have hder : deriv h z = logDeriv f z := (hh z hzR).deriv
  have hδeq : δ = (R - r) / 2 := rfl
  have hbound :
      2 * K * (R + r) / (R - r) / δ =
        4 * K * (R + r) / (R - r) ^ 2 := by
    unfold δ
    field_simp
    ring
  rw [hder] at hcauchy
  refine hcauchy.trans ?_
  have : (2 * K * (R + r) / (R - r)) / δ ≤
      4 * K * (R + r) / (R - r) ^ 2 := le_of_eq hbound
  simpa [div_eq_mul_inv] using this


/-- r520 contour revision.  `norm_riemannZetaMulSubOne_le_of_re_gt`
needs `Re > δ > 0`, so a disk `D(2+iT, R)` cannot cover
`σ = -1/4` without the functional equation.  The r517 identity
`contour_identity_fixed_T` is hardcoded at `σ₁ = -1/4` but its
hypotheses (left edge zero-free, pole interior, right edge
Dirichlet) hold for every `σ₁ ∈ (-1/4, 0)` by
`riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero`.  Intended
contour: `[-1/16, 2]`.  This cut prepares the r510-safe
horizontal `[1/2, 2]` (inner radius `3/2` inside the r511
inner disk `13/8`).  The left sliver `[-1/16, 1/2]` remains
the `|F|`-on-`Re ≲ 0` clamp. -/

lemma logDeriv_riemannZeta_eq_logDeriv_mulSubOne_sub
    {s : ℂ} (hs : s ≠ 1) (hz : riemannZeta s ≠ 0) :
    logDeriv riemannZeta s =
      logDeriv riemannZetaMulSubOne s - 1 / (s - 1) := by
  have hne : s - 1 ≠ 0 := sub_ne_zero.mpr hs
  have hF : riemannZetaMulSubOne s = (s - 1) * riemannZeta s :=
    riemannZetaMulSubOne_apply_of_ne hs
  have hFne : riemannZetaMulSubOne s ≠ 0 := by
    rw [hF]; exact mul_ne_zero hne hz
  have hf_eq :
      riemannZeta =ᶠ[𝓝 s]
        fun w => riemannZetaMulSubOne w / (w - 1) := by
    have hopen : ({1}ᶜ : Set ℂ) ∈ 𝓝 s :=
      isOpen_compl_singleton.mem_nhds hs
    filter_upwards [hopen] with w hw
    have hw0 : w - 1 ≠ 0 := sub_ne_zero.mpr hw
    rw [riemannZetaMulSubOne_apply_of_ne hw]
    field_simp [hw0]
  have hlog :
      logDeriv riemannZeta s =
        logDeriv (fun w => riemannZetaMulSubOne w / (w - 1)) s := by
    simp [logDeriv_apply, hf_eq.deriv_eq, hf_eq.eq_of_nhds]
  have hdg : DifferentiableAt ℂ riemannZetaMulSubOne s :=
    (analyticAt_riemannZetaMulSubOne s).differentiableAt
  have hdd : DifferentiableAt ℂ (fun w : ℂ => w - 1) s := by fun_prop
  rw [hlog, logDeriv_div s hFne hne hdg hdd]
  have hlin : logDeriv (fun w : ℂ => w - 1) s = 1 / (s - 1) := by
    simpa using logDeriv_sub_const_pow 1 1 s
  rw [hlin]

lemma re_gt_one_div_eight_of_mem_landau_ball {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.ball ((2 : ℂ) + T * I) (13 / 8)) :
    (1 / 8 : ℝ) < z.re := by
  have hdist : ‖z - ((2 : ℂ) + T * I)‖ < (13 / 8 : ℝ) := by
    simpa [dist_eq_norm] using Metric.mem_ball.mp hz
  have hre : |z.re - 2| < (13 / 8 : ℝ) := by
    have h := abs_re_le_norm (z - ((2 : ℂ) + T * I))
    have hre' : (z - ((2 : ℂ) + T * I)).re = z.re - 2 := by
      simp [sub_re, add_re, mul_re, I_re]
    exact lt_of_le_of_lt (by rwa [hre'] at h) hdist
  have : (3 / 8 : ℝ) < z.re := by
    have := (abs_lt.mp hre).1
    linarith
  linarith

lemma norm_le_four_add_abs_of_mem_landau_ball {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.ball ((2 : ℂ) + T * I) (13 / 8)) :
    ‖z‖ ≤ 4 + |T| := by
  set c := (2 : ℂ) + T * I
  have hdist : ‖z - c‖ < (13 / 8 : ℝ) := by
    simpa [dist_eq_norm, c] using Metric.mem_ball.mp hz
  have hzc : ‖z‖ ≤ ‖c‖ + 13 / 8 := by
    have hzeq : z = c + (z - c) := by rw [add_comm, sub_add_cancel]
    rw [hzeq]
    calc
      ‖c + (z - c)‖ ≤ ‖c‖ + ‖z - c‖ := norm_add_le _ _
      _ ≤ ‖c‖ + 13 / 8 := add_le_add_right hdist.le _
  have hc : ‖c‖ ≤ 2 + |T| := by
    calc
      ‖c‖ ≤ ‖(2 : ℂ)‖ + ‖T * I‖ := norm_add_le _ _
      _ = 2 + |T| := by simp [c, norm_mul, Complex.norm_I]
  nlinarith

lemma norm_riemannZetaMulSubOne_le_on_landau_ball {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.ball ((2 : ℂ) + T * I) (13 / 8)) :
    ‖riemannZetaMulSubOne z‖ ≤
      (4 + |T|) + (4 + |T|) * (5 + |T|) * zetaFractCellMajorant (1 / 8) := by
  have hδ : (0 : ℝ) < 1 / 8 := by norm_num
  have hre := re_gt_one_div_eight_of_mem_landau_ball hz
  have hnorm := norm_le_four_add_abs_of_mem_landau_ball hz
  have hbound := norm_riemannZetaMulSubOne_le_of_re_gt hδ hre
  have hCI : 0 ≤ zetaFractCellMajorant (1 / 8) := zetaFractCellMajorant_nonneg
  have hz1 : ‖z‖ + 1 ≤ (4 + |T|) + 1 := by linarith [hnorm]
  have h51 : (4 + |T|) + 1 = 5 + |T| := by ring
  have hbound' : ‖riemannZetaMulSubOne z‖ ≤
      ‖z‖ + ‖z‖ * (‖z‖ + 1) * zetaFractCellMajorant (1 / 8) := by
    simpa [zetaFractCellMajorant] using hbound
  have hprod : ‖z‖ * (‖z‖ + 1) * zetaFractCellMajorant (1 / 8) ≤
      (4 + |T|) * (5 + |T|) * zetaFractCellMajorant (1 / 8) := by
    rw [← h51]
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul hnorm hz1 (add_nonneg (norm_nonneg z) zero_le_one)
        (add_nonneg (by norm_num : (0 : ℝ) ≤ 4) (abs_nonneg T)))
      hCI
  exact hbound'.trans (add_le_add hnorm hprod)

noncomputable def landauInnerDisk (T : ℝ) : Finset ℂ :=
  riemannZetaZerosInClosedDisk ((2 : ℂ) + T * I) (13 / 8)

noncomputable def landauPoly (T : ℝ) : ℂ → ℂ :=
  fun z => ∏ ρ ∈ landauInnerDisk T,
    (z - ρ) ^ riemannZetaMultiplicity ρ

lemma logDeriv_landauPoly {T : ℝ} {s : ℂ}
    (hs : ∀ ρ ∈ landauInnerDisk T, s ≠ ρ) :
    logDeriv (landauPoly T) s =
      ∑ ρ ∈ landauInnerDisk T,
        (riemannZetaMultiplicity ρ : ℂ) / (s - ρ) := by
  unfold landauPoly
  have hf : ∀ ρ ∈ landauInnerDisk T,
      (s - ρ) ^ riemannZetaMultiplicity ρ ≠ 0 := by
    intro ρ hρ
    exact pow_ne_zero _ (sub_ne_zero.mpr (hs ρ hρ))
  have hd : ∀ ρ ∈ landauInnerDisk T,
      DifferentiableAt ℂ
        (fun z : ℂ => (z - ρ) ^ riemannZetaMultiplicity ρ) s := by
    intro ρ _hρ; fun_prop
  rw [logDeriv_prod hf hd]
  refine Finset.sum_congr rfl ?_
  intro ρ hρ
  simpa using logDeriv_sub_const_pow ρ (riemannZetaMultiplicity ρ) s

lemma one_add_log_two_add_abs_le {T : ℝ} (hT : (2 : ℝ) ≤ T) :
    1 + Real.log (2 + |T|) ≤ 2 * (1 + Real.log T) := by
  have hTpos : 0 < T := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) hT
  have habs : |T| = T := abs_of_nonneg hTpos.le
  have hlogT : 0 ≤ Real.log T :=
    Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
  have h2T : (2 : ℝ) + |T| ≤ 2 * T := by
    rw [habs]; nlinarith [hT]
  have hpos : 0 < 2 + |T| := by positivity
  have hle : Real.log (2 + |T|) ≤ Real.log (2 * T) :=
    Real.log_le_log hpos h2T
  have hmul : Real.log (2 * T) = Real.log 2 + Real.log T :=
    Real.log_mul (by norm_num) hTpos.ne'
  have h2 : Real.log 2 ≤ 1 :=
    le_of_lt (lt_trans Real.log_two_lt_d9 (by norm_num))
  linarith [hle, hmul, h2, hlogT]

lemma sum_divisor_inner_mul_log_le (T : ℝ) :
    (∑ z ∈ landauInnerDisk T,
        (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) z : ℝ)) *
        Real.log (14 / 13 : ℝ) ≤
      ∑ᶠ u, (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) u : ℝ) *
        Real.log ((7 / 4 : ℝ) * ‖((2 : ℂ) + T * I) - u‖⁻¹) := by
  set c := (2 : ℂ) + T * I
  set D := MeromorphicOn.divisor riemannZetaMulSubOne (Metric.closedBall c |7 / 4|)
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hfin : D.support.Finite :=
    D.finiteSupport (isCompact_closedBall c |7 / 4|)
  set s := hfin.toFinset
  set Z := landauInnerDisk T
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hrabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) := abs_of_pos (by norm_num)
  have hZsub : Z ⊆ s := by
    intro z hz
    exact hfin.mem_toFinset.mpr
      (mem_jensen_support_of_mem_disk_radius (by norm_num : (0 : ℝ) < 13 / 8)
        (by norm_num) (by simpa [Z, landauInnerDisk, c] using hz))
  have htermnn : ∀ u ∈ s, 0 ≤ (D u : ℝ) *
      Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := by
    intro u hu
    have huB : u ∈ Metric.closedBall c |7 / 4| :=
      D.supportWithinDomain (hfin.mem_toFinset.mp hu)
    exact mul_nonneg (riemannZetaMulSubOne_divisor_nonneg T u)
      (jensen_log_weight_nonneg T huB)
  have hsupp :
      (fun u => (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹)).support ⊆ s := by
    intro u hu
    have : D u ≠ 0 := by
      intro h00
      simp [h00] at hu
    exact hfin.mem_toFinset.mpr this
  have hleft :
      ∑ z ∈ Z, (D z : ℝ) * Real.log (14 / 13 : ℝ) ≤
        ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
    refine Finset.sum_le_sum ?_
    intro z hz
    have hz' := mem_riemannZetaZerosInClosedDisk.mp
      (by simpa [Z, landauInnerDisk, c] using hz)
    have hzF : riemannZetaMulSubOne z = 0 :=
      riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
    have hzc : z ≠ c := by
      intro h
      exact riemannZetaMulSubOne_center_ne_zero T (by simpa [c, h] using hzF)
    have hpos : 0 < ‖c - z‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hzc.symm)
    have hle : ‖c - z‖ ≤ (13 / 8 : ℝ) := by
      have : dist z c ≤ (13 / 8 : ℝ) := by
        simpa [c, hrabs, Metric.mem_closedBall] using hz'.1
      simpa [dist_eq_norm, norm_sub_rev] using this
    have hlogle : Real.log (14 / 13 : ℝ) ≤
        Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) := by
      apply Real.log_le_log (by positivity)
      rw [← div_eq_mul_inv, div_le_div_iff₀ (by positivity) hpos]
      nlinarith
    have hD : 0 ≤ (D z : ℝ) := riemannZetaMulSubOne_divisor_nonneg T z
    exact mul_le_mul_of_nonneg_left hlogle hD
  have hmid :
      ∑ z ∈ Z, (D z : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - z‖⁻¹) ≤
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    Finset.sum_le_sum_of_subset_of_nonneg hZsub fun u hu _ => htermnn u hu
  have hfinsum :
      ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) =
        ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
    finsum_eq_sum_of_support_subset _ hsupp
  have hfactor :
      ∑ z ∈ Z, (D z : ℝ) * Real.log (14 / 13 : ℝ) =
        (∑ z ∈ Z, (D z : ℝ)) * Real.log (14 / 13 : ℝ) :=
    (Finset.sum_mul _ _ _).symm
  calc
    (∑ z ∈ Z, (D z : ℝ)) * Real.log (14 / 13 : ℝ) =
        ∑ z ∈ Z, (D z : ℝ) * Real.log (14 / 13 : ℝ) := hfactor.symm
    _ ≤ ∑ u ∈ s, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) :=
      hleft.trans hmid
    _ = ∑ᶠ u, (D u : ℝ) * Real.log ((7 / 4 : ℝ) * ‖c - u‖⁻¹) := hfinsum.symm

lemma sum_divisor_inner_le (T : ℝ) :
    (∑ z ∈ landauInnerDisk T,
        (MeromorphicOn.divisor riemannZetaMulSubOne
          (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) z : ℝ)) ≤
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|)) := by
  have hlog : 0 < Real.log (14 / 13 : ℝ) := Real.log_pos (by norm_num)
  have hL : 0 ≤ Real.log (2 + |T|) :=
    Real.log_nonneg (by nlinarith [abs_nonneg T])
  have hchain :
      (∑ z ∈ landauInnerDisk T,
          (MeromorphicOn.divisor riemannZetaMulSubOne
            (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) z : ℝ)) *
          Real.log (14 / 13 : ℝ) ≤
        Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ :=
    (sum_divisor_inner_mul_log_le T).trans
      (riemannZetaMulSubOne_jensen_sum_le T)
  have hnum :
      Real.log (jensenSphereMajorant T) -
          Real.log ‖riemannZetaMulSubOne ((2 : ℂ) + T * I)‖ ≤
        Real.log jensenSphereMajorantCoeff +
          Real.log ‖riemannZeta 2‖ + 2 * Real.log (2 + |T|) := by
    linarith [log_jensenSphereMajorant_le T, log_center_neg_le T]
  have hA :
      0 ≤ Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ := by
    have h1 : 0 ≤ Real.log jensenSphereMajorantCoeff :=
      le_of_lt (Real.log_pos one_lt_jensenSphereMajorantCoeff)
    have h2 : 0 ≤ Real.log ‖riemannZeta 2‖ :=
      le_of_lt (Real.log_pos one_lt_norm_riemannZeta_two)
    linarith
  have hpack :
      Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ +
          2 * Real.log (2 + |T|) ≤
        (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) *
          (1 + Real.log (2 + |T|)) := by
    nlinarith [hL, hA]
  have hle := hchain.trans (hnum.trans hpack)
  unfold zetaZerosInDiskCardBoundInner
  rw [div_mul_eq_mul_div]
  exact (le_div_iff₀ hlog).mpr (by simpa [mul_comm] using hle)

lemma riemannZetaMultiplicity_le_divisor_inner {T : ℝ} {z : ℂ}
    (hz : z ∈ landauInnerDisk T) :
    (riemannZetaMultiplicity z : ℝ) ≤
      (MeromorphicOn.divisor riemannZetaMulSubOne
        (Metric.closedBall ((2 : ℂ) + T * I) |7 / 4|) z : ℝ) := by
  set c := (2 : ℂ) + T * I
  set U := Metric.closedBall c |7 / 4|
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk, c] using hz)
  have hzF : riemannZetaMulSubOne z = 0 :=
    riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
  have hRabs : |(7 / 4 : ℝ)| = (7 / 4 : ℝ) := abs_of_pos (by norm_num)
  have hrabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) := abs_of_pos (by norm_num)
  have hzB : z ∈ U := by
    have : (13 / 8 : ℝ) ≤ (7 / 4 : ℝ) := by norm_num
    have hzball : z ∈ Metric.closedBall c (13 / 8) := by
      simpa [c, hrabs] using hz'.1
    exact Metric.closedBall_subset_closedBall (by simpa [hRabs] using this) hzball
  have hmer := riemannZetaMulSubOne_meromorphicOn_closedBall c (7 / 4)
  have hAn := analyticAt_riemannZetaMulSubOne z
  have hAnZ := analyticAt_riemannZeta hz'.2.2
  have hordF : analyticOrderAt riemannZetaMulSubOne z =
      analyticOrderAt riemannZeta z := by
    have hne : z ≠ 1 := hz'.2.2
    have heq : riemannZetaMulSubOne =ᶠ[𝓝 z]
        fun w => (w - 1) * riemannZeta w :=
      riemannZetaMulSubOne_eq_mul hne
    have hlin : AnalyticAt ℂ (fun w : ℂ => w - 1) z := by fun_prop
    have hlin0 : analyticOrderAt (fun w : ℂ => w - 1) z = 0 :=
      hlin.analyticOrderAt_eq_zero.mpr (sub_ne_zero.mpr hne)
    have hfun :
        (fun w : ℂ => (w - 1) * riemannZeta w) =
          (fun w : ℂ => w - 1) * riemannZeta := rfl
    rw [analyticOrderAt_congr heq, hfun, analyticOrderAt_mul hlin hAnZ,
      hlin0, zero_add]
  have hD : MeromorphicOn.divisor riemannZetaMulSubOne U z =
      (analyticOrderNatAt riemannZetaMulSubOne z : ℤ) := by
    have htop : analyticOrderAt riemannZetaMulSubOne z ≠ ⊤ := by
      rw [hordF]
      exact analyticOrderAt_riemannZeta_ne_top hz'.2.2
    rw [MeromorphicOn.divisor_apply hmer hzB, hAn.meromorphicOrderAt_eq]
    cases hord : analyticOrderAt riemannZetaMulSubOne z
    · exact (htop hord).elim
    · simp [analyticOrderNatAt, hord]
  have hm : riemannZetaMultiplicity z = analyticOrderNatAt riemannZeta z := rfl
  have hEq : analyticOrderNatAt riemannZetaMulSubOne z =
      analyticOrderNatAt riemannZeta z := by
    have htopF : analyticOrderAt riemannZetaMulSubOne z ≠ ⊤ := by
      rw [hordF]
      exact analyticOrderAt_riemannZeta_ne_top hz'.2.2
    have htopZ : analyticOrderAt riemannZeta z ≠ ⊤ :=
      analyticOrderAt_riemannZeta_ne_top hz'.2.2
    apply Nat.cast_injective (R := ℕ∞)
    rw [Nat.cast_analyticOrderNatAt htopF, Nat.cast_analyticOrderNatAt htopZ, hordF]
  rw [hm, ← hEq, hD]
  exact_mod_cast le_rfl

lemma sum_multiplicity_landauInnerDisk_le (T : ℝ) :
    (∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ)) ≤
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|)) := by
  refine (Finset.sum_le_sum ?_).trans (sum_divisor_inner_le T)
  intro ρ hρ
  exact riemannZetaMultiplicity_le_divisor_inner hρ

lemma norm_sum_multiplicity_inv_le_of_gap {T A : ℝ}
    (hA : 0 < A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    {s : ℂ} (hs : s.im = T) :
    ‖∑ ρ ∈ landauInnerDisk T,
        (riemannZetaMultiplicity ρ : ℂ) / (s - ρ)‖ ≤
      (zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|))) *
        (A * (1 + Real.log T)) := by
  have hdenpos : 0 < A * (1 + Real.log T) := by
    have hlog : 0 ≤ Real.log T :=
      Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
    exact mul_pos hA (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1)
      (le_add_of_nonneg_right hlog))
  have hterm : ∀ ρ ∈ landauInnerDisk T,
      ‖(riemannZetaMultiplicity ρ : ℂ) / (s - ρ)‖ ≤
        (riemannZetaMultiplicity ρ : ℝ) * (A * (1 + Real.log T)) := by
    intro ρ hρ
    have hz' := mem_riemannZetaZerosInClosedDisk.mp
      (by simpa [landauInnerDisk] using hρ)
    have hgapρ : 1 / (A * (1 + Real.log T)) ≤ |ρ.im - T| :=
      hgap ρ hz'.2.1 hz'.2.2
    have hne : s ≠ ρ := by
      intro heq
      have : s.im = ρ.im := congrArg Complex.im heq
      rw [hs] at this
      have : |ρ.im - T| = 0 := by simp [this]
      have hpos : 0 < 1 / (A * (1 + Real.log T)) := one_div_pos.mpr hdenpos
      linarith
    have hdist : 1 / (A * (1 + Real.log T)) ≤ ‖s - ρ‖ := by
      have : |s.im - ρ.im| ≤ ‖s - ρ‖ := by
        simpa [sub_im] using abs_im_le_norm (s - ρ)
      rw [hs] at this
      exact hgapρ.trans (by simpa [abs_sub_comm] using this)
    have hinv : ‖s - ρ‖⁻¹ ≤ A * (1 + Real.log T) := by
      have hsp : 0 < ‖s - ρ‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hne)
      rw [inv_le_iff_one_le_mul₀ hsp, mul_comm]
      exact (div_le_iff₀ hdenpos).mp hdist
    rw [norm_div, Complex.norm_natCast]
    exact mul_le_mul_of_nonneg_left hinv (Nat.cast_nonneg _)
  have hsum :=
    (norm_sum_le _ _).trans (Finset.sum_le_sum hterm)
  have hfactor :
      ∑ ρ ∈ landauInnerDisk T,
          (riemannZetaMultiplicity ρ : ℝ) * (A * (1 + Real.log T)) =
        (∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ)) *
          (A * (1 + Real.log T)) :=
    (Finset.sum_mul _ _ _).symm
  rw [hfactor] at hsum
  exact hsum.trans (mul_le_mul_of_nonneg_right
    (sum_multiplicity_landauInnerDisk_le T)
    (le_of_lt hdenpos))

/-- r521: holomorphic zero-free quotient `g = F/P` via the r516
update-fill (orders cancel on the inner-disk zeros). -/
lemma analyticAt_landauPoly (T : ℝ) (z : ℂ) :
    AnalyticAt ℂ (landauPoly T) z :=
  (landauInnerDisk T).analyticAt_fun_prod fun ρ _ => by fun_prop

lemma meromorphicAt_landauPoly (T : ℝ) (z : ℂ) :
    MeromorphicAt (landauPoly T) z :=
  (analyticAt_landauPoly T z).meromorphicAt

lemma meromorphicOrderAt_pow_sub_const (ρ : ℂ) (n : ℕ) (x : ℂ) :
    meromorphicOrderAt (fun z : ℂ => (z - ρ) ^ n) x =
      if x = ρ then (n : WithTop ℤ) else (0 : WithTop ℤ) := by
  by_cases hx : x = ρ
  · rw [if_pos hx]
    have heq : (fun z : ℂ => (z - ρ) ^ n) = ((· - ρ) ^ n) := rfl
    rw [heq, hx]
    simpa using meromorphicOrderAt_pow_id_sub_const (n := n)
  · have han : AnalyticAt ℂ (fun z : ℂ => (z - ρ) ^ n) x := by fun_prop
    have hne : (x - ρ) ^ n ≠ 0 :=
      pow_ne_zero _ (sub_ne_zero.mpr hx)
    rw [if_neg hx, han.meromorphicOrderAt_eq,
      han.analyticOrderAt_eq_zero.mpr hne]
    simp

lemma landauPoly_ne_zero_of_not_mem {T : ℝ} {x : ℂ}
    (hx : x ∉ landauInnerDisk T) :
    landauPoly T x ≠ 0 := by
  unfold landauPoly
  refine Finset.prod_ne_zero_iff.mpr ?_
  intro ρ hρ
  have hne : x ≠ ρ := fun h => hx (by simpa [h] using hρ)
  exact pow_ne_zero _ (sub_ne_zero.mpr hne)

lemma landauPoly_eq_zero_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    landauPoly T ρ = 0 := by
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk] using hρ)
  have hm : 0 < riemannZetaMultiplicity ρ :=
    riemannZetaMultiplicity_pos hz'.2.1 hz'.2.2
  unfold landauPoly
  refine Finset.prod_eq_zero hρ ?_
  simp [sub_self, zero_pow (M₀ := ℂ) hm.ne']

lemma meromorphicOrderAt_landauPoly_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    meromorphicOrderAt (landauPoly T) ρ =
      (riemannZetaMultiplicity ρ : WithTop ℤ) := by
  have hf : ∀ τ ∈ landauInnerDisk T,
      MeromorphicAt (fun z : ℂ =>
        (z - τ) ^ riemannZetaMultiplicity τ) ρ :=
    fun _ _ => by fun_prop
  have hsum := meromorphicOrderAt_fun_prod (s := landauInnerDisk T)
    (f := fun τ z => (z - τ) ^ riemannZetaMultiplicity τ) hf
  unfold landauPoly
  rw [hsum]
  have hterm : ∀ τ ∈ landauInnerDisk T,
      meromorphicOrderAt (fun z : ℂ =>
        (z - τ) ^ riemannZetaMultiplicity τ) ρ =
        if ρ = τ then (riemannZetaMultiplicity τ : WithTop ℤ)
        else (0 : WithTop ℤ) :=
    fun τ _ => meromorphicOrderAt_pow_sub_const τ _ ρ
  rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq]
  simp [hρ]

lemma meromorphicOrderAt_landauPoly_of_not_mem {T : ℝ} {x : ℂ}
    (hx : x ∉ landauInnerDisk T) :
    meromorphicOrderAt (landauPoly T) x = 0 := by
  have hf : ∀ τ ∈ landauInnerDisk T,
      MeromorphicAt (fun z : ℂ =>
        (z - τ) ^ riemannZetaMultiplicity τ) x :=
    fun _ _ => by fun_prop
  have hsum := meromorphicOrderAt_fun_prod (s := landauInnerDisk T)
    (f := fun τ z => (z - τ) ^ riemannZetaMultiplicity τ) hf
  unfold landauPoly
  rw [hsum]
  refine Finset.sum_eq_zero ?_
  intro τ hτ
  have hne : x ≠ τ := fun h => hx (by simpa [h] using hτ)
  simpa [hne] using meromorphicOrderAt_pow_sub_const τ
    (riemannZetaMultiplicity τ) x

lemma meromorphicOrderAt_riemannZetaMulSubOne_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    meromorphicOrderAt riemannZetaMulSubOne ρ =
      (riemannZetaMultiplicity ρ : WithTop ℤ) := by
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk] using hρ)
  have hAn := analyticAt_riemannZetaMulSubOne ρ
  have hAnZ := analyticAt_riemannZeta hz'.2.2
  have hordF : analyticOrderAt riemannZetaMulSubOne ρ =
      analyticOrderAt riemannZeta ρ := by
    have hne : ρ ≠ 1 := hz'.2.2
    have heq : riemannZetaMulSubOne =ᶠ[𝓝 ρ]
        fun w => (w - 1) * riemannZeta w :=
      riemannZetaMulSubOne_eq_mul hne
    have hlin : AnalyticAt ℂ (fun w : ℂ => w - 1) ρ := by fun_prop
    have hlin0 : analyticOrderAt (fun w : ℂ => w - 1) ρ = 0 :=
      hlin.analyticOrderAt_eq_zero.mpr (sub_ne_zero.mpr hne)
    have hfun :
        (fun w : ℂ => (w - 1) * riemannZeta w) =
          (fun w : ℂ => w - 1) * riemannZeta := rfl
    rw [analyticOrderAt_congr heq, hfun, analyticOrderAt_mul hlin hAnZ,
      hlin0, zero_add]
  have htopZ : analyticOrderAt riemannZeta ρ ≠ ⊤ :=
    analyticOrderAt_riemannZeta_ne_top hz'.2.2
  have htopF : analyticOrderAt riemannZetaMulSubOne ρ ≠ ⊤ := by
    rw [hordF]; exact htopZ
  rw [hAn.meromorphicOrderAt_eq, hordF]
  cases hord : analyticOrderAt riemannZeta ρ
  · exact (htopZ hord).elim
  · simp [riemannZetaMultiplicity, analyticOrderNatAt, hord]

noncomputable def landauRaw (T : ℝ) : ℂ → ℂ :=
  riemannZetaMulSubOne / landauPoly T

lemma meromorphicAt_landauRaw (T : ℝ) (x : ℂ) :
    MeromorphicAt (landauRaw T) x :=
  (analyticAt_riemannZetaMulSubOne x).meromorphicAt.div
    (meromorphicAt_landauPoly T x)

lemma meromorphicOrderAt_landauRaw (T : ℝ) (x : ℂ) :
    meromorphicOrderAt (landauRaw T) x =
      meromorphicOrderAt riemannZetaMulSubOne x -
        meromorphicOrderAt (landauPoly T) x :=
  meromorphicOrderAt_div
    (analyticAt_riemannZetaMulSubOne x).meromorphicAt
    (meromorphicAt_landauPoly T x)

lemma meromorphicOrderAt_landauRaw_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    meromorphicOrderAt (landauRaw T) ρ = 0 := by
  rw [meromorphicOrderAt_landauRaw, meromorphicOrderAt_riemannZetaMulSubOne_of_mem hρ,
    meromorphicOrderAt_landauPoly_of_mem hρ]
  simp

lemma meromorphicOrderAt_landauRaw_nonneg (T : ℝ) (x : ℂ) :
    0 ≤ meromorphicOrderAt (landauRaw T) x := by
  by_cases hx : x ∈ landauInnerDisk T
  · simpa [meromorphicOrderAt_landauRaw_of_mem hx]
  · rw [meromorphicOrderAt_landauRaw, meromorphicOrderAt_landauPoly_of_not_mem hx]
    simpa using (analyticAt_riemannZetaMulSubOne x).meromorphicOrderAt_nonneg

noncomputable def landauFillAt (T : ℝ) {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) : ℂ :=
  Classical.choose
    (exists_analyticAt_update_of_meromorphicOrderAt_nonneg
      (meromorphicAt_landauRaw T ρ)
      (meromorphicOrderAt_landauRaw_nonneg T ρ))

lemma analyticAt_update_landauRaw {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    AnalyticAt ℂ (update (landauRaw T) ρ (landauFillAt T hρ)) ρ :=
  Classical.choose_spec
    (exists_analyticAt_update_of_meromorphicOrderAt_nonneg
      (meromorphicAt_landauRaw T ρ)
      (meromorphicOrderAt_landauRaw_nonneg T ρ))

lemma landauFillAt_ne_zero {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    landauFillAt T hρ ≠ 0 := by
  have han := analyticAt_update_landauRaw hρ
  have htend : Filter.Tendsto (landauRaw T) (𝓝[≠] ρ)
      (𝓝 (landauFillAt T hρ)) :=
    continuousAt_update_same.mp han.continuousAt
  obtain ⟨c, hc0, hc⟩ :=
    tendsto_ne_zero_of_meromorphicOrderAt_eq_zero
      (meromorphicAt_landauRaw T ρ)
      (meromorphicOrderAt_landauRaw_of_mem hρ)
  exact (tendsto_nhds_unique htend hc) ▸ hc0

noncomputable def landauQuotient (T : ℝ) : ℂ → ℂ :=
  fun z =>
    if hz : z ∈ landauInnerDisk T then landauFillAt T hz
    else landauRaw T z

lemma landauQuotient_of_not_mem {T : ℝ} {z : ℂ}
    (hz : z ∉ landauInnerDisk T) :
    landauQuotient T z = landauRaw T z := by
  simp [landauQuotient, hz]

lemma landauQuotient_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    landauQuotient T ρ = landauFillAt T hρ := by
  simp [landauQuotient, hρ]

lemma eventuallyEq_landauQuotient_of_not_mem {T : ℝ} {s : ℂ}
    (hs : s ∉ landauInnerDisk T) :
    landauQuotient T =ᶠ[𝓝 s] landauRaw T := by
  have hnhds : (landauInnerDisk T : Set ℂ)ᶜ ∈ 𝓝 s :=
    (Finset.isClosed (landauInnerDisk T)).isOpen_compl.mem_nhds
      (mem_compl hs)
  filter_upwards [hnhds] with z hz
  exact landauQuotient_of_not_mem hz

lemma eventuallyEq_landauQuotient_update {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    landauQuotient T =ᶠ[𝓝 ρ]
      update (landauRaw T) ρ (landauFillAt T hρ) := by
  have hnhds :
      ((landauInnerDisk T).erase ρ : Set ℂ)ᶜ ∈ 𝓝 ρ :=
    ((landauInnerDisk T).erase ρ).isClosed.isOpen_compl.mem_nhds
      (by simp)
  filter_upwards [hnhds] with z hz
  by_cases hzs : z = ρ
  · subst hzs
    simp [landauQuotient, hρ, update_self]
  · have hzp : z ∉ landauInnerDisk T := fun h =>
      hz (Finset.mem_erase.mpr ⟨hzs, h⟩)
    rw [update_of_ne hzs, landauQuotient_of_not_mem hzp]

lemma analyticAt_landauQuotient (T : ℝ) (s : ℂ) :
    AnalyticAt ℂ (landauQuotient T) s := by
  by_cases hs : s ∈ landauInnerDisk T
  · exact (analyticAt_update_landauRaw hs).congr
      (eventuallyEq_landauQuotient_update hs).symm
  · have hP : landauPoly T s ≠ 0 := landauPoly_ne_zero_of_not_mem hs
    have hraw : AnalyticAt ℂ (landauRaw T) s :=
      (analyticAt_riemannZetaMulSubOne s).div
        (analyticAt_landauPoly T s) hP
    exact hraw.congr (eventuallyEq_landauQuotient_of_not_mem hs).symm

lemma analyticOnNhd_landauQuotient (T : ℝ) :
    AnalyticOnNhd ℂ (landauQuotient T) univ :=
  fun s _ => analyticAt_landauQuotient T s

lemma riemannZetaMulSubOne_eq_landauPoly_mul_quotient
    (T : ℝ) (z : ℂ) :
    riemannZetaMulSubOne z =
      landauPoly T z * landauQuotient T z := by
  by_cases hz : z ∈ landauInnerDisk T
  · have hF : riemannZetaMulSubOne z = 0 := by
      have hz' := mem_riemannZetaZerosInClosedDisk.mp
        (by simpa [landauInnerDisk] using hz)
      exact riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩
    rw [hF, landauPoly_eq_zero_of_mem hz, zero_mul]
  · rw [landauQuotient_of_not_mem hz]
    have hP : landauPoly T z ≠ 0 := landauPoly_ne_zero_of_not_mem hz
    rw [landauRaw, Pi.div_apply, ← mul_div_assoc]
    exact (mul_div_cancel_left₀ (riemannZetaMulSubOne z) hP).symm

lemma landauQuotient_ne_zero_of_mem {T : ℝ} {ρ : ℂ}
    (hρ : ρ ∈ landauInnerDisk T) :
    landauQuotient T ρ ≠ 0 := by
  rw [landauQuotient_of_mem hρ]
  exact landauFillAt_ne_zero hρ

lemma landauQuotient_ne_zero_of_not_mem {T : ℝ} {z : ℂ}
    (hz : z ∉ landauInnerDisk T)
    (hF : riemannZetaMulSubOne z ≠ 0) :
    landauQuotient T z ≠ 0 := by
  rw [landauQuotient_of_not_mem hz]
  have hP : landauPoly T z ≠ 0 := landauPoly_ne_zero_of_not_mem hz
  simp [landauRaw, hF, hP]

lemma landauQuotient_ne_zero_on_landau_ball {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.ball ((2 : ℂ) + T * I) (13 / 8)) :
    landauQuotient T z ≠ 0 := by
  by_cases hmem : z ∈ landauInnerDisk T
  · exact landauQuotient_ne_zero_of_mem hmem
  · have hF : riemannZetaMulSubOne z ≠ 0 := by
      intro h0
      have hζ := riemannZetaMulSubOne_eq_zero_iff.mp h0
      have hrabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) :=
        abs_of_pos (by norm_num)
      have hzcl : z ∈ Metric.closedBall ((2 : ℂ) + T * I) (13 / 8) :=
        Metric.ball_subset_closedBall hz
      have : z ∈ landauInnerDisk T :=
        mem_riemannZetaZerosInClosedDisk.mpr
          ⟨by simpa [hrabs] using hzcl, hζ.1, hζ.2⟩
      exact hmem this
    exact landauQuotient_ne_zero_of_not_mem hmem hF

lemma norm_riemannZetaMulSubOne_le_jensen_of_mem_landau_ball
    {T : ℝ} {z : ℂ}
    (hz : z ∈ Metric.ball ((2 : ℂ) + T * I) (13 / 8)) :
    ‖riemannZetaMulSubOne z‖ ≤ jensenSphereMajorant T :=
  (norm_riemannZetaMulSubOne_le_on_landau_ball hz).trans (le_max_right _ _)

lemma landau_center_not_mem_inner (T : ℝ) :
    ((2 : ℂ) + T * I) ∉ landauInnerDisk T := by
  intro h
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk] using h)
  exact riemannZetaMulSubOne_center_ne_zero T
    (riemannZetaMulSubOne_eq_zero_iff.mpr ⟨hz'.2.1, hz'.2.2⟩)

lemma card_landauInnerDisk_le_sum_multiplicity (T : ℝ) :
    ((landauInnerDisk T).card : ℝ) ≤
      ∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ) := by
  have h1 : ((landauInnerDisk T).card : ℝ) =
      ∑ ρ ∈ landauInnerDisk T, (1 : ℝ) := by
    simp
  rw [h1]
  refine Finset.sum_le_sum ?_
  intro ρ hρ
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk] using hρ)
  have hm := riemannZetaMultiplicity_pos hz'.2.1 hz'.2.2
  exact_mod_cast hm

lemma exists_landau_midRadius (T : ℝ) :
    ∃ R : ℝ, (49 / 32 : ℝ) ≤ R ∧ R ≤ (51 / 32 : ℝ) ∧
      ∀ ρ ∈ landauInnerDisk T,
        (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
          |R - ‖ρ - ((2 : ℂ) + T * I)‖| := by
  set c := (2 : ℂ) + T * I
  set s := (landauInnerDisk T).image fun ρ : ℂ => ‖ρ - c‖
  have hab : (49 / 32 : ℝ) ≤ (51 / 32 : ℝ) := by norm_num
  obtain ⟨R, hR1, hR2, hfar⟩ :=
    exists_point_far_from_finset_any s hab
  refine ⟨R, hR1, hR2, ?_⟩
  intro ρ hρ
  have him : ‖ρ - c‖ ∈ s :=
    Finset.mem_image.mpr ⟨ρ, hρ, rfl⟩
  have h := hfar _ him
  have hlen : (51 / 32 : ℝ) - 49 / 32 = (1 / 16 : ℝ) := by norm_num
  have hfrac :
      (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
        ((51 / 32 : ℝ) - 49 / 32) /
          (2 * (s.card + 1 : ℝ)) := by
    have hden : 0 < 2 * (s.card + 1 : ℝ) := by positivity
    have hcard : (s.card : ℝ) ≤ (landauInnerDisk T).card :=
      Nat.cast_le.mpr Finset.card_image_le
    have : (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) =
        (1 / 16 : ℝ) / (2 * ((landauInnerDisk T).card + 1 : ℝ)) := by
      field_simp; ring
    rw [this, hlen]
    exact div_le_div_of_nonneg_left (by norm_num) hden
      (by nlinarith [hcard])
  exact hfrac.trans h

lemma mem_closedBall_three_halves_of_horizontal
    {T σ : ℝ} (hσ1 : (1 / 2 : ℝ) ≤ σ) (hσ2 : σ ≤ 2) :
    σ + T * I ∈ Metric.closedBall ((2 : ℂ) + T * I) (3 / 2) := by
  have hdist : ‖(σ + T * I) - ((2 : ℂ) + T * I)‖ = |σ - 2| := by
    have heq : (σ + T * I) - ((2 : ℂ) + T * I) = ↑(σ - 2) := by
      norm_cast
      simp
    rw [heq, Complex.norm_real, Real.norm_eq_abs]
  have hle : |σ - 2| ≤ (3 / 2 : ℝ) := by
    rw [abs_sub_comm]
    exact abs_le.mpr ⟨by linarith, by linarith⟩
  rw [Metric.mem_closedBall, dist_eq_norm, hdist]
  exact hle

lemma horizontal_ne_one {T σ : ℝ} (hT : (2 : ℝ) ≤ T) :
    (σ : ℂ) + T * I ≠ 1 := by
  intro h
  have him : ((σ : ℂ) + T * I).im = (1 : ℂ).im := congrArg Complex.im h
  simp at him
  linarith

lemma riemannZeta_ne_zero_of_landau_gap {T A : ℝ}
    (hA : 0 < A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    {σ : ℝ} :
    riemannZeta (σ + T * I) ≠ 0 := by
  intro hz
  have hs1 := horizontal_ne_one (σ := σ) hT
  have hdenpos : 0 < A * (1 + Real.log T) := by
    have hlog : 0 ≤ Real.log T :=
      Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
    exact mul_pos hA (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1)
      (le_add_of_nonneg_right hlog))
  have hgapρ := hgap _ hz hs1
  have : |((σ : ℂ) + T * I).im - T| = 0 := by simp
  have hpos : 0 < 1 / (A * (1 + Real.log T)) := one_div_pos.mpr hdenpos
  linarith

lemma not_mem_landauInnerDisk_of_gap {T A : ℝ}
    (hA : 0 < A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    {σ : ℝ} :
    (σ : ℂ) + T * I ∉ landauInnerDisk T := by
  intro h
  have hz' := mem_riemannZetaZerosInClosedDisk.mp
    (by simpa [landauInnerDisk] using h)
  exact riemannZeta_ne_zero_of_landau_gap hA hT hgap hz'.2.1

lemma logDeriv_riemannZeta_eq_landauQuotient_add
    {T : ℝ} {s : ℂ} (hs1 : s ≠ 1) (hP : ∀ ρ ∈ landauInnerDisk T, s ≠ ρ)
    (hζ : riemannZeta s ≠ 0) :
    logDeriv riemannZeta s =
      logDeriv (landauQuotient T) s +
        logDeriv (landauPoly T) s - 1 / (s - 1) := by
  have hF0 : riemannZetaMulSubOne s ≠ 0 := by
    intro h0
    exact hζ (riemannZetaMulSubOne_eq_zero_iff.mp h0).1
  have hP0 : landauPoly T s ≠ 0 := by
    refine landauPoly_ne_zero_of_not_mem ?_
    intro hmem
    exact hP s hmem rfl
  have hg0 : landauQuotient T s ≠ 0 :=
    landauQuotient_ne_zero_of_not_mem
      (fun hmem => hP s hmem rfl) hF0
  have hlogF := logDeriv_riemannZeta_eq_logDeriv_mulSubOne_sub hs1 hζ
  have heq : riemannZetaMulSubOne = fun z =>
      landauPoly T z * landauQuotient T z := by
    ext z
    exact riemannZetaMulSubOne_eq_landauPoly_mul_quotient T z
  have hlogmul :
      logDeriv riemannZetaMulSubOne s =
        logDeriv (landauPoly T) s + logDeriv (landauQuotient T) s := by
    have hmul := logDeriv_mul s hP0 hg0
      (analyticAt_landauPoly T s).differentiableAt
      (analyticAt_landauQuotient T s).differentiableAt
    rw [heq]
    exact hmul
  rw [hlogF, hlogmul]
  ring

/-- Classical Landau / Borel–Carathéodory local splitting on a gap
edge `Im = T`.  Contour revision (r520): the r510 disk stays in
`Re > 0`, so the sealed range is `σ ∈ [1/2, 2]` (inner radius
`3/2` inside `D(2+iT, 13/8)`).  The intended contour is
`[-1/16, 2]`; the sliver `[-1/16, 1/2]` needs `|F|` on `Re ≲ 0`.
The cubic log absorbs the `log T · log log T` Blaschke factor
(the horizontal integral still dies: poly-log / `T² → 0`).
Named, not a `sorry`. -/
def HorizontalEdgeLandauBound : Prop :=
  ∃ A B : ℝ, 0 < A ∧ 0 < B ∧
    ∀ {T : ℝ}, (2 : ℝ) ≤ T →
      (∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) →
      ∀ σ : ℝ, (1 / 2 : ℝ) ≤ σ → σ ≤ 2 →
        ‖logDeriv riemannZeta (σ + T * I)‖ ≤ B * (1 + Real.log T) ^ 3

lemma norm_sub_ge_abs_dist_sub {c w ρ : ℂ} {R : ℝ}
    (hw : dist w c = R) :
    |R - ‖ρ - c‖| ≤ ‖w - ρ‖ := by
  have h := abs_norm_sub_norm_le (w - c) (ρ - c)
  have hwcn : ‖w - c‖ = R := by simpa [dist_eq_norm] using hw
  have hsub : (w - c) - (ρ - c) = w - ρ := by ring
  simpa [hwcn, hsub] using h

lemma norm_landauPoly_ge_on_mid_sphere {T R : ℝ} {w : ℂ}
    (hw : w ∈ Metric.sphere ((2 : ℂ) + T * I) R)
    (hfar : ∀ ρ ∈ landauInnerDisk T,
      (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
        |R - ‖ρ - ((2 : ℂ) + T * I)‖|) :
    ((1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ))) ^
        (∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ) ≤
      ‖landauPoly T w‖ := by
  set c := (2 : ℂ) + T * I
  set η : ℝ := (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ))
  set N : ℕ := ∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ
  have hwR : dist w c = R := Metric.mem_sphere.mp hw
  have heta0 : 0 ≤ η := by
    have : 0 < ((landauInnerDisk T).card + 1 : ℝ) := by positivity
    positivity
  have hfac : ∀ ρ ∈ landauInnerDisk T,
      η ^ riemannZetaMultiplicity ρ ≤
        ‖w - ρ‖ ^ riemannZetaMultiplicity ρ := by
    intro ρ hρ
    have hle : η ≤ ‖w - ρ‖ :=
      (hfar ρ hρ).trans (norm_sub_ge_abs_dist_sub (c := c) hwR)
    exact pow_le_pow_left₀ heta0 hle _
  have hprod :=
    Finset.prod_le_prod (fun _ _ => pow_nonneg heta0 _) hfac
  have hleft :
      ∏ ρ ∈ landauInnerDisk T, η ^ riemannZetaMultiplicity ρ = η ^ N :=
    Finset.prod_pow_eq_pow_sum _ _ _
  have hright :
      ∏ ρ ∈ landauInnerDisk T, ‖w - ρ‖ ^ riemannZetaMultiplicity ρ =
        ‖landauPoly T w‖ := by
    unfold landauPoly
    rw [norm_prod]
    refine Finset.prod_congr rfl ?_
    intro ρ _; rw [norm_pow]
  rwa [hleft, hright] at hprod

lemma not_mem_landauInnerDisk_of_mid_sphere {T R : ℝ} {w : ℂ}
    (hw : w ∈ Metric.sphere ((2 : ℂ) + T * I) R)
    (hfar : ∀ ρ ∈ landauInnerDisk T,
      (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
        |R - ‖ρ - ((2 : ℂ) + T * I)‖|)
    (heta : 0 < (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ))) :
    w ∉ landauInnerDisk T := by
  intro hmem
  have hwR : dist w ((2 : ℂ) + T * I) = R := Metric.mem_sphere.mp hw
  have hsep := hfar w hmem
  have : |R - ‖w - ((2 : ℂ) + T * I)‖| = 0 := by
    have : ‖w - ((2 : ℂ) + T * I)‖ = R := by
      simpa [dist_eq_norm] using hwR
    simp [this]
  linarith

lemma norm_landauQuotient_le_on_mid_sphere {T R : ℝ} {w : ℂ}
    (hRlt : R < (13 / 8 : ℝ))
    (hw : w ∈ Metric.sphere ((2 : ℂ) + T * I) R)
    (hfar : ∀ ρ ∈ landauInnerDisk T,
      (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
        |R - ‖ρ - ((2 : ℂ) + T * I)‖|) :
    ‖landauQuotient T w‖ ≤
      jensenSphereMajorant T *
        ((1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)))⁻¹ ^
          (∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ) := by
  set c := (2 : ℂ) + T * I
  set η : ℝ := (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ))
  set N : ℕ := ∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ
  have hwR : dist w c = R := Metric.mem_sphere.mp hw
  have hw13 : w ∈ Metric.ball c (13 / 8) := by
    rw [Metric.mem_ball, hwR]; exact hRlt
  have heta_pos : 0 < η := by
    have : 0 < ((landauInnerDisk T).card + 1 : ℝ) := by positivity
    positivity
  have hwS := not_mem_landauInnerDisk_of_mid_sphere hw hfar heta_pos
  have hg : landauQuotient T w = landauRaw T w :=
    landauQuotient_of_not_mem hwS
  have hPge := norm_landauPoly_ge_on_mid_sphere hw hfar
  have hFle : ‖riemannZetaMulSubOne w‖ ≤ jensenSphereMajorant T :=
    norm_riemannZetaMulSubOne_le_jensen_of_mem_landau_ball hw13
  have hPpos : 0 < ‖landauPoly T w‖ :=
    lt_of_lt_of_le (pow_pos heta_pos N) hPge
  have hgw : ‖landauQuotient T w‖ =
      ‖riemannZetaMulSubOne w‖ / ‖landauPoly T w‖ := by
    rw [hg, landauRaw, Pi.div_apply, norm_div]
  have hMF0 : 0 ≤ jensenSphereMajorant T :=
    le_trans zero_le_one (one_le_jensenSphereMajorant T)
  have h1 : ‖riemannZetaMulSubOne w‖ / ‖landauPoly T w‖ ≤
      jensenSphereMajorant T / ‖landauPoly T w‖ :=
    div_le_div_of_nonneg_right hFle (norm_nonneg _)
  have h2 : jensenSphereMajorant T / ‖landauPoly T w‖ ≤
      jensenSphereMajorant T / (η ^ N) :=
    div_le_div_of_nonneg_left hMF0 (pow_pos heta_pos N) hPge
  have h3 : jensenSphereMajorant T / (η ^ N) =
      jensenSphereMajorant T * η⁻¹ ^ N := by
    rw [div_eq_mul_inv, inv_pow]
  rw [hgw]
  exact (h1.trans h2).trans_eq h3

lemma norm_landauQuotient_le_on_mid_closedBall {T R : ℝ}
    (hRpos : 0 < R) (hRlt : R < (13 / 8 : ℝ))
    (hfar : ∀ ρ ∈ landauInnerDisk T,
      (1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)) ≤
        |R - ‖ρ - ((2 : ℂ) + T * I)‖|)
    {z : ℂ} (hz : z ∈ Metric.closedBall ((2 : ℂ) + T * I) R) :
    ‖landauQuotient T z‖ ≤
      jensenSphereMajorant T *
        ((1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)))⁻¹ ^
          (∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ) := by
  set c := (2 : ℂ) + T * I
  set Cbd : ℝ :=
    jensenSphereMajorant T *
      ((1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)))⁻¹ ^
        (∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ)
  have hAn := analyticOnNhd_landauQuotient T
  have hdiff : DifferentiableOn ℂ (landauQuotient T) (Metric.ball c R) :=
    (hAn.mono (Set.subset_univ _)).differentiableOn
  have hcont : ContinuousOn (landauQuotient T)
      (closure (Metric.ball c R)) :=
    hAn.continuousOn.mono (Set.subset_univ _)
  have hdc : DiffContOnCl ℂ (landauQuotient T) (Metric.ball c R) :=
    ⟨hdiff, hcont⟩
  have hfront : ∀ w ∈ frontier (Metric.ball c R),
      ‖landauQuotient T w‖ ≤ Cbd := by
    intro w hw
    have hw' : w ∈ Metric.sphere c R :=
      Metric.frontier_ball_subset_sphere hw
    exact norm_landauQuotient_le_on_mid_sphere hRlt hw' hfar
  by_cases hzt : z ∈ Metric.ball c R
  · exact Complex.norm_le_of_forall_mem_frontier_norm_le
      Metric.isBounded_ball hdc hfront (subset_closure hzt)
  · have hw : z ∈ Metric.sphere c R := by
      have hzle : dist z c ≤ R := Metric.mem_closedBall.mp hz
      have hznlt : ¬ dist z c < R := fun h =>
        hzt (Metric.mem_ball.mpr h)
      exact Metric.mem_sphere.mpr (le_antisymm hzle (le_of_not_gt hznlt))
    exact norm_landauQuotient_le_on_mid_sphere hRlt hw hfar

lemma log_norm_landauQuotient_center_ge (T : ℝ) :
    -Real.log (13 / 8 : ℝ) *
        (∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ)) -
      Real.log ‖riemannZeta 2‖ ≤
      Real.log ‖landauQuotient T ((2 : ℂ) + T * I)‖ := by
  set c := (2 : ℂ) + T * I
  set N : ℕ := ∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ
  have hcS : c ∉ landauInnerDisk T := landau_center_not_mem_inner T
  have hg : landauQuotient T c = landauRaw T c :=
    landauQuotient_of_not_mem hcS
  have hP0 : landauPoly T c ≠ 0 := landauPoly_ne_zero_of_not_mem hcS
  have hF0 : riemannZetaMulSubOne c ≠ 0 :=
    riemannZetaMulSubOne_center_ne_zero T
  have hgw : ‖landauQuotient T c‖ =
      ‖riemannZetaMulSubOne c‖ / ‖landauPoly T c‖ := by
    rw [hg, landauRaw, Pi.div_apply, norm_div]
  have hPle : ‖landauPoly T c‖ ≤ (13 / 8 : ℝ) ^ N := by
    have hfac : ∀ ρ ∈ landauInnerDisk T,
        ‖c - ρ‖ ^ riemannZetaMultiplicity ρ ≤
          (13 / 8 : ℝ) ^ riemannZetaMultiplicity ρ := by
      intro ρ hρ
      have hz' := mem_riemannZetaZerosInClosedDisk.mp
        (by simpa [landauInnerDisk, c] using hρ)
      have hrabs : |(13 / 8 : ℝ)| = (13 / 8 : ℝ) :=
        abs_of_pos (by norm_num)
      have hle : ‖ρ - c‖ ≤ (13 / 8 : ℝ) := by
        simpa [c, hrabs, dist_eq_norm, Metric.mem_closedBall] using hz'.1
      have : ‖c - ρ‖ = ‖ρ - c‖ := norm_sub_rev _ _
      rw [this]
      exact pow_le_pow_left₀ (norm_nonneg _) hle _
    have hprod :=
      Finset.prod_le_prod (fun ρ _ => pow_nonneg (norm_nonneg _) _) hfac
    have hright :
        ∏ ρ ∈ landauInnerDisk T,
            (13 / 8 : ℝ) ^ riemannZetaMultiplicity ρ =
          (13 / 8 : ℝ) ^ N :=
      Finset.prod_pow_eq_pow_sum _ _ _
    have hleft : ‖landauPoly T c‖ =
        ∏ ρ ∈ landauInnerDisk T,
          ‖c - ρ‖ ^ riemannZetaMultiplicity ρ := by
      unfold landauPoly
      rw [norm_prod]
      refine Finset.prod_congr rfl ?_
      intro ρ _; rw [norm_pow]
    rw [hright] at hprod
    rwa [hleft]
  have hFge := norm_riemannZetaMulSubOne_center_ge T
  have hζ2 : 0 < ‖riemannZeta 2‖ := by
    rw [norm_riemannZeta_two]; positivity
  have hgcpos : 0 < ‖landauQuotient T c‖ := by
    rw [hgw]
    exact div_pos (norm_pos_iff.mpr hF0) (norm_pos_iff.mpr hP0)
  have hlog : Real.log ‖landauQuotient T c‖ =
      Real.log ‖riemannZetaMulSubOne c‖ - Real.log ‖landauPoly T c‖ := by
    rw [hgw, Real.log_div (norm_pos_iff.mpr hF0).ne'
      (norm_pos_iff.mpr hP0).ne']
  have hlogF : -Real.log ‖riemannZeta 2‖ ≤
      Real.log ‖riemannZetaMulSubOne c‖ := by
    have := log_center_neg_le T
    linarith
  have h138 : 1 < (13 / 8 : ℝ) := by norm_num
  have hlogP : Real.log ‖landauPoly T c‖ ≤
      (N : ℝ) * Real.log (13 / 8 : ℝ) := by
    have hPpos : 0 < ‖landauPoly T c‖ := norm_pos_iff.mpr hP0
    have h138pos : 0 < (13 / 8 : ℝ) := by norm_num
    have := Real.log_le_log hPpos hPle
    have hpow : Real.log ((13 / 8 : ℝ) ^ N) =
        (N : ℝ) * Real.log (13 / 8 : ℝ) :=
      Real.log_pow _ _
    rwa [hpow] at this
  have hsum : (N : ℝ) =
      ∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ) := by
    simp [N, Nat.cast_sum]
  rw [hlog, ← hsum]
  linarith [hlogF, hlogP]

lemma landau_mid_geom_factor {R : ℝ}
    (hRa : (49 / 32 : ℝ) ≤ R) (hRb : R ≤ (51 / 32 : ℝ)) :
    (R + 3 / 2) / (R - 3 / 2) ^ 2 ≤ (4096 : ℝ) := by
  have hden : (1 / 32 : ℝ) ≤ R - 3 / 2 := by linarith
  have hdenpos : 0 < R - 3 / 2 := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1 / 32) hden
  have hnum : R + 3 / 2 ≤ (99 / 32 : ℝ) := by linarith
  have hsq : (1 / 32 : ℝ) ^ 2 ≤ (R - 3 / 2) ^ 2 :=
    pow_le_pow_left₀ (by norm_num) hden 2
  have hpos : 0 < (R - 3 / 2) ^ 2 := pow_pos hdenpos 2
  have : (R + 3 / 2) / (R - 3 / 2) ^ 2 ≤
      (99 / 32 : ℝ) / (1 / 32 : ℝ) ^ 2 := by
    rw [div_le_div_iff₀ hpos (by positivity)]
    nlinarith [hnum, hsq, sq_nonneg (R - 3 / 2)]
  have hval : (99 / 32 : ℝ) / (1 / 32 : ℝ) ^ 2 = (3168 : ℝ) := by
    norm_num
  linarith

noncomputable def landauHorizontalConst : ℝ :=
  100000000 * (1 + zetaZerosInDiskCardBoundInner) ^ 3 *
    (1 + Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ +
      Real.log 32 + Real.log (13 / 8) + 4)

lemma landauHorizontalConst_pos : 0 < landauHorizontalConst := by
  have hC : 0 < 1 + zetaZerosInDiskCardBoundInner := by
    linarith [zetaZerosInDiskCardBoundInner_pos]
  have h1 : 0 < Real.log jensenSphereMajorantCoeff :=
    Real.log_pos one_lt_jensenSphereMajorantCoeff
  have h2 : 0 < Real.log ‖riemannZeta 2‖ :=
    Real.log_pos one_lt_norm_riemannZeta_two
  have h3 : 0 < Real.log 32 := Real.log_pos (by norm_num)
  have h4 : 0 < Real.log (13 / 8 : ℝ) := Real.log_pos (by norm_num)
  unfold landauHorizontalConst
  positivity

set_option maxHeartbeats 400000 in
lemma landau_cubic_pack {Cin L a b c d : ℝ}
    (hC : 0 ≤ Cin) (hL : 1 ≤ L)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d) :
    16384 * (1 + (a + b + 4 + 2 * Cin * (c + (2 * Cin + 1)) +
        2 * Cin * d) * L ^ 2) + 2 * Cin * L ^ 2 + 1 ≤
      100000000 * (1 + Cin) ^ 3 * (1 + a + b + c + d + 4) * L ^ 3 := by
  set Q : ℝ := 1 + a + b + c + d + 4
  set P : ℝ := a + b + 4 + 2 * Cin * (c + (2 * Cin + 1)) + 2 * Cin * d
  set U : ℝ := 1 + Cin
  have hQ : (1 : ℝ) ≤ Q := by linarith
  have hU : (1 : ℝ) ≤ U := by linarith
  have hP0 : 0 ≤ P := by
    have : 0 ≤ 2 * Cin := by linarith
    nlinarith
  have hL2 : (1 : ℝ) ≤ L * L := by nlinarith [hL]
  have hL3 : L * L ≤ L * L * L := by nlinarith [hL]
  have hU2 : (1 : ℝ) ≤ U * U := by nlinarith [hU]
  have hU3 : U * U ≤ U * U * U := by nlinarith [hU]
  have hP : P ≤ 20 * (U * U * U) * Q := by
    have hPexp : P = a + b + 4 + 2 * Cin * c + 4 * Cin * Cin + 2 * Cin +
        2 * Cin * d := by ring
    rw [hPexp]
    have h1 : a + b + 4 ≤ Q := by linarith
    have h2 : 2 * Cin * c ≤ 2 * U * Q := by nlinarith
    have h3 : 2 * Cin * d ≤ 2 * U * Q := by nlinarith
    have h4 : 4 * Cin * Cin + 2 * Cin ≤ 4 * U * U := by nlinarith
    have hU3' : U ≤ U * U * U := by nlinarith [hU, hU2]
    have h2u : 2 * U * Q ≤ 2 * (U * U * U) * Q :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hU3' (by norm_num : (0 : ℝ) ≤ 2))
        (le_trans (by norm_num : (0 : ℝ) ≤ 1) hQ)
    have h4u : 4 * U * U ≤ 4 * (U * U * U) * Q := by
      have : U * U ≤ (U * U * U) * Q := by nlinarith [hU, hQ]
      nlinarith
    have h1u : Q ≤ (U * U * U) * Q := by nlinarith [hU, hU2, hU3, hQ]
    nlinarith [h1, h2, h3, h4, h2u, h4u, h1u]
  have hleft : 16384 * (1 + P * (L * L)) + 2 * Cin * (L * L) + 1 ≤
      (16385 + 2 * Cin + 16384 * P) * (L * L) := by
    nlinarith [hL2, hC, hP0]
  have h16385 : (16385 : ℝ) ≤ 16385 * (U * U * U) * Q := by
    nlinarith [hU, hU2, hU3, hQ]
  have h2c : 2 * Cin ≤ 2 * (U * U * U) * Q := by
    nlinarith [hU, hU2, hU3, hQ, hC]
  have h16384P : 16384 * P ≤ 327680 * (U * U * U) * Q := by
    nlinarith [hP]
  have hcoef : 16385 + 2 * Cin + 16384 * P ≤ 400000 * (U * U * U) * Q := by
    linarith [h16385, h2c, h16384P]
  have hmid : (16385 + 2 * Cin + 16384 * P) * (L * L) ≤
      400000 * (U * U * U) * Q * (L * L * L) := by
    have := mul_le_mul hcoef hL3 (by nlinarith [hL])
      (by nlinarith [hU, hQ])
    nlinarith
  have hfin : 400000 * (U * U * U) * Q * (L * L * L) ≤
      100000000 * (U * U * U) * Q * (L * L * L) := by
    nlinarith [hU, hQ, hL]
  have hpowU : (1 + Cin) ^ 3 = U * U * U := by
    simp [U]; ring
  have hpowL : L ^ 2 = L * L := by ring
  have hpowL3 : L ^ 3 = L * L * L := by ring
  have hgoal : 16384 * (1 + P * (L * L)) + 2 * Cin * (L * L) + 1 ≤
      100000000 * (U * U * U) * Q * (L * L * L) :=
    hleft.trans (hmid.trans hfin)
  rw [hpowU, hpowL, hpowL3]
  simpa [P, Q, U] using hgoal

/-- r524: A≥1 scales the A=1 cubic pack; the extra factor sits on B. -/
lemma landau_cubic_pack_scale {Cin L a b c d A : ℝ}
    (hA : (1 : ℝ) ≤ A) (hC : 0 ≤ Cin) (hL : 1 ≤ L)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d) :
    16384 * (1 + (a + b + 4 + 2 * Cin * (c + (2 * Cin + 1)) +
        2 * Cin * d) * L ^ 2) + 2 * A * Cin * L ^ 2 + 1 ≤
      A * (100000000 * (1 + Cin) ^ 3 * (1 + a + b + c + d + 4) * L ^ 3) := by
  have hpack := landau_cubic_pack (Cin := Cin) (L := L) (a := a) (b := b)
    (c := c) (d := d) hC hL ha hb hc hd
  set Q : ℝ := a + b + 4 + 2 * Cin * (c + (2 * Cin + 1)) + 2 * Cin * d
  set U : ℝ := 16384 * (1 + Q * L ^ 2) + 1
  set V : ℝ := 2 * Cin * L ^ 2
  have hQ0 : 0 ≤ Q := by
    have : 0 ≤ 2 * Cin := by linarith
    nlinarith
  have hU0 : 0 ≤ U := by
    have hL2 : 0 ≤ L ^ 2 := sq_nonneg L
    unfold U; nlinarith
  have hV0 : 0 ≤ V := by
    have hL2 : 0 ≤ L ^ 2 := sq_nonneg L
    unfold V; nlinarith
  have hscale : U + A * V ≤ A * (U + V) := by
    have hx : U ≤ A * U := le_mul_of_one_le_left hU0 hA
    nlinarith [hx]
  have hUV : U + V =
      16384 * (1 + Q * L ^ 2) + 2 * Cin * L ^ 2 + 1 := by
    unfold U V; ring
  have hUA : U + A * V =
      16384 * (1 + Q * L ^ 2) + 2 * A * Cin * L ^ 2 + 1 := by
    unfold U V; ring
  have hpack' : U + V ≤
      100000000 * (1 + Cin) ^ 3 * (1 + a + b + c + d + 4) * L ^ 3 := by
    simpa [hUV, Q] using hpack
  have hmul : A * (U + V) ≤
      A * (100000000 * (1 + Cin) ^ 3 * (1 + a + b + c + d + 4) * L ^ 3) :=
    mul_le_mul_of_nonneg_left hpack' (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA)
  rw [← hUA]
  exact hscale.trans hmul

set_option maxHeartbeats 800000 in
lemma horizontalEdgeLandauBound_of_gap {T A : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    {σ : ℝ} (hσ1 : (1 / 2 : ℝ) ≤ σ) (hσ2 : σ ≤ 2) :
    ‖logDeriv riemannZeta (σ + T * I)‖ ≤
      (A * landauHorizontalConst) * (1 + Real.log T) ^ 3 := by
  set c := (2 : ℂ) + T * I
  set s := (σ : ℂ) + T * I
  set L := (1 : ℝ) + Real.log T
  set Cin := zetaZerosInDiskCardBoundInner
  set S := landauInnerDisk T
  set n := S.card
  set η : ℝ := (1 : ℝ) / (32 * (n + 1 : ℝ))
  set N : ℕ := ∑ ρ ∈ S, riemannZetaMultiplicity ρ
  set MF := jensenSphereMajorant T
  have hL : (1 : ℝ) ≤ L := by
    have : 0 ≤ Real.log T :=
      Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
    exact le_add_of_nonneg_right this
  have hLpos : 0 < L := lt_of_lt_of_le zero_lt_one hL
  have hLL : L ≤ L ^ 2 := by nlinarith [hL]
  have hCin : 0 < Cin := zetaZerosInDiskCardBoundInner_pos
  have hNreal : (N : ℝ) = ∑ ρ ∈ S, (riemannZetaMultiplicity ρ : ℝ) := by
    simp [N, Nat.cast_sum]
  have hNleL : (N : ℝ) ≤ 2 * Cin * L := by
    have h := (sum_multiplicity_landauInnerDisk_le T).trans
      (mul_le_mul_of_nonneg_left (one_add_log_two_add_abs_le hT) hCin.le)
    have heq : zetaZerosInDiskCardBoundInner * (2 * (1 + Real.log T)) =
        2 * Cin * L := by
      simp [Cin, L]; ring
    simpa [S, hNreal, heq] using h
  have hs1 : s ≠ 1 := horizontal_ne_one (σ := σ) hT
  have hApos : (0 : ℝ) < A :=
    lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA
  have hζ : riemannZeta s ≠ 0 :=
    riemannZeta_ne_zero_of_landau_gap (A := A) hApos hT hgap
  have hsnot : s ∉ S :=
    not_mem_landauInnerDisk_of_gap (A := A) hApos hT hgap
  have hPne : ∀ ρ ∈ S, s ≠ ρ :=
    fun ρ hρ heq => hsnot (by simpa [S, heq] using hρ)
  have hsplit := logDeriv_riemannZeta_eq_landauQuotient_add (T := T) hs1
    (by simpa [S] using hPne) hζ
  have hPlog := logDeriv_landauPoly (T := T) (s := s)
    (by simpa [S] using hPne)
  have him : s.im = T := by simp [s]
  have hPnormL : ‖logDeriv (landauPoly T) s‖ ≤ 2 * A * Cin * L ^ 2 := by
    have h := norm_sum_multiplicity_inv_le_of_gap (A := A) hApos hT hgap him
    have h' : ‖logDeriv (landauPoly T) s‖ ≤
        Cin * (1 + Real.log (2 + |T|)) * (A * L) := by
      rw [hPlog]
      simpa [S, Cin, L] using h
    have := h'.trans (mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left (one_add_log_two_add_abs_le hT) hCin.le)
      (mul_nonneg hApos.le hLpos.le))
    nlinarith [hCin.le, hL, hA]
  have hs1norm : ‖(1 : ℂ) / (s - 1)‖ ≤ (1 : ℝ) := by
    have hne : s - 1 ≠ 0 := sub_ne_zero.mpr hs1
    have himle : T ≤ ‖s - 1‖ := by
      have : |(s - 1).im| ≤ ‖s - 1‖ := abs_im_le_norm (s - 1)
      have him : (s - 1).im = T := by simp [s]
      rw [him, abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) hT)] at this
      exact this
    rw [norm_div, norm_one]
    have : (1 : ℝ) ≤ ‖s - 1‖ :=
      le_trans (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT) himle
    simpa [one_div] using inv_le_one_of_one_le₀ this
  obtain ⟨R, hRa, hRb, hfar⟩ := exists_landau_midRadius T
  have hRpos : 0 < R :=
    lt_of_lt_of_le (by norm_num : (0 : ℝ) < 49 / 32) hRa
  have hrR : (3 / 2 : ℝ) < R :=
    lt_of_lt_of_le (by norm_num : (3 / 2 : ℝ) < 49 / 32) hRa
  have hRlt : R < (13 / 8 : ℝ) :=
    lt_of_le_of_lt hRb (by norm_num)
  have hclR : Metric.closedBall c R ⊆ Metric.ball c (13 / 8) :=
    Metric.closedBall_subset_ball hRlt
  have hAn := analyticOnNhd_landauQuotient T
  have hdiff : DifferentiableOn ℂ (landauQuotient T) (Metric.ball c R) :=
    (hAn.mono (Set.subset_univ _)).differentiableOn
  have hneR : ∀ z ∈ Metric.ball c R, landauQuotient T z ≠ 0 :=
    fun z hz => landauQuotient_ne_zero_on_landau_ball
      (hclR (Metric.ball_subset_closedBall hz))
  have heta_pos : 0 < η := by
    have : 0 < (n + 1 : ℝ) := by positivity
    positivity
  set Cbd : ℝ := MF * η⁻¹ ^ N
  have hCeq : Cbd = jensenSphereMajorant T *
      ((1 : ℝ) / (32 * ((landauInnerDisk T).card + 1 : ℝ)))⁻¹ ^
        (∑ ρ ∈ landauInnerDisk T, riemannZetaMultiplicity ρ) := by
    simp [Cbd, MF, η, N, n, S]
  have hCbdle : ∀ z ∈ Metric.ball c R, ‖landauQuotient T z‖ ≤ Cbd := by
    intro z hz
    have := norm_landauQuotient_le_on_mid_closedBall hRpos hRlt
      (by simpa [S] using hfar)
      (Metric.ball_subset_closedBall hz)
    convert this
  have hMFpos : 0 < MF :=
    lt_of_lt_of_le zero_lt_one (one_le_jensenSphereMajorant T)
  have hCpos : 0 < Cbd := by
    have : 0 < η⁻¹ := inv_pos.mpr heta_pos
    positivity
  have hlogR : ∀ z ∈ Metric.ball c R,
      Real.log ‖landauQuotient T z‖ ≤ Real.log Cbd :=
    fun z hz => Real.log_le_log (norm_pos_iff.mpr (hneR z hz)) (hCbdle z hz)
  have hzBall : s ∈ Metric.closedBall c (3 / 2) :=
    mem_closedBall_three_halves_of_horizontal hσ1 hσ2
  have hker :=
    norm_logDeriv_le_of_log_norm_le (f := landauQuotient T) (c := c)
      (M := Real.log Cbd) (R := R) (r := (3 / 2 : ℝ))
      hRpos (by norm_num) hrR hdiff hneR hlogR hzBall
  have hgeom := landau_mid_geom_factor hRa hRb
  set K : ℝ := max (Real.log Cbd - Real.log ‖landauQuotient T c‖) (1 : ℝ)
  have hKform : 4 * max (Real.log Cbd - Real.log ‖landauQuotient T c‖) (1 : ℝ) *
      (R + 3 / 2) / (R - 3 / 2) ^ 2 =
        4 * K * ((R + 3 / 2) / (R - 3 / 2) ^ 2) := by
    unfold K
    ring
  have hgker : ‖logDeriv (landauQuotient T) s‖ ≤ 4 * K * 4096 := by
    have := hker.trans_eq hKform
    exact this.trans (mul_le_mul_of_nonneg_left hgeom (by
      have hKpos : 0 ≤ K := le_trans (by norm_num : (0 : ℝ) ≤ 1) (le_max_right _ _)
      positivity))
  have hn1 : (n + 1 : ℝ) ≤ (2 * Cin + 1) * L := by
    have hnle : (n : ℝ) ≤ (N : ℝ) := by
      simpa [n, S, hNreal] using card_landauInnerDisk_le_sum_multiplicity T
    nlinarith [hnle, hNleL, hL]
  have hinvη : η⁻¹ = 32 * (n + 1 : ℝ) := by
    unfold η; field_simp
  have hlogη : Real.log η⁻¹ ≤ Real.log 32 + (n + 1 : ℝ) := by
    have hn1pos : 0 < (n + 1 : ℝ) := by positivity
    have : η⁻¹ = 32 * (n + 1 : ℝ) := hinvη
    have h32 : 0 < (32 : ℝ) := by norm_num
    rw [this, Real.log_mul (ne_of_gt h32) hn1pos.ne']
    have : Real.log (n + 1 : ℝ) ≤ (n + 1 : ℝ) - 1 :=
      Real.log_le_sub_one_of_pos hn1pos
    linarith
  have hlogηL : Real.log η⁻¹ ≤ Real.log 32 + (2 * Cin + 1) * L :=
    hlogη.trans (add_le_add_right hn1 (Real.log 32))
  have hlogMF : Real.log MF ≤
      Real.log jensenSphereMajorantCoeff + 4 * L := by
    have := log_jensenSphereMajorant_le T
    have h2 : 2 * Real.log (2 + |T|) ≤ 4 * L := by
      have : 1 + Real.log (2 + |T|) ≤ 2 * L := one_add_log_two_add_abs_le hT
      nlinarith [Real.log_nonneg (by nlinarith [abs_nonneg T] : (1 : ℝ) ≤ 2 + |T|)]
    linarith
  have hc0 : landauQuotient T c ≠ 0 :=
    landauQuotient_ne_zero_on_landau_ball
      (Metric.mem_ball_self (by norm_num : (0 : ℝ) < 13 / 8))
  have hcenter := log_norm_landauQuotient_center_ge T
  have hMsub : Real.log Cbd - Real.log ‖landauQuotient T c‖ ≤
      Real.log MF + (N : ℝ) * Real.log η⁻¹ +
        (N : ℝ) * Real.log (13 / 8 : ℝ) + Real.log ‖riemannZeta 2‖ := by
    have hclog : Real.log Cbd = Real.log MF + (N : ℝ) * Real.log η⁻¹ := by
      have hinvpos : 0 < η⁻¹ := inv_pos.mpr heta_pos
      rw [show Cbd = MF * η⁻¹ ^ N from rfl, Real.log_mul hMFpos.ne'
        (pow_ne_zero _ hinvpos.ne'), Real.log_pow]
    have hneg : -Real.log ‖landauQuotient T c‖ ≤
        (N : ℝ) * Real.log (13 / 8 : ℝ) + Real.log ‖riemannZeta 2‖ := by
      have hsum : (N : ℝ) =
          ∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ) := hNreal.trans
        (by simp [S])
      have := hcenter
      rw [← hsum] at this
      linarith [this]
    linarith [hclog, hneg]
  have hlog32n : 0 ≤ Real.log 32 :=
    (Real.log_pos (by norm_num : (1 : ℝ) < 32)).le
  have hlog138n : 0 ≤ Real.log (13 / 8 : ℝ) :=
    (Real.log_pos (by norm_num : (1 : ℝ) < 13 / 8)).le
  have hlogKn : 0 ≤ Real.log jensenSphereMajorantCoeff :=
    (Real.log_pos one_lt_jensenSphereMajorantCoeff).le
  have hlogzn : 0 ≤ Real.log ‖riemannZeta 2‖ :=
    (Real.log_pos one_lt_norm_riemannZeta_two).le
  have hPack : Real.log Cbd - Real.log ‖landauQuotient T c‖ ≤
      (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
        2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
          2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 := by
    have hη1 : (1 : ℝ) ≤ η⁻¹ := by
      rw [hinvη]
      have hn1 : (1 : ℝ) ≤ (n + 1 : ℝ) := by
        exact_mod_cast Nat.succ_le_succ (Nat.zero_le n)
      nlinarith [hn1]
    have hNη : (N : ℝ) * Real.log η⁻¹ ≤
        2 * Cin * L * (Real.log 32 + (2 * Cin + 1) * L) :=
      mul_le_mul hNleL hlogηL (Real.log_nonneg hη1)
        (mul_nonneg (mul_nonneg (by norm_num) hCin.le) hLpos.le)
    have hNηL : (N : ℝ) * Real.log η⁻¹ ≤
        (2 * Cin * Real.log 32 + 2 * Cin * (2 * Cin + 1)) * L ^ 2 := by
      have h1 : 2 * Cin * Real.log 32 * L ≤
          2 * Cin * Real.log 32 * L ^ 2 :=
        mul_le_mul_of_nonneg_left hLL
          (mul_nonneg (mul_nonneg (by norm_num) hCin.le) hlog32n)
      have hNη' : 2 * Cin * L * (Real.log 32 + (2 * Cin + 1) * L) =
          2 * Cin * Real.log 32 * L + 2 * Cin * (2 * Cin + 1) * L ^ 2 := by
        ring
      linarith [hNη, hNη', h1]
    have hN138 : (N : ℝ) * Real.log (13 / 8 : ℝ) ≤
        2 * Cin * Real.log (13 / 8 : ℝ) * L ^ 2 := by
      have h := mul_le_mul_of_nonneg_right hNleL hlog138n
      have h' : (2 * Cin * Real.log (13 / 8 : ℝ)) * L ≤
          (2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 :=
        mul_le_mul_of_nonneg_left hLL
          (mul_nonneg (mul_nonneg (by norm_num) hCin.le) hlog138n)
      have h'' : 2 * Cin * L * Real.log (13 / 8 : ℝ) =
          (2 * Cin * Real.log (13 / 8 : ℝ)) * L := by ring
      have h''' : 2 * Cin * Real.log (13 / 8 : ℝ) * L ^ 2 =
          (2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 := by ring
      exact h.trans (h''.trans_le (h'''.symm ▸ h'))
    have hMFL : Real.log MF ≤
        (Real.log jensenSphereMajorantCoeff + 4) * L ^ 2 := by
      nlinarith [hlogMF, hLL, hlogKn]
    have hz2 : Real.log ‖riemannZeta 2‖ ≤
        Real.log ‖riemannZeta 2‖ * L ^ 2 := by
      nlinarith [hLL, hlogzn]
    linarith [hMsub, hMFL, hz2, hNηL, hN138]
  have hK : K ≤ 1 +
      (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
        2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
          2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 := by
    have ha := le_max_left
      (Real.log Cbd - Real.log ‖landauQuotient T c‖) (1 : ℝ)
    have : K ≤ max
        ((Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
          2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
            2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2) (1 : ℝ) :=
      max_le_max hPack le_rfl
    have hnn : 0 ≤
        (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
          2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
            2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 := by
      have : 0 ≤ Real.log jensenSphereMajorantCoeff :=
        (Real.log_pos one_lt_jensenSphereMajorantCoeff).le
      have : 0 ≤ Real.log ‖riemannZeta 2‖ :=
        (Real.log_pos one_lt_norm_riemannZeta_two).le
      positivity
    have hmax : max
        ((Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
          2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
            2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2) (1 : ℝ) ≤
        1 +
          (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
            2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
              2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2 := by
      exact max_le (le_add_of_nonneg_left (by norm_num)) (le_add_of_nonneg_right hnn)
    exact this.trans hmax
  have hgL : ‖logDeriv (landauQuotient T) s‖ ≤
      16384 * (1 +
        (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 4 +
          2 * Cin * (Real.log 32 + (2 * Cin + 1)) +
            2 * Cin * Real.log (13 / 8 : ℝ)) * L ^ 2) := by
    have : 4 * K * 4096 = 16384 * K := by ring
    rw [this] at hgker
    exact hgker.trans (mul_le_mul_of_nonneg_left hK (by norm_num))
  have htri : ‖logDeriv riemannZeta s‖ ≤
      ‖logDeriv (landauQuotient T) s‖ +
        ‖logDeriv (landauPoly T) s‖ + ‖(1 : ℂ) / (s - 1)‖ := by
    rw [hsplit, sub_eq_add_neg]
    have h1 := norm_add_le
      (logDeriv (landauQuotient T) s + logDeriv (landauPoly T) s)
      (-(1 / (s - 1)))
    have h2 := norm_add_le
      (logDeriv (landauQuotient T) s) (logDeriv (landauPoly T) s)
    have h3 : ‖-(1 / (s - 1))‖ = ‖(1 : ℂ) / (s - 1)‖ := norm_neg _
    linarith [h1, h2, h3]
  have hsumle := htri.trans (add_le_add (add_le_add hgL hPnormL) hs1norm)
  have hfinal : ‖logDeriv riemannZeta s‖ ≤
      (A * landauHorizontalConst) * L ^ 3 := by
    have hbig := landau_cubic_pack_scale (Cin := Cin) (L := L) (A := A)
      (a := Real.log jensenSphereMajorantCoeff)
      (b := Real.log ‖riemannZeta 2‖)
      (c := Real.log 32)
      (d := Real.log (13 / 8 : ℝ))
      hA hCin.le hL hlogKn hlogzn hlog32n hlog138n
    have hconst : A * landauHorizontalConst * L ^ 3 =
        A * (100000000 * (1 + Cin) ^ 3 *
          (1 + Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ +
            Real.log 32 + Real.log (13 / 8) + 4) * L ^ 3) := by
      simp [landauHorizontalConst, Cin]; ring
    exact hsumle.trans (hbig.trans_eq hconst.symm)
  simpa [s, L] using hfinal

theorem horizontalEdgeLandauBound : HorizontalEdgeLandauBound :=
  ⟨(1 : ℝ), landauHorizontalConst, by norm_num, landauHorizontalConst_pos,
    fun {T} hT hgap σ hσ1 hσ2 => by
      simpa using horizontalEdgeLandauBound_of_gap (A := (1 : ℝ))
        le_rfl hT hgap hσ1 hσ2⟩

lemma horizontalEdgeLandauBound_landauGap {T : ℝ}
    (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (ordinateGapConstLandau * (1 + Real.log T)) ≤ |ρ.im - T|)
    {σ : ℝ} (hσ1 : (1 / 2 : ℝ) ≤ σ) (hσ2 : σ ≤ 2) :
    ‖logDeriv riemannZeta (σ + T * I)‖ ≤
      (ordinateGapConstLandau * landauHorizontalConst) *
        (1 + Real.log T) ^ 3 :=
  horizontalEdgeLandauBound_of_gap ordinateGapConstLandau_one_le hT hgap hσ1 hσ2

lemma digamma_add_nat {z : ℂ} (hz : ∀ m : ℕ, z ≠ -m) (n : ℕ) :
    digamma (z + n) = digamma z + ∑ k ∈ Finset.range n, (z + k)⁻¹ := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hzn : ∀ m : ℕ, (z + n : ℂ) ≠ -m := by
      intro m hm
      apply hz (n + m)
      have hadd : z + ((n + m : ℕ) : ℂ) = 0 := by
        have : z + n + m = 0 := by
          rw [hm]; simp
        simpa [add_assoc, Nat.cast_add] using this
      exact add_eq_zero_iff_eq_neg.mp hadd
    have hstep := digamma_apply_add_one (z + n) hzn
    have hcast : (z + (n + 1 : ℕ) : ℂ) = z + n + 1 := by
      simp [Nat.cast_succ]; ring
    rw [hcast, hstep, ih, Finset.sum_range_succ]
    abel

lemma norm_inv_sub_inv {a b : ℂ} (ha : a ≠ 0) (hb : b ≠ 0) :
    ‖a⁻¹ - b⁻¹‖ = ‖a - b‖ / (‖a‖ * ‖b‖) := by
  have : a⁻¹ - b⁻¹ = (b - a) / (a * b) := by field_simp [ha, hb]
  rw [this, norm_div, norm_mul, norm_sub_rev]

lemma digamma_kernel_term_norm_le {z : ℂ} {n : ℕ}
    (hne : (n : ℂ) + z ≠ 0) :
    ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
      ‖z - 1‖ / ((n + 1 : ℝ) * ‖(n : ℂ) + z‖) := by
  have ha : (n + 1 : ℂ) ≠ 0 := by
    exact_mod_cast (Nat.succ_ne_zero n)
  have h := norm_inv_sub_inv ha hne
  have hnum : ‖(n + 1 : ℂ) - ((n : ℂ) + z)‖ = ‖z - 1‖ := by
    have : (n + 1 : ℂ) - ((n : ℂ) + z) = 1 - z := by
      ring
    rw [this, norm_sub_rev]
  have hden : ‖(n + 1 : ℂ)‖ = (n + 1 : ℝ) := by
    have hcast : (n + 1 : ℂ) = ((n + 1 : ℕ) : ℂ) := by
      simp [Nat.cast_succ]
    rw [hcast, Complex.norm_natCast]
    exact_mod_cast rfl
  rw [h, hnum, hden]

lemma log_one_add_ge_div {x : ℝ} (hx : 0 ≤ x) :
    x / (1 + x) ≤ Real.log (1 + x) := by
  have hx1 : 0 < 1 + x := by linarith
  have hy : 0 < (1 : ℝ) / (1 + x) := one_div_pos.mpr hx1
  have h := Real.log_le_sub_one_of_pos hy
  have hlog : Real.log ((1 : ℝ) / (1 + x)) = -Real.log (1 + x) := by
    rw [Real.log_div (by norm_num) hx1.ne', Real.log_one, zero_sub]
  have hsub : (1 : ℝ) / (1 + x) - 1 = -(x / (1 + x)) := by
    field_simp; ring
  linarith

lemma inv_succ_le_log_sub {k : ℕ} (hk : 0 < k) :
    (1 : ℝ) / (k + 1) ≤ Real.log (k + 1) - Real.log k := by
  have hx : 0 < (k : ℝ) := Nat.cast_pos.mpr hk
  have h := log_one_add_ge_div (x := (1 : ℝ) / k) (div_nonneg zero_le_one hx.le)
  have hid : ((1 : ℝ) / k) / (1 + 1 / k) = 1 / (k + 1) := by field_simp
  have hlog : Real.log (1 + 1 / k) = Real.log (k + 1) - Real.log k := by
    have : (1 : ℝ) + 1 / k = (k + 1) / k := by field_simp
    rw [this, Real.log_div (by positivity) hx.ne']
  rw [← hid, ← hlog]
  exact h

lemma sum_range_inv_succ_le_one_add_log (n : ℕ) :
    ∑ k ∈ Finset.range n, (1 : ℝ) / ((k : ℝ) + 1) ≤
      1 + Real.log ((n : ℝ) + 1) := by
  cases n with
  | zero => simp
  | succ n =>
    have h : ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / ((k : ℝ) + 1) ≤
        1 + Real.log ((n : ℝ) + 1) := by
      induction n with
      | zero => simp
      | succ n ih =>
        rw [Finset.sum_range_succ]
        have hstep := inv_succ_le_log_sub (k := n + 1) (Nat.succ_pos _)
        have hn : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := Nat.cast_succ n
        have hstep' : (1 : ℝ) / ((n : ℝ) + 1 + 1) ≤
            Real.log ((n : ℝ) + 1 + 1) - Real.log ((n : ℝ) + 1) := by
          simpa [hn] using hstep
        have hsum := add_le_add ih hstep'
        have hsum' : ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / ((k : ℝ) + 1)
            + (1 : ℝ) / ((n : ℝ) + 1 + 1)
            ≤ 1 + Real.log ((n : ℝ) + 1 + 1) := by
          convert hsum using 1
          ring
        simpa [hn] using hsum'
    have hn : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := Nat.cast_succ n
    have hlog : Real.log ((n : ℝ) + 1) ≤ Real.log (((n + 1 : ℕ) : ℝ) + 1) := by
      refine Real.log_le_log (by positivity) ?_
      linarith
    exact h.trans (add_le_add_right hlog 1)

lemma norm_nat_add_z_ge_im (n : ℕ) (z : ℂ) :
    |z.im| ≤ ‖(n : ℂ) + z‖ := by
  have : ((n : ℂ) + z).im = z.im := by simp
  simpa [this] using abs_im_le_norm ((n : ℂ) + z)

/-- r523 working lemma, n-le-T half: each Weierstrass term is
  bounded by ‖z-1‖/((n+1)|Im z|) via ‖n+z‖.
The harmonic sum supplies the log. -/
lemma sum_digamma_kernel_norm_le {z : ℂ} {N : ℕ} {T : ℝ}
    (hT : (2 : ℝ) ≤ T) (hIm : T ≤ |z.im|)
    (hne : ∀ n : ℕ, (n : ℂ) + z ≠ 0) :
    ∑ n ∈ Finset.range N,
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        ‖z - 1‖ / T * (1 + Real.log ((N : ℝ) + 1)) := by
  have hTpos : 0 < T := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) hT
  have hz1 : 0 ≤ ‖z - 1‖ := norm_nonneg _
  have hterm : ∀ n : ℕ,
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        ‖z - 1‖ / ((n + 1 : ℝ) * T) := by
    intro n
    have ht := digamma_kernel_term_norm_le (hne n)
    have hge : T ≤ ‖(n : ℂ) + z‖ :=
      hIm.trans (norm_nat_add_z_ge_im n z)
    have hden : 0 < (n + 1 : ℝ) := by positivity
    exact ht.trans (div_le_div_of_nonneg_left hz1 (mul_pos hden hTpos)
      (mul_le_mul_of_nonneg_left hge hden.le))
  have hle := Finset.sum_le_sum (s := Finset.range N) fun n _ => hterm n
  have hfactor : ∑ n ∈ Finset.range N,
      ‖z - 1‖ / ((n + 1 : ℝ) * T) =
    (‖z - 1‖ / T) * ∑ n ∈ Finset.range N, (1 : ℝ) / ((n : ℝ) + 1) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl ?_
    intro n _; field_simp
  have hH := sum_range_inv_succ_le_one_add_log N
  exact hle.trans (hfactor.trans_le
    (mul_le_mul_of_nonneg_left hH (div_nonneg hz1 hTpos.le)))

lemma sum_Ico_inv_telescope {N M : ℕ} (hN : 0 < N) (hNM : N ≤ M) :
    ∑ n ∈ Finset.Ico N M, ((1 : ℝ) / (n : ℝ) - 1 / ((n : ℝ) + 1)) =
      (1 : ℝ) / N - 1 / M := by
  induction M, hNM using Nat.le_induction with
  | base => simp
  | succ M hNM ih =>
    rw [Finset.sum_Ico_succ_top hNM, ih, Nat.cast_succ]
    ring

lemma norm_nat_add_ge_sub (n : ℕ) (z : ℂ) :
    (n : ℝ) - ‖z‖ ≤ ‖(n : ℂ) + z‖ := by
  have h := norm_sub_le ((n : ℂ) + z) z
  have hn : ‖(n : ℂ)‖ = (n : ℝ) := Complex.norm_natCast n
  have : (n : ℝ) ≤ ‖(n : ℂ) + z‖ + ‖z‖ := by
    simpa [hn, add_sub_cancel_right] using h
  linarith

/-- r524 n>T half: for `n ≥ N` and `2‖z‖ ≤ N`, each Weierstrass
term is `O(1/n²)`; the telescope `Σ 1/(n(n+1)) = 1/N - 1/M`. -/
lemma sum_digamma_kernel_tail_le {z : ℂ} {N M : ℕ}
    (hN : 0 < N) (hNM : N ≤ M)
    (hne : ∀ n : ℕ, (n : ℂ) + z ≠ 0)
    (hz : (2 : ℝ) * ‖z‖ ≤ N) :
    ∑ n ∈ Finset.Ico N M,
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        (2 : ℝ) * ‖z - 1‖ / N := by
  have hz1 : 0 ≤ ‖z - 1‖ := norm_nonneg _
  have hNpos : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hzN : ‖z‖ ≤ (N : ℝ) / 2 :=
    (le_div_iff₀ (by norm_num : (0 : ℝ) < 2)).mpr (by simpa [mul_comm] using hz)
  have hterm : ∀ n ∈ Finset.Ico N M,
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / n - 1 / ((n : ℝ) + 1)) := by
    intro n hn
    have hnN : N ≤ n := (Finset.mem_Ico.mp hn).1
    have hn1 : (1 : ℝ) ≤ (n : ℝ) := by
      exact_mod_cast (Nat.succ_le_of_lt (lt_of_lt_of_le hN hnN))
    have hge : (n : ℝ) / 2 ≤ ‖(n : ℂ) + z‖ := by
      have hsub : (n : ℝ) - ‖z‖ ≤ ‖(n : ℂ) + z‖ := norm_nat_add_ge_sub n z
      have : (n : ℝ) / 2 ≤ (n : ℝ) - ‖z‖ := by
        have hNle : (N : ℝ) ≤ n := Nat.cast_le.mpr hnN
        nlinarith [hzN, hNle]
      exact this.trans hsub
    have ht := digamma_kernel_term_norm_le (hne n)
    have hden : 0 < (n + 1 : ℝ) := by positivity
    have hnhalf : 0 < (n : ℝ) / 2 := by positivity
    have hle := ht.trans (div_le_div_of_nonneg_left hz1
      (mul_pos hden hnhalf)
      (mul_le_mul_of_nonneg_left hge hden.le))
    have hid : ‖z - 1‖ / ((n + 1 : ℝ) * ((n : ℝ) / 2)) =
        (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / n - 1 / ((n : ℝ) + 1)) := by
      have hn0 : (n : ℝ) ≠ 0 := ne_of_gt (lt_of_lt_of_le zero_lt_one hn1)
      field_simp [hn0]
      ring
    exact hle.trans_eq hid
  have hsum := Finset.sum_le_sum hterm
  have htel := sum_Ico_inv_telescope hN hNM
  have hfactor :
      ∑ n ∈ Finset.Ico N M,
          (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / n - 1 / ((n : ℝ) + 1)) =
        (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / N - 1 / M) := by
    rw [← Finset.mul_sum, htel]
  have htail : (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / N - 1 / M) ≤
      (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / N) := by
    have hM : (0 : ℝ) ≤ (1 : ℝ) / M := div_nonneg zero_le_one (Nat.cast_nonneg _)
    have : (1 : ℝ) / N - 1 / M ≤ (1 : ℝ) / N := sub_le_self _ hM
    exact mul_le_mul_of_nonneg_left this (mul_nonneg (by norm_num) hz1)
  have hdiv : (2 : ℝ) * ‖z - 1‖ * ((1 : ℝ) / N) = (2 : ℝ) * ‖z - 1‖ / N := by
    field_simp
  exact hsum.trans (hfactor.trans_le (htail.trans_eq hdiv))

/-- Positive reals are never non-positive integers, as complex
values.  Uses `congrArg re`, not `exact_mod_cast`. -/
lemma ofReal_ne_neg_nat {x : ℝ} (hx : 0 < x) (m : ℕ) :
    (x : ℂ) ≠ -m := by
  intro h
  have hre : x = -(m : ℝ) := by
    simpa using congrArg Complex.re h
  have hneg : -(m : ℝ) ≤ 0 := neg_nonpos.mpr (Nat.cast_nonneg _)
  linarith

lemma pos_ne_neg_nat {x : ℝ} (hx : 0 < x) (m : ℕ) : x ≠ -m := by
  intro h
  have hneg : -(m : ℝ) ≤ 0 := neg_nonpos.mpr (Nat.cast_nonneg _)
  linarith

/-- r526 bridge: `deriv (Real.log ∘ Real.Gamma) x = (digamma ↑x).re`
for `x > 0`.  Route: `HasDerivAt.real_of_complex` on
`Complex.Gamma`, `Real.Gamma t = (Complex.Gamma ↑t).re`, then
`congrArg re` on `ψ = Γ'/Γ` and `div_ofReal_re` (the quotient of
two via-real values).  Not `exact_mod_cast`. -/
lemma hasDerivAt_re_Gamma_ofReal {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun t : ℝ => Real.log (Real.Gamma t))
      (digamma (x : ℂ)).re x := by
  have hG : DifferentiableAt ℂ Gamma (x : ℂ) :=
    differentiableAt_Gamma _ (ofReal_ne_neg_nat hx)
  have hreG : HasDerivAt (fun t : ℝ => (Gamma t).re)
      (deriv Gamma (x : ℂ)).re x :=
    hG.hasDerivAt.real_of_complex
  have hGreal : HasDerivAt Real.Gamma (deriv Gamma (x : ℂ)).re x :=
    hreG
  have hpos : 0 < Real.Gamma x := Real.Gamma_pos_of_pos hx
  have hlog : HasDerivAt (fun t : ℝ => Real.log (Real.Gamma t))
      ((deriv Gamma (x : ℂ)).re / Real.Gamma x) x :=
    hGreal.log hpos.ne'
  have hψ : (digamma (x : ℂ)).re =
      (deriv Gamma (x : ℂ)).re / Real.Gamma x := by
    have hlogD : digamma (x : ℂ) =
        deriv Gamma (x : ℂ) / Gamma (x : ℂ) := by
      rw [digamma_def, logDeriv_apply]
    have hre := congrArg Complex.re hlogD
    rw [Gamma_ofReal, div_ofReal_re] at hre
    exact hre
  exact hlog.congr_deriv hψ.symm

lemma deriv_Gamma_ofReal {x : ℝ} (hx : 0 < x) :
    deriv Gamma (x : ℂ) = ↑(deriv (fun t : ℝ => Real.Gamma t) x) := by
  have hC : HasDerivAt (fun t : ℝ => Gamma (t : ℂ))
      (deriv Gamma (x : ℂ)) x :=
    (differentiableAt_Gamma _ (ofReal_ne_neg_nat hx)).hasDerivAt.comp_ofReal
  have hR0 : HasDerivAt Real.Gamma
      (deriv (fun t : ℝ => Real.Gamma t) x) x :=
    (Real.differentiableAt_Gamma (pos_ne_neg_nat hx)).hasDerivAt
  have hR : HasDerivAt (fun t : ℝ => (Real.Gamma t : ℂ))
      ↑(deriv (fun t : ℝ => Real.Gamma t) x) x :=
    hR0.ofReal_comp
  have hC' : HasDerivAt (fun t : ℝ => (Real.Gamma t : ℂ))
      (deriv Gamma (x : ℂ)) x :=
    hC.congr_of_eventuallyEq
      (Eventually.of_forall fun t => (Gamma_ofReal t).symm)
  exact HasDerivAt.unique hC' hR

/-- On `(0, ∞)` the complex digamma is real-valued. -/
lemma digamma_ofReal {x : ℝ} (hx : 0 < x) :
    digamma (x : ℂ) = ↑((digamma (x : ℂ)).re) := by
  have hdiv : digamma (x : ℂ) =
      deriv Gamma (x : ℂ) / Gamma (x : ℂ) := by
    rw [digamma_def, logDeriv_apply]
  have hre : (digamma (x : ℂ)).re =
      deriv (fun t : ℝ => Real.Gamma t) x / Real.Gamma x := by
    have hlog := (hasDerivAt_re_Gamma_ofReal hx).deriv
    have hG := (Real.differentiableAt_Gamma (pos_ne_neg_nat hx)).hasDerivAt
    have hlog' := (hG.log (Real.Gamma_pos_of_pos hx).ne').deriv
    exact hlog.symm.trans hlog'
  calc
    digamma (x : ℂ) = deriv Gamma (x : ℂ) / Gamma (x : ℂ) := hdiv
    _ = ↑(deriv (fun t : ℝ => Real.Gamma t) x) / ↑(Real.Gamma x) := by
        rw [deriv_Gamma_ofReal hx, Gamma_ofReal]
    _ = ↑(deriv (fun t : ℝ => Real.Gamma t) x / Real.Gamma x) :=
        (ofReal_div _ _).symm
    _ = ↑((digamma (x : ℂ)).re) := by rw [hre]

lemma monotoneOn_log_Gamma_deriv :
    MonotoneOn (deriv (fun t : ℝ => Real.log (Real.Gamma t))) (Ioi 0) :=
  Real.convexOn_log_Gamma.monotoneOn_deriv fun _t ht =>
    (Real.differentiableAt_Gamma
        (pos_ne_neg_nat (mem_Ioi.mp ht))).log
      (Real.Gamma_pos_of_pos (mem_Ioi.mp ht)).ne'

lemma monotoneOn_re_digamma :
    MonotoneOn (fun t : ℝ => (digamma (t : ℂ)).re) (Ioi 0) := by
  intro a ha b hb hab
  have h := monotoneOn_log_Gamma_deriv ha hb hab
  have ha' := (hasDerivAt_re_Gamma_ofReal (mem_Ioi.mp ha)).deriv
  have hb' := (hasDerivAt_re_Gamma_ofReal (mem_Ioi.mp hb)).deriv
  rwa [ha', hb'] at h

lemma re_digamma_add_nat {x : ℝ} (hx : 0 < x) (n : ℕ) :
    (digamma ((x : ℂ) + n)).re =
      (digamma (x : ℂ)).re + ∑ k ∈ Finset.range n, (x + k)⁻¹ := by
  have hz : ∀ m : ℕ, (x : ℂ) ≠ -m := ofReal_ne_neg_nat hx
  rw [digamma_add_nat hz n, add_re, re_sum]
  refine congrArg _ (Finset.sum_congr rfl fun k _ => ?_)
  have hxk : 0 < x + (k : ℝ) := by positivity
  have : ((x : ℂ) + k)⁻¹ = ↑((x + k)⁻¹ : ℝ) := by
    rw [← ofReal_natCast k, ← ofReal_add, ofReal_inv]
  rw [this, ofReal_re]

lemma re_digamma_nat_succ (n : ℕ) :
    (digamma ((n + 1 : ℕ) : ℂ)).re =
      -Real.eulerMascheroniConstant +
        ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) := by
  have h1 : (1 : ℝ) > 0 := by norm_num
  have hcast : ((n + 1 : ℕ) : ℂ) = (1 : ℂ) + n := by
    rw [Nat.cast_succ, add_comm]
  have hre := re_digamma_add_nat h1 n
  have hψ1 : (digamma (1 : ℂ)).re = -Real.eulerMascheroniConstant := by
    rw [digamma_one, neg_re, ofReal_re]
  have hsum : ∑ k ∈ Finset.range n, ((1 : ℝ) + k)⁻¹ =
      ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) := by
    refine Finset.sum_congr rfl fun k _ => ?_
    field_simp
    ring
  simpa [hcast, hψ1, hsum] using hre

lemma summable_one_div_succ_sq :
    Summable fun n : ℕ => (1 : ℝ) / ((n + 1 : ℝ) ^ 2) := by
  have h := (Real.summable_one_div_nat_add_rpow (1 : ℝ) 2).mpr
    (by norm_num : (1 : ℝ) < 2)
  convert h using 1
  ext n
  have hn : 0 < (n + 1 : ℝ) := by positivity
  rw [abs_of_pos hn, Real.rpow_two]

lemma summable_digamma_kernel_real {x : ℝ} (hx1 : 1 < x) (_hx2 : x < 2) :
    Summable fun n : ℕ => (1 : ℝ) / (n + 1) - 1 / (n + x) := by
  refine Summable.of_norm_bounded summable_one_div_succ_sq fun n => ?_
  have hx0 : 0 < x := lt_trans (by norm_num : (0 : ℝ) < 1) hx1
  have hden : 0 < (n + 1 : ℝ) := by positivity
  have hdenx : 0 < (n : ℝ) + x := by positivity
  have hterm : (1 : ℝ) / (n + 1) - 1 / (n + x) =
      (x - 1) / ((n + 1) * (n + x)) := by
    field_simp
    ring
  have hnn : ‖(1 : ℝ) / (n + 1) - 1 / (n + x)‖ =
      |x - 1| / ((n + 1) * (n + x)) := by
    rw [hterm, Real.norm_eq_abs, abs_div, abs_mul, abs_of_pos hden,
      abs_of_pos hdenx]
  have hx1abs : |x - 1| = x - 1 := abs_of_pos (sub_pos.mpr hx1)
  have hle : (x - 1) / ((n + 1) * (n + x)) ≤
      (1 : ℝ) / ((n + 1) ^ 2) := by
    have hnum : x - 1 ≤ 1 := by linarith
    have hdenle : (n + 1 : ℝ) ^ 2 ≤ (n + 1) * (n + x) := by
      have : (n + 1 : ℝ) ≤ n + x := by linarith
      nlinarith
    have hpos : 0 < (n + 1 : ℝ) ^ 2 := by positivity
    rw [div_le_div_iff₀ (mul_pos hden hdenx) hpos]
    nlinarith [sq_nonneg (n + 1 : ℝ)]
  rw [hnn, hx1abs]
  simpa [Real.norm_eq_abs, abs_of_nonneg (div_nonneg (sq_nonneg _) hden.le)]
    using hle

lemma sandwich_partial_digamma_kernel {x : ℝ} (hx1 : 1 < x) (hx2 : x < 2)
    (n : ℕ) :
    0 ≤ (digamma (x : ℂ)).re + Real.eulerMascheroniConstant -
        ∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)) ∧
    (digamma (x : ℂ)).re + Real.eulerMascheroniConstant -
        ∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)) ≤
      (1 : ℝ) / (n + 1) := by
  have hx0 : 0 < x := lt_trans (by norm_num : (0 : ℝ) < 1) hx1
  have hmono := monotoneOn_re_digamma
  have hn1 : (n + 1 : ℝ) ∈ Ioi (0 : ℝ) := mem_Ioi.mpr (by positivity)
  have hxn : x + n ∈ Ioi (0 : ℝ) := mem_Ioi.mpr (by positivity)
  have hn2 : (n + 2 : ℝ) ∈ Ioi (0 : ℝ) := mem_Ioi.mpr (by positivity)
  have hlo : (n + 1 : ℝ) ≤ x + n := by linarith
  have hhi : x + n ≤ (n + 2 : ℝ) := by linarith
  have hle1 := hmono hn1 hxn hlo
  have hle2 := hmono hxn hn2 hhi
  have hψn1 : (digamma ((n + 1 : ℝ) : ℂ)).re =
      -Real.eulerMascheroniConstant +
        ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) := by
    have hcast : ((n + 1 : ℝ) : ℂ) = ((n + 1 : ℕ) : ℂ) := by
      norm_cast
    rw [hcast, re_digamma_nat_succ]
  have hsum1 : ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / (k + 1) =
      ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) + 1 / (n + 1) :=
    Finset.sum_range_succ _ n
  have hψn2 : (digamma ((n + 2 : ℝ) : ℂ)).re =
      -Real.eulerMascheroniConstant +
        (∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) + 1 / (n + 1)) := by
    have hcast : ((n + 2 : ℝ) : ℂ) = ((n + 1 + 1 : ℕ) : ℂ) := by
      norm_cast
    rw [hcast, re_digamma_nat_succ (n + 1), hsum1]
  have hψxn : (digamma ((x + n : ℝ) : ℂ)).re =
      (digamma (x : ℂ)).re + ∑ k ∈ Finset.range n, (x + k)⁻¹ := by
    have hcast : ((x + n : ℝ) : ℂ) = (x : ℂ) + n := by
      rw [ofReal_add, ofReal_natCast]
    rw [hcast, re_digamma_add_nat hx0 n]
  have hleft : -Real.eulerMascheroniConstant +
        ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) ≤
      (digamma (x : ℂ)).re + ∑ k ∈ Finset.range n, (x + k)⁻¹ := by
    have h : (digamma ((n + 1 : ℝ) : ℂ)).re ≤
        (digamma ((x + n : ℝ) : ℂ)).re := hle1
    rwa [hψn1, hψxn] at h
  have hright :
      (digamma (x : ℂ)).re + ∑ k ∈ Finset.range n, (x + k)⁻¹ ≤
        -Real.eulerMascheroniConstant +
          (∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) + 1 / (n + 1)) := by
    have h : (digamma ((x + n : ℝ) : ℂ)).re ≤
        (digamma ((n + 2 : ℝ) : ℂ)).re := hle2
    rwa [hψxn, hψn2] at h
  have hdiff :
      ∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)) =
        ∑ k ∈ Finset.range n, (1 : ℝ) / (k + 1) -
          ∑ k ∈ Finset.range n, (x + k)⁻¹ := by
    simp_rw [sub_eq_add_neg, Finset.sum_add_distrib, Finset.sum_neg_distrib]
    congr 2
    refine Finset.sum_congr rfl fun k _ => ?_
    simp [add_comm]
  constructor
  · linarith [hleft, hdiff]
  · linarith [hright, hdiff]

lemma tendsto_partial_digamma_kernel_real {x : ℝ}
    (hx1 : 1 < x) (hx2 : x < 2) :
    Tendsto (fun n : ℕ =>
        ∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)))
      atTop (𝓝 ((digamma (x : ℂ)).re + Real.eulerMascheroniConstant)) := by
  set L := (digamma (x : ℂ)).re + Real.eulerMascheroniConstant
  have hbound : ∀ n : ℕ,
      |∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)) - L| ≤
        (1 : ℝ) / (n + 1) := by
    intro n
    obtain ⟨h0, h1⟩ := sandwich_partial_digamma_kernel hx1 hx2 n
    have : 0 ≤ L - ∑ k ∈ Finset.range n,
        ((1 : ℝ) / (k + 1) - 1 / (k + x)) := by
      simpa [L, sub_eq_add_neg, add_comm, add_left_comm, add_assoc] using h0
    have hle : L - ∑ k ∈ Finset.range n,
        ((1 : ℝ) / (k + 1) - 1 / (k + x)) ≤ (1 : ℝ) / (n + 1) := by
      simpa [L, sub_eq_add_neg, add_comm, add_left_comm, add_assoc] using h1
    rw [abs_sub_comm]
    exact abs_le.mpr ⟨by linarith, by linarith⟩
  have hsqueeze :
      Tendsto (fun n : ℕ =>
        |∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x)) - L|)
        atTop (𝓝 0) := by
    refine squeeze_zero (fun _ => abs_nonneg _) hbound ?_
    exact (tendsto_const_nhds (x := (1 : ℝ))).div_atTop
      ((tendsto_natCast_atTop_atTop.comp (tendsto_add_atTop_nat 1)).congr
        fun n => Nat.cast_succ n)
  exact tendsto_iff_dist_tendsto_zero.mpr
    (hsqueeze.congr fun n =>
      (Real.dist_eq
        (∑ k ∈ Finset.range n, ((1 : ℝ) / (k + 1) - 1 / (k + x))) L).symm)

lemma re_digamma_weierstrass_Ioo {x : ℝ} (hx1 : 1 < x) (hx2 : x < 2) :
    (digamma (x : ℂ)).re = -Real.eulerMascheroniConstant +
      ∑' n : ℕ, ((1 : ℝ) / (n + 1) - 1 / (n + x)) := by
  have hf : ∀ n : ℕ, 0 ≤ (1 : ℝ) / (n + 1) - 1 / (n + x) := by
    intro n
    have : (n + 1 : ℝ) ≤ n + x := by linarith
    exact sub_nonneg.mpr (one_div_le_one_div_of_le (by positivity) this)
  have hsum :
      HasSum (fun n : ℕ => (1 : ℝ) / (n + 1) - 1 / (n + x))
        ((digamma (x : ℂ)).re + Real.eulerMascheroniConstant) :=
    (hasSum_iff_tendsto_nat_of_nonneg hf _).2
      (tendsto_partial_digamma_kernel_real hx1 hx2)
  linarith [hsum.tsum_eq]

lemma ofReal_digamma_kernel {x : ℝ} {n : ℕ} (hx : 0 < x) :
    ↑((1 : ℝ) / (n + 1) - 1 / (n + x)) =
      ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + x)⁻¹) := by
  have hn : (n + 1 : ℝ) ≠ 0 := by positivity
  have hxk : (n : ℝ) + x ≠ 0 := by positivity
  rw [ofReal_sub, ofReal_div, ofReal_one, ofReal_div, ofReal_one,
    ofReal_add, ofReal_natCast, ofReal_add, ofReal_natCast]
  simp [add_comm]

lemma digamma_eq_weierstrass_ofReal_Ioo {x : ℝ} (hx1 : 1 < x) (hx2 : x < 2) :
    digamma (x : ℂ) = -(Real.eulerMascheroniConstant : ℂ) +
      ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + x)⁻¹) := by
  have hx0 : 0 < x := lt_trans (by norm_num : (0 : ℝ) < 1) hx1
  have hre := re_digamma_weierstrass_Ioo hx1 hx2
  have hreal := digamma_ofReal hx0
  have hterm : ∀ n : ℕ,
      ↑((1 : ℝ) / (n + 1) - 1 / (n + x)) =
        ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + x)⁻¹) :=
    fun n => ofReal_digamma_kernel hx0
  calc
    digamma (x : ℂ) = ↑((digamma (x : ℂ)).re) := hreal
    _ = ↑(-Real.eulerMascheroniConstant +
          ∑' n : ℕ, ((1 : ℝ) / (n + 1) - 1 / (n + x))) := by
        rw [hre]
    _ = -(Real.eulerMascheroniConstant : ℂ) +
          ↑(∑' n : ℕ, ((1 : ℝ) / (n + 1) - 1 / (n + x))) := by
        rw [ofReal_add, ofReal_neg]
    _ = -(Real.eulerMascheroniConstant : ℂ) +
          ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + x)⁻¹) := by
        rw [ofReal_tsum]
        exact congrArg _ (tsum_congr hterm)

def digammaStrip : Set ℂ :=
  {z | (1 / 4 : ℝ) < z.re ∧ z.re < (2 : ℝ)}

lemma isOpen_digammaStrip : IsOpen digammaStrip :=
  (isOpen_lt continuous_const continuous_re).inter
    (isOpen_lt continuous_re continuous_const)

lemma isPreconnected_digammaStrip : IsPreconnected digammaStrip :=
  ((convex_halfSpace_re_gt (1 / 4 : ℝ)).inter
    (convex_halfSpace_re_lt (2 : ℝ))).isPreconnected

lemma mem_digammaStrip_ne_neg_nat {z : ℂ} (hz : z ∈ digammaStrip)
    (m : ℕ) : z ≠ -m := by
  intro h
  have hre : z.re = -(m : ℝ) := by simp [h]
  have hstrip : (1 / 4 : ℝ) < z.re := hz.1
  have hnonpos : z.re ≤ (0 : ℝ) := by
    rw [hre]
    exact neg_nonpos.mpr (show (0 : ℝ) ≤ (m : ℝ) from Nat.cast_nonneg m)
  linarith

lemma nat_add_ne_zero_of_mem_digammaStrip {z : ℂ} (hz : z ∈ digammaStrip)
    (n : ℕ) : (n : ℂ) + z ≠ 0 := by
  intro h
  have : (n : ℝ) + z.re = 0 := by
    simpa [add_re, natCast_re] using congrArg Complex.re h
  have hstrip : (1 / 4 : ℝ) < z.re := hz.1
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  linarith

lemma analyticAt_Gamma_of_mem_digammaStrip {z : ℂ} (hz : z ∈ digammaStrip) :
    AnalyticAt ℂ Gamma z :=
  (DifferentiableOn.analyticOnNhd
      (fun w hw => (differentiableAt_Gamma w
        (mem_digammaStrip_ne_neg_nat hw)).differentiableWithinAt)
      isOpen_digammaStrip)
    z hz

lemma analyticAt_digamma_of_mem_digammaStrip {z : ℂ} (hz : z ∈ digammaStrip) :
    AnalyticAt ℂ digamma z :=
  (analyticAt_Gamma_of_mem_digammaStrip hz).deriv.div
    (analyticAt_Gamma_of_mem_digammaStrip hz)
    (Complex.Gamma_ne_zero_of_re_pos
      (lt_trans (by norm_num : (0 : ℝ) < 1 / 4) hz.1))

lemma analyticOnNhd_digamma_strip : AnalyticOnNhd ℂ digamma digammaStrip :=
  fun z hz => analyticAt_digamma_of_mem_digammaStrip hz

lemma digamma_kernel_term_norm_le_strip {z : ℂ} {n : ℕ}
    (hz : z ∈ digammaStrip) :
    ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
      4 * ‖z - 1‖ / ((n + 1 : ℝ) ^ 2) := by
  have hne := nat_add_ne_zero_of_mem_digammaStrip hz n
  have ht := digamma_kernel_term_norm_le hne
  have hn0 : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hstrip : (1 / 4 : ℝ) < z.re := hz.1
  have hre : (n : ℝ) + (1 / 4 : ℝ) ≤ ‖(n : ℂ) + z‖ := by
    have habs : |((n : ℂ) + z).re| ≤ ‖(n : ℂ) + z‖ := abs_re_le_norm _
    have hreval : ((n : ℂ) + z).re = n + z.re := by simp
    have hpos : (0 : ℝ) ≤ n + z.re := by linarith
    have : n + z.re ≤ ‖(n : ℂ) + z‖ := by
      simpa [hreval, abs_of_nonneg hpos] using habs
    linarith
  have hden : 0 < (n + 1 : ℝ) := by positivity
  have hquarter : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hle := ht.trans (div_le_div_of_nonneg_left (norm_nonneg (z - 1))
    (mul_pos hden hquarter)
    (mul_le_mul_of_nonneg_left hre hden.le))
  have hfinal : ‖z - 1‖ / ((n + 1 : ℝ) * (n + 1 / 4)) ≤
      4 * ‖z - 1‖ / ((n + 1 : ℝ) ^ 2) := by
    have hpos : 0 < (n + 1 : ℝ) ^ 2 := by positivity
    have hpos' : 0 < (n + 1 : ℝ) * (n + 1 / 4) := by positivity
    rw [div_le_div_iff₀ hpos' hpos]
    have hcoeff : (n + 1 : ℝ) ≤ 4 * (n + 1 / 4) := by linarith
    have hnn : 0 ≤ ‖z - 1‖ := norm_nonneg _
    have hn1 : 0 ≤ (n + 1 : ℝ) := hden.le
    calc
      ‖z - 1‖ * (n + 1) ^ 2
          = ‖z - 1‖ * (n + 1) * (n + 1) := by ring
      _ ≤ ‖z - 1‖ * (n + 1) * (4 * (n + 1 / 4)) :=
          mul_le_mul_of_nonneg_left hcoeff (mul_nonneg hnn hn1)
      _ = 4 * ‖z - 1‖ * ((n + 1) * (n + 1 / 4)) := by ring
  exact hle.trans hfinal

lemma summable_digamma_kernel {z : ℂ} (hz : z ∈ digammaStrip) :
    Summable fun n : ℕ => ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹) :=
  Summable.of_norm_bounded
    (summable_one_div_succ_sq.mul_left (4 * ‖z - 1‖)) fun n => by
      simpa [div_eq_mul_inv, mul_comm, mul_left_comm, mul_assoc]
        using digamma_kernel_term_norm_le_strip (n := n) hz

lemma differentiableOn_digamma_kernel (n : ℕ) :
    DifferentiableOn ℂ (fun z => ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹))
      digammaStrip := by
  intro z hz
  have hconst : DifferentiableAt ℂ (fun _ : ℂ => ((n + 1 : ℂ)⁻¹)) z :=
    differentiableAt_const _
  have hadd : DifferentiableAt ℂ (fun w : ℂ => (n : ℂ) + w) z :=
    differentiableAt_const (n : ℂ) |>.add differentiableAt_id
  have hinv : DifferentiableAt ℂ (fun w : ℂ => ((n : ℂ) + w)⁻¹) z :=
    hadd.inv (nat_add_ne_zero_of_mem_digammaStrip hz n)
  exact (hconst.sub hinv).differentiableWithinAt

lemma analyticAt_digammaWeierstrass {z0 : ℂ} (hz0 : z0 ∈ digammaStrip) :
    AnalyticAt ℂ (fun z =>
        -(Real.eulerMascheroniConstant : ℂ) +
          ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)) z0 := by
  have h1 : 0 < z0.re - 1 / 4 := sub_pos.mpr hz0.1
  have h2 : 0 < 2 - z0.re := sub_pos.mpr hz0.2
  let r := min (min (z0.re - 1 / 4) (2 - z0.re)) (1 : ℝ) / 2
  have hr : 0 < r := by
    have : 0 < min (min (z0.re - 1 / 4) (2 - z0.re)) (1 : ℝ) := by
      refine lt_min (lt_min h1 h2) (by norm_num)
    positivity
  have hball : Metric.ball z0 r ⊆ digammaStrip := by
    intro z hz
    have hd : ‖z - z0‖ < r := by simpa [dist_eq_norm] using hz
    have hre : |z.re - z0.re| ≤ ‖z - z0‖ := abs_re_le_norm (z - z0)
    have hre' := abs_lt.mp (hre.trans_lt hd)
    have hrle1 : r ≤ (z0.re - 1 / 4) / 2 := by
      have : r ≤ min (z0.re - 1 / 4) (2 - z0.re) / 2 := by
        have hmin : min (min (z0.re - 1 / 4) (2 - z0.re)) (1 : ℝ) ≤
            min (z0.re - 1 / 4) (2 - z0.re) := min_le_left _ _
        dsimp [r]
        linarith
      have : min (z0.re - 1 / 4) (2 - z0.re) ≤ z0.re - 1 / 4 :=
        min_le_left _ _
      linarith
    have hrle2 : r ≤ (2 - z0.re) / 2 := by
      have : r ≤ min (z0.re - 1 / 4) (2 - z0.re) / 2 := by
        have hmin : min (min (z0.re - 1 / 4) (2 - z0.re)) (1 : ℝ) ≤
            min (z0.re - 1 / 4) (2 - z0.re) := min_le_left _ _
        dsimp [r]
        linarith
      have : min (z0.re - 1 / 4) (2 - z0.re) ≤ 2 - z0.re :=
        min_le_right _ _
      linarith
    constructor
    · linarith
    · linarith
  let M := r + ‖z0 - 1‖ + 1
  have hMpos : 0 < M := by positivity
  have hterm : ∀ (n : ℕ) (z : ℂ), z ∈ Metric.ball z0 r →
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        4 * M / ((n + 1 : ℝ) ^ 2) := by
    intro n z hz
    have hzS := hball hz
    have hle := digamma_kernel_term_norm_le_strip (n := n) hzS
    have hd : ‖z - z0‖ < r := by simpa [dist_eq_norm] using hz
    have hz1 : ‖z - 1‖ ≤ r + ‖z0 - 1‖ := by
      have hdecomp : z - 1 = (z - z0) + (z0 - 1) := by abel
      rw [hdecomp]
      exact (norm_add_le _ _).trans (add_le_add hd.le le_rfl)
    have hz1M : ‖z - 1‖ ≤ M := by
      dsimp [M]; linarith
    have hden : 0 < (n + 1 : ℝ) ^ 2 := by positivity
    exact hle.trans (div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left hz1M (by norm_num : (0 : ℝ) ≤ 4))
      hden.le)
  have hu : Summable fun n : ℕ => 4 * M / ((n + 1 : ℝ) ^ 2) := by
    simpa [div_eq_mul_inv, mul_comm, mul_left_comm, mul_assoc]
      using summable_one_div_succ_sq.mul_left (4 * M)
  have hdiff : DifferentiableOn ℂ
      (fun z => ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹))
      (Metric.ball z0 r) :=
    differentiableOn_tsum_of_summable_norm hu
      (fun n => (differentiableOn_digamma_kernel n).mono hball)
      Metric.isOpen_ball hterm
  have htsum := (hdiff.analyticOnNhd Metric.isOpen_ball) z0
    (Metric.mem_ball_self hr)
  exact analyticAt_const.add htsum

lemma analyticOnNhd_digammaWeierstrass :
    AnalyticOnNhd ℂ (fun z =>
        -(Real.eulerMascheroniConstant : ℂ) +
          ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹))
      digammaStrip :=
  fun z hz => analyticAt_digammaWeierstrass hz

lemma three_halves_mem_digammaStrip :
    ((3 / 2 : ℝ) : ℂ) ∈ digammaStrip := by
  constructor <;> (simp; norm_num)

lemma xs_Ioo_three_halves (n : ℕ) :
    (3 / 2 : ℝ) + 1 / (n + 3) ∈ Ioo (1 : ℝ) 2 := by
  have hn : 0 < (n + 3 : ℝ) := by positivity
  constructor
  · have : 0 < (1 : ℝ) / (n + 3) := one_div_pos.mpr hn
    linarith
  · have : (1 : ℝ) / (n + 3) ≤ 1 / 3 := by
      exact one_div_le_one_div_of_le (by norm_num : (0 : ℝ) < 3)
        (by linarith : (3 : ℝ) ≤ n + 3)
    linarith

set_option maxHeartbeats 400000 in
lemma tendsto_ofReal_punctured_three_halves :
    Tendsto (fun n : ℕ => (((3 / 2 : ℝ) + 1 / (n + 3) : ℝ) : ℂ))
      atTop (𝓝[≠] ((3 / 2 : ℝ) : ℂ)) := by
  rw [tendsto_nhdsWithin_iff]
  constructor
  · have hden : Tendsto (fun n : ℕ => (n : ℝ) + 3) atTop atTop :=
      (tendsto_natCast_atTop_atTop.comp (tendsto_add_atTop_nat 3)).congr
        fun n => by simp [Nat.cast_add]
    have hx : Tendsto (fun n : ℕ => (3 / 2 : ℝ) + 1 / (n + 3))
        atTop (𝓝 (3 / 2 : ℝ)) := by
      simpa using
        (tendsto_const_nhds (x := (3 / 2 : ℝ))).add
          ((tendsto_const_nhds (x := (1 : ℝ))).div_atTop hden)
    exact (continuous_ofReal.tendsto (3 / 2 : ℝ)).comp hx
  · refine Eventually.of_forall fun n => ?_
    have hpos : (0 : ℝ) < 1 / (n + 3) := by positivity
    have hne : (3 / 2 : ℝ) + 1 / (n + 3) ≠ (3 / 2 : ℝ) := by
      intro h
      linarith [hpos]
    exact ofReal_injective.ne hne

lemma frequently_eq_digamma_weierstrass_three_halves :
    ∃ᶠ z in 𝓝[≠] ((3 / 2 : ℝ) : ℂ),
      digamma z = -(Real.eulerMascheroniConstant : ℂ) +
        ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹) := by
  refine tendsto_ofReal_punctured_three_halves.frequently
    (Frequently.of_forall fun n => ?_)
  obtain ⟨hx1, hx2⟩ := xs_Ioo_three_halves n
  simpa using digamma_eq_weierstrass_ofReal_Ioo hx1 hx2

lemma digamma_eq_weierstrass_on_strip :
    EqOn digamma (fun z =>
        -(Real.eulerMascheroniConstant : ℂ) +
          ∑' n : ℕ, ((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹))
      digammaStrip :=
  analyticOnNhd_digamma_strip.eqOn_of_preconnected_of_frequently_eq
    analyticOnNhd_digammaWeierstrass
    isPreconnected_digammaStrip
    three_halves_mem_digammaStrip
    frequently_eq_digamma_weierstrass_three_halves

lemma mem_digammaStrip_of_horizontal {z : ℂ}
    (hre1 : (1 / 2 : ℝ) ≤ z.re) (hre2 : z.re ≤ (3 / 2 : ℝ)) :
    z ∈ digammaStrip := by
  constructor <;> linarith

lemma sum_Ico_add_eq_sum_range {N M : ℕ} (f : ℕ → ℝ) :
    ∑ n ∈ Finset.Ico N (N + M), f n =
      ∑ k ∈ Finset.range M, f (N + k) := by
  induction M with
  | zero => simp
  | succ M ih =>
    rw [Nat.add_succ, Finset.sum_Ico_succ_top (Nat.le_add_right N M), ih,
      Finset.sum_range_succ]

lemma tsum_digamma_kernel_norm_tail_le {z : ℂ} {N : ℕ}
    (hN : 0 < N) (hne : ∀ n : ℕ, (n : ℂ) + z ≠ 0)
    (hzN : (2 : ℝ) * ‖z‖ ≤ N)
    (hsum : Summable fun n : ℕ =>
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖) :
    ∑' k : ℕ, ‖(((k + N : ℕ) + 1 : ℂ)⁻¹ -
        (((k + N : ℕ) : ℂ) + z)⁻¹)‖ ≤
      (2 : ℝ) * ‖z - 1‖ / N := by
  set f : ℕ → ℝ := fun n =>
    ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖
  have hshift : Summable fun k : ℕ => f (k + N) := by
    simpa [add_comm] using (summable_nat_add_iff N).mpr hsum
  have hlim :
      Tendsto (fun M : ℕ => ∑ k ∈ Finset.range M, f (k + N))
        atTop (𝓝 (∑' k : ℕ, f (k + N))) :=
    hshift.hasSum.tendsto_sum_nat
  have hle : ∀ M : ℕ,
      ∑ k ∈ Finset.range M, f (k + N) ≤ (2 : ℝ) * ‖z - 1‖ / N := by
    intro M
    have hIco :
        ∑ k ∈ Finset.range M, f (k + N) =
          ∑ n ∈ Finset.Ico N (N + M), f n := by
      simpa [add_comm] using
        (sum_Ico_add_eq_sum_range (N := N) (M := M) f).symm
    rw [hIco]
    exact sum_digamma_kernel_tail_le hN (Nat.le_add_right N M) hne hzN
  exact le_of_tendsto hlim (Eventually.of_forall hle)

set_option maxHeartbeats 800000 in
lemma norm_digamma_le_log_of_horizontal {z : ℂ}
    (hre1 : (1 / 2 : ℝ) ≤ z.re) (hre2 : z.re ≤ (3 / 2 : ℝ))
    (him : (2 : ℝ) ≤ |z.im|) :
    ‖digamma z‖ ≤
      (6 + |Real.eulerMascheroniConstant|) *
        (1 + Real.log (2 + |z.im|)) := by
  have hzS : z ∈ digammaStrip := mem_digammaStrip_of_horizontal hre1 hre2
  have hid := digamma_eq_weierstrass_on_strip hzS
  have hne : ∀ n : ℕ, (n : ℂ) + z ≠ 0 :=
    nat_add_ne_zero_of_mem_digammaStrip hzS
  have hsumN : Summable fun n : ℕ =>
      ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun n => digamma_kernel_term_norm_le_strip hzS)
      (by
        simpa [div_eq_mul_inv, mul_comm, mul_left_comm, mul_assoc]
          using summable_one_div_succ_sq.mul_left (4 * ‖z - 1‖))
  set T : ℝ := |z.im|
  have hT : (2 : ℝ) ≤ T := him
  have hTpos : 0 < T := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 2) hT
  have hz1 : ‖z - 1‖ ≤ (1 / 2 : ℝ) + T := by
    have hreim := norm_le_abs_re_add_abs_im (z - 1)
    have hre1bound : |z.re - 1| ≤ 1 / 2 := by
      rw [abs_le]; constructor <;> linarith
    simpa [sub_re, sub_im, one_re, one_im] using
      hreim.trans (add_le_add hre1bound le_rfl)
  have hznorm : ‖z‖ ≤ (3 / 2 : ℝ) + T := by
    have hreabs : |z.re| ≤ 3 / 2 := by
      rw [abs_le]; constructor <;> linarith
    exact (norm_le_abs_re_add_abs_im z).trans (add_le_add hreabs le_rfl)
  have hzge : T ≤ ‖z‖ := by simpa [T] using abs_im_le_norm z
  let N : ℕ := Nat.ceil (2 * ‖z‖)
  have hNreal : (2 : ℝ) * ‖z‖ ≤ N := Nat.le_ceil _
  have hNposR : (4 : ℝ) ≤ N := by
    have : (4 : ℝ) ≤ 2 * ‖z‖ := by nlinarith [hzge, hT]
    exact this.trans hNreal
  have hNpos : 0 < N := Nat.cast_pos.mp (lt_of_lt_of_le (by norm_num) hNposR)
  have hNlt : (N : ℝ) < 2 * ‖z‖ + 1 :=
    Nat.ceil_lt_add_one (mul_nonneg (by norm_num) (norm_nonneg _))
  have hγ : ‖-(Real.eulerMascheroniConstant : ℂ)‖ =
      |Real.eulerMascheroniConstant| := by
    simp [norm_neg]
  have htri : ‖digamma z‖ ≤ |Real.eulerMascheroniConstant| +
      ∑' n : ℕ, ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ := by
    rw [hid]
    exact (norm_add_le _ _).trans
      (add_le_add (le_of_eq hγ) (norm_tsum_le_tsum_norm hsumN))
  have hsplit := hsumN.sum_add_tsum_nat_add N
  have hhead :=
    sum_digamma_kernel_norm_le (z := z) (N := N) (T := T) hT le_rfl hne
  have htail :=
    tsum_digamma_kernel_norm_tail_le (z := z) (N := N)
      hNpos hne hNreal hsumN
  set L := (1 : ℝ) + Real.log (2 + T)
  have hL : (1 : ℝ) ≤ L := by
    have : 0 ≤ Real.log (2 + T) :=
      Real.log_nonneg (by nlinarith [hT])
    linarith
  have hNlog : 1 + Real.log ((N : ℝ) + 1) ≤ 3 * L := by
    have hpow : (N : ℝ) + 1 ≤ (2 + T) ^ 3 := by
      have hN1 : (N : ℝ) + 1 < 2 * ‖z‖ + 2 := by linarith
      have hbound : 2 * ‖z‖ + 2 ≤ 2 * ((3 / 2 : ℝ) + T) + 2 := by
        nlinarith [hznorm]
      have hsimp : 2 * ((3 / 2 : ℝ) + T) + 2 ≤ 5 + 2 * T := by
        norm_num
        linarith
      have hcube : 5 + 2 * T ≤ (2 + T) ^ 3 := by
        nlinarith [sq_nonneg (T - 2), pow_nonneg (by linarith : (0 : ℝ) ≤ T) 3,
          hT]
      linarith
    have hposN : (0 : ℝ) < (N : ℝ) + 1 := by positivity
    have hposT : (0 : ℝ) < 2 + T := by positivity
    have hlog := Real.log_le_log hposN hpow
    have hlogpow : Real.log ((2 + T) ^ 3) = 3 * Real.log (2 + T) :=
      Real.log_pow (2 + T) 3
    have hstep : 1 + Real.log ((N : ℝ) + 1) ≤
        1 + 3 * Real.log (2 + T) := by linarith [hlog, hlogpow]
    have hpackL : 1 + 3 * Real.log (2 + T) ≤ 3 * L := by
      have hlognn : 0 ≤ Real.log (2 + T) :=
        Real.log_nonneg (by nlinarith [hT] : (1 : ℝ) ≤ 2 + T)
      dsimp [L]
      nlinarith [hlognn]
    exact hstep.trans hpackL
  have hhead' : ∑ n ∈ Finset.range N,
        ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
      (15 / 4 : ℝ) * L := by
    have hfac : ‖z - 1‖ / T ≤ (5 / 4 : ℝ) := by
      have h1 : ‖z - 1‖ / T ≤ ((1 / 2 : ℝ) + T) / T :=
        div_le_div_of_nonneg_right hz1 hTpos.le
      have h2 : ((1 / 2 : ℝ) + T) / T = 1 / (2 * T) + 1 := by
        field_simp
      have h3 : 1 / (2 * T) + 1 ≤ (5 / 4 : ℝ) := by
        have : 1 / (2 * T) ≤ 1 / 4 := by
          rw [one_div_le_one_div (mul_pos (by norm_num) hTpos) (by norm_num)]
          nlinarith [hT]
        linarith
      linarith
    have hlog0 : 0 ≤ 1 + Real.log ((N : ℝ) + 1) := by
      have hNnn : (0 : ℝ) ≤ N := Nat.cast_nonneg N
      have : (1 : ℝ) ≤ (N : ℝ) + 1 := by linarith [hNnn]
      linarith [Real.log_nonneg this]
    have hmul :=
      mul_le_mul hfac hNlog hlog0 (by norm_num : (0 : ℝ) ≤ 5 / 4)
    have hring : (5 / 4 : ℝ) * (3 * L) = (15 / 4) * L := by ring
    exact hhead.trans (hmul.trans_eq hring)
  have htail' :
      ∑' k : ℕ, ‖(((k + N : ℕ) + 1 : ℂ)⁻¹ -
          (((k + N : ℕ) : ℂ) + z)⁻¹)‖ ≤
        (5 / 4 : ℝ) := by
    have hNge : 0 < (N : ℝ) := Nat.cast_pos.mpr hNpos
    have h2z : 0 < 2 * ‖z‖ := by nlinarith [hzge, hT]
    have h1 : (2 : ℝ) * ‖z - 1‖ / N ≤
        2 * ((1 / 2 : ℝ) + T) / N :=
      div_le_div_of_nonneg_right
        (mul_le_mul_of_nonneg_left hz1 (by norm_num)) hNge.le
    have h2 : 2 * ((1 / 2 : ℝ) + T) / N ≤
        2 * ((1 / 2 : ℝ) + T) / (2 * ‖z‖) :=
      div_le_div_of_nonneg_left (by positivity) h2z hNreal
    have h3 : 2 * ((1 / 2 : ℝ) + T) / (2 * ‖z‖) =
        ((1 / 2 : ℝ) + T) / ‖z‖ := by
      field_simp
    have h4 : ((1 / 2 : ℝ) + T) / ‖z‖ ≤ ((1 / 2 : ℝ) + T) / T :=
      div_le_div_of_nonneg_left (by positivity) hTpos hzge
    have h5 : ((1 / 2 : ℝ) + T) / T = 1 / (2 * T) + 1 := by
      field_simp
    have h6 : 1 / (2 * T) + 1 ≤ (5 / 4 : ℝ) := by
      have : 1 / (2 * T) ≤ 1 / 4 := by
        rw [one_div_le_one_div (mul_pos (by norm_num) hTpos) (by norm_num)]
        nlinarith [hT]
      linarith
    exact htail.trans (h1.trans (h2.trans (h3.trans_le (h4.trans (h5.trans_le h6)))))
  have hsumle :
      ∑' n : ℕ, ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
        (15 / 4 : ℝ) * L + 5 / 4 := by
    calc
      ∑' n : ℕ, ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖
          = ∑ n ∈ Finset.range N,
              ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ +
            ∑' k : ℕ, ‖(((k + N : ℕ) + 1 : ℂ)⁻¹ -
                (((k + N : ℕ) : ℂ) + z)⁻¹)‖ := hsplit.symm
      _ ≤ (15 / 4 : ℝ) * L + 5 / 4 := add_le_add hhead' htail'
  have hpack : |Real.eulerMascheroniConstant| +
        ((15 / 4 : ℝ) * L + 5 / 4) ≤
      (6 + |Real.eulerMascheroniConstant|) * L := by
    have hγL : |Real.eulerMascheroniConstant| ≤
        |Real.eulerMascheroniConstant| * L :=
      le_mul_of_one_le_right (abs_nonneg _) hL
    have h54 : (5 / 4 : ℝ) ≤ (5 / 4) * L :=
      le_mul_of_one_le_right (by norm_num) hL
    nlinarith
  have hmid : |Real.eulerMascheroniConstant| +
        ∑' n : ℕ, ‖((n + 1 : ℂ)⁻¹ - ((n : ℂ) + z)⁻¹)‖ ≤
      |Real.eulerMascheroniConstant| + ((15 / 4 : ℝ) * L + 5 / 4) :=
    add_le_add le_rfl hsumle
  exact (htri.trans hmid).trans hpack

/-- Sliver remainder (FE consumer: `Re ∈ [1/2, 17/16]`).
r526 closed route A: real convexity ⇒ Weierstrass on `(1,2)` ⇒
identity on `{1/4 < Re < 2}` ⇒ `|ψ|` log bound. -/
def DigammaHorizontalLogBound : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧
    ∀ {z : ℂ}, (1 / 2 : ℝ) ≤ z.re → z.re ≤ (17 / 16 : ℝ) →
      (2 : ℝ) ≤ |z.im| →
        ‖digamma z‖ ≤ C * (1 + Real.log (2 + |z.im|))

theorem digammaHorizontalLogBound : DigammaHorizontalLogBound :=
  ⟨6 + |Real.eulerMascheroniConstant|,
    add_nonneg (by norm_num) (abs_nonneg _),
    fun {z} hre1 hre2 him =>
      norm_digamma_le_log_of_horizontal hre1
        (hre2.trans (by norm_num : (17 / 16 : ℝ) ≤ 3 / 2)) him⟩

/-- r527: `|cos(x+iy)|² = cos²x + sinh²y`. -/
lemma normSq_cos (z : ℂ) :
    ‖cos z‖ ^ 2 = Real.cos z.re ^ 2 + Real.sinh z.im ^ 2 := by
  have hz : cos z =
      (Real.cos z.re * Real.cosh z.im : ℝ) +
        (-(Real.sin z.re * Real.sinh z.im) : ℝ) * I := by
    rw [cos_eq]
    simp [← ofReal_cos, ← ofReal_sin, ← ofReal_cosh, ← ofReal_sinh,
      sub_eq_add_neg, neg_mul]
  rw [hz, norm_add_mul_I, Real.sq_sqrt (add_nonneg (sq_nonneg _) (sq_nonneg _))]
  ring_nf
  have hcosh2 : Real.cosh z.im ^ 2 = 1 + Real.sinh z.im ^ 2 := Real.cosh_sq' _
  nlinarith [Real.sin_sq_add_cos_sq z.re]

lemma normSq_sin (z : ℂ) :
    ‖sin z‖ ^ 2 = Real.sin z.re ^ 2 + Real.sinh z.im ^ 2 := by
  have hz : sin z =
      (Real.sin z.re * Real.cosh z.im : ℝ) +
        (Real.cos z.re * Real.sinh z.im : ℝ) * I := by
    rw [sin_eq]
    simp [← ofReal_sin, ← ofReal_cos, ← ofReal_cosh, ← ofReal_sinh]
  rw [hz, norm_add_mul_I, Real.sq_sqrt (add_nonneg (sq_nonneg _) (sq_nonneg _))]
  ring_nf
  have hcosh2 : Real.cosh z.im ^ 2 = 1 + Real.sinh z.im ^ 2 := Real.cosh_sq' _
  nlinarith [Real.sin_sq_add_cos_sq z.re]

lemma cos_ne_zero_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : cos z ≠ 0 := by
  have hsinh : Real.sinh z.im ≠ 0 := Real.sinh_ne_zero.mpr h
  intro hcos
  have hsq0 : ‖cos z‖ ^ 2 = 0 := by simp [hcos]
  have hsqpos : 0 < ‖cos z‖ ^ 2 := by
    rw [normSq_cos]
    nlinarith [sq_pos_of_ne_zero hsinh, sq_nonneg (Real.cos z.re)]
  linarith

/-- r527: `|tan z|² ≤ 1 + 1/sinh²(Im z)` for `Im z ≠ 0`. -/
lemma norm_tan_sq_le_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) :
    ‖tan z‖ ^ 2 ≤ 1 + 1 / Real.sinh z.im ^ 2 := by
  have hsinh : Real.sinh z.im ≠ 0 := Real.sinh_ne_zero.mpr h
  rw [tan_eq_sin_div_cos, norm_div, div_pow, normSq_sin, normSq_cos]
  have hsinhpos : 0 < Real.sinh z.im ^ 2 := sq_pos_of_ne_zero hsinh
  have hle : Real.sin z.re ^ 2 + Real.sinh z.im ^ 2 ≤
      1 + Real.sinh z.im ^ 2 := by
    nlinarith [Real.sin_sq_le_one z.re]
  have hge : Real.sinh z.im ^ 2 ≤
      Real.cos z.re ^ 2 + Real.sinh z.im ^ 2 := by
    nlinarith [sq_nonneg (Real.cos z.re)]
  have hfrac :
      (Real.sin z.re ^ 2 + Real.sinh z.im ^ 2) /
          (Real.cos z.re ^ 2 + Real.sinh z.im ^ 2) ≤
        (1 + Real.sinh z.im ^ 2) / Real.sinh z.im ^ 2 :=
    (div_le_div_of_nonneg_left
        (add_nonneg (sq_nonneg _) (sq_nonneg _)) hsinhpos hge).trans
      (div_le_div_of_nonneg_right hle hsinhpos.le)
  have hsimp : (1 + Real.sinh z.im ^ 2) / Real.sinh z.im ^ 2 =
      1 + 1 / Real.sinh z.im ^ 2 := by
    field_simp
    ring
  exact hfrac.trans_eq hsimp

/-- r527: on `|Im z| ≥ 2`, `|tan z| ≤ √(1 + 1/sinh² 2)`. -/
lemma norm_tan_le_of_two_le_abs_im {z : ℂ} (h : (2 : ℝ) ≤ |z.im|) :
    ‖tan z‖ ≤ Real.sqrt (1 + 1 / Real.sinh 2 ^ 2) := by
  have him : z.im ≠ 0 := by
    intro hz
    have : |z.im| = 0 := by simp [hz]
    linarith
  have hsq := norm_tan_sq_le_of_im_ne_zero him
  have hmono : Real.sinh 2 ≤ Real.sinh |z.im| := Real.sinh_le_sinh.mpr h
  have hsinh2 : Real.sinh 2 ≤ |Real.sinh z.im| := by
    rwa [Real.abs_sinh]
  have h2pos : 0 < Real.sinh 2 := Real.sinh_pos_iff.mpr (by norm_num)
  have hden : Real.sinh 2 ^ 2 ≤ Real.sinh z.im ^ 2 := by
    have : Real.sinh 2 ^ 2 ≤ |Real.sinh z.im| ^ 2 := by
      nlinarith [hsinh2, h2pos]
    simpa [sq_abs] using this
  have hle : 1 + 1 / Real.sinh z.im ^ 2 ≤ 1 + 1 / Real.sinh 2 ^ 2 := by
    have hpos : 0 < Real.sinh 2 ^ 2 := sq_pos_of_pos h2pos
    have hnum : (0 : ℝ) ≤ 1 := by norm_num
    simpa [add_comm] using
      add_le_add_left (div_le_div_of_nonneg_left hnum hpos hden) (1 : ℝ)
  exact Real.le_sqrt_of_sq_le (hsq.trans hle)

lemma ne_neg_nat_of_two_le_abs_im {s : ℂ} (h : (2 : ℝ) ≤ |s.im|)
    (n : ℕ) : s ≠ -n := by
  intro hs
  simp [hs] at h
  linarith

lemma ne_one_of_two_le_abs_im {s : ℂ} (h : (2 : ℝ) ≤ |s.im|) : s ≠ 1 := by
  intro hs
  simp [hs] at h
  linarith

lemma digamma_eq_succ_sub_inv {s : ℂ} (h : (2 : ℝ) ≤ |s.im|) :
    digamma s = digamma (s + 1) - s⁻¹ :=
  eq_sub_of_add_eq (digamma_apply_add_one s (ne_neg_nat_of_two_le_abs_im h)).symm

lemma norm_digamma_le_log_of_sliver {s : ℂ}
    (hre1 : (-1 / 16 : ℝ) ≤ s.re) (hre2 : s.re ≤ (1 / 2 : ℝ))
    (him : (2 : ℝ) ≤ |s.im|) :
    ‖digamma s‖ ≤
      (6 + |Real.eulerMascheroniConstant|) *
        (1 + Real.log (2 + |s.im|)) + 1 / 2 := by
  have hrec := digamma_eq_succ_sub_inv him
  have hre1' : (1 / 2 : ℝ) ≤ (s + 1).re := by
    simp [add_re]; linarith
  have hre2' : (s + 1).re ≤ (3 / 2 : ℝ) := by
    simp [add_re]; linarith
  have him' : (2 : ℝ) ≤ |(s + 1).im| := by
    simpa [add_im] using him
  have hψ := norm_digamma_le_log_of_horizontal hre1' hre2' him'
  have hψ' : ‖digamma (s + 1)‖ ≤
      (6 + |Real.eulerMascheroniConstant|) *
        (1 + Real.log (2 + |s.im|)) := by
    simpa [add_im] using hψ
  have hinv : ‖s⁻¹‖ ≤ (1 / 2 : ℝ) := by
    have hge : (2 : ℝ) ≤ ‖s‖ := him.trans (abs_im_le_norm s)
    rw [norm_inv]
    simpa [one_div] using
      inv_anti₀ (by norm_num : (0 : ℝ) < 2) hge
  have htri : ‖digamma s‖ ≤ ‖digamma (s + 1)‖ + ‖s⁻¹‖ := by
    rw [hrec]; exact norm_sub_le _ _
  linarith [hψ', hinv, htri]

noncomputable def zetaFEFactor (s : ℂ) : ℂ :=
  2 * (2 * (Real.pi : ℂ)) ^ (-s) * Gamma s * cos (Real.pi * s / 2)

lemma riemannZeta_one_sub_factor {s : ℂ}
    (hs : ∀ n : ℕ, s ≠ -n) (hs1 : s ≠ 1) :
    riemannZeta (1 - s) = zetaFEFactor s * riemannZeta s := by
  simpa [zetaFEFactor, mul_assoc] using riemannZeta_one_sub hs hs1

lemma two_mul_pi_ne_zero : (2 * (Real.pi : ℂ)) ≠ 0 :=
  mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero)

lemma logDeriv_neg_cpow_two_pi (s : ℂ) :
    logDeriv (fun w : ℂ => (2 * (Real.pi : ℂ)) ^ (-w)) s =
      - Complex.log (2 * (Real.pi : ℂ)) := by
  have hc := two_mul_pi_ne_zero
  have h := (hasDerivAt_neg s).const_cpow (Or.inl hc)
  have hne : (2 * (Real.pi : ℂ)) ^ (-s) ≠ 0 :=
    cpow_ne_zero_iff.mpr (Or.inl hc)
  rw [logDeriv_apply, h.deriv]
  field_simp [hne]

lemma hasDerivAt_pi_mul_div_two (s : ℂ) :
    HasDerivAt (fun w : ℂ => (Real.pi : ℂ) * w / 2)
      ((Real.pi : ℂ) / 2) s := by
  convert ((hasDerivAt_id s).const_mul (Real.pi : ℂ)).div_const 2 using 1
  ring

lemma logDeriv_cos_pi_div_two {s : ℂ}
    (hcos : cos (Real.pi * s / 2) ≠ 0) :
    logDeriv (fun w : ℂ => cos (Real.pi * w / 2)) s =
      - ((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2) := by
  have hd := hasDerivAt_pi_mul_div_two s
  have hf : DifferentiableAt ℂ cos (Real.pi * s / 2) :=
    (hasDerivAt_cos _).differentiableAt
  have hld : logDeriv cos (Real.pi * s / 2) = - tan (Real.pi * s / 2) := by
    rw [logDeriv_apply, Complex.deriv_cos, tan_eq_sin_div_cos]
    field_simp [hcos]
  have hcomp :=
    logDeriv_comp (f := cos)
      (g := fun w : ℂ => (Real.pi : ℂ) * w / 2) hf hd.differentiableAt
  have hfun : (fun w : ℂ => cos (Real.pi * w / 2)) =
      cos ∘ fun w : ℂ => (Real.pi : ℂ) * w / 2 := rfl
  rw [hfun, hcomp, hld, hd.deriv]
  ring

lemma differentiableAt_zetaFEFactor {s : ℂ}
    (hG : ∀ n : ℕ, s ≠ -n) :
    DifferentiableAt ℂ zetaFEFactor s := by
  have hc := two_mul_pi_ne_zero
  have hcpow :
      DifferentiableAt ℂ (fun w : ℂ => (2 * (Real.pi : ℂ)) ^ (-w)) s :=
    ((hasDerivAt_neg s).const_cpow (Or.inl hc)).differentiableAt
  have hΓ : DifferentiableAt ℂ Gamma s := differentiableAt_Gamma s hG
  have hcos : DifferentiableAt ℂ (fun w : ℂ => cos (Real.pi * w / 2)) s :=
    ((hasDerivAt_cos _).comp s (hasDerivAt_pi_mul_div_two s)).differentiableAt
  have hfun : zetaFEFactor = fun w =>
      (2 : ℂ) * ((2 * (Real.pi : ℂ)) ^ (-w) *
        (Gamma w * cos (Real.pi * w / 2))) := by
    funext w; unfold zetaFEFactor; ring
  rw [hfun]
  exact (hcpow.mul (hΓ.mul hcos)).const_mul _

lemma logDeriv_zetaFEFactor {s : ℂ}
    (hG : ∀ n : ℕ, s ≠ -n)
    (hcos : cos (Real.pi * s / 2) ≠ 0) :
    logDeriv zetaFEFactor s =
      - Complex.log (2 * (Real.pi : ℂ)) + digamma s
        - ((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2) := by
  have hc := two_mul_pi_ne_zero
  have hcpow0 : (2 * (Real.pi : ℂ)) ^ (-s) ≠ 0 :=
    cpow_ne_zero_iff.mpr (Or.inl hc)
  have hΓ0 : Gamma s ≠ 0 := Complex.Gamma_ne_zero hG
  have hdiffC :
      DifferentiableAt ℂ (fun w : ℂ => (2 * (Real.pi : ℂ)) ^ (-w)) s :=
    ((hasDerivAt_neg s).const_cpow (Or.inl hc)).differentiableAt
  have hdiffΓ : DifferentiableAt ℂ Gamma s := differentiableAt_Gamma s hG
  have hdiffCos : DifferentiableAt ℂ (fun w : ℂ => cos (Real.pi * w / 2)) s :=
    ((hasDerivAt_cos _).comp s (hasDerivAt_pi_mul_div_two s)).differentiableAt
  have hfun : zetaFEFactor =
      fun w => (2 : ℂ) * ((2 * (Real.pi : ℂ)) ^ (-w) *
        (Gamma w * cos (Real.pi * w / 2))) := by
    funext w; unfold zetaFEFactor; ring
  have hprod0 : Gamma s * cos (Real.pi * s / 2) ≠ 0 :=
    mul_ne_zero hΓ0 hcos
  rw [hfun]
  rw [logDeriv_const_mul (f := fun w =>
      (2 * (Real.pi : ℂ)) ^ (-w) *
        (Gamma w * cos (Real.pi * w / 2))) s (2 : ℂ) two_ne_zero]
  rw [logDeriv_mul (f := fun w => (2 * (Real.pi : ℂ)) ^ (-w))
      (g := fun w => Gamma w * cos (Real.pi * w / 2))
      s hcpow0 hprod0 hdiffC (hdiffΓ.mul hdiffCos)]
  rw [logDeriv_mul (f := Gamma)
      (g := fun w => cos (Real.pi * w / 2))
      s hΓ0 hcos hdiffΓ hdiffCos]
  rw [logDeriv_neg_cpow_two_pi, logDeriv_cos_pi_div_two hcos, digamma_def]
  ring

lemma ne_neg_nat_of_im_ne_zero {s : ℂ} (h : s.im ≠ 0) (n : ℕ) : s ≠ -n := by
  intro hs
  simp [hs] at h

lemma ne_one_of_im_ne_zero {s : ℂ} (h : s.im ≠ 0) : s ≠ 1 := by
  intro hs
  simp [hs] at h

lemma im_pi_mul_div_two (s : ℂ) :
    ((Real.pi : ℂ) * s / 2).im = Real.pi * s.im / 2 := by
  simp [div_eq_mul_inv, mul_im]

lemma cos_pi_div_two_ne_zero_of_two_le_abs_im {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) :
    cos (Real.pi * s / 2) ≠ 0 := by
  have him : ((Real.pi : ℂ) * s / 2).im ≠ 0 := by
    rw [im_pi_mul_div_two]
    have hs : s.im ≠ 0 := by
      intro hz; simp [hz] at h; linarith
    exact div_ne_zero (mul_ne_zero Real.pi_ne_zero hs) two_ne_zero
  exact cos_ne_zero_of_im_ne_zero him

lemma two_le_abs_im_pi_div_two {s : ℂ} (h : (2 : ℝ) ≤ |s.im|) :
    (2 : ℝ) ≤ |((Real.pi : ℂ) * s / 2).im| := by
  rw [im_pi_mul_div_two, abs_div, abs_mul, abs_of_pos Real.pi_pos,
    abs_of_pos (by norm_num : (0 : ℝ) < 2)]
  have hπ : (3 : ℝ) < Real.pi := Real.pi_gt_three
  nlinarith

lemma zetaFEFactor_ne_zero_of_two_le_abs_im {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) :
    zetaFEFactor s ≠ 0 := by
  have hG : ∀ n : ℕ, s ≠ -n := ne_neg_nat_of_two_le_abs_im h
  unfold zetaFEFactor
  refine mul_ne_zero (mul_ne_zero (mul_ne_zero two_ne_zero ?_) ?_)
    (cos_pi_div_two_ne_zero_of_two_le_abs_im h)
  · exact cpow_ne_zero_iff.mpr (Or.inl two_mul_pi_ne_zero)
  · exact Complex.Gamma_ne_zero hG

lemma eventuallyEq_riemannZeta_one_sub_factor {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) :
    (fun w : ℂ => riemannZeta (1 - w)) =ᶠ[𝓝 s]
      fun w => zetaFEFactor w * riemannZeta w := by
  have hball : Metric.ball s 1 ⊆ {w : ℂ | (1 : ℝ) ≤ |w.im|} := by
    intro w hw
    have hd : ‖w - s‖ < 1 := mem_ball_iff_norm.mp hw
    have himle : |w.im - s.im| ≤ ‖w - s‖ := by
      simpa [sub_im] using abs_im_le_norm (w - s)
    have htri : |s.im| ≤ |w.im| + |w.im - s.im| := by
      calc
        |s.im| = |w.im + (s.im - w.im)| := by ring_nf
        _ ≤ |w.im| + |s.im - w.im| := abs_add_le _ _
        _ = |w.im| + |w.im - s.im| := by rw [abs_sub_comm]
    have hlower : |s.im| - ‖w - s‖ ≤ |w.im| := by
      linarith [htri, himle]
    have hone : (1 : ℝ) ≤ |s.im| - ‖w - s‖ := by
      linarith [h, le_of_lt hd]
    exact hone.trans hlower
  refine Filter.eventuallyEq_of_mem
      (Metric.ball_mem_nhds s (by norm_num : (0 : ℝ) < 1)) ?_
  intro w hw
  have him : w.im ≠ 0 := by
    have : (1 : ℝ) ≤ |w.im| := hball hw
    intro hz; simp [hz] at this; linarith
  exact riemannZeta_one_sub_factor (ne_neg_nat_of_im_ne_zero him)
    (ne_one_of_im_ne_zero him)

lemma hasDerivAt_one_sub (s : ℂ) :
    HasDerivAt (fun w : ℂ => 1 - w) (-1) s := by
  convert (hasDerivAt_const s (1 : ℂ)).sub (hasDerivAt_id s) using 1
  ring

lemma logDeriv_riemannZeta_functional {s : ℂ}
    (h : (2 : ℝ) ≤ |s.im|) (hz : riemannZeta s ≠ 0) :
    logDeriv riemannZeta s =
      - logDeriv riemannZeta (1 - s) - logDeriv zetaFEFactor s := by
  have hs1 : s ≠ 1 := ne_one_of_two_le_abs_im h
  have h1s : 1 - s ≠ 1 := by
    intro heq
    have him0 : s.im = 0 := by
      have : (1 - s).im = (1 : ℂ).im := congrArg Complex.im heq
      simpa [sub_im] using this
    simp [him0] at h
    linarith
  have hG : ∀ n : ℕ, s ≠ -n := ne_neg_nat_of_two_le_abs_im h
  have hGne := zetaFEFactor_ne_zero_of_two_le_abs_im h
  have hfe := eventuallyEq_riemannZeta_one_sub_factor h
  have hld :
      logDeriv (fun w : ℂ => riemannZeta (1 - w)) s =
        logDeriv (fun w => zetaFEFactor w * riemannZeta w) s := by
    rw [logDeriv_apply, logDeriv_apply, hfe.deriv_eq, hfe.eq_of_nhds]
  have hd := hasDerivAt_one_sub s
  have hf : DifferentiableAt ℂ riemannZeta (1 - s) :=
    differentiableAt_riemannZeta h1s
  have hL : logDeriv (fun w : ℂ => riemannZeta (1 - w)) s =
      - logDeriv riemannZeta (1 - s) := by
    have hcomp :=
      logDeriv_comp (f := riemannZeta) (g := fun w : ℂ => 1 - w)
        hf hd.differentiableAt
    have hfun : (fun w : ℂ => riemannZeta (1 - w)) =
        riemannZeta ∘ fun w : ℂ => 1 - w := rfl
    rw [hfun, hcomp, hd.deriv]
    ring
  have hR : logDeriv (fun w => zetaFEFactor w * riemannZeta w) s =
      logDeriv zetaFEFactor s + logDeriv riemannZeta s :=
    logDeriv_mul s hGne hz (differentiableAt_zetaFEFactor hG)
      (differentiableAt_riemannZeta hs1)
  have hsum : logDeriv zetaFEFactor s + logDeriv riemannZeta s =
      - logDeriv riemannZeta (1 - s) := by
    rw [← hR, ← hld, hL]
  exact eq_sub_of_add_eq (add_comm (logDeriv zetaFEFactor s) _ ▸ hsum)

lemma norm_log_two_pi :
    ‖Complex.log (2 * (Real.pi : ℂ))‖ = Real.log (2 * Real.pi) := by
  have hpos : 0 < (2 : ℝ) * Real.pi :=
    mul_pos (by norm_num) Real.pi_pos
  have h1 : (1 : ℝ) ≤ 2 * Real.pi := by
    have : (2 : ℝ) * 3 < 2 * Real.pi :=
      mul_lt_mul_of_pos_left Real.pi_gt_three (by norm_num)
    linarith
  have hcoe : (2 * (Real.pi : ℂ)) = (↑((2 : ℝ) * Real.pi) : ℂ) := by
    rw [ofReal_mul, ofReal_ofNat]
  calc
    ‖Complex.log (2 * (Real.pi : ℂ))‖
        = ‖Complex.log (↑((2 : ℝ) * Real.pi))‖ := by rw [hcoe]
    _ = ‖(Real.log (2 * Real.pi) : ℂ)‖ := by rw [← ofReal_log hpos.le]
    _ = |Real.log (2 * Real.pi)| := Complex.norm_real _
    _ = Real.log (2 * Real.pi) := abs_of_nonneg (Real.log_nonneg h1)

noncomputable def sliverEdgeConst : ℝ :=
  landauHorizontalConst +
    2 * (6 + |Real.eulerMascheroniConstant|) +
    Real.log (2 * Real.pi) + (1 / 2 : ℝ) +
    (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)

lemma sliverEdgeConst_nonneg : 0 ≤ sliverEdgeConst := by
  have hL := landauHorizontalConst_pos.le
  have hlog : 0 ≤ Real.log (2 * Real.pi) :=
    Real.log_nonneg (by nlinarith [Real.pi_gt_three])
  unfold sliverEdgeConst
  positivity

lemma sliver_cubic_pack {A L LHC Cψ C0 d g : ℝ}
    (hA : (1 : ℝ) ≤ A) (hL : (1 : ℝ) ≤ L)
    (hLHC : 0 ≤ LHC) (hCψ : 0 ≤ Cψ) (hC0 : 0 ≤ C0)
    (hd : d ≤ A * LHC * L ^ 3)
    (hg : g ≤ Cψ * (2 * L) + C0) :
    d + g ≤ A * (LHC + 2 * Cψ + C0) * L ^ 3 := by
  have hL3 : L ≤ L ^ 3 := le_self_pow₀ hL (by norm_num : (3 : ℕ) ≠ 0)
  have h1L : (1 : ℝ) ≤ L ^ 3 := le_trans hL hL3
  have hg' : g ≤ (2 * Cψ + C0) * L ^ 3 := by
    have hψ : Cψ * (2 * L) ≤ 2 * Cψ * L ^ 3 := by
      nlinarith [hCψ, hL3]
    have h0 : C0 ≤ C0 * L ^ 3 := by nlinarith [hC0, h1L]
    nlinarith [hg, hψ, h0]
  have hrest : (2 * Cψ + C0) * L ^ 3 ≤ A * (2 * Cψ + C0) * L ^ 3 :=
    mul_le_mul_of_nonneg_right (le_mul_of_one_le_left (by positivity) hA)
      (pow_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 1) hL) 3)
  nlinarith [hd, hg', hrest, hA, hLHC]

lemma sliverEdgeBound_of_dual {s : ℂ} {T A : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hre1 : (-1 / 16 : ℝ) ≤ s.re) (hre2 : s.re ≤ (1 / 2 : ℝ))
    (himT : |s.im| = T) (hz : riemannZeta s ≠ 0)
    (hdual : ‖logDeriv riemannZeta (1 - s)‖ ≤
      A * landauHorizontalConst * (1 + Real.log T) ^ 3) :
    ‖logDeriv riemannZeta s‖ ≤
      A * sliverEdgeConst * (1 + Real.log T) ^ 3 := by
  have him : (2 : ℝ) ≤ |s.im| := by rw [himT]; exact hT
  have hG : ∀ n : ℕ, s ≠ -n := ne_neg_nat_of_two_le_abs_im him
  have hcos := cos_pi_div_two_ne_zero_of_two_le_abs_im him
  have hid := logDeriv_riemannZeta_functional him hz
  have hFE := logDeriv_zetaFEFactor hG hcos
  have hψ := norm_digamma_le_log_of_sliver hre1 hre2 him
  have htan :=
    norm_tan_le_of_two_le_abs_im (z := Real.pi * s / 2)
      (two_le_abs_im_pi_div_two him)
  set L : ℝ := 1 + Real.log T
  have hL : (1 : ℝ) ≤ L := by
    have : 0 ≤ Real.log T :=
      Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
    exact le_add_of_nonneg_right this
  have hlog2 : 1 + Real.log (2 + |s.im|) ≤ 2 * L := by
    have hTabs : |T| = T :=
      abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) hT)
    rw [himT, ← hTabs]
    simpa [L] using one_add_log_two_add_abs_le hT
  have hπtan : ‖((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ ≤
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2) := by
    have hπ : ‖(Real.pi : ℂ)‖ = Real.pi := by
      simp [Complex.norm_real, abs_of_pos Real.pi_pos]
    have h2 : ‖(2 : ℂ)‖ = 2 := by norm_num
    rw [norm_mul, norm_div, hπ, h2]
    exact mul_le_mul_of_nonneg_left htan (div_nonneg Real.pi_pos.le (by norm_num))
  have hGnorm : ‖logDeriv zetaFEFactor s‖ ≤
      (6 + |Real.eulerMascheroniConstant|) * (1 + Real.log (2 + |s.im|)) +
        (Real.log (2 * Real.pi) + 1 / 2 +
          (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)) := by
    rw [hFE]
    have hsplit :
        ‖-Complex.log (2 * (Real.pi : ℂ)) + digamma s
            - ((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ ≤
          ‖Complex.log (2 * (Real.pi : ℂ))‖ + ‖digamma s‖ +
            ‖((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ := by
      refine (norm_sub_le _ _).trans ?_
      gcongr
      simpa using norm_add_le (-Complex.log (2 * (Real.pi : ℂ))) (digamma s)
    refine hsplit.trans ?_
    rw [norm_log_two_pi]
    nlinarith [hψ, hπtan]
  have htri : ‖logDeriv riemannZeta s‖ ≤
      ‖logDeriv riemannZeta (1 - s)‖ + ‖logDeriv zetaFEFactor s‖ := by
    rw [hid]
    simpa using
      (norm_sub_le (-logDeriv riemannZeta (1 - s)) (logDeriv zetaFEFactor s))
  set Cψ : ℝ := 6 + |Real.eulerMascheroniConstant|
  set C0 : ℝ :=
    Real.log (2 * Real.pi) + 1 / 2 +
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)
  have hg : ‖logDeriv zetaFEFactor s‖ ≤ Cψ * (2 * L) + C0 := by
    refine hGnorm.trans ?_
    have : Cψ * (1 + Real.log (2 + |s.im|)) ≤ Cψ * (2 * L) :=
      mul_le_mul_of_nonneg_left hlog2 (by positivity)
    nlinarith [this]
  have hpack :=
    sliver_cubic_pack (A := A) (L := L) (LHC := landauHorizontalConst)
      (Cψ := Cψ) (C0 := C0)
      (d := ‖logDeriv riemannZeta (1 - s)‖)
      (g := ‖logDeriv zetaFEFactor s‖)
      hA hL landauHorizontalConst_pos.le
      (by unfold Cψ; positivity)
      (by
        unfold C0
        have : 0 ≤ Real.log (2 * Real.pi) :=
          Real.log_nonneg (by nlinarith [Real.pi_gt_three])
        positivity)
      hdual hg
  have hC : landauHorizontalConst + 2 * Cψ + C0 = sliverEdgeConst := by
    unfold sliverEdgeConst Cψ C0; ring
  simpa [L, hC] using htri.trans hpack

lemma sliverEdgeBound_negIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ (1 / 2 : ℝ))
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) :
    ‖logDeriv riemannZeta ((σ : ℂ) - T * I)‖ ≤
      A * sliverEdgeConst * (1 + Real.log T) ^ 3 := by
  set s : ℂ := (σ : ℂ) - T * I
  have hre1 : (-1 / 16 : ℝ) ≤ s.re := by simpa [s] using hσ1
  have hre2 : s.re ≤ (1 / 2 : ℝ) := by simpa [s] using hσ2
  have himT : |s.im| = T := by
    have him : s.im = -T := by simp [s]
    rw [him, abs_neg, abs_of_nonneg
      (le_trans (by norm_num : (0 : ℝ) ≤ 2) hT)]
  have hdualσ1 : (1 / 2 : ℝ) ≤ 1 - σ := by linarith
  have hdualσ2 : 1 - σ ≤ 2 := by linarith
  have hdual :=
    horizontalEdgeLandauBound_of_gap (T := T) (A := A) hA hT hgap
      (σ := 1 - σ) hdualσ1 hdualσ2
  have h1s : (1 : ℂ) - s = (1 - σ : ℂ) + T * I := by
    simp [s]; ring
  have hdual' : ‖logDeriv riemannZeta (1 - s)‖ ≤
      A * landauHorizontalConst * (1 + Real.log T) ^ 3 := by
    simpa [h1s] using hdual
  have him : (2 : ℝ) ≤ |s.im| := by rw [himT]; exact hT
  have hz1 : riemannZeta (1 - s) ≠ 0 := by
    simpa [h1s, ofReal_sub, ofReal_one] using
      riemannZeta_ne_zero_of_landau_gap (A := A) (σ := 1 - σ)
        (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA) hT hgap
  have hz : riemannZeta s ≠ 0 := by
    intro hz0
    have hFE := riemannZeta_one_sub_factor (ne_neg_nat_of_two_le_abs_im him)
      (ne_one_of_two_le_abs_im him)
    rw [hFE, hz0, mul_zero] at hz1
    exact hz1 rfl
  exact sliverEdgeBound_of_dual hA hT hre1 hre2 himT hz hdual'

/-- r528: Dirichlet series has real coefficients, so `ζ(conj s)=conj(ζ s)`
on `Re > 1`. -/
lemma riemannZeta_conj_of_one_lt_re {s : ℂ} (hs : 1 < s.re) :
    riemannZeta (conj s) = conj (riemannZeta s) := by
  have hs' : 1 < (conj s).re := by simpa [conj_re] using hs
  rw [zeta_eq_tsum_one_div_nat_add_one_cpow hs,
    zeta_eq_tsum_one_div_nat_add_one_cpow hs', conj_tsum]
  refine tsum_congr fun n => ?_
  have harg : arg (n + 1 : ℂ) ≠ Real.pi := by
    have hn : (n + 1 : ℂ) = ((n + 1 : ℕ) : ℂ) := by norm_cast
    rw [hn, natCast_arg]
    exact Real.pi_ne_zero.symm
  have hcpow : (n + 1 : ℂ) ^ conj s = conj ((n + 1 : ℂ) ^ s) := by
    simpa using cpow_conj (n + 1 : ℂ) s harg
  simp [one_div, hcpow, map_inv₀]

lemma conj_ne_one {s : ℂ} (hs : s ≠ 1) : conj s ≠ 1 := by
  intro h
  exact hs (by simpa [star_star] using congrArg conj h)

lemma differentiableOn_riemannZeta_conj_conj :
    DifferentiableOn ℂ (conj ∘ riemannZeta ∘ conj) ({1}ᶜ) := by
  intro s hs
  have hdiff : DifferentiableAt ℂ (conj ∘ riemannZeta ∘ conj) s := by
    simpa [star_star] using
      (differentiableAt_riemannZeta (conj_ne_one hs)).conj_conj
  exact hdiff.differentiableWithinAt

lemma analyticOnNhd_riemannZeta_conj_conj :
    AnalyticOnNhd ℂ (conj ∘ riemannZeta ∘ conj) ({1}ᶜ) :=
  differentiableOn_riemannZeta_conj_conj.analyticOnNhd isOpen_compl_singleton

lemma eventuallyEq_riemannZeta_conj_conj_two :
    (conj ∘ riemannZeta ∘ conj) =ᶠ[𝓝 (2 : ℂ)] riemannZeta := by
  have hball : Metric.ball (2 : ℂ) (1 / 2) ⊆ {z : ℂ | 1 < z.re} := by
    intro z hz
    have hd : ‖z - 2‖ < (1 / 2 : ℝ) := mem_ball_iff_norm.mp hz
    have hre : |z.re - 2| ≤ ‖z - 2‖ := by
      simpa [sub_re] using abs_re_le_norm (z - 2)
    have habs : |z.re - 2| < (1 / 2 : ℝ) := hre.trans_lt hd
    have hlo : -((1 : ℝ) / 2) < z.re - 2 := (abs_lt.mp habs).1
    have h32 : (3 / 2 : ℝ) < z.re := by
      have := add_lt_add_right hlo (2 : ℝ)
      convert this using 1
      · norm_num
      · ring
    exact lt_trans (by norm_num : (1 : ℝ) < 3 / 2) h32
  refine Filter.eventuallyEq_of_mem
      (Metric.ball_mem_nhds (2 : ℂ) (by norm_num : (0 : ℝ) < 1 / 2)) ?_
  intro z hz
  have h := riemannZeta_conj_of_one_lt_re (hball hz)
  simp [Function.comp_apply, h]

lemma eqOn_riemannZeta_conj_conj :
    EqOn (conj ∘ riemannZeta ∘ conj) riemannZeta ({1}ᶜ) :=
  analyticOnNhd_riemannZeta_conj_conj.eqOn_of_preconnected_of_eventuallyEq
    analyticOnNhd_riemannZeta_compl_one isPreconnected_compl_one
    (by norm_num : (2 : ℂ) ≠ 1) eventuallyEq_riemannZeta_conj_conj_two

/-- r528: Schwarz reflection for `ζ` off the pole. -/
lemma riemannZeta_conj {s : ℂ} (hs : s ≠ 1) :
    riemannZeta (conj s) = conj (riemannZeta s) := by
  have h : conj (riemannZeta (conj s)) = riemannZeta s := by
    simpa [Function.comp_apply] using eqOn_riemannZeta_conj_conj hs
  calc riemannZeta (conj s)
      = conj (conj (riemannZeta (conj s))) := (star_star _).symm
    _ = conj (riemannZeta s) := by rw [h]

lemma conj_ofReal_add_real_mul_I (σ τ : ℝ) :
    conj ((σ : ℂ) + τ * I) = (σ : ℂ) - τ * I := by
  rw [map_add, conj_ofReal, map_mul, conj_ofReal, conj_I]
  ring

lemma riemannZeta_ne_zero_conj {s : ℂ} (hs : s ≠ 1)
    (hz : riemannZeta s ≠ 0) :
    riemannZeta (conj s) ≠ 0 := by
  rw [riemannZeta_conj hs]
  exact fun h => hz ((map_eq_zero (starRingEnd ℂ)).mp h)

lemma deriv_riemannZeta_conj {s : ℂ} (hs : s ≠ 1) :
    deriv riemannZeta (conj s) = conj (deriv riemannZeta s) := by
  have hopen : {1}ᶜ ∈ 𝓝 s := isOpen_compl_singleton.mem_nhds hs
  have heq : (conj ∘ riemannZeta ∘ conj) =ᶠ[𝓝 s] riemannZeta :=
    eventuallyEq_iff_exists_mem.2 ⟨{1}ᶜ, hopen, eqOn_riemannZeta_conj_conj⟩
  have hder : deriv (conj ∘ riemannZeta ∘ conj) s = deriv riemannZeta s :=
    heq.deriv_eq
  have hcc : deriv (conj ∘ riemannZeta ∘ conj) s =
      conj (deriv riemannZeta (conj s)) := by
    simp [deriv_conj_conj]
  have h : conj (deriv riemannZeta (conj s)) = deriv riemannZeta s :=
    hcc.symm.trans hder
  calc deriv riemannZeta (conj s)
      = conj (conj (deriv riemannZeta (conj s))) := (star_star _).symm
    _ = conj (deriv riemannZeta s) := by rw [h]

lemma logDeriv_riemannZeta_conj {s : ℂ} (hs : s ≠ 1)
    (_hz : riemannZeta s ≠ 0) :
    logDeriv riemannZeta (conj s) = conj (logDeriv riemannZeta s) := by
  rw [logDeriv_apply, logDeriv_apply, deriv_riemannZeta_conj hs,
    riemannZeta_conj hs, map_div₀]

lemma norm_logDeriv_riemannZeta_conj {s : ℂ} (hs : s ≠ 1)
    (hz : riemannZeta s ≠ 0) :
    ‖logDeriv riemannZeta (conj s)‖ = ‖logDeriv riemannZeta s‖ := by
  rw [logDeriv_riemannZeta_conj hs hz, norm_conj]

lemma landauHorizontalConst_le_sliverEdgeConst :
    landauHorizontalConst ≤ sliverEdgeConst := by
  unfold sliverEdgeConst
  have hrest : 0 ≤
      2 * (6 + |Real.eulerMascheroniConstant|) +
        Real.log (2 * Real.pi) + (1 / 2 : ℝ) +
        (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2) := by
    have : 0 ≤ Real.log (2 * Real.pi) :=
      Real.log_nonneg (by nlinarith [Real.pi_gt_three])
    positivity
  linarith [landauHorizontalConst_pos.le]

lemma riemannZeta_ne_zero_of_sliver_negIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ (1 / 2 : ℝ))
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) :
    riemannZeta ((σ : ℂ) - T * I) ≠ 0 := by
  set s : ℂ := (σ : ℂ) - T * I
  have himT : |s.im| = T := by
    have him : s.im = -T := by simp [s]
    rw [him, abs_neg, abs_of_nonneg
      (le_trans (by norm_num : (0 : ℝ) ≤ 2) hT)]
  have him : (2 : ℝ) ≤ |s.im| := by rw [himT]; exact hT
  have h1s : (1 : ℂ) - s = (1 - σ : ℂ) + T * I := by
    simp [s]; ring
  have hz1 : riemannZeta (1 - s) ≠ 0 := by
    simpa [h1s, ofReal_sub, ofReal_one] using
      riemannZeta_ne_zero_of_landau_gap (A := A) (σ := 1 - σ)
        (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA) hT hgap
  intro hz0
  have hFE := riemannZeta_one_sub_factor (ne_neg_nat_of_two_le_abs_im him)
    (ne_one_of_two_le_abs_im him)
  rw [hFE, hz0, mul_zero] at hz1
  exact hz1 rfl

/-- Upper sliver `σ + iT` by conjugating the lower edge. -/
lemma sliverEdgeBound_posIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ (1 / 2 : ℝ))
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) :
    ‖logDeriv riemannZeta ((σ : ℂ) + T * I)‖ ≤
      A * sliverEdgeConst * (1 + Real.log T) ^ 3 := by
  have hT0 : 0 ≤ T := le_trans (by norm_num : (0 : ℝ) ≤ 2) hT
  have him : (2 : ℝ) ≤ |((σ : ℂ) - T * I).im| := by
    have : ((σ : ℂ) - T * I).im = -T := by simp
    rw [this, abs_neg, abs_of_nonneg hT0]
    exact hT
  have hs : ((σ : ℂ) - T * I) ≠ 1 := ne_one_of_two_le_abs_im him
  have hz := riemannZeta_ne_zero_of_sliver_negIm hA hT hσ1 hσ2 hgap
  have hconj : conj ((σ : ℂ) - T * I) = (σ : ℂ) + T * I := by
    simpa [sub_eq_add_neg, neg_neg] using conj_ofReal_add_real_mul_I σ (-T)
  rw [← hconj, norm_logDeriv_riemannZeta_conj hs hz]
  exact sliverEdgeBound_negIm hA hT hσ1 hσ2 hgap

lemma riemannZeta_ne_zero_of_sliver_posIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ (1 / 2 : ℝ))
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) :
    riemannZeta ((σ : ℂ) + T * I) ≠ 0 := by
  have hT0 : 0 ≤ T := le_trans (by norm_num : (0 : ℝ) ≤ 2) hT
  have him : (2 : ℝ) ≤ |((σ : ℂ) - T * I).im| := by
    have : ((σ : ℂ) - T * I).im = -T := by simp
    rw [this, abs_neg, abs_of_nonneg hT0]
    exact hT
  have hs : ((σ : ℂ) - T * I) ≠ 1 := ne_one_of_two_le_abs_im him
  have hz := riemannZeta_ne_zero_of_sliver_negIm hA hT hσ1 hσ2 hgap
  have hconj : conj ((σ : ℂ) - T * I) = (σ : ℂ) + T * I := by
    simpa [sub_eq_add_neg, neg_neg] using conj_ofReal_add_real_mul_I σ (-T)
  simpa [hconj] using riemannZeta_ne_zero_conj hs hz

lemma horizontalEdgeLandauBound_negIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    (hσ1 : (1 / 2 : ℝ) ≤ σ) (hσ2 : σ ≤ 2) :
    ‖logDeriv riemannZeta ((σ : ℂ) - T * I)‖ ≤
      (A * landauHorizontalConst) * (1 + Real.log T) ^ 3 := by
  have hs : ((σ : ℂ) + T * I) ≠ 1 := horizontal_ne_one (σ := σ) hT
  have hz : riemannZeta ((σ : ℂ) + T * I) ≠ 0 :=
    riemannZeta_ne_zero_of_landau_gap (A := A) (σ := σ)
      (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA) hT hgap
  rw [← conj_ofReal_add_real_mul_I σ T, norm_logDeriv_riemannZeta_conj hs hz]
  exact horizontalEdgeLandauBound_of_gap hA hT hgap hσ1 hσ2

lemma riemannZeta_ne_zero_of_landau_gap_negIm {T A σ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|) :
    riemannZeta ((σ : ℂ) - T * I) ≠ 0 := by
  have hs : ((σ : ℂ) + T * I) ≠ 1 := horizontal_ne_one (σ := σ) hT
  have hz : riemannZeta ((σ : ℂ) + T * I) ≠ 0 :=
    riemannZeta_ne_zero_of_landau_gap (A := A) (σ := σ)
      (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA) hT hgap
  simpa [conj_ofReal_add_real_mul_I] using riemannZeta_ne_zero_conj hs hz

/-- Glued horizontal bound on `σ ∈ [-1/16, 2]`, `|τ| = T ≥ 2`. -/
lemma horizontalEdgeBound_glued {T A σ τ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ 2)
    (hτ : |τ| = T) :
    ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤
      A * sliverEdgeConst * (1 + Real.log T) ^ 3 := by
  have hL : (1 : ℝ) ≤ 1 + Real.log T :=
    le_add_of_nonneg_right
      (Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT))
  have hscale
      (hle : ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤
        A * landauHorizontalConst * (1 + Real.log T) ^ 3) :
      ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤
        A * sliverEdgeConst * (1 + Real.log T) ^ 3 :=
    hle.trans (mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left landauHorizontalConst_le_sliverEdgeConst
        (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA))
      (pow_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 1) hL) 3))
  rcases eq_or_eq_neg_of_abs_eq hτ with hτp | hτn
  · subst hτp
    rcases le_total σ (1 / 2 : ℝ) with hlo | hhi
    · exact sliverEdgeBound_posIm hA hT hσ1 hlo hgap
    · exact hscale (horizontalEdgeLandauBound_of_gap hA hT hgap hhi hσ2)
  · subst hτn
    rcases le_total σ (1 / 2 : ℝ) with hlo | hhi
    · simpa [sub_eq_add_neg] using sliverEdgeBound_negIm hA hT hσ1 hlo hgap
    · refine hscale ?_
      simpa [sub_eq_add_neg] using
        horizontalEdgeLandauBound_negIm hA hT hgap hhi hσ2

lemma riemannZeta_ne_zero_of_glued_gap {T A σ τ : ℝ}
    (hA : (1 : ℝ) ≤ A) (hT : (2 : ℝ) ≤ T)
    (hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    (hσ1 : (-1 / 16 : ℝ) ≤ σ) (hσ2 : σ ≤ 2)
    (hτ : |τ| = T) :
    riemannZeta ((σ : ℂ) + τ * I) ≠ 0 := by
  rcases eq_or_eq_neg_of_abs_eq hτ with hτp | hτn
  · subst hτp
    rcases le_total σ (1 / 2 : ℝ) with hlo | hhi
    · exact riemannZeta_ne_zero_of_sliver_posIm hA hT hσ1 hlo hgap
    · exact riemannZeta_ne_zero_of_landau_gap (A := A) (σ := σ)
        (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1) hA) hT hgap
  · subst hτn
    rcases le_total σ (1 / 2 : ℝ) with hlo | hhi
    · simpa [sub_eq_add_neg] using
        riemannZeta_ne_zero_of_sliver_negIm hA hT hσ1 hlo hgap
    · simpa [sub_eq_add_neg] using
        riemannZeta_ne_zero_of_landau_gap_negIm (A := A) (σ := σ)
          hA hT hgap

lemma horizontal_ne_one_of_abs {σ τ T : ℝ}
    (hT : (2 : ℝ) ≤ T) (hτ : |τ| = T) :
    (σ : ℂ) + τ * I ≠ 1 := by
  have him : (2 : ℝ) ≤ |((σ : ℂ) + τ * I).im| := by
    simp
    rwa [hτ]
  exact ne_one_of_two_le_abs_im him

lemma norm_intervalIntegral_le_length_mul
    {f : ℝ → ℂ} {a b C : ℝ} (hab : a ≤ b)
    (hf : IntervalIntegrable f volume a b)
    (hbd : ∀ x, a ≤ x → x ≤ b → ‖f x‖ ≤ C) :
    ‖∫ x in a..b, f x‖ ≤ (b - a) * C := by
  have hC : 0 ≤ C :=
    (norm_nonneg (f a)).trans (hbd a le_rfl hab)
  refine (intervalIntegral.norm_integral_le_integral_norm hab).trans ?_
  have hnorm : IntervalIntegrable (fun x => ‖f x‖) volume a b := hf.norm
  have hconst : IntervalIntegrable (fun _ : ℝ => C) volume a b :=
    intervalIntegrable_const
  refine (intervalIntegral.integral_mono_on hab hnorm hconst
    fun x hx => hbd x hx.1 hx.2).trans_eq ?_
  simp [intervalIntegral.integral_const, smul_eq_mul,
    abs_of_nonneg (sub_nonneg.mpr hab)]

/-- Length × sup bound for a horizontal edge of `(ζ′/ζ) ĥ`.
The edge must miss zeros and the pole so the integrand is continuous.
`|ζ′/ζ|` is an input (Landau on `[1/2, 2]`; FE/`ψ` on the sliver). -/
lemma norm_horizontal_logDeriv_hat_integral_le
    (F : FullWeilTest) {σ₁ σ₂ τ B : ℝ}
    (hσ : σ₁ ≤ σ₂) (hB : 0 ≤ B)
    (hne1 : ∀ σ, σ ∈ Icc σ₁ σ₂ → (σ : ℂ) + τ * I ≠ 1)
    (hnz : ∀ σ, σ ∈ Icc σ₁ σ₂ → riemannZeta ((σ : ℂ) + τ * I) ≠ 0)
    (hbd : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤ B) :
    ∃ C : ℝ, 0 ≤ C ∧
      ‖∫ x : ℝ in σ₁..σ₂,
          logDeriv riemannZeta ((x : ℂ) + τ * I) *
            F.hat ((x : ℂ) + τ * I)‖ ≤
        (σ₂ - σ₁) * B * C / (1 + τ ^ 2) := by
  obtain ⟨C, hC0, hhat⟩ := F.norm_hat_le_inv_sq_on_Icc σ₁ σ₂
  refine ⟨C, hC0, ?_⟩
  set f : ℝ → ℂ := fun x =>
    logDeriv riemannZeta ((x : ℂ) + τ * I) * F.hat ((x : ℂ) + τ * I)
  have hpathOn : ContinuousOn (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂) :=
    continuous_ofReal.continuousOn.add continuousOn_const
  have hlogOn : ContinuousOn (logDeriv riemannZeta)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := hz
    exact (analyticAt_logDeriv_riemannZeta (hne1 x hx) (hnz x hx)).continuousAt.continuousWithinAt
  have hFOn : ContinuousOn F.hat
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    fun _ _ => (F.analyticAt_hat _).continuousAt.continuousWithinAt
  have hmaps : Set.MapsTo (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    Set.mapsTo_image _ _
  have hcont : ContinuousOn f (Icc σ₁ σ₂) :=
    (hlogOn.comp hpathOn hmaps).mul (hFOn.comp hpathOn hmaps)
  have hf : IntervalIntegrable f volume σ₁ σ₂ :=
    hcont.intervalIntegrable_of_Icc hσ
  have hbound : ∀ x, σ₁ ≤ x → x ≤ σ₂ → ‖f x‖ ≤ B * C / (1 + τ ^ 2) := by
    intro x hx1 hx2
    have hx : x ∈ Icc σ₁ σ₂ := ⟨hx1, hx2⟩
    have hζ := hbd x hx
    have hh := hhat ((x : ℂ) + τ * I) (by simp [hx])
    have him : ((x : ℂ) + τ * I).im = τ := by simp
    dsimp [f]
    rw [norm_mul]
    have := mul_le_mul hζ (by simpa [him] using hh) (norm_nonneg _) hB
    simpa [mul_div_assoc] using this
  have hle := norm_intervalIntegral_le_length_mul hσ hf hbound
  have : (σ₂ - σ₁) * (B * C / (1 + τ ^ 2)) =
      (σ₂ - σ₁) * B * C / (1 + τ ^ 2) := by ring
  exact hle.trans_eq this

/-- Same bound with a pre-chosen hat constant (uniform in the height). -/
lemma norm_horizontal_logDeriv_hat_integral_le_with
    (F : FullWeilTest) {σ₁ σ₂ τ B C : ℝ}
    (hσ : σ₁ ≤ σ₂) (hB : 0 ≤ B) (hC0 : 0 ≤ C)
    (hne1 : ∀ σ, σ ∈ Icc σ₁ σ₂ → (σ : ℂ) + τ * I ≠ 1)
    (hnz : ∀ σ, σ ∈ Icc σ₁ σ₂ → riemannZeta ((σ : ℂ) + τ * I) ≠ 0)
    (hbd : ∀ σ, σ ∈ Icc σ₁ σ₂ →
      ‖logDeriv riemannZeta ((σ : ℂ) + τ * I)‖ ≤ B)
    (hhat : ∀ s : ℂ, s.re ∈ Icc σ₁ σ₂ →
      ‖F.hat s‖ ≤ C / (1 + s.im ^ 2)) :
    ‖∫ x : ℝ in σ₁..σ₂,
        logDeriv riemannZeta ((x : ℂ) + τ * I) *
          F.hat ((x : ℂ) + τ * I)‖ ≤
      (σ₂ - σ₁) * B * C / (1 + τ ^ 2) := by
  set f : ℝ → ℂ := fun x =>
    logDeriv riemannZeta ((x : ℂ) + τ * I) * F.hat ((x : ℂ) + τ * I)
  have hpathOn : ContinuousOn (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂) :=
    continuous_ofReal.continuousOn.add continuousOn_const
  have hlogOn : ContinuousOn (logDeriv riemannZeta)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) := by
    intro z hz
    obtain ⟨x, hx, rfl⟩ := hz
    exact (analyticAt_logDeriv_riemannZeta (hne1 x hx)
      (hnz x hx)).continuousAt.continuousWithinAt
  have hFOn : ContinuousOn F.hat
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    fun _ _ => (F.analyticAt_hat _).continuousAt.continuousWithinAt
  have hmaps : Set.MapsTo (fun x : ℝ => (x : ℂ) + τ * I) (Icc σ₁ σ₂)
      ((fun x : ℝ => (x : ℂ) + τ * I) '' Icc σ₁ σ₂) :=
    Set.mapsTo_image _ _
  have hcont : ContinuousOn f (Icc σ₁ σ₂) :=
    (hlogOn.comp hpathOn hmaps).mul (hFOn.comp hpathOn hmaps)
  have hf : IntervalIntegrable f volume σ₁ σ₂ :=
    hcont.intervalIntegrable_of_Icc hσ
  have hbound : ∀ x, σ₁ ≤ x → x ≤ σ₂ → ‖f x‖ ≤ B * C / (1 + τ ^ 2) := by
    intro x hx1 hx2
    have hx : x ∈ Icc σ₁ σ₂ := ⟨hx1, hx2⟩
    have hζ := hbd x hx
    have hh := hhat ((x : ℂ) + τ * I) (by simp [hx])
    have him : ((x : ℂ) + τ * I).im = τ := by simp
    dsimp [f]
    rw [norm_mul]
    have := mul_le_mul hζ (by simpa [him] using hh) (norm_nonneg _) hB
    simpa [mul_div_assoc] using this
  have hle := norm_intervalIntegral_le_length_mul hσ hf hbound
  have : (σ₂ - σ₁) * (B * C / (1 + τ ^ 2)) =
      (σ₂ - σ₁) * B * C / (1 + τ ^ 2) := by ring
  exact hle.trans_eq this

/-- r528: full horizontals `[-1/16, 2]` along the Landau gap
sequence.  Closed by the glued `|ζ′/ζ|` bound and `log³/T² → 0`. -/
def HorizontalEdgesTendstoZero : Prop :=
  ∀ F : FullWeilTest,
    ∃ T : ℕ → ℝ,
      (∀ k : ℕ, ((2 * k + 1 : ℕ) : ℝ) ≤ T k) ∧
      Tendsto T atTop atTop ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + T k * I) *
            F.hat ((x : ℂ) + T k * I)) atTop (nhds 0) ∧
      Tendsto (fun k =>
        ∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
            F.hat ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0)

lemma tendsto_one_add_log_cubed_div_one_add_sq :
    Tendsto (fun t : ℝ => (1 + Real.log t) ^ 3 / (1 + t ^ 2))
      atTop (nhds 0) := by
  have hlog : Tendsto (fun t : ℝ => Real.log t ^ 3 / t ^ 2)
      atTop (nhds 0) := by
    have h := Real.tendsto_pow_log_div_mul_add_atTop (1 : ℝ) 0 3 one_ne_zero
    have hinv : Tendsto (fun t : ℝ => t⁻¹) atTop (nhds 0) :=
      tendsto_inv_atTop_zero
    have hmul : Tendsto
        (fun t : ℝ => (Real.log t ^ 3 / (1 * t + 0)) * t⁻¹)
        atTop (nhds 0) := by
      convert h.mul hinv
      rw [mul_zero]
    refine hmul.congr' ?_
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with t ht
    simp [one_mul, add_zero]
    field_simp [ht.ne']
  have hle : ∀ᶠ t in atTop,
      0 ≤ (1 + Real.log t) ^ 3 / (1 + t ^ 2) ∧
        (1 + Real.log t) ^ 3 / (1 + t ^ 2) ≤
          8 * (Real.log t ^ 3 / t ^ 2) := by
    filter_upwards [eventually_ge_atTop (3 : ℝ)] with t ht
    have ht0 : (0 : ℝ) < t := lt_of_lt_of_le (by norm_num : (0 : ℝ) < 3) ht
    have ht1 : (1 : ℝ) ≤ t := le_trans (by norm_num : (1 : ℝ) ≤ 3) ht
    have hlog0 : 0 ≤ Real.log t := Real.log_nonneg ht1
    have hlog1 : (1 : ℝ) ≤ Real.log t := by
      rw [Real.le_log_iff_exp_le ht0]
      exact le_trans Real.exp_one_lt_three.le ht
    have h1 : 1 + Real.log t ≤ 2 * Real.log t := by linarith
    have hnum : (1 + Real.log t) ^ 3 ≤ (2 * Real.log t) ^ 3 :=
      pow_le_pow_left₀ (add_nonneg (by norm_num : (0 : ℝ) ≤ 1) hlog0) h1 3
    have h8 : (2 * Real.log t) ^ 3 = 8 * Real.log t ^ 3 := by ring
    have hden : t ^ 2 ≤ 1 + t ^ 2 := le_add_of_nonneg_left (by norm_num)
    have hnum8 : (1 + Real.log t) ^ 3 ≤ 8 * Real.log t ^ 3 := by
      rwa [← h8]
    have hnn : 0 ≤ (1 + Real.log t) ^ 3 / (1 + t ^ 2) :=
      div_nonneg (pow_nonneg (add_nonneg (by norm_num : (0 : ℝ) ≤ 1) hlog0) 3)
        (add_nonneg (by norm_num : (0 : ℝ) ≤ 1) (sq_nonneg t))
    refine ⟨hnn, ?_⟩
    have h1' : (1 + Real.log t) ^ 3 / (1 + t ^ 2) ≤
        (1 + Real.log t) ^ 3 / t ^ 2 :=
      div_le_div_of_nonneg_left
        (pow_nonneg (add_nonneg (by norm_num : (0 : ℝ) ≤ 1) hlog0) 3)
        (pow_pos ht0 2) hden
    have h2' : (1 + Real.log t) ^ 3 / t ^ 2 ≤
        (8 * Real.log t ^ 3) / t ^ 2 :=
      div_le_div_of_nonneg_right hnum8 (pow_nonneg ht0.le 2)
    have h3' : (8 * Real.log t ^ 3) / t ^ 2 =
        8 * (Real.log t ^ 3 / t ^ 2) := by ring
    exact h1'.trans (h2'.trans_eq h3')
  refine squeeze_zero' (hle.mono fun _ h => h.1) (hle.mono fun _ h => h.2) ?_
  convert hlog.const_mul (8 : ℝ)
  rw [mul_zero]

theorem horizontalEdgesTendstoZero : HorizontalEdgesTendstoZero := by
  intro F
  obtain ⟨T, hTbd, hgapP, _hgapN⟩ := exists_gap_sequence_landau
  obtain ⟨C, hC0, hhat⟩ := F.norm_hat_le_inv_sq_on_Icc (-1 / 16 : ℝ) 2
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
      (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA)) sliverEdgeConst_nonneg) hC0
  have hlen : (2 : ℝ) - (-1 / 16) = 2 + 1 / 16 := by ring
  have hedge (τ : ℕ → ℝ) (hτ : ∀ k, |τ k| = T k) (k : ℕ) :
      ‖∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + τ k * I) *
            F.hat ((x : ℂ) + τ k * I)‖ ≤
        K * (L k ^ 3 / (1 + T k ^ 2)) := by
    have hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (A * (1 + Real.log (T k))) ≤ |ρ.im - T k| := hgapP k
    have hbd : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
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
    have hle := norm_horizontal_logDeriv_hat_integral_le_with
      F hσ (hB0 k) hC0 hne1 hnz hbd hhat
    have hsq : 1 + τ k ^ 2 = 1 + T k ^ 2 := by
      have : |τ k| ^ 2 = T k ^ 2 := by simp [hτ]
      simpa [sq_abs] using this
    convert hle using 1
    unfold B L K
    rw [hsq, hlen]
    ring
  have hdecay : Tendsto (fun k => L k ^ 3 / (1 + T k ^ 2))
      atTop (nhds 0) :=
    tendsto_one_add_log_cubed_div_one_add_sq.comp hTtop
  have hpos := hedge (fun k => T k)
    (fun k => abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k)))
  have hneg := hedge (fun k => -(T k)) (fun k => by simp [abs_neg,
    abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k))])
  have hnorm {I : ℕ → ℂ}
      (hle : ∀ k, ‖I k‖ ≤ K * (L k ^ 3 / (1 + T k ^ 2))) :
      Tendsto I atTop (nhds 0) :=
    tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero (fun _ => norm_nonneg _) hle (by
        convert hdecay.const_mul K
        rw [mul_zero]))
  refine ⟨T, hTlo, hTtop, hnorm hpos, hnorm hneg⟩

/-- r529: Dirichlet comparison on the FE dual line `Re ≥ 17/16`. -/
lemma norm_logDeriv_riemannZeta_le_at_seventeen_sixteen {s : ℂ}
    (hs : (17 / 16 : ℝ) ≤ s.re) :
    ‖logDeriv riemannZeta s‖ ≤
      ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ :=
  norm_logDeriv_riemannZeta_le_of_re_ge (by norm_num : (1 : ℝ) < 17 / 16) hs

lemma riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hs : s.re = -1 / 16) : riemannZeta s ≠ 0 :=
  riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero
    (by linarith [hs] : (-1 / 4 : ℝ) < s.re)
    (by linarith [hs] : s.re < 0)

/-- Explicit log-linear constant on `Re = -1/16`, `|Im| ≥ 2`. -/
noncomputable def leftEdgeConst : ℝ :=
  ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ +
    (6 + |Real.eulerMascheroniConstant|) +
    Real.log (2 * Real.pi) + (1 / 2 : ℝ) +
    (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)

lemma leftEdgeConst_nonneg : 0 ≤ leftEdgeConst := by
  unfold leftEdgeConst
  have hlog : 0 ≤ Real.log (2 * Real.pi) :=
    Real.log_nonneg (by nlinarith [Real.pi_gt_three])
  positivity

/-- Gap-free left-edge bound: FE + Dirichlet at `17/16` + sliver `ψ`/`tan`. -/
lemma left_edge_logDeriv_bound {s : ℂ}
    (hre : s.re = -1 / 16) (him : (2 : ℝ) ≤ |s.im|) :
    ‖logDeriv riemannZeta s‖ ≤
      leftEdgeConst * (1 + Real.log (2 + |s.im|)) := by
  have hz : riemannZeta s ≠ 0 :=
    riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen hre
  have hid := logDeriv_riemannZeta_functional him hz
  have hG : ∀ n : ℕ, s ≠ -n := ne_neg_nat_of_two_le_abs_im him
  have hcos := cos_pi_div_two_ne_zero_of_two_le_abs_im him
  have hFE := logDeriv_zetaFEFactor hG hcos
  have hre1 : (-1 / 16 : ℝ) ≤ s.re := le_of_eq hre.symm
  have hre2 : s.re ≤ (1 / 2 : ℝ) := by linarith [hre]
  have hψ := norm_digamma_le_log_of_sliver hre1 hre2 him
  have htan :=
    norm_tan_le_of_two_le_abs_im (z := Real.pi * s / 2)
      (two_le_abs_im_pi_div_two him)
  have hdualre : (17 / 16 : ℝ) ≤ (1 - s).re := by
    simp [sub_re, hre]
    norm_num
  have hdual :=
    norm_logDeriv_riemannZeta_le_at_seventeen_sixteen hdualre
  have hπtan : ‖((Real.pi : ℂ) / 2) * tan (Real.pi * s / 2)‖ ≤
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2) := by
    have hπ : ‖(Real.pi : ℂ)‖ = Real.pi := by
      simp [Complex.norm_real, abs_of_pos Real.pi_pos]
    have h2 : ‖(2 : ℂ)‖ = 2 := by norm_num
    rw [norm_mul, norm_div, hπ, h2]
    exact mul_le_mul_of_nonneg_left htan
      (div_nonneg Real.pi_pos.le (by norm_num))
  have hGnorm : ‖logDeriv zetaFEFactor s‖ ≤
      (6 + |Real.eulerMascheroniConstant|) *
        (1 + Real.log (2 + |s.im|)) +
        (Real.log (2 * Real.pi) + 1 / 2 +
          (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)) := by
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
  have htri : ‖logDeriv riemannZeta s‖ ≤
      ‖logDeriv riemannZeta (1 - s)‖ + ‖logDeriv zetaFEFactor s‖ := by
    rw [hid]
    simpa using
      (norm_sub_le (-logDeriv riemannZeta (1 - s)) (logDeriv zetaFEFactor s))
  set L : ℝ := 1 + Real.log (2 + |s.im|)
  have hL : (1 : ℝ) ≤ L := by
    have : 0 ≤ Real.log (2 + |s.im|) :=
      Real.log_nonneg (by nlinarith [abs_nonneg s.im])
    exact le_add_of_nonneg_right this
  set D : ℝ := ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖
  set Cψ : ℝ := 6 + |Real.eulerMascheroniConstant|
  set C0 : ℝ :=
    Real.log (2 * Real.pi) + 1 / 2 +
      (Real.pi / 2) * Real.sqrt (1 + 1 / Real.sinh 2 ^ 2)
  have hpack : D + Cψ * L + C0 ≤ (D + Cψ + C0) * L := by
    have hD : 0 ≤ D := norm_nonneg _
    have hCψ : 0 ≤ Cψ := by unfold Cψ; positivity
    have hC0 : 0 ≤ C0 := by
      unfold C0
      have : 0 ≤ Real.log (2 * Real.pi) :=
        Real.log_nonneg (by nlinarith [Real.pi_gt_three])
      positivity
    nlinarith [hL, hD, hCψ, hC0]
  have hsum : ‖logDeriv riemannZeta s‖ ≤ D + Cψ * L + C0 :=
    (htri.trans (add_le_add hdual hGnorm)).trans_eq (by ring)
  have hC : D + Cψ + C0 = leftEdgeConst := by
    unfold leftEdgeConst D Cψ C0; ring
  simpa [L, hC] using hsum.trans hpack

/-- Restated from `Re = -1/4` to the r522 contour `Re = -1/16`. -/
def LeftEdgeLogDerivBound : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧
    ∀ {s : ℂ}, s.re = -1 / 16 → (2 : ℝ) ≤ |s.im| →
      ‖logDeriv riemannZeta s‖ ≤ C * (1 + Real.log (2 + |s.im|))

theorem leftEdgeLogDerivBound : LeftEdgeLogDerivBound :=
  ⟨leftEdgeConst, leftEdgeConst_nonneg,
    fun hre him => left_edge_logDeriv_bound hre him⟩

lemma right_edge_logDeriv_bound {s : ℂ} (hre : s.re = 2) :
    ‖logDeriv riemannZeta s‖ ≤ ‖logDeriv riemannZeta (2 : ℂ)‖ :=
  norm_logDeriv_riemannZeta_le_at_two (by simp [hre])

/-- Pointwise majorant of the left integrand for `|τ| ≥ 2`. -/
lemma left_edge_integrand_norm_le (F : FullWeilTest) {C : ℝ}
    (hhat : ∀ s : ℂ, |s.re| ≤ (1 / 16 : ℝ) →
      ‖F.hat s‖ ≤ C / (1 + s.im ^ 2))
    {τ : ℝ} (hτ : (2 : ℝ) ≤ |τ|) :
    ‖logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)‖ ≤
      leftEdgeConst * C * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) := by
  have hre : (((-1 / 16 : ℝ) : ℂ) + τ * I).re = -1 / 16 := by simp
  have him : (2 : ℝ) ≤ |(((-1 / 16 : ℝ) : ℂ) + τ * I).im| := by
    simpa using hτ
  have hζ := left_edge_logDeriv_bound hre him
  have habs : |(((-1 / 16 : ℝ) : ℂ) + τ * I).re| ≤ (1 / 16 : ℝ) := by
    simp [hre]
    norm_num
  have hh := hhat _ habs
  have himτ : (((-1 / 16 : ℝ) : ℂ) + τ * I).im = τ := by simp
  have hζ' : ‖logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I)‖ ≤
      leftEdgeConst * (1 + Real.log (2 + |τ|)) := by
    simpa [himτ] using hζ
  have hL : 0 ≤ 1 + Real.log (2 + |τ|) :=
    add_nonneg (by norm_num)
      (Real.log_nonneg (by nlinarith [abs_nonneg τ]))
  rw [norm_mul]
  have := mul_le_mul hζ' (by simpa [himτ] using hh) (norm_nonneg _)
    (mul_nonneg leftEdgeConst_nonneg hL)
  simpa [mul_div_assoc, mul_assoc, mul_left_comm, mul_comm C] using this

/-- Pointwise majorant of the right integrand on the whole line. -/
lemma right_edge_integrand_norm_le (F : FullWeilTest) {C : ℝ}
    (hhat : ∀ s : ℂ, |s.re| ≤ 2 →
      ‖F.hat s‖ ≤ C / (1 + s.im ^ 2))
    (τ : ℝ) :
    ‖logDeriv riemannZeta ((2 : ℂ) + τ * I) *
        F.hat ((2 : ℂ) + τ * I)‖ ≤
      ‖logDeriv riemannZeta (2 : ℂ)‖ * C / (1 + τ ^ 2) := by
  have hre : ((2 : ℂ) + τ * I).re = 2 := by simp
  have hζ := right_edge_logDeriv_bound hre
  have habs : |((2 : ℂ) + τ * I).re| ≤ 2 := by
    simp [hre]
  have hh := hhat _ habs
  have himτ : ((2 : ℂ) + τ * I).im = τ := by simp
  rw [norm_mul]
  have := mul_le_mul hζ (by simpa [himτ] using hh) (norm_nonneg _)
    (norm_nonneg _)
  simpa [mul_div_assoc] using this

/-- A two-sided Landau gap forbids zeros on the horizontal sides. -/
lemma abs_im_lt_of_landau_gaps {T A : ℝ} {σ₁ σ₂ : ℝ} {ρ : ℂ}
    (hA : (0 : ℝ) < A) (hT : (2 : ℝ) ≤ T)
    (hgapP : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im - T|)
    (hgapN : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (A * (1 + Real.log T)) ≤ |ρ.im + T|)
    (hρ : ρ ∈ riemannZetaZerosOnClosedRect σ₁ σ₂ T) :
    |ρ.im| < T := by
  have hmem := mem_riemannZetaZerosOnClosedRect.mp hρ
  have hrect := mem_zetaClosedRect.mp hmem.1
  have hle : |ρ.im| ≤ T := abs_le.mpr ⟨hrect.2.2.1, hrect.2.2.2⟩
  refine lt_of_le_of_ne hle ?_
  intro heq
  have hdenpos : 0 < A * (1 + Real.log T) := by
    have hlog : 0 ≤ Real.log T :=
      Real.log_nonneg (le_trans (by norm_num : (1 : ℝ) ≤ 2) hT)
    exact mul_pos hA (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 1)
      (le_add_of_nonneg_right hlog))
  have hpos : 0 < 1 / (A * (1 + Real.log T)) := one_div_pos.mpr hdenpos
  rcases eq_or_eq_neg_of_abs_eq heq with hp | hn
  · have hgap := hgapP ρ hmem.2.1 hmem.2.2
    rw [hp, sub_self, abs_zero] at hgap
    exact (lt_irrefl (0 : ℝ) (hpos.trans_le hgap)).elim
  · have hgap := hgapN ρ hmem.2.1 hmem.2.2
    rw [hn, neg_add_cancel, abs_zero] at hgap
    exact (lt_irrefl (0 : ℝ) (hpos.trans_le hgap)).elim

/-- Intended `T→∞` identity (proved below as a theorem). -/
def ContourIdentityLimitAlongGaps : Prop :=
  ∀ F : FullWeilTest,
    I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          F.hat ((2 : ℂ) + τ * I)) -
      I • (∫ τ : ℝ, logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)) =
      (2 * (Real.pi : ℂ) * I) *
        ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) -
          F.hat 1)

/-- Vertical line path `τ ↦ σ + τ I`. Named so composition does not
elaborate `+` as a function `HAdd`. -/
lemma continuous_vertical_path (σ : ℝ) :
    Continuous (fun τ : ℝ => (σ : ℂ) + τ * I) :=
  continuous_const.add (continuous_ofReal.mul continuous_const)

lemma ne_one_of_re_eq {σ : ℝ} (hσ : σ ≠ 1) (τ : ℝ) :
    (σ : ℂ) + τ * I ≠ 1 := by
  intro h
  have : σ = 1 := by
    simpa using congrArg Complex.re h
  exact hσ this

lemma continuous_logDeriv_hat_vertical
    (F : FullWeilTest) (σ : ℝ)
    (h1 : σ ≠ 1)
    (hz : ∀ τ : ℝ, riemannZeta ((σ : ℂ) + τ * I) ≠ 0) :
    Continuous (fun τ : ℝ =>
      logDeriv riemannZeta ((σ : ℂ) + τ * I) *
        F.hat ((σ : ℂ) + τ * I)) := by
  set path : ℝ → ℂ := fun τ => (σ : ℂ) + τ * I
  have hpath : Continuous path := continuous_vertical_path σ
  have hlog : Continuous (fun τ : ℝ => logDeriv riemannZeta (path τ)) :=
    continuous_iff_continuousAt.mpr fun τ =>
      ContinuousAt.comp (f := path) (g := logDeriv riemannZeta)
        (analyticAt_logDeriv_riemannZeta
          (show path τ ≠ 1 from ne_one_of_re_eq h1 τ)
          (by simpa [path] using hz τ)).continuousAt
        (hpath.continuousAt (x := τ))
  have hhat : Continuous (fun τ : ℝ => F.hat (path τ)) :=
    continuous_iff_continuousAt.mpr fun τ =>
      ContinuousAt.comp (f := path) (g := F.hat)
        (F.analyticAt_hat (path τ)).continuousAt
        (hpath.continuousAt (x := τ))
  simpa [path] using hlog.mul hhat

lemma continuous_right_edge_integrand (F : FullWeilTest) :
    Continuous (fun τ : ℝ =>
      logDeriv riemannZeta ((2 : ℂ) + τ * I) *
        F.hat ((2 : ℂ) + τ * I)) :=
  continuous_logDeriv_hat_vertical F 2 (by norm_num)
    (fun τ => riemannZeta_ne_zero_of_re_eq_two (by simp))

lemma continuous_left_edge_integrand (F : FullWeilTest) :
    Continuous (fun τ : ℝ =>
      logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)) :=
  continuous_logDeriv_hat_vertical F (-1 / 16) (by norm_num)
    (fun τ => riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen (by simp))

lemma integrable_right_edge_integrand (F : FullWeilTest) :
    Integrable (fun τ : ℝ =>
      logDeriv riemannZeta ((2 : ℂ) + τ * I) *
        F.hat ((2 : ℂ) + τ * I)) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le 2 (by norm_num)
  set f : ℝ → ℂ := fun τ =>
    logDeriv riemannZeta ((2 : ℂ) + τ * I) * F.hat ((2 : ℂ) + τ * I)
  set K : ℝ := ‖logDeriv riemannZeta (2 : ℂ)‖ * C
  have hK0 : 0 ≤ K := mul_nonneg (norm_nonneg _) hC0
  have hbd : ∀ τ, ‖f τ‖ ≤ K / (1 + τ ^ 2) := fun τ =>
    right_edge_integrand_norm_le F hhat τ
  have hmaj : Integrable (fun τ : ℝ => K * (1 + τ ^ 2)⁻¹) :=
    integrable_inv_one_add_sq.const_mul K
  have hmaj' : Integrable (fun τ : ℝ => K / (1 + τ ^ 2)) := by
    simpa [div_eq_mul_inv] using hmaj
  exact hmaj'.mono' (continuous_right_edge_integrand F).aestronglyMeasurable
    (Filter.Eventually.of_forall hbd)

/-- `1 + log(2+|τ|) ≤ (1+log 3 + 8) (1+τ²)^{1/8}`. -/
lemma one_add_log_le_rpow_eighth (τ : ℝ) :
    1 + Real.log (2 + |τ|) ≤
      (1 + Real.log 3 + 8) * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) := by
  have hbase : (1 : ℝ) ≤ 1 + τ ^ 2 := by nlinarith [sq_nonneg τ]
  have hu : (1 : ℝ) ≤ (1 + τ ^ 2) ^ (8⁻¹ : ℝ) :=
    Real.one_le_rpow hbase (by norm_num)
  have hlogsq : Real.log (1 + τ ^ 2) ≤
      8 * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) := by
    have hpos : 0 < 1 + τ ^ 2 := by nlinarith [sq_nonneg τ]
    have hpow : 0 < (1 + τ ^ 2) ^ (8⁻¹ : ℝ) :=
      Real.rpow_pos_of_pos hpos _
    have := Real.log_le_sub_one_of_pos hpow
    have hlogpow :
        Real.log ((1 + τ ^ 2) ^ (8⁻¹ : ℝ)) =
          (8⁻¹ : ℝ) * Real.log (1 + τ ^ 2) :=
      Real.log_rpow hpos _
    have h8 : Real.log (1 + τ ^ 2) ≤
        8 * ((1 + τ ^ 2) ^ (8⁻¹ : ℝ) - 1) := by
      have : (8⁻¹ : ℝ) * Real.log (1 + τ ^ 2) ≤
          (1 + τ ^ 2) ^ (8⁻¹ : ℝ) - 1 := by
        simpa [hlogpow] using this
      have := mul_le_mul_of_nonneg_left this (by norm_num : (0 : ℝ) ≤ 8)
      simpa [mul_sub, mul_assoc, inv_mul_cancel₀ (by norm_num : (8 : ℝ) ≠ 0)]
        using this
    nlinarith [h8, hu]
  have hcmp : 2 + |τ| ≤ 3 * (1 + τ ^ 2) := by
    have hsq : 0 ≤ (|τ| - 1) ^ 2 := sq_nonneg _
    have : (2 : ℝ) * |τ| ≤ 1 + τ ^ 2 := by
      nlinarith [hsq, sq_abs τ]
    nlinarith [abs_nonneg τ]
  have hpos2 : 0 < 2 + |τ| := by positivity
  have hlogle : Real.log (2 + |τ|) ≤ Real.log 3 + Real.log (1 + τ ^ 2) := by
    have := Real.log_le_log hpos2 hcmp
    have hmul : Real.log (3 * (1 + τ ^ 2)) =
        Real.log 3 + Real.log (1 + τ ^ 2) :=
      Real.log_mul (by norm_num) (by nlinarith [sq_nonneg τ])
    exact this.trans_eq hmul
  have hsum : 1 + Real.log (2 + |τ|) ≤
      1 + Real.log 3 + 8 * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) := by
    have : Real.log (2 + |τ|) ≤
        Real.log 3 + 8 * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) :=
      hlogle.trans (by linarith [hlogsq])
    linarith
  have hpack : 1 + Real.log 3 + 8 * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) ≤
      (1 + Real.log 3 + 8) * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) := by
    have hc : 0 ≤ 1 + Real.log 3 :=
      add_nonneg (by norm_num) (Real.log_nonneg (by norm_num))
    nlinarith [hu, hc]
  exact hsum.trans hpack

lemma integrable_one_add_log_mul_inv_sq :
    Integrable (fun τ : ℝ =>
      (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2)) := by
  have hr : (1 : ℝ) < 7 / 4 := by norm_num
  have hpow : Integrable
      (fun τ : ℝ => (1 + ‖τ‖ ^ 2) ^ (-(7 / 4 : ℝ) / 2)) :=
    integrable_rpow_neg_one_add_norm_sq
      (by norm_num : (Module.finrank ℝ ℝ : ℝ) < 7 / 4)
  have hpow' : Integrable (fun τ : ℝ => (1 + τ ^ 2) ^ (-(7 / 8 : ℝ))) := by
    convert hpow using 1
    ext τ
    simp [sq_abs]
    ring_nf
  set C : ℝ := 1 + Real.log 3 + 8
  have hC0 : 0 ≤ C := by
    unfold C
    exact add_nonneg (add_nonneg (by norm_num)
      (Real.log_nonneg (by norm_num))) (by norm_num)
  have hnn : ∀ τ : ℝ,
      0 ≤ (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) := fun τ =>
    div_nonneg
      (add_nonneg (by norm_num)
        (Real.log_nonneg (by nlinarith [abs_nonneg τ])))
      (by nlinarith [sq_nonneg τ])
  have hbd : ∀ τ,
      (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) ≤
        C * (1 + τ ^ 2) ^ (-(7 / 8 : ℝ)) := by
    intro τ
    have hden : 0 < 1 + τ ^ 2 := by nlinarith [sq_nonneg τ]
    have hle := one_add_log_le_rpow_eighth τ
    have hrw : C * (1 + τ ^ 2) ^ (8⁻¹ : ℝ) / (1 + τ ^ 2) =
        C * (1 + τ ^ 2) ^ (-(7 / 8 : ℝ)) := by
      have hexp : (8⁻¹ : ℝ) = (1 : ℝ) / 8 := by norm_num
      have : (1 + τ ^ 2) ^ ((1 : ℝ) / 8) / (1 + τ ^ 2) =
          (1 + τ ^ 2) ^ (-(7 / 8 : ℝ)) := by
        have hadd := (Real.rpow_add hden ((1 : ℝ) / 8) (-1)).symm
        have hsum : (1 : ℝ) / 8 + -1 = -(7 / 8) := by norm_num
        rw [div_eq_mul_inv, ← Real.rpow_neg_one, hadd, hsum]
      rw [hexp, mul_div_assoc, this]
    exact (div_le_div_of_nonneg_right hle hden.le).trans_eq hrw
  have hmaj : Integrable
      (fun τ : ℝ => C * (1 + τ ^ 2) ^ (-(7 / 8 : ℝ))) :=
    hpow'.const_mul C
  have hmeas : AEStronglyMeasurable
      (fun τ : ℝ => (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2)) volume := by
    refine Continuous.aestronglyMeasurable ?_
    refine Continuous.div ?_ (continuous_const.add (continuous_pow 2))
      (fun τ => by nlinarith [sq_nonneg τ])
    exact continuous_const.add
      (Real.continuousOn_log.comp_continuous
        (continuous_const.add continuous_abs)
        fun x => ne_of_gt (add_pos_of_pos_of_nonneg
          (by norm_num : (0 : ℝ) < 2) (abs_nonneg x)))
  exact hmaj.mono' hmeas (Filter.Eventually.of_forall fun τ => by
    rw [Real.norm_eq_abs, abs_of_nonneg (hnn τ)]
    exact hbd τ)

lemma exists_left_edge_compact_bound (F : FullWeilTest) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ τ : ℝ, |τ| ≤ 2 →
      ‖logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)‖ ≤ M := by
  set f : ℝ → ℂ := fun τ =>
    logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
      F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)
  have hOn : ContinuousOn f (Icc (-2 : ℝ) 2) :=
    (continuous_left_edge_integrand F).continuousOn
  obtain ⟨M, hM⟩ :=
    isCompact_Icc.exists_bound_of_continuousOn hOn
  refine ⟨M, ?_, ?_⟩
  · exact le_trans (norm_nonneg (f 0))
      (hM 0 ⟨by norm_num, by norm_num⟩)
  · intro τ hτ
    exact hM τ (abs_le.mp hτ)

lemma integrable_left_edge_integrand (F : FullWeilTest) :
    Integrable (fun τ : ℝ =>
      logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le (1 / 16) (by norm_num)
  obtain ⟨M, hM0, hM⟩ := exists_left_edge_compact_bound F
  set f : ℝ → ℂ := fun τ =>
    logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
      F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)
  set K : ℝ := leftEdgeConst * C
  have hK0 : 0 ≤ K := mul_nonneg leftEdgeConst_nonneg hC0
  set g : ℝ → ℝ := fun τ =>
    Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ +
      K * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2)
  have hind : Integrable
      (Set.indicator (Icc (-2 : ℝ) 2) (fun _ : ℝ => M)) :=
    (continuousOn_const.integrableOn_compact isCompact_Icc).integrable_indicator
      measurableSet_Icc
  have hlog := integrable_one_add_log_mul_inv_sq.const_mul K
  have hlog' : Integrable
      (fun τ : ℝ => K * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2)) := by
    convert hlog using 1
    ext τ
    ring
  have hmaj : Integrable g := hind.add hlog'
  have hbd : ∀ τ, ‖f τ‖ ≤ g τ := by
    intro τ
    have hlognn : 0 ≤
        K * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) := by
      have hL : 0 ≤ 1 + Real.log (2 + |τ|) :=
        add_nonneg (by norm_num)
          (Real.log_nonneg (by nlinarith [abs_nonneg τ]))
      exact div_nonneg (mul_nonneg hK0 hL)
        (by nlinarith [sq_nonneg τ])
    have hindnn : 0 ≤
        Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ :=
      Set.indicator_apply_nonneg (fun _ => hM0)
    by_cases hτ : |τ| ≤ 2
    · have hmem : τ ∈ Icc (-2 : ℝ) 2 := abs_le.mp hτ
      have : Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ = M :=
        Set.indicator_of_mem hmem (fun _ => M)
      have hf : ‖f τ‖ ≤ M := hM τ hτ
      simpa [g, this] using le_add_of_le_of_nonneg hf hlognn
    · have hge : (2 : ℝ) ≤ |τ| := le_of_lt (lt_of_not_ge hτ)
      have htail := left_edge_integrand_norm_le F hhat hge
      have hnot : τ ∉ Icc (-2 : ℝ) 2 := fun h => hτ (abs_le.mpr h)
      have : Set.indicator (Icc (-2 : ℝ) 2) (fun _ => M) τ = 0 :=
        Set.indicator_of_notMem hnot (fun _ => M)
      have hKrew : K * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) =
          leftEdgeConst * C * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) := by
        unfold K; ring
      have hf : ‖f τ‖ ≤
          leftEdgeConst * C * (1 + Real.log (2 + |τ|)) / (1 + τ ^ 2) := by
        simpa [f, norm_mul] using htail
      simpa [g, this, hKrew] using le_add_of_nonneg_of_le hindnn hf
  exact hmaj.mono' (continuous_left_edge_integrand F).aestronglyMeasurable
    (Filter.Eventually.of_forall hbd)

lemma riemannZetaMultiplicity_le_of_mem_inner {T : ℝ} {z : ℂ}
    (hz : z ∈ landauInnerDisk T) :
    (riemannZetaMultiplicity z : ℝ) ≤
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |T|)) := by
  have hpt : (riemannZetaMultiplicity z : ℝ) ≤
      ∑ ρ ∈ landauInnerDisk T, (riemannZetaMultiplicity ρ : ℝ) :=
    Finset.single_le_sum (fun _ _ => Nat.cast_nonneg _) hz
  exact hpt.trans (sum_multiplicity_landauInnerDisk_le T)

lemma abs_heightCenter_le_X_add {X T : ℝ} (hX : 0 ≤ X)
    (hT : T ∈ zetaZeroHeightCenters X) :
    |T| ≤ X + 5 / 4 := by
  have h1 := abs_heightCenter_le X hT
  have h2 := zetaZeroHeightCenterBound_cast_le X hX
  have hmul : (zetaZeroHeightCenterBound X : ℝ) * (5 / 8) ≤
      ((8 : ℝ) * X / 5 + 2) * (5 / 8) :=
    mul_le_mul_of_nonneg_right h2 (by norm_num)
  have hsimp : ((8 : ℝ) * X / 5 + 2) * (5 / 8) = X + 5 / 4 := by ring
  linarith [h1, hmul, hsimp]

lemma riemannZetaMultiplicity_le_log_of_re_ge_half {z : ℂ} {X : ℝ}
    (hX : 0 ≤ X) (hz : z ∈ riemannZetaZerosOnClosedRect 0 1 X)
    (hre : (1 / 2 : ℝ) ≤ z.re) :
    (riemannZetaMultiplicity z : ℝ) ≤
      zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + X + 5 / 4)) := by
  obtain ⟨T, hT, hzD⟩ := mem_disk_of_half_strip hX hz hre
  have hmem : z ∈ landauInnerDisk T := by
    simpa [landauInnerDisk] using hzD
  have hle := riemannZetaMultiplicity_le_of_mem_inner hmem
  have hTab := abs_heightCenter_le_X_add hX hT
  have hcmp : 2 + |T| ≤ 2 + X + 5 / 4 := by linarith
  have hpos : 0 < 2 + |T| := by positivity
  have hlog := Real.log_le_log hpos hcmp
  have hC : 0 ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  have h1 : 0 ≤ 1 + Real.log (2 + |T|) :=
    add_nonneg (by norm_num)
      (Real.log_nonneg (by nlinarith [abs_nonneg T]))
  refine hle.trans ?_
  exact mul_le_mul_of_nonneg_left (add_le_add_right hlog 1) hC

lemma isCriticalStrip_one_sub {z : ℂ} (hz : IsCriticalStripZetaZero z) :
    IsCriticalStripZetaZero (1 - z) := by
  refine ⟨riemannZeta_one_sub_eq_zero_of hz.2.1 hz.2.2 hz.1, ?_, ?_⟩
  · simp only [sub_re, one_re]; linarith [hz.2.2]
  · simp only [sub_re, one_re]; linarith [hz.2.1]

lemma analyticOrderAt_sub_id (s : ℂ) :
    analyticOrderAt (fun w : ℂ => s - w) s = 1 := by
  have hf : AnalyticAt ℂ (fun w : ℂ => s - w) s := by fun_prop
  have hz : (s - s : ℂ) = 0 := sub_self _
  have hd : deriv (fun w : ℂ => s - w) s ≠ 0 := by
    have hder : HasDerivAt (fun w : ℂ => s - w) (-1) s := by
      simpa using (hasDerivAt_const s s).sub (hasDerivAt_id s)
    simp [hder.deriv]
  exact hf.analyticOrderAt_eq_one_of_zero_deriv_ne_zero hz hd

lemma riemannZetaMultiplicity_eq_one_sub {z : ℂ}
    (hz : IsCriticalStripZetaZero z) (him : (2 : ℝ) ≤ |z.im|) :
    riemannZetaMultiplicity z = riemannZetaMultiplicity (1 - z) := by
  have hG : ∀ n : ℕ, z ≠ -n := ne_neg_nat_of_two_le_abs_im him
  have hχ0 := zetaFEFactor_ne_zero_of_two_le_abs_im him
  have hχ : AnalyticAt ℂ zetaFEFactor z := by
    refine analyticAt_iff_eventually_differentiableAt.mpr ?_
    refine Filter.eventually_of_mem
        (Metric.ball_mem_nhds z (by norm_num : (0 : ℝ) < 1)) ?_
    intro w hw
    have hd : ‖w - z‖ < 1 := mem_ball_iff_norm.mp hw
    have himle : |w.im - z.im| ≤ ‖w - z‖ := by
      simpa [sub_im] using abs_im_le_norm (w - z)
    have hlower : (1 : ℝ) ≤ |w.im| := by
      have htri : |z.im| ≤ |w.im| + |w.im - z.im| := by
        calc |z.im| = |w.im + (z.im - w.im)| := by ring_nf
          _ ≤ |w.im| + |z.im - w.im| := abs_add_le _ _
          _ = |w.im| + |w.im - z.im| := by rw [abs_sub_comm]
      linarith [him, himle, htri, le_of_lt hd]
    exact differentiableAt_zetaFEFactor (ne_neg_nat_of_im_ne_zero
      (fun him0 => by rw [him0, abs_zero] at hlower; linarith))
  have hζz : AnalyticAt ℂ riemannZeta z :=
    analyticAt_riemannZeta (isCriticalStripZetaZero_ne_one hz)
  have hζ1 : AnalyticAt ℂ riemannZeta (1 - z) := by
    refine analyticAt_riemannZeta ?_
    intro h
    have : z = 0 := by linear_combination -(h)
    exact isCriticalStripZetaZero_ne_zero hz this
  set oneSub : ℂ → ℂ := fun w => 1 - w
  have hg : AnalyticAt ℂ oneSub z := by fun_prop
  have hcomp := hζ1.analyticOrderAt_comp hg
  have hsub : analyticOrderAt (fun w : ℂ => oneSub w - oneSub z) z = 1 := by
    have : (fun w : ℂ => oneSub w - oneSub z) = fun w => z - w := by
      ext w; unfold oneSub; ring
    simpa [this] using analyticOrderAt_sub_id z
  have hcomp' : analyticOrderAt (riemannZeta ∘ oneSub) z =
      analyticOrderAt riemannZeta (1 - z) := by
    rw [hcomp, hsub, mul_one]
  have hfe := eventuallyEq_riemannZeta_one_sub_factor him
  have hmul : analyticOrderAt (fun w => zetaFEFactor w * riemannZeta w) z =
      analyticOrderAt zetaFEFactor z + analyticOrderAt riemannZeta z :=
    analyticOrderAt_mul hχ hζz
  have hχord : analyticOrderAt zetaFEFactor z = 0 :=
    analyticOrderAt_eq_zero.mpr (Or.inr hχ0)
  have hfeord : analyticOrderAt
      (fun w : ℂ => riemannZeta (1 - w)) z =
        analyticOrderAt riemannZeta z := by
    rw [analyticOrderAt_congr hfe, hmul, hχord, zero_add]
  have hord : analyticOrderAt riemannZeta z =
      analyticOrderAt riemannZeta (1 - z) :=
    hfeord.symm.trans hcomp'
  unfold riemannZetaMultiplicity analyticOrderNatAt
  simp [hord]

lemma riemannZetaMultiplicity_le_log {z : ℂ}
    (hz : IsCriticalStripZetaZero z)
    (him : (2 : ℝ) ≤ |z.im| ∨ (1 / 2 : ℝ) ≤ z.re) :
    (riemannZetaMultiplicity z : ℝ) ≤
      zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + |z.im| + 5 / 4)) := by
  have hX : 0 ≤ |z.im| := abs_nonneg _
  have hrect : z ∈ riemannZetaZerosOnClosedRect 0 1 |z.im| :=
    mem_rect_of_criticalStrip hz le_rfl
  rcases him with h2 | hre
  · by_cases hre : (1 / 2 : ℝ) ≤ z.re
    · exact riemannZetaMultiplicity_le_log_of_re_ge_half hX hrect hre
    · have h1z := isCriticalStrip_one_sub hz
      have hre' : (1 / 2 : ℝ) ≤ (1 - z).re := by
        simp only [sub_re, one_re]; linarith [lt_of_not_ge hre]
      have him1 : |(1 - z).im| = |z.im| := by simp [sub_im, abs_neg]
      have hrect1 : 1 - z ∈
          riemannZetaZerosOnClosedRect 0 1 |(1 - z).im| :=
        mem_rect_of_criticalStrip h1z le_rfl
      have hle :=
        riemannZetaMultiplicity_le_log_of_re_ge_half
          (abs_nonneg _) hrect1 hre'
      have heq := riemannZetaMultiplicity_eq_one_sub hz h2
      simpa [heq, him1] using hle
  · exact riemannZetaMultiplicity_le_log_of_re_ge_half hX hrect hre

lemma tendsto_intervalIntegral_neg_to (f : ℝ → ℂ) {T : ℕ → ℝ}
    (hf : Integrable f) (hT : Tendsto T atTop atTop) :
    Tendsto (fun k => ∫ τ : ℝ in (-T k)..(T k), f τ) atTop
      (𝓝 (∫ τ : ℝ, f τ)) :=
  intervalIntegral_tendsto_integral hf
    (tendsto_neg_atTop_atBot.comp hT) hT

lemma tendsto_right_edge_interval (F : FullWeilTest) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ τ : ℝ in (-T k)..(T k),
        logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          F.hat ((2 : ℂ) + τ * I)) atTop
      (𝓝 (∫ τ : ℝ,
        logDeriv riemannZeta ((2 : ℂ) + τ * I) *
          F.hat ((2 : ℂ) + τ * I))) :=
  tendsto_intervalIntegral_neg_to _
    (integrable_right_edge_integrand F) hT

lemma tendsto_left_edge_interval (F : FullWeilTest) {T : ℕ → ℝ}
    (hT : Tendsto T atTop atTop) :
    Tendsto (fun k =>
      ∫ τ : ℝ in (-T k)..(T k),
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)) atTop
      (𝓝 (∫ τ : ℝ,
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I))) :=
  tendsto_intervalIntegral_neg_to _
    (integrable_left_edge_integrand F) hT

lemma tendsto_finset_atTop_of_monotone {α : Type*} [DecidableEq α]
    (s : ℕ → Finset α) (hmono : Monotone s)
    (hexh : ∀ x : α, ∃ n, x ∈ s n) :
    Tendsto s atTop atTop := by
  refine tendsto_atTop_atTop.mpr fun t => ?_
  classical
  let N : ℕ := t.sup fun x => Classical.choose (hexh x)
  refine ⟨N, fun n hn => ?_⟩
  intro x hx
  have hxN : Classical.choose (hexh x) ≤ N :=
    Finset.le_sup (f := fun y => Classical.choose (hexh y)) hx
  exact hmono (le_trans hxN hn) (Classical.choose_spec (hexh x))

noncomputable def stripZerosBelow (T : ℝ) :
    Finset {z : ℂ // IsCriticalStripZetaZero z} := by
  classical
  exact (riemannZetaZerosOnClosedRect 0 1 T).subtype
    IsCriticalStripZetaZero

lemma mem_stripZerosBelow {T : ℝ}
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}} :
    ρ ∈ stripZerosBelow T ↔
      ρ.val ∈ riemannZetaZerosOnClosedRect 0 1 T := by
  classical
  simpa [stripZerosBelow] using
    (Finset.mem_subtype (p := IsCriticalStripZetaZero)
      (s := riemannZetaZerosOnClosedRect 0 1 T) (x := ρ))

lemma spectralPartialSum_eq_subtype (F : ℂ → ℂ) (T : ℝ) :
    spectralPartialSum F 0 1 T =
      ∑ ρ ∈ stripZerosBelow T,
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F ρ := by
  classical
  unfold spectralPartialSum
  refine Eq.symm ?_
  refine Finset.sum_bij
    (fun (ρ : {z : ℂ // IsCriticalStripZetaZero z})
        (_ : ρ ∈ stripZerosBelow T) => (ρ : ℂ)) ?_ ?_ ?_ ?_
  · intro ρ hρ
    exact (mem_stripZerosBelow.mp hρ)
  · intro ρ σ _ _ h
    exact Subtype.ext h
  · intro x hx
    exact ⟨⟨x, isCriticalStrip_of_mem_rect hx⟩, mem_stripZerosBelow.mpr hx, rfl⟩
  · intro ρ _
    rfl

lemma stripZerosBelow_mono {T₁ T₂ : ℝ} (h : T₁ ≤ T₂) :
    stripZerosBelow T₁ ⊆ stripZerosBelow T₂ := by
  intro ρ hρ
  have hz := (mem_stripZerosBelow.mp hρ)
  have hz' := mem_riemannZetaZerosOnClosedRect.mp hz
  have hrect := mem_zetaClosedRect.mp hz'.1
  refine mem_stripZerosBelow.mpr
    (mem_riemannZetaZerosOnClosedRect.mpr ⟨?_, hz'.2.1, hz'.2.2⟩)
  exact mem_zetaClosedRect.mpr ⟨hrect.1, hrect.2.1,
    le_trans (neg_le_neg h) hrect.2.2.1, le_trans hrect.2.2.2 h⟩

/-- Weight ` (1+log(2+|Im|+5/4)) / (1+Im^2) ` on strip zeros. -/
noncomputable def stripZeroWeight (z : ℂ) : ℝ :=
  (1 + Real.log (2 + |z.im| + 5 / 4)) / (1 + z.im ^ 2)

lemma stripZeroWeight_nonneg (z : ℂ) : 0 ≤ stripZeroWeight z :=
  div_nonneg
    (add_nonneg (by norm_num)
      (Real.log_nonneg (by nlinarith [abs_nonneg z.im])))
    (by nlinarith [sq_nonneg z.im])

lemma exists_weighted_hat_bound (F : FullWeilTest) :
    ∃ C : ℝ, 0 ≤ C ∧
      ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ‖ ≤
          C * stripZeroWeight (ρ : ℂ) := by
  obtain ⟨Chat, hChat0, hhat⟩ := F.norm_hat_le_inv_sq
  classical
  set S := riemannZetaZerosOnClosedRect 0 1 2
  set M : ℝ :=
    ∑ z ∈ S, ‖(riemannZetaMultiplicity z : ℂ) * F.hat z‖
  have hM0 : 0 ≤ M := Finset.sum_nonneg fun _ _ => norm_nonneg _
  have hCin0 : 0 ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  set C : ℝ := zetaZerosInDiskCardBoundInner * Chat + 5 * M
  have hC0 : 0 ≤ C :=
    add_nonneg (mul_nonneg hCin0 hChat0) (mul_nonneg (by norm_num) hM0)
  refine ⟨C, hC0, fun ρ => ?_⟩
  have hnn :
      0 ≤ 1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4) :=
    add_nonneg (by norm_num)
      (Real.log_nonneg (by nlinarith [abs_nonneg (ρ : ℂ).im]))
  have hdenpos : 0 < 1 + (ρ : ℂ).im ^ 2 :=
    by nlinarith [sq_nonneg (ρ : ℂ).im]
  by_cases him : (2 : ℝ) ≤ |(ρ : ℂ).im|
  · have hm := riemannZetaMultiplicity_le_log ρ.property (Or.inl him)
    have hIcc : (ρ : ℂ).re ∈ Icc (0 : ℝ) 1 :=
      ⟨le_of_lt ρ.property.2.1, le_of_lt ρ.property.2.2⟩
    have hh := hhat (ρ : ℂ) hIcc
    have hmn :
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ)‖ =
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) := by
      rw [← Complex.ofReal_natCast, Complex.norm_real]
      exact abs_of_nonneg (Nat.cast_nonneg _)
    have hprod :
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ‖ =
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖F.hat ρ‖ := by
      rw [norm_mul, hmn]
    have hmul :=
      mul_le_mul hm hh (norm_nonneg _)
        (mul_nonneg hCin0 hnn)
    have hCin : zetaZerosInDiskCardBoundInner * Chat ≤ C :=
      le_add_of_nonneg_right (mul_nonneg (by norm_num) hM0)
    calc ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ‖
        = (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖F.hat ρ‖ := hprod
      _ ≤ (zetaZerosInDiskCardBoundInner *
            (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4))) *
              (Chat / (1 + (ρ : ℂ).im ^ 2)) := hmul
      _ = (zetaZerosInDiskCardBoundInner * Chat) *
            stripZeroWeight (ρ : ℂ) := by
          unfold stripZeroWeight
          field_simp [hdenpos.ne']
      _ ≤ C * stripZeroWeight (ρ : ℂ) :=
          mul_le_mul_of_nonneg_right hCin (stripZeroWeight_nonneg _)
  · have hlt : |(ρ : ℂ).im| < 2 := lt_of_not_ge him
    have hmem : (ρ : ℂ) ∈ S :=
      mem_rect_of_criticalStrip ρ.property (le_of_lt hlt)
    have hsingle :=
      Finset.single_le_sum
        (f := fun z : ℂ =>
          ‖(riemannZetaMultiplicity z : ℂ) * F.hat z‖)
        (fun _ _ => norm_nonneg _) hmem
    have himlt := abs_lt.mp hlt
    have hdenlt : 1 + (ρ : ℂ).im ^ 2 < 5 := by
      nlinarith [himlt.1, himlt.2]
    have hlog0 : 0 ≤ Real.log (2 + |(ρ : ℂ).im| + 5 / 4) :=
      Real.log_nonneg (by nlinarith [abs_nonneg (ρ : ℂ).im])
    have hw : (1 : ℝ) / 5 ≤ stripZeroWeight (ρ : ℂ) := by
      have hinv : (1 : ℝ) / 5 ≤ 1 / (1 + (ρ : ℂ).im ^ 2) :=
        (one_div_le_one_div (by norm_num : (0 : ℝ) < 5) hdenpos).mpr
          (le_of_lt hdenlt)
      have hlo : 1 / (1 + (ρ : ℂ).im ^ 2) ≤ stripZeroWeight (ρ : ℂ) := by
        unfold stripZeroWeight
        exact div_le_div_of_nonneg_right
          (le_add_of_nonneg_right hlog0) hdenpos.le
      exact hinv.trans hlo
    have h5M : (5 : ℝ) * M ≤ C :=
      le_add_of_nonneg_left (mul_nonneg hCin0 hChat0)
    have hMle : M ≤ (5 : ℝ) * M * stripZeroWeight (ρ : ℂ) := by
      have hwnn := stripZeroWeight_nonneg (ρ : ℂ)
      nlinarith [hw, hM0, hwnn]
    have hC5 : (5 : ℝ) * M * stripZeroWeight (ρ : ℂ) ≤
        C * stripZeroWeight (ρ : ℂ) :=
      mul_le_mul_of_nonneg_right h5M (stripZeroWeight_nonneg _)
    exact hsingle.trans (hMle.trans hC5)

lemma log_dyadic_weight_le (j : ℕ) :
    1 + Real.log (2 + (2 : ℝ) ^ (j + 1) + 5 / 4) ≤
      3 * ((j : ℝ) + 3) := by
  have hge2 : (2 : ℝ) ≤ (2 : ℝ) ^ (j + 1) := by
    have hpow1 : (2 : ℝ) ^ (j + 1) = 2 * (2 : ℝ) ^ j := by ring
    have hone : (1 : ℝ) ≤ (2 : ℝ) ^ j := one_le_pow₀ (by norm_num)
    nlinarith [hpow1, hone]
  have h2 : 2 + (2 : ℝ) ^ (j + 1) + 5 / 4 ≤ (2 : ℝ) ^ (j + 3) := by
    have hpow : (2 : ℝ) ^ (j + 3) = 4 * (2 : ℝ) ^ (j + 1) := by ring
    nlinarith [hpow, hge2]
  have hpos : 0 < 2 + (2 : ℝ) ^ (j + 1) + 5 / 4 := by positivity
  have hlog : Real.log (2 + (2 : ℝ) ^ (j + 1) + 5 / 4) ≤
      Real.log ((2 : ℝ) ^ (j + 3)) :=
    Real.log_le_log hpos h2
  have hlogpow : Real.log ((2 : ℝ) ^ (j + 3)) =
      (j + 3 : ℝ) * Real.log 2 := by
    simpa [Nat.cast_add, Nat.cast_ofNat] using Real.log_pow (2 : ℝ) (j + 3)
  have hlog2 : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2)
    linarith
  nlinarith [hlog, hlogpow, hlog2]

lemma stripZeroWeight_dyadic_le {j : ℕ} {z : ℂ}
    (hz : z ∈ zetaZeroDyadicBlock j) :
    stripZeroWeight z ≤
      3 * ((j : ℝ) + 3) * ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
  have him := (mem_dyadicBlock.mp hz).2
  have hnum : 1 + Real.log (2 + |z.im| + 5 / 4) ≤
      3 * ((j : ℝ) + 3) := by
    have hcmp : 2 + |z.im| + 5 / 4 ≤
        2 + (2 : ℝ) ^ (j + 1) + 5 / 4 := by linarith [le_of_lt him.2]
    have hpos : 0 < 2 + |z.im| + 5 / 4 := by positivity
    have hlog := Real.log_le_log hpos hcmp
    have hnum' : 1 + Real.log (2 + |z.im| + 5 / 4) ≤
        1 + Real.log (2 + (2 : ℝ) ^ (j + 1) + 5 / 4) := by
      linarith [hlog]
    exact hnum'.trans (log_dyadic_weight_le j)
  have h2j : 0 < (2 : ℝ) ^ j := pow_pos (by norm_num) _
  have hsq : ((2 : ℝ) ^ j) ^ 2 ≤ z.im ^ 2 := by
    have : ((2 : ℝ) ^ j) ^ 2 ≤ |z.im| ^ 2 :=
      sq_le_sq.mpr (by simpa [abs_of_nonneg h2j.le] using him.1)
    simpa [sq_abs] using this
  have hdenpos : 0 < 1 + z.im ^ 2 := by nlinarith [sq_nonneg z.im]
  have hge : ((2 : ℝ) ^ j) ^ 2 ≤ 1 + z.im ^ 2 := by nlinarith [hsq]
  have hinv : (1 + z.im ^ 2)⁻¹ ≤ ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
    have h4 : 0 < ((2 : ℝ) ^ j) ^ 2 := sq_pos_of_pos h2j
    have := (inv_le_inv₀ hdenpos h4).mpr hge
    simpa [inv_pow] using this
  unfold stripZeroWeight
  rw [div_eq_mul_inv]
  exact mul_le_mul hnum hinv (inv_nonneg.mpr hdenpos.le) (by positivity)

noncomputable def zetaZeroWeightBlockBound : ℝ :=
  24 * zetaZeroCountUpToXBoundConst

lemma zetaZeroWeightBlockBound_nonneg : 0 ≤ zetaZeroWeightBlockBound :=
  mul_nonneg (by norm_num) (le_of_lt zetaZeroCountUpToXBoundConst_pos)

lemma dyadicBlock_weight_sum_le (j : ℕ) :
    ∑ z ∈ zetaZeroDyadicBlock j, stripZeroWeight z ≤
      zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j := by
  set B := zetaZeroDyadicBlock j
  have hX : 0 ≤ (2 : ℝ) ^ (j + 1) := pow_nonneg (by norm_num) _
  have hcard := card_zeros_le ((2 : ℝ) ^ (j + 1)) hX
  have hBcard : (B.card : ℝ) ≤
      ((riemannZetaZerosOnClosedRect 0 1 ((2 : ℝ) ^ (j + 1))).card : ℝ) :=
    Nat.cast_le.mpr (Finset.card_le_card (Finset.filter_subset _ _))
  have hterm : ∀ z ∈ B, stripZeroWeight z ≤
      3 * ((j : ℝ) + 3) * ((2 : ℝ) ^ j)⁻¹ ^ 2 :=
    fun z hz => stripZeroWeight_dyadic_le hz
  have hsum : ∑ z ∈ B, stripZeroWeight z ≤
      (B.card : ℝ) * (3 * ((j : ℝ) + 3) * ((2 : ℝ) ^ j)⁻¹ ^ 2) := by
    have := Finset.sum_le_card_nsmul B stripZeroWeight
      (3 * ((j : ℝ) + 3) * ((2 : ℝ) ^ j)⁻¹ ^ 2) hterm
    simpa [nsmul_eq_mul] using this
  have hC := le_of_lt zetaZeroCountUpToXBoundConst_pos
  have hpack : (B.card : ℝ) * ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤
      zetaZeroCountUpToXBoundConst * (1 + (2 : ℝ) ^ (j + 1)) *
        (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) * ((2 : ℝ) ^ j)⁻¹ ^ 2 := by
    have h1 := hBcard.trans hcard
    exact mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
  have hfac := dyadic_count_factor_le j
  have hcardinv :
      zetaZeroCountUpToXBoundConst * (1 + (2 : ℝ) ^ (j + 1)) *
          (1 + Real.log (2 + (2 : ℝ) ^ (j + 1))) * ((2 : ℝ) ^ j)⁻¹ ^ 2 ≤
        zetaZeroCountUpToXBoundConst * (8 * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j) := by
    convert mul_le_mul_of_nonneg_left hfac hC using 1 <;> ring
  have hnn3 : 0 ≤ 3 * ((j : ℝ) + 3) := by positivity
  have hsum' : ∑ z ∈ B, stripZeroWeight z ≤
      (zetaZeroCountUpToXBoundConst * (8 * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j)) *
        (3 * ((j : ℝ) + 3)) := by
    have h1 := hsum.trans
      (by
        have := mul_le_mul_of_nonneg_right hpack hnn3
        convert this using 1
        ring)
    exact h1.trans (mul_le_mul_of_nonneg_right hcardinv hnn3)
  have hfin :
      (zetaZeroCountUpToXBoundConst * (8 * ((j : ℝ) + 2) * (2 : ℝ)⁻¹ ^ j)) *
          (3 * ((j : ℝ) + 3)) ≤
        zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j := by
    unfold zetaZeroWeightBlockBound
    have hle : ((j : ℝ) + 2) * ((j : ℝ) + 3) ≤ ((j : ℝ) + 3) ^ 2 := by
      nlinarith
    nlinarith [hC, hle, pow_nonneg (by norm_num : (0 : ℝ) ≤ 2⁻¹) j]
  exact hsum'.trans hfin

set_option maxHeartbeats 400000 in
lemma summable_nat_add_three_sq_mul_two_pow_neg :
    Summable fun j : ℕ => ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j := by
  have hr : ‖(2 : ℝ)⁻¹‖ < 1 := by norm_num
  have h2 : Summable fun n : ℕ => (n : ℝ) ^ 2 * (2 : ℝ)⁻¹ ^ n :=
    summable_pow_mul_geometric_of_norm_lt_one 2 hr
  have h1 : Summable fun n : ℕ => (n : ℝ) * (2 : ℝ)⁻¹ ^ n := by
    simpa using summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have h0 : Summable fun n : ℕ => (2 : ℝ)⁻¹ ^ n :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  convert (h2.add (h1.mul_left 6)).add (h0.mul_left 9) using 1
  ext n
  ring

lemma summable_dyadic_weight_majorant :
    Summable fun j : ℕ =>
      zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j := by
  convert (summable_nat_add_three_sq_mul_two_pow_neg).mul_left
    zetaZeroWeightBlockBound using 1
  ext j
  ring

open scoped ENNReal
open Classical

noncomputable def stripZeroWeightENN (z : ℂ) : ℝ≥0∞ :=
  if IsCriticalStripZetaZero z then ENNReal.ofReal (stripZeroWeight z) else 0

lemma stripZeroWeightENN_eq_ofReal {z : ℂ}
    (hz : IsCriticalStripZetaZero z) :
    stripZeroWeightENN z = ENNReal.ofReal (stripZeroWeight z) :=
  if_pos hz

lemma tsum_weight_compact :
    ∑' z : (zetaZeroCompactBlock : Set ℂ), stripZeroWeightENN z =
      ∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z := by
  rw [← Finset.tsum_subtype zetaZeroCompactBlock stripZeroWeightENN]
  rfl

lemma tsum_weight_dyadic (j : ℕ) :
    ∑' z : (zetaZeroDyadicBlock j : Set ℂ), stripZeroWeightENN z =
      ∑ z ∈ zetaZeroDyadicBlock j, stripZeroWeightENN z := by
  rw [← Finset.tsum_subtype (zetaZeroDyadicBlock j) stripZeroWeightENN]
  rfl

lemma sum_weightENN_eq_ofReal (s : Finset ℂ)
    (hs : ∀ z ∈ s, IsCriticalStripZetaZero z) :
    ∑ z ∈ s, stripZeroWeightENN z =
      ENNReal.ofReal (∑ z ∈ s, stripZeroWeight z) := by
  have hcongr : ∑ z ∈ s, stripZeroWeightENN z =
      ∑ z ∈ s, ENNReal.ofReal (stripZeroWeight z) :=
    Finset.sum_congr rfl fun z hz => stripZeroWeightENN_eq_ofReal (hs z hz)
  rw [hcongr, ENNReal.ofReal_sum_of_nonneg fun z _ => stripZeroWeight_nonneg z]

lemma sum_weight_compact_ne_top :
    (∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z) ≠ ∞ := by
  rw [sum_weightENN_eq_ofReal _ fun z hz => isCritical_of_mem_compact hz]
  exact ENNReal.ofReal_ne_top

lemma sum_weight_dyadic_le (j : ℕ) :
    ∑ z ∈ zetaZeroDyadicBlock j, stripZeroWeightENN z ≤
      ENNReal.ofReal
        (zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j) := by
  rw [sum_weightENN_eq_ofReal _ fun z hz => isCritical_of_mem_dyadic hz]
  exact ENNReal.ofReal_le_ofReal (dyadicBlock_weight_sum_le j)

lemma tsum_weight_strip_le :
    ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, stripZeroWeightENN z ≤
      ∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z +
        ∑' j : ℕ, ENNReal.ofReal
          (zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j) := by
  have hunion := stripZeros_eq_blocks
  have h1 :
      ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, stripZeroWeightENN z =
        ∑' z : ↥((zetaZeroCompactBlock : Set ℂ) ∪
            ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ)), stripZeroWeightENN z :=
    tsum_congr_set_coe _ hunion
  have h2 := ENNReal.tsum_union_le stripZeroWeightENN
    (zetaZeroCompactBlock : Set ℂ)
    (⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ))
  have h3 := ENNReal.tsum_iUnion_le_tsum stripZeroWeightENN
    fun j : ℕ => (zetaZeroDyadicBlock j : Set ℂ)
  have hcomp : ∑' z : (zetaZeroCompactBlock : Set ℂ), stripZeroWeightENN z =
      ∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z := tsum_weight_compact
  have hdy : ∑' j : ℕ,
      ∑' z : (zetaZeroDyadicBlock j : Set ℂ), stripZeroWeightENN z ≤
      ∑' j : ℕ, ENNReal.ofReal
        (zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ j) := by
    refine ENNReal.tsum_le_tsum fun j => ?_
    rw [tsum_weight_dyadic]
    exact sum_weight_dyadic_le j
  calc
    ∑' z : {z : ℂ | IsCriticalStripZetaZero z}, stripZeroWeightENN z =
        ∑' z : ↥((zetaZeroCompactBlock : Set ℂ) ∪
            ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ)), stripZeroWeightENN z := h1
    _ ≤ ∑' z : (zetaZeroCompactBlock : Set ℂ), stripZeroWeightENN z +
          ∑' z : ⋃ j : ℕ, (zetaZeroDyadicBlock j : Set ℂ),
            stripZeroWeightENN z := h2
    _ ≤ ∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z +
          ∑' j : ℕ, ∑' z : (zetaZeroDyadicBlock j : Set ℂ),
            stripZeroWeightENN z := by
        rw [hcomp]; exact add_le_add le_rfl h3
    _ ≤ ∑ z ∈ zetaZeroCompactBlock, stripZeroWeightENN z +
          ∑' j : ℕ, ENNReal.ofReal
            (zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 *
              (2 : ℝ)⁻¹ ^ j) :=
        add_le_add le_rfl hdy

lemma tsum_dyadic_weight_majorant_ne_top :
    (∑' j : ℕ, ENNReal.ofReal
        (zetaZeroWeightBlockBound * ((j : ℝ) + 3) ^ 2 *
          (2 : ℝ)⁻¹ ^ j)) ≠ ∞ := by
  have hf : ∀ n : ℕ, 0 ≤
      zetaZeroWeightBlockBound * ((n : ℝ) + 3) ^ 2 * (2 : ℝ)⁻¹ ^ n :=
    fun n =>
      mul_nonneg (mul_nonneg zetaZeroWeightBlockBound_nonneg (sq_nonneg _))
        (pow_nonneg (by norm_num) _)
  rw [← ENNReal.ofReal_tsum_of_nonneg hf summable_dyadic_weight_majorant]
  exact ENNReal.ofReal_ne_top

lemma tsum_weight_strip_ne_top :
    (∑' z : {z : ℂ | IsCriticalStripZetaZero z}, stripZeroWeightENN z) ≠ ∞ := by
  have hle := tsum_weight_strip_le
  exact ne_top_of_le_ne_top
    (ENNReal.add_ne_top.mpr ⟨sum_weight_compact_ne_top,
      tsum_dyadic_weight_majorant_ne_top⟩) hle

lemma tsum_ofReal_weight_ne_top :
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      ENNReal.ofReal (stripZeroWeight (ρ : ℂ))) ≠ ∞ := by
  have heq :
      (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
        ENNReal.ofReal (stripZeroWeight (ρ : ℂ))) =
        fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
          stripZeroWeightENN ρ.val :=
    funext fun ρ => (stripZeroWeightENN_eq_ofReal ρ.property).symm
  rw [heq]
  exact tsum_weight_strip_ne_top

lemma summable_stripZeroWeight :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      stripZeroWeight (ρ : ℂ) := by
  have htop := tsum_ofReal_weight_ne_top
  have hNN := ENNReal.summable_toNNReal_of_tsum_ne_top htop
  refine (summable_congr fun ρ => ?_).mpr (NNReal.summable_coe.mpr hNN)
  exact (ENNReal.toReal_ofReal (stripZeroWeight_nonneg (ρ : ℂ))).symm

lemma summable_weighted_hat (F : FullWeilTest) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ := by
  obtain ⟨C, hC0, hbd⟩ := exists_weighted_hat_bound F
  refine Summable.of_norm
    (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hbd
      (summable_stripZeroWeight.mul_left C))

lemma landau_gap_T_mono {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Monotone T := by
  intro a b hab
  rcases eq_or_lt_of_le hab with h | h
  · subst h; exact le_rfl
  · have ha : T a ≤ ((2 * a + 3 : ℕ) : ℝ) + 1 := (hTbd a).2
    have hb : ((2 * b + 3 : ℕ) : ℝ) ≤ T b := (hTbd b).1
    have hnat : (2 * a + 3 : ℕ) + 1 ≤ 2 * b + 3 := by
      have : a + 1 ≤ b := Nat.succ_le_of_lt h
      omega
    have hstep : ((2 * a + 3 : ℕ) : ℝ) + 1 ≤ ((2 * b + 3 : ℕ) : ℝ) :=
      by exact_mod_cast hnat
    exact ha.trans (hstep.trans hb)

lemma landau_gap_T_tendsto {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Tendsto T atTop atTop :=
  tendsto_atTop_mono (fun k =>
    le_trans (by exact_mod_cast (by omega : k ≤ 2 * k + 3)) (hTbd k).1)
    tendsto_natCast_atTop_atTop

lemma landau_gap_T_two_le {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) (k : ℕ) :
    (2 : ℝ) ≤ T k :=
  le_trans (by norm_num : (2 : ℝ) ≤ 3)
    (le_trans (by exact_mod_cast
      (Nat.le_add_left 3 (2 * k) : 3 ≤ 2 * k + 3)) (hTbd k).1)

lemma stripZerosBelow_landau_mono {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Monotone fun k => stripZerosBelow (T k) :=
  fun _ _ h => stripZerosBelow_mono (landau_gap_T_mono hTbd h)

lemma exists_mem_stripZerosBelow_landau {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ∃ k, ρ ∈ stripZerosBelow (T k) := by
  obtain ⟨k, hk⟩ :=
    (tendsto_atTop_atTop.mp (landau_gap_T_tendsto hTbd)) |(ρ : ℂ).im|
  refine ⟨k, mem_stripZerosBelow.mpr
    (mem_rect_of_criticalStrip ρ.property (hk k le_rfl))⟩

lemma tendsto_stripZerosBelow_landau {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Tendsto (fun k => stripZerosBelow (T k)) atTop atTop :=
  tendsto_finset_atTop_of_monotone _
    (stripZerosBelow_landau_mono hTbd)
    (exists_mem_stripZerosBelow_landau hTbd)

lemma tendsto_spectralPartialSum_tsum (F : FullWeilTest) {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1) :
    Tendsto (fun k => spectralPartialSum F.hat (-1 / 16) 2 (T k)) atTop
      (𝓝 (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ)) := by
  have hsum := (summable_weighted_hat F).hasSum
  have hfin := tendsto_stripZerosBelow_landau hTbd
  have hsub :
      Tendsto (fun k =>
        ∑ ρ ∈ stripZerosBelow (T k),
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) atTop
        (𝓝 (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ)) :=
    hsum.comp hfin
  refine hsub.congr fun k => ?_
  rw [spectralPartialSum_eq_critical F.hat (by norm_num) (by norm_num),
    spectralPartialSum_eq_subtype]

lemma tendsto_horizontal_edges_of_landau (F : FullWeilTest) {T : ℕ → ℝ}
    (hTbd : ∀ k : ℕ, ((2 * k + 3 : ℕ) : ℝ) ≤ T k ∧
      T k ≤ ((2 * k + 3 : ℕ) : ℝ) + 1)
    (hgapP : ∀ k : ℕ, ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
      1 / (ordinateGapConstLandau * (1 + Real.log (T k))) ≤
        |ρ.im - T k|) :
    Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + T k * I) *
          F.hat ((x : ℂ) + T k * I)) atTop (nhds 0) ∧
    Tendsto (fun k =>
      ∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
          F.hat ((x : ℂ) + (-(T k) : ℝ) * I)) atTop (nhds 0) := by
  obtain ⟨C, hC0, hhat⟩ := F.norm_hat_le_inv_sq_on_Icc (-1 / 16 : ℝ) 2
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
  have hK0 : 0 ≤ K :=
    mul_nonneg (mul_nonneg (mul_nonneg (by norm_num)
      (le_trans (by norm_num : (0 : ℝ) ≤ 1) hA)) sliverEdgeConst_nonneg) hC0
  have hlen : (2 : ℝ) - (-1 / 16) = 2 + 1 / 16 := by ring
  have hedge (τ : ℕ → ℝ) (hτ : ∀ k, |τ k| = T k) (k : ℕ) :
      ‖∫ x : ℝ in (-1 / 16 : ℝ)..2,
          logDeriv riemannZeta ((x : ℂ) + τ k * I) *
            F.hat ((x : ℂ) + τ k * I)‖ ≤
        K * (L k ^ 3 / (1 + T k ^ 2)) := by
    have hgap : ∀ ρ : ℂ, riemannZeta ρ = 0 → ρ ≠ 1 →
        1 / (A * (1 + Real.log (T k))) ≤ |ρ.im - T k| := hgapP k
    have hbd : ∀ σ, σ ∈ Icc (-1 / 16 : ℝ) 2 →
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
    have hle := norm_horizontal_logDeriv_hat_integral_le_with
      F hσ (hB0 k) hC0 hne1 hnz hbd hhat
    have hsq : 1 + τ k ^ 2 = 1 + T k ^ 2 := by
      have : |τ k| ^ 2 = T k ^ 2 := by simp [hτ]
      simpa [sq_abs] using this
    convert hle using 1
    unfold B L K
    rw [hsq, hlen]
    ring
  have hdecay : Tendsto (fun k => L k ^ 3 / (1 + T k ^ 2))
      atTop (nhds 0) :=
    tendsto_one_add_log_cubed_div_one_add_sq.comp hTtop
  have hpos := hedge (fun k => T k)
    (fun k => abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k)))
  have hneg := hedge (fun k => -(T k)) (fun k => by simp [abs_neg,
    abs_of_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 2) (hT2 k))])
  have hnorm {I : ℕ → ℂ}
      (hle : ∀ k, ‖I k‖ ≤ K * (L k ^ 3 / (1 + T k ^ 2))) :
      Tendsto I atTop (nhds 0) :=
    tendsto_zero_iff_norm_tendsto_zero.mpr
      (squeeze_zero (fun _ => norm_nonneg _) hle (by
        convert hdecay.const_mul K
        rw [mul_zero]))
  exact ⟨hnorm hpos, hnorm hneg⟩

lemma rectangleIntegral_logDeriv_hat (F : FullWeilTest) (T : ℝ) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T : ℝ) * I) =
    (∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (-T : ℝ) * I) *
          F.hat ((x : ℂ) + (-T : ℝ) * I)) -
    (∫ x : ℝ in (-1 / 16 : ℝ)..2,
        logDeriv riemannZeta ((x : ℂ) + (T : ℝ) * I) *
          F.hat ((x : ℂ) + (T : ℝ) * I)) +
    I • (∫ y : ℝ in (-T)..T,
        logDeriv riemannZeta ((2 : ℂ) + y * I) * F.hat ((2 : ℂ) + y * I)) -
    I • (∫ y : ℝ in (-T)..T,
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + y * I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + y * I)) := by
  unfold rectangleIntegral
  have hzre : (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I).re = -1 / 16 := by simp
  have hwre : (((2 : ℝ) : ℂ) + (T : ℝ) * I).re = 2 := by simp
  have hzim : (((-1 / 16 : ℝ) : ℂ) + (-T : ℝ) * I).im = -T := by simp
  have hwim : (((2 : ℝ) : ℂ) + (T : ℝ) * I).im = T := by simp
  simp [hzre, hwre, hzim, hwim]

set_option maxHeartbeats 800000 in
theorem contourIdentityLimitAlongGaps : ContourIdentityLimitAlongGaps := by
  intro F
  obtain ⟨T, hTbd, hgapP, hgapN⟩ := exists_gap_sequence_landau
  obtain ⟨hTop, hBot⟩ := tendsto_horizontal_edges_of_landau F hTbd hgapP
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
      rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
        (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
        (((2 : ℝ) : ℂ) + (T k : ℝ) * I) =
        (2 * (Real.pi : ℂ) * I) *
          (spectralPartialSum F.hat (-1 / 16) 2 (T k) - F.hat 1) :=
    fun k => contour_identity_fixed_T_neg_one_div_sixteen F (hTpos k) (hord k)
  have hright := tendsto_right_edge_interval F hTtop
  have hleft := tendsto_left_edge_interval F hTtop
  have hspec := tendsto_spectralPartialSum_tsum F hTbd
  have hsides :
      Tendsto (fun k =>
        (∫ x : ℝ in (-1 / 16 : ℝ)..2,
            logDeriv riemannZeta ((x : ℂ) + (-(T k) : ℝ) * I) *
              F.hat ((x : ℂ) + (-(T k) : ℝ) * I)) -
        (∫ x : ℝ in (-1 / 16 : ℝ)..2,
            logDeriv riemannZeta ((x : ℂ) + (T k : ℝ) * I) *
              F.hat ((x : ℂ) + (T k : ℝ) * I)) +
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv riemannZeta ((2 : ℂ) + y * I) *
              F.hat ((2 : ℂ) + y * I)) -
        I • (∫ y : ℝ in (-(T k))..(T k),
            logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + y * I) *
              F.hat (((-1 / 16 : ℝ) : ℂ) + y * I))) atTop
        (𝓝 (I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
              F.hat ((2 : ℂ) + τ * I)) -
            I • (∫ τ : ℝ, logDeriv riemannZeta
              (((-1 / 16 : ℝ) : ℂ) + τ * I) *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)))) := by
    convert ((hBot.sub hTop).add (hright.const_smul I)).sub
      (hleft.const_smul I) using 1
    simp
  have hrect :
      Tendsto (fun k =>
        rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * F.hat ζ)
          (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
          (((2 : ℝ) : ℂ) + (T k : ℝ) * I)) atTop
        (𝓝 (I • (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * I) *
              F.hat ((2 : ℂ) + τ * I)) -
            I • (∫ τ : ℝ, logDeriv riemannZeta
              (((-1 / 16 : ℝ) : ℂ) + τ * I) *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * I)))) :=
    hsides.congr fun k => (rectangleIntegral_logDeriv_hat F (T k)).symm
  have hspec' :
      Tendsto (fun k =>
        (2 * (Real.pi : ℂ) * I) *
          (spectralPartialSum F.hat (-1 / 16) 2 (T k) - F.hat 1)) atTop
        (𝓝 ((2 * (Real.pi : ℂ) * I) *
          ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) -
            F.hat 1))) :=
    (hspec.sub tendsto_const_nhds).const_mul _
  exact tendsto_nhds_unique (hrect.congr hid) hspec'

end ContourEdges

/-- Spectral pairing supplied by the r530 contour limit:
`Re(∑ m_ρ ĥ(ρ) − ĥ(1))`.  Independently of the finite-window
three-channel construction.  The identification
`fullWeilForm = standardExplicitFormula` is the open dictionary. -/
noncomputable def standardExplicitFormula (F : FullWeilTest) : ℝ :=
  ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) - F.hat 1).re

section HatFourierInversion

open MeasureTheory Filter Function
open scoped FourierTransform Topology RealInnerProductSpace

/-- Slice `t ↦ g(t) e^{σ t}` of a compactly supported Weil test. -/
noncomputable def FullWeilTest.hatSlice (F : FullWeilTest) (σ : ℝ) : ℝ → ℂ :=
  fun t => (F.toFun t : ℂ) * Complex.exp (σ * t)

lemma FullWeilTest.continuous_hatSlice (F : FullWeilTest) (σ : ℝ) :
    Continuous (F.hatSlice σ) :=
  (Complex.continuous_ofReal.comp F.continuous_toFun).mul
    (Complex.continuous_exp.comp (continuous_const.mul Complex.continuous_ofReal))

lemma FullWeilTest.hasCompactSupport_hatSlice (F : FullWeilTest) (σ : ℝ) :
    HasCompactSupport (F.hatSlice σ) :=
  HasCompactSupport.of_support_subset_isCompact isCompact_Icc
    (fun t ht => F.support_subset_Icc (by
      refine mem_support.mpr ?_
      intro hg
      have : F.hatSlice σ t = 0 := by
        unfold FullWeilTest.hatSlice
        simp [hg]
      exact (mem_support.mp ht) this))

lemma FullWeilTest.integrable_hatSlice (F : FullWeilTest) (σ : ℝ) :
    Integrable (F.hatSlice σ) :=
  (F.continuous_hatSlice σ).integrable_of_hasCompactSupport
    (F.hasCompactSupport_hatSlice σ)

lemma FullWeilTest.hat_eq_fourier_slice (F : FullWeilTest) (σ ξ : ℝ) :
    F.hat ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I) = 𝓕 (F.hatSlice σ) ξ := by
  unfold FullWeilTest.hat FullWeilTest.hatSlice
  rw [Real.fourier_eq']
  refine integral_congr_ae (Eventually.of_forall fun t => ?_)
  have hinter : ⟪t, ξ⟫ = t * ξ := mul_comm ξ t
  dsimp
  have hmul :
      ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I) * (t : ℂ) =
        (σ : ℂ) * t + ((-(2 * Real.pi) * ξ) * Complex.I) * t := by
    simp [add_mul]
  have hexp :
      Complex.exp (((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I) * t) =
        Complex.exp ((σ : ℂ) * t) *
          Complex.exp (((-(2 * Real.pi) * ξ) * Complex.I) * t) := by
    rw [hmul, Complex.exp_add]
  have hfour :
      Complex.exp ((↑(-2 * Real.pi * ⟪t, ξ⟫) * Complex.I)) =
        Complex.exp (((-(2 * Real.pi) * ξ) * Complex.I) * t) := by
    simp [hinter, mul_comm, mul_left_comm, mul_assoc]
  calc
    (F.toFun t : ℂ) * Complex.exp
        (((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I) * t) =
        (F.toFun t : ℂ) * (Complex.exp ((σ : ℂ) * t) *
          Complex.exp (((-(2 * Real.pi) * ξ) * Complex.I) * t)) := by
      rw [hexp]
    _ = Complex.exp ((↑(-2 * Real.pi * ⟪t, ξ⟫) * Complex.I)) *
          ((F.toFun t : ℂ) * Complex.exp (σ * t)) := by
      rw [hfour]
      ring

lemma integrable_inv_one_add_scaled_sq :
    Integrable fun ξ : ℝ => (1 + (2 * Real.pi * ξ) ^ 2)⁻¹ := by
  have hmaj : Integrable fun ξ : ℝ => (1 + ξ ^ 2)⁻¹ :=
    integrable_inv_one_add_sq
  have hcont : Continuous fun ξ : ℝ => (1 + (2 * Real.pi * ξ) ^ 2)⁻¹ :=
    Continuous.inv₀
      (continuous_const.add ((continuous_const.mul continuous_id).pow 2))
      fun ξ => by nlinarith [sq_nonneg (2 * Real.pi * ξ)]
  refine hmaj.mono' hcont.aestronglyMeasurable
    (Eventually.of_forall fun ξ => ?_)
  have hle : 1 + ξ ^ 2 ≤ 1 + (2 * Real.pi * ξ) ^ 2 := by
    have : (1 : ℝ) ≤ (2 * Real.pi) ^ 2 := by
      nlinarith [Real.pi_gt_three]
    nlinarith [sq_nonneg ξ, this]
  have hpos : 0 < 1 + ξ ^ 2 := by nlinarith [sq_nonneg ξ]
  have hpos' : 0 < 1 + (2 * Real.pi * ξ) ^ 2 := by
    nlinarith [sq_nonneg (2 * Real.pi * ξ)]
  rw [Real.norm_eq_abs, abs_of_nonneg (inv_nonneg.mpr hpos'.le)]
  exact (inv_le_inv₀ hpos' hpos).mpr hle

lemma FullWeilTest.integrable_fourier_hatSlice (F : FullWeilTest) (σ : ℝ) :
    Integrable (𝓕 (F.hatSlice σ)) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le |σ| (abs_nonneg _)
  have hbd : ∀ ξ : ℝ, ‖𝓕 (F.hatSlice σ) ξ‖ ≤
      C * (1 + (2 * Real.pi * ξ) ^ 2)⁻¹ := by
    intro ξ
    have hre :
        |(((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I).re)| ≤ |σ| := by
      simp
    have him :
        ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I).im =
          -(2 * Real.pi * ξ) := by
      simp
    have heq := F.hat_eq_fourier_slice σ ξ
    have hle : ‖F.hat ((σ : ℂ) + (-(2 * Real.pi) * ξ) * Complex.I)‖ ≤
        C / (1 + (2 * Real.pi * ξ) ^ 2) := by
      have hle0 := hhat _ hre
      convert hle0 using 2
      rw [him]
      ring
    rw [← heq]
    simpa [div_eq_mul_inv] using hle
  have hmaj : Integrable fun ξ : ℝ =>
      C * (1 + (2 * Real.pi * ξ) ^ 2)⁻¹ :=
    integrable_inv_one_add_scaled_sq.const_mul C
  have hmeas : AEStronglyMeasurable (𝓕 (F.hatSlice σ)) volume :=
    (VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
      (continuous_inner (𝕜 := ℝ)) (F.integrable_hatSlice σ)).aestronglyMeasurable
  exact hmaj.mono' hmeas (Eventually.of_forall hbd)

/-- Mathlib Fourier inversion on the Paley--Wiener slice
`t ↦ g(t) e^{σ t}`. -/
lemma FullWeilTest.fourierInv_hatSlice (F : FullWeilTest) (σ : ℝ) :
    𝓕⁻ (𝓕 (F.hatSlice σ)) = F.hatSlice σ :=
  (F.continuous_hatSlice σ).fourierInv_fourier_eq
    (F.integrable_hatSlice σ) (F.integrable_fourier_hatSlice σ)

/-- The `2π`-frequency form of the Paley--Wiener inversion:
`∫ ĥ(σ+iτ) e^{-iτ u} dτ = 2π g(u) e^{σ u}`. -/
lemma FullWeilTest.hat_fourier_inversion (F : FullWeilTest) (σ u : ℝ) :
    (∫ τ : ℝ, F.hat ((σ : ℂ) + τ * Complex.I) *
        Complex.exp (-(τ : ℂ) * Complex.I * u)) =
      (2 * Real.pi : ℂ) * F.hatSlice σ u := by
  set g : ℝ → ℂ := fun τ =>
    Complex.exp (-(τ : ℂ) * Complex.I * u) *
      F.hat ((σ : ℂ) + τ * Complex.I)
  have hinter : ∀ ξ : ℝ, ⟪ξ, u⟫ = ξ * u := fun ξ => mul_comm u ξ
  have hpoint : ∀ ξ : ℝ,
      Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (F.hatSlice σ) ξ =
        g (-(2 * Real.pi) * ξ) := by
    intro ξ
    dsimp [g]
    rw [← F.hat_eq_fourier_slice σ ξ]
    simp [hinter ξ, mul_comm, mul_left_comm, mul_assoc]
  have hFinv :
      𝓕⁻ (𝓕 (F.hatSlice σ)) u =
        ∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (F.hatSlice σ) ξ := by
    rw [Real.fourierInv_eq']
    refine integral_congr_ae (Eventually.of_forall fun ξ => ?_)
    simp [smul_eq_mul]
  have hscale :
      (∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
          𝓕 (F.hatSlice σ) ξ) =
        ∫ ξ : ℝ, g (-(2 * Real.pi) * ξ) :=
    integral_congr_ae (Eventually.of_forall hpoint)
  have hcomp := Measure.integral_comp_mul_left g (-(2 * Real.pi))
  have habs : |(-(2 * Real.pi))⁻¹| = (2 * Real.pi)⁻¹ := by
    rw [abs_inv, abs_neg, abs_of_pos]
    exact mul_pos (by norm_num) Real.pi_pos
  have h0 : 𝓕⁻ (𝓕 (F.hatSlice σ)) u = F.hatSlice σ u :=
    congrArg (fun f : ℝ → ℂ => f u) (F.fourierInv_hatSlice σ)
  have hslice : F.hatSlice σ u =
      ((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ := by
    calc
      F.hatSlice σ u = 𝓕⁻ (𝓕 (F.hatSlice σ)) u := h0.symm
      _ = ∫ ξ : ℝ, Complex.exp ((↑(2 * Real.pi * ⟪ξ, u⟫) * Complex.I)) *
            𝓕 (F.hatSlice σ) ξ := hFinv
      _ = ∫ ξ : ℝ, g (-(2 * Real.pi) * ξ) := hscale
      _ = |(-(2 * Real.pi))⁻¹| • ∫ τ : ℝ, g τ := hcomp
      _ = ((2 * Real.pi)⁻¹ : ℝ) • ∫ τ : ℝ, g τ := by rw [habs]
      _ = ((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ := by
        rw [Complex.real_smul]
        norm_cast
  have hgoal :
      (∫ τ : ℝ, F.hat ((σ : ℂ) + τ * Complex.I) *
          Complex.exp (-(τ : ℂ) * Complex.I * u)) =
        ∫ τ : ℝ, g τ :=
    integral_congr_ae (Eventually.of_forall fun τ => by
      dsimp [g]; ring)
  rw [hgoal]
  have hπ : (2 * Real.pi : ℂ) ≠ 0 := by
    exact_mod_cast (mul_ne_zero (by norm_num : (2 : ℝ) ≠ 0) Real.pi_ne_zero)
  calc
    ∫ τ : ℝ, g τ =
        (2 * Real.pi : ℂ) * (((2 * Real.pi)⁻¹ : ℂ) * ∫ τ : ℝ, g τ) := by
      field_simp [hπ]
    _ = (2 * Real.pi : ℂ) * F.hatSlice σ u := by
      rw [← hslice]

end HatFourierInversion

section RightEdgePrime

open MeasureTheory Filter
open scoped LSeries.notation

/-- Bare von-Mangoldt pairing: `∑ Λ(n) g(log n)`.  Finite because
`g` vanishes for `log n > R`.  This is the Re=2 contour prime
content, not the corpus comb channel. -/
noncomputable def FullWeilTest.primeEval (F : FullWeilTest) : ℝ :=
  ∑' n : ℕ, ArithmeticFunction.vonMangoldt n * F.toFun (Real.log n)

lemma FullWeilTest.toFun_log_eq_zero_of_lt_anchor
    (F : FullWeilTest) {n : ℕ} (hn : F.fullAnchor < n) :
    F.toFun (Real.log n) = 0 := by
  have hceil : Nat.ceil (Real.exp F.supportRadius) ≤ F.fullAnchor :=
    le_max_right _ _
  have hnR : (Nat.ceil (Real.exp F.supportRadius) : ℝ) < (n : ℝ) :=
    mod_cast (lt_of_le_of_lt hceil hn)
  have hexp : Real.exp F.supportRadius < (n : ℝ) :=
    lt_of_le_of_lt (Nat.le_ceil _) hnR
  have hlog : F.supportRadius < Real.log n := by
    have := Real.log_lt_log (Real.exp_pos F.supportRadius) hexp
    simpa [Real.log_exp] using this
  have habs : |Real.log n| = Real.log n :=
    abs_of_nonneg (le_trans F.supportRadius_nonneg hlog.le)
  exact F.support_toFun _ (by rwa [habs])

lemma FullWeilTest.primeEval_eq_sum (F : FullWeilTest) :
    F.primeEval =
      ∑ n ∈ Finset.range (F.fullAnchor + 1),
        ArithmeticFunction.vonMangoldt n * F.toFun (Real.log n) := by
  unfold FullWeilTest.primeEval
  exact tsum_eq_sum fun n hn => by
    have hlt : F.fullAnchor < n := by
      have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
      omega
    rw [F.toFun_log_eq_zero_of_lt_anchor hlt, mul_zero]

/-- Corpus comb channel is the r310 gauge `2Λ/√n`, not bare `Λ`. -/
lemma fullWeilCombSide_eq_two_div_sqrt_sum (F : FullWeilTest) :
    fullWeilCombSide F =
      ∑ n ∈ windowAtoms F.fullAnchor,
        (2 / Real.sqrt n) * ArithmeticFunction.vonMangoldt n *
          F.toFun (Real.log n) := by
  unfold fullWeilCombSide
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [combMass_eq_gauge, mul_assoc]

lemma logDeriv_riemannZeta_right_edge (τ : ℝ) :
    logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) =
      - L ↗ArithmeticFunction.vonMangoldt ((2 : ℂ) + τ * Complex.I) :=
  logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt (by simp)

lemma norm_LSeries_term_vonMangoldt_right_edge (n : ℕ) (τ : ℝ) :
    ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((2 : ℂ) + τ * Complex.I) n‖ =
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have hpos : 0 < n := Nat.pos_of_ne_zero hn
    rw [LSeries.term_of_ne_zero hn, LSeries.term_of_ne_zero hn,
      norm_div, norm_div, Complex.norm_natCast_cpow_of_pos hpos,
      Complex.norm_natCast_cpow_of_pos hpos]
    simp

lemma continuous_hat_right_edge (F : FullWeilTest) :
    Continuous fun τ : ℝ => F.hat ((2 : ℂ) + τ * Complex.I) :=
  continuous_iff_continuousAt.mpr fun τ =>
    ContinuousAt.comp (f := fun τ : ℝ => (2 : ℂ) + τ * Complex.I)
      (g := F.hat) (F.analyticAt_hat _).continuousAt
      (continuous_vertical_path 2).continuousAt

lemma continuous_LSeries_term_vonMangoldt_right_edge (n : ℕ) :
    Continuous fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((2 : ℂ) + τ * Complex.I) n := by
  rcases eq_or_ne n 0 with rfl | hn
  · simpa using continuous_const
  · have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
    have hpow : Continuous fun τ : ℝ =>
        (n : ℂ) ^ ((2 : ℂ) + τ * Complex.I) :=
      (continuous_vertical_path 2).const_cpow (Or.inl hpos)
    have hdiv : Continuous fun τ : ℝ =>
        (ArithmeticFunction.vonMangoldt n : ℂ) /
          (n : ℂ) ^ ((2 : ℂ) + τ * Complex.I) :=
      Continuous.div continuous_const hpow fun τ => by
        simp [Complex.cpow_eq_zero_iff, hpos]
    convert hdiv using 1
    funext τ
    rw [LSeries.term_of_ne_zero hn]

lemma integrable_right_edge_term_mul_hat (F : FullWeilTest) (n : ℕ) :
    Integrable fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((2 : ℂ) + τ * Complex.I) n *
        F.hat ((2 : ℂ) + τ * Complex.I) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le 2 (by norm_num)
  have hcont :
      Continuous fun τ : ℝ =>
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I) :=
    (continuous_LSeries_term_vonMangoldt_right_edge n).mul
      (continuous_hat_right_edge F)
  have hbd : ∀ τ : ℝ,
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I)‖ ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          C / (1 + τ ^ 2) := by
    intro τ
    have hre : |((2 : ℂ) + τ * Complex.I).re| ≤ 2 := by simp
    have him : ((2 : ℂ) + τ * Complex.I).im = τ := by simp
    have hh := hhat _ hre
    rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_right_edge]
    have := mul_le_mul_of_nonneg_left (by simpa [him] using hh)
      (norm_nonneg (LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n))
    simpa [mul_div_assoc] using this
  have hmaj : Integrable fun τ : ℝ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
        C / (1 + τ ^ 2) := by
    simpa [div_eq_mul_inv, mul_assoc] using
      (integrable_inv_one_add_sq.const_mul
        (‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ * C))
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

lemma summable_integral_norm_right_edge_term (F : FullWeilTest) :
    Summable fun n : ℕ =>
      ∫ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            F.hat ((2 : ℂ) + τ * Complex.I)‖ := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le 2 (by norm_num)
  have h2 : 1 < (2 : ℂ).re := by simp
  have hΛ : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact ArithmeticFunction.LSeriesSummable_vonMangoldt h2
  have hint : Integrable fun τ : ℝ => C / (1 + τ ^ 2) := by
    simpa [div_eq_mul_inv] using integrable_inv_one_add_sq.const_mul C
  have hbd : ∀ n : ℕ,
      (∫ τ : ℝ,
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              F.hat ((2 : ℂ) + τ * Complex.I)‖) ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          ∫ τ : ℝ, C / (1 + τ ^ 2) := by
    intro n
    have hle : ∀ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            F.hat ((2 : ℂ) + τ * Complex.I)‖ ≤
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
            (C / (1 + τ ^ 2)) := by
      intro τ
      have hre : |((2 : ℂ) + τ * Complex.I).re| ≤ 2 := by simp
      have him : ((2 : ℂ) + τ * Complex.I).im = τ := by simp
      have hh := hhat _ hre
      rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_right_edge]
      have := mul_le_mul_of_nonneg_left (by simpa [him] using hh)
        (norm_nonneg (LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n))
      simpa [mul_div_assoc] using this
    have hmeas : Integrable fun τ : ℝ =>
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
          (C / (1 + τ ^ 2)) :=
      hint.const_mul _
    refine (integral_mono_of_nonneg
      (Eventually.of_forall fun _ => norm_nonneg _)
      hmeas (Eventually.of_forall hle)).trans_eq ?_
    rw [integral_const_mul]
  have hsum : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt (2 : ℂ) n‖ *
        ∫ τ : ℝ, C / (1 + τ ^ 2) :=
    hΛ.mul_right _
  exact Summable.of_nonneg_of_le
    (fun _ => integral_nonneg fun _ => norm_nonneg _) hbd hsum

lemma logDeriv_hat_eq_tsum_neg_term_hat (F : FullWeilTest) (τ : ℝ) :
    logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        F.hat ((2 : ℂ) + τ * Complex.I) =
      ∑' n : ℕ,
        -(LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I)) := by
  have hs : 1 < ((2 : ℂ) + τ * Complex.I).re := by simp
  have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
  rw [logDeriv_riemannZeta_right_edge, LSeries, neg_mul, ← tsum_mul_right,
    tsum_neg]

lemma LSeries_term_vonMangoldt_right_edge_eq_exp
    {n : ℕ} (hn : n ≠ 0) (τ : ℝ) :
    LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((2 : ℂ) + τ * Complex.I) n =
      (ArithmeticFunction.vonMangoldt n : ℂ) *
        Complex.exp (-((2 : ℂ) + τ * Complex.I) * Real.log n) := by
  have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hlog : Complex.log (n : ℂ) = (Real.log n : ℂ) := by
    rw [← Complex.ofReal_natCast]
    exact (Complex.ofReal_log (Nat.cast_nonneg n)).symm
  rw [LSeries.term_of_ne_zero hn, div_eq_mul_inv, ← Complex.cpow_neg]
  rw [Complex.cpow_def_of_ne_zero hpos, hlog]
  ring_nf

lemma integral_term_mul_hat_eq_two_pi_vonMangoldt
    (F : FullWeilTest) {n : ℕ} (hn : n ≠ 0) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (F.toFun (Real.log n) : ℂ) := by
  have hinv := F.hat_fourier_inversion 2 (Real.log n)
  have hslice : F.hatSlice 2 (Real.log n) =
      (F.toFun (Real.log n) : ℂ) *
        Complex.exp ((2 : ℂ) * Real.log n) := rfl
  have hpoint : ∀ τ : ℝ,
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((2 : ℂ) + τ * Complex.I) n *
        F.hat ((2 : ℂ) + τ * Complex.I) =
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          Complex.exp (-(2 : ℂ) * Real.log n) *
            (F.hat ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) := by
    intro τ
    rw [LSeries_term_vonMangoldt_right_edge_eq_exp hn τ]
    have hsplit :
        Complex.exp (-((2 : ℂ) + τ * Complex.I) * Real.log n) =
          Complex.exp (-(2 : ℂ) * Real.log n) *
            Complex.exp (-(τ : ℂ) * Complex.I * Real.log n) := by
      rw [← Complex.exp_add]
      ring_nf
    rw [hsplit]
    ring
  set c : ℂ :=
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      Complex.exp (-(2 : ℂ) * Real.log n)
  have hrew :
      (∫ τ : ℝ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
              ((2 : ℂ) + τ * Complex.I) n *
            F.hat ((2 : ℂ) + τ * Complex.I)) =
        c * ∫ τ : ℝ,
              F.hat ((2 : ℂ) + τ * Complex.I) *
                Complex.exp (-(τ : ℂ) * Complex.I * Real.log n) := by
    have heq :
        (fun τ : ℝ =>
            LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              F.hat ((2 : ℂ) + τ * Complex.I)) =
          fun τ : ℝ =>
            c * (F.hat ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) :=
      funext hpoint
    have heq' :
        (fun τ : ℝ =>
            c * (F.hat ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n))) =
          fun τ : ℝ =>
            c • (F.hat ((2 : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) :=
      funext fun _ => (smul_eq_mul _ _).symm
    rw [heq, heq', integral_smul, smul_eq_mul]
  rw [hrew]
  have hinv' :
      (∫ τ : ℝ, F.hat ((2 : ℂ) + τ * Complex.I) *
          Complex.exp (-(τ : ℂ) * Complex.I * Real.log n)) =
        (2 * Real.pi : ℂ) * F.hatSlice 2 (Real.log n) := hinv
  rw [hinv', hslice]
  have hcancel :
      Complex.exp (-(2 : ℂ) * Real.log n) *
          Complex.exp ((2 : ℂ) * Real.log n) = 1 := by
    rw [← Complex.exp_add]
    ring_nf
    simp
  have hfactor :
      c * ((2 * Real.pi : ℂ) *
        ((F.toFun (Real.log n) : ℂ) *
          Complex.exp ((2 : ℂ) * Real.log n))) =
        (2 * Real.pi : ℂ) *
          (F.toFun (Real.log n) : ℂ) *
          (c * Complex.exp ((2 : ℂ) * Real.log n)) := by
    ring
  have hcval :
      c * Complex.exp ((2 : ℂ) * Real.log n) =
        (ArithmeticFunction.vonMangoldt n : ℂ) := by
    unfold c
    rw [mul_assoc, hcancel, mul_one]
  rw [hfactor, hcval]
  ring

lemma integral_term_mul_hat_eq_two_pi_vonMangoldt_all
    (F : FullWeilTest) (n : ℕ) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (F.toFun (Real.log n) : ℂ) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp [LSeries.term_zero]
  · exact integral_term_mul_hat_eq_two_pi_vonMangoldt F hn

lemma primeEval_complex_eq (F : FullWeilTest) :
    (∑' n : ℕ,
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (F.toFun (Real.log n) : ℂ)) =
      (F.primeEval : ℂ) := by
  have hzero : ∀ n : ℕ, n ∉ Finset.range (F.fullAnchor + 1) →
      (ArithmeticFunction.vonMangoldt n : ℂ) *
        (F.toFun (Real.log n) : ℂ) = 0 := by
    intro n hn
    have hlt : F.fullAnchor < n := by
      have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
      omega
    rw [F.toFun_log_eq_zero_of_lt_anchor hlt, Complex.ofReal_zero, mul_zero]
  rw [tsum_eq_sum hzero, F.primeEval_eq_sum]
  simp [Complex.ofReal_sum, Complex.ofReal_mul]

/-- Right vertical integral equals `-2π ∑ Λ(n) g(log n)`. -/
lemma rightVerticalIntegral_eq_prime_sum (F : FullWeilTest) :
    (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
        F.hat ((2 : ℂ) + τ * Complex.I)) =
      - (2 * Real.pi : ℂ) * (F.primeEval : ℂ) := by
  have hpt :
      (∫ τ : ℝ, logDeriv riemannZeta ((2 : ℂ) + τ * Complex.I) *
          F.hat ((2 : ℂ) + τ * Complex.I)) =
        ∫ τ : ℝ,
          ∑' n : ℕ,
            -(LSeries.term ↗ArithmeticFunction.vonMangoldt
                ((2 : ℂ) + τ * Complex.I) n *
              F.hat ((2 : ℂ) + τ * Complex.I)) :=
    integral_congr_ae (Eventually.of_forall
      (logDeriv_hat_eq_tsum_neg_term_hat F))
  have hswap :=
    integral_tsum_of_summable_integral_norm
      (F := fun (n : ℕ) (τ : ℝ) =>
        -(LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((2 : ℂ) + τ * Complex.I) n *
          F.hat ((2 : ℂ) + τ * Complex.I)))
      (fun n => (integrable_right_edge_term_mul_hat F n).neg)
      (by
        simpa [norm_neg] using
          summable_integral_norm_right_edge_term F)
  rw [hpt, ← hswap]
  simp_rw [integral_neg, integral_term_mul_hat_eq_two_pi_vonMangoldt_all F]
  have hsummable :
      Summable fun n : ℕ =>
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          (F.toFun (Real.log n) : ℂ) :=
    summable_of_ne_finset_zero fun n hn => by
      have hlt : F.fullAnchor < n := by
        have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
        omega
      rw [F.toFun_log_eq_zero_of_lt_anchor hlt, Complex.ofReal_zero, mul_zero]
  have hfactor :
      (∑' n : ℕ,
          (2 * Real.pi : ℂ) *
            (ArithmeticFunction.vonMangoldt n : ℂ) *
              (F.toFun (Real.log n) : ℂ)) =
        (2 * Real.pi : ℂ) * (F.primeEval : ℂ) := by
    rw [← primeEval_complex_eq F]
    rw [← tsum_mul_left]
    exact tsum_congr fun n => by ring
  rw [tsum_neg, hfactor]
  ring

end RightEdgePrime

section LeftEdgePrime

open MeasureTheory Filter Complex
open scoped LSeries.notation Topology

/-- The existing r527 identity, but from an eventual FE equality
rather than the `|Im| ≥ 2` ball.  Used on the whole left edge. -/
lemma logDeriv_riemannZeta_functional_of_eventually {s : ℂ}
    (hfe : (fun w : ℂ => riemannZeta (1 - w)) =ᶠ[𝓝 s]
      fun w => zetaFEFactor w * riemannZeta w)
    (hs1 : s ≠ 1) (h1s : 1 - s ≠ 1)
    (hG : ∀ n : ℕ, s ≠ -n)
    (hGne : zetaFEFactor s ≠ 0) (hz : riemannZeta s ≠ 0) :
    logDeriv riemannZeta s =
      - logDeriv riemannZeta (1 - s) - logDeriv zetaFEFactor s := by
  have hld :
      logDeriv (fun w : ℂ => riemannZeta (1 - w)) s =
        logDeriv (fun w => zetaFEFactor w * riemannZeta w) s := by
    rw [logDeriv_apply, logDeriv_apply, hfe.deriv_eq, hfe.eq_of_nhds]
  have hd := hasDerivAt_one_sub s
  have hf : DifferentiableAt ℂ riemannZeta (1 - s) :=
    differentiableAt_riemannZeta h1s
  have hL : logDeriv (fun w : ℂ => riemannZeta (1 - w)) s =
      - logDeriv riemannZeta (1 - s) := by
    have hcomp :=
      logDeriv_comp (f := riemannZeta) (g := fun w : ℂ => 1 - w)
        hf hd.differentiableAt
    have hfun : (fun w : ℂ => riemannZeta (1 - w)) =
        riemannZeta ∘ fun w : ℂ => 1 - w := rfl
    rw [hfun, hcomp, hd.deriv]
    ring
  have hR : logDeriv (fun w => zetaFEFactor w * riemannZeta w) s =
      logDeriv zetaFEFactor s + logDeriv riemannZeta s :=
    logDeriv_mul s hGne hz (differentiableAt_zetaFEFactor hG)
      (differentiableAt_riemannZeta hs1)
  have hsum : logDeriv zetaFEFactor s + logDeriv riemannZeta s =
      - logDeriv riemannZeta (1 - s) := by
    rw [← hR, ← hld, hL]
  exact eq_sub_of_add_eq (add_comm (logDeriv zetaFEFactor s) _ ▸ hsum)

lemma ne_neg_nat_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hre : s.re = -1 / 16) (n : ℕ) : s ≠ -n := by
  intro hs
  have hre' : (-n : ℂ).re = -1 / 16 := by rw [← hs, hre]
  have : -(n : ℝ) = -1 / 16 := by simpa using hre'
  have hn : (n : ℝ) = 1 / 16 := by linarith
  have hlt : (n : ℝ) < 1 := by
    rw [hn]; norm_num
  have : n < 1 := mod_cast hlt
  have h0 : n = 0 := by omega
  simp [h0] at hn

lemma ne_one_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hre : s.re = -1 / 16) : s ≠ 1 := by
  intro hs
  have : (1 : ℂ).re = -1 / 16 := by rw [← hs, hre]
  norm_num at this

lemma ne_zero_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hre : s.re = -1 / 16) : s ≠ 0 := by
  intro hs
  simp [hs] at hre
  norm_num at hre

lemma cos_pi_div_two_ne_zero_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hre : s.re = -1 / 16) :
    Complex.cos (Real.pi * s / 2) ≠ 0 := by
  by_cases him : s.im = 0
  · have hs : s = ((-1 / 16 : ℝ) : ℂ) :=
      Complex.ext (by simpa using hre) (by simpa [him])
    rw [hs]
    have harg : (Real.pi : ℂ) * ((-1 / 16 : ℝ) : ℂ) / 2 =
        ((-(Real.pi / 32) : ℝ) : ℂ) := by
      simp [div_eq_mul_inv]
      ring
    rw [harg, ← ofReal_cos, Real.cos_neg]
    refine ofReal_ne_zero.mpr
      (ne_of_gt (Real.cos_pos_of_mem_Ioo ⟨?_, ?_⟩))
    · have hπ : (0 : ℝ) < Real.pi := Real.pi_pos
      linarith
    · exact div_lt_div_of_pos_left Real.pi_pos (by norm_num) (by norm_num)
  · have himπ : ((Real.pi : ℂ) * s / 2).im ≠ 0 := by
      rw [im_pi_mul_div_two]
      exact div_ne_zero (mul_ne_zero Real.pi_ne_zero him) two_ne_zero
    exact cos_ne_zero_of_im_ne_zero himπ

lemma zetaFEFactor_ne_zero_of_re_eq_neg_one_div_sixteen {s : ℂ}
    (hre : s.re = -1 / 16) : zetaFEFactor s ≠ 0 := by
  have hG : ∀ n : ℕ, s ≠ -n :=
    ne_neg_nat_of_re_eq_neg_one_div_sixteen hre
  unfold zetaFEFactor
  refine mul_ne_zero (mul_ne_zero (mul_ne_zero two_ne_zero ?_) ?_)
    (cos_pi_div_two_ne_zero_of_re_eq_neg_one_div_sixteen hre)
  · exact cpow_ne_zero_iff.mpr (Or.inl two_mul_pi_ne_zero)
  · exact Complex.Gamma_ne_zero hG

lemma re_mem_left_edge_nhds_ball {s w : ℂ}
    (hre : s.re = -1 / 16)
    (hw : w ∈ Metric.ball s (1 / 32)) :
    - (3 / 32 : ℝ) < w.re ∧ w.re < - (1 / 32 : ℝ) := by
  have hd : ‖w - s‖ < 1 / 32 := mem_ball_iff_norm.mp hw
  have hre_le : |w.re - s.re| ≤ ‖w - s‖ := by
    simpa [sub_re] using abs_re_le_norm (w - s)
  have hre_lt : |w.re - (-1 / 16)| < 1 / 32 := by
    rw [hre] at hre_le
    exact lt_of_le_of_lt hre_le hd
  have hio := abs_lt.mp hre_lt
  constructor <;> linarith [hio.1, hio.2]

lemma eventuallyEq_riemannZeta_one_sub_factor_left_edge {s : ℂ}
    (hre : s.re = -1 / 16) :
    (fun w : ℂ => riemannZeta (1 - w)) =ᶠ[𝓝 s]
      fun w => zetaFEFactor w * riemannZeta w := by
  refine Filter.eventuallyEq_of_mem
      (Metric.ball_mem_nhds s (by norm_num : (0 : ℝ) < 1 / 32)) ?_
  intro w hw
  obtain ⟨hlo, hhi⟩ := re_mem_left_edge_nhds_ball hre hw
  have hw1 : w ≠ 1 := by
    intro heq
    have : (1 : ℝ) = w.re := by simpa using congrArg Complex.re heq.symm
    linarith
  have hwG : ∀ n : ℕ, w ≠ -n := by
    intro n hn
    have hre' : w.re = -(n : ℝ) := by
      simpa using congrArg Complex.re hn
    have hn0 : n ≠ 0 := by
      intro h0
      simp [h0] at hre'
      linarith [hhi]
    have hn1 : (1 : ℝ) ≤ (n : ℝ) :=
      Nat.one_le_cast.mpr (Nat.succ_le_iff.mpr (Nat.pos_of_ne_zero hn0))
    have : w.re ≤ -1 := by
      rw [hre']
      linarith [hn1]
    linarith [hlo]
  exact riemannZeta_one_sub_factor hwG hw1

/-- FE logDeriv on the whole left vertical, including `|τ| < 2`. -/
lemma logDeriv_riemannZeta_left_edge (τ : ℝ) :
    logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
      - logDeriv riemannZeta (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) -
        logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  set s : ℂ := ((-1 / 16 : ℝ) : ℂ) + τ * Complex.I
  have hre : s.re = -1 / 16 := by simp [s]
  have hsub : 1 - s = ((17 / 16 : ℝ) : ℂ) - τ * Complex.I := by
    apply Complex.ext
    · simp [s]; ring
    · simp [s]
  have hs1 : s ≠ 1 := ne_one_of_re_eq_neg_one_div_sixteen hre
  have h1s : 1 - s ≠ 1 := by
    intro heq
    have : s = 0 := by
      simpa using congrArg (fun z : ℂ => 1 - z) heq
    exact ne_zero_of_re_eq_neg_one_div_sixteen hre this
  have hG : ∀ n : ℕ, s ≠ -n :=
    ne_neg_nat_of_re_eq_neg_one_div_sixteen hre
  have hGne := zetaFEFactor_ne_zero_of_re_eq_neg_one_div_sixteen hre
  have hz : riemannZeta s ≠ 0 :=
    riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen hre
  have hfe := eventuallyEq_riemannZeta_one_sub_factor_left_edge hre
  have hmain :=
    logDeriv_riemannZeta_functional_of_eventually hfe hs1 h1s hG hGne hz
  rw [hsub] at hmain
  simpa [s] using hmain

/-- Explicit archimedean factor `χ'/χ` on the whole left edge,
including `τ = 0`.  Separate from the reflected prime comb.
NO RH CLAIM. -/
lemma logDeriv_zetaFEFactor_left_edge (τ : ℝ) :
    logDeriv zetaFEFactor (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
      - Complex.log (2 * (Real.pi : ℂ)) +
        digamma (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
        ((Real.pi : ℂ) / 2) *
          tan (Real.pi * (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) / 2) := by
  set s : ℂ := ((-1 / 16 : ℝ) : ℂ) + τ * Complex.I
  have hre : s.re = -1 / 16 := by simp [s]
  have hG : ∀ n : ℕ, s ≠ -n :=
    ne_neg_nat_of_re_eq_neg_one_div_sixteen hre
  have hcos := cos_pi_div_two_ne_zero_of_re_eq_neg_one_div_sixteen hre
  simpa [s] using logDeriv_zetaFEFactor hG hcos

lemma logDeriv_riemannZeta_dual_left_edge (τ : ℝ) :
    logDeriv riemannZeta (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) =
      - L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) :=
  logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt (by simp; norm_num)

/-- Honest left-edge prime pairing: `∑ Λ(n) n⁻¹ g(-log n)`.
The inversion variable is `-log n`; evenness of `g` identifies
this with `∑ Λ(n) n⁻¹ g(log n)` below.  Finite because `g`
vanishes for `|log n| > R`. -/
noncomputable def FullWeilTest.reflectedPrimeEval (F : FullWeilTest) : ℝ :=
  ∑' n : ℕ, ArithmeticFunction.vonMangoldt n * (n : ℝ)⁻¹ *
    F.toFun (-Real.log n)

lemma FullWeilTest.reflectedPrimeEval_eq_inv_toFun
    (F : FullWeilTest) :
    F.reflectedPrimeEval =
      ∑' n : ℕ, ArithmeticFunction.vonMangoldt n * (n : ℝ)⁻¹ *
        F.toFun (Real.log n) := by
  unfold FullWeilTest.reflectedPrimeEval
  refine tsum_congr fun n => ?_
  rw [F.even_toFun]

lemma FullWeilTest.reflectedPrimeEval_eq_sum (F : FullWeilTest) :
    F.reflectedPrimeEval =
      ∑ n ∈ Finset.range (F.fullAnchor + 1),
        ArithmeticFunction.vonMangoldt n * (n : ℝ)⁻¹ *
          F.toFun (Real.log n) := by
  rw [F.reflectedPrimeEval_eq_inv_toFun]
  exact tsum_eq_sum fun n hn => by
    have hlt : F.fullAnchor < n := by
      have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
      omega
    rw [F.toFun_log_eq_zero_of_lt_anchor hlt, mul_zero]

/-- The two contour prime channels combine to
`∑ Λ(n)(1 + n⁻¹) g(log n)`, not the corpus `2Λ/√n`. -/
lemma contourPrimePairing_eq_one_add_inv_sum (F : FullWeilTest) :
    F.primeEval + F.reflectedPrimeEval =
      ∑ n ∈ Finset.range (F.fullAnchor + 1),
        ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
          F.toFun (Real.log n) := by
  rw [F.primeEval_eq_sum, F.reflectedPrimeEval_eq_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun n _ => ?_
  ring

/-- Pointwise weight discrepancy: `1 + n⁻¹ ≥ 2/√n`, equality only at
`n = 1` (where `Λ = 0`).  The contour pairing is not the corpus gauge. -/
lemma one_add_inv_ge_two_div_sqrt {n : ℕ} (hn : 0 < n) :
    2 / Real.sqrt n ≤ 1 + (n : ℝ)⁻¹ := by
  have hpos : (0 : ℝ) < n := Nat.cast_pos.mpr hn
  have hsqrt : 0 < Real.sqrt n := Real.sqrt_pos.mpr hpos
  have hexpand : (Real.sqrt n - 1) ^ 2 =
      (n : ℝ) - 2 * Real.sqrt n + 1 := by
    calc (Real.sqrt n - 1) ^ 2
        = Real.sqrt n ^ 2 - 2 * Real.sqrt n + 1 := by ring
      _ = (n : ℝ) - 2 * Real.sqrt n + 1 := by rw [Real.sq_sqrt hpos.le]
  have hside : 2 * Real.sqrt n ≤ (n : ℝ) + 1 := by
    have hsq : 0 ≤ (Real.sqrt n - 1) ^ 2 := sq_nonneg _
    linarith [hsq, hexpand]
  have hleft : 2 * Real.sqrt n / n = 2 / Real.sqrt n := by
    calc 2 * Real.sqrt n / n
        = 2 * Real.sqrt n / (Real.sqrt n * Real.sqrt n) := by
          nth_rw 2 [← Real.mul_self_sqrt hpos.le]
      _ = 2 / Real.sqrt n := by
          field_simp [hsqrt.ne']
  have hright : ((n : ℝ) + 1) / n = 1 + (n : ℝ)⁻¹ := by
    rw [add_div, div_self hpos.ne', div_eq_mul_inv, one_mul]
  have hgoal : 2 * Real.sqrt n / n ≤ ((n : ℝ) + 1) / n :=
    div_le_div_of_nonneg_right hside hpos.le
  rwa [hleft, hright] at hgoal

lemma continuous_hat_left_edge (F : FullWeilTest) :
    Continuous fun τ : ℝ =>
      F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) :=
  continuous_iff_continuousAt.mpr fun τ =>
    ContinuousAt.comp (f := fun τ : ℝ =>
        ((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)
      (g := F.hat) (F.analyticAt_hat _).continuousAt
      (continuous_vertical_path (-1 / 16)).continuousAt

lemma continuous_dual_left_path :
    Continuous fun τ : ℝ =>
      ((17 / 16 : ℝ) : ℂ) - τ * Complex.I := by
  convert (continuous_vertical_path (17 / 16)).comp continuous_neg using 1
  funext τ
  simp [sub_eq_add_neg]

lemma continuous_LSeries_term_vonMangoldt_dual_left_edge (n : ℕ) :
    Continuous fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n := by
  rcases eq_or_ne n 0 with rfl | hn
  · simpa using continuous_const
  · have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
    have hpow : Continuous fun τ : ℝ =>
        (n : ℂ) ^ (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) :=
      continuous_dual_left_path.const_cpow (Or.inl hpos)
    have hdiv : Continuous fun τ : ℝ =>
        (ArithmeticFunction.vonMangoldt n : ℂ) /
          (n : ℂ) ^ (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) :=
      Continuous.div continuous_const hpow fun τ => by
        simp [Complex.cpow_eq_zero_iff, hpos]
    convert hdiv using 1
    funext τ
    rw [LSeries.term_of_ne_zero hn]

lemma norm_LSeries_term_vonMangoldt_dual_left_edge (n : ℕ) (τ : ℝ) :
    ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n‖ =
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp
  · have hpos : 0 < n := Nat.pos_of_ne_zero hn
    rw [LSeries.term_of_ne_zero hn, LSeries.term_of_ne_zero hn,
      norm_div, norm_div, Complex.norm_natCast_cpow_of_pos hpos,
      Complex.norm_natCast_cpow_of_pos hpos]
    simp

lemma integrable_left_edge_term_mul_hat (F : FullWeilTest) (n : ℕ) :
    Integrable fun τ : ℝ =>
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le (1 / 16) (by norm_num)
  have hcont :
      Continuous fun τ : ℝ =>
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) :=
    (continuous_LSeries_term_vonMangoldt_dual_left_edge n).mul
      (continuous_hat_left_edge F)
  have hbd : ∀ τ : ℝ,
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ *
          C / (1 + τ ^ 2) := by
    intro τ
    have hre : |(((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).re| ≤ 1 / 16 := by
      simp
      norm_num
    have him : (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).im = τ := by simp
    have hh := hhat _ hre
    rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_dual_left_edge]
    have := mul_le_mul_of_nonneg_left (by simpa [him] using hh)
      (norm_nonneg (LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n))
    simpa [mul_div_assoc] using this
  have hmaj : Integrable fun τ : ℝ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ * C / (1 + τ ^ 2) := by
    simpa [div_eq_mul_inv, mul_assoc] using
      (integrable_inv_one_add_sq.const_mul
        (‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ * C))
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

lemma summable_integral_norm_left_edge_term (F : FullWeilTest) :
    Summable fun n : ℕ =>
      ∫ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le (1 / 16) (by norm_num)
  have hσ : 1 < (((17 / 16 : ℝ) : ℂ).re) := by simp; norm_num
  have hΛ : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ := by
    rw [summable_norm_iff]
    exact ArithmeticFunction.LSeriesSummable_vonMangoldt hσ
  have hint : Integrable fun τ : ℝ => C / (1 + τ ^ 2) := by
    simpa [div_eq_mul_inv] using integrable_inv_one_add_sq.const_mul C
  have hbd : ∀ n : ℕ,
      (∫ τ : ℝ,
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖) ≤
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ *
          ∫ τ : ℝ, C / (1 + τ ^ 2) := by
    intro n
    have hle : ∀ τ : ℝ,
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
          ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
            ((17 / 16 : ℝ) : ℂ) n‖ *
            (C / (1 + τ ^ 2)) := by
      intro τ
      have hre : |(((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).re| ≤ 1 / 16 := by
        simp
        norm_num
      have him : (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).im = τ := by simp
      have hh := hhat _ hre
      rw [Complex.norm_mul, norm_LSeries_term_vonMangoldt_dual_left_edge]
      have := mul_le_mul_of_nonneg_left (by simpa [him] using hh)
        (norm_nonneg (LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n))
      simpa [mul_div_assoc] using this
    have hmeas : Integrable fun τ : ℝ =>
        ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
          ((17 / 16 : ℝ) : ℂ) n‖ * (C / (1 + τ ^ 2)) :=
      hint.const_mul _
    refine (integral_mono_of_nonneg
      (Eventually.of_forall fun _ => norm_nonneg _)
      hmeas (Eventually.of_forall hle)).trans_eq ?_
    rw [integral_const_mul]
  have hsum : Summable fun n : ℕ =>
      ‖LSeries.term ↗ArithmeticFunction.vonMangoldt
        ((17 / 16 : ℝ) : ℂ) n‖ *
        ∫ τ : ℝ, C / (1 + τ ^ 2) :=
    hΛ.mul_right _
  exact Summable.of_nonneg_of_le
    (fun _ => integral_nonneg fun _ => norm_nonneg _) hbd hsum

lemma logDeriv_hat_eq_tsum_dual_term_hat_sub_fe (F : FullWeilTest)
    (τ : ℝ) :
    logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
      (∑' n : ℕ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
        logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by simp; norm_num
  have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
  rw [logDeriv_riemannZeta_left_edge, logDeriv_riemannZeta_dual_left_edge,
    neg_neg, sub_mul, LSeries, tsum_mul_right]

lemma LSeries_term_vonMangoldt_dual_left_edge_eq_exp
    {n : ℕ} (hn : n ≠ 0) (τ : ℝ) :
    LSeries.term ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n =
      (ArithmeticFunction.vonMangoldt n : ℂ) *
        Complex.exp (-(((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          Real.log n) := by
  have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hlog : Complex.log (n : ℂ) = (Real.log n : ℂ) := by
    rw [← Complex.ofReal_natCast]
    exact (Complex.ofReal_log (Nat.cast_nonneg n)).symm
  rw [LSeries.term_of_ne_zero hn, div_eq_mul_inv, ← Complex.cpow_neg]
  rw [Complex.cpow_def_of_ne_zero hpos, hlog]
  ring_nf

lemma exp_neg_real_log_nat {n : ℕ} (hn : n ≠ 0) :
    Complex.exp (-(Real.log n : ℂ)) = (n : ℂ)⁻¹ := by
  have hpos : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hlog : Complex.log (n : ℂ) = (Real.log n : ℂ) := by
    rw [← Complex.ofReal_natCast]
    exact (Complex.ofReal_log (Nat.cast_nonneg n)).symm
  rw [← hlog, Complex.exp_neg, Complex.exp_log hpos]

/-- Termwise inversion at `σ = -1/16`, `u = -log n`.
The Dirichlet power `n^{-17/16}` times the slice factor `n^{1/16}`
cancels to `n⁻¹`. -/
lemma integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n
    (F : FullWeilTest) {n : ℕ} (hn : n ≠ 0) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
          (F.toFun (-Real.log n) : ℂ) := by
  set u : ℝ := -Real.log n
  have hinv := F.hat_fourier_inversion (-1 / 16) u
  have hslice : F.hatSlice (-1 / 16) u =
      (F.toFun u : ℂ) * Complex.exp ((-1 / 16 : ℝ) * u) := rfl
  have hpoint : ∀ τ : ℝ,
      LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
        (ArithmeticFunction.vonMangoldt n : ℂ) *
          Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
            (F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) := by
    intro τ
    rw [LSeries_term_vonMangoldt_dual_left_edge_eq_exp hn τ]
    have hsplit :
        Complex.exp (-(((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            Real.log n) =
          Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
            Complex.exp (-(τ : ℂ) * Complex.I * u) := by
      rw [← Complex.exp_add]
      congr 1
      unfold u
      push_cast
      ring
    rw [hsplit]
    ring
  set c : ℂ :=
    (ArithmeticFunction.vonMangoldt n : ℂ) *
      Complex.exp (-((17 / 16 : ℂ) * Real.log n))
  have hrew :
      (∫ τ : ℝ,
          LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
        c * ∫ τ : ℝ,
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
                Complex.exp (-(τ : ℂ) * Complex.I * u) := by
    have heq :
        (fun τ : ℝ =>
            LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
          fun τ : ℝ =>
            c * (F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) :=
      funext hpoint
    have heq' :
        (fun τ : ℝ =>
            c * (F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u))) =
          fun τ : ℝ =>
            c • (F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              Complex.exp (-(τ : ℂ) * Complex.I * u)) :=
      funext fun _ => (smul_eq_mul _ _).symm
    rw [heq, heq', integral_smul, smul_eq_mul]
  rw [hrew]
  have hinv' :
      (∫ τ : ℝ, F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          Complex.exp (-(τ : ℂ) * Complex.I * u)) =
        (2 * Real.pi : ℂ) * F.hatSlice (-1 / 16) u := hinv
  rw [hinv', hslice]
  have hexpσ :
      Complex.exp ((-1 / 16 : ℝ) * u) =
        Complex.exp ((-1 / 16 : ℂ) * (u : ℂ)) := by
    simp [ofReal_mul]
  have hcancel :
      Complex.exp (-((17 / 16 : ℂ) * Real.log n)) *
          Complex.exp ((-1 / 16 : ℂ) * (u : ℂ)) =
        Complex.exp (-(Real.log n : ℂ)) := by
    rw [← Complex.exp_add]
    congr 1
    unfold u
    push_cast
    ring
  have hfactor :
      c * ((2 * Real.pi : ℂ) *
        ((F.toFun u : ℂ) * Complex.exp ((-1 / 16 : ℝ) * u))) =
        (2 * Real.pi : ℂ) * (F.toFun u : ℂ) *
          (c * Complex.exp ((-1 / 16 : ℂ) * (u : ℂ))) := by
    rw [hexpσ]
    ring
  have hcval :
      c * Complex.exp ((-1 / 16 : ℂ) * (u : ℂ)) =
        (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ := by
    unfold c
    rw [mul_assoc, hcancel, exp_neg_real_log_nat hn]
  rw [hfactor, hcval]
  simp [u]
  ring

lemma integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n_all
    (F : FullWeilTest) (n : ℕ) :
    (∫ τ : ℝ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) *
        (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
          (F.toFun (-Real.log n) : ℂ) := by
  rcases eq_or_ne n 0 with rfl | hn
  · simp [LSeries.term_zero]
  · exact integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n F hn

lemma reflectedPrimeEval_complex_eq (F : FullWeilTest) :
    (∑' n : ℕ,
        (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
          (F.toFun (-Real.log n) : ℂ)) =
      (F.reflectedPrimeEval : ℂ) := by
  have hzero : ∀ n : ℕ, n ∉ Finset.range (F.fullAnchor + 1) →
      (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
        (F.toFun (-Real.log n) : ℂ) = 0 := by
    intro n hn
    have hlt : F.fullAnchor < n := by
      have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
      omega
    rw [F.even_toFun, F.toFun_log_eq_zero_of_lt_anchor hlt,
      Complex.ofReal_zero, mul_zero]
  rw [tsum_eq_sum hzero]
  have hsum := F.reflectedPrimeEval_eq_sum
  rw [hsum, Complex.ofReal_sum]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [F.even_toFun, Complex.ofReal_mul, Complex.ofReal_mul,
    Complex.ofReal_inv, Complex.ofReal_natCast]

lemma continuous_logDeriv_dual_left_edge :
    Continuous fun τ : ℝ =>
      logDeriv riemannZeta
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) :=
  continuous_iff_continuousAt.mpr fun τ =>
    ContinuousAt.comp
      (f := fun τ : ℝ => ((17 / 16 : ℝ) : ℂ) - τ * Complex.I)
      (g := logDeriv riemannZeta)
      (analyticAt_logDeriv_riemannZeta
        (by
          intro h
          have : (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re = 1 := by
            simpa using congrArg Complex.re h
          simp at this
          norm_num at this)
        (riemannZeta_ne_zero_of_one_lt_re (by simp; norm_num))).continuousAt
      continuous_dual_left_path.continuousAt

lemma integrable_LSeries_hat_left_edge (F : FullWeilTest) :
    Integrable fun τ : ℝ =>
      L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  obtain ⟨C, hC0, hhat⟩ :=
    F.norm_hat_le_inv_sq_of_abs_re_le (1 / 16) (by norm_num)
  have hcont :
      Continuous fun τ : ℝ =>
        L ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
    have hL : Continuous fun τ : ℝ =>
        L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) := by
      convert continuous_logDeriv_dual_left_edge.neg using 1
      funext τ
      rw [logDeriv_riemannZeta_dual_left_edge, neg_neg]
    exact hL.mul (continuous_hat_left_edge F)
  have hbd : ∀ τ : ℝ,
      ‖L ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)‖ ≤
        ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ *
          C / (1 + τ ^ 2) := by
    intro τ
    have hre : |(((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).re| ≤ 1 / 16 := by
      simp
      norm_num
    have him : (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I).im = τ := by simp
    have hh := hhat _ hre
    have hζ : ‖logDeriv riemannZeta
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ ≤
        ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ :=
      norm_logDeriv_riemannZeta_le_at_seventeen_sixteen (by simp)
    have hL : ‖L ↗ArithmeticFunction.vonMangoldt
        (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ ≤
        ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ := by
      have hnorm : ‖L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ =
          ‖logDeriv riemannZeta
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I)‖ := by
        rw [logDeriv_riemannZeta_dual_left_edge, norm_neg]
      rw [hnorm]
      exact hζ
    rw [Complex.norm_mul]
    have := mul_le_mul hL (by simpa [him] using hh) (norm_nonneg _)
      (norm_nonneg _)
    simpa [mul_div_assoc] using this
  have hmaj : Integrable fun τ : ℝ =>
      ‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ * C / (1 + τ ^ 2) := by
    simpa [div_eq_mul_inv, mul_assoc] using
      (integrable_inv_one_add_sq.const_mul
        (‖logDeriv riemannZeta ((17 / 16 : ℝ) : ℂ)‖ * C))
  exact hmaj.mono' hcont.aestronglyMeasurable (Eventually.of_forall hbd)

lemma integrable_left_edge_fe_integrand (F : FullWeilTest) :
    Integrable fun τ : ℝ =>
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  have hpt : (fun τ : ℝ =>
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
    (fun τ : ℝ =>
      L ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
    (fun τ : ℝ =>
      logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) := by
    funext τ
    have h := logDeriv_hat_eq_tsum_dual_term_hat_sub_fe F τ
    have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by simp; norm_num
    have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
    have htsum :
        (∑' n : ℕ,
            LSeries.term ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
          L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
      rw [LSeries, tsum_mul_right]
    rw [htsum] at h
    calc
      logDeriv zetaFEFactor
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) =
          L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
          (L ↗ArithmeticFunction.vonMangoldt
              (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
            F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
            logDeriv zetaFEFactor
                (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) := by
        ring
      _ = L ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
        logDeriv riemannZeta (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
        rw [← h]
  rw [hpt]
  exact (integrable_LSeries_hat_left_edge F).sub
    (integrable_left_edge_integrand F)

/-- Named remaining clamp: the left-edge archimedean channel
`∫ (χ'/χ)(-1/16+iτ) ĥ dτ`, not evaluated in this round. -/
noncomputable def FullWeilTest.leftEdgeArchIntegral
    (F : FullWeilTest) : ℂ :=
  ∫ τ : ℝ, logDeriv zetaFEFactor
      (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
    F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)

/-- r534: the arch clamp with its three honest factors exposed:
the `-log(2π)` constant, the digamma term, and the tangent term.
This is a pointwise substitution under the already convergent combined
integral; splitting the three improper integrals separately still
requires individual digamma/tangent integrability estimates. -/
lemma leftEdgeArchIntegral_eq_explicit_factor_integral
    (F : FullWeilTest) :
    F.leftEdgeArchIntegral =
      ∫ τ : ℝ,
        (- Complex.log (2 * (Real.pi : ℂ)) +
            digamma (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) -
            ((Real.pi : ℂ) / 2) *
              tan (Real.pi *
                (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) / 2)) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
  unfold FullWeilTest.leftEdgeArchIntegral
  apply integral_congr_ae
  filter_upwards with τ
  rw [logDeriv_zetaFEFactor_left_edge]

/-- Left vertical integral equals
`2π ∑ Λ(n) n⁻¹ g(-log n)` minus the arch clamp. -/
lemma leftVerticalIntegral_eq_reflected_prime_sub_arch
    (F : FullWeilTest) :
    (∫ τ : ℝ, logDeriv riemannZeta
          (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
      (2 * Real.pi : ℂ) * (F.reflectedPrimeEval : ℂ) -
        F.leftEdgeArchIntegral := by
  have hpt :
      (∫ τ : ℝ, logDeriv riemannZeta
            (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) =
        ∫ τ : ℝ,
          (∑' n : ℕ,
              LSeries.term ↗ArithmeticFunction.vonMangoldt
                (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I)) -
            logDeriv zetaFEFactor
              (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) *
              F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) :=
    integral_congr_ae (Eventually.of_forall
      (logDeriv_hat_eq_tsum_dual_term_hat_sub_fe F))
  have hA := integrable_LSeries_hat_left_edge F
  have hB := integrable_left_edge_fe_integrand F
  have hA' : Integrable fun τ : ℝ =>
      ∑' n : ℕ,
        LSeries.term ↗ArithmeticFunction.vonMangoldt
          (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
        F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I) := by
    convert hA using 1
    funext τ
    have hs : 1 < (((17 / 16 : ℝ) : ℂ) - τ * Complex.I).re := by simp; norm_num
    have _hL := ArithmeticFunction.LSeriesSummable_vonMangoldt hs
    rw [LSeries, tsum_mul_right]
  have hsplit := integral_sub hA' hB
  rw [hpt, hsplit]
  have hswap :=
    integral_tsum_of_summable_integral_norm
      (F := fun (n : ℕ) (τ : ℝ) =>
        LSeries.term ↗ArithmeticFunction.vonMangoldt
            (((17 / 16 : ℝ) : ℂ) - τ * Complex.I) n *
          F.hat (((-1 / 16 : ℝ) : ℂ) + τ * Complex.I))
      (integrable_left_edge_term_mul_hat F)
      (summable_integral_norm_left_edge_term F)
  rw [← hswap]
  simp_rw [integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n_all F]
  have hsummable :
      Summable fun n : ℕ =>
        (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
          (F.toFun (-Real.log n) : ℂ) :=
    summable_of_ne_finset_zero fun n hn => by
      have hlt : F.fullAnchor < n := by
        have : ¬ n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
        omega
      rw [F.even_toFun, F.toFun_log_eq_zero_of_lt_anchor hlt,
        Complex.ofReal_zero, mul_zero]
  have hfactor :
      (∑' n : ℕ,
          (2 * Real.pi : ℂ) *
            (ArithmeticFunction.vonMangoldt n : ℂ) * (n : ℂ)⁻¹ *
              (F.toFun (-Real.log n) : ℂ)) =
        (2 * Real.pi : ℂ) * (F.reflectedPrimeEval : ℂ) := by
    rw [← reflectedPrimeEval_complex_eq F]
    rw [← tsum_mul_left]
    exact tsum_congr fun n => by ring
  rw [hfactor]
  rfl

end LeftEdgePrime

/-- r534 honest contour assembly, before taking real parts.  Horizontal
edges have vanished in `contourIdentityLimitAlongGaps`; the pole at `1`
is the explicit `-F.hat 1` on the spectral side.  The two vertical
prime channels have weights `Λ(n)` and `Λ(n)/n`, respectively. -/
theorem contourExplicitFormula_honest_complex (F : FullWeilTest) :
    (2 * (Real.pi : ℂ)) *
        ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) -
          F.hat 1) =
      F.leftEdgeArchIntegral -
        (2 * (Real.pi : ℂ)) *
          ((F.primeEval : ℂ) + (F.reflectedPrimeEval : ℂ)) := by
  have hcont := contourIdentityLimitAlongGaps F
  rw [rightVerticalIntegral_eq_prime_sum F,
    leftVerticalIntegral_eq_reflected_prime_sub_arch F] at hcont
  simp only [smul_eq_mul] at hcont
  apply mul_left_cancel₀ Complex.I_ne_zero
  calc
    Complex.I * ((2 * (Real.pi : ℂ)) *
        ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) -
          F.hat 1)) =
        (2 * (Real.pi : ℂ) * Complex.I) *
          ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * F.hat ρ) -
            F.hat 1) := by ring
    _ = Complex.I *
          (- (2 * Real.pi : ℂ) * (F.primeEval : ℂ)) -
        Complex.I *
          ((2 * Real.pi : ℂ) * (F.reflectedPrimeEval : ℂ) -
            F.leftEdgeArchIntegral) := hcont.symm
    _ = Complex.I *
        (F.leftEdgeArchIntegral -
          (2 * (Real.pi : ℂ)) *
            ((F.primeEval : ℂ) + (F.reflectedPrimeEval : ℂ))) := by ring

/-- r534 honest three-channel contour identity in the real normalization
used by `standardExplicitFormula`.  This is the actual contour output:
arch clamp minus the `(1+n⁻¹)` prime comb, with the pole subtraction
already present in `standardExplicitFormula`. -/
theorem contourExplicitFormula_honest (F : FullWeilTest) :
    (2 * Real.pi) * standardExplicitFormula F =
      F.leftEdgeArchIntegral.re -
        (2 * Real.pi) *
          (∑ n ∈ Finset.range (F.fullAnchor + 1),
            ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
              F.toFun (Real.log n)) := by
  have h := congrArg Complex.re (contourExplicitFormula_honest_complex F)
  rw [← contourPrimePairing_eq_one_add_inv_sum F]
  simpa [standardExplicitFormula] using h

/-- Corrected r534 identification target: the spectral explicit formula
equals the honest contour assembly after multiplication by `2π`.
Unlike `StandardExplicitFormulaIdentification`, its prime channel is
`Λ(n)(1+n⁻¹)`, exactly as proved by the two vertical-edge inversions. -/
def HonestContourExplicitFormulaIdentification : Prop :=
  ∀ F : FullWeilTest,
    (2 * Real.pi) * standardExplicitFormula F =
      F.leftEdgeArchIntegral.re -
        (2 * Real.pi) *
          (∑ n ∈ Finset.range (F.fullAnchor + 1),
            ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
              F.toFun (Real.log n))

/-- r534: the corrected honest identification is a theorem of the
completed contour and Fourier-inversion machinery. -/
theorem honest_contour_explicit_formula_identification :
    HonestContourExplicitFormulaIdentification :=
  contourExplicitFormula_honest

/-- The arithmetic channel delivered by the completed contour: the finite
`Λ(n)(1+n⁻¹)` sum at the full-test support anchor. -/
noncomputable def fullWeilHonestPrimeSide (F : FullWeilTest) : ℝ :=
  ∑ n ∈ Finset.range (F.fullAnchor + 1),
    ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
      F.toFun (Real.log n)

/-- The contour arch clamp in the real normalization of the Weil form. -/
noncomputable def fullWeilHonestArchSide (F : FullWeilTest) : ℝ :=
  F.leftEdgeArchIntegral.re / (2 * Real.pi)

/-- There is no additional arithmetic-side pole channel in the honest
contour normalization: `-F.hat 1` is already present on the spectral side
of `standardExplicitFormula`. -/
noncomputable def fullWeilHonestPoleSide (_F : FullWeilTest) : ℝ := 0

/-- r538 honest full Weil form.  This is exactly the real normalization of
`contourExplicitFormula_honest`: contour arch clamp minus the
`Λ(n)(1+n⁻¹)` prime channel, with `-F.hat 1` already booked spectrally. -/
noncomputable def fullWeilFormHonest (F : FullWeilTest) : ℝ :=
  fullWeilHonestArchSide F - fullWeilHonestPrimeSide F +
    fullWeilHonestPoleSide F

/-- r538 bridge 2 for the honestly weighted form.  The contour theorem's
spectral side is literally `standardExplicitFormula`, so no spectral-limit
seam remains. -/
theorem standard_explicit_formula_identification_honest
    (F : FullWeilTest) (_hF : F.admissible) :
    fullWeilFormHonest F = standardExplicitFormula F := by
  have hcont := contourExplicitFormula_honest F
  unfold fullWeilFormHonest fullWeilHonestArchSide
    fullWeilHonestPrimeSide fullWeilHonestPoleSide
  have hπ : 2 * Real.pi ≠ 0 := mul_ne_zero (by norm_num) Real.pi_ne_zero
  calc
    F.leftEdgeArchIntegral.re / (2 * Real.pi) -
          (∑ n ∈ Finset.range (F.fullAnchor + 1),
            ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
              F.toFun (Real.log n)) + 0 =
        (F.leftEdgeArchIntegral.re - (2 * Real.pi) *
          (∑ n ∈ Finset.range (F.fullAnchor + 1),
            ArithmeticFunction.vonMangoldt n * (1 + (n : ℝ)⁻¹) *
              F.toFun (Real.log n))) / (2 * Real.pi) := by
      field_simp [hπ]
      ring
    _ = ((2 * Real.pi) * standardExplicitFormula F) /
          (2 * Real.pi) := by rw [hcont]
    _ = standardExplicitFormula F := by field_simp [hπ]


/-- Honest-form positivity is exactly standard explicit-formula positivity
on the admissible full test class. -/
theorem fullWeilFormHonest_nonneg_iff_standard_nonneg :
    (∀ F : FullWeilTest, F.admissible → 0 ≤ fullWeilFormHonest F) ↔
      (∀ F : FullWeilTest, F.admissible → 0 ≤ standardExplicitFormula F) := by
  constructor
  · intro h F hF
    rw [← standard_explicit_formula_identification_honest F hF]
    exact h F hF
  · intro h F hF
    rw [standard_explicit_formula_identification_honest F hF]
    exact h F hF

/-- The corpus comb, although indexed only by prime powers up to the
window's squared anchor, equals the support-truncated range sum. -/
lemma fullWeilCombSide_eq_range_sum (F : FullWeilTest) :
    fullWeilCombSide F =
      ∑ n ∈ Finset.range (F.fullAnchor + 1),
        (2 / Real.sqrt n) * ArithmeticFunction.vonMangoldt n *
          F.toFun (Real.log n) := by
  let term : ℕ → ℝ := fun n =>
    combMass n * F.toFun (Real.log n)
  have ha1 : 1 ≤ F.fullAnchor := le_max_left _ _
  have hatoms : ∀ n : ℕ, n ∉ windowAtoms F.fullAnchor → term n = 0 := by
    intro n hn
    by_cases hpp : IsPrimePow n
    · have hgt : F.fullAnchor ^ 2 < n := by
        by_contra hle
        exact hn (Finset.mem_filter.mpr
          ⟨Finset.mem_range.mpr (by omega), hpp⟩)
      have hanchor : F.fullAnchor < n := by nlinarith
      unfold term
      rw [F.toFun_log_eq_zero_of_lt_anchor hanchor, mul_zero]
    · have hΛ : ArithmeticFunction.vonMangoldt n = 0 := by
        by_contra hne
        exact hpp (ArithmeticFunction.vonMangoldt_ne_zero_iff.mp hne)
      simp [term, combMass, hΛ]
  have hrange : ∀ n : ℕ, n ∉ Finset.range (F.fullAnchor + 1) →
      term n = 0 := by
    intro n hn
    have hanchor : F.fullAnchor < n := by
      have : ¬n < F.fullAnchor + 1 := fun h => hn (Finset.mem_range.mpr h)
      omega
    unfold term
    rw [F.toFun_log_eq_zero_of_lt_anchor hanchor, mul_zero]
  calc
    fullWeilCombSide F =
        ∑ n ∈ windowAtoms F.fullAnchor, term n := by rfl
    _ = ∑' n : ℕ, term n := (tsum_eq_sum hatoms).symm
    _ = ∑ n ∈ Finset.range (F.fullAnchor + 1), term n :=
      tsum_eq_sum hrange
    _ = ∑ n ∈ Finset.range (F.fullAnchor + 1),
          (2 / Real.sqrt n) * ArithmeticFunction.vonMangoldt n *
            F.toFun (Real.log n) := by
      refine Finset.sum_congr rfl fun n _ => ?_
      unfold term
      rw [combMass_eq_gauge, mul_assoc]

/-- The positive perfect-square excess of the honest contour comb over
the corpus `2Λ/√n` comb, on the common support-truncated range. -/
noncomputable def surplusComb (F : FullWeilTest) : ℝ :=
  ∑ n ∈ Finset.range (F.fullAnchor + 1),
    ArithmeticFunction.vonMangoldt n *
      (1 - (Real.sqrt n)⁻¹) ^ 2 * F.toFun (Real.log n)

lemma one_add_inv_eq_two_div_sqrt_add_sq {n : ℕ} (hn : 0 < n) :
    1 + (n : ℝ)⁻¹ =
      2 / Real.sqrt n + (1 - (Real.sqrt n)⁻¹) ^ 2 := by
  have hnR : (0 : ℝ) < n := Nat.cast_pos.mpr hn
  have hsqrt : Real.sqrt n ≠ 0 := (Real.sqrt_pos.mpr hnR).ne'
  have hsqrt_sq : Real.sqrt n * Real.sqrt n = (n : ℝ) :=
    Real.mul_self_sqrt hnR.le
  field_simp [hsqrt, hnR.ne']
  nlinarith

/-- r538 arithmetic bridge: the honest prime channel is exactly the corpus
prime channel plus the perfect-square surplus. -/
theorem fullWeilFormHonest_eq_corpus_add_surplus (F : FullWeilTest) :
    fullWeilHonestPrimeSide F = fullWeilCombSide F + surplusComb F := by
  unfold fullWeilHonestPrimeSide surplusComb
  rw [fullWeilCombSide_eq_range_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun n _ => ?_
  by_cases hn : n = 0
  · subst n
    simp [combMass]
  · have hweight := one_add_inv_eq_two_div_sqrt_add_sq
      (Nat.pos_of_ne_zero hn)
    rw [hweight]
    ring

/-- Total non-prime gauge difference between the corpus continuation and
the contour normalization.  It includes the corpus pole integral because
the honest contour books `-F.hat 1` directly on the spectral side. -/
noncomputable def archGaugeDelta (F : FullWeilTest) : ℝ :=
  (fullWeilArchSide F + fullWeilPoleSide F) -
    (fullWeilHonestArchSide F + fullWeilHonestPoleSide F)

/-- Sign-correct old/new decomposition.  The corpus form is the honest
form plus the heavier-comb surplus plus the remaining arch/pole gauge. -/
theorem fullWeilForm_eq_honest_add_surplus_add_archGaugeDelta
    (F : FullWeilTest) :
    fullWeilForm F =
      fullWeilFormHonest F + surplusComb F + archGaugeDelta F := by
  unfold fullWeilForm fullWeilFormHonest archGaugeDelta
  rw [fullWeilFormHonest_eq_corpus_add_surplus F]
  ring


/-- Missing bridge 2: identify the continued custom three-channel form
with the standard Weil explicit formula.

r534 normalization obstruction: `fullWeilForm` subtracts the corpus
comb `2Λ(n)/√n`, whereas `contourExplicitFormula_honest` subtracts the
strictly heavier contour comb `Λ(n)(1+n⁻¹)` (away from `n = 1`, where
`Λ(1)=0`).  The proved contour therefore does not establish this Prop.
The r538 honest route defines `fullWeilFormHonest` with the contour
weights and proves
`standard_explicit_formula_identification_honest`.  The original corpus
form stays blocked; its exact discrepancy is exposed by `surplusComb`
and `archGaugeDelta`, not hidden in a dictionary lemma.

r638L retires the former asserting sorry
`standard_explicit_formula_identification` and keeps this Prop only as
an auditable rejected gauge contract. -/
def StandardExplicitFormulaIdentification : Prop :=
  ∀ F : FullWeilTest, F.admissible →
    fullWeilForm F = standardExplicitFormula F

/-- A nontrivial zero in exactly Mathlib's sense: zero of
`riemannZeta`, not a negative even integer, and not the pole at `1`. -/
def IsNontrivialRiemannZetaZero (s : ℂ) : Prop :=
  riemannZeta s = 0 ∧
    (¬∃ n : ℕ, s = -2 * (n + 1)) ∧
    s ≠ 1

/-- Guinand--Weil explicit formula landing site (design, r487).

Intended theorem: for every admissible `F`, the arithmetic
prime+arch+pole form equals the multiplicity-weighted spectral sum
over nontrivial zeros of `riemannZeta`.  Mathlib v4.29.1 has no
`ZetaZero` enumeration or multiplicity API, so the spectral sum and
its local finiteness must be developed before this Prop is proved.

References: A. Weil (1952), E. Bombieri, ``The Riemann Hypothesis'',
Clay Mathematics Institute (2000), explicit-formula/Weil-criterion
sections. -/
def GuinandWeilExplicitFormula : Prop :=
  ∀ F : FullWeilTest, F.admissible →
    fullWeilForm F = standardExplicitFormula F

/-- Exact criterion brick: every off-critical nontrivial zeta zero can
be separated by an admissible autocorrelation whose standard explicit
formula is negative.  This packages the classical Weil-criterion
construction without inventing a nonexistent Mathlib zero API. -/
def FullWeilSeparatesOffCriticalZeros : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s → s.re ≠ 1 / 2 →
    ∃ F : FullWeilTest, F.admissible ∧ standardExplicitFormula F < 0

/-- Missing bridge 3: the standard Weil criterion, stated against
mathlib's actual zeta interface `riemannZeta` and its formal
`RiemannHypothesis` predicate. -/
def StandardWeilCriterionToMathlibRH : Prop :=
  (∀ F : FullWeilTest, F.admissible →
      0 ≤ standardExplicitFormula F) →
    RiemannHypothesis

/-- The final Mathlib interface is pure logic once off-critical
separation is available. -/
theorem standard_weil_criterion_to_mathlib_rh_of_separation
    (hseparate : FullWeilSeparatesOffCriticalZeros) :
    StandardWeilCriterionToMathlibRH := by
  intro hpos s hz htrivial hpole
  by_contra hcritical
  obtain ⟨F, hF, hneg⟩ :=
    hseparate s ⟨hz, htrivial, hpole⟩ hcritical
  exact (not_lt_of_ge (hpos F hF)) hneg


/-- r538 honest criterion wiring.  This consumes the same off-critical
separation hypothesis as the standard criterion; honest positivity adds no
new route around that classical brick. -/
theorem honest_weil_criterion_to_mathlib_rh
    (hseparate : FullWeilSeparatesOffCriticalZeros)
    (hpos : ∀ F : FullWeilTest, F.admissible → 0 ≤ fullWeilFormHonest F) :
    RiemannHypothesis := by
  apply standard_weil_criterion_to_mathlib_rh_of_separation hseparate
  exact fullWeilFormHonest_nonneg_iff_standard_nonneg.mp hpos

/-- OPEN CLASSICAL BRICK 3 (r487): Weil's off-critical separation
construction.  The logical conversion to Mathlib `RiemannHypothesis`
is proved above. -/
theorem fullWeil_separates_offCritical_zeros :
    FullWeilSeparatesOffCriticalZeros := by
  sorry

/-- Bridge 3 is now a proved wrapper around the single named
separation theorem. -/
theorem standard_weil_criterion_to_mathlib_rh :
    StandardWeilCriterionToMathlibRH :=
  standard_weil_criterion_to_mathlib_rh_of_separation
    fullWeil_separates_offCritical_zeros

end RH
