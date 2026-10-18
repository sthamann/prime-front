/-
  DenseWeilCore — the canonical countable dense test family, finitary core.
  =========================================================================

  Machine-checked FINITARY side of the dense-Weil-core construction
  (Agent C of the GLOBAL-HANDOFF round; Python counterpart
  experiments/tfpt-discovery/dense_weil_core_probe.py, verdict
  DENSE-CORE-CANONICAL, 26/26).  The family replacing the frozen
  24-function battery is

      D = ⋃_{r,m} V_{2^-m, r}(ℚ),

  spanned by the dyadic boxes box(m,k) = 1_[k·2^-m, (k+1)·2^-m) and the
  dyadic hats hat(m,k) (tent with nodes (k, k+1, k+2)·2^-m), with the
  FIXED lexicographic enumeration

      rank(m, k, kind) = 2·(tri(m+k) + m) + kind,   kind: 0 = box, 1 = hat

  (lexicographic in (weight m+k, level m, kind)).  This module proves:

    (1) ENUMERATION IS A BIJECTION with computable stage bounds:
        `enum_rank` / `rank_enum` (two-sided inverse ℕ ≃ Idx) and
        `weight_le` (level + position of member n is ≤ n / 2), so every
        finite initial segment I_n embeds in the SINGLE finite tower
        stage (d, r) = (2^-(n/2), n/2 + 2): `segment_embeds`,
        `grid_dvd_stage` (dyadic grid divisibility), `support_le_stage`.
        The triangular decode is division-free (`tri` recursive, `dec`
        a lexicographic successor walk), so everything kernel-computes:
        concrete certificates `rank_battery_hat8` (battery hat 8 =
        hat(2,3) = member 35, probe D5.3) and `rank_tower_box`
        (rank(box(6,100)) = 11354, the deployed-battery segment bound
        of probe D5.2) are closed by `rfl`.

    (2) GRID MODULE CLOSURE: coefficient vectors over any commutative
        ring form a module (`Supported.add/smul/mono`) closed under the
        product/correlation combinatorics the Gram construction needs
        at the grid level: discrete convolution `conv` and window
        cross-correlation `corr` (= conv against the window reversal
        `revw`) keep finite support with the sharp bound N + M - 1
        (`conv_supported`, `corr_supported`) and are bilinear
        (`conv_add_left/right`, `conv_smul_left/right`).  The unit-
        vector lag dictionary is exact: `corr_unit` (correlation of two
        grid cells is the shifted delta at lag (N-1) - n).

    (3) DYADIC INHERITANCE: the one-step refinement `refine`
        (level m -> m+1 coefficient inheritance j ↦ f (j/2)) is linear
        (`refine_add/smul`, definitionally), injective
        (`refine_injective`), support-doubling (`refine_supported`),
        and splits each cell into its two children exactly
        (`refine_unit`: refine (unit k) = unit (2k) + unit (2k+1)).

  HONEST SCOPE (what stays Python-side / analytic, stated up front):
  true L²-density of span_ℚ D in the admissible Weil test space, Weil
  admissibility itself (Iwaniec–Kowalski Thm 5.12 hypotheses; the
  deployed tent test pairs of v677 S2(i)), the continuum piecewise-
  polynomial correlation algebra (exact-ℚ certificates in the probe,
  checks D3.*), and the quantitative approximation rates (probe D2).
  This file contains NO number theory, NO analysis: only the finitary
  enumeration, stage, and grid-combinatorics layer.  No `sorry`, no
  `native_decide`.
-/
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 1000000

namespace TfptCarrier.DenseWeilCore

/-! ### 1. Triangular numbers and the lexicographic pair walk -/

/-- Triangular numbers, division-free recursion: tri t = t(t+1)/2. -/
def tri : ℕ → ℕ
  | 0 => 0
  | t + 1 => tri t + (t + 1)

theorem tri_succ (t : ℕ) : tri (t + 1) = tri t + (t + 1) := rfl

theorem le_tri (t : ℕ) : t ≤ tri t := by
  induction t with
  | zero => simp [tri]
  | succ t ih => rw [tri_succ]; omega

theorem tri_le_tri {s t : ℕ} (h : s ≤ t) : tri s ≤ tri t := by
  induction h with
  | refl => exact le_rfl
  | step _ ih => rw [tri_succ]; omega

/-- Successor step of the lexicographic walk on {(t, m) : m ≤ t}
(weight-major, then level). -/
def nextPair (p : ℕ × ℕ) : ℕ × ℕ :=
  if p.2 < p.1 then (p.1, p.2 + 1) else (p.1 + 1, 0)

/-- The q-th pair (weight, level) in lexicographic order. -/
def dec : ℕ → ℕ × ℕ
  | 0 => (0, 0)
  | q + 1 => nextPair (dec q)

theorem dec_snd_le_fst (q : ℕ) : (dec q).2 ≤ (dec q).1 := by
  induction q with
  | zero => simp [dec]
  | succ q ih =>
    show (nextPair (dec q)).2 ≤ (nextPair (dec q)).1
    rcases hdq : dec q with ⟨t, m⟩
    rw [hdq] at ih
    simp only [nextPair]
    split_ifs with h
    · exact h
    · exact Nat.zero_le _

/-- The closed rank of the pair (t, m): tri t + m. -/
def pairRank (t m : ℕ) : ℕ := tri t + m

/-- The walk inverts the closed rank: rank of the q-th pair is q. -/
theorem pairRank_dec (q : ℕ) : pairRank (dec q).1 (dec q).2 = q := by
  induction q with
  | zero => simp [dec, pairRank, tri]
  | succ q ih =>
    have hle := dec_snd_le_fst q
    show pairRank (nextPair (dec q)).1 (nextPair (dec q)).2 = q + 1
    rcases hdq : dec q with ⟨t, m⟩
    rw [hdq] at ih hle
    simp only [nextPair]
    split_ifs with h
    · show pairRank t (m + 1) = q + 1
      simp only [pairRank] at ih ⊢
      omega
    · show pairRank (t + 1) 0 = q + 1
      simp only [pairRank, tri_succ] at ih ⊢
      omega

theorem tri_le_pairRank (t m : ℕ) : tri t ≤ pairRank t m :=
  Nat.le_add_right _ _

theorem pairRank_lt {t m : ℕ} (h : m ≤ t) : pairRank t m < tri (t + 1) := by
  simp only [pairRank, tri_succ]; omega

/-- pairRank is injective on the domain {m ≤ t} (weight is recovered
from the triangular sandwich, then the level cancels). -/
theorem pairRank_inj {t m t' m' : ℕ} (h : m ≤ t) (h' : m' ≤ t')
    (heq : pairRank t m = pairRank t' m') : t = t' ∧ m = m' := by
  have ht : t = t' := by
    by_contra hne
    rcases Nat.lt_or_ge t t' with hlt | hge
    · have h1 := pairRank_lt h
      have h2 : tri (t + 1) ≤ tri t' := tri_le_tri hlt
      have h3 := tri_le_pairRank t' m'
      omega
    · have hlt' : t' < t := lt_of_le_of_ne hge (Ne.symm hne)
      have h1 := pairRank_lt h'
      have h2 : tri (t' + 1) ≤ tri t := tri_le_tri hlt'
      have h3 := tri_le_pairRank t m
      omega
  subst ht
  simp only [pairRank] at heq
  exact ⟨rfl, by omega⟩

/-- Two-sided inverse, other direction: decoding the closed rank
returns the pair. -/
theorem dec_pairRank {t m : ℕ} (h : m ≤ t) : dec (pairRank t m) = (t, m) := by
  have h1 := pairRank_dec (pairRank t m)
  have h2 := dec_snd_le_fst (pairRank t m)
  rcases hd : dec (pairRank t m) with ⟨t', m'⟩
  rw [hd] at h1 h2
  have h1' : pairRank t' m' = pairRank t m := h1
  have h2' : m' ≤ t' := h2
  obtain ⟨ht, hm⟩ := pairRank_inj h2' h h1'
  rw [ht, hm]

/-! ### 2. The family index and the fixed lexicographic enumeration -/

/-- Index of a family member: dyadic level m, position k, and kind
(`hat = false` is the box 1_[k·2^-m,(k+1)·2^-m), `hat = true` the tent
with nodes (k, k+1, k+2)·2^-m). -/
structure Idx where
  level : ℕ
  pos : ℕ
  hat : Bool
deriving DecidableEq, Repr

/-- The FIXED lexicographic enumeration rank (frozen in the probe and
hashed there): rank = 2·(tri(level+pos) + level) + kind. -/
def rank (i : Idx) : ℕ :=
  2 * pairRank (i.level + i.pos) i.level + (if i.hat then 1 else 0)

/-- Inverse enumeration ℕ → Idx. -/
def enum (n : ℕ) : Idx :=
  ⟨(dec (n / 2)).2, (dec (n / 2)).1 - (dec (n / 2)).2, n % 2 == 1⟩

/-- The enumeration is a bijection, direction 1: enum ∘ rank = id. -/
theorem enum_rank (i : Idx) : enum (rank i) = i := by
  obtain ⟨m, k, b⟩ := i
  have hq : rank ⟨m, k, b⟩ = 2 * pairRank (m + k) m + (if b then 1 else 0) :=
    rfl
  have hdiv : rank ⟨m, k, b⟩ / 2 = pairRank (m + k) m := by
    rw [hq]; split <;> omega
  have hmod : rank ⟨m, k, b⟩ % 2 = (if b then 1 else 0) := by
    rw [hq]; split <;> omega
  have hdq : dec (rank ⟨m, k, b⟩ / 2) = (m + k, m) := by
    rw [hdiv]; exact dec_pairRank (Nat.le_add_right m k)
  simp only [enum, hdq, hmod]
  cases b <;> simp

/-- The enumeration is a bijection, direction 2: rank ∘ enum = id. -/
theorem rank_enum (n : ℕ) : rank (enum n) = n := by
  have hle := dec_snd_le_fst (n / 2)
  have hpd := pairRank_dec (n / 2)
  rcases hd : dec (n / 2) with ⟨t, m⟩
  rw [hd] at hle hpd
  simp only [enum, rank, hd]
  have ht : m + (t - m) = t := by omega
  rw [ht, hpd]
  rcases Nat.mod_two_eq_zero_or_one n with h | h <;> simp [h] <;> omega

/-! ### 3. Computable stage bounds: finite segments in finite stages -/

theorem le_pairRank_self (t m : ℕ) : t ≤ pairRank t m :=
  le_trans (le_tri t) (Nat.le_add_right _ _)

/-- THE STAGE BOUND: the weight (level + position) of the n-th family
member is at most n / 2 — computable, and certified numerically for
n < 100000 in the probe (G0.4). -/
theorem weight_le (n : ℕ) : (enum n).level + (enum n).pos ≤ n / 2 := by
  have hle := dec_snd_le_fst (n / 2)
  have hpd := pairRank_dec (n / 2)
  have h := le_pairRank_self (dec (n / 2)).1 (dec (n / 2)).2
  show (dec (n / 2)).2 + ((dec (n / 2)).1 - (dec (n / 2)).2) ≤ n / 2
  omega

/-- Stage map, grid exponent: member n lives on grid d(n) = 2^-(n/2). -/
def stageLevel (n : ℕ) : ℕ := n / 2

/-- Stage map, support reach: r(n) = n/2 + 2 grid-units of level 0. -/
def stageReach (n : ℕ) : ℕ := n / 2 + 2

theorem level_le_stage (n : ℕ) : (enum n).level ≤ stageLevel n := by
  have := weight_le n; simp only [stageLevel]; omega

/-- Support end in units of the member's OWN grid is pos + 2 cells
(pos + 1 for a box, pos + 2 for a hat), bounded by the stage reach. -/
theorem support_le_stage (n : ℕ) : (enum n).pos + 2 ≤ stageReach n := by
  have := weight_le n; simp only [stageReach]; omega

/-- EVERY FINITE INITIAL SEGMENT EMBEDS IN A FINITE TOWER STAGE:
each member of I_N = {enum 0, …, enum N} satisfies the level and
reach bounds of the single stage (2^-(N/2), N/2 + 2). -/
theorem segment_embeds {N n : ℕ} (h : n ≤ N) :
    (enum n).level ≤ stageLevel N ∧ (enum n).pos + 2 ≤ stageReach N := by
  have hw := weight_le n
  have hd : n / 2 ≤ N / 2 := Nat.div_le_div_right h
  exact ⟨by simp only [stageLevel]; omega, by simp only [stageReach]; omega⟩

/-- Dyadic grid divisibility: the member's grid 2^-level refines into
the stage grid 2^-stageLevel exactly (2^level ∣ 2^stageLevel). -/
theorem grid_dvd_stage {N n : ℕ} (h : n ≤ N) :
    2 ^ (enum n).level ∣ 2 ^ stageLevel N := by
  refine pow_dvd_pow 2 ?_
  have := (segment_embeds h).1
  exact this

/-! ### 4. Concrete kernel certificates (probe D5) -/

/-- Battery hat 8 (peak 1, width 1/4) IS the family member hat(2,3),
enumeration rank 35 — probe check D5.3, kernel-evaluated. -/
theorem rank_battery_hat8 : rank ⟨2, 3, true⟩ = 35 := rfl

theorem enum_35 : enum 35 = ⟨2, 3, true⟩ := rfl

/-- The deployed sampled 24-battery lives below rank(box(6,100)) =
11354 — probe check D5.2, kernel-evaluated (tri 106 = 5671). -/
theorem rank_tower_box : rank ⟨6, 100, false⟩ = 11354 := rfl

/-- First members of the enumeration, kernel-evaluated: box(0,0),
hat(0,0), box(0,1), hat(0,1), box(1,0). -/
theorem enum_first :
    enum 0 = ⟨0, 0, false⟩ ∧ enum 1 = ⟨0, 0, true⟩ ∧
    enum 2 = ⟨0, 1, false⟩ ∧ enum 3 = ⟨0, 1, true⟩ ∧
    enum 4 = ⟨1, 0, false⟩ :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

/-! ### 5. Grid module closed under the correlation combinatorics -/

section Grid

variable {R : Type*} [CommRing R]

/-- A coefficient vector supported below N (a finite tower stage). -/
def Supported (N : ℕ) (f : ℕ → R) : Prop := ∀ k, N ≤ k → f k = 0

theorem Supported.mono {N M : ℕ} {f : ℕ → R} (hf : Supported N f)
    (h : N ≤ M) : Supported M f :=
  fun k hk => hf k (le_trans h hk)

theorem Supported.add {N : ℕ} {f g : ℕ → R} (hf : Supported N f)
    (hg : Supported N g) : Supported N (f + g) :=
  fun k hk => by simp [hf k hk, hg k hk]

theorem Supported.smul {N : ℕ} {f : ℕ → R} (c : R) (hf : Supported N f) :
    Supported N (c • f) :=
  fun k hk => by simp [hf k hk]

/-- Discrete convolution of coefficient vectors. -/
def conv (f g : ℕ → R) (n : ℕ) : R :=
  ∑ j ∈ Finset.range (n + 1), f j * g (n - j)

/-- SHARP support closure: window-N times window-M data stays in the
window-(N + M - 1) stage — the finite-stage closure the Gram
construction needs. -/
theorem conv_supported {N M : ℕ} {f g : ℕ → R}
    (hf : Supported N f) (hg : Supported M g) :
    Supported (N + M - 1) (conv f g) := by
  intro n hn
  refine Finset.sum_eq_zero fun j hj => ?_
  have hjn := Finset.mem_range.mp hj
  rcases Nat.lt_or_ge j N with h | h
  · have hM : M ≤ n - j := by omega
    rw [hg _ hM, mul_zero]
  · rw [hf j h, zero_mul]

theorem conv_add_left (f f' g : ℕ → R) :
    conv (f + f') g = conv f g + conv f' g := by
  funext n
  simp [conv, add_mul, Finset.sum_add_distrib]

theorem conv_add_right (f g g' : ℕ → R) :
    conv f (g + g') = conv f g + conv f g' := by
  funext n
  simp [conv, mul_add, Finset.sum_add_distrib]

theorem conv_smul_left (c : R) (f g : ℕ → R) :
    conv (c • f) g = c • conv f g := by
  funext n
  simp only [conv, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun j _ => by ring

theorem conv_smul_right (c : R) (f g : ℕ → R) :
    conv f (c • g) = c • conv f g := by
  funext n
  simp only [conv, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun j _ => by ring

/-- Reversal on the window [0, N): the flip g_j ↦ g_{N-1-j}. -/
def revw (N : ℕ) (g : ℕ → R) (k : ℕ) : R :=
  if k < N then g (N - 1 - k) else 0

theorem revw_supported (N : ℕ) (g : ℕ → R) : Supported N (revw N g) :=
  fun k hk => by simp [revw, Nat.not_lt.mpr hk]

theorem revw_add (N : ℕ) (g g' : ℕ → R) :
    revw N (g + g') = revw N g + revw N g' := by
  funext k
  simp only [revw, Pi.add_apply]
  split_ifs <;> simp

/-- Window cross-correlation: corr N f g encodes every lag read
(f ⋆ g~)(d) at index n = (N-1) - d — convolution against the window
reversal, so all closure/bilinearity theorems apply verbatim. -/
def corr (N : ℕ) (f g : ℕ → R) : ℕ → R := conv f (revw N g)

theorem corr_supported {N : ℕ} {f : ℕ → R} (g : ℕ → R)
    (hf : Supported N f) : Supported (N + N - 1) (corr N f g) :=
  conv_supported hf (revw_supported N g)

theorem corr_add_left (N : ℕ) (f f' g : ℕ → R) :
    corr N (f + f') g = corr N f g + corr N f' g :=
  conv_add_left f f' (revw N g)

theorem corr_add_right (N : ℕ) (f g g' : ℕ → R) :
    corr N f (g + g') = corr N f g + corr N f g' := by
  rw [corr, revw_add, conv_add_right]; rfl

theorem corr_smul_left (N : ℕ) (c : R) (f g : ℕ → R) :
    corr N (c • f) g = c • corr N f g :=
  conv_smul_left c f (revw N g)

/-- Grid cell (unit coefficient vector) — the box at position k. -/
def unit (k : ℕ) : ℕ → R := fun j => if j = k then 1 else 0

theorem unit_supported (k : ℕ) : Supported (R := R) (k + 1) (unit k) :=
  fun j hj => if_neg (by omega)

/-- THE EXACT LAG DICTIONARY: the window-N cross-correlation of two
grid cells p, q < N is the shifted delta at index p + (N-1) - q
(lag d = p - q read at n = (N-1) - d) — the grid-level content of the
probe's D3 box×box certificate. -/
theorem corr_unit (N p q : ℕ) (hp : p < N) (hq : q < N) (n : ℕ) :
    corr N (unit p) (unit q) n
      = if n = p + (N - 1) - q then (1 : R) else 0 := by
  have hterm : ∀ j ∈ Finset.range (n + 1), j ≠ p →
      unit (R := R) p j * revw N (unit q) (n - j) = 0 := by
    intro j _ hj
    simp [unit, hj]
  rcases Nat.lt_or_ge n p with hpn | hpn
  · rw [corr, conv,
      Finset.sum_eq_zero fun j hj =>
        hterm j hj (by have := Finset.mem_range.mp hj; omega)]
    rw [if_neg (by omega)]
  · rw [corr, conv,
      Finset.sum_eq_single_of_mem p (Finset.mem_range.mpr (by omega))
        hterm]
    show unit (R := R) p p * revw N (unit q) (n - p)
        = if n = p + (N - 1) - q then 1 else 0
    have hup : unit (R := R) p p = 1 := if_pos rfl
    rw [hup, one_mul]
    show (if n - p < N then unit (R := R) q (N - 1 - (n - p)) else 0)
        = if n = p + (N - 1) - q then 1 else 0
    by_cases hn : n = p + (N - 1) - q
    · have hlt : n - p < N := by omega
      have hqq : N - 1 - (n - p) = q := by omega
      rw [if_pos hn, if_pos hlt, hqq]
      exact if_pos rfl
    · rw [if_neg hn]
      by_cases hlt : n - p < N
      · rw [if_pos hlt]
        exact if_neg fun hqq => hn (by omega)
      · exact if_neg hlt

/-! ### 6. Dyadic inheritance at the grid level -/

/-- One-step dyadic refinement: level-m coefficients inherited on the
level-(m+1) grid, j ↦ f (j / 2). -/
def refine (f : ℕ → R) : ℕ → R := fun j => f (j / 2)

theorem refine_supported {N : ℕ} {f : ℕ → R} (hf : Supported N f) :
    Supported (2 * N) (refine f) :=
  fun k hk => hf _ (by omega)

theorem refine_add (f g : ℕ → R) : refine (f + g) = refine f + refine g :=
  rfl

theorem refine_smul (c : R) (f : ℕ → R) : refine (c • f) = c • refine f :=
  rfl

omit [CommRing R] in
/-- Refinement is injective — nothing is lost passing to a finer
stage (evaluate at even positions). -/
theorem refine_injective : Function.Injective (refine (R := R)) := by
  intro f g h
  funext k
  have h2 : (2 * k) / 2 = k := by omega
  have hk := congrFun h (2 * k)
  simpa only [refine, h2] using hk

/-- EXACT CELL SPLITTING: a coarse cell is exactly the sum of its two
children — the grid-level dyadic inheritance verified in ℚ for all of
I_64 by the probe (D4.2). -/
theorem refine_unit (k : ℕ) :
    refine (R := R) (unit k) = unit (2 * k) + unit (2 * k + 1) := by
  funext j
  simp only [refine, unit, Pi.add_apply]
  by_cases h1 : j = 2 * k
  · subst h1
    rw [if_pos (by omega), if_pos rfl, if_neg (by omega), add_zero]
  · by_cases h2 : j = 2 * k + 1
    · subst h2
      rw [if_pos (by omega), if_neg h1, if_pos rfl, zero_add]
    · rw [if_neg (by omega), if_neg h1, if_neg h2, add_zero]

end Grid

end TfptCarrier.DenseWeilCore
