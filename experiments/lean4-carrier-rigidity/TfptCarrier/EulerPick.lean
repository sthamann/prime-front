/-
  EulerPick — the Euler–Pick forward direction (finite-sum core).
  ================================================================

  Lean seam of round 93 (PRIME.SCREW.VERBLUNSKY.INVARIANT.01, V0c):
  numeric counterpart `experiments/tfpt-discovery/vbk_invariant_probe.py`
  (23/23 gates) and note CCCXCIII.  The audited criterion there is

      RH  ⇔  Pick_N = [(P(σ_j)+P(σ_k))/(σ_j+σ_k)] ⪰ 0 for every N,
      P(σ) = ξ'/ξ(1/2+σ),   σ_j = 1 + 1/j.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`) — the FORWARD direction's algebraic core, for
  FINITE zero sets:

    (1) `pick_entry_decomposition` — the exact per-zero identity: for
        σ, τ > 0 and any real ordinate γ,

          (2σ/(γ²+σ²) + 2τ/(γ²+τ²)) / (σ+τ)
            = 2·[ (σ/(γ²+σ²))·(τ/(γ²+τ²)) + (γ/(γ²+σ²))·(γ/(γ²+τ²)) ],

        i.e. each zero contributes the sum of TWO rank-one Gram
        matrices (the symbolic identity gated in V0c, here exact in
        the kernel — no floats, no truncation).

    (2) `pickMatrix_entry_eq_gram_sum` — the finite-sum Pick matrix
        built from `eulerP γ σ = Σ_i 2σ/(γ_i²+σ²)` is entrywise the
        sum over zeros of those two Grams.

    (3) `pickForm_nonneg` — THE HEADLINE: for every real ordinate
        family (γ_i), every positive node family (σ_j), and every
        witness c, the Pick quadratic form Σ_{j,k} c_j c_k M_{j,k} is
        nonnegative — PSD in the witness formulation of the campaign
        map.  `pickMatrix_posSemidef` — the same as
        `Matrix.PosSemidef` (symmetry + form nonnegativity), the shape
        `CofinalWeil.CofinalHypothesis` consumes.

    (4) `pickMatrix_svNodes_posSemidef` — the concrete instantiation
        at the Stieltjes–Vitali nodes σ_j = 1 + 1/(j+1) of V0a (all
        nodes positive, accumulating at the interior point 1).

  THE HONEST BOUNDARY.  Everything here is for a FINITE index type of
  ordinates γ_i.  The identification of `eulerP` with the actual
  ξ'/ξ(1/2+σ) — the convergent sum over ALL nontrivial zeta zeros,
  under RH with real ordinates — is classical analytic input (the
  Hadamard/partial-fraction expansion) and is NOT formalized; neither
  is any limit N → ∞.  The BACKWARD direction (Pick interpolation,
  Nicolau 2015 Thm 2 / Pick 1916, Montel, the identity theorem, the
  pole contradiction) is cited in V0c and NOT formalized here.  This
  module makes the forward algebra — "real ordinates ⇒ every finite
  Pick section is PSD" — kernel-checked; it does not decide, assume,
  or imply where the ordinates of ζ actually lie.  No RH claim.
-/
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic

namespace TfptCarrier
namespace EulerPick

open Finset Matrix

variable {ι n : Type*} [Fintype ι] [Fintype n]

/-! ### The finite Euler sum and the Pick matrix -/

/-- The finite Euler sum `P(σ) = Σ_i 2σ/(γ_i² + σ²)` over a finite
family of real ordinates γ_i.  For the actual ξ'/ξ(1/2+σ) this is the
partial-fraction sum over zeros — that identification is classical
input, NOT formalized (see module docstring). -/
noncomputable def eulerP (γ : ι → ℝ) (σ : ℝ) : ℝ :=
  ∑ i, 2 * σ / (γ i ^ 2 + σ ^ 2)

/-- The Pick matrix of the half-plane problem at nodes σ_j with
values `eulerP γ σ_j`: `M[j,k] = (P(σ_j)+P(σ_k))/(σ_j+σ_k)`. -/
noncomputable def pickMatrix (γ : ι → ℝ) (σ : n → ℝ) : Matrix n n ℝ :=
  Matrix.of fun j k => (eulerP γ (σ j) + eulerP γ (σ k)) / (σ j + σ k)

/-- First Gram coordinate of a zero: `a_i(j) = σ_j/(γ_i²+σ_j²)`. -/
noncomputable def gramA (γ : ι → ℝ) (σ : n → ℝ) (i : ι) (j : n) : ℝ :=
  σ j / (γ i ^ 2 + σ j ^ 2)

/-- Second Gram coordinate of a zero: `b_i(j) = γ_i/(γ_i²+σ_j²)`. -/
noncomputable def gramB (γ : ι → ℝ) (σ : n → ℝ) (i : ι) (j : n) : ℝ :=
  γ i / (γ i ^ 2 + σ j ^ 2)

/-! ### (1) The exact per-zero identity -/

/-- **The per-zero rank-two decomposition** — the symbolic identity of
V0c, exact in the kernel: one real ordinate γ contributes to the Pick
entry at positive nodes σ, τ exactly twice the sum of the two Gram
products.  This is the entire algebraic content of the forward
direction. -/
theorem pick_entry_decomposition {s t : ℝ} (hs : 0 < s) (ht : 0 < t)
    (γ : ℝ) :
    (2 * s / (γ ^ 2 + s ^ 2) + 2 * t / (γ ^ 2 + t ^ 2)) / (s + t)
      = 2 * (s / (γ ^ 2 + s ^ 2) * (t / (γ ^ 2 + t ^ 2))
           + γ / (γ ^ 2 + s ^ 2) * (γ / (γ ^ 2 + t ^ 2))) := by
  have h1 : γ ^ 2 + s ^ 2 ≠ 0 := by positivity
  have h2 : γ ^ 2 + t ^ 2 ≠ 0 := by positivity
  have h3 : s + t ≠ 0 := by positivity
  field_simp
  ring

/-! ### (2) The entrywise Gram-sum identity -/

omit [Fintype n] in
/-- **Entrywise Gram sum**: the finite-sum Pick matrix is, entry by
entry, the sum over zeros of the two rank-one Grams. -/
theorem pickMatrix_entry_eq_gram_sum (γ : ι → ℝ) (σ : n → ℝ)
    (hσ : ∀ j, 0 < σ j) (j k : n) :
    pickMatrix γ σ j k
      = ∑ i, 2 * (gramA γ σ i j * gramA γ σ i k
                + gramB γ σ i j * gramB γ σ i k) := by
  unfold pickMatrix eulerP gramA gramB
  rw [Matrix.of_apply, ← Finset.sum_add_distrib, Finset.sum_div]
  exact Finset.sum_congr rfl fun i _ =>
    pick_entry_decomposition (hσ j) (hσ k) (γ i)

/-! ### (3) The headline: the Pick form is nonnegative -/

omit [Fintype ι] in
/-- The per-zero quadratic form collapses to two explicit squares:
`Σ_{j,k} c_j c_k · 2(a_j a_k + b_j b_k) = 2(Σ_j c_j a_j)² + 2(Σ_j c_j b_j)²`. -/
theorem per_zero_form_eq_squares (γ : ι → ℝ) (σ : n → ℝ) (c : n → ℝ)
    (i : ι) :
    ∑ j, ∑ k, c j * c k * (2 * (gramA γ σ i j * gramA γ σ i k
                              + gramB γ σ i j * gramB γ σ i k))
      = 2 * (∑ j, c j * gramA γ σ i j) ^ 2
      + 2 * (∑ j, c j * gramB γ σ i j) ^ 2 := by
  rw [sq, sq, Finset.sum_mul_sum, Finset.sum_mul_sum, Finset.mul_sum,
    Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun k _ => by ring

/-- **THE EULER–PICK FORWARD DIRECTION** (finite-sum core, witness
formulation): real ordinates γ_i and positive nodes σ_j make the Pick
quadratic form nonnegative at every witness c — each zero contributes
two squares and nothing else.  No hypothesis relates γ to ζ; the
theorem is exactly "real ordinates ⇒ PSD sections", the kernel-checked
half of the Euler–Pick criterion of V0c. -/
theorem pickForm_nonneg (γ : ι → ℝ) (σ : n → ℝ) (hσ : ∀ j, 0 < σ j)
    (c : n → ℝ) :
    0 ≤ ∑ j, ∑ k, c j * c k * pickMatrix γ σ j k := by
  have expand : ∑ j, ∑ k, c j * c k * pickMatrix γ σ j k
      = ∑ i, (2 * (∑ j, c j * gramA γ σ i j) ^ 2
            + 2 * (∑ j, c j * gramB γ σ i j) ^ 2) := by
    calc ∑ j, ∑ k, c j * c k * pickMatrix γ σ j k
        = ∑ j, ∑ k, ∑ i, c j * c k
            * (2 * (gramA γ σ i j * gramA γ σ i k
                  + gramB γ σ i j * gramB γ σ i k)) := by
          refine Finset.sum_congr rfl fun j _ =>
            Finset.sum_congr rfl fun k _ => ?_
          rw [pickMatrix_entry_eq_gram_sum γ σ hσ j k, Finset.mul_sum]
      _ = ∑ j, ∑ i, ∑ k, c j * c k
            * (2 * (gramA γ σ i j * gramA γ σ i k
                  + gramB γ σ i j * gramB γ σ i k)) :=
          Finset.sum_congr rfl fun j _ => Finset.sum_comm
      _ = ∑ i, ∑ j, ∑ k, c j * c k
            * (2 * (gramA γ σ i j * gramA γ σ i k
                  + gramB γ σ i j * gramB γ σ i k)) := Finset.sum_comm
      _ = ∑ i, (2 * (∑ j, c j * gramA γ σ i j) ^ 2
              + 2 * (∑ j, c j * gramB γ σ i j) ^ 2) :=
          Finset.sum_congr rfl fun i _ => per_zero_form_eq_squares γ σ c i
  rw [expand]
  exact Finset.sum_nonneg fun i _ => by positivity

/-- **The Pick matrix is PSD** in Mathlib's `Matrix.PosSemidef` — the
exact shape consumed by `CofinalWeil.CofinalHypothesis`.  Symmetry is
by inspection of the entry; nonnegativity of the form is
`pickForm_nonneg`. -/
theorem pickMatrix_posSemidef (γ : ι → ℝ) (σ : n → ℝ)
    (hσ : ∀ j, 0 < σ j) : (pickMatrix γ σ).PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg ?_ fun x => ?_
  · ext j k
    simp only [Matrix.conjTranspose_apply, star_trivial, pickMatrix,
      Matrix.of_apply]
    rw [add_comm (eulerP γ (σ k)), add_comm (σ k)]
  · have expand : x ⬝ᵥ (pickMatrix γ σ *ᵥ x)
        = ∑ j, ∑ k, x j * x k * pickMatrix γ σ j k := by
      simp only [Matrix.mulVec, dotProduct, Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ =>
        Finset.sum_congr rfl fun k _ => by ring
    rw [star_trivial, expand]
    exact pickForm_nonneg γ σ hσ x

/-! ### (4) The Stieltjes–Vitali nodes -/

/-- The concrete node sequence of V0a: σ_j = 1 + 1/(j+1) ∈ (1, 2],
accumulating at the interior point 1 of the safe Euler half-plane. -/
noncomputable def svNode (j : ℕ) : ℝ :=
  1 + 1 / ((j : ℝ) + 1)

/-- Every Stieltjes–Vitali node is positive. -/
theorem svNode_pos (j : ℕ) : 0 < svNode j := by
  unfold svNode
  positivity

/-- **Concrete instantiation**: at the Stieltjes–Vitali nodes, every
finite Pick section built from real ordinates is PSD — the forward
half of the V0c criterion at the deployed nodes, for every finite
ordinate family and every section size N. -/
theorem pickMatrix_svNodes_posSemidef (γ : ι → ℝ) (N : ℕ) :
    (pickMatrix γ (fun j : Fin N => svNode j)).PosSemidef :=
  pickMatrix_posSemidef γ _ fun j => svNode_pos j

end EulerPick
end TfptCarrier
