/-
RH/CoxeterCompletion.lean -- r617L algebraic core of
E8.COXETER.EULER.COMPLETION.01.

Polynomial identities for Φ₃₀ over ℤ[X] / ℚ[X], and the trace readout
Tr C = −1 for any square matrix with characteristic polynomial Φ₃₀.

NOT FORMALIZED (analytic corollary, recorded only as prose): the Euler
product
  ∏_p (1 − p^{−s}) Φ₃₀(p^{−s})
    = ζ(6s) ζ(10s) ζ(15s) / (ζ(2s) ζ(3s) ζ(5s) ζ(30s))
is absolutely convergent for Re s > 1/2.

The trace-free completion is zero-free and pole-free in Re s > 1/2.
The splitting into the scalar zeta channel and the Coxeter channel is
open and RH-equivalent. No RH claim.

The linear-coefficient vanishing is a property of the class
{Tr C = −1}, not of E₈.

CLAIM BOUNDARY.  NO RH CLAIM.
-/
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.RingTheory.Polynomial.Cyclotomic.Expand
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace RH

open Polynomial Matrix

set_option maxHeartbeats 800000

/-- Explicit octic: Φ₃₀(X) = X⁸ + X⁷ − X⁵ − X⁴ − X³ + X + 1.

Route: `expand 5 Φ₆ = Φ₃₀ Φ₆` with Mathlib's `cyclotomic_six` and
`cyclotomic_expand_eq_cyclotomic_mul`, then cancel Φ₆ in the integral
domain ℤ[X]. -/
theorem cyclotomic30_explicit :
    cyclotomic 30 ℤ = X ^ 8 + X ^ 7 - X ^ 5 - X ^ 4 - X ^ 3 + X + 1 := by
  apply mul_right_cancel₀ (cyclotomic_ne_zero 6 ℤ)
  rw [show 30 = 6 * 5 by rfl,
    ← cyclotomic_expand_eq_cyclotomic_mul Nat.prime_five (by decide)]
  simp [cyclotomic_six]
  ring

/-- Möbius / Euler-product polynomial identity at n = 30:
Φ₃₀(X) (1−X) (1−X⁶) (1−X¹⁰) (1−X¹⁵) = (1−X²) (1−X³) (1−X⁵) (1−X³⁰).

Equivalent (up to four sign flips `1 − X^k = −(X^k − 1)`) to the
divisor product `∏_{d∣k} Φ_d = X^k − 1` for k ∈ {1,2,3,5,6,10,15,30}. -/
theorem moebius_identity_30 :
    cyclotomic 30 ℤ * (1 - X) * (1 - X ^ 6) * (1 - X ^ 10) * (1 - X ^ 15) =
      (1 - X ^ 2) * (1 - X ^ 3) * (1 - X ^ 5) * (1 - X ^ 30) := by
  rw [cyclotomic30_explicit]
  ring

/-- Trace-free completion: the linear coefficient of (1−X) Φ₃₀ vanishes. -/
theorem completion_explicit :
    (1 - X) * cyclotomic 30 ℤ = 1 - X ^ 2 - X ^ 3 + X ^ 6 + X ^ 7 - X ^ 9 := by
  rw [cyclotomic30_explicit]
  ring

theorem completion_linear_coeff_zero :
    ((1 - X) * cyclotomic 30 ℤ).coeff 1 = 0 := by
  rw [completion_explicit]
  simp [coeff_one, coeff_X_pow]

private theorem totient_thirty : Nat.totient 30 = 8 := by decide

private theorem cyclotomic30_coeff_seven :
    (cyclotomic 30 ℤ).coeff 7 = 1 := by
  rw [cyclotomic30_explicit]
  simp [coeff_one, coeff_X, coeff_X_pow]

/-- Any square matrix over ℚ with characteristic polynomial Φ₃₀ has
trace −1 (the class {Tr C = −1}, not an E₈-specific fact).

Degree: `charpoly_natDegree_eq_dim` plus `natDegree_cyclotomic` give
`Fintype.card n = φ(30) = 8`, so the second-highest coefficient is
the X⁷ coefficient 1 of Φ₃₀. -/
theorem trace_eq_neg_one_of_charpoly_cyclotomic30
    {n : Type*} [Fintype n] [DecidableEq n] (C : Matrix n n ℚ)
    (h : C.charpoly = cyclotomic 30 ℚ) : C.trace = -1 := by
  have hdim : Fintype.card n = 8 := by
    have hnd := charpoly_natDegree_eq_dim C
    rw [h, natDegree_cyclotomic, totient_thirty] at hnd
    exact hnd.symm
  haveI : Nonempty n := Fintype.card_pos_iff.mp (by rw [hdim]; decide)
  rw [trace_eq_neg_charpoly_coeff, h, hdim]
  have hcoeff : (cyclotomic 30 ℚ).coeff 7 = 1 := by
    rw [← map_cyclotomic_int 30 ℚ, coeff_map, cyclotomic30_coeff_seven]
    simp
  norm_num [hcoeff]

end RH
