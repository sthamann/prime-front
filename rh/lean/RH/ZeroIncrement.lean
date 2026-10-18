-- RH/ZeroIncrement.lean -- r546 local zero-count increment bound.
--
-- CLAIM BOUNDARY: sorry-free classical zero-count bookkeeping only.
-- This module makes no claim for or against the Riemann Hypothesis.
--
-- r547: owns `gaborZeroCount` so `RH.GaborSeparation` can import this
-- file without a cycle.  Path A increment is proved; Trudgian remains
-- an inactive Path B Prop in `RH.GaborSeparation`.

import RH.ExternalBridges

namespace RH

open Set Complex Classical

/-- Zero-counting function for positive ordinates of nontrivial zeta zeros.
`Set.ncard` keeps the statement independent of a nonexistent Mathlib
`ZetaZero` enumeration API. -/
noncomputable def gaborZeroCount (T : ℝ) : ℕ :=
  Set.ncard {s : ℂ | IsNontrivialRiemannZetaZero s ∧ 0 < s.im ∧ s.im ≤ T}

/-- A positive-ordinate nontrivial zero lies in the open critical strip.
The left-half-plane case is excluded by the functional equation: a zero
there with nonzero imaginary part would reflect into the zero-free half-plane
`re ≥ 1`; the boundary lines are zero-free as well. -/
lemma nontrivialZero_re_mem_Ioo {s : ℂ}
    (hs : IsNontrivialRiemannZetaZero s) (him : 0 < s.im) :
    s.re ∈ Set.Ioo (0 : ℝ) 1 := by
  constructor
  · by_contra h
    have hre : s.re ≤ 0 := le_of_not_gt h
    rcases lt_or_eq_of_le hre with hlt | heq
    · exact (ne_of_gt him) (riemannZeta_eq_zero_im_eq_zero_of_re_lt_zero hlt hs.1)
    · exact (riemannZeta_ne_zero_of_re_eq_zero heq) hs.1
  · by_contra h
    exact riemannZeta_ne_zero_of_one_le_re (le_of_not_gt h) hs.1

/-- The positive-ordinate nontrivial zeros up to any real height are finite. -/
lemma gaborZeroCount_finite :
    ∀ T : ℝ,
      {s : ℂ | IsNontrivialRiemannZetaZero s ∧ 0 < s.im ∧ s.im ≤ T}.Finite := by
  intro T
  refine (finite_riemannZeta_zeros_on_closedRect 0 1 |T|).subset ?_
  intro s hs
  have hstrip := nontrivialZero_re_mem_Ioo hs.1 hs.2.1
  have himlo : -|T| ≤ s.im := by
    have : 0 ≤ |T| := abs_nonneg T
    linarith [hs.2.1]
  have himhi : s.im ≤ |T| := hs.2.2.trans (le_abs_self T)
  refine ⟨mem_zetaClosedRect.mpr
    ⟨le_of_lt hstrip.1, le_of_lt hstrip.2, himlo, himhi⟩, hs.1.1, hs.1.2.2⟩

/-- Finset presentation of `gaborZeroCount`; this is the finite set selected
by exactly the predicate used in the public `Set.ncard` definition. -/
noncomputable def gaborZerosUpTo (T : ℝ) : Finset ℂ :=
  (gaborZeroCount_finite T).toFinset

lemma mem_gaborZerosUpTo {T : ℝ} {s : ℂ} :
    s ∈ gaborZerosUpTo T ↔
      IsNontrivialRiemannZetaZero s ∧ 0 < s.im ∧ s.im ≤ T :=
  Set.Finite.mem_toFinset _

/-- The `Set.ncard` zero count is the card of its matching finite witness. -/
lemma gaborZeroCount_eq_card (T : ℝ) :
    gaborZeroCount T = (gaborZerosUpTo T).card := by
  unfold gaborZeroCount gaborZerosUpTo
  exact Set.ncard_eq_toFinset_card _ (gaborZeroCount_finite T)

lemma gaborZerosUpTo_mono {T U : ℝ} (hTU : T ≤ U) :
    gaborZerosUpTo T ⊆ gaborZerosUpTo U := by
  intro s hs
  rw [mem_gaborZerosUpTo] at hs ⊢
  exact ⟨hs.1, hs.2.1, hs.2.2.trans hTU⟩

lemma gaborZerosUpTo_sdiff_subset_unit (T : ℝ) :
    gaborZerosUpTo (T + 1) \ gaborZerosUpTo T ⊆
      (riemannZetaZerosOnClosedRect 0 1 (T + 1)).filter
        (fun z => T ≤ z.im ∧ z.im ≤ T + 1) := by
  intro s hs
  obtain ⟨hsTop, hsOld⟩ := Finset.mem_sdiff.mp hs
  rw [mem_gaborZerosUpTo] at hsTop
  have hstrip := nontrivialZero_re_mem_Ioo hsTop.1 hsTop.2.1
  have himlo : T ≤ s.im := by
    by_contra h
    have hsT : s.im ≤ T := le_of_not_ge h
    exact hsOld (mem_gaborZerosUpTo.mpr ⟨hsTop.1, hsTop.2.1, hsT⟩)
  have hrect : s ∈ riemannZetaZerosOnClosedRect 0 1 (T + 1) := by
    apply mem_riemannZetaZerosOnClosedRect.mpr
    refine ⟨mem_zetaClosedRect.mpr
      ⟨le_of_lt hstrip.1, le_of_lt hstrip.2, ?_, hsTop.2.2⟩,
      hsTop.1.1, hsTop.1.2.2⟩
    linarith [hsTop.2.1]
  exact Finset.mem_filter.mpr ⟨hrect, himlo, hsTop.2.2⟩

/-- Unit increments are stated after casting the natural subtraction to
`ℝ`.  This preserves the exact `gaborZeroCount` API while giving downstream
analytic estimates a coercion-free real inequality. -/
theorem zeta_unit_increment :
    ∃ C : ℝ, 0 < C ∧
      ∀ T : ℝ, Real.exp 1 ≤ T →
        ((gaborZeroCount (T + 1) - gaborZeroCount T : ℕ) : ℝ) ≤
          C * (1 + Real.log (T + 3)) := by
  refine ⟨2 * zetaZerosInDiskCardBoundInner, ?_, ?_⟩
  · exact mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos
  intro T hT
  have hmono := gaborZerosUpTo_mono
    (T := T) (U := T + 1) (by linarith)
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
          (fun z => T ≤ z.im ∧ z.im ≤ T + 1)).card : ℝ) := by
    exact_mod_cast hcard
  have harg : 2 + T + 1 = T + 3 := by ring
  rw [harg] at hwindow
  exact hcast.trans hwindow

/-- Path A (r545/r547, live).  Unit-interval increment with an explicit
constant.  r544: this counting bound is *not* by itself a uniform
Gabor inequality; the remaining work is Gaussian-density transfer and
off-line remainder control.  Trudgian's sharper error term is inactive
Path B (`TrudgianZeroDensityBound`). -/
def GaborIncrementBound : Prop :=
  ∃ C : ℝ, 0 < C ∧
    ∀ T : ℝ, Real.exp 1 ≤ T →
      ((gaborZeroCount (T + 1) - gaborZeroCount T : ℕ) : ℝ) ≤
        C * (1 + Real.log (T + 3))

theorem gaborIncrementBound_holds : GaborIncrementBound :=
  zeta_unit_increment

end RH
