/- Prime Front: original cofinal theorem signature locks, unchanged. -/
import TfptCarrier.CofinalPredefinition

namespace TFPT.Carrier.AuditContract

/-- The mathematical cofinal theorem is available for an arbitrary
    explicit fixed `idx`; this signature does not claim that binder
    order proves computational independence. -/
example {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}
    (idx : ℕ → ℕ) (hmono : StrictMono idx)
    (A : TfptCarrier.CofinalPredefinition.MatrixFamily κ)
    (hpsd : ∀ j, (A (idx j)).PosSemidef)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Filter.Tendsto
      (fun m => TfptCarrier.CofinalWeil.ladderForm A sample m v)
      Filter.atTop (nhds (QW v))) :
    (∀ j v, 0 ≤ TfptCarrier.CofinalWeil.ladderForm A sample (idx j) v) ∧
    (∀ v, Filter.Tendsto
      (fun j => TfptCarrier.CofinalWeil.ladderForm A sample (idx j) v)
      Filter.atTop (nhds (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  TfptCarrier.CofinalPredefinition.cofinal_weil_for_fixed_idx
    idx hmono A hpsd sample QW hconv

/-- Hardened cofinal API: the exact same implication additionally
    consumes the explicit PREDEFINED/noninterference contract field. -/
example {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}
    {contract : TfptCarrier.CofinalPredefinition.NoninterferenceContract κ}
    {A : TfptCarrier.CofinalPredefinition.MatrixFamily κ}
    (H : TfptCarrier.CofinalPredefinition.PredefinedCofinalHypothesis
      contract A)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Filter.Tendsto
      (fun m => TfptCarrier.CofinalWeil.ladderForm A sample m v)
      Filter.atTop (nhds (QW v))) :
    (∀ j v, 0 ≤ TfptCarrier.CofinalWeil.ladderForm
      A sample (H.core.idx j) v) ∧
    (∀ v, Filter.Tendsto
      (fun j => TfptCarrier.CofinalWeil.ladderForm
        A sample (H.core.idx j) v)
      Filter.atTop (nhds (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  TfptCarrier.CofinalPredefinition.cofinal_weil_predefined
    H sample QW hconv

/-- Negative audit lock: the old scalar payload accepts a sign-mined
    selector, while the exposed selector fails extensional
    family-noninterference. -/
example :
    TfptCarrier.CofinalWeil.IsCofinalWitness
      TfptCarrier.CofinalPredefinition.alternatingMargin
      (TfptCarrier.CofinalPredefinition.signMinedIndex
        TfptCarrier.CofinalPredefinition.alternatingMargin) :=
  TfptCarrier.CofinalPredefinition.old_api_accepts_sign_mined_idx

example :
    ¬ TfptCarrier.CofinalPredefinition.FamilyNoninterfering
      TfptCarrier.CofinalPredefinition.signMinedIndex :=
  TfptCarrier.CofinalPredefinition.signMinedIndex_not_familyNoninterfering

end TFPT.Carrier.AuditContract
