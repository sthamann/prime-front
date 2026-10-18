/-
  ExcessSkeleton — the two-giants decomposition and the certified
  skeleton of the excess floor.
  ================================================================

  The formal geography of the sharpest wall form of the prime front
  (2026-08-07, rounds 27+28): in identified-corner coordinates the
  deployed floor splits per rung as

      tau_X  =  lambda_min(S)  +  EXCESS

  with S the comb-blind structural block and the excess carried
  entirely by the prime-power comb.  Numeric counterparts:
  `verification/v842_excess_certified_skeleton.py` (the certified
  skeleton: strictly positive interval enclosures of tau_X on all 67
  reachable rungs; the h = 2 Epstein comb certified NEGATIVE on every
  anchor) and `verification/v841_relation_carrier_ladder.py` (the
  relational corner, the four gates); discovery probes
  `excess_certified_skeleton_probe.py`, `relation_corner_ladder_probe.py`.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`).  The structural half of the certified skeleton, at
  the finite matrix / real-arithmetic level (house precedent:
  SectorPositiveDescent, GramCompactness):

    (1) `formAt` / `formAt_add` / `excessAt_eq_comb` — THE
        DECOMPOSITION: quadratic forms on a chosen witness split
        additively across A = S + C; the excess — the gap between the
        full form and the structural form on the witness — is carried
        EXACTLY by the comb block.  `IsFormLowerBound` — a
        lambda_min-type lower bound in Rayleigh form (uniform over
        directions); `le_formAt_of_isFormLowerBound` — any such bound
        is dominated by the Rayleigh value at a normalized witness;
        `isFormLowerBound_add` — bounds compose across the
        decomposition (the naive two-giants composition, whose
        certified cost v842 measured; the direct enclosure is the
        payoff); `posSemidef_formAt_nonneg` — the PSD case.  NOTE the
        deployed structural block is NOT assumed PSD: at the deployed
        rungs lambda_min(S) is strictly negative (≈ −2.28 at kz = 9)
        and the excess (≈ +2.285) carries the positivity.

    (2) `enclosure_mem` / `pos_of_certified` — THE MARGIN
        CERTIFICATE logic, trivial but load-bearing: the enclosure
        discipline |computed − true| ≤ budget together with
        computed − budget > 0 forces true > 0.  This is the exact
        formal shape of every strictly-positive interval certificate
        in v842 (chol_cert discipline: certificates cover the linear
        algebra above the deployed float data).

    (3) `neg_of_certified` / `certified_negative_excludes` — THE
        DISCRIMINATOR SHAPE: a certified-negative enclosure
        (computed + budget < 0) excludes positivity — the
        fake-rejection logic of the h = 2 Epstein side (routed-corner
        enclosures −0.786/−1.100/−1.228 on the anchors).

    (4) `ladder_pos_on_finset` — THE FINITE LADDER: per-rung strictly
        positive certificates give positivity at every certified rung
        (the v842 content on the 67 reachable rungs; the finset
        quantifier is the honest extent of any table).
        `pointwise_pos_not_uniform` — the KERNEL-CHECKED GAP: there
        are margin sequences strictly positive at EVERY rung with NO
        uniform lower bound (witness 1/(n+1)) — no finite table,
        certified or not, settles the uniform statement.

    (5) `RungLadder` / `excess_floor` — THE BRIDGE THEOREM: rung data
        (structural + comb blocks, identified witnesses) + the one
        named hypothesis `uniform_margin_bound` give the floor
        statement for all rungs — decomposition proven per rung,
        uniform floor delta > 0, strict positivity everywhere, and
        the per-rung `IdentificationPositivity` instances of
        SectorPositiveDescent (`uniform_to_identification`).

  THE HONEST BOUNDARY (the kill criterion — the point of this
  module).  `UniformMarginBound` enters as a NAMED HYPOTHESIS, not a
  theorem, mirroring `IdentificationPositivity` in
  SectorPositiveDescent.  The two named hypotheses are related but
  DISTINCT: `UniformMarginBound` on the floor margins IMPLIES the
  per-rung `IdentificationPositivity` instances
  (`uniform_to_identification`, proven), but the converse FAILS even
  with per-rung strictness (`pointwise_pos_not_uniform`, proven) —
  the uniform quantifier is strictly stronger than any collection of
  per-rung certificates.  Nothing in this module (or in any
  structural extension of it) can discharge it: by the GUE-side
  findings (v839/v840) the required datum is finer-than-statistical.

  No continuum theorem, no RH statement, no arithmetic
  identification is formalized or claimed here.
-/
import TfptCarrier.SectorPositiveDescent

namespace TfptCarrier
namespace ExcessSkeleton

open Matrix

/-! ### (1) The decomposition A = S + C on a witness -/

section Decomposition

variable {ι : Type*} [Fintype ι]

/-- The quadratic form of a real matrix at a witness vector:
`formAt A x = xᵀAx`. -/
def formAt (A : Matrix ι ι ℝ) (x : ι → ℝ) : ℝ :=
  x ⬝ᵥ (A *ᵥ x)

/-- **The decomposition**: quadratic forms split additively across
A = S + C — the full form is the structural form plus the comb form,
on every witness. -/
theorem formAt_add (S C : Matrix ι ι ℝ) (x : ι → ℝ) :
    formAt (S + C) x = formAt S x + formAt C x := by
  simp [formAt, Matrix.add_mulVec, dotProduct_add]

/-- The excess at a witness: the gap between the full form and the
structural form (the definition v841 measured along the ladder). -/
def excessAt (S C : Matrix ι ι ℝ) (x : ι → ℝ) : ℝ :=
  formAt (S + C) x - formAt S x

/-- **The excess is carried exactly by the comb block**: the gap
between the full and the structural form IS the comb form. -/
theorem excessAt_eq_comb (S C : Matrix ι ι ℝ) (x : ι → ℝ) :
    excessAt S C x = formAt C x := by
  rw [excessAt, formAt_add]; ring

/-- A lambda_min-type lower bound in Rayleigh form: delta bounds the
quadratic form uniformly over all directions, weighted by ‖x‖². -/
def IsFormLowerBound (A : Matrix ι ι ℝ) (δ : ℝ) : Prop :=
  ∀ x : ι → ℝ, δ * (x ⬝ᵥ x) ≤ formAt A x

/-- **Rayleigh witness evaluation**: any uniform form lower bound is
dominated by the Rayleigh value at a normalized witness — the
one-directional content of every lambda_min certificate. -/
theorem le_formAt_of_isFormLowerBound {A : Matrix ι ι ℝ} {δ : ℝ}
    (h : IsFormLowerBound A δ) {x : ι → ℝ} (hx : x ⬝ᵥ x = 1) :
    δ ≤ formAt A x := by
  have hb := h x
  rwa [hx, mul_one] at hb

/-- PSD matrices have nonnegative form at every witness (the
comb-blind structural positivity of SectorPositiveDescent, in
witness coordinates). -/
theorem posSemidef_formAt_nonneg {A : Matrix ι ι ℝ}
    (hA : A.PosSemidef) (x : ι → ℝ) : 0 ≤ formAt A x := by
  have h := hA.dotProduct_mulVec_nonneg x
  rwa [star_trivial] at h

/-- PSD gives the zero lower bound in Rayleigh form. -/
theorem isFormLowerBound_zero_of_posSemidef {A : Matrix ι ι ℝ}
    (hA : A.PosSemidef) : IsFormLowerBound A 0 := fun x => by
  rw [zero_mul]
  exact posSemidef_formAt_nonneg hA x

/-- **The naive two-giants composition**: lower bounds add across the
decomposition A = S + C.  (v842 measured the certified cost of this
composition against the sharp direct enclosure — the direct enclosure
is the payoff; this lemma is the composed fallback.) -/
theorem isFormLowerBound_add {S C : Matrix ι ι ℝ} {δ ε : ℝ}
    (hS : IsFormLowerBound S δ) (hC : IsFormLowerBound C ε) :
    IsFormLowerBound (S + C) (δ + ε) := fun x => by
  have h1 := hS x
  have h2 := hC x
  rw [formAt_add, add_mul]
  linarith

end Decomposition

/-! ### (2) The interval-certificate logic (the margin certificate) -/

section Certificate

/-- **The enclosure discipline**: |computed − true| ≤ budget encloses
the true value in [computed − budget, computed + budget]. -/
theorem enclosure_mem {t c b : ℝ} (h : |c - t| ≤ b) :
    c - b ≤ t ∧ t ≤ c + b := by
  have hab := abs_le.mp h
  constructor <;> linarith [hab.1, hab.2]

/-- **THE MARGIN CERTIFICATE** (trivial but load-bearing — the exact
formal shape of every strictly-positive interval certificate in
v842): if the computed value clears its own error budget,
computed − budget > 0, then the true margin is strictly positive. -/
theorem pos_of_certified {t c b : ℝ} (h : |c - t| ≤ b)
    (hpos : 0 < c - b) : 0 < t :=
  lt_of_lt_of_le hpos (enclosure_mem h).1

/-- Interval form: a strictly positive certified lower endpoint gives
strict positivity ("if the certified enclosure [lo, hi] of the margin
satisfies 0 < lo then the margin is positive"). -/
theorem pos_of_enclosure_lo {t lo : ℝ} (hlo : lo ≤ t) (h : 0 < lo) :
    0 < t :=
  lt_of_lt_of_le h hlo

/-! ### (3) The discriminator shape (the Epstein side) -/

/-- **The certified-negative reading**: if even computed + budget is
negative, the true value is strictly negative — the h = 2 Epstein
comb fails its margin certificate on every anchor. -/
theorem neg_of_certified {t c b : ℝ} (h : |c - t| ≤ b)
    (hneg : c + b < 0) : t < 0 :=
  lt_of_le_of_lt (enclosure_mem h).2 hneg

/-- **THE DISCRIMINATOR**: a certified-negative enclosure EXCLUDES
positivity — the fake-rejection logic as a formal lemma. -/
theorem certified_negative_excludes {t c b : ℝ} (h : |c - t| ≤ b)
    (hneg : c + b < 0) : ¬ 0 ≤ t :=
  not_le.mpr (neg_of_certified h hneg)

end Certificate

/-! ### (4) The ladder quantifier and the honest boundary -/

section Ladder

/-- **The finite ladder**: strictly positive per-rung certificates
give positivity at every certified rung.  The finset quantifier is
the honest extent of any table — v842 certifies exactly the 67
reachable rungs, and this lemma is what those 67 certificates
formally yield. -/
theorem ladder_pos_on_finset (τ c b : ℕ → ℝ) (s : Finset ℕ)
    (henc : ∀ m ∈ s, |c m - τ m| ≤ b m)
    (hstrict : ∀ m ∈ s, 0 < c m - b m) :
    ∀ m ∈ s, 0 < τ m :=
  fun m hm => pos_of_certified (henc m hm) (hstrict m hm)

/-- **THE HONEST BOUNDARY** (the kill criterion of this module).
`UniformMarginBound margin` says: the margins along the whole ladder
admit a single uniform strictly positive lower bound delta.

This is a NAMED HYPOTHESIS, deliberately NOT a theorem — mirroring
`IdentificationPositivity` in SectorPositiveDescent.  The certified
skeleton (v842, PRIME.RELATION.SKELETON.01) produced strictly
positive interval enclosures on every reachable rung, but the wall is
the INFINITE QUANTIFIER over that sequence: any future route must
supply a uniform lower bound on the excess margin tau_X, and by the
GUE-side findings (v839 pair-correlation bridge, v840 loop-gain
ablation) the required datum is finer-than-statistical — no
structural argument in this module's class, and no finite table of
certificates (see `pointwise_pos_not_uniform`), can discharge it.
Any future closure of the prime front must discharge THIS
hypothesis. -/
def UniformMarginBound (margin : ℕ → ℝ) : Prop :=
  ∃ δ : ℝ, 0 < δ ∧ ∀ m, δ ≤ margin m

/-- A uniform margin bound gives strict positivity at every rung
(the trivial direction — the content lives in the hypothesis). -/
theorem uniformMarginBound_pos {margin : ℕ → ℝ}
    (h : UniformMarginBound margin) (m : ℕ) : 0 < margin m := by
  obtain ⟨δ, hδ, hb⟩ := h
  exact lt_of_lt_of_le hδ (hb m)

/-- **THE KERNEL-CHECKED GAP** — why no finite table settles the
wall: there are margin sequences strictly positive at EVERY rung that
admit NO uniform lower bound (witness 1/(m+1)).  Per-rung certified
positivity, extended to all rungs, is still strictly weaker than
`UniformMarginBound`. -/
theorem pointwise_pos_not_uniform :
    ∃ margin : ℕ → ℝ, (∀ m, 0 < margin m) ∧
      ¬ UniformMarginBound margin := by
  refine ⟨fun m => 1 / ((m : ℝ) + 1), fun m => by positivity, ?_⟩
  rintro ⟨δ, hδ, hb⟩
  obtain ⟨n, hn⟩ := exists_nat_gt (1 / δ)
  have hlt : 1 / ((n : ℝ) + 1) < δ := by
    have h1 : (0 : ℝ) < 1 / δ := by positivity
    have h2 : 1 / δ < (n : ℝ) + 1 := by linarith
    calc 1 / ((n : ℝ) + 1) < 1 / (1 / δ) :=
          one_div_lt_one_div_of_lt h1 h2
      _ = δ := one_div_one_div δ
  exact absurd (hb n) (not_le.mpr hlt)

end Ladder

/-! ### (5) The bridge theorem (the excess-coordinates sector floor) -/

section Bridge

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)]

/-- A rung ladder in identified-corner coordinates: per rung a
structural block S_m, a comb block C_m, and the identified witness
x_m (the deployed corner direction whose Rayleigh value is the
floor margin tau_X at that rung). -/
structure RungLadder (κ : ℕ → Type*) [∀ m, Fintype (κ m)] where
  /-- The comb-blind structural block at rung m. -/
  S : ∀ m, Matrix (κ m) (κ m) ℝ
  /-- The prime-power comb block at rung m. -/
  C : ∀ m, Matrix (κ m) (κ m) ℝ
  /-- The identified witness direction at rung m. -/
  x : ∀ m, κ m → ℝ

/-- The floor margin at rung m: the full form S + C on the witness
(the formal stand-in for tau_X at that rung). -/
def RungLadder.floorMargin (L : RungLadder κ) (m : ℕ) : ℝ :=
  formAt (L.S m + L.C m) (L.x m)

/-- The structural part at rung m (the comb-blind giant). -/
def RungLadder.structuralPart (L : RungLadder κ) (m : ℕ) : ℝ :=
  formAt (L.S m) (L.x m)

/-- The excess at rung m (the arithmetic giant). -/
def RungLadder.excess (L : RungLadder κ) (m : ℕ) : ℝ :=
  excessAt (L.S m) (L.C m) (L.x m)

/-- **The per-rung decomposition, proven**: tau_X splits as the
structural part plus the excess on every rung. -/
theorem RungLadder.decomposition (L : RungLadder κ) (m : ℕ) :
    L.floorMargin m = L.structuralPart m + L.excess m := by
  rw [floorMargin, structuralPart, excess, excessAt]; ring

/-- The excess is the comb form on the witness, rung by rung. -/
theorem RungLadder.excess_eq_comb (L : RungLadder κ) (m : ℕ) :
    L.excess m = formAt (L.C m) (L.x m) :=
  excessAt_eq_comb _ _ _

/-- **The named hypotheses are related but distinct**:
`UniformMarginBound` on the floor margins IMPLIES the per-rung
`IdentificationPositivity` instance of SectorPositiveDescent — the
identified functional being the quadratic form at the rung's witness,
evaluated at the rung's full matrix S + C.  The converse FAILS: an
`IdentificationPositivity` instance is one nonnegativity at one
matrix, and even strict per-rung positivity at every rung does not
recover the uniform delta (`pointwise_pos_not_uniform`).  The uniform
quantifier is strictly stronger — that strength is exactly the open
wall. -/
theorem uniform_to_identification (L : RungLadder κ)
    (h : UniformMarginBound L.floorMargin) (m : ℕ) :
    SectorPositiveDescent.IdentificationPositivity
      (fun G => formAt G (L.x m)) (L.S m + L.C m) :=
  le_of_lt (uniformMarginBound_pos h m)

/-- **THE EXCESS FLOOR** — the module's final theorem, the
excess-coordinates analogue of `sector_floor`, with the logical
geography kernel-checked.  Given a rung ladder:

  * PROVEN (structural): the per-rung decomposition
    tau_X = structural + excess, with the excess carried exactly by
    the comb block;
  * HYPOTHESIS (named, not proven): `uniform_margin_bound` — the
    single non-structural input, passed through untouched;
  * CONSEQUENCES: a uniform strictly positive floor delta on all
    rungs, strict positivity at every rung, and the per-rung
    `IdentificationPositivity` instances of SectorPositiveDescent.

Structural pieces + the one named hypothesis ⇒ the floor statement
for all rungs. -/
theorem excess_floor (L : RungLadder κ)
    (uniform_margin_bound : UniformMarginBound L.floorMargin) :
    (∀ m, L.floorMargin m = L.structuralPart m + L.excess m) ∧
    (∀ m, L.excess m = formAt (L.C m) (L.x m)) ∧
    (∃ δ : ℝ, 0 < δ ∧ ∀ m, δ ≤ L.floorMargin m) ∧
    (∀ m, 0 < L.floorMargin m) ∧
    (∀ m, SectorPositiveDescent.IdentificationPositivity
      (fun G => formAt G (L.x m)) (L.S m + L.C m)) :=
  ⟨L.decomposition, L.excess_eq_comb, uniform_margin_bound,
    uniformMarginBound_pos uniform_margin_bound,
    uniform_to_identification L uniform_margin_bound⟩

end Bridge

end ExcessSkeleton
end TfptCarrier
