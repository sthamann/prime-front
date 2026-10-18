/-
  PositiveC2Lift — the positive two-channel decomposition of the TFPT
  cusp channel and the C2 packet automaton, finite core kernel-checked.
  ====================================================================

  THE STATEMENTS (machine side, HECKE.POSITIVE_C2_LIFT.01 +
  HECKE.PACKET_COMPOSITION.01; baseline Check32.lean /
  HECKE.CARRIER_CHECK32.01):

    A = (E_odd + f8)/2 = (1/16) θ₂(2τ)⁴ θ₃(4τ)⁴
    B = (E_odd − f8)/2 = (1/16) θ₂(2τ)⁴ θ₂(4τ)⁴ = 16 H,
    H = q³ ψ(q²)⁴ ψ(q⁴)⁴ = η(4τ)⁴ η(8τ)⁸ / η(2τ)⁴,

  BOTH channels with nonnegative integer coefficients [E neu], and the
  C2 packet automaton M_n = [[A_n, B_n], [B_n, A_n]] with Hadamard
  diagonalization Had·M_n·Had = 2·diag(σ₃(n), a_n) and composition
  M_{mn} = M_m·M_n (coprime odd m, n) [E neu for the algebra].

  THIS MODULE (finite core only, everything kernel `decide` /
  `norm_num` / elementary tactics, no sorry, no native_decide):
    • the verified 32-row table (n, a_n, σ₃(n), A_n, B_n, R_n) for all
      odd n ≤ 63, with σ₃ recomputed inside Lean from the divisor sum;
    • first-N coefficient identities  E_odd = A + B  and  f8 = A − B
      (i.e. A_n + B_n = σ₃(n), A_n − B_n = a_n) as exact integer
      statements, WITH nonnegativity A_n ≥ 0, B_n ≥ 0;
    • the B ≡ 0 (mod 16) witnesses and the exact lift B_n = 16·R_n,
      including the degeneracy anchors R = 1, 4, 10, 24, 43 at
      n = 3, 5, 7, 9, 11 (table membership, kernel-checked);
    • the GENERAL packet algebra over ℤ (not just instances):
      the XOR-grammar product law, the Hadamard character identities
      (eigenvectors (1,1) and (1,−1) with eigenvalues A+B and A−B),
      and Had·M·Had = diag(2(A+B), 2(A−B));
    • M_15 = M_3 · M_5 as an EXACT integer matrix identity
      ([[1768,1760],[1760,1768]], Hadamard diagonal (7056, 16) =
      2·(3528, 8)), plus M_9 = M_3² − 27·I;
    • the dependency lemma of the five-condition validator, derived
      generally: A + B = 1 + p³ and 16 ∣ B imply
      a ≡ 1 + p³ (mod 32) — i.e. V1 ∧ V3 ⇒ V4, so the check32
      congruence is a COROLLARY of the positive decomposition.

  PROVENANCE of the hardcoded table: exact integer arithmetic
  (eta/theta builds by definition, Kronecker-substitution big-int
  products) in experiments/tfpt-discovery/hecke_positive_c2_lift_probe.py,
  run 2026-08-05, 42/42 checks, verdict C2LIFT-THEOREM: decomposition
  and positivity verified to q^50000 (6250× the conservative Sturm
  bound 8 for weight 4 on Γ₀(16)), Hadamard census 0 failures,
  XOR-grammar composition on 41053 coprime odd pairs, prime-power
  recursion on 70 odd prime powers, validator 9591/9591 odd primes
  p < 10⁵, controls fire.  a_n and σ₃ columns agree with Check32.lean;
  a_p for p = 3, 5, 7, 11, 13 corpus-anchored (v535).

  What is NOT formalized here: modularity, the Sturm closure, the
  Gauss/Jacobi product identities, and the full censuses — those live
  in the Python probe with typed classical citations.  [C neu] fences
  (sheet-parity reading of A/B; "1, μ₄-corners, decuple" reading of
  1, 4, 10) are interpretations and are NOT stated as theorems.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.PositiveC2Lift

open Matrix

/-! ### The verified channel table (provenance in header) -/

/-- `(n, a_n, σ₃ n, A_n, B_n, R_n)` for ALL odd `n ≤ 63`: the first 32
odd coefficients of the cusp channel `f8`, the Eisenstein channel
`E_odd`, and the two POSITIVE channels `A = (E_odd + f8)/2`,
`B = (E_odd − f8)/2 = 16 R`.  Values from
`hecke_positive_c2_lift_probe.py` (2026-08-05, C2LIFT-THEOREM). -/
def table : List (ℕ × ℤ × ℕ × ℤ × ℤ × ℤ) :=
  [(1, 1, 1, 1, 0, 0),
   (3, -4, 28, 12, 16, 1),
   (5, -2, 126, 62, 64, 4),
   (7, 24, 344, 184, 160, 10),
   (9, -11, 757, 373, 384, 24),
   (11, -44, 1332, 644, 688, 43),
   (13, 22, 2198, 1110, 1088, 68),
   (15, 8, 3528, 1768, 1760, 110),
   (17, 50, 4914, 2482, 2432, 152),
   (19, 44, 6860, 3452, 3408, 213),
   (21, -96, 9632, 4768, 4864, 304),
   (23, -56, 12168, 6056, 6112, 382),
   (25, -121, 15751, 7815, 7936, 496),
   (27, 152, 20440, 10296, 10144, 634),
   (29, 198, 24390, 12294, 12096, 756),
   (31, -160, 29792, 14816, 14976, 936),
   (33, 176, 37296, 18736, 18560, 1160),
   (35, -48, 43344, 21648, 21696, 1356),
   (37, -162, 50654, 25246, 25408, 1588),
   (39, -88, 61544, 30728, 30816, 1926),
   (41, -198, 68922, 34362, 34560, 2160),
   (43, 52, 79508, 39780, 39728, 2483),
   (45, 22, 95382, 47702, 47680, 2980),
   (47, 528, 103824, 52176, 51648, 3228),
   (49, 233, 117993, 59113, 58880, 3680),
   (51, -200, 137592, 68696, 68896, 4306),
   (53, -242, 148878, 74318, 74560, 4660),
   (55, 88, 167832, 83960, 83872, 5242),
   (57, -176, 192080, 95952, 96128, 6008),
   (59, -668, 205380, 102356, 103024, 6439),
   (61, 550, 226982, 113766, 113216, 7076),
   (63, -264, 260408, 130072, 130336, 8146)]

/-- Divisor cube sum `σ₃(n) = Σ_{d ∣ n} d³`, list-computable form
(identical to `Check32.sigma3`). -/
def sigma3 (n : ℕ) : ℕ :=
  ((List.range (n + 1)).filter (fun d => d ≠ 0 && n % d = 0)).foldl
    (fun s d => s + d ^ 3) 0

/-- The hardcoded `σ₃` column is CORRECT: recomputed inside Lean from
the divisor sum for every table row. -/
theorem table_sigma3_correct :
    table.all (fun t => sigma3 t.1 == t.2.2.1) = true := by decide

/-- The table covers ALL odd `n ≤ 63`: the census window is gap-free
(32 rows, 8× beyond the conservative Sturm bound 8). -/
theorem table_gapfree :
    (List.range 32).all
      (fun k => (table.map Prod.fst).contains (2 * k + 1)) = true ∧
    table.length = 32 := by constructor <;> decide

/-- THE DECOMPOSITION, first 32 odd coefficients as exact integer
statements:  `E_odd = A + B` and `f8 = A − B`, i.e.
`A_n + B_n = σ₃(n)` and `A_n − B_n = a_n` for every table row. -/
theorem table_decomposition :
    table.all (fun t =>
      (t.2.2.2.1 + t.2.2.2.2.1 == (t.2.2.1 : ℤ)) &&
      (t.2.2.2.1 - t.2.2.2.2.1 == t.2.1)) = true := by decide

/-- POSITIVITY: both channels are nonnegative on every table row
(the machine census extends this to all `n ≤ 50000`). -/
theorem table_nonneg :
    table.all (fun t =>
      decide (0 ≤ t.2.2.2.1) && decide (0 ≤ t.2.2.2.2.1)) = true := by
  decide

/-- The mod-16 witnesses and the exact lift: `B_n = 16 R_n` (hence
`B_n ≡ 0 (mod 16)`) for every table row. -/
theorem table_B_eq_16R :
    table.all (fun t =>
      (t.2.2.2.2.1 == 16 * t.2.2.2.2.2) &&
      (t.2.2.2.2.1 % 16 == 0)) = true := by decide

/-- The degeneracy anchors `R(3), R(5), R(7), R(9), R(11) =
1, 4, 10, 24, 43` (microstate counts; Python-side the octuple
enumeration) as kernel-checked table membership. -/
theorem degeneracy_anchors :
    (3, (-4 : ℤ), 28, (12 : ℤ), (16 : ℤ), (1 : ℤ)) ∈ table ∧
    (5, (-2 : ℤ), 126, (62 : ℤ), (64 : ℤ), (4 : ℤ)) ∈ table ∧
    (7, (24 : ℤ), 344, (184 : ℤ), (160 : ℤ), (10 : ℤ)) ∈ table ∧
    (9, (-11 : ℤ), 757, (373 : ℤ), (384 : ℤ), (24 : ℤ)) ∈ table ∧
    (11, (-44 : ℤ), 1332, (644 : ℤ), (688 : ℤ), (43 : ℤ)) ∈ table := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-! ### The C2 packet algebra (general, over ℤ) -/

/-- The C2 packet matrix `M(A, B) = [[A, B], [B, A]]`. -/
def M (A B : ℤ) : Matrix (Fin 2) (Fin 2) ℤ := !![A, B; B, A]

/-- The integer Hadamard matrix (the unitary normalisation carries a
factor `1/√2` per copy, hence the factor 2 in `hadamard_conj`). -/
def Had : Matrix (Fin 2) (Fin 2) ℤ := !![1, 1; 1, -1]

/-- THE XOR GRAMMAR, general: the packet matrices compose by
`M(A₁,B₁)·M(A₂,B₂) = M(A₁A₂ + B₁B₂, A₁B₂ + B₁A₂)` — the C2 group
algebra multiplication (channel index adds mod 2). -/
theorem packet_mul (A₁ B₁ A₂ B₂ : ℤ) :
    M A₁ B₁ * M A₂ B₂ = M (A₁ * A₂ + B₁ * B₂) (A₁ * B₂ + B₁ * A₂) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [M, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- Hadamard character identity, aligned sheet: `(1,1)` is an
eigenvector of every packet with eigenvalue `A + B` (= σ₃(n) on the
verified data — the Eisenstein character). -/
theorem char_plus (A B : ℤ) :
    (M A B).mulVec ![1, 1] = ![A + B, A + B] := by
  funext i
  fin_cases i <;> simp [M, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
  ring

/-- Hadamard character identity, anti-aligned sheet: `(1,−1)` is an
eigenvector with eigenvalue `A − B` (= a_n — the cusp character). -/
theorem char_minus (A B : ℤ) :
    (M A B).mulVec ![1, -1] = ![A - B, -(A - B)] := by
  funext i
  fin_cases i <;>
    simp [M, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> ring

/-- Hadamard conjugation diagonalizes every packet:
`Had·M(A,B)·Had = diag(2(A+B), 2(A−B))`. -/
theorem hadamard_conj (A B : ℤ) :
    Had * M A B * Had = !![2 * (A + B), 0; 0, 2 * (A - B)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [M, Had, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-! ### The worked composition, exact integer matrices -/

/-- **M_15 = M_3 · M_5** as an exact integer matrix identity:
`M(12,16)·M(62,64) = M(1768,1760)` (verified coefficients:
`(A₃,B₃) = (12,16)`, `(A₅,B₅) = (62,64)`, `(A₁₅,B₁₅) = (1768,1760)`,
table rows above). -/
theorem M15_composition : M 12 16 * M 62 64 = M 1768 1760 := by decide

/-- The Hadamard diagonal of `M_15` is `2·diag(3528, 8)` —
`σ₃(15) = 3528` and `a₁₅ = 8`, the worked example of the automaton. -/
theorem M15_hadamard :
    Had * M 1768 1760 * Had = !![7056, 0; 0, 16] := by decide

/-- The prime-power recursion at `p = 3, k = 2`:
`M_9 = M_3² − 27·I` (`27 = 3³`; `(A₉,B₉) = (373,384)`). -/
theorem M9_recursion :
    M 12 16 * M 12 16 - !![27, 0; 0, 27] = M 373 384 := by decide

/-! ### The validator dependency, derived generally -/

/-- V1 ∧ V3 ⇒ V4, general: if a packet satisfies the sum rule
`σ = A + B` with `a = A − B` and the mod-16 witness `16 ∣ B`, then
`a ≡ σ (mod 32)` — the check32 congruence is a COROLLARY of the
positive decomposition (dependency note of the five-condition
validator, kernel-derived, not censused). -/
theorem check32_from_decomposition (σ a A B : ℤ)
    (hsum : A + B = σ) (hdiff : A - B = a) (h16 : B % 16 = 0) :
    (a - σ) % 32 = 0 := by omega

/-- The mod-64 lift still FAILS at `q³` (maximality is untouched by
the positive lift): `a₃ − σ₃(3) = −32`, divisible by 32, not by 64
(Lean's `emod` is nonnegative: `−32 % 64 = 32`). -/
theorem mod64_still_fails_at_3 :
    ((-4 : ℤ) - 28) % 32 = 0 ∧ ((-4 : ℤ) - 28) % 64 = 32 := by decide

/-- Structural arithmetic of the maximality witness, on the R side:
`σ₃(3) − a₃ = 32 = 32·R(3)` with `R(3) = 1` ODD — the mod-64 failure
is exactly the oddness of the first microstate count. -/
theorem maximality_is_R3_odd :
    (28 : ℤ) - (-4) = 32 * 1 ∧ (1 : ℤ) % 2 = 1 := by decide

end TfptCarrier.PositiveC2Lift
