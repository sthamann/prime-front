/-
  CofinalPredefinition — honest hardening of the cofinal-index API.
  =================================================================

  `CofinalWeil.CofinalHypothesis A` contains exactly the mathematical
  payload needed by the limit theorem: an index sequence, strict
  monotonicity, and PSD on the selected rungs.  It does NOT encode the
  computational provenance of that index sequence.  In particular,
  Lean's ordinary binder order and structure-field order do not stop a
  producer from first inspecting `A` and then constructing `idx`.

  This module makes that boundary explicit without pretending that
  dependent type theory tracks information flow automatically:

    * `cofinal_weil_for_fixed_idx` states the mathematical theorem for
      an arbitrary explicit index parameter.  This prevents the theorem
      body itself from choosing a ladder, but says nothing about how a
      caller produced the parameter.

    * `NoninterferenceContract` is an ABSTRACT external audit relation.
      `PredefinedCofinalHypothesis` adds a named proof of that relation
      to the mathematical core, and `cofinal_weil_predefined` is the
      hardened public wrapper.  The repository deliberately supplies no
      universal implementation of `Predefined`: doing so requires a
      formal source/construction language or another trusted provenance
      boundary.

    * `old_api_accepts_sign_mined_idx` is the negative test requested by
      the audit: the old mathematical payload accepts a selector that
      branches on signs.

    * `signMinedIndex_not_familyNoninterfering` shows that the exposed
      sign-mining selector fails the natural extensional
      noninterference predicate.

    * `constantizedSelector_familyNoninterfering` and
      `constantizedSelector_agrees` prove the residual metatheoretic
      limitation: once only the resulting function value is retained,
      any selector can be replaced at one observed family by a constant
      selector with the same output.  Extensional types therefore cannot
      recover construction history.  A DSL, an effect system, or an
      externally audited source boundary is required for the intended
      algorithmic claim.

  No RH statement is present.  The only mathematical conclusion remains
  the conditional cofinal-limit implication already proved in
  `CofinalWeil`.
-/
import TfptCarrier.CofinalWeil

namespace TfptCarrier
namespace CofinalPredefinition

open Filter Topology Matrix CofinalWeil

/-- A ladder index sequence, cofinal in the mesh-refinement order of
`CofinalWeil.CofinalHypothesis` (the order in which `hconv` holds). -/
abbrev IndexSequence := ℕ → ℕ

/-- The matrix family consumed by the cofinal extraction theorem. -/
abbrev MatrixFamily (κ : ℕ → Type*) [∀ m, Fintype (κ m)] :=
  ∀ m, Matrix (κ m) (κ m) ℝ

/-- **EXTERNAL NONINTERFERENCE CONTRACT.**

`Predefined A idx` is intentionally abstract.  A concrete application
must supply its meaning and its proof; this module does not identify
ordinary quantifier order with computational independence. -/
structure NoninterferenceContract (κ : ℕ → Type*)
    [∀ m, Fintype (κ m)] where
  Predefined : MatrixFamily κ → IndexSequence → Prop

/-- The hardened cofinal hypothesis: the old mathematical payload plus
an explicit certificate for the application's external noninterference
contract.  The field is load-bearing audit metadata even though the
limit proof uses only `core`. -/
structure PredefinedCofinalHypothesis {κ : ℕ → Type*}
    [∀ m, Fintype (κ m)] (contract : NoninterferenceContract κ)
    (A : MatrixFamily κ) where
  core : CofinalHypothesis A
  noninterference : contract.Predefined A core.idx

/-- The mathematical extraction theorem with `idx` an explicit
parameter.  Binder order prevents this theorem body from selecting an
index, but does NOT prove that the caller computed `idx` independently
of `A` or its signs. -/
theorem cofinal_weil_for_fixed_idx {κ : ℕ → Type*}
    [∀ m, Fintype (κ m)] {V : Type*}
    (idx : IndexSequence) (hmono : StrictMono idx)
    (A : MatrixFamily κ) (hpsd : ∀ j, (A (idx j)).PosSemidef)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    (∀ j v, 0 ≤ ladderForm A sample (idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  cofinal_weil ⟨idx, hmono, hpsd⟩ sample QW hconv

/-- **HARDENED PUBLIC API.**  The cofinal implication with PREDEFINED
represented by an explicit, named contract certificate.  Lean checks
the implication and the presence/type of the certificate; the intended
algorithmic meaning of the abstract contract remains an external audit
premise until the construction language is formalized. -/
theorem cofinal_weil_predefined {κ : ℕ → Type*}
    [∀ m, Fintype (κ m)] {V : Type*}
    {contract : NoninterferenceContract κ} {A : MatrixFamily κ}
    (H : PredefinedCofinalHypothesis contract A)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    (∀ j v, 0 ≤ ladderForm A sample (H.core.idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (H.core.idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  cofinal_weil H.core sample QW hconv

/-! ### Negative test: the old payload accepts sign mining -/

/-- A selector that reads the sign at the even candidate and chooses
the even or odd member of that pair accordingly. -/
noncomputable def signMinedIndex (margin : ℕ → ℝ) : IndexSequence :=
  fun j => if 0 ≤ margin (2 * j) then 2 * j else 2 * j + 1

/-- The sign-mined selector is strictly monotone for every input:
selected rung `j` lies in `{2j, 2j+1}`. -/
theorem signMinedIndex_strictMono (margin : ℕ → ℝ) :
    StrictMono (signMinedIndex margin) := by
  intro a b hab
  simp only [signMinedIndex]
  split <;> split <;> omega

/-- Alternating signs: the even member of every pair is positive and
the odd member is negative. -/
def alternatingMargin (m : ℕ) : ℝ :=
  if Even m then 1 else -1

/-- **OLD-API COUNTEREXAMPLE.**  `IsCofinalWitness` (the scalar payload
of the original `CofinalHypothesis`) accepts an index whose constructor
explicitly inspects the measured sign.  This is not a counterexample to
the limit theorem; it is a counterexample to the former prose claim that
the type itself enforced preregistration. -/
theorem old_api_accepts_sign_mined_idx :
    IsCofinalWitness alternatingMargin
      (signMinedIndex alternatingMargin) := by
  constructor
  · exact signMinedIndex_strictMono alternatingMargin
  · intro j
    simp [signMinedIndex, alternatingMargin]

/-! ### What extensional noninterference can and cannot express -/

/-- A selector is extensionally family-independent when changing the
entire input family cannot change its returned index sequence. -/
def FamilyNoninterfering {Family : Type*}
    (selector : Family → IndexSequence) : Prop :=
  ∀ A B, selector A = selector B

/-- The actual sign-mining selector fails extensional
family-noninterference. -/
theorem signMinedIndex_not_familyNoninterfering :
    ¬ FamilyNoninterfering signMinedIndex := by
  intro h
  have h0 := congrFun (h (fun _ => (1 : ℝ)) (fun _ => (-1 : ℝ))) 0
  norm_num [signMinedIndex] at h0

/-- Freeze any selector at one observed family.  The resulting selector
is extensionally independent because it ignores its explicit input. -/
def constantizedSelector {Family : Type*} (A₀ : Family)
    (selector : Family → IndexSequence) : Family → IndexSequence :=
  fun _ => selector A₀

/-- Constantization always passes extensional family independence. -/
theorem constantizedSelector_familyNoninterfering {Family : Type*}
    (A₀ : Family) (selector : Family → IndexSequence) :
    FamilyNoninterfering (constantizedSelector A₀ selector) := by
  intro A B
  rfl

/-- At the observed family, constantization returns exactly the original
selector's value.  Hence extensional equality at one produced `idx`
cannot reveal whether the historical producer inspected signs. -/
theorem constantizedSelector_agrees {Family : Type*} (A₀ : Family)
    (selector : Family → IndexSequence) :
    constantizedSelector A₀ selector A₀ = selector A₀ :=
  rfl

end CofinalPredefinition
end TfptCarrier
