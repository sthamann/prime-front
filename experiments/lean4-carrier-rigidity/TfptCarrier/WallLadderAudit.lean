/-
  TFPT Carrier — Wall-ladder audit surface (off-CI)
  -------------------------------------------------

  The `#print axioms` / `#check` / `example` signature-lock lines for
  the certified wall finite head, moved verbatim out of AxiomCheck,
  AuditCheck, and AuditContract so those three modules no longer
  import `WallCertifiedHead` (and therefore do not pull in the
  generated `WallLadder/RungKz*` kernel `decide` certificates).

  This file is part of the full `TfptCarrier` root. It is *not* part
  of `TfptCarrier.CIRoot`. GitHub Actions runs `scripts/audit.sh --core`
  and never elaborates this module. Local full audit still does, after
  `scripts/build_wall_ladder.sh`. See AUDIT_TRANSCRIPT.txt.

  No proof content is added or changed here — only relocated.
  NO RH claim.
-/

import TfptCarrier.WallCertifiedHead
import TfptCarrier.CofinalPredefinition

-- Certified wall finite head (PRIME.PORT.BALLLADDER.01 Lean seam; v897)
-- The 18 per-rung PD certificates are kernel `decide` runs on exported exact
-- integer data (NO axioms declared); the composition into cofinal Weil carries
-- its two NAMED hypotheses (HeadEnclosure, TailPositivity) as explicit
-- arguments of the theorem — hypotheses, never axioms.
#print axioms TfptCarrier.WallLadder.posSemidef_of_diagDominant
#print axioms TfptCarrier.WallLadder.posDef_of_rungOk
#print axioms TfptCarrier.WallLadder.checked_is_census_prefix
#print axioms TfptCarrier.WallLadder.certified_head
#print axioms TfptCarrier.WallLadder.wall_cofinal_weil
#print axioms TfptCarrier.WallLadder.wall_certified_head_cofinal_weil

-- Certified wall finite head (PRIME.PORT.BALLLADDER.01 Lean seam; v897)
#check @TfptCarrier.WallLadder.rungOk
#check @TfptCarrier.WallLadder.posSemidef_of_diagDominant
#check @TfptCarrier.WallLadder.posDef_of_rungOk
#check @TfptCarrier.WallLadder.EnclosureBridge
#check @TfptCarrier.WallLadder.HeadEnclosure
#check @TfptCarrier.WallLadder.TailPositivity
#check @TfptCarrier.WallLadder.posSemidef_of_bridge
#check @TfptCarrier.WallLadder.head_psd_of_enclosure
#check @TfptCarrier.WallLadder.cofinalHypothesis_of_head_tail
#check @TfptCarrier.WallLadder.wall_cofinal_weil
#check @TfptCarrier.WallLadder.census
#check @TfptCarrier.WallLadder.checkedData
#check @TfptCarrier.WallLadder.checked_is_census_prefix
#check @TfptCarrier.WallLadder.certified_head
#check @TfptCarrier.WallLadder.wall_certified_head_cofinal_weil

/-- Certified wall finite head (PRIME.PORT.BALLLADDER.01 Lean seam; v897):
    every exported integer certificate matrix of the kernel-checked
    18-rung head is positive definite. -/
example :
    ∀ d ∈ TfptCarrier.WallLadder.checkedData,
      (TfptCarrier.WallLadder.MmatR d).PosDef :=
  TfptCarrier.WallLadder.certified_head

/-- The checked head is exactly the first 18 rungs (ascending h) of the
    frozen 42-rung v897 census. -/
example :
    TfptCarrier.WallLadder.checkedData.map (fun d => (d.kz, d.h))
      = TfptCarrier.WallLadder.census.take 18 :=
  TfptCarrier.WallLadder.checked_is_census_prefix

/-- The composed finite-head theorem: 18 kernel certificates
    + `HeadEnclosure` (NAMED: v897 E1–E4 interval enclosure)
    + `TailPositivity` (NAMED: the 24 deeper rungs + asymptotic tail)
    + form convergence ⇒ the full `cofinal_weil` conclusion.
    NO RH claim — the two mathematical hypotheses remain open inputs;
    PREDEFINED/noninterference is a separate external audit premise,
    signature-locked below by the hardened wrapper. -/
example {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}
    (A : ∀ m, Matrix (κ m) (κ m) ℝ) (idx : ℕ → ℕ)
    (hmono : StrictMono idx)
    (hbridge : TfptCarrier.WallLadder.HeadEnclosure A idx
      TfptCarrier.WallLadder.checkedData)
    (htail : TfptCarrier.WallLadder.TailPositivity A idx
      TfptCarrier.WallLadder.checkedData.length)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Filter.Tendsto
      (fun m => TfptCarrier.CofinalWeil.ladderForm A sample m v)
      Filter.atTop (nhds (QW v))) :
    (∀ j v, 0 ≤ TfptCarrier.CofinalWeil.ladderForm A sample (idx j) v) ∧
    (∀ v, Filter.Tendsto
      (fun j => TfptCarrier.CofinalWeil.ladderForm A sample (idx j) v)
      Filter.atTop (nhds (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  TfptCarrier.WallLadder.wall_certified_head_cofinal_weil
    A idx hmono hbridge htail sample QW hconv
