/-
RH/GaborDominanceLog.lean -- r575 counting-theorem occupancy.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

The constant `K_bin = 43` form in `GaborDominanceBound` is a
historical special case.  The counting-compatible statement is
`GaborDominanceBoundLog`: unit-bin masses may grow like
`gaborKBinAt |k| = 2 C_inner (1+log(|k|+3))`.

r575 closes `GaborLogFarPacking`, then `GaborRemainderBudgetLog`
and `GaborHonestWeilLeMajorantLog`, so `GaborDominanceBoundLog`
is a theorem.  Majorants are conservative; negativity needs
only budget < 9/10.
-/
import RH.GaborDominanceAssembly
import RH.GaborZeroSummable
import RH.ZeroIncrement
import Mathlib.Analysis.SpecificLimits.Normed

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical
open Set Finset

/-! ## Linear majorant of the counting cap -/

lemma one_add_log_le_self {x : ℝ} (hx : 1 ≤ x) :
    1 + Real.log x ≤ x := by
  have hx0 : 0 < x := lt_of_lt_of_le (by norm_num) hx
  linarith [Real.log_le_sub_one_of_pos hx0]

/-- `(1+log(γ+3))/(γ+3) ≤ 2` for `γ ≥ 0`.  The factor `1/(γ+3)`
from `online_exp_le_log` swallows the Path-A increment; the 2 is
a coarse room that also covers `(γ+5)/(γ+3)`. -/
lemma one_add_log_div_self_le_two {x : ℝ} (hx : 0 ≤ x) :
    (1 + Real.log (x + 3)) / (x + 3) ≤ (2 : ℝ) := by
  have hx1 : (1 : ℝ) ≤ x + 3 := by linarith
  have hle := one_add_log_le_self hx1
  have hden : 0 < x + 3 := by linarith
  exact ((div_le_one₀ hden).mpr hle).trans (by norm_num)

lemma add_five_div_add_three_le_two {x : ℝ} (hx : 0 ≤ x) :
    (x + 5) / (x + 3) ≤ (2 : ℝ) := by
  have hden : 0 < x + 3 := by linarith
  rw [div_le_iff₀ hden]
  linarith

lemma gaborKBinAt_le_linear (k : ℤ) :
    gaborKBinAt (|k| : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * ((|k| : ℝ) + 3) := by
  unfold gaborKBinAt
  have hx : (1 : ℝ) ≤ (|k| : ℝ) + 3 := by nlinarith [abs_nonneg (k : ℝ)]
  exact mul_le_mul_of_nonneg_left (one_add_log_le_self hx)
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le

lemma gaborKBinAt_mono {x y : ℝ} (hx : -2 ≤ x) (hxy : x ≤ y) :
    gaborKBinAt x ≤ gaborKBinAt y := by
  unfold gaborKBinAt
  have hx0 : 0 < x + 3 := by linarith
  have hlog : Real.log (x + 3) ≤ Real.log (y + 3) :=
    Real.log_le_log hx0 (by linarith [hxy])
  exact mul_le_mul_of_nonneg_left (add_le_add_right hlog 1)
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le

/-! ## Counting-theorem bridges -/

theorem zeta_unit_increment_le_gaborKBinAt {T : ℝ}
    (hT : Real.exp 1 ≤ T) :
    ((gaborZeroCount (T + 1) - gaborZeroCount T : ℕ) : ℝ) ≤
      gaborKBinAt T := by
  have hmono := gaborZerosUpTo_mono (T := T) (U := T + 1) (by linarith)
  have hdiff :
      gaborZeroCount (T + 1) - gaborZeroCount T =
        (gaborZerosUpTo (T + 1) \ gaborZerosUpTo T).card := by
    rw [gaborZeroCount_eq_card, gaborZeroCount_eq_card,
      Finset.card_sdiff, Finset.inter_eq_left.mpr hmono]
  rw [hdiff]
  have hcard := Finset.card_le_card (gaborZerosUpTo_sdiff_subset_unit T)
  have hwindow := card_window_zeros_unit_le T
    (le_trans (by norm_num : (1 : ℝ) ≤ Real.exp 1) hT)
  have hcast :
      (((gaborZerosUpTo (T + 1) \ gaborZerosUpTo T).card : ℕ) : ℝ) ≤
        (((riemannZetaZerosOnClosedRect 0 1 (T + 1)).filter
          (fun z => T ≤ z.im ∧ z.im ≤ T + 1)).card : ℝ) :=
    Nat.cast_le.mpr hcard
  have harg : 2 + T + 1 = T + 3 := by ring
  rw [harg] at hwindow
  simpa [gaborKBinAt] using hcast.trans hwindow

theorem stripZerosWindow_card_le_gaborKBinAt (k : ℤ) :
    ((stripZerosWindow (k : ℝ)).card : ℝ) ≤ gaborKBinAt (|k| : ℝ) := by
  simpa [gaborKBinAt, gaborBinCountMajorant] using
    card_strip_window_le (k : ℝ)

theorem incrementCompliantLog_of_le_strip
    (Z : GaborCanonicalConfig)
    (h : ∀ k : ℤ,
      (Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)).sum
        (fun q => (Z.mult q : ℝ)) ≤
          ((stripZerosWindow (k : ℝ)).card : ℝ)) :
    GaborConfigIncrementCompliantLog Z := by
  intro k
  exact (h k).trans (stripZerosWindow_card_le_gaborKBinAt k)

/-! ## Arithmetico-geometric series -/

lemma abs_floor_le_abs_add_one (x : ℝ) :
    (|Int.floor x| : ℝ) ≤ |x| + 1 := by
  have hle : (Int.floor x : ℝ) ≤ x := Int.floor_le x
  have hgt : x - 1 < (Int.floor x : ℝ) :=
    sub_lt_iff_lt_add.mpr (Int.lt_floor_add_one x)
  exact abs_le.mpr ⟨le_of_lt (by linarith [hgt, neg_le_abs x]),
    by linarith [le_abs_self x]⟩

lemma real_norm_lt_one_of_mem_Ico {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1) :
    ‖r‖ < 1 := by
  rwa [Real.norm_eq_abs, abs_of_nonneg hr0]

lemma summable_add_const_mul_geometric {r C : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) :
    Summable fun n : ℕ => ((n : ℝ) + C) * r ^ n := by
  have hnorm : ‖r‖ < 1 := real_norm_lt_one_of_mem_Ico hr0 hr1
  refine (((hasSum_coe_mul_geometric_of_norm_lt_one hnorm).summable).add
    ((summable_geometric_of_lt_one hr0 hr1).mul_left C)).congr fun n => ?_
  ring

lemma tsum_add_const_mul_geometric {r C : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) :
    ∑' n : ℕ, ((n : ℝ) + C) * r ^ n =
      C / (1 - r) + r / (1 - r) ^ 2 := by
  have hnorm : ‖r‖ < 1 := real_norm_lt_one_of_mem_Ico hr0 hr1
  have hn : ∑' n : ℕ, (n : ℝ) * r ^ n = r / (1 - r) ^ 2 :=
    tsum_coe_mul_geometric_of_norm_lt_one hnorm
  have h1 : ∑' n : ℕ, r ^ n = 1 / (1 - r) := by
    simpa [one_div] using tsum_geometric_of_lt_one hr0 hr1
  have hsm₁ := (hasSum_coe_mul_geometric_of_norm_lt_one hnorm).summable
  have hsm₂ := summable_geometric_of_lt_one hr0 hr1
  have hsplit :
      ∑' n : ℕ, ((n : ℝ) + C) * r ^ n =
        ∑' n : ℕ, (n : ℝ) * r ^ n + C * ∑' n : ℕ, r ^ n := by
    have hcongr :
        (fun n : ℕ => ((n : ℝ) + C) * r ^ n) =
          (fun n : ℕ => (n : ℝ) * r ^ n + C * r ^ n) := by
      funext n; ring
    rw [hcongr, hsm₁.tsum_add (hsm₂.mul_left _), tsum_mul_left]
  rw [hsplit, hn, h1]
  field_simp
  ring

lemma tsum_add_three_mul_geometric {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1) :
    ∑' n : ℕ, ((n : ℝ) + 3) * r ^ n = gaborArithGeomMajorant r := by
  simpa [gaborArithGeomMajorant] using tsum_add_const_mul_geometric hr0 hr1

lemma gaborArithGeomMajorant_le_eight {r : ℝ}
    (_hr0 : 0 ≤ r) (hr : r ≤ (1 / 2 : ℝ)) :
    gaborArithGeomMajorant r ≤ (8 : ℝ) := by
  have hr1 : r < 1 := lt_of_le_of_lt hr (by norm_num)
  have hden : (1 / 2 : ℝ) ≤ 1 - r := by linarith
  have hden0 : 0 < 1 - r := sub_pos.mpr hr1
  have h3 : 3 / (1 - r) ≤ (6 : ℝ) := by
    rw [div_le_iff₀ hden0, show (6 : ℝ) * (1 - r) = 6 - 6 * r by ring]
    linarith [hr]
  have hsq : r / (1 - r) ^ 2 ≤ (2 : ℝ) := by
    rw [div_le_iff₀ (sq_pos_of_pos hden0)]
    nlinarith [hr, hden]
  unfold gaborArithGeomMajorant
  linarith [h3, hsq]

/-! ## Weighted fiber packing (finite sums) -/

lemma increment_fiber_le_log (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z) (k : ℤ)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    (S.filter (fun q => ordinateBin q.2 = k)).sum
        (fun q => (Z.mult q : ℝ)) ≤ gaborKBinAt (|k| : ℝ) := by
  have hsub :
      S.filter (fun q => ordinateBin q.2 = k) ⊆
        Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1) := by
    intro q hq
    have hqS := (mem_filter.mp hq).1
    have hbin : ordinateBin q.2 = k := (mem_filter.mp hq).2
    have hm := mem_ordinateBin q.2
    exact mem_filter.mpr ⟨hS hqS, by simpa [hbin] using hm⟩
  exact (sum_le_sum_of_subset_of_nonneg hsub
      (fun _ _ _ => Nat.cast_nonneg _)).trans (hinc k)

theorem bin_partial_summation_mult_log
    {w : ℝ → ℝ} (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts)
    {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k)
    (hM : ∀ q ∈ S, w q.2 ≤ M (ordinateBin q.2)) :
    S.sum (fun q => (Z.mult q : ℝ) * w q.2) ≤
      ∑ k ∈ S.image (fun q => ordinateBin q.2),
        gaborKBinAt (|k| : ℝ) * M k := by
  have hpt : S.sum (fun q => (Z.mult q : ℝ) * w q.2) ≤
      S.sum (fun q => (Z.mult q : ℝ) * M (ordinateBin q.2)) :=
    sum_le_sum fun q hq =>
      mul_le_mul_of_nonneg_left (hM q hq) (Nat.cast_nonneg _)
  let g : ℝ × ℝ → ℤ := fun q => ordinateBin q.2
  have hfib := sum_fiber_weight S Z.mult g M
  have hsum₂ :
      S.sum (fun q => (Z.mult q : ℝ) * M (g q)) ≤
        ∑ k ∈ S.image g, gaborKBinAt (|k| : ℝ) * M k := by
    rw [hfib]
    refine sum_le_sum fun k _hk => ?_
    exact mul_le_mul_of_nonneg_right
      (increment_fiber_le_log Z hinc k S hS) (hM0 k)
  exact hpt.trans (by simpa [g] using hsum₂)

lemma lin_pack_sum {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k) (K : Finset ℤ) :
    ∑ k ∈ K, gaborKBinAt (|k| : ℝ) * M k ≤
      (2 * zetaZerosInDiskCardBoundInner) *
        ∑ k ∈ K, ((|k| : ℝ) + 3) * M k := by
  have hpt : ∀ k ∈ K,
      gaborKBinAt (|k| : ℝ) * M k ≤
        (2 * zetaZerosInDiskCardBoundInner) * ((|k| : ℝ) + 3) * M k :=
    fun k _ => mul_le_mul_of_nonneg_right (gaborKBinAt_le_linear k) (hM0 k)
  refine (sum_le_sum hpt).trans_eq ?_
  simp [mul_sum, mul_assoc]

/-! ## Plus packing -/

lemma plus_weighted_tsum_le {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega) :
    ∑' n : ℕ, ((n : ℝ) + 3) *
        Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) ≤
      Real.exp (-omega ^ 2 / (2 * a)) *
        gaborArithGeomMajorant (Real.exp (-omega / a)) := by
  have hξ0 : 0 ≤ Real.exp (-omega / a) := (Real.exp_pos _).le
  have hξ1 : Real.exp (-omega / a) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
  have hterm : ∀ n : ℕ,
      ((n : ℝ) + 3) * Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) ≤
        Real.exp (-omega ^ 2 / (2 * a)) *
          (((n : ℝ) + 3) * (Real.exp (-omega / a)) ^ n) :=
    fun n => by
      have := gaborPlusBin_geom ha hω n
      nlinarith [this, add_nonneg (Nat.cast_nonneg n) (by norm_num : (0 : ℝ) ≤ 3)]
  have hsmR :=
    (summable_add_const_mul_geometric (C := (3 : ℝ)) hξ0 hξ1).mul_left
      (Real.exp (-omega ^ 2 / (2 * a)))
  have hsmL :
      Summable fun n : ℕ =>
        ((n : ℝ) + 3) * Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) :=
    Summable.of_nonneg_of_le (fun _ => by positivity)
      (fun n => (hterm n).trans (le_of_eq (by ring))) hsmR
  have hle := Summable.tsum_le_tsum
    (fun n => (hterm n).trans (le_of_eq (by ring))) hsmL hsmR
  refine hle.trans_eq ?_
  rw [tsum_mul_left, tsum_add_three_mul_geometric hξ0 hξ1]

theorem gabor_plus_amp_pack_log
    {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliantLog Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    S.sum (fun q => (Z.mult q : ℝ) *
        Real.exp (-(q.2 + omega) ^ 2 / (2 * a))) ≤
      (2 * zetaZerosInDiskCardBoundInner) *
        Real.exp (-omega ^ 2 / (2 * a)) *
          gaborArithGeomMajorant (Real.exp (-omega / a)) := by
  let M : ℤ → ℝ := fun k =>
    Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a))
  have hM0 : ∀ k, 0 ≤ M k := fun _ => (Real.exp_pos _).le
  have hM : ∀ q ∈ S,
      Real.exp (-(q.2 + omega) ^ 2 / (2 * a)) ≤ M (ordinateBin q.2) :=
    fun q hq => plus_gauss_mono_bin ha hω (Z.gamma_pos q (hS hq))
  have hpack :=
    bin_partial_summation_mult_log (w := fun t =>
      Real.exp (-(t + omega) ^ 2 / (2 * a))) Z hinc S hS hM0 hM
  refine hpack.trans ?_
  set K := S.image (fun q => ordinateBin q.2)
  have hlin := lin_pack_sum (M := M) hM0 K
  have hnn : ∀ k ∈ K, 0 ≤ k := fun k hk => by
    obtain ⟨q, hq, rfl⟩ := mem_image.mp hk
    exact ordinateBin_nonneg_of_pos (Z.gamma_pos q (hS hq))
  have hnat :
      ∑ k ∈ K, ((|k| : ℝ) + 3) * M k ≤
        ∑' n : ℕ, ((n : ℝ) + 3) *
          Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) := by
    let φ : ℤ → ℕ := fun k => k.toNat
    have hKp : K.filter (fun k => 0 ≤ k) = K := by
      ext k; constructor
      · exact fun hk => (mem_filter.mp hk).1
      · intro hk; exact mem_filter.mpr ⟨hk, hnn k hk⟩
    have hinj : ∀ k₁ ∈ K, ∀ k₂ ∈ K, φ k₁ = φ k₂ → k₁ = k₂ := by
      intro k₁ hk₁ k₂ hk₂ h
      have h1 := hnn k₁ hk₁
      have h2 := hnn k₂ hk₂
      have : (k₁.toNat : ℤ) = (k₂.toNat : ℤ) := by exact_mod_cast h
      rw [Int.toNat_of_nonneg h1, Int.toNat_of_nonneg h2] at this
      exact this
    have himage :
        ∑ k ∈ K, ((|k| : ℝ) + 3) * M k =
          ∑ n ∈ K.image φ, ((n : ℝ) + 3) *
            Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) := by
      rw [sum_image hinj]
      refine sum_congr rfl fun k hk => ?_
      have habs : (|k| : ℝ) = (k : ℝ) :=
        abs_of_nonneg (by exact_mod_cast hnn k hk)
      have hφ : (k : ℝ) = (φ k : ℝ) := by
        exact_mod_cast (Int.toNat_of_nonneg (hnn k hk)).symm
      simp [M, habs, hφ]
    have hξ0 : 0 ≤ Real.exp (-omega / a) := (Real.exp_pos _).le
    have hξ1 : Real.exp (-omega / a) < 1 := by
      rw [Real.exp_lt_one_iff]
      exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
    have hsmR :=
      (summable_add_const_mul_geometric (C := (3 : ℝ)) hξ0 hξ1).mul_left
        (Real.exp (-omega ^ 2 / (2 * a)))
    have hsm : Summable fun n : ℕ =>
        ((n : ℝ) + 3) * Real.exp (-((n : ℝ) + omega) ^ 2 / (2 * a)) :=
      Summable.of_nonneg_of_le (fun _ => by positivity)
        (fun n => mul_le_mul_of_nonneg_left (gaborPlusBin_geom ha hω n)
          (by positivity))
        (hsmR.congr fun n => by ring)
    rw [himage]
    exact hsm.sum_le_tsum _ (fun _ _ => by positivity)
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hplus := plus_weighted_tsum_le ha hω
  have hassoc :
      (2 * zetaZerosInDiskCardBoundInner) *
          (Real.exp (-omega ^ 2 / (2 * a)) *
            gaborArithGeomMajorant (Real.exp (-omega / a))) =
        (2 * zetaZerosInDiskCardBoundInner) *
          Real.exp (-omega ^ 2 / (2 * a)) *
            gaborArithGeomMajorant (Real.exp (-omega / a)) := by
    ring
  exact (hlin.trans (mul_le_mul_of_nonneg_left hnat hC0)).trans
    ((mul_le_mul_of_nonneg_left hplus hC0).trans_eq hassoc)

/-! ## Far-tail series -/

lemma exp_neg_succ_geom {a : ℝ} (ha : 0 < a) (n : ℕ) :
    Real.exp (-((n + 1 : ℕ) : ℝ) / (2 * a)) =
      Real.exp (-(1 : ℝ) / (2 * a)) *
        (Real.exp (-(1 : ℝ) / (2 * a))) ^ n := by
  have hn : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by exact_mod_cast rfl
  have : -((n + 1 : ℕ) : ℝ) / (2 * a) =
      (n : ℝ) * (-(1 : ℝ) / (2 * a)) + (-(1 : ℝ) / (2 * a)) := by
    rw [hn]
    field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]
    ring
  rw [this, Real.exp_add, Real.exp_nat_mul, mul_comm]

lemma gaborFarTailLog_summable {a omega : ℝ} (ha : 0 < a) :
    Summable fun n : ℕ =>
      ((n : ℝ) + |omega| + 8) *
        Real.exp (-((n + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  have hξ0 : 0 ≤ Real.exp (-(1 : ℝ) / (2 * a)) := (Real.exp_pos _).le
  have hξ1 : Real.exp (-(1 : ℝ) / (2 * a)) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (by norm_num) (mul_pos (by norm_num) ha)
  have hsm :=
    (summable_add_const_mul_geometric (C := |omega| + 8) hξ0 hξ1).mul_left
      (Real.exp (-(1 : ℝ) / (2 * a)))
  refine Summable.of_nonneg_of_le (fun _ => by positivity)
    (fun n => mul_le_mul_of_nonneg_left (gauss_theta_term_le_geom ha n)
      (by positivity)) (hsm.congr fun n => ?_)
  have hexp := exp_neg_succ_geom ha n
  calc
    Real.exp (-(1 : ℝ) / (2 * a)) *
          (((n : ℝ) + (|omega| + 8)) *
            (Real.exp (-(1 : ℝ) / (2 * a))) ^ n)
        = ((n : ℝ) + |omega| + 8) *
            (Real.exp (-(1 : ℝ) / (2 * a)) *
              (Real.exp (-(1 : ℝ) / (2 * a))) ^ n) := by
      ring
    _ = ((n : ℝ) + |omega| + 8) *
          Real.exp (-((n + 1 : ℕ) : ℝ) / (2 * a)) := by
      rw [← hexp]

/-- Linear prefactor is monotone in `|ω|`; used to cap
`θ_log(2, ω(a))` by the host ordinate as `ω(a)` retunes. -/
lemma gaborFarTailLog_mono_abs {a omega omega' : ℝ} (ha : 0 < a)
    (hle : |omega| ≤ |omega'|) :
    gaborFarTailLog a omega ≤ gaborFarTailLog a omega' := by
  have hsm := gaborFarTailLog_summable (a := a) (omega := omega) ha
  have hsm' := gaborFarTailLog_summable (a := a) (omega := omega') ha
  refine Summable.tsum_le_tsum ?_ hsm hsm'
  intro n
  have hlin : (n : ℝ) + |omega| + 8 ≤ (n : ℝ) + |omega'| + 8 := by
    linarith [hle]
  exact mul_le_mul_of_nonneg_right hlin (Real.exp_pos _).le

lemma gaborFarTailLog_le_geom {a omega : ℝ} (ha : 0 < a)
    (hξ : Real.exp (-(1 : ℝ) / (2 * a)) ≤ (1 / 2 : ℝ)) :
    gaborFarTailLog a omega ≤
      2 * Real.exp (-(1 : ℝ) / (2 * a)) * (|omega| + 9) := by
  set ξ := Real.exp (-(1 : ℝ) / (2 * a))
  have hξ0 : 0 ≤ ξ := (Real.exp_pos _).le
  have hξ1 : ξ < 1 := lt_of_le_of_lt hξ (by norm_num)
  have hterm : ∀ n : ℕ,
      ((n : ℝ) + |omega| + 8) *
          Real.exp (-((n + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) ≤
        ξ * (((n : ℝ) + (|omega| + 8)) * ξ ^ n) := by
    intro n
    have hgeom := gauss_theta_term_le_geom ha n
    have hexp : Real.exp (-((n + 1 : ℕ) : ℝ) / (2 * a)) = ξ * ξ ^ n := by
      simpa [ξ] using exp_neg_succ_geom ha n
    calc
      ((n : ℝ) + |omega| + 8) *
            Real.exp (-((n + 1 : ℕ) : ℝ) ^ 2 / (2 * a))
          ≤ ((n : ℝ) + |omega| + 8) *
              Real.exp (-((n + 1 : ℕ) : ℝ) / (2 * a)) :=
        mul_le_mul_of_nonneg_left hgeom (by positivity)
      _ = ((n : ℝ) + |omega| + 8) * (ξ * ξ ^ n) := by rw [hexp]
      _ = ξ * (((n : ℝ) + (|omega| + 8)) * ξ ^ n) := by ring
  have hsmR := (summable_add_const_mul_geometric (C := |omega| + 8)
    hξ0 hξ1).mul_left ξ
  have hsmL := gaborFarTailLog_summable (a := a) (omega := omega) ha
  have hle := Summable.tsum_le_tsum hterm hsmL hsmR
  have heq := tsum_add_const_mul_geometric (C := |omega| + 8) hξ0 hξ1
  have hden : (1 / 2 : ℝ) ≤ 1 - ξ := by linarith [hξ]
  have hden0 : 0 < 1 - ξ := sub_pos.mpr hξ1
  have hbrack :
      (|omega| + 8) / (1 - ξ) + ξ / (1 - ξ) ^ 2 ≤ 2 * (|omega| + 9) := by
    have h1 : (|omega| + 8) / (1 - ξ) ≤ 2 * (|omega| + 8) := by
      rw [div_le_iff₀ hden0]
      nlinarith [hden, abs_nonneg omega]
    have h2 : ξ / (1 - ξ) ^ 2 ≤ (2 : ℝ) := by
      rw [div_le_iff₀ (sq_pos_of_pos hden0)]
      nlinarith [hξ, hden]
    linarith [h1, h2, abs_nonneg omega]
  unfold gaborFarTailLog
  have hts :
      ∑' n : ℕ, ξ * (((n : ℝ) + (|omega| + 8)) * ξ ^ n) =
        ξ * ((|omega| + 8) / (1 - ξ) + ξ / (1 - ξ) ^ 2) := by
    rw [tsum_mul_left, heq]
  have hmid := hle.trans_eq hts
  have hfin := mul_le_mul_of_nonneg_left hbrack hξ0
  have hident : ξ * (2 * (|omega| + 9)) = 2 * ξ * (|omega| + 9) := by ring
  exact hmid.trans (hfin.trans_eq hident)

lemma abs_mem_central3 (n k : ℤ)
    (hk : k ∈ ({n - 1, n, n + 1} : Finset ℤ)) :
    |k| ≤ |n| + 1 := by
  have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa using hk
  rcases this with h | h | h
  · subst h
    have hle : |n + (-1)| ≤ |n| + |(-1 : ℤ)| := abs_add_le n (-1)
    simpa using hle
  · subst h; exact le_add_of_nonneg_right (by norm_num)
  · subst h
    have hle : |n + 1| ≤ |n| + |(1 : ℤ)| := abs_add_le n 1
    simpa using hle

lemma far_right_weight_le {n k : ℤ} {omega : ℝ}
    (hn : n = Int.floor omega) (hk : n + 2 ≤ k) :
    (|k| : ℝ) + 3 ≤ ((k - n - 2).toNat : ℝ) + |omega| + 8 := by
  have hnn : 0 ≤ k - n - 2 := by omega
  have hto : ((k - n - 2).toNat : ℤ) = k - n - 2 := Int.toNat_of_nonneg hnn
  have hkn : |(k : ℝ)| ≤ |(k : ℝ) - (n : ℝ)| + |(n : ℝ)| := by
    simpa using abs_add_le ((k : ℝ) - (n : ℝ)) (n : ℝ)
  have hkn0 : |(k : ℝ) - (n : ℝ)| = (k : ℝ) - (n : ℝ) :=
    abs_of_nonneg (by exact_mod_cast (by omega : (0 : ℤ) ≤ k - n))
  have hnabs := abs_floor_le_abs_add_one omega
  rw [← hn] at hnabs
  have hmR : ((k - n - 2).toNat : ℝ) = (k : ℝ) - (n : ℝ) - 2 := by
    exact_mod_cast hto
  linarith [hkn, hkn0, hnabs, hmR]

lemma far_left_weight_le {n k : ℤ} {omega : ℝ}
    (hn : n = Int.floor omega) (hk : k ≤ n - 2) :
    (|k| : ℝ) + 3 ≤ ((n - 2 - k).toNat : ℝ) + |omega| + 8 := by
  have hnn : 0 ≤ n - 2 - k := by omega
  have hto : ((n - 2 - k).toNat : ℤ) = n - 2 - k := Int.toNat_of_nonneg hnn
  have hkn : |(k : ℝ)| ≤ |(k : ℝ) - (n : ℝ)| + |(n : ℝ)| := by
    simpa using abs_add_le ((k : ℝ) - (n : ℝ)) (n : ℝ)
  have hkn0 : |(k : ℝ) - (n : ℝ)| = (n : ℝ) - (k : ℝ) := by
    have : (k : ℝ) - (n : ℝ) ≤ 0 := by
      exact_mod_cast (by omega : k - n ≤ (0 : ℤ))
    rw [abs_of_nonpos this]; ring
  have hnabs := abs_floor_le_abs_add_one omega
  rw [← hn] at hnabs
  have hmR : ((n - 2 - k).toNat : ℝ) = (n : ℝ) - 2 - (k : ℝ) := by
    exact_mod_cast hto
  linarith [hkn, hkn0, hnabs, hmR]

lemma weighted_far_right_le {a omega : ℝ} (ha : 0 < a) (n : ℤ)
    (hn : n = Int.floor omega) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => n + 2 ≤ k),
        ((|k| : ℝ) + 3) *
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      gaborFarTailLog a omega := by
  set Kr := K.filter (fun k => n + 2 ≤ k)
  let φ : ℤ → ℕ := fun k => Int.toNat (k - n - 2)
  have hφ : ∀ k ∈ Kr, ((k - n - 1 : ℤ) : ℝ) = ((φ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have hk' : n + 2 ≤ k := (mem_filter.mp hk).2
    have hnn : 0 ≤ k - n - 2 := by omega
    have hto : ((k - n - 2).toNat : ℤ) = k - n - 2 := Int.toNat_of_nonneg hnn
    have h1 : (k - n - 1 : ℤ) = (k - n - 2) + 1 := by ring
    have h2 : ((φ k + 1 : ℕ) : ℤ) = (k - n - 2) + 1 := by
      unfold φ; rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]; exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kr, ∀ k₂ ∈ Kr, φ k₁ = φ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hφeq
    have h1 : 0 ≤ k₁ - n - 2 := by
      have : n + 2 ≤ k₁ := (mem_filter.mp hk₁).2; omega
    have h2 : 0 ≤ k₂ - n - 2 := by
      have : n + 2 ≤ k₂ := (mem_filter.mp hk₂).2; omega
    have : k₁ - n - 2 = k₂ - n - 2 := by
      calc
        k₁ - n - 2 = ((k₁ - n - 2).toNat : ℤ) := (Int.toNat_of_nonneg h1).symm
        _ = ((k₂ - n - 2).toNat : ℤ) := by exact_mod_cast hφeq
        _ = k₂ - n - 2 := Int.toNat_of_nonneg h2
    omega
  have hsm := gaborFarTailLog_summable (a := a) (omega := omega) ha
  have himage :
      ∑ k ∈ Kr, ((|k| : ℝ) + 3) *
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
        ∑ m ∈ Kr.image φ, ((m : ℝ) + |omega| + 8) *
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have hpt : ∀ k ∈ Kr,
        ((|k| : ℝ) + 3) *
            Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
          ((φ k : ℝ) + |omega| + 8) *
            Real.exp (-((φ k + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
      intro k hk
      rw [hφ k hk]
      exact mul_le_mul_of_nonneg_right
        (far_right_weight_le hn (mem_filter.mp hk).2) (Real.exp_pos _).le
    have hsum := sum_le_sum hpt
    let f : ℕ → ℝ := fun m =>
      ((m : ℝ) + |omega| + 8) *
        Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a))
    have heq : ∑ k ∈ Kr, f (φ k) = ∑ m ∈ Kr.image φ, f m :=
      (sum_image hinj).symm
    exact hsum.trans_eq heq
  exact himage.trans (hsm.sum_le_tsum _ (fun _ _ => by positivity))

lemma weighted_far_left_le {a omega : ℝ} (ha : 0 < a) (n : ℤ)
    (hn : n = Int.floor omega) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k ≤ n - 2),
        ((|k| : ℝ) + 3) *
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      gaborFarTailLog a omega := by
  set Kl := K.filter (fun k => k ≤ n - 2)
  let ψ : ℤ → ℕ := fun k => Int.toNat (n - 2 - k)
  have hψ : ∀ k ∈ Kl, ((n - 1 - k : ℤ) : ℝ) = ((ψ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have hk' : k ≤ n - 2 := (mem_filter.mp hk).2
    have hnn : 0 ≤ n - 2 - k := by omega
    have hto : ((n - 2 - k).toNat : ℤ) = n - 2 - k := Int.toNat_of_nonneg hnn
    have h1 : (n - 1 - k : ℤ) = (n - 2 - k) + 1 := by ring
    have h2 : ((ψ k + 1 : ℕ) : ℤ) = (n - 2 - k) + 1 := by
      unfold ψ; rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]; exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kl, ∀ k₂ ∈ Kl, ψ k₁ = ψ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hψeq
    have h1 : 0 ≤ n - 2 - k₁ := by
      have : k₁ ≤ n - 2 := (mem_filter.mp hk₁).2; omega
    have h2 : 0 ≤ n - 2 - k₂ := by
      have : k₂ ≤ n - 2 := (mem_filter.mp hk₂).2; omega
    have : n - 2 - k₁ = n - 2 - k₂ := by
      calc
        n - 2 - k₁ = ((n - 2 - k₁).toNat : ℤ) := (Int.toNat_of_nonneg h1).symm
        _ = ((n - 2 - k₂).toNat : ℤ) := by exact_mod_cast hψeq
        _ = n - 2 - k₂ := Int.toNat_of_nonneg h2
    omega
  have hsm := gaborFarTailLog_summable (a := a) (omega := omega) ha
  have himage :
      ∑ k ∈ Kl, ((|k| : ℝ) + 3) *
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
        ∑ m ∈ Kl.image ψ, ((m : ℝ) + |omega| + 8) *
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have hpt : ∀ k ∈ Kl,
        ((|k| : ℝ) + 3) *
            Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
          ((ψ k : ℝ) + |omega| + 8) *
            Real.exp (-((ψ k + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
      intro k hk
      rw [hψ k hk]
      exact mul_le_mul_of_nonneg_right
        (far_left_weight_le hn (mem_filter.mp hk).2) (Real.exp_pos _).le
    have hsum := sum_le_sum hpt
    let f : ℕ → ℝ := fun m =>
      ((m : ℝ) + |omega| + 8) *
        Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a))
    have heq : ∑ k ∈ Kl, f (ψ k) = ∑ m ∈ Kl.image ψ, f m :=
      (sum_image hinj).symm
    exact hsum.trans_eq heq
  exact himage.trans (hsm.sum_le_tsum _ (fun _ _ => by positivity))

lemma weighted_far_bins_le {a omega : ℝ} (ha : 0 < a) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k =>
        k ≤ Int.floor omega - 2 ∨ Int.floor omega + 2 ≤ k),
        ((|k| : ℝ) + 3) * gaussBinMax a omega k ≤
      2 * gaborFarTailLog a omega := by
  set n := Int.floor omega
  have hdisj :
      (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)).sum
          (fun k => ((|k| : ℝ) + 3) * gaussBinMax a omega k) ≤
        (K.filter (fun k => n + 2 ≤ k)).sum
            (fun k => ((|k| : ℝ) + 3) *
              Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a))) +
          (K.filter (fun k => k ≤ n - 2)).sum
            (fun k => ((|k| : ℝ) + 3) *
              Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a))) := by
    have hpt : ∀ k ∈ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
        ((|k| : ℝ) + 3) * gaussBinMax a omega k ≤
          (if n + 2 ≤ k then
              ((|k| : ℝ) + 3) *
                Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
            (if k ≤ n - 2 then
                ((|k| : ℝ) + 3) *
                  Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) := by
      intro k hk
      have hor : k ≤ n - 2 ∨ n + 2 ≤ k := (mem_filter.mp hk).2
      rcases hor with hl | hr
      · have hr' : ¬ n + 2 ≤ k := by omega
        have hle := gaussBinMax_le_left (a := a) (c := omega) ha (n := n) rfl hl
        have hcast : ((n - 1 - k : ℤ) : ℝ) = (n : ℝ) - 1 - (k : ℝ) := by
          rw [Int.cast_sub, Int.cast_sub, Int.cast_one]
        rw [hcast] at hle
        simp [hr', hl]
        exact mul_le_mul_of_nonneg_left hle (by positivity)
      · have hl' : ¬ k ≤ n - 2 := by omega
        have hle := gaussBinMax_le_right (a := a) (c := omega) ha (n := n) rfl hr
        have hcast : ((k - n - 1 : ℤ) : ℝ) = (k : ℝ) - (n : ℝ) - 1 := by
          rw [Int.cast_sub, Int.cast_sub, Int.cast_one]
        rw [hcast] at hle
        simp [hr, hl']
        exact mul_le_mul_of_nonneg_left hle (by positivity)
    have := sum_le_sum hpt
    rw [sum_add_distrib] at this
    have hr :
        ∑ k ∈ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
            (if n + 2 ≤ k then
                ((|k| : ℝ) + 3) *
                  Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
          ∑ k ∈ K.filter (fun k => n + 2 ≤ k),
            ((|k| : ℝ) + 3) *
              Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) := by
      have hsub :
          (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)).filter
              (fun k => n + 2 ≤ k) ⊆ K.filter (fun k => n + 2 ≤ k) := by
        intro k hk
        exact mem_filter.mpr ⟨(mem_filter.mp (mem_filter.mp hk).1).1,
          (mem_filter.mp hk).2⟩
      have hite :=
        (Finset.sum_filter (s := K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k))
          (p := fun k => n + 2 ≤ k)
          (f := fun k => ((|k| : ℝ) + 3) *
            Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
      rw [hite]
      exact sum_le_sum_of_subset_of_nonneg hsub (fun _ _ _ => by positivity)
    have hl :
        ∑ k ∈ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
            (if k ≤ n - 2 then
                ((|k| : ℝ) + 3) *
                  Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
          ∑ k ∈ K.filter (fun k => k ≤ n - 2),
            ((|k| : ℝ) + 3) *
              Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) := by
      have hsub :
          (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)).filter
              (fun k => k ≤ n - 2) ⊆ K.filter (fun k => k ≤ n - 2) := by
        intro k hk
        exact mem_filter.mpr ⟨(mem_filter.mp (mem_filter.mp hk).1).1,
          (mem_filter.mp hk).2⟩
      have hite :=
        (Finset.sum_filter (s := K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k))
          (p := fun k => k ≤ n - 2)
          (f := fun k => ((|k| : ℝ) + 3) *
            Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
      rw [hite]
      exact sum_le_sum_of_subset_of_nonneg hsub (fun _ _ _ => by positivity)
    linarith [this, hr, hl]
  linarith [hdisj, weighted_far_right_le ha n rfl K,
    weighted_far_left_le ha n rfl K]

/-! ## Far minus-lobe packing -/

/-- Far minus-lobe at every height against `gaborTFarLog`.
The isolation radius is the window: foreign ordinates satisfy
`ε_iso < |γ−ω|` after shrink, matching the central cap. -/
def GaborLogFarPacking : Prop :=
  ∀ {a omega : ℝ} (_ha : 0 < a)
      (Z : GaborCanonicalConfig) (_hinc : GaborConfigIncrementCompliantLog Z)
      (S : Finset (ℝ × ℝ)) (_hS : S ⊆ Z.pts)
      (_hout : ∀ q ∈ S, gaborIsolationEpsilon a < |q.2 - omega|),
    S.sum (fun q => (Z.mult q : ℝ) * gaussWeight a omega q.2) ≤
      gaborTFarLog a omega


theorem gabor_far_minus_pack_log
    {a omega : ℝ} (ha : 0 < a)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliantLog Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts)
    (hout : ∀ q ∈ S, gaborIsolationEpsilon a < |q.2 - omega|) :
    S.sum (fun q => (Z.mult q : ℝ) * gaussWeight a omega q.2) ≤
      gaborTFarLog a omega := by
  set ε := gaborIsolationEpsilon a
  have hε : 0 ≤ ε := Real.sqrt_nonneg _
  let n := Int.floor omega
  let central : Finset ℤ := {n - 1, n, n + 1}
  let M : ℤ → ℝ := fun k =>
    if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a omega k
    else Real.exp (-ε ^ 2 / (2 * a))
  have hM0 : ∀ k, 0 ≤ M k := by
    intro k; unfold M; split_ifs
    · exact gaussBinMax_nonneg ha k
    · exact (Real.exp_pos _).le
  have hM : ∀ q ∈ S, gaussWeight a omega q.2 ≤ M (ordinateBin q.2) := by
    intro q hq
    simpa [M, ε] using far_minus_majorant ha hε (hout q hq)
  have hpack :=
    bin_partial_summation_mult_log (w := gaussWeight a omega) Z hinc S hS hM0 hM
  refine hpack.trans ?_
  set K := S.image (fun q => ordinateBin q.2)
  have hlin := lin_pack_sum (M := M) hM0 K
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hKfar :
      ∑ k ∈ K, ((|k| : ℝ) + 3) * M k ≤
        4 * ((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a)) +
          2 * gaborFarTailLog a omega := by
    have hpt : ∀ k ∈ K,
        ((|k| : ℝ) + 3) * M k ≤
          (if k ∈ central then ((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a))
            else 0) +
            (if k ≤ n - 2 ∨ n + 2 ≤ k then
                ((|k| : ℝ) + 3) * gaussBinMax a omega k else 0) := by
      intro k _hk
      unfold M
      by_cases hfar : k ≤ n - 2 ∨ n + 2 ≤ k
      · have hcen : k ∉ central := by
          intro hk
          have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [central] using hk
          omega
        simp [hfar, hcen]
      · have hcen : k ∈ central := by
          have : n - 1 ≤ k ∧ k ≤ n + 1 := by omega
          have : k = n - 1 ∨ k = n ∨ k = n + 1 := by omega
          simpa [central] using this
        have habs := abs_mem_central3 n k (by simpa [central] using hcen)
        have : (|k| : ℝ) + 3 ≤ (|n| : ℝ) + 4 := by
          have : (|k| : ℝ) ≤ (|n| : ℝ) + 1 := by exact_mod_cast habs
          linarith
        simp [hfar, hcen]
        exact mul_le_mul_of_nonneg_right this (Real.exp_pos _).le
    have hsum := sum_le_sum hpt
    rw [sum_add_distrib] at hsum
    have hcen4 :
        ∑ k ∈ K, (if k ∈ central then
            ((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a)) else 0) ≤
          4 * ((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a)) := by
      have hite :
          ∑ k ∈ K, (if k ∈ central then
              ((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a)) else 0) =
            ((K.filter (fun k => k ∈ central)).card : ℝ) *
              (((|n| : ℝ) + 4) * Real.exp (-ε ^ 2 / (2 * a))) := by
        rw [sum_ite, sum_const, sum_const, nsmul_eq_mul, nsmul_eq_mul,
          mul_zero, add_zero]
      rw [hite]
      have hsub : K.filter (fun k => k ∈ central) ⊆ central :=
        fun k hk => (mem_filter.mp hk).2
      have hcard : ((K.filter (fun k => k ∈ central)).card : ℝ) ≤ (3 : ℝ) :=
        Nat.cast_le.mpr ((Finset.card_le_card hsub).trans
          (le_of_eq (central3_card n)))
      have hexp0 : 0 ≤ Real.exp (-ε ^ 2 / (2 * a)) := (Real.exp_pos _).le
      have hn4 : 0 ≤ (|n| : ℝ) + 4 := by
        nlinarith [abs_nonneg (n : ℝ)]
      have hmul :=
        mul_le_mul_of_nonneg_right hcard (mul_nonneg hn4 hexp0)
      nlinarith [hmul, hn4, hexp0]
    have hfar :
        ∑ k ∈ K, (if k ≤ n - 2 ∨ n + 2 ≤ k then
            ((|k| : ℝ) + 3) * gaussBinMax a omega k else 0) ≤
          2 * gaborFarTailLog a omega := by
      have hite :
          ∑ k ∈ K, (if k ≤ n - 2 ∨ n + 2 ≤ k then
              ((|k| : ℝ) + 3) * gaussBinMax a omega k else 0) =
            ∑ k ∈ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
              ((|k| : ℝ) + 3) * gaussBinMax a omega k :=
        (sum_filter (p := fun k => k ≤ n - 2 ∨ n + 2 ≤ k)
          (f := fun k => ((|k| : ℝ) + 3) * gaussBinMax a omega k)).symm
      rw [hite]
      exact weighted_far_bins_le ha K
    linarith [hsum, hcen4, hfar]
  refine hlin.trans ((mul_le_mul_of_nonneg_left hKfar hC0).trans_eq ?_)
  unfold gaborTFarLog
  simp [n, ε]
  ring

theorem gaborLogFarPacking_holds : GaborLogFarPacking :=
  fun {_a} {_omega} ha Z hinc S hS hout =>
    gabor_far_minus_pack_log ha Z hinc S hS hout

theorem gabor_cross_amp_pack_log
    {a : ℝ} (ha : 0 < a)
    (Z : GaborCanonicalConfig) (hinc : GaborConfigIncrementCompliantLog Z)
    (S : Finset (ℝ × ℝ)) (hS : S ⊆ Z.pts) :
    S.sum (fun q => (Z.mult q : ℝ) * Real.exp (-q.2 ^ 2 / (2 * a))) ≤
      (2 * zetaZerosInDiskCardBoundInner) * gaborThetaLobeLog a := by
  let w : ℝ → ℝ := fun t => Real.exp (-t ^ 2 / (2 * a))
  let M : ℤ → ℝ := fun k => gaussBinMax a 0 k
  have hM0 : ∀ k, 0 ≤ M k := fun k => gaussBinMax_nonneg ha k
  have hM : ∀ q ∈ S, w q.2 ≤ M (ordinateBin q.2) := by
    intro q _hq
    have : w q.2 = gaussWeight a 0 q.2 := by
      unfold gaussWeight w; congr 1; ring
    rw [this]
    exact le_gaussBinMax ha (mem_Icc_of_ordinateBin q.2)
  have hpack :=
    bin_partial_summation_mult_log (w := w) Z hinc S hS hM0 hM
  refine hpack.trans ?_
  have hlin := lin_pack_sum (M := M) hM0 (S.image (fun q => ordinateBin q.2))
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  refine hlin.trans (mul_le_mul_of_nonneg_left ?_ hC0)
  -- (|k|+3) * gaussBinMax a 0 ≤ central 12 + two far tails at ω=0
  set K := S.image (fun q => ordinateBin q.2)
  set n : ℤ := Int.floor (0 : ℝ)
  have hn0 : n = 0 := by simp [n]
  let central : Finset ℤ := {n - 1, n, n + 1}
  have hpt : ∀ k ∈ K,
      ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤
        (if k ∈ central then (4 : ℝ) else 0) +
          (if k ≤ n - 2 ∨ n + 2 ≤ k then
              ((|k| : ℝ) + 3) * gaussBinMax a 0 k else 0) := by
    intro k _hk
    by_cases hcen : k ∈ central
    · have hfar : ¬ (k ≤ n - 2 ∨ n + 2 ≤ k) := by
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [central] using hcen
        omega
      simp [hcen, hfar]
      have habs := abs_mem_central3 n k (by simpa [central] using hcen)
      have : (|k| : ℝ) + 3 ≤ (4 : ℝ) := by
        have : (|k| : ℝ) ≤ 1 := by
          have : (|k| : ℤ) ≤ 1 := by
            rw [hn0] at habs; exact habs.trans (by norm_num)
          exact_mod_cast this
        linarith
      exact (mul_le_of_le_one_right (by positivity)
        (gaussBinMax_le_one (a := a) (c := 0) ha k)).trans this
    · have hfar : k ≤ n - 2 ∨ n + 2 ≤ k := by
        have : k ≠ n - 1 ∧ k ≠ n ∧ k ≠ n + 1 := by
          refine ⟨?_, ?_, ?_⟩
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
        omega
      simp [hcen, hfar]
  have hsum := sum_le_sum hpt
  rw [sum_add_distrib] at hsum
  have hcen :
      ∑ k ∈ K, (if k ∈ central then (4 : ℝ) else 0) ≤ (12 : ℝ) := by
    have hite :
        ∑ k ∈ K, (if k ∈ central then (4 : ℝ) else 0) =
          ((K.filter (fun k => k ∈ central)).card : ℝ) * 4 := by
      rw [sum_ite, sum_const, sum_const, nsmul_eq_mul, nsmul_eq_mul,
        mul_zero, add_zero]
    rw [hite]
    have hsub : K.filter (fun k => k ∈ central) ⊆ central :=
      fun k hk => (mem_filter.mp hk).2
    have hcard : ((K.filter (fun k => k ∈ central)).card : ℝ) ≤ (3 : ℝ) :=
      Nat.cast_le.mpr ((Finset.card_le_card hsub).trans
        (le_of_eq (central3_card n)))
    nlinarith [hcard]
  have hfar :
      ∑ k ∈ K, (if k ≤ n - 2 ∨ n + 2 ≤ k then
          ((|k| : ℝ) + 3) * gaussBinMax a 0 k else 0) ≤
        2 * gaborFarTailLog a 0 := by
    have hite :
        ∑ k ∈ K, (if k ≤ n - 2 ∨ n + 2 ≤ k then
            ((|k| : ℝ) + 3) * gaussBinMax a 0 k else 0) =
          ∑ k ∈ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
            ((|k| : ℝ) + 3) * gaussBinMax a 0 k :=
      (sum_filter (p := fun k => k ≤ n - 2 ∨ n + 2 ≤ k)
        (f := fun k => ((|k| : ℝ) + 3) * gaussBinMax a 0 k)).symm
    rw [hite, hn0]
    simpa using weighted_far_bins_le (a := a) (omega := (0 : ℝ)) ha K
  unfold gaborThetaLobeLog
  linarith [hsum, hcen, hfar]

theorem gabor_dominanceBound_of_log
    (hlog : GaborDominanceBoundLog) :
    GaborDominanceBound := by
  intro Z hZ hinc hdist
  exact hlog Z hZ (incrementCompliant_implies_log hinc) hdist

/-! ## Honest Weil (log occupancy) -/

lemma gaborFarTailLog_nonneg {a omega : ℝ} :
    0 ≤ gaborFarTailLog a omega :=
  tsum_nonneg fun _ => by positivity

lemma gaborThetaLobeLog_nonneg {a : ℝ} : 0 ≤ gaborThetaLobeLog a := by
  unfold gaborThetaLobeLog
  linarith [gaborFarTailLog_nonneg (a := a) (omega := (0 : ℝ))]

lemma gaborArithGeomMajorant_nonneg {r : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) :
    0 ≤ gaborArithGeomMajorant r := by
  have hden : 0 < 1 - r := sub_pos.mpr hr1
  unfold gaborArithGeomMajorant
  exact add_nonneg (div_nonneg (by norm_num) hden.le)
    (div_nonneg hr0 (sq_pos_of_pos hden).le)

/-- Packing comparison at a free admissible width
`0 < a ≤ isolationShrink`.  Plus / cross / far-minus majorants
are a-monotone (sharper Gaussians); peak emptiness uses the
retuned centre `ω(a) = γ★ − πa/σ★` and the monotone radius
constraint, not a frozen shrink ω. -/
theorem gaborHonestWeilLeMajorantLog_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborHonestWeil a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) Z gaborCInc ≤
      gaborEnhancement (gaborHostSigma Z hZ) a *
          (-gaborEtaTune (gaborHostSigma Z hZ) a *
            (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a
              (gaborIsolationOmega (gaborHostSigma Z hZ)
                (gaborHostGamma Z hZ) a) +
            gaborTFarLog a
              (gaborIsolationOmega (gaborHostSigma Z hZ)
                (gaborHostGamma Z hZ) a)) +
        gaborHonestOnlineBudget a
          (gaborIsolationOmega (gaborHostSigma Z hZ)
            (gaborHostGamma Z hZ) a) gaborCInc := by
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set omega := gaborIsolationOmega σ γ a
  set host : ℝ × ℝ := (σ, γ)
  have hs := gaborHostSigma_pos Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hω : 0 < omega :=
    gaborIsolationOmega_pos hs hg ha.le
      (hle.trans (isolationShrinkOfConfig_le_omegaCap Z hZ))
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hωeq : omega = gaborIsolationOmega σ γ a := rfl
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
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hplus_sum :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a *
          ((2 * zetaZerosInDiskCardBoundInner) *
            Real.exp (-omega ^ 2 / (2 * a)) *
              gaborArithGeomMajorant (Real.exp (-omega / a))) := by
    have h1 := sum_le_sum hplus_pt
    have h2 :=
      sum_enhancement_mul (gaborEnhancement σ a) Z.pts Z.mult
        (fun q => Real.exp (-(q.2 + omega) ^ 2 / (2 * a)))
    rw [h2] at h1
    exact h1.trans (mul_le_mul_of_nonneg_left
      (gabor_plus_amp_pack_log ha hω Z hinc Z.pts subset_rfl) hE.le)
  have hcross_sum :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) ≤
        gaborEnhancement σ a *
          ((2 * zetaZerosInDiskCardBoundInner) *
            Real.exp (-omega ^ 2 / (2 * a)) *
              (2 * gaborThetaLobeLog a)) := by
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
    have hpack := gabor_cross_amp_pack_log ha Z hinc Z.pts subset_rfl
    have hc0 : 0 ≤
        2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a)) := by
      positivity
    have hscale :
        (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            Z.pts.sum (fun q => (Z.mult q : ℝ) *
              Real.exp (-q.2 ^ 2 / (2 * a))) ≤
          (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            ((2 * zetaZerosInDiskCardBoundInner) * gaborThetaLobeLog a) :=
      mul_le_mul_of_nonneg_left hpack hc0
    have heq :
        (2 * gaborEnhancement σ a * Real.exp (-omega ^ 2 / (2 * a))) *
            ((2 * zetaZerosInDiskCardBoundInner) * gaborThetaLobeLog a) =
          gaborEnhancement σ a *
            ((2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (2 * gaborThetaLobeLog a)) := by
      ring
    exact h1.trans (hscale.trans_eq heq)
  have hε0 : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
  have hout : ∀ q ∈ Z.pts.erase host,
      gaborIsolationEpsilon a < |q.2 - omega| := by
    intro q hq
    have := foreign_not_in_peakWindow_of_le Z hZ hdist
      (erase_subset _ _ hq) (ne_of_mem_erase hq) ha hle
    simpa [gaborInPeakWindow, omega] using lt_of_not_ge this
  have hminus_sum :
      (Z.pts.erase host).sum (fun q =>
          (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a * gaborTFarLog a omega := by
    have h1 := sum_le_sum hminus_pt
    have h2 :=
      sum_enhancement_mul (gaborEnhancement σ a) (Z.pts.erase host) Z.mult
        (fun q => gaussWeight a omega q.2)
    rw [h2] at h1
    exact h1.trans (mul_le_mul_of_nonneg_left
      (gabor_far_minus_pack_log ha Z hinc (Z.pts.erase host)
        (erase_subset _ _) hout) hE.le)
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
  have hξ0 : 0 ≤ Real.exp (-omega / a) := (Real.exp_pos _).le
  have hξ1 : Real.exp (-omega / a) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
  have hpack :
      Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborPlusTerm a omega q.1 q.2) +
          Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * (2 * gaborCrossTerm a omega q.1 q.2)) +
          (Z.pts.erase host).sum (fun q =>
            (Z.mult q : ℝ) * gaborMinusTerm a omega q.1 q.2) ≤
        gaborEnhancement σ a *
          (gaborTPlusLooseLog a omega + gaborTFarLog a omega) := by
    have hsum :
        gaborEnhancement σ a *
            ((2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                gaborArithGeomMajorant (Real.exp (-omega / a))) +
          gaborEnhancement σ a *
            ((2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (2 * gaborThetaLobeLog a)) +
          gaborEnhancement σ a * gaborTFarLog a omega ≤
        gaborEnhancement σ a *
          (gaborTPlusLooseLog a omega + gaborTFarLog a omega) := by
      have hθ : 0 ≤ gaborThetaLobeLog a := gaborThetaLobeLog_nonneg
      have hAG : 0 ≤
          gaborArithGeomMajorant (Real.exp (-omega / a)) :=
        gaborArithGeomMajorant_nonneg hξ0 hξ1
      have hexp0 : 0 ≤ Real.exp (-omega ^ 2 / (2 * a)) :=
        (Real.exp_pos _).le
      have hmid :
          (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (2 * gaborThetaLobeLog a) ≤
            (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (4 * gaborThetaLobeLog a) :=
        mul_le_mul_of_nonneg_left (by nlinarith [hθ])
          (mul_nonneg hC0 hexp0)
      unfold gaborTPlusLooseLog
      have hident :
          gaborEnhancement σ a *
              ((2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  gaborArithGeomMajorant (Real.exp (-omega / a))) +
            gaborEnhancement σ a *
              ((2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  (2 * gaborThetaLobeLog a)) +
            gaborEnhancement σ a * gaborTFarLog a omega =
          gaborEnhancement σ a *
            ((2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  (gaborArithGeomMajorant (Real.exp (-omega / a)) +
                    2 * gaborThetaLobeLog a) +
              gaborTFarLog a omega) := by
        ring
      rw [hident]
      refine mul_le_mul_of_nonneg_left ?_ hE.le
      have hL :
          (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (gaborArithGeomMajorant (Real.exp (-omega / a)) +
                  2 * gaborThetaLobeLog a) =
            (2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  gaborArithGeomMajorant (Real.exp (-omega / a)) +
              (2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  (2 * gaborThetaLobeLog a) := by
        ring
      have hR :
          (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (gaborArithGeomMajorant (Real.exp (-omega / a)) +
                  4 * gaborThetaLobeLog a) =
            (2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  gaborArithGeomMajorant (Real.exp (-omega / a)) +
              (2 * zetaZerosInDiskCardBoundInner) *
                Real.exp (-omega ^ 2 / (2 * a)) *
                  (4 * gaborThetaLobeLog a) := by
        ring
      have hcore :
          (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (gaborArithGeomMajorant (Real.exp (-omega / a)) +
                  2 * gaborThetaLobeLog a) ≤
            (2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                (gaborArithGeomMajorant (Real.exp (-omega / a)) +
                  4 * gaborThetaLobeLog a) := by
        rw [hL, hR]
        simpa [add_comm] using
          add_le_add_left hmid
            ((2 * zetaZerosInDiskCardBoundInner) *
              Real.exp (-omega ^ 2 / (2 * a)) *
                gaborArithGeomMajorant (Real.exp (-omega / a)))
      exact add_le_add hcore le_rfl
    linarith [hplus_sum, hcross_sum, hminus_sum, hsum]
  have hWle :
      gaborHonestWeil a omega Z gaborCInc ≤
        gaborEnhancement σ a *
            (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
              gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
          gaborHonestOnlineBudget a omega gaborCInc := by
    rw [hW, hhostMinus]
    have hdecomp :
        gaborEnhancement σ a *
              (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ)) +
            gaborEnhancement σ a *
              (gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
            gaborHonestOnlineBudget a omega gaborCInc =
          gaborEnhancement σ a *
              (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
                gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
            gaborHonestOnlineBudget a omega gaborCInc := by
      ring
    linarith [hpack, hdecomp]
  simpa [omega, σ] using hWle

theorem gaborHonestWeilLeMajorantLog_holds :
    GaborHonestWeilLeMajorantLog := by
  intro Z hZ hinc hdist
  simpa [isolationShrinkOfConfig_omega_eq] using
    gaborHonestWeilLeMajorantLog_of_le Z hZ hinc hdist
      (isolationShrinkOfConfig_a_pos Z hZ) le_rfl

/-! ## Remainder budget (log occupancy) -/

lemma mul_exp_neg_le_one_div_e {x : ℝ} (hx : 0 < x) :
    x * Real.exp (-x) ≤ 1 / Real.exp 1 := by
  have hxee : x * Real.exp 1 ≤ Real.exp x := by
    have hlog : Real.log x + 1 ≤ x := by
      linarith [Real.log_le_sub_one_of_pos hx]
    simpa [Real.exp_add, Real.exp_log hx] using Real.exp_le_exp.mpr hlog
  have hident : x * Real.exp (-x) = x / Real.exp x := by
    rw [Real.exp_neg]; field_simp
  rw [hident]
  have hxee' : x * Real.exp 1 ≤ (1 : ℝ) * Real.exp x := by
    simpa using hxee
  exact (div_le_div_iff₀ (Real.exp_pos x) (Real.exp_pos 1)).mpr hxee'

lemma gaborFarSmallnessA_le_central {gamma : ℝ} (hg : 0 < gamma) :
    gaborFarSmallnessA gamma ≤
      1 / (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) := by
  have hB : 0 <
      1600 * zetaZerosInDiskCardBoundInner * (gamma + 10) :=
    mul_pos (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos)
      (by linarith)
  exact one_div_le_one_div_of_le hB (le_max_right _ _)

lemma gaborFarSmallnessA_le_tail {gamma : ℝ} (hg : 0 < gamma) :
    gaborFarSmallnessA gamma ≤
      1 / (2 * (gamma + Real.log (zetaZerosInDiskCardBoundInner + 1) + 20)) := by
  have hC : 0 < zetaZerosInDiskCardBoundInner :=
    zetaZerosInDiskCardBoundInner_pos
  have hlog : 0 ≤ Real.log (zetaZerosInDiskCardBoundInner + 1) :=
    Real.log_nonneg (by linarith [hC])
  have hA : 0 <
      2 * (gamma + Real.log (zetaZerosInDiskCardBoundInner + 1) + 20) :=
    mul_pos (by norm_num)
      (add_pos_of_pos_of_nonneg (add_pos_of_pos_of_nonneg hg hlog) (by norm_num))
  exact one_div_le_one_div_of_le hA (le_max_left _ _)

lemma isolationShrinkOfConfig_omega_le_gamma
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).2 ≤ gaborHostGamma Z hZ := by
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hωeq := isolationShrinkOfConfig_omega_eq Z hZ
  have hsub : 0 ≤ Real.pi * (isolationShrinkOfConfig Z hZ).1 /
      gaborHostSigma Z hZ :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
  have hdef :
      (isolationShrinkOfConfig Z hZ).2 =
        gaborHostGamma Z hZ -
          Real.pi * (isolationShrinkOfConfig Z hZ).1 /
            gaborHostSigma Z hZ := by
    rw [hωeq]; rfl
  linarith [hdef, hsub]

lemma plus_omega_sq_div_two_a_ge_log {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hplus : a ≤ gaborPlusSmallnessA gamma) :
    Real.log (gaborCInc + 1) + 256 ≤
      gaborIsolationOmega sigma gamma a ^ 2 / (2 * a) := by
  have hω : gamma / 2 ≤ gaborIsolationOmega sigma gamma a :=
    gaborIsolationOmega_pos_of_cap hs hg ha.le hωcap
  have hC : 0 < gaborCInc := gaborCInc_pos
  have hlog : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  have hden : 0 < 8 * (Real.log (gaborCInc + 1) + 256) :=
    mul_pos (by norm_num) (add_pos_of_nonneg_of_pos hlog (by norm_num))
  have hγa : a * (8 * (Real.log (gaborCInc + 1) + 256)) ≤ gamma ^ 2 :=
    (le_div_iff₀ hden).mp hplus
  have hfrac : Real.log (gaborCInc + 1) + 256 ≤ gamma ^ 2 / (8 * a) := by
    have : (Real.log (gaborCInc + 1) + 256) * (8 * a) ≤ gamma ^ 2 := by
      linarith
    exact (le_div_iff₀ (mul_pos (by norm_num) ha)).mpr this
  have hωsq : (gamma / 2) ^ 2 ≤ gaborIsolationOmega sigma gamma a ^ 2 := by
    have hnn : 0 ≤ gamma / 2 := by linarith
    have hωnn : 0 ≤ gaborIsolationOmega sigma gamma a := le_trans hnn hω
    exact sq_le_sq.mpr (by rwa [abs_of_nonneg hnn, abs_of_nonneg hωnn])
  have hident : (gamma / 2) ^ 2 / (2 * a) = gamma ^ 2 / (8 * a) := by
    field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]
    ring
  have hleft : (gamma / 2) ^ 2 / (2 * a) ≤
      gaborIsolationOmega sigma gamma a ^ 2 / (2 * a) :=
    div_le_div_of_nonneg_right hωsq (mul_nonneg (by norm_num) ha.le)
  exact hfrac.trans (hident.symm.trans_le hleft)

lemma gaborTPlusLooseLog_le_one_hundred {sigma gamma a omega : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a) (hω : 0 < omega)
    (hωeq : omega = gaborIsolationOmega sigma gamma a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hplus : a ≤ gaborPlusSmallnessA gamma) :
    gaborTPlusLooseLog a omega ≤ (1 / 100 : ℝ) := by
  have hξ : Real.exp (-omega / a) ≤ (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_le_half hs hg ha hωcap hγsq hbin
  have hAG := gaborArithGeomMajorant_le_eight (Real.exp_pos _).le hξ
  have h64bin := inv_two_a_ge_sixty_four ha hbin
  have hξfar : Real.exp (-(1 : ℝ) / (2 * a)) ≤ (1 / 2 : ℝ) :=
    (Real.exp_le_exp.mpr (by
      rw [neg_div]; exact neg_le_neg h64bin)).trans
      (exp_neg_sixty_four_le.trans (by norm_num))
  have htail := gaborFarTailLog_le_geom (omega := (0 : ℝ)) ha hξfar
  have hΘ : gaborThetaLobeLog a ≤ (13 : ℝ) := by
    unfold gaborThetaLobeLog
    have : 2 * gaborFarTailLog a 0 ≤ (1 : ℝ) := by
      have hle : 2 * gaborFarTailLog a 0 ≤
          2 * (2 * Real.exp (-(1 : ℝ) / (2 * a)) * (|0| + 9)) :=
        mul_le_mul_of_nonneg_left htail (by norm_num)
      have : 2 * (2 * Real.exp (-(1 : ℝ) / (2 * a)) * 9) =
          36 * Real.exp (-(1 : ℝ) / (2 * a)) := by ring
      have hexp : 36 * Real.exp (-(1 : ℝ) / (2 * a)) ≤
          36 * Real.exp (-(64 : ℝ)) :=
        mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr (by
          rw [neg_div]; exact neg_le_neg h64bin)) (by norm_num)
      have htiny : 36 * Real.exp (-(64 : ℝ)) ≤ (1 : ℝ) := by
        have := mul_le_mul_of_nonneg_left exp_neg_sixty_four_le
          (by norm_num : (0 : ℝ) ≤ 36)
        have hident : 36 * (1 / (2 : ℝ) ^ 64) = 36 / (2 : ℝ) ^ 64 := by ring
        exact (this.trans_eq hident).trans (by norm_num)
      have habs0 : |(0 : ℝ)| + 9 = (9 : ℝ) := by simp
      linarith [hle, this, hexp, htiny, habs0]
    linarith
  have hbrack :
      gaborArithGeomMajorant (Real.exp (-omega / a)) +
        4 * gaborThetaLobeLog a ≤ (60 : ℝ) := by
    nlinarith [hAG, hΘ, gaborThetaLobeLog_nonneg (a := a)]
  have hlog := plus_omega_sq_div_two_a_ge_log hs hg ha hωcap hplus
  have hexp : Real.exp (-omega ^ 2 / (2 * a)) ≤
      Real.exp (-(Real.log (gaborCInc + 1) + 256)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div, hωeq]
    exact neg_le_neg hlog
  have hident :
      Real.exp (-(Real.log (gaborCInc + 1) + 256)) =
        Real.exp (-256) / (gaborCInc + 1) := by
    rw [neg_add, Real.exp_add, Real.exp_neg,
      Real.exp_log (by linarith [gaborCInc_pos] : (0 : ℝ) < gaborCInc + 1)]
    field_simp
  have hC : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  unfold gaborTPlusLooseLog
  have hmain :
      (2 * zetaZerosInDiskCardBoundInner) *
          Real.exp (-omega ^ 2 / (2 * a)) *
            (gaborArithGeomMajorant (Real.exp (-omega / a)) +
              4 * gaborThetaLobeLog a) ≤
        (2 * zetaZerosInDiskCardBoundInner) *
          (Real.exp (-256) / (gaborCInc + 1)) * 60 := by
    have h1 := mul_le_mul_of_nonneg_left (hexp.trans_eq hident) hC
    exact mul_le_mul h1 hbrack (by
      exact add_nonneg (gaborArithGeomMajorant_nonneg (Real.exp_pos _).le
          (lt_of_le_of_lt hξ (by norm_num)))
        (mul_nonneg (by norm_num) gaborThetaLobeLog_nonneg))
      (mul_nonneg hC (div_nonneg (Real.exp_pos _).le
        (by linarith [gaborCInc_pos])))
  have hCinc : (2 * zetaZerosInDiskCardBoundInner : ℝ) = gaborCInc := by
    unfold gaborCInc; rfl
  have hsimp :
      (2 * zetaZerosInDiskCardBoundInner) *
          (Real.exp (-256) / (gaborCInc + 1)) * 60 =
        60 * gaborCInc / (gaborCInc + 1) * Real.exp (-256) := by
    rw [hCinc]; field_simp
  have hfrac : 60 * gaborCInc / (gaborCInc + 1) ≤ (60 : ℝ) := by
    have hden : 0 < gaborCInc + 1 := by linarith [gaborCInc_pos]
    have hle : gaborCInc / (gaborCInc + 1) ≤ 1 :=
      (div_le_one hden).mpr (by linarith [gaborCInc_pos])
    have hmul : 60 * (gaborCInc / (gaborCInc + 1)) ≤ 60 * 1 :=
      mul_le_mul_of_nonneg_left hle (by norm_num)
    have hident : 60 * gaborCInc / (gaborCInc + 1) =
        60 * (gaborCInc / (gaborCInc + 1)) := by ring
    exact hident.trans_le (hmul.trans_eq (by ring))
  have hexp2 : 60 * Real.exp (-256) ≤ 60 / (2 : ℝ) ^ 256 := by
    have := mul_le_mul_of_nonneg_left (exp_neg_nat_le_inv_two_pow 256)
      (by norm_num : (0 : ℝ) ≤ 60)
    have hident : 60 * (1 / (2 : ℝ) ^ 256) = 60 / (2 : ℝ) ^ 256 := by ring
    rwa [hident] at this
  have htiny : 60 / (2 : ℝ) ^ 256 < (1 / 100 : ℝ) := by norm_num
  refine hmain.trans ?_
  rw [hsimp]
  have hnn : 0 ≤ Real.exp (-256) := (Real.exp_pos _).le
  have hscale : 60 * gaborCInc / (gaborCInc + 1) * Real.exp (-256) ≤
      60 * Real.exp (-256) :=
    mul_le_mul_of_nonneg_right hfrac hnn
  exact (hscale.trans hexp2).trans htiny.le

lemma gaborCInc_two_farTail_le_one_two_hundred {a omega gamma : ℝ}
    (ha : 0 < a) (hg : 0 < gamma) (hω : 0 < omega)
    (hωle : omega ≤ gamma)
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hfar : a ≤ gaborFarSmallnessA gamma) :
    (2 * zetaZerosInDiskCardBoundInner) * (2 * gaborFarTailLog a omega) ≤
      (1 / 200 : ℝ) := by
  have hC : 0 < zetaZerosInDiskCardBoundInner :=
    zetaZerosInDiskCardBoundInner_pos
  have h64 := inv_two_a_ge_sixty_four ha hbin
  have hξfar : Real.exp (-(1 : ℝ) / (2 * a)) ≤ (1 / 2 : ℝ) :=
    (Real.exp_le_exp.mpr (by
      rw [neg_div]; exact neg_le_neg h64)).trans
      (exp_neg_sixty_four_le.trans (by norm_num))
  have htail0 := gaborFarTailLog_le_geom (omega := omega) ha hξfar
  have hB : 0 < 1600 * zetaZerosInDiskCardBoundInner * (gamma + 10) :=
    mul_pos (mul_pos (by norm_num) hC) (by linarith)
  have h1a : 800 * zetaZerosInDiskCardBoundInner * (gamma + 10) ≤
      1 / (2 * a) := by
    have haB : a ≤ 1 / (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) :=
      hfar.trans (gaborFarSmallnessA_le_central hg)
    have : a * (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) ≤ 1 :=
      (le_div_iff₀ hB).mp haB
    have : 1600 * zetaZerosInDiskCardBoundInner * (gamma + 10) ≤ 1 / a :=
      (le_div_iff₀ ha).mpr (by linarith)
    have hhalf : (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) / 2 ≤
        (1 / a) / 2 :=
      div_le_div_of_nonneg_right this (by norm_num)
    have hL : (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) / 2 =
        800 * zetaZerosInDiskCardBoundInner * (gamma + 10) := by ring
    have hR : (1 / a) / 2 = 1 / (2 * a) := by field_simp [ne_of_gt ha]
    rwa [hL, hR] at hhalf
  have hξ :
      Real.exp (-(1 : ℝ) / (2 * a)) ≤
        Real.exp (-(800 * zetaZerosInDiskCardBoundInner * (gamma + 10))) :=
    Real.exp_le_exp.mpr (by rw [neg_div]; exact neg_le_neg h1a)
  have htail :
      (2 * zetaZerosInDiskCardBoundInner) * (2 * gaborFarTailLog a omega) ≤
        (1 / 200 : ℝ) := by
    have hlin : gaborFarTailLog a omega ≤
        2 * Real.exp (-(1 : ℝ) / (2 * a)) * (|omega| + 9) := htail0
    have habs : |omega| = omega := abs_of_nonneg hω.le
    have hω9 : |omega| + 9 ≤ gamma + 9 := by linarith [habs, hωle]
    have h1 :
        4 * zetaZerosInDiskCardBoundInner * gaborFarTailLog a omega ≤
          4 * zetaZerosInDiskCardBoundInner *
            (2 * Real.exp (-(1 : ℝ) / (2 * a)) * (gamma + 9)) := by
      have hlin' : gaborFarTailLog a omega ≤
          2 * Real.exp (-(1 : ℝ) / (2 * a)) * (gamma + 9) :=
        hlin.trans (mul_le_mul_of_nonneg_left hω9 (by positivity))
      exact mul_le_mul_of_nonneg_left hlin' (by positivity)
    have h2 :
        8 * zetaZerosInDiskCardBoundInner * (gamma + 9) *
            Real.exp (-(1 : ℝ) / (2 * a)) ≤
          8 * zetaZerosInDiskCardBoundInner * (gamma + 9) *
            Real.exp (-(800 * zetaZerosInDiskCardBoundInner * (gamma + 10))) :=
      mul_le_mul_of_nonneg_left hξ (by positivity)
    set u := zetaZerosInDiskCardBoundInner * (gamma + 10)
    have hu : 0 < u := mul_pos hC (by linarith)
    have hγ9 : gamma + 9 ≤ gamma + 10 := by linarith
    have h3 :
        8 * zetaZerosInDiskCardBoundInner * (gamma + 9) *
            Real.exp (-(800 * zetaZerosInDiskCardBoundInner * (gamma + 10))) ≤
          8 * u * Real.exp (-(800 * u)) := by
      have : 8 * zetaZerosInDiskCardBoundInner * (gamma + 9) ≤ 8 * u := by
        have hL : 8 * zetaZerosInDiskCardBoundInner * (gamma + 9) =
            8 * (zetaZerosInDiskCardBoundInner * (gamma + 9)) := by ring
        have hR : 8 * u =
            8 * (zetaZerosInDiskCardBoundInner * (gamma + 10)) := by
          unfold u; ring
        rw [hL, hR]
        exact mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hγ9 hC.le) (by norm_num)
      have hu_eq : 800 * zetaZerosInDiskCardBoundInner * (gamma + 10) =
          800 * u := by unfold u; ring
      rw [hu_eq]
      exact mul_le_mul_of_nonneg_right this (Real.exp_pos _).le
    have h4 : 8 * u * Real.exp (-(800 * u)) ≤ 8 / (800 * Real.exp 1) := by
      have hx : (800 * u) * Real.exp (-(800 * u)) ≤ 1 / Real.exp 1 :=
        mul_exp_neg_le_one_div_e (mul_pos (by norm_num) hu)
      have hident :
          8 * u * Real.exp (-(800 * u)) =
            (8 / 800) * ((800 * u) * Real.exp (-(800 * u))) := by
        ring
      rw [hident]
      have hstep : (8 / 800 : ℝ) * ((800 * u) * Real.exp (-(800 * u))) ≤
          (8 / 800 : ℝ) * (1 / Real.exp 1) :=
        mul_le_mul_of_nonneg_left hx (by norm_num)
      have heq : (8 / 800 : ℝ) * (1 / Real.exp 1) =
          8 / (800 * Real.exp 1) := by field_simp
      exact hstep.trans_eq heq
    have h5 : 8 / (800 * Real.exp 1) ≤ (1 / 200 : ℝ) := by
      have he : (2 : ℝ) ≤ Real.exp 1 := by
        have := Real.add_one_le_exp (1 : ℝ)
        linarith
      have hden : 0 < 800 * Real.exp 1 :=
        mul_pos (by norm_num) (Real.exp_pos _)
      have hden2 : 0 < 800 * (2 : ℝ) := by norm_num
      have hle : 8 / (800 * Real.exp 1) ≤ 8 / (800 * 2) :=
        div_le_div_of_nonneg_left (by norm_num) hden2
          (mul_le_mul_of_nonneg_left he (by norm_num))
      have : (8 : ℝ) / (800 * 2) = 1 / 200 := by norm_num
      exact hle.trans this.le
    have hassoc :
        (2 * zetaZerosInDiskCardBoundInner) * (2 * gaborFarTailLog a omega) =
          4 * zetaZerosInDiskCardBoundInner * gaborFarTailLog a omega := by
      ring
    have hassoc2 :
        4 * zetaZerosInDiskCardBoundInner *
            (2 * Real.exp (-(1 : ℝ) / (2 * a)) * (gamma + 9)) =
          8 * zetaZerosInDiskCardBoundInner * (gamma + 9) *
            Real.exp (-(1 : ℝ) / (2 * a)) := by
      ring
    linarith [hassoc, h1, hassoc2, h2, h3, h4, h5]
  exact htail

lemma gaborTFarLog_le_one_fifty {a omega gamma : ℝ}
    (ha : 0 < a) (hg : 0 < gamma) (hω : 0 < omega)
    (hωle : omega ≤ gamma)
    (hfour : a ≤ 1 / (4 * (gaborKBin : ℝ)))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hfar : a ≤ gaborFarSmallnessA gamma) :
    gaborTFarLog a omega ≤ (1 / 50 : ℝ) := by
  have hexpA : Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) = a := by
    have hε := gaborIsolationEpsilon_sq_of_small ha hfour
    rw [neg_div, hε, Real.exp_neg, Real.exp_log (one_div_pos.mpr ha)]
    exact inv_eq_of_mul_eq_one_left (by field_simp [ne_of_gt ha])
  have hn : (|Int.floor omega| : ℝ) + 4 ≤ gamma + 5 := by
    have hfl := abs_floor_le_abs_add_one omega
    have habs : |omega| = omega := abs_of_nonneg hω.le
    linarith [hfl, habs, hωle]
  have hcenA := (hfar.trans (gaborFarSmallnessA_le_central hg))
  have hC : 0 < zetaZerosInDiskCardBoundInner :=
    zetaZerosInDiskCardBoundInner_pos
  have hcen :
      4 * (2 * zetaZerosInDiskCardBoundInner) *
          ((|Int.floor omega| : ℝ) + 4) *
          Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) ≤
        (1 / 200 : ℝ) := by
    rw [hexpA]
    have h1 :
        8 * zetaZerosInDiskCardBoundInner *
            ((|Int.floor omega| : ℝ) + 4) * a ≤
          8 * zetaZerosInDiskCardBoundInner * (gamma + 5) * a :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hn (by positivity)) ha.le
    have haB : a ≤ 1 / (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10)) :=
      hcenA
    have hden : 0 < 1600 * zetaZerosInDiskCardBoundInner * (gamma + 10) :=
      mul_pos (mul_pos (by norm_num) hC) (by linarith)
    have h2 :
        8 * zetaZerosInDiskCardBoundInner * (gamma + 5) * a ≤
          8 * zetaZerosInDiskCardBoundInner * (gamma + 5) *
            (1 / (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10))) :=
      mul_le_mul_of_nonneg_left haB (by positivity)
    have hident :
        8 * zetaZerosInDiskCardBoundInner * (gamma + 5) *
            (1 / (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10))) =
          (gamma + 5) / (200 * (gamma + 10)) := by
      field_simp [ne_of_gt hC, ne_of_gt (by linarith : (0 : ℝ) < gamma + 10)]
      ring
    have hfrac : (gamma + 5) / (200 * (gamma + 10)) < (1 / 200 : ℝ) := by
      have hden' : 0 < 200 * (gamma + 10) :=
        mul_pos (by norm_num) (by linarith)
      rw [div_lt_div_iff₀ hden' (by norm_num : (0 : ℝ) < 200)]
      nlinarith [hg]
    have hassoc :
        4 * (2 * zetaZerosInDiskCardBoundInner) *
            ((|Int.floor omega| : ℝ) + 4) * a =
          8 * zetaZerosInDiskCardBoundInner *
            ((|Int.floor omega| : ℝ) + 4) * a := by
      ring
    linarith [hassoc, h1, h2, hident, hfrac]
  have htail :=
    gaborCInc_two_farTail_le_one_two_hundred ha hg hω hωle hbin hfar
  unfold gaborTFarLog
  linarith [hcen, htail,
    (by norm_num : (1 / 200 : ℝ) + (1 / 200 : ℝ) ≤ (1 / 50 : ℝ))]

theorem gaborRemainderBudgetLog_holds : GaborRemainderBudgetLog := by
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
  have hplus := isolationShrinkOfConfig_le_plus Z hZ
  have hfar := isolationShrinkOfConfig_le_far Z hZ
  have hωeq : omega = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  have h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a) := by
    rw [hωeq]
    exact omega_sq_div_two_a_ge_sixty_four hs hg ha hωcap hγsq
  have hξlt : Real.exp (-omega / a) < (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_lt_half hs hg ha hωcap hγsq hbin
  have hTplus :=
    gaborTPlusLooseLog_le_one_hundred hs hg ha hω hωeq hωcap hγsq hbin hplus
  have hTfar :=
    gaborTFarLog_le_one_fifty ha hg hω
      (isolationShrinkOfConfig_omega_le_gamma Z hZ) hfour hbin hfar
  have hRon := gaborRon_div_E_le_one_hundred hs ha hω h64 hξlt hbin hon
  linarith [hTplus, hTfar, hRon,
    (by norm_num : (1 / 100 : ℝ) + (1 / 50 : ℝ) + (1 / 100 : ℝ) < (9 / 10 : ℝ))]

theorem gabor_dominanceAssemblyLog_holds : GaborDominanceAssemblyLog :=
  ⟨gaborHonestWeilLeMajorantLog_holds, gaborRemainderBudgetLog_holds⟩

theorem gabor_dominanceBoundLog_holds : GaborDominanceBoundLog :=
  gabor_dominanceBoundLog_of_assembly gabor_dominanceAssemblyLog_holds

#print axioms gaborFarTailLog_mono_abs
#print axioms gaborKBinAt_le_linear
#print axioms gaborKBinAt_mono
#print axioms zeta_unit_increment_le_gaborKBinAt
#print axioms stripZerosWindow_card_le_gaborKBinAt
#print axioms incrementCompliantLog_of_le_strip
#print axioms gabor_dominanceBound_of_log
#print axioms gabor_dominanceBoundLog_of_assembly
#print axioms gaborLogFarPacking_holds
#print axioms gabor_plus_amp_pack_log
#print axioms gabor_far_minus_pack_log
#print axioms gabor_cross_amp_pack_log
#print axioms gaborHonestWeilLeMajorantLog_of_le
#print axioms gaborHonestWeilLeMajorantLog_holds
#print axioms gaborRemainderBudgetLog_holds
#print axioms gabor_dominanceAssemblyLog_holds
#print axioms gabor_dominanceBoundLog_holds

end RH
