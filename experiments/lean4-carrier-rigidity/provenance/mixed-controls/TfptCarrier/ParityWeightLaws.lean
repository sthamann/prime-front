/-
  TFPT Carrier — Parity Weight Laws (the v587/v590/v591 exact cores)
  ------------------------------------------------------------------

  Machine-checked algebraic cores of the 2026-08-01 backflow round:

  1. `branch_merge` — the piecewise structure of the diagonal lag
     weight cancels: the autocorrelation branch (d < m) and the
     reflection-convolution branch assemble to the SAME single
     closed expression (v587, PRIME.WCLOSED.01).  Stated as the
     linear-in-trig-values field identity that carries the proof.

  2. `pole_rank_one` / `pole_null_vector` — the pole (exponential)
     part of the deterministic model is an exactly separable
     rank-one matrix: its 2x2 determinant vanishes identically and
     `(g2, -g1)` is a null vector (v591, PRIME.POLERANKONE.01).

  3. `direction_law` / `direction_law_approach` — the locking
     direction of the rank-one pole term obeys
     v2/v1 = -(a^2 + 16 p)/(2 (a^2 + 4 p))  (p = pi^2), and its
     distance from the null-ray value -1/2 is exactly
     -6 p/(a^2 + 4 p): the a -> infinity limit -1/2 (the Pythagorean
     null ray (2,-1)) is contained algebraically (v591).

  4. `S0_involution` / `S0_commutes_V` / `S0_trace` — the sheet
     involution of v590 (QGEO.INVOL.01): the explicit integer matrix
     S0 squares to 1, commutes with the sheet flow V = Q diag(0,1,1)
     of the compiler Q, and has the Sigma-signature trace -1.

  All statements are pure algebra over ℝ resp. ℤ; no analysis is
  imported.  The trig inputs of (1) enter as opaque real values, so
  the lemma is exactly the algebraic content of the branch merge.
-/

import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

namespace TFPT.Carrier.ParityWeightLaws

/-! ### 1. The branch merge of the diagonal lag weight (v587) -/

/--
With `c = cos(w d)`, `s0 = sin(w d)`, `s1 = sin(w (d+1))`,
`S = sin w ≠ 0`, the assembled weight on the autocorrelation branch,
`2 ac(d) − cv(2m−1−d)`, equals the single closed expression
`(2m − d) c + s1/S` — the same expression the reflection branch
produces, so the apparent piecewise break at `d = m` cancels.
-/
theorem branch_merge (m d c s0 s1 S : ℝ) (hS : S ≠ 0) :
    2 * ((m - d) * c + (s1 + s0) / (2 * S)) - (s0 / S - d * c)
      = (2 * m - d) * c + s1 / S := by
  field_simp
  ring

/-! ### 2. The rank-one pole term (v591) -/

/-- The pole part `S^pole = c · g gᵀ` has vanishing determinant. -/
theorem pole_rank_one (c g1 g2 : ℝ) :
    (c * g1 * g1) * (c * g2 * g2) - (c * g1 * g2) ^ 2 = 0 := by
  ring

/-- `(g2, -g1)` is a null vector of the separable matrix `c · g gᵀ`. -/
theorem pole_null_vector (c g1 g2 : ℝ) :
    (c * g1 * g1) * g2 + (c * g1 * g2) * (-g1) = 0 ∧
    (c * g1 * g2) * g2 + (c * g2 * g2) * (-g1) = 0 := by
  constructor <;> ring

/-! ### 3. The locking-direction law (v591) -/

/--
With `g1 = 1/(a² + 4p)` and `g2 = 2/(a² + 16p)` (`p = π²`), the null
direction of the rank-one pole term has slope
`v2/v1 = -g1/g2 = -(a² + 16p)/(2(a² + 4p))`.
-/
theorem direction_law (a p : ℝ) (h1 : a ^ 2 + 4 * p ≠ 0) :
    -(1 / (a ^ 2 + 4 * p)) / (2 / (a ^ 2 + 16 * p))
      = -(a ^ 2 + 16 * p) / (2 * (a ^ 2 + 4 * p)) := by
  field_simp

/--
The distance of the direction law from the null-ray value `-1/2` is
exactly `-6p/(a² + 4p)`: the `a → ∞` limit `-1/2` (the Pythagorean
null ray `(2, -1)`) is contained algebraically.
-/
theorem direction_law_approach (a p : ℝ) (h1 : a ^ 2 + 4 * p ≠ 0) :
    -(a ^ 2 + 16 * p) / (2 * (a ^ 2 + 4 * p)) + 1 / 2
      = -(6 * p) / (a ^ 2 + 4 * p) := by
  have h2 : (2 : ℝ) * (a ^ 2 + 4 * p) ≠ 0 := mul_ne_zero two_ne_zero h1
  rw [div_add_div _ _ h2 two_ne_zero, div_eq_div_iff (by
    exact mul_ne_zero h2 two_ne_zero) h1]
  ring

/-! ### 3b. The closed determinant law (v592) -/

/--
The Laplace denominators factor completely, so
`D_11 · D_22 = D_12²` (with `p = π²`).
-/
theorem det_denominators_factor (a p : ℝ) :
    (a ^ 2 + 4 * p) ^ 2 * (a ^ 2 + 16 * p) ^ 2
      = ((a ^ 2 + 4 * p) * (a ^ 2 + 16 * p)) ^ 2 := by
  ring

/--
The closed determinant law of v592: with the exact rational-exponential
entries (`p = π²`, `E = e^a` entering as an opaque value), the 2×2
determinant collapses to the closed factored form — in particular the
`E²` terms cancel identically (the rank-one cancellation) and the
determinant is one full exponential order suppressed.
-/
theorem det_S_closed (a p E : ℝ) (h1 : a ^ 2 + 4 * p ≠ 0)
    (_h2 : a ^ 2 + 16 * p ≠ 0) :
    (4 * a * (-a ^ 3 - 4 * p * a - 8 * p * E + 8 * p)
        / (a ^ 2 + 4 * p) ^ 2)
      * (4 * a * (-a ^ 3 - 16 * p * a - 32 * p * E + 32 * p)
        / (a ^ 2 + 16 * p) ^ 2)
      - (64 * p * a * (1 - E)
        / ((a ^ 2 + 4 * p) * (a ^ 2 + 16 * p))) ^ 2
      = 16 * a ^ 3 * (a ^ 5 + 20 * p * a ^ 3 + 40 * p * a ^ 2 * E
          - 40 * p * a ^ 2 + 64 * p ^ 2 * a + 256 * p ^ 2 * E
          - 256 * p ^ 2)
        / ((a ^ 2 + 4 * p) ^ 2 * (a ^ 2 + 16 * p) ^ 2) := by
  field_simp
  ring

/-! ### 4. The sheet involution (v590) -/

/-- The sheet involution selected in v590 (QGEO.INVOL.01). -/
def S0 : Matrix (Fin 3) (Fin 3) ℤ := !![1, -1, 0; 0, -1, 0; 0, 0, -1]

/-- The sheet flow `V = Q diag(0,1,1)` of the compiler `Q`. -/
def V : Matrix (Fin 3) (Fin 3) ℤ := !![0, 1, 0; 0, 2, 0; 0, 2, 1]

theorem S0_involution : S0 * S0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_three]

theorem S0_commutes_V : S0 * V = V * S0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, V, Matrix.mul_apply, Fin.sum_univ_three]

theorem S0_trace : Matrix.trace S0 = -1 := by
  simp [Matrix.trace, S0, Fin.sum_univ_three]

/-! ### 5. The involution group of v590: the concrete (ℤ/2)³ members

The integral `V`-commuting involutions found in v590 form the group
`{±1, ±A, ±B, ±S0}` with the Klein-four relation `A * B = S0`.  We
verify the two further generators and the closure relation; the
completeness of the classification (that these are ALL integral
`V`-commuting involutions) rests on the spectral-projector argument
machine-checked in `v590_involution_existence.py`.
-/

/-- The `ε = (+,+,-)` member: `+1` on the `V`-eigenspaces `{0,1}`. -/
def A : Matrix (Fin 3) (Fin 3) ℤ := !![1, -1, 0; 0, -1, 0; 0, -4, 1]

/-- The `ε = (+,-,+)` member: `+1` on the `V`-eigenspaces `{0,2}`. -/
def B : Matrix (Fin 3) (Fin 3) ℤ := !![1, 0, 0; 0, 1, 0; 0, 4, -1]

theorem A_involution : A * A = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, Matrix.mul_apply, Fin.sum_univ_three]

theorem B_involution : B * B = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, Matrix.mul_apply, Fin.sum_univ_three]

theorem A_commutes_V : A * V = V * A := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, V, Matrix.mul_apply, Fin.sum_univ_three]

theorem B_commutes_V : B * V = V * B := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, V, Matrix.mul_apply, Fin.sum_univ_three]

/-- The Klein-four closure: `A · B = S0` — the sheet involution is the
product of the two eigenspace-pair involutions. -/
theorem klein_closure : A * B = S0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, B, S0, Matrix.mul_apply, Fin.sum_univ_three]

end TFPT.Carrier.ParityWeightLaws
