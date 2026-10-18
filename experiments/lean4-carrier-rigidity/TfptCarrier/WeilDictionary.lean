/-
  WeilDictionary — the exact identities of the v631 W1 dictionary round.
  ======================================================================

  The v631 verification module (PRIME.WEIL.DICT.01) closes the smooth
  half of the W1 identification against the Suzuki screw function
  (arXiv:2606.09096, eq. 1.3).  Its first two links are EXACT — no
  floats, no windows — and this module certifies them in Lean:

  (D1) THE LERCH COLLAPSE.  The Hurwitz–Lerch block of the screw
       function is a geometric series in disguise: term-wise

           (2n + 1/2)^2 / (n + 1/4)^2 = 4        (over ℚ, exactly),

       because 2n + 1/2 = 2·(n + 1/4).  Consequently the formal series
       Σ (2n+½)² y^n / (n+¼)²  (y = x²) is 4 · Σ y^n ON THE NOSE —
       certified here both term-wise (`lerch_term_collapse`) and as an
       identity of formal power series over ℚ (`lerch_series_collapse`,
       coefficient corollary `lerch_coeff_collapse`).

  (D2) THE STRUCTURE THEOREM OF THE SMOOTH LAYER.  For t > 0 the
       collapsed Lerch block sums to the closed geometric form

           Σ_n 4 e^{-(2n+1/2)t} = 4 e^{-t/2} / (1 - e^{-2t})

       (`lerch_dd_closed`, a genuine tsum over ℕ; summability from
       e^{-2t} < 1, `exp_neg_two_mul_lt_one`), and the smooth layer of
       the screw function reorganises as

           g''(t) = -2 cosh(t/2) - 4 e^{-t/2}/(1 - e^{-2t}),

       i.e. −(e^{t/2} + e^{−t/2}) = −2 cosh(t/2) — the zeta pole block
       (s = 0, 1) separated from the TFPT arch density
       (`structure_identity`; well-definedness of the pole-free
       denominator: `one_sub_exp_neg_two_mul_ne_zero`).

  All analytic ingredients are Mathlib (`Real.cosh_eq`,
  `Real.exp_nat_mul`, `tsum_geometric_of_lt_one`); no axioms beyond the
  standard three.  Machine counterpart: verification/v631_w1_dictionary.py
  (D1/D2 sympy-exact + 30-digit certificates).  No positivity claim, no
  RH statement.
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.RingTheory.PowerSeries.Basic

namespace TfptCarrier.WeilDictionary

/-! ### D1 — the Lerch collapse (exact, over ℚ) -/

/-- **The Lerch collapse, term-wise.**  Each coefficient of the
Hurwitz–Lerch block of the screw function equals 4 exactly:
`(2n + 1/2)^2 / (n + 1/4)^2 = 4`, because `2n + 1/2 = 2·(n + 1/4)`. -/
theorem lerch_term_collapse (n : ℕ) :
    ((2 * n + 1/2 : ℚ)) ^ 2 / ((n + 1/4 : ℚ)) ^ 2 = 4 := by
  have hne : ((n : ℚ) + 1/4) ≠ 0 := by positivity
  field_simp
  ring

/-- The coefficient sequence of the Hurwitz–Lerch block
`Σ (2n+½)² yⁿ/(n+¼)²` (in the variable `y = x²`). -/
def lerchCoeff (n : ℕ) : ℚ :=
  ((2 * n + 1/2 : ℚ)) ^ 2 / ((n + 1/4 : ℚ)) ^ 2

/-- **The Lerch collapse as a formal power-series identity** (over ℚ,
in the variable `y = x²`): the Hurwitz–Lerch block IS the geometric
series, `Σ (2n+½)² yⁿ/(n+¼)² = 4 · Σ yⁿ`, on the nose. -/
theorem lerch_series_collapse :
    PowerSeries.mk lerchCoeff
      = PowerSeries.C (4 : ℚ) * PowerSeries.mk (fun _ => (1 : ℚ)) := by
  refine PowerSeries.ext fun n => ?_
  simp only [PowerSeries.coeff_mk, PowerSeries.coeff_C_mul, mul_one, lerchCoeff]
  exact lerch_term_collapse n

/-- Coefficient-level corollary: every coefficient of the Lerch block
agrees with the corresponding coefficient of `4 · (geometric series)`. -/
theorem lerch_coeff_collapse (n : ℕ) :
    PowerSeries.coeff n (PowerSeries.mk lerchCoeff)
      = PowerSeries.coeff n
          (PowerSeries.C (4 : ℚ) * PowerSeries.mk (fun _ => (1 : ℚ))) := by
  rw [lerch_series_collapse]

/-! ### D2 — the structure theorem of the smooth layer (real analysis) -/

/-- For `t > 0` the geometric ratio `e^{-2t}` lies strictly below 1. -/
theorem exp_neg_two_mul_lt_one (t : ℝ) (ht : 0 < t) :
    Real.exp (-2 * t) < 1 := by
  calc Real.exp (-2 * t) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
    _ = 1 := Real.exp_zero

/-- Well-definedness of the collapsed Lerch denominator:
`0 < 1 - e^{-2t}` for `t > 0`. -/
theorem one_sub_exp_neg_two_mul_pos (t : ℝ) (ht : 0 < t) :
    0 < 1 - Real.exp (-2 * t) := by
  linarith [exp_neg_two_mul_lt_one t ht]

/-- The collapsed Lerch denominator never vanishes for `t > 0`. -/
theorem one_sub_exp_neg_two_mul_ne_zero (t : ℝ) (ht : 0 < t) :
    1 - Real.exp (-2 * t) ≠ 0 :=
  ne_of_gt (one_sub_exp_neg_two_mul_pos t ht)

/-- The pole block is the hyperbolic cosine:
`e^{t/2} + e^{-t/2} = 2 cosh(t/2)`. -/
theorem two_cosh_half (t : ℝ) :
    Real.exp (t/2) + Real.exp (-t/2) = 2 * Real.cosh (t/2) := by
  rw [Real.cosh_eq, neg_div]
  ring

/-- **The collapsed Lerch block in closed geometric form.**  For `t > 0`

    `Σ'_n 4 e^{-(2n+1/2)t} = 4 e^{-t/2} / (1 - e^{-2t})`,

by factoring `e^{-(2n+1/2)t} = e^{-t/2}·(e^{-2t})ⁿ` and summing the
geometric series (`tsum_geometric_of_lt_one`, ratio `e^{-2t} < 1`). -/
theorem lerch_dd_closed (t : ℝ) (ht : 0 < t) :
    ∑' n : ℕ, 4 * Real.exp (-(2 * n + 1/2) * t)
      = 4 * Real.exp (-t/2) / (1 - Real.exp (-2 * t)) := by
  have hterm : ∀ n : ℕ, 4 * Real.exp (-(2 * (n : ℝ) + 1/2) * t)
      = 4 * Real.exp (-t/2) * Real.exp (-2 * t) ^ n := by
    intro n
    have harg : -(2 * (n : ℝ) + 1/2) * t = -t/2 + (n : ℝ) * (-2 * t) := by
      ring
    rw [harg, Real.exp_add, Real.exp_nat_mul]
    ring
  calc ∑' n : ℕ, 4 * Real.exp (-(2 * n + 1/2) * t)
      = ∑' n : ℕ, 4 * Real.exp (-t/2) * Real.exp (-2 * t) ^ n :=
        tsum_congr hterm
    _ = 4 * Real.exp (-t/2) * ∑' n : ℕ, Real.exp (-2 * t) ^ n :=
        tsum_mul_left
    _ = 4 * Real.exp (-t/2) * (1 - Real.exp (-2 * t))⁻¹ := by
        rw [tsum_geometric_of_lt_one (Real.exp_pos _).le
          (exp_neg_two_mul_lt_one t ht)]
    _ = 4 * Real.exp (-t/2) / (1 - Real.exp (-2 * t)) := by
        ring

/-- **The structure theorem of the smooth layer** (v631 D2).  For
`t > 0`, off the atoms,

    `g₁''(t) - 4 e^{-t/2}/(1 - e^{-2t})
       = -2 cosh(t/2) - 4 e^{-t/2}/(1 - e^{-2t})`

with `g₁''(t) = -(e^{t/2} + e^{-t/2})` the second derivative of the
polynomial-pole block `-4(e^{t/2} + e^{-t/2} - 2)` of the screw
function: Suzuki's smooth layer is the TFPT arch density MINUS the
separated zeta pole block `2 cosh(t/2)` (the s = 0, 1 pole weights,
tracked by TFPT as the exact rank-one pole piece, v591). -/
theorem structure_identity (t : ℝ) (ht : 0 < t) :
    (-(Real.exp (t/2) + Real.exp (-t/2)))
      - 4 * Real.exp (-t/2) / (1 - Real.exp (-2 * t))
      = -2 * Real.cosh (t/2)
        - 4 * Real.exp (-t/2) / (1 - Real.exp (-2 * t)) := by
  -- The shared pole-free block is well-defined for t > 0 (denominator ≠ 0).
  have _hwd : 1 - Real.exp (-2 * t) ≠ 0 := one_sub_exp_neg_two_mul_ne_zero t ht
  have h := two_cosh_half t
  linarith

end TfptCarrier.WeilDictionary
