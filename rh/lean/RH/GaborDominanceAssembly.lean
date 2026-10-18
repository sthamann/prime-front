/-
RH/GaborDominanceAssembly.lean -- r571 packing + remainder budget.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r569 left `GaborDominanceAssembly` unasserted.  This module
assembles the existing sorry-free bricks:

  * host minus-lobe `m★ · (−η · E)` (`gaborHostMerge_minusLobe`);
  * plus / cross bin packing into `T_plus_loose`
    (`gaborPlusLobe_majorant`, `gauss_binMax_tsum_le`);
  * foreign minus-lobe packing into `T_far` after isolation
    empties the peak window (`gaborTGap_eq_zero` style);
  * elementary remainder budget under the r569 width cap.

No statement is weakened.  `GaborDominanceBound` is a theorem
via `gabor_dominanceBound_of_assembly`.
-/
import RH.GaborDominanceProof
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace RH

set_option maxHeartbeats 800000

open scoped Classical
open Set Finset

/-! ## Elementary constants and theta tails -/

lemma gaborKBin_ge_one : (1 : ℝ) ≤ (gaborKBin : ℝ) := by
  unfold gaborKBin
  norm_num

lemma gaborSmallnessA_le_inv_four_bin (sigma gamma : ℝ) (hg : 0 ≤ gamma) :
    gaborSmallnessA sigma gamma ≤ 1 / (4 * (gaborKBin : ℝ)) := by
  refine (gaborSmallnessA_le_binSq sigma gamma hg).trans ?_
  have hK : (1 : ℝ) ≤ (gaborKBin : ℝ) := gaborKBin_ge_one
  have hpos : (0 : ℝ) < 4 * (gaborKBin : ℝ) :=
    mul_pos (by norm_num) gaborKBin_pos
  have hpos' : (0 : ℝ) < 8 * (gaborKBin : ℝ) ^ 2 :=
    mul_pos (by norm_num) (sq_pos_of_pos gaborKBin_pos)
  rw [div_le_div_iff₀ hpos' hpos]
  nlinarith [sq_nonneg ((gaborKBin : ℝ) - 1), hK]

lemma thetaLobe_ge_three {a : ℝ} (_ha : 0 < a) : (3 : ℝ) ≤ thetaLobe a := by
  unfold thetaLobe
  have h : 0 ≤ ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) :=
    tsum_nonneg fun _ => (Real.exp_pos _).le
  linarith

lemma thetaLobe_sub_three_eq {a : ℝ} :
    thetaLobe a - 3 =
      2 * ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  unfold thetaLobe
  ring

lemma theta_lobe_tail_le_geom {a : ℝ} (ha : 0 < a) :
    ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) ≤
      Real.exp (-(1 : ℝ) / (2 * a)) /
        (1 - Real.exp (-(1 : ℝ) / (2 * a))) := by
  have hξ0 : 0 ≤ Real.exp (-(1 : ℝ) / (2 * a)) := (Real.exp_pos _).le
  have hξ1 : Real.exp (-(1 : ℝ) / (2 * a)) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (by norm_num) (mul_pos (by norm_num) ha)
  have hterm : ∀ m : ℕ,
      Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) ≤
        Real.exp (-(1 : ℝ) / (2 * a)) *
          (Real.exp (-(1 : ℝ) / (2 * a))) ^ m := by
    intro m
    refine (gauss_theta_term_le_geom ha m).trans_eq ?_
    have hm : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by exact_mod_cast rfl
    have : -((m + 1 : ℕ) : ℝ) / (2 * a) =
        (m : ℝ) * (-(1 : ℝ) / (2 * a)) + (-(1 : ℝ) / (2 * a)) := by
      rw [hm]
      field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]
      ring
    rw [this, Real.exp_add, Real.exp_nat_mul]
    ring
  have hgeom : Summable fun m : ℕ =>
      (Real.exp (-(1 : ℝ) / (2 * a))) ^ m :=
    summable_geometric_of_lt_one hξ0 hξ1
  have hsm := hgeom.mul_left (Real.exp (-(1 : ℝ) / (2 * a)))
  have hle :=
    Summable.tsum_le_tsum hterm (theta_lobe_summable ha) hsm
  refine hle.trans_eq ?_
  rw [tsum_mul_left, tsum_geometric_of_lt_one hξ0 hξ1]
  exact (div_eq_mul_inv _ _).symm

lemma thetaLobe_sub_three_le_geom {a : ℝ} (ha : 0 < a) :
    thetaLobe a - 3 ≤
      2 * Real.exp (-(1 : ℝ) / (2 * a)) /
        (1 - Real.exp (-(1 : ℝ) / (2 * a))) := by
  rw [thetaLobe_sub_three_eq]
  have := theta_lobe_tail_le_geom ha
  have h2 : (0 : ℝ) ≤ 2 := by norm_num
  have := mul_le_mul_of_nonneg_left this h2
  convert this using 1
  field_simp

lemma exp_neg_nat_le_inv_two_pow (n : ℕ) :
    Real.exp (-(n : ℝ)) ≤ 1 / (2 : ℝ) ^ n := by
  have h2 : (2 : ℝ) ≤ Real.exp 1 := by
    linarith [Real.add_one_le_exp (1 : ℝ)]
  have hpow : (2 : ℝ) ^ n ≤ (Real.exp 1) ^ n :=
    pow_le_pow_left₀ (by norm_num) h2 n
  have hexp : (Real.exp 1) ^ n = Real.exp (n : ℝ) := by
    rw [← Real.exp_nat_mul]
    simp
  rw [Real.exp_neg, one_div]
  exact (inv_le_inv₀ (Real.exp_pos _) (pow_pos (by norm_num) n)).mpr
    (hpow.trans_eq hexp)

lemma exp_neg_sixty_four_le : Real.exp (-(64 : ℝ)) ≤ 1 / (2 : ℝ) ^ 64 := by
  simpa using exp_neg_nat_le_inv_two_pow 64

/-! ## Isolation-shrink numeric facts -/

lemma isolationShrinkOfConfig_le_lock (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborALock (gaborHostSigma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_lock _ _)

lemma isolationShrinkOfConfig_le_omegaCap (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborOmegaCap (gaborHostSigma Z hZ) (gaborHostGamma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_omegaCap _ _)

lemma isolationShrinkOfConfig_le_gamma_sq (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborHostGamma Z hZ ^ 2 / 512 :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_gamma_sq _ _)

lemma isolationShrinkOfConfig_le_binSq (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      1 / (8 * (gaborKBin : ℝ) ^ 2) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_binSq _ _ (gaborHostGamma_pos Z hZ).le)

lemma isolationShrinkOfConfig_le_binSqLog (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      1 / (8 * gaborKBinAt (gaborHostGamma Z hZ) ^ 2) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_binSqLog _ _)

lemma isolationShrinkOfConfig_le_online (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborOnlineSmallnessA (gaborHostSigma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_online _ _)

lemma isolationShrinkOfConfig_le_onlineLog (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborOnlineSmallnessALog (gaborHostSigma Z hZ) (gaborHostGamma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_onlineLog _ _)

lemma isolationShrinkOfConfig_le_plus (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborPlusSmallnessA (gaborHostGamma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_plus _ _)

lemma isolationShrinkOfConfig_le_far (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborFarSmallnessA (gaborHostGamma Z hZ) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_far _ _)

lemma isolationShrinkOfConfig_le_inv_four_bin (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      1 / (4 * (gaborKBin : ℝ)) :=
  (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
    (gaborSmallnessA_le_inv_four_bin _ _ (gaborHostGamma_pos Z hZ).le)

lemma isolationShrinkOfConfig_omega_half (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    gaborHostGamma Z hZ / 2 ≤ (isolationShrinkOfConfig Z hZ).2 := by
  rw [isolationShrinkOfConfig_omega_eq]
  exact gaborIsolationOmega_pos_of_cap (gaborHostSigma_pos Z hZ)
    (gaborHostGamma_pos Z hZ) (isolationShrinkOfConfig_a_pos Z hZ).le
    (isolationShrinkOfConfig_le_omegaCap Z hZ)

/-! ## Weighted bin packing -/

lemma ordinateBin_nonneg_of_pos {t : ℝ} (ht : 0 < t) :
    (0 : ℤ) ≤ ordinateBin t := by
  have h := mem_ordinateBin t
  have hnot : ¬ ordinateBin t ≤ -1 := by
    intro hk
    have hle : (ordinateBin t : ℝ) + 1 ≤ 0 := by
      have : ordinateBin t + 1 ≤ 0 := by omega
      exact_mod_cast this
    linarith [h.2, ht]
  omega

lemma sum_fiber_weight (S : Finset (ℝ × ℝ)) (mult : ℝ × ℝ → ℕ)
    (g : ℝ × ℝ → ℤ) (M : ℤ → ℝ) :
    S.sum (fun q => (mult q : ℝ) * M (g q)) =
      ∑ k ∈ S.image g,
        (S.filter (fun q => g q = k)).sum (fun q => (mult q : ℝ)) * M k := by
  have hmaps : ∀ q ∈ S, g q ∈ S.image g :=
    fun q hq => mem_image_of_mem g hq
  have hinner : ∀ k ∈ S.image g,
      (S.filter (fun q => g q = k)).sum
          (fun q => (mult q : ℝ) * M (g q)) =
        (S.filter (fun q => g q = k)).sum (fun q => (mult q : ℝ)) * M k := by
    intro k _hk
    have : ∀ q ∈ S.filter (fun q => g q = k),
        (mult q : ℝ) * M (g q) = (mult q : ℝ) * M k := by
      intro q hq
      rw [(mem_filter.mp hq).2]
    rw [sum_congr rfl this, sum_mul]
  have hS :=
    disjiUnion_filter_eq_of_maps_to (s := S) (t := S.image g) (f := g) hmaps
  conv_lhs => rw [← hS]
  rw [sum_disjiUnion]
  exact sum_congr rfl hinner

lemma increment_fiber_le (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliant Z) (k : ℤ)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    (S.filter (fun q => ordinateBin q.2 = k)).sum
        (fun q => (Z.mult q : ℝ)) ≤ (gaborKBin : ℝ) := by
  have hsub :
      S.filter (fun q => ordinateBin q.2 = k) ⊆
        Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1) := by
    intro q hq
    have hqS := (mem_filter.mp hq).1
    have hbin : ordinateBin q.2 = k := (mem_filter.mp hq).2
    have hm := mem_ordinateBin q.2
    have hm' : (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1 := by
      simpa [hbin] using hm
    exact mem_filter.mpr ⟨hS hqS, hm'⟩
  exact (sum_le_sum_of_subset_of_nonneg hsub
      (fun _ _ _ => Nat.cast_nonneg _)).trans (hinc k)

/-- Multiplicity-aware bin packing against a pointwise bin majorant. -/
theorem bin_partial_summation_mult
    {w : ℝ → ℝ} (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliant Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts)
    {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k)
    (hM : ∀ q ∈ S, w q.2 ≤ M (ordinateBin q.2))
    (hMs : Summable M) :
    S.sum (fun q => (Z.mult q : ℝ) * w q.2) ≤
      (gaborKBin : ℝ) * ∑' k : ℤ, M k := by
  have hpt : S.sum (fun q => (Z.mult q : ℝ) * w q.2) ≤
      S.sum (fun q => (Z.mult q : ℝ) * M (ordinateBin q.2)) := by
    refine sum_le_sum fun q hq => ?_
    exact mul_le_mul_of_nonneg_left (hM q hq) (Nat.cast_nonneg _)
  let g : ℝ × ℝ → ℤ := fun q => ordinateBin q.2
  have hfib := sum_fiber_weight S Z.mult g M
  have hsum₂ :
      S.sum (fun q => (Z.mult q : ℝ) * M (g q)) ≤
        ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k := by
    rw [hfib]
    refine sum_le_sum fun k _hk => ?_
    have hmass := increment_fiber_le Z hinc k S hS
    exact mul_le_mul_of_nonneg_right hmass (hM0 k)
  have hsum₃ :
      ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k =
        (gaborKBin : ℝ) * ∑ k ∈ S.image g, M k := by
    simp [mul_sum]
  have hsum₄ : ∑ k ∈ S.image g, M k ≤ ∑' k : ℤ, M k :=
    hMs.sum_le_tsum _ (fun _ _ => hM0 _)
  calc
    S.sum (fun q => (Z.mult q : ℝ) * w q.2)
        ≤ S.sum (fun q => (Z.mult q : ℝ) * M (g q)) := hpt
    _ ≤ ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k := hsum₂
    _ = (gaborKBin : ℝ) * ∑ k ∈ S.image g, M k := hsum₃
    _ ≤ (gaborKBin : ℝ) * ∑' k : ℤ, M k :=
        mul_le_mul_of_nonneg_left hsum₄ gaborKBin_pos.le

/-! ## Plus / cross / far packings -/

lemma plus_gauss_mono_bin {a omega t : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (ht : 0 < t) :
    Real.exp (-(t + omega) ^ 2 / (2 * a)) ≤
      Real.exp (-((ordinateBin t : ℝ) + omega) ^ 2 / (2 * a)) := by
  have hmem := mem_Icc_of_ordinateBin t
  have hk0 : (0 : ℤ) ≤ ordinateBin t := ordinateBin_nonneg_of_pos ht
  have hge : (ordinateBin t : ℝ) + omega ≤ t + omega := by
    linarith [hmem.1]
  have hpos : 0 ≤ (ordinateBin t : ℝ) + omega :=
    add_nonneg (by exact_mod_cast hk0) hω.le
  have hsq : ((ordinateBin t : ℝ) + omega) ^ 2 ≤ (t + omega) ^ 2 :=
    sq_le_sq.mpr (by rwa [abs_of_nonneg hpos, abs_of_nonneg (by linarith)])
  refine Real.exp_le_exp.mpr ?_
  exact div_le_div_of_nonneg_right (neg_le_neg hsq)
    (mul_nonneg (by norm_num) ha.le)

lemma plus_bin_tsum_le {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => 0 ≤ k),
        Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a)) ≤
      ∑' n : ℕ, Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) := by
  set Kp := K.filter (fun k => 0 ≤ k)
  let φ : ℤ → ℕ := fun k => k.toNat
  have hφ : ∀ k ∈ Kp, (k : ℝ) = (φ k : ℝ) := by
    intro k hk
    have hk0 : 0 ≤ k := (mem_filter.mp hk).2
    exact_mod_cast (Int.toNat_of_nonneg hk0).symm
  have hinj : ∀ k₁ ∈ Kp, ∀ k₂ ∈ Kp, φ k₁ = φ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ h
    have h1 : 0 ≤ k₁ := (mem_filter.mp hk₁).2
    have h2 : 0 ≤ k₂ := (mem_filter.mp hk₂).2
    have : (k₁.toNat : ℤ) = (k₂.toNat : ℤ) := by exact_mod_cast h
    rw [Int.toNat_of_nonneg h1, Int.toNat_of_nonneg h2] at this
    exact this
  have himage :
      ∑ k ∈ Kp, Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a)) =
        ∑ n ∈ Kp.image φ,
          Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) := by
    rw [sum_image hinj]
    refine sum_congr rfl fun k hk => ?_
    rw [hφ k hk]
  have hsm :
      Summable fun n : ℕ =>
        Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) :=
    Summable.of_nonneg_of_le (fun _ => (Real.exp_pos _).le)
      (fun n => gaborPlusBin_geom ha hω n)
      ((summable_geometric_of_lt_one (Real.exp_pos _).le
          (by
            rw [Real.exp_lt_one_iff]
            exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha)).mul_left _)
  rw [himage]
  exact hsm.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)

theorem gabor_plus_amp_pack
    {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliant Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    S.sum (fun q => (Z.mult q : ℝ) *
        Real.exp (-(q.2 + omega) ^ 2 / (2 * a))) ≤
      (gaborKBin : ℝ) *
        (∑' n : ℕ, Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a))) := by
  have hpt : ∀ q ∈ S,
      Real.exp (-(q.2 + omega) ^ 2 / (2 * a)) ≤
        Real.exp (-((ordinateBin q.2 : ℝ) + omega) ^ 2 / (2 * a)) := by
    intro q hq
    exact plus_gauss_mono_bin ha hω (Z.gamma_pos q (hS hq))
  have hsum₁ :
      S.sum (fun q => (Z.mult q : ℝ) *
          Real.exp (-(q.2 + omega) ^ 2 / (2 * a))) ≤
        S.sum (fun q => (Z.mult q : ℝ) *
          Real.exp (-((ordinateBin q.2 : ℝ) + omega) ^ 2 / (2 * a))) :=
    sum_le_sum fun q hq =>
      mul_le_mul_of_nonneg_left (hpt q hq) (Nat.cast_nonneg (Z.mult q))
  let g : ℝ × ℝ → ℤ := fun q => ordinateBin q.2

  let M : ℤ → ℝ := fun k =>
    Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a))
  have hfib := sum_fiber_weight S Z.mult g M
  have hsum₂ :
      S.sum (fun q => (Z.mult q : ℝ) * M (g q)) ≤
        ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k := by
    rw [hfib]
    refine sum_le_sum fun k _hk => ?_
    exact mul_le_mul_of_nonneg_right
      (increment_fiber_le Z hinc k S hS) (Real.exp_pos _).le
  have hsum₃ :
      ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k =
        (gaborKBin : ℝ) * ∑ k ∈ S.image g, M k := by
    simp [mul_sum]
  have hnn : ∀ k ∈ S.image g, 0 ≤ k := by
    intro k hk
    obtain ⟨q, hq, rfl⟩ := mem_image.mp hk
    exact ordinateBin_nonneg_of_pos (Z.gamma_pos q (hS hq))
  have hsum₄ :
      ∑ k ∈ S.image g, M k ≤
        ∑' n : ℕ, Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) := by
    have : ∑ k ∈ S.image g, M k =
        ∑ k ∈ (S.image g).filter (fun k => 0 ≤ k), M k := by
      refine (sum_subset (filter_subset _ _) ?_).symm
      intro k hk hkf
      have : 0 ≤ k := hnn k hk
      exact (hkf (mem_filter.mpr ⟨hk, this⟩)).elim
    rw [this]
    simpa [M] using plus_bin_tsum_le ha hω (S.image g)
  calc
    S.sum (fun q => (Z.mult q : ℝ) *
        Real.exp (-(q.2 + omega) ^ 2 / (2 * a)))
        ≤ S.sum (fun q => (Z.mult q : ℝ) * M (g q)) := hsum₁
    _ ≤ ∑ k ∈ S.image g, (gaborKBin : ℝ) * M k := hsum₂
    _ = (gaborKBin : ℝ) * ∑ k ∈ S.image g, M k := hsum₃
    _ ≤ (gaborKBin : ℝ) *
          (∑' n : ℕ, Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a))) :=
        mul_le_mul_of_nonneg_left hsum₄ gaborKBin_pos.le

theorem gabor_plus_amp_pack_loose
    {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliant Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    S.sum (fun q => (Z.mult q : ℝ) *
        Real.exp (-(q.2 + omega) ^ 2 / (2 * a))) ≤
      (gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) /
        (1 - Real.exp (-omega / a)) := by
  refine (gabor_plus_amp_pack ha hω Z hinc S hS).trans ?_
  have hmaj := gaborPlusLobe_majorant ha hω
  have := mul_le_mul_of_nonneg_left hmaj gaborKBin_pos.le
  convert this using 1
  field_simp

theorem gabor_cross_amp_pack
    {a : ℝ} (ha : 0 < a)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliant Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    S.sum (fun q => (Z.mult q : ℝ) * Real.exp (-q.2 ^ 2 / (2 * a))) ≤
      (gaborKBin : ℝ) * thetaLobe a := by
  let w : ℝ → ℝ := fun t => Real.exp (-t ^ 2 / (2 * a))
  let M : ℤ → ℝ := fun k => gaussBinMax a 0 k
  have hM0 : ∀ k, 0 ≤ M k := fun k => gaussBinMax_nonneg ha k
  have hM : ∀ q ∈ S, w q.2 ≤ M (ordinateBin q.2) := by
    intro q _hq
    have : w q.2 = gaussWeight a 0 q.2 := by
      unfold gaussWeight w
      congr 1
      ring
    rw [this]
    exact le_gaussBinMax ha (mem_Icc_of_ordinateBin q.2)
  have hpack :=
    bin_partial_summation_mult (w := w) Z hinc S hS hM0 hM
      (gaussBinMax_summable ha)
  refine hpack.trans ?_
  exact mul_le_mul_of_nonneg_left (gauss_binMax_tsum_le ha) gaborKBin_pos.le

lemma gaussBinMax_far_tsum_le {a c : ℝ} (ha : 0 < a) :
    (∑' k : ℤ,
      if k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k then
        gaussBinMax a c k else 0) ≤ thetaLobe a - 3 := by
  refine Real.tsum_le_of_sum_le
    (fun k => by
      split_ifs
      · exact gaussBinMax_nonneg ha k
      · exact le_rfl) fun K => ?_
  have hite :
      ∑ k ∈ K,
          (if k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k then
            gaussBinMax a c k else 0) =
        ∑ k ∈ K.filter (fun k =>
            k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k),
          gaussBinMax a c k :=
    (sum_filter (p := fun k =>
        k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k)
      (f := fun k => gaussBinMax a c k)).symm
  rw [hite]
  exact gaussBinMax_far_sum_le ha K

lemma foreign_not_in_peakWindow
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hdist : Z.gammaDistinct) {q : ℝ × ℝ} (hq : q ∈ Z.pts)
    (hne : q ≠ (gaborHostSigma Z hZ, gaborHostGamma Z hZ)) :
    ¬ gaborInPeakWindow q.2 (isolationShrinkOfConfig Z hZ).2
        (isolationShrinkOfConfig Z hZ).1 := by
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set ω := (isolationShrinkOfConfig Z hZ).2
  have hωeq : ω = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  have hγne : q.2 ≠ γ := by
    intro heq
    exact hne (gaborHost_unique_gamma Z hZ hdist hq heq)
  have hfor : (Z.pts.filter (fun r => r.2 ≠ γ)).Nonempty :=
    ⟨q, mem_filter.mpr ⟨hq, hγne⟩⟩
  have hadm := isolationShrinkOfConfig_admissible_of_foreign Z hZ hfor
  have hgap := gaborForeignDMin_le Z γ hq hγne
  have hs := gaborHostSigma_pos Z hZ
  have hd := gaborForeignDMin_pos Z γ
  rw [hωeq]
  exact admissible_peakWindow_empty hs hd hadm hgap

/-- Peak-window emptiness at a free admissible width
`0 < a ≤ isolationShrink`.  ω retunes with a
(`gaborIsolationOmega`); emptiness is the radius constraint,
which is monotone.  The detune `πa/σ★` shrinks (lock:
`πa/σ★ ≤ πσ★/512` by `gaborALock_detune_le_quarter`). -/
lemma foreign_not_in_peakWindow_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hdist : Z.gammaDistinct) {q : ℝ × ℝ} (hq : q ∈ Z.pts)
    (hne : q ≠ (gaborHostSigma Z hZ, gaborHostGamma Z hZ))
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    ¬ gaborInPeakWindow q.2
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) a := by
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  have hγne : q.2 ≠ γ := by
    intro heq
    exact hne (gaborHost_unique_gamma Z hZ hdist hq heq)
  have hfor : (Z.pts.filter (fun r => r.2 ≠ γ)).Nonempty :=
    ⟨q, mem_filter.mpr ⟨hq, hγne⟩⟩
  have hadm := isolationShrinkOfConfig_admissible_of_le Z hZ hfor ha hle
  have hgap := gaborForeignDMin_le Z γ hq hγne
  have hs := gaborHostSigma_pos Z hZ
  have hd := gaborForeignDMin_pos Z γ
  exact admissible_peakWindow_empty hs hd hadm hgap

lemma far_minus_majorant
    {a omega ε t : ℝ} (ha : 0 < a) (hε : 0 ≤ ε)
    (hout : ε < |t - omega|) :
    gaussWeight a omega t ≤
      if ordinateBin t ≤ Int.floor omega - 2 ∨
          Int.floor omega + 2 ≤ ordinateBin t then
        gaussBinMax a omega (ordinateBin t)
      else
        Real.exp (-ε ^ 2 / (2 * a)) := by
  set k := ordinateBin t
  set n := Int.floor omega
  by_cases hfar : k ≤ n - 2 ∨ n + 2 ≤ k
  · simp [hfar]
    exact le_gaussBinMax ha (mem_Icc_of_ordinateBin t)
  · simp [hfar]
    unfold gaussWeight
    refine Real.exp_le_exp.mpr ?_
    have hsq : ε ^ 2 ≤ (t - omega) ^ 2 :=
      sq_le_sq.mpr (by
        rw [abs_of_nonneg hε]
        exact hout.le)
    exact div_le_div_of_nonneg_right (neg_le_neg hsq)
      (mul_nonneg (by norm_num) ha.le)

lemma far_M_tsum_le {a omega ε : ℝ} (ha : 0 < a) (_hε : 0 ≤ ε) :
    (∑' k : ℤ,
      if k ≤ Int.floor omega - 2 ∨ Int.floor omega + 2 ≤ k then
        gaussBinMax a omega k
      else Real.exp (-ε ^ 2 / (2 * a))) ≤
      4 * Real.exp (-ε ^ 2 / (2 * a)) + (thetaLobe a - 3) := by
  set n := Int.floor omega
  set c : ℝ := Real.exp (-ε ^ 2 / (2 * a))
  have hc0 : 0 ≤ c := (Real.exp_pos _).le
  let s : Finset ℤ := {n - 1, n, n + 1}
  have hpt : ∀ k : ℤ,
      (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else c) =
        (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else (0 : ℝ)) +
          (if k ∈ s then c else 0) := by
    intro k
    by_cases hfar : k ≤ n - 2 ∨ n + 2 ≤ k
    · have hcen : k ∉ s := by
        intro hk
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [s] using hk
        omega
      simp [hfar, hcen]
    · have hcen : k ∈ s := by
        have : n - 1 ≤ k ∧ k ≤ n + 1 := by omega
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by omega
        simpa [s] using this
      simp [hfar, hcen]
  have hf : Summable fun k : ℤ =>
      if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else (0 : ℝ) :=
    Summable.of_nonneg_of_le
      (fun k => by
        split_ifs
        · exact gaussBinMax_nonneg ha k
        · exact le_rfl)
      (fun k => by
        split_ifs
        · exact le_rfl
        · exact gaussBinMax_nonneg ha k)
      (gaussBinMax_summable ha)
  have hg : Summable fun k : ℤ => if k ∈ s then c else (0 : ℝ) :=
    (hasSum_sum_of_ne_finset_zero (s := s)
      (fun k hk => by simp [hk])).summable
  have hts :
      (∑' k : ℤ,
        if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else c) =
        (∑' k : ℤ,
          if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else 0) +
          (∑' k : ℤ, if k ∈ s then c else 0) := by
    have hsum :
        (∑' k : ℤ,
          ((if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else (0 : ℝ)) +
            (if k ∈ s then c else (0 : ℝ)))) =
          (∑' k : ℤ,
            if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else (0 : ℝ)) +
            (∑' k : ℤ, if k ∈ s then c else (0 : ℝ)) :=
      hf.tsum_add hg
    rw [← hsum]
    exact tsum_congr hpt
  have hcen :
      (∑' k : ℤ, if k ∈ s then c else 0) = (3 : ℝ) * c := by
    have hz : ∀ k ∉ s, (if k ∈ s then c else 0) = 0 := by
      intro k hk
      simp [hk]
    rw [tsum_eq_sum hz]
    have hval : ∀ k ∈ s, (if k ∈ s then c else 0) = c :=
      fun k hk => if_pos hk
    rw [sum_congr rfl hval, sum_const, nsmul_eq_mul]
    have hcard : (s.card : ℝ) = 3 := by
      exact_mod_cast central3_card n
    rw [hcard]
  rw [hts, hcen]
  have hfar := gaussBinMax_far_tsum_le (c := omega) ha
  have h3 : (3 : ℝ) * c ≤ 4 * c := by nlinarith [hc0]
  linarith [hfar, h3]

lemma far_M_summable {a omega ε : ℝ} (ha : 0 < a) :
    Summable fun k : ℤ =>
      if k ≤ Int.floor omega - 2 ∨ Int.floor omega + 2 ≤ k then
        gaussBinMax a omega k
      else Real.exp (-ε ^ 2 / (2 * a)) := by
  set n := Int.floor omega
  set c : ℝ := Real.exp (-ε ^ 2 / (2 * a))
  let s : Finset ℤ := {n - 1, n, n + 1}
  have h1 : Summable fun k : ℤ =>
      if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k else (0 : ℝ) :=
    Summable.of_nonneg_of_le
      (fun k => by
        split_ifs
        · exact gaussBinMax_nonneg ha k
        · exact le_rfl)
      (fun k => by
        split_ifs
        · exact le_rfl
        · exact gaussBinMax_nonneg ha k)
      (gaussBinMax_summable ha)
  have h2 : Summable fun k : ℤ => if k ∈ s then c else (0 : ℝ) :=
    (hasSum_sum_of_ne_finset_zero (s := s)
      (fun k hk => by simp [hk])).summable
  refine (h1.add h2).congr fun k => ?_
  by_cases hfar : k ≤ n - 2 ∨ n + 2 ≤ k
  · have hcen : k ∉ s := by
      intro hk
      have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [s] using hk
      omega
    simp [hfar, hcen]
  · have hcen : k ∈ s := by
      have : n - 1 ≤ k ∧ k ≤ n + 1 := by omega
      have : k = n - 1 ∨ k = n ∨ k = n + 1 := by omega
      simpa [s] using this
    simp [hfar, hcen]

theorem gabor_far_minus_pack
    {a omega ε : ℝ} (ha : 0 < a) (hε : 0 ≤ ε)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliant Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts)
    (hout : ∀ q ∈ S, ε < |q.2 - omega|) :
    S.sum (fun q => (Z.mult q : ℝ) * gaussWeight a omega q.2) ≤
      (gaborKBin : ℝ) *
        (4 * Real.exp (-ε ^ 2 / (2 * a)) + (thetaLobe a - 3)) := by
  let M : ℤ → ℝ := fun k =>
    if k ≤ Int.floor omega - 2 ∨ Int.floor omega + 2 ≤ k then
      gaussBinMax a omega k
    else Real.exp (-ε ^ 2 / (2 * a))
  have hM0 : ∀ k, 0 ≤ M k := by
    intro k
    unfold M
    split_ifs
    · exact gaussBinMax_nonneg ha k
    · exact (Real.exp_pos _).le
  have hM : ∀ q ∈ S, gaussWeight a omega q.2 ≤ M (ordinateBin q.2) := by
    intro q hq
    simpa [M] using far_minus_majorant ha hε (hout q hq)
  have hpack :=
    bin_partial_summation_mult (w := gaussWeight a omega) Z hinc S hS
      hM0 hM (far_M_summable ha)
  refine hpack.trans ?_
  exact mul_le_mul_of_nonneg_left (far_M_tsum_le ha hε) gaborKBin_pos.le

/-! ## Honest Weil packing comparison -/

lemma gaborMinus_eq_gaussWeight {a omega gamma : ℝ} :
    Real.exp (-(gamma - omega) ^ 2 / (2 * a)) =
      gaussWeight a omega gamma := by
  unfold gaussWeight
  rfl

lemma le_mul_enhancement {E x b : ℝ} (hE : 0 < E) (h : x / E ≤ b) :
    x ≤ E * b := by
  have := (div_le_iff₀ hE).mp h
  rwa [mul_comm b E] at this

lemma sum_enhancement_mul (E : ℝ) (S : Finset (ℝ × ℝ))
    (mult : ℝ × ℝ → ℕ) (w : ℝ × ℝ → ℝ) :
    S.sum (fun q => (mult q : ℝ) * E * w q) =
      E * S.sum (fun q => (mult q : ℝ) * w q) := by
  calc
    S.sum (fun q => (mult q : ℝ) * E * w q)
        = S.sum (fun q => E * ((mult q : ℝ) * w q)) := by
          refine sum_congr rfl fun q _ => ?_
          ring
    _ = E * S.sum (fun q => (mult q : ℝ) * w q) := by
          rw [← mul_sum]

theorem gaborHonestWeilLeMajorant_holds : GaborHonestWeilLeMajorant := by
  intro Z hZ hinc hdist
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set host : ℝ × ℝ := (σ, γ)
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hω := isolationShrinkOfConfig_omega_pos Z hZ
  have hs := gaborHostSigma_pos Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hωeq : omega = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  have hhost := gaborHost_mem Z hZ
  have hσ0 : ∀ q ∈ Z.pts, 0 ≤ q.1 :=
    fun q hq => (Z.sigma_off q hq).1.le
  have hσle : ∀ q ∈ Z.pts, q.1 ≤ σ :=
    fun q hq => gaborHostSigma_max Z hZ hq
  have hhostMinus :
      (Z.mult host : ℝ) * gaborMinusTerm a omega σ γ =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ)) := by
    have hm : Z.mult host = gaborHostMult Z hZ := rfl
    rw [hωeq, hm]
    have :=
      gaborHostMerge_minusLobe (m := gaborHostMult Z hZ) (sigma := σ)
        (gamma := γ) (a := a) hs ha
    convert this using 1
    ring
  have hplus_pt : ∀ q ∈ Z.pts,
      (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2 ≤
        (Z.mult q : ℝ) * gaborEnhancement σ a *
          Real.exp (-(q.2 + omega) ^ 2 / (2 * a)) := by
    intro q hq
    have hdiv :=
      gaborPlusTerm_div_E_le_gauss (sigmaStar := σ) (omega := omega)
        (sigma := q.1) (gamma := q.2) ha (hσ0 q hq) (hσle q hq)
    have hle := le_mul_enhancement hE hdiv
    simpa [mul_assoc] using
      mul_le_mul_of_nonneg_left hle (Nat.cast_nonneg (Z.mult q))
  have hcross_pt : ∀ q ∈ Z.pts,
      (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2) ≤
        (Z.mult q : ℝ) * (2 * gaborEnhancement σ a) *
          (Real.exp (-omega ^ 2 / (2 * a)) *
            Real.exp (-q.2 ^ 2 / (2 * a))) := by
    intro q hq
    have hdiv :=
      gaborCrossTerm_div_E_le_lobe (sigmaStar := σ) (omega := omega)
        (sigma := q.1) (gamma := q.2) ha (hσ0 q hq) (hσle q hq)
    have hle := le_mul_enhancement hE hdiv
    have h2 := mul_le_mul_of_nonneg_left hle (by norm_num : (0 : ℝ) ≤ 2)
    have hmul :=
      mul_le_mul_of_nonneg_left h2 (Nat.cast_nonneg (Z.mult q))
    have hassoc :
        (Z.mult q : ℝ) * (2 * gaborEnhancement σ a) *
            (Real.exp (-omega ^ 2 / (2 * a)) *
              Real.exp (-q.2 ^ 2 / (2 * a))) =
          (Z.mult q : ℝ) *
            (2 * (gaborEnhancement σ a *
              (Real.exp (-omega ^ 2 / (2 * a)) *
                Real.exp (-q.2 ^ 2 / (2 * a))))) := by
      ring
    rwa [hassoc]
  have hminus_pt : ∀ q ∈ Z.pts.erase host,
      (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2 ≤
        (Z.mult q : ℝ) * gaborEnhancement σ a *
          gaussWeight a omega q.2 := by
    intro q hq
    have hqpts : q ∈ Z.pts := erase_subset _ _ hq
    have hdiv :=
      gaborMinusTerm_div_E_le_gauss (sigmaStar := σ) (omega := omega)
        (sigma := q.1) (gamma := q.2) ha (hσ0 q hqpts) (hσle q hqpts)
    have hle := le_mul_enhancement hE hdiv
    simpa [mul_assoc, gaborMinus_eq_gaussWeight] using
      mul_le_mul_of_nonneg_left hle (Nat.cast_nonneg (Z.mult q))
  have hplus_sum :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a *
          ((gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) /
            (1 - Real.exp (-omega / a))) := by
    have h1 := sum_le_sum hplus_pt
    have h2 :=
      sum_enhancement_mul (gaborEnhancement σ a) Z.pts Z.mult
        (fun q => Real.exp (-(q.2 + omega) ^ 2 / (2 * a)))
    rw [h2] at h1
    exact h1.trans (mul_le_mul_of_nonneg_left
      (gabor_plus_amp_pack_loose ha hω Z hinc Z.pts subset_rfl) hE.le)
  have hcross_sum :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) ≤
        gaborEnhancement σ a *
          ((gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
            (2 * thetaLobe a)) := by
    have h1 := sum_le_sum hcross_pt
    have hfactor :
        Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * (2 * gaborEnhancement σ a) *
              (Real.exp (-omega ^ 2 / (2 * a)) *
                Real.exp (-q.2 ^ 2 / (2 * a)))) =
          (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            Z.pts.sum (fun q => (Z.mult q : ℝ) *
              Real.exp (-q.2 ^ 2 / (2 * a))) := by
      calc
        _ = Z.pts.sum (fun q =>
              (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
                ((Z.mult q : ℝ) * Real.exp (-q.2 ^ 2 / (2 * a)))) := by
          refine sum_congr rfl fun q _ => ?_
          ring
        _ = _ := by rw [← mul_sum]
    rw [hfactor] at h1
    have hpack := gabor_cross_amp_pack ha Z hinc Z.pts subset_rfl
    have hc0 : 0 ≤
        2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a)) := by
      positivity
    have hscale :
        (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            Z.pts.sum (fun q => (Z.mult q : ℝ) *
              Real.exp (-q.2 ^ 2 / (2 * a))) ≤
          (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            ((gaborKBin : ℝ) * thetaLobe a) :=
      mul_le_mul_of_nonneg_left hpack hc0
    have heq :
        (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            ((gaborKBin : ℝ) * thetaLobe a) =
          gaborEnhancement σ a *
            ((gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
              (2 * thetaLobe a)) := by
      ring
    exact h1.trans (hscale.trans_eq heq)
  have hε0 : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
  have hout : ∀ q ∈ Z.pts.erase host,
      gaborIsolationEpsilon a < |q.2 - omega| := by
    intro q hq
    have := foreign_not_in_peakWindow Z hZ hdist
      (erase_subset _ _ hq) (ne_of_mem_erase hq)
    simpa [gaborInPeakWindow] using lt_of_not_ge this
  have hminus_sum :
      (Z.pts.erase host).sum (fun q =>
          (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a * gaborTFar a := by
    have h1 := sum_le_sum hminus_pt
    have h2 :=
      sum_enhancement_mul (gaborEnhancement σ a) (Z.pts.erase host) Z.mult
        (fun q => gaussWeight a omega q.2)
    rw [h2] at h1
    refine h1.trans (mul_le_mul_of_nonneg_left ?_ hE.le)
    simpa [gaborTFar] using
      gabor_far_minus_pack ha hε0 Z hinc (Z.pts.erase host)
        (erase_subset _ _) hout
  have hQsum :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) =
        Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) := by
    have hpt : ∀ q ∈ Z.pts,
        (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2 =
          (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2 +
            (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2 +
            (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2) := by
      intro q _
      rw [gaborQuadrupole_eq_terms]
      ring
    rw [sum_congr rfl hpt, sum_add_distrib, sum_add_distrib]
  have hsplitM :=
    Finset.sum_erase_add
      (fun q => (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2)
      (s := Z.pts) hhost
  have hW :
      gaborHonestWeil a omega Z gaborCInc =
        (Z.mult host : ℝ) * gaborMinusTerm a omega σ γ +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) +
          (Z.pts.erase host).sum (fun q =>
            (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) +
          gaborHonestOnlineBudget a omega gaborCInc := by
    unfold gaborHonestWeil
    rw [hQsum, ← hsplitM]
    simp [host]
    ring
  have hpack :
      Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) +
          (Z.pts.erase host).sum (fun q =>
            (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a * (gaborTPlusLoose a omega + gaborTFar a) := by
    have hsum :
        gaborEnhancement σ a *
            ((gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) /
              (1 - Real.exp (-omega / a))) +
          gaborEnhancement σ a *
            ((gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
              (2 * thetaLobe a)) +
          gaborEnhancement σ a * gaborTFar a =
        gaborEnhancement σ a * (gaborTPlusLoose a omega + gaborTFar a) := by
      unfold gaborTPlusLoose
      ring
    linarith [hplus_sum, hcross_sum, hminus_sum, hsum]
  have hWle :
      gaborHonestWeil a omega Z gaborCInc ≤
        gaborEnhancement σ a *
            (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
              gaborTPlusLoose a omega + gaborTFar a) +
          gaborHonestOnlineBudget a omega gaborCInc := by
    rw [hW, hhostMinus]
    have hdecomp :
        gaborEnhancement σ a *
              (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ)) +
            gaborEnhancement σ a * (gaborTPlusLoose a omega + gaborTFar a) +
            gaborHonestOnlineBudget a omega gaborCInc =
          gaborEnhancement σ a *
              (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
                gaborTPlusLoose a omega + gaborTFar a) +
            gaborHonestOnlineBudget a omega gaborCInc := by
      ring
    linarith [hpack, hdecomp]
  simpa [a, omega, σ] using hWle

/-! ## Remainder budget under the r569 cap -/

lemma gaborKBin_eq : (gaborKBin : ℝ) = 43 := by
  simp [gaborKBin]

lemma binSq_inv_le {a : ℝ} (ha : 0 < a)
    (h : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    8 * (gaborKBin : ℝ) ^ 2 ≤ 1 / a := by
  have hC : (0 : ℝ) < 8 * (gaborKBin : ℝ) ^ 2 :=
    mul_pos (by norm_num) (sq_pos_of_pos gaborKBin_pos)
  rw [le_div_iff₀ ha, mul_comm]
  exact (le_div_iff₀ hC).mp h

lemma inv_two_a_ge_sixty_four {a : ℝ} (ha : 0 < a)
    (h : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    (64 : ℝ) ≤ 1 / (2 * a) := by
  have h1 := binSq_inv_le ha h
  have hhalf : (8 * (gaborKBin : ℝ) ^ 2) / 2 ≤ (1 / a) / 2 :=
    div_le_div_of_nonneg_right h1 (by norm_num)
  have hL : (8 * (gaborKBin : ℝ) ^ 2) / 2 = 4 * (gaborKBin : ℝ) ^ 2 := by ring
  have hR : (1 / a) / 2 = 1 / (2 * a) := by
    field_simp [ne_of_gt ha]
  rw [hL, hR] at hhalf
  have h64 : (64 : ℝ) ≤ 4 * (gaborKBin : ℝ) ^ 2 := by
    simp [gaborKBin]; norm_num
  exact h64.trans hhalf

lemma omega_sq_div_two_a_ge_sixty_four {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512) :
    (64 : ℝ) ≤ gaborIsolationOmega sigma gamma a ^ 2 / (2 * a) := by
  have hωhalf := gaborIsolationOmega_pos_of_cap hs hg ha.le hωcap
  have hω0 : 0 ≤ gaborIsolationOmega sigma gamma a :=
    (half_pos hg).le.trans hωhalf
  have hsq : (gamma / 2) ^ 2 ≤ gaborIsolationOmega sigma gamma a ^ 2 :=
    sq_le_sq.mpr (by
      rw [abs_of_nonneg (div_nonneg hg.le (by norm_num)), abs_of_nonneg hω0]
      exact hωhalf)
  have hfrac : (gamma / 2) ^ 2 / (2 * a) ≤
      gaborIsolationOmega sigma gamma a ^ 2 / (2 * a) :=
    div_le_div_of_nonneg_right hsq (mul_nonneg (by norm_num) ha.le)
  have hform : (gamma / 2) ^ 2 / (2 * a) = gamma ^ 2 / (8 * a) := by ring
  have h64 : (64 : ℝ) ≤ gamma ^ 2 / (8 * a) := by
    have : 64 * (8 * a) ≤ gamma ^ 2 := by
      have ha512 : a * 512 ≤ gamma ^ 2 :=
        (le_div_iff₀ (by norm_num : (0 : ℝ) < 512)).mp hγsq
      linarith
    exact (le_div_iff₀ (mul_pos (by norm_num) ha)).mpr this
  exact h64.trans (hform ▸ hfrac)

lemma isolationOmega_div_a_ge_sixty_four {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    (64 : ℝ) ≤ gaborIsolationOmega sigma gamma a / a := by
  have h64 := omega_sq_div_two_a_ge_sixty_four hs hg ha hωcap hγsq
  have hω := gaborIsolationOmega_pos hs hg ha.le hωcap
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hident :
      (gaborIsolationOmega sigma gamma a / a) ^ 2 =
        (gaborIsolationOmega sigma gamma a ^ 2 / (2 * a)) * (2 / a) := by
    field_simp [ha0]
  have hmul :
      64 * (2 / a) ≤
        (gaborIsolationOmega sigma gamma a ^ 2 / (2 * a)) * (2 / a) :=
    mul_le_mul_of_nonneg_right h64 (div_nonneg (by norm_num) ha.le)
  have hL : 64 * (2 / a) = 128 / a := by ring
  have hratio_sq : 128 / a ≤ (gaborIsolationOmega sigma gamma a / a) ^ 2 := by
    rw [hident, ← hL]
    exact hmul
  have ha_inv := binSq_inv_le ha hbin
  have h128 : 128 * (8 * (gaborKBin : ℝ) ^ 2) ≤ 128 / a := by
    have := mul_le_mul_of_nonneg_left ha_inv (by norm_num : (0 : ℝ) ≤ 128)
    rwa [mul_one_div] at this
  have hsqK : ((32 : ℝ) * (gaborKBin : ℝ)) ^ 2 =
      128 * (8 * (gaborKBin : ℝ) ^ 2) := by ring
  have hsq : ((32 : ℝ) * (gaborKBin : ℝ)) ^ 2 ≤
      (gaborIsolationOmega sigma gamma a / a) ^ 2 := by
    rw [hsqK]
    exact h128.trans hratio_sq
  have hpos : 0 ≤ (32 : ℝ) * (gaborKBin : ℝ) :=
    mul_nonneg (by norm_num) gaborKBin_pos.le
  have hωa0 : 0 ≤ gaborIsolationOmega sigma gamma a / a :=
    div_nonneg hω.le ha.le
  have habs := sq_le_sq.mp hsq
  rw [abs_of_nonneg hpos, abs_of_nonneg hωa0] at habs
  have h32 : (64 : ℝ) ≤ 32 * (gaborKBin : ℝ) := by
    simp [gaborKBin]; norm_num
  exact h32.trans habs

lemma exp_neg_omega_a_le_half {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    Real.exp (-gaborIsolationOmega sigma gamma a / a) ≤ (1 / 2 : ℝ) := by
  have hωa := isolationOmega_div_a_ge_sixty_four hs hg ha hωcap hγsq hbin
  have h1 : Real.exp (-gaborIsolationOmega sigma gamma a / a) ≤
      Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg hωa
  have h2 : Real.exp (-(64 : ℝ)) ≤ Real.exp (-(4 : ℝ)) :=
    Real.exp_le_exp.mpr (by norm_num)
  have h3 : Real.exp (-(4 : ℝ)) ≤ (1 / 16 : ℝ) := gaborExp_neg_four_le
  have h4 : (1 / 16 : ℝ) ≤ (1 / 2 : ℝ) := by norm_num
  exact h1.trans (h2.trans (h3.trans h4))

lemma thetaLeftPos_of_small {a omega : ℝ}
    (hω : 0 < omega) (hξ : Real.exp (-omega / a) < (1 / 2 : ℝ)) :
    thetaLeftPos a omega =
      Real.exp (-omega ^ 2 / (2 * a)) /
        (1 - Real.exp (-omega / a)) := by
  rw [thetaLeftPos, if_neg (not_or.mpr ⟨not_le.mpr hω, not_le.mpr hξ⟩)]

lemma exp_over_one_sub_le {x y : ℝ} (hx : 0 ≤ x) (hy : x ≤ y)
    (hy1 : y ≤ (1 / 2 : ℝ)) :
    x / (1 - y) ≤ 2 * y := by
  have hden : (1 / 2 : ℝ) ≤ 1 - y := by linarith
  have hden0 : 0 < 1 - y := lt_of_lt_of_le (by norm_num) hden
  have h1 : x / (1 - y) ≤ y / (1 - y) :=
    div_le_div_of_nonneg_right hy hden0.le
  have h2 : y / (1 - y) ≤ y / (1 / 2 : ℝ) :=
    div_le_div_of_nonneg_left (le_trans hx hy) (by norm_num) hden
  have h3 : y / (1 / 2 : ℝ) = 2 * y := by field_simp
  exact h1.trans (h2.trans_eq h3)

lemma thetaLobe_sub_three_le_four_exp {a : ℝ} (ha : 0 < a)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    thetaLobe a - 3 ≤ 4 * Real.exp (-(64 : ℝ)) := by
  have hge := inv_two_a_ge_sixty_four ha hbin
  have hx : Real.exp (-(1 : ℝ) / (2 * a)) ≤ Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg hge
  have hhalf : Real.exp (-(1 : ℝ) / (2 * a)) ≤ (1 / 2 : ℝ) :=
    hx.trans (exp_neg_sixty_four_le.trans (by norm_num))
  have hself :=
    exp_over_one_sub_le (Real.exp_pos _).le le_rfl hhalf
  have hfrac :
      Real.exp (-(1 : ℝ) / (2 * a)) /
          (1 - Real.exp (-(1 : ℝ) / (2 * a))) ≤
        2 * Real.exp (-(64 : ℝ)) :=
    hself.trans (mul_le_mul_of_nonneg_left hx (by norm_num))
  have hgeom := thetaLobe_sub_three_le_geom ha
  have : 2 * (Real.exp (-(1 : ℝ) / (2 * a)) /
      (1 - Real.exp (-(1 : ℝ) / (2 * a)))) ≤
      2 * (2 * Real.exp (-(64 : ℝ))) :=
    mul_le_mul_of_nonneg_left hfrac (by norm_num)
  have h2 : 2 * (2 * Real.exp (-(64 : ℝ))) = 4 * Real.exp (-(64 : ℝ)) := by ring
  have hgeom' : thetaLobe a - 3 ≤
      2 * (Real.exp (-(1 : ℝ) / (2 * a)) /
        (1 - Real.exp (-(1 : ℝ) / (2 * a)))) := by
    convert thetaLobe_sub_three_le_geom ha using 1
    ring
  exact hgeom'.trans (this.trans_eq h2)

lemma thetaLobe_lt_four_of_bin {a : ℝ} (ha : 0 < a)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    thetaLobe a < 4 := by
  have hle := thetaLobe_sub_three_le_four_exp ha hbin
  have hsmall : 4 * Real.exp (-(64 : ℝ)) < 1 := by
    have hmul := mul_le_mul_of_nonneg_left exp_neg_sixty_four_le
      (by norm_num : (0 : ℝ) ≤ 4)
    have hident : 4 * (1 / (2 : ℝ) ^ 64) = 4 / (2 : ℝ) ^ 64 := by ring
    exact (hmul.trans_eq hident).trans_lt (by norm_num)
  linarith [hle, hsmall]

lemma gaborHonestOnline_div_E {sigma a omega : ℝ} (ha : 0 < a) :
    gaborHonestOnlineBudget a omega gaborCInc / gaborEnhancement sigma a =
      gaborCInc / 2 *
        (thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega) *
        Real.exp (-sigma ^ 2 / (2 * a)) := by
  unfold gaborHonestOnlineBudget gaborSCert gaborEnhancement
  set B := thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hπ0 : Real.pi ≠ 0 := Real.pi_pos.ne'
  have h4 : (4 : ℝ) ≠ 0 := by norm_num
  have hexp0 : Real.exp (sigma ^ 2 / (2 * a)) ≠ 0 := (Real.exp_pos _).ne'
  have hstep :
      (2 * gaborCInc * (Real.pi / (4 * a) * B)) /
          (Real.pi / a * Real.exp (sigma ^ 2 / (2 * a))) =
        (gaborCInc / 2) * B * (1 / Real.exp (sigma ^ 2 / (2 * a))) := by
    field_simp [ha0, hπ0, h4, hexp0]
    ring
  rw [hstep, one_div]
  have hexp : (Real.exp (sigma ^ 2 / (2 * a)))⁻¹ =
      Real.exp (-sigma ^ 2 / (2 * a)) := by
    rw [← Real.exp_neg, neg_div]
  rw [hexp]

lemma online_exp_le {sigma a : ℝ} (_hs : 0 < sigma) (ha : 0 < a)
    (hsm : a ≤ gaborOnlineSmallnessA sigma) :
    Real.exp (-sigma ^ 2 / (2 * a)) ≤
      Real.exp (-256) / (gaborCInc + 1) := by
  have hC : 0 < gaborCInc := gaborCInc_pos
  have hlog : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  have hden : 0 < 2 * (Real.log (gaborCInc + 1) + 256) :=
    mul_pos (by norm_num) (add_pos_of_nonneg_of_pos hlog (by norm_num))
  have : a * (2 * (Real.log (gaborCInc + 1) + 256)) ≤ sigma ^ 2 :=
    (le_div_iff₀ hden).mp hsm
  have hfrac : Real.log (gaborCInc + 1) + 256 ≤ sigma ^ 2 / (2 * a) := by
    have : (Real.log (gaborCInc + 1) + 256) * (2 * a) ≤ sigma ^ 2 := by
      linarith
    exact (le_div_iff₀ (mul_pos (by norm_num) ha)).mpr this
  have hexp : Real.exp (-sigma ^ 2 / (2 * a)) ≤
      Real.exp (-(Real.log (gaborCInc + 1) + 256)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg hfrac
  have hident :
      Real.exp (-(Real.log (gaborCInc + 1) + 256)) =
        Real.exp (-256) / (gaborCInc + 1) := by
    rw [neg_add, Real.exp_add, Real.exp_neg,
      Real.exp_log (by linarith : (0 : ℝ) < gaborCInc + 1)]
    field_simp
  exact hexp.trans_eq hident

lemma gaborTFar_le_one_eighty {a : ℝ} (ha : 0 < a)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hfour : a ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborTFar a ≤ (1 / 70 : ℝ) := by
  rw [gaborTFar_of_small ha hfour]
  have h4a : (gaborKBin : ℝ) * (4 * a) ≤ (1 / 86 : ℝ) := by
    have ha4 : 4 * a ≤ 4 * (1 / (8 * (gaborKBin : ℝ) ^ 2)) :=
      mul_le_mul_of_nonneg_left hbin (by norm_num)
    have hK : (gaborKBin : ℝ) * (4 * a) ≤
        (gaborKBin : ℝ) * (4 * (1 / (8 * (gaborKBin : ℝ) ^ 2))) :=
      mul_le_mul_of_nonneg_left ha4 gaborKBin_pos.le
    have hident :
        (gaborKBin : ℝ) * (4 * (1 / (8 * (gaborKBin : ℝ) ^ 2))) =
          1 / (2 * (gaborKBin : ℝ)) := by
      field_simp [ne_of_gt gaborKBin_pos]
      ring
    have h86 : 1 / (2 * (gaborKBin : ℝ)) = (1 / 86 : ℝ) := by
      simp [gaborKBin]; norm_num
    exact hK.trans (hident.trans h86).le
  have htail : (gaborKBin : ℝ) * (thetaLobe a - 3) ≤ (1 / 1000 : ℝ) := by
    have hΘ := thetaLobe_sub_three_le_four_exp ha hbin
    have hmul : (gaborKBin : ℝ) * (thetaLobe a - 3) ≤
        172 * Real.exp (-(64 : ℝ)) := by
      have := mul_le_mul_of_nonneg_left hΘ gaborKBin_pos.le
      have hident : (gaborKBin : ℝ) * (4 * Real.exp (-(64 : ℝ))) =
          172 * Real.exp (-(64 : ℝ)) := by
        simp [gaborKBin]; ring
      rwa [hident] at this
    have hexp : 172 * Real.exp (-(64 : ℝ)) ≤ 172 * (1 / (2 : ℝ) ^ 64) :=
      mul_le_mul_of_nonneg_left exp_neg_sixty_four_le (by norm_num)
    have hident : 172 * (1 / (2 : ℝ) ^ 64) = 172 / (2 : ℝ) ^ 64 := by ring
    exact hmul.trans ((hexp.trans_eq hident).trans (by norm_num))
  linarith [h4a, htail,
    (by norm_num : (1 / 86 : ℝ) + (1 / 1000 : ℝ) ≤ (1 / 70 : ℝ))]

lemma mul_exp_neg_sixty_four_le (c : ℝ) (hc : 0 ≤ c) :
    c * Real.exp (-(64 : ℝ)) ≤ c / (2 : ℝ) ^ 64 := by
  have := mul_le_mul_of_nonneg_left exp_neg_sixty_four_le hc
  have hident : c * (1 / (2 : ℝ) ^ 64) = c / (2 : ℝ) ^ 64 := by ring
  rwa [hident] at this

lemma gaborTPlusLoose_le_one_hundred {a omega : ℝ}
    (ha : 0 < a) (hω : 0 < omega)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hξ : Real.exp (-omega / a) ≤ (1 / 2 : ℝ))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    gaborTPlusLoose a omega ≤ (1 / 100 : ℝ) := by
  unfold gaborTPlusLoose
  have hΘ := thetaLobe_lt_four_of_bin ha hbin
  have hden : 0 < 1 - Real.exp (-omega / a) := by
    have : Real.exp (-omega / a) < 1 := by
      rw [Real.exp_lt_one_iff]
      exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
    exact sub_pos.mpr this
  have hinv : 1 / (1 - Real.exp (-omega / a)) ≤ (2 : ℝ) := by
    have : (1 / 2 : ℝ) ≤ 1 - Real.exp (-omega / a) := by linarith [hξ]
    exact ((one_div_le_one_div hden (by norm_num : (0 : ℝ) < 1 / 2)).mpr this).trans_eq
      (by norm_num)
  have hηexp : Real.exp (-omega ^ 2 / (2 * a)) ≤ Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg h64
  have hbrack : 1 / (1 - Real.exp (-omega / a)) + 2 * thetaLobe a ≤ (10 : ℝ) := by
    nlinarith [hinv, hΘ.le]
  have hmain : (gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
        (1 / (1 - Real.exp (-omega / a)) + 2 * thetaLobe a) ≤
      430 * Real.exp (-(64 : ℝ)) := by
    have h1 := mul_le_mul_of_nonneg_left hηexp gaborKBin_pos.le
    have h2 :=
      mul_le_mul h1 hbrack (by
        have : 0 ≤ 1 / (1 - Real.exp (-omega / a)) := one_div_nonneg.mpr hden.le
        nlinarith [thetaLobe_ge_three ha, this])
        (mul_nonneg gaborKBin_pos.le (Real.exp_pos _).le)
    have hident : (gaborKBin : ℝ) * Real.exp (-(64 : ℝ)) * 10 =
        430 * Real.exp (-(64 : ℝ)) := by
      simp [gaborKBin]; ring
    rwa [hident] at h2
  have hexp : 430 * Real.exp (-(64 : ℝ)) ≤ 430 / (2 : ℝ) ^ 64 :=
    mul_exp_neg_sixty_four_le 430 (by norm_num)
  exact hmain.trans (hexp.trans (by norm_num))

lemma gaborRon_div_E_le_one_hundred {sigma a omega : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hω : 0 < omega)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hξ : Real.exp (-omega / a) < (1 / 2 : ℝ))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hon : a ≤ gaborOnlineSmallnessA sigma) :
    gaborHonestOnlineBudget a omega gaborCInc / gaborEnhancement sigma a ≤
      (1 / 100 : ℝ) := by
  rw [gaborHonestOnline_div_E ha]
  have hΘ := thetaLobe_lt_four_of_bin ha hbin
  have hΘ3 := thetaLobe_ge_three ha
  have hηexp : Real.exp (-omega ^ 2 / (2 * a)) ≤ Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg h64
  have hleft := thetaLeftPos_of_small (a := a) (omega := omega) hω hξ
  have hleft_le : thetaLeftPos a omega ≤ (1 : ℝ) := by
    rw [hleft]
    have hden : (1 / 2 : ℝ) ≤ 1 - Real.exp (-omega / a) := by linarith [hξ.le]
    have h1 :
        Real.exp (-omega ^ 2 / (2 * a)) / (1 - Real.exp (-omega / a)) ≤
          Real.exp (-(64 : ℝ)) / (1 - Real.exp (-omega / a)) :=
      div_le_div_of_nonneg_right hηexp (by linarith [hξ.le])
    have h2 :
        Real.exp (-(64 : ℝ)) / (1 - Real.exp (-omega / a)) ≤
          Real.exp (-(64 : ℝ)) / (1 / 2 : ℝ) :=
      div_le_div_of_nonneg_left (Real.exp_pos _).le (by norm_num) hden
    have h3 : Real.exp (-(64 : ℝ)) / (1 / 2 : ℝ) = 2 * Real.exp (-(64 : ℝ)) := by
      field_simp
    have hfrac := h1.trans (h2.trans_eq h3)
    have htiny : 2 * Real.exp (-(64 : ℝ)) ≤ 1 :=
      (mul_exp_neg_sixty_four_le 2 (by norm_num)).trans (by norm_num)
    exact hfrac.trans htiny
  have hcross_le : 2 * thetaCrossPos a omega ≤ (1 : ℝ) := by
    unfold thetaCrossPos
    have hident :
        2 * (Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) / 2) =
          Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) := by ring
    rw [hident]
    have hmul : Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) ≤
        Real.exp (-(64 : ℝ)) * 3 :=
      mul_le_mul hηexp (by linarith [hΘ]) (by linarith [hΘ3]) (Real.exp_pos _).le
    have htiny : 3 * Real.exp (-(64 : ℝ)) ≤ 1 :=
      (mul_exp_neg_sixty_four_le 3 (by norm_num)).trans (by norm_num)
    exact hmul.trans (by linarith [htiny])
  have hbrack : thetaLobe a + thetaLeftPos a omega +
      2 * thetaCrossPos a omega ≤ (6 : ℝ) := by
    linarith [hΘ.le, hleft_le, hcross_le]
  have hexp := online_exp_le hs ha hon
  have hC : 0 < gaborCInc := gaborCInc_pos
  have hprod :
      gaborCInc / 2 *
          (thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega) *
          Real.exp (-sigma ^ 2 / (2 * a)) ≤
        3 * Real.exp (-256) := by
    have h1 : gaborCInc / 2 *
          (thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega) ≤
        gaborCInc / 2 * 6 :=
      mul_le_mul_of_nonneg_left hbrack (div_nonneg hC.le (by norm_num))
    have h2 :=
      mul_le_mul h1 hexp (Real.exp_pos _).le
        (mul_nonneg (div_nonneg hC.le (by norm_num)) (by positivity))
    have hC1 : gaborCInc / (gaborCInc + 1) ≤ 1 :=
      (div_le_one₀ (by linarith : (0 : ℝ) < gaborCInc + 1)).mpr (by linarith)
    have hident :
        gaborCInc / 2 * 6 * (Real.exp (-256) / (gaborCInc + 1)) =
          3 * (gaborCInc / (gaborCInc + 1)) * Real.exp (-256) := by
      field_simp
      ring
    have h3' : 3 * (gaborCInc / (gaborCInc + 1)) ≤ 3 :=
      (mul_le_mul_of_nonneg_left hC1 (by norm_num : (0 : ℝ) ≤ 3)).trans_eq
        (by norm_num)
    have h3 : 3 * (gaborCInc / (gaborCInc + 1)) * Real.exp (-256) ≤
        3 * Real.exp (-256) :=
      mul_le_mul_of_nonneg_right h3' (Real.exp_pos _).le
    exact h2.trans (hident.trans_le h3)
  have h256 : Real.exp (-256) ≤ 1 / (2 : ℝ) ^ 256 :=
    exp_neg_nat_le_inv_two_pow 256
  have htiny : 3 * Real.exp (-256) ≤ 3 * (1 / (2 : ℝ) ^ 256) :=
    mul_le_mul_of_nonneg_left h256 (by norm_num)
  have hident256 : 3 * (1 / (2 : ℝ) ^ 256) = 3 / (2 : ℝ) ^ 256 := by ring
  exact hprod.trans ((htiny.trans_eq hident256).trans (by norm_num))

lemma exp_neg_omega_a_lt_half {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    Real.exp (-gaborIsolationOmega sigma gamma a / a) < (1 / 2 : ℝ) := by
  have hωa := isolationOmega_div_a_ge_sixty_four hs hg ha hωcap hγsq hbin
  have h1 : Real.exp (-gaborIsolationOmega sigma gamma a / a) ≤
      Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg hωa
  have h2 : Real.exp (-(64 : ℝ)) ≤ Real.exp (-(4 : ℝ)) :=
    Real.exp_le_exp.mpr (by norm_num)
  exact (h1.trans h2).trans_lt (gaborExp_neg_four_le.trans_lt (by norm_num))

theorem gaborRemainderBudget_holds : GaborRemainderBudget := by
  intro Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hω := isolationShrinkOfConfig_omega_pos Z hZ
  have hs := gaborHostSigma_pos Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hωcap := isolationShrinkOfConfig_le_omegaCap Z hZ
  have hγsq := isolationShrinkOfConfig_le_gamma_sq Z hZ
  have hbin := isolationShrinkOfConfig_le_binSq Z hZ
  have hon := isolationShrinkOfConfig_le_online Z hZ
  have hfour := isolationShrinkOfConfig_le_inv_four_bin Z hZ
  have hωeq : omega = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  have h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a) := by
    rw [hωeq]
    exact omega_sq_div_two_a_ge_sixty_four hs hg ha hωcap hγsq
  have hξ : Real.exp (-omega / a) ≤ (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_le_half hs hg ha hωcap hγsq hbin
  have hξlt : Real.exp (-omega / a) < (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_lt_half hs hg ha hωcap hγsq hbin
  have hTfar := gaborTFar_le_one_eighty ha hbin hfour
  have hTplus := gaborTPlusLoose_le_one_hundred ha hω h64 hξ hbin
  have hRon := gaborRon_div_E_le_one_hundred hs ha hω h64 hξlt hbin hon
  linarith [hTplus, hTfar, hRon,
    (by norm_num : (1 / 100 : ℝ) + (1 / 70 : ℝ) + (1 / 100 : ℝ) < (9 / 10 : ℝ))]

theorem gabor_dominanceAssembly_holds : GaborDominanceAssembly :=
  ⟨gaborHonestWeilLeMajorant_holds, gaborRemainderBudget_holds⟩

theorem gabor_dominanceBound_holds : GaborDominanceBound :=
  gabor_dominanceBound_of_assembly gabor_dominanceAssembly_holds

#print axioms gaborHonestWeilLeMajorant_holds
#print axioms gaborRemainderBudget_holds
#print axioms gabor_dominanceAssembly_holds
#print axioms gabor_dominanceBound_holds

end RH

