/-
  WallCofinalComposition — plugging the certified finite head into
  the cofinal Weil implication.
  =================================================================

  This module composes the kernel-checked per-rung certificates of
  WallLadderChecker (the exported v897 wall matrices, each proven
  positive definite by `decide` in the Lean kernel) with the minimal
  H theorem `CofinalWeil.cofinal_weil`.  It is the FORMAL SEAM between
  the finite head of the prime-front wall and the RH-side geography —
  stated so that every remaining gap is a NAMED hypothesis, never
  papered over.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`, no axioms):

    (1) `posSemidef_of_bridge` — a true ladder matrix that dominates
        (in the PSD order) a nonnegative multiple of a certified PD
        certificate matrix is itself PSD.  This is the lemma through
        which a kernel-checked integer certificate lifts to the true
        analytic rung.

    (2) `head_psd_of_enclosure` — the finite-head composition: the
        per-rung kernel certificates (a list `ds`) plus the per-rung
        enclosure bridges give PSD of the TRUE ladder matrices at
        every head position `j < ds.length`.

    (3) `cofinalHypothesis_of_head_tail` — finite head + named tail
        assemble into exactly `CofinalWeil.CofinalHypothesis` (H_cof),
        the one positivity input of the cofinal Weil implication.
        The supplied `idx` must be cofinal in the MESH-REFINEMENT
        order in which `hconv` holds, not merely in the window depth:
        at fixed mesh the read is eventually constant and converges
        to the wrong limit.

    (4) `wall_cofinal_weil` — the end-to-end composition: certified
        head + `HeadEnclosure` + `TailPositivity` + per-element form
        convergence ⇒ the full conclusion of `cofinal_weil` (cofinal
        nonnegativity, convergence along the ladder, and QW ≥ 0 on
        the dense family).

  THE HONEST BOUNDARY — the two NAMED HYPOTHESES this module is
  about (deliberately hypotheses, NOT theorems):

    * `HeadEnclosure` — the interval-enclosure identification: the
      true rung-j wall matrix dominates Q⁻¹ times the exported
      integer certificate matrix.  This is EXACTLY the v897 E1–E4
      error accounting (node-enclosure lemma, outward-rounded
      archimedean layer, tent-atom rigour, and the rigorous shift
      shift_int = h + ⌈2·h·rad_max·Q⌉ giving
      K_true ⪰ (N − shift·1)/Q).  It is carried by the Python
      interval arithmetic of verification/v897_*.py and is NOT
      re-proven in Lean — no analytic ladder assembly is formalized
      here.

    * `TailPositivity` — everything beyond the kernel-checked head:
      the reachable rungs not (yet) kernel-checked AND the entire
      asymptotic tail h → ∞.  No finite table can discharge it
      (`ExcessSkeleton.pointwise_pos_not_uniform` is the kernel-checked
      reminder); it stays with the registered port contracts
      (PRIME.PORT.TAIL.01 / PRIME.PORT.LEADING.SIGN.01).

  NO RH claim.  `cofinal_weil` is an implication with (H_cof) as
  input; this module shrinks the unproven part of (H_cof) by the
  kernel-checked head and NAMES what remains.  For the preregistered
  reading, PREDEFINED/noninterference is an additional external
  premise made explicit by `CofinalPredefinition.lean`; this module's
  binder order alone does not prove it.
-/
import TfptCarrier.CofinalWeil
import TfptCarrier.WallLadderChecker

namespace TfptCarrier
namespace WallLadder

open Matrix Filter Topology CofinalWeil

/-! ### (1) The enclosure bridge -/

/-- **NAMED HYPOTHESIS (the enclosure bridge)**: the true rung matrix
`B` dominates `Q⁻¹` times the exported integer certificate matrix (up
to the index identification `e`).  This is v897's E4 error accounting
`K_true ⪰ (N − shift·1)/Q`, external to Lean. -/
def EnclosureBridge {ι : Type*} [Fintype ι] (B : Matrix ι ι ℝ)
    (d : RungData) : Prop :=
  ∃ e : ι ≃ Fin d.h,
    (B - ((Qgrid : ℝ))⁻¹ • (MmatR d).submatrix e e).PosSemidef

/-- A bridge from a PSD certificate forces the true rung PSD:
`B = (B − Q⁻¹·M') + Q⁻¹·M'` with both summands PSD. -/
theorem posSemidef_of_bridge {ι : Type*} [Fintype ι]
    {B : Matrix ι ι ℝ} {d : RungData} (hM : (MmatR d).PosSemidef)
    (hB : EnclosureBridge B d) : B.PosSemidef := by
  obtain ⟨e, hpsd⟩ := hB
  have hq : (0 : ℝ) ≤ ((Qgrid : ℝ))⁻¹ := by
    rw [Qgrid]
    norm_num
  have h1 : (((Qgrid : ℝ))⁻¹ • (MmatR d).submatrix e e).PosSemidef :=
    (hM.submatrix e).smul hq
  have h2 := hpsd.add h1
  rwa [sub_add_cancel] at h2

/-! ### (2) The named hypotheses of the composition -/

section Ladder

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)]

/-- **NAMED HYPOTHESIS (the head identification)**: each of the first
`ds.length` ladder rungs (ascending h, the certified prefix of the
v897 census) satisfies the enclosure bridge against its exported
certificate.  Backed by the v897 interval arithmetic — NOT proven in
Lean. -/
def HeadEnclosure (A : ∀ m, Matrix (κ m) (κ m) ℝ) (idx : ℕ → ℕ)
    (ds : List RungData) : Prop :=
  ∀ (j : ℕ) (hj : j < ds.length),
    EnclosureBridge (A (idx j)) (ds.get ⟨j, hj⟩)

/-- **NAMED HYPOTHESIS (the remaining wall)**: PSD of the true ladder
matrices at every rung index `≥ J` — the reachable rungs not (yet)
kernel-checked AND the whole asymptotic tail h → ∞.  This is the open
part of (H_cof); no finite table can discharge it. -/
def TailPositivity (A : ∀ m, Matrix (κ m) (κ m) ℝ) (idx : ℕ → ℕ)
    (J : ℕ) : Prop :=
  ∀ j, J ≤ j → (A (idx j)).PosSemidef

/-! ### (3) The composition into (H_cof) -/

/-- **THE FINITE-HEAD COMPOSITION**: kernel certificates + enclosure
bridges force PSD of the TRUE ladder matrices on the whole head. -/
theorem head_psd_of_enclosure {A : ∀ m, Matrix (κ m) (κ m) ℝ}
    {idx : ℕ → ℕ} {ds : List RungData}
    (hcert : ∀ d ∈ ds, (MmatR d).PosSemidef)
    (hbridge : HeadEnclosure A idx ds) :
    ∀ (j : ℕ), j < ds.length → (A (idx j)).PosSemidef := fun j hj =>
  posSemidef_of_bridge
    (hcert (ds.get ⟨j, hj⟩) (ds.get_mem ⟨j, hj⟩)) (hbridge j hj)

/-- **HEAD + TAIL = (H_cof)**: the certified finite head and the named
tail hypothesis assemble into exactly the `CofinalHypothesis` that
`CofinalWeil.cofinal_weil` consumes.  The ladder `idx` is an explicit
parameter, but this theorem does not infer its computational provenance;
the hardened API requires the separate external noninterference
certificate. -/
def cofinalHypothesis_of_head_tail (A : ∀ m, Matrix (κ m) (κ m) ℝ)
    (idx : ℕ → ℕ) (hmono : StrictMono idx) (J : ℕ)
    (head : ∀ j, j < J → (A (idx j)).PosSemidef)
    (tail : TailPositivity A idx J) :
    CofinalHypothesis A where
  idx := idx
  mono := hmono
  psd := fun j => by
    rcases Nat.lt_or_ge j J with h | h
    · exact head j h
    · exact tail j h

/-! ### (4) The end-to-end theorem -/

/-- **WALL COFINAL WEIL** — the module's final theorem, the full
composition chain:

  kernel-checked per-rung certificates (hcert; `decide` on exported
  v897 data)  +  `HeadEnclosure` (NAMED: the v897 interval-enclosure
  identification)  +  `TailPositivity` (NAMED: everything beyond the
  checked head)  +  per-element form convergence

  ⇒  the conclusion of `CofinalWeil.cofinal_weil`: nonnegative ladder
  values on all rungs of the supplied ladder, convergence along it,
  and nonnegativity of the limit functional on the dense family.

Only the two NAMED hypotheses and form convergence remain unproven —
the finite head itself is closed by the kernel.  PREDEFINED is not among
the mathematical premises used by this implication; it remains the
external audit premise of `CofinalPredefinition`. -/
theorem wall_cofinal_weil {V : Type*}
    (A : ∀ m, Matrix (κ m) (κ m) ℝ) (idx : ℕ → ℕ)
    (hmono : StrictMono idx) (ds : List RungData)
    (hcert : ∀ d ∈ ds, (MmatR d).PosSemidef)
    (hbridge : HeadEnclosure A idx ds)
    (htail : TailPositivity A idx ds.length)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    (∀ j v, 0 ≤ ladderForm A sample (idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  cofinal_weil
    (cofinalHypothesis_of_head_tail A idx hmono ds.length
      (head_psd_of_enclosure hcert hbridge) htail)
    sample QW hconv

end Ladder

end WallLadder
end TfptCarrier
