/-
  KreinDefect — the defect theorem of the Krein route: the last
  logical link, formalized BEFORE the analytic packages decide.
  ================================================================

  THE HOUSE PATTERN (package D, 2026-08-08 midday plan): build the
  kernel-checked FRAME first, so that no hidden remainder can appear
  later behind the analytic lemmas.  Whatever the running packages
  deliver, the logical geography is already fixed here.

  THE ROUTE.  The Krein-defect representation writes the target form
  as a difference of two channel energies,

      Q(f) = ‖B₊ f‖² − ‖B₋ f‖²   (matrix form: B₊ᴴB₊ − B₋ᴴB₋),

  and positivity of Q is EXACTLY the statement that the negative
  channel is a contraction of the positive one.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`; over ℝ, where ᴴ is the transpose and
  v ⬝ᵥ v is the squared Euclidean norm — the house style avoids the
  norm API, the Loewner-order certificate (1 − CᴴC) ⪰ 0 replaces
  ‖C‖ ≤ 1).

    (1) `defect` — THE DEFECT REPRESENTATION: the matrix
        B₊ᴴB₊ − B₋ᴴB₋; `formAt_gram` / `formAt_defect` — its
        quadratic form IS ‖B₊f‖² − ‖B₋f‖² (dot-product reading).

    (2) `defect_psd_of_contraction` — THE MAIN THEOREM: if
        B₋ = C·B₊ with the contraction certificate
        (1 − CᴴC).PosSemidef (the Loewner form of ‖C‖ ≤ 1), then
        the defect is PSD.  Proof: the defect factors EXACTLY as
        B₊ᴴ(1 − CᴴC)B₊ (`defect_factorization`) and congruence
        preserves PSD (`PosSemidef.conjTranspose_mul_mul_same`) —
        pointwise this is fᴴB₊ᴴ(1 − CᴴC)B₊f ≥ 0, i.e.
        ‖B₋f‖² = ‖CB₊f‖² ≤ ‖B₊f‖².  `defect_form_bound` — the
        pointwise contraction reading, explicit.

    (3) `douglas_contraction_of_defect_psd` — THE CONVERSE
        DIRECTION (the honest completeness): if the defect is PSD
        and B₊ is invertible (the clean finite-dimensional range
        condition: ran(B₊) is everything), a contraction C with
        B₋ = CB₊ exists — the explicit construction C := B₋·B₊⁻¹,
        with the certificate (1 − CᴴC) = B₊⁻ᴴ(defect)B₊⁻¹ ⪰ 0.
        HONESTY NOTE (the general case is a CITATION, not a
        theorem here): for singular B₊ the same works on ran(B₊)
        via the pseudoinverse C := B₋B₊† (zero on the complement),
        with Q ⪰ 0 forcing ‖Cx‖ ≤ ‖x‖ on ran(B₊) — Douglas,
        "On majorization, factorization, and range inclusion of
        operators on Hilbert space", Proc. AMS 17 (1966) 413–415.
        The full-rank case proven here carries the entire logical
        content of the equivalence; the range bookkeeping of the
        singular case is deliberately left as the classical
        citation.

    (4) `krein_cofinal` — THE COFINAL COMPOSITION: a family
        B₊(m), B₋(m) with source contractors on a cofinal ladder
        (`ContractorRecurrence`) yields the CofinalHypothesis for
        the defect forms — wired into the existing chain exactly as
        CofinalCurrent: index extraction via
        `Filter.extraction_of_frequently_atTop`, then
        `krein_cofinal_weil` composes with
        `CofinalWeil.weil_nonneg_of_cofinal`: contractors on a
        ladder + per-element form convergence ⇒ the limit
        functional is nonnegative on the whole dense family.  No
        hidden wall can appear behind the contractor certificates.

  THE CIRCULARITY WARNING (the point of `SourceContractor`).  A
  contractor C computed FROM THE TARGET — from its eigenvectors, or
  as B₋B₊† (exactly the converse direction (3)) — is a
  REFORMULATION of positivity, not a proof of it: feeding it back
  into (2) is circular.  The theorem's value activates only with a
  SOURCE-BUILT C: a contraction constructed from the source algebra
  with an INDEPENDENT norm certificate, never touching the measured
  signs of the target.  `SourceContractor` is the named-hypothesis
  pattern for exactly this: the structure holds C, the
  factorization, and the certificate as DATA a consumer must supply
  from the source side.  PROVENANCE (typed, not proven here):
  PRIME.KREIN.SOURCEALGEBRA.01 (running) is the search for that
  source-built contractor; until it lands, `SourceContractor` is a
  named hypothesis.  No continuum theorem, no RH statement, no
  arithmetic identification is formalized or claimed here.
-/
import TfptCarrier.CofinalWeil

namespace TfptCarrier
namespace KreinDefect

open Filter Topology Matrix ExcessSkeleton CofinalWeil

variable {ι ρ σ : Type*} [Fintype ι] [Fintype ρ] [Fintype σ]

/-! ### (1) The defect representation -/

/-- **THE DEFECT MATRIX**: B₊ᴴB₊ − B₋ᴴB₋ — the matrix of the form
Q(f) = ‖B₊f‖² − ‖B₋f‖² (see `formAt_defect`).  B₊ is the positive
channel, B₋ the negative channel; both may be rectangular. -/
def defect (Bp : Matrix ρ ι ℝ) (Bm : Matrix σ ι ℝ) : Matrix ι ι ℝ :=
  Bpᴴ * Bp - Bmᴴ * Bm

/-- Quadratic forms subtract across matrix differences. -/
theorem formAt_sub (A B : Matrix ι ι ℝ) (x : ι → ℝ) :
    formAt (A - B) x = formAt A x - formAt B x := by
  simp [formAt, Matrix.sub_mulVec, dotProduct_sub]

/-- The Gram form is the channel energy: fᵀ(BᴴB)f = (Bf) ⬝ᵥ (Bf)
— over ℝ the squared Euclidean norm ‖Bf‖². -/
theorem formAt_gram (B : Matrix ρ ι ℝ) (f : ι → ℝ) :
    formAt (Bᴴ * B) f = (B *ᵥ f) ⬝ᵥ (B *ᵥ f) := by
  simp only [formAt]
  rw [← Matrix.mulVec_mulVec, Matrix.dotProduct_mulVec,
    Matrix.vecMul_conjTranspose, star_trivial, star_trivial]

/-- **THE DEFECT FORM**: Q(f) = ‖B₊f‖² − ‖B₋f‖², exactly — the
quadratic form of the defect matrix is the difference of the two
channel energies. -/
theorem formAt_defect (Bp : Matrix ρ ι ℝ) (Bm : Matrix σ ι ℝ)
    (f : ι → ℝ) :
    formAt (defect Bp Bm) f
      = (Bp *ᵥ f) ⬝ᵥ (Bp *ᵥ f) - (Bm *ᵥ f) ⬝ᵥ (Bm *ᵥ f) := by
  rw [defect, formAt_sub, formAt_gram, formAt_gram]

/-- The pointwise contraction reading of a PSD defect:
‖B₋f‖² ≤ ‖B₊f‖² for every f. -/
theorem defect_form_bound {Bp : Matrix ρ ι ℝ} {Bm : Matrix σ ι ℝ}
    (hD : (defect Bp Bm).PosSemidef) (f : ι → ℝ) :
    (Bm *ᵥ f) ⬝ᵥ (Bm *ᵥ f) ≤ (Bp *ᵥ f) ⬝ᵥ (Bp *ᵥ f) := by
  have h := posSemidef_formAt_nonneg hD f
  rw [formAt_defect] at h
  linarith

/-! ### (2) The main theorem: contraction ⇒ defect PSD -/

section Contraction

variable [DecidableEq ρ]

omit [Fintype ι] in
/-- **The exact factorization** behind the main theorem: if
B₋ = C·B₊, the defect is the congruence of the contraction
certificate by the positive channel:

    B₊ᴴB₊ − (CB₊)ᴴ(CB₊) = B₊ᴴ(1 − CᴴC)B₊.  -/
theorem defect_factorization (Bp : Matrix ρ ι ℝ)
    (C : Matrix σ ρ ℝ) :
    defect Bp (C * Bp) = Bpᴴ * (1 - Cᴴ * C) * Bp := by
  simp only [defect, Matrix.conjTranspose_mul, Matrix.mul_sub,
    Matrix.sub_mul, Matrix.mul_one, Matrix.mul_assoc]

/-- **THE MAIN THEOREM** — `defect_psd_of_contraction`: if the
negative channel factors through the positive one, B₋ = C·B₊, and C
carries the contraction certificate (1 − CᴴC) ⪰ 0 (the Loewner form
of ‖C‖ ≤ 1 — no operator-norm API needed), then the defect is PSD:
Q(f) = ‖B₊f‖² − ‖CB₊f‖² ≥ 0 for every f.  Proof: the exact
factorization B₊ᴴ(1 − CᴴC)B₊ plus congruence-invariance of PSD. -/
theorem defect_psd_of_contraction (Bp : Matrix ρ ι ℝ)
    {Bm : Matrix σ ι ℝ} {C : Matrix σ ρ ℝ} (hfact : Bm = C * Bp)
    (hC : (1 - Cᴴ * C).PosSemidef) :
    (defect Bp Bm).PosSemidef := by
  rw [hfact, defect_factorization]
  exact hC.conjTranspose_mul_mul_same Bp

/-! ### (3) The converse direction (Douglas) -/

/-- **THE CONVERSE DIRECTION** — the honest completeness, full-rank
case: if the defect is PSD and B₊ is invertible, a contraction C
with B₋ = CB₊ exists — explicitly C := B₋·B₊⁻¹, whose certificate
is the congruence 1 − CᴴC = B₊⁻ᴴ(defect)B₊⁻¹ ⪰ 0.

HONESTY NOTE: the general (singular B₊) case is the classical
citation — Douglas 1966, via the pseudoinverse C := B₋B₊† on
ran(B₊) and 0 on its complement, with Q ⪰ 0 forcing ‖Cx‖ ≤ ‖x‖ on
ran(B₊); the range bookkeeping is deliberately NOT formalized here
(the full-rank case carries the logical content of the
equivalence).

CIRCULARITY WARNING: this converse is exactly why a
target-computed contractor proves nothing new — the C constructed
HERE is mined from B₊, B₋ themselves.  Only a source-built C (see
`SourceContractor`) turns the equivalence into a route. -/
theorem douglas_contraction_of_defect_psd [DecidableEq ι]
    (Bp : Matrix ι ι ℝ) [Invertible Bp] (Bm : Matrix σ ι ℝ)
    (hD : (defect Bp Bm).PosSemidef) :
    ∃ C : Matrix σ ι ℝ, Bm = C * Bp ∧ (1 - Cᴴ * C).PosSemidef := by
  refine ⟨Bm * ⅟Bp,
    by rw [Matrix.mul_assoc, invOf_mul_self, Matrix.mul_one], ?_⟩
  have key : 1 - (Bm * ⅟Bp)ᴴ * (Bm * ⅟Bp)
      = (⅟Bp)ᴴ * defect Bp Bm * ⅟Bp := by
    simp only [defect, Matrix.conjTranspose_mul, Matrix.mul_sub,
      Matrix.sub_mul, Matrix.mul_assoc]
    rw [mul_invOf_self, Matrix.mul_one, ← Matrix.conjTranspose_mul,
      mul_invOf_self, Matrix.conjTranspose_one]
  rw [key]
  exact hD.conjTranspose_mul_mul_same _

/-! ### The named hypothesis: the source-built contractor -/

/-- **THE NAMED HYPOTHESIS — SourceContractor**: the contractor C
together with its factorization and its INDEPENDENT norm
certificate, as data a consumer must supply.

THE CIRCULARITY WARNING (why this is a structure and not a
theorem): a C computed from the target — its eigenvectors, or the
pseudoinverse B₋B₊† of the converse direction — is a REFORMULATION
of the positivity to be proven, not a proof; feeding it into
`defect_psd_of_contraction` is circular.  The route activates only
when C is built from the SOURCE algebra with a norm certificate
established independently of the measured target signs.

PROVENANCE (typed, not proven here): PRIME.KREIN.SOURCEALGEBRA.01
(running) — the search for the source-built contractor.  Until that
lands, every field below is a named hypothesis. -/
structure SourceContractor (Bp : Matrix ρ ι ℝ)
    (Bm : Matrix σ ι ℝ) where
  /-- The contractor — to be built from the source algebra, never
  from the target's eigendata. -/
  C : Matrix σ ρ ℝ
  /-- The factorization of the negative channel through the
  positive one. -/
  factors : Bm = C * Bp
  /-- The INDEPENDENT norm certificate, in Loewner form:
  (1 − CᴴC) ⪰ 0, i.e. ‖C‖ ≤ 1 — certified source-side. -/
  contraction : (1 - Cᴴ * C).PosSemidef

/-- A source contractor certifies the defect PSD (the main theorem,
consumed through the named-hypothesis pattern). -/
theorem SourceContractor.defect_psd {Bp : Matrix ρ ι ℝ}
    {Bm : Matrix σ ι ℝ} (sc : SourceContractor Bp Bm) :
    (defect Bp Bm).PosSemidef :=
  defect_psd_of_contraction Bp sc.factors sc.contraction

end Contraction

/-! ### (4) The cofinal composition -/

section Cofinal

variable {κ ρ' σ' : ℕ → Type*} [∀ m, Fintype (κ m)]
  [∀ m, Fintype (ρ' m)] [∀ m, Fintype (σ' m)]
  [∀ m, DecidableEq (ρ' m)]

/-- The defect ladder of a channel family. -/
def defectLadder (Bp : ∀ m, Matrix (ρ' m) (κ m) ℝ)
    (Bm : ∀ m, Matrix (σ' m) (κ m) ℝ) :
    ∀ m, Matrix (κ m) (κ m) ℝ :=
  fun m => defect (Bp m) (Bm m)

/-- **Contractors on a cofinal ladder**: past every rung there is a
later rung carrying a source contractor.  The recurrence shape
mirrors `CofinalCurrent.PhaseRecurrence`.  The ladder is extracted
from contractor existence; this mathematical recurrence does NOT by
itself certify sign-independent construction.  PREDEFINED remains the
external contract of `CofinalPredefinition`. -/
def ContractorRecurrence (Bp : ∀ m, Matrix (ρ' m) (κ m) ℝ)
    (Bm : ∀ m, Matrix (σ' m) (κ m) ℝ) : Prop :=
  ∀ m₀ : ℕ, ∃ m, m₀ < m ∧ Nonempty (SourceContractor (Bp m) (Bm m))

/-- **THE COFINAL COMPOSITION** — `krein_cofinal`: source
contractors on a cofinal ladder produce the mathematical core
`CofinalHypothesis` for the defect ladder — the index sequence is
extracted from the recurrence
(`Filter.extraction_of_frequently_atTop`), and PSD at every extracted
rung is the main theorem applied to that rung's contractor.  Upgrading
this result to `PredefinedCofinalHypothesis` requires the separate
external noninterference certificate. -/
theorem krein_cofinal (Bp : ∀ m, Matrix (ρ' m) (κ m) ℝ)
    (Bm : ∀ m, Matrix (σ' m) (κ m) ℝ)
    (h : ContractorRecurrence Bp Bm) :
    Nonempty (CofinalHypothesis (defectLadder Bp Bm)) := by
  obtain ⟨idx, hmono, hmem⟩ :=
    Filter.extraction_of_frequently_atTop
      (Filter.frequently_atTop'.mpr h)
  exact ⟨{ idx := idx
           mono := hmono
           psd := fun j => (hmem j).some.defect_psd }⟩

/-- **THE COMPOSED COROLLARY** — `krein_cofinal_weil`: the full
chain, kernel-checked.  Contractors on a cofinal ladder +
per-element convergence of the defect forms to the limit functional
force QW ≥ 0 on the WHOLE dense family (composition with
`CofinalWeil.weil_nonneg_of_cofinal`, the minimal H theorem).
Whatever discharges the contractor recurrence discharges the
chain — no hidden wall behind the analytic packages. -/
theorem krein_cofinal_weil {V : Type*}
    (Bp : ∀ m, Matrix (ρ' m) (κ m) ℝ)
    (Bm : ∀ m, Matrix (σ' m) (κ m) ℝ)
    (h : ContractorRecurrence Bp Bm)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto
      (fun m => ladderForm (defectLadder Bp Bm) sample m v)
      atTop (𝓝 (QW v))) :
    ∀ v, 0 ≤ QW v := by
  obtain ⟨H⟩ := krein_cofinal Bp Bm h
  exact weil_nonneg_of_cofinal H sample QW hconv

end Cofinal

end KreinDefect
end TfptCarrier
