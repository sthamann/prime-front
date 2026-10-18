/-
  CofinalWeil — the minimal H theorem: cofinal positivity suffices.
  ================================================================

  The MINIMAL load-bearing statement of the extraction chain (work
  package F1, 2026-08-07 evening plan), REPLACING the over-strong
  `UniformMarginBound` of ExcessSkeleton in the RH-side geography.
  Numeric counterpart: `experiments/tfpt-discovery/
  continuum_extraction_probe.py` (PRIME.EXTRACTION.CHAIN.01, run 2,
  19/19 PASS, verdict EXTRACTION-CHAIN-COMPLETE): the implication
  chain needs NO Mosco compactness, NO uniform delta, NO diagonal
  argument — per-element convergence of the ladder forms plus
  positivity along ONE supplied ladder, cofinal IN THE
  MESH-REFINEMENT ORDER in which that convergence holds, already
  forces the limit functional to be nonnegative on the dense family.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`).

    (1) `CofinalHypothesis` — THE MATHEMATICAL CORE of the cofinal
        hypothesis (H_cof): a strictly monotone index sequence
        m_j → ∞ along which the ladder matrices are PSD.  This
        structure records the resulting index and certificates; it
        does NOT track how a producer computed the index.  The
        PREDEFINED/sign-independent audit premise is made explicit
        by `CofinalPredefinition.PredefinedCofinalHypothesis`.

    (2) `limit_nonneg_of_cofinal_seq` — THE MINIMAL IMPLICATION at
        sequence level: q_m(v) → L and q_{m_j}(v) ≥ 0 on the ladder
        force L ≥ 0.  This IS the ε/2 argument
        (L = lim_j q_{m_j}(v) ≥ 0), packaged as
        `ge_of_tendsto'` along the subsequence — PROVEN, not
        assumed.  `weil_nonneg_of_cofinal` — the same for a whole
        dense family: per-element convergence of the ladder forms
        to the limit functional + (H_cof) ⇒ the limit functional is
        nonnegative on the WHOLE dense family.  No diagonal
        argument appears: the same cofinal ladder serves every
        element simultaneously (matrix PSD is uniform in the
        witness).

    (3) THE RELATION LEMMAS — the strict hierarchy, kernel-checked:
          `uniformMarginBound_to_cofinal`   (uniform ⇒ cofinal),
          `pointwise_to_cofinal`            (all-rung ⇒ cofinal),
          `cofinal_not_uniform`             (cofinal ⇏ uniform,
                                             witness 1/(m+1) via
                                             ExcessSkeleton.pointwise_pos_not_uniform),
          `cofinal_not_pointwise`           (cofinal ⇏ all-rung,
                                             witness ±1 on the even
                                             ladder).
        Together with `ExcessSkeleton.uniformMarginBound_pos` and
        `ExcessSkeleton.pointwise_pos_not_uniform`:
        uniform ⊊ pointwise ⊊ cofinal — the old hypothesis is
        STRICTLY stronger, twice over.

    (4) `cofinal_weil` — the assembly: ladder matrices + sampling
        maps + per-element form convergence + (H_cof) ⇒ nonnegative
        ladder values on the cofinal rungs, convergence along the
        ladder, and nonnegativity of the limit functional on the
        dense family.

  WHAT IS ABSENT — BY DESIGN (the point of the theorem; the
  acceptance list of F1).  The hypotheses of `cofinal_weil` contain:
    * NO uniform margin (no `UniformMarginBound`, no δ > 0),
    * NO inverse matrix and no resolvent,
    * NO Mosco convergence and no coercivity,
    * NO limit operator — only the limit VALUES QW(v) appear;
      no operator on any limit space is constructed or assumed,
    * NO diagonal argument — the quantifier order is
      ∀ element ∃ limit, with ONE ladder for all elements.
  Only three inputs remain: the dense family (as an abstract index
  type — density itself and the continuity extension to all test
  functions are the two classical lemmas of the probe's synthesis,
  typed there as citations, deliberately NOT formalized here; NOTE
  the 2026-08-13 correction: the extension hypothesis is NOT
  C⁰-continuity of Q_W in the pure sup norm, which is FALSE — the
  even Lipschitz family e_n(w) = (1/n) min(1, w/e^{-n²}) (1 − w/2)_+
  has ‖e_n‖_∞ → 0 while |A[e_n]| grows linearly, v912 control C5 —
  but uniform convergence PLUS an equi-Lipschitz/Dini condition at
  the origin, supplied by the admissible even compactly supported BV
  class; the DENSITY leg in that topology remains the citation),
  per-element form convergence (Piece 2, no longer a measurement:
  PROVEN unconditionally at rate O(D² log(1/D)) = O(2^{-2j} j) with
  explicit constants — verification/v912_form_convergence_theorem.py;
  see `CofinalEnvelope.lean`, which states that envelope as a named
  premise and DERIVES the `hconv` below from it), and cofinal
  positivity (H_cof — the arithmetic wall, and nothing else).

  THE HONEST BOUNDARY.  (H_cof) is the named hypothesis this module
  is ABOUT — it stays a hypothesis everywhere; nothing here proves,
  gates, or even evaluates positivity of any actual tower form.
  Relation to the ExcessSkeleton boundary: `UniformMarginBound`
  implies (H_cof) (`uniformMarginBound_to_cofinal`) and the converse
  fails kernel-checked (`cofinal_not_uniform`) — the wall content
  has strictly decreased.  No continuum theorem, no RH statement, no
  arithmetic identification is formalized or claimed here.
-/
import TfptCarrier.ExcessSkeleton

namespace TfptCarrier
namespace CofinalWeil

open Filter Topology Matrix ExcessSkeleton

/-! ### (1) The cofinal hypothesis (H_cof) -/

section Hypothesis

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)]

/-- **THE MATHEMATICAL CORE OF THE COFINAL HYPOTHESIS (H_cof)** —
the minimal positivity input used by the limit proof: a strictly
monotone index sequence m_j → ∞ along which the ladder matrices are
PSD.

THE ORDER IS THE MESH-REFINEMENT ORDER.  `idx` is cofinal in the
index `m` of `A`, and in the deployed instantiation that index is the
MESH level (`CofinalEnvelope.mesh m = 2^(-m)`) — the order in which
`hconv` holds.  Cofinality in the WINDOW/cap parameter at a FIXED
mesh D₀ is NOT admissible: past the faithful cap the deployed read is
already exactly cap-independent, so such a ladder is eventually
CONSTANT and converges to QW + W_C[e_{D₀}], not to QW; positivity
along it yields only QW ≥ -|W_C[e_{D₀}]| (measured false floors
-2.114e-03 at D₀ = 1/32 and -2.128e-04 at D₀ = 1/128,
`experiments/tfpt-discovery/hcof_dodging_audit_probe.py` S6.8).

PREREGISTRATION DEMAND: the sequence `idx` must be chosen
INDEPENDENTLY of any measured signs.  This structure does NOT enforce
that algorithmic demand: a caller can inspect `A` before constructing
the value, and ordinary field/binder order is not an information-flow
theorem.  `CofinalPredefinition.lean` supplies the hardened API with an
explicit abstract `NoninterferenceContract`, a negative sign-mining
example, and the formal provenance-erasure limitation.  This
mathematical core replaces the over-strong
`ExcessSkeleton.UniformMarginBound`: no uniform margin δ > 0 is
demanded, only PSD at the ladder rungs. -/
structure CofinalHypothesis (A : ∀ m, Matrix (κ m) (κ m) ℝ) where
  /-- The selected ladder.  This field stores a value, not its
  computational provenance; see the structure doc comment. -/
  idx : ℕ → ℕ
  /-- The ladder is strictly monotone (hence tends to ∞). -/
  mono : StrictMono idx
  /-- PSD at every ladder rung — nothing about the rungs between. -/
  psd : ∀ j, (A (idx j)).PosSemidef

end Hypothesis

/-! ### (2) The minimal implication -/

section Implication

/-- **THE MINIMAL IMPLICATION, sequence level** — the ε/2 argument,
proven: if the form values converge, q_m(v) → L, and are
nonnegative along a strictly monotone ladder, q_{m_j}(v) ≥ 0, then
the limit is nonnegative: L = lim_j q_{m_j}(v) ≥ 0.  No uniform
margin, no rate, no monotonicity of the values — cofinal
nonnegativity plus convergence alone.

WHY COFINALITY SUFFICES, in one line: if L < 0 then convergence makes
the catch set {m : q_m < 0} a TAIL of the mesh order, and a cofinal
set meets every tail.  This is the entire immunity of the hypothesis,
and it is exactly what an index criterion whose catch set is merely
almost-periodic (unbounded complement) does not have. -/
theorem limit_nonneg_of_cofinal_seq {q : ℕ → ℝ} {L : ℝ}
    (idx : ℕ → ℕ) (hmono : StrictMono idx)
    (hpos : ∀ j, 0 ≤ q (idx j))
    (hconv : Tendsto q atTop (𝓝 L)) : 0 ≤ L :=
  ge_of_tendsto' (hconv.comp hmono.tendsto_atTop) hpos

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}

/-- The ladder form: the quadratic form of the rung-m matrix at the
rung-m sample of the element v — the formal stand-in for
Q_m(v) = D_m (S_m v)ᵀ T_m (S_m v) of the extraction probe. -/
def ladderForm (A : ∀ m, Matrix (κ m) (κ m) ℝ)
    (sample : ∀ m, V → κ m → ℝ) (m : ℕ) (v : V) : ℝ :=
  formAt (A m) (sample m v)

/-- PSD rungs have nonnegative ladder forms at EVERY element — the
reason no diagonal argument is needed: one PSD certificate per rung
covers the whole dense family at once. -/
theorem ladderForm_nonneg {A : ∀ m, Matrix (κ m) (κ m) ℝ}
    (sample : ∀ m, V → κ m → ℝ) {m : ℕ} (hm : (A m).PosSemidef)
    (v : V) : 0 ≤ ladderForm A sample m v :=
  posSemidef_formAt_nonneg hm (sample m v)

/-- **THE MINIMAL H THEOREM** (dense-family form): per-element
convergence of the ladder forms to the limit functional QW on the
dense family, plus (H_cof), force QW ≥ 0 on the WHOLE family.  The
hypotheses contain no uniform margin, no inverse, no Mosco
coercivity, and no limit operator — only density (V), form
convergence, cofinal positivity. -/
theorem weil_nonneg_of_cofinal {A : ∀ m, Matrix (κ m) (κ m) ℝ}
    (H : CofinalHypothesis A) (sample : ∀ m, V → κ m → ℝ)
    (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    ∀ v, 0 ≤ QW v := fun v =>
  limit_nonneg_of_cofinal_seq H.idx H.mono
    (fun j => ladderForm_nonneg sample (H.psd j) v) (hconv v)

end Implication

/-! ### (3) The relation lemmas: uniform ⊊ pointwise ⊊ cofinal -/

section Relations

/-- A supplied ladder `idx` witnesses cofinal nonnegativity of a
margin sequence.  The binder order matches the intended
preregistration API but does not prove computational independence. -/
def IsCofinalWitness (margin : ℕ → ℝ) (idx : ℕ → ℕ) : Prop :=
  StrictMono idx ∧ ∀ j, 0 ≤ margin (idx j)

/-- **The old hypothesis is stronger**: a uniform margin bound gives
cofinal nonnegativity — on the identity ladder, with room to spare
(the bound is strict at every rung). -/
theorem uniformMarginBound_to_cofinal {margin : ℕ → ℝ}
    (h : UniformMarginBound margin) :
    IsCofinalWitness margin id :=
  ⟨strictMono_id, fun j => (uniformMarginBound_pos h j).le⟩

/-- All-rung nonnegativity gives cofinal nonnegativity (identity
ladder) — the intermediate rung of the hierarchy. -/
theorem pointwise_to_cofinal {margin : ℕ → ℝ}
    (h : ∀ m, 0 ≤ margin m) : IsCofinalWitness margin id :=
  ⟨strictMono_id, fun j => h j⟩

/-- **Converse failure 1 (the honest note)**: cofinal — even
ALL-RUNG STRICT — positivity does NOT give a uniform margin bound.
Witness 1/(m+1), reusing the kernel-checked gap
`ExcessSkeleton.pointwise_pos_not_uniform`.  H_cof is strictly
weaker than `UniformMarginBound`: replacing the latter by the former
is a genuine reduction of the wall. -/
theorem cofinal_not_uniform :
    ∃ margin : ℕ → ℝ, IsCofinalWitness margin id ∧
      ¬ UniformMarginBound margin := by
  obtain ⟨margin, hpos, hnu⟩ := pointwise_pos_not_uniform
  exact ⟨margin, ⟨strictMono_id, fun j => (hpos j).le⟩, hnu⟩

/-- **Converse failure 2**: cofinal nonnegativity does not even give
all-rung nonnegativity — witness ±1 on the even ladder idx j = 2j
(the odd rungs are strictly negative).  H_cof genuinely quantifies
over the ladder only. -/
theorem cofinal_not_pointwise :
    ∃ (margin : ℕ → ℝ) (idx : ℕ → ℕ),
      IsCofinalWitness margin idx ∧ ∃ m, margin m < 0 := by
  refine ⟨fun m => if Even m then 1 else -1, fun j => 2 * j,
    ⟨fun a b h => by dsimp only; omega, fun j => ?_⟩,
    1, by norm_num [Nat.even_iff]⟩
  dsimp only
  rw [if_pos ⟨j, two_mul j⟩]
  norm_num

end Relations

/-! ### (4) The assembly -/

section Assembly

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}

/-- **COFINAL WEIL** — the module's final theorem, the minimal
extraction statement with the logical geography kernel-checked.
Given ladder matrices, sampling maps, per-element form convergence
on the dense family, and the ONE named hypothesis (H_cof):

  * PROVEN: the ladder forms are nonnegative at every cofinal rung
    for every element; the forms converge along the ladder; the
    limit functional is nonnegative on the whole dense family.
  * ABSENT BY DESIGN: uniform margins, inverses, Mosco coercivity,
    limit operators, diagonal arguments — none is needed, none
    appears.

Only density, form convergence, and cofinal positivity enter — the
measured quantifier reduction of EXTRACTION-CHAIN-COMPLETE, as a
kernel-checked implication.  This core theorem does not certify the
provenance of `H.idx`; the hardened wrapper
`CofinalPredefinition.cofinal_weil_predefined` adds the named external
noninterference premise. -/
theorem cofinal_weil {A : ∀ m, Matrix (κ m) (κ m) ℝ}
    (H : CofinalHypothesis A) (sample : ∀ m, V → κ m → ℝ)
    (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    (∀ j v, 0 ≤ ladderForm A sample (H.idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (H.idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  ⟨fun j v => ladderForm_nonneg sample (H.psd j) v,
    fun v => (hconv v).comp H.mono.tendsto_atTop,
    weil_nonneg_of_cofinal H sample QW hconv⟩

end Assembly

end CofinalWeil
end TfptCarrier
