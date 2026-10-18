/-
  PinchIdentity — the round-142 s×gap defect identity and pinch.
  ==============================================================

  Lean seam of round 142 (PRIME.TLAWCAP.SUSCAP2R.01; contract
  PRIME.THEOREMS.LEAN2.01, second hardening round): THEOREM W1 of
  `experiments/tfpt-discovery/tlawcap_suscap2r_probe.py` — the exact
  algebra of the bordered-secular root on a finite eigenstructure.

  The setting (all data finite and real, stated as hypotheses):
  reduced eigenvalue gaps δᵢ = (qᵢ − q₀)/τ (i ≥ 1), normalized
  overlaps ẽᵢ with ground weight ρ² = ẽ₀², the secular gap
  g = (λ* − τ)/τ solving the ROOT EQUATION ρ²/g = Σᵢ ẽᵢ²/(δᵢ − g),
  and the susceptibility coordinate s with s·ρ² = Σᵢ ẽᵢ²/δᵢ.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `defect_identity` — THE s×GAP DEFECT IDENTITY (W1 display):
        from the root equation, via the exact per-term split
        1/(δ−g) = 1/δ + g/(δ(δ−g)),
          1 − s·g = (g²/ρ²)·Σᵢ ẽᵢ²/(δᵢ(δᵢ − g)).
        s×gap == 1 is NOT an exact identity: the defect is exactly
        the positive second-order susceptibility term.

    (2) `sg_le_one` — THE UPPER PINCH: the defect sum is
        term-wise nonnegative (0 < g < δᵢ), so s·g ≤ 1.

    (3) `one_sub_div_le_sg` — THE LOWER PINCH: bounding 1/δᵢ by
        1/δ₁ term-wise and re-consuming the root equation,
        defect ≤ g/δ₁, i.e. 1 − g/δ₁ ≤ s·g.

    (4) `pinch` — THE TWO-SIDED PINCH (W1 headline):
        1 − g/δ₁ ≤ s·g ≤ 1.

  THE HONEST BOUNDARY.  These are finite-sum field/order lemmas on
  an ABSTRACT eigenvalue/overlap family: the identification of
  (δᵢ, ẽᵢ, g, s) with the round-138/139 compressed Weil matrix data,
  the existence/position of the secular root λ* ∈ (q₀, q₁), and every
  SUSCAP2R/DELTA1FLOOR polynomial-demand statement remain the probe's
  measured/audited content and are NOT formalized.  No RH claim in
  any direction.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace TfptCarrier
namespace PinchIdentity

open Finset

variable {ι : Type*} [Fintype ι]
variable {e δ : ι → ℝ} {g ρ2 s : ℝ}

/-- **THE s×GAP DEFECT IDENTITY** (round-142 W1 display): from the
bordered-secular root equation `ρ²/g = Σᵢ ẽᵢ²/(δᵢ − g)` and the
susceptibility definition `s·ρ² = Σᵢ ẽᵢ²/δᵢ`, exactly
`1 − s·g = (g²/ρ²)·Σᵢ ẽᵢ²/(δᵢ(δᵢ − g))` — the defect of s×gap from
one is the second-order susceptibility term, with no remainder. -/
theorem defect_identity (hg : 0 < g) (hρ : 0 < ρ2)
    (hδ : ∀ i, g < δ i)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g))
    (hs : s * ρ2 = ∑ i, e i ^ 2 / δ i) :
    1 - s * g = g ^ 2 / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g)) := by
  have hsplit : ∀ i, e i ^ 2 / (δ i - g)
      = e i ^ 2 / δ i + g * (e i ^ 2 / (δ i * (δ i - g))) := by
    intro i
    have h1 : δ i ≠ 0 := ne_of_gt (hg.trans (hδ i))
    have h2 : δ i - g ≠ 0 := ne_of_gt (sub_pos.mpr (hδ i))
    field_simp
    ring
  have hsum : ∑ i, e i ^ 2 / (δ i - g)
      = (∑ i, e i ^ 2 / δ i)
        + g * ∑ i, e i ^ 2 / (δ i * (δ i - g)) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun i _ => hsplit i
  rw [hsum, ← hs] at hroot
  -- hroot : ρ2 / g = s * ρ2 + g * Σᵢ ẽᵢ²/(δᵢ(δᵢ−g))
  have hgne : g ≠ 0 := ne_of_gt hg
  have hρne : ρ2 ≠ 0 := ne_of_gt hρ
  have hkey : g * ∑ i, e i ^ 2 / (δ i * (δ i - g))
      = ρ2 / g - s * ρ2 := by linarith
  have hone : g / ρ2 * (ρ2 / g - s * ρ2) = 1 - s * g := by
    field_simp
  calc 1 - s * g
      = g / ρ2 * (ρ2 / g - s * ρ2) := hone.symm
    _ = g / ρ2 * (g * ∑ i, e i ^ 2 / (δ i * (δ i - g))) := by rw [hkey]
    _ = g ^ 2 / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g)) := by ring

/-- The defect sum is term-wise nonnegative on the eigenstructure
(0 < g < δᵢ): the second-order susceptibility carries no sign
channel. -/
theorem defect_sum_nonneg (hg : 0 < g) (hδ : ∀ i, g < δ i) :
    0 ≤ ∑ i, e i ^ 2 / (δ i * (δ i - g)) :=
  Finset.sum_nonneg fun i _ =>
    div_nonneg (sq_nonneg _)
      (mul_nonneg (hg.trans (hδ i)).le (sub_pos.mpr (hδ i)).le)

/-- **THE UPPER PINCH** (round-142 W1): the defect is nonnegative,
so `s·g ≤ 1` — s×gap never exceeds one on the eigenstructure. -/
theorem sg_le_one (hg : 0 < g) (hρ : 0 < ρ2)
    (hδ : ∀ i, g < δ i)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g))
    (hs : s * ρ2 = ∑ i, e i ^ 2 / δ i) :
    s * g ≤ 1 := by
  have hd := defect_identity hg hρ hδ hroot hs
  have h1 : 0 ≤ 1 - s * g := by
    rw [hd]
    exact mul_nonneg (div_nonneg (sq_nonneg g) hρ.le)
      (defect_sum_nonneg hg hδ)
  linarith

/-- **THE LOWER PINCH** (round-142 W1): with δ₁ below the reduced
gap family (δ₁ ≤ δᵢ, g < δ₁), bounding 1/δᵢ ≤ 1/δ₁ term-wise and
re-consuming the root equation bounds the defect by g/δ₁:
`1 − g/δ₁ ≤ s·g`. -/
theorem one_sub_div_le_sg {δ1 : ℝ} (hg : 0 < g) (hρ : 0 < ρ2)
    (hδ1 : ∀ i, δ1 ≤ δ i) (hgδ1 : g < δ1)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g))
    (hs : s * ρ2 = ∑ i, e i ^ 2 / δ i) :
    1 - g / δ1 ≤ s * g := by
  have hδ : ∀ i, g < δ i := fun i => hgδ1.trans_le (hδ1 i)
  have hδ1pos : 0 < δ1 := hg.trans hgδ1
  have hd := defect_identity hg hρ hδ hroot hs
  -- term-wise: δ₁·ẽᵢ²/(δᵢ(δᵢ−g)) ≤ ẽᵢ²/(δᵢ−g)
  have hterm : ∀ i, δ1 * (e i ^ 2 / (δ i * (δ i - g)))
      ≤ e i ^ 2 / (δ i - g) := by
    intro i
    have hδpos : 0 < δ i := hg.trans (hδ i)
    have hfrac : δ1 * (e i ^ 2 / (δ i * (δ i - g)))
        = δ1 / δ i * (e i ^ 2 / (δ i - g)) := by
      rw [div_mul_div_comm, mul_div_assoc']
    rw [hfrac]
    have hle1 : δ1 / δ i ≤ 1 := (div_le_one hδpos).mpr (hδ1 i)
    have hX : 0 ≤ e i ^ 2 / (δ i - g) :=
      div_nonneg (sq_nonneg _) (sub_pos.mpr (hδ i)).le
    calc δ1 / δ i * (e i ^ 2 / (δ i - g))
        ≤ 1 * (e i ^ 2 / (δ i - g)) :=
          mul_le_mul_of_nonneg_right hle1 hX
      _ = e i ^ 2 / (δ i - g) := one_mul _
  -- summed: δ₁·(defect sum) ≤ ρ²/g
  have hsummed : δ1 * ∑ i, e i ^ 2 / (δ i * (δ i - g)) ≤ ρ2 / g := by
    rw [hroot, Finset.mul_sum]
    exact Finset.sum_le_sum fun i _ => hterm i
  -- assemble: 1 − s·g = (g²/ρ²)·Sd ≤ g/δ₁
  have hgρ : 0 < g / ρ2 := div_pos hg hρ
  have hstep := mul_le_mul_of_nonneg_left hsummed hgρ.le
  -- hstep : (g/ρ²)·(δ₁·Sd) ≤ (g/ρ²)·(ρ²/g)
  have hone : g / ρ2 * (ρ2 / g) = 1 := by
    field_simp
  have hbound : 1 - s * g ≤ g / δ1 := by
    rw [hd]
    have hrearr : g ^ 2 / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g))
        = g / δ1 * (δ1 * (g / ρ2
            * ∑ i, e i ^ 2 / (δ i * (δ i - g)))) := by
      field_simp
    rw [hrearr]
    have hδSd : δ1 * (g / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g))) ≤ 1 := by
      calc δ1 * (g / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g)))
          = g / ρ2 * (δ1 * ∑ i, e i ^ 2 / (δ i * (δ i - g))) := by ring
        _ ≤ g / ρ2 * (ρ2 / g) := hstep
        _ = 1 := hone
    calc g / δ1 * (δ1 * (g / ρ2 * ∑ i, e i ^ 2 / (δ i * (δ i - g))))
        ≤ g / δ1 * 1 :=
          mul_le_mul_of_nonneg_left hδSd (div_pos hg hδ1pos).le
      _ = g / δ1 := mul_one _
  linarith

/-- **THE TWO-SIDED PINCH** (round-142 W1 headline):
`1 − g/δ₁ ≤ s·g ≤ 1` — the measured 0.99985…1.00000 strings ARE
this pinch, with the defect exactly one gap ratio deep. -/
theorem pinch {δ1 : ℝ} (hg : 0 < g) (hρ : 0 < ρ2)
    (hδ1 : ∀ i, δ1 ≤ δ i) (hgδ1 : g < δ1)
    (hroot : ρ2 / g = ∑ i, e i ^ 2 / (δ i - g))
    (hs : s * ρ2 = ∑ i, e i ^ 2 / δ i) :
    1 - g / δ1 ≤ s * g ∧ s * g ≤ 1 :=
  ⟨one_sub_div_le_sg hg hρ hδ1 hgδ1 hroot hs,
   sg_le_one hg hρ (fun i => hgδ1.trans_le (hδ1 i)) hroot hs⟩

end PinchIdentity
end TfptCarrier
