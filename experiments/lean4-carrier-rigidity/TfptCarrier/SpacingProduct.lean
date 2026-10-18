/-
  SpacingProduct — the round-135 spacing-product identity, general K.
  ===================================================================

  Lean seam of round 135 (PRIME.HPIN.FLOOR.01; contract
  PRIME.THEOREMS.LEAN2.01, second hardening round): THEOREM D1 of
  `experiments/tfpt-discovery/hpin_floor_probe.py`, the
  secular-derivative identity, in its spacing form — proven here for
  a GENERIC finite lattice over an arbitrary field (the probe gated
  it sympy-generically per block).

  The objects: F(y) = A₀ + Σ_k w_k/(y − b_k) with simple poles at a
  finite lattice b : κ → F; its derivative in WEIGHT FORM
  F′(y) = −Σ_k w_k/(y − b_k)²; and the numerator polynomial
  N = A₀·∏_k(X − b_k) + Σ_k w_k·∏_{l≠k}(X − b_l), whose roots
  y : ι → F are the census roots of F.  The root data enters as ONE
  polynomial identity: C A₀ · ∏_i (X − y_i) = N (degree match,
  leading value A₀ — exactly the probe's "spacing form" premise).

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `nodal_erase_wronskian` — the per-pole Wronskian collapse
        D_k′·D − D_k·D′ = −D_k² for D = ∏(X−b_l), D_k the erased
        product: the polynomial engine of the weight form.

    (2) `spacing_product_cleared` — THE SPACING-PRODUCT IDENTITY
        (D1, denominator-cleared): at every root y_j of the
        numerator polynomial off the lattice,
          F′(y_j)·∏_k(y_j − b_k) = A₀·∏_{i≠j}(y_j − y_i).

    (3) `spacing_product` — THE D1 SPACING FORM as stated:
          F′(y_j) = A₀·∏_{i≠j}(y_j − y_i) / ∏_k(y_j − b_k).

    (4) `fderivWeight_ne_zero` — THE FLOOR IS THE SPACING PRODUCT:
        for A₀ ≠ 0 and a simple root (y_j ≠ y_i for i ≠ j),
        F′(y_j) ≠ 0 — real-rootedness gives a nonvanishing secular
        derivative, the D1 floor anatomy.

  PROOF ROUTE (all polynomial algebra): evaluate the root
  factorization at y_j (the numerator vanishes), differentiate it
  formally and evaluate again (`Polynomial.derivative`, with
  mathlib's `Lagrange.nodal` derivative-at-a-node lemma collapsing
  the root side to the spacing product), then convert N′(y_j) into
  the weight form through the per-pole Wronskian collapse (1).

  THE HONEST BOUNDARY.  This is exact rational-function algebra
  over an abstract field: the identification of b_k with the frozen
  anchor lattice ω_k², of y_j with census roots of the ground
  profile, the E_N′ node-floor assembly 4|A₀|·|sin(Aμ_j)|·(spacing
  product)/(lattice product), and all measured floor bars remain
  the probe's content and are NOT formalized.  No RH claim in any
  direction.
-/
import Mathlib.LinearAlgebra.Lagrange
import Mathlib.Tactic

namespace TfptCarrier
namespace SpacingProduct

open Polynomial Lagrange Finset

variable {F : Type*} [Field F] {ι κ : Type*} [DecidableEq ι] [DecidableEq κ]

/-- The weight-form secular derivative `F′(x) = −Σ_k w_k/(x − b_k)²`
of F(y) = A₀ + Σ_k w_k/(y − b_k) (probe round 135, weight form). -/
noncomputable def fderivWeight (t : Finset κ) (w b : κ → F) (x : F) : F :=
  -∑ k ∈ t, w k / (x - b k) ^ 2

/-- The numerator polynomial of F = A₀ + Σ_k w_k/(X − b_k):
`N = A₀·∏_k(X − b_k) + Σ_k w_k·∏_{l≠k}(X − b_l)`. -/
noncomputable def numeratorPoly (t : Finset κ) (A0 : F) (w b : κ → F) :
    F[X] :=
  C A0 * nodal t b + ∑ k ∈ t, C (w k) * nodal (t.erase k) b

/-- **The per-pole Wronskian collapse**: with D = ∏_{l∈t}(X − b_l)
and D_k the k-erased product, `D_k′·D − D_k·D′ = −D_k²` exactly —
the polynomial identity behind the weight form of F′. -/
theorem nodal_erase_wronskian {t : Finset κ} {k : κ} (hk : k ∈ t)
    (b : κ → F) :
    derivative (nodal (t.erase k) b) * nodal t b
      - nodal (t.erase k) b * derivative (nodal t b)
      = -(nodal (t.erase k) b) ^ 2 := by
  rw [nodal_eq_mul_nodal_erase hk, derivative_mul, derivative_X_sub_C]
  ring

/-- **THE SPACING-PRODUCT IDENTITY** (round-135 D1, denominator-
cleared form): if the census roots y factor the numerator
polynomial — `C A₀·∏_i(X − y_i) = N` — then at every root y_j off
the lattice,
`F′(y_j)·∏_k(y_j − b_k) = A₀·∏_{i≠j}(y_j − y_i)`. -/
theorem spacing_product_cleared {s : Finset ι} {t : Finset κ}
    {y : ι → F} {b w : κ → F} {A0 : F} {j : ι} (hj : j ∈ s)
    (hfact : C A0 * nodal s y = numeratorPoly t A0 w b)
    (hyb : ∀ k ∈ t, y j ≠ b k) :
    fderivWeight t w b (y j) * ∏ k ∈ t, (y j - b k)
      = A0 * ∏ i ∈ s.erase j, (y j - y i) := by
  -- (A) evaluate the factorization at the root y_j
  have h0 := congrArg (eval (y j)) hfact
  rw [eval_mul, eval_C, eval_nodal_at_node hj, mul_zero,
    numeratorPoly, eval_add, eval_mul, eval_C, eval_finset_sum] at h0
  simp only [eval_mul, eval_C] at h0
  -- h0 : 0 = A0·D(y_j) + Σ_k w_k·D_k(y_j)
  -- (B) differentiate the factorization, evaluate at y_j
  have h1 := congrArg (eval (y j)) (congrArg derivative hfact)
  rw [derivative_C_mul, eval_mul, eval_C,
    eval_nodal_derivative_eval_node_eq hj, eval_nodal,
    numeratorPoly, derivative_add, derivative_C_mul,
    derivative_sum] at h1
  simp only [derivative_C_mul] at h1
  rw [eval_add, eval_mul, eval_C, eval_finset_sum] at h1
  simp only [eval_mul, eval_C] at h1
  -- h1 : A0·∏_{i≠j}(y_j−y_i) = A0·D′(y_j) + Σ_k w_k·D_k′(y_j)
  -- (C) the Wronskian collapse, evaluated at y_j
  have hW : ∀ k ∈ t,
      eval (y j) (derivative (nodal (t.erase k) b))
          * eval (y j) (nodal t b)
        - eval (y j) (nodal (t.erase k) b)
          * eval (y j) (derivative (nodal t b))
        = -(eval (y j) (nodal (t.erase k) b)) ^ 2 := by
    intro k hk
    have h := congrArg (eval (y j)) (nodal_erase_wronskian hk b)
    simpa using h
  -- (D) the per-pole factor D = (y_j − b_k)·D_k
  have hDk : ∀ k ∈ t, eval (y j) (nodal t b)
      = (y j - b k) * eval (y j) (nodal (t.erase k) b) := by
    intro k hk
    have h := congrArg (eval (y j)) (nodal_eq_mul_nodal_erase (v := b) hk)
    simpa using h
  -- (E) the lattice product does not vanish at y_j
  have hD0 : eval (y j) (nodal t b) ≠ 0 :=
    eval_nodal_not_at_node hyb
  -- (F) assembly: F′(y_j)·D² = (A0·∏_{i≠j})·D, then cancel one D
  have hterm : ∀ k ∈ t,
      w k / (y j - b k) ^ 2 * eval (y j) (nodal t b) ^ 2
        = w k * eval (y j) (nodal (t.erase k) b) ^ 2 := by
    intro k hk
    have hne : y j - b k ≠ 0 := sub_ne_zero.mpr (hyb k hk)
    rw [hDk k hk]
    field_simp
  have hchain : fderivWeight t w b (y j) * eval (y j) (nodal t b) ^ 2
      = (A0 * ∏ i ∈ s.erase j, (y j - y i))
          * eval (y j) (nodal t b) := by
    have e1 : fderivWeight t w b (y j) * eval (y j) (nodal t b) ^ 2
        = -∑ k ∈ t, w k * eval (y j) (nodal (t.erase k) b) ^ 2 := by
      rw [fderivWeight, neg_mul, Finset.sum_mul, neg_inj]
      exact Finset.sum_congr rfl hterm
    have e2 : -∑ k ∈ t, w k * eval (y j) (nodal (t.erase k) b) ^ 2
        = ∑ k ∈ t, w k
            * (eval (y j) (derivative (nodal (t.erase k) b))
                * eval (y j) (nodal t b)
              - eval (y j) (nodal (t.erase k) b)
                * eval (y j) (derivative (nodal t b))) := by
      rw [neg_eq_iff_eq_neg, ← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun k hk => ?_
      linear_combination (w k) * hW k hk
    have e3 : ∑ k ∈ t, w k
            * (eval (y j) (derivative (nodal (t.erase k) b))
                * eval (y j) (nodal t b)
              - eval (y j) (nodal (t.erase k) b)
                * eval (y j) (derivative (nodal t b)))
        = eval (y j) (nodal t b)
            * ∑ k ∈ t, w k * eval (y j) (derivative (nodal (t.erase k) b))
          - eval (y j) (derivative (nodal t b))
            * ∑ k ∈ t, w k * eval (y j) (nodal (t.erase k) b) := by
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun k _ => by ring
    have hS1 : ∑ k ∈ t, w k * eval (y j) (derivative (nodal (t.erase k) b))
        = A0 * (∏ i ∈ s.erase j, (y j - y i))
          - A0 * eval (y j) (derivative (nodal t b)) := by
      linear_combination -h1
    have hS0 : ∑ k ∈ t, w k * eval (y j) (nodal (t.erase k) b)
        = -(A0 * eval (y j) (nodal t b)) := by
      linear_combination -h0
    rw [e1, e2, e3, hS1, hS0]
    ring
  have hsq : (fderivWeight t w b (y j) * eval (y j) (nodal t b))
        * eval (y j) (nodal t b)
      = ((A0 * ∏ i ∈ s.erase j, (y j - y i)))
        * eval (y j) (nodal t b) := by
    rw [mul_assoc, ← pow_two]
    exact hchain
  have hcancel := mul_right_cancel₀ hD0 hsq
  rwa [eval_nodal] at hcancel

/-- **THE D1 SPACING FORM** (round-135 headline): at every census
root y_j off the lattice,
`F′(y_j) = A₀·∏_{i≠j}(y_j − y_i) / ∏_k(y_j − b_k)` — the secular
derivative IS the node-spacing product over the lattice product. -/
theorem spacing_product {s : Finset ι} {t : Finset κ}
    {y : ι → F} {b w : κ → F} {A0 : F} {j : ι} (hj : j ∈ s)
    (hfact : C A0 * nodal s y = numeratorPoly t A0 w b)
    (hyb : ∀ k ∈ t, y j ≠ b k) :
    fderivWeight t w b (y j)
      = A0 * (∏ i ∈ s.erase j, (y j - y i)) / ∏ k ∈ t, (y j - b k) := by
  have hprod : (∏ k ∈ t, (y j - b k)) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun k hk => sub_ne_zero.mpr (hyb k hk)
  rw [eq_div_iff hprod]
  exact spacing_product_cleared hj hfact hyb

/-- **THE FLOOR IS THE SPACING PRODUCT** (round-135 D1 corollary):
for A₀ ≠ 0 and a SIMPLE root (y_j ≠ y_i for every other index),
`F′(y_j) ≠ 0` — the secular derivative floor never vanishes at a
simple census root. -/
theorem fderivWeight_ne_zero {s : Finset ι} {t : Finset κ}
    {y : ι → F} {b w : κ → F} {A0 : F} {j : ι} (hj : j ∈ s)
    (hfact : C A0 * nodal s y = numeratorPoly t A0 w b)
    (hyb : ∀ k ∈ t, y j ≠ b k) (hA0 : A0 ≠ 0)
    (hyy : ∀ i ∈ s.erase j, y j ≠ y i) :
    fderivWeight t w b (y j) ≠ 0 := by
  rw [spacing_product hj hfact hyb]
  exact div_ne_zero
    (mul_ne_zero hA0 (Finset.prod_ne_zero_iff.mpr
      fun i hi => sub_ne_zero.mpr (hyy i hi)))
    (Finset.prod_ne_zero_iff.mpr fun k hk =>
      sub_ne_zero.mpr (hyb k hk))

end SpacingProduct
end TfptCarrier
