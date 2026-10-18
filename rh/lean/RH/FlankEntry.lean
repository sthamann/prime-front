/-
RH/FlankEntry.lean -- r384: kernel-anchor of the r382 entry lemma
(FlankEntryPrefix) against the r380 pivot layer.

Targets (lemma-first, three exits: proved / named-decomposed /
documented-impossible-with-mathlib-reason):
  A. Flank predicates F1 (ν-run length ≤ 2), F2c (local mass ratio ≤ c)
     and the named Prop `FlankEntryPrefix` on the existing
     `SignedAtoms` / `VonMangoldtWindow.toSignedAtoms` carrier
     (no parallel Hankel).
  B. Sorry-free finite algebra: pair-energy identity; h₀,h₁ from mass
     and pair energy; the 3-atom flank toy over ℚ; the clustered
     run-of-3 kill H₃ = −28500; composition
     FlankEntryPrefix + adaptive_band_from_entry.
  C. Christoffel comparison h_k(w) ≥ (1−λ) h_k(μ): named Prop
     `ChristoffelPivotBound` (discrete OP / CD kernel for general k;
     mathlib v4.29.1 has Schur / Hankel dets, not the CD basis).
     Special cases k = 0 and k = 1 PROVED (completing the square).

Does not assert (P1)/(P2), L*, or any window census.  Zero `sorry`.
Census stays 5.  NO RH CLAIM.

Provenance: r382 `rh/problem/pivot_entry_lemma.tex` +
`verify_pivot_entry.py` (14/14); r380 `RH/PivotCoordinate.lean`.
-/
import RH.PivotCoordinate
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace RH

open Matrix

/-! ## Moments on the existing `SignedAtoms` carrier -/

/-- Power moment `m_k = ∑_j w_j x_j^k` of a signed atomic measure. -/
noncomputable def SignedAtoms.mom {S : ℕ} (m : SignedAtoms S) (k : ℕ) : ℝ :=
  ∑ j, m.w j * m.x j ^ k

lemma SignedAtoms.hankel_eq_mom {S p : ℕ} (m : SignedAtoms S)
    (i k : Fin p) : m.hankel p i k = m.mom ((i : ℕ) + (k : ℕ)) :=
  rfl

/-- Pair energy `½ ∑_{i,j} w_i w_j (x_i − x_j)²`. -/
noncomputable def SignedAtoms.pairEnergy {S : ℕ} (m : SignedAtoms S) : ℝ :=
  (1 / 2) * ∑ i, ∑ j, m.w i * m.w j * (m.x i - m.x j) ^ 2

lemma pair_energy_sum_sq_left {S : ℕ} (m : SignedAtoms S) :
    ∑ i, ∑ j, m.w i * m.w j * (m.x i) ^ 2 = m.mom 2 * m.mom 0 := by
  calc ∑ i, ∑ j, m.w i * m.w j * (m.x i) ^ 2
      = ∑ i, ∑ j, (m.w i * (m.x i) ^ 2) * m.w j := by
        refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
        ring
    _ = ∑ i, (m.w i * (m.x i) ^ 2) * ∑ j, m.w j := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [← Finset.mul_sum]
    _ = (∑ i, m.w i * (m.x i) ^ 2) * ∑ j, m.w j := by
        rw [Finset.sum_mul]
    _ = m.mom 2 * m.mom 0 := by
        simp [SignedAtoms.mom]

lemma pair_energy_sum_sq_right {S : ℕ} (m : SignedAtoms S) :
    ∑ i, ∑ j, m.w i * m.w j * (m.x j) ^ 2 = m.mom 0 * m.mom 2 := by
  calc ∑ i, ∑ j, m.w i * m.w j * (m.x j) ^ 2
      = ∑ i, ∑ j, m.w i * (m.w j * (m.x j) ^ 2) := by
        refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
        ring
    _ = ∑ i, m.w i * ∑ j, m.w j * (m.x j) ^ 2 := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [← Finset.mul_sum]
    _ = (∑ i, m.w i) * ∑ j, m.w j * (m.x j) ^ 2 := by
        rw [Finset.sum_mul]
    _ = m.mom 0 * m.mom 2 := by
        simp [SignedAtoms.mom]

lemma pair_energy_sum_cross {S : ℕ} (m : SignedAtoms S) :
    ∑ i, ∑ j, (m.w i * m.x i) * (m.w j * m.x j) = m.mom 1 * m.mom 1 := by
  rw [← Finset.sum_mul_sum]
  simp [SignedAtoms.mom]

/-- Double-sum expansion: `∑_{i,j} w_i w_j (x_i−x_j)² = 2(m₀ m₂ − m₁²)`. -/
lemma pair_energy_double_sum {S : ℕ} (m : SignedAtoms S) :
    ∑ i, ∑ j, m.w i * m.w j * (m.x i - m.x j) ^ 2
      = 2 * (m.mom 0 * m.mom 2 - m.mom 1 ^ 2) := by
  calc ∑ i, ∑ j, m.w i * m.w j * (m.x i - m.x j) ^ 2
      = ∑ i, ∑ j,
          (m.w i * m.w j * (m.x i) ^ 2
            - 2 * (m.w i * m.x i) * (m.w j * m.x j)
            + m.w i * m.w j * (m.x j) ^ 2) := by
        refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
        ring
    _ = ∑ i, ∑ j, m.w i * m.w j * (m.x i) ^ 2
        - ∑ i, ∑ j, (2 * (m.w i * m.x i) * (m.w j * m.x j))
        + ∑ i, ∑ j, m.w i * m.w j * (m.x j) ^ 2 := by
        simp [Finset.sum_add_distrib, Finset.sum_sub_distrib]
    _ = m.mom 2 * m.mom 0
        - 2 * (m.mom 1 * m.mom 1)
        + m.mom 0 * m.mom 2 := by
        have h2 : ∑ i, ∑ j, (2 * (m.w i * m.x i) * (m.w j * m.x j))
            = 2 * (m.mom 1 * m.mom 1) := by
          have h := pair_energy_sum_cross m
          calc ∑ i, ∑ j, (2 * (m.w i * m.x i) * (m.w j * m.x j))
              = ∑ i, ∑ j, (2 * ((m.w i * m.x i) * (m.w j * m.x j))) := by
                refine Finset.sum_congr rfl fun i _ =>
                  Finset.sum_congr rfl fun j _ => ?_
                ring
            _ = 2 * ∑ i, ∑ j, (m.w i * m.x i) * (m.w j * m.x j) := by
                simp [Finset.mul_sum]
            _ = 2 * (m.mom 1 * m.mom 1) := by rw [h]
        rw [pair_energy_sum_sq_left, pair_energy_sum_sq_right, h2]
    _ = 2 * (m.mom 0 * m.mom 2 - m.mom 1 ^ 2) := by ring

/-- **Pair-energy identity** (r382 Lemma, PROVED).  For any finite
signed atomic measure,
  `m₀ m₂ − m₁² = ½ ∑_{i,j} w_i w_j (x_i − x_j)²`.
Pure `Finset` algebra; no analysis.  NO RH CLAIM. -/
theorem pair_energy_identity {S : ℕ} (m : SignedAtoms S) :
    m.mom 0 * m.mom 2 - m.mom 1 ^ 2 = m.pairEnergy := by
  unfold SignedAtoms.pairEnergy
  have h := pair_energy_double_sum m
  have : (1 / 2 : ℝ) * (2 * (m.mom 0 * m.mom 2 - m.mom 1 ^ 2))
      = m.mom 0 * m.mom 2 - m.mom 1 ^ 2 := by ring
  rw [h, this]

/-! ## (F1), (F2c), `FlankEntryPrefix` -/

/-- Weight at a raw index, `0` off the support. -/
noncomputable def SignedAtoms.weightAt {S : ℕ} (m : SignedAtoms S) (n : ℕ) : ℝ :=
  if h : n < S then m.w ⟨n, h⟩ else 0

/-- **(F1).** No three consecutive negative weights: every ν-run on
the indexed support has length at most 2. -/
def FlankRunBound {S : ℕ} (m : SignedAtoms S) : Prop :=
  ∀ i j k : Fin S,
    (i : ℕ) + 1 = (j : ℕ) → (j : ℕ) + 1 = (k : ℕ) →
    ¬ (m.w i < 0 ∧ m.w j < 0 ∧ m.w k < 0)

/-- A maximal consecutive negative run on the indexed support,
written as a half-open interval `[lo, hi)`. -/
def IsMaximalNegRun {S : ℕ} (m : SignedAtoms S) (lo hi : ℕ) : Prop :=
  lo < hi ∧ hi ≤ S ∧
    (∀ n, lo ≤ n → n < hi → m.weightAt n < 0) ∧
    (lo = 0 ∨ ¬ m.weightAt (lo - 1) < 0) ∧
    (hi = S ∨ ¬ m.weightAt hi < 0)

/-- ν-mass of the run `[lo, hi)`. -/
noncomputable def runNegMass {S : ℕ} (m : SignedAtoms S) (lo hi : ℕ) : ℝ :=
  -∑ n : Fin S, if lo ≤ (n : ℕ) ∧ (n : ℕ) < hi then m.w n else 0

/-- Immediately adjacent μ-mass (at most two flanking positive atoms). -/
noncomputable def flankMass {S : ℕ} (m : SignedAtoms S) (lo hi : ℕ) : ℝ :=
  (if lo = 0 then 0 else max (m.weightAt (lo - 1)) 0) +
    (if hi = S then 0 else max (m.weightAt hi) 0)

/-- **(F2c).** Every maximal negative run has ν-mass at most `c` times
its immediately flanking μ-mass. -/
def FlankRatioBound {S : ℕ} (m : SignedAtoms S) (c : ℝ) : Prop :=
  ∀ lo hi, IsMaximalNegRun m lo hi →
    runNegMass m lo hi ≤ c * flankMass m lo hi

/-- (F2_{2/3}) together with (F1), on a linearly ordered support.
This is Definition `def:flank` of r382 with `c = 2/3`. -/
def FlankTwoThird {S : ℕ} (m : SignedAtoms S) : Prop :=
  StrictMono m.x ∧ FlankRunBound m ∧ FlankRatioBound m (2 / 3)

/-- Source-defined entry `n₀ = ⌊2N/5⌋` with `N = ⌈S/2⌉ = (S+1)/2`
(Lean natural division). -/
def windowCap (S : ℕ) : ℕ := (S + 1) / 2

def entryIndex (S : ℕ) : ℕ := (2 * windowCap S) / 5

/-- **Named Prop (r382 remainder, r384 docking).**  The (2/3)-flank
condition implies a positive Hankel-pivot prefix through the
source-defined entry `n₀ = ⌊2N/5⌋`.

WHY NAMED, NOT A SORRY (r384 mathlib census, v4.29.1): the finite
identities below (pair energy, h₀/h₁, the 3-atom flank, the
clustered run-of-3 kill) are PROVED, and the transport
`adaptive_band_from_entry` is PROVED in `RH/PivotCoordinate.lean`.
The inductive core — Christoffel minimization of `h_k` at every
depth `k ≤ n₀` plus a uniform λ_max bound on the flank-dressed
CD kernel `E_{k+1}` — is the discrete OP / CD remainder, the same
class as `ComplementaryDualHankelInertia`.  Never a silent `sorry`.
NO RH CLAIM. -/
def FlankEntryPrefix : Prop :=
  ∀ {S : ℕ} (m : SignedAtoms S),
    FlankTwoThird m → ∀ i ≤ entryIndex S, 0 < m.h i

/-! ## h₀, h₁ from mass and pair energy -/

/-- `h₀ = m₀`. -/
theorem h_zero {S : ℕ} (m : SignedAtoms S) : m.h 0 = m.mom 0 := by
  unfold SignedAtoms.h
  rw [Matrix.det_fin_one, Matrix.det_fin_zero]
  simp [SignedAtoms.hankel, SignedAtoms.mom]

theorem hankel_one_det {S : ℕ} (m : SignedAtoms S) :
    (m.hankel 1).det = m.mom 0 := by
  rw [Matrix.det_fin_one]
  simp [SignedAtoms.hankel, SignedAtoms.mom]

theorem hankel_two_det {S : ℕ} (m : SignedAtoms S) :
    (m.hankel 2).det = m.pairEnergy := by
  rw [Matrix.det_fin_two]
  simp only [SignedAtoms.hankel_eq_mom]
  have h00 : ((0 : Fin 2) : ℕ) + ((0 : Fin 2) : ℕ) = 0 := rfl
  have h11 : ((1 : Fin 2) : ℕ) + ((1 : Fin 2) : ℕ) = 2 := rfl
  have h01 : ((0 : Fin 2) : ℕ) + ((1 : Fin 2) : ℕ) = 1 := rfl
  have h10 : ((1 : Fin 2) : ℕ) + ((0 : Fin 2) : ℕ) = 1 := rfl
  rw [h00, h11, h01, h10]
  rw [← pow_two]
  exact pair_energy_identity m

/-- `h₁ = (m₀ m₂ − m₁²) / m₀ = (pair energy) / m₀` whenever `m₀ ≠ 0`. -/
theorem h_one {S : ℕ} (m : SignedAtoms S) (_h0 : m.mom 0 ≠ 0) :
    m.h 1 = m.pairEnergy / m.mom 0 := by
  unfold SignedAtoms.h
  rw [hankel_two_det, hankel_one_det]

theorem h0_pos_of_mass {S : ℕ} (m : SignedAtoms S) (hm : 0 < m.mom 0) :
    0 < m.h 0 := by
  rwa [h_zero]

theorem h1_pos_of_pairEnergy {S : ℕ} (m : SignedAtoms S)
    (hm : 0 < m.mom 0) (hE : 0 < m.pairEnergy) : 0 < m.h 1 := by
  have h0 : m.mom 0 ≠ 0 := hm.ne'
  rw [h_one m h0]
  exact div_pos hE hm

/-- Completing the square for a monic linear: the quadratic in the
barycentre offset is a square over `m₀`. -/
lemma monic_linear_completing_square {S : ℕ} (m : SignedAtoms S) (α : ℝ)
    (h0 : m.mom 0 ≠ 0) :
    m.mom 2 - 2 * α * m.mom 1 + α ^ 2 * m.mom 0
      = m.mom 0 * (α - m.mom 1 / m.mom 0) ^ 2
        + (m.mom 0 * m.mom 2 - m.mom 1 ^ 2) / m.mom 0 := by
  field_simp [h0]
  ring

lemma monic_linear_eq_weighted_sq {S : ℕ} (m : SignedAtoms S) (α : ℝ) :
    m.mom 2 - 2 * α * m.mom 1 + α ^ 2 * m.mom 0
      = ∑ j, m.w j * (m.x j - α) ^ 2 := by
  simp only [SignedAtoms.mom]
  have hexp : ∀ j : Fin S,
      m.w j * (m.x j - α) ^ 2
        = m.w j * (m.x j) ^ 2 - 2 * α * (m.w j * m.x j) + α ^ 2 * m.w j := by
    intro j
    ring
  simp_rw [hexp]
  simp [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.mul_sum]

lemma monic_linear_ge_h1 {S : ℕ} (m : SignedAtoms S) (α : ℝ)
    (hm : 0 < m.mom 0) :
    m.h 1 ≤ ∑ j, m.w j * (m.x j - α) ^ 2 := by
  have h0 : m.mom 0 ≠ 0 := hm.ne'
  have hsq := monic_linear_completing_square m α h0
  have hE := pair_energy_identity m
  have hnonneg : 0 ≤ m.mom 0 * (α - m.mom 1 / m.mom 0) ^ 2 :=
    mul_nonneg hm.le (sq_nonneg _)
  have : (m.mom 0 * m.mom 2 - m.mom 1 ^ 2) / m.mom 0 ≤
      m.mom 2 - 2 * α * m.mom 1 + α ^ 2 * m.mom 0 := by
    linarith [hsq]
  rw [h_one m h0, ← hE, ← monic_linear_eq_weighted_sq]
  exact this

lemma barycenter_attains_h1 {S : ℕ} (m : SignedAtoms S) (h0 : m.mom 0 ≠ 0) :
    ∑ j, m.w j * (m.x j - m.mom 1 / m.mom 0) ^ 2 = m.h 1 := by
  have hcs := monic_linear_completing_square m (m.mom 1 / m.mom 0) h0
  have hsq : (m.mom 1 / m.mom 0 - m.mom 1 / m.mom 0) ^ 2 = 0 := by ring
  rw [← monic_linear_eq_weighted_sq, hcs, hsq, mul_zero, zero_add,
    pair_energy_identity, h_one m h0]

/-! ## Local 3-atom positivity under (F2c), `c < 1` -/

/-- Mass positivity of a single flanked ν-atom: `μ_L − ν + μ_R > 0`
whenever `ν ≤ c(μ_L+μ_R)`, `c < 1`, and the flanks are not both zero. -/
theorem three_atom_mass_pos (μL ν μR c : ℝ)
    (hμL : 0 ≤ μL) (hμR : 0 ≤ μR) (hν : 0 ≤ ν)
    (hc0 : 0 ≤ c) (hc1 : c < 1)
    (hr : ν ≤ c * (μL + μR)) (hfl : 0 < μL + μR) :
    0 < μL - ν + μR := by
  have hfactor : 0 < 1 - c := sub_pos.mpr hc1
  have hflnn : 0 ≤ μL + μR := add_nonneg hμL hμR
  have _hcnn : 0 ≤ c * (μL + μR) := mul_nonneg hc0 hflnn
  have _hν' : 0 ≤ ν := hν
  have : μL - ν + μR ≥ (1 - c) * (μL + μR) := by linarith
  have : 0 < (1 - c) * (μL + μR) := mul_pos hfactor hfl
  linarith

/-- Equal-flank equally-spaced pair energy: on `{0,1,2}` with weights
`{μ, −ν, μ}` and `ν ≤ c·2μ`, `c < 1`, the pair energy is
`4μ² − 2νμ ≥ 4μ²(1−c) > 0`. -/
theorem three_atom_equal_flank_pairEnergy_pos (μ ν c : ℝ)
    (hμ : 0 < μ) (hν : 0 ≤ ν) (hc0 : 0 ≤ c) (hc1 : c < 1)
    (hr : ν ≤ c * (μ + μ)) :
    0 < 4 * μ * μ - ν * (μ + μ) := by
  have _hν' : 0 ≤ ν := hν
  have _hc0' : 0 ≤ c := hc0
  nlinarith [sq_pos_of_pos hμ]

/-! ## Positive / negative parts (for Christoffel) -/

noncomputable def SignedAtoms.posPart {S : ℕ} (m : SignedAtoms S) :
    SignedAtoms S where
  x := m.x
  w := fun j => max (m.w j) 0

noncomputable def SignedAtoms.negPart {S : ℕ} (m : SignedAtoms S) :
    SignedAtoms S where
  x := m.x
  w := fun j => max (-m.w j) 0

lemma posPart_sub_negPart {S : ℕ} (m : SignedAtoms S) (j : Fin S) :
    m.posPart.w j - m.negPart.w j = m.w j := by
  simp only [SignedAtoms.posPart, SignedAtoms.negPart]
  rcases le_total (m.w j) 0 with h | h
  · rw [max_eq_right h, max_eq_left (neg_nonneg.mpr h)]
    ring
  · rw [max_eq_left h, max_eq_right (neg_nonpos.mpr h)]
    ring

lemma mom_split {S : ℕ} (m : SignedAtoms S) (k : ℕ) :
    m.mom k = m.posPart.mom k - m.negPart.mom k := by
  simp only [SignedAtoms.mom]
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  have hx : m.posPart.x j = m.x j := rfl
  have hy : m.negPart.x j = m.x j := rfl
  rw [hx, hy, ← sub_mul, posPart_sub_negPart]

lemma weighted_sq_split {S : ℕ} (m : SignedAtoms S) (α : ℝ) :
    ∑ j, m.w j * (m.x j - α) ^ 2
      = ∑ j, m.posPart.w j * (m.x j - α) ^ 2
        - ∑ j, m.negPart.w j * (m.x j - α) ^ 2 := by
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← sub_mul, posPart_sub_negPart]

/-! ## Exact ℚ toys (r382 Lemmas, PROVED) -/

/-- Three-atom flank toy: nodes `{0,1,2}`, weights `{3,−2,3}`. -/
noncomputable def threeAtomFlank : SignedAtoms 3 where
  x := ![0, 1, 2]
  w := ![3, -2, 3]

theorem threeAtom_moms :
    threeAtomFlank.mom 0 = 4 ∧ threeAtomFlank.mom 1 = 4
      ∧ threeAtomFlank.mom 2 = 10 := by
  simp [SignedAtoms.mom, threeAtomFlank, Fin.sum_univ_three]
  constructor
  · norm_num
  constructor
  · norm_num
  · norm_num

theorem threeAtom_hankel1 : threeAtomFlank.hankel 1 = !![4] := by
  ext i k
  fin_cases i
  fin_cases k
  simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]
  norm_num

theorem threeAtom_hankel2 :
    threeAtomFlank.hankel 2 = !![4, 4; 4, 10] := by
  ext i k
  fin_cases i <;> fin_cases k
  · simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]; norm_num
  · simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]; norm_num
  · simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]; norm_num
  · simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]; norm_num

theorem threeAtom_hankel3 :
    threeAtomFlank.hankel 3 = !![4, 4, 10; 4, 10, 22; 10, 22, 46] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, threeAtomFlank, Fin.sum_univ_three]
      norm_num

lemma det_fin_three_of (a b c d e f g h i : ℝ) :
    !![a, b, c; d, e, f; g, h, i].det
      = a * e * i - a * f * h - b * d * i + b * f * g + c * d * h - c * e * g := by
  rw [Matrix.det_fin_three]
  simp [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.vecHead, Matrix.vecTail]

/-- **Three-atom flank lemma** (r382, PROVED over ℚ).  Ratio
`2/(3+3) = 1/3`, pivots `h₀ = 4`, `h₁ = 6`, `h₂ = −3`. -/
theorem threeAtom_flank_pivots :
    threeAtomFlank.h 0 = 4 ∧ threeAtomFlank.h 1 = 6
      ∧ threeAtomFlank.h 2 = -3 := by
  have h0 : threeAtomFlank.h 0 = 4 := by
    unfold SignedAtoms.h
    rw [threeAtom_hankel1, Matrix.det_fin_one, Matrix.det_fin_zero]
    norm_num
  have h1 : threeAtomFlank.h 1 = 6 := by
    unfold SignedAtoms.h
    rw [threeAtom_hankel2, threeAtom_hankel1, Matrix.det_fin_two,
      Matrix.det_fin_one]
    norm_num
  have h2 : threeAtomFlank.h 2 = -3 := by
    unfold SignedAtoms.h
    rw [threeAtom_hankel3, threeAtom_hankel2, det_fin_three_of,
      Matrix.det_fin_two]
    norm_num
  exact ⟨h0, h1, h2⟩

theorem threeAtom_ratio_one_third :
    (2 : ℝ) / (3 + 3) = 1 / 3 := by norm_num

theorem threeAtom_h0_h1_pos :
    0 < threeAtomFlank.h 0 ∧ 0 < threeAtomFlank.h 1 := by
  have h := threeAtom_flank_pivots
  constructor <;> linarith

/-- Clustered run-of-3 kill: nodes `{0,…,6}`, weights
`{2,2,−1,−1,−1,2,2}`. -/
noncomputable def clusterRun3 : SignedAtoms 7 where
  x := ![0, 1, 2, 3, 4, 5, 6]
  w := ![2, 2, -1, -1, -1, 2, 2]

theorem clusterRun3_hankel1 : clusterRun3.hankel 1 = !![5] := by
  ext i k
  fin_cases i
  fin_cases k
  simp [SignedAtoms.hankel, clusterRun3, Fin.sum_univ_seven]
  norm_num

theorem clusterRun3_hankel2 :
    clusterRun3.hankel 2 = !![5, 15; 15, 95] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, clusterRun3, Fin.sum_univ_seven]
      norm_num

theorem clusterRun3_hankel3 :
    clusterRun3.hankel 3
      = !![5, 15, 95; 15, 95, 585; 95, 585, 3491] := by
  ext i k
  fin_cases i <;> fin_cases k <;>
    · simp [SignedAtoms.hankel, clusterRun3, Fin.sum_univ_seven]
      norm_num

/-- **Clustered run-of-3 kill** (r382, PROVED over ℚ).  `H₁ > 0`,
`H₂ > 0`, `H₃ = −28500 < 0` before half-filling (`N = 4`). -/
theorem clusterRun3_H3 :
    (clusterRun3.hankel 1).det = 5
      ∧ (clusterRun3.hankel 2).det = 250
      ∧ (clusterRun3.hankel 3).det = -28500 := by
  constructor
  · rw [clusterRun3_hankel1, Matrix.det_fin_one]; norm_num
  constructor
  · rw [clusterRun3_hankel2, Matrix.det_fin_two]; norm_num
  · rw [clusterRun3_hankel3, det_fin_three_of]; norm_num

theorem clusterRun3_H3_neg : (clusterRun3.hankel 3).det < 0 := by
  have h := clusterRun3_H3
  linarith

/-- Five-atom 2-versus-1 interlacing toy. -/
noncomputable def fiveAtomInterlace : SignedAtoms 5 where
  x := ![-2, -1, 0, 1, 2]
  w := ![2, -1, 2, -1, 2]

theorem fiveAtom_energy :
    fiveAtomInterlace.mom 0 * fiveAtomInterlace.mom 2
      - fiveAtomInterlace.mom 1 ^ 2 = 56
      ∧ fiveAtomInterlace.pairEnergy = 56 := by
  have hm0 : fiveAtomInterlace.mom 0 = 4 := by
    simp [SignedAtoms.mom, fiveAtomInterlace, Fin.sum_univ_five]
    try norm_num
  have hm1 : fiveAtomInterlace.mom 1 = 0 := by
    simp [SignedAtoms.mom, fiveAtomInterlace, Fin.sum_univ_five]
    try norm_num
  have hm2 : fiveAtomInterlace.mom 2 = 14 := by
    simp [SignedAtoms.mom, fiveAtomInterlace, Fin.sum_univ_five]
    try norm_num
  have hid := pair_energy_identity fiveAtomInterlace
  constructor
  · rw [hm0, hm1, hm2]; norm_num
  · rw [← hid, hm0, hm1, hm2]; norm_num

theorem fiveAtom_h0_h1 :
    fiveAtomInterlace.h 0 = 4 ∧ fiveAtomInterlace.h 1 = 14 := by
  have hm0 : fiveAtomInterlace.mom 0 = 4 := by
    simp [SignedAtoms.mom, fiveAtomInterlace, Fin.sum_univ_five]
    try norm_num
  have hE : fiveAtomInterlace.pairEnergy = 56 := fiveAtom_energy.2
  constructor
  · rw [h_zero, hm0]
  · have : fiveAtomInterlace.mom 0 ≠ 0 := by rw [hm0]; norm_num
    rw [h_one _ this, hE, hm0]; norm_num

/-! ## Christoffel comparison: named Prop + proved k = 0, 1 -/

/-- **Named Prop (r384 remainder).**  Christoffel comparison
`h_k(w) ≥ (1 − λ) h_k(μ)` whenever `∫ p² dν ≤ λ ∫ p² dμ` for every
coefficient vector of degree `< k+1` and `0 < h_k(μ)`.

WHY NAMED, NOT A SORRY: mathlib v4.29.1 identifies `h_k` with a Hankel
determinant ratio (and, for `k ≤ 1`, with the monic linear completing-
the-square minimum, PROVED below).  The general-`k` identification of
that minimum with the μ-orthonormal CD kernel, and of `λ` with
`λ_max(E_{k+1})`, is discrete OP theory (same class as
`ComplementaryDualHankelInertia` / `CauchyInterlace`).  Never a
silent `sorry`.  NO RH CLAIM. -/
def ChristoffelPivotBound : Prop :=
  ∀ {S k : ℕ} (m : SignedAtoms S) (lam : ℝ),
    (∀ c : Fin (k + 1) → ℝ,
      c ⬝ᵥ (m.negPart.hankel (k + 1) *ᵥ c)
        ≤ lam * (c ⬝ᵥ (m.posPart.hankel (k + 1) *ᵥ c))) →
    0 < m.posPart.h k →
    (1 - lam) * m.posPart.h k ≤ m.h k

/-- Hypothesis form of the named Prop. -/
theorem christoffel_of_bound (h : ChristoffelPivotBound)
    {S k : ℕ} (m : SignedAtoms S) (lam : ℝ)
    (hRay : ∀ c : Fin (k + 1) → ℝ,
      c ⬝ᵥ (m.negPart.hankel (k + 1) *ᵥ c)
        ≤ lam * (c ⬝ᵥ (m.posPart.hankel (k + 1) *ᵥ c)))
    (hμ : 0 < m.posPart.h k) :
    (1 - lam) * m.posPart.h k ≤ m.h k :=
  h m lam hRay hμ

/-- **Christoffel, k = 0** (PROVED).  `h₀(w) = m₀(μ) − m₀(ν)`, and the
Rayleigh bound on the constant polynomial is the mass comparison. -/
theorem christoffel_bound_k0 {S : ℕ} (m : SignedAtoms S) (lam : ℝ)
    (hRay : m.negPart.mom 0 ≤ lam * m.posPart.mom 0) :
    (1 - lam) * m.posPart.h 0 ≤ m.h 0 := by
  rw [h_zero, h_zero, mom_split m 0]
  linarith

/-- **Christoffel, k = 1** (PROVED).  Completing the square: `h₁` is
the monic-linear minimum, so the w-barycentre test function plus
Rayleigh plus `lam ≤ 1` give the comparison. -/
theorem christoffel_bound_k1 {S : ℕ} (m : SignedAtoms S) (lam : ℝ)
    (hRay : ∀ α : ℝ,
      ∑ j, m.negPart.w j * (m.x j - α) ^ 2
        ≤ lam * ∑ j, m.posPart.w j * (m.x j - α) ^ 2)
    (hlam : lam ≤ 1) (hm : 0 < m.mom 0) (hμ0 : 0 < m.posPart.mom 0)
    (_hμ1 : 0 < m.posPart.h 1) :
    (1 - lam) * m.posPart.h 1 ≤ m.h 1 := by
  set α := m.mom 1 / m.mom 0
  have h0 : m.mom 0 ≠ 0 := hm.ne'
  have hw : m.h 1 = ∑ j, m.w j * (m.x j - α) ^ 2 :=
    (barycenter_attains_h1 m h0).symm
  have hsplit := weighted_sq_split m α
  have hR := hRay α
  have hμmin := monic_linear_ge_h1 m.posPart α hμ0
  have h1mlam : 0 ≤ 1 - lam := sub_nonneg.mpr hlam
  have hcmp : ∑ j, m.posPart.w j * (m.x j - α) ^ 2
        - ∑ j, m.negPart.w j * (m.x j - α) ^ 2
      ≥ (1 - lam) * ∑ j, m.posPart.w j * (m.x j - α) ^ 2 := by
    linarith
  have hge : (1 - lam) * ∑ j, m.posPart.w j * (m.x j - α) ^ 2
      ≥ (1 - lam) * m.posPart.h 1 :=
    mul_le_mul_of_nonneg_left hμmin h1mlam
  calc (1 - lam) * m.posPart.h 1
      ≤ (1 - lam) * ∑ j, m.posPart.w j * (m.x j - α) ^ 2 := hge
    _ ≤ ∑ j, m.posPart.w j * (m.x j - α) ^ 2
          - ∑ j, m.negPart.w j * (m.x j - α) ^ 2 := hcmp
    _ = m.h 1 := by rw [hw, hsplit]

/-- Three-atom Christoffel comparison over ℚ: `h₁(w) = 6 ≥ 4 =
(1 − 1/3) h₁(μ)`. -/
theorem threeAtom_christoffel_k1 :
    let μ := threeAtomFlank.posPart
    (1 - (1 / 3 : ℝ)) * μ.h 1 ≤ threeAtomFlank.h 1
      ∧ threeAtomFlank.h 1 = 6 ∧ μ.h 1 = 6 := by
  intro μ
  have hw := threeAtom_flank_pivots
  have hμmoms : μ.mom 0 = 6 ∧ μ.mom 1 = 6 ∧ μ.mom 2 = 12 := by
    simp [μ, SignedAtoms.posPart, SignedAtoms.mom, threeAtomFlank,
      Fin.sum_univ_three]
    try norm_num
  have hμ0z : μ.mom 0 ≠ 0 := by rw [hμmoms.1]; norm_num
  have hμE : μ.pairEnergy = 36 := by
    have hid := pair_energy_identity μ
    rw [← hid, hμmoms.1, hμmoms.2.1, hμmoms.2.2]; norm_num
  have hμ1 : μ.h 1 = 6 := by
    rw [h_one μ hμ0z, hμE, hμmoms.1]; norm_num
  refine ⟨?_, hw.2.1, hμ1⟩
  rw [hw.2.1, hμ1]
  norm_num

/-! ## Bridge: `FlankEntryPrefix` + `adaptive_band_from_entry` -/

/-- FlankEntryPrefix plus the Jacobi count: the source Hankel at the
entry has vanishing negative inertia. -/
theorem indNeg_entry_of_flank (hF : FlankEntryPrefix) {S : ℕ}
    (m : SignedAtoms S) (hfl : FlankTwoThird m)
    (hnz : ∀ i ≤ entryIndex S + 1, (m.hankel i).det ≠ 0) :
    indNeg (m.hankel (entryIndex S + 1)) = 0 := by
  classical
  have hpos : ∀ i ≤ entryIndex S, 0 < m.h i := hF m hfl
  have hcount := indNeg_hankel_eq_neg_pivot_count m hnz
  have hempty :
      {i : Fin (entryIndex S + 1) | m.h (i : ℕ) < 0} = ∅ := by
    ext i
    simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
    intro hneg
    have : (i : ℕ) ≤ entryIndex S := Nat.le_of_lt_succ i.isLt
    linarith [hpos i.val this]
  rw [hcount, hempty, Set.ncard_empty]

theorem indNeg_entry_le_one (hF : FlankEntryPrefix) {S : ℕ}
    (m : SignedAtoms S) (hfl : FlankTwoThird m)
    (hnz : ∀ i ≤ entryIndex S + 1, (m.hankel i).det ≠ 0) :
    indNeg (m.hankel (entryIndex S + 1)) ≤ 1 := by
  rw [indNeg_entry_of_flank hF m hfl hnz]
  exact zero_le_one

/-- **Adaptive band from a flank entry** (PROVED, pure composition).
`FlankEntryPrefix` puts `ind₋ H_{n₀+1} = 0 ≤ 1`; any Loewner chain
`A_{n+1} = A_n + v_n v_nᵀ` whose rung `n₀` does not exceed that
inertia is then bounded by `adaptive_band_from_entry`. -/
theorem adaptive_band_from_flank_entry (hF : FlankEntryPrefix)
    {S : ℕ} (m : SignedAtoms S) (hfl : FlankTwoThird m)
    (hnz : ∀ i ≤ entryIndex S + 1, (m.hankel i).det ≠ 0)
    {n : Type*} [Fintype n] [DecidableEq n]
    (A : ℕ → Matrix n n ℝ) (v : ℕ → n → ℝ)
    (hSym : ∀ k, (A k).IsHermitian)
    (hStep : ∀ k, A (k + 1) = A k + vecMulVec (v k) (v k))
    (hStart : indNeg (A (entryIndex S))
      ≤ indNeg (m.hankel (entryIndex S + 1))) :
    ∀ k, entryIndex S ≤ k → indNeg (A k) ≤ 1 := by
  have h0 := indNeg_entry_of_flank hF m hfl hnz
  have hEntry : indNeg (A (entryIndex S)) ≤ 1 := by
    omega
  exact adaptive_band_from_entry A v hSym hStep (entryIndex S) hEntry

end RH
