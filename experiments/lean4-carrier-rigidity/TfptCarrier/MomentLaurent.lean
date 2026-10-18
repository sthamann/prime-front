/-
  MomentLaurent — the round-156 moment-Laurent law, kernel-checked.
  =================================================================

  Lean seam of round 156 (PRIME.ROOT.LADDER.01; contract
  PRIME.THEOREMS.LEAN2.01, second hardening round): the exact
  finite-lattice halves of THEOREMS L1/L2 of
  `experiments/tfpt-discovery/rootladder_probe.py` (with the r154 P2
  jet recursion of `nearalign_probe.py` as the first display).

  The objects, on a FINITE lattice b : ι → ℝ with weights v = w/A₀:
  the secular profile S(y) = Σ v_k/(y − b_k) (so F/A₀ = 1 + S), the
  one-jet-up profile T(y) = Σ v_k b_k/(y − b_k), the normalized jets
  jet m = a_{2(m+1)} = Σ v_k b_k^m (jet 0 = a₂ = −y_t), the moment
  ratios J_{m+2} = a_{2(m+2)}/y_t^{m+2}, and the finite Laurent
  profile Φ_M(z) = z − 1 + Σ_{m<M} J_{m+2}/z^{m+1}.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `y_mul_S` — THE JET RECURSION (r154 P2 / r156 L1 base):
        y·S(y) = a₂ + T(y) exactly (partial fractions).

    (2) `secular_dictionary` — THE FIRST L1 DISPLAY: with
        a₂ = −y_t, (y/y_t)·F(y)/A₀ = z − 1 + T(y)/y_t at z = y/y_t.

    (3) `geom_remainder` / `T_laurent` — THE SECOND L1 DISPLAY,
        finite-exact: T(y) = Σ_{m<M} a_{2(m+2)}/y^{m+1} + R_M(y)
        with the EXACT partial-geometric remainder
        R_M(y) = Σ_k v_k b_k^{M+1}/(y^M(y − b_k)) — no limit taken.

    (4) `moment_laurent_law` — THE MOMENT-LAURENT LAW (L1
        assembled): (y/y_t)·F(y)/A₀ = Φ_M(z) + R_M(y)/y_t exactly —
        above the band the escaped-root ladder is an algebraic
        function of the moment ratios alone, up to the explicit
        remainder.

    (5) `z_mul_one_sub_z_le_quarter` — THE QUARTER CAP (L2):
        z(1−z) ≤ 1/4 for every real z, exactly.

    (6) `quarter_cap_algebra` / `quarter_cap_bound` — THE L2
        TOP-ROOT CAP SKELETON: if Φ_{M+1}(z₀) = 0 then
        J₂ = z₀(1−z₀) − z₀·ρ_M(z₀) with ρ_M the explicit finite
        tail, hence J₂ ≤ 1/4 + |z₀·ρ_M(z₀)| — the census-real top
        root caps its own leading moment ratio up to the named
        tail term.

  THE HONEST BOUNDARY.  All identities are finite-sum real field
  algebra with EXPLICIT remainders: the M → ∞ Laurent convergence
  on y > b_top, the identification of (v, b) with the frozen
  anchor-block ground data, the census-root/ladder measurements, the
  tail-size estimates (z·|ρ| ≈ 0.003…0.009 measured) and TOPROOT
  demands remain the probe's content and are NOT formalized.  No RH
  claim in any direction.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace TfptCarrier
namespace MomentLaurent

open Finset

variable {ι : Type*} [Fintype ι]
variable {v b : ι → ℝ} {y yt : ℝ}

/-- The secular profile `S(y) = Σ v_k/(y − b_k)` — so F/A₀ = 1 + S. -/
noncomputable def S (v b : ι → ℝ) (y : ℝ) : ℝ := ∑ k, v k / (y - b k)

/-- The one-jet-up profile `T(y) = Σ v_k b_k/(y − b_k)`. -/
noncomputable def T (v b : ι → ℝ) (y : ℝ) : ℝ :=
  ∑ k, v k * b k / (y - b k)

/-- The normalized jets: `jet m = a_{2(m+1)} = Σ v_k b_k^m`
(jet 0 = a₂). -/
def jet (v b : ι → ℝ) (m : ℕ) : ℝ := ∑ k, v k * b k ^ m

/-- **THE JET RECURSION** (r154 P2 / r156 L1 base):
`y·S(y) = a₂ + T(y)` exactly — partial fractions, per term. -/
theorem y_mul_S (hy : ∀ k, y ≠ b k) :
    y * S v b y = jet v b 0 + T v b y := by
  rw [S, T, jet, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun k _ => ?_
  have h : y - b k ≠ 0 := sub_ne_zero.mpr (hy k)
  rw [pow_zero, mul_one]
  field_simp
  ring

/-- **THE FIRST L1 DISPLAY** (the secular-Laurent dictionary): with
`a₂ = −y_t`, exactly `(y/y_t)·(1 + S(y)) = z − 1 + T(y)/y_t` at
z = y/y_t — the profile F/A₀ in ladder currency. -/
theorem secular_dictionary (hy : ∀ k, y ≠ b k) (hyt : yt ≠ 0)
    (ha2 : jet v b 0 = -yt) :
    y / yt * (1 + S v b y) = y / yt - 1 + T v b y / yt := by
  have h := y_mul_S (v := v) (b := b) hy
  rw [ha2] at h
  have hT : T v b y = y * S v b y + yt := by linarith
  rw [hT]
  field_simp
  ring

/-- The scalar finite-geometric split with EXACT remainder:
`b/(y−b) = Σ_{m<M} b^{m+1}/y^{m+1} + b^{M+1}/(y^M(y−b))`. -/
theorem geom_remainder {y c : ℝ} (hy : y ≠ 0) (hc : y ≠ c) (M : ℕ) :
    c / (y - c)
      = (∑ m ∈ Finset.range M, c ^ (m + 1) / y ^ (m + 1))
        + c ^ (M + 1) / (y ^ M * (y - c)) := by
  induction M with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    have h1 : y - c ≠ 0 := sub_ne_zero.mpr hc
    have h2 : y ^ n ≠ 0 := pow_ne_zero _ hy
    field_simp
    ring

/-- **THE SECOND L1 DISPLAY** (finite Laurent with exact remainder):
`T(y) = Σ_{m<M} a_{2(m+2)}/y^{m+1} + Σ_k v_k b_k^{M+1}/(y^M(y−b_k))`
— the one-jet-up profile IS the moment data, up to the explicit
partial-geometric remainder. -/
theorem T_laurent (hy0 : y ≠ 0) (hy : ∀ k, y ≠ b k) (M : ℕ) :
    T v b y
      = (∑ m ∈ Finset.range M, jet v b (m + 1) / y ^ (m + 1))
        + ∑ k, v k * b k ^ (M + 1) / (y ^ M * (y - b k)) := by
  have hk : ∀ k, v k * b k / (y - b k)
      = (∑ m ∈ Finset.range M, v k * b k ^ (m + 1) / y ^ (m + 1))
        + v k * b k ^ (M + 1) / (y ^ M * (y - b k)) := by
    intro k
    have h := geom_remainder hy0 (hy k) M
    calc v k * b k / (y - b k)
        = v k * (b k / (y - b k)) := mul_div_assoc _ _ _
      _ = v k * ((∑ m ∈ Finset.range M, b k ^ (m + 1) / y ^ (m + 1))
            + b k ^ (M + 1) / (y ^ M * (y - b k))) := by rw [h]
      _ = _ := by
          rw [mul_add, Finset.mul_sum]
          simp only [mul_div_assoc]
  calc T v b y
      = ∑ k, ((∑ m ∈ Finset.range M, v k * b k ^ (m + 1) / y ^ (m + 1))
          + v k * b k ^ (M + 1) / (y ^ M * (y - b k))) :=
        Finset.sum_congr rfl fun k _ => hk k
    _ = (∑ k, ∑ m ∈ Finset.range M, v k * b k ^ (m + 1) / y ^ (m + 1))
          + ∑ k, v k * b k ^ (M + 1) / (y ^ M * (y - b k)) :=
        Finset.sum_add_distrib
    _ = (∑ m ∈ Finset.range M, ∑ k, v k * b k ^ (m + 1) / y ^ (m + 1))
          + ∑ k, v k * b k ^ (M + 1) / (y ^ M * (y - b k)) := by
        rw [Finset.sum_comm]
    _ = (∑ m ∈ Finset.range M, jet v b (m + 1) / y ^ (m + 1))
          + ∑ k, v k * b k ^ (M + 1) / (y ^ M * (y - b k)) := by
        refine congrArg (· + _) (Finset.sum_congr rfl fun m _ => ?_)
        rw [jet, Finset.sum_div]

/-- The moment ratios `J_{m+2} = a_{2(m+2)}/y_t^{m+2}` (so `Jmom 0`
is the leading ratio J₂). -/
noncomputable def Jmom (v b : ι → ℝ) (yt : ℝ) (m : ℕ) : ℝ :=
  jet v b (m + 1) / yt ^ (m + 2)

/-- The finite moment-Laurent profile
`Φ_M(z) = z − 1 + Σ_{m<M} J_{m+2}/z^{m+1}`. -/
noncomputable def Phi (v b : ι → ℝ) (yt : ℝ) (M : ℕ) (z : ℝ) : ℝ :=
  z - 1 + ∑ m ∈ Finset.range M, Jmom v b yt m / z ^ (m + 1)

/-- **THE MOMENT-LAURENT LAW** (r156 L1 assembled, finite-exact):
`(y/y_t)·F(y)/A₀ = Φ_M(y/y_t) + R_M(y)/y_t` with the explicit
remainder `R_M(y) = Σ_k v_k b_k^{M+1}/(y^M(y−b_k))` — the secular
profile above the band is the moment-ratio profile Φ, exactly, up
to the named finite-geometric remainder. -/
theorem moment_laurent_law (hy0 : y ≠ 0) (hy : ∀ k, y ≠ b k)
    (hyt : yt ≠ 0) (ha2 : jet v b 0 = -yt) (M : ℕ) :
    y / yt * (1 + S v b y)
      = Phi v b yt M (y / yt)
        + (∑ k, v k * b k ^ (M + 1) / (y ^ M * (y - b k))) / yt := by
  rw [secular_dictionary hy hyt ha2, T_laurent hy0 hy M, Phi]
  rw [add_div, Finset.sum_div]
  have hterm : ∀ m ∈ Finset.range M,
      jet v b (m + 1) / y ^ (m + 1) / yt
        = Jmom v b yt m / (y / yt) ^ (m + 1) := by
    intro m _
    rw [Jmom, div_pow]
    have hyp : y ^ (m + 1) ≠ 0 := pow_ne_zero _ hy0
    have hytp : yt ^ (m + 1) ≠ 0 := pow_ne_zero _ hyt
    have hytp2 : yt ^ (m + 2) ≠ 0 := pow_ne_zero _ hyt
    field_simp
    ring
  rw [Finset.sum_congr rfl hterm]
  ring

/-! ### The L2 quarter cap -/

/-- **THE QUARTER CAP** (r156 L2, first half): `z(1−z) ≤ 1/4` for
every real z, exactly — because 1/4 − z(1−z) = (z − 1/2)². -/
theorem z_mul_one_sub_z_le_quarter (z : ℝ) : z * (1 - z) ≤ 1 / 4 := by
  nlinarith [sq_nonneg (z - 1 / 2)]

/-- **THE L2 CAP ALGEBRA** (the top-root skeleton): if the finite
profile has the real root Φ_{M+1}(z₀) = 0 then the leading moment
ratio is EXACTLY `J₂ = z₀(1−z₀) − z₀·ρ_M(z₀)` with the explicit
finite tail `ρ_M(z) = Σ_{m<M} J_{m+3}/z^{m+2}`. -/
theorem quarter_cap_algebra {z0 : ℝ} (hz0 : z0 ≠ 0) (M : ℕ)
    (hroot : Phi v b yt (M + 1) z0 = 0) :
    Jmom v b yt 0
      = z0 * (1 - z0)
        - z0 * ∑ m ∈ Finset.range M, Jmom v b yt (m + 1) / z0 ^ (m + 2) := by
  rw [Phi, Finset.sum_range_succ'] at hroot
  have hsum : ∑ m ∈ Finset.range M, Jmom v b yt (m + 1) / z0 ^ (m + 1 + 1)
      = ∑ m ∈ Finset.range M, Jmom v b yt (m + 1) / z0 ^ (m + 2) :=
    Finset.sum_congr rfl fun m _ => rfl
  rw [hsum] at hroot
  field_simp at hroot
  linear_combination hroot

/-- **THE L2 QUARTER-CAP BOUND**: at a real root z₀ of Φ_{M+1},
`J₂ ≤ 1/4 + |z₀·ρ_M(z₀)|` — the census-real top root caps its own
leading moment ratio, up to the named finite tail. -/
theorem quarter_cap_bound {z0 : ℝ} (hz0 : z0 ≠ 0) (M : ℕ)
    (hroot : Phi v b yt (M + 1) z0 = 0) :
    Jmom v b yt 0
      ≤ 1 / 4
        + |z0 * ∑ m ∈ Finset.range M,
            Jmom v b yt (m + 1) / z0 ^ (m + 2)| := by
  have h := quarter_cap_algebra hz0 M hroot
  have h1 := z_mul_one_sub_z_le_quarter z0
  have h2 := neg_abs_le
    (z0 * ∑ m ∈ Finset.range M, Jmom v b yt (m + 1) / z0 ^ (m + 2))
  linarith

end MomentLaurent
end TfptCarrier
