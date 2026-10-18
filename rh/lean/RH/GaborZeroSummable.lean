/-
RH/GaborZeroSummable.lean -- r557 brick: summability of ĥ_W(ρ)
over nontrivial zeta zeros (pure Gabor class).

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free comparison of the strip
Gaussian majorant against the Path-A increment.  This file does not
prove `GaborExplicitFormula`.

The live scaling tests are pure (`coeffs = ⟨1,0,0⟩`).  Entirety of
`gaborHat` is available for every even quartic.  The r587 quartic
poly-in-t majorant discharges unweighted zero-summability for every
even quartic (`gaborHatQuarticZeroSummableRemainder_holds`).
-/
import RH.GaborHatAnalytic
import RH.GaborThetaBound
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace RH

set_option maxHeartbeats 800000

open scoped Classical
open Complex Set Finset

/-! ## Log-versus-Gaussian comparison series -/

lemma log_add_b_nonneg {b : ℝ} (hb : 1 ≤ b) (n : ℕ) :
    0 ≤ 1 + Real.log ((n : ℝ) + b) := by
  have hn : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  have : (1 : ℝ) ≤ (n : ℝ) + b := by linarith
  exact add_nonneg (by norm_num) (Real.log_nonneg this)

lemma one_add_log_le_add {b : ℝ} (hb : 1 ≤ b) (n : ℕ) :
    1 + Real.log ((n : ℝ) + b) ≤ (n : ℝ) + b + 1 := by
  have hx : (0 : ℝ) < (n : ℝ) + b :=
    add_pos_of_nonneg_of_pos (Nat.cast_nonneg _) (lt_of_lt_of_le (by norm_num) hb)
  have hlog : Real.log ((n : ℝ) + b) ≤ (n : ℝ) + b :=
    (Real.log_le_sub_one_of_pos hx).trans (by linarith)
  linarith

lemma exp_neg_sq_le_exp_neg {c : ℝ} (hc : 0 < c) {n : ℕ} (hn : 1 ≤ n) :
    Real.exp (-c * (n : ℝ) ^ 2) ≤ Real.exp (-c * (n : ℝ)) := by
  refine Real.exp_le_exp.mpr ?_
  have hn1 : (1 : ℝ) ≤ (n : ℝ) := Nat.one_le_cast.mpr hn
  have hsq : (n : ℝ) ≤ (n : ℝ) ^ 2 := by nlinarith [hn1]
  exact mul_le_mul_of_nonpos_left hsq (neg_nonpos.mpr hc.le)

lemma log_mul_gauss_le_geom {c b : ℝ} (hc : 0 < c) (hb : 1 ≤ b) (n : ℕ) :
    (1 + Real.log ((n : ℝ) + b)) * Real.exp (-c * (n : ℝ) ^ 2) ≤
      ((n : ℝ) + b + 1) * Real.exp (-c * (n : ℝ)) := by
  have hexp : Real.exp (-c * (n : ℝ) ^ 2) ≤ Real.exp (-c * (n : ℝ)) := by
    rcases Nat.eq_zero_or_pos n with hn | hn
    · subst hn; simp
    · exact exp_neg_sq_le_exp_neg hc (Nat.succ_le_iff.mpr hn)
  exact mul_le_mul (one_add_log_le_add hb n) hexp (Real.exp_pos _).le
    (by positivity)

lemma exp_neg_mul_nat {c : ℝ} (n : ℕ) :
    Real.exp (-c * (n : ℝ)) = Real.exp (-c) ^ n := by
  rw [show -c * (n : ℝ) = (n : ℝ) * (-c) by ring, Real.exp_nat_mul]

lemma summable_nat_linear_exp_neg {c : ℝ} (hc : 0 < c) :
    Summable fun n : ℕ => ((n : ℝ) + 1) * Real.exp (-c * (n : ℝ)) := by
  have hr : ‖(Real.exp (-c) : ℝ)‖ < 1 := by
    rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
    exact Real.exp_lt_one_iff.mpr (neg_lt_zero.mpr hc)
  have hpow : Summable fun n : ℕ => (n : ℝ) ^ 1 * Real.exp (-c) ^ n :=
    summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have h1 : Summable fun n : ℕ => (n : ℝ) * Real.exp (-c) ^ n := by
    simpa using hpow
  have hgeom : Summable fun n : ℕ => Real.exp (-c) ^ n :=
    summable_geometric_of_norm_lt_one hr
  convert h1.add hgeom using 1
  ext n
  rw [exp_neg_mul_nat]
  ring

lemma summable_nat_add_const_exp_neg {c A : ℝ} (hc : 0 < c) :
    Summable fun n : ℕ => ((n : ℝ) + A) * Real.exp (-c * (n : ℝ)) := by
  have hr : ‖(Real.exp (-c) : ℝ)‖ < 1 := by
    rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
    exact Real.exp_lt_one_iff.mpr (neg_lt_zero.mpr hc)
  have hpow : Summable fun n : ℕ => (n : ℝ) ^ 1 * Real.exp (-c) ^ n :=
    summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have h1 : Summable fun n : ℕ => (n : ℝ) * Real.exp (-c) ^ n := by
    simpa using hpow
  have hgeom : Summable fun n : ℕ => Real.exp (-c) ^ n :=
    summable_geometric_of_norm_lt_one hr
  convert (h1.add (hgeom.mul_left A)) using 1
  ext n
  rw [exp_neg_mul_nat]
  ring

set_option maxHeartbeats 2000000 in
theorem summable_log_mul_gauss {c b : ℝ} (hc : 0 < c) (hb : 1 ≤ b) :
    Summable fun n : ℕ =>
      (1 + Real.log ((n : ℝ) + b)) * Real.exp (-c * (n : ℝ) ^ 2) := by
  refine Summable.of_nonneg_of_le
    (fun n => mul_nonneg (log_add_b_nonneg hb n) (Real.exp_pos _).le)
    (fun n => log_mul_gauss_le_geom hc hb n) ?_
  convert summable_nat_add_const_exp_neg (A := b + 1) hc using 1
  ext n
  ring

/-! ## Two-sided unit-window card bound -/

noncomputable def stripZerosWindow (N : ℝ) : Finset ℂ :=
  (riemannZetaZerosOnClosedRect 0 1 (|N| + 1)).filter
    fun z => N ≤ z.im ∧ z.im ≤ N + 1

lemma mem_stripZerosWindow {N : ℝ} {z : ℂ} :
    z ∈ stripZerosWindow N ↔
      z ∈ riemannZetaZerosOnClosedRect 0 1 (|N| + 1) ∧
        N ≤ z.im ∧ z.im ≤ N + 1 :=
  Finset.mem_filter

lemma card_strip_window_re_ge_half (N : ℝ) :
    ((stripZerosWindow N).filter
        (fun z => (1 / 2 : ℝ) ≤ z.re)).card ≤
      (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  refine card_le_card ?_
  intro z hz
  have hzf := mem_filter.mp hz
  have hzW := mem_stripZerosWindow.mp hzf.1
  have hzR := mem_riemannZetaZerosOnClosedRect.mp hzW.1
  have hrect := mem_zetaClosedRect.mp hzR.1
  refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hzR.2.1, hzR.2.2⟩
  exact mem_unit_height_inner_disk hzf.2 hrect.2.1 hzW.2

lemma card_strip_window_re_lt_half (N : ℝ) :
    ((stripZerosWindow N).filter
        (fun z => z.re < (1 / 2 : ℝ))).card ≤
      (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  set Slt := (stripZerosWindow N).filter fun z => z.re < (1 / 2 : ℝ)
  set D := riemannZetaZerosInClosedDisk
    ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)
  have hinj : Function.Injective fun z : ℂ => 1 - z :=
    fun a b h => sub_right_inj.mp h
  have himage : Slt.image (fun z => 1 - z) ⊆ D := by
    intro w hw
    obtain ⟨z, hzlt, rfl⟩ := mem_image.mp hw
    have hzf := mem_filter.mp hzlt
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
      rw [re_one_sub]; linarith [hzf.2]
    have hre_le : (1 - z).re ≤ 1 := by
      rw [re_one_sub]; linarith [hrect.1]
    have him : -(N + 1 : ℝ) ≤ (1 - z).im ∧
        (1 - z).im ≤ (-(N + 1 : ℝ) + 1) := by
      have himz : (1 - z).im = -z.im := by simp [sub_im]
      rw [himz]
      constructor <;> linarith [hzW.2.1, hzW.2.2]
    refine mem_riemannZetaZerosInClosedDisk.mpr ⟨?_, hwR.2.1, hwR.2.2⟩
    exact mem_unit_height_inner_disk (N := -(N + 1 : ℝ))
      hre_ge hre_le him
  exact (Finset.card_image_of_injective Slt hinj).symm.trans_le
    (Finset.card_le_card himage)

lemma card_strip_window_le_disks (N : ℝ) :
    (stripZerosWindow N).card ≤
      (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (N + 1 / 2 : ℝ) * I) (13 / 8)).card +
        (riemannZetaZerosInClosedDisk
          ((2 : ℂ) + (-(N + 1 : ℝ) + 1 / 2 : ℝ) * I) (13 / 8)).card := by
  set S := stripZerosWindow N
  set Sge := S.filter fun z => (1 / 2 : ℝ) ≤ z.re
  set Slt := S.filter fun z => z.re < (1 / 2 : ℝ)
  have hunion : Sge ∪ Slt = S := by
    ext z
    constructor
    · intro hz
      rcases mem_union.mp hz with h | h
      · exact (mem_filter.mp h).1
      · exact (mem_filter.mp h).1
    · intro hz
      by_cases hre : (1 / 2 : ℝ) ≤ z.re
      · exact mem_union.mpr (Or.inl (mem_filter.mpr ⟨hz, hre⟩))
      · exact mem_union.mpr
          (Or.inr (mem_filter.mpr ⟨hz, lt_of_not_ge hre⟩))
  have hdisj : Disjoint Sge Slt := by
    refine disjoint_left.mpr ?_
    intro z hzge hzlt
    exact (not_lt_of_ge (mem_filter.mp hzge).2) (mem_filter.mp hzlt).2
  have hpart : S.card = Sge.card + Slt.card := by
    rw [← hunion, card_union_of_disjoint hdisj]
  linarith [hpart, card_strip_window_re_ge_half N,
    card_strip_window_re_lt_half N]

lemma card_strip_window_le (N : ℝ) :
    ((stripZerosWindow N).card : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner *
        (1 + Real.log (|N| + 3)) := by
  have hnat := card_strip_window_le_disks N
  have hC0 : (0 : ℝ) ≤ zetaZerosInDiskCardBoundInner :=
    le_of_lt zetaZerosInDiskCardBoundInner_pos
  set τp : ℝ := N + (1 / 2 : ℝ)
  set τm : ℝ := -(N + 1 : ℝ) + (1 / 2 : ℝ)
  have hDp := zetaZerosInDisk_card_le_inner τp
  have hDm := zetaZerosInDisk_card_le_inner τm
  have hτm : τm = -τp := by unfold τp τm; ring
  have habsp : |τp| ≤ |N| + 1 := by
    unfold τp
    have : |N + 1 / 2| ≤ |N| + |(1 / 2 : ℝ)| := abs_add_le _ _
    have : |(1 / 2 : ℝ)| = (1 / 2 : ℝ) := abs_of_pos (by norm_num)
    linarith
  have habsm : |τm| ≤ |N| + 1 := by
    rw [hτm, abs_neg]
    exact habsp
  have hlogp : 1 + Real.log (2 + |τp|) ≤ 1 + Real.log (|N| + 3) := by
    have hx : 0 < 2 + |τp| := by positivity
    have hle : 2 + |τp| ≤ |N| + 3 := by linarith [habsp]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hlogm : 1 + Real.log (2 + |τm|) ≤ 1 + Real.log (|N| + 3) := by
    have hx : 0 < 2 + |τm| := by positivity
    have hle : 2 + |τm| ≤ |N| + 3 := by linarith [habsm]
    exact add_le_add_right (Real.log_le_log hx hle) 1
  have hp :
      ((riemannZetaZerosInClosedDisk
          ((2 : ℂ) + τp * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (|N| + 3)) :=
    hDp.trans (mul_le_mul_of_nonneg_left hlogp hC0)
  have hm :
      ((riemannZetaZerosInClosedDisk
          ((2 : ℂ) + τm * I) (13 / 8)).card : ℝ) ≤
        zetaZerosInDiskCardBoundInner * (1 + Real.log (|N| + 3)) :=
    hDm.trans (mul_le_mul_of_nonneg_left hlogm hC0)
  have hcast :
      ((stripZerosWindow N).card : ℝ) ≤
        ((riemannZetaZerosInClosedDisk
            ((2 : ℂ) + τp * I) (13 / 8)).card : ℝ) +
          ((riemannZetaZerosInClosedDisk
              ((2 : ℂ) + τm * I) (13 / 8)).card : ℝ) := by
    have h0 : (N + 1 / 2 : ℝ) = τp := by unfold τp; ring
    have h1 : (-(N + 1 : ℝ) + 1 / 2 : ℝ) = τm := by unfold τm; ring
    have h := (Nat.cast_le (α := ℝ)).mpr hnat
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
  linarith [hcast, hp, hm]

/-! ## Weighted bin partial summation -/

theorem bin_partial_summation_weighted
    {α : Type*} [DecidableEq α]
    {w : ℝ → ℝ} (_hw : ∀ t, 0 ≤ w t)
    (S : Finset α) (γ : α → ℝ)
    (C : ℤ → ℝ) (hC0 : ∀ k, 0 ≤ C k)
    (hC : ∀ k : ℤ,
      ((S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1)).card : ℝ) ≤
        C k)
    {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k)
    (hM : ∀ (k : ℤ) (t : ℝ), t ∈ Icc (k : ℝ) ((k : ℝ) + 1) → w t ≤ M k)
    (hMs : Summable fun k : ℤ => C k * M k) :
    (S.sum (fun x => w (γ x)) : ℝ) ≤ ∑' k : ℤ, C k * M k := by
  have hpt : ∀ x ∈ S, w (γ x) ≤ M (ordinateBin (γ x)) := by
    intro x _hx
    exact hM _ _ (mem_Icc_of_ordinateBin (γ x))
  have hsum₁ : S.sum (fun x => w (γ x)) ≤
      S.sum (fun x => M (ordinateBin (γ x))) :=
    sum_le_sum hpt
  let g : α → ℤ := fun x => ordinateBin (γ x)
  let bins := S.image g
  have hfib := sum_fiber_mul S g M
  have hsum₂ :
      S.sum (fun x => M (g x)) ≤ ∑ k ∈ bins, C k * M k := by
    rw [hfib]
    refine sum_le_sum fun k _hk => ?_
    have hsub :
        S.filter (fun x => g x = k) ⊆
          S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1) := by
      intro x hx
      have hxS := (mem_filter.mp hx).1
      have hbin : g x = k := (mem_filter.mp hx).2
      have hm := mem_ordinateBin (γ x)
      have hm' : (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1 := by
        simpa [g, hbin] using hm
      exact mem_filter.mpr ⟨hxS, hm'⟩
    have hcard :
        ((S.filter (fun x => g x = k)).card : ℝ) ≤ C k :=
      (Nat.cast_le.mpr (Finset.card_le_card hsub)).trans (hC k)
    exact mul_le_mul_of_nonneg_right hcard (hM0 k)
  have hsum₄ : ∑ k ∈ bins, C k * M k ≤ ∑' k : ℤ, C k * M k :=
    hMs.sum_le_tsum _ (fun k _ => mul_nonneg (hC0 k) (hM0 k))
  calc
    (S.sum (fun x => w (γ x)) : ℝ) ≤ S.sum (fun x => M (g x)) := hsum₁
    _ ≤ ∑ k ∈ bins, C k * M k := hsum₂
    _ ≤ ∑' k : ℤ, C k * M k := hsum₄

/-! ## Increment majorant on every integer bin -/

noncomputable def gaborBinCountMajorant (k : ℤ) : ℝ :=
  2 * zetaZerosInDiskCardBoundInner * (1 + Real.log ((|k| : ℝ) + 3))

lemma gaborBinCountMajorant_nonneg (k : ℤ) :
    0 ≤ gaborBinCountMajorant k := by
  unfold gaborBinCountMajorant
  have hlog : 0 ≤ Real.log ((|k| : ℝ) + 3) :=
    Real.log_nonneg (by nlinarith [abs_nonneg (k : ℝ)])
  have hC := zetaZerosInDiskCardBoundInner_pos
  positivity

lemma mem_stripZerosWindow_of_critical {N : ℝ} {z : ℂ}
    (hz : IsCriticalStripZetaZero z)
    (hN : N ≤ z.im ∧ z.im ≤ N + 1) :
    z ∈ stripZerosWindow N := by
  have him : |z.im| ≤ |N| + 1 := by
    have hlo : -(|N| + 1) ≤ z.im := by
      have : -(|N| : ℝ) ≤ N := neg_abs_le N
      linarith [hN.1]
    have hhi : z.im ≤ |N| + 1 := by
      have : N + 1 ≤ |N| + 1 := by linarith [le_abs_self N]
      exact hN.2.trans this
    exact abs_le.mpr ⟨hlo, hhi⟩
  exact mem_stripZerosWindow.mpr ⟨mem_rect_of_criticalStrip hz him, hN⟩

lemma strip_zero_bin_card_le
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) (k : ℤ) :
    ((S.filter (fun ρ => (k : ℝ) < ρ.val.im ∧
        ρ.val.im ≤ (k : ℝ) + 1)).card : ℝ) ≤
      gaborBinCountMajorant k := by
  set Sk : Finset {z : ℂ // IsCriticalStripZetaZero z} :=
    S.filter fun ρ => (k : ℝ) < ρ.val.im ∧ ρ.val.im ≤ (k : ℝ) + 1
  have himage : Sk.image (fun ρ => ρ.val) ⊆ stripZerosWindow (k : ℝ) := by
    intro z hz
    obtain ⟨ρ, hρ, rfl⟩ := mem_image.mp hz
    have hbin := (mem_filter.mp hρ).2
    exact mem_stripZerosWindow_of_critical ρ.property ⟨hbin.1.le, hbin.2⟩
  have hinj : Function.Injective
      fun ρ : {z : ℂ // IsCriticalStripZetaZero z} => ρ.val :=
    fun _ _ h => Subtype.ext h
  have hcard := (Finset.card_image_of_injective Sk hinj).symm.trans_le
    (card_le_card himage)
  exact (Nat.cast_le.mpr hcard).trans (card_strip_window_le (k : ℝ))

/-! ## Endpoint Gaussian bounds on unit bins -/

lemma gaussWeight_eq_exp {c t : ℝ} (hc : 0 < c) :
    gaussWeight (1 / (2 * c)) 0 t = Real.exp (-c * t ^ 2) := by
  unfold gaussWeight
  simp only [sub_zero]
  have hden : 2 * (1 / (2 * c)) = 1 / c := by field_simp [hc.ne']
  rw [hden]
  field_simp [hc.ne']

lemma gauss_binMax_le_exp_nonneg {c : ℝ} (hc : 0 < c) {k : ℤ}
    (hk : 0 ≤ k) :
    gaussBinMax (1 / (2 * c)) 0 k ≤ Real.exp (-c * (k : ℝ) ^ 2) := by
  have ha : 0 < 1 / (2 * c) :=
    div_pos (by norm_num) (mul_pos (by norm_num) hc)
  refine csSup_le (gaussWeight_image_nonempty _ _ k) ?_
  intro y hy
  obtain ⟨t, ht, rfl⟩ := hy
  have ht0 : 0 ≤ t := le_trans (by exact_mod_cast hk) ht.1
  have hk0 : 0 ≤ (k : ℝ) := by exact_mod_cast hk
  have hsq : (k : ℝ) ^ 2 ≤ t ^ 2 :=
    sq_le_sq.mpr (by
      rw [abs_of_nonneg hk0, abs_of_nonneg ht0]
      exact ht.1)
  rw [gaussWeight_eq_exp hc]
  refine Real.exp_le_exp.mpr ?_
  have : -c * t ^ 2 = -(c * t ^ 2) := by ring
  have : -c * (k : ℝ) ^ 2 = -(c * (k : ℝ) ^ 2) := by ring
  linarith [mul_le_mul_of_nonneg_left hsq hc.le]

lemma gauss_binMax_le_exp_neg {c : ℝ} (hc : 0 < c) {k : ℤ}
    (hk : k < 0) :
    gaussBinMax (1 / (2 * c)) 0 k ≤
      Real.exp (-c * ((k : ℝ) + 1) ^ 2) := by
  have ha : 0 < 1 / (2 * c) :=
    div_pos (by norm_num) (mul_pos (by norm_num) hc)
  refine csSup_le (gaussWeight_image_nonempty _ _ k) ?_
  intro y hy
  obtain ⟨t, ht, rfl⟩ := hy
  have hk1 : (k : ℝ) + 1 ≤ 0 := by exact_mod_cast (Int.add_one_le_iff.mpr hk)
  have ht0 : t ≤ 0 := le_trans ht.2 hk1
  have hsq : ((k : ℝ) + 1) ^ 2 ≤ t ^ 2 :=
    sq_le_sq.mpr (by
      rw [abs_of_nonpos hk1, abs_of_nonpos ht0]
      linarith [ht.2])
  rw [gaussWeight_eq_exp hc]
  refine Real.exp_le_exp.mpr ?_
  have : -c * t ^ 2 = -(c * t ^ 2) := by ring
  have : -c * ((k : ℝ) + 1) ^ 2 = -(c * ((k : ℝ) + 1) ^ 2) := by ring
  linarith [mul_le_mul_of_nonneg_left hsq hc.le]

lemma summable_binCount_mul_gaussBinMax {c : ℝ} (hc : 0 < c) :
    Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k := by
  have ha : 0 < 1 / (2 * c) :=
    div_pos (by norm_num) (mul_pos (by norm_num) hc)
  have hpos := summable_log_mul_gauss (c := c) (b := 3) hc (by norm_num)
  have hneg := summable_log_mul_gauss (c := c) (b := 4) hc (by norm_num)
  have hC : 0 ≤ 2 * zetaZerosInDiskCardBoundInner :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  set g3 : ℕ → ℝ := fun n =>
    (1 + Real.log ((n : ℝ) + 3)) * Real.exp (-c * (n : ℝ) ^ 2)
  set g4 : ℕ → ℝ := fun n =>
    (1 + Real.log ((n : ℝ) + 4)) * Real.exp (-c * (n : ℝ) ^ 2)
  have hg3 : ∀ n, 0 ≤ g3 n :=
    fun n => mul_nonneg (log_add_b_nonneg (by norm_num) n) (Real.exp_pos _).le
  have hg4 : ∀ n, 0 ≤ g4 n :=
    fun n => mul_nonneg (log_add_b_nonneg (by norm_num) n) (Real.exp_pos _).le
  set bound : ℝ :=
    (2 * zetaZerosInDiskCardBoundInner) * (∑' n : ℕ, g3 n + ∑' n : ℕ, g4 n)
  have hK : ∀ K : Finset ℤ,
      ∑ k ∈ K, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k ≤
        bound := by
    intro K
    let Kp := K.filter fun k : ℤ => 0 ≤ k
    let Kn := K.filter fun k : ℤ => k < 0
    have hunion : Kp ∪ Kn = K := by
      ext k
      constructor
      · intro hk
        rcases mem_union.mp hk with h | h
        · exact (mem_filter.mp h).1
        · exact (mem_filter.mp h).1
      · intro hk
        by_cases h : 0 ≤ k
        · exact mem_union.mpr (Or.inl (mem_filter.mpr ⟨hk, h⟩))
        · exact mem_union.mpr (Or.inr (mem_filter.mpr ⟨hk, lt_of_not_ge h⟩))
    have hdisj : Disjoint Kp Kn := by
      refine disjoint_left.mpr ?_
      intro k hkp hkn
      exact (not_lt_of_ge (mem_filter.mp hkp).2) (mem_filter.mp hkn).2
    have hsplit :
        ∑ k ∈ K, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k =
          ∑ k ∈ Kp, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k +
            ∑ k ∈ Kn, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k := by
      rw [← hunion, sum_union hdisj]
    set g3 : ℕ → ℝ := fun n =>
      (1 + Real.log ((n : ℝ) + 3)) * Real.exp (-c * (n : ℝ) ^ 2)
    set g4 : ℕ → ℝ := fun n =>
      (1 + Real.log ((n : ℝ) + 4)) * Real.exp (-c * (n : ℝ) ^ 2)
    have hg3 : ∀ n, 0 ≤ g3 n :=
      fun n => mul_nonneg (log_add_b_nonneg (by norm_num) n) (Real.exp_pos _).le
    have hg4 : ∀ n, 0 ≤ g4 n :=
      fun n => mul_nonneg (log_add_b_nonneg (by norm_num) n) (Real.exp_pos _).le
    have htermP : ∀ k ∈ Kp,
        gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) * g3 k.toNat := by
      intro k hk
      have hk0 : 0 ≤ k := (mem_filter.mp hk).2
      have hM := gauss_binMax_le_exp_nonneg hc hk0
      have hto : (k.toNat : ℝ) = (k : ℝ) := by
        exact_mod_cast (Int.toNat_of_nonneg hk0)
      have habs : (|k| : ℝ) = (k : ℝ) := abs_of_nonneg (by exact_mod_cast hk0)
      unfold gaborBinCountMajorant g3
      rw [hto, habs]
      have : (2 * zetaZerosInDiskCardBoundInner) *
            (1 + Real.log ((k : ℝ) + 3)) * gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) *
            (1 + Real.log ((k : ℝ) + 3)) * Real.exp (-c * (k : ℝ) ^ 2) :=
        mul_le_mul_of_nonneg_left hM (mul_nonneg hC (by
          have hkR : 0 ≤ (k : ℝ) := by exact_mod_cast hk0
          have : 0 ≤ Real.log ((k : ℝ) + 3) :=
            Real.log_nonneg (by nlinarith [hkR])
          linarith))
      simpa [mul_assoc] using this
    have htermN : ∀ k ∈ Kn,
        gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) *
            g4 (Int.toNat (-(k + 1))) := by
      intro k hk
      have hk0 : k < 0 := (mem_filter.mp hk).2
      have hM := gauss_binMax_le_exp_neg hc hk0
      have hn : 0 ≤ -(k + 1) := by omega
      have hto : ((Int.toNat (-(k + 1))) : ℝ) = -((k : ℝ) + 1) := by
        have hcast : ((Int.toNat (-(k + 1))) : ℤ) = -(k + 1) :=
          Int.toNat_of_nonneg hn
        have : ((Int.toNat (-(k + 1))) : ℝ) = ((-(k + 1) : ℤ) : ℝ) := by
          exact_mod_cast hcast
        rw [this]
        push_cast
        ring
      have habs : (|k| : ℝ) = -(k : ℝ) :=
        abs_of_neg (by exact_mod_cast hk0)
      have hlog : (|k| : ℝ) + 3 = ((Int.toNat (-(k + 1))) : ℝ) + 4 := by
        rw [habs, hto]; ring
      have hsq : ((k : ℝ) + 1) ^ 2 = ((Int.toNat (-(k + 1))) : ℝ) ^ 2 := by
        calc
          ((k : ℝ) + 1) ^ 2 = (-((k : ℝ) + 1)) ^ 2 := (neg_sq _).symm
          _ = ((Int.toNat (-(k + 1))) : ℝ) ^ 2 := by rw [hto]
      unfold gaborBinCountMajorant g4
      rw [hlog]
      have : (2 * zetaZerosInDiskCardBoundInner) *
            (1 + Real.log (((Int.toNat (-(k + 1))) : ℝ) + 4)) *
              gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) *
            (1 + Real.log (((Int.toNat (-(k + 1))) : ℝ) + 4)) *
              Real.exp (-c * ((k : ℝ) + 1) ^ 2) :=
        mul_le_mul_of_nonneg_left hM (mul_nonneg hC (by
          have : 0 ≤ Real.log (((Int.toNat (-(k + 1))) : ℝ) + 4) :=
            Real.log_nonneg (by
              have hnR : (0 : ℝ) ≤ ((Int.toNat (-(k + 1))) : ℝ) :=
                Nat.cast_nonneg _
              have : (1 : ℝ) ≤ ((Int.toNat (-(k + 1))) : ℝ) + 4 := by
                linarith [hnR]
              exact this)
          linarith))
      rw [hsq] at this
      simpa [mul_assoc] using this
    have hsumP :
        ∑ k ∈ Kp, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) * ∑' n : ℕ, g3 n := by
      have hle := sum_le_sum htermP
      have himage :
          ∑ k ∈ Kp, (2 * zetaZerosInDiskCardBoundInner) * g3 k.toNat =
            (2 * zetaZerosInDiskCardBoundInner) *
              ∑ k ∈ Kp, g3 k.toNat := by
        simp [mul_sum]
      have hinj : ∀ k₁ ∈ Kp, ∀ k₂ ∈ Kp, k₁.toNat = k₂.toNat → k₁ = k₂ := by
        intro k₁ hk₁ k₂ hk₂ h
        have h1 : 0 ≤ k₁ := (mem_filter.mp hk₁).2
        have h2 : 0 ≤ k₂ := (mem_filter.mp hk₂).2
        have hk1 : (k₁.toNat : ℤ) = k₁ := Int.toNat_of_nonneg h1
        have hk2 : (k₂.toNat : ℤ) = k₂ := Int.toNat_of_nonneg h2
        exact_mod_cast (by
          have : (k₁.toNat : ℤ) = (k₂.toNat : ℤ) := by exact_mod_cast h
          rw [hk1, hk2] at this
          exact this)
      have hsumg : ∑ k ∈ Kp, g3 k.toNat =
          ∑ n ∈ Kp.image Int.toNat, g3 n :=
        (sum_image hinj).symm
      have hts : ∑ n ∈ Kp.image Int.toNat, g3 n ≤ ∑' n : ℕ, g3 n :=
        hpos.sum_le_tsum _ (fun n _ => hg3 n)
      calc
        _ ≤ ∑ k ∈ Kp, (2 * zetaZerosInDiskCardBoundInner) * g3 k.toNat := hle
        _ = (2 * zetaZerosInDiskCardBoundInner) * ∑ k ∈ Kp, g3 k.toNat :=
          himage
        _ = (2 * zetaZerosInDiskCardBoundInner) *
              ∑ n ∈ Kp.image Int.toNat, g3 n := by rw [hsumg]
        _ ≤ (2 * zetaZerosInDiskCardBoundInner) * ∑' n : ℕ, g3 n :=
          mul_le_mul_of_nonneg_left hts hC
    have hsumN :
        ∑ k ∈ Kn, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k ≤
          (2 * zetaZerosInDiskCardBoundInner) * ∑' n : ℕ, g4 n := by
      have hle := sum_le_sum htermN
      let φ : ℤ → ℕ := fun k => Int.toNat (-(k + 1))
      have himage :
          ∑ k ∈ Kn, (2 * zetaZerosInDiskCardBoundInner) * g4 (φ k) =
            (2 * zetaZerosInDiskCardBoundInner) * ∑ k ∈ Kn, g4 (φ k) := by
        simp [mul_sum, φ]
      have hinj : ∀ k₁ ∈ Kn, ∀ k₂ ∈ Kn, φ k₁ = φ k₂ → k₁ = k₂ := by
        intro k₁ hk₁ k₂ hk₂ h
        have h1 : 0 ≤ -(k₁ + 1) := by
          have : k₁ < 0 := (mem_filter.mp hk₁).2
          omega
        have h2 : 0 ≤ -(k₂ + 1) := by
          have : k₂ < 0 := (mem_filter.mp hk₂).2
          omega
        have ht1 := Int.toNat_of_nonneg h1
        have ht2 := Int.toNat_of_nonneg h2
        have : -(k₁ + 1) = -(k₂ + 1) := by
          calc
            -(k₁ + 1) = ((-(k₁ + 1)).toNat : ℤ) := ht1.symm
            _ = ((-(k₂ + 1)).toNat : ℤ) := by exact_mod_cast h
            _ = -(k₂ + 1) := ht2
        omega
      have hsumg : ∑ k ∈ Kn, g4 (φ k) = ∑ n ∈ Kn.image φ, g4 n :=
        (sum_image hinj).symm
      have hts : ∑ n ∈ Kn.image φ, g4 n ≤ ∑' n : ℕ, g4 n :=
        hneg.sum_le_tsum _ (fun n _ => hg4 n)
      calc
        _ ≤ ∑ k ∈ Kn, (2 * zetaZerosInDiskCardBoundInner) * g4 (φ k) := hle
        _ = (2 * zetaZerosInDiskCardBoundInner) * ∑ k ∈ Kn, g4 (φ k) :=
          himage
        _ = (2 * zetaZerosInDiskCardBoundInner) * ∑ n ∈ Kn.image φ, g4 n := by
          rw [hsumg]
        _ ≤ (2 * zetaZerosInDiskCardBoundInner) * ∑' n : ℕ, g4 n :=
          mul_le_mul_of_nonneg_left hts hC
    rw [hsplit]
    unfold bound
    linarith [hsumP, hsumN]
  exact summable_of_sum_le
    (fun k => mul_nonneg (gaborBinCountMajorant_nonneg k)
      (gaussBinMax_nonneg ha k)) hK

/-! ## Summability of ĥ_W(ρ) -/

theorem norm_gaborHat_le_gauss_critical
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ ρ : ℂ, IsCriticalStripZetaZero ρ →
        ‖gaborHat F ρ‖ ≤ C * Real.exp (-c * ρ.im ^ 2) := by
  obtain ⟨c, C, hc, hC, hbd⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF 0 1
  refine ⟨c, C, hc, hC, ?_⟩
  intro ρ hρ
  simpa [Complex.re_add_im ρ] using
    hbd ρ.re ρ.im (le_of_lt hρ.2.1) (le_of_lt hρ.2.2)

lemma summable_gauss_over_zeros {c : ℝ} (hc : 0 < c) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      Real.exp (-c * (ρ : ℂ).im ^ 2) := by
  have ha : 0 < 1 / (2 * c) :=
    div_pos (by norm_num) (mul_pos (by norm_num) hc)
  have hMs := summable_binCount_mul_gaussBinMax hc
  have hS : ∀ S : Finset {z : ℂ // IsCriticalStripZetaZero z},
      ∑ ρ ∈ S, Real.exp (-c * (ρ : ℂ).im ^ 2) ≤
        ∑' k : ℤ, gaborBinCountMajorant k * gaussBinMax (1 / (2 * c)) 0 k :=
    fun S =>
      bin_partial_summation_weighted
        (w := fun t => Real.exp (-c * t ^ 2))
        (fun _ => (Real.exp_pos _).le)
        S (fun ρ => (ρ : ℂ).im)
        gaborBinCountMajorant gaborBinCountMajorant_nonneg
        (fun k => strip_zero_bin_card_le S k)
        (fun k => gaussBinMax_nonneg ha k)
        (fun k t ht => by
          have := le_gaussBinMax (a := 1 / (2 * c)) (c := 0) ha ht
          rw [gaussWeight_eq_exp hc] at this
          exact this)
        hMs
  exact summable_of_sum_le (fun _ => (Real.exp_pos _).le) hS

/-- The family `ρ ↦ ĥ_W(ρ)` over critical-strip zeros is (absolutely)
summable for every pure Gabor test. -/
theorem summable_gaborHat_over_zeros
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      gaborHat F (ρ : ℂ) := by
  obtain ⟨c, C, hc, hC, hbd⟩ := norm_gaborHat_le_gauss_critical hF
  have hnorm : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      ‖gaborHat F (ρ : ℂ)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun ρ => hbd ρ ρ.property)
      ((summable_gauss_over_zeros hc).mul_left C)
  exact hnorm.of_norm

/-- Named remainder: the same family for a general even quartic, once
the coefficient-dependent three-lobe majorant is available.  Discharged
by `gaborHatQuarticZeroSummableRemainder_holds`. -/
def GaborHatQuarticZeroSummableRemainder : Prop :=
  ∀ F : GaborWeilTest,
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      gaborHat F (ρ : ℂ)

theorem norm_gaborHat_le_gauss_critical_quartic (F : GaborWeilTest) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ ρ : ℂ, IsCriticalStripZetaZero ρ →
        ‖gaborHat F ρ‖ ≤ C * Real.exp (-c * ρ.im ^ 2) := by
  have ha : 0 < F.a := F.a_pos
  obtain ⟨K, hK0, hK⟩ := one_add_abs_pow_mul_gauss
    (c := 1 / (4 * F.a)) (div_pos (by norm_num) (mul_pos (by norm_num) ha)) 8
  set Cthree : ℝ :=
    Real.pi / (4 * F.a) * Real.exp ((1 / 2 : ℝ) ^ 2 / (2 * F.a))
  set Cfac : ℝ :=
    1 + gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
      (1 + (1 / 2 : ℝ) + |F.omega|) ^ 8
  set Cσ : ℝ := Cthree * Cfac
  set Cg : ℝ := 4 * Real.exp (F.omega ^ 2 / (2 * F.a))
  have hCthree0 : 0 ≤ Cthree := by unfold Cthree; positivity
  have hCfac0 : 0 ≤ Cfac := by unfold Cfac; positivity
  have hCσ0 : 0 ≤ Cσ := mul_nonneg hCthree0 hCfac0
  have hCg0 : 0 ≤ Cg := by unfold Cg; positivity
  have hC : 0 < Cσ * Cg * K + 1 := by
    have : 0 ≤ Cσ * Cg * K :=
      mul_nonneg (mul_nonneg hCσ0 hCg0) hK0
    linarith
  refine ⟨1 / (8 * F.a), Cσ * Cg * K + 1,
    div_pos (by norm_num) (mul_pos (by norm_num) ha), hC, ?_⟩
  intro ρ hρ
  have hpoly := norm_gaborHat_le_poly_three_lobe F ρ
  have hre : |ρ.re - 1 / 2| ≤ (1 / 2 : ℝ) :=
    abs_le.mpr ⟨by linarith [hρ.2.1], by linarith [hρ.2.2]⟩
  have hCthree : gaborHatThreeLobeConst F.a ρ.re ≤ Cthree := by
    unfold gaborHatThreeLobeConst Cthree
    apply mul_le_mul_of_nonneg_left ?_
      (div_nonneg Real.pi_pos.le (by positivity))
    apply Real.exp_le_exp.mpr
    refine div_le_div_of_nonneg_right ?_ (by positivity)
    have habs : |ρ.re - 1 / 2| ≤ |(1 / 2 : ℝ)| := by
      simpa [abs_of_nonneg (by norm_num : (0 : ℝ) ≤ (1 / 2 : ℝ))] using hre
    exact sq_le_sq.mpr habs
  have hCfac :
      1 + gaussianPolynomialFactorBound F.coeffs F.a ^ 2 *
          (1 + |ρ.re - 1 / 2| + |F.omega|) ^ 8 ≤ Cfac := by
    unfold Cfac
    have harg : 1 + |ρ.re - 1 / 2| + |F.omega| ≤
        1 + (1 / 2 : ℝ) + |F.omega| := by linarith [hre]
    exact add_le_add le_rfl
      (mul_le_mul_of_nonneg_left
        (pow_le_pow_left₀ (by positivity) harg 8) (sq_nonneg _))
  have hCσ : gaborHatQuarticThreeLobeConst F ρ.re ≤ Cσ := by
    unfold gaborHatQuarticThreeLobeConst Cσ
    exact mul_le_mul hCthree hCfac (by positivity) hCthree0
  have hlobe : gaborThreeLobe F.a F.omega ρ.im ≤
      Cg * Real.exp (-ρ.im ^ 2 / (4 * F.a)) := by
    unfold Cg
    exact gaborThreeLobe_le_gaussian F.a F.omega ρ.im ha
  have hl0 : 0 ≤ gaborThreeLobe F.a F.omega ρ.im :=
    gaborThreeLobe_nonneg F.a F.omega ρ.im
  have hpow0 : 0 ≤ (1 + |ρ.im|) ^ 8 := by positivity
  have h1 :
      gaborHatQuarticThreeLobeConst F ρ.re * (1 + |ρ.im|) ^ 8 *
          gaborThreeLobe F.a F.omega ρ.im ≤
        Cσ * (1 + |ρ.im|) ^ 8 * gaborThreeLobe F.a F.omega ρ.im :=
    mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_right hCσ hpow0) hl0
  have h2 :
      Cσ * (1 + |ρ.im|) ^ 8 * gaborThreeLobe F.a F.omega ρ.im ≤
        Cσ * (1 + |ρ.im|) ^ 8 *
          (Cg * Real.exp (-ρ.im ^ 2 / (4 * F.a))) :=
    mul_le_mul_of_nonneg_left hlobe (mul_nonneg hCσ0 hpow0)
  have hrate : Real.exp (-ρ.im ^ 2 / (4 * F.a)) =
      Real.exp (-(1 / (4 * F.a)) * ρ.im ^ 2) := by
    congr 1
    field_simp [ha.ne']
  have hrew :
      Cσ * (1 + |ρ.im|) ^ 8 *
          (Cg * Real.exp (-ρ.im ^ 2 / (4 * F.a))) =
        (Cσ * Cg) * ((1 + |ρ.im|) ^ 8 *
          Real.exp (-(1 / (4 * F.a)) * ρ.im ^ 2)) := by
    rw [hrate]
    ring
  have hsw :
      (Cσ * Cg) * ((1 + |ρ.im|) ^ 8 *
          Real.exp (-(1 / (4 * F.a)) * ρ.im ^ 2)) ≤
        (Cσ * Cg * K) * Real.exp (-((1 / (4 * F.a)) / 2) * ρ.im ^ 2) := by
    have := mul_le_mul_of_nonneg_left (hK ρ.im) (mul_nonneg hCσ0 hCg0)
    simpa [mul_assoc] using this
  have hhalf : Real.exp (-((1 / (4 * F.a)) / 2) * ρ.im ^ 2) =
      Real.exp (-(1 / (8 * F.a)) * ρ.im ^ 2) := by
    congr 1
    have : -((1 / (4 * F.a)) / 2) = -(1 / (8 * F.a)) := by
      field_simp [ha.ne']
      norm_num
    rw [this]
  have hbound :
      ‖gaborHat F ρ‖ ≤
        (Cσ * Cg * K) * Real.exp (-(1 / (8 * F.a)) * ρ.im ^ 2) := by
    refine hpoly.trans ?_
    refine h1.trans (h2.trans ?_)
    rw [hrew]
    refine hsw.trans_eq ?_
    rw [hhalf]
  exact hbound.trans (mul_le_mul_of_nonneg_right (by linarith)
    (Real.exp_pos _).le)

theorem summable_gaborHat_over_zeros_quartic (F : GaborWeilTest) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      gaborHat F (ρ : ℂ) := by
  obtain ⟨c, C, hc, hC, hbd⟩ := norm_gaborHat_le_gauss_critical_quartic F
  have hnorm : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      ‖gaborHat F (ρ : ℂ)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun ρ => hbd ρ ρ.property)
      ((summable_gauss_over_zeros hc).mul_left C)
  exact hnorm.of_norm

theorem gaborHatQuarticZeroSummableRemainder_holds :
    GaborHatQuarticZeroSummableRemainder :=
  summable_gaborHat_over_zeros_quartic

#print axioms norm_gaborHat_le_gauss_critical_quartic
#print axioms summable_gaborHat_over_zeros_quartic
#print axioms gaborHatQuarticZeroSummableRemainder_holds

end RH
