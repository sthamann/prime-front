/-
RH/GaborThetaBound.lean -- r552 Gauss-bin majorant and bin partial summation.

CLAIM BOUNDARY.  NO RH CLAIM.  Sorry-free elementary analysis only.
This file does not modify or discharge `GaborSeparationInequality`.

r549 sealed probe (`gabor_density_transfer_probe`, VERDICT TRANSFER_UNIFORM):
the unit-bin maxima of a Gaussian lobe admit a center-independent
Jacobi-theta majorant

    Σ_{k∈ℤ} max_{[k,k+1]} exp(-(t-c)²/(2a))
      ≤ Θ_lobe(a) := 3 + 2 Σ_{m≥1} exp(-m²/(2a)).

Combined with a uniform unit-bin count bound C, partial summation
gives a γ-independent Gaussian mass bound C · Θ_lobe(a).

The live Path A increment `gaborIncrementBound_holds` supplies the
prefactor `C = 2 * zetaZerosInDiskCardBoundInner` and still multiplies
by `1+log(T+3)`.  The theorems below pull that prefactor out as a
hypothesis on the bin count; they do not claim the log-free increment
as a theorem, and they do not prove the continuous-density brick
`TrudgianGaussianMeasureTransfer` (the `sqrt(2πa)` integral transfer).
-/
import RH.ZeroIncrement
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace RH

open scoped Classical
open Set Finset

/-- Unit-bin Gaussian weight `exp(-(t-c)²/(2a))`. -/
noncomputable def gaussWeight (a c t : ℝ) : ℝ :=
  Real.exp (-(t - c) ^ 2 / (2 * a))

/-- Supremum of the Gaussian weight on the closed unit bin `[k,k+1]`. -/
noncomputable def gaussBinMax (a c : ℝ) (k : ℤ) : ℝ :=
  sSup (gaussWeight a c '' Icc (k : ℝ) ((k : ℝ) + 1))

/-- Jacobi-theta lobe majorant `Θ_lobe(a) = 3 + 2 Σ_{m≥1} exp(-m²/(2a))`. -/
noncomputable def thetaLobe (a : ℝ) : ℝ :=
  3 + 2 * ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a))

/-- Half-open unit bin of an ordinate, matching `gaborZeroCount`
increments: `T < im ≤ T+1` is the bin of `T`. -/
noncomputable def ordinateBin (t : ℝ) : ℤ :=
  Int.ceil t - 1

lemma gaussWeight_nonneg (a c t : ℝ) : 0 ≤ gaussWeight a c t :=
  (Real.exp_pos _).le

lemma gaussWeight_le_one {a c t : ℝ} (ha : 0 < a) :
    gaussWeight a c t ≤ 1 := by
  unfold gaussWeight
  refine Real.exp_le_one_iff.mpr ?_
  exact div_nonpos_of_nonpos_of_nonneg
    (neg_nonpos.mpr (sq_nonneg _))
    (mul_nonneg (by norm_num) ha.le)

/-- Pointwise bin-max bound: on `[k,k+1]`, the Gaussian is at most
`exp(-d²/(2a))` whenever `d` lower-bounds `|t-c|` throughout the bin.
This is the distance-class form (`d = m` or `d = m-1`). -/
theorem gauss_bin_max_bound {a c : ℝ} (ha : 0 < a) (k : ℤ) {t : ℝ}
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1)) {d : ℝ} (hd : 0 ≤ d)
    (hdist : ∀ s ∈ Icc (k : ℝ) ((k : ℝ) + 1), d ≤ |s - c|) :
    gaussWeight a c t ≤ Real.exp (-d ^ 2 / (2 * a)) := by
  have habs : d ≤ |t - c| := hdist t ht
  have hsq : d ^ 2 ≤ (t - c) ^ 2 :=
    sq_le_sq.mpr (by rwa [abs_of_nonneg hd])
  unfold gaussWeight
  refine Real.exp_le_exp.mpr ?_
  exact div_le_div_of_nonneg_right (neg_le_neg hsq)
    (mul_nonneg (by norm_num) ha.le)

lemma gaussWeight_bddAbove {a c : ℝ} (ha : 0 < a) (k : ℤ) :
    BddAbove (gaussWeight a c '' Icc (k : ℝ) ((k : ℝ) + 1)) :=
  ⟨1, fun y hy => by
    obtain ⟨t, _, rfl⟩ := hy
    exact gaussWeight_le_one ha⟩

lemma gaussWeight_image_nonempty (a c : ℝ) (k : ℤ) :
    (gaussWeight a c '' Icc (k : ℝ) ((k : ℝ) + 1)).Nonempty :=
  ⟨gaussWeight a c (k : ℝ), ⟨(k : ℝ), ⟨le_rfl, by linarith⟩, rfl⟩⟩

lemma le_gaussBinMax {a c t : ℝ} (ha : 0 < a) {k : ℤ}
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1)) :
    gaussWeight a c t ≤ gaussBinMax a c k := by
  unfold gaussBinMax
  exact le_csSup (gaussWeight_bddAbove ha k) (mem_image_of_mem _ ht)

lemma gaussBinMax_nonneg {a c : ℝ} (ha : 0 < a) (k : ℤ) :
    0 ≤ gaussBinMax a c k :=
  (gaussWeight_nonneg a c (k : ℝ)).trans
    (le_gaussBinMax ha ⟨le_rfl, by linarith⟩)

lemma gaussBinMax_le_one {a c : ℝ} (ha : 0 < a) (k : ℤ) :
    gaussBinMax a c k ≤ 1 := by
  unfold gaussBinMax
  refine csSup_le (gaussWeight_image_nonempty a c k) ?_
  intro y hy
  obtain ⟨t, _, rfl⟩ := hy
  exact gaussWeight_le_one ha

lemma gaussBinMax_le_exp {a c d : ℝ} (ha : 0 < a) (k : ℤ) (hd : 0 ≤ d)
    (hdist : ∀ t ∈ Icc (k : ℝ) ((k : ℝ) + 1), d ≤ |t - c|) :
    gaussBinMax a c k ≤ Real.exp (-d ^ 2 / (2 * a)) := by
  unfold gaussBinMax
  refine csSup_le (gaussWeight_image_nonempty a c k) ?_
  intro y hy
  obtain ⟨t, ht, rfl⟩ := hy
  exact gauss_bin_max_bound ha k ht hd hdist

lemma int_cast_sub_sub (k n : ℤ) :
    ((k - n - 1 : ℤ) : ℝ) = (k : ℝ) - (n : ℝ) - 1 := by
  push_cast
  ring

lemma int_cast_sub_sub' (n k : ℤ) :
    ((n - 1 - k : ℤ) : ℝ) = (n : ℝ) - 1 - (k : ℝ) := by
  push_cast
  ring

lemma gauss_bin_dist_right {c : ℝ} {k n : ℤ}
    (hn : n = Int.floor c) (hk : n + 2 ≤ k) {t : ℝ}
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1)) :
    ((k - n - 1 : ℤ) : ℝ) ≤ |t - c| := by
  have hclt : c < (n : ℝ) + 1 := hn ▸ Int.lt_floor_add_one c
  have hkR : (n : ℝ) + 2 ≤ (k : ℝ) := by exact_mod_cast hk
  have htc : 0 ≤ t - c := by linarith [ht.1, hkR, hclt]
  rw [abs_of_nonneg htc, int_cast_sub_sub]
  linarith [ht.1, hkR, hclt]

lemma gauss_bin_dist_left {c : ℝ} {k n : ℤ}
    (hn : n = Int.floor c) (hk : k ≤ n - 2) {t : ℝ}
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1)) :
    ((n - 1 - k : ℤ) : ℝ) ≤ |t - c| := by
  have hnle : (n : ℝ) ≤ c := hn ▸ Int.floor_le c
  have htc : t - c ≤ 0 := by
    have : (k : ℝ) + 1 ≤ (n : ℝ) - 1 := by
      have hle : (k : ℝ) ≤ (n : ℝ) - 2 := by exact_mod_cast hk
      linarith
    linarith [ht.2, hnle]
  rw [abs_of_nonpos htc, int_cast_sub_sub']
  linarith [ht.2, hnle]

lemma gaussBinMax_le_right {a c : ℝ} (ha : 0 < a) {k n : ℤ}
    (hn : n = Int.floor c) (hk : n + 2 ≤ k) :
    gaussBinMax a c k ≤
      Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) := by
  refine gaussBinMax_le_exp ha k ?_ ?_
  · have : (0 : ℤ) ≤ k - n - 1 := by omega
    exact_mod_cast this
  · intro t ht
    exact gauss_bin_dist_right hn hk ht

lemma gaussBinMax_le_left {a c : ℝ} (ha : 0 < a) {k n : ℤ}
    (hn : n = Int.floor c) (hk : k ≤ n - 2) :
    gaussBinMax a c k ≤
      Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) := by
  refine gaussBinMax_le_exp ha k ?_ ?_
  · have : (0 : ℤ) ≤ n - 1 - k := by omega
    exact_mod_cast this
  · intro t ht
    exact gauss_bin_dist_left hn hk ht

/-- Comparison `exp(-m²/(2a)) ≤ exp(-m/(2a))` for the `m`-th theta term. -/
theorem gauss_theta_term_le_geom {a : ℝ} (ha : 0 < a) (m : ℕ) :
    Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) ≤
      Real.exp (-((m + 1 : ℕ) : ℝ) / (2 * a)) := by
  refine Real.exp_le_exp.mpr ?_
  have hden : 0 ≤ 2 * a := mul_nonneg (by norm_num) ha.le
  have hx : (1 : ℝ) ≤ ((m + 1 : ℕ) : ℝ) := by
    exact_mod_cast Nat.succ_pos m
  have hsq : ((m + 1 : ℕ) : ℝ) ≤ ((m + 1 : ℕ) : ℝ) ^ 2 := by nlinarith
  exact div_le_div_of_nonneg_right (neg_le_neg hsq) hden

/-- The theta series `Σ_{m≥1} exp(-m²/(2a))` converges by geometric
comparison `exp(-m²/(2a)) ≤ exp(-m/(2a))`. -/
theorem theta_lobe_summable {a : ℝ} (ha : 0 < a) :
    Summable fun m : ℕ =>
      Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  have hc : -(1 : ℝ) / (2 * a) < 0 := by
    rw [neg_div]
    exact neg_lt_zero.mpr (div_pos (by norm_num) (mul_pos (by norm_num) ha))
  have hgeom : Summable fun n : ℕ =>
      Real.exp ((n : ℝ) * (-(1 : ℝ) / (2 * a))) :=
    Real.summable_exp_nat_mul_iff.mpr hc
  have hshift : Summable fun m : ℕ =>
      Real.exp (-((m + 1 : ℕ) : ℝ) / (2 * a)) := by
    have h := (summable_nat_add_iff (f := fun n : ℕ =>
      Real.exp ((n : ℝ) * (-(1 : ℝ) / (2 * a)))) 1).mpr hgeom
    refine h.congr fun m => ?_
    congr 1
    have : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by exact_mod_cast rfl
    rw [this]
    ring
  exact Summable.of_nonneg_of_le (fun _ => (Real.exp_pos _).le)
    (fun m => gauss_theta_term_le_geom ha m) hshift

private lemma sum_right_tail_le {a : ℝ} (ha : 0 < a) (n : ℤ) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => n + 2 ≤ k),
        Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  set Kr := K.filter (fun k => n + 2 ≤ k)
  let φ : ℤ → ℕ := fun k => Int.toNat (k - n - 2)
  have hφ : ∀ k ∈ Kr, ((k - n - 1 : ℤ) : ℝ) = ((φ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have hk' : n + 2 ≤ k := (mem_filter.mp hk).2
    have hnn : 0 ≤ k - n - 2 := by omega
    have hto : ((k - n - 2).toNat : ℤ) = k - n - 2 :=
      Int.toNat_of_nonneg hnn
    have h1 : (k - n - 1 : ℤ) = (k - n - 2) + 1 := by ring
    have h2 : ((φ k + 1 : ℕ) : ℤ) = (k - n - 2) + 1 := by
      unfold φ
      rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]
    exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kr, ∀ k₂ ∈ Kr, φ k₁ = φ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hφeq
    have h1 : 0 ≤ k₁ - n - 2 := by
      have : n + 2 ≤ k₁ := (mem_filter.mp hk₁).2
      omega
    have h2 : 0 ≤ k₂ - n - 2 := by
      have : n + 2 ≤ k₂ := (mem_filter.mp hk₂).2
      omega
    have ht1 := Int.toNat_of_nonneg h1
    have ht2 := Int.toNat_of_nonneg h2
    have : k₁ - n - 2 = k₂ - n - 2 := by
      calc
        k₁ - n - 2 = ((k₁ - n - 2).toNat : ℤ) := ht1.symm
        _ = ((k₂ - n - 2).toNat : ℤ) := by exact_mod_cast hφeq
        _ = k₂ - n - 2 := ht2
    omega
  have hsummable := theta_lobe_summable ha
  have himage :
      ∑ k ∈ Kr, Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) =
        ∑ m ∈ Kr.image φ,
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    rw [sum_image hinj]
    refine sum_congr rfl fun k hk => ?_
    rw [hφ k hk]
  rw [himage]
  exact hsummable.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)

private lemma sum_left_tail_le {a : ℝ} (ha : 0 < a) (n : ℤ) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k ≤ n - 2),
        Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  set Kl := K.filter (fun k => k ≤ n - 2)
  let ψ : ℤ → ℕ := fun k => Int.toNat (n - 2 - k)
  have hψ : ∀ k ∈ Kl, ((n - 1 - k : ℤ) : ℝ) = ((ψ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have hk' : k ≤ n - 2 := (mem_filter.mp hk).2
    have hnn : 0 ≤ n - 2 - k := by omega
    have hto : ((n - 2 - k).toNat : ℤ) = n - 2 - k :=
      Int.toNat_of_nonneg hnn
    have h1 : (n - 1 - k : ℤ) = (n - 2 - k) + 1 := by ring
    have h2 : ((ψ k + 1 : ℕ) : ℤ) = (n - 2 - k) + 1 := by
      unfold ψ
      rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]
    exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kl, ∀ k₂ ∈ Kl, ψ k₁ = ψ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hψeq
    have h1 : 0 ≤ n - 2 - k₁ := by
      have : k₁ ≤ n - 2 := (mem_filter.mp hk₁).2
      omega
    have h2 : 0 ≤ n - 2 - k₂ := by
      have : k₂ ≤ n - 2 := (mem_filter.mp hk₂).2
      omega
    have ht1 := Int.toNat_of_nonneg h1
    have ht2 := Int.toNat_of_nonneg h2
    have : n - 2 - k₁ = n - 2 - k₂ := by
      calc
        n - 2 - k₁ = ((n - 2 - k₁).toNat : ℤ) := ht1.symm
        _ = ((n - 2 - k₂).toNat : ℤ) := by exact_mod_cast hψeq
        _ = n - 2 - k₂ := ht2
    omega
  have hsummable := theta_lobe_summable ha
  have himage :
      ∑ k ∈ Kl, Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) =
        ∑ m ∈ Kl.image ψ,
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    rw [sum_image hinj]
    refine sum_congr rfl fun k hk => ?_
    rw [hψ k hk]
  rw [himage]
  exact hsummable.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)

lemma central3_card (n : ℤ) :
    ({n - 1, n, n + 1} : Finset ℤ).card = 3 := by
  have h01 : n ≠ n + 1 := by omega
  have h20 : n - 1 ≠ n := by omega
  have h21 : n - 1 ≠ n + 1 := by omega
  simp [Finset.card_insert_of_notMem, Finset.card_singleton, h01, h20, h21]

lemma gaussBinMax_sum_le {a c : ℝ} (ha : 0 < a) (K : Finset ℤ) :
    ∑ k ∈ K, gaussBinMax a c k ≤ thetaLobe a := by
  set n := Int.floor c
  let central : Finset ℤ := {n - 1, n, n + 1}
  have hterm : ∀ k ∈ K,
      gaussBinMax a c k ≤
        (if k ∈ central then (1 : ℝ) else 0) +
          (if n + 2 ≤ k then
              Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
            (if k ≤ n - 2 then
                Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) := by
    intro k _hk
    by_cases hcen : k ∈ central
    · have hn2 : ¬ n + 2 ≤ k := by
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [central] using hcen
        omega
      have hn3 : ¬ k ≤ n - 2 := by
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by simpa [central] using hcen
        omega
      simp [hcen, hn2, hn3]
      exact gaussBinMax_le_one (a := a) (c := c) ha k
    · have hr? : n + 2 ≤ k ∨ k ≤ n - 2 := by
        have : k ≠ n - 1 ∧ k ≠ n ∧ k ≠ n + 1 := by
          refine ⟨?_, ?_, ?_⟩
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
        omega
      rcases hr? with hr | hl
      · have hl' : ¬ k ≤ n - 2 := by omega
        have hle := gaussBinMax_le_right (a := a) (c := c) ha (n := n) rfl hr
        simp [hcen, hr, hl']
        rw [int_cast_sub_sub] at hle
        exact hle
      · have hr : ¬ n + 2 ≤ k := by omega
        have hle := gaussBinMax_le_left (a := a) (c := c) ha (n := n) rfl hl
        simp [hcen, hr, hl]
        rw [int_cast_sub_sub'] at hle
        exact hle
  have hsum := sum_le_sum hterm
  have hsplit :
      ∑ k ∈ K,
          ((if k ∈ central then (1 : ℝ) else 0) +
            (if n + 2 ≤ k then
                Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
              (if k ≤ n - 2 then
                  Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0)) =
        ∑ k ∈ K, (if k ∈ central then (1 : ℝ) else 0) +
          ∑ k ∈ K, (if n + 2 ≤ k then
              Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
            ∑ k ∈ K, (if k ≤ n - 2 then
                Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) := by
    simp [sum_add_distrib]
  rw [hsplit] at hsum
  have hcen :
      ∑ k ∈ K, (if k ∈ central then (1 : ℝ) else 0) ≤ (3 : ℝ) := by
    have hite :
        ∑ k ∈ K, (if k ∈ central then (1 : ℝ) else 0) =
          ((K.filter (fun k => k ∈ central)).card : ℝ) := by
      rw [sum_ite, sum_const, sum_const, nsmul_eq_mul, nsmul_eq_mul,
        mul_zero, add_zero, mul_one]
    rw [hite]
    have hsub : K.filter (fun k => k ∈ central) ⊆ central := by
      intro k hk
      exact (Finset.mem_filter.mp hk).2
    have hle' := Finset.card_le_card hsub
    exact Nat.cast_le.mpr (hle'.trans (le_of_eq (central3_card n)))
  have hright :
      ∑ k ∈ K, (if n + 2 ≤ k then
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
        ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have : ∑ k ∈ K, (if n + 2 ≤ k then
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) =
        ∑ k ∈ K.filter (fun k => n + 2 ≤ k),
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) := by
      exact (sum_filter (p := fun k => n + 2 ≤ k)
        (f := fun k => Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
    rw [this]
    exact sum_right_tail_le ha n K
  have hleft :
      ∑ k ∈ K, (if k ≤ n - 2 then
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
        ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have : ∑ k ∈ K, (if k ≤ n - 2 then
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) =
        ∑ k ∈ K.filter (fun k => k ≤ n - 2),
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) := by
      exact (sum_filter (p := fun k => k ≤ n - 2)
        (f := fun k => Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
    rw [this]
    exact sum_left_tail_le ha n K
  unfold thetaLobe
  linarith [hsum, hcen, hright, hleft]

lemma gaussBinMax_summable {a c : ℝ} (ha : 0 < a) :
    Summable fun k : ℤ => gaussBinMax a c k :=
  summable_of_sum_le (fun k => gaussBinMax_nonneg ha k)
    (fun K => gaussBinMax_sum_le ha K)

/-- `Σ_k max_{[k,k+1]} exp(-(t-c)²/(2a)) ≤ Θ_lobe(a)`, any center `c`. -/
theorem gauss_binMax_tsum_le {a c : ℝ} (ha : 0 < a) :
    ∑' k : ℤ, gaussBinMax a c k ≤ thetaLobe a :=
  Real.tsum_le_of_sum_le (fun k => gaussBinMax_nonneg ha k)
    (fun K => gaussBinMax_sum_le ha K)

lemma mem_ordinateBin (t : ℝ) :
    (ordinateBin t : ℝ) < t ∧ t ≤ (ordinateBin t : ℝ) + 1 := by
  unfold ordinateBin
  constructor
  · have : (Int.ceil t : ℝ) < t + 1 := Int.ceil_lt_add_one t
    push_cast
    linarith
  · have : t ≤ (Int.ceil t : ℝ) := Int.le_ceil t
    push_cast
    linarith

lemma ordinateBin_unique {t : ℝ} {k : ℤ}
    (hk : (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1) :
    ordinateBin t = k := by
  have hk2 : t ≤ ((k + 1 : ℤ) : ℝ) := by
    have : ((k + 1 : ℤ) : ℝ) = (k : ℝ) + 1 := by norm_cast
    rw [this]
    exact hk.2
  have hle : Int.ceil t ≤ k + 1 := Int.ceil_le.mpr hk2
  have hge : k + 1 ≤ Int.ceil t := by
    rw [Int.add_one_le_iff]
    refine lt_of_not_ge ?_
    intro h
    have : t ≤ (k : ℝ) := (Int.ceil_le (a := t) (z := k)).mp h
    exact not_le_of_gt hk.1 this
  unfold ordinateBin
  omega

lemma mem_Icc_of_ordinateBin (t : ℝ) :
    t ∈ Icc (ordinateBin t : ℝ) ((ordinateBin t : ℝ) + 1) := by
  have h := mem_ordinateBin t
  exact ⟨h.1.le, h.2⟩

/-- Fiber decomposition of a finite set along an integer label. -/
lemma sum_fiber_mul {α : Type*} [DecidableEq α]
    (S : Finset α) (g : α → ℤ) (M : ℤ → ℝ) :
    S.sum (fun x => M (g x)) =
      ∑ k ∈ S.image g,
        ((S.filter (fun x => g x = k)).card : ℝ) * M k := by
  classical
  set S0 := S
  set bins := S0.image g
  have hmaps : ∀ x ∈ S0, g x ∈ bins :=
    fun x hx => Finset.mem_image_of_mem g hx
  have hinner : ∀ k ∈ bins,
      (S0.filter (fun x => g x = k)).sum (fun x => M (g x)) =
        ((S0.filter (fun x => g x = k)).card : ℝ) * M k := by
    intro k _hk
    have : ∀ x ∈ S0.filter (fun x => g x = k), M (g x) = M k := by
      intro x hx
      rw [(Finset.mem_filter.mp hx).2]
    rw [Finset.sum_congr rfl this, Finset.sum_const, nsmul_eq_mul]
  have hS :=
    Finset.disjiUnion_filter_eq_of_maps_to (s := S0) (t := bins) (f := g) hmaps
  conv_lhs => rw [← hS]
  rw [Finset.sum_disjiUnion]
  exact Finset.sum_congr rfl hinner

/-- Abstract bin partial summation for a finite labelled set: if every
half-open unit bin contains at most `C` labels, the weighted sum is at
most `C` times the sum of bin maxima. -/
theorem bin_partial_summation
    {α : Type*} [DecidableEq α]
    {w : ℝ → ℝ} (_hw : ∀ t, 0 ≤ w t)
    (S : Finset α) (γ : α → ℝ) {C : ℝ} (hC0 : 0 ≤ C)
    (hC : ∀ k : ℤ,
      ((S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1)).card : ℝ) ≤ C)
    {M : ℤ → ℝ} (hM0 : ∀ k, 0 ≤ M k)
    (hM : ∀ (k : ℤ) (t : ℝ), t ∈ Icc (k : ℝ) ((k : ℝ) + 1) → w t ≤ M k)
    (hMs : Summable M) :
    (S.sum (fun x => w (γ x)) : ℝ) ≤ C * ∑' k : ℤ, M k := by
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
      S.sum (fun x => M (g x)) ≤ ∑ k ∈ bins, C * M k := by
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
        change g x = k at hbin
        simpa [g, hbin] using hm
      exact Finset.mem_filter.mpr ⟨hxS, hm'⟩
    have hcard :
        ((S.filter (fun x => g x = k)).card : ℝ) ≤ C :=
      (Nat.cast_le.mpr (Finset.card_le_card hsub)).trans (hC k)
    exact mul_le_mul_of_nonneg_right hcard (hM0 k)
  have hsum₃ : ∑ k ∈ bins, C * M k = C * ∑ k ∈ bins, M k := by
    simp [mul_sum]
  have hsum₄ : ∑ k ∈ bins, M k ≤ ∑' k : ℤ, M k :=
    hMs.sum_le_tsum _ (fun _ _ => hM0 _)
  calc
    (S.sum (fun x => w (γ x)) : ℝ) ≤ S.sum (fun x => M (g x)) := hsum₁
    _ ≤ ∑ k ∈ bins, C * M k := hsum₂
    _ = C * ∑ k ∈ bins, M k := hsum₃
    _ ≤ C * ∑' k : ℤ, M k := mul_le_mul_of_nonneg_left hsum₄ hC0

/-- r579: the same comparison with a *per-bin* occupancy cap `C k`
(Path-A log increment) instead of a uniform constant. -/
theorem bin_partial_summation_varC
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
      exact Finset.mem_filter.mpr ⟨hxS, hm'⟩
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

/-- The `gaborZeroCount` increment is the card of the unit bin
`T < im ≤ T+1` inside `gaborZerosUpTo`. -/
lemma gaborZerosUpTo_bin_card {T : ℝ} {k : ℤ}
    (_hk0 : 0 ≤ (k : ℝ)) (hkT : (k : ℝ) + 1 ≤ T) :
    ((gaborZerosUpTo T).filter
        (fun s => (k : ℝ) < s.im ∧ s.im ≤ (k : ℝ) + 1)).card =
      gaborZeroCount ((k : ℝ) + 1) - gaborZeroCount (k : ℝ) := by
  have hmono :=
    gaborZerosUpTo_mono (T := (k : ℝ)) (U := (k : ℝ) + 1) (by linarith)
  rw [gaborZeroCount_eq_card, gaborZeroCount_eq_card]
  have hdiff :
      (gaborZerosUpTo ((k : ℝ) + 1)).card - (gaborZerosUpTo (k : ℝ)).card =
        (gaborZerosUpTo ((k : ℝ) + 1) \ gaborZerosUpTo (k : ℝ)).card := by
    have hcard :
        (gaborZerosUpTo ((k : ℝ) + 1) \ gaborZerosUpTo (k : ℝ)).card =
          (gaborZerosUpTo ((k : ℝ) + 1)).card -
            (gaborZerosUpTo (k : ℝ) ∩ gaborZerosUpTo ((k : ℝ) + 1)).card :=
      Finset.card_sdiff
    rw [Finset.inter_eq_left.mpr hmono] at hcard
    exact hcard.symm
  rw [hdiff]
  refine Finset.card_bij (fun s _ => s) ?_ (fun _ _ _ _ h => h) ?_
  · intro s hs
    have hs' := Finset.mem_filter.mp hs
    have hsT := mem_gaborZerosUpTo.mp hs'.1
    refine Finset.mem_sdiff.mpr ⟨?_, ?_⟩
    · exact mem_gaborZerosUpTo.mpr ⟨hsT.1, hsT.2.1, hs'.2.2⟩
    · intro hOld
      exact not_lt_of_ge (mem_gaborZerosUpTo.mp hOld).2.2 hs'.2.1
  · intro s hs
    obtain ⟨hsTop, hsOld⟩ := Finset.mem_sdiff.mp hs
    have hTop := mem_gaborZerosUpTo.mp hsTop
    have him : (k : ℝ) < s.im := by
      by_contra h
      exact hsOld (mem_gaborZerosUpTo.mpr
        ⟨hTop.1, hTop.2.1, le_of_not_gt h⟩)
    have hsT : s ∈ gaborZerosUpTo T :=
      mem_gaborZerosUpTo.mpr ⟨hTop.1, hTop.2.1, hTop.2.2.trans hkT⟩
    exact ⟨s, Finset.mem_filter.mpr ⟨hsT, him, hTop.2.2⟩, rfl⟩

/-- r552: Gaussian mass of a finite ordinate set is at most the Path-A
increment *prefactor* times `Θ_lobe(a)`, independently of the packet
center, once every unit bin has at most that many points.
`gaborIncrementBound_holds` names the prefactor
`2 * zetaZerosInDiskCardBoundInner`. -/
theorem gauss_online_mass_uniform
    {α : Type*} [DecidableEq α]
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset α) (γ : α → ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1)).card : ℝ) ≤
        2 * zetaZerosInDiskCardBoundInner) :
    (S.sum (fun x => gaussWeight a c (γ x)) : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * thetaLobe a := by
  have hC0 : 0 ≤ 2 * zetaZerosInDiskCardBoundInner :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hM0 : ∀ k : ℤ, 0 ≤ gaussBinMax a c k :=
    fun k => gaussBinMax_nonneg ha k
  have hM : ∀ (k : ℤ) (t : ℝ), t ∈ Icc (k : ℝ) ((k : ℝ) + 1) →
      gaussWeight a c t ≤ gaussBinMax a c k :=
    fun _k _t ht => le_gaussBinMax ha ht
  have hbound :=
    bin_partial_summation (α := α) (w := gaussWeight a c)
      (fun _ => gaussWeight_nonneg _ _ _) S γ hC0 hinc hM0 hM
      (gaussBinMax_summable ha)
  exact hbound.trans
    (mul_le_mul_of_nonneg_left (gauss_binMax_tsum_le ha) hC0)

/-- Specialization to a finite real ordinate set. -/
theorem gauss_online_mass_uniform_ordinates
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        2 * zetaZerosInDiskCardBoundInner) :
    (S.sum (gaussWeight a c) : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * thetaLobe a :=
  gauss_online_mass_uniform ha c S id hinc

/-- Specialization to `gaborZerosUpTo`, using the ZeroIncrement count. -/
theorem gauss_online_mass_uniform_gaborZeros
    {a : ℝ} (ha : 0 < a) (c : ℝ) {T : ℝ}
    (hinc : ∀ k : ℤ,
      ((gaborZerosUpTo T).filter
          (fun s => (k : ℝ) < s.im ∧ s.im ≤ (k : ℝ) + 1)).card.cast ≤
        2 * zetaZerosInDiskCardBoundInner) :
    ((gaborZerosUpTo T).sum (fun s => gaussWeight a c s.im) : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * thetaLobe a :=
  gauss_online_mass_uniform ha c (gaborZerosUpTo T) Complex.im hinc

/-- r579 log-occupancy discrete Gauss transfer: unit-bin card
`≤ C k` (e.g. Path-A `1+log`) yields mass `≤ ∑ C(k) · binMax(k)`. -/
theorem gauss_online_mass_varC
    {α : Type*} [DecidableEq α]
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset α) (γ : α → ℝ)
    (C : ℤ → ℝ) (hC0 : ∀ k, 0 ≤ C k)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun x => (k : ℝ) < γ x ∧ γ x ≤ (k : ℝ) + 1)).card : ℝ) ≤
        C k)
    (hMs : Summable fun k : ℤ => C k * gaussBinMax a c k) :
    (S.sum (fun x => gaussWeight a c (γ x)) : ℝ) ≤
      ∑' k : ℤ, C k * gaussBinMax a c k :=
  bin_partial_summation_varC (w := gaussWeight a c)
    (fun _ => gaussWeight_nonneg _ _ _) S γ C hC0 hinc
    (fun k => gaussBinMax_nonneg ha k)
    (fun _k _t ht => le_gaussBinMax ha ht) hMs

theorem gauss_online_mass_varC_ordinates
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (C : ℤ → ℝ) (hC0 : ∀ k, 0 ≤ C k)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        C k)
    (hMs : Summable fun k : ℤ => C k * gaussBinMax a c k) :
    (S.sum (gaussWeight a c) : ℝ) ≤
      ∑' k : ℤ, C k * gaussBinMax a c k :=
  gauss_online_mass_varC ha c S id C hC0 hinc hMs

#print axioms gauss_bin_max_bound
#print axioms gauss_theta_term_le_geom
#print axioms theta_lobe_summable
#print axioms gauss_binMax_tsum_le
#print axioms bin_partial_summation
#print axioms gauss_online_mass_uniform
#print axioms gaborZerosUpTo_bin_card
#print axioms gauss_online_mass_uniform_gaborZeros
#print axioms bin_partial_summation_varC
#print axioms gauss_online_mass_varC
#print axioms gauss_online_mass_varC_ordinates

end RH
