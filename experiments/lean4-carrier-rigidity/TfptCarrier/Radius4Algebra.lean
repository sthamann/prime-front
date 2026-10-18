/-
  Radius4Algebra — the radius-4 arc's field algebra, kernel-checked.
  ==================================================================

  Lean seam of round 117 (PRIME.RADIUS4.DETERMINANT.LIMIT.01; note
  CDXVII, contract PRIME.RADIUS4.LEAN.01): the pure field algebra of
  the radius-4 reduction, matching the sympy-exact gates of
  `experiments/tfpt-discovery/radius4_reduction_probe.py`
  (R1i-w-range, R1i-diagonal-identity, R1ii-matched-w,
  R1ii-weight-sum, R1iv-determinant-circle, R1vi-residue-rigidity).

  The objects: the weight `y a z = a/(a-z)` and the rate
  `w a z = -a z/(a-z)^2` of one zero-image z at the anchor a, with
  `w = y (1-y)`.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `w_eq_y_one_sub_y` — the Loewner-form factorization
        w = y(1-y); `diagonal_identity` — the per-zero diagonal
        summand collapse y^{m+1}(1-y)^m = y·(y(1-y))^m (probe gate
        R1i-diagonal-identity, here for EVERY m, not m ≤ 4).

    (2) `det_factor` — the determinant geometry (probe gate
        R1iv-determinant-circle): with Vieta data z₊+z₋ = a(2-t) and
        z₊z₋ = a², one has (z-z₊)(z-z₋) = (z-a)²(1 - t·w a z) as an
        exact field identity.

    (3) `wOnLine_nonneg` / `wOnLine_le_quarter` — THE ON-LINE BOUND
        (probe gate R1i-w-range): 0 ≤ w_a(-γ²) = aγ²/(a+γ²)² ≤ 1/4,
        via the exact square (a-γ²)² ≥ 0; `w_onLine_eq` — the complex
        w at z = -γ² IS that real value.

    (4) `matched_w` / `matched_excess_pos` — THE OFF-LINE STRICT
        VIOLATION (probe gate R1ii-matched-w): at the matched pin
        a₀ = δ²+γ² and z₀ = (δ+iγ)², the rate w_{a₀}(z₀) is EXACTLY
        REAL, equal to (δ²+γ²)/(4γ²) = (1/4)(1+δ²/γ²), and strictly
        exceeds 1/4 whenever δ ≠ 0 — off-line existence is a RATE
        violation with no sign channel.

    (5) `partner_w` / `partner_weight_sum` — THE 2-TO-1 RESIDUE
        RIGIDITY (probe gate R1vi-residue-rigidity): the map
        z ↦ w a z is 2-to-1 with partner a²/z, w(a²/z) = w(z), and
        the weights of same-w partners sum EXACTLY to one:
        y(z) + y(a²/z) = 1.  At the matched pin the partner is z̄, so
        (4) is this duality on the circle |z| = a.

  THE HONEST BOUNDARY.  Everything here is FIELD ALGEBRA over ℝ/ℂ:
  no ζ, no zero of any L-function, no limit, no operator enters.  The
  identification of z with squared zero-ordinates of ξ_Q or ξ, the
  assembly into determinants D_a(t), the Cauchy–Hadamard read of
  limsup |d_m|^{1/m}, and every convergence statement remain the
  probe's measured/classical content and are NOT formalized.  No RH
  claim in any direction.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace TfptCarrier
namespace Radius4Algebra

open Complex

/-! ### The weight and the rate -/

/-- The weight of a zero-image z at the anchor a: `y = a/(a-z)`
(the residue coefficient of the diagonal generating function). -/
noncomputable def y (a z : ℂ) : ℂ := a / (a - z)

/-- The rate of a zero-image z at the anchor a:
`w = -a z/(a-z)²` — the radius-4 contraction datum. -/
noncomputable def w (a z : ℂ) : ℂ := -a * z / (a - z) ^ 2

/-- **Loewner factorization**: `w = y(1-y)` wherever both are
defined (a ≠ z). -/
theorem w_eq_y_one_sub_y {a z : ℂ} (h : a ≠ z) :
    w a z = y a z * (1 - y a z) := by
  have h' : a - z ≠ 0 := sub_ne_zero.mpr h
  unfold w y
  field_simp
  ring

/-- **The diagonal summand collapse** (probe gate
R1i-diagonal-identity, all m): `y^{m+1}(1-y)^m = y·(y(1-y))^m` — the
m-th diagonal cell of one zero is exactly `y·w^m`. -/
theorem diagonal_identity (u : ℂ) (m : ℕ) :
    u ^ (m + 1) * (1 - u) ^ m = u * (u * (1 - u)) ^ m := by
  rw [mul_pow, pow_succ]
  ring

/-! ### (2) Determinant geometry -/

/-- **The determinant factor** (probe gate R1iv-determinant-circle):
with the Vieta data z₊ + z₋ = a(2-t), z₊z₋ = a², each zero-image z
contributes the exact factor `(z-z₊)(z-z₋) = (z-a)²(1 - t·w a z)`. -/
theorem det_factor {a t z zp zm : ℂ} (hsum : zp + zm = a * (2 - t))
    (hprod : zp * zm = a ^ 2) (hz : z ≠ a) :
    (z - zp) * (z - zm) = (z - a) ^ 2 * (1 - t * w a z) := by
  have h : a - z ≠ 0 := sub_ne_zero.mpr fun h' => hz h'.symm
  have hw : (z - a) ^ 2 * w a z = -a * z := by
    have hsq : (z - a) ^ 2 = (a - z) ^ 2 := by ring
    unfold w
    rw [hsq, mul_div_assoc']
    field_simp
  calc (z - zp) * (z - zm)
      = z ^ 2 - (zp + zm) * z + zp * zm := by ring
    _ = z ^ 2 - a * (2 - t) * z + a ^ 2 := by rw [hsum, hprod]
    _ = (z - a) ^ 2 - t * ((z - a) ^ 2 * w a z) := by rw [hw]; ring
    _ = (z - a) ^ 2 * (1 - t * w a z) := by ring

/-! ### (3) The on-line bound -/

/-- The on-line rate in real currency:
`wOnLine a γ = aγ²/(a+γ²)²` — the value of `w a (-γ²)`. -/
noncomputable def wOnLine (a g : ℝ) : ℝ := a * g ^ 2 / (a + g ^ 2) ^ 2

/-- The on-line rate is nonnegative. -/
theorem wOnLine_nonneg {a : ℝ} (ha : 0 < a) (g : ℝ) :
    0 ≤ wOnLine a g := by
  unfold wOnLine
  positivity

/-- **THE ON-LINE QUARTER BOUND** (probe gate R1i-w-range):
`wOnLine a γ ≤ 1/4`, exactly because
`1/4 - aγ²/(a+γ²)² = (a-γ²)²/(4(a+γ²)²) ≥ 0`. -/
theorem wOnLine_le_quarter {a : ℝ} (ha : 0 < a) (g : ℝ) :
    wOnLine a g ≤ 1 / 4 := by
  have hden : (a + g ^ 2) ≠ 0 := by positivity
  have key : 1 / 4 - wOnLine a g
      = (a - g ^ 2) ^ 2 / (4 * (a + g ^ 2) ^ 2) := by
    unfold wOnLine
    field_simp
    ring
  have h2 : 0 ≤ (a - g ^ 2) ^ 2 / (4 * (a + g ^ 2) ^ 2) :=
    div_nonneg (sq_nonneg _) (by positivity)
  linarith

/-- The complex rate at the on-line image z = -γ² IS the real
on-line rate: `w a (-γ²) = aγ²/(a+γ²)²`. -/
theorem w_onLine_eq {a : ℝ} (ha : 0 < a) (g : ℝ) :
    w (a : ℂ) (-(g : ℂ) ^ 2) = ((wOnLine a g : ℝ) : ℂ) := by
  have hpos : (0 : ℝ) < a + g ^ 2 := by positivity
  have h : (a : ℂ) + (g : ℂ) ^ 2 ≠ 0 := by
    have : ((a + g ^ 2 : ℝ) : ℂ) ≠ 0 := by
      exact_mod_cast hpos.ne'
    push_cast at this
    exact this
  unfold w wOnLine
  rw [sub_neg_eq_add]
  push_cast
  field_simp

/-! ### (4) The off-line matched-pin violation -/

/-- **THE MATCHED-PIN RATE IS EXACTLY REAL** (probe gate
R1ii-matched-w): at a₀ = δ²+γ² and z₀ = (δ+iγ)²,
`w_{a₀}(z₀) = (δ²+γ²)/(4γ²)` — a real number, with no imaginary
part to hide behind. -/
theorem matched_w (d g : ℝ) (hg : g ≠ 0) :
    w ((d ^ 2 + g ^ 2 : ℝ) : ℂ) (((d : ℂ) + (g : ℂ) * I) ^ 2)
      = (((d ^ 2 + g ^ 2) / (4 * g ^ 2) : ℝ) : ℂ) := by
  have hg' : (g : ℂ) ≠ 0 := by exact_mod_cast hg
  have hgd : (g : ℂ) - (d : ℂ) * I ≠ 0 := by
    intro h
    apply hg
    have hre := congrArg Complex.re h
    simpa using hre
  have hsub : ((d ^ 2 + g ^ 2 : ℝ) : ℂ) - ((d : ℂ) + (g : ℂ) * I) ^ 2
      = 2 * (g : ℂ) * ((g : ℂ) - (d : ℂ) * I) := by
    push_cast
    linear_combination (-(g : ℂ) ^ 2) * Complex.I_sq
  have hz0 : ((d : ℂ) + (g : ℂ) * I) ^ 2
      = -((g : ℂ) - (d : ℂ) * I) ^ 2 := by
    linear_combination ((d : ℂ) ^ 2 + (g : ℂ) ^ 2) * Complex.I_sq
  unfold w
  rw [hsub, hz0]
  push_cast
  field_simp
  ring

/-- **THE STRICT VIOLATION** (round 117 §3.2): for δ ≠ 0 the matched
rate exceeds the on-line ceiling by exactly the excess δ²/(4γ²):
`1/4 < (δ²+γ²)/(4γ²)`. -/
theorem matched_excess_pos {d g : ℝ} (hd : d ≠ 0) (hg : g ≠ 0) :
    1 / 4 < (d ^ 2 + g ^ 2) / (4 * g ^ 2) := by
  have hg2 : 0 < g ^ 2 :=
    lt_of_le_of_ne (sq_nonneg g) (Ne.symm (pow_ne_zero 2 hg))
  have hd2 : 0 < d ^ 2 :=
    lt_of_le_of_ne (sq_nonneg d) (Ne.symm (pow_ne_zero 2 hd))
  have key : (d ^ 2 + g ^ 2) / (4 * g ^ 2) - 1 / 4
      = d ^ 2 / (4 * g ^ 2) := by
    field_simp
    ring
  have h2 : 0 < d ^ 2 / (4 * g ^ 2) := div_pos hd2 (by linarith)
  linarith

/-! ### (5) The 2-to-1 partner rigidity -/

/-- **Rate rigidity of the partner map** (probe gate
R1vi-residue-rigidity, first half): z ↦ w a z is 2-to-1 with partner
a²/z — `w a (a²/z) = w a z`. -/
theorem partner_w {a z : ℂ} (ha : a ≠ 0) (hz : z ≠ 0) (hza : z ≠ a) :
    w a (a ^ 2 / z) = w a z := by
  have hz' : z - a ≠ 0 := sub_ne_zero.mpr hza
  have haz : a - z ≠ 0 := sub_ne_zero.mpr fun h => hza h.symm
  have h1 : a - a ^ 2 / z = a * (z - a) / z := by
    field_simp
  unfold w
  rw [h1]
  field_simp
  ring

/-- **THE PARTNER WEIGHT SUM IS EXACTLY ONE** (probe gate
R1vi-residue-rigidity, second half — the round-117 headline
identity): `y(z) + y(a²/z) = 1`.  Same-w partners carry total
residue -1/w ≠ 0; at the matched pin the partner is z̄ and this is
the "weight exactly 1" law. -/
theorem partner_weight_sum {a z : ℂ} (ha : a ≠ 0) (hz : z ≠ 0)
    (hza : z ≠ a) : y a z + y a (a ^ 2 / z) = 1 := by
  have hz' : z - a ≠ 0 := sub_ne_zero.mpr hza
  have haz : a - z ≠ 0 := sub_ne_zero.mpr fun h => hza h.symm
  have h1 : a - a ^ 2 / z = a * (z - a) / z := by
    field_simp
  unfold y
  rw [h1]
  field_simp
  ring

end Radius4Algebra
end TfptCarrier
