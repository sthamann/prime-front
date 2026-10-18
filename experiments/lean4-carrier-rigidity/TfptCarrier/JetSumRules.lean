/-
  JetSumRules — the round-135/154 jet sum rules, K = 2 exact.
  ===========================================================

  Lean seam of rounds 135 and 154 (PRIME.HPIN.FLOOR.01 /
  PRIME.NEAR.ALIGN.01; contract PRIME.THEOREMS.LEAN2.01, second
  hardening round): THEOREM D2 of
  `experiments/tfpt-discovery/hpin_floor_probe.py` and THEOREM P5 of
  `experiments/tfpt-discovery/nearalign_probe.py` — the
  reciprocal-derivative sum rules of F(y) = A₀ + Σ_k w_k/(y − b_k),
  proven EXACTLY at the fixed lattice size K = 2 (each verified
  sympy-exactly before formalization), with the general-K residue
  forms packaged behind the SVSkeleton-style honesty lock.

  The K = 2 data: lattice b₁ ≠ b₂ with weights w₁, w₂, census roots
  y₁ ≠ y₂ of the numerator polynomial, entering through the two
  Vieta relations (the coefficient match of
  A₀(X−y₁)(X−y₂) = A₀(X−b₁)(X−b₂) + w₁(X−b₂) + w₂(X−b₁)):
    w₁ + w₂       = A₀(b₁+b₂−y₁−y₂)        (A₂ relation)
    w₁b₂ + w₂b₁   = A₀(b₁b₂−y₁y₂)          (constant relation).
  Jets: A₂ = w₁+w₂, A₄ = w₁b₁+w₂b₂.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `spacing_two` — the K = 2 instance of the D1 spacing form:
        F′(y₁) = A₀(y₁−y₂)/((y₁−b₁)(y₁−b₂)) (the general-K form is
        proven in `SpacingProduct`).

    (2) `sum_rule_first` (D2): Σ_j 1/F′(y_j) = −A₂/A₀².

    (3) `sum_rule_second` (D2): Σ_j y_j/F′(y_j) = −A₄/A₀² + A₂²/A₀³.

    (4) `sum_rule_jet` (P5, first display):
        Σ_j F″(y_j)/F′(y_j)³ = 2A₂/A₀³.

    (5) `sum_rule_jet_second` (P5, second display):
        Σ_j [1/F′(y_j)² − y_j F″(y_j)/F′(y_j)³] = 3A₂²/A₀⁴ − 2A₄/A₀³.

    (6) `JetSumRuleSkeleton` — THE GENERAL-K FORMS AS A TYPED
        HYPOTHESIS PACKAGE (the SVSkeleton discipline): the
        residue-calculus step (contour integration of 1/F, y/F and
        1/F², y/F² over large circles — cited, NOT proven) is a
        NAMED HYPOTHESIS; `jet_sum_rules_conditional` composes it;
        `jetSkeleton_inhabited` shows consistency and
        `jetSkeleton_not_unconditional` — THE HONESTY LOCK — shows
        the package alone proves NO sum-rule statement.

  THE HONEST BOUNDARY.  The kernel-checked content is exact field
  algebra at K = 2 (every K = 2 statement below is proven for an
  arbitrary field, no ordering used).  The general-K sum rules need
  the residue theorem on 1/F, y/F², … over expanding contours —
  that classical step is a NAMED HYPOTHESIS of the skeleton, never
  an axiom.  The identification of (b, w) with the frozen anchor
  lattice, the F′-sign census (MIXED, measured), the out-of-zone
  localization of the sum-rule mass, and the D2s sign-uniform floor
  remain the probe's measured content.  No RH claim in any
  direction.
-/
import Mathlib.Tactic

namespace TfptCarrier
namespace JetSumRules

variable {F : Type*} [Field F]

/-- The K = 2 weight-form secular derivative
`F′(y) = −(w₁/(y−b₁)² + w₂/(y−b₂)²)`. -/
noncomputable def fprime (b1 b2 w1 w2 y : F) : F :=
  -(w1 / (y - b1) ^ 2 + w2 / (y - b2) ^ 2)

/-- The K = 2 weight-form second derivative
`F″(y) = 2(w₁/(y−b₁)³ + w₂/(y−b₂)³)`. -/
noncomputable def fsecond (b1 b2 w1 w2 y : F) : F :=
  2 * (w1 / (y - b1) ^ 3 + w2 / (y - b2) ^ 3)

section RulesTwo

variable {A0 b1 b2 w1 w2 y1 y2 : F}

/-- **The K = 2 spacing form** (round-135 D1 at K = 2; the general
form is `SpacingProduct.spacing_product`): under the Vieta
relations, `F′(y₁) = A₀(y₁−y₂)/((y₁−b₁)(y₁−b₂))`. -/
theorem spacing_two (hb : b1 ≠ b2) (h11 : y1 ≠ b1) (h12 : y1 ≠ b2)
    (hsum : w1 + w2 = A0 * (b1 + b2 - y1 - y2))
    (hprod : w1 * b2 + w2 * b1 = A0 * (b1 * b2 - y1 * y2)) :
    fprime b1 b2 w1 w2 y1 = A0 * (y1 - y2) / ((y1 - b1) * (y1 - b2)) := by
  have hb' : b2 - b1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hb)
  have hw1' : w1 = (A0 * (b1 * b2 - y1 * y2)
      - b1 * (A0 * (b1 + b2 - y1 - y2))) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination hprod - b1 * hsum
  have hw2' : w2 = (b2 * (A0 * (b1 + b2 - y1 - y2))
      - A0 * (b1 * b2 - y1 * y2)) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination b2 * hsum - hprod
  subst hw1' hw2'
  unfold fprime
  have h1 : y1 - b1 ≠ 0 := sub_ne_zero.mpr h11
  have h2 : y1 - b2 ≠ 0 := sub_ne_zero.mpr h12
  field_simp
  ring

/-- **THE FIRST JET SUM RULE** (round-135 D2):
`1/F′(y₁) + 1/F′(y₂) = −A₂/A₀²` with A₂ = w₁ + w₂ — the
reciprocal-floor mass is one jet, exactly. -/
theorem sum_rule_first (hb : b1 ≠ b2) (hA0 : A0 ≠ 0) (hy : y1 ≠ y2)
    (h11 : y1 ≠ b1) (h12 : y1 ≠ b2) (h21 : y2 ≠ b1) (h22 : y2 ≠ b2)
    (hsum : w1 + w2 = A0 * (b1 + b2 - y1 - y2))
    (hprod : w1 * b2 + w2 * b1 = A0 * (b1 * b2 - y1 * y2)) :
    1 / fprime b1 b2 w1 w2 y1 + 1 / fprime b1 b2 w1 w2 y2
      = -((w1 + w2) / A0 ^ 2) := by
  rw [spacing_two hb h11 h12 hsum hprod,
    spacing_two (A0 := A0) (y2 := y1) hb h21 h22
      (by linear_combination hsum) (by linear_combination hprod),
    hsum]
  have h1 : y1 - b1 ≠ 0 := sub_ne_zero.mpr h11
  have h2 : y1 - b2 ≠ 0 := sub_ne_zero.mpr h12
  have h3 : y2 - b1 ≠ 0 := sub_ne_zero.mpr h21
  have h4 : y2 - b2 ≠ 0 := sub_ne_zero.mpr h22
  have h5 : y1 - y2 ≠ 0 := sub_ne_zero.mpr hy
  have h6 : y2 - y1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hy)
  field_simp
  ring

/-- **THE SECOND JET SUM RULE** (round-135 D2):
`y₁/F′(y₁) + y₂/F′(y₂) = −A₄/A₀² + A₂²/A₀³` with
A₄ = w₁b₁ + w₂b₂. -/
theorem sum_rule_second (hb : b1 ≠ b2) (hA0 : A0 ≠ 0) (hy : y1 ≠ y2)
    (h11 : y1 ≠ b1) (h12 : y1 ≠ b2) (h21 : y2 ≠ b1) (h22 : y2 ≠ b2)
    (hsum : w1 + w2 = A0 * (b1 + b2 - y1 - y2))
    (hprod : w1 * b2 + w2 * b1 = A0 * (b1 * b2 - y1 * y2)) :
    y1 / fprime b1 b2 w1 w2 y1 + y2 / fprime b1 b2 w1 w2 y2
      = -((w1 * b1 + w2 * b2) / A0 ^ 2) + (w1 + w2) ^ 2 / A0 ^ 3 := by
  have hA4 : w1 * b1 + w2 * b2
      = (b1 + b2) * (A0 * (b1 + b2 - y1 - y2))
        - A0 * (b1 * b2 - y1 * y2) := by
    linear_combination (b1 + b2) * hsum - hprod
  rw [spacing_two hb h11 h12 hsum hprod,
    spacing_two (A0 := A0) (y2 := y1) hb h21 h22
      (by linear_combination hsum) (by linear_combination hprod),
    hA4, hsum]
  have h1 : y1 - b1 ≠ 0 := sub_ne_zero.mpr h11
  have h2 : y1 - b2 ≠ 0 := sub_ne_zero.mpr h12
  have h3 : y2 - b1 ≠ 0 := sub_ne_zero.mpr h21
  have h4 : y2 - b2 ≠ 0 := sub_ne_zero.mpr h22
  have h5 : y1 - y2 ≠ 0 := sub_ne_zero.mpr hy
  have h6 : y2 - y1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hy)
  field_simp
  ring

/-- **THE JET-CURVATURE SUM RULE** (round-154 P5, first display):
`F″(y₁)/F′(y₁)³ + F″(y₂)/F′(y₂)³ = 2A₂/A₀³`. -/
theorem sum_rule_jet (hb : b1 ≠ b2) (hA0 : A0 ≠ 0) (hy : y1 ≠ y2)
    (h11 : y1 ≠ b1) (h12 : y1 ≠ b2) (h21 : y2 ≠ b1) (h22 : y2 ≠ b2)
    (hsum : w1 + w2 = A0 * (b1 + b2 - y1 - y2))
    (hprod : w1 * b2 + w2 * b1 = A0 * (b1 * b2 - y1 * y2)) :
    fsecond b1 b2 w1 w2 y1 / fprime b1 b2 w1 w2 y1 ^ 3
        + fsecond b1 b2 w1 w2 y2 / fprime b1 b2 w1 w2 y2 ^ 3
      = 2 * (w1 + w2) / A0 ^ 3 := by
  have hb' : b2 - b1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hb)
  have hw1' : w1 = (A0 * (b1 * b2 - y1 * y2)
      - b1 * (A0 * (b1 + b2 - y1 - y2))) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination hprod - b1 * hsum
  have hw2' : w2 = (b2 * (A0 * (b1 + b2 - y1 - y2))
      - A0 * (b1 * b2 - y1 * y2)) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination b2 * hsum - hprod
  rw [spacing_two hb h11 h12 hsum hprod,
    spacing_two (A0 := A0) (y2 := y1) hb h21 h22
      (by linear_combination hsum) (by linear_combination hprod),
    hsum]
  subst hw1' hw2'
  unfold fsecond
  have h1 : y1 - b1 ≠ 0 := sub_ne_zero.mpr h11
  have h2 : y1 - b2 ≠ 0 := sub_ne_zero.mpr h12
  have h3 : y2 - b1 ≠ 0 := sub_ne_zero.mpr h21
  have h4 : y2 - b2 ≠ 0 := sub_ne_zero.mpr h22
  have h5 : y1 - y2 ≠ 0 := sub_ne_zero.mpr hy
  have h6 : y2 - y1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hy)
  field_simp
  ring

/-- **THE SECOND-ORDER ℓ² SUM RULE** (round-154 P5, second display):
`Σ_j [1/F′(y_j)² − y_j F″(y_j)/F′(y_j)³] = 3A₂²/A₀⁴ − 2A₄/A₀³` —
the root-side ℓ² mass is jets plus an F″-weighted sum, still
jet-class data. -/
theorem sum_rule_jet_second (hb : b1 ≠ b2) (hA0 : A0 ≠ 0)
    (hy : y1 ≠ y2)
    (h11 : y1 ≠ b1) (h12 : y1 ≠ b2) (h21 : y2 ≠ b1) (h22 : y2 ≠ b2)
    (hsum : w1 + w2 = A0 * (b1 + b2 - y1 - y2))
    (hprod : w1 * b2 + w2 * b1 = A0 * (b1 * b2 - y1 * y2)) :
    (1 / fprime b1 b2 w1 w2 y1 ^ 2
        - y1 * fsecond b1 b2 w1 w2 y1 / fprime b1 b2 w1 w2 y1 ^ 3)
      + (1 / fprime b1 b2 w1 w2 y2 ^ 2
        - y2 * fsecond b1 b2 w1 w2 y2 / fprime b1 b2 w1 w2 y2 ^ 3)
      = 3 * (w1 + w2) ^ 2 / A0 ^ 4
        - 2 * (w1 * b1 + w2 * b2) / A0 ^ 3 := by
  have hb' : b2 - b1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hb)
  have hw1' : w1 = (A0 * (b1 * b2 - y1 * y2)
      - b1 * (A0 * (b1 + b2 - y1 - y2))) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination hprod - b1 * hsum
  have hw2' : w2 = (b2 * (A0 * (b1 + b2 - y1 - y2))
      - A0 * (b1 * b2 - y1 * y2)) / (b2 - b1) := by
    rw [eq_div_iff hb']
    linear_combination b2 * hsum - hprod
  have hA4 : w1 * b1 + w2 * b2
      = (b1 + b2) * (A0 * (b1 + b2 - y1 - y2))
        - A0 * (b1 * b2 - y1 * y2) := by
    linear_combination (b1 + b2) * hsum - hprod
  rw [spacing_two hb h11 h12 hsum hprod,
    spacing_two (A0 := A0) (y2 := y1) hb h21 h22
      (by linear_combination hsum) (by linear_combination hprod),
    hA4, hsum]
  subst hw1' hw2'
  unfold fsecond
  have h1 : y1 - b1 ≠ 0 := sub_ne_zero.mpr h11
  have h2 : y1 - b2 ≠ 0 := sub_ne_zero.mpr h12
  have h3 : y2 - b1 ≠ 0 := sub_ne_zero.mpr h21
  have h4 : y2 - b2 ≠ 0 := sub_ne_zero.mpr h22
  have h5 : y1 - y2 ≠ 0 := sub_ne_zero.mpr hy
  have h6 : y2 - y1 ≠ 0 := sub_ne_zero.mpr (Ne.symm hy)
  field_simp
  ring

end RulesTwo

/-! ### The general-K sum rules and their honesty lock -/

/-- **THE GENERAL-K JET SUM RULES AS A TYPED HYPOTHESIS PACKAGE** —
every field is a NAMED HYPOTHESIS with its citation; none is proven
here (the SVSkeleton discipline).  The `Prop` parameters keep the
package fully abstract: nothing about lattices, contours, or ζ is
smuggled into the kernel. -/
structure JetSumRuleSkeleton where
  /-- The spacing form F′(y_j) = A₀·∏(y_j−y_i)/∏(y_j−b_k) at every
  simple census root (its general-K statement IS kernel-checked:
  `SpacingProduct.spacing_product`; this node cites it). -/
  SpacingForm : Prop
  /-- The residue-calculus step (cited, NOT proven): contour
  integration of 1/F, y/F, 1/F², y/F² over expanding circles with
  vanishing outer contribution — the classical hull of D2/P5. -/
  ResidueCalculus : Prop
  /-- The general-K first sum rule Σ_j 1/F′(y_j) = −A₂/A₀². -/
  SumRuleFirst : Prop
  /-- The general-K second sum rule
  Σ_j y_j/F′(y_j) = −A₄/A₀² + A₂²/A₀³. -/
  SumRuleSecond : Prop
  /-- The general-K jet-curvature rules (P5 family). -/
  SumRuleJet : Prop
  /-- NAMED HYPOTHESIS: spacing form + residue calculus give all
  three general-K rules. -/
  residue_step : SpacingForm → ResidueCalculus →
    SumRuleFirst ∧ SumRuleSecond ∧ SumRuleJet

/-- **The composition** — the only theorem the skeleton yields, with
its conditionality fully visible in the type. -/
theorem jet_sum_rules_conditional (S : JetSumRuleSkeleton)
    (hsp : S.SpacingForm) (hres : S.ResidueCalculus) :
    S.SumRuleFirst ∧ S.SumRuleSecond ∧ S.SumRuleJet :=
  S.residue_step hsp hres

/-- Non-vacuity: the package is consistent (inhabited with all
nodes True). -/
theorem jetSkeleton_inhabited : Nonempty JetSumRuleSkeleton :=
  ⟨{ SpacingForm := True, ResidueCalculus := True,
     SumRuleFirst := True, SumRuleSecond := True, SumRuleJet := True,
     residue_step := fun _ _ => ⟨trivial, trivial, trivial⟩ }⟩

/-- **THE HONESTY LOCK**: the skeleton proves nothing
unconditionally — there is an instance whose sum-rule conclusions
are False (all nodes False, the implication vacuous).  The
general-K rules must enter through the kernel-checked spacing form
AND the named residue-calculus hull, never from the packaging. -/
theorem jetSkeleton_not_unconditional :
    ∃ S : JetSumRuleSkeleton,
      ¬ S.SumRuleFirst ∧ ¬ S.ResidueCalculus :=
  ⟨{ SpacingForm := False, ResidueCalculus := False,
     SumRuleFirst := False, SumRuleSecond := False,
     SumRuleJet := False,
     residue_step := fun h _ => h.elim },
   fun h => h, fun h => h⟩

end JetSumRules
end TfptCarrier
