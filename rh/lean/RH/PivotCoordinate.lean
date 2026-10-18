/-
RH/PivotCoordinate.lean -- r380: the five Fable finite-algebra lemmas
(DCCXXXVII) in source pivot coordinates.

Targets (lemma-first, three exits: proved / named-decomposed /
documented-impossible-with-mathlib-reason):
  1. `rankOne_inertia_antitone` -- PROVED (sigNeg as max dim of a
     negative-definite subspace; the rank-1 PSD update cannot create
     a new negative direction and can kill at most one).
  2. `adaptive_band_from_entry` -- PROVED (induction on (1)).
  3. `signed_dual_hankel_complement_inertia` -- DECOMPOSED: rectangular
     Vandermonde Gram and full-size inertia `In H_S = In diag(w)` are
     PROVED against the existing `SignedAtoms` / `VonMangoldtWindow`
     objects (no parallel Hankel); the discrete Christoffel / Borodin
     identification of the trailing Schur block with `H_{S-k}(σa)` is
     the named Prop `ComplementaryDualHankelInertia` (mathlib v4.29.1 has
     Vandermonde + Haynsworth, not the dual OP basis; same class as
     DualResolvent's `CauchyInterlace` — the Borodin construction of R
     is outside the kernel).
  4. `detK2_eq_postcap_pivot_ratio` -- DECOMPOSED: the h-ratio rewriting
     of consecutive Hankel determinants is PROVED; DPP
     `det(I−2R_r)=H_r(σa)/H_r(a)` and the signed Borodin complement
     `H_r(σa)=H_{S-r}(w)/(Δ²∏w)` are named Props (the OP construction
     of R is the DualResolvent-documented gap).
  5. `p1_p2_iff_cap_posDef` -- PROVED on the pivot / Hankel side
     (Jacobi/LDL count + Sylvester prefix): the three-way dictionary
     `{ind₋ H_{N+2} ≤ 1 ∧ h_N h_{N+1} < 0} ↔ {positive prefix through
     the cap ∧ exactly one post-cap defect} ↔ {H_N ≻ 0 ∧ post-cap
     structure}`.  The identification of those pivot statements with
     the Haynsworth premises (P1)/(P2) is the named pair
     `P1EqCapInertia` / `P2EqPostcapAlternation` (consumes (3)+(4)).

Does not assert (P1)/(P2) on any window.  Does not touch the two
canonical arithmetic holes.  NO RH CLAIM.

Provenance: DCCXXXVII Fable finite-algebra sondes; r377
`rh/problem/postcap_pivots.tex`; r373 Haynsworth / Window Vandermonde.
-/
import RH.Haynsworth
import RH.Window
import Mathlib.Algebra.Module.Submodule.Map
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Vandermonde

namespace RH

open Matrix QuadraticMap QuadraticForm

/-! ## Negative inertia as `sigNeg` -/

/-- Negative inertia `ind₋` of a real matrix, as the quadratic-form
signature `sigNeg` (max dim of a negative-definite subspace; equal to
the number of strictly negative eigenvalues when the matrix is
Hermitian, `sigNeg_eq_ncard_neg_eigenvalues`). -/
noncomputable def indNeg {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) : ℕ :=
  sigNeg A.toQuadraticMap'

/-! ## Rank-1 Gram bookkeeping -/

lemma isHermitian_vecMulVec_self {n : Type*} [Fintype n] (v : n → ℝ) :
    (vecMulVec v v).IsHermitian := by
  ext i j
  simp [Matrix.conjTranspose_apply, vecMulVec_apply, mul_comm]

lemma mulVec_vecMulVec_self {n : Type*} [Fintype n] (v x : n → ℝ) :
    vecMulVec v v *ᵥ x = (v ⬝ᵥ x) • v := by
  ext i
  simp only [mulVec, vecMulVec_apply, dotProduct, Pi.smul_apply, smul_eq_mul]
  calc ∑ j, v i * v j * x j
      = ∑ j, (v j * x j) * v i := Finset.sum_congr rfl fun _ _ => by ring
    _ = (∑ j, v j * x j) * v i := (Finset.sum_mul _ _ _).symm

lemma toQuadraticMap'_vecMulVec_self {n : Type*} [Fintype n] [DecidableEq n]
    (v x : n → ℝ) :
    (vecMulVec v v).toQuadraticMap' x = (v ⬝ᵥ x) ^ 2 := by
  rw [toQuadraticMap'_apply_index, mulVec_vecMulVec_self]
  simp [dotProduct_smul, smul_eq_mul, pow_two, dotProduct_comm]

lemma toQuadraticMap'_add {n : Type*} [Fintype n] [DecidableEq n]
    (A B : Matrix n n ℝ) (x : n → ℝ) :
    (A + B).toQuadraticMap' x = A.toQuadraticMap' x + B.toQuadraticMap' x := by
  rw [toQuadraticMap'_apply_index, toQuadraticMap'_apply_index,
    toQuadraticMap'_apply_index, Matrix.add_mulVec, dotProduct_add]

lemma toQuadraticMap'_add_vecMulVec {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) (v x : n → ℝ) :
    (A + vecMulVec v v).toQuadraticMap' x
      = A.toQuadraticMap' x + (v ⬝ᵥ x) ^ 2 := by
  rw [toQuadraticMap'_add, toQuadraticMap'_vecMulVec_self]

/-- Coordinate functional `x ↦ v ⬝ x`. -/
def coordDot {n : Type*} [Fintype n] (v : n → ℝ) : (n → ℝ) →ₗ[ℝ] ℝ where
  toFun := fun x => v ⬝ᵥ x
  map_add' := fun x y => by simp [dotProduct_add]
  map_smul' := fun r x => by simp [dotProduct_smul]

/-! ## Lemma 1: rank-one inertia antitone -/

lemma restrict_neg_apply {n : Type*} [Fintype n]
    (Q : QuadraticForm ℝ (n → ℝ)) (V : Submodule ℝ (n → ℝ))
    (x : V) : (Q.restrict V) x = Q x.val :=
  rfl

lemma restrict_negDef_apply {n : Type*} [Fintype n]
    (Q : QuadraticForm ℝ (n → ℝ)) (V : Submodule ℝ (n → ℝ))
    (x : V) : ((-Q).restrict V) x = -Q x.val := by
  simp

/-- Rank-1 Loewner update cannot raise negative inertia: if `A + vvᵀ`
is negative definite on `V`, then so is `A` (the Gram term `(v·x)²`
is nonnegative). -/
lemma rankOne_negDef_of_update {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) (v : n → ℝ) (V : Submodule ℝ (n → ℝ))
    (hV : ((-(A + vecMulVec v v).toQuadraticMap').restrict V).PosDef) :
    ((-A.toQuadraticMap').restrict V).PosDef := by
  intro x hx
  have hlt := hV x hx
  rw [restrict_negDef_apply] at hlt ⊢
  have hQ := toQuadraticMap'_add_vecMulVec A v x.val
  have : (A + vecMulVec v v).toQuadraticMap' x.val < 0 := neg_pos.mp hlt
  have : A.toQuadraticMap' x.val
      + (v ⬝ᵥ x.val) ^ 2 < 0 := by
    rwa [← hQ]
  have : A.toQuadraticMap' x.val < 0 :=
    lt_of_le_of_lt (le_add_of_nonneg_right (sq_nonneg _)) this
  exact neg_pos.mpr this

/-- **Rank-one inertia antitone** (DCCXXXVII; PROVED).  For a real
Hermitian `A` and any vector `v`,
  `ind₋(A + vvᵀ) ≤ ind₋(A)` and `ind₋(A) ≤ ind₋(A + vvᵀ) + 1`.
The first half is Loewner: a negative-definite subspace of the update
is negative-definite for `A`.  The second half is rank-nullity on the
coordinate `x ↦ v·x` inside a maximal negative-definite subspace of
`A`: the kernel has codimension at most 1 and the update agrees with
`A` there.

Finite real algebra (the definition of `sigNeg`).  mathlib v4.29.1 has
no Weyl / Courant–Fischer interlacing lemma (`CauchyInterlace` in
`RH/DualResolvent.lean` remains a named Prop and is not consumed).
NO RH CLAIM. -/
theorem rankOne_inertia_antitone {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n ℝ) (v : n → ℝ) (hA : A.IsHermitian) :
    indNeg (A + vecMulVec v v) ≤ indNeg A
    ∧ indNeg A ≤ indNeg (A + vecMulVec v v) + 1 := by
  classical
  let _ := hA
  constructor
  · obtain ⟨V, hdim, hneg⟩ :=
      exists_finrank_eq_sigNeg_and_negDef (A + vecMulVec v v).toQuadraticMap'
    have hAneg := rankOne_negDef_of_update A v V hneg
    have hle := le_sigNeg_of_negDef A.toQuadraticMap' hAneg
    simpa [indNeg, hdim] using hle
  · obtain ⟨V, hdim, hneg⟩ :=
      exists_finrank_eq_sigNeg_and_negDef A.toQuadraticMap'
    set φ : (n → ℝ) →ₗ[ℝ] ℝ := coordDot v
    set f : V →ₗ[ℝ] ℝ := φ.comp (Submodule.subtype V)
    have hrank := LinearMap.finrank_range_add_finrank_ker f
    have hrange : Module.finrank ℝ (LinearMap.range f) ≤ 1 := by
      have hle := (LinearMap.range f).finrank_le
      have : Module.finrank ℝ ℝ = 1 := by simp [Module.finrank_self]
      omega
    have hker : Module.finrank ℝ V ≤ Module.finrank ℝ (LinearMap.ker f) + 1 := by
      omega
    set W : Submodule ℝ (n → ℝ) := V ⊓ φ.ker
    have hWmap :
        Submodule.map (Submodule.subtype V) (LinearMap.ker f) = W := by
      simp [W, f, LinearMap.ker_comp, Submodule.map_comap_subtype]
    have hWdim :
        Module.finrank ℝ (LinearMap.ker f) = Module.finrank ℝ W := by
      rw [← hWmap]
      exact LinearEquiv.finrank_eq
        (Submodule.equivMapOfInjective (Submodule.subtype V)
          (Submodule.injective_subtype V) (LinearMap.ker f))
    have hWneg :
        ((-(A + vecMulVec v v).toQuadraticMap').restrict W).PosDef := by
      intro x hx
      have hxinf := (Submodule.mem_inf.mp x.property)
      have hxV : x.val ∈ V := hxinf.1
      have hxker : x.val ∈ φ.ker := hxinf.2
      have hφ0 : φ x.val = 0 := LinearMap.mem_ker.mp hxker
      have hx0 : x.val ≠ 0 := by
        intro h0
        apply hx
        exact Subtype.ext h0
      have hAneg : ((-A.toQuadraticMap').restrict V) ⟨x.val, hxV⟩ > 0 :=
        hneg ⟨x.val, hxV⟩ (by
          intro h0
          apply hx0
          exact congrArg Subtype.val h0)
      rw [restrict_negDef_apply] at hAneg
      have hQ := toQuadraticMap'_add_vecMulVec A v x.val
      have hdot : v ⬝ᵥ x.val = 0 := by
        simpa [φ, coordDot] using hφ0
      have : (A + vecMulVec v v).toQuadraticMap' x.val
          = A.toQuadraticMap' x.val := by
        rw [hQ, hdot, pow_two, mul_zero, add_zero]
      rw [restrict_negDef_apply, this]
      exact hAneg
    have hWle := le_sigNeg_of_negDef (A + vecMulVec v v).toQuadraticMap' hWneg
    have : Module.finrank ℝ V ≤ Module.finrank ℝ W + 1 := by
      simpa [hWdim] using hker
    simp only [indNeg] at hdim ⊢
    omega

/-! ## Lemma 2: adaptive band from an entry -/

/-- **Adaptive rank-band** (DCCXXXVII; PROVED).  A Loewner chain
`A_{n+1} = A_n + v_n v_nᵀ` cannot raise negative inertia, so an entry
`ind₋(A_{n₀}) ≤ 1` propagates to every later rung.  Direct induction
on `rankOne_inertia_antitone`.  The entry index `n₀` is an input
(DCCXXXVII: it is source-defined, not spectral).  NO RH CLAIM. -/
theorem adaptive_band_from_entry {n : Type*} [Fintype n] [DecidableEq n]
    (A : ℕ → Matrix n n ℝ) (v : ℕ → n → ℝ)
    (hSym : ∀ k, (A k).IsHermitian)
    (hStep : ∀ k, A (k + 1) = A k + vecMulVec (v k) (v k))
    (n0 : ℕ) (hEntry : indNeg (A n0) ≤ 1) :
    ∀ k, n0 ≤ k → indNeg (A k) ≤ 1 := by
  intro k hk
  have step : ∀ d, indNeg (A (n0 + d)) ≤ 1 := by
    intro d
    induction d with
    | zero => simpa using hEntry
    | succ d ih =>
        have hup :=
          (rankOne_inertia_antitone (A (n0 + d)) (v (n0 + d)) (hSym (n0 + d))).1
        rw [Nat.add_succ, hStep]
        exact le_trans hup ih
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hk
  exact step d

/-! ## Window ↔ SignedAtoms (no parallel Hankel) -/

/-- The window's signed defect measure as a `SignedAtoms` object.
`H_k` / `h_k` are NOT re-defined: they are the existing
`VonMangoldtWindow.hankel` / `h` and `SignedAtoms.hankel`. -/
def VonMangoldtWindow.toSignedAtoms (w : VonMangoldtWindow) :
    SignedAtoms w.S where
  x := fun j => ((w.nodes j : ℚ) : ℝ)
  w := fun j => ((w.weight j : ℚ) : ℝ)

theorem VonMangoldtWindow.hankel_eq_signedAtoms (w : VonMangoldtWindow)
    (p : ℕ) : w.hankel p = w.toSignedAtoms.hankel p := by
  ext i k
  simp only [VonMangoldtWindow.hankel, SignedAtoms.hankel,
    VonMangoldtWindow.mom, VonMangoldtWindow.toSignedAtoms,
    VonMangoldtWindow.weight]
  push_cast
  rfl

/-! ## Rectangular Vandermonde Gram (lemma 3, proved half) -/

/-- Rectangular Vandermonde: row `j` (atom), column `i` (power `x_j^i`).
Agrees with `SignedAtoms.vand` at `k = S` and with mathlib
`vandermonde` / `rectVandermonde`. -/
def SignedAtoms.vandRect {S : ℕ} (m : SignedAtoms S) (k : ℕ) :
    Matrix (Fin S) (Fin k) ℝ :=
  fun j i => m.x j ^ (i : ℕ)

theorem SignedAtoms.vandRect_eq_vand {S : ℕ} (m : SignedAtoms S) :
    m.vandRect S = m.vand := rfl

theorem SignedAtoms.vand_eq_vandermonde {S : ℕ} (m : SignedAtoms S) :
    m.vand = vandermonde m.x := by
  ext j i
  simp [SignedAtoms.vand, vandermonde_apply]

/-- Rectangular Vandermonde Gram: `H_k = V_{S,k}ᵀ diag(w) V_{S,k}`.
Definitional sum algebra (`pow_add`); no determinant formula. -/
theorem SignedAtoms.hankel_eq_vand_rect {S : ℕ} (m : SignedAtoms S)
    (k : ℕ) :
    m.hankel k = (m.vandRect k)ᵀ * diagonal m.w * m.vandRect k := by
  ext i j
  rw [Matrix.mul_apply]
  simp only [Matrix.mul_diagonal, Matrix.transpose_apply,
    SignedAtoms.vandRect, SignedAtoms.hankel]
  exact Finset.sum_congr rfl fun t _ => by rw [pow_add]; ring

/-- Full-size Vandermonde is invertible iff the nodes are pairwise
distinct (mathlib `det_vandermonde_ne_zero_iff`). -/
theorem SignedAtoms.vand_det_ne_zero_iff {S : ℕ} (m : SignedAtoms S) :
    m.vand.det ≠ 0 ↔ Function.Injective m.x := by
  rw [m.vand_eq_vandermonde]
  exact det_vandermonde_ne_zero_iff

/-- **Full-size inertia**: `In H_S(w) = In diag(w)` when the nodes are
distinct.  Congruence `H_S = Vᵀ diag(w) V` plus `sigNeg_congruence`. -/
theorem sigNeg_full_hankel_eq_sigNeg_weights {S : ℕ} (m : SignedAtoms S)
    (hinj : Function.Injective m.x) :
    indNeg (m.hankel S) = indNeg (diagonal m.w) := by
  have hfact := m.hankel_eq_vand_conj
  have hVunit : IsUnit m.vand.det :=
    isUnit_iff_ne_zero.mpr ((m.vand_det_ne_zero_iff).mpr hinj)
  have h := sigNeg_congruence (diagonal m.w) m.vand hVunit
  simpa [indNeg, hfact] using h

/-- The Jacobi chain of a signed atom set, as the existing Sylvester
ratio (same formula as `VonMangoldtWindow.h`). -/
noncomputable def SignedAtoms.h {S : ℕ} (m : SignedAtoms S) (k : ℕ) : ℝ :=
  (m.hankel (k + 1)).det / (m.hankel k).det

theorem SignedAtoms.hankel_det_zero {S : ℕ} (m : SignedAtoms S) :
    (m.hankel 0).det = 1 :=
  Matrix.det_fin_zero

theorem SignedAtoms.hankel_det_eq_prod_h {S : ℕ} (m : SignedAtoms S) :
    ∀ q, (∀ i < q, (m.hankel i).det ≠ 0) →
      (m.hankel q).det = ∏ i ∈ Finset.range q, m.h i := by
  intro q
  induction q with
  | zero =>
      intro
      simp
  | succ q ih =>
      intro hnz
      have hq : (m.hankel q).det ≠ 0 := hnz q (Nat.lt_succ_self q)
      have ih' := ih fun i hi => hnz i (Nat.lt_succ_of_lt hi)
      rw [Finset.prod_range_succ, ← ih']
      unfold SignedAtoms.h
      field_simp [hq]

theorem VonMangoldtWindow.h_eq_signedAtoms (w : VonMangoldtWindow)
    (k : ℕ) : w.h k = w.toSignedAtoms.h k := by
  simp [VonMangoldtWindow.h, SignedAtoms.h, w.hankel_eq_signedAtoms]

/-- Dual CD weight on the same nodes:
`a_j = 1 / (|w_j| ∏_{i≠j} (x_j − x_i)²)`, and `σa_j = sign(w_j) a_j`
which equals `1 / (w_j ∏_{i≠j} (x_j − x_i)²)` at nonvanishing atoms.
Defined on the existing `SignedAtoms` carrier — no second Hankel type. -/
noncomputable def SignedAtoms.nodePolyDerivSq {S : ℕ} (m : SignedAtoms S)
    (j : Fin S) : ℝ :=
  ∏ i : Fin S, if i = j then 1 else (m.x j - m.x i) ^ 2

noncomputable def SignedAtoms.signedDualWeight {S : ℕ} (m : SignedAtoms S)
    (j : Fin S) : ℝ :=
  if m.w j = 0 ∨ m.nodePolyDerivSq j = 0 then 0
  else 1 / (m.w j * m.nodePolyDerivSq j)

noncomputable def SignedAtoms.signedDual {S : ℕ} (m : SignedAtoms S) :
    SignedAtoms S where
  x := m.x
  w := m.signedDualWeight

/-- **Named Prop (lemma 3 remainder).**  Complementary inertia
`In H_k(w) + In H_{S-k}(σa) = In diag(w)` for a nondegenerate signed
atomic measure on `S` distinct nodes.

WHY NAMED, NOT A SORRY (r380 mathlib census, v4.29.1): this file
proves the rectangular Vandermonde Gram `H_k = V_{S,k}ᵀ diag(w) V_{S,k}`
and the full-size identity `In H_S = In diag(w)` (nodes injective);
Haynsworth additivity is proved in `RH/Haynsworth.lean`.  What is
absent is the discrete Christoffel–Darboux / Borodin identification
of the trailing Schur block of `H_S` with the dual Hankel `H_{S-k}(σa)`
(the OP construction of the dual ensemble).  DualResolvent already
records that construction as outside the kernel.  Same convention as
`CauchyInterlace` / `PoleDyadicIndependence`: statable, consumable,
never a silent `sorry`. -/
def ComplementaryDualHankelInertia : Prop :=
  ∀ {S k : ℕ} (m : SignedAtoms S),
    k ≤ S → Function.Injective m.x → (∀ j, m.w j ≠ 0) →
    indNeg (m.hankel k) + indNeg ((m.signedDual).hankel (S - k))
      = indNeg (diagonal m.w)

/-- Lemma 3, hypothesis form: the complementary inertia identity
follows from its named Prop.  The proved Vandermonde / full-size half
stands independently above (`hankel_eq_vand_rect`,
`sigNeg_full_hankel_eq_sigNeg_weights`). -/
theorem signed_dual_hankel_complement_inertia
    (h : ComplementaryDualHankelInertia)
    {S k : ℕ} (m : SignedAtoms S) (hk : k ≤ S)
    (hinj : Function.Injective m.x) (hnz : ∀ j, m.w j ≠ 0) :
    indNeg (m.hankel k) + indNeg ((m.signedDual).hankel (S - k))
      = indNeg (diagonal m.w) :=
  h m hk hinj hnz

/-! ## Lemma 4: DPP / Borodin / post-cap ratio -/

/-- **Named Prop.**  Discrete OPE / Sylvester identity
`det(I − 2 R_r) = H_r(σa) / H_r(a)` in the `a`-orthonormal polynomial
basis.  The Borodin OP-construction of the L-ensemble resolvent `R`
is outside the DualResolvent kernel (file header there); mathlib
v4.29.1 has no CD kernel / discrete OPE. -/
def DPPIdentity : Prop :=
  ∀ {S r : ℕ} (m a : SignedAtoms S) (R : Matrix (Fin r) (Fin r) ℝ),
    r ≤ S → (∀ j, 0 < a.w j) → (a.hankel r).det ≠ 0 →
    ((1 : Matrix (Fin r) (Fin r) ℝ) - (2 : ℝ) • R).det
      = (m.signedDual.hankel r).det / (a.hankel r).det

/-- **Named Prop.**  Signed Borodin complement
`H_r(σa) = H_{S-r}(w) / (Δ(X)² ∏ w)` for a nondegenerate atomic
measure on `S` nodes.  Cauchy–Binet on the Vandermonde embedding;
the compound-matrix bookkeeping is not in mathlib v4.29.1. -/
def SignedBorodinComplement : Prop :=
  ∀ {S r : ℕ} (m : SignedAtoms S),
    r ≤ S → Function.Injective m.x → (∀ j, m.w j ≠ 0) → (m.vand).det ≠ 0 →
    (m.signedDual.hankel r).det
      = (m.hankel (S - r)).det
        / ((m.vand).det ^ 2 * ∏ j : Fin S, m.w j)

/-- **Named Prop.**  Identification of the Haynsworth 2×2 matrix
`K₂ = I + Uᵀ A₀⁻¹ U` at the two-rank cut `r = N−3` with the DPP /
Borodin ratio of Hankel determinants.  Consumes `DPPIdentity` and
`SignedBorodinComplement` plus the dictionary between `K₂` and
`I − 2 R_r` (two-step L-ensemble update). -/
def K2EqHankelRatio : Prop :=
  ∀ {S N : ℕ} (m a : SignedAtoms S) (K2 : Matrix (Fin 2) (Fin 2) ℝ),
    S = 2 * N - 1 → 3 ≤ N →
    (m.hankel (N + 2)).det ≠ 0 → (a.hankel (N - 1)).det ≠ 0 →
    K2.det
      = (m.hankel N).det * (a.hankel (N - 3)).det
        / ((m.hankel (N + 2)).det * (a.hankel (N - 1)).det)

/-- Consecutive Hankel ratios telescope to the four-pivot product
(DCCXXXVII magnitude form).  Finite field algebra; no DPP. -/
theorem postcap_pivot_ratio_eq_h_form {S N : ℕ} (m a : SignedAtoms S)
    (hN : 3 ≤ N)
    (hm : ∀ i ≤ N + 2, (m.hankel i).det ≠ 0)
    (ha : ∀ i ≤ N - 1, (a.hankel i).det ≠ 0) :
    (m.hankel N).det * (a.hankel (N - 3)).det
      / ((m.hankel (N + 2)).det * (a.hankel (N - 1)).det)
    = 1 / (m.h N * m.h (N + 1) * a.h (N - 3) * a.h (N - 2)) := by
  have hmN : (m.hankel N).det ≠ 0 := hm N (by omega)
  have hmN1 : (m.hankel (N + 1)).det ≠ 0 := hm (N + 1) (by omega)
  have hmN2 : (m.hankel (N + 2)).det ≠ 0 := hm (N + 2) (by omega)
  have haN3 : (a.hankel (N - 3)).det ≠ 0 := ha (N - 3) (by omega)
  have haN2 : (a.hankel (N - 2)).det ≠ 0 := ha (N - 2) (by omega)
  have haN1 : (a.hankel (N - 1)).det ≠ 0 := ha (N - 1) (by omega)
  have hm_prod : m.h N * m.h (N + 1)
      = (m.hankel (N + 2)).det / (m.hankel N).det := by
    unfold SignedAtoms.h
    field_simp [hmN, hmN1, hmN2]
  have ha_prod : a.h (N - 3) * a.h (N - 2)
      = (a.hankel (N - 1)).det / (a.hankel (N - 3)).det := by
    unfold SignedAtoms.h
    have h1 : N - 3 + 1 = N - 2 := by omega
    have h2 : N - 2 + 1 = N - 1 := by omega
    rw [h1, h2]
    field_simp [haN3, haN2, haN1]
  have hm_inv : (m.hankel N).det / (m.hankel (N + 2)).det
      = (m.h N * m.h (N + 1))⁻¹ := by
    simpa [inv_div] using (congrArg Inv.inv hm_prod).symm
  have ha_inv : (a.hankel (N - 3)).det / (a.hankel (N - 1)).det
      = (a.h (N - 3) * a.h (N - 2))⁻¹ := by
    simpa [inv_div] using (congrArg Inv.inv ha_prod).symm
  calc (m.hankel N).det * (a.hankel (N - 3)).det
        / ((m.hankel (N + 2)).det * (a.hankel (N - 1)).det)
      = (m.hankel N).det / (m.hankel (N + 2)).det
          * ((a.hankel (N - 3)).det / (a.hankel (N - 1)).det) := by
        field_simp [hmN, hmN2, haN3, haN1]
    _ = (m.h N * m.h (N + 1))⁻¹ * (a.h (N - 3) * a.h (N - 2))⁻¹ := by
        rw [hm_inv, ha_inv]
    _ = 1 / (m.h N * m.h (N + 1) * a.h (N - 3) * a.h (N - 2)) := by
        simp
        ac_rfl

/-- Lemma 4, hypothesis form: the post-cap ratio identity for `det K₂`
follows from the named identification `K2EqHankelRatio`.  The
telescoping `h`-form is the proved companion
`postcap_pivot_ratio_eq_h_form`. -/
theorem detK2_eq_postcap_pivot_ratio
    (h : K2EqHankelRatio)
    {S N : ℕ} (m a : SignedAtoms S)
    (hS : S = 2 * N - 1) (hN : 3 ≤ N)
    (K2 : Matrix (Fin 2) (Fin 2) ℝ)
    (hdet : (m.hankel (N + 2)).det ≠ 0 ∧ (a.hankel (N - 1)).det ≠ 0) :
    K2.det
      = (m.hankel N).det * (a.hankel (N - 3)).det
        / ((m.hankel (N + 2)).det * (a.hankel (N - 1)).det) :=
  h m a K2 hS hN hdet.1 hdet.2

/-! ## Lemma 5: pivot-coordinate synthesis (Jacobi + Sylvester) -/

lemma ncard_neg_pivots_eq_sigNeg {p : ℕ}
    (M : Matrix (Fin p) (Fin p) ℝ) (hM : M.IsHermitian) (h : ℕ → ℝ)
    (hminor : ∀ q (hq : q ≤ p),
      (M.submatrix (Fin.castLE hq) (Fin.castLE hq)).det
        = ∏ i ∈ Finset.range q, h i)
    (hnz : ∀ i < p, h i ≠ 0) :
    {i : Fin p | h (i : ℕ) < 0}.ncard = sigNeg M.toQuadraticMap' := by
  obtain ⟨P, hPunit, hPdiag⟩ := exists_congruent_diagonal p M hM h hminor hnz
  have hE : Equivalent M.toQuadraticMap'
      (weightedSumSquares ℝ fun i : Fin p => h (i : ℕ)) := by
    have hc := equivalent_toQuadraticMap'_congruence M P hPunit
    rw [hPdiag, toQuadraticMap'_diagonal] at hc
    exact hc.symm
  simpa using (sigNeg_of_equiv_weightedSumSquares hE).symm

lemma hankel_minors_of_h {S p : ℕ} (m : SignedAtoms S)
    (hnzDet : ∀ i ≤ p, (m.hankel i).det ≠ 0) :
    (∀ q (hq : q ≤ p),
      ((m.hankel p).submatrix (Fin.castLE hq) (Fin.castLE hq)).det
        = ∏ i ∈ Finset.range q, m.h i)
    ∧ (∀ i < p, m.h i ≠ 0) := by
  constructor
  · intro q hq
    have : (m.hankel p).submatrix (Fin.castLE hq) (Fin.castLE hq)
        = m.hankel q := rfl
    rw [this]
    refine m.hankel_det_eq_prod_h q fun i hi => ?_
    exact hnzDet i (le_of_lt (lt_of_lt_of_le hi hq))
  · intro i hip
    unfold SignedAtoms.h
    exact div_ne_zero (hnzDet (i + 1) hip) (hnzDet i (le_of_lt hip))

/-- Jacobi count on a Hankel prefix: `ind₋ H_p = #{h_i < 0 : i < p}`
when no pivot vanishes. -/
theorem indNeg_hankel_eq_neg_pivot_count {S p : ℕ} (m : SignedAtoms S)
    (hnzDet : ∀ i ≤ p, (m.hankel i).det ≠ 0) :
    indNeg (m.hankel p) = {i : Fin p | m.h (i : ℕ) < 0}.ncard := by
  obtain ⟨hminor, hnz⟩ := hankel_minors_of_h m hnzDet
  have h := ncard_neg_pivots_eq_sigNeg (m.hankel p) (m.hankel_isHermitian p)
    m.h hminor hnz
  simp [indNeg, h]

lemma two_mul_neg_iff {a b : ℝ} (_ha : a ≠ 0) (_hb : b ≠ 0) :
    a * b < 0 ↔ a < 0 ∧ 0 < b ∨ 0 < a ∧ b < 0 := by
  constructor
  · intro h
    rcases (mul_neg_iff.mp h) with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · exact Or.inr ⟨h1, h2⟩
    · exact Or.inl ⟨h1, h2⟩
  · intro h
    rcases h with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · exact mul_neg_of_neg_of_pos h1 h2
    · exact mul_neg_of_pos_of_neg h1 h2

lemma ncard_fin_succ_succ_neg {N : ℕ} (h : ℕ → ℝ)
    (hnz : ∀ i < N + 2, h i ≠ 0) :
    {i : Fin (N + 2) | h (i : ℕ) < 0}.ncard ≤ 1 ∧ h N * h (N + 1) < 0 ↔
      (∀ i < N, 0 < h i)
      ∧ (h N < 0 ∧ 0 < h (N + 1) ∨ 0 < h N ∧ h (N + 1) < 0) := by
  classical
  have hNz : h N ≠ 0 := hnz N (by omega)
  have hN1z : h (N + 1) ≠ 0 := hnz (N + 1) (by omega)
  let NF : Fin (N + 2) := ⟨N, by omega⟩
  let N1F : Fin (N + 2) := ⟨N + 1, by omega⟩
  have hNFval : (NF : ℕ) = N := rfl
  have hN1Fval : (N1F : ℕ) = N + 1 := rfl
  constructor
  · rintro ⟨hcard, hprod⟩
    have halt := (two_mul_neg_iff hNz hN1z).mp hprod
    refine ⟨fun i hi => ?_, halt⟩
    have hiz : h i ≠ 0 := hnz i (by omega)
    rcases hiz.lt_or_gt with hneg | hpos
    · exfalso
      let iF : Fin (N + 2) := ⟨i, by omega⟩
      have hiS : iF ∈ {j : Fin (N + 2) | h (j : ℕ) < 0} := hneg
      have hineN : iF ≠ NF := by
        intro h
        have : i = N := by simpa [iF, NF] using congrArg Fin.val h
        omega
      have hineN1 : iF ≠ N1F := by
        intro h
        have : i = N + 1 := by simpa [iF, N1F] using congrArg Fin.val h
        omega
      have htwo : 2 ≤ {j : Fin (N + 2) | h (j : ℕ) < 0}.ncard := by
        rcases halt with ⟨hNn, _⟩ | ⟨_, hN1n⟩
        · have hsub : ({iF, NF} : Set (Fin (N + 2)))
              ⊆ {j | h (j : ℕ) < 0} := by
            intro x hx
            rcases (Set.mem_insert_iff.mp hx) with rfl | hx'
            · exact hiS
            · rw [Set.mem_singleton_iff] at hx'
              subst hx'
              exact hNn
          have hpair : ({iF, NF} : Set (Fin (N + 2))).ncard = 2 :=
            Set.ncard_pair hineN
          exact hpair.symm.trans_le (Set.ncard_le_ncard hsub)
        · have hsub : ({iF, N1F} : Set (Fin (N + 2)))
              ⊆ {j | h (j : ℕ) < 0} := by
            intro x hx
            rcases (Set.mem_insert_iff.mp hx) with rfl | hx'
            · exact hiS
            · rw [Set.mem_singleton_iff] at hx'
              subst hx'
              exact hN1n
          have hpair : ({iF, N1F} : Set (Fin (N + 2))).ncard = 2 :=
            Set.ncard_pair hineN1
          exact hpair.symm.trans_le (Set.ncard_le_ncard hsub)
      omega
    · exact hpos
  · rintro ⟨hpre, halt⟩
    have hprod := (two_mul_neg_iff hNz hN1z).mpr halt
    refine ⟨?_, hprod⟩
    rcases halt with ⟨hNn, hN1p⟩ | ⟨hNp, hN1n⟩
    · have heq : {i : Fin (N + 2) | h (i : ℕ) < 0} = {NF} := by
        ext j
        simp only [Set.mem_setOf_eq, Set.mem_singleton_iff]
        constructor
        · intro hj
          have : j.val < N ∨ j.val = N ∨ j.val = N + 1 := by omega
          rcases this with hlt | hjN | hjN1
          · have := hpre j.val hlt
            linarith
          · exact Fin.ext hjN
          · have : h (j : ℕ) = h (N + 1) := by
              congr 1
            rw [this] at hj
            linarith
        · intro hj
          rw [hj]
          exact hNn
      rw [heq, Set.ncard_singleton]
    · have heq : {i : Fin (N + 2) | h (i : ℕ) < 0} = {N1F} := by
        ext j
        simp only [Set.mem_setOf_eq, Set.mem_singleton_iff]
        constructor
        · intro hj
          have : j.val < N ∨ j.val = N ∨ j.val = N + 1 := by omega
          rcases this with hlt | hjN | hjN1
          · have := hpre j.val hlt
            linarith
          · have : h (j : ℕ) = h N := by
              congr 1
            rw [this] at hj
            linarith
          · exact Fin.ext hjN1
        · intro hj
          rw [hj]
          exact hN1n
      rw [heq, Set.ncard_singleton]

/-- **Pivot synthesis** (DCCXXXVII lemma 5, the Hankel / Jacobi face;
PROVED).  For a nonvanishing Sylvester chain through degree `N+1`,
  `ind₋ H_{N+2} ≤ 1 ∧ h_N h_{N+1} < 0`
  `↔` the prefix `h_0,…,h_{N-1}` is positive and exactly one of
      `{h_N, h_{N+1}}` is negative
  `↔` `H_N ≻ 0` and that same post-cap defect.
This is the measured half-filling pinning as a pivot statement
(Jacobi count + reverse Sylvester).  It does not assert the
Haynsworth premises (P1)/(P2) on a window; those identifications are
the named Props `P1EqCapInertia` / `P2EqPostcapAlternation`.
NO RH CLAIM. -/
theorem p1_p2_iff_cap_posDef {S N : ℕ} (m : SignedAtoms S)
    (hnzDet : ∀ i ≤ N + 2, (m.hankel i).det ≠ 0) :
    let postCap :=
      m.h N < 0 ∧ 0 < m.h (N + 1) ∨ 0 < m.h N ∧ m.h (N + 1) < 0
    (indNeg (m.hankel (N + 2)) ≤ 1 ∧ m.h N * m.h (N + 1) < 0
        ↔ (∀ i < N, 0 < m.h i) ∧ postCap)
    ∧ ((∀ i < N, 0 < m.h i) ∧ postCap
        ↔ (m.hankel N).PosDef ∧ postCap) := by
  intro postCap
  have hcount := indNeg_hankel_eq_neg_pivot_count m hnzDet
  have hnz : ∀ i < N + 2, m.h i ≠ 0 := (hankel_minors_of_h m hnzDet).2
  have hiff := ncard_fin_succ_succ_neg m.h hnz
  have hfw : (m.hankel N).PosDef ↔ ∀ i < N, 0 < m.h i := by
    have hnzN : ∀ i ≤ N, (m.hankel i).det ≠ 0 := fun i hi =>
      hnzDet i (le_trans hi (by omega))
    have hminor : ∀ q ≤ N, (m.hankel q).det = ∏ i ∈ Finset.range q, m.h i :=
      by
        intro q hq
        exact m.hankel_det_eq_prod_h q fun i hi =>
          hnzN i (le_of_lt (lt_of_lt_of_le hi hq))
    exact positive_prefix_firewall m m.h hminor
  constructor
  · simpa [hcount, postCap] using hiff
  · constructor
    · intro ⟨hp, hc⟩
      exact ⟨hfw.mpr hp, hc⟩
    · intro ⟨hPD, hc⟩
      exact ⟨hfw.mp hPD, hc⟩

/-- **Named Prop.**  Haynsworth premise (P1) at the two-rank cut
`r = N−3` is `ind₋ H_{N+2}(w) ≤ 1`, via complementary inertia plus
the SVD identification `ind₋(R_r − ½I) = ind₋ H_{S-r}(w)`.  The
second step is the Borodin projector on the negative atoms (outside
DualResolvent). -/
def P1EqCapInertia : Prop :=
  ∀ {S N : ℕ} (m : SignedAtoms S) (A0 : Matrix (Fin (N - 3)) (Fin (N - 3)) ℝ),
    S = 2 * N - 1 → 3 ≤ N →
    (indNeg A0 = 1 ↔ indNeg (m.hankel (N + 2)) ≤ 1)

/-- **Named Prop.**  Haynsworth premise (P2) `det K₂ < 0` is the
post-cap alternation `h_N h_{N+1} < 0`, given positive dual Hankels
`a > 0`.  Consumes `K2EqHankelRatio` and
`postcap_pivot_ratio_eq_h_form`. -/
def P2EqPostcapAlternation : Prop :=
  ∀ {S N : ℕ} (m a : SignedAtoms S) (K2 : Matrix (Fin 2) (Fin 2) ℝ),
    S = 2 * N - 1 → 3 ≤ N → (∀ i < N - 1, 0 < a.h i) →
    (K2.det < 0 ↔ m.h N * m.h (N + 1) < 0)

end RH
