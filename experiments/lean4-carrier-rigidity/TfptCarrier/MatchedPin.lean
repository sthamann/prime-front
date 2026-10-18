/-
  MatchedPin — the round-125 matched-pin algebra, kernel-checked.
  ===============================================================

  Lean seam of round 125 (PRIME.KR4.DRIVER.CERT.01; note CDXXVI,
  contract PRIME.RADIUS4.LEAN.01): the exact algebra that makes the
  certified driver detection fire, matching the full-order-gated
  dictionary of `experiments/tfpt-discovery/driver_cert_probe.py`
  (`dscaled_pair`, gate G08): for one zero μ = δ + iγ at the anchor
  a₀, the weight is `y = a₀/(a₀ - μ²)` and the rate is
  `v = 4y(1-y)`; at the MATCHED pin a* = δ² + γ² everything becomes
  exactly real and exactly computable.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `matched_y` / `matched_y_conj` — THE MATCHED WEIGHT:
        y* = (γ + iδ)/(2γ) exactly (and (γ - iδ)/(2γ) for the
        conjugate zero) — the round-125 identity
        "y* = (gamma + i delta)/(2 gamma)".

    (2) `matched_weight_sum` — WEIGHT EXACTLY 1: the conjugate pair
        carries total weight y(μ) + y(μ̄) = 1; `matched_y_re` —
        equivalently Re y* = 1/2, so the pair's m-th diagonal cell
        is the PURELY POSITIVE +v*^m with no sign channel.

    (3) `matched_v` / `matched_v_gt_one` — THE MATCHED RATE IS
        EXACTLY REAL: v* = 4y*(1-y*) = 1 + δ²/γ² = 1 + ε, and
        v* > 1 whenever δ ≠ 0 — a certified rate-ratio above 1 IS an
        off-line detection (round-125 fire logic, algebra half).

    (4) `vRate_eq_four_w` — the dictionary lock: v = 4·w a μ² with
        the round-117 rate w of `Radius4Algebra`, so (3) is the
        radius-4 matched violation in rate currency (v* = 4w* with
        w* = (δ²+γ²)/(4γ²)).

    (5) `onLine_y_v` / `onLine_rate_pos` / `onLine_rate_le_one` —
        THE ON-LINE CONTRAST: an on-line zero (μ = iγ) has real
        weight y = a/(a+γ²) and rate v = 4y(1-y) = 4·wOnLine a γ ∈
        (0, 1] — on-line spectra contribute positive NON-INCREASING
        diagonal streams, which is exactly why a certified increase
        detects off-line mass.

  THE HONEST BOUNDARY.  These are exact complex-field lemmas about
  ONE zero-image at ONE pin.  The full round-125 statement
  d'_m(a₀) = (1+ε)^m + Σ_onl y_j v_j^m + Σ_off 2Re[y v^m] over the
  actual ξ_Q spectrum, the peel, the error budgets E_meas/R_peel,
  the certified LB ladder, and every statement about actual zeta or
  Epstein zeros remain the probe's measured/audited content and are
  NOT formalized.  No RH claim in any direction.
-/
import TfptCarrier.Radius4Algebra

namespace TfptCarrier
namespace MatchedPin

open Complex

/-! ### The per-zero weight and rate of the depth dictionary -/

/-- The weight of a zero μ at the anchor a in the round-125 depth
dictionary: `y = a/(a - μ²)` (equal to `Radius4Algebra.y a μ²`). -/
noncomputable def yPin (a μ : ℂ) : ℂ := a / (a - μ ^ 2)

/-- The rate of a zero μ at the anchor a: `v = 4y(1-y)`. -/
noncomputable def vRate (a μ : ℂ) : ℂ := 4 * yPin a μ * (1 - yPin a μ)

/-- Dictionary lock against round 117: `yPin a μ = y a (μ²)`. -/
theorem yPin_eq_y (a μ : ℂ) : yPin a μ = Radius4Algebra.y a (μ ^ 2) :=
  rfl

/-- **The rate is four times the radius-4 rate**: `v = 4·w a μ²`
wherever defined — round 125 lives on the round-117 arc. -/
theorem vRate_eq_four_w {a μ : ℂ} (h : a ≠ μ ^ 2) :
    vRate a μ = 4 * Radius4Algebra.w a (μ ^ 2) := by
  rw [vRate, yPin_eq_y, Radius4Algebra.w_eq_y_one_sub_y h]
  ring

/-! ### The matched pin a* = δ² + γ² -/

section Matched

variable (d g : ℝ)

private lemma hgd_ne (hg : g ≠ 0) : (g : ℂ) - (d : ℂ) * I ≠ 0 := by
  intro h
  apply hg
  have hre := congrArg Complex.re h
  simpa using hre

private lemma hgd_ne' (hg : g ≠ 0) : (g : ℂ) + (d : ℂ) * I ≠ 0 := by
  intro h
  apply hg
  have hre := congrArg Complex.re h
  simpa using hre

private lemma hsub_matched :
    ((d ^ 2 + g ^ 2 : ℝ) : ℂ) - ((d : ℂ) + (g : ℂ) * I) ^ 2
      = 2 * (g : ℂ) * ((g : ℂ) - (d : ℂ) * I) := by
  push_cast
  linear_combination (-(g : ℂ) ^ 2) * Complex.I_sq

private lemma hsub_matched' :
    ((d ^ 2 + g ^ 2 : ℝ) : ℂ) - ((d : ℂ) - (g : ℂ) * I) ^ 2
      = 2 * (g : ℂ) * ((g : ℂ) + (d : ℂ) * I) := by
  push_cast
  linear_combination (-(g : ℂ) ^ 2) * Complex.I_sq

/-- **THE MATCHED WEIGHT** (round 125, gate G08 algebra): at the
matched pin a* = δ² + γ², the zero μ = δ + iγ has weight EXACTLY
`y* = (γ + iδ)/(2γ)`. -/
theorem matched_y (hg : g ≠ 0) :
    yPin ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) + (g : ℂ) * I)
      = ((g : ℂ) + (d : ℂ) * I) / (2 * (g : ℂ)) := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have h2g : (2 : ℂ) * (g : ℂ) ≠ 0 := mul_ne_zero two_ne_zero hg'
  have hden : 2 * (g : ℂ) * ((g : ℂ) - (d : ℂ) * I) ≠ 0 :=
    mul_ne_zero h2g (hgd_ne d g hg)
  unfold yPin
  rw [hsub_matched d g, div_eq_div_iff hden h2g]
  push_cast
  linear_combination (2 * (g : ℂ) * (d : ℂ) ^ 2) * Complex.I_sq

/-- The conjugate zero μ̄ = δ - iγ has weight `(γ - iδ)/(2γ)`. -/
theorem matched_y_conj (hg : g ≠ 0) :
    yPin ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) - (g : ℂ) * I)
      = ((g : ℂ) - (d : ℂ) * I) / (2 * (g : ℂ)) := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have h2g : (2 : ℂ) * (g : ℂ) ≠ 0 := mul_ne_zero two_ne_zero hg'
  have hden : 2 * (g : ℂ) * ((g : ℂ) + (d : ℂ) * I) ≠ 0 :=
    mul_ne_zero h2g (hgd_ne' d g hg)
  unfold yPin
  rw [hsub_matched' d g, div_eq_div_iff hden h2g]
  push_cast
  linear_combination (2 * (g : ℂ) * (d : ℂ) ^ 2) * Complex.I_sq

/-- **WEIGHT EXACTLY 1** (round 125: "Treibergewicht EXAKT 1"): the
conjugate pair at the matched pin carries total weight one —
`y(μ) + y(μ̄) = 1`.  This is the round-117 partner identity
y(z) + y(a²/z) = 1 on the circle |z| = a. -/
theorem matched_weight_sum (hg : g ≠ 0) :
    yPin ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) + (g : ℂ) * I)
      + yPin ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) - (g : ℂ) * I) = 1 := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have h2g : (2 : ℂ) * (g : ℂ) ≠ 0 := mul_ne_zero two_ne_zero hg'
  rw [matched_y d g hg, matched_y_conj d g hg, ← add_div,
    div_eq_one_iff_eq h2g]
  ring

/-- The matched weight has real part exactly 1/2 (the fire-logic
coefficient: the pair's m = 0 cell reads 2·Re y* = 1). -/
theorem matched_y_re (hg : g ≠ 0) :
    (yPin ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) + (g : ℂ) * I)).re
      = 1 / 2 := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have hy := matched_y d g hg
  have : (((g : ℂ) + (d : ℂ) * I) / (2 * (g : ℂ))).re = 1 / 2 := by
    rw [Complex.div_re]
    simp [Complex.normSq, Complex.mul_re, Complex.mul_im]
    field_simp
  rw [hy, this]

/-- **THE MATCHED RATE IS EXACTLY REAL** (round 125: "v* = 1 + eps
EXAKT REELL am matched Pin"): v* = 4y*(1-y*) = 1 + δ²/γ² = 1 + ε
with ε = δ²/γ² the excess. -/
theorem matched_v (hg : g ≠ 0) :
    vRate ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ((d : ℂ) + (g : ℂ) * I)
      = ((1 + d ^ 2 / g ^ 2 : ℝ) : ℂ) := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have hne : ((d ^ 2 + g ^ 2 : ℝ) : ℂ) ≠ ((d : ℂ) + (g : ℂ) * I) ^ 2 := by
    rw [← sub_ne_zero, hsub_matched d g]
    exact mul_ne_zero (mul_ne_zero two_ne_zero hg') (hgd_ne d g hg)
  rw [vRate_eq_four_w hne, Radius4Algebra.matched_w d g hg]
  push_cast
  field_simp
  ring

/-- **THE STRICT RATE EXCESS** (the fire criterion's algebraic
floor): 1 < 1 + δ²/γ² whenever δ ≠ 0 — the matched rate of an
off-line zero strictly exceeds every on-line rate ceiling. -/
theorem matched_v_gt_one (hd : d ≠ 0) (hg : g ≠ 0) :
    1 < 1 + d ^ 2 / g ^ 2 := by
  have hg2 : 0 < g ^ 2 :=
    lt_of_le_of_ne (sq_nonneg g) (Ne.symm (pow_ne_zero 2 hg))
  have hd2 : 0 < d ^ 2 :=
    lt_of_le_of_ne (sq_nonneg d) (Ne.symm (pow_ne_zero 2 hd))
  have : 0 < d ^ 2 / g ^ 2 := div_pos hd2 hg2
  linarith

end Matched

/-! ### The on-line contrast -/

/-- The on-line dictionary (round 125 `dscaled_pair`, d = 0 branch):
an on-line zero has real weight y = a/(a+γ²), and its rate
4y(1-y) is exactly 4·wOnLine a γ. -/
theorem onLine_y_v (a g : ℝ) (h : a + g ^ 2 ≠ 0) :
    4 * (a / (a + g ^ 2)) * (1 - a / (a + g ^ 2))
      = 4 * Radius4Algebra.wOnLine a g := by
  unfold Radius4Algebra.wOnLine
  field_simp
  ring

/-- On-line rates are strictly positive (γ ≠ 0): the on-line stream
never vanishes, it only decays. -/
theorem onLine_rate_pos {a g : ℝ} (ha : 0 < a) (hg : g ≠ 0) :
    0 < 4 * Radius4Algebra.wOnLine a g := by
  have hg2 : 0 < g ^ 2 :=
    lt_of_le_of_ne (sq_nonneg g) (Ne.symm (pow_ne_zero 2 hg))
  have hnum : 0 < a * g ^ 2 := mul_pos ha hg2
  have hden : 0 < (a + g ^ 2) ^ 2 := by positivity
  have : 0 < Radius4Algebra.wOnLine a g := div_pos hnum hden
  linarith

/-- **On-line rates never exceed one** (round 125:
"v = 4y(1-y) ∈ (0,1]"): 4·wOnLine a γ ≤ 1 — pure on-line spectra
give monotone non-increasing diagonal streams, so a certified
increase is an off-line detection. -/
theorem onLine_rate_le_one {a : ℝ} (ha : 0 < a) (g : ℝ) :
    4 * Radius4Algebra.wOnLine a g ≤ 1 := by
  have := Radius4Algebra.wOnLine_le_quarter ha g
  linarith

end MatchedPin
end TfptCarrier
