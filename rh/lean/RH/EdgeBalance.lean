/-
RH/EdgeBalance.lean -- r426: the edge-balance chain (r417–r424, with
the r425 reduction of γ < 1) as sorry-free finite real algebra.

Abstract forms only (no window / source objects).  Targets:

  (a) Woodbury-sch as a corollary of the r406 OneDefect identities
      (`oneDefectDelta_eq_woodbury` / `oneDefect_update_posDef_iff`).
      The campaign scalar is
        `sch = den − 2 + sᵀ (H + U Uᵀ)⁻¹ s`,
      which is `(den − 1) − Δ` for `J = I`.  At `den = 1` this is
      exactly the one-defect PosDef criterion.
  (b) Chart trichotomy: the Schur complement of a 2×2 signature
      `J₂ = diag(ε_a, ε_b)`, `ε ∈ {±1}`, in the 3×3 block is
        `sch = φ − (ε_a ã² + ε_b b̃²)`
      (since `J₂⁻¹ = J₂`).  Three branches:
        P1      `ε = (−1, +1)`  `sch = φ + ã² − b̃²`
        vacuous `ε = (+1, +1)`  `sch = φ − (ã² + b̃²)`
        tot     `ε = (−1, −1)`  `sch = φ + ã² + b̃²`.
  (c) Vacuous τ²-separator: `sch < 0 ↔ τ² > φ` on the vacuous chart
      (τ² := ã² + b̃²).  In particular `φ < 0` forces `sch < 0`
      for every coupling.
  (d) den formula: `den = 1 + γ − v_t·s` with `γ = ‖b‖²/B_w`, and
        `den < 2 ↔ γ < 1 + v_t·s`.
      The bridge `γ < 1 ∧ v_t·s ≥ 0 ⇒ den < 2` is the r423
      implication.  `γ < 1` itself follows from `‖b‖² ≤ S < B_w`
      (r425: the first comparison is kernel Loewner, named; the
      second is `q_N < 1`, named).

Named Props (not `sorry`): `BorderIsMuParseval` (r424 identification),
`BorderLoewnerLeS` (r425 kernel comparison), `QNLtOne` (cofinal
`q_N < 1`; already the v960 census, not cofinal).  Census of the
pilot stays 5.  Does not assert (P1)/(P2), L*, or any window census.
Zero `sorry`.  NO RH CLAIM.

Provenance: r417–r425 sealed probes; PRIME.RDAGGER.EDGE_BALANCE_LEAN.01.
-/
import RH.OneDefect
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace RH

open Matrix BigOperators

variable {n : Type*} [Fintype n] [DecidableEq n]
variable {k : Type*} [Fintype k] [DecidableEq k]

/-! ## (a) Woodbury-sch, corollary of OneDefect -/

/-- Campaign Schur scalar in Woodbury form
`sch = den − 2 + sᵀ (H + U Uᵀ)⁻¹ s` (r417). -/
noncomputable def schWoodbury (den : ℝ) (H : Matrix n n ℝ)
    (U : Matrix n k ℝ) (s : n → ℝ) : ℝ :=
  den - 2 + s ⬝ᵥ ((H + U * Uᵀ)⁻¹ *ᵥ s)

/-- Border-border entry `φ_bb = den − 2 + sᵀ H⁻¹ s` (r418). -/
noncomputable def phiBB (den : ℝ) (H : Matrix n n ℝ) (s : n → ℝ) : ℝ :=
  den - 2 + s ⬝ᵥ (H⁻¹ *ᵥ s)

/-- Last-slot contribution `c_J = den − 2`. -/
def cJ (den : ℝ) : ℝ := den - 2

/-- Self-energy `Σ = sᵀ H⁻¹ s`. -/
noncomputable def selfEnergy (H : Matrix n n ℝ) (s : n → ℝ) : ℝ :=
  s ⬝ᵥ (H⁻¹ *ᵥ s)

/-- **r418 split.**  `φ_bb = c_J + Σ` on every chart. -/
theorem phiBB_eq_cJ_add_selfEnergy (den : ℝ) (H : Matrix n n ℝ)
    (s : n → ℝ) : phiBB den H s = cJ den + selfEnergy H s := by
  simp [phiBB, cJ, selfEnergy]

lemma mul_one_mul_transpose (U : Matrix n k ℝ) :
    U * (1 : Matrix k k ℝ) * Uᵀ = U * Uᵀ := by
  rw [Matrix.mul_one]

/-- **(a)** Woodbury-sch is the OneDefect discriminant with `J = I`:
`sch = (den − 1) − Δ`.  Specializes `oneDefectDelta_eq_woodbury`. -/
theorem schWoodbury_eq_oneDefectDelta {H : Matrix n n ℝ} (hH : H.PosDef)
    (U : Matrix n k ℝ) (s : n → ℝ) (den : ℝ) :
    schWoodbury den H U s =
      (den - 1) - oneDefectDelta H (1 : Matrix k k ℝ) U s := by
  have hJ : (1 : Matrix k k ℝ).PosDef := PosDef.one
  have hΔ := oneDefectDelta_eq_woodbury hH hJ U s
  have hU : U * (1 : Matrix k k ℝ) * Uᵀ = U * Uᵀ :=
    mul_one_mul_transpose U
  have hQ :
      s ⬝ᵥ ((H + U * Uᵀ)⁻¹ *ᵥ s) =
        1 - oneDefectDelta H (1 : Matrix k k ℝ) U s := by
    have hΔ' : oneDefectDelta H (1 : Matrix k k ℝ) U s =
        1 - s ⬝ᵥ ((H + U * (1 : Matrix k k ℝ) * Uᵀ)⁻¹ *ᵥ s) := hΔ
    rw [hU] at hΔ'
    linarith
  simp only [schWoodbury, hQ]
  ring

/-- At `den = 1`, `sch < 0` is the r406 one-defect PosDef criterion. -/
theorem schWoodbury_one_neg_iff_update {H : Matrix n n ℝ} (hH : H.PosDef)
    (U : Matrix n k ℝ) (s : n → ℝ) :
    schWoodbury 1 H U s < 0 ↔
      (H - vecMulVec s s + U * (1 : Matrix k k ℝ) * Uᵀ).PosDef := by
  have hJ : (1 : Matrix k k ℝ).PosDef := PosDef.one
  have hiff := oneDefect_update_posDef_iff hH hJ U s
  have hsch :
      schWoodbury 1 H U s = -oneDefectDelta H (1 : Matrix k k ℝ) U s := by
    have h := schWoodbury_eq_oneDefectDelta hH U s 1
    linarith
  constructor
  · intro hneg
    have : 0 < oneDefectDelta H (1 : Matrix k k ℝ) U s := by linarith
    exact hiff.mpr this
  · intro hPD
    have : 0 < oneDefectDelta H (1 : Matrix k k ℝ) U s := hiff.mp hPD
    linarith

/-- **r417 Woodbury = Schur.**  `sch = φ_bb − rᵀ K⁻¹ r` with
`r = Uᵀ H⁻¹ s` and `K = I + Uᵀ H⁻¹ U`. -/
theorem schWoodbury_eq_phiBB_sub {H : Matrix n n ℝ} (hH : H.PosDef)
    (U : Matrix n k ℝ) (s : n → ℝ) (den : ℝ) :
    let r := Uᵀ *ᵥ (H⁻¹ *ᵥ s)
    let K := (1 : Matrix k k ℝ)⁻¹ + Uᵀ * H⁻¹ * U
    schWoodbury den H U s = phiBB den H s - r ⬝ᵥ (K⁻¹ *ᵥ r) := by
  intro r K
  have hsch := schWoodbury_eq_oneDefectDelta hH U s den
  have hΔ :
      oneDefectDelta H (1 : Matrix k k ℝ) U s =
        1 - s ⬝ᵥ (H⁻¹ *ᵥ s) + r ⬝ᵥ (K⁻¹ *ᵥ r) := by
    simp [oneDefectDelta, r, K]
  rw [hsch, hΔ, phiBB]
  ring

/-! ## (b) Chart trichotomy (3×3 Schur of a signature block) -/

/-- The three 2×2 signatures of the mixed Haynsworth chart. -/
inductive ChartBranch
  | p1
  | vacuous
  | tot

/-- Unnormalized Sylvester Schur of the 3×3 chart block. -/
def schChart : ChartBranch → ℝ → ℝ → ℝ → ℝ
  | .p1, φ, a, b => φ + a ^ 2 - b ^ 2
  | .vacuous, φ, a, b => φ - (a ^ 2 + b ^ 2)
  | .tot, φ, a, b => φ + a ^ 2 + b ^ 2

/-- Signature entries `ε ∈ {±1}` of `J₂ = diag(ε_a, ε_b)`. -/
def chartEps : ChartBranch → ℝ × ℝ
  | .p1 => (-1, 1)
  | .vacuous => (1, 1)
  | .tot => (-1, -1)

theorem chartEps_sq (br : ChartBranch) :
    (chartEps br).1 ^ 2 = 1 ∧ (chartEps br).2 ^ 2 = 1 := by
  cases br <;> simp [chartEps]

/-- **(b)** The 3×3 Schur of `diag(ε_a, ε_b)` is
`φ − (ε_a ã² + ε_b b̃²)`.  Because `ε² = 1` one has `J₂⁻¹ = J₂`. -/
theorem schChart_eq_eps (br : ChartBranch) (φ a b : ℝ) :
    schChart br φ a b =
      φ - ((chartEps br).1 * a ^ 2 + (chartEps br).2 * b ^ 2) := by
  cases br <;> simp [schChart, chartEps] <;> ring

theorem schChart_p1 (φ a b : ℝ) :
    schChart .p1 φ a b = φ + a ^ 2 - b ^ 2 :=
  rfl

theorem schChart_vacuous (φ a b : ℝ) :
    schChart .vacuous φ a b = φ - (a ^ 2 + b ^ 2) :=
  rfl

theorem schChart_tot (φ a b : ℝ) :
    schChart .tot φ a b = φ + a ^ 2 + b ^ 2 :=
  rfl

/-! ## (c) Vacuous τ²-separator -/

/-- Unnormalized coupling radius `τ² = ã² + b̃²`. -/
def tauSq (a b : ℝ) : ℝ := a ^ 2 + b ^ 2

theorem tauSq_nonneg (a b : ℝ) : 0 ≤ tauSq a b :=
  add_nonneg (sq_nonneg a) (sq_nonneg b)

/-- **(c)** On the vacuous chart, `sch < 0 ↔ τ² > φ`. -/
theorem vacuous_sch_neg_iff (φ a b : ℝ) :
    schChart .vacuous φ a b < 0 ↔ tauSq a b > φ := by
  simp only [schChart, tauSq]
  constructor <;> intro h <;> linarith

/-- On the vacuous chart, `φ < 0` makes the whole disk live:
couplings cannot kill the sign (r417/r419). -/
theorem vacuous_live_of_phi_neg (a b : ℝ) {φ : ℝ} (hφ : φ < 0) :
    schChart .vacuous φ a b < 0 :=
  (vacuous_sch_neg_iff φ a b).mpr (lt_of_lt_of_le hφ (tauSq_nonneg a b))

/-! ## (d) den formula and the γ-bridge -/

/-- Occupation ratio `γ = ‖b‖² / B_w`. -/
noncomputable def gammaOf (bSq Bw : ℝ) : ℝ := bSq / Bw

/-- Border normalisation `den = 1 + γ − v_t·s` (r420/r423). -/
def denOf (γ vts : ℝ) : ℝ := 1 + γ - vts

theorem denOf_eq (bSq Bw vts : ℝ) :
    denOf (gammaOf bSq Bw) vts = 1 + bSq / Bw - vts :=
  rfl

/-- **(d)** `den < 2 ↔ γ < 1 + v_t·s`. -/
theorem den_lt_two_iff (γ vts : ℝ) :
    denOf γ vts < 2 ↔ γ < 1 + vts := by
  simp only [denOf]
  constructor <;> intro h <;> linarith

/-- r423 bridge: `γ < 1` and a nonnegative border correction give
`den < 2`.  The measured `v_t·s > 0` only widens the gap. -/
theorem den_lt_two_of_gamma_lt_one {γ vts : ℝ}
    (hγ : γ < 1) (hv : 0 ≤ vts) : denOf γ vts < 2 :=
  (den_lt_two_iff γ vts).mpr (by linarith)

/-- `γ < 1` follows from `‖b‖² ≤ S < B_w` (r425 composition). -/
theorem gamma_lt_one_of_le_S_lt_Bw {bSq S Bw : ℝ}
    (hBw : 0 < Bw) (hle : bSq ≤ S) (hlt : S < Bw) :
    gammaOf bSq Bw < 1 := by
  have hlt' : bSq < Bw := lt_of_le_of_lt hle hlt
  exact (div_lt_one hBw).mpr hlt'

/-- Composed r423+r425 bridge: Loewner `‖b‖² ≤ S` plus `S < B_w`
plus a nonnegative correction give `den < 2`. -/
theorem den_lt_two_of_le_S_lt_Bw {bSq S Bw vts : ℝ}
    (hBw : 0 < Bw) (hle : bSq ≤ S) (hlt : S < Bw) (hv : 0 ≤ vts) :
    denOf (gammaOf bSq Bw) vts < 2 :=
  den_lt_two_of_gamma_lt_one (gamma_lt_one_of_le_S_lt_Bw hBw hle hlt) hv

/-! ## Named remainders (hypothesis form, not `sorry`)

The proved layer never consumes a window object.  The three names
below are the r424/r425 source identifications, same class as
`P1EqCapInertia`: they are hypotheses, not holes. -/

/-- **Named Prop (r424).**  `b` is the coefficient vector of the
signed border `σ` in a (truncated) μ-ONB frame: `b_k = ⟨σ, π̂_k⟩`.
Window transcription of the r424 SATZ; ℚ-toy `b = (3/5, 4/5)`. -/
def BorderIsMuParseval {ι κ : Type*} [Fintype ι] [Fintype κ]
    (b : κ → ℝ) (pi : κ → ι → ℝ) (σ : ι → ℝ) : Prop :=
  ∀ k, b k = σ ⬝ᵥ pi k

/-- Parseval bookkeeping: the coefficient identity implies
`‖b‖² = ∑_k ⟨σ, π̂_k⟩²`. -/
theorem parseval_normSq {ι κ : Type*} [Fintype ι] [Fintype κ]
    (b : κ → ℝ) (pi : κ → ι → ℝ) (σ : ι → ℝ)
    (h : BorderIsMuParseval b pi σ) :
    b ⬝ᵥ b = ∑ k, (σ ⬝ᵥ pi k) ^ 2 := by
  unfold BorderIsMuParseval at h
  simp [dotProduct, pow_two, h]

/-- **Named Prop (r425).**  `‖b‖² ≤ S` — the Loewner comparison
`K_μ ≼ K_{μ−ν}` on `P_<N`, as a hypothesis on a campaign pair. -/
def BorderLoewnerLeS {κ : Type*} [Fintype κ] (b : κ → ℝ) (S : ℝ) : Prop :=
  b ⬝ᵥ b ≤ S

/-- **Named Prop (r425 remainder).**  `S < B_w`, equivalently
`q_N < 1` on the r425 dictionary `B_w = S` iff `q_N = 1`.
Cofinality is the existing mincut, not a new `sorry`. -/
def QNLtOne (S Bw : ℝ) : Prop := S < Bw

/-- Named composition: Parseval/Loewner plus `q_N < 1` give `γ < 1`. -/
theorem gamma_lt_one_of_named {κ : Type*} [Fintype κ]
    (b : κ → ℝ) (S Bw : ℝ) (hBw : 0 < Bw)
    (hL : BorderLoewnerLeS b S) (hQ : QNLtOne S Bw) :
    gammaOf (b ⬝ᵥ b) Bw < 1 :=
  gamma_lt_one_of_le_S_lt_Bw hBw hL hQ

end RH
