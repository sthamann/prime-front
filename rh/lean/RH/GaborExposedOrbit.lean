/-
RH/GaborExposedOrbit.lean -- r605 existential pure-Gabor separator.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.
The live statement is an equivalence: nonnegativity of
`gaborZeroSide` on every pure packet is equivalent to Mathlib
`RiemannHypothesis`.  Positivity of `gaborZeroSide` stays open.

The prescribed-packet pointwise form `GaborZeroSideForAllZeros`
(scaling law `a = σ²/64`, `ω = γ − πa/σ`) is OVERSPECIFIED (r605):
numerics r549/r551/r591 show it fails under competitor zeros.
The RH criterion only needs an existential separator
`¬RH → ∃ a ω, gaborZeroSide (pureGaborTest a ω) < 0`.
The reverse `RH → 0 ≤ gaborZeroSide` is
`rh_implies_gaborZeroSide_nonneg`.

No asserting `sorry`.  Census unchanged.  No new axioms.
-/
import RH.GaborArithmeticSeparator
import Mathlib.Analysis.Normed.Group.InfiniteSum
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Order.Interval.Set.Infinite

namespace RH

set_option maxHeartbeats 4000000

open scoped Classical ComplexConjugate
open Set Finset Filter Complex
open scoped Topology Real

/-! ## Score -/

/-- Dominant-lobe exponent numerator `σ² − (|t| − ω)²`. -/
noncomputable def gaborScore (σ t omega : ℝ) : ℝ :=
  σ ^ 2 - (|t| - omega) ^ 2

lemma sq_abs_sub (t omega : ℝ) :
    (|t| - omega) ^ 2 = t ^ 2 - 2 * |t| * omega + omega ^ 2 := by
  calc
    (|t| - omega) ^ 2
        = |t| ^ 2 - 2 * |t| * omega + omega ^ 2 := by ring
    _ = t ^ 2 - 2 * |t| * omega + omega ^ 2 := by rw [sq_abs]

lemma gaborScore_eq (σ t omega : ℝ) :
    gaborScore σ t omega =
      σ ^ 2 - t ^ 2 + 2 * |t| * omega - omega ^ 2 := by
  unfold gaborScore
  rw [sq_abs_sub]
  ring

lemma gaborScore_affine (σ t omega : ℝ) :
    gaborScore σ t omega + omega ^ 2 =
      2 * |t| * omega + σ ^ 2 - t ^ 2 := by
  rw [gaborScore_eq]
  ring

lemma gaborScore_nonpos_of_sigma_zero (t omega : ℝ) :
    gaborScore 0 t omega ≤ 0 := by
  unfold gaborScore
  nlinarith [sq_nonneg (|t| - omega)]

lemma abs_sub_le_add (a b : ℝ) : |a - b| ≤ |a| + |b| := by
  simpa using abs_sub_le a 0 b

lemma abs_abs_sub_omega_le_abs_add (t omega : ℝ) (hω : 0 ≤ omega) :
    abs (|t| - omega) ≤ |t + omega| := by
  by_cases ht : 0 ≤ t
  · rw [abs_of_nonneg ht, abs_of_nonneg (add_nonneg ht hω)]
    have h := abs_sub_le_add t omega
    simpa [abs_of_nonneg ht, abs_of_nonneg hω] using h
  · have htlt : t < 0 := lt_of_not_ge ht
    have heq : t + omega = -(|t| - omega) := by
      rw [abs_of_neg htlt]
      ring
    rw [heq, abs_neg]

lemma abs_abs_sub_omega_le_abs_sub (t omega : ℝ) (hω : 0 ≤ omega) :
    abs (|t| - omega) ≤ |t - omega| := by
  by_cases ht : 0 ≤ t
  · rw [abs_of_nonneg ht]
  · have htlt : t < 0 := lt_of_not_ge ht
    have heq : t - omega = -(|t| + omega) := by
      rw [abs_of_neg htlt]
      ring
    rw [heq, abs_neg, abs_of_nonneg (add_nonneg (abs_nonneg _) hω)]
    have h := abs_sub_le_add (|t|) omega
    rwa [abs_of_nonneg (abs_nonneg t), abs_of_nonneg hω] at h

lemma plus_lobe_num_le_score (σ t omega : ℝ) (hω : 0 ≤ omega) :
    σ ^ 2 - (t + omega) ^ 2 ≤ gaborScore σ t omega := by
  unfold gaborScore
  have h := sq_le_sq.mpr (abs_abs_sub_omega_le_abs_add t omega hω)
  linarith

lemma minus_lobe_num_le_score (σ t omega : ℝ) (hω : 0 ≤ omega) :
    σ ^ 2 - (t - omega) ^ 2 ≤ gaborScore σ t omega := by
  unfold gaborScore
  have h := sq_le_sq.mpr (abs_abs_sub_omega_le_abs_sub t omega hω)
  linarith

lemma center_lobe_num_le_score (σ t omega : ℝ) (hω : 0 ≤ omega) :
    σ ^ 2 - t ^ 2 - omega ^ 2 ≤ gaborScore σ t omega := by
  unfold gaborScore
  rw [sq_abs_sub]
  nlinarith [mul_nonneg (abs_nonneg t) hω]

lemma minus_lobe_num_eq_score_of_nonneg_im (σ t omega : ℝ) (ht : 0 ≤ t) :
    σ ^ 2 - (t - omega) ^ 2 = gaborScore σ t omega := by
  unfold gaborScore
  rw [abs_of_nonneg ht]

lemma plus_lobe_num_eq_score_sub_four
    (σ t omega : ℝ) (ht : 0 ≤ t) :
    σ ^ 2 - (t + omega) ^ 2 =
      gaborScore σ t omega - 4 * t * omega := by
  rw [← minus_lobe_num_eq_score_of_nonneg_im σ t omega ht]
  ring

lemma center_lobe_num_eq_score_sub_two
    (σ t omega : ℝ) (ht : 0 ≤ t) :
    σ ^ 2 - t ^ 2 - omega ^ 2 =
      gaborScore σ t omega - 2 * t * omega := by
  rw [← minus_lobe_num_eq_score_of_nonneg_im σ t omega ht]
  ring

lemma half_abs_sq (σ : ℝ) : (|σ| / 2) ^ 2 = σ ^ 2 / 4 := by
  have h : (|σ| / 2) ^ 2 = |σ| ^ 2 / 4 := by ring
  rw [h, sq_abs]

lemma gaborScore_near {σ t omega : ℝ}
    (h : abs (|t| - omega) < |σ| / 2) (hσ : σ ≠ 0) :
    (3 / 4 : ℝ) * σ ^ 2 < gaborScore σ t omega := by
  unfold gaborScore
  have hpos : 0 ≤ |σ| / 2 := div_nonneg (abs_nonneg _) (by norm_num)
  have hsq : (|t| - omega) ^ 2 < (|σ| / 2) ^ 2 := by
    rw [sq_lt_sq, abs_of_nonneg hpos]
    exact h
  rw [half_abs_sq] at hsq
  have hposσ : 0 < σ ^ 2 := sq_pos_of_ne_zero hσ
  linarith [hposσ]

lemma abs_re_sub_half_lt_half_of_strip
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    |(ρ : ℂ).re - 1 / 2| < 1 / 2 := by
  have h := ρ.property
  rw [abs_lt]
  constructor <;> linarith [h.2.1, h.2.2]

lemma sigma_sq_lt_quarter
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ((ρ : ℂ).re - 1 / 2) ^ 2 < (1 / 4 : ℝ) := by
  have h := abs_re_sub_half_lt_half_of_strip ρ
  have hsq : ((ρ : ℂ).re - 1 / 2) ^ 2 < (1 / 2 : ℝ) ^ 2 := by
    rw [← sq_abs, sq_lt_sq, abs_of_nonneg (abs_nonneg _),
      abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)]
    exact h
  have h14 : (1 / 2 : ℝ) ^ 2 = 1 / 4 := by norm_num
  rwa [h14] at hsq

lemma sq_lt_of_abs_lt {x b : ℝ} (hb : 0 ≤ b) (h : |x| < b) :
    x ^ 2 < b ^ 2 := by
  rw [← sq_abs, sq_lt_sq, abs_of_nonneg (abs_nonneg _), abs_of_nonneg hb]
  exact h

lemma gaborScore_far {σ t t0 σ0 omega : ℝ}
    (hσ : |σ| < 1 / 2)
    (ht : |t0| + 1 < |t|)
    (hω : omega < |t0| + |σ0| / 2)
    (hσ0 : |σ0| < 1 / 2) :
    gaborScore σ t omega < 0 := by
  unfold gaborScore
  have hgap : (3 / 4 : ℝ) < |t| - omega := by
    have : (3 / 4 : ℝ) < 1 - |σ0| / 2 := by linarith
    have : 1 - |σ0| / 2 < |t0| + 1 - omega := by linarith
    linarith
  have hpos : 0 ≤ |t| - omega :=
    le_of_lt (lt_trans (by norm_num : (0 : ℝ) < 3 / 4) hgap)
  have hsq : (9 / 16 : ℝ) < (|t| - omega) ^ 2 := by
    have h34 : (3 / 4 : ℝ) ^ 2 = 9 / 16 := by norm_num
    have : (3 / 4 : ℝ) ^ 2 < (|t| - omega) ^ 2 :=
      sq_lt_of_abs_lt hpos (by
        rw [abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 3 / 4)]
        exact hgap)
    rwa [h34] at this
  have hσ2 : σ ^ 2 < (1 / 4 : ℝ) := by
    have h14 : (1 / 2 : ℝ) ^ 2 = 1 / 4 := by norm_num
    have : σ ^ 2 < (1 / 2 : ℝ) ^ 2 :=
      sq_lt_of_abs_lt (by norm_num) hσ
    rwa [h14] at this
  linarith

lemma abs_sub_sq_ge_half_sq (t omega : ℝ) :
    t ^ 2 / 2 - omega ^ 2 ≤ (|t| - omega) ^ 2 := by
  have h :
      (|t| - omega) ^ 2 - (t ^ 2 / 2 - omega ^ 2) =
        (1 / 2) * (|t| - 2 * omega) ^ 2 := by
    rw [sq_abs_sub, ← sq_abs t]
    ring
  nlinarith [sq_nonneg (|t| - 2 * omega), h]

/-! ## Strip coordinates and the FE/conj orbit -/

noncomputable def stripSigma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : ℝ :=
  (ρ : ℂ).re - 1 / 2

noncomputable def stripGamma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : ℝ :=
  (ρ : ℂ).im

lemma stripSigma_ne_zero_iff
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripSigma ρ ≠ 0 ↔ (ρ : ℂ).re ≠ 1 / 2 :=
  sub_ne_zero

lemma stripGamma_ne_zero
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripGamma ρ ≠ 0 := by
  intro h
  exact not_isCriticalStripZetaZero_of_im_zero (by
    simpa [stripGamma] using h) ρ.property

lemma abs_stripSigma_lt_half
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    |stripSigma ρ| < 1 / 2 :=
  abs_re_sub_half_lt_half_of_strip ρ

noncomputable def stripOrbitFinset
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    Finset {z : ℂ // IsCriticalStripZetaZero z} :=
  {ρ, stripStarEquiv ρ, stripFEEquiv ρ, stripOrbitEquiv ρ}

lemma mem_stripOrbitFinset
    (ρ τ : {z : ℂ // IsCriticalStripZetaZero z}) :
    τ ∈ stripOrbitFinset ρ ↔
      τ = ρ ∨ τ = stripStarEquiv ρ ∨ τ = stripFEEquiv ρ ∨
        τ = stripOrbitEquiv ρ := by
  simp [stripOrbitFinset]

lemma stripStar_sigma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripSigma (stripStarEquiv ρ) = stripSigma ρ := by
  simp [stripSigma, stripStarEquiv, Complex.conj_re]

lemma stripStar_gamma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripGamma (stripStarEquiv ρ) = -stripGamma ρ := by
  simp [stripGamma, stripStarEquiv, Complex.conj_im]

lemma stripFE_sigma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripSigma (stripFEEquiv ρ) = -stripSigma ρ := by
  simp [stripSigma, stripFEEquiv, sub_re]
  ring

lemma stripFE_gamma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripGamma (stripFEEquiv ρ) = -stripGamma ρ := by
  simp [stripGamma, stripFEEquiv, sub_im]

lemma stripOrbit_sigma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripSigma (stripOrbitEquiv ρ) = -stripSigma ρ := by
  unfold stripOrbitEquiv
  rw [Equiv.trans_apply, stripFE_sigma, stripStar_sigma]

lemma stripOrbit_gamma (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripGamma (stripOrbitEquiv ρ) = stripGamma ρ := by
  unfold stripOrbitEquiv
  rw [Equiv.trans_apply, stripFE_gamma, stripStar_gamma]
  ring

lemma stripStar_re (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripStarEquiv ρ : ℂ).re = (ρ : ℂ).re := by
  simp [stripStarEquiv, Complex.conj_re]

lemma stripStar_im (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripStarEquiv ρ : ℂ).im = -(ρ : ℂ).im := by
  simp [stripStarEquiv, Complex.conj_im]

lemma stripFE_re (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripFEEquiv ρ : ℂ).re = 1 - (ρ : ℂ).re := by
  simp [stripFEEquiv, sub_re]

lemma stripFE_im (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripFEEquiv ρ : ℂ).im = -(ρ : ℂ).im := by
  simp [stripFEEquiv, sub_im]

lemma stripOrbit_re (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripOrbitEquiv ρ : ℂ).re = 1 - (ρ : ℂ).re := by
  unfold stripOrbitEquiv
  rw [Equiv.trans_apply, stripFE_re, stripStar_re]

lemma stripOrbit_im (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    (stripOrbitEquiv ρ : ℂ).im = (ρ : ℂ).im := by
  unfold stripOrbitEquiv
  rw [Equiv.trans_apply, stripFE_im, stripStar_im]
  ring

lemma gaborScore_of_orbit_mem
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) (omega : ℝ)
    {τ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hτ : τ ∈ stripOrbitFinset ρ) :
    gaborScore (stripSigma τ) (stripGamma τ) omega =
      gaborScore (stripSigma ρ) (stripGamma ρ) omega := by
  rcases (mem_stripOrbitFinset ρ τ).mp hτ with h | h | h | h
  · simp [h]
  · rw [h, stripStar_sigma, stripStar_gamma]
    unfold gaborScore
    simp [abs_neg]
  · rw [h, stripFE_sigma, stripFE_gamma]
    unfold gaborScore
    simp [abs_neg]
  · rw [h, stripOrbit_sigma, stripOrbit_gamma]
    unfold gaborScore
    simp

lemma eq_zero_of_eq_neg {x : ℝ} (h : x = -x) : x = 0 := by
  nlinarith [h]

lemma eq_or_neg_of_abs_eq_abs {a b : ℝ} (h : |a| = |b|) :
    a = b ∨ a = -b := by
  have hsq : a ^ 2 = b ^ 2 := by
    rw [← sq_abs a, ← sq_abs b, h]
  exact (sq_eq_sq_iff_eq_or_eq_neg).mp hsq

lemma mem_stripOrbitFinset_of_same_abs
    {ρ τ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hσ : |stripSigma τ| = |stripSigma ρ|)
    (ht : |stripGamma τ| = |stripGamma ρ|) :
    τ ∈ stripOrbitFinset ρ := by
  apply (mem_stripOrbitFinset ρ τ).mpr
  rcases eq_or_neg_of_abs_eq_abs hσ with hσ | hσ
  · rcases eq_or_neg_of_abs_eq_abs ht with ht | ht
    · left
      apply Subtype.ext
      apply Complex.ext
      · dsimp [stripSigma] at hσ
        linarith
      · dsimp [stripGamma] at ht
        exact ht
    · right; left
      apply Subtype.ext
      apply Complex.ext
      · dsimp [stripSigma] at hσ
        rw [stripStar_re]
        linarith
      · dsimp [stripGamma] at ht
        rw [stripStar_im, ht]
  · rcases eq_or_neg_of_abs_eq_abs ht with ht | ht
    · right; right; right
      apply Subtype.ext
      apply Complex.ext
      · dsimp [stripSigma] at hσ
        rw [stripOrbit_re]
        linarith
      · dsimp [stripGamma] at ht
        rw [stripOrbit_im, ht]
    · right; right; left
      apply Subtype.ext
      apply Complex.ext
      · dsimp [stripSigma] at hσ
        rw [stripFE_re]
        linarith
      · dsimp [stripGamma] at ht
        rw [stripFE_im, ht]

lemma stripOrbit_distinct
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hσ : stripSigma ρ ≠ 0) (ht : stripGamma ρ ≠ 0) :
    ρ ≠ stripStarEquiv ρ ∧
      ρ ≠ stripFEEquiv ρ ∧
      ρ ≠ stripOrbitEquiv ρ ∧
      stripStarEquiv ρ ≠ stripFEEquiv ρ ∧
      stripStarEquiv ρ ≠ stripOrbitEquiv ρ ∧
      stripFEEquiv ρ ≠ stripOrbitEquiv ρ := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro h
    have := congrArg stripGamma h
    rw [stripStar_gamma] at this
    exact ht (eq_zero_of_eq_neg this)
  · intro h
    have := congrArg stripSigma h
    rw [stripFE_sigma] at this
    exact hσ (eq_zero_of_eq_neg this)
  · intro h
    have := congrArg stripSigma h
    rw [stripOrbit_sigma] at this
    exact hσ (eq_zero_of_eq_neg this)
  · intro h
    have := congrArg stripSigma h
    rw [stripStar_sigma, stripFE_sigma] at this
    exact hσ (eq_zero_of_eq_neg this)
  · intro h
    have := congrArg stripGamma h
    rw [stripStar_gamma, stripOrbit_gamma] at this
    exact ht (eq_zero_of_eq_neg this.symm)
  · intro h
    have := congrArg stripGamma h
    rw [stripFE_gamma, stripOrbit_gamma] at this
    exact ht (eq_zero_of_eq_neg this.symm)

lemma not_mem_orbit_of_ne
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hσ : stripSigma ρ ≠ 0) (ht : stripGamma ρ ≠ 0) :
    ρ ∉ ({stripStarEquiv ρ, stripFEEquiv ρ,
      stripOrbitEquiv ρ} : Finset _) := by
  have h := stripOrbit_distinct hσ ht
  simp [h.1, h.2.1, h.2.2.1]

lemma stripOrbitFinset_sum
    (f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ)
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hσ : stripSigma ρ ≠ 0) (ht : stripGamma ρ ≠ 0) :
    ∑ τ ∈ stripOrbitFinset ρ, f τ =
      f ρ + f (stripStarEquiv ρ) + f (stripFEEquiv ρ) +
        f (stripOrbitEquiv ρ) := by
  have hd := stripOrbit_distinct hσ ht
  have h1 : ρ ∉ ({stripStarEquiv ρ, stripFEEquiv ρ,
      stripOrbitEquiv ρ} : Finset _) := by
    simp [hd.1, hd.2.1, hd.2.2.1]
  have h2 : stripStarEquiv ρ ∉
      ({stripFEEquiv ρ, stripOrbitEquiv ρ} : Finset _) := by
    simp [hd.2.2.2.1, hd.2.2.2.2.1]
  have h3 : stripFEEquiv ρ ∉
      ({stripOrbitEquiv ρ} : Finset _) := by
    simp [hd.2.2.2.2.2]
  rw [stripOrbitFinset, sum_insert h1, sum_insert h2, sum_insert h3,
    sum_singleton]
  abel

lemma stripOrbitFinset_sum_hat
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩)
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (hσ : stripSigma ρ ≠ 0) (ht : stripGamma ρ ≠ 0) :
    ∑ τ ∈ stripOrbitFinset ρ,
        (riemannZetaMultiplicity (τ : ℂ) : ℂ) * gaborHat F τ =
      (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
        (gaborHat F ρ).re := by
  have hsum := stripOrbitFinset_sum
    (fun τ => (riemannZetaMultiplicity (τ : ℂ) : ℂ) * gaborHat F τ)
    hσ ht
  have horbit := gabor_orbit_sum_eq_four_re hF ρ
  rw [hsum]
  convert horbit using 1

/-! ## ¬RH produces an off-critical strip zero -/

lemma Gammaℝ_ne_zero_of_nontrivial {s : ℂ}
    (htriv : ¬∃ n : ℕ, s = -2 * (n + 1)) (hs0 : s ≠ 0) :
    Gammaℝ s ≠ 0 := by
  intro hG
  obtain ⟨n, hn⟩ := Gammaℝ_eq_zero_iff.mp hG
  cases n with
  | zero =>
    apply hs0
    simpa using hn
  | succ k =>
    apply htriv
    refine ⟨k, ?_⟩
    rw [hn]
    push_cast
    ring

lemma not_rh_off_critical (h : ¬RiemannHypothesis) :
    ∃ s : ℂ, riemannZeta s = 0 ∧
      (¬∃ n : ℕ, s = -2 * (n + 1)) ∧ s ≠ 1 ∧ s.re ≠ 1 / 2 := by
  unfold RiemannHypothesis at h
  simpa [not_forall, Classical.not_imp] using h

lemma isCriticalStrip_of_not_RH
    (h : ¬RiemannHypothesis) :
    ∃ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      (ρ : ℂ).re ≠ 1 / 2 := by
  obtain ⟨s, hz, htriv, hpole, hcrit⟩ := not_rh_off_critical h
  have hs0 : s ≠ 0 := by
    intro h0
    rw [h0, riemannZeta_zero] at hz
    norm_num at hz
  have him : s.im ≠ 0 := by
    intro him
    have hsreal : s = (s.re : ℂ) := by
      apply Complex.ext
      · simp
      · simp [him]
    have hz' : riemannZeta (s.re : ℂ) = 0 := by
      rwa [← hsreal]
    rcases lt_trichotomy s.re 0 with hlt | heq | hgt
    · have hG : Gammaℝ s ≠ 0 :=
        Gammaℝ_ne_zero_of_nontrivial htriv hs0
      have hΛ : completedRiemannZeta s = 0 := by
        have hdef := riemannZeta_def_of_ne_zero hs0
        have hzdiv : completedRiemannZeta s / Gammaℝ s = 0 := by
          rwa [hdef] at hz
        exact (div_eq_zero_iff.mp hzdiv).resolve_right hG
      have hΛ1 : completedRiemannZeta (1 - s) = 0 := by
        rw [completedRiemannZeta_one_sub, hΛ]
      have hs1 : 1 - s ≠ 0 := by
        intro h1
        exact hpole (sub_eq_zero.mp h1).symm
      have hre1 : 0 < (1 - s).re := by
        rw [sub_re, one_re]
        linarith
      have hG1 : Gammaℝ (1 - s) ≠ 0 :=
        Gammaℝ_ne_zero_of_re_pos hre1
      have hz1 : riemannZeta (1 - s) = 0 := by
        rw [riemannZeta_def_of_ne_zero hs1, hΛ1, zero_div]
      have hge : (1 : ℝ) ≤ (1 - s).re := by
        rw [sub_re, one_re]
        linarith
      exact riemannZeta_ne_zero_of_one_le_re hge hz1
    · exact (riemannZeta_ne_zero_of_re_eq_zero heq) hz
    · rcases lt_or_ge s.re 1 with hlt1 | hge1
      · exact riemannZeta_ne_zero_of_mem_Ioo hgt hlt1 hz'
      · exact riemannZeta_ne_zero_of_one_le_re hge1 hz
  have hIoo :=
    nontrivialZero_re_mem_Ioo_of_im_ne ⟨hz, htriv, hpole⟩ him
  refine ⟨⟨s, hz, hIoo.1, hIoo.2⟩, hcrit⟩

/-! ## Exposed frequency -/

noncomputable def exposedLeft (t0 σ0 : ℝ) : ℝ :=
  max 0 (|t0| - |σ0| / 2)

noncomputable def exposedRight (t0 σ0 : ℝ) : ℝ :=
  |t0| + |σ0| / 2

lemma exposedLeft_lt_right {t0 σ0 : ℝ} (hσ : σ0 ≠ 0) :
    exposedLeft t0 σ0 < exposedRight t0 σ0 := by
  unfold exposedLeft exposedRight
  have hpos : 0 < |σ0| := abs_pos.mpr hσ
  have hR : 0 < |t0| + |σ0| / 2 :=
    add_pos_of_nonneg_of_pos (abs_nonneg _) (half_pos hpos)
  have hR' : |t0| - |σ0| / 2 < |t0| + |σ0| / 2 := by linarith
  exact max_lt hR hR'

lemma exposed_mem_score_interval {t0 σ0 omega : ℝ}
    (hω : omega ∈ Ioo (exposedLeft t0 σ0) (exposedRight t0 σ0)) :
    abs (|t0| - omega) < |σ0| / 2 := by
  have hL : exposedLeft t0 σ0 < omega := hω.1
  have hR : omega < exposedRight t0 σ0 := hω.2
  have hlo : |t0| - |σ0| / 2 < omega :=
    (le_max_right 0 (|t0| - |σ0| / 2)).trans_lt hL
  have hhi : omega < |t0| + |σ0| / 2 := hR
  rw [abs_lt]
  constructor <;> linarith

noncomputable def scoreTieOmega
    (ρ τ : {z : ℂ // IsCriticalStripZetaZero z}) : ℝ :=
  ((stripSigma τ ^ 2 - stripSigma ρ ^ 2) -
      (|stripGamma τ| ^ 2 - |stripGamma ρ| ^ 2)) /
    (2 * (|stripGamma ρ| - |stripGamma τ|))

lemma gaborScore_eq_iff_tie
    (ρ τ : {z : ℂ // IsCriticalStripZetaZero z}) (omega : ℝ)
    (ht : |stripGamma ρ| ≠ |stripGamma τ|) :
    gaborScore (stripSigma ρ) (stripGamma ρ) omega =
        gaborScore (stripSigma τ) (stripGamma τ) omega ↔
      omega = scoreTieOmega ρ τ := by
  have hsqρ : stripGamma ρ ^ 2 = |stripGamma ρ| ^ 2 := (sq_abs _).symm
  have hsqτ : stripGamma τ ^ 2 = |stripGamma τ| ^ 2 := (sq_abs _).symm
  have hden : (2 : ℝ) * (|stripGamma ρ| - |stripGamma τ|) ≠ 0 :=
    mul_ne_zero (by norm_num) (sub_ne_zero.mpr ht)
  have hdiff :
      gaborScore (stripSigma ρ) (stripGamma ρ) omega -
          gaborScore (stripSigma τ) (stripGamma τ) omega =
        2 * (|stripGamma ρ| - |stripGamma τ|) * omega -
          ((stripSigma τ ^ 2 - stripSigma ρ ^ 2) -
            (|stripGamma τ| ^ 2 - |stripGamma ρ| ^ 2)) := by
    rw [gaborScore_eq, gaborScore_eq, hsqρ, hsqτ]
    ring
  constructor
  · intro heq
    have h0 : 2 * (|stripGamma ρ| - |stripGamma τ|) * omega =
        (stripSigma τ ^ 2 - stripSigma ρ ^ 2) -
          (|stripGamma τ| ^ 2 - |stripGamma ρ| ^ 2) := by
      linarith [hdiff, sub_eq_zero.mpr heq]
    unfold scoreTieOmega
    exact eq_div_of_mul_eq hden (by linarith [h0])
  · intro hω
    have hmul : 2 * (|stripGamma ρ| - |stripGamma τ|) * omega =
        (stripSigma τ ^ 2 - stripSigma ρ ^ 2) -
          (|stripGamma τ| ^ 2 - |stripGamma ρ| ^ 2) := by
      rw [hω]
      unfold scoreTieOmega
      exact mul_div_cancel₀ _ hden
    have h0 :
        gaborScore (stripSigma ρ) (stripGamma ρ) omega -
            gaborScore (stripSigma τ) (stripGamma τ) omega = 0 := by
      linarith [hdiff, hmul]
    exact sub_eq_zero.mp h0

noncomputable def exposedForbidden
    (Z : Finset {z : ℂ // IsCriticalStripZetaZero z}) :
    Finset ℝ :=
  Z.image (fun ρ => |stripGamma ρ|) ∪
    ((Z.product Z).filter
        (fun p => |stripGamma p.1| ≠ |stripGamma p.2|)).image
      (fun p => scoreTieOmega p.1 p.2)

lemma exists_exposed_omega
    (t0 σ0 : ℝ) (hσ : σ0 ≠ 0)
    (Z : Finset {z : ℂ // IsCriticalStripZetaZero z}) :
    ∃ omega, omega ∈ Ioo (exposedLeft t0 σ0) (exposedRight t0 σ0) ∧
      omega ∉ exposedForbidden Z := by
  have hI : (Ioo (exposedLeft t0 σ0) (exposedRight t0 σ0)).Infinite :=
    Ioo_infinite (exposedLeft_lt_right hσ)
  exact hI.exists_notMem_finset (exposedForbidden Z)

/-- Data of an exposed FE/conj orbit at a fixed packet centre `omega`. -/
structure ExposedOrbit where
  ρ : {z : ℂ // IsCriticalStripZetaZero z}
  omega : ℝ
  M : ℝ
  Δ : ℝ
  omega_pos : 0 < omega
  sigma_ne : stripSigma ρ ≠ 0
  gamma_pos : 0 < stripGamma ρ
  M_eq : M = gaborScore (stripSigma ρ) (stripGamma ρ) omega
  M_pos : 0 < M
  d_ne : stripGamma ρ - omega ≠ 0
  Δ_pos : 0 < Δ
  Δ_le_two : Δ ≤ 2 * stripGamma ρ * omega
  rest_le :
    ∀ τ : {z : ℂ // IsCriticalStripZetaZero z},
      τ ∉ stripOrbitFinset ρ →
        gaborScore (stripSigma τ) (stripGamma τ) omega ≤ M - Δ

lemma exposedLeft_nonneg (t0 σ0 : ℝ) : 0 ≤ exposedLeft t0 σ0 :=
  le_max_left _ _

noncomputable def posIm_orbit
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    {z : ℂ // IsCriticalStripZetaZero z} :=
  if 0 < stripGamma ρ then ρ else stripStarEquiv ρ

lemma posIm_orbit_gamma_pos
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    0 < stripGamma (posIm_orbit ρ) := by
  unfold posIm_orbit
  split_ifs with h
  · exact h
  · have hne := stripGamma_ne_zero ρ
    have hle : stripGamma ρ ≤ 0 := le_of_not_gt h
    have hlt : stripGamma ρ < 0 := lt_of_le_of_ne hle hne
    rw [stripStar_gamma]
    linarith

lemma posIm_orbit_sigma
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripSigma (posIm_orbit ρ) = stripSigma ρ := by
  unfold posIm_orbit
  split_ifs
  · rfl
  · exact stripStar_sigma ρ

lemma posIm_orbit_mem
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    posIm_orbit ρ ∈ stripOrbitFinset ρ := by
  unfold posIm_orbit
  split_ifs
  · simp [mem_stripOrbitFinset]
  · simp [mem_stripOrbitFinset]

lemma stripOrbitFinset_star
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripOrbitFinset (stripStarEquiv ρ) = stripOrbitFinset ρ := by
  ext τ
  simp only [mem_stripOrbitFinset]
  have hss : stripStarEquiv (stripStarEquiv ρ) = ρ := by
    apply Subtype.ext
    simp [stripStarEquiv]
  have hfe_star : stripFEEquiv (stripStarEquiv ρ) = stripOrbitEquiv ρ := by
    apply Subtype.ext
    change (1 - star (ρ : ℂ) : ℂ) = 1 - star (ρ : ℂ)
    rfl
  have horb_star : stripOrbitEquiv (stripStarEquiv ρ) = stripFEEquiv ρ := by
    apply Subtype.ext
    change (1 - star (star (ρ : ℂ)) : ℂ) = 1 - (ρ : ℂ)
    simp
  constructor
  · intro h
    rcases h with h | h | h | h
    · rw [h]; exact Or.inr (Or.inl rfl)
    · rw [h, hss]; exact Or.inl rfl
    · rw [h, hfe_star]; exact Or.inr (Or.inr (Or.inr rfl))
    · rw [h, horb_star]; exact Or.inr (Or.inr (Or.inl rfl))
  · intro h
    rcases h with h | h | h | h
    · rw [h]; exact Or.inr (Or.inl hss.symm)
    · rw [h]; exact Or.inl rfl
    · rw [h, ← horb_star]; exact Or.inr (Or.inr (Or.inr rfl))
    · rw [h, ← hfe_star]; exact Or.inr (Or.inr (Or.inl rfl))

lemma stripOrbitFinset_posIm
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    stripOrbitFinset (posIm_orbit ρ) = stripOrbitFinset ρ := by
  unfold posIm_orbit
  split_ifs
  · rfl
  · exact stripOrbitFinset_star ρ

lemma abs_gamma_posIm
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    |stripGamma (posIm_orbit ρ)| = |stripGamma ρ| := by
  unfold posIm_orbit
  split_ifs
  · rfl
  · rw [stripStar_gamma, abs_neg]

lemma scoreTieOmega_same_sigma
    (ρ ρ' τ : {z : ℂ // IsCriticalStripZetaZero z})
    (hσ : stripSigma ρ = stripSigma ρ')
    (ht : |stripGamma ρ| = |stripGamma ρ'|) :
    scoreTieOmega ρ τ = scoreTieOmega ρ' τ := by
  unfold scoreTieOmega
  simp [hσ, ht]

lemma score_eq_of_same_abs_im {ρ τ : {z : ℂ // IsCriticalStripZetaZero z}}
    {omega : ℝ}
    (ht : |stripGamma ρ| = |stripGamma τ|)
    (heq : gaborScore (stripSigma ρ) (stripGamma ρ) omega =
      gaborScore (stripSigma τ) (stripGamma τ) omega) :
    |stripSigma ρ| = |stripSigma τ| := by
  have hA := gaborScore_eq (stripSigma ρ) (stripGamma ρ) omega
  have hB := gaborScore_eq (stripSigma τ) (stripGamma τ) omega
  have ht2 : stripGamma ρ ^ 2 = stripGamma τ ^ 2 := by
    rw [← sq_abs (stripGamma ρ), ← sq_abs (stripGamma τ)]
    exact congrArg (fun x : ℝ => x ^ 2) ht
  have hσ2 : stripSigma ρ ^ 2 = stripSigma τ ^ 2 := by
    rw [hA, hB, ht, ht2] at heq
    linarith
  exact (sq_eq_sq_iff_abs_eq_abs (stripSigma ρ) (stripSigma τ)).mp hσ2

lemma exists_exposedOrbit_of_not_rh
    (h : ¬RiemannHypothesis) : Nonempty ExposedOrbit := by
  obtain ⟨ρ0, hcrit⟩ := isCriticalStrip_of_not_RH h
  have hσ0 : stripSigma ρ0 ≠ 0 := (stripSigma_ne_zero_iff ρ0).mpr hcrit
  set t0 := stripGamma ρ0
  set σ0 := stripSigma ρ0
  set T : ℝ := |t0| + 1
  set Z := stripZerosBelow T
  have hρ0Z : ρ0 ∈ Z := by
    refine mem_stripZerosBelow.mpr ?_
    exact mem_rect_of_criticalStrip ρ0.property (by
      change |stripGamma ρ0| ≤ |stripGamma ρ0| + 1
      linarith [abs_nonneg t0])
  have hZne : Z.Nonempty := ⟨ρ0, hρ0Z⟩
  obtain ⟨omega, hωI, hωf⟩ := exists_exposed_omega t0 σ0 hσ0 Z
  have hω0 : 0 < omega := (exposedLeft_nonneg t0 σ0).trans_lt hωI.1
  obtain ⟨ρm, hρmZ, hmax⟩ :=
    Z.exists_max_image
      (fun ρ => gaborScore (stripSigma ρ) (stripGamma ρ) omega) hZne
  set ρ : {z : ℂ // IsCriticalStripZetaZero z} := posIm_orbit ρm
  have hγpos : 0 < stripGamma ρ := posIm_orbit_gamma_pos ρm
  have hσeq : stripSigma ρ = stripSigma ρm := posIm_orbit_sigma ρm
  have horbEq : stripOrbitFinset ρ = stripOrbitFinset ρm :=
    stripOrbitFinset_posIm ρm
  have hScore :
      gaborScore (stripSigma ρ) (stripGamma ρ) omega =
        gaborScore (stripSigma ρm) (stripGamma ρm) omega :=
    gaborScore_of_orbit_mem ρm omega (posIm_orbit_mem ρm)
  have hnear :
      (3 / 4 : ℝ) * σ0 ^ 2 < gaborScore σ0 t0 omega :=
    gaborScore_near (exposed_mem_score_interval hωI) hσ0
  have hpos0 : 0 < gaborScore σ0 t0 omega :=
    lt_trans (mul_pos (by norm_num) (sq_pos_of_ne_zero hσ0)) hnear
  have hle0 :
      gaborScore σ0 t0 omega ≤
        gaborScore (stripSigma ρm) (stripGamma ρm) omega :=
    hmax ρ0 hρ0Z
  have hMpos : 0 < gaborScore (stripSigma ρ) (stripGamma ρ) omega := by
    linarith [hScore, hle0, hpos0]
  have hσ : stripSigma ρ ≠ 0 := by
    intro hσz
    have : gaborScore (stripSigma ρ) (stripGamma ρ) omega ≤ 0 := by
      rw [hσz]
      exact gaborScore_nonpos_of_sigma_zero _ _
    linarith
  have habsγ : |stripGamma ρ| = |stripGamma ρm| := abs_gamma_posIm ρm
  have hd : stripGamma ρ - omega ≠ 0 := by
    intro hdeq
    have hωabs : omega = |stripGamma ρ| := by
      have : stripGamma ρ = omega := sub_eq_zero.mp hdeq
      rw [abs_of_pos hγpos, this]
    have : omega ∈ exposedForbidden Z := by
      refine mem_union.mpr (Or.inl ?_)
      refine mem_image.mpr ⟨ρm, hρmZ, ?_⟩
      rw [hωabs, habsγ]
    exact hωf this
  have huniq :
      ∀ τ ∈ Z, τ ∉ stripOrbitFinset ρ →
        gaborScore (stripSigma τ) (stripGamma τ) omega <
          gaborScore (stripSigma ρ) (stripGamma ρ) omega := by
    intro τ hτZ hnot
    have hle' :
        gaborScore (stripSigma τ) (stripGamma τ) omega ≤
          gaborScore (stripSigma ρ) (stripGamma ρ) omega := by
      linarith [hmax τ hτZ, hScore]
    refine lt_of_le_of_ne hle' ?_
    intro heq
    by_cases htEq : |stripGamma ρ| = |stripGamma τ|
    · have hσAbs := score_eq_of_same_abs_im htEq heq.symm
      have hin := mem_stripOrbitFinset_of_same_abs hσAbs.symm htEq.symm
      exact hnot hin
    · have hωeq : omega = scoreTieOmega ρ τ :=
        (gaborScore_eq_iff_tie ρ τ omega htEq).mp heq.symm
      have hmem : omega ∈ exposedForbidden Z := by
        refine mem_union.mpr (Or.inr ?_)
        refine mem_image.mpr ⟨(ρm, τ), ?_, ?_⟩
        · refine mem_filter.mpr ⟨mem_product.mpr ⟨hρmZ, hτZ⟩, ?_⟩
          rw [← habsγ]
          exact htEq
        · have := scoreTieOmega_same_sigma ρ ρm τ hσeq habsγ
          rw [← this, ← hωeq]
      exact hωf hmem
  set M := gaborScore (stripSigma ρ) (stripGamma ρ) omega
  set restZ := Z.filter (fun τ => τ ∉ stripOrbitFinset ρ)
  let Δ_win : ℝ :=
    if hne : restZ.Nonempty then
      (restZ.image fun τ =>
          M - gaborScore (stripSigma τ) (stripGamma τ) omega).min'
        (image_nonempty.mpr hne)
    else
      M / 2
  have hΔwin_pos : 0 < Δ_win := by
    dsimp [Δ_win]
    split_ifs with hne
    · have hmem :=
        (restZ.image fun τ =>
            M - gaborScore (stripSigma τ) (stripGamma τ) omega).min'_mem
          (image_nonempty.mpr hne)
      obtain ⟨τ, hτ, hΔeq⟩ := mem_image.mp hmem
      have hτf := mem_filter.mp hτ
      have hlt := huniq τ hτf.1 hτf.2
      have : 0 < M - gaborScore (stripSigma τ) (stripGamma τ) omega :=
        sub_pos.mpr hlt
      rwa [← hΔeq]
    · exact half_pos hMpos
  have htω : 0 < 2 * stripGamma ρ * omega :=
    mul_pos (mul_pos (by norm_num) hγpos) hω0
  set Δ := min Δ_win (min (M / 2) (2 * stripGamma ρ * omega))
  have hΔpos : 0 < Δ :=
    lt_min hΔwin_pos (lt_min (half_pos hMpos) htω)
  have hΔtwo : Δ ≤ 2 * stripGamma ρ * omega :=
    le_trans (min_le_right _ _) (min_le_right _ _)
  have hrest :
      ∀ τ : {z : ℂ // IsCriticalStripZetaZero z},
        τ ∉ stripOrbitFinset ρ →
          gaborScore (stripSigma τ) (stripGamma τ) omega ≤ M - Δ := by
    intro τ hnot
    by_cases hZ : τ ∈ Z
    · have hτrest : τ ∈ restZ := mem_filter.mpr ⟨hZ, hnot⟩
      have hne : restZ.Nonempty := ⟨τ, hτrest⟩
      have hmin : Δ_win ≤
          M - gaborScore (stripSigma τ) (stripGamma τ) omega := by
        have hΔeq' : Δ_win =
            (restZ.image fun σ =>
                M - gaborScore (stripSigma σ) (stripGamma σ) omega).min'
              (image_nonempty.mpr hne) := by
          simp [Δ_win, dif_pos hne]
        rw [hΔeq']
        exact min'_le _ _ (mem_image.mpr ⟨τ, hτrest, rfl⟩)
      have : Δ ≤ Δ_win := min_le_left _ _
      linarith
    · have him : T < |stripGamma τ| := by
        have : ¬ |stripGamma τ| ≤ T := by
          intro hle
          have : τ ∈ Z := mem_stripZerosBelow.mpr
            (mem_rect_of_criticalStrip τ.property (by
              simpa [stripGamma] using hle))
          exact hZ this
        exact not_le.mp this
      have hfar :=
        gaborScore_far (σ := stripSigma τ) (t := stripGamma τ)
          (t0 := t0) (σ0 := σ0) (omega := omega)
          (abs_stripSigma_lt_half τ) (by simpa [T] using him)
          hωI.2 (abs_stripSigma_lt_half ρ0)
      have : Δ ≤ M / 2 :=
        le_trans (min_le_right _ _) (min_le_left _ _)
      linarith [hMpos]
  refine ⟨⟨ρ, omega, M, Δ, hω0, hσ, hγpos, rfl, hMpos, hd, hΔpos, hΔtwo,
    hrest⟩⟩

/-! ## Phase lock on the exposed minus lobe -/

noncomputable def exposedWidth (E : ExposedOrbit) : ℝ :=
  |stripSigma E.ρ * (stripGamma E.ρ - E.omega)|

lemma exposedWidth_pos (E : ExposedOrbit) : 0 < exposedWidth E :=
  abs_pos.mpr (mul_ne_zero E.sigma_ne E.d_ne)

lemma cos_odd_mul_pi (n : ℕ) :
    Real.cos ((2 * n + 1 : ℝ) * Real.pi) = -1 := by
  have hcast : (2 * n + 1 : ℝ) = ((2 * n + 1 : ℕ) : ℝ) := by
    push_cast
    ring
  rw [hcast, Real.cos_nat_mul_pi]
  exact Odd.neg_one_pow (odd_two_mul_add_one n)

noncomputable def exposedPhaseLockA (E : ExposedOrbit) (n : ℕ) : ℝ :=
  exposedWidth E / ((2 * n + 1) * Real.pi)

lemma exposedPhaseLockA_pos (E : ExposedOrbit) (n : ℕ) :
    0 < exposedPhaseLockA E n :=
  div_pos (exposedWidth_pos E)
    (mul_pos (by exact_mod_cast Nat.succ_pos (2 * n)) Real.pi_pos)

lemma exposed_phase_abs_div (E : ExposedOrbit) (n : ℕ) :
    |stripSigma E.ρ * (stripGamma E.ρ - E.omega) /
      exposedPhaseLockA E n| = (2 * n + 1) * Real.pi := by
  have ha := exposedPhaseLockA_pos E n
  have hW := exposedWidth_pos E
  have hπ : 0 < (2 * n + 1 : ℝ) * Real.pi :=
    mul_pos (by exact_mod_cast Nat.succ_pos (2 * n)) Real.pi_pos
  have hcalc :
      stripSigma E.ρ * (stripGamma E.ρ - E.omega) /
          exposedPhaseLockA E n =
        (stripSigma E.ρ * (stripGamma E.ρ - E.omega) *
          ((2 * n + 1) * Real.pi)) / exposedWidth E := by
    unfold exposedPhaseLockA
    field_simp [ha.ne', hπ.ne']
  rw [hcalc, abs_div, abs_mul, abs_of_pos hπ, abs_of_pos hW]
  unfold exposedWidth at hW ⊢
  field_simp [ne_of_gt hW]

lemma exposed_minus_lobe_cos (E : ExposedOrbit) (n : ℕ) :
    Real.cos (stripSigma E.ρ * (stripGamma E.ρ - E.omega) /
      exposedPhaseLockA E n) = -1 := by
  have habs := exposed_phase_abs_div E n
  have hx : stripSigma E.ρ * (stripGamma E.ρ - E.omega) /
      exposedPhaseLockA E n =
      (2 * n + 1) * Real.pi ∨
      stripSigma E.ρ * (stripGamma E.ρ - E.omega) /
        exposedPhaseLockA E n =
        -((2 * n + 1) * Real.pi) :=
    eq_or_eq_neg_of_abs_eq habs
  rcases hx with hx | hx
  · rw [hx, cos_odd_mul_pi]
  · rw [hx, Real.cos_neg, cos_odd_mul_pi]

lemma strip_delta_re (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ((ρ : ℂ) - (1 / 2 : ℂ)).re = stripSigma ρ := by
  simp [stripSigma, sub_re]

lemma strip_delta_im (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ((ρ : ℂ) - (1 / 2 : ℂ)).im = stripGamma ρ := by
  simp [stripGamma, sub_im]

lemma gaborHatThreeLobeConst_add_half (a σ : ℝ) :
    gaborHatThreeLobeConst a (σ + 1 / 2) =
      Real.pi / (4 * a) * Real.exp (σ ^ 2 / (2 * a)) := by
  unfold gaborHatThreeLobeConst
  simp

lemma four_mul_pi_div_four_a {a : ℝ} (ha : a ≠ 0) :
    (4 : ℝ) * (Real.pi / (4 * a)) = Real.pi / a := by
  field_simp [ha]

lemma gaborHatThreeLobe_eq_lobe_exps
    (a omega σ t : ℝ) (ha : 0 < a) :
    gaborHatThreeLobeConst a (σ + 1 / 2) * gaborThreeLobe a omega t =
      Real.pi / (4 * a) *
        (Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) +
          Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a))) := by
  have hden : (2 * a) ≠ 0 := by positivity
  rw [gaborHatThreeLobeConst_add_half]
  unfold gaborThreeLobe
  have h1 :
      Real.exp (σ ^ 2 / (2 * a)) * Real.exp (-(t - omega) ^ 2 / (2 * a)) =
        Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [hden]
    ring
  have h2 :
      Real.exp (σ ^ 2 / (2 * a)) * Real.exp (-(t + omega) ^ 2 / (2 * a)) =
        Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [hden]
    ring
  have h3 :
      Real.exp (σ ^ 2 / (2 * a)) *
          Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)) =
        Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [hden]
    ring
  calc
    Real.pi / (4 * a) * Real.exp (σ ^ 2 / (2 * a)) *
        (Real.exp (-(t - omega) ^ 2 / (2 * a)) +
          Real.exp (-(t + omega) ^ 2 / (2 * a)) +
          2 * Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a))) =
      Real.pi / (4 * a) *
        (Real.exp (σ ^ 2 / (2 * a)) *
            Real.exp (-(t - omega) ^ 2 / (2 * a)) +
          Real.exp (σ ^ 2 / (2 * a)) *
            Real.exp (-(t + omega) ^ 2 / (2 * a)) +
          2 * (Real.exp (σ ^ 2 / (2 * a)) *
            Real.exp (-(t ^ 2 + omega ^ 2) / (2 * a)))) := by
      ring
    _ = Real.pi / (4 * a) *
        (Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) +
          Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a))) := by
      rw [h1, h2, h3]

lemma gaborHatThreeLobe_le_score
    (a omega σ t : ℝ) (ha : 0 < a) (hω : 0 ≤ omega) :
    gaborHatThreeLobeConst a (σ + 1 / 2) * gaborThreeLobe a omega t ≤
      (Real.pi / a) *
        Real.exp (gaborScore σ t omega / (2 * a)) := by
  have hden : 0 < 2 * a := by positivity
  have hπa : 0 < Real.pi / (4 * a) :=
    div_pos Real.pi_pos (by positivity)
  have hm := minus_lobe_num_le_score σ t omega hω
  have hp := plus_lobe_num_le_score σ t omega hω
  have hc := center_lobe_num_le_score σ t omega hω
  have hme : Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) ≤
      Real.exp (gaborScore σ t omega / (2 * a)) :=
    Real.exp_le_exp.mpr (div_le_div_of_nonneg_right hm hden.le)
  have hpe : Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) ≤
      Real.exp (gaborScore σ t omega / (2 * a)) :=
    Real.exp_le_exp.mpr (div_le_div_of_nonneg_right hp hden.le)
  have hce : Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)) ≤
      Real.exp (gaborScore σ t omega / (2 * a)) :=
    Real.exp_le_exp.mpr (div_le_div_of_nonneg_right hc hden.le)
  have hsum :
      Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) +
          Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)) ≤
        (4 : ℝ) * Real.exp (gaborScore σ t omega / (2 * a)) := by
    nlinarith [Real.exp_pos ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)),
      Real.exp_pos ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)),
      Real.exp_pos ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a)),
      hme, hpe, hce]
  have hrew := gaborHatThreeLobe_eq_lobe_exps a omega σ t ha
  have h4 := four_mul_pi_div_four_a (ne_of_gt ha)
  calc
    gaborHatThreeLobeConst a (σ + 1 / 2) * gaborThreeLobe a omega t =
        Real.pi / (4 * a) *
          (Real.exp ((σ ^ 2 - (t - omega) ^ 2) / (2 * a)) +
            Real.exp ((σ ^ 2 - (t + omega) ^ 2) / (2 * a)) +
            2 * Real.exp ((σ ^ 2 - t ^ 2 - omega ^ 2) / (2 * a))) := hrew
    _ ≤ Real.pi / (4 * a) *
          ((4 : ℝ) * Real.exp (gaborScore σ t omega / (2 * a))) :=
      mul_le_mul_of_nonneg_left hsum hπa.le
    _ = (4 * (Real.pi / (4 * a))) *
          Real.exp (gaborScore σ t omega / (2 * a)) := by ring
    _ = (Real.pi / a) * Real.exp (gaborScore σ t omega / (2 * a)) := by
      rw [h4]

lemma norm_pureGaborHatDelta_le_score
    (a omega : ℝ) (ha : 0 < a) (hω : 0 ≤ omega) (δ : ℂ) :
    ‖pureGaborHatDelta a omega δ‖ ≤
      (Real.pi / a) *
        Real.exp (gaborScore δ.re δ.im omega / (2 * a)) := by
  have htri := norm_pureGaborHatDelta_le_three_lobe a omega ha δ
  have hsc := gaborHatThreeLobe_le_score a omega δ.re δ.im ha hω
  exact htri.trans hsc

lemma norm_gaborHat_pure_le_score
    {a omega : ℝ} (ha : 0 < a) (hω : 0 ≤ omega)
    (τ : {z : ℂ // IsCriticalStripZetaZero z}) :
    ‖gaborHat (pureGaborTest a omega ha) (τ : ℂ)‖ ≤
      (Real.pi / a) *
        Real.exp (gaborScore (stripSigma τ) (stripGamma τ) omega /
          (2 * a)) := by
  have hF : (pureGaborTest a omega ha).coeffs = ⟨1, 0, 0⟩ := rfl
  rw [gaborHat_of_pure hF]
  simp only [pureGaborTest]
  have h :=
    norm_pureGaborHatDelta_le_score a omega ha hω ((τ : ℂ) - (1 / 2 : ℂ))
  rw [strip_delta_re, strip_delta_im] at h
  exact h

lemma plus_lobe_num_le_M_sub_Δ (E : ExposedOrbit) :
    stripSigma E.ρ ^ 2 - (stripGamma E.ρ + E.omega) ^ 2 ≤
      E.M - E.Δ := by
  have ht : 0 ≤ stripGamma E.ρ := le_of_lt E.gamma_pos
  have hplus := plus_lobe_num_eq_score_sub_four
    (stripSigma E.ρ) (stripGamma E.ρ) E.omega ht
  have h4 : 4 * stripGamma E.ρ * E.omega ≥ E.Δ := by
    have : (2 : ℝ) * (2 * stripGamma E.ρ * E.omega) =
        4 * stripGamma E.ρ * E.omega := by ring
    have h2 : (2 : ℝ) * (2 * stripGamma E.ρ * E.omega) ≥ 2 * E.Δ :=
      mul_le_mul_of_nonneg_left E.Δ_le_two (by norm_num)
    linarith [E.Δ_pos]
  calc
    stripSigma E.ρ ^ 2 - (stripGamma E.ρ + E.omega) ^ 2 =
        gaborScore (stripSigma E.ρ) (stripGamma E.ρ) E.omega -
          4 * stripGamma E.ρ * E.omega := hplus
    _ = E.M - 4 * stripGamma E.ρ * E.omega := by rw [E.M_eq]
    _ ≤ E.M - E.Δ := by linarith

lemma center_lobe_num_le_M_sub_Δ (E : ExposedOrbit) :
    stripSigma E.ρ ^ 2 - stripGamma E.ρ ^ 2 - E.omega ^ 2 ≤
      E.M - E.Δ := by
  have ht : 0 ≤ stripGamma E.ρ := le_of_lt E.gamma_pos
  have hcen := center_lobe_num_eq_score_sub_two
    (stripSigma E.ρ) (stripGamma E.ρ) E.omega ht
  calc
    stripSigma E.ρ ^ 2 - stripGamma E.ρ ^ 2 - E.omega ^ 2 =
        gaborScore (stripSigma E.ρ) (stripGamma E.ρ) E.omega -
          2 * stripGamma E.ρ * E.omega := hcen
    _ = E.M - 2 * stripGamma E.ρ * E.omega := by rw [E.M_eq]
    _ ≤ E.M - E.Δ := by linarith [E.Δ_le_two]

lemma minus_lobe_num_eq_M (E : ExposedOrbit) :
    stripSigma E.ρ ^ 2 - (stripGamma E.ρ - E.omega) ^ 2 = E.M := by
  have ht : 0 ≤ stripGamma E.ρ := le_of_lt E.gamma_pos
  rw [minus_lobe_num_eq_score_of_nonneg_im _ _ _ ht, E.M_eq]

lemma re_gaborHat_exposed_le (E : ExposedOrbit) (n : ℕ) :
    (gaborHat (pureGaborTest (exposedPhaseLockA E n) E.omega
        (exposedPhaseLockA_pos E n)) (E.ρ : ℂ)).re ≤
      -(Real.pi / (4 * exposedPhaseLockA E n)) *
          Real.exp (E.M / (2 * exposedPhaseLockA E n)) +
        (3 * Real.pi / (4 * exposedPhaseLockA E n)) *
          Real.exp ((E.M - E.Δ) / (2 * exposedPhaseLockA E n)) := by
  set a := exposedPhaseLockA E n
  have ha : 0 < a := exposedPhaseLockA_pos E n
  have hF : (pureGaborTest a E.omega ha).coeffs = ⟨1, 0, 0⟩ := rfl
  rw [gaborHat_of_pure hF]
  simp only [pureGaborTest]
  rw [re_pureGaborHatDelta a E.omega ha, strip_delta_re, strip_delta_im]
  set σ := stripSigma E.ρ
  set t := stripGamma E.ρ
  set ω := E.omega
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hπ : 0 < Real.pi / (4 * a) :=
    div_pos Real.pi_pos (by positivity)
  have hminus : σ ^ 2 - (t - ω) ^ 2 = E.M := minus_lobe_num_eq_M E
  have hcos := exposed_minus_lobe_cos E n
  have hpe :
      Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) ≤
        Real.exp ((E.M - E.Δ) / (2 * a)) :=
    Real.exp_le_exp.mpr
      (div_le_div_of_nonneg_right (plus_lobe_num_le_M_sub_Δ E) hden.le)
  have hce :
      Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) ≤
        Real.exp ((E.M - E.Δ) / (2 * a)) :=
    Real.exp_le_exp.mpr
      (div_le_div_of_nonneg_right (center_lobe_num_le_M_sub_Δ E) hden.le)
  have habs_cos (θ : ℝ) : |Real.cos θ| ≤ 1 := Real.abs_cos_le_one θ
  have hrest :
      |Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
            Real.cos (σ * (t + ω) / a) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
            Real.cos (σ * t / a)| ≤
        3 * Real.exp ((E.M - E.Δ) / (2 * a)) := by
    have h1 : |Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
          Real.cos (σ * (t + ω) / a)| ≤
        Real.exp ((E.M - E.Δ) / (2 * a)) := by
      rw [abs_mul, abs_of_pos (Real.exp_pos _)]
      exact (mul_le_of_le_one_right (Real.exp_pos _).le
        (habs_cos _)).trans hpe
    have h2 : |2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
          Real.cos (σ * t / a)| ≤
        2 * Real.exp ((E.M - E.Δ) / (2 * a)) := by
      rw [abs_mul, abs_mul, abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 2),
        abs_of_pos (Real.exp_pos _)]
      have : Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
          |Real.cos (σ * t / a)| ≤
          Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) :=
        mul_le_of_le_one_right (Real.exp_pos _).le (habs_cos _)
      nlinarith [hce, this]
    have htri := abs_add_le
      (Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
        Real.cos (σ * (t + ω) / a))
      (2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
        Real.cos (σ * t / a))
    nlinarith [htri, h1, h2]
  have hlead :
      Real.exp ((σ ^ 2 - (t - ω) ^ 2) / (2 * a)) *
          Real.cos (σ * (t - ω) / a) =
        -Real.exp (E.M / (2 * a)) := by
    rw [hminus, hcos]
    ring
  have hdecomp :
      Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
            Real.cos (σ * (t + ω) / a) +
          Real.exp ((σ ^ 2 - (t - ω) ^ 2) / (2 * a)) *
            Real.cos (σ * (t - ω) / a) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
            Real.cos (σ * t / a) =
        -Real.exp (E.M / (2 * a)) +
          (Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
              Real.cos (σ * (t + ω) / a) +
            2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
              Real.cos (σ * t / a)) := by
    rw [hlead]
    ring
  have hx :
      Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
            Real.cos (σ * (t + ω) / a) +
          Real.exp ((σ ^ 2 - (t - ω) ^ 2) / (2 * a)) *
            Real.cos (σ * (t - ω) / a) +
          2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
            Real.cos (σ * t / a) ≤
        -Real.exp (E.M / (2 * a)) +
          3 * Real.exp ((E.M - E.Δ) / (2 * a)) := by
    rw [hdecomp]
    have hxle := le_abs_self
      (Real.exp ((σ ^ 2 - (t + ω) ^ 2) / (2 * a)) *
          Real.cos (σ * (t + ω) / a) +
        2 * Real.exp ((σ ^ 2 - t ^ 2 - ω ^ 2) / (2 * a)) *
          Real.cos (σ * t / a))
    linarith [hxle, hrest]
  have hscaled := mul_le_mul_of_nonneg_left hx hπ.le
  have hrhs :
      Real.pi / (4 * a) *
          (-Real.exp (E.M / (2 * a)) +
            3 * Real.exp ((E.M - E.Δ) / (2 * a))) =
        -(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
          (3 * Real.pi / (4 * a)) *
            Real.exp ((E.M - E.Δ) / (2 * a)) := by ring
  change _ ≤
      -(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
        (3 * Real.pi / (4 * a)) *
          Real.exp ((E.M - E.Δ) / (2 * a))
  exact hscaled.trans_eq hrhs

lemma gaborScore_div_two_le_gauss (σ t omega : ℝ)
    (hσ : σ ^ 2 ≤ (1 / 4 : ℝ)) :
    gaborScore σ t omega / 2 ≤
      (1 / 8 : ℝ) + omega ^ 2 / 2 - t ^ 2 / 4 := by
  have hsq := abs_sub_sq_ge_half_sq t omega
  unfold gaborScore
  linarith

lemma summable_exposedScoreWeight (omega : ℝ) :
    Summable fun τ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
        Real.exp (gaborScore (stripSigma τ) (stripGamma τ) omega / 2) := by
  have hc : (0 : ℝ) < 1 / 4 := by norm_num
  obtain ⟨K, hK0, hK⟩ := one_add_log_mul_gauss_le_local hc
  set Cm : ℝ :=
    zetaZerosInDiskCardBoundInner +
      ∑ ρ ∈ riemannZetaZerosOnClosedRect 0 1 2,
        (riemannZetaMultiplicity ρ : ℝ)
  have hCm0 : 0 < Cm :=
    lt_of_lt_of_le zetaZerosInDiskCardBoundInner_pos
      (le_add_of_nonneg_right
        (Finset.sum_nonneg fun _ _ => Nat.cast_nonneg _))
  set Cω : ℝ := Real.exp ((1 / 8 : ℝ) + omega ^ 2 / 2)
  have hCω0 : 0 ≤ Cω := (Real.exp_pos _).le
  have hbd : ∀ τ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          Real.exp (gaborScore (stripSigma τ) (stripGamma τ) omega / 2) ≤
        (Cm * Cω * K) *
          Real.exp (-((1 / 4 : ℝ) / 2) * (τ : ℂ).im ^ 2) := by
    intro τ
    have hσ2 : stripSigma τ ^ 2 ≤ (1 / 4 : ℝ) :=
      le_of_lt (sigma_sq_lt_quarter τ)
    have hsc := gaborScore_div_two_le_gauss (stripSigma τ)
      (stripGamma τ) omega hσ2
    have hexp :
        Real.exp (gaborScore (stripSigma τ) (stripGamma τ) omega / 2) ≤
          Cω * Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2) := by
      have hsum :
          gaborScore (stripSigma τ) (stripGamma τ) omega / 2 ≤
            ((1 / 8 : ℝ) + omega ^ 2 / 2) +
              (-(1 / 4 : ℝ) * stripGamma τ ^ 2) := by
        unfold stripGamma at hsc ⊢
        linarith [hsc]
      have := Real.exp_le_exp.mpr hsum
      rw [Real.exp_add] at this
      simpa [Cω, stripGamma] using this
    have hm := riemannZetaMultiplicity_le_log_all_local τ.property
    have hlog := hK (τ : ℂ).im
    have hmlin :
        (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2) ≤
          Cm * K * Real.exp (-((1 / 4 : ℝ) / 2) * (τ : ℂ).im ^ 2) := by
      set e : ℝ := Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2)
      have he0 : 0 ≤ e := (Real.exp_pos _).le
      have h1 :
          (riemannZetaMultiplicity (τ : ℂ) : ℝ) * e ≤
            Cm * (1 + Real.log (2 + |(τ : ℂ).im| + 5 / 4)) * e :=
        mul_le_mul_of_nonneg_right hm he0
      have h2 :
          Cm * (1 + Real.log (2 + |(τ : ℂ).im| + 5 / 4)) * e ≤
            Cm * (K * Real.exp (-((1 / 4 : ℝ) / 2) * (τ : ℂ).im ^ 2)) := by
        have := mul_le_mul_of_nonneg_left hlog (le_of_lt hCm0)
        simpa [e, mul_assoc] using this
      exact (h1.trans h2).trans_eq (by ring)
    have hprod :
        (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            Real.exp (gaborScore (stripSigma τ) (stripGamma τ) omega / 2) ≤
          (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            (Cω * Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2)) :=
      mul_le_mul_of_nonneg_left hexp
        (Nat.cast_nonneg (riemannZetaMultiplicity (τ : ℂ)))
    have hrearr :
        (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            (Cω * Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2)) =
          Cω * ((riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            Real.exp (-(1 / 4 : ℝ) * (τ : ℂ).im ^ 2)) := by ring
    have hfin := (hprod.trans_eq hrearr).trans
      (mul_le_mul_of_nonneg_left hmlin hCω0)
    convert hfin using 1
    ring
  refine Summable.of_nonneg_of_le
    (fun _ => mul_nonneg (Nat.cast_nonneg _) (Real.exp_pos _).le) hbd
    ((summable_gauss_over_zeros (half_pos hc)).mul_left (Cm * Cω * K))

lemma summable_exposedRestWeight (E : ExposedOrbit) :
    Summable fun τ : {z : ℂ // IsCriticalStripZetaZero z} =>
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
        Real.exp
          ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
            (E.M - E.Δ)) / 2) := by
  have hbase := summable_exposedScoreWeight E.omega
  refine (hbase.mul_left (Real.exp (-(E.M - E.Δ) / 2))).congr fun τ => ?_
  have hsplit :
      (gaborScore (stripSigma τ) (stripGamma τ) E.omega - (E.M - E.Δ)) / 2 =
        gaborScore (stripSigma τ) (stripGamma τ) E.omega / 2 +
          (-(E.M - E.Δ) / 2) := by ring
  rw [hsplit, Real.exp_add]
  ring

lemma div_two_a_le_half {a x : ℝ} (ha : 0 < a) (ha1 : a ≤ 1)
    (hx : x ≤ 0) : x / (2 * a) ≤ x / 2 := by
  have h2 : (0 : ℝ) < 2 := by norm_num
  have h2a : 0 < 2 * a := mul_pos h2 ha
  have h2ale : 2 * a ≤ 2 := by nlinarith
  have hinv : (1 : ℝ) / 2 ≤ 1 / (2 * a) :=
    one_div_le_one_div_of_le h2a h2ale
  have := mul_le_mul_of_nonpos_left hinv hx
  simpa [div_eq_mul_inv, one_div] using this

lemma gaborZeroSide_eq_orbit_add_tail
    {a omega : ℝ} (ha : 0 < a)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    gaborZeroSide (pureGaborTest a omega ha) =
      (∑ τ ∈ stripOrbitFinset ρ,
          (riemannZetaMultiplicity (τ : ℂ) : ℂ) *
            gaborHat (pureGaborTest a omega ha) τ).re +
        (∑' τ : {τ // τ ∉ stripOrbitFinset ρ},
          (riemannZetaMultiplicity (τ : ℂ) : ℂ) *
            gaborHat (pureGaborTest a omega ha) τ).re := by
  set F := pureGaborTest a omega ha
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun τ => (riemannZetaMultiplicity (τ : ℂ) : ℂ) * gaborHat F τ
  have hsm : Summable f := gaborMultiplicityWeightedHatSummable F rfl
  have hsplit := hsm.sum_add_tsum_subtype_compl (stripOrbitFinset ρ)
  unfold gaborZeroSide
  change (∑' τ, f τ).re = (∑ τ ∈ stripOrbitFinset ρ, f τ).re +
      (∑' τ : {τ // τ ∉ stripOrbitFinset ρ}, f τ).re
  rw [← hsplit, Complex.add_re]

lemma re_four_mul_nat_mul_re (m : ℕ) (z : ℂ) :
    ((4 : ℂ) * (m : ℂ) * z.re).re = 4 * (m : ℝ) * z.re := by
  simp

lemma four_mul_three_pi_div_four {a : ℝ} (ha : a ≠ 0) :
    (4 : ℝ) * (3 * Real.pi / (4 * a)) = 3 * Real.pi / a := by
  field_simp [ha]

lemma orbit_re_le_exposed (E : ExposedOrbit) (n : ℕ) :
    (∑ τ ∈ stripOrbitFinset E.ρ,
        (riemannZetaMultiplicity (τ : ℂ) : ℂ) *
          gaborHat (pureGaborTest (exposedPhaseLockA E n) E.omega
            (exposedPhaseLockA_pos E n)) τ).re ≤
      -(Real.pi / exposedPhaseLockA E n) *
          (riemannZetaMultiplicity (E.ρ : ℂ) : ℝ) *
          Real.exp (E.M / (2 * exposedPhaseLockA E n)) +
        (3 * Real.pi / exposedPhaseLockA E n) *
          (riemannZetaMultiplicity (E.ρ : ℂ) : ℝ) *
          Real.exp ((E.M - E.Δ) / (2 * exposedPhaseLockA E n)) := by
  set a := exposedPhaseLockA E n
  have ha : 0 < a := exposedPhaseLockA_pos E n
  set F := pureGaborTest a E.omega ha
  have hF : F.coeffs = ⟨1, 0, 0⟩ := rfl
  have ht : stripGamma E.ρ ≠ 0 := ne_of_gt E.gamma_pos
  have hsum := stripOrbitFinset_sum_hat (F := F) hF E.sigma_ne ht
  have hre := re_gaborHat_exposed_le E n
  set m := riemannZetaMultiplicity (E.ρ : ℂ)
  have hm0 : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
  have h4 := re_four_mul_nat_mul_re m (gaborHat F (E.ρ : ℂ))
  have hmul :
      4 * (m : ℝ) * (gaborHat F (E.ρ : ℂ)).re ≤
        4 * (m : ℝ) *
          (-(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
            (3 * Real.pi / (4 * a)) *
              Real.exp ((E.M - E.Δ) / (2 * a))) :=
    mul_le_mul_of_nonneg_left hre (mul_nonneg (by norm_num) hm0)
  have hπ4 := four_mul_pi_div_four_a (ne_of_gt ha)
  have hπ3 := four_mul_three_pi_div_four (ne_of_gt ha)
  have halg :
      4 * (m : ℝ) *
          (-(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
            (3 * Real.pi / (4 * a)) *
              Real.exp ((E.M - E.Δ) / (2 * a))) =
        -(Real.pi / a) * (m : ℝ) * Real.exp (E.M / (2 * a)) +
          (3 * Real.pi / a) * (m : ℝ) *
            Real.exp ((E.M - E.Δ) / (2 * a)) := by
    calc
      4 * (m : ℝ) *
            (-(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
              (3 * Real.pi / (4 * a)) *
                Real.exp ((E.M - E.Δ) / (2 * a))) =
          -(4 * (Real.pi / (4 * a))) * (m : ℝ) *
              Real.exp (E.M / (2 * a)) +
            (4 * (3 * Real.pi / (4 * a))) * (m : ℝ) *
              Real.exp ((E.M - E.Δ) / (2 * a)) := by ring
      _ = -(Real.pi / a) * (m : ℝ) * Real.exp (E.M / (2 * a)) +
            (3 * Real.pi / a) * (m : ℝ) *
              Real.exp ((E.M - E.Δ) / (2 * a)) := by
        rw [hπ4, hπ3]
  change _ ≤
      -(Real.pi / a) * (m : ℝ) * Real.exp (E.M / (2 * a)) +
        (3 * Real.pi / a) * (m : ℝ) *
          Real.exp ((E.M - E.Δ) / (2 * a))
  calc
    (∑ τ ∈ stripOrbitFinset E.ρ,
          (riemannZetaMultiplicity (τ : ℂ) : ℂ) * gaborHat F τ).re =
        ((4 : ℂ) * (m : ℂ) * (gaborHat F (E.ρ : ℂ)).re).re := by
      rw [hsum]
    _ = 4 * (m : ℝ) * (gaborHat F (E.ρ : ℂ)).re := h4
    _ ≤ 4 * (m : ℝ) *
          (-(Real.pi / (4 * a)) * Real.exp (E.M / (2 * a)) +
            (3 * Real.pi / (4 * a)) *
              Real.exp ((E.M - E.Δ) / (2 * a))) := hmul
    _ = -(Real.pi / a) * (m : ℝ) * Real.exp (E.M / (2 * a)) +
          (3 * Real.pi / a) * (m : ℝ) *
            Real.exp ((E.M - E.Δ) / (2 * a)) := halg

lemma tail_norm_le_restWeight
    (E : ExposedOrbit) {a : ℝ} (ha : 0 < a) (ha1 : a ≤ 1)
    (τ : {z : ℂ // IsCriticalStripZetaZero z})
    (hτ : τ ∉ stripOrbitFinset E.ρ) :
    ‖(riemannZetaMultiplicity (τ : ℂ) : ℂ) *
        gaborHat (pureGaborTest a E.omega ha) (τ : ℂ)‖ ≤
      (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a)) *
        ((riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          Real.exp
            ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
              (E.M - E.Δ)) / 2)) := by
  have hω : 0 ≤ E.omega := le_of_lt E.omega_pos
  have hn := norm_gaborHat_pure_le_score ha hω τ
  have hnorm :
      ‖(riemannZetaMultiplicity (τ : ℂ) : ℂ) *
          gaborHat (pureGaborTest a E.omega ha) (τ : ℂ)‖ =
        (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          ‖gaborHat (pureGaborTest a E.omega ha) (τ : ℂ)‖ := by
    rw [norm_mul]; simp
  have hx :
      gaborScore (stripSigma τ) (stripGamma τ) E.omega - (E.M - E.Δ) ≤ 0 :=
    sub_nonpos.mpr (E.rest_le τ hτ)
  have hexp := Real.exp_le_exp.mpr (div_two_a_le_half ha ha1 hx)
  have hπ : 0 ≤ Real.pi / a := div_nonneg Real.pi_pos.le ha.le
  have hrew :
      gaborScore (stripSigma τ) (stripGamma τ) E.omega / (2 * a) =
        (E.M - E.Δ) / (2 * a) +
          (gaborScore (stripSigma τ) (stripGamma τ) E.omega - (E.M - E.Δ)) /
            (2 * a) := by ring
  rw [hnorm]
  have hmul :
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          ‖gaborHat (pureGaborTest a E.omega ha) (τ : ℂ)‖ ≤
        (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          ((Real.pi / a) *
            Real.exp (gaborScore (stripSigma τ) (stripGamma τ) E.omega /
              (2 * a))) :=
    mul_le_mul_of_nonneg_left hn
      (Nat.cast_nonneg (riemannZetaMultiplicity (τ : ℂ)))
  have hrearr :
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
          ((Real.pi / a) *
            Real.exp (gaborScore (stripSigma τ) (stripGamma τ) E.omega /
              (2 * a))) =
        (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a)) *
          ((riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            Real.exp
              ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
                (E.M - E.Δ)) / (2 * a))) := by
    rw [hrew, Real.exp_add]
    ring
  refine (hmul.trans_eq hrearr).trans ?_
  refine mul_le_mul_of_nonneg_left ?_ (mul_nonneg hπ (Real.exp_pos _).le)
  exact mul_le_mul_of_nonneg_left hexp
    (Nat.cast_nonneg (riemannZetaMultiplicity (τ : ℂ)))

lemma tail_re_le_exposed (E : ExposedOrbit) {a : ℝ} (ha : 0 < a)
    (ha1 : a ≤ 1) :
    (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ},
        (riemannZetaMultiplicity (τ : ℂ) : ℂ) *
          gaborHat (pureGaborTest a E.omega ha) τ).re ≤
      (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a)) *
        ∑' τ : {z : ℂ // IsCriticalStripZetaZero z},
          (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
            Real.exp
              ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
                (E.M - E.Δ)) / 2) := by
  set F := pureGaborTest a E.omega ha
  set f : {z : ℂ // IsCriticalStripZetaZero z} → ℂ :=
    fun τ => (riemannZetaMultiplicity (τ : ℂ) : ℂ) * gaborHat F τ
  set w : {z : ℂ // IsCriticalStripZetaZero z} → ℝ :=
    fun τ =>
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
        Real.exp
          ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
            (E.M - E.Δ)) / 2)
  have hsm : Summable f := gaborMultiplicityWeightedHatSummable F rfl
  have hw : Summable w := summable_exposedRestWeight E
  have hπ : 0 ≤ Real.pi / a := div_nonneg Real.pi_pos.le ha.le
  set C : ℝ := (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a))
  have hC0 : 0 ≤ C := mul_nonneg hπ (Real.exp_pos _).le
  have htail : Summable fun τ : {τ // τ ∉ stripOrbitFinset E.ρ} => f ↑τ :=
    hsm.subtype {τ | τ ∉ stripOrbitFinset E.ρ}
  have hnorm : Summable fun τ : {τ // τ ∉ stripOrbitFinset E.ρ} => ‖f ↑τ‖ :=
    htail.norm
  have hre :
      (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, f ↑τ).re ≤
        ‖∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, f ↑τ‖ :=
    (le_abs_self _).trans (Complex.abs_re_le_norm _)
  have hnts :=
    norm_tsum_le_tsum_norm
      (f := fun τ : {τ // τ ∉ stripOrbitFinset E.ρ} => f ↑τ) hnorm
  have hpt : ∀ τ : {τ // τ ∉ stripOrbitFinset E.ρ}, ‖f ↑τ‖ ≤ C * w ↑τ := by
    intro τ
    simpa [f, F, C, w] using
      tail_norm_le_restWeight E ha ha1 (τ : _) τ.property
  have hwsub : Summable fun τ : {τ // τ ∉ stripOrbitFinset E.ρ} => w ↑τ :=
    hw.subtype {τ | τ ∉ stripOrbitFinset E.ρ}
  have hcmp :
      (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, ‖f ↑τ‖) ≤
        ∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, C * w ↑τ :=
    hnorm.tsum_le_tsum hpt (hwsub.mul_left C)
  have hsub :
      (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, w ↑τ) ≤
        ∑' τ : {z : ℂ // IsCriticalStripZetaZero z}, w τ :=
    Summable.tsum_subtype_le w {τ | τ ∉ stripOrbitFinset E.ρ}
      (fun _ => mul_nonneg (Nat.cast_nonneg _) (Real.exp_pos _).le) hw
  have hCtsum :
      (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, C * w ↑τ) =
        C * ∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, w ↑τ :=
    hwsub.tsum_mul_left C
  have hbound :
      (∑' τ : {τ // τ ∉ stripOrbitFinset E.ρ}, f ↑τ).re ≤
        C * ∑' τ : {z : ℂ // IsCriticalStripZetaZero z}, w τ := by
    have := (hre.trans hnts).trans (hcmp.trans_eq hCtsum)
    exact this.trans (mul_le_mul_of_nonneg_left hsub hC0)
  simpa [C, w, F, f] using hbound

lemma exists_exposedPhaseLockA_small (E : ExposedOrbit) {C : ℝ}
    (hC : 0 < C) :
    ∃ n : ℕ, exposedPhaseLockA E n ≤ 1 ∧
      Real.exp (-E.Δ / (2 * exposedPhaseLockA E n)) < C := by
  set W := exposedWidth E
  have hW : 0 < W := exposedWidth_pos E
  have hπ : 0 < Real.pi := Real.pi_pos
  have hΔ : 0 < E.Δ := E.Δ_pos
  set L : ℝ := max 0 (-Real.log C)
  set bound : ℝ :=
    max (W / Real.pi) ((2 * W * L) / (E.Δ * Real.pi))
  have hbound0 : 0 < bound :=
    lt_of_lt_of_le (div_pos hW hπ) (le_max_left _ _)
  obtain ⟨n, hn⟩ := exists_nat_gt bound
  have h2n : (2 * n + 1 : ℝ) > bound := by
    have : (2 * n + 1 : ℝ) = 2 * (n : ℝ) + 1 := by push_cast; ring
    nlinarith [hn, hbound0]
  have ha : 0 < exposedPhaseLockA E n := exposedPhaseLockA_pos E n
  have ha_le : exposedPhaseLockA E n ≤ 1 := by
    unfold exposedPhaseLockA
    change W / ((2 * n + 1) * Real.pi) ≤ 1
    have hgt : W / Real.pi < (2 * n + 1 : ℝ) :=
      lt_of_le_of_lt (le_max_left _ _) h2n
    have hWlt : W < (2 * n + 1 : ℝ) * Real.pi := by
      have := mul_lt_mul_of_pos_right hgt hπ
      have hWπ : W / Real.pi * Real.pi = W := by
        field_simp [ne_of_gt hπ]
      rwa [hWπ] at this
    have hden : 0 < (2 * n + 1 : ℝ) * Real.pi :=
      mul_pos (by exact_mod_cast Nat.succ_pos (2 * n)) hπ
    exact (div_le_one hden).mpr hWlt.le
  refine ⟨n, ha_le, ?_⟩
  have h2a : 0 < 2 * exposedPhaseLockA E n := mul_pos (by norm_num) ha
  have hexp0 : Real.exp (-E.Δ / (2 * exposedPhaseLockA E n)) < 1 :=
    Real.exp_lt_one_iff.mpr (div_neg_of_neg_of_pos (neg_lt_zero.mpr hΔ) h2a)
  by_cases hC1 : 1 ≤ C
  · exact hexp0.trans_le hC1
  · have hClt : C < 1 := lt_of_not_ge hC1
    have hloglt : Real.log C < 0 := Real.log_neg hC hClt
    have hL : L = -Real.log C := max_eq_right (neg_nonneg.mpr hloglt.le)
    have hcoef : 0 < E.Δ * Real.pi / (2 * W) :=
      div_pos (mul_pos hΔ hπ) (mul_pos (by norm_num) hW)
    have hstep : (2 * W * L) / (E.Δ * Real.pi) < (2 * n + 1 : ℝ) :=
      lt_of_le_of_lt (le_max_right _ _) h2n
    have hmul := mul_lt_mul_of_pos_right hstep hcoef
    have hLHS : (2 * W * L) / (E.Δ * Real.pi) * (E.Δ * Real.pi / (2 * W)) = L := by
      field_simp [ne_of_gt hΔ, ne_of_gt hπ, ne_of_gt hW]
    have hRHS :
        (2 * n + 1 : ℝ) * (E.Δ * Real.pi / (2 * W)) =
          E.Δ / (2 * exposedPhaseLockA E n) := by
      unfold exposedPhaseLockA W
      field_simp [ne_of_gt hW, ne_of_gt hπ, ne_of_gt ha]
    have hΔa : L < E.Δ / (2 * exposedPhaseLockA E n) := by
      rwa [hLHS, hRHS] at hmul
    have : E.Δ / (2 * exposedPhaseLockA E n) > -Real.log C := by
      rwa [hL] at hΔa
    have hlt : -E.Δ / (2 * exposedPhaseLockA E n) < Real.log C := by
      have := neg_lt_neg this
      simpa [neg_div] using this
    have := Real.exp_lt_exp.mpr hlt
    rwa [Real.exp_log hC] at this

/-- Phase-locked packet on an exposed orbit has negative zero-side. -/
def GaborExposedOrbitAssembly : Prop :=
  ∀ E : ExposedOrbit,
    ∃ n : ℕ, gaborZeroSide
      (pureGaborTest (exposedPhaseLockA E n) E.omega
        (exposedPhaseLockA_pos E n)) < 0

theorem gaborExposedOrbitAssembly_holds : GaborExposedOrbitAssembly := by
  intro E
  set mR : ℝ := (riemannZetaMultiplicity (E.ρ : ℂ) : ℝ)
  have hmposNat : 0 < riemannZetaMultiplicity (E.ρ : ℂ) :=
    riemannZetaMultiplicity_pos E.ρ.property.1
      (isCriticalStripZetaZero_ne_one E.ρ.property)
  have hmpos : 0 < mR := Nat.cast_pos.mpr hmposNat
  set R1 : ℝ :=
    ∑' τ : {z : ℂ // IsCriticalStripZetaZero z},
      (riemannZetaMultiplicity (τ : ℂ) : ℝ) *
        Real.exp
          ((gaborScore (stripSigma τ) (stripGamma τ) E.omega -
            (E.M - E.Δ)) / 2)
  have hR0 : 0 ≤ R1 :=
    tsum_nonneg fun _ =>
      mul_nonneg (Nat.cast_nonneg _) (Real.exp_pos _).le
  set C : ℝ := mR / (3 * mR + R1 + 1)
  have hCpos : 0 < C :=
    div_pos hmpos (by
      exact add_pos_of_nonneg_of_pos
        (add_nonneg (mul_nonneg (by norm_num) hmpos.le) hR0) (by norm_num))
  obtain ⟨n, ha1, hexp⟩ := exists_exposedPhaseLockA_small E hCpos
  set a := exposedPhaseLockA E n
  have ha : 0 < a := exposedPhaseLockA_pos E n
  have hsplit :=
    gaborZeroSide_eq_orbit_add_tail (omega := E.omega)
      (exposedPhaseLockA_pos E n) E.ρ
  have horbit := orbit_re_le_exposed E n
  have htail :=
    tail_re_le_exposed E (exposedPhaseLockA_pos E n) ha1
  have hsum :
      gaborZeroSide
          (pureGaborTest (exposedPhaseLockA E n) E.omega
            (exposedPhaseLockA_pos E n)) ≤
        -(Real.pi / a) * mR * Real.exp (E.M / (2 * a)) +
          (3 * Real.pi / a) * mR *
            Real.exp ((E.M - E.Δ) / (2 * a)) +
          (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a)) * R1 := by
    have := add_le_add horbit htail
    simpa [hsplit, a, mR, R1] using this
  have hexp_split :
      Real.exp ((E.M - E.Δ) / (2 * a)) =
        Real.exp (E.M / (2 * a)) * Real.exp (-E.Δ / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have hrew :
      -(Real.pi / a) * mR * Real.exp (E.M / (2 * a)) +
          (3 * Real.pi / a) * mR *
            Real.exp ((E.M - E.Δ) / (2 * a)) +
          (Real.pi / a) * Real.exp ((E.M - E.Δ) / (2 * a)) * R1 =
        (Real.pi / a) * Real.exp (E.M / (2 * a)) *
          (-mR + (3 * mR + R1) * Real.exp (-E.Δ / (2 * a))) := by
    rw [hexp_split]
    ring
  have hbr :
      -mR + (3 * mR + R1) * Real.exp (-E.Δ / (2 * a)) < 0 := by
    have hden : 0 < 3 * mR + R1 + 1 :=
      add_pos_of_nonneg_of_pos
        (add_nonneg (mul_nonneg (by norm_num) hmpos.le) hR0) (by norm_num)
    have hpos3 : 0 < 3 * mR + R1 :=
      add_pos_of_pos_of_nonneg (mul_pos (by norm_num) hmpos) hR0
    have hmul :
        (3 * mR + R1) * Real.exp (-E.Δ / (2 * a)) <
          (3 * mR + R1) * C :=
      mul_lt_mul_of_pos_left hexp hpos3
    have hfrac : (3 * mR + R1) * C < mR := by
      dsimp [C]
      rw [← mul_div_assoc, div_lt_iff₀ hden]
      nlinarith [mul_pos hmpos hmpos]
    linarith
  have hpre : 0 < Real.pi / a * Real.exp (E.M / (2 * a)) :=
    mul_pos (div_pos Real.pi_pos ha) (Real.exp_pos _)
  have hZ := hsum.trans_eq hrew
  have hneg :
      (Real.pi / a) * Real.exp (E.M / (2 * a)) *
          (-mR + (3 * mR + R1) * Real.exp (-E.Δ / (2 * a))) < 0 :=
    mul_neg_of_pos_of_neg hpre hbr
  exact ⟨n, hZ.trans_lt hneg⟩

theorem exists_negative_pureGabor_of_not_rh
    (hasm : GaborExposedOrbitAssembly) (h : ¬RiemannHypothesis) :
    ∃ (a omega : ℝ) (ha : 0 < a),
      gaborZeroSide (pureGaborTest a omega ha) < 0 := by
  obtain ⟨E⟩ := exists_exposedOrbit_of_not_rh h
  obtain ⟨n, hneg⟩ := hasm E
  exact ⟨exposedPhaseLockA E n, E.omega, exposedPhaseLockA_pos E n, hneg⟩

theorem gabor_zeroSide_pure_criterion_iff_rh_of_assembly
    (hasm : GaborExposedOrbitAssembly) :
    (∀ (a omega : ℝ) (ha : 0 < a),
      0 ≤ gaborZeroSide (pureGaborTest a omega ha)) ↔
      RiemannHypothesis := by
  constructor
  · intro hpos
    by_contra hRH
    obtain ⟨a, omega, ha, hneg⟩ :=
      exists_negative_pureGabor_of_not_rh hasm hRH
    exact (not_le_of_gt hneg) (hpos a omega ha)
  · intro hRH a omega ha
    exact rh_implies_gaborZeroSide_nonneg hRH rfl

theorem gabor_zeroSide_pure_criterion_iff_rh_unconditional :
    (∀ (a omega : ℝ) (ha : 0 < a),
      0 ≤ gaborZeroSide (pureGaborTest a omega ha)) ↔
      RiemannHypothesis :=
  gabor_zeroSide_pure_criterion_iff_rh_of_assembly
    gaborExposedOrbitAssembly_holds

#print axioms gaborScore_eq
#print axioms plus_lobe_num_le_score
#print axioms minus_lobe_num_le_score
#print axioms isCriticalStrip_of_not_RH
#print axioms exists_exposedOrbit_of_not_rh
#print axioms exposed_minus_lobe_cos
#print axioms gaborExposedOrbitAssembly_holds
#print axioms exists_negative_pureGabor_of_not_rh
#print axioms gabor_zeroSide_pure_criterion_iff_rh_of_assembly
#print axioms gabor_zeroSide_pure_criterion_iff_rh_unconditional
