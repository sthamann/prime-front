/-
  SVSkeleton — the (SV) ⇒ RH reduction chain as a typed hypothesis
  package.
  ================================================================

  Lean seam of rounds 92–93 (SVPIN and PRIME.SCREW.VERBLUNSKY.
  INVARIANT.01 V0a/V0c; notes CCCXCIII and the vbk_invariant_probe
  docstring).  The audited backward chain there is:

    (SV)  =  pointwise Weyl-disk contraction at the countable pin
             sequence σ_r = 1 + 1/r, plus the one-pin normal-family
             bound
      ⇒  every finite Euler–Pick section is PSD
      ⇒  (Pick 1916 / Nicolau 2015 Thm 2; Montel/Vitali normal
          families)  a holomorphic positive-real interpolant H exists
          on the right half-plane through the pin data
      ⇒  (identity theorem at the interior accumulation point σ* = 1,
          nonzero logarithmic-derivative residue at any off-line
          zero, functional equation)  the pole contradiction: no
          off-line zero — the RH-shaped conclusion.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `svNode_mem_Ioc` / `svNode_strictAnti` / `svNode_tendsto_one`
        — THE V0a PIN GEOMETRY, proven: the Stieltjes–Vitali nodes
        σ_r = 1 + 1/(r+1) lie in (1, 2], are strictly decreasing, and
        accumulate at 1 — an INTERIOR point of the safe Euler
        half-plane Re z > 1/2.  This is the kernel-checked content of
        the σ-correction: no σ ↓ 1/2 uniformity is demanded anywhere
        in the chain.

    (2) `SVtoRHSkeleton` — the chain as a STRUCTURE whose fields are
        the three named implications, each carrying its citation in
        the docstring; `sv_implies_rh` — the composition: given the
        package and (SV), the conclusion follows.  The quantifier
        structure (what feeds what, in which order) is thereby
        kernel-checked even though the analytic steps are
        hypotheses.

    (3) `skeleton_inhabited` — non-vacuity: the structure has an
        instance (all nodes True), so the package is consistent;
        `skeleton_not_unconditional` — the HONESTY LOCK: there is
        an instance whose conclusion is False (with SV False), so
        the skeleton alone proves NO RH-shaped statement — the
        entire burden sits in (SV) and the named classical inputs.

  THE HONEST BOUNDARY.  The three implication fields are NAMED
  HYPOTHESES in the exact sense of `CofinalWeil`'s (H_cof)
  discipline: nothing here proves Weyl-disk contraction, Pick
  interpolation, Montel/Vitali, the identity theorem, or any property
  of ζ.  The forward algebraic half of the Euler–Pick criterion
  (real ordinates ⇒ finite sections PSD) IS kernel-checked, in
  `TfptCarrier.EulerPick.pickMatrix_posSemidef`; the δ₁ no-go
  (`TfptCarrier.DeltaOneNoGo`) shows why the middle node demands
  STRICT section data beyond pin finiteness for any carrier-based
  route.  No RH claim — the module's own honesty lock proves that
  no unconditional conclusion can be extracted from the package.
-/
import TfptCarrier.EulerPick
import Mathlib.Analysis.SpecificLimits.Basic

namespace TfptCarrier
namespace SVSkeleton

open Filter Topology EulerPick

/-! ### (1) The V0a pin geometry, proven -/

/-- The Stieltjes–Vitali nodes lie in (1, 2]. -/
theorem svNode_mem_Ioc (j : ℕ) : svNode j ∈ Set.Ioc (1 : ℝ) 2 := by
  unfold svNode
  constructor
  · have h : (0 : ℝ) < 1 / ((j : ℝ) + 1) := by positivity
    linarith
  · have h1 : (1 : ℝ) ≤ (j : ℝ) + 1 := by
      have := Nat.cast_nonneg (α := ℝ) j
      linarith
    have h : 1 / ((j : ℝ) + 1) ≤ 1 := by
      rw [div_le_one (by linarith)]
      linarith
    linarith

/-- The nodes are strictly decreasing (fresh information at every
pin). -/
theorem svNode_strictAnti : StrictAnti svNode := by
  intro i j hij
  unfold svNode
  have hi : (0 : ℝ) < (i : ℝ) + 1 := by positivity
  have hj : (0 : ℝ) < (j : ℝ) + 1 := by positivity
  have hcast : (i : ℝ) + 1 < (j : ℝ) + 1 := by
    have := (Nat.cast_lt (α := ℝ)).mpr hij
    linarith
  have := one_div_lt_one_div_of_lt hi hcast
  linarith

/-- **The pins accumulate at the interior point 1** — the
kernel-checked half of the V0a σ-correction: the identification
point of the chain is σ* = 1, strictly inside the safe Euler
half-plane, and no σ ↓ 1/2 limit occurs. -/
theorem svNode_tendsto_one : Tendsto svNode atTop (𝓝 (1 : ℝ)) := by
  have h : Tendsto (fun j : ℕ => 1 / ((j : ℝ) + 1)) atTop (𝓝 0) :=
    tendsto_one_div_add_atTop_nhds_zero_nat
  have h2 : Tendsto (fun j : ℕ => (1 : ℝ) + 1 / ((j : ℝ) + 1)) atTop
      (𝓝 (1 + 0)) := tendsto_const_nhds.add h
  rw [add_zero] at h2
  exact h2.congr fun j => rfl

/-! ### (2) The chain as a typed hypothesis package -/

/-- **THE (SV) ⇒ RH SKELETON** — the backward chain of the Euler–Pick
criterion as a structure.  Every field is a NAMED HYPOTHESIS with its
citation; none is proven here (see module docstring).  The four
`Prop` parameters keep the package fully abstract: nothing about ζ,
zeros, or half-planes is smuggled into the kernel. -/
structure SVtoRHSkeleton where
  /-- The (SV) input: pointwise Weyl-disk contraction at the pins
  σ_r = 1 + 1/r plus the one-pin normal-family bound (SVPIN). -/
  SV : Prop
  /-- The middle node: every finite Euler–Pick section
  [(P(σ_j)+P(σ_k))/(σ_j+σ_k)] is PSD, for every N.  (The FORWARD
  model half — real ordinates ⇒ PSD — is kernel-checked in
  `EulerPick.pickMatrix_posSemidef`; here the node is the abstract
  statement about the actual ξ′/ξ data.) -/
  SectionsPSD : Prop
  /-- The interpolation node: a holomorphic positive-real interpolant
  through the pin data exists on the right half-plane. -/
  InterpolantExists : Prop
  /-- The RH-shaped conclusion (opaque — no zeta content in Lean). -/
  RH : Prop
  /-- NAMED HYPOTHESIS 1 (measure-theory side of SVPIN, cited):
  Weyl-disk contraction at every pin forces PSD of every finite
  section. -/
  sv_to_psd : SV → SectionsPSD
  /-- NAMED HYPOTHESIS 2 (Pick 1916; Nicolau 2015, Theorem 2;
  Montel/VITALI normal families — cited, NOT proven): all-N PSD
  sections solve the countable interpolation problem. -/
  vitali_pick_interpolation : SectionsPSD → InterpolantExists
  /-- NAMED HYPOTHESIS 3 (identity theorem at the accumulation point
  σ* = 1, HURWITZ-type zero/pole control via the nonzero logarithmic
  residue, functional equation — cited, NOT proven): the interpolant
  identifies with the Euler expression and forbids off-line zeros. -/
  hurwitz_identity_pole_step : InterpolantExists → RH

/-- **The composition** — the only theorem the skeleton yields, with
its conditionality fully visible in the type: (SV) plus the three
named classical inputs give the conclusion.  The quantifier structure
of the campaign map is thereby kernel-checked; the analysis is not. -/
theorem sv_implies_rh (S : SVtoRHSkeleton) (hsv : S.SV) : S.RH :=
  S.hurwitz_identity_pole_step (S.vitali_pick_interpolation (S.sv_to_psd hsv))

/-! ### (3) Non-vacuity and the honesty lock -/

/-- Non-vacuity: the package is consistent (inhabited with all nodes
True). -/
theorem skeleton_inhabited : Nonempty SVtoRHSkeleton :=
  ⟨{ SV := True, SectionsPSD := True, InterpolantExists := True,
     RH := True,
     sv_to_psd := fun h => h,
     vitali_pick_interpolation := fun h => h,
     hurwitz_identity_pole_step := fun h => h }⟩

/-- **THE HONESTY LOCK**: the skeleton proves nothing
unconditionally — there is an instance whose conclusion is False
(all nodes False, implications vacuous).  Any RH-shaped output must
therefore enter through (SV) and the named hypotheses, never from
the packaging. -/
theorem skeleton_not_unconditional :
    ∃ S : SVtoRHSkeleton, ¬ S.RH ∧ ¬ S.SV :=
  ⟨{ SV := False, SectionsPSD := False, InterpolantExists := False,
     RH := False,
     sv_to_psd := fun h => h,
     vitali_pick_interpolation := fun h => h,
     hurwitz_identity_pole_step := fun h => h },
   fun h => h, fun h => h⟩

end SVSkeleton
end TfptCarrier
