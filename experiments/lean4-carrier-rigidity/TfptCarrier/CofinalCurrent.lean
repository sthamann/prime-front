/-
  CofinalCurrent — FORM.PRIME.COFINAL_CURRENT.01: the conditional
  route to the cofinal hypothesis.
  ================================================================

  THE CONDITIONAL THEOREM (2026-08-08 morning analysis, package E):

      ConnectedTail + PositiveHeadCell + PhaseRecurrence ⇒ H_cof,

  wired into the existing CofinalWeil chain, so that the FULL
  implication

      three hypotheses ⇒ H_cof ⇒ (minimal H theorem) ⇒ QW ≥ 0
                                                        on the
                                                        dense family

  is kernel-checked end to end: NO hidden wall can appear behind
  the two analytic lemmas — whatever discharges the three named
  hypotheses discharges the chain.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`).

    (1) `HeadTailSplit` — THE SPLIT STRUCTURE: ladder matrices
        A m = Head m + Tail m with the head depending on the rung
        ONLY through a phase trajectory, Head m = H_m(φ m) for a
        phase function φ : ℕ → Φ (`ladder` is the assembled A).

    (2) THE THREE NAMED HYPOTHESES (each with its provenance typed
        in the doc comment — the module is the FRAME awaiting the
        lemmas; probes C and D are running):
          `ConnectedTail`     — every tail block is PSD
                                (PRIME.RELATION.CONNECTED_COVARIANCE.01),
          `PositiveHeadCell`  — an open cell U in phase space and
                                δ > 0 with the uniform quadratic-form
                                floor δ‖v‖² ≤ vᵀ(H φ)v on the cell
                                (PRIME.COFINAL.PHASE_CELL.01),
          `PhaseRecurrence`   — the trajectory visits U cofinally
                                (the Kronecker/Weyl input; stays a
                                hypothesis at this level).

    (3) `cofinal_current` — THE CONDITIONAL MATHEMATICAL THEOREM: the
        three hypotheses produce the core
        `CofinalWeil.CofinalHypothesis` for the ladder — the index
        sequence is EXTRACTED from the recurrence
        (`Filter.extraction_of_frequently_atTop`), and PSD at every
        extracted rung is head-PSD (cell floor, δ ≥ 0 relaxation)
        plus tail-PSD (`Matrix.PosSemidef.add`).  This does not prove
        that the recurrence/cell was constructed independently of
        measured signs; the PREDEFINED certificate of
        `CofinalPredefinition` remains an additional external premise.
        `cofinal_current_weil` — THE COMPOSED COROLLARY: the three
        hypotheses + per-element form convergence force the limit
        functional to be nonnegative on the whole dense family
        (via `CofinalWeil.weil_nonneg_of_cofinal`).

    (4) HONESTY LEMMAS:
          `PositiveHeadCell.psdHeadCell` / `cofinal_current_of_psd_cell`
              — the δ = 0 boundary: the theorem needs only PSD on
              the cell (`PsdHeadCell`), the strict δ > 0 floor is a
              STRONGER input than required (typed so the analytic
              lemma is not asked for more than the chain consumes);
          `PositiveHeadCell.rayleigh` — what the strict floor DOES
              buy: every normalized witness sees at least δ on the
              cell (via ExcessSkeleton.le_formAt_of_isFormLowerBound);
          `connectedTail_not_sufficient` — the counterexample-style
              note: ConnectedTail ALONE does not give H_cof (a
              1×1 witness with everywhere-negative head) — the
              hypotheses are jointly necessary in this architecture.

  THE HONEST BOUNDARY.  Nothing here proves any of the three
  hypotheses.  `ConnectedTail` is to be supplied by the
  connected-covariance construction (probe C), `PositiveHeadCell`
  by the phase-cell floor measurement (probe D), `PhaseRecurrence`
  by Kronecker/Weyl equidistribution — a CLASSICAL citation whose
  named arithmetic input is the rational independence of the phase
  generators (log-prime independence on the prime front); the
  recurrence stays a named hypothesis at this abstraction level.
  No continuum theorem, no RH statement, no arithmetic
  identification is formalized or claimed here.
-/
import TfptCarrier.CofinalWeil

namespace TfptCarrier
namespace CofinalCurrent

open Filter Topology Matrix ExcessSkeleton CofinalWeil

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {Φ : Type*}

/-! ### (1) The split structure -/

/-- **The head/tail split**: ladder matrices A m = Head m + Tail m,
where the head depends on the rung ONLY through the phase
trajectory: Head m = head m (φ m).  The rung index enters the head
solely as the (size-carrying) level; all sign-relevant dependence is
routed through the phase parameter — exactly the split of the
morning analysis. -/
structure HeadTailSplit (κ : ℕ → Type*) [∀ m, Fintype (κ m)]
    (Φ : Type*) where
  /-- The phase-parametrized head block at each level. -/
  head : ∀ m, Φ → Matrix (κ m) (κ m) ℝ
  /-- The tail block at each level (the connected remainder). -/
  tail : ∀ m, Matrix (κ m) (κ m) ℝ
  /-- The phase trajectory along the tower. -/
  φ : ℕ → Φ

/-- The assembled ladder: A m = Head m (φ m) + Tail m. -/
def HeadTailSplit.ladder (S : HeadTailSplit κ Φ) :
    ∀ m, Matrix (κ m) (κ m) ℝ :=
  fun m => S.head m (S.φ m) + S.tail m

/-! ### (2) The three named hypotheses -/

/-- **HYPOTHESIS 1 — ConnectedTail**: every tail block is PSD.

PROVENANCE (typed, not proven here): to be supplied by the
connected-covariance construction — PRIME.RELATION.CONNECTED_COVARIANCE.01
(probe C, running): the tail is a connected-correlation Gram block,
PSD by construction once the connectedness subtraction is certified.
Until that lemma lands, this is a named hypothesis. -/
def ConnectedTail (S : HeadTailSplit κ Φ) : Prop :=
  ∀ m, (S.tail m).PosSemidef

/-- **HYPOTHESIS 2 — PositiveHeadCell**: an open cell U in phase
space and a margin δ > 0 with the uniform quadratic-form floor
δ‖v‖² ≤ vᵀ(H_m φ)v for every phase in the cell, every level, every
witness (plus hermiticity of the head on the cell — the covariance
shape).  The cell is abstract: a `Set Φ` with its membership
predicate; openness is not needed by the extraction, only
recurrence INTO the set.

PROVENANCE (typed, not proven here): PRIME.COFINAL.PHASE_CELL.01
(probe D, running): the measured strictly-positive floor of the
head form on an explicit phase cell.  Until that lemma lands, this
is a named hypothesis. -/
structure PositiveHeadCell (S : HeadTailSplit κ Φ) (U : Set Φ)
    (δ : ℝ) : Prop where
  /-- The margin is strictly positive. -/
  δ_pos : 0 < δ
  /-- The head is hermitian on the cell (covariance shape). -/
  herm : ∀ ph ∈ U, ∀ m, (S.head m ph).IsHermitian
  /-- The uniform Rayleigh floor on the cell, all levels. -/
  floor : ∀ ph ∈ U, ∀ m, IsFormLowerBound (S.head m ph) δ

/-- The δ = 0 boundary version — all the chain actually consumes:
head PSD on the cell (no margin demanded). -/
def PsdHeadCell (S : HeadTailSplit κ Φ) (U : Set Φ) : Prop :=
  ∀ ph ∈ U, ∀ m, (S.head m ph).PosSemidef

/-- **HYPOTHESIS 3 — PhaseRecurrence**: the phase trajectory visits
the cell cofinally — the cofinal-visit form of Kronecker: past every
rung there is a later rung whose phase lies in U.

PROVENANCE (typed, not proven here): Kronecker/Weyl equidistribution
of the phase flow — a CLASSICAL citation; the named arithmetic input
is the rational independence of the phase generators (on the prime
front: linear independence of the log primes over Q).  The
recurrence itself stays a hypothesis at this abstraction level; no
equidistribution is formalized. -/
def PhaseRecurrence (S : HeadTailSplit κ Φ) (U : Set Φ) : Prop :=
  ∀ m₀ : ℕ, ∃ m, m₀ < m ∧ S.φ m ∈ U

/-! ### Cell positivity: what the floor gives -/

/-- The strict cell floor gives PSD heads on the cell (hermiticity
+ nonnegative form; the δ ≥ 0 relaxation — honesty lemma (a): the
chain needs only this weaker consequence). -/
theorem PositiveHeadCell.psdHeadCell {S : HeadTailSplit κ Φ}
    {U : Set Φ} {δ : ℝ} (hc : PositiveHeadCell S U δ) :
    PsdHeadCell S U := by
  intro ph hph m
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg
    (hc.herm ph hph m) fun x => ?_
  rw [star_trivial]
  have hxx : 0 ≤ x ⬝ᵥ x := by
    simp only [dotProduct]
    exact Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
  exact le_trans (mul_nonneg hc.δ_pos.le hxx) (hc.floor ph hph m x)

/-- What the STRICT floor does buy beyond PSD: every normalized
witness sees at least δ on the cell — the Rayleigh reading, via
`ExcessSkeleton.le_formAt_of_isFormLowerBound`. -/
theorem PositiveHeadCell.rayleigh {S : HeadTailSplit κ Φ}
    {U : Set Φ} {δ : ℝ} (hc : PositiveHeadCell S U δ)
    {ph : Φ} (hph : ph ∈ U) (m : ℕ) {x : κ m → ℝ}
    (hx : x ⬝ᵥ x = 1) : δ ≤ formAt (S.head m ph) x :=
  le_formAt_of_isFormLowerBound (hc.floor ph hph m) hx

/-! ### (3) The conditional theorem and the composed corollary -/

/-- The extraction: cofinal visits yield a strictly monotone index
sequence landing in the cell (`Filter.extraction_of_frequently_atTop`
— the choice-function step, isolated). -/
theorem exists_ladder_of_recurrence {S : HeadTailSplit κ Φ}
    {U : Set Φ} (h : PhaseRecurrence S U) :
    ∃ idx : ℕ → ℕ, StrictMono idx ∧ ∀ j, S.φ (idx j) ∈ U :=
  Filter.extraction_of_frequently_atTop (Filter.frequently_atTop'.mpr h)

/-- **The conditional theorem, δ = 0 form**: ConnectedTail +
PsdHeadCell + PhaseRecurrence produce the cofinal hypothesis for
the assembled ladder — the extracted rungs are PSD as
head-PSD + tail-PSD. -/
theorem cofinal_current_of_psd_cell {U : Set Φ}
    (S : HeadTailSplit κ Φ)
    (connected_tail : ConnectedTail S)
    (psd_head_cell : PsdHeadCell S U)
    (phase_recurrence : PhaseRecurrence S U) :
    Nonempty (CofinalHypothesis S.ladder) := by
  obtain ⟨idx, hmono, hmem⟩ :=
    exists_ladder_of_recurrence phase_recurrence
  exact ⟨{ idx := idx
           mono := hmono
           psd := fun j =>
             (psd_head_cell _ (hmem j) _).add (connected_tail _) }⟩

/-- **THE CONDITIONAL THEOREM** (FORM.PRIME.COFINAL_CURRENT.01):

    ConnectedTail + PositiveHeadCell + PhaseRecurrence ⇒ H_cof.

The index sequence of the cofinal hypothesis is built from the
recurrence; PSD at every extracted rung is the cell floor (relaxed
to PSD) plus the connected tail.  All three inputs are NAMED
hypotheses — nothing about them is proven here; the implication is
what is kernel-checked.  This returns the mathematical core, not a
`PredefinedCofinalHypothesis`: noninterference of the recurrence/cell
construction is not inferred from quantifier order. -/
theorem cofinal_current {U : Set Φ} {δ : ℝ} (S : HeadTailSplit κ Φ)
    (connected_tail : ConnectedTail S)
    (positive_head_cell : PositiveHeadCell S U δ)
    (phase_recurrence : PhaseRecurrence S U) :
    Nonempty (CofinalHypothesis S.ladder) :=
  cofinal_current_of_psd_cell S connected_tail
    positive_head_cell.psdHeadCell phase_recurrence

/-- **THE COMPOSED COROLLARY** — the full chain, kernel-checked:
the three named hypotheses + per-element convergence of the ladder
forms to the limit functional force QW ≥ 0 on the WHOLE dense
family (composition with `CofinalWeil.weil_nonneg_of_cofinal`, the
minimal H theorem).  Whatever discharges the three hypotheses
discharges the chain — no hidden wall behind the two analytic
lemmas. -/
theorem cofinal_current_weil {V : Type*} {U : Set Φ} {δ : ℝ}
    (S : HeadTailSplit κ Φ)
    (connected_tail : ConnectedTail S)
    (positive_head_cell : PositiveHeadCell S U δ)
    (phase_recurrence : PhaseRecurrence S U)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm S.ladder sample m v)
      atTop (𝓝 (QW v))) :
    ∀ v, 0 ≤ QW v := by
  obtain ⟨H⟩ := cofinal_current S connected_tail positive_head_cell
    phase_recurrence
  exact weil_nonneg_of_cofinal H sample QW hconv

/-! ### (4) Joint necessity: the tail alone is not enough -/

/-- **Honesty lemma (b)**: ConnectedTail ALONE does not give H_cof —
witness a 1×1 split with zero tail (PSD everywhere) and
everywhere-negative head: NO index sequence has PSD rungs.  The
three hypotheses are jointly necessary in this architecture: the
tail supplies positivity of the remainder, the cell + recurrence
must still deliver the head. -/
theorem connectedTail_not_sufficient :
    ∃ S : HeadTailSplit (fun _ => Fin 1) Unit,
      ConnectedTail S ∧ IsEmpty (CofinalHypothesis S.ladder) := by
  refine ⟨⟨fun _ _ => Matrix.of fun _ _ => (-1 : ℝ),
    fun _ => 0, fun _ => ()⟩, fun _ => Matrix.PosSemidef.zero,
    ⟨fun H => ?_⟩⟩
  have h := (H.psd 0).dotProduct_mulVec_nonneg (fun _ => 1)
  rw [star_trivial] at h
  have h2 : (0 : ℝ) ≤ -1 := by
    simpa [HeadTailSplit.ladder, Matrix.mulVec, dotProduct] using h
  norm_num at h2

end CofinalCurrent
end TfptCarrier
