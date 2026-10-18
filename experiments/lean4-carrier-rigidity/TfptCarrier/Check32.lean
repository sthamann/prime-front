/-
  Check32 — the mod-32 carrier congruence of the TFPT cusp channel,
  finite core kernel-checked.
  ==================================================================

  THE STATEMENT (machine side, HECKE.CARRIER_CHECK32.01): the cusp
  channel f8(q) = eta(2τ)^4 eta(4τ)^4 = Σ a_n q^n (corpus: v535
  HECKE.GEOM.01, cusp projector π_cusp = (28 − T_3)/32) satisfies

      f8 ≡ E_odd (mod 32),   E_odd = Σ_{n odd} σ₃(n) qⁿ,

  hence a_p ≡ 1 + p³ (mod 32) for every odd prime p, with decoder
  p ≡ (a_p − 1)³ (mod 32).  The mod-64 lift FAILS already at q³
  (a_3 − 28 = −32), so 32 = 2^g_car is the maximal 2-power.

  THIS MODULE (finite core only, everything kernel `decide` /
  `norm_num`, no sorry, no native_decide):
    • the cube map r ↦ r³ is a bijection on the 16 odd residues of
      ZMod 32 (injective + surjective + parity-closed), and the
      decoder round-trip ((1 + p³) − 1)³ = p holds for every odd
      residue (p⁹ = p on units of ZMod 32);
    • the first 32 odd coefficients (all odd n ≤ 63 — 16× beyond the
      Sturm bound 4 = (4/12)·[SL₂(ℤ):Γ₀(8)]) satisfy the congruence
      a_n ≡ σ₃(n) (mod 32) as EXACT integer statements, with σ₃
      recomputed inside Lean from the divisor sum;
    • the decoder verified on the actual prime coefficients in range;
    • the mod-64 failure witness at q³;
    • the Hecke grammar spot identities a_9 = a_3² − 27,
      a_15 = a_3·a_5, a_25 = a_5² − 125;
    • the structural arithmetic 32 = 2⁵ = 16 + 16 = 28 − (−4)
      (2^g_car / dim(S⁺⊕S⁻) (v774) / π_cusp denominator (v535) —
      typed as structural observation, not derivation).

  PROVENANCE of the hardcoded coefficients: exact integer eta-product
  expansion (pentagonal series, Kronecker-substitution big-int
  products) in experiments/tfpt-discovery/hecke_check32_probe.py,
  run 2026-08-05, 20/20 checks, verdict CHECK32-THEOREM: congruence
  verified to q^100000 (25000× Sturm), prime census 9591/9591 odd
  primes p < 10⁵, controls fire (mutant eta exponent 91.7 % failure,
  random-sequence detection rate 0.9676 ≈ 31/32).  a_p values for
  p = 3,5,7,11,13 agree with the corpus table in
  verification/v535_hecke_from_geometry.py.

  What is NOT formalized here: modularity of f8, the Sturm theorem
  (the one cited classical ingredient of the machine-side reading),
  and the full 10⁵ census — those live in the Python probe.
-/
import Mathlib.Tactic

namespace TfptCarrier.Check32

/-! ### The cube map on odd residues mod 32 -/

/-- The cube map preserves oddness on `ZMod 32`. -/
theorem cube_odd_closed :
    ∀ x : ZMod 32, x.val % 2 = 1 → (x ^ 3).val % 2 = 1 := by decide

/-- The cube map is INJECTIVE on the 16 odd residues mod 32. -/
theorem cube_inj_odd :
    ∀ x y : ZMod 32, x.val % 2 = 1 → y.val % 2 = 1 →
      x ^ 3 = y ^ 3 → x = y := by decide

/-- The cube map is SURJECTIVE onto the 16 odd residues mod 32:
together with injectivity and closure this is the bijection census. -/
theorem cube_surj_odd :
    ∀ y : ZMod 32, y.val % 2 = 1 →
      ∃ x : ZMod 32, x.val % 2 = 1 ∧ x ^ 3 = y := by decide

/-- Decoder round-trip: for every odd residue p mod 32,
`((1 + p³) − 1)³ = p` — equivalently `p⁹ = p` on the units of
`ZMod 32` (the unit group has exponent 8). -/
theorem decoder_roundtrip :
    ∀ p : ZMod 32, p.val % 2 = 1 → ((1 + p ^ 3) - 1) ^ 3 = p := by decide

/-! ### The verified coefficient table (provenance in header) -/

/-- `(n, a_n, σ₃ n)` for ALL odd `n ≤ 63` — the first 32 odd
coefficients of `f8 = eta(2τ)^4 eta(4τ)^4`, 16× beyond the Sturm
bound 4.  Values from `hecke_check32_probe.py` (2026-08-05,
CHECK32-THEOREM); `a_3, a_5, a_7, a_11, a_13` corpus-anchored (v535). -/
def table : List (ℕ × ℤ × ℕ) :=
  [(1, 1, 1), (3, -4, 28), (5, -2, 126), (7, 24, 344), (9, -11, 757),
   (11, -44, 1332), (13, 22, 2198), (15, 8, 3528), (17, 50, 4914),
   (19, 44, 6860), (21, -96, 9632), (23, -56, 12168), (25, -121, 15751),
   (27, 152, 20440), (29, 198, 24390), (31, -160, 29792),
   (33, 176, 37296), (35, -48, 43344), (37, -162, 50654),
   (39, -88, 61544), (41, -198, 68922), (43, 52, 79508),
   (45, 22, 95382), (47, 528, 103824), (49, 233, 117993),
   (51, -200, 137592), (53, -242, 148878), (55, 88, 167832),
   (57, -176, 192080), (59, -668, 205380), (61, 550, 226982),
   (63, -264, 260408)]

/-- Divisor cube sum `σ₃(n) = Σ_{d ∣ n} d³`, list-computable form. -/
def sigma3 (n : ℕ) : ℕ :=
  ((List.range (n + 1)).filter (fun d => d ≠ 0 && n % d = 0)).foldl
    (fun s d => s + d ^ 3) 0

/-- The hardcoded `σ₃` column is CORRECT: recomputed inside Lean from
the divisor sum for every table row. -/
theorem table_sigma3_correct :
    table.all (fun t => sigma3 t.1 == t.2.2) = true := by decide

/-- The table covers ALL odd `n ≤ 63`: the census window is gap-free
(and its 32 rows lie 16× beyond the Sturm bound 4). -/
theorem table_gapfree :
    (List.range 32).all
      (fun k => (table.map Prod.fst).contains (2 * k + 1)) = true ∧
    table.length = 32 := by constructor <;> decide

/-- THE CONGRUENCE, first 32 odd coefficients as exact integer
statements: `a_n ≡ σ₃(n) (mod 32)` for every table row. -/
theorem table_congruence :
    table.all (fun t => (t.2.1 - (t.2.2 : ℤ)) % 32 == 0) = true := by
  decide

/-- The prime rows of the table decode: `(a_p − 1)³ ≡ p (mod 32)` on
the actual verified coefficients (primes 3 … 61). -/
theorem decoder_on_data :
    ([(3, -4), (5, -2), (7, 24), (11, -44), (13, 22), (17, 50),
      (19, 44), (23, -56), (29, 198), (31, -160), (37, -162),
      (41, -198), (43, 52), (47, 528), (53, -242), (59, -668),
      (61, 550)] : List (ℕ × ℤ)).all
      (fun t => ((t.2 - 1) ^ 3 - (t.1 : ℤ)) % 32 == 0) = true := by
  decide

/-! ### The mod-64 failure witness and the grammar spots -/

/-- The predeclared must-fail: at `q³` the defect `a_3 − (1 + 3³)`
is exactly `−32` — divisible by 32 … -/
theorem mod32_holds_at_3 : ((-4 : ℤ) - (1 + 3 ^ 3)) % 32 = 0 := by decide

/-- … but NOT by 64: the congruence does not lift, so 32 is the
maximal 2-power (Lean's `emod` is nonnegative: `−32 % 64 = 32`). -/
theorem mod64_fails_at_3 : ((-4 : ℤ) - (1 + 3 ^ 3)) % 64 = 32 := by decide

theorem mod64_witness_nonzero : (32 : ℤ) ≠ 0 := by decide

/-- Hecke grammar spot identities on the verified coefficients:
`a_9 = a_3² − 3³·a_1`, `a_15 = a_3·a_5`, `a_25 = a_5² − 5³·a_1`. -/
theorem grammar_spots :
    (-4 : ℤ) * (-4) - 3 ^ 3 * 1 = -11 ∧
    (-4 : ℤ) * (-2) = 8 ∧
    (-2 : ℤ) * (-2) - 5 ^ 3 * 1 = -121 := by norm_num

/-! ### Structural arithmetic (observation, not derivation) -/

/-- `32 = 2^g_car (g_car = 5, axiom P2) = dim(S⁺ ⊕ S⁻) = 16 + 16
(v774 spinor layer) = 28 − (−4) (the π_cusp = (28 − T_3)/32
denominator, v535 N4a).` Typed as structural observation. -/
theorem structural_32 :
    (2 : ℕ) ^ 5 = 32 ∧ (16 : ℕ) + 16 = 32 ∧ (28 : ℤ) - (-4) = 32 := by
  norm_num

end TfptCarrier.Check32
