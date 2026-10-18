/-
  SineGramKeystone — the sine-Gram lemma, finite exact kernel.
  ============================================================

  Machine-checked algebraic core of the v701 keystone (check S1.1,
  PRIME.KEYSTONE.01): for the moments c_m = Σ_i w_i·cos(m·θ_i) of a
  finite POSITIVE point measure on the circle, the half-integer sine
  moment form

      S[j,k] = c_{|j−k|} − c_{j+k+1}

  is EXACTLY the Gram matrix

      S[j,k] = Σ_i 2·w_i · sin((j+½)·θ_i) · sin((k+½)·θ_i),

  hence xᵀS x = Σ_i 2·w_i·⟨sinᵢ, x⟩² ≥ 0 for nonnegative weights —
  the classical product-to-sum identity 2·sin A·sin B = cos(A−B) −
  cos(A+B), certified in exact arithmetic.  Numeric counterpart:
  verification/v701_big_picture_hunt.py (S1.1, the sine-Gram lemma;
  discovery probe experiments/tfpt-discovery/big_picture_hunt_probe.py,
  11/11 PASS).

  EXACT-ARITHMETIC DESIGN.  No real trigonometry appears.  A circle
  point is a pair (c, s) in a commutative ring with c² + s² = 1 (the
  half-angle parametrisation; rational points = Pythagorean triples,
  the rational t = tan(θ/2) slice).  cos(n·φ) and sin(n·φ) are the
  Chebyshev-recursion sequences `cosSeq`/`sinSeq`; putting θ = 2·φ
  makes every half-integer sine sin((j+½)·θ) = sin((2j+1)·φ)
  POLYNOMIAL in (c, s).  All lemmas are proved over an arbitrary
  commutative ring by induction + `ring`/`linear_combination`; the
  concrete ℚ certificates are checked entrywise by `norm_num` in
  exact rational arithmetic (ℚ arithmetic does not kernel-reduce
  under `decide`, so the certificate layer is normalisation-checked
  instead — same exactness, no floats anywhere).

  Contents:
    * `cos_shift`/`sin_shift`, `cos_sin_add`, `pythagorean`: the
      angle-addition laws and cos² + sin² = 1 at every index, from
      c² + s² = 1 alone;
    * `two_sin_mul_sin`: 2·sin((d+b)φ)·sin(bφ) = cos(dφ) − cos((d+2b)φ)
      — the product-to-sum mechanism (the keystone);
    * `sine_gram_entry`: the half-integer specialisation
      2·sin((2j+1)φ)·sin((2k+1)φ) = cos(2|j−k|φ) − cos(2(j+k+1)φ);
    * `sineForm_eq_gram`: the matrix identity S = Σ_i 2wᵢ·sᵢ sᵢᵀ for
      any finite atom family on the circle (rank-≤-r Gram);
    * `gram_quadform`/`sineForm_quadform`: xᵀS x = Σ_i 2wᵢ⟨sᵢ, x⟩²
      (the Σ-of-squares representation);
    * `sineForm_psd`: 0 ≤ xᵀS x for nonnegative weights, over ℚ;
    * explicit certificates: the Pythagorean atom cos φ = 3/5
      (explicit first eight moments, explicit 4×4 sine form `Scert`,
      explicit rank-1 decomposition Scert = 2·v vᵀ) and a weighted
      three-atom instance on the triples (3,4,5), (5,12,13), (8,15,17).

  HONEST SCOPE.  This is the FINITE algebraic kernel of v701 S1.1
  only: point masses with exact circle coordinates.  NOT formalized:
  general positive measures and the FFT-quadrature limit (v701 S1.3),
  the deployed window decomposition B = odd(p) − odd(pole) and the
  index-reversal wiring (v701 S1.2 — here the half-integer sine form
  IS the definition `sineForm`), Levinson positive feasibility (v701
  S1.4), and the σ_p ≥ 0 program itself (the open L3 gate).  No RH
  statement anywhere.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.SineGramKeystone

variable {R : Type*} [CommRing R]

/-! ### 1. The Chebyshev pair on an abstract circle point -/

/-- `cosSeq c n = cos (n·φ)` for a circle point with `cos φ = c`: the
Chebyshev recursion `cos((n+2)φ) = 2c·cos((n+1)φ) − cos(nφ)`. -/
def cosSeq (c : R) : ℕ → R
  | 0 => 1
  | 1 => c
  | n + 2 => 2 * c * cosSeq c (n + 1) - cosSeq c n

/-- `sinSeq c s n = sin (n·φ)` for a circle point
`(cos φ, sin φ) = (c, s)`: the same recursion with sine initial data. -/
def sinSeq (c s : R) : ℕ → R
  | 0 => 0
  | 1 => s
  | n + 2 => 2 * c * sinSeq c s (n + 1) - sinSeq c s n

/-- One-step shift law at index m (the angle-addition step). -/
private def ShiftEq (c s : R) (m : ℕ) : Prop :=
  cosSeq c (m + 1) = c * cosSeq c m - s * sinSeq c s m ∧
  sinSeq c s (m + 1) = s * cosSeq c m + c * sinSeq c s m

private theorem shiftEq_pair (c s : R) (h : c ^ 2 + s ^ 2 = 1) :
    ∀ m : ℕ, ShiftEq c s m ∧ ShiftEq c s (m + 1) := by
  intro m
  induction m with
  | zero =>
    refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
    · show c = c * 1 - s * 0
      ring
    · show s = s * 1 + c * 0
      ring
    · show 2 * c * c - 1 = c * c - s * s
      linear_combination h
    · show 2 * c * s - 0 = s * c + c * s
      ring
  | succ n ih =>
    obtain ⟨⟨_, _⟩, ⟨hc2, hs2⟩⟩ := ih
    have hc2' : cosSeq c (n + 2)
        = c * cosSeq c (n + 1) - s * sinSeq c s (n + 1) := hc2
    have hs2' : sinSeq c s (n + 2)
        = s * cosSeq c (n + 1) + c * sinSeq c s (n + 1) := hs2
    refine ⟨⟨hc2, hs2⟩, ⟨?_, ?_⟩⟩
    · show cosSeq c (n + 3) = c * cosSeq c (n + 2) - s * sinSeq c s (n + 2)
      have e3 : cosSeq c (n + 3)
          = 2 * c * cosSeq c (n + 2) - cosSeq c (n + 1) := rfl
      rw [e3, hc2', hs2']
      linear_combination cosSeq c (n + 1) * h
    · show sinSeq c s (n + 3) = s * cosSeq c (n + 2) + c * sinSeq c s (n + 2)
      have e3 : sinSeq c s (n + 3)
          = 2 * c * sinSeq c s (n + 2) - sinSeq c s (n + 1) := rfl
      rw [e3, hc2', hs2']
      linear_combination sinSeq c s (n + 1) * h

/-- **Angle-addition shift**: cos((m+1)φ) = c·cos(mφ) − s·sin(mφ). -/
theorem cos_shift (c s : R) (h : c ^ 2 + s ^ 2 = 1) (m : ℕ) :
    cosSeq c (m + 1) = c * cosSeq c m - s * sinSeq c s m :=
  ((shiftEq_pair c s h m).1).1

/-- **Angle-addition shift**: sin((m+1)φ) = s·cos(mφ) + c·sin(mφ). -/
theorem sin_shift (c s : R) (h : c ^ 2 + s ^ 2 = 1) (m : ℕ) :
    sinSeq c s (m + 1) = s * cosSeq c m + c * sinSeq c s m :=
  ((shiftEq_pair c s h m).1).2

/-- **The addition theorems** for the Chebyshev pair: cos((m+n)φ) and
sin((m+n)φ) expand as the classical bilinear laws — from c² + s² = 1
alone, over any commutative ring. -/
theorem cos_sin_add (c s : R) (h : c ^ 2 + s ^ 2 = 1) (m : ℕ) : ∀ n : ℕ,
    cosSeq c (m + n)
      = cosSeq c m * cosSeq c n - sinSeq c s m * sinSeq c s n ∧
    sinSeq c s (m + n)
      = sinSeq c s m * cosSeq c n + cosSeq c m * sinSeq c s n := by
  intro n
  induction n with
  | zero => simp [cosSeq, sinSeq]
  | succ k ih =>
    obtain ⟨ihc, ihs⟩ := ih
    constructor
    · show cosSeq c (m + k + 1)
        = cosSeq c m * cosSeq c (k + 1) - sinSeq c s m * sinSeq c s (k + 1)
      rw [cos_shift c s h (m + k), cos_shift c s h k, sin_shift c s h k,
        ihc, ihs]
      ring
    · show sinSeq c s (m + k + 1)
        = sinSeq c s m * cosSeq c (k + 1) + cosSeq c m * sinSeq c s (k + 1)
      rw [sin_shift c s h (m + k), cos_shift c s h k, sin_shift c s h k,
        ihc, ihs]
      ring

/-- Pythagorean identity at every index: cos(nφ)² + sin(nφ)² = 1. -/
theorem pythagorean (c s : R) (h : c ^ 2 + s ^ 2 = 1) : ∀ n : ℕ,
    cosSeq c n ^ 2 + sinSeq c s n ^ 2 = 1 := by
  intro n
  induction n with
  | zero => simp [cosSeq, sinSeq]
  | succ k ih =>
    rw [cos_shift c s h k, sin_shift c s h k]
    linear_combination (c ^ 2 + s ^ 2) * ih + h

/-! ### 2. Product-to-sum — the keystone mechanism -/

/-- **Product-to-sum** (the S1.1 mechanism): 2·sin((d+b)φ)·sin(bφ)
= cos(dφ) − cos((d+2b)φ), for all indices, over any commutative
ring with c² + s² = 1. -/
theorem two_sin_mul_sin (c s : R) (h : c ^ 2 + s ^ 2 = 1) (d b : ℕ) :
    2 * sinSeq c s (d + b) * sinSeq c s b
      = cosSeq c d - cosSeq c (d + b + b) := by
  obtain ⟨hc, hs⟩ := cos_sin_add c s h d b
  have h2 : cosSeq c (d + b + b)
      = cosSeq c (d + b) * cosSeq c b - sinSeq c s (d + b) * sinSeq c s b :=
    (cos_sin_add c s h (d + b) b).1
  rw [h2, hc, hs]
  linear_combination cosSeq c d * pythagorean c s h b

/-- |j − k| on ℕ (kept self-contained). -/
def adist (j k : ℕ) : ℕ := (j - k) + (k - j)

theorem adist_comm (j k : ℕ) : adist j k = adist k j := by
  unfold adist; omega

theorem adist_of_le {j k : ℕ} (hk : k ≤ j) : adist j k = j - k := by
  unfold adist; omega

private theorem sine_gram_entry_le (c s : R) (h : c ^ 2 + s ^ 2 = 1)
    {j k : ℕ} (hk : k ≤ j) :
    2 * sinSeq c s (2 * j + 1) * sinSeq c s (2 * k + 1)
      = cosSeq c (2 * (j - k)) - cosSeq c (2 * (j + k + 1)) := by
  have base := two_sin_mul_sin c s h (2 * (j - k)) (2 * k + 1)
  have e2 : 2 * (j - k) + (2 * k + 1) + (2 * k + 1) = 2 * (j + k + 1) := by
    omega
  have e1 : 2 * (j - k) + (2 * k + 1) = 2 * j + 1 := by omega
  rw [e2, e1] at base
  exact base

/-- **The half-integer sine-Gram entry** (v701 S1.1, per atom):
2·sin((2j+1)φ)·sin((2k+1)φ) = cos(2|j−k|φ) − cos(2(j+k+1)φ), i.e.
with θ = 2φ: 2·sin((j+½)θ)·sin((k+½)θ) = cos(|j−k|θ) − cos((j+k+1)θ). -/
theorem sine_gram_entry (c s : R) (h : c ^ 2 + s ^ 2 = 1) (j k : ℕ) :
    2 * sinSeq c s (2 * j + 1) * sinSeq c s (2 * k + 1)
      = cosSeq c (2 * adist j k) - cosSeq c (2 * (j + k + 1)) := by
  rcases le_total k j with hk | hj
  · rw [adist_of_le hk]
    exact sine_gram_entry_le c s h hk
  · rw [adist_comm j k, adist_of_le hj]
    have base := sine_gram_entry_le c s h hj
    have ejk : k + j + 1 = j + k + 1 := by omega
    rw [ejk] at base
    calc 2 * sinSeq c s (2 * j + 1) * sinSeq c s (2 * k + 1)
        = 2 * sinSeq c s (2 * k + 1) * sinSeq c s (2 * j + 1) := by ring
      _ = cosSeq c (2 * (k - j)) - cosSeq c (2 * (j + k + 1)) := base

/-! ### 3. The matrix layer: sine form = Gram of the sin vectors -/

/-- The half-integer sine moment form S[j,k] = c_{|j−k|} − c_{j+k+1}
of a moment sequence (v701: the index-reversed odd Toeplitz window
form; here this IS the definition). -/
def sineForm (cm : ℕ → R) (N : ℕ) : Matrix (Fin N) (Fin N) R :=
  Matrix.of fun j k => cm (adist (j : ℕ) (k : ℕ)) - cm ((j : ℕ) + (k : ℕ) + 1)

theorem sineForm_apply (cm : ℕ → R) (N : ℕ) (j k : Fin N) :
    sineForm cm N j k
      = cm (adist (j : ℕ) (k : ℕ)) - cm ((j : ℕ) + (k : ℕ) + 1) := rfl

/-- Moments of the point measure Σ_i wᵢ·δ_{θᵢ} with θᵢ = 2φᵢ:
c_m = Σ_i wᵢ·cos(m·θᵢ) = Σ_i wᵢ·cos(2m·φᵢ). -/
def atomMoments {r : ℕ} (w x : Fin r → R) : ℕ → R :=
  fun m => ∑ i, w i * cosSeq (x i) (2 * m)

/-- The half-integer sine vector of atom i:
(sᵢ)_j = sin((j+½)·θᵢ) = sin((2j+1)·φᵢ). -/
def sinVec {r : ℕ} (x y : Fin r → R) (N : ℕ) (i : Fin r) : Fin N → R :=
  fun j => sinSeq (x i) (y i) (2 * (j : ℕ) + 1)

/-- **The sine-Gram lemma, matrix form** (v701 S1.1): for a finite
atom family on the circle, S = Σ_i 2wᵢ·sᵢ sᵢᵀ EXACTLY — the
half-integer sine form of point-mass moments is a Gram matrix. -/
theorem sineForm_eq_gram {r : ℕ} (w x y : Fin r → R)
    (hxy : ∀ i, x i ^ 2 + y i ^ 2 = 1) (N : ℕ) :
    sineForm (atomMoments w x) N
      = Matrix.of fun j k =>
          ∑ i, 2 * w i * sinVec x y N i j * sinVec x y N i k := by
  ext j k
  simp only [sineForm, atomMoments, sinVec, Matrix.of_apply]
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  have base := sine_gram_entry (x i) (y i) (hxy i) (j : ℕ) (k : ℕ)
  linear_combination (-(w i)) * base

/-- Quadratic-form expansion of a weighted Gram matrix:
Σ_j Σ_k v_j·(Σ_i 2wᵢ uᵢⱼ uᵢₖ)·v_k = Σ_i 2wᵢ·(Σ_j v_j uᵢⱼ)². -/
theorem gram_quadform {r N : ℕ} (w : Fin r → R) (u : Fin r → Fin N → R)
    (v : Fin N → R) :
    ∑ j, ∑ k, v j * (∑ i, 2 * w i * u i j * u i k) * v k
      = ∑ i, 2 * w i * (∑ j, v j * u i j) ^ 2 := by
  calc
    ∑ j, ∑ k, v j * (∑ i, 2 * w i * u i j * u i k) * v k
        = ∑ j, ∑ k, ∑ i, v j * (2 * w i * u i j * u i k) * v k :=
          Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun k _ => by
            rw [Finset.mul_sum, Finset.sum_mul]
    _ = ∑ j, ∑ i, ∑ k, v j * (2 * w i * u i j * u i k) * v k :=
          Finset.sum_congr rfl fun j _ => Finset.sum_comm
    _ = ∑ i, ∑ j, ∑ k, v j * (2 * w i * u i j * u i k) * v k :=
          Finset.sum_comm
    _ = ∑ i, 2 * w i * (∑ j, v j * u i j) ^ 2 := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [pow_two, Finset.sum_mul_sum, Finset.mul_sum]
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun k _ => ?_
          ring

/-- **The Σ-of-squares representation** (v701 S1.1 consequence):
xᵀS x = Σ_i 2wᵢ·⟨sᵢ, x⟩² for the sine form of point-mass moments. -/
theorem sineForm_quadform {r : ℕ} (w x y : Fin r → R)
    (hxy : ∀ i, x i ^ 2 + y i ^ 2 = 1) (N : ℕ) (v : Fin N → R) :
    ∑ j, ∑ k, v j * sineForm (atomMoments w x) N j k * v k
      = ∑ i, 2 * w i * (∑ j, v j * sinVec x y N i j) ^ 2 := by
  rw [sineForm_eq_gram w x y hxy N]
  simp only [Matrix.of_apply]
  exact gram_quadform w (sinVec x y N) v

/-- **PSD** (v701 S1.1): the half-integer sine form of a POSITIVE
point measure is positive semidefinite — positivity of the measure
alone suffices, no support condition. -/
theorem sineForm_psd {r N : ℕ} (w x y : Fin r → ℚ)
    (hxy : ∀ i, x i ^ 2 + y i ^ 2 = 1) (hw : ∀ i, 0 ≤ w i)
    (v : Fin N → ℚ) :
    0 ≤ ∑ j, ∑ k, v j * sineForm (atomMoments w x) N j k * v k := by
  rw [sineForm_quadform w x y hxy N v]
  refine Finset.sum_nonneg fun i _ => ?_
  have h2 : (0 : ℚ) ≤ 2 * w i := by linarith [hw i]
  exact mul_nonneg h2 (sq_nonneg _)

/-! ### 4. Kernel certificates: Pythagorean atoms, N = 4 window -/

/-- cos φ of the (3,4,5) half-angle atom (θ = 2φ, cos θ = −7/25). -/
def cP : ℚ := 3 / 5

/-- sin φ of the (3,4,5) half-angle atom. -/
def sP : ℚ := 4 / 5

theorem atomP_on_circle : cP ^ 2 + sP ^ 2 = 1 := by
  norm_num [cP, sP]

/-- The first eight moments c_m = cos(m·θ) of the single (3,4,5) atom
(exact Chebyshev values — the probe's `c_pm` layer in exact
arithmetic). -/
theorem momentsP :
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 0 = 1 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 1 = -7/25 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 2 = -527/625 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 3 = 11753/15625 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 4
      = 164833/390625 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 5
      = -9653287/9765625 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 6
      = 32125393/244140625 ∧
    atomMoments (fun _ : Fin 1 => (1 : ℚ)) (fun _ => cP) 7
      = 5583548873/6103515625 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    norm_num [atomMoments, cosSeq, cP, Fin.sum_univ_one]

/-- Explicit 4×4 sine form of the single (3,4,5) atom. -/
def Scert : Matrix (Fin 4) (Fin 4) ℚ :=
  !![32/25, 352/625, -24928/15625, 128992/390625;
     352/625, 3872/15625, -274208/390625, 1418912/9765625;
     -24928/15625, -274208/390625, 19418912/9765625, -100484768/244140625;
     128992/390625, 1418912/9765625, -100484768/244140625,
       519966752/6103515625]

/-- Explicit half-integer sine vector v_j = sin((j+½)θ) of the atom. -/
def vCert : Fin 4 → ℚ := ![4/5, 44/125, -3116/3125, 16124/78125]

/-- The abstract sine form of the atom equals the explicit matrix. -/
theorem sineForm_concrete :
    sineForm (atomMoments (fun _ : Fin 1 => (1 : ℚ)) fun _ => cP) 4
      = Scert := by
  ext j k
  fin_cases j <;> fin_cases k <;>
    norm_num [sineForm, atomMoments, adist, cosSeq, cP, Scert,
      Matrix.of_apply, Fin.sum_univ_one]

/-- The abstract sine vector equals the explicit vector. -/
theorem sinVec_concrete :
    sinVec (fun _ : Fin 1 => cP) (fun _ => sP) 4 0 = vCert := by
  funext j
  fin_cases j <;> norm_num [sinVec, sinSeq, cP, sP, vCert]

/-- **Rank-1 certificate**: Scert = 2·v vᵀ exactly — the one-atom sine
form IS a (rank-1) Gram matrix, entry by entry in ℚ. -/
theorem scert_rank_one :
    Scert = Matrix.of fun j k => 2 * vCert j * vCert k := by
  ext j k
  fin_cases j <;> fin_cases k <;> norm_num [Scert, vCert, Matrix.of_apply]

/-- PSD of the concrete one-atom window, from the general theorem. -/
theorem oneAtom_psd (v : Fin 4 → ℚ) :
    0 ≤ ∑ j, ∑ k,
        v j * sineForm (atomMoments (fun _ : Fin 1 => (1 : ℚ)) fun _ => cP)
          4 j k * v k :=
  sineForm_psd (fun _ => 1) (fun _ => cP) (fun _ => sP)
    (fun _ => atomP_on_circle) (fun _ => by norm_num) v

/-- Three Pythagorean atoms: cos φᵢ from (3,4,5), (5,12,13), (8,15,17). -/
def xs : Fin 3 → ℚ := ![3/5, 5/13, 8/17]

/-- The matching sin φᵢ values. -/
def ys : Fin 3 → ℚ := ![4/5, 12/13, 15/17]

/-- Positive rational weights. -/
def ws : Fin 3 → ℚ := ![1, 1/2, 2]

theorem xs_ys_on_circle : ∀ i, xs i ^ 2 + ys i ^ 2 = 1 := by
  intro i; fin_cases i <;> norm_num [xs, ys]

theorem ws_nonneg : ∀ i, 0 ≤ ws i := by
  intro i; fin_cases i <;> norm_num [ws]

/-- The weighted three-atom sine form is the exact Gram matrix of its
three sine vectors (general theorem, instantiated). -/
theorem threeAtom_gram :
    sineForm (atomMoments ws xs) 4
      = Matrix.of fun j k =>
          ∑ i, 2 * ws i * sinVec xs ys 4 i j * sinVec xs ys 4 i k :=
  sineForm_eq_gram ws xs ys xs_ys_on_circle 4

/-- PSD of the weighted three-atom window. -/
theorem threeAtom_psd (v : Fin 4 → ℚ) :
    0 ≤ ∑ j, ∑ k, v j * sineForm (atomMoments ws xs) 4 j k * v k :=
  sineForm_psd ws xs ys xs_ys_on_circle ws_nonneg v

end TfptCarrier.SineGramKeystone
