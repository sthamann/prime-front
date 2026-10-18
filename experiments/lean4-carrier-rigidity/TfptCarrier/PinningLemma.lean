/-
  PinningLemma — the v730 pinning lemma skeleton, exact rational form.
  ====================================================================

  Machine-checked algebraic core of the v730 lemma pair (checks P1.1,
  P1.2, PRIME.PINLEMMA.01):

    L-PIN-1 (residual bound, Wilkinson-type): for self-adjoint A and a
    vector v, dist(x*, spec(A))·‖v‖ ≤ ‖(A − x*)v‖ — the spectral
    distance is dominated by the residual norm; the v730 one-line
    proof runs through the eigen-expansion.

    L-PIN-2 (Kato–Temple, Parlett Thm 11.7.1): the sharpened bound
    via the Rayleigh quotient; its operator core is TEMPLE
    POSITIVITY — if the spectrum avoids the open interval (a, b),
    then ⟨(A − a)v, (A − b)v⟩ ≥ 0.

  Numeric counterpart: verification/v730_strat2_pinning_lemma.py
  (0 violations on 54 synthetic configs and on 598 + 535 real-window
  peaks/zeros; discovery probe
  experiments/tfpt-discovery/strat2_rp_universality… sibling
  strat2_pinning_lemma_probe.py, 12/12 PASS).

  EXACT-ARITHMETIC DESIGN.  Norms and distances involve square
  roots, so both lemmas are formalized in SQUARED, HOMOGENEOUS form —
  sqrt-free, hence exact over ℚ:

    L-PIN-1:  min_i (λ_{i₀} − x*)² · ‖v‖² ≤ ‖(A − x*)v‖²,

  and Mathlib's spectral theorem lives over ℝ/ℂ with irrational
  eigendata, so the abstract layer replaces "self-adjoint" by an
  explicit SCALED EIGENSYSTEM CERTIFICATE: vectors w_i with
  A·w_i = λ_i·w_i and the completeness identity
  Σ_i w_i w_iᵀ / d_i = 1 (d_i = ‖w_i‖²; orthonormality without
  square roots).  Both lemmas are then proved in full generality by
  a rational Parseval expansion.

  The concrete instance is the PYTHAGOREAN (3,4,5)-JACOBI matrix

      J = [[0, 3/5, 0], [3/5, 0, 4/5], [0, 4/5, 0]]

  (the 3-atom measure on nodes (−1, 0, 1) with weights (9/50, 16/25,
  9/50): β₁ = (3/5)², β₂ = (4/5)² — a Jacobi matrix whose
  symmetrised off-diagonal AND full eigensystem are rational:
  eigenvalues (1, 0, −1), eigenvectors (3, 5, 4), (4, 0, −3),
  (3, −5, 4)).  On it the v730 one-line proof engine is certified
  SYMBOLICALLY: the three-term residual identity

      (J − t)·p(t) = −(25/12)·π₃(t)·e₂       for every t : ℚ,

  p(t) = orthonormal-polynomial vector, π₃(t) = t³ − t — the residual
  of the Christoffel vector is rank-one at the last coordinate, and
  it VANISHES exactly at the nodes (exact pinning).

  Contents:
    * `parseval_pair`/`parseval_sq`: rational Parseval for a scaled
      complete eigensystem;
    * `residual_inner`: ⟨w_i, (A − x)u⟩ = (λ_i − x)⟨w_i, u⟩ (uses
      symmetry of A — the self-adjointness step of the proof);
    * `lpin_one`: **L-PIN-1** in squared homogeneous form, full
      abstract proof;
    * `temple_positivity`: **the Kato–Temple operator core** — the
      spectral-gap positivity ⟨(A − a)v, (A − b)v⟩ ≥ 0;
    * concrete certificates for `J35`: symmetry, the full rational
      eigensystem, completeness, `residual_structure` (symbolic in
      t), exact pinning at the nodes, and the instantiated bound at
      the off-node sample x* = 9/10 (`pinning_instance`,
      `pinning_radius_sample`) plus a Temple-positivity instance on
      the spectral gap (1/4, 3/4).

  HONEST SCOPE.  Formalized: the two operator-level inequalities in
  squared rational form and the v730 residual mechanism, with full
  proofs.  NOT formalized: the sqrt/norm (unsquared) statements, the
  existence of the eigensystem for a general symmetric matrix
  (Mathlib's spectral theorem is over ℝ/ℂ; here the eigensystem is a
  certificate INPUT — for the concrete J35 it is provided and
  checked), the Kato–Temple SCALAR rearrangement
  |x* − λ| ≤ |η| + r²/δ (classical algebra on top of
  `temple_positivity`; named citation gap: Parlett, The Symmetric
  Eigenvalue Problem, Thm 11.7.1), and all of v730's window/Wheeler
  layer (P1 scans, P2 comb coherence, P3 real windows).  ℚ
  arithmetic does not kernel-reduce under `decide`, so concrete
  certificates are checked by `norm_num`/`fin_cases`.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.PinningLemma

/-! ### 1. Abstract layer: rational Parseval for a scaled eigensystem -/

/-- **Rational Parseval, bilinear form**: a completeness certificate
Σ_i w_i w_iᵀ / d_i = 1 expands every inner product over the scaled
system — no square roots, exact over ℚ. -/
theorem parseval_pair {n r : ℕ} (w : Fin r → Fin n → ℚ) (d : Fin r → ℚ)
    (hcomp : ∀ a b, (∑ i, w i a * w i b / d i) = if a = b then (1 : ℚ) else 0)
    (v v' : Fin n → ℚ) :
    ∑ a, v a * v' a
      = ∑ i, (∑ a, w i a * v a) * (∑ a, w i a * v' a) / d i := by
  have expand : ∀ i : Fin r,
      (∑ a, w i a * v a) * (∑ a, w i a * v' a) / d i
        = ∑ a, ∑ b, v a * v' b * (w i a * w i b / d i) := by
    intro i
    rw [Finset.sum_mul_sum, Finset.sum_div]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl fun b _ => ?_
    ring
  calc ∑ a, v a * v' a
      = ∑ a, ∑ b, v a * v' b * (if a = b then (1 : ℚ) else 0) := by
        refine Finset.sum_congr rfl fun a _ => ?_
        simp [mul_ite, mul_one, mul_zero, Finset.sum_ite_eq]
    _ = ∑ a, ∑ b, v a * v' b * (∑ i, w i a * w i b / d i) :=
        Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => by
          rw [hcomp a b]
    _ = ∑ a, ∑ b, ∑ i, v a * v' b * (w i a * w i b / d i) :=
        Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
          Finset.mul_sum _ _ _
    _ = ∑ a, ∑ i, ∑ b, v a * v' b * (w i a * w i b / d i) :=
        Finset.sum_congr rfl fun a _ => Finset.sum_comm
    _ = ∑ i, ∑ a, ∑ b, v a * v' b * (w i a * w i b / d i) :=
        Finset.sum_comm
    _ = ∑ i, (∑ a, w i a * v a) * (∑ a, w i a * v' a) / d i :=
        Finset.sum_congr rfl fun i _ => (expand i).symm

/-- Rational Parseval, quadratic form: ‖v‖² = Σ_i ⟨w_i, v⟩² / d_i. -/
theorem parseval_sq {n r : ℕ} (w : Fin r → Fin n → ℚ) (d : Fin r → ℚ)
    (hcomp : ∀ a b, (∑ i, w i a * w i b / d i) = if a = b then (1 : ℚ) else 0)
    (v : Fin n → ℚ) :
    ∑ a, v a ^ 2 = ∑ i, (∑ a, w i a * v a) ^ 2 / d i := by
  have h := parseval_pair w d hcomp v v
  calc ∑ a, v a ^ 2 = ∑ a, v a * v a :=
        Finset.sum_congr rfl fun a _ => by ring
    _ = ∑ i, (∑ a, w i a * v a) * (∑ a, w i a * v a) / d i := h
    _ = ∑ i, (∑ a, w i a * v a) ^ 2 / d i :=
        Finset.sum_congr rfl fun i _ => by ring

/-- **Eigen-transport of the shifted residual** (the self-adjointness
step of the v730 one-line proof): if A is symmetric and
A·w = λ·w, then ⟨w, (A − x)u⟩ = (λ − x)·⟨w, u⟩ for every u. -/
theorem residual_inner {n : ℕ} (A : Matrix (Fin n) (Fin n) ℚ)
    (hA : A.transpose = A) (lam : ℚ) (wv : Fin n → ℚ)
    (hev : A.mulVec wv = lam • wv) (x : ℚ) (u : Fin n → ℚ) :
    (∑ a, wv a * ((A - x • 1).mulVec u) a) = (lam - x) * ∑ a, wv a * u a := by
  have hAe : ∀ a b : Fin n, A b a = A a b := fun a b => by
    conv_lhs => rw [← hA]
    rfl
  have hres : ∀ a, ((A - x • 1).mulVec u) a = (∑ b, A a b * u b) - x * u a := by
    intro a
    rw [Matrix.sub_mulVec]
    simp [Matrix.mulVec, dotProduct, Matrix.smul_apply, Matrix.one_apply,
      mul_ite, Finset.sum_ite_eq, smul_eq_mul]
  have hevA : ∀ b, (∑ a, A a b * wv a) = lam * wv b := by
    intro b
    have h1 : (A.mulVec wv) b = lam * wv b := by
      rw [hev]; simp [Pi.smul_apply, smul_eq_mul]
    calc (∑ a, A a b * wv a) = ∑ a, A b a * wv a :=
          Finset.sum_congr rfl fun a _ => by rw [hAe a b]
      _ = (A.mulVec wv) b := by simp [Matrix.mulVec, dotProduct]
      _ = lam * wv b := h1
  calc ∑ a, wv a * ((A - x • 1).mulVec u) a
      = ∑ a, (wv a * ∑ b, A a b * u b) - ∑ a, wv a * (x * u a) := by
        rw [← Finset.sum_sub_distrib]
        refine Finset.sum_congr rfl fun a _ => ?_
        rw [hres a]; ring
    _ = (∑ b, (∑ a, A a b * wv a) * u b) - x * ∑ a, wv a * u a := by
        congr 1
        · calc ∑ a, (wv a * ∑ b, A a b * u b)
              = ∑ a, ∑ b, A a b * wv a * u b := by
                refine Finset.sum_congr rfl fun a _ => ?_
                rw [Finset.mul_sum]
                exact Finset.sum_congr rfl fun b _ => by ring
            _ = ∑ b, ∑ a, A a b * wv a * u b := Finset.sum_comm
            _ = ∑ b, (∑ a, A a b * wv a) * u b :=
                Finset.sum_congr rfl fun b _ => (Finset.sum_mul _ _ _).symm
        · rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun a _ => by ring
    _ = (∑ b, (lam * wv b) * u b) - x * ∑ a, wv a * u a := by
        have hs : (∑ b, (∑ a, A a b * wv a) * u b) = ∑ b, (lam * wv b) * u b :=
          Finset.sum_congr rfl fun b _ => by rw [hevA b]
        rw [hs]
    _ = (lam - x) * ∑ a, wv a * u a := by
        have hs : (∑ b, (lam * wv b) * u b) = lam * ∑ b, wv b * u b := by
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun b _ => by ring
        rw [hs, sub_mul]

/-- **L-PIN-1** (v730, squared homogeneous form): for a matrix with a
complete scaled rational eigensystem, if λ_{i₀} is the nearest
spectral point to x*, then

    (λ_{i₀} − x*)² · ‖u‖² ≤ ‖(A − x*)u‖²   for EVERY u

— the spectral distance is dominated by the residual norm
(Wilkinson-type residual bound; the one-line eigen-expansion proof,
fully formal). -/
theorem lpin_one {n r : ℕ} (A : Matrix (Fin n) (Fin n) ℚ)
    (hA : A.transpose = A) (w : Fin r → Fin n → ℚ) (d lam : Fin r → ℚ)
    (hd : ∀ i, 0 < d i)
    (hev : ∀ i, A.mulVec (w i) = lam i • w i)
    (hcomp : ∀ a b, (∑ i, w i a * w i b / d i) = if a = b then (1 : ℚ) else 0)
    (x : ℚ) (u : Fin n → ℚ) (i0 : Fin r)
    (hmin : ∀ i, (lam i0 - x) ^ 2 ≤ (lam i - x) ^ 2) :
    (lam i0 - x) ^ 2 * (∑ a, u a ^ 2)
      ≤ ∑ a, ((A - x • 1).mulVec u) a ^ 2 := by
  rw [parseval_sq w d hcomp u, parseval_sq w d hcomp ((A - x • 1).mulVec u),
    Finset.mul_sum]
  refine Finset.sum_le_sum fun i _ => ?_
  rw [residual_inner A hA (lam i) (w i) (hev i) x u]
  have hdne : d i ≠ 0 := (hd i).ne'
  have hkey : ((lam i - x) * ∑ a, w i a * u a) ^ 2 / d i
      = (lam i - x) ^ 2 * ((∑ a, w i a * u a) ^ 2 / d i) := by
    field_simp
  rw [hkey]
  exact mul_le_mul_of_nonneg_right (hmin i)
    (div_nonneg (sq_nonneg _) (hd i).le)

/-- **Temple positivity — the Kato–Temple operator core** (v730
L-PIN-2 mechanism): if the whole spectrum avoids the open interval
(a, b) — i.e. (λ_i − a)(λ_i − b) ≥ 0 for all i — then
⟨(A − a)u, (A − b)u⟩ ≥ 0 for every u.  The classical Kato–Temple
bound is the scalar rearrangement of this inequality at the Rayleigh
quotient (citation gap: Parlett Thm 11.7.1). -/
theorem temple_positivity {n r : ℕ} (A : Matrix (Fin n) (Fin n) ℚ)
    (hA : A.transpose = A) (w : Fin r → Fin n → ℚ) (d lam : Fin r → ℚ)
    (hd : ∀ i, 0 < d i)
    (hev : ∀ i, A.mulVec (w i) = lam i • w i)
    (hcomp : ∀ a b, (∑ i, w i a * w i b / d i) = if a = b then (1 : ℚ) else 0)
    (aa bb : ℚ) (u : Fin n → ℚ)
    (hgap : ∀ i, 0 ≤ (lam i - aa) * (lam i - bb)) :
    0 ≤ ∑ c, ((A - aa • 1).mulVec u) c * ((A - bb • 1).mulVec u) c := by
  rw [parseval_pair w d hcomp ((A - aa • 1).mulVec u) ((A - bb • 1).mulVec u)]
  refine Finset.sum_nonneg fun i _ => ?_
  rw [residual_inner A hA (lam i) (w i) (hev i) aa u,
    residual_inner A hA (lam i) (w i) (hev i) bb u]
  have hdne : d i ≠ 0 := (hd i).ne'
  have hkey : ((lam i - aa) * ∑ a, w i a * u a)
        * ((lam i - bb) * ∑ a, w i a * u a) / d i
      = ((lam i - aa) * (lam i - bb)) * ((∑ a, w i a * u a) ^ 2 / d i) := by
    field_simp
  rw [hkey]
  exact mul_nonneg (hgap i) (div_nonneg (sq_nonneg _) (hd i).le)

/-! ### 2. Concrete instance: the Pythagorean (3,4,5)-Jacobi matrix -/

/-- The (3,4,5)-Jacobi matrix: β₁ = (3/5)², β₂ = (4/5)² — the 3-atom
measure on (−1, 0, 1) with weights (9/50, 16/25, 9/50); the ONLY
symmetric 3×3 Jacobi shape whose off-diagonal AND eigensystem are
simultaneously rational is the Pythagorean slice β₁ + β₂ = 1. -/
def J35 : Matrix (Fin 3) (Fin 3) ℚ := !![0, 3/5, 0; 3/5, 0, 4/5; 0, 4/5, 0]

/-- The rational eigenvectors (unnormalised): (3, 5, 4), (4, 0, −3),
(3, −5, 4). -/
def eigVec : Fin 3 → Fin 3 → ℚ := ![![3, 5, 4], ![4, 0, -3], ![3, -5, 4]]

/-- The eigenvalues (= quadrature nodes = atoms): (1, 0, −1). -/
def eigVal : Fin 3 → ℚ := ![1, 0, -1]

/-- The squared norms ‖w_i‖² = (50, 25, 50). -/
def eigNorm : Fin 3 → ℚ := ![50, 25, 50]

/-- Symmetry certificate. -/
theorem J35_symm : J35.transpose = J35 := by
  ext a b
  fin_cases a <;> fin_cases b <;> norm_num [J35, Matrix.transpose_apply]

/-- Norm positivity. -/
theorem eigNorm_pos : ∀ i, 0 < eigNorm i := by
  intro i; fin_cases i <;> norm_num [eigNorm]

/-- Eigenvector certificates: J·w_i = λ_i·w_i, entrywise in ℚ. -/
theorem eig_cert : ∀ i, J35.mulVec (eigVec i) = eigVal i • eigVec i := by
  intro i
  fin_cases i <;>
    · funext a
      fin_cases a <;>
        norm_num [J35, eigVec, eigVal, Matrix.mulVec, dotProduct,
          Fin.sum_univ_three, Pi.smul_apply, smul_eq_mul,
          Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- Squared-norm certificates: ‖w_i‖² = d_i. -/
theorem eigNorm_cert : ∀ i, (∑ a, eigVec i a ^ 2) = eigNorm i := by
  intro i
  fin_cases i <;>
    norm_num [eigVec, eigNorm, Fin.sum_univ_three, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]

/-- Completeness certificate: Σ_i w_i w_iᵀ / d_i = 1 (rational
resolution of the identity — orthonormality without square roots). -/
theorem eig_complete : ∀ a b : Fin 3,
    (∑ i, eigVec i a * eigVec i b / eigNorm i)
      = if a = b then (1 : ℚ) else 0 := by
  intro a b
  fin_cases a <;> fin_cases b <;>
    norm_num [eigVec, eigNorm, Fin.sum_univ_three, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]

/-- The orthonormal-polynomial (Christoffel) vector of the measure:
p(t) = (p₀, p₁, p₂)(t) = (1, 5t/3, (25t² − 9)/12). -/
def pVec (t : ℚ) : Fin 3 → ℚ := ![1, 5/3 * t, (25 * t ^ 2 - 9) / 12]

/-- π₃(t) = t³ − t: the monic degree-3 orthogonal polynomial — its
roots are exactly the nodes (−1, 0, 1). -/
def pi3 (t : ℚ) : ℚ := t ^ 3 - t

/-- The Christoffel kernel K(t, t) = Σ_k p_k(t)². -/
def christoffel (t : ℚ) : ℚ := ∑ a, pVec t a ^ 2

/-- **The v730 residual structure, symbolic** (the proof engine of
L-PIN-1): for EVERY t : ℚ,

    (J − t)·p(t) = −(25/12)·π₃(t)·e₂

— the three-term recursion makes the residual of the Christoffel
vector rank-one at the last coordinate, with coefficient the
next orthogonal polynomial. -/
theorem residual_structure (t : ℚ) :
    (J35 - t • 1).mulVec (pVec t) = (-(25/12) * pi3 t) • ![0, 0, 1] := by
  have e0 : ((J35 - t • 1).mulVec (pVec t)) 0
      = ((-(25/12) * pi3 t) • (![0, 0, 1] : Fin 3 → ℚ)) 0 := by
    norm_num +decide [J35, pVec, pi3, Matrix.mulVec, dotProduct,
      Fin.sum_univ_three, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, Pi.smul_apply, smul_eq_mul, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]
    ring
  have e1 : ((J35 - t • 1).mulVec (pVec t)) 1
      = ((-(25/12) * pi3 t) • (![0, 0, 1] : Fin 3 → ℚ)) 1 := by
    norm_num +decide [J35, pVec, pi3, Matrix.mulVec, dotProduct,
      Fin.sum_univ_three, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, Pi.smul_apply, smul_eq_mul, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]
    ring
  have e2 : ((J35 - t • 1).mulVec (pVec t)) 2
      = ((-(25/12) * pi3 t) • (![0, 0, 1] : Fin 3 → ℚ)) 2 := by
    norm_num +decide [J35, pVec, pi3, Matrix.mulVec, dotProduct,
      Fin.sum_univ_three, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, Pi.smul_apply, smul_eq_mul, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]
    ring
  funext a
  fin_cases a
  · exact e0
  · exact e1
  · exact e2

/-- **Exact pinning at the nodes**: at t ∈ {−1, 0, 1} the residual
vanishes (π₃ = 0), so the Christoffel vector is an EXACT eigenvector
— the quadrature nodes are pinned with zero certificate radius. -/
theorem node_exact_pinning :
    J35.mulVec (pVec 1) = (1 : ℚ) • pVec 1 ∧
    J35.mulVec (pVec 0) = (0 : ℚ) • pVec 0 ∧
    J35.mulVec (pVec (-1)) = (-1 : ℚ) • pVec (-1) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    · funext a
      fin_cases a <;>
        norm_num [J35, pVec, Matrix.mulVec, dotProduct,
          Fin.sum_univ_three, Pi.smul_apply, smul_eq_mul,
          Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- L-PIN-1 instantiated at J35: the abstract theorem with all
certificates discharged — valid for EVERY x* and every u. -/
theorem lpin_one_J35 (x : ℚ) (u : Fin 3 → ℚ) (i0 : Fin 3)
    (hmin : ∀ i, (eigVal i0 - x) ^ 2 ≤ (eigVal i - x) ^ 2) :
    (eigVal i0 - x) ^ 2 * (∑ a, u a ^ 2)
      ≤ ∑ a, ((J35 - x • 1).mulVec u) a ^ 2 :=
  lpin_one J35 J35_symm eigVec eigNorm eigVal eigNorm_pos eig_cert
    eig_complete x u i0 hmin

/-- Nearest-node certificate at the off-node sample x* = 9/10:
the nearest spectral point is λ = 1 (distance 1/10). -/
theorem sample_min_cert :
    ∀ i, (eigVal 0 - (9/10 : ℚ)) ^ 2 ≤ (eigVal i - (9/10 : ℚ)) ^ 2 := by
  intro i; fin_cases i <;> norm_num [eigVal]

/-- **Certified pinning instance** at x* = 9/10: for every u,
(1/100)·‖u‖² ≤ ‖(J − 9/10)u‖² — the L-PIN-1 bound with concrete
nearest-node distance 1/10. -/
theorem pinning_instance (u : Fin 3 → ℚ) :
    (1/100 : ℚ) * (∑ a, u a ^ 2)
      ≤ ∑ a, ((J35 - (9/10 : ℚ) • 1).mulVec u) a ^ 2 := by
  have h := lpin_one_J35 (9/10) u 0 sample_min_cert
  have he : (eigVal 0 - (9/10 : ℚ)) ^ 2 = 1/100 := by norm_num [eigVal]
  rw [he] at h
  exact h

/-- **The certified pinning radius** at x* = 9/10 (v730's r_K(x*)):
plugging the Christoffel vector into the instance and evaluating the
residual by `residual_structure` gives

    dist² · K(x*) ≤ (25/12)²·π₃(x*)²

— the fully rational form of dist(x*, nodes) ≤ √(g)·|p_K(x*)|/√K. -/
theorem pinning_radius_sample :
    (1/100 : ℚ) * christoffel (9/10) ≤ (25/12) ^ 2 * pi3 (9/10) ^ 2 := by
  have h := pinning_instance (pVec (9/10))
  have hres : (∑ a, ((J35 - (9/10 : ℚ) • 1).mulVec (pVec (9/10))) a ^ 2)
      = (25/12) ^ 2 * pi3 (9/10) ^ 2 := by
    rw [residual_structure]
    norm_num [pi3, Fin.sum_univ_three, Pi.smul_apply, smul_eq_mul,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
  rw [christoffel]
  rw [← hres]
  exact h

/-- Explicit sample values: K(9/10) = 1057/256 and
π₃(9/10) = −171/1000 (so the certified radius² is 3249/105700 —
the probe's r_K² anatomy, exact). -/
theorem sample_values :
    christoffel (9/10) = 1057/256 ∧ pi3 (9/10 : ℚ) = -(171/1000) := by
  constructor <;>
    norm_num [christoffel, pVec, pi3, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- Spectral-gap certificate for the interval (1/4, 3/4): the
spectrum {1, 0, −1} avoids it. -/
theorem gap_cert : ∀ i, 0 ≤ (eigVal i - 1/4) * (eigVal i - 3/4) := by
  intro i; fin_cases i <;> norm_num [eigVal]

/-- **Temple-positivity instance** (the Kato–Temple core at J35): for
every u, ⟨(J − 1/4)u, (J − 3/4)u⟩ ≥ 0 — the spectrum avoids
(1/4, 3/4), so the shifted quadratic form is positive. -/
theorem temple_instance (u : Fin 3 → ℚ) :
    0 ≤ ∑ c, ((J35 - (1/4 : ℚ) • 1).mulVec u) c
        * ((J35 - (3/4 : ℚ) • 1).mulVec u) c :=
  temple_positivity J35 J35_symm eigVec eigNorm eigVal eigNorm_pos
    eig_cert eig_complete (1/4) (3/4) u gap_cert

end TfptCarrier.PinningLemma
