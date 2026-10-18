/-
RH/Augmented.lean -- THE AUGMENTED SUBORDINATION L† (r332, the reviewer
unification round): L* and the terminal statement are the distributed and
the rank-one part of ONE strict sampling inequality.

THE BIRD'S-EYE VIEW (the r332 reviewer mandate, verbatim in content).
With `H_w` the signed Hankel matrix at the half-filling degree, `u_w` the
border vector, `B_w > 0` the budget and `ℓ_w(p) = u_wᵀ c` the border
readout of the coefficient vector `c` of `p`, quadratic completion turns
the full local target statement into ONE inequality:

  (L†)  ∫p² dν_w + |ℓ_w(p)|² / B_w  <  ∫p² dμ_w
        for every real polynomial p ≠ 0 with deg p < N_w.

Everything connecting L† to the existing library is FINITE ALGEBRA, and
this file closes all of it sorry-free:
  * without the border term, L† is verbatim L* (`AugmentedSubordination
    → LStar`: the border square over the positive budget is nonnegative);
  * L† ⟺ `A_{w,cap} ≻ 0` (and all smaller degrees as principal
    submatrices) -- `augmentedSubordination_iff_masterCap`.  The ⟸
    direction is the quadratic completion at the test vector
    `(c, t)` with `t = -ℓ(p)/B`; the ⟹ direction splits the augmented
    quadratic form as `(μ−ν)(p²) − ℓ²/B + B(t + ℓ/B)²` and cases on
    `c = 0` (budget corner) vs `c ≠ 0` (the L† inequality);
  * L† ⟺ L* ∧ Terminal -- `augmentedSubordination_iff_lstar_and_
    terminal`.  Forward: L* directly (drop the border square), Terminal
    through the master cap (`budget_pos_of_augmented` +
    `D_pos_of_augmented` + `q_lt_one_of_pos`, the wave-10 extraction
    lemmas -- the reviewer's H⁻¹u-minimizer evaluation is REPLACED by
    the determinant route: `B − uᵀH⁻¹u = D_cap = det A_cap / det H_cap
    > 0` needs no explicit minimizer).  Backward: the wave-10
    reconstruction chain re-run against its own bricks
    (`lstar_implies_hankel_posDef` + `terminal_margin_pos_of_terminal`
    + `posDef_fromBlocks_border` + principal restriction) --
    deliberately WITHOUT consuming `lstar_terminal_implies_master`, so
    that the corollary relation below is non-circular.

THE CORROLLARY RELATION (documented as demanded): the r305
reconstruction theorem `lstar_terminal_implies_master` (RH/Closure.lean,
byte-stable, NOT touched) is now a corollary of the two equivalences --
`reconstruction_via_augmented` below re-derives its exact statement as
`iff_masterCap.mp ∘ iff_lstar_and_terminal.mpr`, with no reference to
the original.  L† is thereby the COMMON TARGET FORM of the two true
holes, not a third hole: `augmentedSubordination_main` (since C1 in
RH/Canonical.lean, on the canonical final domain) states
`AugmentedSubordination w` as a PROVED consequence of the two existing
holes (`lstar_canonical` + `terminal_canonical`), never as a new
`sorry`.

GEOMETRIC READING (documentation only, not formalized): L† says
`‖T_w‖ < 1` for the observation operator
`T_w p = ((√ν_j · p(x_j))_j, ℓ_w(p)/√B)` on the μ-Hilbert space -- the
distributed channel (ν sampling) and the rank-one channel (border
readout) are jointly strictly subordinate to μ.

SORRY CENSUS OF THIS FILE: ZERO.  The census of the library is
unchanged (8); the two true holes stay byte-identical where they are.

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import RH.Window
import RH.Inertia
import RH.Closure

namespace RH

open Matrix Polynomial VonMangoldtWindow

namespace VonMangoldtWindow

variable (w : VonMangoldtWindow)

/-! ## Finite-algebra helpers: the augmented quadratic form -/

/-- the coefficient polynomial of the zero vector is the zero
polynomial. -/
theorem coeffPoly_zero (n : ℕ) : coeffPoly (0 : Fin n → ℝ) = 0 := by
  simp [coeffPoly]

/-- `coeffPoly` inverts coefficient extraction: for `deg p < n` the
coefficient polynomial of the coefficient vector of `p` is `p` itself
(mathlib `as_sum_range_C_mul_X_pow'`). -/
theorem coeffPoly_coeffs {n : ℕ} (p : Polynomial ℝ)
    (hdeg : p.natDegree < n) :
    coeffPoly (fun i : Fin n => p.coeff (i : ℕ)) = p := by
  rw [coeffPoly, Fin.sum_univ_eq_sum_range
    (fun k => Polynomial.C (p.coeff k) * Polynomial.X ^ k) n]
  exact (p.as_sum_range_C_mul_X_pow' hdeg).symm

/-- the μ-integral of the zero polynomial vanishes. -/
theorem muSq_zero : w.muSq 0 = 0 := by simp [muSq]

/-- the ν-integral of the zero polynomial vanishes. -/
theorem nuSq_zero : w.nuSq 0 = 0 := by simp [nuSq]

/-- the augmented matrix is symmetric, hence Hermitian over ℝ (Hankel
block symmetry + the shared border column). -/
theorem A_isHermitian (n : ℕ) : (w.A n).IsHermitian := by
  ext a b
  rcases a with i | ⟨⟩ <;> rcases b with k | ⟨⟩ <;>
    simp [VonMangoldtWindow.A, Matrix.conjTranspose_apply, hankel,
      Nat.add_comm]

/-- **the augmented quadratic form, split** (finite algebra, PROVED):
at the test vector `(x, t)` the quadratic form of
`A_n = [[H_n, u_n], [u_nᵀ, B]]` is
`xᵀ H_n x + 2 t (u·x) + B t²` -- the wall term, the mixed border term
and the budget corner. -/
theorem A_quadform (n : ℕ) (x : Fin n → ℝ) (t : ℝ) :
    star (Sum.elim x fun _ : Unit => t) ⬝ᵥ
        (w.A n *ᵥ Sum.elim x fun _ : Unit => t)
      = x ⬝ᵥ (w.hankel n *ᵥ x) + 2 * t * (w.borderVec n ⬝ᵥ x)
        + ((w.B : ℚ) : ℝ) * t ^ 2 := by
  have h1 : ∀ i : Fin n,
      (w.A n *ᵥ Sum.elim x fun _ : Unit => t) (Sum.inl i)
        = (w.hankel n *ᵥ x) i + w.borderVec n i * t := by
    intro i
    simp [VonMangoldtWindow.A, Matrix.mulVec, dotProduct,
      Fintype.sum_sum_type, borderVec]
  have h2 : (w.A n *ᵥ Sum.elim x fun _ : Unit => t) (Sum.inr ())
      = w.borderVec n ⬝ᵥ x + ((w.B : ℚ) : ℝ) * t := by
    simp [VonMangoldtWindow.A, Matrix.mulVec, dotProduct,
      Fintype.sum_sum_type, borderVec]
  calc star (Sum.elim x fun _ : Unit => t) ⬝ᵥ
        (w.A n *ᵥ Sum.elim x fun _ : Unit => t)
      = (∑ i : Fin n,
          x i * (w.A n *ᵥ Sum.elim x fun _ : Unit => t) (Sum.inl i))
        + t * (w.A n *ᵥ Sum.elim x fun _ : Unit => t) (Sum.inr ()) := by
        simp [dotProduct, Fintype.sum_sum_type]
    _ = (∑ i : Fin n,
          x i * ((w.hankel n *ᵥ x) i + w.borderVec n i * t))
        + t * (w.borderVec n ⬝ᵥ x + ((w.B : ℚ) : ℝ) * t) := by
        rw [h2]
        congr 1
        exact Finset.sum_congr rfl fun i _ => by rw [h1 i]
    _ = x ⬝ᵥ (w.hankel n *ᵥ x) + 2 * t * (w.borderVec n ⬝ᵥ x)
        + ((w.B : ℚ) : ℝ) * t ^ 2 := by
        have hsum : ∑ i : Fin n,
            x i * ((w.hankel n *ᵥ x) i + w.borderVec n i * t)
            = (∑ i : Fin n, x i * (w.hankel n *ᵥ x) i)
              + t * ∑ i : Fin n, w.borderVec n i * x i := by
          rw [Finset.mul_sum, ← Finset.sum_add_distrib]
          exact Finset.sum_congr rfl fun i _ => by ring
        simp only [dotProduct]
        rw [hsum]
        ring

end VonMangoldtWindow

/-! ## The border readout functional and L† -/

/-- **the border readout functional** `ℓ_w(p) = u_wᵀ c` -- the border
column of the bordered RHP dictionary (v958) paired with the
coefficient vector of `p` through the half-filling cap. -/
noncomputable def borderFunctional (w : VonMangoldtWindow)
    (p : Polynomial ℝ) : ℝ :=
  ∑ i : Fin w.cap, w.borderVec w.cap i * p.coeff (i : ℕ)

/-- the border readout of a coefficient polynomial is the plain dot
product with the coefficient vector. -/
theorem borderFunctional_coeffPoly (w : VonMangoldtWindow)
    (x : Fin w.cap → ℝ) :
    borderFunctional w (coeffPoly x) = w.borderVec w.cap ⬝ᵥ x := by
  simp only [borderFunctional, dotProduct]
  exact Finset.sum_congr rfl fun i _ => by rw [coeffPoly_coeff]

/-- **THE AUGMENTED SUBORDINATION L†** (r332, the reviewer
unification): positive budget normalization, and for every nonzero
real polynomial below the half-filling cap the ν-mass PLUS the
budget-normalized border square stays strictly below the μ-mass --
the distributed (L*) and rank-one (terminal) channels of ONE strict
sampling inequality.  This is a DEFINITION, not a new hole: for MAIN
windows it is PROVED equivalent to the two existing holes
(`augmentedSubordination_main` below). -/
def AugmentedSubordination (w : VonMangoldtWindow) : Prop :=
  0 < ((w.B : ℚ) : ℝ) ∧
  ∀ p : Polynomial ℝ, p ≠ 0 → p.natDegree < w.cap →
    w.nuSq p + borderFunctional w p ^ 2 / ((w.B : ℚ) : ℝ) < w.muSq p

/-! ## L† ⟺ the master cap positivity -/

/-- the quadratic-completion scalar step (ordered-field algebra): at
the minimizing border coordinate `t = -ℓ/B` the mixed and corner terms
collapse to `-ℓ²/B`. -/
private theorem completion_scalar {m ν ℓ B : ℝ} (hB : 0 < B)
    (h : 0 < m - ν + 2 * -(ℓ / B) * ℓ + B * (-(ℓ / B)) ^ 2) :
    ν + ℓ ^ 2 / B < m := by
  have hBne : B ≠ 0 := ne_of_gt hB
  have hkey : 2 * -(ℓ / B) * ℓ + B * (-(ℓ / B)) ^ 2 = -(ℓ ^ 2 / B) := by
    field_simp
    ring
  linarith [hkey]

/-- **L† ⟺ THE MASTER CAP** (r332; the reviewer's central
equivalence, sorry-free): the augmented subordination holds iff every
augmented matrix `A_{w,n} = [[H_n, u_n], [u_nᵀ, B]]` through the
half-filling cap is positive definite.

⟹ : split the augmented quadratic form at `(x, t)` as
`(μ−ν)(p_x²) + 2t·ℓ + B t²`; for `x = 0` the form is the positive
budget corner `B t²`; for `x ≠ 0` complete the square,
`= [(μ−ν)(p_x²) − ℓ²/B] + B(t + ℓ/B)²`, and the bracket is the strict
L† margin.  Smaller degrees restrict as principal submatrices
(`A_eq_submatrix_A_cap`).
⟸ : evaluate the positive form at the reviewer's test vector
`(c, -ℓ(p)/B)`; the budget corner extraction gives `B > 0`.  NO RH
CLAIM. -/
theorem augmentedSubordination_iff_masterCap (w : VonMangoldtWindow) :
    AugmentedSubordination w ↔ ∀ n ≤ w.cap, (w.A n).PosDef := by
  constructor
  · rintro ⟨hB, hstrict⟩
    have hcap : (w.A w.cap).PosDef := by
      refine Matrix.PosDef.of_dotProduct_mulVec_pos
        (w.A_isHermitian w.cap) fun z hz => ?_
      obtain ⟨x, t, rfl⟩ : ∃ (x : Fin w.cap → ℝ) (t : ℝ),
          z = Sum.elim x fun _ : Unit => t :=
        ⟨fun i => z (Sum.inl i), z (Sum.inr ()), by
          funext a; rcases a with i | ⟨⟩ <;> rfl⟩
      rw [w.A_quadform w.cap x t, w.hankel_quadform w.cap x]
      by_cases hx0 : x = 0
      · subst hx0
        have ht : t ≠ 0 := by
          intro h0
          apply hz
          funext a
          rcases a with i | ⟨⟩
          · rfl
          · exact h0
        have ht2 : 0 < t ^ 2 :=
          lt_of_le_of_ne (sq_nonneg t) (Ne.symm (pow_ne_zero 2 ht))
        rw [coeffPoly_zero, w.muSq_zero, w.nuSq_zero, dotProduct_zero]
        simpa using mul_pos hB ht2
      · have hp : coeffPoly x ≠ 0 := coeffPoly_ne_zero hx0
        obtain ⟨i0, -⟩ := Function.ne_iff.mp hx0
        have hdeg : (coeffPoly x).natDegree < w.cap :=
          coeffPoly_natDegree_lt i0.pos x
        have hsx := hstrict (coeffPoly x) hp hdeg
        rw [borderFunctional_coeffPoly] at hsx
        have hnn : 0 ≤ ((w.B : ℚ) : ℝ)
            * (t + (w.borderVec w.cap ⬝ᵥ x) / ((w.B : ℚ) : ℝ)) ^ 2 :=
          mul_nonneg hB.le (sq_nonneg _)
        have hBne : ((w.B : ℚ) : ℝ) ≠ 0 := ne_of_gt hB
        have hkey : ((w.B : ℚ) : ℝ)
            * (t + (w.borderVec w.cap ⬝ᵥ x) / ((w.B : ℚ) : ℝ)) ^ 2
            = 2 * t * (w.borderVec w.cap ⬝ᵥ x)
              + ((w.B : ℚ) : ℝ) * t ^ 2
              + (w.borderVec w.cap ⬝ᵥ x) ^ 2 / ((w.B : ℚ) : ℝ) := by
          field_simp
          ring
        rw [hkey] at hnn
        linarith
    intro n hn
    rw [A_eq_submatrix_A_cap w hn]
    exact posDef_submatrix_of_injective hcap
      ((Fin.castLE_injective hn).sumMap Function.injective_id)
  · intro hA
    have hAcap := hA w.cap le_rfl
    have hB : (0 : ℝ) < ((w.B : ℚ) : ℝ) :=
      w.budget_pos_of_augmented hAcap
    refine ⟨hB, fun p hp hdeg => ?_⟩
    have hpx : coeffPoly (fun i : Fin w.cap => p.coeff (i : ℕ)) = p :=
      coeffPoly_coeffs p hdeg
    have hxne : (fun i : Fin w.cap => p.coeff (i : ℕ)) ≠ 0 := by
      intro h0
      exact hp (by rw [← hpx, h0, coeffPoly_zero])
    have hzne : (Sum.elim (fun i : Fin w.cap => p.coeff (i : ℕ))
        fun _ : Unit => -(borderFunctional w p / ((w.B : ℚ) : ℝ))) ≠ 0 := by
      intro h0
      apply hxne
      funext i
      simpa using congrFun h0 (Sum.inl i)
    have hpos := hAcap.dotProduct_mulVec_pos hzne
    rw [w.A_quadform w.cap (fun i : Fin w.cap => p.coeff (i : ℕ))
        (-(borderFunctional w p / ((w.B : ℚ) : ℝ))),
      w.hankel_quadform w.cap, hpx] at hpos
    have hdotx : w.borderVec w.cap ⬝ᵥ (fun i : Fin w.cap => p.coeff (i : ℕ))
        = borderFunctional w p := by
      rw [← hpx, borderFunctional_coeffPoly, hpx]
    rw [hdotx] at hpos
    exact completion_scalar hB hpos

/-! ## L† ⟺ L* ∧ Terminal -/

/-- **without the border term, L† is L*** (finite algebra, PROVED):
the budget-normalized border square is nonnegative, so dropping it
weakens L† to the plain subordination. -/
theorem augmentedSubordination_implies_lstar (w : VonMangoldtWindow)
    (h : AugmentedSubordination w) : LStar w := by
  obtain ⟨hB, hstrict⟩ := h
  intro p hp hdeg
  have hnn : 0 ≤ borderFunctional w p ^ 2 / ((w.B : ℚ) : ℝ) :=
    div_nonneg (sq_nonneg _) hB.le
  have := hstrict p hp hdeg
  linarith

/-- **with L*, the border term is the Schur condition** (finite
algebra, PROVED): L† implies the terminal statement.  The reviewer's
route through the `H⁻¹u` minimizer is replaced by the determinant
extraction: L† gives the master cap (`iff_masterCap`), then
`B > 0` is the budget corner (`budget_pos_of_augmented`) and
`q < 1` is the positive Schur margin `D_cap = det A_cap / det H_cap
> 0` (`D_pos_of_augmented` + `q_lt_one_of_pos`) -- the Schur condition
`uᵀH⁻¹u < B` in determinant coordinates (`D_eq_schur`), no explicit
minimizer evaluation needed. -/
theorem augmentedSubordination_implies_terminal (w : VonMangoldtWindow)
    (h : AugmentedSubordination w) : TerminalPositive w := by
  have hAcap := (augmentedSubordination_iff_masterCap w).mp h w.cap le_rfl
  have hB := w.budget_pos_of_augmented hAcap
  exact ⟨hB, w.q_lt_one_of_pos hB
    (w.D_pos_of_augmented hAcap (w.hankel_posDef_of_augmented hAcap))⟩

/-- **L† ⟺ L* ∧ Terminal** (r332, the reviewer unification,
sorry-free).  Forward: the two extractions above.  Backward: the
wave-10 reconstruction chain re-run against its own bricks
(`lstar_implies_hankel_posDef`, `terminal_margin_pos_of_terminal`,
`posDef_fromBlocks_border`, principal restriction) -- deliberately
NOT consuming `lstar_terminal_implies_master`, so the corollary
relation `reconstruction_via_augmented` below is non-circular.  NO RH
CLAIM. -/
theorem augmentedSubordination_iff_lstar_and_terminal
    (w : VonMangoldtWindow) :
    AugmentedSubordination w ↔ LStar w ∧ TerminalPositive w := by
  constructor
  · intro h
    exact ⟨augmentedSubordination_implies_lstar w h,
      augmentedSubordination_implies_terminal w h⟩
  · rintro ⟨hL, hT⟩
    refine (augmentedSubordination_iff_masterCap w).mpr fun n hn => ?_
    have hH : (w.hankel w.cap).PosDef := by
      rcases Nat.eq_zero_or_pos w.cap with h0 | hpos
      · rw [h0]
        exact posDef_of_isEmpty _
      · exact lstar_implies_hankel_posDef w hL w.cap le_rfl hpos
    have hD : 0 < w.D w.cap := terminal_margin_pos_of_terminal w hT
    have hdetA : 0 < (w.A w.cap).det := by
      have hdh : 0 < (w.hankel w.cap).det := hH.det_pos
      have hsplit : (w.A w.cap).det
          = w.D w.cap * (w.hankel w.cap).det := by
        rw [VonMangoldtWindow.D, div_mul_cancel₀ _ hdh.ne']
      rw [hsplit]
      exact mul_pos hD hdh
    have hAeq : w.A w.cap = Matrix.fromBlocks (w.hankel w.cap)
        (fun i (_ : Unit) => w.borderVec w.cap i)
        (fun (_ : Unit) k => w.borderVec w.cap k)
        (fun _ _ => ((w.B : ℚ) : ℝ)) := rfl
    have hAcap : (w.A w.cap).PosDef := by
      rw [hAeq]
      exact posDef_fromBlocks_border hH (by rw [← hAeq]; exact hdetA)
    rw [A_eq_submatrix_A_cap w hn]
    exact posDef_submatrix_of_injective hAcap
      ((Fin.castLE_injective hn).sumMap Function.injective_id)

/-! ## The corollary relation to the reconstruction theorem -/

/-- **the r305 reconstruction theorem as a corollary** (r332,
documentation demand): the exact statement of
`lstar_terminal_implies_master` (RH/Closure.lean -- byte-stable, NOT
replaced) re-derived as `iff_masterCap.mp ∘ iff_lstar_and_terminal.mpr`
without referencing the original: L† is the quadratic-completion
packaging of the same finite algebra. -/
theorem reconstruction_via_augmented (w : VonMangoldtWindow)
    (hL : LStar w) (hTerminal : TerminalPositive w) :
    ∀ n ≤ w.cap, (w.A n).PosDef :=
  (augmentedSubordination_iff_masterCap w).mp
    ((augmentedSubordination_iff_lstar_and_terminal w).mpr
      ⟨hL, hTerminal⟩)

/-! ## L† on the final domain: the combined target form -- C1 MOVE

`augmentedSubordination_main` (the combined target form -- L† holds,
PROVED from the two true holes through the equivalence above,
deliberately NOT a new `sorry`) and `augmented_prefix_positive_via_
ldagger` (the master theorem through the L† route) moved to
RH/Canonical.lean with the C1 domain retype: they are now conditioned
on the constructive `CanonicalWindow` predicate and consume the
canonical holes `lstar_canonical` + `terminal_canonical` -- statements
verbatim modulo the domain, proofs verbatim through the two
equivalences of this file.  This file stays sorry-free and
`MainWindow`-free. -/

end RH
