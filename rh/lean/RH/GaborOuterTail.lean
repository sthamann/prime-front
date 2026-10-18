/-
RH/GaborOuterTail.lean -- r593 window-adaptive outer tail.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r592 sealed probe `gabor_window_adaptive_tail_probe.py`: a
window-adaptive packet (host = σ-max in W_R(γ★), R = 1;
a = min(σ★²/512, isolationShrink on d_min); ω = γ★ − πa/σ★)
rescues the r549/r551 local killers by merge/shrink.  The outer
tail is algebraically dead: strip width σ′² − σ★² < 1/4 loses to
window distance |γ′ − ω| ≥ 1.  The r592 near-tie break at
δ = 1e-8 was float64 ω-collapse (πa/σ < ulp(γ)); exact ℝ
arithmetic keeps the shrink.

r594 unloads the two r593 remainder Props: the multiplicity-
weighted outer `|Q|` tsum is dominated by the Path-A log-theta
at width `2a` (rate kept at `exp(−1/(8a))`; the prefactor
depends on the host ordinate, not on zero-set mass), and the
local-margin comparison follows by freezing that theta at
width `2` and sending `a → 0`.  No asserting `sorry`.  Census
unchanged.
-/
import RH.GaborArithmeticSeparator
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace RH

open scoped Classical
open Set Finset

/-! ## (1) Strip width beats window distance -/

/-- Phase detune `q = π a / σ★`. -/
noncomputable def gaborPhaseDetune (sigma a : ℝ) : ℝ :=
  Real.pi * a / sigma

/-- Relative quadrupole exponent numerator
`(σ′² − σ★²) − d² + 2 q |d|` (r592). -/
noncomputable def gaborOuterTailExponentNum
    (sigma' sigmaStar q d : ℝ) : ℝ :=
  (sigma' ^ 2 - sigmaStar ^ 2) - d ^ 2 + 2 * q * |d|

lemma gabor_sigma_sq_lt_quarter {sigma : ℝ}
    (h0 : 0 < sigma) (h1 : sigma < 1 / 2) :
    sigma ^ 2 < (1 / 4 : ℝ) := by
  nlinarith [h0, h1]

/-- Strip-width comparison: `σ′ ∈ (0, 1/2)` and `σ★ ∈ (0, 1/2]`
give `σ′² − σ★² < 1/4`.  NO RH CLAIM. -/
theorem gaborOuterTail_stripWidth_lt_quarter
    {sigma' sigmaStar : ℝ}
    (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (_hσ0 : 0 < sigmaStar) (_hσ : sigmaStar ≤ 1 / 2) :
    sigma' ^ 2 - sigmaStar ^ 2 < (1 / 4 : ℝ) := by
  have hlt := gabor_sigma_sq_lt_quarter hσ'0 hσ'
  linarith [hlt, sq_nonneg sigmaStar]

theorem gaborOuterTail_stripWidth_le_quarter
    {sigma' sigmaStar : ℝ}
    (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2) :
    sigma' ^ 2 - sigmaStar ^ 2 ≤ (1 / 4 : ℝ) :=
  (gaborOuterTail_stripWidth_lt_quarter hσ'0 hσ' hσ0 hσ).le

/-- First link: numerator `≤ 1/4 − |d|² + 2 q |d|`. -/
theorem gaborOuterTail_num_le_edge
    {sigma' sigmaStar q d : ℝ}
    (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2) :
    gaborOuterTailExponentNum sigma' sigmaStar q d ≤
      (1 / 4 : ℝ) - |d| ^ 2 + 2 * q * |d| := by
  unfold gaborOuterTailExponentNum
  have hstrip :=
    gaborOuterTail_stripWidth_le_quarter hσ'0 hσ' hσ0 hσ
  have hsq : d ^ 2 = |d| ^ 2 := (sq_abs d).symm
  linarith [hstrip, hsq]

/-- Algebraic identity `1/4 − |d|² + 2 q |d| = 1/4 − |d|(|d| − 2 q)`. -/
theorem gaborOuterTail_edge_eq (q d : ℝ) :
    (1 / 4 : ℝ) - |d| ^ 2 + 2 * q * |d| =
      (1 / 4 : ℝ) - |d| * (|d| - 2 * q) := by
  ring

/-- Quantitative edge bound: `q ≤ 1/4` and `|d| ≥ 1` give
`1/4 − |d|² + 2 q |d| ≤ −1/4`
(at the vertex `|d| = 1`, `q = 1/4`: `1/4 − 1 + 1/2 = −1/4`). -/
theorem gaborOuterTail_edge_le_neg_quarter
    {q d : ℝ} (_hq0 : 0 ≤ q) (hq : q ≤ (1 / 4 : ℝ))
    (hd : (1 : ℝ) ≤ |d|) :
    (1 / 4 : ℝ) - |d| ^ 2 + 2 * q * |d| ≤ -1 / 4 := by
  have hd0 : 0 ≤ |d| := abs_nonneg d
  have h2q : 2 * q ≤ (1 / 2 : ℝ) := by linarith [hq]
  have hlin : 2 * q * |d| ≤ (1 / 2 : ℝ) * |d| :=
    mul_le_mul_of_nonneg_right h2q hd0
  have hfac :
      |d| ^ 2 - (1 / 2 : ℝ) * |d| - (1 / 2 : ℝ) =
        (|d| - 1) * (|d| + 1 / 2) := by
    ring
  have hge : (1 / 2 : ℝ) ≤ |d| ^ 2 - (1 / 2 : ℝ) * |d| := by
    have : 0 ≤ (|d| - 1) * (|d| + 1 / 2) :=
      mul_nonneg (sub_nonneg.mpr hd) (by linarith [hd0])
    linarith [hfac, this]
  linarith [hlin, hge]

theorem gaborOuterTail_edge_neg
    {q d : ℝ} (hq0 : 0 ≤ q) (hq : q ≤ (1 / 4 : ℝ))
    (hd : (1 : ℝ) ≤ |d|) :
    (1 / 4 : ℝ) - |d| * (|d| - 2 * q) < 0 := by
  have h := gaborOuterTail_edge_le_neg_quarter hq0 hq hd
  rw [gaborOuterTail_edge_eq] at h
  linarith [h]

/-- Full numerator chain, quantitative form `≤ −1/4`. -/
theorem gaborOuterTail_num_le_neg_quarter
    {sigma' sigmaStar q d : ℝ}
    (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2)
    (hq0 : 0 ≤ q) (hq : q ≤ (1 / 4 : ℝ)) (hd : (1 : ℝ) ≤ |d|) :
    gaborOuterTailExponentNum sigma' sigmaStar q d ≤ -1 / 4 :=
  (gaborOuterTail_num_le_edge hσ'0 hσ' hσ0 hσ).trans
    (gaborOuterTail_edge_le_neg_quarter hq0 hq hd)

theorem gaborOuterTail_num_neg
    {sigma' sigmaStar q d : ℝ}
    (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2)
    (hq0 : 0 ≤ q) (hq : q ≤ (1 / 4 : ℝ)) (hd : (1 : ℝ) ≤ |d|) :
    gaborOuterTailExponentNum sigma' sigmaStar q d < 0 :=
  lt_of_le_of_lt
    (gaborOuterTail_num_le_neg_quarter hσ'0 hσ' hσ0 hσ hq0 hq hd)
    (by norm_num)

/-- Same-sign ordinates: plus and cross lobes are no closer than
the minus lobe. -/
theorem gabor_sameSign_plus_ge_minus {omega gamma : ℝ}
    (h : 0 ≤ omega * gamma) :
    (gamma - omega) ^ 2 ≤ (gamma + omega) ^ 2 := by
  have : (gamma + omega) ^ 2 - (gamma - omega) ^ 2 = 4 * (omega * gamma) := by
    ring
  linarith

theorem gabor_sameSign_cross_ge_minus {omega gamma : ℝ}
    (h : 0 ≤ omega * gamma) :
    (gamma - omega) ^ 2 ≤ gamma ^ 2 + omega ^ 2 := by
  have : gamma ^ 2 + omega ^ 2 - (gamma - omega) ^ 2 = 2 * (omega * gamma) := by
    ring
  linarith

theorem gaborThreeLobe_le_four_minus
    {a omega gamma : ℝ} (ha : 0 < a) (hsign : 0 ≤ omega * gamma) :
    gaborThreeLobe a omega gamma ≤
      4 * Real.exp (-(gamma - omega) ^ 2 / (2 * a)) := by
  unfold gaborThreeLobe
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hplus :
      Real.exp (-(gamma + omega) ^ 2 / (2 * a)) ≤
        Real.exp (-(gamma - omega) ^ 2 / (2 * a)) :=
    Real.exp_le_exp.mpr
      (div_le_div_of_nonneg_right
        (neg_le_neg (gabor_sameSign_plus_ge_minus hsign)) hden.le)
  have hcross :
      Real.exp (-(gamma ^ 2 + omega ^ 2) / (2 * a)) ≤
        Real.exp (-(gamma - omega) ^ 2 / (2 * a)) :=
    Real.exp_le_exp.mpr
      (div_le_div_of_nonneg_right
        (neg_le_neg (gabor_sameSign_cross_ge_minus hsign)) hden.le)
  nlinarith [hplus, hcross,
    Real.exp_pos (-(gamma - omega) ^ 2 / (2 * a))]

private lemma abs_add3 (x y z : ℝ) : |x + y + z| ≤ |x| + |y| + |z| := by
  have h1 : |x + y + z| ≤ |x + y| + |z| := abs_add_le (x + y) z
  have h2 : |x + y| ≤ |x| + |y| := abs_add_le x y
  linarith

private lemma exp_shift_sq (sigma a x : ℝ) (ha : 0 < a) :
    Real.exp ((sigma ^ 2 - x ^ 2) / (2 * a)) =
      Real.exp (sigma ^ 2 / (2 * a)) * Real.exp (-x ^ 2 / (2 * a)) := by
  rw [← Real.exp_add]
  congr 1
  field_simp [ha.ne']
  ring

/-- `|Q| ≤ E(σ,a) · threeLobe(a,ω,γ)`.  Uses the existing three-lobe
shape from `GaborHatAnalytic`. -/
theorem abs_gaborQuadrupole_le_enhancement_threeLobe
    {a omega sigma gamma : ℝ} (ha : 0 < a) :
    |gaborQuadrupole a omega sigma gamma| ≤
      gaborEnhancement sigma a * gaborThreeLobe a omega gamma := by
  have hπa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hp := exp_shift_sq sigma a (gamma + omega) ha
  have hm := exp_shift_sq sigma a (gamma - omega) ha
  have hx :
      Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) =
        Real.exp (sigma ^ 2 / (2 * a)) *
          Real.exp (-(gamma ^ 2 + omega ^ 2) / (2 * a)) := by
    rw [← Real.exp_add]
    congr 1
    field_simp [ha.ne']
    ring
  set Ap : ℝ := Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a))
  set Am : ℝ := Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a))
  set Ax : ℝ := Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a))
  have hAp : 0 ≤ Ap := (Real.exp_pos _).le
  have hAm : 0 ≤ Am := (Real.exp_pos _).le
  have hAx : 0 ≤ Ax := (Real.exp_pos _).le
  have hcos1 := Real.abs_cos_le_one (sigma * (gamma + omega) / a)
  have hcos2 := Real.abs_cos_le_one (sigma * (gamma - omega) / a)
  have hcos3 := Real.abs_cos_le_one (sigma * gamma / a)
  have henv :
      |Ap * Real.cos (sigma * (gamma + omega) / a) +
          Am * Real.cos (sigma * (gamma - omega) / a) +
          2 * Ax * Real.cos (sigma * gamma / a)| ≤
        Ap + Am + 2 * Ax := by
    refine (abs_add3 _ _ _).trans ?_
    have t1 : |Ap * Real.cos (sigma * (gamma + omega) / a)| ≤ Ap := by
      rw [abs_mul, abs_of_nonneg hAp]
      exact mul_le_of_le_one_right hAp hcos1
    have t2 : |Am * Real.cos (sigma * (gamma - omega) / a)| ≤ Am := by
      rw [abs_mul, abs_of_nonneg hAm]
      exact mul_le_of_le_one_right hAm hcos2
    have t3 : |2 * Ax * Real.cos (sigma * gamma / a)| ≤ 2 * Ax := by
      rw [mul_assoc, abs_mul, abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 2),
        abs_mul, abs_of_nonneg hAx]
      nlinarith [hAx, hcos3]
    linarith [t1, t2, t3]
  have hrew : Ap + Am + 2 * Ax =
      Real.exp (sigma ^ 2 / (2 * a)) * gaborThreeLobe a omega gamma := by
    simp only [Ap, Am, Ax, gaborThreeLobe, hp, hm, hx]
    ring
  unfold gaborQuadrupole gaborEnhancement
  rw [abs_mul, abs_of_pos hπa]
  have hfinal := mul_le_mul_of_nonneg_left (henv.trans_eq hrew) hπa.le
  simpa [Ap, Am, Ax, mul_assoc] using hfinal

/-- Outer-zero quadrupole: `|Q| ≤ 4 E(σ★,a) exp(−1/(8a))`.
Same-sign hypothesis matches the FD convention `γ,ω > 0`. -/
theorem abs_gaborQuadrupole_outer_le_exp
    {a omega sigma' sigmaStar gamma : ℝ}
    (ha : 0 < a) (hσ'0 : 0 < sigma') (hσ' : sigma' < 1 / 2)
    (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2)
    (hω : 0 < omega) (hγ : 0 < gamma)
    (hq : gaborPhaseDetune sigmaStar a ≤ (1 / 4 : ℝ))
    (hd : (1 : ℝ) ≤ |gamma - omega|) :
    |gaborQuadrupole a omega sigma' gamma| ≤
      4 * gaborEnhancement sigmaStar a *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  have hsign : 0 ≤ omega * gamma := mul_nonneg hω.le hγ.le
  have hthree := gaborThreeLobe_le_four_minus (a := a) ha hsign
  have hQ := abs_gaborQuadrupole_le_enhancement_threeLobe (a := a)
    (omega := omega) (sigma := sigma') (gamma := gamma) ha
  have hq0 : 0 ≤ gaborPhaseDetune sigmaStar a :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hσ0.le
  have hnum :=
    gaborOuterTail_num_le_neg_quarter (sigma' := sigma')
      (sigmaStar := sigmaStar) (q := gaborPhaseDetune sigmaStar a)
      (d := gamma - omega) hσ'0 hσ' hσ0 hσ hq0 hq hd
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hratio :
      gaborEnhancement sigma' a =
        gaborEnhancement sigmaStar a *
          Real.exp ((sigma' ^ 2 - sigmaStar ^ 2) / (2 * a)) := by
    unfold gaborEnhancement
    have hexp :
        Real.exp (sigma' ^ 2 / (2 * a)) =
          Real.exp (sigmaStar ^ 2 / (2 * a)) *
            Real.exp ((sigma' ^ 2 - sigmaStar ^ 2) / (2 * a)) := by
      rw [← Real.exp_add]
      congr 1
      field_simp [ha.ne']
      ring
    rw [hexp]
    ring
  have hE'0 : 0 ≤ gaborEnhancement sigma' a := by
    unfold gaborEnhancement; positivity
  have hE0 : 0 ≤ gaborEnhancement sigmaStar a := by
    unfold gaborEnhancement; positivity
  have henv :
      gaborEnhancement sigma' a * gaborThreeLobe a omega gamma ≤
        gaborEnhancement sigma' a *
          (4 * Real.exp (-(gamma - omega) ^ 2 / (2 * a))) :=
    mul_le_mul_of_nonneg_left hthree hE'0
  have hprod :
      gaborEnhancement sigma' a *
          (4 * Real.exp (-(gamma - omega) ^ 2 / (2 * a))) =
        4 * gaborEnhancement sigmaStar a *
          Real.exp ((sigma' ^ 2 - sigmaStar ^ 2 -
            (gamma - omega) ^ 2) / (2 * a)) := by
    rw [hratio]
    have hexp :
        Real.exp ((sigma' ^ 2 - sigmaStar ^ 2) / (2 * a)) *
            Real.exp (-(gamma - omega) ^ 2 / (2 * a)) =
          Real.exp ((sigma' ^ 2 - sigmaStar ^ 2 -
            (gamma - omega) ^ 2) / (2 * a)) := by
      rw [← Real.exp_add]
      congr 1
      ring
    calc
      gaborEnhancement sigmaStar a *
            Real.exp ((sigma' ^ 2 - sigmaStar ^ 2) / (2 * a)) *
          (4 * Real.exp (-(gamma - omega) ^ 2 / (2 * a))) =
        4 * gaborEnhancement sigmaStar a *
          (Real.exp ((sigma' ^ 2 - sigmaStar ^ 2) / (2 * a)) *
            Real.exp (-(gamma - omega) ^ 2 / (2 * a))) := by
        ring
      _ = 4 * gaborEnhancement sigmaStar a *
          Real.exp ((sigma' ^ 2 - sigmaStar ^ 2 -
            (gamma - omega) ^ 2) / (2 * a)) := by
        rw [hexp]
  have hrel :
      sigma' ^ 2 - sigmaStar ^ 2 - (gamma - omega) ^ 2 ≤
        gaborOuterTailExponentNum sigma' sigmaStar
          (gaborPhaseDetune sigmaStar a) (gamma - omega) := by
    unfold gaborOuterTailExponentNum
    nlinarith [mul_nonneg (mul_nonneg (by norm_num : (0 : ℝ) ≤ 2) hq0)
      (abs_nonneg (gamma - omega))]
  have hexp_le :
      Real.exp ((sigma' ^ 2 - sigmaStar ^ 2 - (gamma - omega) ^ 2) /
          (2 * a)) ≤
        Real.exp (gaborOuterTailExponentNum sigma' sigmaStar
            (gaborPhaseDetune sigmaStar a) (gamma - omega) / (2 * a)) :=
    Real.exp_le_exp.mpr (div_le_div_of_nonneg_right hrel hden.le)
  have hquarter :
      Real.exp (gaborOuterTailExponentNum sigma' sigmaStar
          (gaborPhaseDetune sigmaStar a) (gamma - omega) / (2 * a)) ≤
        Real.exp ((-1 / 4 : ℝ) / (2 * a)) :=
    Real.exp_le_exp.mpr (div_le_div_of_nonneg_right hnum hden.le)
  have hsimp : (-1 / 4 : ℝ) / (2 * a) = -(1 : ℝ) / (8 * a) := by
    field_simp [ha.ne']
    ring
  refine hQ.trans (henv.trans ?_)
  rw [hprod]
  refine mul_le_mul_of_nonneg_left ?_ (mul_nonneg (by norm_num) hE0)
  exact hexp_le.trans (hquarter.trans_eq (by rw [hsimp]))

/-! ## (2) Summable / Finset outer tail -/

/-- Explicit prefactor `C(a) = 4 E(σ★,a)`, decreasing in `a`. -/
noncomputable def gaborOuterTailPrefactor (sigma a : ℝ) : ℝ :=
  4 * gaborEnhancement sigma a

/-- Finite-catalog outer tail.  Multiplicity-weighted sum of `|Q|`
over any finite set of outer points is
`≤ C(a) exp(−1/(8a)) · (total mass)`, with `C = 4 E(σ★,a)`. -/
theorem gaborOuterTail_finset_le
    {a omega sigmaStar : ℝ}
    (ha : 0 < a) (hσ0 : 0 < sigmaStar) (hσ : sigmaStar ≤ 1 / 2)
    (hω : 0 < omega) (hq : gaborPhaseDetune sigmaStar a ≤ (1 / 4 : ℝ))
    (S : Finset (ℝ × ℝ)) (mult : ℝ × ℝ → ℕ)
    (hS : ∀ q ∈ S, 0 < q.1 ∧ q.1 < 1 / 2 ∧ 0 < q.2 ∧
      (1 : ℝ) ≤ |q.2 - omega|) :
    S.sum (fun q => (mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) ≤
      gaborOuterTailPrefactor sigmaStar a *
        Real.exp (-(1 : ℝ) / (8 * a)) *
          S.sum (fun q => (mult q : ℝ)) := by
  have hpt : ∀ q ∈ S,
      (mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2| ≤
        (mult q : ℝ) * (gaborOuterTailPrefactor sigmaStar a *
          Real.exp (-(1 : ℝ) / (8 * a))) := by
    intro q hqS
    have hq' := hS q hqS
    have hQ := abs_gaborQuadrupole_outer_le_exp (a := a)
      (omega := omega) (sigma' := q.1) (sigmaStar := sigmaStar)
      (gamma := q.2) ha hq'.1 hq'.2.1 hσ0 hσ hω hq'.2.2.1 hq hq'.2.2.2
    unfold gaborOuterTailPrefactor
    exact mul_le_mul_of_nonneg_left hQ (Nat.cast_nonneg _)
  have hsum := sum_le_sum hpt
  have hfactor :
      S.sum (fun q =>
          (mult q : ℝ) * (gaborOuterTailPrefactor sigmaStar a *
            Real.exp (-(1 : ℝ) / (8 * a)))) =
        gaborOuterTailPrefactor sigmaStar a *
          Real.exp (-(1 : ℝ) / (8 * a)) *
            S.sum (fun q => (mult q : ℝ)) := by
    calc
      S.sum (fun q =>
          (mult q : ℝ) * (gaborOuterTailPrefactor sigmaStar a *
            Real.exp (-(1 : ℝ) / (8 * a)))) =
          S.sum (fun q =>
            (gaborOuterTailPrefactor sigmaStar a *
              Real.exp (-(1 : ℝ) / (8 * a))) * (mult q : ℝ)) :=
        sum_congr rfl fun q _ => mul_comm _ _
      _ = (gaborOuterTailPrefactor sigmaStar a *
            Real.exp (-(1 : ℝ) / (8 * a))) *
          S.sum (fun q => (mult q : ℝ)) :=
        (mul_sum S (fun q => (mult q : ℝ)) _).symm
  exact hsum.trans_eq hfactor

/-- Multiplicity-weighted `ĥ` series restricted to the outer tail
`|Im ρ − ω| ≥ R` is summable (dominated by the r587 quartic brick). -/
theorem summable_gaborHat_outer_tail (F : GaborWeilTest) (omega R : ℝ) :
    Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
      if R ≤ |(ρ : ℂ).im - omega| then
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
      else 0 := by
  have hfull := gaborMultiplicityWeightedHatSummableQuartic_holds F
  simpa [Set.indicator] using
    hfull.indicator
      {ρ : {z : ℂ // IsCriticalStripZetaZero z} |
        R ≤ |(ρ : ℂ).im - omega|}

/-- Gaussian split: `|t−ω| ≥ R` implies
`gaussWeight(a) ≤ exp(−R²/(4a)) · gaussWeight(2a)`. -/
theorem gaussWeight_outer_split
    {a omega t R : ℝ} (ha : 0 < a) (hR : 0 ≤ R)
    (hd : R ≤ |t - omega|) :
    gaussWeight a omega t ≤
      Real.exp (-R ^ 2 / (4 * a)) * gaussWeight (2 * a) omega t := by
  unfold gaussWeight
  have hden : 0 < 4 * a := mul_pos (by norm_num) ha
  have hd2 : R ^ 2 ≤ (t - omega) ^ 2 := by
    have habs : |R| ≤ |t - omega| := by
      simpa [abs_of_nonneg hR] using hd
    exact sq_le_sq.mpr habs
  have hhalf :
      -(t - omega) ^ 2 / (2 * (2 * a)) = -(t - omega) ^ 2 / (4 * a) := by
    ring
  have hineq :
      -(t - omega) ^ 2 / (2 * a) ≤
        -R ^ 2 / (4 * a) + -(t - omega) ^ 2 / (4 * a) := by
    have hident :
        -R ^ 2 / (4 * a) + -(t - omega) ^ 2 / (4 * a) -
            (-(t - omega) ^ 2 / (2 * a)) =
          ((t - omega) ^ 2 - R ^ 2) / (4 * a) := by
      field_simp [ha.ne']
      ring
    have : 0 ≤ ((t - omega) ^ 2 - R ^ 2) / (4 * a) :=
      div_nonneg (sub_nonneg.mpr hd2) hden.le
    linarith [hident, this]
  rw [← Real.exp_add, hhalf]
  exact Real.exp_le_exp.mpr hineq

/-- Unweighted Finset three-lobe tail against the existing log-theta
majorant at width `2a` (r580). -/
theorem gaborThreeLobe_outer_finset_le_theta
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hS : ∀ ρ ∈ S, 0 < (ρ : ℂ).im ∧ R ≤ |(ρ : ℂ).im - omega|)
    (hω : 0 < omega) :
    S.sum (fun ρ => gaborThreeLobe a omega (ρ : ℂ).im) ≤
      4 * Real.exp (-R ^ 2 / (4 * a)) *
        gaborLogWeightedTheta (2 * a) omega := by
  have h2a : 0 < 2 * a := mul_pos (by norm_num) ha
  have hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax (2 * a) omega k :=
    gaborLogWeightedThetaSummable h2a omega
  have hpt : ∀ ρ ∈ S,
      gaborThreeLobe a omega (ρ : ℂ).im ≤
        4 * Real.exp (-R ^ 2 / (4 * a)) *
          gaussWeight (2 * a) omega (ρ : ℂ).im := by
    intro ρ hρ
    have hsign : 0 ≤ omega * (ρ : ℂ).im :=
      mul_nonneg hω.le (hS ρ hρ).1.le
    have hfour := gaborThreeLobe_le_four_minus (a := a) ha hsign
    have hsplit := gaussWeight_outer_split (a := a) (omega := omega)
      (t := (ρ : ℂ).im) (R := R) ha (by linarith [hR]) (hS ρ hρ).2
    refine hfour.trans ?_
    have := mul_le_mul_of_nonneg_left hsplit (by norm_num : (0 : ℝ) ≤ 4)
    exact this.trans_eq (by ring)
  have hsum := sum_le_sum hpt
  have hfactor :
      S.sum (fun ρ =>
          4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaussWeight (2 * a) omega (ρ : ℂ).im) =
        4 * Real.exp (-R ^ 2 / (4 * a)) *
          S.sum (fun ρ => gaussWeight (2 * a) omega (ρ : ℂ).im) := by
    simp [mul_sum, mul_assoc]
  have hθ :=
    gauss_density_transfer_stripZeros_of_summable h2a omega S hMs
  refine hsum.trans ?_
  rw [hfactor]
  exact mul_le_mul_of_nonneg_left hθ
    (mul_nonneg (by norm_num) (Real.exp_pos _).le)

/-- Unweighted Finset `|Q|` tail via three-lobe + theta.
Rate `exp(−1/(8a))` at `R ≥ 1`. -/
theorem abs_gaborQuadrupole_outer_finset_le_theta
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hS : ∀ ρ ∈ S,
      0 < (ρ : ℂ).re - 1 / 2 ∧ (ρ : ℂ).re - 1 / 2 < 1 / 2 ∧
        0 < (ρ : ℂ).im ∧ R ≤ |(ρ : ℂ).im - omega|) :
    S.sum (fun ρ =>
        |gaborQuadrupole a omega ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|) ≤
      (4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega) *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  have hpt : ∀ ρ ∈ S,
      |gaborQuadrupole a omega ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im| ≤
        (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          gaborThreeLobe a omega (ρ : ℂ).im := by
    intro ρ hρ
    have hQ := abs_gaborQuadrupole_le_enhancement_threeLobe
      (a := a) (omega := omega) (sigma := (ρ : ℂ).re - 1 / 2)
      (gamma := (ρ : ℂ).im) ha
    have hσ2 : ((ρ : ℂ).re - 1 / 2) ^ 2 ≤ (1 / 4 : ℝ) :=
      (gabor_sigma_sq_lt_quarter (hS ρ hρ).1 (hS ρ hρ).2.1).le
    have hE :
        gaborEnhancement ((ρ : ℂ).re - 1 / 2) a ≤
          (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
      unfold gaborEnhancement
      refine mul_le_mul_of_nonneg_left ?_ (div_nonneg Real.pi_pos.le ha.le)
      exact Real.exp_le_exp.mpr
        (div_le_div_of_nonneg_right hσ2 (mul_nonneg (by norm_num) ha.le))
    exact hQ.trans (mul_le_mul_of_nonneg_right hE
      (gaborThreeLobe_nonneg _ _ _))
  have hsum := sum_le_sum hpt
  have hC : 0 ≤ (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
    positivity
  have hfactor :
      S.sum (fun ρ =>
          (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            gaborThreeLobe a omega (ρ : ℂ).im) =
        (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          S.sum (fun ρ => gaborThreeLobe a omega (ρ : ℂ).im) := by
    simp [mul_sum, mul_assoc]
  have hθ := gaborThreeLobe_outer_finset_le_theta (a := a)
    (omega := omega) (R := R) ha hR S
    (fun ρ hρ => ⟨(hS ρ hρ).2.2.1, (hS ρ hρ).2.2.2⟩) hω
  have hR2 : -R ^ 2 / (4 * a) ≤ -(1 : ℝ) / (4 * a) := by
    have hsq : (1 : ℝ) ≤ R ^ 2 := by nlinarith [hR]
    exact div_le_div_of_nonneg_right (neg_le_neg hsq)
      (mul_pos (by norm_num) ha).le
  have hexpR :
      Real.exp ((1 / 4 : ℝ) / (2 * a)) * Real.exp (-R ^ 2 / (4 * a)) ≤
        Real.exp (-(1 : ℝ) / (8 * a)) := by
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have h1 : (1 / 4 : ℝ) / (2 * a) = (1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    have : (1 : ℝ) / (8 * a) + (-R ^ 2 / (4 * a)) ≤
        (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) := by
      linarith [hR2]
    have h2 : (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) =
        -(1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    rw [h1]
    exact this.trans_eq h2
  refine hsum.trans ?_
  rw [hfactor]
  refine (mul_le_mul_of_nonneg_left hθ hC).trans ?_
  have hrew :
      (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          (4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaborLogWeightedTheta (2 * a) omega) =
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega) *
          (Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            Real.exp (-R ^ 2 / (4 * a))) := by
    ring
  rw [hrew]
  have hθ0 : 0 ≤ gaborLogWeightedTheta (2 * a) omega :=
    tsum_nonneg fun k =>
      mul_nonneg (gaborBinCountMajorant_nonneg k)
        (gaussBinMax_nonneg (mul_pos (by norm_num) ha) k)
  have hpre : 0 ≤ 4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega :=
    mul_nonneg (mul_nonneg (by norm_num) (div_nonneg Real.pi_pos.le ha.le))
      hθ0
  exact mul_le_mul_of_nonneg_left hexpR hpre

/-! ## (2b) Multiplicity-weighted tsum (r594) -/

/-- Mass-independent tsum prefactor: crude enhancement ceiling
`π/a` times the Path-A log-theta at width `2a`.  The Jacobi
majorant is centered at `ω`, so the constant depends on the
host ordinate; it does *not* depend on the zero-set mass.
NO RH CLAIM. -/
noncomputable def gaborOuterTailTsumPrefactor (a omega : ℝ) : ℝ :=
  4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega

lemma gaussWeight_mono_a {a a' c t : ℝ} (ha : 0 < a) (haa : a ≤ a') :
    gaussWeight a c t ≤ gaussWeight a' c t := by
  unfold gaussWeight
  refine Real.exp_le_exp.mpr ?_
  have ha' : 0 < a' := lt_of_lt_of_le ha haa
  have hsq : 0 ≤ (t - c) ^ 2 := sq_nonneg _
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hden' : 0 < 2 * a' := mul_pos (by norm_num) ha'
  have hdiv : (t - c) ^ 2 / (2 * a') ≤ (t - c) ^ 2 / (2 * a) :=
    div_le_div_of_nonneg_left hsq hden
      (mul_le_mul_of_nonneg_left haa (by norm_num))
  have hL : -(t - c) ^ 2 / (2 * a) = -((t - c) ^ 2 / (2 * a)) := by
    field_simp [hden.ne']
  have hR : -(t - c) ^ 2 / (2 * a') = -((t - c) ^ 2 / (2 * a')) := by
    field_simp [hden'.ne']
  rw [hL, hR]
  exact neg_le_neg hdiv

lemma gaussBinMax_mono_a {a a' c : ℝ} (ha : 0 < a) (haa : a ≤ a')
    (k : ℤ) :
    gaussBinMax a c k ≤ gaussBinMax a' c k := by
  have ha' : 0 < a' := lt_of_lt_of_le ha haa
  unfold gaussBinMax
  refine csSup_le (gaussWeight_image_nonempty a c k) ?_
  intro y hy
  obtain ⟨t, ht, rfl⟩ := hy
  exact (gaussWeight_mono_a ha haa).trans (le_gaussBinMax ha' ht)

theorem gaborLogWeightedTheta_mono_a {a a' c : ℝ}
    (ha : 0 < a) (haa : a ≤ a') :
    gaborLogWeightedTheta a c ≤ gaborLogWeightedTheta a' c := by
  have ha' : 0 < a' := lt_of_lt_of_le ha haa
  have hsm := gaborLogWeightedThetaSummable ha c
  have hsm' := gaborLogWeightedThetaSummable ha' c
  refine Summable.tsum_le_tsum ?_ hsm hsm'
  intro k
  exact mul_le_mul_of_nonneg_left (gaussBinMax_mono_a ha haa k)
    (gaborBinCountMajorant_nonneg k)

lemma gaborLogWeightedTheta_nonneg {a c : ℝ} (ha : 0 < a) :
    0 ≤ gaborLogWeightedTheta a c :=
  tsum_nonneg fun k =>
    mul_nonneg (gaborBinCountMajorant_nonneg k)
      (gaussBinMax_nonneg ha k)

/-- Multiplicity-weighted Finset three-lobe tail against the
log-theta majorant at width `2a`. -/
theorem gaborThreeLobe_outer_mult_finset_le_theta
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hS : ∀ ρ ∈ S, 0 < (ρ : ℂ).im ∧ R ≤ |(ρ : ℂ).im - omega|)
    (hω : 0 < omega) :
    S.sum (fun ρ =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          gaborThreeLobe a omega (ρ : ℂ).im) ≤
      4 * Real.exp (-R ^ 2 / (4 * a)) *
        gaborLogWeightedTheta (2 * a) omega := by
  have h2a : 0 < 2 * a := mul_pos (by norm_num) ha
  have hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax (2 * a) omega k :=
    gaborLogWeightedThetaSummable h2a omega
  have hpt : ∀ ρ ∈ S,
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          gaborThreeLobe a omega (ρ : ℂ).im ≤
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          (4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaussWeight (2 * a) omega (ρ : ℂ).im) := by
    intro ρ hρ
    have hsign : 0 ≤ omega * (ρ : ℂ).im :=
      mul_nonneg hω.le (hS ρ hρ).1.le
    have hfour := gaborThreeLobe_le_four_minus (a := a) ha hsign
    have hsplit := gaussWeight_outer_split (a := a) (omega := omega)
      (t := (ρ : ℂ).im) (R := R) ha (by linarith [hR]) (hS ρ hρ).2
    have hthree := hfour.trans
      (mul_le_mul_of_nonneg_left hsplit (by norm_num : (0 : ℝ) ≤ 4))
    exact mul_le_mul_of_nonneg_left
      (hthree.trans_eq (by ring)) (Nat.cast_nonneg _)
  have hsum := sum_le_sum hpt
  have he : 0 ≤ 4 * Real.exp (-R ^ 2 / (4 * a)) := by positivity
  have hfactor :
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            (4 * Real.exp (-R ^ 2 / (4 * a)) *
              gaussWeight (2 * a) omega (ρ : ℂ).im)) =
        4 * Real.exp (-R ^ 2 / (4 * a)) *
          S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaussWeight (2 * a) omega (ρ : ℂ).im) := by
    calc
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            (4 * Real.exp (-R ^ 2 / (4 * a)) *
              gaussWeight (2 * a) omega (ρ : ℂ).im)) =
          S.sum (fun ρ =>
            (4 * Real.exp (-R ^ 2 / (4 * a))) *
              ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                gaussWeight (2 * a) omega (ρ : ℂ).im)) :=
        sum_congr rfl fun _ _ => by ring
      _ = (4 * Real.exp (-R ^ 2 / (4 * a))) *
          S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaussWeight (2 * a) omega (ρ : ℂ).im) :=
        (mul_sum _ _ _).symm
  have hθ := gauss_mass_transfer_stripZeros h2a omega S hMs
  refine hsum.trans ?_
  rw [hfactor]
  exact mul_le_mul_of_nonneg_left hθ he

/-- Multiplicity-weighted Finset `|Q|` tail via three-lobe +
log-theta.  Rate `exp(−1/(8a))` at `R ≥ 1`. -/
theorem abs_gaborQuadrupole_outer_mult_finset_le_theta
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z})
    (hS : ∀ ρ ∈ S,
      0 < (ρ : ℂ).re - 1 / 2 ∧ (ρ : ℂ).re - 1 / 2 < 1 / 2 ∧
        0 < (ρ : ℂ).im ∧ R ≤ |(ρ : ℂ).im - omega|) :
    S.sum (fun ρ =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          |gaborQuadrupole a omega
            ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|) ≤
      gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  have hpt : ∀ ρ ∈ S,
      (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          |gaborQuadrupole a omega
            ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im| ≤
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            gaborThreeLobe a omega (ρ : ℂ).im) := by
    intro ρ hρ
    have hQ := abs_gaborQuadrupole_le_enhancement_threeLobe
      (a := a) (omega := omega) (sigma := (ρ : ℂ).re - 1 / 2)
      (gamma := (ρ : ℂ).im) ha
    have hσ2 : ((ρ : ℂ).re - 1 / 2) ^ 2 ≤ (1 / 4 : ℝ) :=
      (gabor_sigma_sq_lt_quarter (hS ρ hρ).1 (hS ρ hρ).2.1).le
    have hE :
        gaborEnhancement ((ρ : ℂ).re - 1 / 2) a ≤
          (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
      unfold gaborEnhancement
      refine mul_le_mul_of_nonneg_left ?_
        (div_nonneg Real.pi_pos.le ha.le)
      exact Real.exp_le_exp.mpr
        (div_le_div_of_nonneg_right hσ2
          (mul_nonneg (by norm_num) ha.le))
    exact mul_le_mul_of_nonneg_left
      (hQ.trans (mul_le_mul_of_nonneg_right hE
        (gaborThreeLobe_nonneg _ _ _)))
      (Nat.cast_nonneg _)
  have hsum := sum_le_sum hpt
  have hC : 0 ≤ (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
    positivity
  have hfactor :
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
              gaborThreeLobe a omega (ρ : ℂ).im)) =
        (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaborThreeLobe a omega (ρ : ℂ).im) := by
    calc
      S.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
              gaborThreeLobe a omega (ρ : ℂ).im)) =
          S.sum (fun ρ =>
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a))) *
              ((riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                gaborThreeLobe a omega (ρ : ℂ).im)) :=
        sum_congr rfl fun _ _ => by ring
      _ = ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a))) *
          S.sum (fun ρ =>
            (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
              gaborThreeLobe a omega (ρ : ℂ).im) :=
        (mul_sum _ _ _).symm
  have hθ := gaborThreeLobe_outer_mult_finset_le_theta (a := a)
    (omega := omega) (R := R) ha hR S
    (fun ρ hρ => ⟨(hS ρ hρ).2.2.1, (hS ρ hρ).2.2.2⟩) hω
  have hR2 : -R ^ 2 / (4 * a) ≤ -(1 : ℝ) / (4 * a) := by
    have hsq : (1 : ℝ) ≤ R ^ 2 := by nlinarith [hR]
    exact div_le_div_of_nonneg_right (neg_le_neg hsq)
      (mul_pos (by norm_num) ha).le
  have hexpR :
      Real.exp ((1 / 4 : ℝ) / (2 * a)) * Real.exp (-R ^ 2 / (4 * a)) ≤
        Real.exp (-(1 : ℝ) / (8 * a)) := by
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have h1 : (1 / 4 : ℝ) / (2 * a) = (1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    have : (1 : ℝ) / (8 * a) + (-R ^ 2 / (4 * a)) ≤
        (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) := by
      linarith [hR2]
    have h2 : (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) =
        -(1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    rw [h1]
    exact this.trans_eq h2
  refine hsum.trans ?_
  rw [hfactor]
  refine (mul_le_mul_of_nonneg_left hθ hC).trans ?_
  have hrew :
      (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          (4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaborLogWeightedTheta (2 * a) omega) =
        gaborOuterTailTsumPrefactor a omega *
          (Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            Real.exp (-R ^ 2 / (4 * a))) := by
    unfold gaborOuterTailTsumPrefactor
    ring
  rw [hrew]
  have hθ0 : 0 ≤ gaborLogWeightedTheta (2 * a) omega :=
    gaborLogWeightedTheta_nonneg (mul_pos (by norm_num) ha)
  have hpre : 0 ≤ gaborOuterTailTsumPrefactor a omega := by
    unfold gaborOuterTailTsumPrefactor
    exact mul_nonneg
      (mul_nonneg (by norm_num) (div_nonneg Real.pi_pos.le ha.le)) hθ0
  exact mul_le_mul_of_nonneg_left hexpR hpre

/-- Outer-tail summand: FD zeros with `|Im ρ − ω| ≥ R`. -/
noncomputable def gaborOuterTailTerm (a omega R : ℝ)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) : ℝ :=
  if gaborFundDomain ρ ∧ R ≤ |(ρ : ℂ).im - omega| then
    (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
      |gaborQuadrupole a omega ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|
  else 0

lemma gaborOuterTailTerm_nonneg (a omega R : ℝ)
    (ρ : {z : ℂ // IsCriticalStripZetaZero z}) :
    0 ≤ gaborOuterTailTerm a omega R ρ := by
  unfold gaborOuterTailTerm
  split_ifs
  · exact mul_nonneg (Nat.cast_nonneg _) (abs_nonneg _)
  · exact le_rfl

lemma gaborFundDomain_sigma_pos
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (h : gaborFundDomain ρ) :
    0 < (ρ : ℂ).re - 1 / 2 :=
  sub_pos.mpr h.1

lemma gaborFundDomain_sigma_lt_half
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}}
    (_h : gaborFundDomain ρ) :
    (ρ : ℂ).re - 1 / 2 < 1 / 2 := by
  linarith [ρ.property.2.2]

lemma gaborOuterTailTerm_finset_le
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega)
    (S : Finset {z : ℂ // IsCriticalStripZetaZero z}) :
    S.sum (gaborOuterTailTerm a omega R) ≤
      gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  set S' := S.filter
    (fun ρ => gaborFundDomain ρ ∧ R ≤ |(ρ : ℂ).im - omega|)
  have hite :
      S.sum (gaborOuterTailTerm a omega R) =
        S'.sum (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            |gaborQuadrupole a omega
              ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|) := by
    unfold gaborOuterTailTerm S'
    exact (sum_filter (p := fun ρ =>
        gaborFundDomain ρ ∧ R ≤ |(ρ : ℂ).im - omega|)
      (f := fun ρ =>
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          |gaborQuadrupole a omega
            ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|)).symm
  have hS' : ∀ ρ ∈ S',
      0 < (ρ : ℂ).re - 1 / 2 ∧ (ρ : ℂ).re - 1 / 2 < 1 / 2 ∧
        0 < (ρ : ℂ).im ∧ R ≤ |(ρ : ℂ).im - omega| := by
    intro ρ hρ
    have hP := (mem_filter.mp hρ).2
    exact ⟨gaborFundDomain_sigma_pos hP.1,
      gaborFundDomain_sigma_lt_half hP.1, hP.1.2, hP.2⟩
  exact hite.trans_le
    (abs_gaborQuadrupole_outer_mult_finset_le_theta
      ha hR hω S' hS')

theorem summable_gaborOuterTailTerm
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega) :
    Summable (gaborOuterTailTerm a omega R) :=
  summable_of_sum_le (gaborOuterTailTerm_nonneg a omega R)
    (fun S => gaborOuterTailTerm_finset_le ha hR hω S)

/-- Multiplicity-weighted tsum of outer `|Q|` sizes
`≤ C(a,ω) exp(−1/(8a))` with the explicit mass-independent
prefactor `C(a,ω) = 4 (π/a) θ_log(2a,ω)`.  The `(1+log)` bin
occupancy is the Path-A increment inside `gaborLogWeightedTheta`;
the Gaussian width-`2a` majorant swallows it.  Rate kept at
`exp(−1/(8a))` (the `R ≥ 1` outer-split plus the `σ′² ≤ 1/4`
enhancement ceiling).  NO RH CLAIM. -/
theorem gaborOuterTail_tsum_le_exp
    {a omega R : ℝ} (ha : 0 < a) (hω : 0 < omega) (hR : (1 : ℝ) ≤ R) :
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      gaborOuterTailTerm a omega R ρ) ≤
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) :=
  Real.tsum_le_of_sum_le (gaborOuterTailTerm_nonneg a omega R)
    (fun S => gaborOuterTailTerm_finset_le ha hR hω S)

/-- Closed form of the tsum bound.  Discharged r594. -/
def GaborOuterTailTsumLeExp : Prop :=
  ∀ {a omega R : ℝ}, 0 < a → 0 < omega → (1 : ℝ) ≤ R →
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      if gaborFundDomain ρ ∧ R ≤ |(ρ : ℂ).im - omega| then
        (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
          |gaborQuadrupole a omega ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|
      else 0) ≤
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a))

theorem GaborOuterTailTsumLeExp_holds : GaborOuterTailTsumLeExp := by
  intro a omega R ha hω hR
  simpa [gaborOuterTailTerm] using
    gaborOuterTail_tsum_le_exp (a := a) (omega := omega) (R := R)
      ha hω hR

/-- `C · exp(−1/(8a)) → 0` as `a → 0⁺`, with an explicit
`a₀ ≤ 1` from `exp(−x) ≤ 1/(1+x) < 8a`. -/
lemma exists_small_width_mul_exp_neg {C ε : ℝ}
    (hC : 0 ≤ C) (hε : 0 < ε) :
    ∃ a0 : ℝ, 0 < a0 ∧ a0 ≤ 1 ∧
      ∀ {a : ℝ}, 0 < a → a < a0 →
        C * Real.exp (-(1 : ℝ) / (8 * a)) < ε := by
  refine ⟨min (1 : ℝ) (ε / (8 * (C + 1))), ?_, min_le_left _ _, ?_⟩
  · exact lt_min (by norm_num)
      (div_pos hε (mul_pos (by norm_num)
        (add_pos_of_nonneg_of_pos hC (by norm_num))))
  intro a ha hlt
  have hexp_le :
      Real.exp (-(1 : ℝ) / (8 * a)) ≤
        1 / (1 + (1 : ℝ) / (8 * a)) := by
    have hge : 1 + (1 : ℝ) / (8 * a) ≤
        Real.exp ((1 : ℝ) / (8 * a)) := by
      simpa [add_comm] using Real.add_one_le_exp ((1 : ℝ) / (8 * a))
    have hpos : 0 < 1 + (1 : ℝ) / (8 * a) := by positivity
    have hinv :
        1 / Real.exp ((1 : ℝ) / (8 * a)) ≤
          1 / (1 + (1 : ℝ) / (8 * a)) :=
      one_div_le_one_div_of_le hpos hge
    have hrew : Real.exp (-(1 : ℝ) / (8 * a)) =
        1 / Real.exp ((1 : ℝ) / (8 * a)) := by
      have hneg : -(1 : ℝ) / (8 * a) = -((1 : ℝ) / (8 * a)) := by
        field_simp [ha.ne']
      rw [hneg, Real.exp_neg, inv_eq_one_div]
    rw [hrew]
    exact hinv
  have hfrac :
      1 / (1 + (1 : ℝ) / (8 * a)) = (8 * a) / (8 * a + 1) := by
    field_simp [ha.ne']
  have hlt_frac : (8 * a) / (8 * a + 1) < 8 * a := by
    have hden : 0 < 8 * a + 1 := by positivity
    rw [div_lt_iff₀ hden]
    nlinarith [mul_pos (by norm_num : (0 : ℝ) < 8) ha]
  have hexp_lt_8a :
      Real.exp (-(1 : ℝ) / (8 * a)) < 8 * a :=
    (hexp_le.trans_eq hfrac).trans_lt hlt_frac
  have haε : a < ε / (8 * (C + 1)) :=
    lt_of_lt_of_le hlt (min_le_right _ _)
  by_cases hC0 : C = 0
  · simpa [hC0] using hε
  · have hCpos : 0 < C := lt_of_le_of_ne hC (Ne.symm hC0)
    have hprod :
        C * Real.exp (-(1 : ℝ) / (8 * a)) < C * (8 * a) :=
      mul_lt_mul_of_pos_left hexp_lt_8a hCpos
    have h8a :
        C * (8 * a) < C * (8 * (ε / (8 * (C + 1)))) :=
      mul_lt_mul_of_pos_left
        (mul_lt_mul_of_pos_left haε (by norm_num)) hCpos
    have hsimp :
        C * (8 * (ε / (8 * (C + 1)))) = C * ε / (C + 1) := by
      field_simp
    have hfracC : C * ε / (C + 1) < ε := by
      have hden : 0 < C + 1 := by positivity
      rw [div_lt_iff₀ hden]
      nlinarith [hCpos, hε]
    exact hprod.trans ((h8a.trans_eq hsimp).trans hfracC)

/-- Weaker tsum form: for every `ε > 0` the outer tail is
`< ε · E(σ★,a)` once `a` is small.  The modulus `a₀` depends
on the host ordinate `ω` (the log-theta at width `2` is frozen)
and on `ε`; it is not uniform in `ω`.  Follows from
`gaborOuterTail_tsum_le_exp` plus
`C(ω) · exp(−1/(8a)) → 0` as `a → 0⁺`.  NO RH CLAIM. -/
def GaborOuterTailSmallerThanLocalMargin : Prop :=
  ∀ {sigmaStar omega : ℝ}, 0 < sigmaStar → sigmaStar ≤ 1 / 2 →
    0 < omega →
      ∀ ε : ℝ, 0 < ε →
        ∃ a0 : ℝ, 0 < a0 ∧
          ∀ {a R : ℝ}, 0 < a → a < a0 → (1 : ℝ) ≤ R →
            (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              if gaborFundDomain ρ ∧ R ≤ |(ρ : ℂ).im - omega| then
                (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
                  |gaborQuadrupole a omega
                    ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|
              else 0) <
                ε * gaborEnhancement sigmaStar a

theorem GaborOuterTailSmallerThanLocalMargin_holds :
    GaborOuterTailSmallerThanLocalMargin := by
  intro sigmaStar omega hσ0 _hσ hω ε hε
  have hθ2 : 0 ≤ gaborLogWeightedTheta (2 : ℝ) omega :=
    gaborLogWeightedTheta_nonneg (by norm_num)
  have hC : 0 ≤ 4 * gaborLogWeightedTheta (2 : ℝ) omega :=
    mul_nonneg (by norm_num) hθ2
  obtain ⟨a0, ha0, ha0le, hsmall⟩ :=
    exists_small_width_mul_exp_neg hC hε
  refine ⟨a0, ha0, ?_⟩
  intro a R ha hlt hR
  have hts :=
    gaborOuterTail_tsum_le_exp (a := a) (omega := omega) (R := R)
      ha hω hR
  have h2a : 0 < 2 * a := mul_pos (by norm_num) ha
  have h2a_le : 2 * a ≤ (2 : ℝ) := by
    have : a < 1 := lt_of_lt_of_le hlt ha0le
    nlinarith
  have hθle :
      gaborLogWeightedTheta (2 * a) omega ≤
        gaborLogWeightedTheta (2 : ℝ) omega :=
    gaborLogWeightedTheta_mono_a h2a h2a_le
  have hπa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hexp0 : 0 ≤ Real.exp (-(1 : ℝ) / (8 * a)) :=
    (Real.exp_pos _).le
  have hpre_le :
      gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) ≤
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
    unfold gaborOuterTailTsumPrefactor
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left hθle
        (mul_nonneg (by norm_num) hπa.le))
      hexp0
  have hcore :
      4 * gaborLogWeightedTheta (2 : ℝ) omega *
        Real.exp (-(1 : ℝ) / (8 * a)) < ε :=
    hsmall ha hlt
  have hexpE :
      (1 : ℝ) ≤ Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    Real.one_le_exp
      (div_nonneg (sq_nonneg _) (mul_nonneg (by norm_num) ha.le))
  have hrhs :
      ε ≤ ε * Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    le_mul_of_one_le_right hε.le hexpE
  have hmid :
      (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
          Real.exp (-(1 : ℝ) / (8 * a)) <
        ε * (Real.pi / a) *
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    have hmul :
        (Real.pi / a) *
            (4 * gaborLogWeightedTheta (2 : ℝ) omega *
              Real.exp (-(1 : ℝ) / (8 * a))) <
          (Real.pi / a) *
            (ε * Real.exp (sigmaStar ^ 2 / (2 * a))) :=
      mul_lt_mul_of_pos_left (hcore.trans_le hrhs) hπa
    have hl :
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
            Real.exp (-(1 : ℝ) / (8 * a)) =
          (Real.pi / a) *
            (4 * gaborLogWeightedTheta (2 : ℝ) omega *
              Real.exp (-(1 : ℝ) / (8 * a))) := by
      ring
    have hr :
        ε * (Real.pi / a) * Real.exp (sigmaStar ^ 2 / (2 * a)) =
          (Real.pi / a) *
            (ε * Real.exp (sigmaStar ^ 2 / (2 * a))) := by
      ring
    exact hl.trans_lt (hmul.trans_eq hr.symm)
  have hE :
      ε * gaborEnhancement sigmaStar a =
        ε * (Real.pi / a) *
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    unfold gaborEnhancement
    ring
  have hchain :=
    (hts.trans hpre_le).trans_lt (hmid.trans_eq hE.symm)
  simpa [gaborOuterTailTerm] using hchain

/-! ## (3) Exact ℝ near-tie / well-definedness -/

theorem gaborPhaseDetune_pos {sigma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) :
    0 < gaborPhaseDetune sigma a :=
  div_pos (mul_pos Real.pi_pos ha) hs

/-- Lock width `a ≤ σ²/512` forces `q ≤ πσ/512 ≤ π/1024 < 1/4`. -/
theorem gaborALock_detune_le_quarter
    {sigma a : ℝ} (hs : 0 < sigma) (hs1 : sigma ≤ 1 / 2)
    (_ha : 0 ≤ a) (hlock : a ≤ gaborALock sigma) :
    gaborPhaseDetune sigma a ≤ (1 / 4 : ℝ) := by
  have hA : gaborALock sigma = sigma ^ 2 / 512 := by
    rw [gaborALock_eq]
    ring
  have hle : a ≤ sigma ^ 2 / 512 := by rwa [hA] at hlock
  have hπ : Real.pi * a / sigma ≤ Real.pi * sigma / 512 := by
    have hmul : Real.pi * a ≤ Real.pi * (sigma ^ 2 / 512) :=
      mul_le_mul_of_nonneg_left hle Real.pi_pos.le
    have hform : Real.pi * (sigma ^ 2 / 512) / sigma =
        Real.pi * sigma / 512 := by
      field_simp [hs.ne']
    exact (div_le_div_of_nonneg_right hmul hs.le).trans_eq hform
  have hσ : Real.pi * sigma / 512 ≤ Real.pi / 1024 := by
    have : sigma / 512 ≤ (1 / 2 : ℝ) / 512 :=
      div_le_div_of_nonneg_right hs1 (by norm_num)
    have hπm : Real.pi * (sigma / 512) ≤
        Real.pi * ((1 / 2 : ℝ) / 512) :=
      mul_le_mul_of_nonneg_left this Real.pi_pos.le
    have hrew : Real.pi * (sigma / 512) = Real.pi * sigma / 512 := by ring
    have hrew' : Real.pi * ((1 / 2 : ℝ) / 512) = Real.pi / 1024 := by ring
    exact (hrew.symm ▸ hπm).trans_eq hrew'
  have hπ4 : Real.pi / 1024 ≤ (1 / 4 : ℝ) := by
    have : Real.pi / 1024 ≤ 4 / 1024 :=
      div_le_div_of_nonneg_right Real.pi_lt_four.le (by norm_num)
    exact this.trans (by norm_num)
  exact hπ.trans (hσ.trans hπ4)

/-- Exact ℝ: `ω = γ − πa/σ < γ` as soon as `a > 0`.  The r592
float64 collapse `πa/σ < ulp(γ)` has no counterpart. -/
theorem gaborIsolationOmega_lt_gamma {sigma gamma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) :
    gaborIsolationOmega sigma gamma a < gamma := by
  have hq : 0 < Real.pi * a / sigma :=
    div_pos (mul_pos Real.pi_pos ha) hs
  unfold gaborIsolationOmega
  linarith [hq]

theorem gaborIsolationOmega_ne_gamma {sigma gamma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) :
    gaborIsolationOmega sigma gamma a ≠ gamma :=
  ne_of_lt (gaborIsolationOmega_lt_gamma hs ha)

/-- Isolation radius `≤ d_min/2` keeps `ω` at least `d_min/2`
away from every foreign ordinate. -/
theorem gaborIsolationOmega_ne_foreign
    {sigma gamma dMin a gamma' : ℝ}
    (hs : 0 < sigma) (hd : 0 < dMin)
    (hadm : gaborAdmissibleA sigma gamma dMin a)
    (hgap : dMin ≤ |gamma' - gamma|) :
    gaborIsolationOmega sigma gamma a ≠ gamma' := by
  have ha : 0 < a := hadm.1
  have hrad : Real.pi * a / sigma + gaborIsolationEpsilon a ≤ dMin / 2 := by
    simpa [gaborIsolationRadius] using hadm.2.2
  have hε : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
  have hpi : 0 ≤ Real.pi * a / sigma :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
  have hdet : |gaborIsolationOmega sigma gamma a - gamma| =
      Real.pi * a / sigma := by
    unfold gaborIsolationOmega
    rw [abs_of_nonpos (by linarith [hpi])]
    ring
  have htri :=
    abs_sub_le gamma' (gaborIsolationOmega sigma gamma a) gamma
  have hlo : dMin / 2 ≤
      |gamma' - gaborIsolationOmega sigma gamma a| := by
    linarith [hgap, hdet, htri, hrad, hε, hd]
  intro heq
  have : |gamma' - gaborIsolationOmega sigma gamma a| = 0 := by
    simp [heq]
  linarith [hlo, this, hd]

/-- Window-adaptive rule is well-defined on `d_min > 0`: some
admissible `a` produces `ω > 0`, `ω ≠ γ★`, and `ω ≠ γ′` for every
foreign gap.  Uses `exists_isolationShrink_omega`.  The greatest
admissible width is `exists_greatest_isolationShrink` (canonical
strip). -/
theorem gaborWindowAdaptiveRule_exists
    {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    ∃ a : ℝ, gaborAdmissibleA sigma gamma dMin a ∧
      0 < gaborIsolationOmega sigma gamma a ∧
        gaborIsolationOmega sigma gamma a ≠ gamma ∧
          ∀ gamma' : ℝ, dMin ≤ |gamma' - gamma| →
            gaborIsolationOmega sigma gamma a ≠ gamma' := by
  obtain ⟨a, hadm, hω⟩ := exists_isolationShrink_omega hs hg hd
  refine ⟨a, hadm, hω, gaborIsolationOmega_ne_gamma hs hadm.1, ?_⟩
  intro gamma' hgap
  exact gaborIsolationOmega_ne_foreign hs hd hadm hgap

theorem isolationShrink_omega_ne_host
    {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    (isolationShrink sigma gamma dMin hs hg hd).2 ≠ gamma := by
  have hspec := isolationShrink_spec hs hg hd
  rw [hspec.2.2]
  exact gaborIsolationOmega_ne_gamma hs hspec.1.1

theorem isolationShrink_omega_ne_foreign
    {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) {gamma' : ℝ}
    (hgap : dMin ≤ |gamma' - gamma|) :
    (isolationShrink sigma gamma dMin hs hg hd).2 ≠ gamma' := by
  have hspec := isolationShrink_spec hs hg hd
  rw [hspec.2.2]
  exact gaborIsolationOmega_ne_foreign hs hd hspec.1 hgap

theorem isolationShrinkTop_omega_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    0 < (isolationShrinkTop sigma gamma hs hg).2 := by
  simpa [isolationShrinkTop] using
    gaborIsolationOmega_pos hs hg
      (gaborAdmissibleAMax_pos hs hg).le
      (min_le_right _ _)

/-- `d_min = 0` / empty-foreign rule: `isolationShrinkTop` still
produces `ω ≠ γ`.  Multiplicity at the host is collected by
`gaborHostMerge_minusLobe` (already a theorem). -/
theorem isolationShrinkTop_omega_ne_gamma {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    (isolationShrinkTop sigma gamma hs hg).2 ≠ gamma := by
  simpa [isolationShrinkTop] using
    gaborIsolationOmega_ne_gamma hs (gaborAdmissibleAMax_pos hs hg)

theorem isolationShrinkOfConfig_omega_ne_host
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).2 ≠ gaborHostGamma Z hZ := by
  rw [isolationShrinkOfConfig_omega_eq]
  exact gaborIsolationOmega_ne_gamma (gaborHostSigma_pos Z hZ)
    (isolationShrinkOfConfig_a_pos Z hZ)

/-- Config packet: smaller width than the raw shrink still keeps
`|ω − γ| = πa/σ ≤ d_min/2`, so foreign ordinates stay distinct.
`d_min = 0` is the empty-foreign branch (`isolationShrinkTop`) plus
`gaborHostMerge_minusLobe`. -/
theorem isolationShrinkOfConfig_omega_ne_foreign
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    {q : ℝ × ℝ} (hq : q ∈ Z.pts)
    (hne : q.2 ≠ gaborHostGamma Z hZ) :
    (isolationShrinkOfConfig Z hZ).2 ≠ q.2 := by
  rw [isolationShrinkOfConfig_omega_eq]
  have hs := gaborHostSigma_pos Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hd := gaborForeignDMin_pos Z (gaborHostGamma Z hZ)
  have hgap := gaborForeignDMin_le Z (gaborHostGamma Z hZ) hq hne
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hneF :
      (Z.pts.filter (fun r => r.2 ≠ gaborHostGamma Z hZ)).Nonempty :=
    ⟨q, mem_filter.mpr ⟨hq, hne⟩⟩
  have hraw :
      isolationShrinkOfConfigRaw Z hZ =
        isolationShrink (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
          (gaborForeignDMin Z (gaborHostGamma Z hZ)) hs hg hd := by
    simp [isolationShrinkOfConfigRaw, hneF]
  have hspec := isolationShrink_spec hs hg hd
  have ha_le : (isolationShrinkOfConfig Z hZ).1 ≤
      (isolationShrinkOfConfigRaw Z hZ).1 := by
    rw [isolationShrinkOfConfig_a_eq]
    exact min_le_left _ _
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set aRaw := (isolationShrinkOfConfigRaw Z hZ).1
  have hπa : Real.pi * a / σ ≤ Real.pi * aRaw / σ :=
    div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left ha_le Real.pi_pos.le) hs.le
  have hε : 0 ≤ gaborIsolationEpsilon aRaw := Real.sqrt_nonneg _
  have hrad : Real.pi * aRaw / σ + gaborIsolationEpsilon aRaw ≤
      gaborForeignDMin Z γ / 2 := by
    simpa [gaborIsolationRadius, hraw, σ, γ, aRaw] using hspec.1.2.2
  have hpi0 : 0 ≤ Real.pi * a / σ :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
  have hdet : |gaborIsolationOmega σ γ a - γ| = Real.pi * a / σ := by
    unfold gaborIsolationOmega
    rw [abs_of_nonpos (by linarith [hpi0])]
    ring
  have htri := abs_sub_le q.2 (gaborIsolationOmega σ γ a) γ
  have hlo : gaborForeignDMin Z γ / 2 ≤
      |q.2 - gaborIsolationOmega σ γ a| := by
    linarith [hgap, hdet, htri, hπa, hrad, hε, hd]
  intro heq
  have : |q.2 - gaborIsolationOmega σ γ a| = 0 := by simp [heq]
  linarith [hlo, this, hd]

/-! ## (4) Window-adaptive cofinal-neg endpoint -/

/-- Window-adaptive cofinal negativity: every large weighted FD
window scores `W_honest ≤ −δ` against its own isolation-shrink
packet.  Distinct from the fixed-packet checkpoint
`GaborFixedPacketCofinalNegAt` (r591: needs an extremality gap).
r592: merge/shrink saves the local killers; the outer tail is
algebraically dead.  Unasserted.  NO RH CLAIM. -/
def GaborWindowAdaptiveCofinalNeg : Prop :=
  ∃ δ : ℝ, 0 < δ ∧
    ∃ T0 : ℝ, ∀ T : ℝ, T0 ≤ T →
      ∀ hZ : (gaborWeightedTruncationConfig T).pts.Nonempty,
        gaborHonestWeil
          (isolationShrinkOfConfig
            (gaborWeightedTruncationConfig T) hZ).1
          (isolationShrinkOfConfig
            (gaborWeightedTruncationConfig T) hZ).2
          (gaborWeightedTruncationConfig T) gaborCInc ≤ -δ

/-- Named implication, not a theorem: window-adaptive cofinal
negativity does not by itself produce per-zero arithmetic
separators.  Missing (L2 r589 Bridge A is RH-core): localization
of a large window to an off-critical host, and identification of
`W_honest` with `gaborArithmeticFormula` of the adaptive packet.
The r593 outer-tail algebra and ℝ near-tie lemmas are the
analytic input, not that identification.  Unasserted.  Not a
`sorry`. -/
def gabor_arithmetic_separator_of_window_adaptive : Prop :=
  GaborWindowAdaptiveCofinalNeg → GaborArithmeticSeparatesOffCriticalZeros

/-- VACUOUS (r600): premise refuted by `gaborSpectralFormula_refuted`;
kept for audit trail.  Sorry-free logic: explicit formula plus the
named implication plus window-adaptive cofinal-neg turns into the
pole-subtracted Mathlib endpoint.  Does not assert RH. -/
theorem gabor_window_adaptive_inputs_to_mathlib_rh
    (hexp : GaborExplicitFormula)
    (hcof : GaborWindowAdaptiveCofinalNeg)
    (himp : gabor_arithmetic_separator_of_window_adaptive)
    (hpos : ∀ F : GaborWeilTest, F.admissible →
      0 ≤ gaborSpectralFormula F) :
    RiemannHypothesis :=
  gabor_arithmetic_inputs_to_mathlib_rh hexp (himp hcof) hpos

/-- Named implication, not a theorem: window-adaptive cofinal
negativity does not by itself produce per-zero zero-side
separators.  Unasserted.  Not a `sorry`. -/
def gabor_zeroSide_separator_of_window_adaptive : Prop :=
  GaborWindowAdaptiveCofinalNeg → GaborZeroSideSeparatesOffCriticalZeros

/-- Live zero-side Mathlib endpoint parallel to the vacuous
`gabor_window_adaptive_inputs_to_mathlib_rh`. -/
theorem gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh
    (hcof : GaborWindowAdaptiveCofinalNeg)
    (himp : gabor_zeroSide_separator_of_window_adaptive)
    (hpos : ∀ F : GaborWeilTest, F.admissible →
      0 ≤ gaborZeroSide F) :
    RiemannHypothesis :=
  gabor_arithmetic_zeroSide_inputs_to_mathlib_rh (himp hcof) hpos

#print axioms gaborOuterTail_num_le_neg_quarter
#print axioms abs_gaborQuadrupole_outer_le_exp
#print axioms gaborOuterTail_finset_le
#print axioms summable_gaborHat_outer_tail
#print axioms gaborThreeLobe_outer_finset_le_theta
#print axioms gaborThreeLobe_outer_mult_finset_le_theta
#print axioms abs_gaborQuadrupole_outer_mult_finset_le_theta
#print axioms gaborOuterTail_tsum_le_exp
#print axioms GaborOuterTailTsumLeExp_holds
#print axioms GaborOuterTailSmallerThanLocalMargin_holds
#print axioms gaborWindowAdaptiveRule_exists
#print axioms isolationShrinkOfConfig_omega_ne_foreign
#print axioms gabor_window_adaptive_inputs_to_mathlib_rh
#print axioms gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh

end RH
