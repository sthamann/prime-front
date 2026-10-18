/-
RH/GaborFEMultiplicity.lean -- r582 FE-invariant analytic order.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

The |Im| >= 2 identity `riemannZetaMultiplicity_eq_one_sub` used
the chi-factor `zetaFEFactor`, which was only known to be holomorphic
and non-vanishing on that sliver.  Mathlib's completed zeta
`Lambda(s) = Lambda(1-s)` (`completedRiemannZeta_one_sub`) is an
identity of meromorphic functions, and on the open critical strip
`Lambda` and `zeta` share zeros and orders: `zeta = Lambda / GammaR`
with `GammaR != 0` holomorphic (`GammaR_eq_zero_iff` forces
`s = -2n`, impossible for `Re s > 0`).  Poles of `Lambda` at `0`
and `1` are excluded because strip zeros of `zeta` are neither
(`IsCriticalStripZetaZero`).

Analytic order is invariant under precomposition with `s |-> 1-s`
(`deriv = -1 != 0`).  Combined with `Lambda o (1-.) = Lambda` this
gives `m(z) = m(1-z)` on the whole strip, including compact bins
`k in {-2,-1,0,1}`.
-/
import RH.GaborZeroSummable
import RH.ExternalBridges
import Mathlib.Analysis.SpecialFunctions.Gamma.Deligne
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.Complex.CauchyIntegral

namespace RH

set_option maxHeartbeats 800000

open scoped Classical ComplexConjugate
open Complex Filter
open scoped Topology

/-! ## GammaR on Re > 0 -/


lemma Gammaℝ_ne_zero_of_re_pos {s : ℂ} (hs : 0 < s.re) : Gammaℝ s ≠ 0 := by
  intro h
  obtain ⟨n, hn⟩ := Gammaℝ_eq_zero_iff.mp h
  have hre : s.re = -((2 : ℝ) * n) := by
    rw [hn]
    simp
  have hn0 : (0 : ℝ) ≤ (2 : ℝ) * n :=
    mul_nonneg (by norm_num) (Nat.cast_nonneg _)
  linarith

lemma analyticAt_inv_Gammaℝ (s : ℂ) :
    AnalyticAt ℂ (fun w : ℂ => (Gammaℝ w)⁻¹) s :=
  (differentiable_Gammaℝ_inv.differentiableOn.analyticOnNhd isOpen_univ)
    s (Set.mem_univ _)

lemma analyticAt_Gammaℝ_of_re_pos {s : ℂ} (hs : 0 < s.re) :
    AnalyticAt ℂ Gammaℝ s := by
  have hΓ0 : Gammaℝ s ≠ 0 := Gammaℝ_ne_zero_of_re_pos hs
  have hinv : AnalyticAt ℂ (fun w : ℂ => (Gammaℝ w)⁻¹) s :=
    analyticAt_inv_Gammaℝ s
  have hinv0 : (Gammaℝ s)⁻¹ ≠ 0 := inv_ne_zero hΓ0
  have hfun : Gammaℝ = fun w : ℂ => ((Gammaℝ w)⁻¹)⁻¹ := by
    funext w
    exact (inv_inv (Gammaℝ w)).symm
  rw [hfun]
  exact hinv.inv hinv0

/-! ## zeta = Lambda / GammaR on the open strip -/

lemma eventuallyEq_riemannZeta_completed_div {s : ℂ} (hs : s ≠ 0) :
    riemannZeta =ᶠ[𝓝 s]
      fun w => completedRiemannZeta w / Gammaℝ w := by
  filter_upwards [eventually_ne_nhds hs] with w hw
  exact riemannZeta_def_of_ne_zero hw

lemma differentiableOn_completedZeta_compl_poles :
    DifferentiableOn ℂ completedRiemannZeta ({0, 1}ᶜ : Set ℂ) := by
  intro s hs
  have hs0 : s ≠ 0 := fun h => hs (Or.inl h)
  have hs1 : s ≠ 1 := fun h => hs (Or.inr h)
  exact (differentiableAt_completedZeta hs0 hs1).differentiableWithinAt

lemma isOpen_compl_zero_one : IsOpen ({0, 1}ᶜ : Set ℂ) :=
  (isClosed_singleton.union isClosed_singleton).isOpen_compl

lemma analyticAt_completedRiemannZeta_of_ne_poles {s : ℂ}
    (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    AnalyticAt ℂ completedRiemannZeta s :=
  (differentiableOn_completedZeta_compl_poles.analyticOnNhd isOpen_compl_zero_one)
    s (by
      intro h
      rcases h with h0 | h1
      · exact hs0 h0
      · exact hs1 (by simpa using h1))

lemma analyticOrderAt_riemannZeta_eq_completed {s : ℂ}
    (h0 : 0 < s.re) (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    analyticOrderAt riemannZeta s =
      analyticOrderAt completedRiemannZeta s := by
  have hΛ : AnalyticAt ℂ completedRiemannZeta s :=
    analyticAt_completedRiemannZeta_of_ne_poles hs0 hs1
  have hΓ : AnalyticAt ℂ Gammaℝ s := analyticAt_Gammaℝ_of_re_pos h0
  have hΓ0 : Gammaℝ s ≠ 0 := Gammaℝ_ne_zero_of_re_pos h0
  have hinv : AnalyticAt ℂ (fun w : ℂ => (Gammaℝ w)⁻¹) s := hΓ.inv hΓ0
  have hinv0 : analyticOrderAt (fun w : ℂ => (Gammaℝ w)⁻¹) s = 0 :=
    hinv.analyticOrderAt_eq_zero.mpr (inv_ne_zero hΓ0)
  have hmul : analyticOrderAt
      (fun w => completedRiemannZeta w * (Gammaℝ w)⁻¹) s =
        analyticOrderAt completedRiemannZeta s +
          analyticOrderAt (fun w : ℂ => (Gammaℝ w)⁻¹) s :=
    analyticOrderAt_mul hΛ hinv
  have hfun :
      (fun w : ℂ => completedRiemannZeta w / Gammaℝ w) =
        fun w => completedRiemannZeta w * (Gammaℝ w)⁻¹ := by
    funext w
    exact div_eq_mul_inv _ _
  have hdivord : analyticOrderAt
      (fun w => completedRiemannZeta w / Gammaℝ w) s =
        analyticOrderAt completedRiemannZeta s := by
    rw [analyticOrderAt_congr (EventuallyEq.of_eq hfun), hmul, hinv0, add_zero]
  exact (analyticOrderAt_congr (eventuallyEq_riemannZeta_completed_div hs0)).trans
    hdivord

/-! ## Lambda o (1-.) = Lambda preserves order -/

lemma completedRiemannZeta_comp_one_sub :
    (fun w : ℂ => completedRiemannZeta (1 - w)) = completedRiemannZeta := by
  funext w
  exact completedRiemannZeta_one_sub w

lemma analyticOrderAt_completed_one_sub {s : ℂ}
    (_hs0 : s ≠ 0) (_hs1 : s ≠ 1)
    (_h1s0 : 1 - s ≠ 0) (_h1s1 : 1 - s ≠ 1) :
    analyticOrderAt completedRiemannZeta s =
      analyticOrderAt completedRiemannZeta (1 - s) := by
  have hg : AnalyticAt ℂ (fun w : ℂ => 1 - w) s := by fun_prop
  have hder : HasDerivAt (fun w : ℂ => 1 - w) (-1) s := by
    simpa using (hasDerivAt_const s (1 : ℂ)).sub (hasDerivAt_id s)
  have hder0 : deriv (fun w : ℂ => 1 - w) s ≠ 0 := by
    simp [hder.deriv]
  have hcomp : analyticOrderAt (completedRiemannZeta ∘ fun w : ℂ => 1 - w) s =
      analyticOrderAt completedRiemannZeta (1 - s) :=
    analyticOrderAt_comp_of_deriv_ne_zero hg hder0
  have hfun :
      (completedRiemannZeta ∘ fun w : ℂ => 1 - w) =
        fun w : ℂ => completedRiemannZeta (1 - w) := rfl
  have hfe : analyticOrderAt (fun w : ℂ => completedRiemannZeta (1 - w)) s =
      analyticOrderAt completedRiemannZeta s := by
    rw [analyticOrderAt_congr
      (EventuallyEq.of_eq completedRiemannZeta_comp_one_sub)]
  exact hfe.symm.trans (hfun ▸ hcomp)

/-- FE-invariant multiplicity on the whole open strip, including
compact bins.  Poles of Lambda at 0 and 1 are excluded by
`IsCriticalStripZetaZero`. -/
lemma riemannZetaMultiplicity_eq_one_sub_all {z : ℂ}
    (hz : IsCriticalStripZetaZero z) :
    riemannZetaMultiplicity z = riemannZetaMultiplicity (1 - z) := by
  have hz0 : z ≠ 0 := isCriticalStripZetaZero_ne_zero hz
  have hz1 : z ≠ 1 := isCriticalStripZetaZero_ne_one hz
  have h1z : IsCriticalStripZetaZero (1 - z) := isCriticalStrip_one_sub hz
  have h1z0 : 1 - z ≠ 0 := isCriticalStripZetaZero_ne_zero h1z
  have h1z1 : 1 - z ≠ 1 := isCriticalStripZetaZero_ne_one h1z
  have hordζ : analyticOrderAt riemannZeta z =
      analyticOrderAt completedRiemannZeta z :=
    analyticOrderAt_riemannZeta_eq_completed hz.2.1 hz0 hz1
  have hordζ1 : analyticOrderAt riemannZeta (1 - z) =
      analyticOrderAt completedRiemannZeta (1 - z) :=
    analyticOrderAt_riemannZeta_eq_completed h1z.2.1 h1z0 h1z1
  have hΛ : analyticOrderAt completedRiemannZeta z =
      analyticOrderAt completedRiemannZeta (1 - z) :=
    analyticOrderAt_completed_one_sub hz0 hz1 h1z0 h1z1
  unfold riemannZetaMultiplicity analyticOrderNatAt
  simp [hordζ, hordζ1, hΛ]

/-! ## Conjugation-invariant analytic order (r585) -/

lemma analyticOrderAt_id_sub (s : ℂ) :
    analyticOrderAt (fun w : ℂ => w - s) s = 1 := by
  have hf : AnalyticAt ℂ (fun w : ℂ => w - s) s := by fun_prop
  have hz : (s - s : ℂ) = 0 := sub_self _
  have hder : HasDerivAt (fun w : ℂ => w - s) 1 s := by
    change HasDerivAt (id - fun _ : ℂ => s) 1 s
    simpa using (hasDerivAt_id s).sub (hasDerivAt_const s s)
  have hd : deriv (fun w : ℂ => w - s) s ≠ 0 := by
    simp [hder.deriv]
  exact hf.analyticOrderAt_eq_one_of_zero_deriv_ne_zero hz hd

lemma analyticOrderAt_pow_id_sub (s : ℂ) (n : ℕ) :
    analyticOrderAt (fun w : ℂ => (w - s) ^ n) s = n := by
  induction n with
  | zero =>
    have hconst : AnalyticAt ℂ (fun _ : ℂ => (1 : ℂ)) s := analyticAt_const
    have h0 : analyticOrderAt (fun _ : ℂ => (1 : ℂ)) s = 0 :=
      hconst.analyticOrderAt_eq_zero.mpr one_ne_zero
    simpa using h0
  | succ n ih =>
    have hf : AnalyticAt ℂ (fun w : ℂ => w - s) s := by fun_prop
    have hp : AnalyticAt ℂ (fun w : ℂ => (w - s) ^ n) s := by fun_prop
    have hfun :
        (fun w : ℂ => (w - s) ^ (n + 1)) =
          (fun w : ℂ => w - s) * fun w => (w - s) ^ n := by
      funext w
      simp [Pi.mul_apply, pow_succ, mul_comm]
    have hmul := analyticOrderAt_mul hf hp
    rw [analyticOrderAt_congr (EventuallyEq.of_eq hfun), hmul,
      analyticOrderAt_id_sub, ih]
    simp [Nat.cast_succ, add_comm]

/-- Schwarz reflection transports finite analytic order: conjugation is
antiholomorphic, but `conj ∘ f ∘ conj` is holomorphic and has the same
order at `s` as `f` has at `conj s`. -/
lemma analyticOrderAt_conj_conj {f : ℂ → ℂ} {s : ℂ}
    (hf : AnalyticAt ℂ f (conj s))
    (hfin : analyticOrderAt f (conj s) ≠ ⊤) :
    analyticOrderAt (conj ∘ f ∘ conj) s =
      analyticOrderAt f (conj s) := by
  obtain ⟨g, hg_an, hg_ne, hg_eq⟩ := hf.analyticOrderAt_ne_top.mp hfin
  set m := analyticOrderNatAt f (conj s)
  have htend : Tendsto conj (𝓝 s) (𝓝 (conj s)) :=
    continuous_conj.continuousAt
  have hnear :
      ∀ᶠ w in 𝓝 s, f (conj w) = (conj w - conj s) ^ m • g (conj w) :=
    htend.eventually hg_eq
  have hcc : (conj ∘ f ∘ conj) =ᶠ[𝓝 s]
      fun w => (w - s) ^ m * (conj ∘ g ∘ conj) w := by
    filter_upwards [hnear] with w hw
    simp only [Function.comp_apply]
    rw [hw, smul_eq_mul, map_mul]
    have hpow : conj ((conj w - conj s) ^ m) = (w - s) ^ m := by
      rw [← map_sub conj w s, ← map_pow, conj_conj]
    rw [hpow]
  obtain ⟨r, hr, hball⟩ := hg_an.exists_ball_analyticOnNhd
  have hdiff : DifferentiableOn ℂ (conj ∘ g ∘ conj) (Metric.ball s r) := by
    intro w hw
    have hw' : conj w ∈ Metric.ball (conj s) r := by
      have hnorm : ‖conj w - conj s‖ = ‖w - s‖ := by
        rw [← map_sub (starRingEnd ℂ), norm_conj]
      simpa [Metric.mem_ball, dist_eq_norm, hnorm] using hw
    have hgan : AnalyticAt ℂ g (conj w) := hball (conj w) hw'
    have hgc : DifferentiableAt ℂ (conj ∘ g ∘ conj) w := by
      simpa [star_star] using hgan.differentiableAt.conj_conj
    exact hgc.differentiableWithinAt
  have hanOn : AnalyticOnNhd ℂ (conj ∘ g ∘ conj) (Metric.ball s r) :=
    hdiff.analyticOnNhd Metric.isOpen_ball
  have hAt : AnalyticAt ℂ (conj ∘ g ∘ conj) s :=
    hanOn s (Metric.mem_ball_self hr)
  have hne : (conj ∘ g ∘ conj) s ≠ 0 := by
    simp [Function.comp_apply, map_eq_zero, hg_ne]
  have han_pow : AnalyticAt ℂ (fun w : ℂ => (w - s) ^ m) s := by fun_prop
  have hmul :
      analyticOrderAt
          (fun w => (w - s) ^ m * (conj ∘ g ∘ conj) w) s =
        analyticOrderAt (fun w : ℂ => (w - s) ^ m) s +
          analyticOrderAt (conj ∘ g ∘ conj) s := by
    simpa [Pi.mul_apply] using analyticOrderAt_mul han_pow hAt
  have hunit : analyticOrderAt (conj ∘ g ∘ conj) s = 0 :=
    hAt.analyticOrderAt_eq_zero.mpr hne
  have hpoword := analyticOrderAt_pow_id_sub s m
  have hord :
      analyticOrderAt (conj ∘ f ∘ conj) s = m := by
    rw [analyticOrderAt_congr hcc, hmul, hpoword, hunit, add_zero]
  have hm : analyticOrderAt f (conj s) = m := by
    unfold m analyticOrderNatAt
    exact (ENat.coe_toNat hfin).symm
  exact hord.trans hm.symm

lemma eventuallyEq_riemannZeta_conj_conj {s : ℂ} (hs : s ≠ 1) :
    (conj ∘ riemannZeta ∘ conj) =ᶠ[𝓝 s] riemannZeta :=
  eventuallyEq_iff_exists_mem.2
    ⟨({1}ᶜ : Set ℂ), isOpen_compl_singleton.mem_nhds hs,
      eqOn_riemannZeta_conj_conj⟩

/-- Analytic order of `ζ` is conjugation-invariant off the pole.
Schwarz reflection `conj ∘ ζ ∘ conj = ζ` plus order transport. -/
lemma riemannZetaMultiplicity_eq_conj {z : ℂ} (hz : z ≠ 1) :
    riemannZetaMultiplicity (conj z) = riemannZetaMultiplicity z := by
  have hz' : conj z ≠ 1 := conj_ne_one hz
  have hζ : AnalyticAt ℂ riemannZeta (conj z) :=
    analyticAt_riemannZeta hz'
  have hfin : analyticOrderAt riemannZeta (conj z) ≠ ⊤ :=
    analyticOrderAt_riemannZeta_ne_top hz'
  have hcc : analyticOrderAt (conj ∘ riemannZeta ∘ conj) z =
      analyticOrderAt riemannZeta (conj z) :=
    analyticOrderAt_conj_conj hζ hfin
  have hid : analyticOrderAt (conj ∘ riemannZeta ∘ conj) z =
      analyticOrderAt riemannZeta z :=
    analyticOrderAt_congr (eventuallyEq_riemannZeta_conj_conj hz)
  unfold riemannZetaMultiplicity analyticOrderNatAt
  simp [← hcc, hid]

lemma riemannZetaMultiplicity_eq_star {z : ℂ} (hz : z ≠ 1) :
    riemannZetaMultiplicity (star z) = riemannZetaMultiplicity z := by
  simpa [Complex.star_def] using riemannZetaMultiplicity_eq_conj hz

/-! ## Multiplicity-weighted unit window -/

lemma sum_multiplicity_one_sub {S : Finset ℂ}
    (hS : ∀ z ∈ S, IsCriticalStripZetaZero z) :
    S.sum (fun z => (riemannZetaMultiplicity z : ℝ)) =
      (S.image (fun z : ℂ => 1 - z)).sum
        (fun w => (riemannZetaMultiplicity w : ℝ)) := by
  have hinj : Set.InjOn (fun z : ℂ => 1 - z) S :=
    fun _ _ _ _ h => sub_right_inj.mp h
  rw [Finset.sum_image hinj]
  refine Finset.sum_congr rfl fun z hz => ?_
  exact_mod_cast riemannZetaMultiplicity_eq_one_sub_all (hS z hz)

lemma strip_re_ge_half_subset_disk (N : ℝ) :
    ((stripZerosWindow N).filter fun z => (1 / 2 : ℝ) ≤ z.re) ⊆
      landauInnerDisk (N + 1 / 2) := by
  intro z hz
  have hzf := Finset.mem_filter.mp hz
  have hzW := mem_stripZerosWindow.mp hzf.1
  have hzR := mem_riemannZetaZerosOnClosedRect.mp hzW.1
  have hrect := mem_zetaClosedRect.mp hzR.1
  refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hzR.2.1, hzR.2.2⟩
  simpa [landauInnerDisk] using
    mem_unit_height_inner_disk hzf.2 hrect.2.1 hzW.2

lemma strip_re_lt_half_image_subset_disk (N : ℝ) :
    ((stripZerosWindow N).filter
        (fun z => z.re < (1 / 2 : ℝ))).image (fun z : ℂ => 1 - z) ⊆
      landauInnerDisk (-(N + 1) + 1 / 2) := by
  intro w hw
  obtain ⟨z, hzlt, rfl⟩ := Finset.mem_image.mp hw
  have hzf := Finset.mem_filter.mp hzlt
  have hzW := mem_stripZerosWindow.mp hzf.1
  have hzR := mem_riemannZetaZerosOnClosedRect.mp hzW.1
  have hrect := mem_zetaClosedRect.mp hzR.1
  have hre0 : 0 < z.re :=
    lt_of_le_of_ne hrect.1 fun h0 =>
      riemannZeta_ne_zero_of_re_eq_zero h0.symm hzR.2.1
  have hre1 : z.re < 1 := lt_of_lt_of_le hzf.2 (by norm_num)
  have hwz := one_sub_mem_closedRect hzW.1 hre0 hre1
  have hwR := mem_riemannZetaZerosOnClosedRect.mp hwz
  have hre_ge : (1 / 2 : ℝ) ≤ (1 - z).re := by
    simp only [sub_re, one_re]; linarith [hzf.2]
  have hre_le : (1 - z).re ≤ 1 := by
    simp only [sub_re, one_re]; linarith [hrect.1]
  have him : -(N + 1 : ℝ) ≤ (1 - z).im ∧
      (1 - z).im ≤ (-(N + 1 : ℝ) + 1) := by
    have himz : (1 - z).im = -z.im := by simp [sub_im]
    rw [himz]
    constructor <;> linarith [hzW.2.1, hzW.2.2]
  refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hwR.2.1, hwR.2.2⟩
  exact mem_unit_height_inner_disk (N := -(N + 1 : ℝ)) hre_ge hre_le him

lemma stripZerosWindow_critical {N : ℝ} {z : ℂ}
    (hz : z ∈ stripZerosWindow N) : IsCriticalStripZetaZero z :=
  isCriticalStrip_of_mem_rect (mem_stripZerosWindow.mp hz).1

lemma sum_multiplicity_strip_re_ge_half_le (N : ℝ) :
    ((stripZerosWindow N).filter
        (fun z => (1 / 2 : ℝ) ≤ z.re)).sum
        (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
      zetaZerosInDiskCardBoundInner * (1 + Real.log (2 + |N + 1 / 2|)) := by
  set Sge := (stripZerosWindow N).filter fun z => (1 / 2 : ℝ) ≤ z.re
  have hsub : Sge ⊆ landauInnerDisk (N + 1 / 2) :=
    strip_re_ge_half_subset_disk N
  have hsum :
      Sge.sum (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        (landauInnerDisk (N + 1 / 2)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub
      (fun _ _ _ => Nat.cast_nonneg _)
  exact hsum.trans (sum_multiplicity_landauInnerDisk_le (N + 1 / 2))

lemma sum_multiplicity_strip_re_lt_half_le (N : ℝ) :
    ((stripZerosWindow N).filter
        (fun z => z.re < (1 / 2 : ℝ))).sum
        (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
      zetaZerosInDiskCardBoundInner *
        (1 + Real.log (2 + |-(N + 1) + 1 / 2|)) := by
  set Slt := (stripZerosWindow N).filter fun z => z.re < (1 / 2 : ℝ)
  have hcrit : ∀ z ∈ Slt, IsCriticalStripZetaZero z :=
    fun z hz => stripZerosWindow_critical (Finset.mem_filter.mp hz).1
  have himg := strip_re_lt_half_image_subset_disk N
  have hsum :=
    (sum_multiplicity_one_sub (S := Slt) hcrit).trans_le
      (Finset.sum_le_sum_of_subset_of_nonneg (f := fun w =>
          (riemannZetaMultiplicity w : ℝ)) himg
        (fun _ _ _ => Nat.cast_nonneg _))
  exact hsum.trans
    (sum_multiplicity_landauInnerDisk_le (-(N + 1) + 1 / 2))

lemma log_disk_center_le (N : ℝ) :
    1 + Real.log (2 + |N + 1 / 2|) ≤ 1 + Real.log (|N| + 3) := by
  have habs : |N + 1 / 2| ≤ |N| + 1 := by
    have := abs_add_le N (1 / 2 : ℝ)
    have : |(1 / 2 : ℝ)| = (1 / 2 : ℝ) := abs_of_pos (by norm_num)
    linarith
  have hx : 0 < 2 + |N + 1 / 2| := by positivity
  have hle : 2 + |N + 1 / 2| ≤ |N| + 3 := by linarith
  exact add_le_add_right (Real.log_le_log hx hle) 1

lemma log_disk_center_neg_le (N : ℝ) :
    1 + Real.log (2 + |-(N + 1) + 1 / 2|) ≤ 1 + Real.log (|N| + 3) := by
  have hτ : |-(N + 1) + 1 / 2| = |N + 1 / 2| := by
    have : -(N + 1) + (1 / 2 : ℝ) = -(N + 1 / 2) := by ring
    rw [this, abs_neg]
  rw [hτ]
  exact log_disk_center_le N

/-- Jensen-with-multiplicity + FE folding: unit-window occupancy is
at most the Path-A increment `2 C_inner (1+log(|N|+3))`. -/
theorem sum_multiplicity_stripZerosWindow_le (N : ℝ) :
    (stripZerosWindow N).sum
        (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (|N| + 3)) := by
  set S := stripZerosWindow N
  set Sge := S.filter fun z => (1 / 2 : ℝ) ≤ z.re
  set Slt := S.filter fun z => z.re < (1 / 2 : ℝ)
  have hunion : Sge ∪ Slt = S := by
    ext z
    constructor
    · intro hz
      rcases Finset.mem_union.mp hz with h | h
      · exact (Finset.mem_filter.mp h).1
      · exact (Finset.mem_filter.mp h).1
    · intro hz
      by_cases hre : (1 / 2 : ℝ) ≤ z.re
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_filter.mpr ⟨hz, hre⟩))
      · exact Finset.mem_union.mpr
          (Or.inr (Finset.mem_filter.mpr ⟨hz, lt_of_not_ge hre⟩))
  have hdisj : Disjoint Sge Slt := by
    refine Finset.disjoint_left.mpr ?_
    intro z hzge hzlt
    exact (not_lt_of_ge (Finset.mem_filter.mp hzge).2)
      (Finset.mem_filter.mp hzlt).2
  have hpart :
      S.sum (fun z => (riemannZetaMultiplicity z : ℝ)) =
        Sge.sum (fun z => (riemannZetaMultiplicity z : ℝ)) +
          Slt.sum (fun z => (riemannZetaMultiplicity z : ℝ)) := by
    rw [← hunion, Finset.sum_union hdisj]
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  have hp := (sum_multiplicity_strip_re_ge_half_le N).trans
    (mul_le_mul_of_nonneg_left (log_disk_center_le N) hC0)
  have hm := (sum_multiplicity_strip_re_lt_half_le N).trans
    (mul_le_mul_of_nonneg_left (log_disk_center_neg_le N) hC0)
  rw [hpart]
  linarith [hp, hm]

#print axioms riemannZetaMultiplicity_eq_one_sub_all
#print axioms riemannZetaMultiplicity_eq_conj
#print axioms riemannZetaMultiplicity_eq_star
#print axioms sum_multiplicity_stripZerosWindow_le

end RH
