/-
  PacketRM14 — the Reed-Muller identification of the 15-label channel.
  ====================================================================

  Machine-checked finite core of PRIME.PACKET.RM14.01 (Arf compiler
  programme).  Numeric counterpart:
  experiments/tfpt-discovery/prime_packet_rm14_probe.py
  (21/21, verdict RM14-EXACT, exact F₂/bitmask arithmetic).

  THE SETTING.  On the label space V = L/(1+i)L ≅ F₂⁴ (family/anchor
  basis, reduced form h̄ = ArfSpinorCompiler.symp, certified from the
  concrete lattice by v752), the affine code on the 15 nonzero points

      C_aff = { c_{a,v}(x) = a + h̄(v,x) }  (32 words)

  is the punctured Reed-Muller code RM(1,4)* = [15,5,7]; its linear
  subcode C₀ = {h̄(v,·)} is the [15,4,8] simplex code; the dual
  C₁^⊥ = shortened RM(2,4) = span{xᵢ, xᵢxⱼ} = [15,10,4]; together
  they build the quantum Reed-Muller CSS code [[15,1,3]].

  Certified here, kernel `decide` / `norm_num` only (no sorry, no
  native_decide):

  W (the affine code and its enumerator):
    * `aff_injective`   — the parametrization (a,v) ↦ c_{a,v} is
      faithful: 32 distinct words;
    * `aff_closed`      — c_{a,v} + c_{b,w} = c_{a+b,v+w} pointwise
      (C_aff is linear, dim 5 with `aff_injective`);
    * `c0_in_c1`        — the a = 0 slice is C₀ = {h̄(v,·)} ⊂ C_aff;
    * `wt_law`          — the punctured weight of c_{a,v} is
      0 / 15 / 8 / 7 for (a,v) = (0,0) / (1,0) / (0,v≠0) / (1,v≠0):
      the weight enumerator 1 + 15z⁷ + 15z⁸ + z¹⁵ in closed form;
    * `aff_enumerator`  — the same as an exact census over the 32
      parameters (counts 1/15/15/1);
    * `simplex_equidistant` — every nonzero C₀ word has weight 8
      (the [15,4,8] simplex property).

  N (NS/R as a codeword, the 7+8 split):
    * `chi_split`       — the F_Σ codeword h̄(·,F_Σ) = χ_NSR has
      punctured weight 8 and its affine complement has weight 7: the
      7+8 split is the two sides of ONE RM codeword, the C2 register
      is the affine bit a.

  D (the dual C₁^⊥ = [15,10,4], generators xᵢ and xᵢxⱼ):
    * `gdual_vanish_at_zero` — every generator vanishes at 0 (the
      inner product over all 16 points equals the punctured one);
    * `dual_gen_orthogonal`  — every generator is orthogonal to every
      C_aff word (all 10 × 32 pairs);
    * `dual_independent`     — the 10 generators are linearly
      independent (census over all 1024 coefficient vectors);
    * `dual_add` / `dual_injective` — the coefficient map is linear
      and faithful: the dual code has exactly 1024 distinct words;
    * `dual_wt4_census` … `dual_wt12_census`, `dual_card`,
      `dual_enumerator_complete` — the weight enumerator
      1 + 105z⁴ + 280z⁶ + 435z⁸ + 168z¹⁰ + 35z¹² as exact censuses
      (in particular NO weight 1, 2 or 3: minimum distance 4);

  Q (the CSS code [[15,1,3]]):
    * `css_check_count` — 4 + 10 = 14 independent checks on 15
      qubits ⇒ k = 1;
    * `xbar_min` / `chi_split` — the X-logical class C₁ \ C₀ = the
      a = 1 slice has minimum weight 7 (dX = 7);
    * `zbar_weight` / `zbar_in_c0perp` / `zbar_not_c1perp` /
      `xbar_zbar_anticommute` — the Z-logical Z̄ = {e₀, e₁, e₀+e₁}
      has weight 3, lies in C₀^⊥ \ C₁^⊥ and anticommutes with the
      X-logical X̄ = 1 + χ;
    * `weight_one_not_c0perp` / `weight_two_not_c0perp` — no word of
      weight 1 or 2 lies in C₀^⊥ (dZ = 3 exactly);
    * `trio_single` / `trio_pair` / `trio_triple` — the
      triorthogonality census of the 4 simplex generator rows:
      single weights 8, pairwise overlaps 4, triple overlaps 2.

  HONEST SCOPE.  The row-hull identity (span of the B rows plus
  complements = C_aff), the independent coordinate construction of
  RM(1,4)*, the self-reproduction cycle RM(1,3) → E8 → V → RM(1,4)*
  → RM(1,3) with its 8!-permutation census (1344 equivalences), the
  full-code triorthogonality census and the must-fail controls are
  the probe's job — not re-formalized here.  The ζ8 phase reading
  stays typed [H] with the pointer to v798 (no identification
  claimed); the TFPT fingerprints (14 = dim G2, 3 = N_fam, 7,
  4 = |μ₄|) are carried as fingerprints only.  ROOTCLASS-MIXED; no
  RH claim, no physics claim.

  Imports TfptCarrier.ArfSpinorCompiler for Label, symp, Fsigma.
-/
import TfptCarrier.ArfSpinorCompiler

set_option maxRecDepth 100000
set_option maxHeartbeats 16000000

namespace TfptCarrier.PacketRM14

open TfptCarrier.ArfSpinorCompiler

/-! ### 1. W — the affine code C_aff = RM(1,4)* = [15,5,7] -/

/-- The affine codeword c_{a,v}(x) = a + h̄(v,x) (as a function on
all of V; the code lives on the 15 nonzero points via `wtP`). -/
def affWord (a : ZMod 2) (v : Label) : Label → ZMod 2 :=
  fun x => a + symp v x

/-- Punctured weight: the number of NONZERO points where the word is
1 (the 15-point channel of the probe). -/
def wtP (c : Label → ZMod 2) : ℕ :=
  (Finset.univ.filter fun x : Label => x ≠ 0 ∧ c x = 1).card

/-- The parametrization is faithful: 32 = 2·16 distinct words. -/
theorem aff_injective :
    ∀ (a b : ZMod 2) (v w : Label),
      (∀ x, affWord a v x = affWord b w x) → a = b ∧ v = w := by
  decide

/-- C_aff is linear: c_{a,v} + c_{b,w} = c_{a+b, v+w} pointwise. -/
theorem aff_closed :
    ∀ (a b : ZMod 2) (v w : Label) (x : Label),
      affWord a v x + affWord b w x = affWord (a + b) (v + w) x := by
  decide

/-- The a = 0 slice is the linear subcode C₀ = {h̄(v,·)}. -/
theorem c0_in_c1 : ∀ (v x : Label), affWord 0 v x = symp v x := by
  decide

/-- **THE WEIGHT LAW** (closed form of the enumerator
1 + 15z⁷ + 15z⁸ + z¹⁵): the punctured weight of c_{a,v} is 0 for
(0,0), 15 for (1,0), 8 for (0, v≠0), 7 for (1, v≠0). -/
theorem wt_law :
    ∀ (a : ZMod 2) (v : Label),
      wtP (affWord a v)
        = if v = 0 then (if a = 0 then 0 else 15)
          else (if a = 0 then 8 else 7) := by
  decide

/-- **THE ENUMERATOR CENSUS** over all 32 parameters:
1 + 15z⁷ + 15z⁸ + z¹⁵. -/
theorem aff_enumerator :
    ((Finset.univ.filter fun p : ZMod 2 × Label =>
      wtP (affWord p.1 p.2) = 0).card = 1) ∧
    ((Finset.univ.filter fun p : ZMod 2 × Label =>
      wtP (affWord p.1 p.2) = 7).card = 15) ∧
    ((Finset.univ.filter fun p : ZMod 2 × Label =>
      wtP (affWord p.1 p.2) = 8).card = 15) ∧
    ((Finset.univ.filter fun p : ZMod 2 × Label =>
      wtP (affWord p.1 p.2) = 15).card = 1) := by
  decide

/-- The simplex property of C₀ = [15,4,8]: every nonzero word is
equidistant of weight 8. -/
theorem simplex_equidistant :
    ∀ v : Label, v ≠ 0 → wtP (affWord 0 v) = 8 := by decide

/-! ### 2. N — NS/R as a codeword: the 7+8 split -/

/-- **THE 7+8 SPLIT IS ONE CODEWORD**: χ_NSR = h̄(·,F_Σ) has
punctured weight 8, its affine complement 1 + χ has weight 7 — the
two sides of a single RM word; the C2 register is the affine bit. -/
theorem chi_split :
    wtP (affWord 0 Fsigma) = 8 ∧ wtP (affWord 1 Fsigma) = 7 := by
  decide

/-! ### 3. D — the dual C₁^⊥ = shortened RM(2,4) = [15,10,4] -/

/-- The 10 canonical dual generators: the 4 coordinates xᵢ and the
6 products xᵢxⱼ (shortened RM(2,4)). -/
def gdual : Fin 10 → Label → ZMod 2 :=
  ![fun x => x 0, fun x => x 1, fun x => x 2, fun x => x 3,
    fun x => x 0 * x 1, fun x => x 0 * x 2, fun x => x 0 * x 3,
    fun x => x 1 * x 2, fun x => x 1 * x 3, fun x => x 2 * x 3]

/-- Every dual generator vanishes at 0 — inner products over all 16
points equal the punctured (15-point) ones. -/
theorem gdual_vanish_at_zero : ∀ k : Fin 10, gdual k 0 = 0 := by
  decide

/-- **ORTHOGONALITY**: every dual generator is orthogonal to every
C_aff word (all 10 × 32 pairs, sums over all 16 points — the x = 0
term vanishes by `gdual_vanish_at_zero`). -/
theorem dual_gen_orthogonal :
    ∀ (k : Fin 10) (a : ZMod 2) (v : Label),
      (∑ x : Label, gdual k x * affWord a v x) = 0 := by
  decide

/-- Coefficient space of the dual: 2¹⁰ = 1024 vectors. -/
abbrev Coeff := Fin 10 → ZMod 2

/-- The dual word of a coefficient vector. -/
def dualWord (c : Coeff) : Label → ZMod 2 :=
  fun x => ∑ k, c k * gdual k x

/-- **INDEPENDENCE**: only the zero coefficient vector gives the
zero word (census over all 1024) — the dual has dimension exactly
10 = 15 − 5. -/
theorem dual_independent :
    ∀ c : Coeff, (∀ x : Label, dualWord c x = 0) → c = 0 := by
  decide

/-- The coefficient map is linear. -/
theorem dual_add (c c' : Coeff) (x : Label) :
    dualWord (c + c') x = dualWord c x + dualWord c' x := by
  simp [dualWord, add_mul, Finset.sum_add_distrib]

/-- The coefficient map is faithful: the dual code has exactly 1024
distinct words. -/
theorem dual_injective (c c' : Coeff)
    (h : ∀ x, dualWord c x = dualWord c' x) : c = c' := by
  have hsum : c + c' = 0 := by
    apply dual_independent
    intro x
    rw [dual_add, h x]
    have : ∀ a : ZMod 2, a + a = 0 := by decide
    exact this _
  funext i
  have hi : c i + c' i = 0 := congrFun hsum i
  have : ∀ a b : ZMod 2, a + b = 0 → a = b := by decide
  exact this _ _ hi

/-- Dual census, weight 4: exactly 105 words. -/
theorem dual_wt4_census :
    (Finset.univ.filter fun c : Coeff =>
      wtP (dualWord c) = 4).card = 105 := by decide

/-- Dual census, weight 6: exactly 280 words. -/
theorem dual_wt6_census :
    (Finset.univ.filter fun c : Coeff =>
      wtP (dualWord c) = 6).card = 280 := by decide

/-- Dual census, weight 8: exactly 435 words. -/
theorem dual_wt8_census :
    (Finset.univ.filter fun c : Coeff =>
      wtP (dualWord c) = 8).card = 435 := by decide

/-- Dual census, weight 10: exactly 168 words. -/
theorem dual_wt10_census :
    (Finset.univ.filter fun c : Coeff =>
      wtP (dualWord c) = 10).card = 168 := by decide

/-- Dual census, weight 12: exactly 35 words. -/
theorem dual_wt12_census :
    (Finset.univ.filter fun c : Coeff =>
      wtP (dualWord c) = 12).card = 35 := by decide

/-- Coefficient count: 2¹⁰ = 1024. -/
theorem dual_card : Fintype.card Coeff = 1024 := by decide

/-- **THE DUAL ENUMERATOR IS COMPLETE**: 1 + 105 + 280 + 435 + 168 +
35 = 1024 — the six weights 0, 4, 6, 8, 10, 12 exhaust the code; in
particular NO word of weight 1, 2 or 3 exists: the minimum distance
of C₁^⊥ = [15,10,4] is 4. -/
theorem dual_enumerator_complete :
    1 + 105 + 280 + 435 + 168 + 35 = 1024 := by norm_num

/-! ### 4. Q — the CSS code [[15,1,3]] -/

/-- **THE CSS CHECK COUNT**: 4 X-checks (C₀) + 10 Z-checks (C₁^⊥) =
14 independent checks on 15 qubits ⇒ k = 15 − 14 = 1. -/
theorem css_check_count : 4 + 10 = 14 ∧ 15 - 14 = 1 := by norm_num

/-- **dX = 7**: every word of the X-logical class C₁ \ C₀ (the
a = 1 slice, by `aff_injective`) has weight ≥ 7; weight 7 is attained
(`chi_split`). -/
theorem xbar_min : ∀ v : Label, 7 ≤ wtP (affWord 1 v) := by decide

/-- The Z-logical Z̄: the weight-3 word supported on the 2-flat
{e₀, e₁, e₀+e₁}. -/
def zbar : Label → ZMod 2 :=
  fun x => if x = ![1, 0, 0, 0] ∨ x = ![0, 1, 0, 0] ∨
              x = ![1, 1, 0, 0] then 1 else 0

/-- Z̄ has weight 3. -/
theorem zbar_weight : wtP zbar = 3 := by decide

/-- Z̄ ∈ C₀^⊥: orthogonal to every simplex word h̄(v,·). -/
theorem zbar_in_c0perp :
    ∀ v : Label, (∑ x : Label, zbar x * symp v x) = 0 := by decide

/-- Z̄ ∉ C₁^⊥: it pairs to 1 with the all-ones word c_{1,0}. -/
theorem zbar_not_c1perp :
    (∑ x : Label, zbar x * affWord 1 0 x) = 1 := by decide

/-- Z̄ anticommutes with the X-logical X̄ = 1 + χ = c_{1,F_Σ}. -/
theorem xbar_zbar_anticommute :
    (∑ x : Label, zbar x * affWord 1 Fsigma x) = 1 := by decide

/-- **dZ = 3, minimality (weight 1)**: no weight-1 word lies in
C₀^⊥ — h̄ is pointwise nondegenerate. -/
theorem weight_one_not_c0perp :
    ∀ x : Label, x ≠ 0 → ∃ v : Label, symp v x = 1 := by decide

/-- **dZ = 3, minimality (weight 2)**: no weight-2 word lies in
C₀^⊥. -/
theorem weight_two_not_c0perp :
    ∀ x y : Label, x ≠ 0 → y ≠ 0 → x ≠ y →
      ∃ v : Label, symp v x + symp v y = 1 := by decide

/-! ### 5. T — the triorthogonality census of the simplex rows -/

/-- The i-th basis label. -/
def bvec (i : Fin 4) : Label := fun j => if j = i then 1 else 0

/-- Single rows: weight 8. -/
theorem trio_single : ∀ i : Fin 4, wtP (affWord 0 (bvec i)) = 8 := by
  decide

/-- Pairwise overlaps: weight 4. -/
theorem trio_pair :
    ∀ i j : Fin 4, i ≠ j →
      (Finset.univ.filter fun x : Label => x ≠ 0 ∧
        symp (bvec i) x = 1 ∧ symp (bvec j) x = 1).card = 4 := by
  decide

/-- Triple overlaps: weight 2. -/
theorem trio_triple :
    ∀ i j k : Fin 4, i ≠ j → i ≠ k → j ≠ k →
      (Finset.univ.filter fun x : Label => x ≠ 0 ∧
        symp (bvec i) x = 1 ∧ symp (bvec j) x = 1 ∧
        symp (bvec k) x = 1).card = 2 := by
  decide

end TfptCarrier.PacketRM14
