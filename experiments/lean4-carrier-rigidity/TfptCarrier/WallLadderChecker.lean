/-
  WallLadderChecker — kernel-checkable positivity certificates for the
  exported prime-front wall-ladder matrices (v897 finite head).
  =================================================================

  Numeric counterpart: `verification/v897_certified_interval_ladder.py`
  (PRIME.PORT.BALLLADDER.01) certifies sigma_h > 0 on the 42 reachable
  rungs h = 142..878 of the deployed v563 window ladder via rigorous
  mpmath.iv interval shifts and exact integer Bareiss (tier 1, h <= 300)
  resp. validated-precision Cholesky (tier 2, h > 300).  The exporter
  `scripts/export_wall_certificates.py` re-runs the FROZEN v897
  machinery (SHA-warded) and dumps, per rung, EXACT data:

    * the dyadic interval-lag midpoints  mid_i = mids[i] / den,
    * the rigorous interval shift  shift  (grid units, Q = 10^20),
    * an integer floor  floorC > 0  and an integer Cholesky witness
      `rows` (the rounded Cholesky factor of  N - shift·1 - 2·floorC·1).

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`; the per-rung `decide` runs in the Lean KERNEL on the
  exported integers).

    (1) `rungOk` — THE CHECKER, pure integer/list arithmetic the kernel
        can evaluate: it rebuilds the certificate matrix
            M = N - shift·1,   N i j = ⌊Q·(mids_{|i-j|} - mids_{2h-1-i-j})/den⌋
        (the v897 E4 grid formula, verbatim on the exported dyadics)
        and verifies that the residual  R = M - floorC·1 - L·Lᵀ  is
        diagonally dominant with nonnegative diagonal, and 0 < floorC.

    (2) `posSemidef_of_diagDominant` — the one real-analysis input,
        PROVEN here (not in mathlib): a symmetric real matrix whose
        diagonal dominates its absolute off-diagonal row sums is PSD
        (the Gershgorin-type quadratic-form estimate
        R i j·x i·x j ≥ -|R i j|·(x i² + x j²)/2 plus the symmetry swap).

    (3) `posDef_of_rungOk` — THE PER-RUNG THEOREM: `rungOk d = true`
        forces  M = L·Lᵀ + R + floorC·1  entrywise (by construction),
        hence  M ⪰ floorC·1 ≻ 0 :  the exported integer wall-certificate
        matrix is POSITIVE DEFINITE, with the explicit integer floor
        floorC (sigma floor floorC/Q).  This is the same sigma_h > 0
        content as a v897 certificate, re-established by the kernel
        from the exported data — the witness `rows` is untrusted input;
        only the checked decomposition carries the proof.

  THE HONEST BOUNDARY.  Nothing here connects M/Q to the TRUE wall
  matrix of the analytic ladder: that identification is exactly the
  v897 E1–E4 interval-arithmetic error accounting
  (K_true ⪰ (N - shift·1)/Q), which stays on the Python side and enters
  the composition (WallCofinalComposition.lean) only as the NAMED
  `EnclosureBridge` hypothesis.  The asymptotic tail (h → ∞) is
  untouched.  NO RH claim.
-/
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Real.StarOrdered

namespace TfptCarrier
namespace WallLadder

open Matrix Finset

/-! ### (1) The exported certificate data and the integer checker -/

/-- One exported wall-ladder certificate: the exact dyadic lag
midpoints (`mids[i] / den`), the rigorous interval shift and the
certified integer floor (grid units, `Q = 10^20`), and the untrusted
integer Cholesky witness `rows`.  Everything the kernel needs to
re-establish positive definiteness of the rung's certificate matrix. -/
structure RungData where
  /-- zone index of the rung (v563 ladder numbering) -/
  kz : ℕ
  /-- matrix size (half the window length M) -/
  h : ℕ
  /-- common dyadic denominator of the exported lag midpoints -/
  den : ℤ
  /-- the rigorous interval shift `h + ⌈2·h·rad_max·Q⌉` (v897 E4) -/
  shift : ℤ
  /-- the certified integer floor (`sigma` floor `floorC/Q`) -/
  floorC : ℤ
  /-- exact lag-midpoint numerators: `mid_i = mids[i] / den` -/
  mids : List ℤ
  /-- the integer Cholesky witness (untrusted; row `i` has `i+1` entries) -/
  rows : List (List ℤ)

/-- The tier-1 grid denominator of v897: `Q = 10^20`. -/
def Qgrid : ℤ := 10 ^ 20

/-- Tail-recursive worker for `decodeSigned` (prepends, so the packed
limbs are consumed in reverse output order). -/
def decodeSignedAux (bits : ℕ) : ℕ → ℕ → List ℤ → List ℤ
  | 0, _, acc => acc
  | c + 1, blob, acc =>
    decodeSignedAux bits c (blob / 2 ^ bits)
      ((((blob % 2 ^ bits : ℕ) : ℤ) - 2 ^ (bits - 1)) :: acc)

/-- Decode `count` signed integers (offset binary, `bits` bits each,
packed with the LAST vector entry in the lowest limb) from one packed
natural — the exported data files carry each vector as a single hex
numeral, which elaborates in linear time (long bracket-list literals
do not). -/
def decodeSigned (bits count blob : ℕ) : List ℤ :=
  decodeSignedAux bits count blob []

/-- Decode the triangular witness rows from per-row packed naturals
(row `i` has `i + 1` limbs).  One blob per row keeps every recursion
depth at most the matrix size `h` — a single flat blob would nest
`h·(h+1)/2` deep and overflow the evaluator stack on deep rungs. -/
def decodeRows (bits : ℕ) : ℕ → List ℕ → List (List ℤ)
  | _, [] => []
  | len, b :: bs => decodeSigned bits len b :: decodeRows bits (len + 1) bs

/-- The exported grid-matrix entry
`N i j = ⌊Q·(mid_{|i-j|} - mid_{2h-1-(i+j)})/den⌋` — the v897 E4
odd-Toeplitz grid formula, evaluated exactly on the exported dyadics
(`Int.fdiv` by the positive `den` is the floor). -/
def nEntry (d : RungData) (i j : ℕ) : ℤ :=
  (Qgrid * (d.mids.getD ((i - j) + (j - i)) 0 -
            d.mids.getD ((2 * d.h - 1) - (i + j)) 0)).fdiv d.den

/-- The certificate-matrix entry: `M = N - shift·1` (the rigorously
shifted grid matrix whose positive definiteness is the rung claim). -/
def mEntry (d : RungData) (i j : ℕ) : ℤ :=
  nEntry d i j - if i = j then d.shift else 0

/-- Truncating integer dot product (structural recursion — the kernel
evaluates this without random access). -/
def dotZ : List ℤ → List ℤ → ℤ
  | a :: as, b :: bs => a * b + dotZ as bs
  | _, _ => 0

/-- The Gram entry `(L·Lᵀ) i j` of the witness. -/
def gEntry (d : RungData) (i j : ℕ) : ℤ :=
  dotZ (d.rows.getD i []) (d.rows.getD j [])

/-- The residual entry `R = M - floorC·1 - L·Lᵀ`. -/
def rEntry (d : RungData) (i j : ℕ) : ℤ :=
  mEntry d i j - (if i = j then d.floorC else 0) - gEntry d i j

/-- `sumTo n f = f 0 + ... + f (n-1)` (kernel-friendly recursion). -/
def sumTo (n : ℕ) (f : ℕ → ℤ) : ℤ :=
  match n with
  | 0 => 0
  | n + 1 => sumTo n f + f n

/-- `allTo n p = p 0 && ... && p (n-1)` (kernel-friendly recursion). -/
def allTo (n : ℕ) (p : ℕ → Bool) : Bool :=
  match n with
  | 0 => true
  | n + 1 => allTo n p && p n

/-- Absolute off-diagonal row sum of the residual at row `i`. -/
def offSum (d : RungData) (i : ℕ) : ℤ :=
  sumTo d.h fun j => if j = i then 0 else ((rEntry d i j).natAbs : ℤ)

/-- Row check: the residual diagonal dominates the absolute
off-diagonal row sum (which also forces `0 ≤ R i i`). -/
def rowOk (d : RungData) (i : ℕ) : Bool :=
  decide (offSum d i ≤ rEntry d i i)

/-- **THE CHECKER**: positive floor, well-shaped witness rows, and a
diagonally dominant residual.  Evaluated by the Lean kernel via
`decide` on the exported data. -/
def rungOk (d : RungData) : Bool :=
  decide (0 < d.floorC) &&
  d.rows.all (fun r => decide (r.length ≤ d.h)) &&
  allTo d.h (rowOk d)

/-! ### (2) Bridge lemmas: checker values = matrix algebra -/

theorem sumTo_eq_sum (n : ℕ) (f : ℕ → ℤ) :
    sumTo n f = ∑ j ∈ range n, f j := by
  induction n with
  | zero => rfl
  | succ n ih => rw [sumTo, ih, sum_range_succ]

theorem allTo_eq_true {n : ℕ} {p : ℕ → Bool} :
    allTo n p = true ↔ ∀ i, i < n → p i = true := by
  induction n with
  | zero => simp [allTo]
  | succ n ih =>
    rw [allTo, Bool.and_eq_true, ih]
    constructor
    · rintro ⟨hall, hn⟩ i hi
      rcases Nat.lt_succ_iff_lt_or_eq.mp hi with h | h
      · exact hall i h
      · exact h ▸ hn
    · exact fun h => ⟨fun i hi => h i (Nat.lt_succ_of_lt hi),
        h n (Nat.lt_succ_self n)⟩

theorem dotZ_comm : ∀ a b : List ℤ, dotZ a b = dotZ b a
  | [], [] => rfl
  | [], _ :: _ => rfl
  | _ :: _, [] => rfl
  | x :: as, y :: bs => by
    show x * y + dotZ as bs = y * x + dotZ bs as
    rw [mul_comm, dotZ_comm as bs]

theorem dotZ_eq_sum : ∀ (n : ℕ) (a b : List ℤ), a.length ≤ n →
    b.length ≤ n →
    dotZ a b = ∑ t ∈ range n, a.getD t 0 * b.getD t 0 := by
  intro n
  induction n with
  | zero =>
    intro a b ha hb
    rw [List.length_eq_zero_iff.mp (Nat.le_zero.mp ha),
        List.length_eq_zero_iff.mp (Nat.le_zero.mp hb)]
    rfl
  | succ n ih =>
    intro a b ha hb
    match a, b with
    | [], b => simp [dotZ]
    | x :: as, [] => simp [dotZ]
    | x :: as, y :: bs =>
      rw [Finset.sum_range_succ']
      simp only [List.getD_cons_succ, List.getD_cons_zero]
      rw [show dotZ (x :: as) (y :: bs) = x * y + dotZ as bs from rfl,
          ih as bs (Nat.succ_le_succ_iff.mp ha)
            (Nat.succ_le_succ_iff.mp hb)]
      ring

/-- Off-diagonal `ite`-sums over `univ` are erase-sums. -/
theorem sum_ite_eq_sum_erase {n : ℕ} {M : Type*} [AddCommMonoid M]
    (i : Fin n) (f : Fin n → M) :
    ∑ j, (if j = i then 0 else f j) = ∑ j ∈ univ.erase i, f j := by
  rw [← Finset.sum_erase_add univ _ (mem_univ i), if_pos rfl, add_zero]
  exact Finset.sum_congr rfl fun j hj =>
    if_neg (Finset.mem_erase.mp hj).1

/-! ### (3) The matrices attached to the data -/

/-- The witness matrix `L` (entries beyond a row's length are `0`). -/
def Lmat (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℤ :=
  .of fun i j => (d.rows.getD i.1 []).getD j.1 0

/-- The integer certificate matrix `M = N - shift·1`. -/
def Mmat (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℤ :=
  .of fun i j => mEntry d i.1 j.1

/-- The residual matrix `R = M - floorC·1 - L·Lᵀ`. -/
def Rmat (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℤ :=
  .of fun i j => rEntry d i.1 j.1

/-- The real certificate matrix (the object of the rung theorem). -/
def MmatR (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℝ :=
  (Mmat d).map (Int.cast : ℤ → ℝ)

/-- The real witness matrix. -/
def LmatR (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℝ :=
  (Lmat d).map (Int.cast : ℤ → ℝ)

/-- The real residual matrix. -/
def RmatR (d : RungData) : Matrix (Fin d.h) (Fin d.h) ℝ :=
  (Rmat d).map (Int.cast : ℤ → ℝ)

theorem nEntry_symm (d : RungData) (i j : ℕ) :
    nEntry d i j = nEntry d j i := by
  unfold nEntry
  rw [Nat.add_comm (i - j) (j - i), Nat.add_comm i j]

theorem mEntry_symm (d : RungData) (i j : ℕ) :
    mEntry d i j = mEntry d j i := by
  unfold mEntry
  rw [nEntry_symm]
  by_cases h : i = j
  · subst h; rfl
  · rw [if_neg h, if_neg fun hh => h hh.symm]

theorem rEntry_symm (d : RungData) (i j : ℕ) :
    rEntry d i j = rEntry d j i := by
  unfold rEntry gEntry
  rw [mEntry_symm, dotZ_comm]
  by_cases h : i = j
  · subst h; rfl
  · rw [if_neg h, if_neg fun hh => h hh.symm]

theorem rmat_isSymm (d : RungData) : (Rmat d).IsSymm := by
  ext i j
  exact rEntry_symm d j.1 i.1

theorem rmatR_isSymm (d : RungData) : (RmatR d).IsSymm :=
  (rmat_isSymm d).map _

/-- **The checked decomposition**: on well-shaped data,
`M = L·Lᵀ + R + floorC·1` over `ℤ` — by construction of the residual,
with the Gram entries identified through `dotZ_eq_sum`. -/
theorem mmat_decomp (d : RungData)
    (hshape : ∀ i : ℕ, (d.rows.getD i []).length ≤ d.h) :
    Mmat d = Lmat d * (Lmat d)ᵀ + Rmat d +
      d.floorC • (1 : Matrix (Fin d.h) (Fin d.h) ℤ) := by
  ext i j
  have hg : gEntry d i.1 j.1 = ∑ t : Fin d.h, Lmat d i t * Lmat d j t := by
    rw [gEntry, dotZ_eq_sum d.h _ _ (hshape i.1) (hshape j.1)]
    rw [← Fin.sum_univ_eq_sum_range
      (fun t => (d.rows.getD i.1 []).getD t 0 * (d.rows.getD j.1 []).getD t 0) d.h]
    rfl
  have   hij : (i = j) ↔ (i.1 = j.1) := Fin.val_inj.symm
  simp only [Matrix.add_apply, Matrix.mul_apply, Matrix.transpose_apply,
    Matrix.smul_apply, Matrix.one_apply, smul_eq_mul, mul_ite, mul_one,
    mul_zero, Mmat, Rmat, Matrix.of_apply]
  rw [← hg]
  simp only [rEntry]
  by_cases h : i = j
  · rw [if_pos h, if_pos (hij.mp h)]; ring
  · rw [if_neg h, if_neg fun hh => h (hij.mpr hh)]; ring

/-- The real decomposition: the entrywise cast of the integer
identity. -/
theorem mmatR_decomp (d : RungData)
    (hshape : ∀ i : ℕ, (d.rows.getD i []).length ≤ d.h) :
    MmatR d = LmatR d * (LmatR d)ᵀ + RmatR d +
      (d.floorC : ℝ) • (1 : Matrix (Fin d.h) (Fin d.h) ℝ) := by
  have h := mmat_decomp d hshape
  ext i j
  have he := congrArg (fun M : Matrix (Fin d.h) (Fin d.h) ℤ => M i j) h
  simp only [Matrix.add_apply, Matrix.mul_apply, Matrix.transpose_apply,
    Matrix.smul_apply, Matrix.one_apply, smul_eq_mul, mul_ite, mul_one,
    mul_zero] at he
  simp only [MmatR, LmatR, RmatR, Matrix.map_apply, Matrix.add_apply,
    Matrix.mul_apply, Matrix.transpose_apply, Matrix.smul_apply,
    Matrix.one_apply, smul_eq_mul, mul_ite, mul_one, mul_zero]
  by_cases hij : i = j
  · rw [if_pos hij] at he ⊢
    exact_mod_cast he
  · rw [if_neg hij] at he ⊢
    exact_mod_cast he

/-! ### (4) Diagonal dominance forces positive semidefiniteness -/

/-- **Diagonal dominance gives PSD** (real symmetric case) — the
Gershgorin-type quadratic-form estimate, proven from scratch:
`∑ᵢⱼ R i j·x i·x j ≥ ∑ᵢ (R i i − ∑_{j≠i} |R i j|)·x i² ≥ 0`. -/
theorem posSemidef_of_diagDominant {n : ℕ}
    {R : Matrix (Fin n) (Fin n) ℝ} (hsym : R.IsSymm)
    (hdom : ∀ i, ∑ j ∈ univ.erase i, |R i j| ≤ R i i) :
    R.PosSemidef := by
  have hherm : R.IsHermitian := by
    rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial]
    exact hsym
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg hherm fun x => ?_
  rw [star_trivial]
  have hform : x ⬝ᵥ R *ᵥ x = ∑ i, ∑ j, R i j * x i * x j := by
    simp only [dotProduct, Matrix.mulVec, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ =>
      Finset.sum_congr rfl fun j _ => by ring
  rw [hform]
  -- split every row into diagonal + off-diagonal
  have hsplit : ∀ i, ∑ j, R i j * x i * x j =
      R i i * x i * x i + ∑ j ∈ univ.erase i, R i j * x i * x j :=
    fun i => by
      rw [add_comm, Finset.sum_erase_add univ _ (mem_univ i)]
  -- off-diagonal terms (division-free): 2·R i j·x i·x j ≥ −(|R i j|·x i² + |R i j|·x j²)
  have hbound : ∀ i, ∀ j ∈ univ.erase i,
      -(|R i j| * x i ^ 2 + |R i j| * x j ^ 2) ≤ 2 * (R i j * x i * x j) := by
    intro i j _
    have h1 : 0 ≤ (|R i j| + R i j) * (x i + x j) ^ 2 :=
      mul_nonneg (by linarith [neg_abs_le (R i j)]) (sq_nonneg _)
    have h2 : 0 ≤ (|R i j| - R i j) * (x i - x j) ^ 2 :=
      mul_nonneg (by linarith [le_abs_self (R i j)]) (sq_nonneg _)
    nlinarith [h1, h2]
  -- the symmetry swap: ∑ᵢ∑_{j≠i} |R i j|·x j² = ∑ᵢ∑_{j≠i} |R i j|·x i²
  have hswap : ∑ i, ∑ j ∈ univ.erase i, |R i j| * x j ^ 2 =
      ∑ i, ∑ j ∈ univ.erase i, |R i j| * x i ^ 2 := by
    have lhs_ite : ∀ (g : Fin n → Fin n → ℝ),
        ∑ i, ∑ j ∈ univ.erase i, g i j =
        ∑ i, ∑ j, (if j = i then 0 else g i j) := fun g =>
      Finset.sum_congr rfl fun i _ => (sum_ite_eq_sum_erase i (g i)).symm
    rw [lhs_ite fun i j => |R i j| * x j ^ 2,
        lhs_ite fun i j => |R i j| * x i ^ 2, Finset.sum_comm]
    refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
    have habs : |R b a| = |R a b| := congrArg abs (hsym.apply a b)
    by_cases h : a = b
    · rw [if_pos h, if_pos h.symm]
    · rw [if_neg h, if_neg fun hh => h hh.symm, habs]
  -- per-row lower bound for 2·(row sum)
  have hlow : ∀ i, 2 * (R i i * x i ^ 2)
      - ∑ j ∈ univ.erase i, (|R i j| * x i ^ 2 + |R i j| * x j ^ 2)
      ≤ 2 * ∑ j, R i j * x i * x j := by
    intro i
    have hs : -∑ j ∈ univ.erase i, (|R i j| * x i ^ 2 + |R i j| * x j ^ 2)
        ≤ ∑ j ∈ univ.erase i, 2 * (R i j * x i * x j) := by
      rw [← Finset.sum_neg_distrib]
      exact Finset.sum_le_sum fun j hj => hbound i j hj
    have hsum2 : ∑ j ∈ univ.erase i, 2 * (R i j * x i * x j)
        = 2 * ∑ j ∈ univ.erase i, R i j * x i * x j :=
      (Finset.mul_sum _ _ _).symm
    have hsq : x i ^ 2 = x i * x i := pow_two (x i)
    rw [hsplit i]
    rw [hsum2] at hs
    linarith [hs, hsq]
  -- the total: 0 ≤ ∑ᵢ (2·R i i·x i² − ∑_{j≠i}(|R i j|·x i² + |R i j|·x j²))
  have hnn : (0 : ℝ) ≤ ∑ i, (2 * (R i i * x i ^ 2)
      - ∑ j ∈ univ.erase i, (|R i j| * x i ^ 2 + |R i j| * x j ^ 2)) := by
    have e1 : ∑ i, (2 * (R i i * x i ^ 2)
        - ∑ j ∈ univ.erase i, (|R i j| * x i ^ 2 + |R i j| * x j ^ 2))
        = ∑ i, 2 * (R i i * x i ^ 2)
          - (∑ i, ∑ j ∈ univ.erase i, |R i j| * x i ^ 2
             + ∑ i, ∑ j ∈ univ.erase i, |R i j| * x j ^ 2) := by
      rw [Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
      congr 1
      exact Finset.sum_congr rfl fun i _ => Finset.sum_add_distrib
    rw [e1, hswap]
    have e2 : ∀ i : Fin n, ∑ j ∈ univ.erase i, |R i j| * x i ^ 2
        = (∑ j ∈ univ.erase i, |R i j|) * x i ^ 2 := fun i =>
      (Finset.sum_mul _ _ _).symm
    have e3 : ∀ i : Fin n,
        (∑ j ∈ univ.erase i, |R i j|) * x i ^ 2 ≤ R i i * x i ^ 2 :=
      fun i => mul_le_mul_of_nonneg_right (hdom i) (sq_nonneg _)
    have e4 : ∑ i, ∑ j ∈ univ.erase i, |R i j| * x i ^ 2
        ≤ ∑ i, R i i * x i ^ 2 :=
      Finset.sum_le_sum fun i _ => (e2 i) ▸ e3 i
    have e5 : ∑ i, 2 * (R i i * x i ^ 2) = 2 * ∑ i, R i i * x i ^ 2 :=
      (Finset.mul_sum _ _ _).symm
    linarith [e4, e5.ge, e5.le]
  -- conclude: 0 ≤ 2·S forces 0 ≤ S
  have htot : ∑ i, (2 * (R i i * x i ^ 2)
      - ∑ j ∈ univ.erase i, (|R i j| * x i ^ 2 + |R i j| * x j ^ 2))
      ≤ ∑ i, 2 * ∑ j, R i j * x i * x j :=
    Finset.sum_le_sum fun i _ => hlow i
  have h2S : (0 : ℝ) ≤ 2 * ∑ i, ∑ j, R i j * x i * x j := by
    have e6 : ∑ i, 2 * ∑ j, R i j * x i * x j
        = 2 * ∑ i, ∑ j, R i j * x i * x j := (Finset.mul_sum _ _ _).symm
    linarith [le_trans hnn htot, e6.le, e6.ge]
  linarith [h2S]

/-! ### (5) The per-rung theorem -/

/-- Unpack the Boolean checker into the three structured facts. -/
theorem rungOk_spec {d : RungData} (hchk : rungOk d = true) :
    0 < d.floorC ∧ (∀ i : ℕ, (d.rows.getD i []).length ≤ d.h) ∧
      ∀ i : Fin d.h, ∑ j ∈ univ.erase i, |Rmat d i j| ≤ Rmat d i i := by
  rw [rungOk, Bool.and_eq_true, Bool.and_eq_true] at hchk
  obtain ⟨⟨h1, h2⟩, h3⟩ := hchk
  refine ⟨of_decide_eq_true h1, ?_, ?_⟩
  · intro i
    rcases hg : d.rows[i]? with _ | r
    · simp [List.getD, hg]
    · have hmem : r ∈ d.rows := List.mem_of_getElem? hg
      have hr := of_decide_eq_true (List.all_eq_true.mp h2 _ hmem)
      simpa [List.getD, hg] using hr
  · intro i
    have hrow := allTo_eq_true.mp h3 i.1 i.2
    have hle : offSum d i.1 ≤ rEntry d i.1 i.1 := of_decide_eq_true hrow
    have hsum : offSum d i.1 = ∑ j ∈ univ.erase i, |Rmat d i j| := by
      rw [offSum, sumTo_eq_sum,
          ← Fin.sum_univ_eq_sum_range
            (fun j => if j = i.1 then 0
              else ((rEntry d i.1 j).natAbs : ℤ)) d.h]
      rw [show (∑ j : Fin d.h, if j.1 = i.1 then 0
            else ((rEntry d i.1 j.1).natAbs : ℤ)) =
          ∑ j : Fin d.h, if j = i then 0 else |Rmat d i j| from
        Finset.sum_congr rfl fun j _ => by
          by_cases h : j = i
          · rw [if_pos (congrArg Fin.val h), if_pos h]
          · rw [if_neg fun hh => h (Fin.val_inj.mp hh), if_neg h,
                Int.natCast_natAbs]
            rfl]
      exact sum_ite_eq_sum_erase i _
    rw [← hsum]
    exact hle

/-- **THE PER-RUNG THEOREM**: a passing kernel check forces the real
certificate matrix `M = N - shift·1` to be positive definite — indeed
`M ⪰ floorC·1` with the explicit positive integer floor.  The witness
is untrusted; the kernel re-derives the decomposition. -/
theorem posDef_of_rungOk (d : RungData) (hchk : rungOk d = true) :
    (MmatR d).PosDef := by
  obtain ⟨hc, hshape, hdom⟩ := rungOk_spec hchk
  rw [mmatR_decomp d hshape]
  have hGram : (LmatR d * (LmatR d)ᵀ).PosSemidef := by
    have h := Matrix.posSemidef_self_mul_conjTranspose (LmatR d)
    rwa [Matrix.conjTranspose_eq_transpose_of_trivial] at h
  have hdomR : ∀ i, ∑ j ∈ univ.erase i, |RmatR d i j| ≤ RmatR d i i := by
    intro i
    have h := hdom i
    have hcast : ((∑ j ∈ univ.erase i, |Rmat d i j| : ℤ) : ℝ)
        ≤ ((Rmat d i i : ℤ) : ℝ) := Int.cast_le.mpr h
    rw [Int.cast_sum] at hcast
    simpa [RmatR, Matrix.map_apply, Int.cast_abs] using hcast
  have hR : (RmatR d).PosSemidef :=
    posSemidef_of_diagDominant (rmatR_isSymm d) hdomR
  have hC : ((d.floorC : ℝ) •
      (1 : Matrix (Fin d.h) (Fin d.h) ℝ)).PosDef :=
    Matrix.PosDef.smul Matrix.PosDef.one (by exact_mod_cast hc)
  exact Matrix.PosDef.posSemidef_add (Matrix.PosSemidef.add hGram hR) hC

end WallLadder
end TfptCarrier
