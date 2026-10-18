/-
  GradeNoGo — FORM.PRIME.GRADE.NO_GO.01: the grade barrier as a
  kernel-checked class-closure theorem.
  ================================================================

  THE DISCOVERY (round 33, 2026-08-08): the entire graveyard of
  direct positivity architectures on the prime front reduces to ONE
  homogeneity law.  A target that is 1-homogeneous in the arithmetic
  weights (grade 1: amplitudes enter linearly) can NEVER be matched
  exactly by a Gram square (grade 2: any B(m)*B(m) with linear B is
  2-homogeneous) — evaluating on a single scaling ray at two scalars
  kills it.  The proof is almost laughably short; that is its
  strength: it is a CLASS closure, not a construction failure.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`; over ℝ, where ᴴ is the transpose).

    (1) `grade_no_go` — THE CORE NO-GO (the two-line proof): if A is
        1-homogeneous along the ray of m (A(t·m) = t·A(m), t ≥ 0),
        G is 2-homogeneous along it (G(t·m) = t²·G(m)), and
        A = G on the ray, then A(m) = 0.  Evaluate at t = 1 and
        t = 2: 2·A(m) = 4·A(m).  `gram_two_homogeneous` — Gram
        squares of LINEAR maps are 2-homogeneous, so
        `grade_no_go_gram`: an exact Gram match of a 1-homogeneous
        target on a ray forces A(m) = 0 AND B(m) = 0.

    (2) THE AFFINE TRILEMMA: `affine_gram_expansion` — the exact
        expansion (B₀+Y)ᴴ(B₀+Y) = B₀ᴴB₀ + (B₀ᴴY + YᴴB₀) + YᴴY into
        the three named components `constantPrice` (grade 0),
        `crossTerm` (grade 1 — the only grade-1 slot a Gram square
        owns), `quadraticPrice` (grade 2).  `affine_gram_tax` — THE
        TAX: if the target is the linear cross term alone, the
        representation error is EXACTLY constantPrice +
        quadraticPrice, both PSD; the error is PSD and its trace
        (= the sum of the two price traces, ≥ 0) is the tax every
        affine background pays.  `affine_grade_no_go` — the
        exhaustive case statement for the affine family: EXACT
        matching of a 1-homogeneous target by an affine Gram on a
        ray forces A(m) = 0, B₀ = 0 AND B₁(m) = 0 — within the
        affine family nothing survives.

        THE TRILEMMA READING (doc-level corollary; the disjunction
        below is the informal wrapper, the kernel content is
        `affine_grade_no_go` + `affine_gram_tax`): any direct
        positive Gram representation of a NONTRIVIAL linear target
        must either (i) let B depend on m through a square root or
        other non-linear map (leaving the linear class — the
        homogeneity mismatch is repaired by hand), or (ii) divide —
        denominators / Schur complements (those died separately: the
        Schur–Gram tax measurement), or (iii) keep a constant
        background B₀ ≠ 0 and pay the PSD tax of `affine_gram_tax`
        (equality only up to the certified error), or (iv) lower the
        grade — stop representing amplitudes and represent RATES
        (see (3)).  What stays informal here: that (i)–(iv) is
        exhaustive for architectures OUTSIDE the affine-Gram family;
        the kernel-checked part is that INSIDE it, exactness is
        impossible and the affine escape is priced.

    (3) `tangent_psd_on_kernel_null` — THE GRADE-LOWERING EXISTENCE
        (the positive counterpart; the door the new route uses): if
        K(t) is PSD for all t ≥ 0 and x is a null vector of the
        form of K(0) (xᵀK(0)x = 0), then any right-derivative limit
        Ψ of the difference quotients (K(t) − K(0))/t (entrywise,
        along t ↓ 0) satisfies xᵀΨx ≥ 0 — nonnegativity of the form
        difference quotient passes to the limit (`ge_of_tendsto`).
        This is the ONLY grade-1 positivity mechanism NOT excluded
        by (1)–(2): the derivative of a PSD family at a kernel-null
        direction is grade-lowering — RATES, not amplitudes.
        Provenance: the PRIME.EULER.SCHUR program (round 33,
        packages B–D); this lemma is the abstract elevator those
        packages instantiate.

  HONESTY NOTES (what the no-go does NOT say).  The no-go excludes
  EXACT matching by Gram squares of linear maps on a scaling ray —
  nothing more: representations with denominators (Schur
  complements) are not touched by (1) (they died separately, by the
  measured Schur–Gram tax — cited, not re-proven here); non-Gram
  mechanisms (signed measures, oscillatory integrals) are outside
  the class closure entirely.  The four graveyard instances of the
  round-32/33 discovery probes — the Schur–Gram tax, the variance
  grade gap, the projection blindness, the phase-leverage failure —
  are instances/relatives of this one law: each tried to place a
  grade-1 arithmetic target into a grade-0/grade-2 positive slot.
  Their probe measurements stay the numeric provenance; this module
  is the common closure.  No continuum theorem, no RH statement, no
  arithmetic identification is formalized or claimed here.
-/
import TfptCarrier.ExcessSkeleton
import Mathlib.Data.Real.StarOrdered

namespace TfptCarrier
namespace GradeNoGo

open Filter Topology Matrix ExcessSkeleton

variable {ι ρ : Type*} [Fintype ι] [Fintype ρ]
variable {M : Type*} [AddCommGroup M] [Module ℝ M]

/-! ### (1) The core no-go -/

omit [Fintype ι] in
/-- **THE CORE NO-GO** (the two-line proof — its brevity is the
point: this is a class closure, not a construction failure): a
1-homogeneous map and a 2-homogeneous map that agree on a scaling
ray agree with 0 at the base point.  Evaluate at t = 1 and t = 2:
2·A(m) = 4·A(m), hence A(m) = 0. -/
theorem grade_no_go (A G : M → Matrix ι ι ℝ) (m : M)
    (hA : ∀ t : ℝ, 0 ≤ t → A (t • m) = t • A m)
    (hG : ∀ t : ℝ, 0 ≤ t → G (t • m) = t ^ 2 • G m)
    (heq : ∀ t : ℝ, 0 ≤ t → A (t • m) = G (t • m)) :
    A m = 0 := by
  have e1 : A m = G m := by
    have h := heq 1 zero_le_one
    rwa [hA 1 zero_le_one, hG 1 zero_le_one, one_smul, one_pow,
      one_smul] at h
  have e2 : (2 : ℝ) • A m = (4 : ℝ) • A m := by
    have h := heq 2 (by norm_num)
    rw [hA 2 (by norm_num), hG 2 (by norm_num), ← e1,
      (by norm_num : ((2 : ℝ) ^ 2) = 4)] at h
    exact h
  have e3 : ((2 : ℝ) - 4) • A m = 0 := by
    rw [sub_smul, e2, sub_self]
  have hne : ((2 : ℝ) - 4) ≠ 0 := by norm_num
  calc A m = ((2 : ℝ) - 4)⁻¹ • (((2 : ℝ) - 4) • A m) := by
        rw [smul_smul, inv_mul_cancel₀ hne, one_smul]
    _ = 0 := by rw [e3, smul_zero]

omit [Fintype ι] in
/-- Gram squares of LINEAR maps are 2-homogeneous:
(B(t·m))ᴴ B(t·m) = t² · (B(m))ᴴ B(m).  This is the grade count that
collides with any 1-homogeneous target. -/
theorem gram_two_homogeneous (B : M →ₗ[ℝ] Matrix ρ ι ℝ) (m : M)
    (t : ℝ) :
    (B (t • m))ᴴ * B (t • m) = t ^ 2 • ((B m)ᴴ * B m) := by
  rw [map_smul, Matrix.conjTranspose_smul, star_trivial,
    Matrix.smul_mul, Matrix.mul_smul, smul_smul, sq]

omit [Fintype ι] in
/-- **The Gram form of the no-go**: an EXACT Gram-square match of a
1-homogeneous target along a scaling ray annihilates both sides —
the target vanishes at the base point and so does the Gram factor.
Grade 1 cannot live inside grade 2. -/
theorem grade_no_go_gram (A : M → Matrix ι ι ℝ)
    (B : M →ₗ[ℝ] Matrix ρ ι ℝ) (m : M)
    (hA : ∀ t : ℝ, 0 ≤ t → A (t • m) = t • A m)
    (heq : ∀ t : ℝ, 0 ≤ t → A (t • m) = (B (t • m))ᴴ * B (t • m)) :
    A m = 0 ∧ B m = 0 := by
  have hA0 : A m = 0 :=
    grade_no_go A (fun x => (B x)ᴴ * B x) m hA
      (fun t _ => gram_two_homogeneous B m t) heq
  refine ⟨hA0, ?_⟩
  have h := heq 1 zero_le_one
  rw [one_smul, hA0] at h
  exact Matrix.conjTranspose_mul_self_eq_zero.mp h.symm

/-! ### (2) The affine trilemma -/

/-- The grade-0 component: the constant price B₀ᴴB₀ of an affine
background (PSD — it never helps a sign, it only costs). -/
def constantPrice (B₀ : Matrix ρ ι ℝ) : Matrix ι ι ℝ :=
  B₀ᴴ * B₀

/-- The grade-1 component: the linear cross term B₀ᴴY + YᴴB₀ — the
ONLY grade-1 slot a Gram square owns (over ℝ this is 2·Re(B₀ᴴY)). -/
def crossTerm (B₀ Y : Matrix ρ ι ℝ) : Matrix ι ι ℝ :=
  B₀ᴴ * Y + Yᴴ * B₀

/-- The grade-2 component: the quadratic price YᴴY (PSD). -/
def quadraticPrice (Y : Matrix ρ ι ℝ) : Matrix ι ι ℝ :=
  Yᴴ * Y

omit [Fintype ι] in
/-- **The exact affine expansion** — the algebraic identity behind
the trilemma: an affine Gram square splits into the three graded
components, exactly. -/
theorem affine_gram_expansion (B₀ Y : Matrix ρ ι ℝ) :
    (B₀ + Y)ᴴ * (B₀ + Y)
      = constantPrice B₀ + crossTerm B₀ Y + quadraticPrice Y := by
  simp only [constantPrice, crossTerm, quadraticPrice,
    Matrix.conjTranspose_add]
  rw [Matrix.add_mul, Matrix.mul_add, Matrix.mul_add]
  abel

/-- The constant price is PSD. -/
theorem constantPrice_posSemidef (B₀ : Matrix ρ ι ℝ) :
    (constantPrice B₀).PosSemidef :=
  Matrix.posSemidef_conjTranspose_mul_self B₀

/-- The quadratic price is PSD. -/
theorem quadraticPrice_posSemidef (Y : Matrix ρ ι ℝ) :
    (quadraticPrice Y).PosSemidef :=
  Matrix.posSemidef_conjTranspose_mul_self Y

/-- **THE TAX THEOREM** (abstract form): if the target is the linear
cross term alone, the representation error of the affine Gram square
is EXACTLY constantPrice + quadraticPrice — a sum of two PSD terms.
So the error is PSD, its trace splits into the two price traces, and
that trace — the TAX — is nonnegative: an affine background can
approach a grade-1 target only from above, never exactly (exactness
is `affine_grade_no_go`). -/
theorem affine_gram_tax (B₀ Y : Matrix ρ ι ℝ) :
    (B₀ + Y)ᴴ * (B₀ + Y) - crossTerm B₀ Y
        = constantPrice B₀ + quadraticPrice Y ∧
      ((B₀ + Y)ᴴ * (B₀ + Y) - crossTerm B₀ Y).PosSemidef ∧
      ((B₀ + Y)ᴴ * (B₀ + Y) - crossTerm B₀ Y).trace
        = (constantPrice B₀).trace + (quadraticPrice Y).trace ∧
      0 ≤ ((B₀ + Y)ᴴ * (B₀ + Y) - crossTerm B₀ Y).trace := by
  have hid : (B₀ + Y)ᴴ * (B₀ + Y) - crossTerm B₀ Y
      = constantPrice B₀ + quadraticPrice Y := by
    rw [affine_gram_expansion]; abel
  have hpsd : (constantPrice B₀ + quadraticPrice Y).PosSemidef :=
    (constantPrice_posSemidef B₀).add (quadraticPrice_posSemidef Y)
  refine ⟨hid, by rw [hid]; exact hpsd, by rw [hid, Matrix.trace_add],
    ?_⟩
  rw [hid]
  exact hpsd.trace_nonneg

omit [Fintype ι] in
/-- **The exhaustive affine case** — the trilemma's kernel-checked
core: EXACT matching of a 1-homogeneous target by an AFFINE Gram
square along a scaling ray forces everything to vanish — the target,
the constant background, and the linear factor.  Within the affine
family nothing survives; every escape (nonlinear √-dependence,
denominators, a priced background, grade lowering) leaves the
family — see the module doc for the informal exhaustiveness
reading. -/
theorem affine_grade_no_go (A : M → Matrix ι ι ℝ)
    (B₀ : Matrix ρ ι ℝ) (B₁ : M →ₗ[ℝ] Matrix ρ ι ℝ) (m : M)
    (hA : ∀ t : ℝ, 0 ≤ t → A (t • m) = t • A m)
    (heq : ∀ t : ℝ, 0 ≤ t →
      A (t • m) = (B₀ + B₁ (t • m))ᴴ * (B₀ + B₁ (t • m))) :
    A m = 0 ∧ B₀ = 0 ∧ B₁ m = 0 := by
  have hB₀ : B₀ = 0 := by
    have h := heq 0 le_rfl
    rw [hA 0 le_rfl] at h
    simp only [zero_smul, map_zero, add_zero] at h
    exact Matrix.conjTranspose_mul_self_eq_zero.mp h.symm
  subst hB₀
  have heq' : ∀ t : ℝ, 0 ≤ t →
      A (t • m) = (B₁ (t • m))ᴴ * B₁ (t • m) := by
    intro t ht
    simpa using heq t ht
  obtain ⟨hA0, hB1⟩ := grade_no_go_gram A B₁ m hA heq'
  exact ⟨hA0, rfl, hB1⟩

/-! ### (3) The grade-lowering existence: the tangent door -/

/-- The quadratic form as an explicit double sum (restatement of
`GramCompactness.dotProduct_mulVec_expand` for `formAt`). -/
theorem formAt_expand (A : Matrix ι ι ℝ) (x : ι → ℝ) :
    formAt A x = ∑ i, ∑ j, x i * A i j * x j :=
  GramCompactness.dotProduct_mulVec_expand A x

/-- **THE ELEVATOR LEMMA** (grade-lowering existence — the positive
counterpart of the no-go, and the ONLY grade-1 positivity mechanism
(1)–(2) do not exclude): let K(t) be PSD for all t ≥ 0, and let x be
a null direction of the base form, xᵀK(0)x = 0.  If the entrywise
difference quotients (K(t) − K(0))/t converge to Ψ as t ↓ 0 (the
right derivative exists), then xᵀΨx ≥ 0: at a kernel-null direction
the DERIVATIVE of a PSD family is itself positively signed — the
form difference quotient is nonnegative for every t > 0 and the sign
passes to the limit (`ge_of_tendsto`).  Grade count: K is grade-2
data, but the derivative at the null direction carries grade-1
content with a sign — RATES, not amplitudes.

PROVENANCE (typed): the PRIME.EULER.SCHUR program (round 33,
packages B–D) instantiates exactly this mechanism; this lemma is the
abstract elevator, proven once. -/
theorem tangent_psd_on_kernel_null {K : ℝ → Matrix ι ι ℝ}
    {Ψ : Matrix ι ι ℝ} {x : ι → ℝ}
    (hK : ∀ t : ℝ, 0 ≤ t → (K t).PosSemidef)
    (hnull : formAt (K 0) x = 0)
    (hΨ : ∀ i j, Tendsto (fun t => (K t i j - K 0 i j) / t)
      (𝓝[>] 0) (𝓝 (Ψ i j))) :
    0 ≤ formAt Ψ x := by
  have key : ∀ t : ℝ, (formAt (K t) x - formAt (K 0) x) / t
      = ∑ i, ∑ j, x i * ((K t i j - K 0 i j) / t) * x j := by
    intro t
    rw [formAt_expand (K t) x, formAt_expand (K 0) x,
      ← Finset.sum_sub_distrib, Finset.sum_div]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_sub_distrib, Finset.sum_div]
    refine Finset.sum_congr rfl fun j _ => ?_
    ring
  have hform : Tendsto (fun t => (formAt (K t) x - formAt (K 0) x) / t)
      (𝓝[>] (0 : ℝ)) (𝓝 (formAt Ψ x)) := by
    rw [formAt_expand Ψ x]
    refine Tendsto.congr (fun t => (key t).symm) ?_
    exact tendsto_finset_sum _ fun i _ =>
      tendsto_finset_sum _ fun j _ =>
        ((hΨ i j).const_mul (x i)).mul_const (x j)
  refine ge_of_tendsto hform ?_
  filter_upwards [self_mem_nhdsWithin] with t ht
  have htpos : (0 : ℝ) < t := Set.mem_Ioi.mp ht
  rw [hnull, sub_zero]
  exact div_nonneg (posSemidef_formAt_nonneg (hK t htpos.le) x)
    htpos.le

end GradeNoGo
end TfptCarrier
