/-
  CellCocycle — the exact cell-cocycle core of the closed
  diagonal-Gram route.
  ==================================================================

  Machine-checked abstract linear-algebra legacy of the qf-offensive
  Gram route (numeric counterpart:
  experiments/tfpt-discovery/qf_cell_cocycle_probe.py, verdict
  COCYCLE-DOMAIN-ONLY: exact identity at machine precision, PD cell
  blocks, PSD corner updates, zero domain breaches — but NO
  convergence cell passed, and per the frozen stakes the Gram route
  CLOSED).  This module states the theorem-shaped facts behind the
  measured run as general Mathlib theorems over ℝ — pure linear
  algebra, no number theory, no window data.

  (a) THE EXACT UPDATE IDENTITY (Banachiewicz / bordered Schur):
    * `invOf_fromBlocks_topLeft` — for [[A, B], [C, D]] with A and
      the Schur complement S = D - C⅟A B invertible, the top-left
      block of the inverse is ⅟A + ⅟A B ⅟S C ⅟A.
    * `transpose_invOf_of_symm` — ⅟A is symmetric when A is.
    * `bordered_update` — the symmetric bordered case
      [[A, B], [Bᵀ, C]]: the grown resolvent's old corner equals the
      previous resolvent PLUS the correction Y ⅟D Yᵀ with Y = ⅟A B
      and D = C - Bᵀ⅟A B — exactly the probe's per-rung identity
      G_{k+1} = G_k + Y D_k^{-1} Yᵀ (gated there to 9.7e-12 over
      73 rungs × 5 z).  Exact hypotheses: A invertible and the cell
      Schur block D invertible (the probe's measured min eig D_k in
      [0.0605, 0.0668] supplies both at real z < 0).

  (b) MONOTONE LOEWNER STEP:
    * `correction_posSemidef` — D positive definite ⇒ the correction
      Y ⅟D Yᵀ is positive semidefinite (congruence with ⅟D ⪰ 0).
    * `bordered_update_posSemidef` — (a) + (b): a PD cell block
      makes the bordered step Loewner-increasing on the old corner.
    * `step_loewner`, `posSemidef_sub_of_le`,
      `flow_monotone_of_steps` — one PSD step is monotone, and the
      finite ordered composition (sum) of such steps is monotone:
      k ≤ l ⇒ G_l ⪰ G_k.
    * `flow_posSemidef` — PSD-ness of the initial G propagates
      through the whole flow (domain preservation in its cleanest
      matrix form; the probe measured zero breaches in 730 tests).
    * `flow_sum_of_steps` — the telescoped normal form
      G_n = G_0 + Σ_{j<n} P_j of the ordered flow.

  (c) BOUNDED MONOTONE MATRIX CONVERGENCE:
    * `exists_entrywise_limit_of_monotone_bounded` — a Loewner-
      monotone sequence of symmetric matrices that is bounded above
      in the Loewner order (∃ U with U ⪰ G_k for all k) converges
      entrywise; the limit L is symmetric, satisfies G_k ⪯ L ⪯ U,
      and is obtained by monotone convergence of the quadratic forms
      x ⬝ᵥ G_k x (each is a monotone bounded real sequence) plus
      polarization.
    * `flow_entrywise_limit_of_bounded` — the same for a flow of
      PSD steps: domain + monotone + bound ⇒ limit.
    HONESTY: this theorem identifies the missing analytic
    ingredient of the measured route PRECISELY — a uniform Loewner
    upper bound U.  The finite ladder certified monotonicity and
    domain preservation but did NOT certify such a bound (its
    renormalized increments stayed flat at reachable depth), and
    this module does NOT claim the bound holds for the source
    operator.  Conditional statement only: IF a uniform bound
    existed, the corner cocycle would converge.

  (d) LINEAR-FRACTIONAL / REDHEFFER COMPOSITION (general form):
    * `lf_numer_factor`, `lf_denom_factor`, `lfDenomInvertible`,
      `lf_comp` — over an ARBITRARY ring (so in particular for
      square real matrices of a fixed size): the composition of two
      linear-fractional maps F ↦ (A F + B) ⅟(C F + D) is the
      linear-fractional map of the product coefficient matrix
      [[A₁,B₁],[C₁,D₁]]·[[A₂,B₂],[C₂,D₂]], with the composed
      denominator invertible whenever both stage denominators are.
    * `lf_shift`, `lf_shift_comp` — the monotone-shift special case
      used by (a)/(b): [[1, S], [0, 1]] acts as F ↦ F + S, and
      shifts compose additively — the probe's cell update is the
      Moebius action of the shift block with S = Y ⅟D Yᵀ.

  HONEST SCOPE.  Formalized: (a), (b), (d) in full generality for
  their stated objects ((d) at one fixed size — the ring form; the
  probe's dimension-changing d(X) transitions and Kato/polar
  transport are NOT formalized), and (c) as the abstract conditional
  convergence theorem.  NOT formalized (probe territory): the
  Toeplitz source construction, the Hotelling state refresh, the
  Nevanlinna/Herglotz complex-point sandwich, the z → 0 boundary
  transition, the renormalized-increment statistics, and every
  floating-point gate.  No `sorry`, no `native_decide`, no `decide`.

  Standalone module: no imports from other TfptCarrier files (built
  while a concurrent worker may hold the TfptCarrier.lean import
  list); the small overlap with GramCompactness (the quadratic-form
  expansion) is deliberate.
-/
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Topology.Order.MonotoneConvergence
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 1000000

open Filter Topology Matrix

namespace TfptCarrier.CellCocycle

variable {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq ι] [DecidableEq κ]

/-! ### (a) The exact update identity (bordered Schur / Banachiewicz) -/

/-- **(a) general form**: for a block matrix [[A, B], [C, D]] with A
and the Schur complement S = D - C⅟A B invertible, the top-left block
of the inverse is the previous inverse PLUS the correction
⅟A·B·⅟S·C·⅟A (Banachiewicz).  Direct projection of Mathlib's
`Matrix.invOf_fromBlocks₁₁_eq`. -/
theorem invOf_fromBlocks_topLeft (A : Matrix ι ι ℝ) (B : Matrix ι κ ℝ)
    (C : Matrix κ ι ℝ) (D : Matrix κ κ ℝ)
    [Invertible A] [Invertible (D - C * ⅟A * B)]
    [Invertible (fromBlocks A B C D)] :
    (⅟(fromBlocks A B C D)).toBlocks₁₁
      = ⅟A + ⅟A * B * ⅟(D - C * ⅟A * B) * C * ⅟A := by
  rw [invOf_fromBlocks₁₁_eq, toBlocks_fromBlocks₁₁]

/-- The inverse of a symmetric invertible matrix is symmetric. -/
theorem transpose_invOf_of_symm (A : Matrix ι ι ℝ) [Invertible A]
    (hA : Aᵀ = A) : (⅟A)ᵀ = ⅟A := by
  rw [invOf_eq_nonsing_inv, transpose_nonsing_inv, hA,
    ← invOf_eq_nonsing_inv]

/-- **(a) THE EXACT CELL UPDATE**: grow the window by one cell,
[[A, B], [Bᵀ, C]] with A symmetric; then the old corner of the grown
inverse is the previous inverse plus the correction Y ⅟D Yᵀ, with
Y = ⅟A·B (the carried state applied to the new columns) and
D = C - Bᵀ⅟A B (the cell Schur block) — the probe's identity
G_{k+1} = G_k + Y D_k⁻¹ Yᵀ in exact matrix form. -/
theorem bordered_update (A : Matrix ι ι ℝ) (B : Matrix ι κ ℝ)
    (C : Matrix κ κ ℝ) (hA : Aᵀ = A)
    [Invertible A] [Invertible (C - Bᵀ * ⅟A * B)]
    [Invertible (fromBlocks A B Bᵀ C)] :
    (⅟(fromBlocks A B Bᵀ C)).toBlocks₁₁
      = ⅟A + (⅟A * B) * ⅟(C - Bᵀ * ⅟A * B) * (⅟A * B)ᵀ := by
  rw [invOf_fromBlocks_topLeft, transpose_mul,
    transpose_invOf_of_symm A hA,
    Matrix.mul_assoc (⅟A * B * ⅟(C - Bᵀ * ⅟A * B)) Bᵀ (⅟A)]

/-! ### (b) The monotone Loewner step and its finite composition -/

omit [DecidableEq ι] in
/-- **(b) PSD correction**: a positive-definite cell block D makes the
correction term Y ⅟D Yᵀ positive semidefinite, for EVERY coefficient
matrix Y (congruence of ⅟D ⪰ 0).  The probe measured exactly this:
min eig D_k ∈ [0.0605, 0.0668] PD, corner update terms PSD to
-1.5e-17. -/
theorem correction_posSemidef {D : Matrix κ κ ℝ} [Invertible D]
    (hD : D.PosDef) (Y : Matrix ι κ ℝ) :
    (Y * ⅟D * Yᵀ).PosSemidef := by
  have hinv : (⅟D).PosSemidef := by
    rw [invOf_eq_nonsing_inv]
    exact hD.inv.posSemidef
  have h := hinv.mul_mul_conjTranspose_same Y
  have hYt : Yᴴ = Yᵀ := by
    ext a b
    simp [Matrix.conjTranspose_apply]
  rwa [hYt] at h

/-- **(a) + (b)**: with a symmetric previous window and a PD cell
Schur block, the bordered step is Loewner-increasing on the old
corner: G_{k+1} ⪰ G_k. -/
theorem bordered_update_posSemidef (A : Matrix ι ι ℝ) (B : Matrix ι κ ℝ)
    (C : Matrix κ κ ℝ) (hA : Aᵀ = A)
    [Invertible A] [Invertible (C - Bᵀ * ⅟A * B)]
    [Invertible (fromBlocks A B Bᵀ C)]
    (hD : (C - Bᵀ * ⅟A * B).PosDef) :
    ((⅟(fromBlocks A B Bᵀ C)).toBlocks₁₁ - ⅟A).PosSemidef := by
  rw [bordered_update A B C hA]
  simpa using correction_posSemidef hD (⅟A * B)

omit [Fintype ι] [DecidableEq ι] in
/-- A single PSD step is Loewner-monotone: (G + P) ⪰ G. -/
theorem step_loewner (G P : Matrix ι ι ℝ) (hP : P.PosSemidef) :
    ((G + P) - G).PosSemidef := by
  simpa using hP

omit [Fintype ι] [DecidableEq ι] in
/-- **(b) finite composition**: if every step of a matrix sequence is
Loewner-increasing, the whole flow is monotone: k ≤ l ⇒ G_l ⪰ G_k. -/
theorem posSemidef_sub_of_le (G : ℕ → Matrix ι ι ℝ)
    (hmono : ∀ k, (G (k + 1) - G k).PosSemidef)
    {k l : ℕ} (hkl : k ≤ l) : (G l - G k).PosSemidef := by
  induction l, hkl using Nat.le_induction with
  | base =>
      rw [sub_self]
      exact Matrix.PosSemidef.zero
  | succ l hkl ih =>
      have h := (hmono l).add ih
      rwa [sub_add_sub_cancel] at h

omit [Fintype ι] [DecidableEq ι] in
/-- The flow written with explicit PSD update terms (the probe's
G_{k+1} = G_k + Y_k D_k⁻¹ Y_kᵀ) is Loewner-monotone. -/
theorem flow_monotone_of_steps (G P : ℕ → Matrix ι ι ℝ)
    (hstep : ∀ k, G (k + 1) = G k + P k) (hP : ∀ k, (P k).PosSemidef)
    {k l : ℕ} (hkl : k ≤ l) : (G l - G k).PosSemidef :=
  posSemidef_sub_of_le G (fun k => by rw [hstep k]; simpa using hP k) hkl

omit [Fintype ι] [DecidableEq ι] in
/-- **(b) domain preservation**: PSD-ness of the initial matrix
propagates through the whole monotone flow — the Stieltjes-cone
transport of the probe in its cleanest matrix form. -/
theorem flow_posSemidef (G : ℕ → Matrix ι ι ℝ)
    (hmono : ∀ k, (G (k + 1) - G k).PosSemidef)
    (h0 : (G 0).PosSemidef) : ∀ k, (G k).PosSemidef := by
  intro k
  have h := (h0.add (posSemidef_sub_of_le G hmono (Nat.zero_le k)))
  have heq : G 0 + (G k - G 0) = G k := by abel
  rwa [heq] at h

omit [Fintype ι] [DecidableEq ι] in
/-- The telescoped normal form of the ordered flow:
G_n = G_0 + Σ_{j<n} P_j (Schur updates COMPOSE additively on the
corner — the summed form of the nested-quotient composition). -/
theorem flow_sum_of_steps (G P : ℕ → Matrix ι ι ℝ)
    (hstep : ∀ k, G (k + 1) = G k + P k) (n : ℕ) :
    G n = G 0 + ∑ j ∈ Finset.range n, P j := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [hstep n, ih, Finset.sum_range_succ]
      abel

/-! ### (c) Bounded monotone matrix convergence -/

omit [DecidableEq ι] in
/-- The bilinear form of a real matrix as an explicit double sum. -/
theorem dotProduct_mulVec_expand (M : Matrix ι ι ℝ) (x y : ι → ℝ) :
    x ⬝ᵥ (M *ᵥ y) = ∑ i, ∑ j, x i * M i j * y j := by
  simp [dotProduct, Matrix.mulVec, Finset.mul_sum, mul_assoc]

/-- Coordinate evaluation of the bilinear form. -/
theorem single_dotProduct_mulVec_single (M : Matrix ι ι ℝ) (i j : ι) :
    (Pi.single i 1 : ι → ℝ) ⬝ᵥ (M *ᵥ Pi.single j 1) = M i j := by
  rw [dotProduct_mulVec_expand]
  simp [Pi.single_apply, ite_mul, mul_ite]

omit [DecidableEq ι] in
/-- Bilinear expansion of the quadratic form on a sum. -/
theorem quadForm_add (M : Matrix ι ι ℝ) (x y : ι → ℝ) :
    (x + y) ⬝ᵥ (M *ᵥ (x + y))
      = x ⬝ᵥ (M *ᵥ x) + y ⬝ᵥ (M *ᵥ y)
        + (x ⬝ᵥ (M *ᵥ y) + y ⬝ᵥ (M *ᵥ x)) := by
  rw [Matrix.mulVec_add, dotProduct_add, add_dotProduct, add_dotProduct]
  ring

/-- Polarization: every entry of a symmetric matrix is a rational
combination of three quadratic-form values. -/
theorem entry_eq_quadForm (M : Matrix ι ι ℝ)
    (hsym : ∀ i j, M i j = M j i) (i j : ι) :
    M i j
      = ((Pi.single i 1 + Pi.single j 1) ⬝ᵥ
            (M *ᵥ (Pi.single i 1 + Pi.single j 1))
          - (Pi.single i 1 : ι → ℝ) ⬝ᵥ (M *ᵥ Pi.single i 1)
          - (Pi.single j 1 : ι → ℝ) ⬝ᵥ (M *ᵥ Pi.single j 1)) / 2 := by
  rw [quadForm_add, single_dotProduct_mulVec_single,
    single_dotProduct_mulVec_single, single_dotProduct_mulVec_single,
    single_dotProduct_mulVec_single, hsym j i]
  ring

/-- **(c) BOUNDED MONOTONE MATRIX CONVERGENCE**: a Loewner-monotone
sequence of symmetric real matrices that is bounded above in the
Loewner order converges entrywise; the limit L is symmetric and
satisfies G_k ⪯ L ⪯ U for every k.  Proof: each quadratic form
x ⬝ᵥ G_k x is a monotone real sequence bounded by x ⬝ᵥ U x, hence
converges to its supremum; polarization recovers the entries.

THE HONESTY CLAUSE: the hypothesis `hbdd` — a UNIFORM Loewner upper
bound — is exactly the ingredient the measured cocycle route lacked.
The probe certified the monotone flow and the domain transport but
NOT this bound; nothing here claims it holds for the source
operator. -/
theorem exists_entrywise_limit_of_monotone_bounded
    (G : ℕ → Matrix ι ι ℝ) (U : Matrix ι ι ℝ)
    (hsym0 : (G 0)ᵀ = G 0)
    (hmono : ∀ k, (G (k + 1) - G k).PosSemidef)
    (hbdd : ∀ k, (U - G k).PosSemidef) :
    ∃ L : Matrix ι ι ℝ, Lᵀ = L
      ∧ (∀ k, (L - G k).PosSemidef) ∧ (U - L).PosSemidef
      ∧ ∀ i j, Tendsto (fun k => G k i j) atTop (𝓝 (L i j)) := by
  have hsub : ∀ {k l : ℕ}, k ≤ l → (G l - G k).PosSemidef :=
    fun {k l} h => posSemidef_sub_of_le G hmono h
  -- entrywise symmetry propagates from G 0 through Hermitian increments
  have hsymE : ∀ k i j, G k i j = G k j i := by
    intro k i j
    have hh := (hsub (Nat.zero_le k)).1
    have h1 := congrFun (congrFun hh i) j
    have h0 := congrFun (congrFun hsym0 i) j
    simp only [Matrix.conjTranspose_apply, Matrix.sub_apply, star_trivial,
      Matrix.transpose_apply] at h1 h0
    linarith
  -- quadratic forms: monotone in k and bounded above by the U-form
  have hqmono : ∀ x : ι → ℝ, Monotone fun k => x ⬝ᵥ (G k *ᵥ x) := by
    intro x
    refine monotone_nat_of_le_succ fun k => ?_
    have h := (hmono k).dotProduct_mulVec_nonneg x
    rw [star_trivial, Matrix.sub_mulVec, dotProduct_sub] at h
    linarith
  have hqle : ∀ (x : ι → ℝ) (k : ℕ),
      x ⬝ᵥ (G k *ᵥ x) ≤ x ⬝ᵥ (U *ᵥ x) := by
    intro x k
    have h := (hbdd k).dotProduct_mulVec_nonneg x
    rw [star_trivial, Matrix.sub_mulVec, dotProduct_sub] at h
    linarith
  have hqbdd : ∀ x : ι → ℝ,
      BddAbove (Set.range fun k => x ⬝ᵥ (G k *ᵥ x)) := by
    intro x
    exact ⟨x ⬝ᵥ (U *ᵥ x), by rintro _ ⟨k, rfl⟩; exact hqle x k⟩
  have hqlim : ∀ x : ι → ℝ,
      Tendsto (fun k => x ⬝ᵥ (G k *ᵥ x)) atTop
        (𝓝 (⨆ k, x ⬝ᵥ (G k *ᵥ x))) :=
    fun x => tendsto_atTop_ciSup (hqmono x) (hqbdd x)
  -- the limit matrix via polarization of the quadratic suprema
  obtain ⟨L, hlim⟩ : ∃ L : Matrix ι ι ℝ,
      ∀ i j, Tendsto (fun k => G k i j) atTop (𝓝 (L i j)) := by
    refine ⟨Matrix.of fun i j =>
      ((⨆ k, (Pi.single i 1 + Pi.single j 1) ⬝ᵥ
          (G k *ᵥ (Pi.single i 1 + Pi.single j 1)))
        - (⨆ k, (Pi.single i 1 : ι → ℝ) ⬝ᵥ (G k *ᵥ Pi.single i 1))
        - (⨆ k, (Pi.single j 1 : ι → ℝ) ⬝ᵥ (G k *ᵥ Pi.single j 1))) / 2,
      fun i j => ?_⟩
    have h := (((hqlim (Pi.single i 1 + Pi.single j 1)).sub
      (hqlim (Pi.single i 1))).sub (hqlim (Pi.single j 1))).div_const
      (2 : ℝ)
    exact h.congr fun k => (entry_eq_quadForm (G k) (hsymE k) i j).symm
  -- symmetry of the limit, by uniqueness of limits
  have hLsym : Lᵀ = L := by
    ext i j
    show L j i = L i j
    have h1 : Tendsto (fun k => G k i j) atTop (𝓝 (L j i)) :=
      (hlim j i).congr fun k => hsymE k j i
    exact tendsto_nhds_unique h1 (hlim i j)
  -- the quadratic form of the limit IS the supremum
  have hquadL : ∀ x : ι → ℝ,
      x ⬝ᵥ (L *ᵥ x) = ⨆ k, x ⬝ᵥ (G k *ᵥ x) := by
    intro x
    have h1 : Tendsto (fun k => x ⬝ᵥ (G k *ᵥ x)) atTop
        (𝓝 (x ⬝ᵥ (L *ᵥ x))) := by
      simp only [dotProduct_mulVec_expand]
      exact tendsto_finset_sum _ fun i _ => tendsto_finset_sum _ fun j _ =>
        ((hlim i j).const_mul (x i)).mul_const (x j)
    exact tendsto_nhds_unique h1 (hqlim x)
  -- L is an upper bound of the flow
  have hLge : ∀ k, (L - G k).PosSemidef := by
    intro k
    refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ fun x => ?_
    · show (L - G k).conjTranspose = L - G k
      ext i j
      have hL := congrFun (congrFun hLsym i) j
      simp only [Matrix.transpose_apply] at hL
      simp only [Matrix.conjTranspose_apply, Matrix.sub_apply, star_trivial]
      rw [hL, hsymE k j i]
    · rw [star_trivial, Matrix.sub_mulVec, dotProduct_sub, hquadL]
      have h := le_ciSup (hqbdd x) k
      linarith
  -- and L stays below the given Loewner bound
  have hUL : (U - L).PosSemidef := by
    refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ fun x => ?_
    · show (U - L).conjTranspose = U - L
      ext i j
      have hh := (hbdd 0).1
      have hUij := congrFun (congrFun hh i) j
      simp only [Matrix.conjTranspose_apply, Matrix.sub_apply,
        star_trivial] at hUij
      have h0 := hsymE 0 j i
      have hU : U j i = U i j := by linarith
      have hL := congrFun (congrFun hLsym i) j
      simp only [Matrix.transpose_apply] at hL
      simp only [Matrix.conjTranspose_apply, Matrix.sub_apply, star_trivial]
      rw [hU, hL]
    · rw [star_trivial, Matrix.sub_mulVec, dotProduct_sub, hquadL]
      have h := ciSup_le fun k => hqle x k
      linarith
  exact ⟨L, hLsym, hLge, hUL, hlim⟩

/-- **(b) + (c)**: a flow of PSD steps (the probe's cell cocycle) with
a symmetric start and a uniform Loewner upper bound converges
entrywise — domain + monotone + bound ⇒ limit.  The bound hypothesis
is exactly what the finite ladder did not certify. -/
theorem flow_entrywise_limit_of_bounded (G P : ℕ → Matrix ι ι ℝ)
    (U : Matrix ι ι ℝ)
    (hstep : ∀ k, G (k + 1) = G k + P k) (hP : ∀ k, (P k).PosSemidef)
    (hsym0 : (G 0)ᵀ = G 0) (hbdd : ∀ k, (U - G k).PosSemidef) :
    ∃ L : Matrix ι ι ℝ, Lᵀ = L
      ∧ (∀ k, (L - G k).PosSemidef) ∧ (U - L).PosSemidef
      ∧ ∀ i j, Tendsto (fun k => G k i j) atTop (𝓝 (L i j)) :=
  exists_entrywise_limit_of_monotone_bounded G U hsym0
    (fun k => by rw [hstep k]; simpa using hP k) hbdd

/-! ### (d) Linear-fractional / Redheffer composition (ring form) -/

section Redheffer

variable {R : Type*} [Ring R]

/-- Numerator factorization of the composed linear-fractional map:
(A₁A₂ + B₁C₂)F + (A₁B₂ + B₁D₂) = (A₁·lf₂(F) + B₁)·(C₂F + D₂). -/
theorem lf_numer_factor (A₁ A₂ B₁ B₂ C₂ D₂ F : R)
    [Invertible (C₂ * F + D₂)] :
    (A₁ * A₂ + B₁ * C₂) * F + (A₁ * B₂ + B₁ * D₂)
      = (A₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + B₁) * (C₂ * F + D₂) := by
  have h : (A₂ * F + B₂) * ⅟(C₂ * F + D₂) * (C₂ * F + D₂)
      = A₂ * F + B₂ := by
    rw [mul_assoc, invOf_mul_self, mul_one]
  calc (A₁ * A₂ + B₁ * C₂) * F + (A₁ * B₂ + B₁ * D₂)
      = A₁ * (A₂ * F + B₂) + B₁ * (C₂ * F + D₂) := by noncomm_ring
    _ = A₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂) * (C₂ * F + D₂))
          + B₁ * (C₂ * F + D₂) := by rw [h]
    _ = (A₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + B₁)
          * (C₂ * F + D₂) := by noncomm_ring

/-- Denominator factorization of the composed linear-fractional map:
(C₁A₂ + D₁C₂)F + (C₁B₂ + D₁D₂) = (C₁·lf₂(F) + D₁)·(C₂F + D₂). -/
theorem lf_denom_factor (A₂ B₂ C₁ C₂ D₁ D₂ F : R)
    [Invertible (C₂ * F + D₂)] :
    (C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂)
      = (C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁) * (C₂ * F + D₂) := by
  have h : (A₂ * F + B₂) * ⅟(C₂ * F + D₂) * (C₂ * F + D₂)
      = A₂ * F + B₂ := by
    rw [mul_assoc, invOf_mul_self, mul_one]
  calc (C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂)
      = C₁ * (A₂ * F + B₂) + D₁ * (C₂ * F + D₂) := by noncomm_ring
    _ = C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂) * (C₂ * F + D₂))
          + D₁ * (C₂ * F + D₂) := by rw [h]
    _ = (C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁)
          * (C₂ * F + D₂) := by noncomm_ring

/-- The composed denominator is invertible whenever both stage
denominators are — invertibility propagates through the Redheffer
composition. -/
@[implicit_reducible]
def lfDenomInvertible (A₂ B₂ C₁ C₂ D₁ D₂ F : R)
    [Invertible (C₂ * F + D₂)]
    [Invertible (C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁)] :
    Invertible ((C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂)) where
  invOf := ⅟(C₂ * F + D₂) * ⅟(C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁)
  invOf_mul_self := by
    rw [lf_denom_factor A₂ B₂ C₁ C₂ D₁ D₂ F, mul_assoc,
      ← mul_assoc (⅟(C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁)),
      invOf_mul_self, one_mul, invOf_mul_self]
  mul_invOf_self := by
    rw [lf_denom_factor A₂ B₂ C₁ C₂ D₁ D₂ F, mul_assoc,
      ← mul_assoc (C₂ * F + D₂), mul_invOf_self, one_mul, mul_invOf_self]

/-- **(d) THE REDHEFFER COMPOSITION THEOREM** (over an arbitrary ring,
in particular for square real matrices of a fixed size): the
composition of two linear-fractional maps F ↦ (A F + B) ⅟(C F + D) is
the linear-fractional map of the PRODUCT coefficient matrix —
lf(M₁, lf(M₂, F)) = lf(M₁·M₂, F) with
M₁·M₂ = [[A₁A₂ + B₁C₂, A₁B₂ + B₁D₂], [C₁A₂ + D₁C₂, C₁B₂ + D₁D₂]].
This is the ordered cocycle multiplication of the probe: Schur
complements COMPOSE, they are not summed. -/
theorem lf_comp (A₁ B₁ C₁ D₁ A₂ B₂ C₂ D₂ F : R)
    [Invertible (C₂ * F + D₂)]
    [Invertible (C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁)]
    [Invertible ((C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂))] :
    ((A₁ * A₂ + B₁ * C₂) * F + (A₁ * B₂ + B₁ * D₂))
        * ⅟((C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂))
      = (A₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + B₁)
        * ⅟(C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁) := by
  have hinv : ⅟((C₁ * A₂ + D₁ * C₂) * F + (C₁ * B₂ + D₁ * D₂))
      = ⅟(C₂ * F + D₂)
        * ⅟(C₁ * ((A₂ * F + B₂) * ⅟(C₂ * F + D₂)) + D₁) := by
    apply invOf_eq_right_inv
    rw [lf_denom_factor A₂ B₂ C₁ C₂ D₁ D₂ F, mul_assoc,
      ← mul_assoc (C₂ * F + D₂), mul_invOf_self, one_mul, mul_invOf_self]
  rw [hinv, lf_numer_factor A₁ A₂ B₁ B₂ C₂ D₂ F, mul_assoc,
    ← mul_assoc (C₂ * F + D₂), mul_invOf_self, one_mul]

/-- The monotone-shift special case: the coefficient block
[[1, S], [0, 1]] acts as the shift F ↦ F + S — the probe's cell
update is this Moebius action with S = Y ⅟D Yᵀ. -/
theorem lf_shift (S F : R) [Invertible ((0 : R) * F + 1)] :
    ((1 : R) * F + S) * ⅟((0 : R) * F + 1) = F + S := by
  have h : ⅟((0 : R) * F + 1) = 1 := invOf_eq_right_inv (by simp)
  rw [h, mul_one, one_mul]

/-- Shifts compose additively: the product of the shift blocks
[[1, S₁], [0, 1]]·[[1, S₂], [0, 1]] = [[1, S₂ + S₁], [0, 1]] acts as
the composed shift — the linear-fractional face of the additive flow
of (b). -/
theorem lf_shift_comp (S₁ S₂ F : R) [Invertible ((0 : R) * F + 1)] :
    ((1 : R) * F + (S₂ + S₁)) * ⅟((0 : R) * F + 1) = (F + S₂) + S₁ := by
  rw [lf_shift (S₂ + S₁) F, ← add_assoc]

end Redheffer

end TfptCarrier.CellCocycle
