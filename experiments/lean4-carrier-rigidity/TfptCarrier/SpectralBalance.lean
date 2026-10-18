/-
  SpectralBalance — the round-157 balance theorems, kernel-checked.
  =================================================================

  Lean seam of round 157 (PRIME.SPECTRAL.BALANCE.01; contract
  PRIME.THEOREMS.LEAN2.01, second hardening round): the exact
  finite-eigenstructure halves of THEOREMS SB1/SB2/SB3 of
  `experiments/tfpt-discovery/spectral_balance_probe.py`.

  The setting is the round-142 eigenstructure (see `PinchIdentity`):
  reduced gaps δᵢ (i ≥ 1) with bottom δ₁, overlaps ẽᵢ normalized
  with the ground weight ρ² by ρ² + Σᵢ ẽᵢ² = 1, secular gap g with
  root equation ρ²/g = Σᵢ ẽᵢ²/(δᵢ − g), susceptibility coordinate s
  with s·ρ² = Σᵢ ẽᵢ²/δᵢ.  For SB1 the data is the FULL eigenvalue
  family λᵢ (i ≥ 1) above the ground τ, with the trace
  TrH = Σᵢ 1/(λᵢ − τ) and the tightness factor
  tf = (λ₁ − τ)·TrH.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `tf_ge_one` / `tf_le_card` — THE SB1 TAIL CLOSURE:
        1 ≤ tf ≤ K−1 unconditionally (each summand
        (λ₁−τ)/(λᵢ−τ) lies in (0, 1], the bottom term is 1) —
        the trivial count bound that closes the tail half of the
        trace loop with NO zeta-like refinement.

    (2) `trace_loop_identity` — THE SB1 LOOP IDENTITY:
        τ·TrH = tf/FULLGAP with FULLGAP = (λ₁−τ)/τ — the dominant
        trace term IS 1/FULLGAP; DELTA1FLOOR ⟺ TRACEFLOOR is a
        re-coordinate, not a reduction.

    (3) `chi_cap` — THE SB2 χ-CAP: from δᵢ ≥ δ₁ and the overlap
        normalization, s·ρ²·δ₁ ≤ 1 − ρ² exactly (the third
        rate-blind one-sided moment instrument).

    (4) `enclosure_lower` / `secular_enclosure` — THE SB3 MERGE
        ENCLOSURE: from the root equation and δᵢ − g ≥ δ₁ − g,
        ρ²·δ₁ ≤ g ≤ δ₁ — the two-sided enclosure of the QSUBGAP
        root, both ends exact.

  THE HONEST BOUNDARY.  All statements are finite-sum real
  field/order lemmas on an abstract eigenvalue/overlap family.  The
  identification with the compressed Weil matrix (rounds 138/139),
  the interlacing δ₁ ≥ FULLGAP (SB3 uses Cauchy interlacing at the
  matrix level — NOT formalized), the measured vacuity/rider
  adjudications (ρ² collapsing, BS super-polynomially falling,
  MERGE-REFUTED-MEASURED), and every polynomial-demand statement
  remain the probe's content.  No RH claim in any direction.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace TfptCarrier
namespace SpectralBalance

open Finset

variable {ι : Type*} [Fintype ι]

/-! ### (1)/(2) The SB1 trace-loop tail closure -/

section TraceLoop

variable {lam : ι → ℝ} {τ : ℝ} {j0 : ι}

/-- The tightness factor of the trace loop:
`tf = (λ₁ − τ)·Σᵢ 1/(λᵢ − τ)` (round-157 SB1). -/
noncomputable def tf (lam : ι → ℝ) (τ : ℝ) (j0 : ι) : ℝ :=
  (lam j0 - τ) * ∑ i, 1 / (lam i - τ)

/-- **THE SB1 LOWER COUNT BOUND**: `1 ≤ tf` — the bottom eigenvalue
contributes exactly 1 and every other term is nonnegative. -/
theorem tf_ge_one (hmin : ∀ i, lam j0 ≤ lam i) (hτ : τ < lam j0) :
    1 ≤ tf lam τ j0 := by
  have hpos : 0 < lam j0 - τ := sub_pos.mpr hτ
  rw [tf, Finset.mul_sum]
  have hj0 : (lam j0 - τ) * (1 / (lam j0 - τ)) = 1 :=
    mul_one_div_cancel (ne_of_gt hpos)
  calc (1 : ℝ) = (lam j0 - τ) * (1 / (lam j0 - τ)) := hj0.symm
    _ ≤ ∑ i, (lam j0 - τ) * (1 / (lam i - τ)) := by
        refine Finset.single_le_sum (f := fun i =>
          (lam j0 - τ) * (1 / (lam i - τ))) (fun i _ => ?_)
          (Finset.mem_univ j0)
        have hi : 0 < lam i - τ := hpos.trans_le (by linarith [hmin i])
        positivity

/-- **THE SB1 UPPER COUNT BOUND** (the tail closure): `tf ≤ K − 1`
where K − 1 is the number of above-ground eigenvalues — each term
(λ₁−τ)/(λᵢ−τ) is at most 1, so the trivial count bound closes the
tail half of the trace loop unconditionally. -/
theorem tf_le_card (hmin : ∀ i, lam j0 ≤ lam i) (hτ : τ < lam j0) :
    tf lam τ j0 ≤ Fintype.card ι := by
  have hpos : 0 < lam j0 - τ := sub_pos.mpr hτ
  rw [tf, Finset.mul_sum]
  calc ∑ i, (lam j0 - τ) * (1 / (lam i - τ))
      ≤ ∑ _i : ι, (1 : ℝ) := by
        refine Finset.sum_le_sum fun i _ => ?_
        have hi : 0 < lam i - τ := hpos.trans_le (by linarith [hmin i])
        rw [mul_one_div]
        exact (div_le_one hi).mpr (by linarith [hmin i])
    _ = Fintype.card ι := by
        rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]

/-- **THE SB1 LOOP IDENTITY**: `τ·TrH = tf/FULLGAP` with
`FULLGAP = (λ₁−τ)/τ` — the dominant trace term IS the inverse
full gap; the r146 Y1 re-coordination is a loop, exactly. -/
theorem trace_loop_identity (hτ : 0 < τ) (hgap : τ < lam j0) :
    τ * ∑ i, 1 / (lam i - τ)
      = tf lam τ j0 / ((lam j0 - τ) / τ) := by
  have h1 : lam j0 - τ ≠ 0 := ne_of_gt (sub_pos.mpr hgap)
  have h2 : τ ≠ 0 := ne_of_gt hτ
  rw [tf]
  field_simp

end TraceLoop

/-! ### (3)/(4) The SB2 χ-cap and the SB3 enclosure -/

section Enclosure

variable {e δ : ι → ℝ} {g ρ2 s δ1 : ℝ}

/-- **THE SB2 χ-CAP** (the direct s-bound): from δᵢ ≥ δ₁ > 0 and the
overlap normalization ρ² + Σᵢ ẽᵢ² = 1,
`s·ρ²·δ₁ ≤ 1 − ρ²` exactly (equality iff two-level). -/
theorem chi_cap (hδ1 : ∀ i, δ1 ≤ δ i) (hδ1pos : 0 < δ1)
    (hnorm : ρ2 + ∑ i, e i ^ 2 = 1)
    (hs : s * ρ2 = ∑ i, e i ^ 2 / δ i) :
    s * ρ2 * δ1 ≤ 1 - ρ2 := by
  have hterm : ∀ i, e i ^ 2 / δ i ≤ e i ^ 2 / δ1 := by
    intro i
    have hδpos : 0 < δ i := hδ1pos.trans_le (hδ1 i)
    rw [div_le_div_iff₀ hδpos hδ1pos]
    exact mul_le_mul_of_nonneg_left (hδ1 i) (sq_nonneg _)
  have hsum : ∑ i, e i ^ 2 / δ i ≤ (∑ i, e i ^ 2) / δ1 := by
    rw [Finset.sum_div]
    exact Finset.sum_le_sum fun i _ => hterm i
  have hcap : s * ρ2 ≤ (1 - ρ2) / δ1 := by
    rw [hs]
    calc ∑ i, e i ^ 2 / δ i ≤ (∑ i, e i ^ 2) / δ1 := hsum
      _ = (1 - ρ2) / δ1 := by rw [show ∑ i, e i ^ 2 = 1 - ρ2 by
            linarith]
  calc s * ρ2 * δ1 ≤ (1 - ρ2) / δ1 * δ1 :=
        mul_le_mul_of_nonneg_right hcap hδ1pos.le
    _ = 1 - ρ2 := div_mul_cancel₀ _ (ne_of_gt hδ1pos)

/-- **THE SB3 LOWER ENCLOSURE END** (the merge coordinate bound):
from the root equation and δᵢ − g ≥ δ₁ − g > 0,
`BS = ρ²·δ₁ ≤ g` exactly. -/
theorem enclosure_lower (hg : 0 < g)
    (hδ1 : ∀ i, δ1 ≤ δ i) (hgδ1 : g < δ1)
    (hnorm : ρ2 + ∑ i, e i ^ 2 = 1)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g)) :
    ρ2 * δ1 ≤ g := by
  have hgap1 : 0 < δ1 - g := sub_pos.mpr hgδ1
  have hterm : ∀ i, e i ^ 2 / (δ i - g) ≤ e i ^ 2 / (δ1 - g) := by
    intro i
    have hgapi : 0 < δ i - g := hgap1.trans_le (by linarith [hδ1 i])
    rw [div_le_div_iff₀ hgapi hgap1]
    exact mul_le_mul_of_nonneg_left (by linarith [hδ1 i]) (sq_nonneg _)
  have hsum : ρ2 / g ≤ (1 - ρ2) / (δ1 - g) := by
    rw [hroot]
    calc ∑ i, e i ^ 2 / (δ i - g)
        ≤ ∑ i, e i ^ 2 / (δ1 - g) := Finset.sum_le_sum fun i _ => hterm i
      _ = (∑ i, e i ^ 2) / (δ1 - g) := (Finset.sum_div _ _ _).symm
      _ = (1 - ρ2) / (δ1 - g) := by
          rw [show ∑ i, e i ^ 2 = 1 - ρ2 by linarith]
  have hcross : ρ2 * (δ1 - g) ≤ (1 - ρ2) * g := by
    have := (div_le_div_iff₀ hg hgap1).mp hsum
    linarith
  nlinarith

/-- **THE SB3 MERGE ENCLOSURE** (both ends exact):
`ρ²·δ₁ ≤ g ≤ δ₁` — the two-sided enclosure of the QSUBGAP secular
root; the lower end is the BOTTOMSHARE merge coordinate
BS = ρ²·δ₁, the upper end is the reduced gap itself. -/
theorem secular_enclosure (hg : 0 < g)
    (hδ1 : ∀ i, δ1 ≤ δ i) (hgδ1 : g < δ1)
    (hnorm : ρ2 + ∑ i, e i ^ 2 = 1)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g)) :
    ρ2 * δ1 ≤ g ∧ g ≤ δ1 :=
  ⟨enclosure_lower hg hδ1 hgδ1 hnorm hroot, hgδ1.le⟩

end Enclosure

end SpectralBalance
end TfptCarrier
