/- Prime Front scoped ParityWeightLaws: original v587/v591/v592 arithmetic identities.
Original full source preserved in provenance/mixed-controls. -/
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


end TFPT.Carrier.ParityWeightLaws
