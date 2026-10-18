/-
RH/GaborSpectralBridge.lean -- r579 spectral-side bridges; r584
tsum≤Closed attachment; r585 conj/star/quadrupole and Bridge-2
tsum+multiplicity (`GaborCriticalLineMassLeLogMajorant`); r588
HasSum exhaustion of the FD windows and real-axis mass vanishing;
r589 window→canonical BoundLog2 hypotheses and the honest
(window-dependent packet) negativity form.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r573 audit gaps attacked here (no new `sorry`):

  Bridge 2 (on-line majorant, log occupancy).  The r552 discrete
  transfer demanded a *constant* bin cap `≤ 2 C_inner`.  The Path-A
  theorem supplies only the log increment.  `RH.GaborInequality`
  now contains the log-weighted Finset transfer
      Σ gaussWeight ≤ ∑_k C(k) · binMax(k)
  (`gauss_density_transfer_binMax_log`).  This file specialises it
  to Path-A `gaborBinCountMajorant`, proves the three-lobe form,
  and the unweighted Finset `|ĥ|` bound.  The tsum+multiplicity
  lift is `GaborCriticalLineMassLeLogMajorant`.  Summability of
  the log-weighted bin-max series is the theorem
  `gaborLogWeightedThetaSummable` (r580).  The multiplicity-
  weighted `ĥ` series is `gaborMultiplicityWeightedHatSummable`.

  Bridge 5 remainder (truncation compliance).  Every finite
  FE-folded window of genuine strip zeros, unweighted
  multiplicity 1, is `GaborConfigIncrementCompliantLog`.
  Weighted (analytic-order) occupancy is
  `GaborTruncationWeightedCompliant`.

  Bridge 6 (Finset → full set).  If every truncation scores
  `W_honest ≤ -δ` against a fixed packet, the quadrupole partial
  sums cannot exceed `-δ - R_on`.  The comparison algebra is
  proved; the identification is
  `GaborQuadrupoleLimitEqOffLineMass`.

gammaDistinct is used only for host-ordinate isolation
(`gammaHostIsolated`): T_gap = 0 and foreign-not-in-peak.  Packing
already sums every point in a bin.  The γ = 0 gap stays in
`GaborIsolationArithmeticImpliesScalingArithmetic`.2.

No asserting `sorry`.
-/
import RH.GaborDominanceLog
import RH.GaborFEMultiplicity
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical ComplexConjugate
open Set Finset Filter
open scoped Topology

/-! ## Log-weighted Jacobi-theta series -/

noncomputable def gaborLogWeightedTheta (a c : ℝ) : ℝ :=
  ∑' k : ℤ, gaborBinCountMajorant k * gaussBinMax a c k

lemma gaborKBinAt_eq_binCountMajorant (k : ℤ) :
    gaborKBinAt (|k| : ℝ) = gaborBinCountMajorant k := by
  unfold gaborKBinAt gaborBinCountMajorant
  rfl

lemma abs_sub_ge_bin_dist (k : ℤ) (c t : ℝ)
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1)) :
    (|k| : ℝ) - |c| - 1 ≤ |t - c| := by
  have htk : |t - (k : ℝ)| ≤ 1 := by
    rw [abs_le]
    constructor <;> linarith [ht.1, ht.2]
  have htri : |(k : ℝ) - c| ≤ |t - (k : ℝ)| + |t - c| := by
    simpa [abs_sub_comm t (k : ℝ)] using abs_sub_le (k : ℝ) t c
  have hkc : (|k| : ℝ) - |c| ≤ |(k : ℝ) - c| :=
    abs_sub_abs_le_abs_sub (k : ℝ) c
  linarith [htk, htri, hkc]

lemma gaussBinMax_le_exp_hostDist {a c : ℝ} (ha : 0 < a) (k : ℤ) :
    gaussBinMax a c k ≤
      Real.exp
        (-(max (0 : ℝ) ((|k| : ℝ) - |c| - 1)) ^ 2 / (2 * a)) := by
  set d : ℝ := max 0 ((|k| : ℝ) - |c| - 1)
  have hd0 : 0 ≤ d := le_max_left _ _
  have hdist : ∀ t ∈ Icc (k : ℝ) ((k : ℝ) + 1), d ≤ |t - c| := by
    intro t ht
    exact max_le (abs_nonneg _) (abs_sub_ge_bin_dist k c t ht)
  exact gaussBinMax_le_exp ha k hd0 hdist

lemma hostDist_half {c : ℝ} {k : ℤ}
    (hk : 2 * (|c| + 1) ≤ (|k| : ℝ)) :
    (|k| : ℝ) / 2 ≤ (|k| : ℝ) - |c| - 1 := by
  linarith

lemma summable_nat_linear_gauss_sq {a : ℝ} (ha : 0 < a) :
    Summable fun n : ℕ =>
      ((n : ℝ) + 3) * Real.exp (-((n : ℝ) ^ 2) / (8 * a)) := by
  have hc : 0 < 1 / (8 * a) :=
    div_pos (by norm_num) (mul_pos (by norm_num) ha)
  have hlin :=
    summable_nat_add_const_exp_neg (c := 1 / (8 * a)) (A := (3 : ℝ)) hc
  refine Summable.of_nonneg_of_le (fun _ => by positivity) (fun n => ?_) hlin
  have hexp : Real.exp (-((n : ℝ) ^ 2) / (8 * a)) ≤
      Real.exp (-(1 / (8 * a)) * (n : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    have hden : 0 < 8 * a := mul_pos (by norm_num) ha
    have hsq : (n : ℝ) ≤ (n : ℝ) ^ 2 := by
      have : 0 ≤ (n : ℝ) * ((n : ℝ) - 1) := by
        rcases Nat.eq_zero_or_pos n with hn | hn
        · subst n; simp
        · exact mul_nonneg (Nat.cast_nonneg n)
            (sub_nonneg.mpr (Nat.one_le_cast.mpr hn))
      nlinarith
    have hdiv : -((n : ℝ) ^ 2) / (8 * a) ≤ -(n : ℝ) / (8 * a) :=
      div_le_div_of_nonneg_right (neg_le_neg hsq) hden.le
    have hrhs : -(1 / (8 * a)) * (n : ℝ) = -(n : ℝ) / (8 * a) := by
      field_simp [hden.ne']
    exact hdiv.trans_eq hrhs.symm
  exact mul_le_mul_of_nonneg_left hexp (by positivity)

lemma binCount_mul_binMax_le_far {a c : ℝ} (ha : 0 < a) {k : ℤ}
    (hk : 2 * (|c| + 1) ≤ (|k| : ℝ)) :
    gaborBinCountMajorant k * gaussBinMax a c k ≤
      (2 * zetaZerosInDiskCardBoundInner) * ((|k| : ℝ) + 3) *
        Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) := by
  have hC : 0 ≤ 2 * zetaZerosInDiskCardBoundInner :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hlin : gaborBinCountMajorant k ≤
      2 * zetaZerosInDiskCardBoundInner * ((|k| : ℝ) + 3) := by
    simpa [gaborKBinAt_eq_binCountMajorant] using gaborKBinAt_le_linear k
  have hdpos : 0 ≤ (|k| : ℝ) - |c| - 1 :=
    le_trans (div_nonneg (abs_nonneg _) (by norm_num)) (hostDist_half hk)
  have hM := gaussBinMax_le_exp_hostDist (a := a) (c := c) ha k
  have hmax : max (0 : ℝ) ((|k| : ℝ) - |c| - 1) =
      (|k| : ℝ) - |c| - 1 := max_eq_right hdpos
  rw [hmax] at hM
  have hhalf := hostDist_half (c := c) hk
  have hsq : ((|k| : ℝ) / 2) ^ 2 ≤ ((|k| : ℝ) - |c| - 1) ^ 2 :=
    sq_le_sq.mpr (by
      rw [abs_of_nonneg (div_nonneg (abs_nonneg _) (by norm_num)),
        abs_of_nonneg hdpos]
      exact hhalf)
  have hexp : Real.exp (-((|k| : ℝ) - |c| - 1) ^ 2 / (2 * a)) ≤
      Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) := by
    refine Real.exp_le_exp.mpr ?_
    have hden : 0 < 2 * a := mul_pos (by norm_num) ha
    have := div_le_div_of_nonneg_right (neg_le_neg hsq) hden.le
    have hr : -((|k| : ℝ) / 2) ^ 2 / (2 * a) =
        -((|k| : ℝ) ^ 2) / (8 * a) := by
      field_simp [ne_of_gt hden, ne_of_gt ha]
      ring
    exact this.trans_eq hr
  have hleft : 0 ≤
      2 * zetaZerosInDiskCardBoundInner * ((|k| : ℝ) + 3) :=
    mul_nonneg hC (add_nonneg (abs_nonneg _) (by norm_num))
  have hprod :
      gaborBinCountMajorant k * gaussBinMax a c k ≤
        (2 * zetaZerosInDiskCardBoundInner * ((|k| : ℝ) + 3)) *
          Real.exp (-((|k| : ℝ) - |c| - 1) ^ 2 / (2 * a)) :=
    mul_le_mul hlin hM (gaussBinMax_nonneg ha k) hleft
  exact hprod.trans (mul_le_mul_of_nonneg_left hexp hleft)

lemma summable_int_linear_gauss_sq {a : ℝ} (ha : 0 < a) :
    Summable fun k : ℤ =>
      ((|k| : ℝ) + 3) * Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) := by
  let f : ℤ → ℝ := fun k =>
    ((|k| : ℝ) + 3) * Real.exp (-((|k| : ℝ) ^ 2) / (8 * a))
  have hnat := summable_nat_linear_gauss_sq ha
  have hpos : Summable fun n : ℕ => f n := by
    refine hnat.congr fun n => ?_
    have hn : |((n : ℤ) : ℝ)| = (n : ℝ) := by
      rw [Int.cast_natCast, abs_of_nonneg (Nat.cast_nonneg n)]
    change ((n : ℝ) + 3) * Real.exp (-((n : ℝ) ^ 2) / (8 * a)) =
      (|((n : ℤ) : ℝ)| + 3) *
        Real.exp (-(|((n : ℤ) : ℝ)| ^ 2) / (8 * a))
    rw [hn]
  have hneg : Summable fun n : ℕ => f (-(n + 1)) := by
    have hshift : Summable fun n : ℕ =>
        (((n + 1 : ℕ) : ℝ) + 3) *
          Real.exp (-(((n + 1 : ℕ) : ℝ) ^ 2) / (8 * a)) :=
      (summable_nat_add_iff (f := fun n : ℕ =>
        ((n : ℝ) + 3) * Real.exp (-((n : ℝ) ^ 2) / (8 * a))) 1).mpr hnat
    refine hshift.congr fun n => ?_
    simp only [f]
    rw [Int.cast_neg, abs_neg]
    have hn : ((n + 1 : ℤ) : ℝ) = ((n + 1 : ℕ) : ℝ) :=
      Int.cast_natCast (n + 1)
    rw [hn, abs_of_nonneg (Nat.cast_nonneg (n + 1))]
  exact Summable.of_nat_of_neg_add_one (f := f) hpos hneg

lemma far_bins_finite (c : ℝ) :
    {k : ℤ | (|k| : ℝ) < 2 * (|c| + 1)}.Finite := by
  set R : ℝ := 2 * (|c| + 1)
  let N : ℤ := Int.ceil R
  have hsub : {k : ℤ | (|k| : ℝ) < R} ⊆ Set.Icc (-N) N := by
    intro k hk
    have hle : (|k| : ℝ) ≤ (N : ℝ) :=
      hk.le.trans (Int.le_ceil R)
    have habs : |k| ≤ N := by exact_mod_cast hle
    exact abs_le.mp habs
  exact (Set.finite_Icc (-N) N).subset hsub

/-- Path-A log occupancy times a general-center Gaussian bin-max
is summable: far bins compare to the linear-Gaussian majorant
(`summable_int_linear_gauss_sq`); the near fiber is finite. -/
def GaborLogWeightedThetaSummable : Prop :=
  ∀ {a : ℝ}, 0 < a → ∀ c : ℝ,
    Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a c k

theorem gaborLogWeightedThetaSummable :
    GaborLogWeightedThetaSummable := by
  intro a ha c
  have hmaj :=
    (summable_int_linear_gauss_sq ha).mul_left
      (2 * zetaZerosInDiskCardBoundInner)
  refine Summable.of_norm_bounded_eventually hmaj ?_
  have hfin := far_bins_finite c
  have hev : ∀ᶠ k : ℤ in Filter.cofinite,
      2 * (|c| + 1) ≤ (|k| : ℝ) := by
    filter_upwards [hfin.compl_mem_cofinite] with k hk
    exact not_lt.mp hk
  filter_upwards [hev] with k hk
  have hfar := binCount_mul_binMax_le_far (a := a) (c := c) ha hk
  have hnn : 0 ≤
      gaborBinCountMajorant k * gaussBinMax a c k :=
    mul_nonneg (gaborBinCountMajorant_nonneg k) (gaussBinMax_nonneg ha k)
  have hassoc :
      (2 * zetaZerosInDiskCardBoundInner) * ((|k| : ℝ) + 3) *
          Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) =
        (2 * zetaZerosInDiskCardBoundInner) *
          (((|k| : ℝ) + 3) *
            Real.exp (-((|k| : ℝ) ^ 2) / (8 * a))) := by
    ring
  rw [Real.norm_eq_abs, abs_of_nonneg hnn]
  exact hfar.trans_eq hassoc

/-- r579 log discrete transfer, specialised to Path-A occupancy.
Summability of the majorant is `gaborLogWeightedThetaSummable`. -/
theorem gauss_density_transfer_binCount_of_summable
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        gaborBinCountMajorant k)
    (hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a c k) :
    (S.sum (gaussWeight a c) : ℝ) ≤ gaborLogWeightedTheta a c :=
  gauss_density_transfer_binMax_log ha c S gaborBinCountMajorant
    gaborBinCountMajorant_nonneg hinc hMs

theorem gauss_density_transfer_stripZeros_of_summable
    {a : ℝ} (ha : 0 < a) (c : ℝ)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a c k) :
    (S.sum (fun ρ => gaussWeight a c (ρ : ℂ).im) : ℝ) ≤
      gaborLogWeightedTheta a c :=
  gauss_online_mass_varC ha c S (fun ρ => (ρ : ℂ).im)
    gaborBinCountMajorant gaborBinCountMajorant_nonneg
    (fun k => strip_zero_bin_card_le S k) hMs

theorem gaborThreeLobe_eq_gauss (a omega t : ℝ) :
    gaborThreeLobe a omega t =
      gaussWeight a omega t + gaussWeight a (-omega) t +
        2 * Real.exp (-omega ^ 2 / (2 * a)) * gaussWeight a 0 t := by
  unfold gaborThreeLobe gaussWeight
  have hneg : t - (-omega) = t + omega := by ring
  have h0 : t - 0 = t := by ring
  rw [hneg, h0]
  have hmid : Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) =
      Real.exp (-omega ^ 2 / (2 * a)) * Real.exp (-t ^ 2 / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    ring
  rw [hmid]
  ring

noncomputable def gaborLogThreeLobeMajorant (a omega : ℝ) : ℝ :=
  gaborLogWeightedTheta a omega + gaborLogWeightedTheta a (-omega) +
    2 * Real.exp (-omega ^ 2 / (2 * a)) * gaborLogWeightedTheta a 0

theorem threeLobe_finset_le_logMajorant_of_summable
    {a omega : ℝ} (ha : 0 < a) (S : Finset ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        gaborBinCountMajorant k)
    (hMsω : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a omega k)
    (hMsω' : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a (-omega) k)
    (hMs0 : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a 0 k) :
    S.sum (gaborThreeLobe a omega) ≤ gaborLogThreeLobeMajorant a omega := by
  have hω := gauss_density_transfer_binCount_of_summable ha omega S hinc hMsω
  have hω' :=
    gauss_density_transfer_binCount_of_summable ha (-omega) S hinc hMsω'
  have h0 := gauss_density_transfer_binCount_of_summable ha 0 S hinc hMs0
  have hcongr : S.sum (gaborThreeLobe a omega) =
      S.sum (fun t =>
        gaussWeight a omega t + gaussWeight a (-omega) t +
          2 * Real.exp (-omega ^ 2 / (2 * a)) * gaussWeight a 0 t) :=
    sum_congr rfl fun t _ => gaborThreeLobe_eq_gauss a omega t
  have hpt : S.sum (gaborThreeLobe a omega) =
      S.sum (gaussWeight a omega) + S.sum (gaussWeight a (-omega)) +
        2 * Real.exp (-omega ^ 2 / (2 * a)) * S.sum (gaussWeight a 0) := by
    rw [hcongr, sum_add_distrib, sum_add_distrib, ← mul_sum]
  have hexp0 : 0 ≤ 2 * Real.exp (-omega ^ 2 / (2 * a)) := by positivity
  unfold gaborLogThreeLobeMajorant
  rw [hpt]
  nlinarith [hω, hω', mul_le_mul_of_nonneg_left h0 hexp0]

theorem threeLobe_stripZeros_le_logMajorant_of_summable
    {a omega : ℝ} (ha : 0 < a)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hMsω : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a omega k)
    (hMsω' : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a (-omega) k)
    (hMs0 : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a 0 k) :
    S.sum (fun ρ => gaborThreeLobe a omega (ρ : ℂ).im) ≤
      gaborLogThreeLobeMajorant a omega := by
  have hω := gauss_density_transfer_stripZeros_of_summable ha omega S hMsω
  have hω' :=
    gauss_density_transfer_stripZeros_of_summable ha (-omega) S hMsω'
  have h0 := gauss_density_transfer_stripZeros_of_summable ha 0 S hMs0
  have hcongr :
      S.sum (fun ρ => gaborThreeLobe a omega (ρ : ℂ).im) =
        S.sum (fun ρ =>
          gaussWeight a omega (ρ : ℂ).im +
            gaussWeight a (-omega) (ρ : ℂ).im +
              2 * Real.exp (-omega ^ 2 / (2 * a)) *
                gaussWeight a 0 (ρ : ℂ).im) :=
    sum_congr rfl fun ρ _ => gaborThreeLobe_eq_gauss a omega (ρ : ℂ).im
  have hpt :
      S.sum (fun ρ => gaborThreeLobe a omega (ρ : ℂ).im) =
        S.sum (fun ρ => gaussWeight a omega (ρ : ℂ).im) +
          S.sum (fun ρ => gaussWeight a (-omega) (ρ : ℂ).im) +
            2 * Real.exp (-omega ^ 2 / (2 * a)) *
              S.sum (fun ρ => gaussWeight a 0 (ρ : ℂ).im) := by
    rw [hcongr, sum_add_distrib, sum_add_distrib, ← mul_sum]
  have hexp0 : 0 ≤ 2 * Real.exp (-omega ^ 2 / (2 * a)) := by positivity
  unfold gaborLogThreeLobeMajorant
  rw [hpt]
  nlinarith [hω, hω', mul_le_mul_of_nonneg_left h0 hexp0]

theorem norm_gaborHat_online_finset_le_logMajorant_of_summable
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hon : ∀ ρ ∈ S, (ρ : ℂ).re = 1 / 2)
    (hMsω : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax F.a F.omega k)
    (hMsω' : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax F.a (-F.omega) k)
    (hMs0 : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax F.a 0 k) :
    S.sum (fun ρ => ‖gaborHat F (ρ : ℂ)‖) ≤
      gaborHatThreeLobeConst F.a (1 / 2) *
        gaborLogThreeLobeMajorant F.a F.omega := by
  have ha : 0 < F.a := F.a_pos
  have hpt : ∀ ρ ∈ S,
      ‖gaborHat F (ρ : ℂ)‖ ≤
        gaborHatThreeLobeConst F.a (1 / 2) *
          gaborThreeLobe F.a F.omega (ρ : ℂ).im := by
    intro ρ hρ
    have hthree := norm_gaborHat_le_three_lobe (F := F) hF (ρ : ℂ)
    have hre : (ρ : ℂ).re = 1 / 2 := hon ρ hρ
    simpa [hre] using hthree
  have hsum := sum_le_sum hpt
  have hfactor :
      S.sum (fun ρ =>
          gaborHatThreeLobeConst F.a (1 / 2) *
            gaborThreeLobe F.a F.omega (ρ : ℂ).im) =
        gaborHatThreeLobeConst F.a (1 / 2) *
          S.sum (fun ρ => gaborThreeLobe F.a F.omega (ρ : ℂ).im) := by
    simp [mul_sum]
  have hC : 0 ≤ gaborHatThreeLobeConst F.a (1 / 2) :=
    gaborHatThreeLobeConst_nonneg F.a (1 / 2) ha
  have hthree :=
    threeLobe_stripZeros_le_logMajorant_of_summable ha S hMsω hMsω' hMs0
  exact hsum.trans (by
    rw [hfactor]
    exact mul_le_mul_of_nonneg_left hthree hC)

/-- r583 closed-form ĥ-side log budget.  After `1+log ≤ |k|+3`, the
three-lobe log-weighted theta tsum is morally bounded by a linear
central 3-bin cap plus the r575 far tail (two ω-lobes and a
suppressed 0-lobe).  The tsum `gaborLogThreeLobeMajorant` stays the
Finset transfer majorant; this closed form is the live remainder
because the tsum-vs-`E` comparison is not load-bearing once the
same absorption applies to the closed form.  r584 proves
`gaborLogThreeLobeMajorant ≤ gaborLogThreeLobeClosed`, so the
ĥ-side remainder sits on the same closed budget. -/
noncomputable def gaborLogThreeLobeClosed (a omega : ℝ) : ℝ :=
  (2 * zetaZerosInDiskCardBoundInner) *
    (6 * (|omega| + 5) + 4 * gaborFarTailLog a omega +
      2 * Real.exp (-omega ^ 2 / (2 * a)) *
        (12 + 2 * gaborFarTailLog a 0))

/-- r583: ĥ-side piece of `R_on_log` is the closed-form majorant,
not the tsum product.  `GaborLogMajorantLeHonestBudgetLog` stays
immediate from the `max`.  `gabor_criticalLineMass_le_honest_of`
is unchanged. -/
noncomputable def gaborOnlineLogBudget (a omega : ℝ) : ℝ :=
  gaborHatThreeLobeConst a (1 / 2) * gaborLogThreeLobeClosed a omega

/-- r582/r583 log-compatible on-line remainder.
`R_on_log = max( C_inc·(1+log(|ω|+3))·2·S_cert , ĥ-log-closed )`.
The first factor is the Path-A increment times the Jacobi envelope
(the r580 counterexample's necessary form).  The second summand is
the live ĥ-side closed majorant, so
`GaborLogMajorantLeHonestBudgetLog` is immediate.  Constant-cap
`gaborHonestOnlineBudget` remains the r575 proxy. -/
noncomputable def gaborHonestOnlineBudgetLog (a omega Cinc : ℝ) : ℝ :=
  max ((1 + Real.log (|omega| + 3)) *
      gaborHonestOnlineBudget a omega Cinc)
    (gaborOnlineLogBudget a omega)

/-- Honest Weil score with the majorant-compatible `R_on_log`. -/
noncomputable def gaborHonestWeilLog (a omega : ℝ) (Z : GaborCanonicalConfig)
    (Cinc : ℝ) : ℝ :=
  Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
    gaborHonestOnlineBudgetLog a omega Cinc

/-- r582 counting-compatible dominance with log-compatible `R_on`.
Same Q-sum packing as `GaborDominanceBoundLog`; only the on-line
remainder and the online cap change. -/
def GaborDominanceBoundLog2 : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliantLog Z →
    Z.gammaDistinct →
    gaborHonestWeilLog (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0

/-- Bridge 2 tsum + multiplicity.  Discharged r585:
`Re(tsum) ≤ tsum m‖ĥ‖ ≤ C_hat · log-majorant ≤ closed budget`. -/
def GaborCriticalLineMassLeLogMajorant : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    gaborCriticalLineMass F ≤ gaborOnlineLogBudget F.a F.omega

/-- Historical comparison against the constant-cap proxy `R_on`.
The unrestricted form does **not** hold: the ω-lobe of the log
majorant is `≳ C_inc (1+log(|ω|+3))`, while
`gaborHonestOnlineBudget = 2 C_inc S_cert` is ω-independent
in occupancy (`Θ_lobe ≥ 3`).  Kept as a named remainder; the
live comparison is `GaborLogMajorantLeHonestBudgetLog`. -/
def GaborLogMajorantLeHonestBudget : Prop :=
  ∀ a omega : ℝ, 0 < a → 0 < omega →
    gaborOnlineLogBudget a omega ≤
      gaborHonestOnlineBudget a omega gaborCInc

/-- Log majorant ≤ log-compatible honest budget.  Immediate from
the `max` in `gaborHonestOnlineBudgetLog`. -/
def GaborLogMajorantLeHonestBudgetLog : Prop :=
  ∀ a omega : ℝ, 0 < a → 0 < omega →
    gaborOnlineLogBudget a omega ≤
      gaborHonestOnlineBudgetLog a omega gaborCInc

theorem gaborLogMajorantLeHonestBudgetLog_holds :
    GaborLogMajorantLeHonestBudgetLog := by
  intro a omega _ha _hω
  exact le_max_right _ _

theorem gabor_criticalLineMass_le_honest_of
    (hlog : GaborCriticalLineMassLeLogMajorant)
    (hbud : GaborLogMajorantLeHonestBudgetLog)
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩)
    (hω : 0 < F.omega) :
    gaborCriticalLineMass F ≤
      gaborHonestOnlineBudgetLog F.a F.omega gaborCInc :=
  (hlog F hF).trans (hbud F.a F.omega F.a_pos hω)

/-! ## r584: tsum log-majorant ≤ closed linear-central + far tail -/

lemma gaborBinCountMajorant_le_linear (k : ℤ) :
    gaborBinCountMajorant k ≤
      2 * zetaZerosInDiskCardBoundInner * ((|k| : ℝ) + 3) := by
  simpa [gaborKBinAt_eq_binCountMajorant] using gaborKBinAt_le_linear k

lemma gaborFarTailLog_neg (a omega : ℝ) :
    gaborFarTailLog a (-omega) = gaborFarTailLog a omega := by
  unfold gaborFarTailLog
  simp [abs_neg]

lemma lin_gaussBinMax_le_far {a c : ℝ} (ha : 0 < a) {k : ℤ}
    (hk : 2 * (|c| + 1) ≤ (|k| : ℝ)) :
    ((|k| : ℝ) + 3) * gaussBinMax a c k ≤
      ((|k| : ℝ) + 3) * Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) := by
  have hdpos : 0 ≤ (|k| : ℝ) - |c| - 1 :=
    le_trans (div_nonneg (abs_nonneg _) (by norm_num)) (hostDist_half hk)
  have hM := gaussBinMax_le_exp_hostDist (a := a) (c := c) ha k
  have hmax : max (0 : ℝ) ((|k| : ℝ) - |c| - 1) =
      (|k| : ℝ) - |c| - 1 := max_eq_right hdpos
  rw [hmax] at hM
  have hhalf := hostDist_half (c := c) hk
  have hsq : ((|k| : ℝ) / 2) ^ 2 ≤ ((|k| : ℝ) - |c| - 1) ^ 2 :=
    sq_le_sq.mpr (by
      rw [abs_of_nonneg (div_nonneg (abs_nonneg _) (by norm_num)),
        abs_of_nonneg hdpos]
      exact hhalf)
  have hexp : Real.exp (-((|k| : ℝ) - |c| - 1) ^ 2 / (2 * a)) ≤
      Real.exp (-((|k| : ℝ) ^ 2) / (8 * a)) := by
    refine Real.exp_le_exp.mpr ?_
    have hden : 0 < 2 * a := mul_pos (by norm_num) ha
    have := div_le_div_of_nonneg_right (neg_le_neg hsq) hden.le
    have hr : -((|k| : ℝ) / 2) ^ 2 / (2 * a) =
        -((|k| : ℝ) ^ 2) / (8 * a) := by
      field_simp [ne_of_gt hden, ne_of_gt ha]
      ring
    exact this.trans_eq hr
  exact mul_le_mul_of_nonneg_left (hM.trans hexp) (by positivity)

lemma lin_gaussBinMax_summable {a c : ℝ} (ha : 0 < a) :
    Summable fun k : ℤ =>
      ((|k| : ℝ) + 3) * gaussBinMax a c k := by
  have hmaj := summable_int_linear_gauss_sq ha
  refine Summable.of_norm_bounded_eventually hmaj ?_
  have hfin := far_bins_finite c
  have hev : ∀ᶠ k : ℤ in Filter.cofinite,
      2 * (|c| + 1) ≤ (|k| : ℝ) := by
    filter_upwards [hfin.compl_mem_cofinite] with k hk
    exact not_lt.mp hk
  filter_upwards [hev] with k hk
  have hnn : 0 ≤ ((|k| : ℝ) + 3) * gaussBinMax a c k :=
    mul_nonneg (by positivity) (gaussBinMax_nonneg ha k)
  rw [Real.norm_eq_abs, abs_of_nonneg hnn]
  exact lin_gaussBinMax_le_far ha hk

lemma central_lin_binMax_le {a c : ℝ} (ha : 0 < a) :
    ∑ k ∈ ({Int.floor c - 1, Int.floor c, Int.floor c + 1} : Finset ℤ),
        ((|k| : ℝ) + 3) * gaussBinMax a c k ≤
      3 * (|c| + 5) := by
  set n := Int.floor c
  set s : Finset ℤ := {n - 1, n, n + 1}
  have hpt : ∀ k ∈ s,
      ((|k| : ℝ) + 3) * gaussBinMax a c k ≤ |c| + 5 := by
    intro k hk
    have habs := abs_mem_central3 n k (by simpa [s] using hk)
    have hk1 : (|k| : ℝ) ≤ (|n| : ℝ) + 1 := by exact_mod_cast habs
    have hn := abs_floor_le_abs_add_one c
    have hle : (|k| : ℝ) + 3 ≤ |c| + 5 := by
      linarith [hk1, hn]
    have hmul :
        ((|k| : ℝ) + 3) * gaussBinMax a c k ≤
          ((|k| : ℝ) + 3) * 1 :=
      mul_le_mul_of_nonneg_left (gaussBinMax_le_one ha k) (by positivity)
    rw [mul_one] at hmul
    exact hmul.trans hle
  have hsum := sum_le_sum hpt
  have hconst :
      ∑ k ∈ s, (|c| + 5) = 3 * (|c| + 5) := by
    rw [sum_const, nsmul_eq_mul]
    have hcard : (s.card : ℝ) = 3 := by
      exact_mod_cast central3_card n
    rw [hcard]
  exact hsum.trans_eq hconst

lemma central_lin_binMax_zero_le {a : ℝ} (ha : 0 < a) :
    ∑ k ∈ ({(-1 : ℤ), 0, 1} : Finset ℤ),
        ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤ (12 : ℝ) := by
  set s : Finset ℤ := {(-1 : ℤ), 0, 1}
  have hs : s = ({Int.floor (0 : ℝ) - 1, Int.floor (0 : ℝ),
      Int.floor (0 : ℝ) + 1} : Finset ℤ) := by
    simp [s]
  have hpt : ∀ k ∈ s,
      ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤ (4 : ℝ) := by
    intro k hk
    have hk4 : (|k| : ℝ) + 3 ≤ 4 := by
      have : k = -1 ∨ k = 0 ∨ k = 1 := by simpa [s] using hk
      rcases this with h | h | h <;> subst h <;> norm_num
    have hmul :
        ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤
          ((|k| : ℝ) + 3) * 1 :=
      mul_le_mul_of_nonneg_left (gaussBinMax_le_one ha k) (by positivity)
    rw [mul_one] at hmul
    exact hmul.trans hk4
  have hsum := sum_le_sum hpt
  have hconst : ∑ k ∈ s, (4 : ℝ) = (12 : ℝ) := by
    rw [sum_const, nsmul_eq_mul]
    have hcard : (s.card : ℝ) = 3 := by
      have hs' : s = ({(0 : ℤ) - 1, 0, 0 + 1} : Finset ℤ) := by simp [s]
      rw [hs']
      exact_mod_cast central3_card (0 : ℤ)
    rw [hcard]
    norm_num
  exact hsum.trans_eq hconst

lemma far_lin_binMax_tsum_le {a c : ℝ} (ha : 0 < a) :
    (∑' k : ℤ,
      if k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k then
        ((|k| : ℝ) + 3) * gaussBinMax a c k else 0) ≤
      2 * gaborFarTailLog a c := by
  refine Real.tsum_le_of_sum_le
    (fun k => by
      split_ifs
      · exact mul_nonneg (by positivity) (gaussBinMax_nonneg ha k)
      · exact le_rfl) fun K => ?_
  have hite :
      ∑ k ∈ K,
          (if k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k then
            ((|k| : ℝ) + 3) * gaussBinMax a c k else 0) =
        ∑ k ∈ K.filter (fun k =>
            k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k),
          ((|k| : ℝ) + 3) * gaussBinMax a c k :=
    (sum_filter (p := fun k =>
        k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k)
      (f := fun k => ((|k| : ℝ) + 3) * gaussBinMax a c k)).symm
  rw [hite]
  exact weighted_far_bins_le ha K

lemma lin_binMax_sum_le {a c : ℝ} (ha : 0 < a) (K : Finset ℤ) :
    ∑ k ∈ K, ((|k| : ℝ) + 3) * gaussBinMax a c k ≤
      3 * (|c| + 5) + 2 * gaborFarTailLog a c := by
  set n := Int.floor c
  set s : Finset ℤ := {n - 1, n, n + 1}
  set f : ℤ → ℝ := fun k => ((|k| : ℝ) + 3) * gaussBinMax a c k
  have hf0 : ∀ k, 0 ≤ f k :=
    fun k => mul_nonneg (by positivity) (gaussBinMax_nonneg ha k)
  have hpart : ∀ k : ℤ, k ∈ s ∨ k ≤ n - 2 ∨ n + 2 ≤ k := by
    intro k
    by_cases h : k ∈ s
    · exact Or.inl h
    · have : ¬ (k = n - 1 ∨ k = n ∨ k = n + 1) := by simpa [s] using h
      exact Or.inr (by omega)
  have hunion :
      K.filter (fun k => k ∈ s) ∪ K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k) = K := by
    ext k
    constructor
    · intro hk
      rcases Finset.mem_union.mp hk with h | h
      · exact (mem_filter.mp h).1
      · exact (mem_filter.mp h).1
    · intro hk
      rcases hpart k with hcen | hfar
      · exact Finset.mem_union.mpr (Or.inl (mem_filter.mpr ⟨hk, hcen⟩))
      · exact Finset.mem_union.mpr (Or.inr (mem_filter.mpr ⟨hk, hfar⟩))
  have hdisj :
      Disjoint (K.filter (fun k => k ∈ s))
        (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)) := by
    refine Finset.disjoint_left.mpr ?_
    intro k hcen hfar
    have hs' : k ∈ s := (mem_filter.mp hcen).2
    have hf' : k ≤ n - 2 ∨ n + 2 ≤ k := (mem_filter.mp hfar).2
    have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [s] using hs'
    omega
  have hsum :
      K.sum f =
        (K.filter (fun k => k ∈ s)).sum f +
          (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)).sum f := by
    rw [← sum_union hdisj, hunion]
  have hcen :
      (K.filter (fun k => k ∈ s)).sum f ≤ 3 * (|c| + 5) := by
    have hsub : K.filter (fun k => k ∈ s) ⊆ s :=
      fun k hk => (mem_filter.mp hk).2
    have hle := sum_le_sum_of_subset_of_nonneg (f := f) hsub
      (fun k _ _ => hf0 k)
    have hcen0 : s.sum f ≤ 3 * (|c| + 5) := by
      simp only [f, s, n]
      exact central_lin_binMax_le ha
    exact hle.trans hcen0
  have hfar :
      (K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)).sum f ≤
        2 * gaborFarTailLog a c := by
    simpa [f, n] using weighted_far_bins_le (a := a) (omega := c) ha K
  linarith [hsum, hcen, hfar]

lemma lin_binMax_tsum_le {a c : ℝ} (ha : 0 < a) :
    ∑' k : ℤ, ((|k| : ℝ) + 3) * gaussBinMax a c k ≤
      3 * (|c| + 5) + 2 * gaborFarTailLog a c :=
  Real.tsum_le_of_sum_le
    (fun k => mul_nonneg (by positivity) (gaussBinMax_nonneg ha k))
    (fun K => lin_binMax_sum_le ha K)

lemma lin_binMax_sum_zero_le {a : ℝ} (ha : 0 < a) (K : Finset ℤ) :
    ∑ k ∈ K, ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤
      12 + 2 * gaborFarTailLog a 0 := by
  set s : Finset ℤ := {(-1 : ℤ), 0, 1}
  set f : ℤ → ℝ := fun k => ((|k| : ℝ) + 3) * gaussBinMax a 0 k
  have hf0 : ∀ k, 0 ≤ f k :=
    fun k => mul_nonneg (by positivity) (gaussBinMax_nonneg ha k)
  have hpart : ∀ k : ℤ, k ∈ s ∨ k ≤ -2 ∨ 2 ≤ k := by
    intro k
    by_cases h : k ∈ s
    · exact Or.inl h
    · have : ¬ (k = -1 ∨ k = 0 ∨ k = 1) := by simpa [s] using h
      exact Or.inr (by omega)
  have hunion :
      K.filter (fun k => k ∈ s) ∪ K.filter (fun k => k ≤ -2 ∨ 2 ≤ k) = K := by
    ext k
    constructor
    · intro hk
      rcases Finset.mem_union.mp hk with h | h
      · exact (mem_filter.mp h).1
      · exact (mem_filter.mp h).1
    · intro hk
      rcases hpart k with hcen | hfar
      · exact Finset.mem_union.mpr (Or.inl (mem_filter.mpr ⟨hk, hcen⟩))
      · exact Finset.mem_union.mpr (Or.inr (mem_filter.mpr ⟨hk, hfar⟩))
  have hdisj :
      Disjoint (K.filter (fun k => k ∈ s))
        (K.filter (fun k => k ≤ -2 ∨ 2 ≤ k)) := by
    refine Finset.disjoint_left.mpr ?_
    intro k hcen hfar
    have hs' : k ∈ s := (mem_filter.mp hcen).2
    have hf' : k ≤ -2 ∨ 2 ≤ k := (mem_filter.mp hfar).2
    have : k = -1 ∨ k = 0 ∨ k = 1 := by simpa [s] using hs'
    omega
  have hsum :
      K.sum f =
        (K.filter (fun k => k ∈ s)).sum f +
          (K.filter (fun k => k ≤ -2 ∨ 2 ≤ k)).sum f := by
    rw [← sum_union hdisj, hunion]
  have hcen :
      (K.filter (fun k => k ∈ s)).sum f ≤ (12 : ℝ) := by
    have hsub : K.filter (fun k => k ∈ s) ⊆ s :=
      fun k hk => (mem_filter.mp hk).2
    have hle := sum_le_sum_of_subset_of_nonneg (f := f) hsub
      (fun k _ _ => hf0 k)
    have hcen0 : s.sum f ≤ (12 : ℝ) := by
      simp only [f, s]
      exact central_lin_binMax_zero_le ha
    exact hle.trans hcen0
  have hfar :
      (K.filter (fun k => k ≤ -2 ∨ 2 ≤ k)).sum f ≤
        2 * gaborFarTailLog a 0 := by
    simpa [f, Int.floor_zero] using
      weighted_far_bins_le (a := a) (omega := (0 : ℝ)) ha K
  linarith [hsum, hcen, hfar]

lemma lin_binMax_tsum_zero_le {a : ℝ} (ha : 0 < a) :
    ∑' k : ℤ, ((|k| : ℝ) + 3) * gaussBinMax a 0 k ≤
      12 + 2 * gaborFarTailLog a 0 :=
  Real.tsum_le_of_sum_le
    (fun k => mul_nonneg (by positivity) (gaussBinMax_nonneg ha k))
    (fun K => lin_binMax_sum_zero_le ha K)

lemma gaborLogWeightedTheta_le_linClosed {a c : ℝ} (ha : 0 < a) :
    gaborLogWeightedTheta a c ≤
      (2 * zetaZerosInDiskCardBoundInner) *
        (3 * (|c| + 5) + 2 * gaborFarTailLog a c) := by
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hnn : ∀ k : ℤ,
      0 ≤ gaborBinCountMajorant k * gaussBinMax a c k :=
    fun k => mul_nonneg (gaborBinCountMajorant_nonneg k)
      (gaussBinMax_nonneg (a := a) (c := c) ha k)
  unfold gaborLogWeightedTheta
  refine Real.tsum_le_of_sum_le hnn fun K => ?_
  have hpt : ∀ k ∈ K,
      gaborBinCountMajorant k * gaussBinMax a c k ≤
        (2 * zetaZerosInDiskCardBoundInner) *
          (((|k| : ℝ) + 3) * gaussBinMax a c k) := by
    intro k _hk
    have hlin := gaborBinCountMajorant_le_linear k
    have hM0 := gaussBinMax_nonneg (a := a) (c := c) ha k
    have hmul := mul_le_mul_of_nonneg_right hlin hM0
    rw [mul_assoc] at hmul
    exact hmul
  have hsum := sum_le_sum hpt
  have hfactor :
      ∑ k ∈ K, (2 * zetaZerosInDiskCardBoundInner) *
          (((|k| : ℝ) + 3) * gaussBinMax a c k) =
        (2 * zetaZerosInDiskCardBoundInner) *
          ∑ k ∈ K, ((|k| : ℝ) + 3) * gaussBinMax a c k := by
    rw [← mul_sum]
  have hlin := lin_binMax_sum_le (a := a) (c := c) ha K
  exact (hsum.trans_eq hfactor).trans (mul_le_mul_of_nonneg_left hlin hC0)

lemma gaborLogWeightedTheta_zero_le_closed {a : ℝ} (ha : 0 < a) :
    gaborLogWeightedTheta a 0 ≤
      (2 * zetaZerosInDiskCardBoundInner) *
        (12 + 2 * gaborFarTailLog a 0) := by
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hnn : ∀ k : ℤ,
      0 ≤ gaborBinCountMajorant k * gaussBinMax a 0 k :=
    fun k => mul_nonneg (gaborBinCountMajorant_nonneg k)
      (gaussBinMax_nonneg (a := a) (c := (0 : ℝ)) ha k)
  unfold gaborLogWeightedTheta
  refine Real.tsum_le_of_sum_le hnn fun K => ?_
  have hpt : ∀ k ∈ K,
      gaborBinCountMajorant k * gaussBinMax a 0 k ≤
        (2 * zetaZerosInDiskCardBoundInner) *
          (((|k| : ℝ) + 3) * gaussBinMax a 0 k) := by
    intro k _hk
    have hlin := gaborBinCountMajorant_le_linear k
    have hM0 := gaussBinMax_nonneg (a := a) (c := (0 : ℝ)) ha k
    have hmul := mul_le_mul_of_nonneg_right hlin hM0
    rw [mul_assoc] at hmul
    exact hmul
  have hsum := sum_le_sum hpt
  have hfactor :
      ∑ k ∈ K, (2 * zetaZerosInDiskCardBoundInner) *
          (((|k| : ℝ) + 3) * gaussBinMax a 0 k) =
        (2 * zetaZerosInDiskCardBoundInner) *
          ∑ k ∈ K, ((|k| : ℝ) + 3) * gaussBinMax a 0 k := by
    rw [← mul_sum]
  have hlin := lin_binMax_sum_zero_le ha K
  exact (hsum.trans_eq hfactor).trans (mul_le_mul_of_nonneg_left hlin hC0)

/-- r584: the Finset-transfer tsum is dominated by the closed
linear-central + r575 far-tail form used in `gaborOnlineLogBudget`. -/
theorem gaborLogThreeLobeMajorant_le_closed {a omega : ℝ} (ha : 0 < a) :
    gaborLogThreeLobeMajorant a omega ≤
      gaborLogThreeLobeClosed a omega := by
  have hC0 : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hω := gaborLogWeightedTheta_le_linClosed (a := a) (c := omega) ha
  have hω' := gaborLogWeightedTheta_le_linClosed (a := a) (c := -omega) ha
  have h0 := gaborLogWeightedTheta_zero_le_closed ha
  have hexp0 : 0 ≤ 2 * Real.exp (-omega ^ 2 / (2 * a)) := by positivity
  have hneg : gaborFarTailLog a (-omega) = gaborFarTailLog a omega :=
    gaborFarTailLog_neg a omega
  have habs : |-omega| = |omega| := abs_neg omega
  have hω'c :
      gaborLogWeightedTheta a (-omega) ≤
        (2 * zetaZerosInDiskCardBoundInner) *
          (3 * (|omega| + 5) + 2 * gaborFarTailLog a omega) := by
    simpa [hneg, habs] using hω'
  have h0c :
      2 * Real.exp (-omega ^ 2 / (2 * a)) * gaborLogWeightedTheta a 0 ≤
        2 * Real.exp (-omega ^ 2 / (2 * a)) *
          ((2 * zetaZerosInDiskCardBoundInner) *
            (12 + 2 * gaborFarTailLog a 0)) :=
    mul_le_mul_of_nonneg_left h0 hexp0
  unfold gaborLogThreeLobeMajorant gaborLogThreeLobeClosed
  have hsum :
      (2 * zetaZerosInDiskCardBoundInner) *
            (3 * (|omega| + 5) + 2 * gaborFarTailLog a omega) +
          (2 * zetaZerosInDiskCardBoundInner) *
            (3 * (|omega| + 5) + 2 * gaborFarTailLog a omega) +
          2 * Real.exp (-omega ^ 2 / (2 * a)) *
            ((2 * zetaZerosInDiskCardBoundInner) *
              (12 + 2 * gaborFarTailLog a 0)) =
        (2 * zetaZerosInDiskCardBoundInner) *
          (6 * (|omega| + 5) + 4 * gaborFarTailLog a omega +
            2 * Real.exp (-omega ^ 2 / (2 * a)) *
              (12 + 2 * gaborFarTailLog a 0)) := by
    ring
  linarith [hω, hω'c, h0c, hsum]

/-- r584 composition: tsum majorant ≤ closed form attaches the
ĥ-side remainder to `gaborOnlineLogBudget`. -/
theorem gaborCriticalLineMass_le_closed_of_tsum
    {F : GaborWeilTest} (_hF : F.coeffs = ⟨1, 0, 0⟩)
    (htsum : gaborCriticalLineMass F ≤
      gaborHatThreeLobeConst F.a (1 / 2) *
        gaborLogThreeLobeMajorant F.a F.omega) :
    gaborCriticalLineMass F ≤ gaborOnlineLogBudget F.a F.omega := by
  have ha : 0 < F.a := F.a_pos
  have hC : 0 ≤ gaborHatThreeLobeConst F.a (1 / 2) :=
    gaborHatThreeLobeConst_nonneg F.a (1 / 2) ha
  have hclosed :=
    gaborLogThreeLobeMajorant_le_closed (a := F.a) (omega := F.omega) ha
  unfold gaborOnlineLogBudget
  exact htsum.trans (mul_le_mul_of_nonneg_left hclosed hC)

lemma sum_fiber_mass {α : Type*} [DecidableEq α]
    (S : Finset α) (g : α → ℤ) (μ : α → ℝ) (M : ℤ → ℝ) :
    S.sum (fun x => μ x * M (g x)) =
      ∑ k ∈ S.image g,
        (S.filter (fun x => g x = k)).sum μ * M k := by
  classical
  have hmaps : ∀ x ∈ S, g x ∈ S.image g :=
    fun x hx => Finset.mem_image_of_mem g hx
  have hinner : ∀ k ∈ S.image g,
      (S.filter (fun x => g x = k)).sum (fun x => μ x * M (g x)) =
        (S.filter (fun x => g x = k)).sum μ * M k := by
    intro k _hk
    have : ∀ x ∈ S.filter (fun x => g x = k), μ x * M (g x) = μ x * M k := by
      intro x hx
      rw [(Finset.mem_filter.mp hx).2]
    rw [Finset.sum_congr rfl this, Finset.sum_mul]
  have hS :=
    Finset.disjiUnion_filter_eq_of_maps_to (s := S) (t := S.image g)
      (f := g) hmaps
  conv_lhs => rw [← hS]
  rw [Finset.sum_disjiUnion]
  exact Finset.sum_congr rfl hinner

lemma bin_partial_summation_mass
    {α : Type*} [DecidableEq α]
    {w : ℝ → ℝ} (_hw : ∀ t, 0 ≤ w t)
    (S : Finset α) (γ : α → ℝ) (μ : α → ℝ) (hμ : ∀ x, 0 ≤ μ x)
    (C : ℤ → ℝ) (hC0 : ∀ k, 0 ≤ C k)
    (hC : ∀ k : ℤ,
      (S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1)).sum μ ≤ C k)
    {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k)
    (hM : ∀ (k : ℤ) (t : ℝ), t ∈ Icc (k : ℝ) ((k : ℝ) + 1) → w t ≤ M k)
    (hMs : Summable fun k : ℤ => C k * M k) :
    S.sum (fun x => μ x * w (γ x)) ≤ ∑' k : ℤ, C k * M k := by
  have hpt : ∀ x ∈ S, μ x * w (γ x) ≤ μ x * M (ordinateBin (γ x)) := by
    intro x _hx
    exact mul_le_mul_of_nonneg_left
      (hM _ _ (mem_Icc_of_ordinateBin (γ x))) (hμ x)
  have hsum₁ : S.sum (fun x => μ x * w (γ x)) ≤
      S.sum (fun x => μ x * M (ordinateBin (γ x))) :=
    sum_le_sum hpt
  let g : α → ℤ := fun x => ordinateBin (γ x)
  let bins := S.image g
  have hsum₂ :
      S.sum (fun x => μ x * M (g x)) ≤ ∑ k ∈ bins, C k * M k := by
    rw [sum_fiber_mass S g μ M]
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
    have hmass :
        (S.filter (fun x => g x = k)).sum μ ≤ C k :=
      (sum_le_sum_of_subset_of_nonneg (f := μ) hsub
        (fun x _ _ => hμ x)).trans (hC k)
    exact mul_le_mul_of_nonneg_right hmass (hM0 k)
  have hsum₄ : ∑ k ∈ bins, C k * M k ≤ ∑' k : ℤ, C k * M k :=
    hMs.sum_le_tsum _ (fun k _ => mul_nonneg (hC0 k) (hM0 k))
  exact hsum₁.trans (hsum₂.trans hsum₄)

lemma strip_zero_bin_mult_le
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) (k : ℤ) :
    (S.filter (fun ρ => (k : ℝ) < ρ.val.im ∧
        ρ.val.im ≤ (k : ℝ) + 1)).sum
      (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) ≤
        gaborBinCountMajorant k := by
  set Sk : Finset {z : ℂ // IsCriticalStripZetaZero z} :=
    S.filter fun ρ => (k : ℝ) < ρ.val.im ∧ ρ.val.im ≤ (k : ℝ) + 1
  have himage : Sk.image (fun ρ => ρ.val) ⊆ stripZerosWindow (k : ℝ) := by
    intro z hz
    obtain ⟨ρ, hρ, rfl⟩ := mem_image.mp hz
    have hbin := (mem_filter.mp hρ).2
    exact mem_stripZerosWindow_of_critical ρ.property ⟨hbin.1.le, hbin.2⟩
  have hinj : Set.InjOn (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      ρ.val) Sk :=
    fun _ _ _ _ h => Subtype.ext h
  have hsum :
      (Sk.image (fun ρ => ρ.val)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) =
        Sk.sum (fun ρ => (riemannZetaMultiplicity ρ.val : ℝ)) :=
    Finset.sum_image hinj
  have hwin :
      (Sk.image (fun ρ => ρ.val)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        (stripZerosWindow (k : ℝ)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) :=
    Finset.sum_le_sum_of_subset_of_nonneg himage
      (fun _ _ _ => Nat.cast_nonneg _)
  have hK := sum_multiplicity_stripZerosWindow_le (k : ℝ)
  have hmaj : (stripZerosWindow (k : ℝ)).sum
      (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        gaborBinCountMajorant k := by
    simpa [gaborBinCountMajorant, gaborKBinAt] using hK
  exact (hsum.symm.trans_le hwin).trans hmaj

lemma gauss_mass_transfer_stripZeros
    {a : ℝ} (ha : 0 < a) (c : ℝ)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a c k) :
    S.sum (fun ρ =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          gaussWeight a c (ρ : ℂ).im) ≤
      gaborLogWeightedTheta a c :=
  bin_partial_summation_mass (w := gaussWeight a c)
    (fun _ => gaussWeight_nonneg _ _ _) S (fun ρ => (ρ : ℂ).im)
    (fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℝ))
    (fun _ => Nat.cast_nonneg _)
    gaborBinCountMajorant gaborBinCountMajorant_nonneg
    (fun k => strip_zero_bin_mult_le S k)
    (fun k => gaussBinMax_nonneg ha k)
    (fun _k _t ht => le_gaussBinMax ha ht) hMs

lemma threeLobe_mult_stripZeros_le_logMajorant
    {a omega : ℝ} (ha : 0 < a)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hMsω : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a omega k)
    (hMsω' : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a (-omega) k)
    (hMs0 : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax a 0 k) :
    S.sum (fun ρ =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          gaborThreeLobe a omega (ρ : ℂ).im) ≤
      gaborLogThreeLobeMajorant a omega := by
  have hω := gauss_mass_transfer_stripZeros ha omega S hMsω
  have hω' := gauss_mass_transfer_stripZeros ha (-omega) S hMsω'
  have h0 := gauss_mass_transfer_stripZeros ha 0 S hMs0
  have hcongr :
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            gaborThreeLobe a omega (ρ : ℂ).im) =
        S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            (gaussWeight a omega (ρ : ℂ).im +
              gaussWeight a (-omega) (ρ : ℂ).im +
              2 * Real.exp (-omega ^ 2 / (2 * a)) *
                gaussWeight a 0 (ρ : ℂ).im)) :=
    sum_congr rfl fun ρ _ => by
      rw [gaborThreeLobe_eq_gauss]
  have hpt :
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            gaborThreeLobe a omega (ρ : ℂ).im) =
        S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaussWeight a omega (ρ : ℂ).im) +
          S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaussWeight a (-omega) (ρ : ℂ).im) +
          2 * Real.exp (-omega ^ 2 / (2 * a)) *
            S.sum (fun ρ =>
              (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                gaussWeight a 0 (ρ : ℂ).im) := by
    rw [hcongr]
    have hdistrib :
        S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              (gaussWeight a omega (ρ : ℂ).im +
                gaussWeight a (-omega) (ρ : ℂ).im +
                2 * Real.exp (-omega ^ 2 / (2 * a)) *
                  gaussWeight a 0 (ρ : ℂ).im)) =
          S.sum (fun ρ =>
              (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                gaussWeight a omega (ρ : ℂ).im +
                (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                  gaussWeight a (-omega) (ρ : ℂ).im +
                2 * Real.exp (-omega ^ 2 / (2 * a)) *
                  ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                    gaussWeight a 0 (ρ : ℂ).im)) :=
      sum_congr rfl fun _ _ => by ring
    rw [hdistrib, sum_add_distrib, sum_add_distrib, ← mul_sum]
  have hexp0 : 0 ≤ 2 * Real.exp (-omega ^ 2 / (2 * a)) := by positivity
  unfold gaborLogThreeLobeMajorant
  rw [hpt]
  nlinarith [hω, hω', mul_le_mul_of_nonneg_left h0 hexp0]

theorem gauss_density_transfer_binCount_of
    (hsm : GaborLogWeightedThetaSummable)
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        gaborBinCountMajorant k) :
    (S.sum (gaussWeight a c) : ℝ) ≤ gaborLogWeightedTheta a c :=
  gauss_density_transfer_binCount_of_summable ha c S hinc (hsm ha c)

/-! ## Bridge 5 remainder: FE-folded truncation -/

noncomputable def gaborOffLineZerosUpTo (T : ℝ) : Finset ℂ :=
  (riemannZetaZerosOnClosedRect 0 1 T).filter
    fun z => z.re ≠ 1 / 2 ∧ 0 < z.im

lemma mem_gaborOffLineZerosUpTo {T : ℝ} {z : ℂ} :
    z ∈ gaborOffLineZerosUpTo T ↔
      z ∈ riemannZetaZerosOnClosedRect 0 1 T ∧
        z.re ≠ 1 / 2 ∧ 0 < z.im :=
  mem_filter

noncomputable def gaborCanonicalKey (z : ℂ) : ℝ × ℝ :=
  (|z.re - 1 / 2|, z.im)

lemma gaborCanonicalKey_sigma_off {T : ℝ} {z : ℂ}
    (hz : z ∈ gaborOffLineZerosUpTo T) :
    0 < (gaborCanonicalKey z).1 ∧ (gaborCanonicalKey z).1 < 1 / 2 := by
  have hz' := mem_gaborOffLineZerosUpTo.mp hz
  have hmem := mem_riemannZetaZerosOnClosedRect.mp hz'.1
  have hrect := mem_zetaClosedRect.mp hmem.1
  have hζ := hmem.2.1
  have hre0 : 0 < z.re :=
    lt_of_le_of_ne hrect.1 fun h =>
      riemannZeta_ne_zero_of_re_eq_zero h.symm hζ
  have hre1 : z.re < 1 :=
    lt_of_le_of_ne hrect.2.1 fun h =>
      riemannZeta_ne_zero_of_one_le_re (le_of_eq h.symm) hζ
  constructor
  · exact abs_pos.mpr (sub_ne_zero.mpr hz'.2.1)
  · unfold gaborCanonicalKey
    rw [abs_lt]
    constructor <;> linarith [hre0, hre1]

lemma gaborCanonicalKey_gamma_pos {T : ℝ} {z : ℂ}
    (hz : z ∈ gaborOffLineZerosUpTo T) :
    0 < (gaborCanonicalKey z).2 :=
  (mem_gaborOffLineZerosUpTo.mp hz).2.2

noncomputable def gaborTruncationPts (T : ℝ) : Finset (ℝ × ℝ) :=
  (gaborOffLineZerosUpTo T).image gaborCanonicalKey

noncomputable def gaborTruncationMult (T : ℝ) (q : ℝ × ℝ) : ℕ :=
  if q ∈ gaborTruncationPts T then 1 else 0

lemma gaborTruncationMult_eq_one {T : ℝ} {q : ℝ × ℝ}
    (hq : q ∈ gaborTruncationPts T) :
    gaborTruncationMult T q = 1 :=
  if_pos hq

noncomputable def gaborTruncationConfig (T : ℝ) : GaborCanonicalConfig where
  pts := gaborTruncationPts T
  mult := gaborTruncationMult T
  mult_pos := by
    intro q hq
    have : gaborTruncationMult T q = 1 :=
      gaborTruncationMult_eq_one hq
    rw [this]
    exact Nat.succ_pos 0
  sigma_off := by
    intro q hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    exact gaborCanonicalKey_sigma_off hz
  gamma_pos := by
    intro q hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    exact gaborCanonicalKey_gamma_pos hz

lemma gaborOffLine_subset_strip {T : ℝ} {k : ℤ} {z : ℂ}
    (hz : z ∈ gaborOffLineZerosUpTo T)
    (hbin : (k : ℝ) < z.im ∧ z.im ≤ (k : ℝ) + 1) :
    z ∈ stripZerosWindow (k : ℝ) := by
  have hz' := mem_gaborOffLineZerosUpTo.mp hz
  have hmem := mem_riemannZetaZerosOnClosedRect.mp hz'.1
  have hrect := mem_zetaClosedRect.mp hmem.1
  have him : (k : ℝ) ≤ z.im ∧ z.im ≤ (k : ℝ) + 1 :=
    ⟨hbin.1.le, hbin.2⟩
  have hcrit : IsCriticalStripZetaZero z :=
    ⟨hmem.2.1,
      lt_of_le_of_ne hrect.1 fun h =>
        riemannZeta_ne_zero_of_re_eq_zero h.symm hmem.2.1,
      lt_of_le_of_ne hrect.2.1 fun h =>
        riemannZeta_ne_zero_of_one_le_re (le_of_eq h.symm) hmem.2.1⟩
  exact mem_stripZerosWindow_of_critical hcrit him

/-- Goal 2: every finite FE-folded truncation is log-compliant. -/
theorem gaborTruncation_incrementCompliantLog (T : ℝ) :
    GaborConfigIncrementCompliantLog (gaborTruncationConfig T) := by
  refine incrementCompliantLog_of_le_strip (gaborTruncationConfig T) ?_
  intro k
  set Z := gaborTruncationConfig T
  set Sk := Z.pts.filter
    (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)
  have hmult : Sk.sum (fun q => (Z.mult q : ℝ)) = (Sk.card : ℝ) := by
    have hpt : ∀ q ∈ Sk, (Z.mult q : ℝ) = 1 := by
      intro q hq
      have hqpts : q ∈ Z.pts := (mem_filter.mp hq).1
      have : Z.mult q = 1 := gaborTruncationMult_eq_one hqpts
      simp [this]
    rw [sum_congr rfl hpt, sum_const, nsmul_eq_mul, mul_one]
  rw [hmult]
  set Pre := (gaborOffLineZerosUpTo T).filter
    (fun z => (k : ℝ) < z.im ∧ z.im ≤ (k : ℝ) + 1)
  have himage : Sk ⊆ Pre.image gaborCanonicalKey := by
    intro q hq
    have hqZ := mem_filter.mp hq
    have hqpts : q ∈ gaborTruncationPts T := hqZ.1
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hqpts
    refine mem_image.mpr ⟨z, ?_, rfl⟩
    exact mem_filter.mpr ⟨hz, hqZ.2⟩
  have hcard_img : (Sk.card : ℕ) ≤ Pre.card :=
    (Finset.card_le_card himage).trans (Finset.card_image_le)
  have hsub : Pre ⊆ stripZerosWindow (k : ℝ) := by
    intro z hz
    have hzf := mem_filter.mp hz
    exact gaborOffLine_subset_strip hzf.1 hzf.2
  have hcard_pre : Pre.card ≤ (stripZerosWindow (k : ℝ)).card :=
    Finset.card_le_card hsub
  exact Nat.cast_le.mpr (hcard_img.trans hcard_pre)

/-- Multiplicity-weighted truncation occupancy.
`stripZerosWindow` / `zeta_unit_increment` count *distinct*
zeros (Finset / `ncard`), not analytic orders.  Jensen-with-
multiplicity (`sum_multiplicity_stripZerosWindow_le`) plus
FE-invariant order `m(z) = m(1-z)` on the whole strip
(`riemannZetaMultiplicity_eq_one_sub_all`) give
`∑ m_z ≤ gaborKBinAt |k|`, including compact bins. -/
def GaborTruncationWeightedCompliant : Prop :=
  ∀ T : ℝ,
    (∀ k : ℤ,
      ((gaborOffLineZerosUpTo T).filter
          (fun z => (k : ℝ) < z.im ∧ z.im ≤ (k : ℝ) + 1)).sum
        (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
          gaborKBinAt (|k| : ℝ))

theorem gaborTruncationWeightedCompliant_holds :
    GaborTruncationWeightedCompliant := by
  intro T k
  set Pre := (gaborOffLineZerosUpTo T).filter
    (fun z => (k : ℝ) < z.im ∧ z.im ≤ (k : ℝ) + 1)
  have hsub : Pre ⊆ stripZerosWindow (k : ℝ) := by
    intro z hz
    have hzf := mem_filter.mp hz
    exact gaborOffLine_subset_strip hzf.1 hzf.2
  have hsum :
      Pre.sum (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        (stripZerosWindow (k : ℝ)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) :=
    Finset.sum_le_sum_of_subset_of_nonneg
      (f := fun z => (riemannZetaMultiplicity z : ℝ)) hsub
      (fun _ _ _ => (Nat.cast_nonneg _ : (0 : ℝ) ≤ _))
  have hwin := sum_multiplicity_stripZerosWindow_le (k : ℝ)
  have hK : (stripZerosWindow (k : ℝ)).sum
      (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        gaborKBinAt (|k| : ℝ) := by
    simpa [gaborKBinAt] using hwin
  exact hsum.trans hK

/-! ## Bridge 6: Finset exhaustion algebra -/

noncomputable def gaborQuadrupoleSum (a omega : ℝ)
    (Z : GaborCanonicalConfig) : ℝ :=
  Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2)

theorem gaborHonestWeil_eq_quadrupoleSum (a omega : ℝ)
    (Z : GaborCanonicalConfig) (Cinc : ℝ) :
    gaborHonestWeil a omega Z Cinc =
      gaborQuadrupoleSum a omega Z +
        gaborHonestOnlineBudget a omega Cinc :=
  rfl

noncomputable def gaborOffLineSpectralMass (F : GaborWeilTest) : ℝ :=
  (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
    if (ρ : ℂ).re ≠ 1 / 2 then
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
    else 0).re

/-- Local replica of the r576 compact+log multiplicity bound
(avoids importing `GaborVerticalLimit`, which r578 is editing). -/
lemma riemannZetaMultiplicity_le_log_all_local {z : ℂ}
    (hz : IsCriticalStripZetaZero z) :
    (riemannZetaMultiplicity z : ℝ) ≤
      (zetaZerosInDiskCardBoundInner +
        ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
          (riemannZetaMultiplicity ρ : ℝ)) *
        (1 + Real.log (2 + |z.im| + 5 / 4)) := by
  set S := riemannZetaZerosOnClosedRect 0 1 2
  set M : ℝ := ∑ ρ ∈ S, (riemannZetaMultiplicity ρ : ℝ)
  set C : ℝ := zetaZerosInDiskCardBoundInner + M
  have hM0 : 0 ≤ M :=
    Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _
  have hC0 : 0 ≤ C :=
    add_nonneg (le_of_lt zetaZerosInDiskCardBoundInner_pos) hM0
  have hlog : (1 : ℝ) ≤ 1 + Real.log (2 + |z.im| + 5 / 4) :=
    le_add_of_nonneg_right
      (Real.log_nonneg (by nlinarith [abs_nonneg z.im]))
  by_cases him : (2 : ℝ) ≤ |z.im| ∨ (1 / 2 : ℝ) ≤ z.re
  · have hle := riemannZetaMultiplicity_le_log hz him
    have hC : zetaZerosInDiskCardBoundInner ≤ C :=
      le_add_of_nonneg_right hM0
    exact hle.trans (mul_le_mul_of_nonneg_right hC
      (add_nonneg (by norm_num)
        (Real.log_nonneg (by nlinarith [abs_nonneg z.im]))))
  · have himlt : |z.im| < 2 := by
      rw [not_or] at him
      exact lt_of_not_ge him.1
    have hzS : z ∈ S :=
      mem_rect_of_criticalStrip hz (le_of_lt himlt)
    have hterm : (riemannZetaMultiplicity z : ℝ) ≤ M :=
      Finset.single_le_sum (fun _ _ => Nat.cast_nonneg _) hzS
    have hMC : M ≤ C := le_add_of_nonneg_left
      (le_of_lt zetaZerosInDiskCardBoundInner_pos)
    exact hterm.trans (hMC.trans (le_mul_of_one_le_right hC0 hlog))

lemma mul_exp_neg_le_exp_neg_one {x : ℝ} (_hx : 0 ≤ x) :
    x * Real.exp (-x) ≤ Real.exp (-1) := by
  have h : x ≤ Real.exp (x - 1) := by
    have := Real.add_one_le_exp (x - 1)
    linarith
  have : x * Real.exp (-x) ≤ Real.exp (x - 1) * Real.exp (-x) :=
    mul_le_mul_of_nonneg_right h (Real.exp_pos _).le
  have hident : Real.exp (x - 1) * Real.exp (-x) = Real.exp (-1) := by
    rw [← Real.exp_add]
    congr 1
    ring
  exact this.trans_eq hident

lemma abs_mul_gauss_sq_bounded {α : ℝ} (hα : 0 < α) (t : ℝ) :
    |t| * Real.exp (-(α * t ^ 2)) ≤
      max (1 : ℝ) (1 / (α * Real.exp 1)) := by
  have hmax : (1 : ℝ) ≤ max (1 : ℝ) (1 / (α * Real.exp 1)) :=
    le_max_left _ _
  by_cases ht : |t| ≤ 1
  · have : |t| * Real.exp (-(α * t ^ 2)) ≤ 1 := by
      have hexp : Real.exp (-(α * t ^ 2)) ≤ 1 :=
        Real.exp_le_one_iff.mpr (neg_nonpos.mpr
          (mul_nonneg hα.le (sq_nonneg _)))
      exact (mul_le_mul ht hexp (Real.exp_pos _).le (by norm_num)).trans_eq
        (one_mul _)
    exact this.trans hmax
  · have ht1 : (1 : ℝ) ≤ |t| := le_of_not_ge ht
    have hsq : |t| ≤ t ^ 2 := by
      nlinarith [ht1, sq_abs t, abs_nonneg t]
    have hexp : Real.exp (-(α * t ^ 2)) ≤ Real.exp (-(α * |t|)) :=
      Real.exp_le_exp.mpr (neg_le_neg (mul_le_mul_of_nonneg_left hsq hα.le))
    have h1 : |t| * Real.exp (-(α * t ^ 2)) ≤ |t| * Real.exp (-(α * |t|)) :=
      mul_le_mul_of_nonneg_left hexp (abs_nonneg _)
    have h2 : |t| * Real.exp (-(α * |t|)) =
        (1 / α) * ((α * |t|) * Real.exp (-(α * |t|))) := by
      field_simp [hα.ne']
    have h3 : (α * |t|) * Real.exp (-(α * |t|)) ≤ Real.exp (-1) :=
      mul_exp_neg_le_exp_neg_one (mul_nonneg hα.le (abs_nonneg _))
    have h4 : (1 / α) * ((α * |t|) * Real.exp (-(α * |t|))) ≤
        (1 / α) * Real.exp (-1) :=
      mul_le_mul_of_nonneg_left h3 (div_nonneg (by norm_num) hα.le)
    have h5 : (1 / α) * Real.exp (-1) = 1 / (α * Real.exp 1) := by
      rw [Real.exp_neg]
      field_simp [hα.ne', (Real.exp_pos (1 : ℝ)).ne']
    have : |t| * Real.exp (-(α * t ^ 2)) ≤ 1 / (α * Real.exp 1) :=
      (h1.trans_eq h2).trans (h4.trans_eq h5)
    exact this.trans (le_max_right _ _)

lemma one_add_log_mul_gauss_le_local {c : ℝ} (hc : 0 < c) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ t : ℝ,
      (1 + Real.log (2 + |t| + 5 / 4)) * Real.exp (-c * t ^ 2) ≤
        K * Real.exp (-(c / 2) * t ^ 2) := by
  have hc2 : 0 < c / 2 := half_pos hc
  set B : ℝ := max (1 : ℝ) (1 / ((c / 2) * Real.exp 1))
  have hB : (1 : ℝ) ≤ B := le_max_left _ _
  have hB0 : 0 ≤ B := le_trans (by norm_num : (0 : ℝ) ≤ 1) hB
  set K : ℝ := (13 / 4) + B
  have hK0 : 0 ≤ K := by
    unfold K; linarith [hB0]
  refine ⟨K, hK0, fun t => ?_⟩
  have hx : (1 : ℝ) ≤ 2 + |t| + 5 / 4 := by
    nlinarith [abs_nonneg t]
  have hlin : 1 + Real.log (2 + |t| + 5 / 4) ≤ 2 + |t| + 5 / 4 :=
    one_add_log_le_self hx
  have hassoc2 : -(c / 2) * t ^ 2 = -((c / 2) * t ^ 2) := by ring
  have hsplit : Real.exp (-c * t ^ 2) =
      Real.exp (-(c / 2) * t ^ 2) * Real.exp (-(c / 2) * t ^ 2) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have hA : (13 / 4 : ℝ) * Real.exp (-(c / 2) * t ^ 2) ≤
      (13 / 4 : ℝ) := by
    have : Real.exp (-(c / 2) * t ^ 2) ≤ 1 :=
      Real.exp_le_one_iff.mpr (by
        rw [hassoc2]
        exact neg_nonpos.mpr (mul_nonneg hc2.le (sq_nonneg _)))
    exact mul_le_of_le_one_right (by norm_num) this
  have habs := abs_mul_gauss_sq_bounded hc2 t
  have hB' : |t| * Real.exp (-(c / 2) * t ^ 2) ≤ B := by
    rw [hassoc2]
    simpa [B] using habs
  have hsum :
      (2 + |t| + 5 / 4) * Real.exp (-(c / 2) * t ^ 2) ≤
        (13 / 4) + B := by
    have : (2 + |t| + 5 / 4) * Real.exp (-(c / 2) * t ^ 2) =
        (13 / 4) * Real.exp (-(c / 2) * t ^ 2) +
          |t| * Real.exp (-(c / 2) * t ^ 2) := by
      ring
    rw [this]
    linarith [hA, hB']
  calc
    (1 + Real.log (2 + |t| + 5 / 4)) * Real.exp (-c * t ^ 2) ≤
        (2 + |t| + 5 / 4) * Real.exp (-c * t ^ 2) :=
      mul_le_mul_of_nonneg_right hlin (Real.exp_pos _).le
    _ = ((2 + |t| + 5 / 4) * Real.exp (-(c / 2) * t ^ 2)) *
          Real.exp (-(c / 2) * t ^ 2) := by
      rw [hsplit]; ring
    _ ≤ K * Real.exp (-(c / 2) * t ^ 2) :=
      mul_le_mul_of_nonneg_right hsum (Real.exp_pos _).le

def GaborMultiplicityWeightedHatSummable : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ

theorem gaborMultiplicityWeightedHatSummable :
    GaborMultiplicityWeightedHatSummable := by
  intro F hF
  obtain ⟨c, Chat, hc, hChat, hhat⟩ := norm_gaborHat_le_gauss_critical hF
  obtain ⟨K, hK0, hK⟩ := one_add_log_mul_gauss_le_local hc
  set Cm : ℝ :=
    zetaZerosInDiskCardBoundInner +
      ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
        (riemannZetaMultiplicity ρ : ℝ)
  have hCm0 : 0 < Cm :=
    lt_of_lt_of_le zetaZerosInDiskCardBoundInner_pos
      (le_add_of_nonneg_right
        (Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _))
  have hbd : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ ≤
        (Cm * Chat * K) * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) := by
    intro ρ
    have hnorm :
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ =
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖gaborHat F ρ‖ := by
      rw [norm_mul]
      simp
    have hm := riemannZetaMultiplicity_le_log_all_local ρ.property
    have hh := hhat ρ ρ.property
    have hlogg := hK (ρ : ℂ).im
    have h1 := mul_le_mul hm hh (norm_nonneg _)
      (mul_nonneg (le_of_lt hCm0)
        (add_nonneg (by norm_num)
          (Real.log_nonneg (by nlinarith [abs_nonneg (ρ : ℂ).im]))))
    have h2 :
        Cm * (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
            (Chat * Real.exp (-c * (ρ : ℂ).im ^ 2)) =
          Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) := by
      ring
    have h3 :
        Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) ≤
          Cm * Chat * (K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2)) :=
      mul_le_mul_of_nonneg_left hlogg
        (mul_nonneg (le_of_lt hCm0) hChat.le)
    have hprod := (h1.trans_eq h2).trans h3
    rw [hnorm]
    simpa [mul_assoc] using hprod
  refine Summable.of_norm
    (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hbd
      ((summable_gauss_over_zeros (half_pos hc)).mul_left (Cm * Chat * K)))

/-- r585: `Re(tsum if_on m ĥ) ≤ tsum m‖ĥ‖ ≤ C_hat · log-majorant`. -/
theorem gaborCriticalLineMass_le_logMajorant_tsum
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    gaborCriticalLineMass F ≤
      gaborHatThreeLobeConst F.a (1 / 2) *
        gaborLogThreeLobeMajorant F.a F.omega := by
  have ha : 0 < F.a := F.a_pos
  have hC : 0 ≤ gaborHatThreeLobeConst F.a (1 / 2) :=
    gaborHatThreeLobeConst_nonneg F.a (1 / 2) ha
  have hMsω := gaborLogWeightedThetaSummable ha F.omega
  have hMsω' := gaborLogWeightedThetaSummable ha (-F.omega)
  have hMs0 := gaborLogWeightedThetaSummable ha (0 : ℝ)
  have hsm := gaborMultiplicityWeightedHatSummable F hF
  let f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun ρ =>
      if (ρ : ℂ).re = 1 / 2 then
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
      else 0
  have hf_le : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      ‖f ρ‖ ≤
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ := by
    intro ρ
    by_cases honρ : (ρ : ℂ).re = 1 / 2
    · simp only [f]
      rw [if_pos honρ]
    · simp only [f]
      rw [if_neg honρ, norm_zero]
      exact norm_nonneg
        ((riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ)
  have hon : Summable f :=
    Summable.of_norm
      (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hf_le hsm.norm)
  have hfnn : ∀ ρ, 0 ≤ ‖f ρ‖ := fun _ => norm_nonneg _
  have hfin : ∀ S : Finset {z : ℂ // IsCriticalStripZetaZero z},
      S.sum (fun ρ => ‖f ρ‖) ≤
        gaborHatThreeLobeConst F.a (1 / 2) *
          gaborLogThreeLobeMajorant F.a F.omega := by
    intro S
    have hS :=
      threeLobe_mult_stripZeros_le_logMajorant ha S hMsω hMsω' hMs0
    have hpt : ∀ ρ ∈ S,
        ‖f ρ‖ ≤
          gaborHatThreeLobeConst F.a (1 / 2) *
            ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaborThreeLobe F.a F.omega (ρ : ℂ).im) := by
      intro ρ _hρ
      by_cases honρ : (ρ : ℂ).re = 1 / 2
      · have hfρ : f ρ =
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ := by
          simp only [f]
          exact if_pos honρ
        rw [hfρ, norm_mul]
        simp
        have hthree := norm_gaborHat_le_three_lobe (F := F) hF (ρ : ℂ)
        have hthree' : ‖gaborHat F ρ‖ ≤
            gaborHatThreeLobeConst F.a (1 / 2) *
              gaborThreeLobe F.a F.omega (ρ : ℂ).im := by
          simpa [honρ] using hthree
        have hh :=
          mul_le_mul_of_nonneg_left hthree'
            (Nat.cast_nonneg (riemannZetaMultiplicity (ρ : ℂ)))
        simpa [mul_assoc, mul_left_comm, mul_comm] using hh
      · have hfρ : f ρ = 0 := by
          simp only [f]
          exact if_neg honρ
        rw [hfρ, norm_zero]
        exact mul_nonneg hC
          (mul_nonneg (Nat.cast_nonneg (riemannZetaMultiplicity (ρ : ℂ)))
            (gaborThreeLobe_nonneg F.a F.omega (ρ : ℂ).im))
    calc
      S.sum (fun ρ => ‖f ρ‖)
          ≤ S.sum (fun ρ =>
              gaborHatThreeLobeConst F.a (1 / 2) *
                ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                  gaborThreeLobe F.a F.omega (ρ : ℂ).im)) :=
        sum_le_sum hpt
      _ = gaborHatThreeLobeConst F.a (1 / 2) *
            S.sum (fun ρ =>
              (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                gaborThreeLobe F.a F.omega (ρ : ℂ).im) := by
        simp [mul_sum]
      _ ≤ gaborHatThreeLobeConst F.a (1 / 2) *
            gaborLogThreeLobeMajorant F.a F.omega :=
        mul_le_mul_of_nonneg_left hS hC
  have hts : ∑' ρ, ‖f ρ‖ ≤
      gaborHatThreeLobeConst F.a (1 / 2) *
        gaborLogThreeLobeMajorant F.a F.omega :=
    Real.tsum_le_of_sum_le hfnn hfin
  have hre : (∑' ρ, f ρ).re ≤ ‖∑' ρ, f ρ‖ :=
    (le_abs_self _).trans (Complex.abs_re_le_norm _)
  have hnts := norm_tsum_le_tsum_norm (f := f) hon.norm
  unfold gaborCriticalLineMass
  change (∑' ρ, f ρ).re ≤ _
  exact (hre.trans hnts).trans hts

theorem gaborCriticalLineMassLeLogMajorant_holds :
    GaborCriticalLineMassLeLogMajorant :=
  fun F hF =>
    gaborCriticalLineMass_le_closed_of_tsum hF
      (gaborCriticalLineMass_le_logMajorant_tsum hF)

/-- Goal 3 algebra: a sequence bounded above by `-δ` cannot
converge above `-δ`. -/
theorem gabor_exhaustion_algebra
    {a omega Cinc δ : ℝ} {s : ℕ → ℝ} {L : ℝ}
    (_hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      s n + gaborHonestOnlineBudget a omega Cinc ≤ -δ)
    (hlim : Tendsto s atTop (𝓝 L)) :
    L + gaborHonestOnlineBudget a omega Cinc ≤ -δ := by
  have htend :
      Tendsto (fun n => s n + gaborHonestOnlineBudget a omega Cinc)
        atTop (𝓝 (L + gaborHonestOnlineBudget a omega Cinc)) :=
    hlim.add tendsto_const_nhds
  exact le_of_tendsto htend (Eventually.of_forall hW)

theorem gabor_truncation_quadrupole_limit_le
    {a omega Cinc δ : ℝ} {L : ℝ} (hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)) Cinc ≤ -δ)
    (hlim : Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop (𝓝 L)) :
    L + gaborHonestOnlineBudget a omega Cinc ≤ -δ := by
  refine gabor_exhaustion_algebra (a := a) (omega := omega)
    (Cinc := Cinc) (δ := δ) (L := L) hδ ?_ hlim
  intro n
  simpa [gaborHonestWeil_eq_quadrupoleSum] using hW n

/-- Named remainder (Bridge 6 identification).  Live
`gaborTruncationConfig` has `mult ≡ 1`, so this unweighted Q-limit
equals the multiplicity-weighted off-line mass only if every
windowed zero is simple.  Conditional form:
`gaborQuadrupoleLimitEqOffLineMass_of_simple`.  The honest
weighted form is the r588 theorem
`gaborWeightedQuadrupoleLimitEqOffLineMass_holds`.  Not a `sorry`. -/
def GaborQuadrupoleLimitEqOffLineMass : Prop :=
  ∀ (a omega : ℝ) (ha : 0 < a),
    Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop
      (𝓝 (gaborOffLineSpectralMass (pureGaborTest a omega ha)))

/-- Zero-side split for every even quartic.  r587: unrestricted
form is the theorem `gaborZeroSideEqOffPlusOn_holds`. -/
def GaborZeroSideEqOffPlusOn : Prop :=
  ∀ F : GaborWeilTest,
    gaborZeroSide F =
      gaborOffLineSpectralMass F + gaborCriticalLineMass F

/-- r586 remainder, discharged r587: multiplicity-weighted `ĥ`
over strip zeros for a general even quartic. -/
def GaborMultiplicityWeightedHatSummableQuartic : Prop :=
  ∀ F : GaborWeilTest,
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ

theorem gaborMultiplicityWeightedHatSummableQuartic_holds :
    GaborMultiplicityWeightedHatSummableQuartic := by
  intro F
  obtain ⟨c, Chat, hc, hChat, hhat⟩ :=
    norm_gaborHat_le_gauss_critical_quartic F
  obtain ⟨K, hK0, hK⟩ := one_add_log_mul_gauss_le_local hc
  set Cm : ℝ :=
    zetaZerosInDiskCardBoundInner +
      ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
        (riemannZetaMultiplicity ρ : ℝ)
  have hCm0 : 0 < Cm :=
    lt_of_lt_of_le zetaZerosInDiskCardBoundInner_pos
      (le_add_of_nonneg_right
        (Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _))
  have hbd : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ ≤
        (Cm * Chat * K) * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2) := by
    intro ρ
    have hnorm :
        ‖(riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ‖ =
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) * ‖gaborHat F ρ‖ := by
      rw [norm_mul]
      simp
    have hm := riemannZetaMultiplicity_le_log_all_local ρ.property
    have hh := hhat ρ ρ.property
    have hlogg := hK (ρ : ℂ).im
    have h1 := mul_le_mul hm hh (norm_nonneg _)
      (mul_nonneg (le_of_lt hCm0)
        (add_nonneg (by norm_num)
          (Real.log_nonneg (by nlinarith [abs_nonneg (ρ : ℂ).im]))))
    have h2 :
        Cm * (1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
            (Chat * Real.exp (-c * (ρ : ℂ).im ^ 2)) =
          Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) := by
      ring
    have h3 :
        Cm * Chat *
            ((1 + Real.log (2 + |(ρ : ℂ).im| + 5 / 4)) *
              Real.exp (-c * (ρ : ℂ).im ^ 2)) ≤
          Cm * Chat * (K * Real.exp (-(c / 2) * (ρ : ℂ).im ^ 2)) :=
      mul_le_mul_of_nonneg_left hlogg
        (mul_nonneg (le_of_lt hCm0) hChat.le)
    have hprod := (h1.trans_eq h2).trans h3
    rw [hnorm]
    simpa [mul_assoc] using hprod
  refine Summable.of_norm
    (Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hbd
      ((summable_gauss_over_zeros (half_pos hc)).mul_left (Cm * Chat * K)))

/-- r584: the unrestricted Prop needs quartic summability.  Under
absolute convergence the indicator split is `tsum` algebra. -/
theorem gaborZeroSide_eq_off_plus_on_of_summable
    {F : GaborWeilTest}
    (hsm : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) :
    gaborZeroSide F =
      gaborOffLineSpectralMass F + gaborCriticalLineMass F := by
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
  have hpt : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      f ρ =
        (if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0) +
          (if (ρ : ℂ).re = 1 / 2 then f ρ else 0) := by
    intro ρ
    by_cases hon : (ρ : ℂ).re = 1 / 2
    · rw [if_neg (not_not.mpr hon), if_pos hon, zero_add]
    · rw [if_pos hon, if_neg hon, add_zero]
  have hoff : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0 :=
    Summable.of_norm
      (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
        (fun ρ => by
          split_ifs
          · exact le_rfl
          · simpa using norm_nonneg (f ρ))
        hsm.norm)
  have hon : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      if (ρ : ℂ).re = 1 / 2 then f ρ else 0 :=
    Summable.of_norm
      (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
        (fun ρ => by
          split_ifs
          · exact le_rfl
          · simpa using norm_nonneg (f ρ))
        hsm.norm)
  have hts :
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z}, f ρ) =
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0) +
          (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            if (ρ : ℂ).re = 1 / 2 then f ρ else 0) := by
    have hsum := hoff.tsum_add hon
    rw [← hsum]
    exact tsum_congr hpt
  unfold gaborZeroSide gaborOffLineSpectralMass gaborCriticalLineMass
  change (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z}, f ρ).re =
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0).re +
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        if (ρ : ℂ).re = 1 / 2 then f ρ else 0).re
  rw [hts, Complex.add_re]

theorem gaborZeroSide_eq_off_plus_on_pure
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    gaborZeroSide F =
      gaborOffLineSpectralMass F + gaborCriticalLineMass F :=
  gaborZeroSide_eq_off_plus_on_of_summable
    (gaborMultiplicityWeightedHatSummable F hF)

theorem gaborZeroSideEqOffPlusOn_of_quartic_summable
    (hsm : GaborMultiplicityWeightedHatSummableQuartic) :
    GaborZeroSideEqOffPlusOn :=
  fun F => gaborZeroSide_eq_off_plus_on_of_summable (hsm F)

theorem gaborZeroSideEqOffPlusOn_holds : GaborZeroSideEqOffPlusOn :=
  gaborZeroSideEqOffPlusOn_of_quartic_summable
    gaborMultiplicityWeightedHatSummableQuartic_holds

/-- Strip zeros are closed under conjugation.  Schwarz reflection
for `riemannZeta` is `riemannZeta_conj`. -/
lemma isCriticalStrip_star {z : ℂ} (hz : IsCriticalStripZetaZero z) :
    IsCriticalStripZetaZero (star z) := by
  have hz1 : z ≠ 1 := isCriticalStripZetaZero_ne_one hz
  have hstar1 : star z ≠ 1 := by
    intro h
    have : (star z).re = 1 := by simp [h]
    have : z.re = 1 := by
      simpa [Complex.star_def, Complex.conj_re] using this
    linarith [hz.2.2, this]
  refine ⟨?_, ?_, ?_⟩
  · have := riemannZeta_conj hz1
    simpa [this, hz.1] using congrArg star hz.1
  · simpa [Complex.star_def, Complex.conj_re] using hz.2.1
  · simpa [Complex.star_def, Complex.conj_re] using hz.2.2

/-- r584 named remainder, discharged r585: analytic order is
conjugation-invariant on the strip.  Transport is
`analyticOrderAt_conj_conj` plus Schwarz reflection. -/
def RiemannZetaMultiplicityEqConj : Prop :=
  ∀ {z : ℂ}, IsCriticalStripZetaZero z →
    riemannZetaMultiplicity (star z) = riemannZetaMultiplicity z

theorem riemannZetaMultiplicityEqConj_holds :
    RiemannZetaMultiplicityEqConj :=
  fun hz => riemannZetaMultiplicity_eq_star
    (isCriticalStripZetaZero_ne_one hz)

lemma star_half : star (1 / 2 : ℂ) = (1 / 2 : ℂ) := by
  simp

lemma star_cexp (z : ℂ) :
    star (Complex.exp z) = Complex.exp (star z) := by
  simpa [Complex.star_def] using (Complex.conj_exp z).symm

lemma star_div (x y : ℂ) : star (x / y) = star x / star y :=
  map_div₀ (starRingEnd ℂ) x y

lemma star_pow (x : ℂ) (n : ℕ) : star (x ^ n) = star x ^ n :=
  map_pow (starRingEnd ℂ) x n

lemma star_mul (x y : ℂ) : star (x * y) = star x * star y :=
  map_mul (starRingEnd ℂ) x y

lemma star_add (x y : ℂ) : star (x + y) = star x + star y :=
  map_add (starRingEnd ℂ) x y

lemma star_neg (x : ℂ) : star (-x) = -star x :=
  map_neg (starRingEnd ℂ) x

lemma star_sub (x y : ℂ) : star (x - y) = star x - star y :=
  map_sub (starRingEnd ℂ) x y

lemma star_pureGaborHatHolomorphic (a omega : ℝ) (δ : ℂ) :
    pureGaborHatHolomorphic a omega (star δ) =
      star (pureGaborHatHolomorphic a omega δ) := by
  unfold pureGaborHatHolomorphic
  have hC :
      star ((Real.pi / (4 * a) : ℝ) : ℂ) =
        ((Real.pi / (4 * a) : ℝ) : ℂ) := by
    simp
  have h2a : star ((2 * a : ℝ) : ℂ) = ((2 * a : ℝ) : ℂ) := by
    simp
  have hIω : star (Complex.I * (omega : ℂ)) = -(Complex.I * (omega : ℂ)) := by
    simp [map_mul (starRingEnd ℂ), Complex.star_def, Complex.conj_I]
  have hp :
      star ((δ + Complex.I * omega) ^ 2 / (2 * a : ℂ)) =
        (star δ - Complex.I * omega) ^ 2 / (2 * a : ℂ) := by
    rw [star_div, star_pow, star_add, hIω, ← sub_eq_add_neg]
    simp
  have hm :
      star ((δ - Complex.I * omega) ^ 2 / (2 * a : ℂ)) =
        (star δ + Complex.I * omega) ^ 2 / (2 * a : ℂ) := by
    rw [star_div, star_pow, star_sub, hIω]
    simp
  have hmidω :
      star ((-(omega : ℂ) ^ 2) / (2 * a : ℂ)) =
        (-(omega : ℂ) ^ 2) / (2 * a : ℂ) := by
    rw [star_div, star_neg, star_pow]
    simp
  have hδ2 : star (δ ^ 2 / (2 * a : ℂ)) = star δ ^ 2 / (2 * a : ℂ) := by
    rw [star_div, star_pow]
    simp
  have hswap :
      Complex.exp ((star δ + Complex.I * omega) ^ 2 / (2 * a : ℂ)) +
          Complex.exp ((star δ - Complex.I * omega) ^ 2 / (2 * a : ℂ)) =
        star (Complex.exp ((δ + Complex.I * omega) ^ 2 / (2 * a : ℂ))) +
          star (Complex.exp ((δ - Complex.I * omega) ^ 2 / (2 * a : ℂ))) := by
    rw [star_cexp, star_cexp, hp, hm, add_comm]
  have hmid :
      (2 : ℂ) * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a : ℂ)) *
          Complex.exp (star δ ^ 2 / (2 * a : ℂ)) =
        star ((2 : ℂ) * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a : ℂ)) *
          Complex.exp (δ ^ 2 / (2 * a : ℂ))) := by
    rw [star_mul, star_mul, star_cexp, star_cexp, hmidω, hδ2]
    simp
  rw [star_mul, star_add, star_add, hC, hswap]
  have hmid' :
      star ((2 : ℂ) * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a : ℂ)) *
          Complex.exp (δ ^ 2 / (2 * a : ℂ))) =
        (2 : ℂ) * Complex.exp (-(omega : ℂ) ^ 2 / (2 * a : ℂ)) *
          Complex.exp (star δ ^ 2 / (2 * a : ℂ)) :=
    hmid.symm
  rw [hmid']

/-- r584 named remainder, discharged r585: pure `gaborHat` commutes
with conjugation.  The ±ω lobes swap; the central lobe is real
quadratic. -/
def GaborHatStarPure : Prop :=
  ∀ {F : GaborWeilTest}, F.coeffs = ⟨1, 0, 0⟩ → ∀ s : ℂ,
    gaborHat F (star s) = star (gaborHat F s)

theorem gaborHat_star_pure
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (s : ℂ) :
    gaborHat F (star s) = star (gaborHat F s) := by
  have hδ : star s - (1 / 2 : ℂ) = star (s - (1 / 2 : ℂ)) := by
    simp [map_sub, star_half]
  rw [gaborHat_eq_pureHolomorphic hF, gaborHat_eq_pureHolomorphic hF, hδ]
  exact star_pureGaborHatHolomorphic F.a F.omega (s - (1 / 2 : ℂ))

theorem gaborHatStarPure_holds : GaborHatStarPure :=
  fun hF s => gaborHat_star_pure hF s

/-- FE + star symmetry: the four Gabor values on an FE/conj orbit
collapse to `4 Re ĥ(s)`. -/
theorem gaborHat_fe_quadrupole_eq_four_re
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) (s : ℂ) :
    gaborHat F s + gaborHat F (1 - s) + gaborHat F (star s) +
      gaborHat F (1 - star s) =
      (4 : ℂ) * (gaborHat F s).re := by
  rw [gaborHat_one_sub F s, gaborHat_one_sub F (star s),
    gaborHat_star_pure hF s]
  set z := gaborHat F s
  have hsum : z + z + star z + star z = 2 * (z + star z) := by
    ring
  rw [hsum, Complex.star_def, Complex.add_conj]
  simp [Complex.ofReal_mul, Complex.ofReal_ofNat]
  ring

/-- r585 false grouping: weight `4` over every `Im>0` off-line
zero double-counts the orbit (`ρ` and `1-ρ̄` both have `Im>0`).
Kept unasserted as a warning.  Honest form:
`GaborOffLineMassEqWeightedQuadrupoleTsum`. -/
def GaborOffLineMassEqWeightedQuadrupoleTsum_doubleCounts : Prop :=
  ∀ (a omega : ℝ) (ha : 0 < a),
    gaborOffLineSpectralMass (pureGaborTest a omega ha) =
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        if (ρ : ℂ).re ≠ 1 / 2 ∧ 0 < (ρ : ℂ).im then
          (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat (pureGaborTest a omega ha) (ρ : ℂ)
        else 0).re

/-- Canonical FD matching `GaborCanonicalConfig` / `Q = 4 Re ĥ(1/2+σ+iγ)`:
`Re > 1/2 ∧ Im > 0`, weight 4. -/
def gaborFundDomain (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : Prop :=
  (1 / 2 : ℝ) < (ρ : ℂ).re ∧ 0 < (ρ : ℂ).im

noncomputable def gaborOffLineRealAxisMass (F : GaborWeilTest) : ℝ :=
  (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
    if (ρ : ℂ).re ≠ 1 / 2 ∧ (ρ : ℂ).im = 0 then
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
    else 0).re

/-- Honest quadrupole tsum: FD weight 4 plus the real-axis remainder
(classically empty; excluded by `gamma_pos`). -/
def GaborOffLineMassEqWeightedQuadrupoleTsum : Prop :=
  ∀ (a omega : ℝ) (ha : 0 < a),
    gaborOffLineSpectralMass (pureGaborTest a omega ha) =
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
        if gaborFundDomain ρ then
          (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat (pureGaborTest a omega ha) (ρ : ℂ)
        else 0).re +
        gaborOffLineRealAxisMass (pureGaborTest a omega ha)

/-- Left-up partner of the FD: `Re<1/2 ∧ Im>0` (`1-ρ̄`). -/
def gaborLeftUp (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : Prop :=
  (ρ : ℂ).re < (1 / 2 : ℝ) ∧ 0 < (ρ : ℂ).im

/-- Right-down partner: `Re>1/2 ∧ Im<0` (`ρ̄`). -/
def gaborRightDown (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : Prop :=
  (1 / 2 : ℝ) < (ρ : ℂ).re ∧ (ρ : ℂ).im < 0

/-- Left-down partner: `Re<1/2 ∧ Im<0` (`1-ρ`). -/
def gaborLeftDown (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : Prop :=
  (ρ : ℂ).re < (1 / 2 : ℝ) ∧ (ρ : ℂ).im < 0

def gaborRealOff (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : Prop :=
  (ρ : ℂ).re ≠ 1 / 2 ∧ (ρ : ℂ).im = 0

noncomputable def stripStarEquiv :
    {z : ℂ // IsCriticalStripZetaZero z} ≃
      {z : ℂ // IsCriticalStripZetaZero z} where
  toFun ρ := ⟨star (ρ : ℂ), isCriticalStrip_star ρ.property⟩
  invFun ρ := ⟨star (ρ : ℂ), isCriticalStrip_star ρ.property⟩
  left_inv ρ := Subtype.ext (star_star (ρ : ℂ))
  right_inv ρ := Subtype.ext (star_star (ρ : ℂ))

noncomputable def stripFEEquiv :
    {z : ℂ // IsCriticalStripZetaZero z} ≃
      {z : ℂ // IsCriticalStripZetaZero z} where
  toFun ρ := ⟨1 - (ρ : ℂ), isCriticalStrip_one_sub ρ.property⟩
  invFun ρ := ⟨1 - (ρ : ℂ), isCriticalStrip_one_sub ρ.property⟩
  left_inv ρ := Subtype.ext (by ring)
  right_inv ρ := Subtype.ext (by ring)

/-- `ρ ↦ 1-ρ̄`.  Swaps the FD with left-up. -/
noncomputable def stripOrbitEquiv :
    {z : ℂ // IsCriticalStripZetaZero z} ≃
      {z : ℂ // IsCriticalStripZetaZero z} :=
  stripStarEquiv.trans stripFEEquiv

lemma tsum_indicator_equiv {α : Type*}
    (e : α ≃ α) (P : α → Prop) [DecidablePred P] (g : α → ℂ) :
    (∑' a, if P a then g (e a) else 0) =
      ∑' b, if P (e.symm b) then g b else 0 := by
  simpa using e.tsum_eq (fun b => if P (e.symm b) then g b else 0)

lemma fundDomain_star_iff
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    gaborFundDomain (stripStarEquiv.symm ρ) ↔ gaborRightDown ρ := by
  change ((1 / 2 : ℝ) < (star (ρ : ℂ)).re ∧
      0 < (star (ρ : ℂ)).im) ↔
    ((1 / 2 : ℝ) < (ρ : ℂ).re ∧ (ρ : ℂ).im < 0)
  simp [Complex.conj_re, Complex.conj_im]

lemma fundDomain_fe_iff
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    gaborFundDomain (stripFEEquiv.symm ρ) ↔ gaborLeftDown ρ := by
  change ((1 / 2 : ℝ) < (1 - (ρ : ℂ)).re ∧
      0 < (1 - (ρ : ℂ)).im) ↔
    ((ρ : ℂ).re < (1 / 2 : ℝ) ∧ (ρ : ℂ).im < 0)
  simp [Complex.sub_re, Complex.sub_im]
  intro
  constructor <;> intro <;> linarith

lemma fundDomain_orbit_iff
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    gaborFundDomain (stripOrbitEquiv.symm ρ) ↔ gaborLeftUp ρ := by
  change ((1 / 2 : ℝ) < (star (1 - (ρ : ℂ))).re ∧
      0 < (star (1 - (ρ : ℂ))).im) ↔
    ((ρ : ℂ).re < (1 / 2 : ℝ) ∧ 0 < (ρ : ℂ).im)
  simp [Complex.conj_re, Complex.conj_im, Complex.sub_re, Complex.sub_im]
  intro
  constructor <;> intro <;> linarith

lemma summable_indicator_of {α : Type*}
    {f : α → ℂ} (hf : Summable f) (P : α → Prop) [DecidablePred P] :
    Summable fun a => if P a then f a else 0 :=
  Summable.of_norm
    (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun a => by
        split_ifs
        · exact le_rfl
        · simpa using norm_nonneg (f a))
      hf.norm)

lemma gabor_orbit_sum_eq_four_re
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ +
      (riemannZetaMultiplicity (star (ρ : ℂ)) : ℂ) *
        gaborHat F (star (ρ : ℂ)) +
      (riemannZetaMultiplicity (1 - (ρ : ℂ)) : ℂ) *
        gaborHat F (1 - (ρ : ℂ)) +
      (riemannZetaMultiplicity (1 - star (ρ : ℂ)) : ℂ) *
        gaborHat F (1 - star (ρ : ℂ)) =
      (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
        (gaborHat F ρ).re := by
  have hz1 : (ρ : ℂ) ≠ 1 := isCriticalStripZetaZero_ne_one ρ.property
  have hmstar := riemannZetaMultiplicity_eq_star hz1
  have hmfe := riemannZetaMultiplicity_eq_one_sub_all ρ.property
  have hstarZ := isCriticalStrip_star ρ.property
  have hmfe_star := riemannZetaMultiplicity_eq_one_sub_all hstarZ
  have h4 := gaborHat_fe_quadrupole_eq_four_re hF (ρ : ℂ)
  set m := (riemannZetaMultiplicity (ρ : ℂ) : ℂ)
  have hm1 : (riemannZetaMultiplicity (star (ρ : ℂ)) : ℂ) = m :=
    congrArg (fun n : ℕ => (n : ℂ)) hmstar
  have hm2 : (riemannZetaMultiplicity (1 - (ρ : ℂ)) : ℂ) = m :=
    congrArg (fun n : ℕ => (n : ℂ)) hmfe.symm
  have hm3 : (riemannZetaMultiplicity (1 - star (ρ : ℂ)) : ℂ) = m := by
    have h := congrArg (fun n : ℕ => (n : ℂ)) hmfe_star.symm
    exact h.trans hm1
  rw [hm1, hm2, hm3]
  calc
    m * gaborHat F ρ + m * gaborHat F (star (ρ : ℂ)) +
          m * gaborHat F (1 - (ρ : ℂ)) +
          m * gaborHat F (1 - star (ρ : ℂ)) =
        m * (gaborHat F ρ + gaborHat F (star (ρ : ℂ)) +
          gaborHat F (1 - (ρ : ℂ)) +
          gaborHat F (1 - star (ρ : ℂ))) := by ring
    _ = m * (gaborHat F ρ + gaborHat F (1 - (ρ : ℂ)) +
          gaborHat F (star (ρ : ℂ)) +
          gaborHat F (1 - star (ρ : ℂ))) := by ring
    _ = m * ((4 : ℂ) * (gaborHat F ρ).re) := by rw [h4]
    _ = (4 : ℂ) * m * (gaborHat F ρ).re := by ring

lemma offLine_split_five
    (f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0) =
      (if gaborFundDomain ρ then f ρ else 0) +
        (if gaborLeftUp ρ then f ρ else 0) +
        (if gaborRightDown ρ then f ρ else 0) +
        (if gaborLeftDown ρ then f ρ else 0) +
        (if gaborRealOff ρ then f ρ else 0) := by
  by_cases hre : (ρ : ℂ).re = 1 / 2
  · have hD : ¬ gaborFundDomain ρ := fun h => (ne_of_gt h.1) hre
    have hL : ¬ gaborLeftUp ρ := fun h => (ne_of_lt h.1) hre
    have hRd : ¬ gaborRightDown ρ := fun h => (ne_of_gt h.1) hre
    have hLd : ¬ gaborLeftDown ρ := fun h => (ne_of_lt h.1) hre
    have hR : ¬ gaborRealOff ρ := fun h => h.1 hre
    rw [if_neg (not_not.mpr hre), if_neg hD, if_neg hL, if_neg hRd,
      if_neg hLd, if_neg hR]
    simp
  · by_cases him : (ρ : ℂ).im = 0
    · have hD : ¬ gaborFundDomain ρ := fun h => (ne_of_gt h.2) him
      have hL : ¬ gaborLeftUp ρ := fun h => (ne_of_gt h.2) him
      have hRd : ¬ gaborRightDown ρ := fun h => (ne_of_lt h.2) him
      have hLd : ¬ gaborLeftDown ρ := fun h => (ne_of_lt h.2) him
      have hR : gaborRealOff ρ := ⟨hre, him⟩
      rw [if_pos hre, if_neg hD, if_neg hL, if_neg hRd, if_neg hLd, if_pos hR]
      ring
    · rcases lt_or_gt_of_ne (Ne.symm hre) with hgt | hlt
      · rcases lt_or_gt_of_ne (Ne.symm him) with hpos | hneg
        · have hD : gaborFundDomain ρ := ⟨hgt, hpos⟩
          have hL : ¬ gaborLeftUp ρ := fun h => (not_lt.mpr hgt.le) h.1
          have hRd : ¬ gaborRightDown ρ := fun h => (not_lt.mpr hpos.le) h.2
          have hLd : ¬ gaborLeftDown ρ := fun h => (not_lt.mpr hgt.le) h.1
          have hR : ¬ gaborRealOff ρ := fun h => him h.2
          rw [if_pos hre, if_pos hD, if_neg hL, if_neg hRd, if_neg hLd, if_neg hR]
          ring
        · have hD : ¬ gaborFundDomain ρ := fun h => (not_lt.mpr hneg.le) h.2
          have hL : ¬ gaborLeftUp ρ := fun h => (not_lt.mpr hgt.le) h.1
          have hRd : gaborRightDown ρ := ⟨hgt, hneg⟩
          have hLd : ¬ gaborLeftDown ρ := fun h => (not_lt.mpr hgt.le) h.1
          have hR : ¬ gaborRealOff ρ := fun h => him h.2
          rw [if_pos hre, if_neg hD, if_neg hL, if_pos hRd, if_neg hLd, if_neg hR]
          ring
      · rcases lt_or_gt_of_ne (Ne.symm him) with hpos | hneg
        · have hD : ¬ gaborFundDomain ρ := fun h => (not_lt.mpr hlt.le) h.1
          have hL : gaborLeftUp ρ := ⟨hlt, hpos⟩
          have hRd : ¬ gaborRightDown ρ := fun h => (not_lt.mpr hlt.le) h.1
          have hLd : ¬ gaborLeftDown ρ := fun h => (not_lt.mpr hpos.le) h.2
          have hR : ¬ gaborRealOff ρ := fun h => him h.2
          rw [if_pos hre, if_neg hD, if_pos hL, if_neg hRd, if_neg hLd, if_neg hR]
          ring
        · have hD : ¬ gaborFundDomain ρ := fun h => (not_lt.mpr hlt.le) h.1
          have hL : ¬ gaborLeftUp ρ := fun h => (not_lt.mpr hneg.le) h.2
          have hRd : ¬ gaborRightDown ρ := fun h => (not_lt.mpr hlt.le) h.1
          have hLd : gaborLeftDown ρ := ⟨hlt, hneg⟩
          have hR : ¬ gaborRealOff ρ := fun h => him h.2
          rw [if_pos hre, if_neg hD, if_neg hL, if_neg hRd, if_pos hLd, if_neg hR]
          ring

theorem gaborOffLineMassEqWeightedQuadrupoleTsum_holds :
    GaborOffLineMassEqWeightedQuadrupoleTsum := by
  intro a omega ha
  set F := pureGaborTest a omega ha
  have hF : F.coeffs = ⟨1, 0, 0⟩ := rfl
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun ρ => (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
  have hsm : Summable f :=
    gaborMultiplicityWeightedHatSummable F hF
  have hD := summable_indicator_of hsm gaborFundDomain
  have hL := summable_indicator_of hsm gaborLeftUp
  have hRd := summable_indicator_of hsm gaborRightDown
  have hLd := summable_indicator_of hsm gaborLeftDown
  have hR := summable_indicator_of hsm gaborRealOff
  have hfive :
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0) =
        (∑' ρ, if gaborFundDomain ρ then f ρ else 0) +
          (∑' ρ, if gaborLeftUp ρ then f ρ else 0) +
          (∑' ρ, if gaborRightDown ρ then f ρ else 0) +
          (∑' ρ, if gaborLeftDown ρ then f ρ else 0) +
          (∑' ρ, if gaborRealOff ρ then f ρ else 0) := by
    have s1 : Summable fun ρ =>
        (if gaborFundDomain ρ then f ρ else 0) +
          (if gaborLeftUp ρ then f ρ else 0) :=
      Summable.add hD hL
    have s2 : Summable fun ρ =>
        ((if gaborFundDomain ρ then f ρ else 0) +
          (if gaborLeftUp ρ then f ρ else 0)) +
          (if gaborRightDown ρ then f ρ else 0) :=
      Summable.add s1 hRd
    have s3 : Summable fun ρ =>
        (((if gaborFundDomain ρ then f ρ else 0) +
          (if gaborLeftUp ρ then f ρ else 0)) +
          (if gaborRightDown ρ then f ρ else 0)) +
          (if gaborLeftDown ρ then f ρ else 0) :=
      Summable.add s2 hLd
    have e1 := hD.tsum_add hL
    have e2 := s1.tsum_add hRd
    have e3 := s2.tsum_add hLd
    have e4 := s3.tsum_add hR
    refine (tsum_congr (offLine_split_five f)).trans ?_
    exact e4.trans (by rw [e3, e2, e1])
  have hstar :
      (∑' ρ, if gaborFundDomain ρ then f (stripStarEquiv ρ) else 0) =
        ∑' ρ, if gaborRightDown ρ then f ρ else 0 := by
    rw [tsum_indicator_equiv stripStarEquiv gaborFundDomain f]
    exact tsum_congr fun ρ => by simp [fundDomain_star_iff]
  have hfe :
      (∑' ρ, if gaborFundDomain ρ then f (stripFEEquiv ρ) else 0) =
        ∑' ρ, if gaborLeftDown ρ then f ρ else 0 := by
    rw [tsum_indicator_equiv stripFEEquiv gaborFundDomain f]
    exact tsum_congr fun ρ => by simp [fundDomain_fe_iff]
  have horbit :
      (∑' ρ, if gaborFundDomain ρ then f (stripOrbitEquiv ρ) else 0) =
        ∑' ρ, if gaborLeftUp ρ then f ρ else 0 := by
    rw [tsum_indicator_equiv stripOrbitEquiv gaborFundDomain f]
    exact tsum_congr fun ρ => by simp [fundDomain_orbit_iff]
  have hsmStar : Summable (f ∘ stripStarEquiv) :=
    (stripStarEquiv.summable_iff (f := f)).mpr hsm
  have hsmFE : Summable (f ∘ stripFEEquiv) :=
    (stripFEEquiv.summable_iff (f := f)).mpr hsm
  have hsmOrb : Summable (f ∘ stripOrbitEquiv) :=
    (stripOrbitEquiv.summable_iff (f := f)).mpr hsm
  have hDstar := summable_indicator_of hsmStar gaborFundDomain
  have hDFE := summable_indicator_of hsmFE gaborFundDomain
  have hDorb := summable_indicator_of hsmOrb gaborFundDomain
  have hpt : ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (if gaborFundDomain ρ then f ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripStarEquiv) ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripFEEquiv) ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripOrbitEquiv) ρ else 0) =
        if gaborFundDomain ρ then (4 : ℂ) * (f ρ).re else 0 := by
    intro ρ
    by_cases h : gaborFundDomain ρ
    · simp only [h, ↓reduceIte, Function.comp_apply]
      have hor := gabor_orbit_sum_eq_four_re hF ρ
      have h1 : f (stripStarEquiv ρ) =
          (riemannZetaMultiplicity (star (ρ : ℂ)) : ℂ) *
            gaborHat F (star (ρ : ℂ)) := by
        simp [f, stripStarEquiv]
      have h2 : f (stripFEEquiv ρ) =
          (riemannZetaMultiplicity (1 - (ρ : ℂ)) : ℂ) *
            gaborHat F (1 - (ρ : ℂ)) := by
        simp [f, stripFEEquiv]
      have h3 : f (stripOrbitEquiv ρ) =
          (riemannZetaMultiplicity (1 - star (ρ : ℂ)) : ℂ) *
            gaborHat F (1 - star (ρ : ℂ)) := by
        simp [f, stripOrbitEquiv, stripStarEquiv, stripFEEquiv, Equiv.trans]
      rw [h1, h2, h3]
      simpa [f, mul_assoc] using hor
    · simp [h]
  have hSum4 : Summable fun ρ =>
      ((if gaborFundDomain ρ then f ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripStarEquiv) ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripFEEquiv) ρ else 0) +
          (if gaborFundDomain ρ then (f ∘ stripOrbitEquiv) ρ else 0)) :=
    Summable.add (Summable.add (Summable.add hD hDstar) hDFE) hDorb
  have h4ts :
      (∑' ρ, if gaborFundDomain ρ then f ρ else 0) +
          (∑' ρ, if gaborFundDomain ρ then (f ∘ stripStarEquiv) ρ else 0) +
          (∑' ρ, if gaborFundDomain ρ then (f ∘ stripFEEquiv) ρ else 0) +
          (∑' ρ, if gaborFundDomain ρ then (f ∘ stripOrbitEquiv) ρ else 0) =
        ∑' ρ, if gaborFundDomain ρ then (4 : ℂ) * (f ρ).re else 0 := by
    have e1 := hD.tsum_add hDstar
    have e2 := (Summable.add hD hDstar).tsum_add hDFE
    have e3 :=
      (Summable.add (Summable.add hD hDstar) hDFE).tsum_add hDorb
    rw [← e1, ← e2, ← e3]
    exact tsum_congr hpt
  have hgroup :
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0) =
        (∑' ρ, if gaborFundDomain ρ then (4 : ℂ) * (f ρ).re else 0) +
          ∑' ρ, if gaborRealOff ρ then f ρ else 0 := by
    rw [hfive, ← horbit, ← hstar, ← hfe]
    simpa [Function.comp_apply, add_assoc, add_left_comm, add_comm] using
      congrArg (fun z => z + ∑' ρ, if gaborRealOff ρ then f ρ else 0) h4ts
  have hD4re : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      if gaborFundDomain ρ then (4 : ℂ) * (f ρ).re else 0 := by
    refine Summable.of_norm
      (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
        (fun ρ => ?_) (hsm.norm.mul_left 4))
    split_ifs
    · have hre : |(f ρ).re| ≤ ‖f ρ‖ := Complex.abs_re_le_norm (f ρ)
      have hle : 4 * |(f ρ).re| ≤ 4 * ‖f ρ‖ :=
        mul_le_mul_of_nonneg_left hre (by norm_num)
      refine le_trans ?_ hle
      simp [norm_mul]
    · simp
  have hD4f : Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      if gaborFundDomain ρ then (4 : ℂ) * f ρ else 0 := by
    refine (summable_congr fun ρ => ?_).mpr (hD.mul_right 4)
    split_ifs <;> ring
  have hre4 :
      (∑' ρ, if gaborFundDomain ρ then (4 : ℂ) * f ρ else 0).re =
        (∑' ρ, if gaborFundDomain ρ then (4 : ℂ) * (f ρ).re else 0).re := by
    rw [Complex.re_tsum hD4f, Complex.re_tsum hD4re]
    exact tsum_congr fun ρ => by
      split_ifs
      · simp [Complex.mul_re]
      · simp
  change
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          if (ρ : ℂ).re ≠ 1 / 2 then f ρ else 0).re =
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            if gaborFundDomain ρ then
              (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
                gaborHat F ρ
            else 0).re +
          gaborOffLineRealAxisMass F
  have hQ :
      (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
          if gaborFundDomain ρ then
            (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
              gaborHat F ρ
          else 0) =
        fun ρ => if gaborFundDomain ρ then (4 : ℂ) * f ρ else 0 := by
    funext ρ
    simp [f, mul_assoc]
  have hReal :
      gaborOffLineRealAxisMass F =
        (∑' ρ, if gaborRealOff ρ then f ρ else 0).re := by
    unfold gaborOffLineRealAxisMass
    refine congrArg Complex.re (tsum_congr fun ρ => ?_)
    simp [gaborRealOff, f]
  rw [hQ, hReal, hgroup, Complex.add_re, hre4]

/-! ## r587: weighted FD truncations -/

noncomputable def gaborWeightedRightRep (q : ℝ × ℝ) : ℂ :=
  (1 / 2 : ℂ) + (q.1 : ℂ) + (q.2 : ℂ) * Complex.I

noncomputable def gaborWeightedTruncationMult (q : ℝ × ℝ) : ℕ :=
  riemannZetaMultiplicity (gaborWeightedRightRep q)

noncomputable def gaborFundZerosUpTo (T : ℝ) : Finset ℂ :=
  (gaborOffLineZerosUpTo T).filter (fun z => (1 / 2 : ℝ) < z.re)

lemma mem_gaborFundZerosUpTo {T : ℝ} {z : ℂ} :
    z ∈ gaborFundZerosUpTo T ↔
      z ∈ gaborOffLineZerosUpTo T ∧ (1 / 2 : ℝ) < z.re :=
  mem_filter

noncomputable def gaborFundKey (z : ℂ) : ℝ × ℝ :=
  (z.re - 1 / 2, z.im)

lemma gaborFundKey_rightRep (z : ℂ) :
    gaborWeightedRightRep (gaborFundKey z) = z := by
  unfold gaborWeightedRightRep gaborFundKey
  apply Complex.ext
  · simp [Complex.add_re, Complex.mul_re, Complex.I_re, Complex.I_im,
      Complex.ofReal_re]
  · simp [Complex.add_im, Complex.mul_im, Complex.I_re, Complex.I_im,
      Complex.ofReal_im]

lemma gaborFundKey_injOn (T : ℝ) :
    Set.InjOn gaborFundKey (gaborFundZerosUpTo T) :=
  fun z _ w _ h => by
    have := congrArg gaborWeightedRightRep h
    simpa [gaborFundKey_rightRep] using this

lemma isCriticalStrip_of_mem_fundZeros {T : ℝ} {z : ℂ}
    (hz : z ∈ gaborFundZerosUpTo T) : IsCriticalStripZetaZero z :=
  isCriticalStrip_of_mem_rect
    (mem_gaborOffLineZerosUpTo.mp (mem_gaborFundZerosUpTo.mp hz).1).1

lemma gaborFundDomain_of_mem_fundZeros {T : ℝ} {z : ℂ}
    (hz : z ∈ gaborFundZerosUpTo T) :
    (1 / 2 : ℝ) < z.re ∧ 0 < z.im :=
  ⟨(mem_gaborFundZerosUpTo.mp hz).2,
    (mem_gaborOffLineZerosUpTo.mp (mem_gaborFundZerosUpTo.mp hz).1).2.2⟩

noncomputable def gaborWeightedTruncationPts (T : ℝ) : Finset (ℝ × ℝ) :=
  (gaborFundZerosUpTo T).image gaborFundKey

noncomputable def gaborWeightedTruncationConfig (T : ℝ) :
    GaborCanonicalConfig where
  pts := gaborWeightedTruncationPts T
  mult := gaborWeightedTruncationMult
  mult_pos := by
    intro q hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    have hzS := isCriticalStrip_of_mem_fundZeros hz
    have hmult :
        gaborWeightedTruncationMult (gaborFundKey z) =
          riemannZetaMultiplicity z := by
      unfold gaborWeightedTruncationMult
      rw [gaborFundKey_rightRep]
    rw [hmult]
    exact riemannZetaMultiplicity_pos hzS.1
      (isCriticalStripZetaZero_ne_one hzS)
  sigma_off := by
    intro q hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    have hD := (mem_gaborFundZerosUpTo.mp hz).2
    have hcrit := isCriticalStrip_of_mem_fundZeros hz
    constructor
    · exact sub_pos.mpr hD
    · change z.re - 1 / 2 < 1 / 2
      linarith [hcrit.2.2]
  gamma_pos := by
    intro q hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    exact (gaborFundDomain_of_mem_fundZeros hz).2

theorem gaborWeightedQuadrupoleSum_eq_fund_partial
    (a omega T : ℝ) (ha : 0 < a) :
    gaborQuadrupoleSum a omega (gaborWeightedTruncationConfig T) =
      (gaborFundZerosUpTo T).sum (fun z =>
        (riemannZetaMultiplicity z : ℝ) *
          (4 * (gaborHat (pureGaborTest a omega ha) z).re)) := by
  unfold gaborQuadrupoleSum gaborWeightedTruncationConfig
    gaborWeightedTruncationPts
  rw [Finset.sum_image (gaborFundKey_injOn T)]
  refine Finset.sum_congr rfl fun z _ => ?_
  have hmult : (gaborWeightedTruncationMult (gaborFundKey z) : ℝ) =
      (riemannZetaMultiplicity z : ℝ) := by
    unfold gaborWeightedTruncationMult
    rw [gaborFundKey_rightRep]
  have hQ := gaborQuadrupole_eq_four_re_hat a omega
    (gaborFundKey z).1 (gaborFundKey z).2 ha
  rw [hmult, hQ]
  have hrep := gaborFundKey_rightRep z
  simp [gaborWeightedRightRep, gaborFundKey] at hrep
  simp [gaborFundKey, hrep]

theorem gaborWeightedTruncation_incrementCompliantLog (T : ℝ) :
    GaborConfigIncrementCompliantLog (gaborWeightedTruncationConfig T) := by
  intro k
  set Z := gaborWeightedTruncationConfig T
  set Sk := Z.pts.filter
    (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)
  set Pre := (gaborFundZerosUpTo T).filter
    (fun z => (k : ℝ) < z.im ∧ z.im ≤ (k : ℝ) + 1)
  have himage : Sk = Pre.image gaborFundKey := by
    ext q
    constructor
    · intro hq
      have hqf := mem_filter.mp hq
      obtain ⟨z, hz, rfl⟩ := mem_image.mp hqf.1
      refine mem_image.mpr ⟨z, mem_filter.mpr ⟨hz, ?_⟩, rfl⟩
      simpa [gaborFundKey] using hqf.2
    · intro hq
      obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
      have hzf := mem_filter.mp hz
      refine mem_filter.mpr ⟨mem_image.mpr ⟨z, hzf.1, rfl⟩, ?_⟩
      simpa [gaborFundKey] using hzf.2
  have hsum :
      Sk.sum (fun q => (Z.mult q : ℝ)) =
        Pre.sum (fun z => (riemannZetaMultiplicity z : ℝ)) := by
    rw [himage, Finset.sum_image
      ((gaborFundKey_injOn T).mono (fun _ hz => (mem_filter.mp hz).1))]
    refine Finset.sum_congr rfl fun z hz => ?_
    change (gaborWeightedTruncationMult (gaborFundKey z) : ℝ) =
      (riemannZetaMultiplicity z : ℝ)
    unfold gaborWeightedTruncationMult
    rw [gaborFundKey_rightRep]
  have hsub : Pre ⊆ stripZerosWindow (k : ℝ) := by
    intro z hz
    have hzf := mem_filter.mp hz
    have hoff := (mem_gaborFundZerosUpTo.mp hzf.1).1
    exact gaborOffLine_subset_strip hoff hzf.2
  have hwin := sum_multiplicity_stripZerosWindow_le (k : ℝ)
  have hK : (stripZerosWindow (k : ℝ)).sum
      (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        gaborKBinAt (|k| : ℝ) := by
    simpa [gaborKBinAt] using hwin
  have hle :
      Pre.sum (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
        (stripZerosWindow (k : ℝ)).sum
          (fun z => (riemannZetaMultiplicity z : ℝ)) :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub
      (fun _ _ _ => (Nat.cast_nonneg _ : (0 : ℝ) ≤ _))
  exact hsum.trans_le (hle.trans hK)

/-! ## r588: HasSum exhaustion of the FD windows -/

lemma stripZerosBelow_succ_mono :
    Monotone fun n : ℕ => stripZerosBelow ((n + 1 : ℕ) : ℝ) :=
  fun _ _ hij =>
    stripZerosBelow_mono (by exact_mod_cast Nat.succ_le_succ hij)

lemma exists_mem_stripZerosBelow_succ
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ∃ n : ℕ, ρ ∈ stripZerosBelow ((n + 1 : ℕ) : ℝ) := by
  obtain ⟨n, hn⟩ := exists_nat_ge |(ρ : ℂ).im|
  refine ⟨n, mem_stripZerosBelow.mpr
    (mem_rect_of_criticalStrip ρ.property (hn.trans ?_))⟩
  exact_mod_cast Nat.le_succ n

lemma tendsto_stripZerosBelow_succ :
    Tendsto (fun n : ℕ => stripZerosBelow ((n + 1 : ℕ) : ℝ))
      atTop atTop :=
  tendsto_finset_atTop_of_monotone _
    stripZerosBelow_succ_mono exists_mem_stripZerosBelow_succ

lemma mem_gaborFundZerosUpTo_iff_subtype {T : ℝ}
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}} :
    (ρ : ℂ) ∈ gaborFundZerosUpTo T ↔
      ρ ∈ (stripZerosBelow T).filter gaborFundDomain := by
  constructor
  · intro hz
    have hoff := (mem_gaborFundZerosUpTo.mp hz).1
    refine mem_filter.mpr ⟨mem_stripZerosBelow.mpr
      (mem_gaborOffLineZerosUpTo.mp hoff).1, ?_⟩
    exact gaborFundDomain_of_mem_fundZeros hz
  · intro hρ
    have hρf := mem_filter.mp hρ
    have hrect := mem_stripZerosBelow.mp hρf.1
    have hD := hρf.2
    refine mem_gaborFundZerosUpTo.mpr ⟨mem_gaborOffLineZerosUpTo.mpr
      ⟨hrect, ne_of_gt hD.1, hD.2⟩, hD.1⟩

lemma four_mul_mult_hat_re (F : GaborWeilTest)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ((4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
      gaborHat F ρ).re =
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
        (4 * (gaborHat F ρ).re) := by
  have h4 : ((4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ)).re =
      (4 : ℝ) * (riemannZetaMultiplicity (ρ : ℂ) : ℝ) := by
    simp [Complex.mul_re]
  have h4i : ((4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ)).im = 0 := by
    simp [Complex.mul_im]
  simp [Complex.mul_re, h4, h4i]
  ring

lemma gaborFundZerosUpTo_sum_eq_strip_re (F : GaborWeilTest) (T : ℝ) :
    (gaborFundZerosUpTo T).sum (fun z =>
      (riemannZetaMultiplicity z : ℝ) *
        (4 * (gaborHat F z).re)) =
      (∑ ρ ∈ stripZerosBelow T,
        if gaborFundDomain ρ then
          (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat F ρ
        else 0).re := by
  classical
  set S := (stripZerosBelow T).filter gaborFundDomain
  have hfilter :
      ∑ ρ ∈ S,
          (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat F ρ =
        ∑ ρ ∈ stripZerosBelow T,
          if gaborFundDomain ρ then
            (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
              gaborHat F ρ
          else 0 := by
    simpa [S] using
      (Finset.sum_filter (s := stripZerosBelow T) (p := gaborFundDomain)
        (f := fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
          (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
            gaborHat F ρ))
  rw [← hfilter, Complex.re_sum]
  refine Finset.sum_bij
    (fun z hz => ⟨z, isCriticalStrip_of_mem_fundZeros hz⟩)
    ?mem ?inj ?surj ?eq
  · intro z hz
    exact (mem_gaborFundZerosUpTo_iff_subtype (ρ :=
      ⟨z, isCriticalStrip_of_mem_fundZeros hz⟩)).mp hz
  · intro z w _ _ h
    simpa using congrArg Subtype.val h
  · intro ρ hρ
    refine ⟨(ρ : ℂ),
      (mem_gaborFundZerosUpTo_iff_subtype (ρ := ρ)).mpr hρ, ?_⟩
    exact Subtype.ext rfl
  · intro z hz
    exact (four_mul_mult_hat_re F
      ⟨z, isCriticalStrip_of_mem_fundZeros hz⟩).symm

/-- r588: FD-window Q-sums exhaust the weight-4 FD tsum. -/
def GaborWeightedQuadrupoleLimitEqFDTsum : Prop :=
  ∀ (a omega : ℝ) (ha : 0 < a),
    Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop
      (𝓝 ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          if gaborFundDomain ρ then
            (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
              gaborHat (pureGaborTest a omega ha) ρ
          else 0).re))

theorem gaborWeightedQuadrupoleLimitEqFDTsum_holds :
    GaborWeightedQuadrupoleLimitEqFDTsum := by
  intro a omega ha
  set F := pureGaborTest a omega ha
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun ρ =>
      if gaborFundDomain ρ then
        (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
          gaborHat F ρ
      else 0
  have hbase := gaborMultiplicityWeightedHatSummableQuartic_holds F
  have hind := summable_indicator_of hbase gaborFundDomain
  have hsm : Summable f := by
    refine (summable_congr fun ρ => ?_).mpr (hind.mul_left 4)
    unfold f
    split_ifs <;> ring
  have hcomp :
      Tendsto (fun n : ℕ =>
          ∑ ρ ∈ stripZerosBelow ((n + 1 : ℕ) : ℝ), f ρ)
        atTop (𝓝 (∑' ρ, f ρ)) :=
    hsm.hasSum.comp tendsto_stripZerosBelow_succ
  have hQ : ∀ n : ℕ,
      gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)) =
        (∑ ρ ∈ stripZerosBelow ((n + 1 : ℕ) : ℝ), f ρ).re := by
    intro n
    rw [gaborWeightedQuadrupoleSum_eq_fund_partial a omega _ ha]
    simpa [f, F] using
      gaborFundZerosUpTo_sum_eq_strip_re F ((n + 1 : ℕ) : ℝ)
  refine ((Complex.continuous_re.tendsto _).comp hcomp).congr ?_
  exact fun n => (hQ n).symm

/-- Honest weighted Bridge-6 identification.  r588: theorem
`gaborWeightedQuadrupoleLimitEqOffLineMass_holds` via FD-HasSum
exhaustion plus `gaborOffLineRealAxisMass_eq_zero`. -/
def GaborWeightedQuadrupoleLimitEqOffLineMass : Prop :=
  ∀ (a omega : ℝ) (ha : 0 < a),
    ∃ cfg : ℕ → GaborCanonicalConfig,
      (∀ n q, q ∈ (cfg n).pts →
        (cfg n).mult q =
          riemannZetaMultiplicity
            ((1 / 2 : ℂ) + (q.1 : ℂ) + (q.2 : ℂ) * Complex.I)) ∧
      Tendsto (fun n : ℕ =>
          gaborQuadrupoleSum a omega (cfg (n + 1)))
        atTop
        (𝓝 (gaborOffLineSpectralMass (pureGaborTest a omega ha)))

/-- The named Bridge-6 identification, granted the real-axis
remainder vanishes.  r588 discharges both hypotheses. -/
theorem gaborWeightedQuadrupoleLimitEqOffLineMass_of_realAxisZero
    (hFD : GaborWeightedQuadrupoleLimitEqFDTsum)
    (hreal : ∀ (a omega : ℝ) (ha : 0 < a),
      gaborOffLineRealAxisMass (pureGaborTest a omega ha) = 0) :
    GaborWeightedQuadrupoleLimitEqOffLineMass := by
  intro a omega ha
  refine ⟨fun n => gaborWeightedTruncationConfig (n : ℝ), ?mult, ?lim⟩
  · intro n q hq
    rfl
  · have hFDlim := hFD a omega ha
    have hmass :=
      gaborOffLineMassEqWeightedQuadrupoleTsum_holds a omega ha
    have h0 := hreal a omega ha
    have hrew :
        gaborOffLineSpectralMass (pureGaborTest a omega ha) =
          (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              if gaborFundDomain ρ then
                (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
                  gaborHat (pureGaborTest a omega ha) ρ
              else 0).re := by
      rw [hmass, h0, add_zero]
    simpa [hrew] using hFDlim

/-! ## r588: no real zeros of ζ in (0,1), via the r509 identity -/

lemma zetaFractCellIntegrand_eq_ofReal (n : ℕ) (σ : ℝ) {x : ℝ}
    (hx : x ∈ Set.Icc (n + 1 : ℝ) (n + 2)) :
    zetaFractCellIntegrand n (σ : ℂ) x =
      (((x - (n + 1 : ℝ)) * Real.rpow x (-σ - 1) : ℝ) : ℂ) := by
  have hxpos : 0 < x :=
    (show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le hx.1
  have hexp : -(σ : ℂ) - 1 = ((-σ - 1 : ℝ) : ℂ) := by
    simp
  have hpow : (x : ℂ) ^ (-(σ : ℂ) - 1) =
      (Real.rpow x (-σ - 1) : ℝ) := by
    rw [hexp]
    exact (Complex.ofReal_cpow hxpos.le (-σ - 1)).symm
  unfold zetaFractCellIntegrand
  rw [hpow]
  simp

lemma zetaFractCell_eq_ofReal (n : ℕ) (σ : ℝ) :
    zetaFractCell n (σ : ℂ) =
      (↑(∫ x in (n + 1 : ℝ)..(n + 2),
        (x - (n + 1 : ℝ)) * Real.rpow x (-σ - 1)) : ℂ) := by
  unfold zetaFractCell
  have hle : (n + 1 : ℝ) ≤ n + 2 := by linarith
  have hcongr :
      ∫ x in (n + 1 : ℝ)..(n + 2), zetaFractCellIntegrand n (σ : ℂ) x =
        ∫ x in (n + 1 : ℝ)..(n + 2),
          (((x - (n + 1 : ℝ)) * Real.rpow x (-σ - 1) : ℝ) : ℂ) := by
    refine intervalIntegral.integral_congr fun x hx => ?_
    have hxI : x ∈ Set.Icc (n + 1 : ℝ) (n + 2) := by
      simpa [uIcc_of_le hle] using hx
    exact zetaFractCellIntegrand_eq_ofReal n σ hxI
  rw [hcongr, intervalIntegral.integral_ofReal]

lemma re_zetaFractCell_nonneg (n : ℕ) (σ : ℝ) :
    0 ≤ (zetaFractCell n (σ : ℂ)).re := by
  rw [zetaFractCell_eq_ofReal]
  simp only [Complex.ofReal_re]
  refine intervalIntegral.integral_nonneg (by linarith) ?_
  intro x hx
  have hxpos : 0 < x :=
    (show (0 : ℝ) < n + 1 by exact_mod_cast Nat.succ_pos n).trans_le hx.1
  exact mul_nonneg (sub_nonneg.mpr hx.1) (Real.rpow_nonneg hxpos.le _)

lemma re_zetaFractIntegral_nonneg {σ : ℝ} (hσ : 0 < σ) :
    0 ≤ (zetaFractIntegral (σ : ℂ)).re := by
  have hsm := summable_zetaFractCell (by simp [hσ] : 0 < (σ : ℂ).re)
  unfold zetaFractIntegral
  rw [Complex.re_tsum hsm]
  exact tsum_nonneg fun n => re_zetaFractCell_nonneg n σ

/-- ζ(σ) ≠ 0 for real σ ∈ (0,1).  Path: r509 identity
`ζ(s) = s/(s-1) − s·zetaFractIntegral(s)` on `{Re s>0, s≠1}`;
the cell series has nonnegative real part on the positive real
axis, so the right-hand side has negative real part. -/
lemma riemannZeta_ne_zero_of_mem_Ioo {σ : ℝ} (hσ0 : 0 < σ) (hσ1 : σ < 1) :
    riemannZeta (σ : ℂ) ≠ 0 := by
  have hs : 0 < (σ : ℂ).re := by simp [hσ0]
  have hne1 : (σ : ℂ) ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    simp at this
    linarith
  have hid :=
    riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos hs hne1
  intro hz
  have heq :
      (σ : ℂ) / ((σ : ℂ) - 1) =
        (σ : ℂ) * zetaFractIntegral (σ : ℂ) := by
    rw [hz] at hid
    exact eq_of_sub_eq_zero hid.symm
  have hL : ((σ : ℂ) / ((σ : ℂ) - 1)).re = σ / (σ - 1) := by
    have hsub : (σ : ℂ) - 1 = ((σ - 1 : ℝ) : ℂ) := by simp
    have hdiv : (σ : ℂ) / ((σ - 1 : ℝ) : ℂ) =
        ((σ / (σ - 1) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_div]
    rw [hsub, hdiv, Complex.ofReal_re]
  have hR : ((σ : ℂ) * zetaFractIntegral (σ : ℂ)).re =
      σ * (zetaFractIntegral (σ : ℂ)).re := by
    simp [Complex.mul_re]
  have hLt : σ / (σ - 1) < 0 :=
    div_neg_of_pos_of_neg hσ0 (sub_neg.mpr hσ1)
  have hGe : 0 ≤ σ * (zetaFractIntegral (σ : ℂ)).re :=
    mul_nonneg hσ0.le (re_zetaFractIntegral_nonneg hσ0)
  have : σ / (σ - 1) = σ * (zetaFractIntegral (σ : ℂ)).re := by
    rw [← hL, heq, hR]
  linarith

lemma not_isCriticalStripZetaZero_of_im_zero {z : ℂ}
    (him : z.im = 0) : ¬ IsCriticalStripZetaZero z := by
  intro hz
  have hzreal : z = (z.re : ℂ) := by
    apply Complex.ext
    · rw [Complex.ofReal_re]
    · rw [Complex.ofReal_im, him]
  have hz0 : riemannZeta (z.re : ℂ) = 0 :=
    hzreal ▸ hz.1
  exact riemannZeta_ne_zero_of_mem_Ioo hz.2.1 hz.2.2 hz0

theorem gaborOffLineRealAxisMass_eq_zero (F : GaborWeilTest) :
    gaborOffLineRealAxisMass F = 0 := by
  unfold gaborOffLineRealAxisMass
  have h0 :
      (fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
        if (ρ : ℂ).re ≠ 1 / 2 ∧ (ρ : ℂ).im = 0 then
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
        else 0) = fun _ => 0 := by
    funext ρ
    split_ifs with h
    · exact (not_isCriticalStripZetaZero_of_im_zero h.2 ρ.property).elim
    · rfl
  rw [h0, tsum_zero, Complex.zero_re]

theorem gaborWeightedQuadrupoleLimitEqOffLineMass_holds :
    GaborWeightedQuadrupoleLimitEqOffLineMass :=
  gaborWeightedQuadrupoleLimitEqOffLineMass_of_realAxisZero
    gaborWeightedQuadrupoleLimitEqFDTsum_holds
    (fun _ _ _ => gaborOffLineRealAxisMass_eq_zero _)

lemma gaborCanonicalKey_eq_fundKey {z : ℂ}
    (h : (1 / 2 : ℝ) < z.re) :
    gaborCanonicalKey z = gaborFundKey z := by
  unfold gaborCanonicalKey gaborFundKey
  rw [abs_of_pos (sub_pos.mpr h)]

lemma gaborOffLine_partner_mem_fund {T : ℝ} {z : ℂ}
    (hz : z ∈ gaborOffLineZerosUpTo T) (hleft : z.re < (1 / 2 : ℝ)) :
    1 - star z ∈ gaborFundZerosUpTo T := by
  have hz' := mem_gaborOffLineZerosUpTo.mp hz
  have hcrit : IsCriticalStripZetaZero z :=
    isCriticalStrip_of_mem_rect hz'.1
  have h1 : IsCriticalStripZetaZero (1 - star z) :=
    isCriticalStrip_one_sub (isCriticalStrip_star hcrit)
  have him : |(1 - star z).im| ≤ T := by
    have hmem := mem_riemannZetaZerosOnClosedRect.mp hz'.1
    have hrect := mem_zetaClosedRect.mp hmem.1
    have himz : (1 - star z).im = z.im := by
      simp [Complex.sub_im, Complex.star_def, Complex.conj_im]
    rw [himz, abs_of_pos hz'.2.2]
    exact hrect.2.2.2
  have hrect' := mem_rect_of_criticalStrip h1 him
  have hRew : (1 - star z).re = 1 - z.re := by
    simp [Complex.sub_re, Complex.star_def, Complex.conj_re]
  have hImw : (1 - star z).im = z.im := by
    simp [Complex.sub_im, Complex.star_def, Complex.conj_im]
  refine mem_gaborFundZerosUpTo.mpr ⟨mem_gaborOffLineZerosUpTo.mpr
    ⟨hrect', ?_, ?_⟩, ?_⟩
  · rw [hRew]
    linarith
  · rw [hImw]
    exact hz'.2.2
  · rw [hRew]
    linarith

lemma gaborCanonicalKey_left_eq_fundKey_partner {z : ℂ}
    (hleft : z.re < (1 / 2 : ℝ)) :
    gaborCanonicalKey z = gaborFundKey (1 - star z) := by
  unfold gaborCanonicalKey gaborFundKey
  have hre : (1 - star z).re = 1 - z.re := by
    simp [Complex.sub_re, Complex.star_def, Complex.conj_re]
  have him : (1 - star z).im = z.im := by
    simp [Complex.sub_im, Complex.star_def, Complex.conj_im]
  rw [hre, him]
  have hpos : 0 < 1 / 2 - z.re := by linarith
  rw [abs_of_neg (sub_neg.mpr hleft)]
  ring

lemma gaborTruncationPts_eq_weighted (T : ℝ) :
    gaborTruncationPts T = gaborWeightedTruncationPts T := by
  ext q
  constructor
  · intro hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    have hz' := mem_gaborOffLineZerosUpTo.mp hz
    by_cases hR : (1 / 2 : ℝ) < z.re
    · refine mem_image.mpr ⟨z, mem_gaborFundZerosUpTo.mpr ⟨hz, hR⟩, ?_⟩
      exact (gaborCanonicalKey_eq_fundKey hR).symm
    · have hleft : z.re < (1 / 2 : ℝ) :=
        lt_of_le_of_ne (le_of_not_gt hR) hz'.2.1
      refine mem_image.mpr
        ⟨1 - star z, gaborOffLine_partner_mem_fund hz hleft, ?_⟩
      exact (gaborCanonicalKey_left_eq_fundKey_partner hleft).symm
  · intro hq
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    have hD := (mem_gaborFundZerosUpTo.mp hz).2
    refine mem_image.mpr ⟨z, (mem_gaborFundZerosUpTo.mp hz).1, ?_⟩
    exact gaborCanonicalKey_eq_fundKey hD

lemma gaborQuadrupoleSum_truncation_eq_weighted_of_simple
    (a omega T : ℝ) (ha : 0 < a)
    (hsimple : ∀ z, z ∈ gaborFundZerosUpTo T →
      riemannZetaMultiplicity z = 1) :
    gaborQuadrupoleSum a omega (gaborTruncationConfig T) =
      gaborQuadrupoleSum a omega (gaborWeightedTruncationConfig T) := by
  have hpts := gaborTruncationPts_eq_weighted T
  unfold gaborQuadrupoleSum gaborTruncationConfig
    gaborWeightedTruncationConfig
  simp only [hpts]
  refine Finset.sum_congr rfl fun q hq => ?_
  have h1 : (gaborTruncationMult T q : ℝ) = 1 := by
    have : q ∈ gaborTruncationPts T := by
      simpa [hpts] using hq
    rw [gaborTruncationMult_eq_one this]
    simp
  have h2 : (gaborWeightedTruncationMult q : ℝ) = 1 := by
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hq
    unfold gaborWeightedTruncationMult
    rw [gaborFundKey_rightRep, hsimple z hz]
    simp
  rw [h1, h2]

/-- Unweighted Q-limit equals the off-line mass if every strip
zero is simple.  The unconditional Prop stays named: live
`gaborTruncationConfig` has `mult ≡ 1`. -/
theorem gaborQuadrupoleLimitEqOffLineMass_of_simple
    (hsimple : ∀ z, IsCriticalStripZetaZero z →
      riemannZetaMultiplicity z = 1) :
    GaborQuadrupoleLimitEqOffLineMass := by
  intro a omega ha
  have hW := gaborWeightedQuadrupoleLimitEqFDTsum_holds a omega ha
  have hmass :=
    gaborOffLineMassEqWeightedQuadrupoleTsum_holds a omega ha
  have h0 := gaborOffLineRealAxisMass_eq_zero (pureGaborTest a omega ha)
  have heq : ∀ n : ℕ,
      gaborQuadrupoleSum a omega
          (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)) =
        gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)) :=
    fun n => gaborQuadrupoleSum_truncation_eq_weighted_of_simple
      a omega _ ha fun z hz =>
        hsimple z (isCriticalStrip_of_mem_fundZeros hz)
  have hrew :
      gaborOffLineSpectralMass (pureGaborTest a omega ha) =
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            if gaborFundDomain ρ then
              (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
                gaborHat (pureGaborTest a omega ha) ρ
            else 0).re := by
    rw [hmass, h0, add_zero]
  exact (tendsto_congr heq).mpr (by simpa [hrew] using hW)

/-- r588: the weighted identification is a theorem. -/
def GaborWeightedTruncationExhaustsOffLine : Prop :=
  GaborWeightedQuadrupoleLimitEqOffLineMass

theorem gaborWeightedTruncationExhaustsOffLine_holds :
    GaborWeightedTruncationExhaustsOffLine :=
  gaborWeightedQuadrupoleLimitEqOffLineMass_holds

/-- r584: exhaustion chain for a pure packet, using the proved
on/off split.  Does not assert the unrestricted Prop. -/
theorem gaborZeroSide_le_of_truncation_of_pure
    {a omega δ : ℝ} (ha : 0 < a) (hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)) gaborCInc ≤ -δ)
    (hlim : GaborQuadrupoleLimitEqOffLineMass)
    (hon : gaborCriticalLineMass (pureGaborTest a omega ha) ≤
      gaborHonestOnlineBudget a omega gaborCInc) :
    gaborZeroSide (pureGaborTest a omega ha) ≤ -δ := by
  have hL := hlim a omega ha
  have halg := gabor_truncation_quadrupole_limit_le hδ hW hL
  have hsplit :=
    gaborZeroSide_eq_off_plus_on_pure (F := pureGaborTest a omega ha) rfl
  have hon' :
      gaborOffLineSpectralMass (pureGaborTest a omega ha) +
        gaborCriticalLineMass (pureGaborTest a omega ha) ≤
          gaborOffLineSpectralMass (pureGaborTest a omega ha) +
            gaborHonestOnlineBudget a omega gaborCInc :=
    add_le_add_right hon
      (gaborOffLineSpectralMass (pureGaborTest a omega ha))
  exact (hsplit.trans_le hon').trans halg

/-- Sorry-free chain: uniform truncation negativity + the named
identifications + on-line mass `≤ R_on` ⇒ spectral zero-side
`≤ -δ`. -/
theorem gaborZeroSide_le_of_truncation_bridges
    {a omega δ : ℝ} (ha : 0 < a) (hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)) gaborCInc ≤ -δ)
    (hlim : GaborQuadrupoleLimitEqOffLineMass)
    (hsplit : GaborZeroSideEqOffPlusOn)
    (hon : gaborCriticalLineMass (pureGaborTest a omega ha) ≤
      gaborHonestOnlineBudget a omega gaborCInc) :
    gaborZeroSide (pureGaborTest a omega ha) ≤ -δ := by
  have hL := hlim a omega ha
  have halg := gabor_truncation_quadrupole_limit_le hδ hW hL
  have hon' :
      gaborOffLineSpectralMass (pureGaborTest a omega ha) +
        gaborCriticalLineMass (pureGaborTest a omega ha) ≤
          gaborOffLineSpectralMass (pureGaborTest a omega ha) +
            gaborHonestOnlineBudget a omega gaborCInc :=
    add_le_add_right hon
      (gaborOffLineSpectralMass (pureGaborTest a omega ha))
  exact ((hsplit _).trans_le hon').trans halg

theorem gabor_weighted_truncation_quadrupole_limit_le
    {a omega Cinc δ : ℝ} {L : ℝ} (hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)) Cinc ≤ -δ)
    (hlim : Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop (𝓝 L)) :
    L + gaborHonestOnlineBudget a omega Cinc ≤ -δ := by
  refine gabor_exhaustion_algebra (a := a) (omega := omega)
    (Cinc := Cinc) (δ := δ) (L := L) hδ ?_ hlim
  intro n
  simpa [gaborHonestWeil_eq_quadrupoleSum] using hW n

/-- Live weighted chain: uniform negativity of the multiplicity-
weighted FD windows plus the r588 identification plus on-line
mass `≤ R_on` ⇒ spectral zero-side `≤ -δ`.  The unweighted chain
above stays, but needs simple zeros. -/
theorem gaborZeroSide_le_of_weighted_truncation_of_pure
    {a omega δ : ℝ} (ha : 0 < a) (hδ : 0 < δ)
    (hW : ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)) gaborCInc ≤ -δ)
    (hon : gaborCriticalLineMass (pureGaborTest a omega ha) ≤
      gaborHonestOnlineBudget a omega gaborCInc) :
    gaborZeroSide (pureGaborTest a omega ha) ≤ -δ := by
  have hFDlim := gaborWeightedQuadrupoleLimitEqFDTsum_holds a omega ha
  have hmass :=
    gaborOffLineMassEqWeightedQuadrupoleTsum_holds a omega ha
  have h0 := gaborOffLineRealAxisMass_eq_zero (pureGaborTest a omega ha)
  have hrew :
      gaborOffLineSpectralMass (pureGaborTest a omega ha) =
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            if gaborFundDomain ρ then
              (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
                gaborHat (pureGaborTest a omega ha) ρ
            else 0).re := by
    rw [hmass, h0, add_zero]
  have hL : Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop
      (𝓝 (gaborOffLineSpectralMass (pureGaborTest a omega ha))) := by
    simpa [hrew] using hFDlim
  have halg := gabor_weighted_truncation_quadrupole_limit_le hδ hW hL
  have hsplit :=
    gaborZeroSide_eq_off_plus_on_pure (F := pureGaborTest a omega ha) rfl
  have hon' :
      gaborOffLineSpectralMass (pureGaborTest a omega ha) +
        gaborCriticalLineMass (pureGaborTest a omega ha) ≤
          gaborOffLineSpectralMass (pureGaborTest a omega ha) +
            gaborHonestOnlineBudget a omega gaborCInc :=
    add_le_add_right hon
      (gaborOffLineSpectralMass (pureGaborTest a omega ha))
  exact (hsplit.trans_le hon').trans halg

/-- Packet-fixed uniform margin used by the exhaustion theorem.
A single `(a,ω,δ)` that scores every unweighted window `≤ -δ`.
Folgt NICHT aus BoundLog2: its isolation packet is retuned to
each catalog's host, so `(a,ω)` (and `E`) move with the window.
Unasserted.  Not a `sorry`. -/
def GaborTruncationUniformNeg (a omega δ : ℝ) : Prop :=
  0 < δ ∧
    ∀ n : ℕ,
      gaborHonestWeil a omega
        (gaborTruncationConfig ((n + 1 : ℕ) : ℝ)) gaborCInc ≤ -δ

/-! ## r589: FD window → BoundLog2 hypotheses -/

theorem gaborWeightedTruncation_pts_nonempty_iff (T : ℝ) :
    (gaborWeightedTruncationConfig T).pts.Nonempty ↔
      (gaborFundZerosUpTo T).Nonempty := by
  constructor
  · intro h
    obtain ⟨q, hq⟩ := h
    obtain ⟨z, hz, _⟩ := Finset.mem_image.mp
      (show q ∈ gaborWeightedTruncationPts T from hq)
    exact ⟨z, hz⟩
  · intro h
    obtain ⟨z, hz⟩ := h
    exact ⟨gaborFundKey z, Finset.mem_image.mpr ⟨z, hz, rfl⟩⟩

/-- Empty FD window: the quadrupole sum vanishes (hence `≤ 0`).
The honest score is then exactly `R_on` / `R_on_log` and is not
claimed negative. -/
theorem gaborWeightedTruncation_empty_quadrupole
    (a omega T : ℝ)
    (hempty : ¬ (gaborWeightedTruncationConfig T).pts.Nonempty) :
    gaborQuadrupoleSum a omega (gaborWeightedTruncationConfig T) = 0 := by
  have hpts :
      (gaborWeightedTruncationConfig T).pts = ∅ :=
    Finset.not_nonempty_iff_eq_empty.mp hempty
  unfold gaborQuadrupoleSum
  rw [hpts, Finset.sum_empty]

theorem gaborWeightedTruncation_empty_quadrupole_nonpos
    (a omega T : ℝ)
    (hempty : ¬ (gaborWeightedTruncationConfig T).pts.Nonempty) :
    gaborQuadrupoleSum a omega (gaborWeightedTruncationConfig T) ≤ 0 :=
  (gaborWeightedTruncation_empty_quadrupole a omega T hempty).le

/-- A one-point FD window has pairwise distinct ordinates. -/
theorem gaborWeightedTruncation_singleton_gammaDistinct
    (T : ℝ)
    (hcard : (gaborWeightedTruncationConfig T).pts.card = 1) :
    (gaborWeightedTruncationConfig T).gammaDistinct := by
  obtain ⟨q0, hq0⟩ := Finset.card_eq_one.mp hcard
  intro q1 hq1 q2 hq2 _heq
  have h1 : q1 = q0 :=
    Finset.mem_singleton.mp (hq0 ▸ hq1)
  have h2 : q2 = q0 :=
    Finset.mem_singleton.mp (hq0 ▸ hq2)
  rw [h1, h2]

theorem gaborWeightedTruncation_singleton_hostIsolated
    (T : ℝ) (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty)
    (hcard : (gaborWeightedTruncationConfig T).pts.card = 1) :
    (gaborWeightedTruncationConfig T).gammaHostIsolated hZ :=
  gammaDistinct_hostIsolated _ hZ
    (gaborWeightedTruncation_singleton_gammaDistinct T hcard)

/-- BoundLog2 inputs that the FD window supplies unconditionally:
log increment-compliance (r588), `γ>0` / `0<σ<1/2` (structure),
and a well-defined isolation host on every nonempty window.
The remaining hypothesis is `gammaDistinct`. -/
theorem gaborWeightedTruncation_boundLog2_hyps (T : ℝ)
    (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty) :
    GaborConfigIncrementCompliantLog (gaborWeightedTruncationConfig T) ∧
      (gaborHostSigma (gaborWeightedTruncationConfig T) hZ,
          gaborHostGamma (gaborWeightedTruncationConfig T) hZ) ∈
        (gaborWeightedTruncationConfig T).pts ∧
      0 < gaborHostSigma (gaborWeightedTruncationConfig T) hZ ∧
      gaborHostSigma (gaborWeightedTruncationConfig T) hZ < 1 / 2 ∧
      0 < gaborHostGamma (gaborWeightedTruncationConfig T) hZ ∧
      0 < gaborHostMult (gaborWeightedTruncationConfig T) hZ :=
  ⟨gaborWeightedTruncation_incrementCompliantLog T,
    gaborHost_mem _ hZ,
    gaborHostSigma_pos _ hZ,
    gaborHostSigma_lt_half _ hZ,
    gaborHostGamma_pos _ hZ,
    gaborHostMult_pos _ hZ⟩

/-- Pairwise distinct ordinates on every FD window.  Two
fund-domain zeros may share an imaginary part and differ in `σ`;
the image `gaborFundKey` is injective on points, not on the
`γ`-coordinate.  Isolation only needs `gammaHostIsolated`;
packing already sums every point.  Unasserted.  Not a `sorry`. -/
def GaborWeightedTruncationGammaDistinct : Prop :=
  ∀ T : ℝ, (gaborWeightedTruncationConfig T).gammaDistinct

/-- Honest weighted analog of `GaborTruncationUniformNeg`.

Quantifier (exact):
  `∀ T, nonempty window → gammaDistinct →
      W_log(isolationShrink(window), window) < 0`.

The isolation pair `(a,ω)` and the enhancement
`E = (π/a) exp(σ★²/(2a))` depend on the window through its
lexicographic host.  The fraction `η − 9/10 > 0` is n-free
(`a ≤ a_lock` ⇒ `η ≥ exp(−π²/1024)`).  There is no packet-fixed
`δ > 0` independent of `T`: BoundLog2 retunes `(a,ω)` per catalog,
so `GaborTruncationUniformNeg` is not implied.

Discharged by `gaborWeightedTruncationNegLog_holds` once
`GaborDominanceBoundLog2` is in scope (Log2). -/
def GaborWeightedTruncationNegLog : Prop :=
  ∀ T : ℝ,
    ∀ hZ : (gaborWeightedTruncationConfig T).pts.Nonempty,
      (gaborWeightedTruncationConfig T).gammaDistinct →
      gaborHonestWeilLog
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
        (gaborWeightedTruncationConfig T) gaborCInc < 0

/-- Quantitative form: `W_log < (9/10 − η(σ,a)) · E(σ,a) < 0`.
The factor `9/10 − η` is n-free and negative under the lock;
`E` is configuration-dependent.  Stronger lock-margin
`W_log < (9/10 − exp(−π²/1024)) · E` is proved in Log2. -/
def GaborWeightedTruncationNegLogQuant : Prop :=
  ∀ T : ℝ,
    ∀ hZ : (gaborWeightedTruncationConfig T).pts.Nonempty,
      (gaborWeightedTruncationConfig T).gammaDistinct →
      gaborHonestWeilLog
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
        (gaborWeightedTruncationConfig T) gaborCInc <
      ((9 / 10 : ℝ) -
          gaborEtaTune
            (gaborHostSigma (gaborWeightedTruncationConfig T) hZ)
            (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1) *
        gaborEnhancement
          (gaborHostSigma (gaborWeightedTruncationConfig T) hZ)
          (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1

/-! ## r582 BoundLog2 assembly (log-compatible R_on) -/

def GaborHonestWeilLeMajorantLog2 : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliantLog Z →
    Z.gammaDistinct →
    gaborHonestWeilLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc ≤
      gaborEnhancement (gaborHostSigma Z hZ)
            (isolationShrinkOfConfig Z hZ).1 *
          (-gaborEtaTune (gaborHostSigma Z hZ)
              (isolationShrinkOfConfig Z hZ).1 *
            (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog (isolationShrinkOfConfig Z hZ).1
              (isolationShrinkOfConfig Z hZ).2 +
            gaborTFarLog (isolationShrinkOfConfig Z hZ).1
              (isolationShrinkOfConfig Z hZ).2) +
        gaborHonestOnlineBudgetLog (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc

/-- Named remainder: `T₊_log + T_far_log + R_on_log/E < 9/10`.
Both pieces of the `max` are absorbed by `gaborOnlineSmallnessALog`
(`online_exp_le_log`): the proxy `(1+log)·R_on/E` and the closed
ĥ-side form `gaborOnlineLogBudget/E`.  Packing
(`GaborHonestWeilLeMajorantLog2`) is a theorem. -/
def GaborRemainderBudgetLog2 : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    gaborTPlusLooseLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 +
      gaborTFarLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 +
      gaborHonestOnlineBudgetLog (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc /
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 < (9 / 10 : ℝ)

theorem gaborHonestWeilLeMajorantLog2_holds :
    GaborHonestWeilLeMajorantLog2 := by
  intro Z hZ hinc hdist
  have hW := gaborHonestWeilLeMajorantLog_holds Z hZ hinc hdist
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  have hQ :
      Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) ≤
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) := by
    have hident :
        gaborHonestWeil a omega Z gaborCInc =
          Z.pts.sum (fun q =>
              (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
            gaborHonestOnlineBudget a omega gaborCInc :=
      rfl
    linarith [hW, hident]
  have hWlog :
      gaborHonestWeilLog a omega Z gaborCInc =
        Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
          gaborHonestOnlineBudgetLog a omega gaborCInc :=
    rfl
  have hQadd :
      Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
        gaborHonestOnlineBudgetLog a omega gaborCInc ≤
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc := by
    linarith [hQ]
  simpa [a, omega, σ] using hWlog.trans_le hQadd

theorem gabor_dominanceBoundLog2_of_pack_and_budget
    (hpack : GaborHonestWeilLeMajorantLog2)
    (hbud : GaborRemainderBudgetLog2) :
    GaborDominanceBoundLog2 := by
  intro Z hZ hinc hdist
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hm := gaborHostMult_pos Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hlock : a ≤ gaborALock σ :=
    (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_lock σ (gaborHostGamma Z hZ))
  have hη : (9 / 10 : ℝ) < gaborEtaTune σ a :=
    gaborEta_gt_nine_tenths hs ha hlock
  have hWle := hpack Z hZ hinc hdist
  have hR := hbud Z hZ
  have hm1 : (1 : ℝ) ≤ (gaborHostMult Z hZ : ℝ) := by
    exact_mod_cast Nat.succ_le_of_lt hm
  have hneg :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
        gaborTPlusLooseLog a omega + gaborTFarLog a omega +
        gaborHonestOnlineBudgetLog a omega gaborCInc /
          gaborEnhancement σ a < 0 := by
    have hηm : (9 / 10 : ℝ) <
        gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) :=
      lt_of_lt_of_le hη (le_mul_of_one_le_right (Real.exp_pos _).le hm1)
    linarith [hR, hηm]
  have hform :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega +
            gaborHonestOnlineBudgetLog a omega gaborCInc /
              gaborEnhancement σ a) := by
    field_simp [ne_of_gt hE]
  have hRHS :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc < 0 := by
    rw [hform]
    exact mul_neg_of_pos_of_neg hE hneg
  exact hWle.trans_lt hRHS

lemma online_exp_le_log {sigma gamma a : ℝ}
    (_hs : 0 < sigma) (hg : -2 ≤ gamma) (ha : 0 < a)
    (hsm : a ≤ gaborOnlineSmallnessALog sigma gamma) :
    Real.exp (-sigma ^ 2 / (2 * a)) ≤
      Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3)) := by
  have hC : 0 < gaborCInc := gaborCInc_pos
  have hlogC : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  have hlogγ : 0 ≤ Real.log (gamma + 3) :=
    Real.log_nonneg (by linarith)
  have hden : 0 <
      2 * (Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256) :=
    mul_pos (by norm_num)
      (add_pos_of_nonneg_of_pos (add_nonneg hlogC hlogγ) (by norm_num))
  have hfrac :
      Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256 ≤
        sigma ^ 2 / (2 * a) := by
    have : (Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256) * (2 * a) ≤
        sigma ^ 2 := by
      have := (le_div_iff₀ hden).mp hsm
      linarith
    exact (le_div_iff₀ (mul_pos (by norm_num) ha)).mpr this
  have hexp : Real.exp (-sigma ^ 2 / (2 * a)) ≤
      Real.exp
        (-(Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg hfrac
  have hident :
      Real.exp
          (-(Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256)) =
        Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3)) := by
    have h1 :
        -(Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256) =
          -Real.log (gaborCInc + 1) + -Real.log (gamma + 3) + -256 := by
      ring
    rw [h1, Real.exp_add, Real.exp_add, Real.exp_neg, Real.exp_neg,
      Real.exp_neg]
    rw [Real.exp_log (by linarith : (0 : ℝ) < gaborCInc + 1)]
    rw [Real.exp_log (by linarith : (0 : ℝ) < gamma + 3)]
    field_simp
  exact hexp.trans_eq hident

#print axioms gaborKBinAt_eq_binCountMajorant
#print axioms abs_sub_ge_bin_dist
#print axioms gaussBinMax_le_exp_hostDist
#print axioms hostDist_half
#print axioms summable_nat_linear_gauss_sq
#print axioms binCount_mul_binMax_le_far
#print axioms summable_int_linear_gauss_sq
#print axioms gaborLogWeightedThetaSummable
#print axioms gauss_density_transfer_binCount_of_summable
#print axioms gaborThreeLobe_eq_gauss
#print axioms threeLobe_finset_le_logMajorant_of_summable
#print axioms norm_gaborHat_online_finset_le_logMajorant_of_summable
#print axioms gaborLogMajorantLeHonestBudgetLog_holds
#print axioms gabor_criticalLineMass_le_honest_of
#print axioms gaborCanonicalKey_sigma_off
#print axioms gaborTruncation_incrementCompliantLog
#print axioms gaborTruncationWeightedCompliant_holds
#print axioms riemannZetaMultiplicity_le_log_all_local
#print axioms gaborMultiplicityWeightedHatSummable
#print axioms gabor_exhaustion_algebra
#print axioms gabor_truncation_quadrupole_limit_le
#print axioms gaborZeroSide_le_of_truncation_bridges
#print axioms gaborHonestWeilLeMajorantLog2_holds
#print axioms gabor_dominanceBoundLog2_of_pack_and_budget
#print axioms online_exp_le_log
#print axioms gaborLogThreeLobeMajorant_le_closed
#print axioms gaborBinCountMajorant_le_linear
#print axioms lin_gaussBinMax_summable
#print axioms lin_binMax_tsum_le
#print axioms gaborLogWeightedTheta_le_linClosed
#print axioms gaborCriticalLineMass_le_closed_of_tsum
#print axioms gaborCriticalLineMass_le_logMajorant_tsum
#print axioms gaborCriticalLineMassLeLogMajorant_holds
#print axioms gaborZeroSide_eq_off_plus_on_of_summable
#print axioms gaborZeroSide_eq_off_plus_on_pure
#print axioms gaborZeroSideEqOffPlusOn_of_quartic_summable
#print axioms isCriticalStrip_star
#print axioms riemannZetaMultiplicityEqConj_holds
#print axioms gaborHat_star_pure
#print axioms gaborHatStarPure_holds
#print axioms gaborHat_fe_quadrupole_eq_four_re
#print axioms gaborZeroSide_le_of_truncation_of_pure
#print axioms tsum_indicator_equiv
#print axioms gabor_orbit_sum_eq_four_re
#print axioms offLine_split_five
#print axioms gaborOffLineMassEqWeightedQuadrupoleTsum_holds
#print axioms gaborMultiplicityWeightedHatSummableQuartic_holds
#print axioms gaborZeroSideEqOffPlusOn_holds
#print axioms gaborFundKey_rightRep
#print axioms gaborWeightedQuadrupoleSum_eq_fund_partial
#print axioms gaborWeightedTruncation_incrementCompliantLog
#print axioms gaborWeightedQuadrupoleLimitEqOffLineMass_of_realAxisZero
#print axioms gaborWeightedQuadrupoleLimitEqFDTsum_holds
#print axioms riemannZeta_ne_zero_of_mem_Ioo
#print axioms gaborOffLineRealAxisMass_eq_zero
#print axioms gaborWeightedQuadrupoleLimitEqOffLineMass_holds
#print axioms gaborQuadrupoleLimitEqOffLineMass_of_simple
#print axioms gaborWeightedTruncationExhaustsOffLine_holds
#print axioms gabor_weighted_truncation_quadrupole_limit_le
#print axioms gaborZeroSide_le_of_weighted_truncation_of_pure
#print axioms gaborWeightedTruncation_pts_nonempty_iff
#print axioms gaborWeightedTruncation_empty_quadrupole
#print axioms gaborWeightedTruncation_empty_quadrupole_nonpos
#print axioms gaborWeightedTruncation_singleton_gammaDistinct
#print axioms gaborWeightedTruncation_singleton_hostIsolated
#print axioms gaborWeightedTruncation_boundLog2_hyps

end RH
