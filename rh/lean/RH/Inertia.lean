/-
RH/Inertia.lean -- the matrix-theorem layer (since wave 10 / r305:
PROVED except the Jacobi inertia theorem `crossing_budget`).

Provenance:
  * PSD base theorem: ledger PRIME.PORT.RHP.BORDERED.READOUT.01 [E],
    module verification/v958_bordered_tau_readout_dictionary.py, section S0
    (exact rationals: positive measure => Gram/Hankel PSD => border readout
    T >= 0; bordered [[G,u],[u^T,B]] PSD iff B >= u^T G^{-1} u), and the
    positive-prefix firewall of v959 S0.5 (det H_p = prod h_i Sylvester
    chain, PRIME.PORT.RHP.COUPLEDTAU.TERMINAL.01 [E]).
  * Half-filling law: ledger PRIME.FREEMOMENT.JFRACTION.01 /
    PRIME.PORT.SIGNEDMOMENT.HOLEDUAL.01 (in module
    verification/v956_signedmoment_halffilling_duality.py, rounds r228-r229):
    N_w = ceil(#supp(mutilde)/2); an S-atom signed measure has exactly S
    free moment parameters and the largest Hankel window inside them is
    (S+1)/2.
  * Sylvester pull-back / inertia theorem: v956 round r229
    (INERTIA_THEOREM_EXACT, pontryagin_maxpos_probe.py SPEC_SHA
    b062906cb458da2a).

HONESTY MARKER (updated r305, the wave-10 Lean round; updated C1):
the declared mathlib-based second stage is now largely DONE.  PROVED
in this file:
  * the counting layer (`window_cap_arith`, `moment_counting_free_pivots`,
    `first_forced_pivot` -- waves 2/5),
  * the general matrix layer (`posDef_of_isEmpty`,
    `posDef_of_posSemidef_det_ne_zero`, `posDef_submatrix_of_injective`,
    `posDef_fromBlocks_border`, `posDef_succ_of_posDef_det_pos`,
    `posDef_of_leading_det_pos` = Sylvester's criterion -- wave 10, r305),
  * `psd_base` (PSD of a positive discrete measure),
  * `positive_prefix_firewall` (the Sylvester prefix criterion, both
    directions),
  * `sylvester_pullback` (congruence invariance of PosDef),
  * `half_filling_boundary` (prefix positivity => PosDef at the cap).
C1 UPDATE (the reviewer final-domain block): `crossing_budget` (the
Jacobi inertia theorem T2) is now PROVED -- this file carries ZERO
`sorry`.  The r305 assessment "mathlib carries neither Jacobi's
minor-sign rule nor Sylvester's law of inertia in counting form" is
half stale: mathlib v4.29.1 DOES carry Sylvester's law at the
quadratic-form signature level
(`QuadraticForm.sigNeg_of_equiv_weightedSumSquares`,
Mathlib.LinearAlgebra.QuadraticForm.Signature); the pivot/minor
dictionary (Jacobi's rule as an LDL-type congruence, the Vandermonde
factorization, the matrix-congruence face of the law) is built in the
JacobiInertia section below.  The exact-rational certificate (v962
T2 / r279) stands beside the proof as the measured anchor.

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.LinearAlgebra.QuadraticForm.Basic
import Mathlib.LinearAlgebra.QuadraticForm.Signature
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Data.Matrix.Block
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic.Linarith

namespace RH

open Matrix

/-! ## The general matrix layer (wave 10 / r305, PROVED).

Classical finite-dimensional facts the roadmap statements below consume,
proved against the mathlib `Matrix.PosDef` API.  Everything is over `ℝ`
(the corpus casts exact rationals into `ℝ` for the PosDef API, cf.
RH/Window.lean). -/

/-- the empty matrix is positive definite (base of every Sylvester
induction). -/
theorem posDef_of_isEmpty {n : Type*} [Fintype n] [IsEmpty n]
    (M : Matrix n n ℝ) : M.PosDef := by
  refine Matrix.PosDef.of_dotProduct_mulVec_pos ?_ fun x hx => ?_
  · ext i j
    exact isEmptyElim i
  · exact absurd (funext fun i => isEmptyElim i) hx

/-- a positive semidefinite real matrix with nonvanishing determinant is
positive definite (spectral route: all eigenvalues nonnegative and their
product nonzero). -/
theorem posDef_of_posSemidef_det_ne_zero {n : Type*} [Fintype n]
    [DecidableEq n] {M : Matrix n n ℝ} (hpsd : M.PosSemidef)
    (hdet : M.det ≠ 0) : M.PosDef := by
  rw [hpsd.isHermitian.posDef_iff_eigenvalues_pos]
  intro i
  rcases (hpsd.eigenvalues_nonneg i).lt_or_eq with h | h
  · exact h
  · exact absurd (by
      rw [hpsd.isHermitian.det_eq_prod_eigenvalues]
      exact Finset.prod_eq_zero (Finset.mem_univ i) (by simpa using h.symm))
      hdet

/-- a principal submatrix (along an injective index map) of a positive
definite matrix is positive definite: restrict the quadratic form to the
zero-extension of the test vector. -/
theorem posDef_submatrix_of_injective {l n : Type*} [Fintype l] [Fintype n]
    {M : Matrix n n ℝ} (hM : M.PosDef) {e : l → n}
    (he : Function.Injective e) : (M.submatrix e e).PosDef := by
  classical
  refine Matrix.PosDef.of_dotProduct_mulVec_pos (hM.isHermitian.submatrix e)
    fun x hx => ?_
  set y : n → ℝ := Function.extend e x (0 : n → ℝ) with hy
  have hye : ∀ i, y (e i) = x i := fun i => he.extend_apply x (0 : n → ℝ) i
  have hy0 : ∀ j, (¬ ∃ i, e i = j) → y j = 0 := fun j hj =>
    Function.extend_apply' x (0 : n → ℝ) j hj
  have hyne : y ≠ 0 := by
    obtain ⟨i0, hi0⟩ := Function.ne_iff.mp hx
    intro h0
    exact hi0 (by rw [← hye i0, h0]; rfl)
  have hinner : ∀ j : n, (M *ᵥ y) j = ∑ i : l, M j (e i) * x i := by
    intro j
    show ∑ t : n, M j t * y t = _
    rw [show ∑ t : n, M j t * y t
        = ∑ t ∈ Finset.univ.map ⟨e, he⟩, M j t * y t from
      (Finset.sum_subset (Finset.subset_univ _) fun t _ ht => by
        rw [hy0 t (by simpa [Finset.mem_map] using ht), mul_zero]).symm]
    rw [Finset.sum_map]
    simp only [Function.Embedding.coeFn_mk, hye]
  have key : star y ⬝ᵥ (M *ᵥ y) = star x ⬝ᵥ (M.submatrix e e *ᵥ x) := by
    show ∑ t : n, star (y t) * (M *ᵥ y) t = _
    rw [show ∑ t : n, star (y t) * (M *ᵥ y) t
        = ∑ t ∈ Finset.univ.map ⟨e, he⟩, star (y t) * (M *ᵥ y) t from
      (Finset.sum_subset (Finset.subset_univ _) fun t _ ht => by
        rw [hy0 t (by simpa [Finset.mem_map] using ht)]
        simp).symm]
    rw [Finset.sum_map]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [Function.Embedding.coeFn_mk, hye, hinner]
    rfl
  rw [← key]
  exact hM.dotProduct_mulVec_pos hyne

/-- **the bordered block step**: a symmetric bordered matrix
`[[A, v], [vᵀ, d]]` with positive definite core `A` and positive
determinant is positive definite (Schur complement: the 1x1 Schur block
is `det/det A > 0`, so the bordered matrix is PSD with nonvanishing
determinant). -/
theorem posDef_fromBlocks_border {m : Type*} [Fintype m] [DecidableEq m]
    {A : Matrix m m ℝ} {v : m → ℝ} {d : ℝ} (hA : A.PosDef)
    (hdet : 0 < (Matrix.fromBlocks A (fun i (_ : Unit) => v i)
      (fun (_ : Unit) k => v k) (fun _ _ => d)).det) :
    (Matrix.fromBlocks A (fun i (_ : Unit) => v i)
      (fun (_ : Unit) k => v k) (fun _ _ => d)).PosDef := by
  classical
  haveI : Invertible A :=
    A.invertibleOfIsUnitDet (isUnit_iff_ne_zero.mpr hA.det_pos.ne')
  have hBH : (fun i (_ : Unit) => v i)ᴴ = (fun (_ : Unit) k => v k) := by
    ext ⟨⟩ k
    simp [Matrix.conjTranspose_apply]
  rw [← hBH] at hdet ⊢
  set B : Matrix m Unit ℝ := fun i _ => v i with hB
  set Dm : Matrix Unit Unit ℝ := fun _ _ => d with hDm
  have hdet2 : (Matrix.fromBlocks A B Bᴴ Dm).det
      = A.det * (Dm - Bᴴ * A⁻¹ * B).det := by
    rw [Matrix.det_fromBlocks₁₁, Matrix.invOf_eq_nonsing_inv]
  rw [hdet2] at hdet
  have hschur_pos : 0 < (Dm - Bᴴ * A⁻¹ * B) () () := by
    rcases mul_pos_iff.mp hdet with ⟨_, hs⟩ | ⟨hneg, _⟩
    · rwa [Matrix.det_unique] at hs
    · exact absurd hA.det_pos (not_lt.mpr hneg.le)
  have hschur_psd : (Dm - Bᴴ * A⁻¹ * B).PosSemidef := by
    refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ fun y => ?_
    · ext ⟨⟩ ⟨⟩
      simp [Matrix.conjTranspose_apply]
    · have hform : star y ⬝ᵥ ((Dm - Bᴴ * A⁻¹ * B) *ᵥ y)
          = (Dm - Bᴴ * A⁻¹ * B) () () * (y () * y ()) := by
        simp [dotProduct, Matrix.mulVec]
        ring
      rw [hform]
      exact mul_nonneg hschur_pos.le (mul_self_nonneg _)
  have hpsd : (Matrix.fromBlocks A B Bᴴ Dm).PosSemidef :=
    (Matrix.PosDef.fromBlocks₁₁ B Dm hA).mpr hschur_psd
  refine posDef_of_posSemidef_det_ne_zero hpsd ?_
  rw [hdet2]
  exact (mul_pos hA.det_pos (by rwa [Matrix.det_unique])).ne'

/-- **the Sylvester bordering step**: a symmetric `(q+1) x (q+1)` real
matrix whose leading `q x q` block is positive definite and whose
determinant is positive is positive definite. -/
theorem posDef_succ_of_posDef_det_pos {q : ℕ}
    {M : Matrix (Fin (q + 1)) (Fin (q + 1)) ℝ} (hherm : M.IsHermitian)
    (hblock : (M.submatrix Fin.castSucc Fin.castSucc).PosDef)
    (hdet : 0 < M.det) : M.PosDef := by
  classical
  have hsym : ∀ i j, M i j = M j i := fun i j => by
    have := congrFun (congrFun hherm i) j
    simpa [Matrix.conjTranspose_apply] using this.symm
  set f : Fin q ⊕ Unit → Fin (q + 1) :=
    Sum.elim Fin.castSucc (fun _ => Fin.last q) with hf
  have hfinj : Function.Injective f := by
    rintro (a | ⟨⟩) (b | ⟨⟩) hab
    · simp only [hf, Sum.elim_inl] at hab
      exact congrArg Sum.inl (Fin.castSucc_injective q hab)
    · exfalso
      simp only [hf, Sum.elim_inl, Sum.elim_inr] at hab
      have := congrArg Fin.val hab
      simp only [Fin.val_castSucc, Fin.val_last] at this
      exact absurd this (Nat.ne_of_lt a.isLt)
    · exfalso
      simp only [hf, Sum.elim_inl, Sum.elim_inr] at hab
      have := congrArg Fin.val hab
      simp only [Fin.val_castSucc, Fin.val_last] at this
      exact absurd this.symm (Nat.ne_of_lt b.isLt)
    · rfl
  have hfbij : Function.Bijective f :=
    (Fintype.bijective_iff_injective_and_card f).mpr ⟨hfinj, by simp⟩
  set e : (Fin q ⊕ Unit) ≃ Fin (q + 1) := Equiv.ofBijective f hfbij with he
  have hEq : M.submatrix e e = Matrix.fromBlocks
      (M.submatrix Fin.castSucc Fin.castSucc)
      (fun i (_ : Unit) => M (Fin.castSucc i) (Fin.last q))
      (fun (_ : Unit) k => M (Fin.castSucc k) (Fin.last q))
      (fun _ _ => M (Fin.last q) (Fin.last q)) := by
    ext (i | ⟨⟩) (k | ⟨⟩)
    · rfl
    · rfl
    · exact hsym (Fin.last q) (Fin.castSucc k)
    · rfl
  have hdet' : 0 < (M.submatrix e e).det := by
    rwa [Matrix.det_submatrix_equiv_self]
  rw [hEq] at hdet'
  have hborder := posDef_fromBlocks_border hblock hdet'
  have hsub : (M.submatrix e e).PosDef := by
    rw [hEq]
    exact hborder
  have hM : M = (M.submatrix e e).submatrix e.symm e.symm := by
    rw [Matrix.submatrix_submatrix, Equiv.self_comp_symm,
      Matrix.submatrix_id_id]
  rw [hM]
  exact posDef_submatrix_of_injective hsub e.symm.injective

/-- **Sylvester's criterion** (the classical reverse direction): a
symmetric real matrix all of whose leading principal minors are positive
is positive definite.  Induction on the leading block via
`posDef_succ_of_posDef_det_pos`. -/
theorem posDef_of_leading_det_pos {p : ℕ} {M : Matrix (Fin p) (Fin p) ℝ}
    (hherm : M.IsHermitian)
    (hminors : ∀ q (hq : q ≤ p),
      0 < (M.submatrix (Fin.castLE hq) (Fin.castLE hq)).det) :
    M.PosDef := by
  have main : ∀ q (hq : q ≤ p),
      (M.submatrix (Fin.castLE hq) (Fin.castLE hq)).PosDef := by
    intro q
    induction q with
    | zero => exact fun _ => posDef_of_isEmpty _
    | succ r ih =>
        intro hq
        have hr : r ≤ p := le_trans (Nat.le_succ r) hq
        refine posDef_succ_of_posDef_det_pos (hherm.submatrix _) ?_
          (hminors (r + 1) hq)
        have hcomp : (Fin.castLE hq) ∘ (Fin.castSucc : Fin r → Fin (r + 1))
            = Fin.castLE hr := funext fun i => Fin.ext rfl
        rw [Matrix.submatrix_submatrix, hcomp]
        exact ih hr
  have hp := main p le_rfl
  have hid : (Fin.castLE (le_refl p)) = (id : Fin p → Fin p) :=
    funext fun i => Fin.ext rfl
  rwa [hid, Matrix.submatrix_id_id] at hp

/-- A discrete signed measure: `S` atoms `x_j` with signed weights `w_j`.
(The corpus object is the von-Mangoldt double zone mutilde = mu - nu.) -/
structure SignedAtoms (S : ℕ) where
  x : Fin S → ℝ
  w : Fin S → ℝ

namespace SignedAtoms

variable {S : ℕ} (m : SignedAtoms S)

/-- The `p x p` moment (Hankel) matrix `H_p(i,k) = sum_j w_j x_j^(i+k)`. -/
def hankel (p : ℕ) : Matrix (Fin p) (Fin p) ℝ :=
  fun i k => ∑ j, m.w j * m.x j ^ ((i : ℕ) + (k : ℕ))

/-- The Hankel matrices are symmetric (hence Hermitian over ℝ). -/
theorem hankel_isHermitian (p : ℕ) : (m.hankel p).IsHermitian := by
  ext i k
  simp [hankel, Nat.add_comm (i : ℕ) (k : ℕ)]

end SignedAtoms

/-- **PSD base theorem** (v958 S0, [E] at the exact-rational level).
For a POSITIVE measure (all weights nonnegative) every moment matrix is
positive semidefinite, hence every border readout `T = t^T H t >= 0`.
The must-fail of v958 S0: a genuinely signed measure breaks this -- the
wall content is precisely the quasi-definiteness of the signed defect
measure.

PROVED (wave 10 / r305): the standard argument
`T = integral of (sum t_i x^i)^2 dmu >= 0`, i.e. the quadratic form is
the mu-integral of a square. -/
theorem psd_base {S p : ℕ} (m : SignedAtoms S) (hw : ∀ j, 0 ≤ m.w j) :
    (m.hankel p).PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg (m.hankel_isHermitian p)
    fun x => ?_
  have key : star x ⬝ᵥ (m.hankel p *ᵥ x)
      = ∑ j, m.w j * (∑ i : Fin p, x i * m.x j ^ (i : ℕ)) ^ 2 := by
    calc star x ⬝ᵥ (m.hankel p *ᵥ x)
        = ∑ i : Fin p, ∑ k : Fin p, x i * x k
            * ∑ j, m.w j * m.x j ^ ((i : ℕ) + (k : ℕ)) := by
          simp only [dotProduct, Matrix.mulVec, SignedAtoms.hankel,
            Pi.star_apply, star_trivial]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun k _ => ?_
          ring
      _ = ∑ i : Fin p, ∑ k : Fin p, ∑ j, x i * x k
            * (m.w j * m.x j ^ ((i : ℕ) + (k : ℕ))) := by
          refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl
            fun k _ => ?_
          rw [Finset.mul_sum]
      _ = ∑ i : Fin p, ∑ j, ∑ k : Fin p, x i * x k
            * (m.w j * m.x j ^ ((i : ℕ) + (k : ℕ))) :=
          Finset.sum_congr rfl fun i _ => Finset.sum_comm
      _ = ∑ j, ∑ i : Fin p, ∑ k : Fin p, x i * x k
            * (m.w j * m.x j ^ ((i : ℕ) + (k : ℕ))) :=
          Finset.sum_comm
      _ = ∑ j, m.w j * (∑ i : Fin p, x i * m.x j ^ (i : ℕ)) ^ 2 := by
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [sq, Finset.sum_mul_sum, Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun k _ => ?_
          rw [pow_add]
          ring
  rw [key]
  exact Finset.sum_nonneg fun j _ => mul_nonneg (hw j) (sq_nonneg _)

/-- **Positive-prefix firewall** (v959 S0.5, [E] at the exact-rational
level).  The prefix moment kernel `H_p` is positive definite iff the whole
h-prefix `h_0 .. h_{p-1}` is positive, via the exact Sylvester chain
`det H_p = prod_{i<p} h_i`.  Here the h-chain is DEFINED as the ratio of
consecutive leading principal minors (the corpus norm-square chain).

PROVED (wave 10 / r305).  Forward: every leading block is a principal
submatrix of the PosDef `H_p` (via `Fin.castLE`), so every leading minor
is positive and each `h i` is a ratio of positive prefix products.
Reverse: Sylvester's criterion (`posDef_of_leading_det_pos` above), the
minors being the positive products `prod_{i<q} h_i`.  (Certified with
exact Sylvester chains and a firing signed must-fail in v959 S0.5;
firewall table: MAIN pmax = N, controls pmax = 21/25/27.) -/
theorem positive_prefix_firewall {S p : ℕ} (m : SignedAtoms S)
    (h : ℕ → ℝ)
    (hminor : ∀ q ≤ p,
      ((m.hankel q).det = ∏ i ∈ Finset.range q, h i)) :
    (m.hankel p).PosDef ↔ ∀ i < p, 0 < h i := by
  have hsub : ∀ q (hq : q ≤ p),
      (m.hankel p).submatrix (Fin.castLE hq) (Fin.castLE hq)
        = m.hankel q := fun q hq => rfl
  constructor
  · intro hpd i hip
    have hdetq : ∀ q (hq : q ≤ p), 0 < ∏ k ∈ Finset.range q, h k := by
      intro q hq
      rw [← hminor q hq, ← hsub q hq]
      exact (posDef_submatrix_of_injective hpd (Fin.castLE_injective hq)).det_pos
    have h1 := hdetq i (le_of_lt hip)
    have h2 := hdetq (i + 1) hip
    rw [Finset.prod_range_succ] at h2
    by_contra hle
    have hle' : h i ≤ 0 := not_lt.mp hle
    have : (∏ k ∈ Finset.range i, h k) * h i ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos h1.le hle'
    linarith
  · intro hpos
    refine posDef_of_leading_det_pos (m.hankel_isHermitian p) fun q hq => ?_
    rw [hsub q hq, hminor q hq]
    exact Finset.prod_pos fun i hi =>
      hpos i (lt_of_lt_of_le (Finset.mem_range.mp hi) hq)

/-- **Sylvester pull-back / inertia invariance** (v956 r229,
INERTIA_THEOREM_EXACT).  A congruence `A^T M A` with invertible `A`
preserves positive definiteness (and, in the full statement, the whole
inertia triple -- stated here in the PosDef form the lane consumes).

PROVED (wave 10 / r305): mathlib's
`Matrix.PosDef.conjTranspose_mul_mul_same` with `Aᴴ = Aᵀ` over `ℝ` and
mulVec-injectivity of the invertible congruence matrix. -/
theorem sylvester_pullback {n : ℕ} (A M : Matrix (Fin n) (Fin n) ℝ)
    (hA : IsUnit A.det) (hM : M.PosDef) :
    (Aᵀ * M * A).PosDef := by
  have hinj : Function.Injective A.mulVec :=
    A.mulVec_injective_iff_isUnit.mpr ((Matrix.isUnit_iff_isUnit_det A).mpr hA)
  have hpd := hM.conjTranspose_mul_mul_same hinj
  rwa [Matrix.conjTranspose_eq_transpose_of_trivial] at hpd

/-- **Half-filling window cap, counting part** (v956 r229, PROVED).
`H_n` consumes the moments `m_0 .. m_{2n-2}`, i.e. `2n - 1` moments; an
`S`-atom signed measure has exactly `S` free moment parameters; hence the
largest Hankel window inside the free moments is `N_w = (S+1)/2 = ceil(S/2)`:
`2n - 1 <= S` iff `n <= (S+1)/2` (natural-number arithmetic). -/
theorem window_cap_arith (S n : ℕ) (hn : 0 < n) :
    2 * n - 1 ≤ S ↔ n ≤ (S + 1) / 2 := by
  omega

/-- **T1, the moment counting theorem -- counting core** (v962 / r281,
PROVED).  The pivot `h_n` consumes the moments `m_0 .. m_{2n}`; an
`S`-atom signed measure has exactly `S` free moments `m_0 .. m_{S-1}`
(Vandermonde bijection; every later moment is forced by the node
polynomial); hence `h_n` is a FREE pivot iff `2n <= S - 1` iff
`n < N_w = (S+1)/2`: the free pivots are EXACTLY `h_0 .. h_{N_w - 1}` --
half-filling is the end of the free moment space.  "Why half-filling"
is answered by counting; the exact-rational freedom demonstration
(`dm = e_{S-1}` moves `h_{N_w-1}` alone) and the forcing recurrence live
in v962 S0 (ledger `PRIME.WALL.HALFFILLING_PINNING_THEORY.01` [E]). -/
theorem moment_counting_free_pivots (S n : ℕ) (hS : 1 ≤ S) :
    2 * n ≤ S - 1 ↔ n < (S + 1) / 2 := by
  omega

/-- **T1 complement** (v962 / r281, PROVED): `h_{N_w}` is the FIRST
FORCED pivot -- it consumes `m_{2 N_w}` with `2 N_w >= S`, beyond the
free moment window. -/
theorem first_forced_pivot (S : ℕ) (hS : 1 ≤ S) :
    ¬ 2 * ((S + 1) / 2) ≤ S - 1 := by
  omega

/-! ## The Jacobi/Sylvester inertia layer (C1: `crossing_budget` PROVED)

The r305 adjudication kept `crossing_budget` open because mathlib
v4.29.1 was assessed as carrying neither Jacobi's minor-sign rule nor
Sylvester's law of inertia in counting form.  The C1 re-audit found
the second half of that assessment STALE: mathlib's
`Mathlib.LinearAlgebra.QuadraticForm.Signature` proves the uniqueness
part of **Sylvester's law of inertia**
(`QuadraticForm.sigNeg_of_equiv_weightedSumSquares`: for any
weighted-sum-of-squares diagonalization of a real quadratic form, the
number of negative weights is the invariant `sigNeg`).  What remained
to build here is the pivot/minor dictionary:
  * `toQuadraticMap'_apply_real` / `toQuadraticMap'_diagonal` -- the
    matrix quadratic form and its diagonal case as a weighted sum of
    squares (bookkeeping);
  * `equivalent_toQuadraticMap'_congruence` -- matrix congruence
    `Pᵀ M P` with `IsUnit P.det` gives equivalent quadratic forms
    (the matrix face of Sylvester's law);
  * `hankel_eq_vand_conj` -- the Vandermonde factorization
    `H_S = Vᵀ (diag w) V` (definitional sum algebra: NO Vandermonde
    determinant formula is consumed -- invertibility of `V` falls out
    of `det H_S ≠ 0`);
  * `exists_congruent_diagonal` -- **Jacobi's rule as an LDL-type
    congruence**: a symmetric real matrix whose leading principal
    minors realize the pivot products `∏ h i` with all pivots nonzero
    is congruent to `diagonal h` (induction on the dimension; the
    step is the Schur-complement block elimination
    `Tᵀ [[A, B], [Bᵀ, d]] T = [[A, 0], [0, d − BᵀA⁻¹B]]` with the
    unit-triangular `T = [[1, −A⁻¹B], [0, 1]]`, and the 1×1 Schur
    block is pinned to `h p` by the minor hypothesis).
`crossing_budget` then reads: `#(h < 0) = sigNeg = #(w < 0)`. -/

section JacobiInertia

open QuadraticMap

/-- the matrix quadratic form evaluates as `x ⬝ᵥ (M *ᵥ x)`
(bookkeeping for `Matrix.toQuadraticMap'`). -/
theorem toQuadraticMap'_apply_real {k : ℕ} (M : Matrix (Fin k) (Fin k) ℝ)
    (x : Fin k → ℝ) : M.toQuadraticMap' x = x ⬝ᵥ (M *ᵥ x) :=
  Matrix.toLinearMap₂'_apply' M x x

/-- the diagonal matrix quadratic form IS the weighted sum of squares
(the shape mathlib's inertia law counts). -/
theorem toQuadraticMap'_diagonal {k : ℕ} (d : Fin k → ℝ) :
    (Matrix.diagonal d).toQuadraticMap'
      = QuadraticMap.weightedSumSquares ℝ d := by
  ext x
  rw [toQuadraticMap'_apply_real, QuadraticMap.weightedSumSquares_apply]
  simp only [dotProduct, Matrix.mulVec_diagonal, smul_eq_mul]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- **matrix congruence gives equivalent quadratic forms** (the matrix
face of Sylvester's law): for invertible `P` the forms of `Pᵀ M P` and
`M` are isometrically equivalent via `x ↦ P *ᵥ x`. -/
theorem equivalent_toQuadraticMap'_congruence {k : ℕ}
    (M P : Matrix (Fin k) (Fin k) ℝ) (hP : IsUnit P.det) :
    QuadraticMap.Equivalent (Pᵀ * M * P).toQuadraticMap'
      M.toQuadraticMap' := by
  haveI hPinv : Invertible P := P.invertibleOfIsUnitDet hP
  refine ⟨{ P.toLinearEquiv' hPinv with map_app' := fun x => ?_ }⟩
  show M.toQuadraticMap' (Matrix.toLin' P x) = _
  rw [Matrix.toLin'_apply, toQuadraticMap'_apply_real,
    toQuadraticMap'_apply_real]
  rw [show (Pᵀ * M * P) *ᵥ x = Pᵀ *ᵥ (M *ᵥ (P *ᵥ x)) by
    rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, Matrix.mul_assoc]]
  conv_rhs => rw [Matrix.dotProduct_mulVec, Matrix.vecMul_transpose]

/-- the Vandermonde sampling matrix of a signed atom set: row `j`
(atom), column `i` (power `x_j^i`). -/
def SignedAtoms.vand {S : ℕ} (m : SignedAtoms S) :
    Matrix (Fin S) (Fin S) ℝ :=
  fun j i => m.x j ^ (i : ℕ)

/-- **the Vandermonde factorization** `H_S = Vᵀ (diag w) V` --
definitional sum algebra (`pow_add` regrouping), no determinant
formula consumed. -/
theorem SignedAtoms.hankel_eq_vand_conj {S : ℕ} (m : SignedAtoms S) :
    m.hankel S = m.vandᵀ * Matrix.diagonal m.w * m.vand := by
  ext i k
  rw [Matrix.mul_apply]
  simp only [Matrix.mul_diagonal, Matrix.transpose_apply,
    SignedAtoms.vand, SignedAtoms.hankel]
  exact Finset.sum_congr rfl fun j _ => by rw [pow_add]; ring

/-- **Jacobi's rule as an LDL-type congruence** (C1): a symmetric real
`p × p` matrix whose leading principal minors are the exact pivot
products `det M_q = ∏_{i<q} h i` with every pivot `h i ≠ 0` is
congruent (`Pᵀ M P`, `P` invertible) to the pivot diagonal.  Induction
on `p` via the Schur-complement block elimination; the corner Schur
block is pinned to `h p` by the minor hypothesis. -/
theorem exists_congruent_diagonal (p : ℕ) :
    ∀ (M : Matrix (Fin p) (Fin p) ℝ), M.IsHermitian →
      ∀ h : ℕ → ℝ,
      (∀ q (hq : q ≤ p), (M.submatrix (Fin.castLE hq) (Fin.castLE hq)).det
          = ∏ i ∈ Finset.range q, h i) →
      (∀ i < p, h i ≠ 0) →
      ∃ P : Matrix (Fin p) (Fin p) ℝ, IsUnit P.det ∧
        Pᵀ * M * P = Matrix.diagonal fun i : Fin p => h (i : ℕ) := by
  induction p with
  | zero =>
      intro M _ h _ _
      exact ⟨1, by simp, by ext i j; exact isEmptyElim i⟩
  | succ p ih =>
      intro M hherm h hminor hnz
      have hsym : ∀ i j, M i j = M j i := fun i j => by
        have := congrFun (congrFun hherm i) j
        simpa [Matrix.conjTranspose_apply] using this.symm
      -- the leading block and its data
      set A : Matrix (Fin p) (Fin p) ℝ :=
        M.submatrix Fin.castSucc Fin.castSucc with hAdef
      have hAherm : A.IsHermitian := hherm.submatrix _
      have hAsymm : Aᵀ = A := by
        have := hAherm
        rwa [Matrix.IsHermitian,
          Matrix.conjTranspose_eq_transpose_of_trivial] at this
      have hAminor : ∀ q (hq : q ≤ p),
          (A.submatrix (Fin.castLE hq) (Fin.castLE hq)).det
            = ∏ i ∈ Finset.range q, h i := by
        intro q hq
        have hcomp : (Fin.castSucc : Fin p → Fin (p + 1)) ∘ Fin.castLE hq
            = Fin.castLE (le_trans hq (Nat.le_succ p)) :=
          funext fun i => Fin.ext rfl
        rw [hAdef, Matrix.submatrix_submatrix, hcomp]
        exact hminor q (le_trans hq (Nat.le_succ p))
      have hAdet : A.det = ∏ i ∈ Finset.range p, h i := by
        have hp := hAminor p le_rfl
        have hid : (Fin.castLE (le_refl p)) = (id : Fin p → Fin p) :=
          funext fun i => Fin.ext rfl
        rwa [hid, Matrix.submatrix_id_id] at hp
      have hAdet_ne : A.det ≠ 0 := by
        rw [hAdet]
        exact Finset.prod_ne_zero_iff.mpr fun i hi =>
          hnz i (Nat.lt_succ_of_lt (Finset.mem_range.mp hi))
      have hAunit : IsUnit A.det := isUnit_iff_ne_zero.mpr hAdet_ne
      have hAAinv : A * A⁻¹ = 1 := Matrix.mul_nonsing_inv A hAunit
      have hAinvA : A⁻¹ * A = 1 := Matrix.nonsing_inv_mul A hAunit
      have hAinvT : (A⁻¹)ᵀ = A⁻¹ := by
        rw [Matrix.transpose_nonsing_inv, hAsymm]
      have hMdet : M.det = (∏ i ∈ Finset.range p, h i) * h p := by
        have hp := hminor (p + 1) le_rfl
        have hid : (Fin.castLE (le_refl (p + 1)))
            = (id : Fin (p + 1) → Fin (p + 1)) := funext fun i => Fin.ext rfl
        rw [hid, Matrix.submatrix_id_id] at hp
        rw [hp, Finset.prod_range_succ]
      -- the sum-type picture (the wave-10 reindexing pattern)
      set f : Fin p ⊕ Unit → Fin (p + 1) :=
        Sum.elim Fin.castSucc (fun _ => Fin.last p) with hf
      have hfinj : Function.Injective f := by
        rintro (a | ⟨⟩) (b | ⟨⟩) hab
        · simp only [hf, Sum.elim_inl] at hab
          exact congrArg Sum.inl (Fin.castSucc_injective p hab)
        · exfalso
          simp only [hf, Sum.elim_inl, Sum.elim_inr] at hab
          have := congrArg Fin.val hab
          simp only [Fin.val_castSucc, Fin.val_last] at this
          exact absurd this (Nat.ne_of_lt a.isLt)
        · exfalso
          simp only [hf, Sum.elim_inl, Sum.elim_inr] at hab
          have := congrArg Fin.val hab
          simp only [Fin.val_castSucc, Fin.val_last] at this
          exact absurd this.symm (Nat.ne_of_lt b.isLt)
        · rfl
      have hfbij : Function.Bijective f :=
        (Fintype.bijective_iff_injective_and_card f).mpr ⟨hfinj, by simp⟩
      set e : (Fin p ⊕ Unit) ≃ Fin (p + 1) := Equiv.ofBijective f hfbij
        with he
      set B : Matrix (Fin p) Unit ℝ :=
        fun i _ => M (Fin.castSucc i) (Fin.last p) with hBdef
      set dc : Matrix Unit Unit ℝ :=
        fun _ _ => M (Fin.last p) (Fin.last p) with hdcdef
      have hEq : M.submatrix e e = Matrix.fromBlocks A B Bᵀ dc := by
        ext (i | ⟨⟩) (k | ⟨⟩)
        · rfl
        · rfl
        · exact hsym (Fin.last p) (Fin.castSucc k)
        · rfl
      -- step 1: Schur block elimination by the unit-triangular T
      set T : Matrix (Fin p ⊕ Unit) (Fin p ⊕ Unit) ℝ :=
        Matrix.fromBlocks 1 (-(A⁻¹ * B)) 0 1 with hTdef
      set s : Matrix Unit Unit ℝ := dc - Bᵀ * (A⁻¹ * B) with hsdef
      have hTdet : T.det = 1 := by
        rw [hTdef, Matrix.det_fromBlocks_zero₂₁]
        simp
      have hstep1 : Tᵀ * (M.submatrix e e) * T
          = Matrix.fromBlocks A 0 0 s := by
        have hXT : Matrix.fromBlocks A B Bᵀ dc * T
            = Matrix.fromBlocks A 0 Bᵀ s := by
          rw [hTdef, Matrix.fromBlocks_multiply]
          congr 1
          · rw [Matrix.mul_one, Matrix.mul_zero, add_zero]
          · rw [Matrix.mul_neg, ← Matrix.mul_assoc, hAAinv,
              Matrix.one_mul, Matrix.mul_one, neg_add_cancel]
          · rw [Matrix.mul_one, Matrix.mul_zero, add_zero]
          · rw [hsdef, Matrix.mul_neg, Matrix.mul_one, neg_add_eq_sub]
        rw [hEq, Matrix.mul_assoc, hXT, hTdef, Matrix.fromBlocks_transpose]
        simp only [Matrix.transpose_one, Matrix.transpose_zero]
        rw [Matrix.fromBlocks_multiply]
        congr 1
        · simp
        · simp
        · rw [Matrix.transpose_neg, Matrix.transpose_mul, hAinvT,
            Matrix.neg_mul, Matrix.mul_assoc, hAinvA, Matrix.mul_one,
            Matrix.one_mul, neg_add_cancel]
        · simp
      -- the corner Schur block is pinned to `h p` by the minors
      have hsval : s = Matrix.diagonal (fun _ : Unit => h p) := by
        have hdet1 : (Matrix.fromBlocks A (0 : Matrix (Fin p) Unit ℝ)
            (0 : Matrix Unit (Fin p) ℝ) s).det = A.det * s.det :=
          Matrix.det_fromBlocks_zero₂₁ _ _ _
        have hdet2 : (Tᵀ * (M.submatrix e e) * T).det = M.det := by
          rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose, hTdet,
            Matrix.det_submatrix_equiv_self]
          ring
        have hsdet : A.det * s.det = A.det * h p := by
          rw [← hdet1, ← hstep1, hdet2, hMdet, hAdet]
        have hs : s.det = h p := mul_left_cancel₀ hAdet_ne hsdet
        have hsval' : s () () = h p := by
          rw [← hs, Matrix.det_unique]
        ext ⟨⟩ ⟨⟩
        rw [hsval', Matrix.diagonal_apply_eq]
      -- step 2: diagonalize the leading block by the induction hypothesis
      obtain ⟨P₀, hP₀unit, hP₀⟩ := ih A hAherm h hAminor
        (fun i hi => hnz i (Nat.lt_succ_of_lt hi))
      set U : Matrix (Fin p ⊕ Unit) (Fin p ⊕ Unit) ℝ :=
        Matrix.fromBlocks P₀ 0 0 1 with hUdef
      have hUdet : U.det = P₀.det := by
        rw [hUdef, Matrix.det_fromBlocks_zero₂₁]
        simp
      have hstep2 : Uᵀ * Matrix.fromBlocks A 0 0 s * U
          = Matrix.diagonal (Sum.elim (fun i : Fin p => h (i : ℕ))
              (fun _ : Unit => h p)) := by
        have hXU : Matrix.fromBlocks A 0 0 s * U
            = Matrix.fromBlocks (A * P₀) 0 0 s := by
          rw [hUdef, Matrix.fromBlocks_multiply]
          congr 1
          · simp
          · simp
          · simp
          · simp
        rw [Matrix.mul_assoc, hXU, hUdef, Matrix.fromBlocks_transpose]
        simp only [Matrix.transpose_one, Matrix.transpose_zero]
        rw [Matrix.fromBlocks_multiply, ← Matrix.fromBlocks_diagonal]
        congr 1
        · rw [Matrix.zero_mul, add_zero, ← Matrix.mul_assoc, hP₀]
        · simp
        · simp
        · rw [Matrix.zero_mul, Matrix.one_mul, zero_add, hsval]
      -- the combined congruence on the sum type
      set W : Matrix (Fin p ⊕ Unit) (Fin p ⊕ Unit) ℝ := T * U with hWdef
      have hWunit : IsUnit W.det := by
        rw [hWdef, Matrix.det_mul, hTdet, one_mul, hUdet]
        exact hP₀unit
      have hWcongr : Wᵀ * (M.submatrix e e) * W
          = Matrix.diagonal (Sum.elim (fun i : Fin p => h (i : ℕ))
              (fun _ : Unit => h p)) := by
        calc Wᵀ * (M.submatrix e e) * W
            = Uᵀ * (Tᵀ * (M.submatrix e e) * T) * U := by
              rw [hWdef, Matrix.transpose_mul]
              simp only [Matrix.mul_assoc]
          _ = Uᵀ * Matrix.fromBlocks A 0 0 s * U := by rw [hstep1]
          _ = _ := hstep2
      -- transport along `e` back to `Fin (p + 1)`
      refine ⟨W.submatrix e.symm e.symm, ?_, ?_⟩
      · rwa [Matrix.det_submatrix_equiv_self e.symm]
      · have hMeq : M = (M.submatrix e e).submatrix e.symm e.symm := by
          rw [Matrix.submatrix_submatrix, Equiv.self_comp_symm,
            Matrix.submatrix_id_id]
        calc (W.submatrix e.symm e.symm)ᵀ * M * W.submatrix e.symm e.symm
            = (Wᵀ * (M.submatrix e e) * W).submatrix e.symm e.symm := by
              rw [Matrix.transpose_submatrix]
              conv_lhs => rw [hMeq]
              rw [Matrix.submatrix_mul_equiv, Matrix.submatrix_mul_equiv]
          _ = Matrix.diagonal fun i : Fin (p + 1) => h (i : ℕ) := by
              rw [hWcongr, Matrix.submatrix_diagonal_equiv]
              congr 1
              funext i
              rcases hcase : e.symm i with j | ⟨⟩
              · have hi : i = e (Sum.inl j) := by
                  rw [← hcase, Equiv.apply_symm_apply]
                have hval : (j : ℕ) = (i : ℕ) := by rw [hi]; rfl
                simp only [Function.comp_apply, hcase, Sum.elim_inl, hval]
              · have hi : i = e (Sum.inr ()) := by
                  rw [← hcase, Equiv.apply_symm_apply]
                have hval : p = (i : ℕ) := by rw [hi]; rfl
                simp only [Function.comp_apply, hcase, Sum.elim_inr, hval]

/-- **T2, the crossing budget theorem -- PROVED** (C1; v962 / r279:
Jacobi's minor-sign rule + the Sylvester congruence
`H_S = Vᵀ (diag w) V ~ diag w`).  For a nondegenerate `S`-atom signed
measure whose Sylvester chain `h` has no vanishing entry below `S`,
the number of negative pivots over the full algebraic continuation
equals the number of negative atoms: the Maslov crossing budget is
world-blindly fixed by the source -- the entire arithmetic of the
wall is WHERE this fixed budget is spent (`free_window_positivity`,
RH/Canonical.lean since C1).

PROOF (C1; formerly the ONE remaining sorry of this file -- the r305
"mathlib carries neither" assessment is corrected in the section
header): both `diagonal (h ∘ val)` (via `exists_congruent_diagonal`,
the Jacobi/LDL side) and `diagonal w` (via `hankel_eq_vand_conj`, the
Vandermonde side -- `V` invertible because `det H_S = ∏ h i ≠ 0`) are
congruent to `H_S`, so both negative counts equal the inertia
invariant `sigNeg` of the moment quadratic form (mathlib's Sylvester
law, `QuadraticForm.sigNeg_of_equiv_weightedSumSquares`).  Certified
exactly (rationals, five frozen signed measures; real-side w9 104 /
w13 98 / controls 141/94/6 / kz15 121 / kz52 551) in v962 T2 / round
279 (oriented_theorem_probe.py, SPEC_SHA 9107709b4f4a65d1); ledger
`PRIME.WALL.HALFFILLING_PINNING_THEORY.01` [E]. -/
theorem crossing_budget {S : ℕ} (m : SignedAtoms S) (h : ℕ → ℝ)
    (hminor : ∀ q ≤ S,
      ((m.hankel q).det = ∏ i ∈ Finset.range q, h i))
    (hnz : ∀ i < S, h i ≠ 0) :
    (Finset.univ.filter fun n : Fin S => h n < 0).card
      = (Finset.univ.filter fun j : Fin S => m.w j < 0).card := by
  classical
  -- the minor hypothesis in submatrix form (the leading blocks of
  -- `H_S` ARE the smaller Hankel matrices, definitionally)
  have hminor' : ∀ q (hq : q ≤ S),
      ((m.hankel S).submatrix (Fin.castLE hq) (Fin.castLE hq)).det
        = ∏ i ∈ Finset.range q, h i := fun q hq => hminor q hq
  have hdetM_ne : (m.hankel S).det ≠ 0 := by
    rw [hminor S le_rfl]
    exact Finset.prod_ne_zero_iff.mpr fun i hi =>
      hnz i (Finset.mem_range.mp hi)
  -- the Jacobi/LDL side: `H_S ~ diagonal (h ∘ val)`
  obtain ⟨P, hPunit, hPdiag⟩ := exists_congruent_diagonal S (m.hankel S)
    (m.hankel_isHermitian S) h hminor' hnz
  -- the Vandermonde side: `H_S ~ diagonal w`
  have hfact := m.hankel_eq_vand_conj
  have hVunit : IsUnit m.vand.det := by
    refine isUnit_iff_ne_zero.mpr fun hV0 => hdetM_ne ?_
    rw [hfact, Matrix.det_mul, hV0, mul_zero]
  -- both diagonals are equivalent to the moment quadratic form
  have hE1 : QuadraticMap.Equivalent (m.hankel S).toQuadraticMap'
      (QuadraticMap.weightedSumSquares ℝ fun i : Fin S => h (i : ℕ)) := by
    have hc := equivalent_toQuadraticMap'_congruence (m.hankel S) P hPunit
    rw [hPdiag, toQuadraticMap'_diagonal] at hc
    exact hc.symm
  have hE2 : QuadraticMap.Equivalent (m.hankel S).toQuadraticMap'
      (QuadraticMap.weightedSumSquares ℝ m.w) := by
    have hc := equivalent_toQuadraticMap'_congruence
      (Matrix.diagonal m.w) m.vand hVunit
    rw [← hfact, toQuadraticMap'_diagonal] at hc
    exact hc
  -- Sylvester's law of inertia (mathlib): both counts are `sigNeg`
  have h1 := QuadraticForm.sigNeg_of_equiv_weightedSumSquares hE1
  have h2 := QuadraticForm.sigNeg_of_equiv_weightedSumSquares hE2
  have hconv : ∀ f : Fin S → ℝ, {i : Fin S | f i < 0}.ncard
      = (Finset.univ.filter fun i : Fin S => f i < 0).card := by
    intro f
    rw [Set.ncard_eq_toFinset_card', Set.toFinset_setOf]
  calc (Finset.univ.filter fun n : Fin S => h n < 0).card
      = {i : Fin S | h (i : ℕ) < 0}.ncard := (hconv _).symm
    _ = sigNeg (m.hankel S).toQuadraticMap' := h1.symm
    _ = {j : Fin S | m.w j < 0}.ncard := h2
    _ = (Finset.univ.filter fun j : Fin S => m.w j < 0).card := hconv _

end JacobiInertia

/-- **Half-filling boundary** (v956 r228/r229, [E] measured on all five
windows: N_w/#supp = 0.5004..0.5017 with first r-flip at N_w + O(1)).
The substantive statement: on the MAIN windows the signed defect measure is
quasi-definite exactly up to half-filling of the union support and no
degree further -- the wall is maximal.

PROVED (wave 10 / r305): given the wall hypothesis `hwall` (the
h-prefix positive through half-filling -- the arithmetic content, which
stays an INPUT here), the conclusion is the reverse Sylvester direction
of `positive_prefix_firewall` at `p = (S+1)/2 <= S`.  The counting half
is `window_cap_arith`; the quasi-definiteness boundary itself (that
`hwall` HOLDS on the main windows) remains measured arithmetic content,
carried by L* (RH/Window.lean). -/
theorem half_filling_boundary {S : ℕ} (m : SignedAtoms S)
    (h : ℕ → ℝ)
    (hminor : ∀ q ≤ S, ((m.hankel q).det = ∏ i ∈ Finset.range q, h i))
    (hwall : ∀ i < (S + 1) / 2, 0 < h i) :
    (m.hankel ((S + 1) / 2)).PosDef := by
  have hminor' : ∀ q ≤ (S + 1) / 2,
      ((m.hankel q).det = ∏ i ∈ Finset.range q, h i) := by
    intro q hq
    exact hminor q (le_trans hq (by omega))
  exact (positive_prefix_firewall m h hminor').mpr hwall

end RH
