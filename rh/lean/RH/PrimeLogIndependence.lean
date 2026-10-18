/-
RH/PrimeLogIndependence.lean -- r617L Q-linear independence of {log p}.

Mathlib (v4.29.1) has no existing lemma `linearIndependent_log_primes`
(or `Real.linearIndependent_log_primes` / `Nat.Primes.linearIndependent_log`).
The statement is proved here from unique factorization of ℕ.

Corollary (words only, no extra analytic content): no finite-order
clock can realize two distinct prime lengths c·log p and c·log q as
commensurable periods.  r607 / r613 are experiments only.

CLAIM BOUNDARY.  NO RH CLAIM.
-/
import Mathlib.Algebra.Algebra.Rat
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.GroupWithZero.Action
import Mathlib.Algebra.Ring.Rat
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Nat.Cast.Field
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.NumberTheory.Real.Irrational

namespace RH

open Finset Real
open scoped Classical

/-- `n + toNat(-n) = toNat n` as integers. -/
private theorem int_add_toNat_neg (n : ℤ) : n + (-n).toNat = n.toNat := by
  rcases le_or_gt 0 n with h | h
  · rw [Int.toNat_of_nonneg h, Int.toNat_eq_zero.mpr (neg_nonpos.mpr h),
      Int.natCast_zero, add_zero]
  · have hnneg : 0 ≤ -n := neg_nonneg.mpr (le_of_lt h)
    have hn0 : n.toNat = 0 := Int.toNat_eq_zero.mpr (le_of_lt h)
    rw [hn0, Int.toNat_of_nonneg hnneg, Int.natCast_zero, add_neg_cancel]

/-- Multiplicity of a listed prime in a product of prime powers. -/
private theorem factorization_prod_prime_pow
    (s : Finset Nat.Primes) (e : Nat.Primes → ℕ) (i : Nat.Primes)
    (hi : i ∈ s) :
    (∏ j ∈ s, (j : ℕ) ^ e j).factorization (i : ℕ) = e i := by
  rw [Nat.factorization_prod_apply fun j _ => pow_ne_zero _ j.property.ne_zero]
  refine (sum_eq_single i ?_ ?_).trans ?_
  · intro j hj hne
    rw [Nat.Prime.factorization_pow j.property, Finsupp.single_eq_of_ne]
    exact fun h => hne (Nat.Primes.coe_nat_injective h.symm)
  · intro hnot
    exact (hnot hi).elim
  · rw [Nat.Prime.factorization_pow i.property, Finsupp.single_eq_same]

/-- `{log p | p prime}` is linearly independent over ℚ.

If `∑ a_p log p = 0` is a finite rational combination, a common
denominator produces an integer combination; exponentiation yields
`∏ p^{n_p} = 1` in ℝ; unique factorization of the two natural numbers
`∏_{n_p>0} p^{n_p}` and `∏_{n_p<0} p^{-n_p}` forces every `n_p = 0`. -/
theorem linearIndependent_log_primes :
    LinearIndependent ℚ (fun p : Nat.Primes => Real.log (p : ℝ)) := by
  classical
  rw [linearIndependent_iff']
  intro s g hg i hi
  let d : ℕ := ∏ j ∈ s, (g j).den
  have hdpos : 0 < d := prod_pos fun j _ => (g j).den_pos
  have hdne : (d : ℚ) ≠ 0 := Nat.cast_ne_zero.2 hdpos.ne'
  have hdiv : ∀ j ∈ s, (g j).den ∣ d := fun j hj =>
    dvd_prod_of_mem (fun k => (g k).den) hj
  let n : Nat.Primes → ℤ := fun j => (d / (g j).den : ℕ) * (g j).num
  have hn_eq : ∀ j ∈ s, (n j : ℚ) = (d : ℚ) * g j := by
    intro j hj
    simp only [n, Int.cast_mul, Int.cast_natCast]
    rw [Nat.cast_div (hdiv j hj) (Nat.cast_ne_zero.2 (g j).den_ne_zero)]
    rw [div_mul_eq_mul_div, mul_div_assoc, (g j).num_div_den]
  have hsumZ : ∑ j ∈ s, (n j : ℝ) * Real.log (j : ℝ) = 0 := by
    have hsmul : ∑ j ∈ s, ((d : ℚ) * g j) • Real.log (j : ℝ) = 0 := by
      simp_rw [← smul_smul]
      rw [← smul_sum, hg, smul_zero]
    refine Eq.trans ?_ hsmul
    refine sum_congr rfl fun j hj => ?_
    rw [Algebra.smul_def, eq_ratCast, ← hn_eq j hj, Rat.cast_intCast]
  have hlog : ∑ j ∈ s, Real.log ((j : ℝ) ^ n j) = 0 := by
    simpa [Real.log_zpow] using hsumZ
  have hprod_ne : ∀ j ∈ s, (j : ℝ) ^ n j ≠ 0 := fun j _ =>
    zpow_ne_zero _ (Nat.cast_ne_zero.2 j.property.ne_zero)
  have hprod_log : Real.log (∏ j ∈ s, (j : ℝ) ^ n j) = 0 := by
    rw [log_prod hprod_ne]
    exact hlog
  have hprod_pos : 0 < ∏ j ∈ s, (j : ℝ) ^ n j :=
    prod_pos fun j _ => zpow_pos (Nat.cast_pos.2 j.property.pos) _
  have hprod_one : ∏ j ∈ s, (j : ℝ) ^ n j = 1 :=
    eq_one_of_pos_of_log_eq_zero hprod_pos hprod_log
  let P : ℕ := ∏ j ∈ s, (j : ℕ) ^ (n j).toNat
  let Q : ℕ := ∏ j ∈ s, (j : ℕ) ^ (-n j).toNat
  have hP_cast : (P : ℝ) = ∏ j ∈ s, (j : ℝ) ^ (n j).toNat := by
    simp [P, Nat.cast_prod, Nat.cast_pow]
  have hQ_cast : (Q : ℝ) = ∏ j ∈ s, (j : ℝ) ^ (-n j).toNat := by
    simp [Q, Nat.cast_prod, Nat.cast_pow]
  have hmul : (∏ j ∈ s, (j : ℝ) ^ n j) * (Q : ℝ) = (P : ℝ) := by
    rw [hQ_cast, hP_cast, ← prod_mul_distrib]
    refine prod_congr rfl fun j hj => ?_
    have hj0 : (j : ℝ) ≠ 0 := Nat.cast_ne_zero.2 j.property.ne_zero
    rw [← zpow_natCast, ← zpow_natCast, ← zpow_add₀ hj0]
    congr 1
    exact_mod_cast int_add_toNat_neg (n j)
  have hPQ : P = Q := by
    have : (P : ℝ) = (Q : ℝ) := by
      simpa [hprod_one] using hmul.symm
    exact Nat.cast_injective this
  have hto : (n i).toNat = (-n i).toNat := by
    have hPfact : P.factorization (i : ℕ) = (n i).toNat := by
      simpa [P] using factorization_prod_prime_pow s (fun j => (n j).toNat) i hi
    have hQfact : Q.factorization (i : ℕ) = (-n i).toNat := by
      simpa [Q] using factorization_prod_prime_pow s (fun j => (-n j).toNat) i hi
    rw [← hPfact, ← hQfact, hPQ]
  have hn0 : n i = 0 := by
    rcases le_or_gt (n i) 0 with hle | hgt
    · have hL : (n i).toNat = 0 := Int.toNat_eq_zero.mpr hle
      have hR : (-n i).toNat = 0 := hto ▸ hL
      have : -n i ≤ 0 := Int.toNat_eq_zero.mp hR
      linarith
    · have hR : (-n i).toNat = 0 :=
        Int.toNat_eq_zero.mpr (neg_nonpos.mpr (le_of_lt hgt))
      have hL : (n i).toNat = 0 := hto.trans hR
      have : n i ≤ 0 := Int.toNat_eq_zero.mp hL
      linarith
  have : (d : ℚ) * g i = 0 := by
    rw [← hn_eq i hi, hn0, Int.cast_zero]
  exact (mul_eq_zero.mp this).resolve_left hdne

/-- Distinct prime logarithms are incommensurable: `log p / log q ∉ ℚ`.
This is the two-prime special case used by the commensurability
corollary in `tfpt_prime_front.tex` §(vi). -/
theorem log_ratio_irrational (p q : ℕ) (hp : p.Prime) (hq : q.Prime) (hne : p ≠ q) :
    Irrational (Real.log p / Real.log q) := by
  rintro ⟨r, hr⟩
  let P : Nat.Primes := ⟨p, hp⟩
  let Q : Nat.Primes := ⟨q, hq⟩
  have hnePQ : P ≠ Q := fun h => hne (congrArg Subtype.val h)
  have hq0 : Real.log q ≠ 0 := by
    intro h0
    have : (q : ℝ) = 1 :=
      eq_one_of_pos_of_log_eq_zero (Nat.cast_pos.2 hq.pos) h0
    exact hq.ne_one (Nat.cast_eq_one.mp this)
  have hlin : (r : ℝ) * Real.log q = Real.log p := by
    rw [hr, div_mul_cancel₀ _ hq0]
  have hsum :
      ∑ j ∈ ({P, Q} : Finset Nat.Primes),
        (if j = P then (1 : ℚ) else -r) • Real.log (j : ℝ) = 0 := by
    rw [sum_pair hnePQ, if_pos rfl, if_neg (Ne.symm hnePQ)]
    simp [Algebra.smul_def, eq_ratCast, P, Q]
    linarith [hlin]
  have hP0 :=
    (linearIndependent_iff'.mp linearIndependent_log_primes)
      ({P, Q} : Finset Nat.Primes)
      (fun j => if j = P then (1 : ℚ) else -r) hsum P (mem_insert_self _ _)
  simp at hP0

end RH
