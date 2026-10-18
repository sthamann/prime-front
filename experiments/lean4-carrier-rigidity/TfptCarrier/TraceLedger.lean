/-
  TraceLedger — the finite Gauss-quadrature trace formula, exact ledger kernel.
  ============================================================================

  Machine-checked algebraic core of the v719 F1 ledger (check F1,
  PRIME.MOONSHOT.05): on every finite truncation the Gauss-quadrature
  identity

      tr p(J_K) = Σ_i w_i p(x_i) = Σ_d a_d m_d      (deg p ≤ 2K−1)

  holds EXACTLY — the spectral side (nodes/weights) and the geometric
  side (moment ledger) are the same number.  Numeric counterpart:
  verification/v719_moonshot_traceformula.py (F1, max rel dev 1.7e-11
  over 9 windows × 14 battery vectors; discovery probe
  experiments/tfpt-discovery/moonshot_traceformula_probe.py, 24/24 PASS).

  EXACT-ARITHMETIC DESIGN.  Nodes and weights of a Gauss rule are
  algebraic (roots of the orthogonal polynomial), so the certificate
  works on the MOMENT side, where everything is rational:

    * the Jacobi matrix is kept in MONIC (non-symmetric tridiagonal)
      form T with sub-diagonal 1, diagonal α_k, super-diagonal β_k —
      over ℚ this matrix is exactly rational (the symmetrised form
      needs √β and is NOT);
    * "tr" is the GNS/quadrature state τ(f) = ⟨e₀, f(T) e₀⟩ = (f(T))₀₀
      (the cyclic-vector state of the truncation, v719's ledger trace);
      the genuine matrix trace tr(T^m) = Σ_i x_i^m (unweighted node
      power sums) is certified separately;
    * the general layer proves, by induction on m from an INTERTWINING
      CERTIFICATE V·T = diag(x)·V (V = the monic orthogonal polynomials
      evaluated at the nodes — the three-term recursion in matrix
      form), that state moments = measure moments and matrix trace =
      node power sums, for ALL m at full capture;
    * the concrete instance is the 4-atom rational family
      x = (−2, −1, 1, 2), w = (1/6, 1/3, 1/3, 1/6) with moments
      m = (1, 0, 2, 0, 6, 0, 22, …), monic Jacobi data α = 0,
      β = (2, 1, 2); the K = 3 truncation reproduces m_0 … m_5
      (degree 2K−1 = 5) and MUST-FAILS at m_6 (18 ≠ 22) — Gauss
      exactness is sharp.

  Contents:
    * `intertwine_pow`: V·T = D·V ⟹ V·T^m = D^m·V (induction — the
      three-term recursion transported to all powers);
    * `three_term_intertwine`: the three-term recursion certificates
      (x·π_k = π_{k+1} + α_k π_k + β_k π_{k−1} at every node, last
      column: π_K(node) = 0) imply the intertwining — Jacobi structure
      ⟹ moments = traces;
    * `state_moments`: (T^m)₀₀ = Σ_i w_i x_i^m for all m, from the
      intertwining + normalisation certificates (π₀ = 1, wᵀV = e₀ᵀ);
    * `trace_powers`: tr(T^m) = Σ_i x_i^m for all m, given a rational
      inverse certificate for V (spectral trace formula);
    * `ledger_state`: the v719 ledger form — for every coefficient
      vector a, (Σ_d a_d·T^d)₀₀ = Σ_d a_d·m_d (linearity);
    * concrete certificates: `T4`/`Vmat`/`VmatInv` with all
      hypothesis certificates checked entrywise in ℚ by `norm_num`;
      headline theorems `gauss_state_trace_formula`,
      `spectral_trace_formula`, `ledger_identity` (∀ m / ∀ a);
    * truncation sharpness: `T3` power certificates,
      `trunc_exact_deg5` ((T3^m)₀₀ = m_m for m ≤ 5) and
      `trunc_sharp_deg6` ((T3^6)₀₀ = 18 ≠ 22 = m_6).

  HONEST SCOPE.  This is the FINITE rational kernel of v719 F1 only:
  point measures, monic Jacobi form, moment-side identities.  NOT
  formalized: the analytic GNS truncations of v719 (Wheeler recursion
  from deployed windows, bandlimited test functions, the POL/ATOM/ARCH
  dictionary of F1, and everything in F2/F3).  ℚ arithmetic does not
  kernel-reduce under `decide`, so concrete certificates are checked
  by `norm_num`/`fin_cases` — same exactness, no floats anywhere.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.TraceLedger

variable {R : Type*} [CommRing R]

/-! ### 1. General layer: intertwining transports the three-term recursion -/

/-- Diagonal powers, entrywise. -/
theorem diagonal_pow_apply {n : ℕ} (x : Fin n → R) :
    ∀ m : ℕ, (Matrix.diagonal x) ^ m = Matrix.diagonal fun i => x i ^ m := by
  intro m
  induction m with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, ih, Matrix.diagonal_mul_diagonal]
    congr 1
    funext i
    simp [pow_succ]

/-- **Intertwining transport** (induction on m): a one-step
intertwining certificate V·T = diag(x)·V propagates to every power —
the algebraic content of "the three-term recursion diagonalises all
moments at once". -/
theorem intertwine_pow {n K : ℕ} (T : Matrix (Fin K) (Fin K) R)
    (x : Fin n → R) (V : Matrix (Fin n) (Fin K) R)
    (h : V * T = Matrix.diagonal x * V) :
    ∀ m : ℕ, V * T ^ m = (Matrix.diagonal x) ^ m * V := by
  intro m
  induction m with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, pow_succ, ← Matrix.mul_assoc, ih, Matrix.mul_assoc, h,
      ← Matrix.mul_assoc]

/-- The monic Jacobi matrix of size 4: sub-diagonal 1, diagonal α,
super-diagonal β (the three-term recursion x·π_k = π_{k+1} + α_k π_k
+ β_k π_{k−1} as a multiplication matrix in the monic basis). -/
def jacobi4 (a0 a1 a2 a3 b1 b2 b3 : R) : Matrix (Fin 4) (Fin 4) R :=
  !![a0, b1, 0, 0;
     1, a1, b2, 0;
     0, 1, a2, b3;
     0, 0, 1, a3]

/-- **Three-term recursion ⟹ intertwining** (Jacobi structure ⟹
moments = traces): if the columns of V satisfy the three-term
recursion at every node and the LAST recursion step closes (π₄ = 0 at
every node — nodes are roots of π₄), then V intertwines the Jacobi
matrix with the node diagonal. -/
theorem three_term_intertwine {n : ℕ} (x : Fin n → R)
    (V : Matrix (Fin n) (Fin 4) R) (a0 a1 a2 a3 b1 b2 b3 : R)
    (h0 : ∀ i, x i * V i 0 = a0 * V i 0 + V i 1)
    (h1 : ∀ i, x i * V i 1 = b1 * V i 0 + a1 * V i 1 + V i 2)
    (h2 : ∀ i, x i * V i 2 = b2 * V i 1 + a2 * V i 2 + V i 3)
    (h3 : ∀ i, x i * V i 3 = b3 * V i 2 + a3 * V i 3) :
    V * jacobi4 a0 a1 a2 a3 b1 b2 b3 = Matrix.diagonal x * V := by
  have e0 : ∀ i, (V * jacobi4 a0 a1 a2 a3 b1 b2 b3) i 0 = x i * V i 0 := by
    intro i
    norm_num [jacobi4, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
    linear_combination -(h0 i)
  have e1 : ∀ i, (V * jacobi4 a0 a1 a2 a3 b1 b2 b3) i 1 = x i * V i 1 := by
    intro i
    norm_num [jacobi4, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
    linear_combination -(h1 i)
  have e2 : ∀ i, (V * jacobi4 a0 a1 a2 a3 b1 b2 b3) i 2 = x i * V i 2 := by
    intro i
    norm_num [jacobi4, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
    linear_combination -(h2 i)
  have e3 : ∀ i, (V * jacobi4 a0 a1 a2 a3 b1 b2 b3) i 3 = x i * V i 3 := by
    intro i
    norm_num [jacobi4, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
    linear_combination -(h3 i)
  ext i k
  rw [Matrix.diagonal_mul]
  fin_cases k
  · exact e0 i
  · exact e1 i
  · exact e2 i
  · exact e3 i

/-- **Gauss/GNS state reading** (v719 F1, moment side): the cyclic
state (T^m)₀₀ equals the m-th moment Σ_i w_i x_i^m, for ALL m ≥ 0,
given the intertwining plus two normalisation certificates
(π₀ ≡ 1: first column of V is 1; quadrature weights: wᵀV = e₀ᵀ,
i.e. Σ_i w_i π_k(x_i) = δ_{k0} — orthogonality to π₀). -/
theorem state_moments {r K : ℕ} (T : Matrix (Fin (K + 1)) (Fin (K + 1)) R)
    (x w : Fin r → R) (V : Matrix (Fin r) (Fin (K + 1)) R)
    (hint : V * T = Matrix.diagonal x * V)
    (hcol : ∀ i, V i 0 = 1)
    (hw : ∀ k, (∑ i, w i * V i k) = if k = 0 then 1 else 0) :
    ∀ m : ℕ, (T ^ m) 0 0 = ∑ i, w i * x i ^ m := by
  intro m
  have hVm : V * T ^ m = Matrix.diagonal (fun i => x i ^ m) * V := by
    rw [intertwine_pow T x V hint m, diagonal_pow_apply]
  have hrow : ∀ i, (∑ k, V i k * (T ^ m) k 0) = x i ^ m := by
    intro i
    have h1 : (V * T ^ m) i 0 = ∑ k, V i k * (T ^ m) k 0 := Matrix.mul_apply
    have h2 : (Matrix.diagonal (fun i => x i ^ m) * V) i 0
        = x i ^ m * V i 0 := Matrix.diagonal_mul _ _ _ _
    rw [← h1, hVm, h2, hcol i, mul_one]
  calc (T ^ m) 0 0
      = ∑ k, (if k = 0 then (1 : R) else 0) * (T ^ m) k 0 := by simp
    _ = ∑ k, (∑ i, w i * V i k) * (T ^ m) k 0 :=
        Finset.sum_congr rfl fun k _ => by rw [hw k]
    _ = ∑ k, ∑ i, w i * V i k * (T ^ m) k 0 :=
        Finset.sum_congr rfl fun k _ => Finset.sum_mul _ _ _
    _ = ∑ i, ∑ k, w i * V i k * (T ^ m) k 0 := Finset.sum_comm
    _ = ∑ i, w i * ∑ k, V i k * (T ^ m) k 0 := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun k _ => by ring
    _ = ∑ i, w i * x i ^ m :=
        Finset.sum_congr rfl fun i _ => by rw [hrow i]

/-- **Spectral trace formula** (v719 F1, spectral side): given a
rational inverse certificate for V, the genuine matrix trace of every
power is the node power sum: tr(T^m) = Σ_i x_i^m. -/
theorem trace_powers {K : ℕ} (T : Matrix (Fin K) (Fin K) R)
    (x : Fin K → R) (V Vinv : Matrix (Fin K) (Fin K) R)
    (hint : V * T = Matrix.diagonal x * V)
    (hVi : Vinv * V = 1) (hiV : V * Vinv = 1) :
    ∀ m : ℕ, (T ^ m).trace = ∑ i, x i ^ m := by
  intro m
  have h1 : T ^ m = Vinv * ((Matrix.diagonal x) ^ m * V) := by
    calc T ^ m = (Vinv * V) * T ^ m := by rw [hVi, one_mul]
      _ = Vinv * (V * T ^ m) := by rw [Matrix.mul_assoc]
      _ = Vinv * ((Matrix.diagonal x) ^ m * V) := by
          rw [intertwine_pow T x V hint m]
  rw [h1, Matrix.trace_mul_comm, Matrix.mul_assoc, hiV, mul_one,
    diagonal_pow_apply, Matrix.trace_diagonal]

/-- **The v719 ledger identity** (linearity): for every coefficient
vector a of every length, the state of the polynomial Σ_d a_d T^d is
the coefficient ledger Σ_d a_d m_d — "trace = moment combination". -/
theorem ledger_state {r K : ℕ} (T : Matrix (Fin (K + 1)) (Fin (K + 1)) R)
    (x w : Fin r → R) (V : Matrix (Fin r) (Fin (K + 1)) R)
    (hint : V * T = Matrix.diagonal x * V)
    (hcol : ∀ i, V i 0 = 1)
    (hw : ∀ k, (∑ i, w i * V i k) = if k = 0 then 1 else 0)
    (deg : ℕ) (a : Fin deg → R) :
    (∑ d, a d • T ^ (d : ℕ)) 0 0 = ∑ d, a d * ∑ i, w i * x i ^ (d : ℕ) := by
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
  exact Finset.sum_congr rfl fun d _ => by
    rw [state_moments T x w V hint hcol hw (d : ℕ)]

/-! ### 2. Concrete certificates: the 4-atom rational family -/

/-- Atoms x = (−2, −1, 1, 2). -/
def xAtoms : Fin 4 → ℚ := ![-2, -1, 1, 2]

/-- Positive weights w = (1/6, 1/3, 1/3, 1/6), normalised to m₀ = 1. -/
def wAtoms : Fin 4 → ℚ := ![1/6, 1/3, 1/3, 1/6]

/-- Moments m_m = Σ_i w_i x_i^m of the family:
(1, 0, 2, 0, 6, 0, 22, 0, 86, …). -/
def moment (m : ℕ) : ℚ := ∑ i, wAtoms i * xAtoms i ^ m

/-- Unweighted node power sums Σ_i x_i^m (the spectral trace side). -/
def powerSum (m : ℕ) : ℚ := ∑ i, xAtoms i ^ m

/-- The monic Jacobi matrix of the family: α = 0 (symmetry),
β = (2, 1, 2) — computed from the moment determinants, exact in ℚ. -/
def T4 : Matrix (Fin 4) (Fin 4) ℚ := jacobi4 0 0 0 0 2 1 2

/-- The K = 3 truncation (leading 3×3 block of `T4`). -/
def T3 : Matrix (Fin 3) (Fin 3) ℚ := !![0, 2, 0; 1, 0, 1; 0, 1, 0]

/-- V i k = π_k(x_i): the monic orthogonal polynomials π = (1, x,
x² − 2, x³ − 3x) evaluated at the atoms. -/
def Vmat : Matrix (Fin 4) (Fin 4) ℚ :=
  !![1, -2, 2, -2;
     1, -1, -1, 2;
     1, 1, -1, -2;
     1, 2, 2, 2]

/-- Exact rational inverse of `Vmat` (its first row is the Gauss
weight vector — quadrature weights from the inverse Vandermonde). -/
def VmatInv : Matrix (Fin 4) (Fin 4) ℚ :=
  !![1/6, 1/3, 1/3, 1/6;
     -1/6, -1/6, 1/6, 1/6;
     1/6, -1/6, -1/6, 1/6;
     -1/12, 1/6, -1/6, 1/12]

/-- Three-term recursion certificate, step 0: x·π₀ = 0·π₀ + π₁. -/
theorem Vmat_rec0 : ∀ i, xAtoms i * Vmat i 0 = 0 * Vmat i 0 + Vmat i 1 := by
  intro i
  fin_cases i <;>
    norm_num [xAtoms, Vmat, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- Three-term recursion certificate, step 1: x·π₁ = 2·π₀ + 0·π₁ + π₂. -/
theorem Vmat_rec1 : ∀ i,
    xAtoms i * Vmat i 1 = 2 * Vmat i 0 + 0 * Vmat i 1 + Vmat i 2 := by
  intro i
  fin_cases i <;>
    norm_num [xAtoms, Vmat, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- Three-term recursion certificate, step 2: x·π₂ = 1·π₁ + 0·π₂ + π₃. -/
theorem Vmat_rec2 : ∀ i,
    xAtoms i * Vmat i 2 = 1 * Vmat i 1 + 0 * Vmat i 2 + Vmat i 3 := by
  intro i
  fin_cases i <;>
    norm_num [xAtoms, Vmat, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- Last recursion step closes: x·π₃ = 2·π₂ + 0·π₃ — because
π₄ = (x²−1)(x²−4) vanishes at every atom (nodes = roots of π₄). -/
theorem Vmat_rec3 : ∀ i,
    xAtoms i * Vmat i 3 = 2 * Vmat i 2 + 0 * Vmat i 3 := by
  intro i
  fin_cases i <;>
    norm_num [xAtoms, Vmat, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- **The intertwining certificate**, from the three-term recursion
(general lemma instantiated — Jacobi structure at work). -/
theorem Vmat_intertwines : Vmat * T4 = Matrix.diagonal xAtoms * Vmat :=
  three_term_intertwine xAtoms Vmat 0 0 0 0 2 1 2
    Vmat_rec0 Vmat_rec1 Vmat_rec2 Vmat_rec3

/-- Normalisation: π₀ ≡ 1 (first column of V). -/
theorem Vmat_col0 : ∀ i, Vmat i 0 = 1 := by
  intro i
  fin_cases i <;>
    norm_num [Vmat, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- Quadrature-weight certificate: wᵀV = e₀ᵀ, i.e.
Σ_i w_i π_k(x_i) = δ_{k0} (orthogonality of π_k to π₀ = 1). -/
theorem weights_dual : ∀ k : Fin 4,
    (∑ i, wAtoms i * Vmat i k) = if k = 0 then 1 else 0 := by
  intro k
  fin_cases k <;>
    norm_num [wAtoms, Vmat, Fin.sum_univ_four, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

/-- Inverse certificate, left. -/
theorem VmatInv_mul : VmatInv * Vmat = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [VmatInv, Vmat, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.one_apply, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-- Inverse certificate, right. -/
theorem Vmat_mul_inv : Vmat * VmatInv = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [VmatInv, Vmat, Matrix.mul_apply, Fin.sum_univ_four,
      Matrix.one_apply, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons]

/-! ### 3. Headline theorems (K = 4, full capture: all m at once) -/

/-- **Gauss-quadrature state trace formula** (v719 F1, moment side):
(T₄^m)₀₀ = m_m for EVERY m ≥ 0 — at full capture (K = #atoms) the
ledger is exact at all degrees, not only ≤ 2K−1. -/
theorem gauss_state_trace_formula : ∀ m : ℕ, (T4 ^ m) 0 0 = moment m := by
  intro m
  exact state_moments T4 xAtoms wAtoms Vmat Vmat_intertwines
    Vmat_col0 weights_dual m

/-- **Spectral trace formula** (v719 F1, spectral side):
tr(T₄^m) = Σ_i x_i^m for every m — the matrix trace IS the node
power sum. -/
theorem spectral_trace_formula : ∀ m : ℕ, (T4 ^ m).trace = powerSum m := by
  intro m
  exact trace_powers T4 xAtoms Vmat VmatInv Vmat_intertwines
    VmatInv_mul Vmat_mul_inv m

/-- **The ledger identity** (v719 F1): for every coefficient vector a,
τ(Σ_d a_d T₄^d) = Σ_d a_d m_d — trace = moment combination, the
certifiable form of tr p(J_K) = Σ_d a_d m_d. -/
theorem ledger_identity (deg : ℕ) (a : Fin deg → ℚ) :
    (∑ d, a d • T4 ^ (d : ℕ)) 0 0 = ∑ d, a d * moment (d : ℕ) := by
  exact ledger_state T4 xAtoms wAtoms Vmat Vmat_intertwines
    Vmat_col0 weights_dual deg a

/-- Explicit ledger values: m₀ = 1, m₂ = 2, m₄ = 6, m₆ = 22 (odd
moments vanish by symmetry). -/
theorem moment_values :
    moment 0 = 1 ∧ moment 1 = 0 ∧ moment 2 = 2 ∧ moment 3 = 0 ∧
    moment 4 = 6 ∧ moment 5 = 0 ∧ moment 6 = 22 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]

/-- Explicit spectral values: tr(T₄²) = 10, tr(T₄⁴) = 34 (via the
general trace formula — no matrix powers computed by hand). -/
theorem trace_values : (T4 ^ 2).trace = 10 ∧ (T4 ^ 4).trace = 34 := by
  constructor <;>
    · rw [spectral_trace_formula]
      norm_num [powerSum, xAtoms, Fin.sum_univ_four, Matrix.cons_val_two,
        Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

/-! ### 4. Truncation sharpness (K = 3): exact up to 2K−1, fails after -/

/-- T₃² certificate. -/
theorem T3_pow2 : T3 ^ 2 = !![2, 0, 2; 0, 3, 0; 1, 0, 1] := by
  rw [pow_two]
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- T₃³ certificate. -/
theorem T3_pow3 : T3 ^ 3 = !![0, 6, 0; 3, 0, 3; 0, 3, 0] := by
  rw [pow_succ, T3_pow2]
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- T₃⁴ certificate. -/
theorem T3_pow4 : T3 ^ 4 = !![6, 0, 6; 0, 9, 0; 3, 0, 3] := by
  rw [pow_succ, T3_pow3]
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- T₃⁵ certificate. -/
theorem T3_pow5 : T3 ^ 5 = !![0, 18, 0; 9, 0, 9; 0, 9, 0] := by
  rw [pow_succ, T3_pow4]
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- T₃⁶ certificate. -/
theorem T3_pow6 : T3 ^ 6 = !![18, 0, 18; 0, 27, 0; 9, 0, 9] := by
  rw [pow_succ, T3_pow5]
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- **Gauss exactness at the truncation** (v719 F1, degree bound):
the K = 3 rule reproduces the moments of the 4-atom measure exactly
up to degree 2K−1 = 5: (T₃^m)₀₀ = m_m for m = 0, …, 5. -/
theorem trunc_exact_deg5 :
    (T3 ^ 0) 0 0 = moment 0 ∧ (T3 ^ 1) 0 0 = moment 1 ∧
    (T3 ^ 2) 0 0 = moment 2 ∧ (T3 ^ 3) 0 0 = moment 3 ∧
    (T3 ^ 4) 0 0 = moment 4 ∧ (T3 ^ 5) 0 0 = moment 5 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four, Matrix.one_apply,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
  · norm_num [pow_one, T3, moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
  · rw [T3_pow2]
    norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
  · rw [T3_pow3]
    norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
  · rw [T3_pow4]
    norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]
  · rw [T3_pow5]
    norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons]

/-- **Sharpness (must-fail control)**: at degree 6 = 2K the K = 3
rule breaks: (T₃⁶)₀₀ = 18 ≠ 22 = m₆ — Gauss exactness stops exactly
at 2K−1. -/
theorem trunc_sharp_deg6 : (T3 ^ 6) 0 0 ≠ moment 6 := by
  rw [T3_pow6]
  norm_num [moment, wAtoms, xAtoms, Fin.sum_univ_four, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

/-- T₃ is the leading principal block of T₄ (the truncation is the
corner of the full Jacobi matrix). -/
theorem T3_is_corner : ∀ i j : Fin 3,
    T3 i j = T4 (Fin.castLE (by norm_num) i) (Fin.castLE (by norm_num) j) := by
  intro i j
  fin_cases i <;> fin_cases j <;>
    norm_num [T3, T4, jacobi4, Fin.castLE, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

end TfptCarrier.TraceLedger
