/-
  ParityLemma — the secular parity lemma (T4 of the TPL round).
  ================================================================

  Lean seam of round 85 (TPL, note CCCLXXXIV (2e)) and its S6 secular
  representation in `experiments/tfpt-discovery/tp_opus_probe.py`
  (32/32 gates): the ground eigenvector of the Galerkin matrix
  collapses the basis to E(t) = sin(at)·2t·f(t²) with the SECULAR
  function f(u) = Σ_k g_k/(u − ω_k) (poles ω_k = om_k², residues
  g_k = (−1)^k c_k/n_k), and the probe's measured law is: a mode
  interval (ω_k, ω_{k+1}) carries an EVEN number of zeros of f iff
  sign(g_k) ≠ sign(g_{k+1}).

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `tendsto_secular_atTop` / `tendsto_secular_atBot` /
        `tendsto_secular_atTop_of_neg_left` — THE BLOW-UP LAWS: at a
        pole with positive residue the secular function tends to +∞
        from the right and to −∞ from the left (to +∞ from the left
        when the residue is negative) — the rest of the sum is
        continuous at the pole, the polar term dominates.  PROVEN.

    (2) `exists_zero_of_pos_pos` / `exists_zero_of_same_sign` /
        `exists_zero_adjacent` — THE EXISTENCE DIRECTION, proven
        unconditionally: if the residues at the two ends of a
        pole-free interval have the SAME sign, f has at least one
        zero strictly inside (IVT between the two blow-ups).  On a
        strictly monotone pole ladder (Fin K) this applies verbatim
        to every adjacent mode interval.

    (3) `parity_of_alternating` — THE COMBINATORIAL PARITY CORE,
        proven: a sequence of reals with s_0 > 0 and alternating
        signs (s_i·s_{i+1} < 0) has 0 < s_n iff n is even.
        `sign_constant_of_no_zero` — a continuous function with no
        zero on an open interval has constant sign there (IVT).

    (4) `zero_count_odd_of_pos_pos` / `zero_count_even_of_pos_neg` /
        `zero_count_even_iff_opposite_residues` — THE PARITY LEMMA:
        given a COMPLETE FINITE listing x_0 < … < x_{m−1} of the
        zeros of f in the mode interval, and the named SIMPLICITY
        hypothesis (see below), the zero count m is ODD iff the two
        boundary residues have the same sign — exactly the S6 law
        "even count iff sign(g_k) ≠ sign(g_{k+1})".

  THE NAMED HYPOTHESIS (the honest boundary).  The assembled parity
  theorems consume, besides finiteness/completeness of the zero
  listing, the hypothesis `simplicity`: the secular values at the
  canonical midpoint samples of consecutive zero-gaps have strictly
  ALTERNATING signs.  For a function whose zeros in the interval are
  all SIMPLE (odd order) this is exactly the sign bookkeeping of the
  probe — deriving it from nonvanishing derivatives (or from the
  rationality of f) needs derivative analysis NOT formalized here, so
  it enters as a named hypothesis, mirroring the (H_cof) discipline
  of `CofinalWeil`.  Without it the parity claim is FALSE (an
  even-order zero flips no sign), so the hypothesis is genuinely
  load-bearing, not decorative.  The identification of (g, ω) with
  the eigenvector data of the wall matrix is the probe's side; no
  spectral claim, no positivity claim, no RH claim is made here.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Tactic

namespace TfptCarrier
namespace ParityLemma

open Filter Topology Set

variable {ι : Type*} [Fintype ι]

/-! ### The secular function -/

/-- The secular function f(u) = Σ_l g_l/(u − ω_l) of a finite pole
family — the S6 normal form of the wall minimizer's zero engine. -/
noncomputable def secular (g ω : ι → ℝ) (u : ℝ) : ℝ :=
  ∑ l, g l / (u - ω l)

/-- Global sign flip of the residues negates the secular function
(zeros are unchanged). -/
theorem secular_neg (g ω : ι → ℝ) (u : ℝ) :
    secular (fun l => -g l) ω u = - secular g ω u := by
  simp [secular, neg_div]

/-- Splitting off the polar term of one designated pole. -/
theorem secular_split [DecidableEq ι] (g ω : ι → ℝ) (j : ι) (u : ℝ) :
    secular g ω u
      = g j / (u - ω j) + ∑ l ∈ Finset.univ.erase j, g l / (u - ω l) :=
  (Finset.add_sum_erase Finset.univ (fun l => g l / (u - ω l))
    (Finset.mem_univ j)).symm

/-- The secular function is continuous away from the poles. -/
theorem continuousAt_secular (g ω : ι → ℝ) {u : ℝ}
    (hu : ∀ l, u ≠ ω l) : ContinuousAt (secular g ω) u := by
  refine tendsto_finset_sum _ fun l _ => ?_
  exact continuousAt_const.div (continuousAt_id.sub continuousAt_const)
    (sub_ne_zero_of_ne (hu l))

/-! ### (1) The blow-up laws at a pole -/

section BlowUp

variable (g ω : ι → ℝ)

/-- The rest of the sum (all terms except pole j) is continuous at
the pole ω j, provided the poles are separated. -/
theorem continuousAt_rest [DecidableEq ι] {j : ι}
    (hsep : ∀ l, l ≠ j → ω l ≠ ω j) :
    ContinuousAt (fun u => ∑ l ∈ Finset.univ.erase j, g l / (u - ω l))
      (ω j) := by
  refine tendsto_finset_sum _ fun l hl => ?_
  have hlj : ω j ≠ ω l := (hsep l (Finset.ne_of_mem_erase hl)).symm
  exact continuousAt_const.div (continuousAt_id.sub continuousAt_const)
    (sub_ne_zero_of_ne hlj)

/-- The recentering u ↦ u − ω j maps the right-neighborhood filter of
the pole to the right-neighborhood filter of 0. -/
theorem tendsto_sub_nhdsGT (c : ℝ) :
    Tendsto (fun u => u - c) (𝓝[>] c) (𝓝[>] (0 : ℝ)) := by
  refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
  · have h : Tendsto (fun u : ℝ => u - c) (𝓝 c) (𝓝 (c - c)) :=
      ((continuous_id.sub continuous_const).tendsto c)
    simpa using h.mono_left nhdsWithin_le_nhds
  · filter_upwards [self_mem_nhdsWithin] with u hu
    simpa [sub_pos] using hu

/-- The left-sided analogue: u ↦ u − c maps 𝓝[<] c to 𝓝[<] 0. -/
theorem tendsto_sub_nhdsLT (c : ℝ) :
    Tendsto (fun u => u - c) (𝓝[<] c) (𝓝[<] (0 : ℝ)) := by
  refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
  · have h : Tendsto (fun u : ℝ => u - c) (𝓝 c) (𝓝 (c - c)) :=
      ((continuous_id.sub continuous_const).tendsto c)
    simpa using h.mono_left nhdsWithin_le_nhds
  · filter_upwards [self_mem_nhdsWithin] with u hu
    simpa [sub_neg] using hu

/-- **Blow-up from the right**: at a pole with POSITIVE residue the
secular function tends to +∞ from the right — the polar term
dominates the continuous rest. -/
theorem tendsto_secular_atTop {j : ι} (hgj : 0 < g j)
    (hsep : ∀ l, l ≠ j → ω l ≠ ω j) :
    Tendsto (secular g ω) (𝓝[>] (ω j)) atTop := by
  classical
  have hpole : Tendsto (fun u => g j / (u - ω j)) (𝓝[>] (ω j)) atTop := by
    have hinv : Tendsto (fun u => (u - ω j)⁻¹) (𝓝[>] (ω j)) atTop :=
      tendsto_inv_nhdsGT_zero.comp (tendsto_sub_nhdsGT (ω j))
    have := (tendsto_const_mul_atTop_of_pos hgj).mpr hinv
    simpa [div_eq_mul_inv] using this
  have hrest : Tendsto
      (fun u => ∑ l ∈ Finset.univ.erase j, g l / (u - ω l))
      (𝓝[>] (ω j))
      (𝓝 (∑ l ∈ Finset.univ.erase j, g l / (ω j - ω l))) :=
    (continuousAt_rest g ω hsep).mono_left nhdsWithin_le_nhds
  exact (hpole.atTop_add hrest).congr
    fun u => (secular_split g ω j u).symm

/-- **Blow-down from the left**: at a pole with POSITIVE residue the
secular function tends to −∞ from the left. -/
theorem tendsto_secular_atBot {k : ι} (hgk : 0 < g k)
    (hsep : ∀ l, l ≠ k → ω l ≠ ω k) :
    Tendsto (secular g ω) (𝓝[<] (ω k)) atBot := by
  classical
  have hpole : Tendsto (fun u => g k / (u - ω k)) (𝓝[<] (ω k)) atBot := by
    have hinv : Tendsto (fun u => (u - ω k)⁻¹) (𝓝[<] (ω k)) atBot :=
      tendsto_inv_nhdsLT_zero.comp (tendsto_sub_nhdsLT (ω k))
    have := (tendsto_const_mul_atBot_of_pos hgk).mpr hinv
    simpa [div_eq_mul_inv] using this
  have hrest : Tendsto
      (fun u => ∑ l ∈ Finset.univ.erase k, g l / (u - ω l))
      (𝓝[<] (ω k))
      (𝓝 (∑ l ∈ Finset.univ.erase k, g l / (ω k - ω l))) :=
    (continuousAt_rest g ω hsep).mono_left nhdsWithin_le_nhds
  exact (hpole.atBot_add hrest).congr
    fun u => (secular_split g ω k u).symm

/-- **Blow-up from the left for a NEGATIVE residue**: sign-flip of
`tendsto_secular_atBot` through `secular_neg`. -/
theorem tendsto_secular_atTop_of_neg_left {k : ι} (hgk : g k < 0)
    (hsep : ∀ l, l ≠ k → ω l ≠ ω k) :
    Tendsto (secular g ω) (𝓝[<] (ω k)) atTop := by
  have hbot : Tendsto (secular (fun l => -g l) ω) (𝓝[<] (ω k)) atBot :=
    tendsto_secular_atBot (fun l => -g l) ω (by simpa using hgk) hsep
  have := tendsto_neg_atTop_iff.mpr hbot
  exact this.congr fun u => by rw [secular_neg, neg_neg]

/-- **Blow-down from the right for a NEGATIVE residue**. -/
theorem tendsto_secular_atBot_of_neg_right {j : ι} (hgj : g j < 0)
    (hsep : ∀ l, l ≠ j → ω l ≠ ω j) :
    Tendsto (secular g ω) (𝓝[>] (ω j)) atBot := by
  have htop : Tendsto (secular (fun l => -g l) ω) (𝓝[>] (ω j)) atTop :=
    tendsto_secular_atTop (fun l => -g l) ω (by simpa using hgj) hsep
  have := tendsto_neg_atBot_iff.mpr htop
  exact this.congr fun u => by rw [secular_neg, neg_neg]

end BlowUp

/-! ### (3a) Constant sign on a zero-free interval (IVT) -/

/-- **Constant sign on a zero-free interval**: a function continuous
and nonvanishing on an open interval has the same strict sign at any
two of its points (else the IVT manufactures a zero). -/
theorem sign_constant_of_no_zero {f : ℝ → ℝ} {p q : ℝ}
    (hcont : ∀ u ∈ Set.Ioo p q, ContinuousAt f u)
    (hnz : ∀ u ∈ Set.Ioo p q, f u ≠ 0)
    {u v : ℝ} (hu : u ∈ Set.Ioo p q) (hv : v ∈ Set.Ioo p q) :
    0 < f u * f v := by
  have main : ∀ u v : ℝ, u ∈ Set.Ioo p q → v ∈ Set.Ioo p q → u ≤ v →
      0 < f u * f v := by
    intro u v hu hv huv
    have hsub : Set.Icc u v ⊆ Set.Ioo p q := fun w hw =>
      ⟨lt_of_lt_of_le hu.1 hw.1, lt_of_le_of_lt hw.2 hv.2⟩
    have hconton : ContinuousOn f (Set.Icc u v) := fun w hw =>
      (hcont w (hsub hw)).continuousWithinAt
    rcases lt_or_gt_of_ne (hnz u hu) with hfu | hfu
    · rcases lt_or_gt_of_ne (hnz v hv) with hfv | hfv
      · exact mul_pos_of_neg_of_neg hfu hfv
      · exfalso
        obtain ⟨w, hw, hfw⟩ :=
          intermediate_value_Icc huv hconton ⟨hfu.le, hfv.le⟩
        exact hnz w (hsub hw) hfw
    · rcases lt_or_gt_of_ne (hnz v hv) with hfv | hfv
      · exfalso
        obtain ⟨w, hw, hfw⟩ :=
          intermediate_value_Icc' huv hconton ⟨hfv.le, hfu.le⟩
        exact hnz w (hsub hw) hfw
      · exact mul_pos hfu hfv
  rcases le_total u v with h | h
  · exact main u v hu hv h
  · rw [mul_comm]; exact main v u hv hu h

/-! ### (2) The existence direction -/

section Existence

variable (g ω : ι → ℝ)

/-- **Existence, positive-positive core**: if the residues at both
ends of a pole-free interval are positive, the secular function has a
zero strictly inside — f > 0 just right of the left pole, f < 0 just
left of the right pole, IVT in between.  PROVEN, no simplicity
hypothesis needed. -/
theorem exists_zero_of_pos_pos {j k : ι} (hjk : ω j < ω k)
    (hsepj : ∀ l, l ≠ j → ω l ≠ ω j) (hsepk : ∀ l, l ≠ k → ω l ≠ ω k)
    (hgap : ∀ l, ω l ∉ Set.Ioo (ω j) (ω k))
    (hgj : 0 < g j) (hgk : 0 < g k) :
    ∃ u ∈ Set.Ioo (ω j) (ω k), secular g ω u = 0 := by
  have hcontIoo : ∀ u ∈ Set.Ioo (ω j) (ω k),
      ContinuousAt (secular g ω) u := by
    intro u hu
    refine continuousAt_secular g ω fun l he => ?_
    exact hgap l (by rw [← he]; exact hu)
  -- a point with positive value just right of ω j
  have hc : ω j < (ω j + ω k) / 2 := by linarith
  have hIoo₁ : Set.Ioo (ω j) ((ω j + ω k) / 2) ∈ 𝓝[>] (ω j) :=
    Ioo_mem_nhdsGT hc
  have hev₁ : ∀ᶠ u in 𝓝[>] (ω j), 0 < secular g ω u :=
    (tendsto_secular_atTop g ω hgj hsepj).eventually_gt_atTop 0
  obtain ⟨x₁, hx₁pos, hx₁mem⟩ :=
    (hev₁.and (eventually_of_mem hIoo₁ fun u hu => hu)).exists
  -- a point with negative value just left of ω k
  have hc' : (ω j + ω k) / 2 < ω k := by linarith
  have hIoo₂ : Set.Ioo ((ω j + ω k) / 2) (ω k) ∈ 𝓝[<] (ω k) :=
    Ioo_mem_nhdsLT hc'
  have hev₂ : ∀ᶠ u in 𝓝[<] (ω k), secular g ω u < 0 :=
    (tendsto_secular_atBot g ω hgk hsepk).eventually_lt_atBot 0
  obtain ⟨x₂, hx₂neg, hx₂mem⟩ :=
    (hev₂.and (eventually_of_mem hIoo₂ fun u hu => hu)).exists
  -- IVT between them
  have hx12 : x₁ ≤ x₂ := le_of_lt (lt_trans hx₁mem.2 hx₂mem.1)
  have hsub : Set.Icc x₁ x₂ ⊆ Set.Ioo (ω j) (ω k) := fun w hw =>
    ⟨lt_of_lt_of_le hx₁mem.1 hw.1,
     lt_of_le_of_lt hw.2 hx₂mem.2⟩
  have hconton : ContinuousOn (secular g ω) (Set.Icc x₁ x₂) :=
    fun w hw => (hcontIoo w (hsub hw)).continuousWithinAt
  obtain ⟨u, hu, hfu⟩ :=
    intermediate_value_Icc' hx12 hconton ⟨hx₂neg.le, hx₁pos.le⟩
  exact ⟨u, hsub hu, hfu⟩

/-- **Existence for same-sign residues** (the valuable direction of
the parity lemma, proven unconditionally): equal residue signs at the
two ends of a pole-free interval force at least one interior zero. -/
theorem exists_zero_of_same_sign {j k : ι} (hjk : ω j < ω k)
    (hsepj : ∀ l, l ≠ j → ω l ≠ ω j) (hsepk : ∀ l, l ≠ k → ω l ≠ ω k)
    (hgap : ∀ l, ω l ∉ Set.Ioo (ω j) (ω k))
    (hsame : 0 < g j * g k) :
    ∃ u ∈ Set.Ioo (ω j) (ω k), secular g ω u = 0 := by
  rcases mul_pos_iff.mp hsame with ⟨hgj, hgk⟩ | ⟨hgj, hgk⟩
  · exact exists_zero_of_pos_pos g ω hjk hsepj hsepk hgap hgj hgk
  · obtain ⟨u, hu, hz⟩ :=
      exists_zero_of_pos_pos (fun l => -g l) ω hjk hsepj hsepk hgap
        (by simpa using hgj) (by simpa using hgk)
    rw [secular_neg, neg_eq_zero] at hz
    exact ⟨u, hu, hz⟩

end Existence

/-- **Existence on the mode ladder**: on a strictly monotone pole
ladder ω : Fin K → ℝ, every adjacent mode interval whose two residues
share a sign contains a zero of the secular function — the concrete
S6 instance. -/
theorem exists_zero_adjacent {K : ℕ} (g ω : Fin K → ℝ)
    (hω : StrictMono ω) (k : Fin K) (hk1 : (k : ℕ) + 1 < K)
    (hsame : 0 < g k * g ⟨(k : ℕ) + 1, hk1⟩) :
    ∃ u ∈ Set.Ioo (ω k) (ω ⟨(k : ℕ) + 1, hk1⟩), secular g ω u = 0 := by
  have hlt : k < (⟨(k : ℕ) + 1, hk1⟩ : Fin K) :=
    Fin.lt_def.mpr (Nat.lt_succ_self _)
  refine exists_zero_of_same_sign g ω (hω hlt) ?_ ?_ ?_ hsame
  · exact fun l hl he => hl (hω.injective he)
  · exact fun l hl he => hl (hω.injective he)
  · rintro l ⟨h1, h2⟩
    have hl1 : (k : ℕ) < (l : ℕ) := Fin.lt_def.mp (hω.lt_iff_lt.mp h1)
    have hl2 : (l : ℕ) < (k : ℕ) + 1 := Fin.lt_def.mp (hω.lt_iff_lt.mp h2)
    omega

/-! ### (3b) The combinatorial parity core -/

/-- **Parity from alternation**: if s_0 > 0 and consecutive terms
strictly alternate in sign up to n, then s_n is positive exactly for
even n.  Pure induction; this is the entire combinatorial content of
the parity lemma. -/
theorem parity_of_alternating (s : ℕ → ℝ) (h0 : 0 < s 0) :
    ∀ n, (∀ i, i < n → s i * s (i + 1) < 0) → (0 < s n ↔ Even n) := by
  intro n
  induction n with
  | zero => intro _; simp [h0]
  | succ n ih =>
    intro halt
    have hn := ih fun i hi => halt i (by omega)
    have hswap := halt n (by omega)
    constructor
    · intro hpos
      have hsn : s n < 0 := by nlinarith
      rw [Nat.even_add_one]
      intro hev
      exact absurd (hn.mpr hev) (not_lt.mpr hsn.le)
    · intro hev
      have hnodd : ¬ Even n := by rwa [Nat.even_add_one] at hev
      have hsn : ¬ 0 < s n := fun h => hnodd (hn.mp h)
      have hne : s n ≠ 0 := fun h => by simp [h] at hswap
      have hlt : s n < 0 := lt_of_le_of_ne (not_lt.mp hsn) hne
      nlinarith

/-! ### The gap scaffolding for the zero listing -/

/-- Left endpoint of gap i in the listing a < x_0 < … < x_{m−1} < b:
gap 0 starts at a, gap i (i ≥ 1) starts at x_{i−1}. -/
def gapLeft (a : ℝ) (x : ℕ → ℝ) (i : ℕ) : ℝ :=
  if i = 0 then a else x (i - 1)

/-- Right endpoint of gap i: gap i (i < m) ends at x_i, gap m ends
at b. -/
def gapRight (b : ℝ) (x : ℕ → ℝ) (m i : ℕ) : ℝ :=
  if i < m then x i else b

/-- The canonical midpoint sample of gap i — the point at which the
simplicity hypothesis reads the sign of the secular function. -/
noncomputable def gapSample (a b : ℝ) (x : ℕ → ℝ) (m i : ℕ) : ℝ :=
  (gapLeft a x i + gapRight b x m i) / 2

section Gaps

variable {a b : ℝ} {x : ℕ → ℝ} {m : ℕ}

/-- Each gap is a genuine interval. -/
theorem gapLeft_lt_gapRight (hab : a < b)
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    (hmem : ∀ i, i < m → x i ∈ Set.Ioo a b)
    {i : ℕ} (hi : i ≤ m) : gapLeft a x i < gapRight b x m i := by
  unfold gapLeft gapRight
  rcases Nat.eq_zero_or_pos i with h0 | hpos
  · subst h0
    rw [if_pos rfl]
    by_cases hm : 0 < m
    · rw [if_pos hm]; exact (hmem 0 hm).1
    · rw [if_neg hm]; exact hab
  · rw [if_neg (by omega)]
    by_cases him : i < m
    · rw [if_pos him]; exact hmono (i - 1) i (by omega) him
    · rw [if_neg him]
      exact (hmem (i - 1) (by omega)).2

/-- Each gap sits inside the mode interval. -/
theorem gap_subset (hmem : ∀ i, i < m → x i ∈ Set.Ioo a b)
    {i : ℕ} (hi : i ≤ m) :
    Set.Ioo (gapLeft a x i) (gapRight b x m i) ⊆ Set.Ioo a b := by
  have hL : a ≤ gapLeft a x i := by
    unfold gapLeft
    rcases Nat.eq_zero_or_pos i with h0 | hpos
    · subst h0; simp
    · rw [if_neg (by omega)]
      exact (hmem (i - 1) (by omega)).1.le
  have hR : gapRight b x m i ≤ b := by
    unfold gapRight
    by_cases him : i < m
    · rw [if_pos him]; exact (hmem i him).2.le
    · rw [if_neg him]
  intro u hu
  exact ⟨lt_of_le_of_lt hL hu.1, lt_of_lt_of_le hu.2 hR⟩

/-- No listed zero lies strictly inside any gap — the gaps are
zero-free once the listing is complete. -/
theorem listed_not_mem_gap
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    {i : ℕ} (hi : i ≤ m) {l : ℕ} (hl : l < m) :
    x l ∉ Set.Ioo (gapLeft a x i) (gapRight b x m i) := by
  rintro ⟨h1, h2⟩
  rcases lt_or_ge l i with hli | hil
  · have hi0 : i ≠ 0 := by omega
    have hle : x l ≤ x (i - 1) := by
      rcases eq_or_lt_of_le (by omega : l ≤ i - 1) with he | hlt
      · rw [he]
      · exact (hmono l (i - 1) hlt (by omega)).le
    rw [gapLeft, if_neg hi0] at h1
    linarith
  · have him : i < m := lt_of_le_of_lt hil hl
    have hle : x i ≤ x l := by
      rcases eq_or_lt_of_le hil with he | hlt
      · rw [he]
      · exact (hmono i l hlt hl).le
    rw [gapRight, if_pos him] at h2
    linarith

/-- The midpoint sample lies in its gap. -/
theorem gapSample_mem (hab : a < b)
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    (hmem : ∀ i, i < m → x i ∈ Set.Ioo a b)
    {i : ℕ} (hi : i ≤ m) :
    gapSample a b x m i
      ∈ Set.Ioo (gapLeft a x i) (gapRight b x m i) := by
  have h := gapLeft_lt_gapRight hab hmono hmem hi
  unfold gapSample
  constructor <;> linarith

end Gaps

/-! ### (4) The assembled parity lemma -/

section Parity

variable (g ω : ι → ℝ)

/-- **THE PARITY LEMMA, same-sign core (both residues positive)**:
given a complete finite listing x_0 < … < x_{m−1} of the zeros of the
secular function in the pole-free mode interval (ω j, ω k), and the
NAMED simplicity hypothesis (strictly alternating signs at the
canonical gap samples — see module docstring), positive residues at
BOTH ends force an ODD zero count.  The boundary signs are PROVEN
from the blow-up laws; only the interior alternation is hypothesis. -/
theorem zero_count_odd_of_pos_pos {j k : ι} (hjk : ω j < ω k)
    (hsepj : ∀ l, l ≠ j → ω l ≠ ω j) (hsepk : ∀ l, l ≠ k → ω l ≠ ω k)
    (hgap : ∀ l, ω l ∉ Set.Ioo (ω j) (ω k))
    (hgj : 0 < g j) (hgk : 0 < g k)
    {m : ℕ} {x : ℕ → ℝ}
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    (hmem : ∀ i, i < m → x i ∈ Set.Ioo (ω j) (ω k))
    (_hzero : ∀ i, i < m → secular g ω (x i) = 0)
    (hcomplete : ∀ u ∈ Set.Ioo (ω j) (ω k), secular g ω u = 0 →
      ∃ i < m, x i = u)
    (simplicity : ∀ i, i < m →
      secular g ω (gapSample (ω j) (ω k) x m i)
        * secular g ω (gapSample (ω j) (ω k) x m (i + 1)) < 0) :
    ¬ Even m := by
  have hab : ω j < ω k := hjk
  -- continuity inside the mode interval
  have hcontIoo : ∀ u ∈ Set.Ioo (ω j) (ω k),
      ContinuousAt (secular g ω) u := by
    intro u hu
    refine continuousAt_secular g ω fun l he => ?_
    exact hgap l (by rw [← he]; exact hu)
  -- the gaps are zero-free
  have hnzgap : ∀ i, i ≤ m → ∀ u ∈ Set.Ioo (gapLeft (ω j) x i)
      (gapRight (ω k) x m i), secular g ω u ≠ 0 := by
    intro i hi u hu hz
    obtain ⟨l, hl, hxl⟩ :=
      hcomplete u (gap_subset hmem hi hu) hz
    exact listed_not_mem_gap hmono hi hl (hxl ▸ hu)
  have hcontgap : ∀ i, i ≤ m → ∀ u ∈ Set.Ioo (gapLeft (ω j) x i)
      (gapRight (ω k) x m i), ContinuousAt (secular g ω) u :=
    fun i hi u hu => hcontIoo u (gap_subset hmem hi hu)
  -- boundary sign at the left end: s 0 > 0
  have h0 : 0 < secular g ω (gapSample (ω j) (ω k) x m 0) := by
    have hR : ω j < gapRight (ω k) x m 0 := by
      have h := gapLeft_lt_gapRight hab hmono hmem (Nat.zero_le m)
      simpa [gapLeft] using h
    have hIoo : Set.Ioo (ω j) (gapRight (ω k) x m 0) ∈ 𝓝[>] (ω j) :=
      Ioo_mem_nhdsGT hR
    have hev : ∀ᶠ u in 𝓝[>] (ω j), 0 < secular g ω u :=
      (tendsto_secular_atTop g ω hgj hsepj).eventually_gt_atTop 0
    obtain ⟨u₀, hu₀pos, hu₀mem⟩ :=
      (hev.and (eventually_of_mem hIoo fun u hu => hu)).exists
    have hu₀gap : u₀ ∈ Set.Ioo (gapLeft (ω j) x 0)
        (gapRight (ω k) x m 0) := by
      simpa [gapLeft] using hu₀mem
    have hconst := sign_constant_of_no_zero
      (hcontgap 0 (Nat.zero_le m)) (hnzgap 0 (Nat.zero_le m))
      hu₀gap (gapSample_mem hab hmono hmem (Nat.zero_le m))
    rcases mul_pos_iff.mp hconst with ⟨_, h⟩ | ⟨h, _⟩
    · exact h
    · linarith
  -- boundary sign at the right end: s m < 0
  have hm : secular g ω (gapSample (ω j) (ω k) x m m) < 0 := by
    have hL : gapLeft (ω j) x m < ω k := by
      have h := gapLeft_lt_gapRight hab hmono hmem (le_refl m)
      simpa [gapRight] using h
    have hIoo : Set.Ioo (gapLeft (ω j) x m) (ω k) ∈ 𝓝[<] (ω k) :=
      Ioo_mem_nhdsLT hL
    have hev : ∀ᶠ u in 𝓝[<] (ω k), secular g ω u < 0 :=
      (tendsto_secular_atBot g ω hgk hsepk).eventually_lt_atBot 0
    obtain ⟨u₁, hu₁neg, hu₁mem⟩ :=
      (hev.and (eventually_of_mem hIoo fun u hu => hu)).exists
    have hu₁gap : u₁ ∈ Set.Ioo (gapLeft (ω j) x m)
        (gapRight (ω k) x m m) := by
      simpa [gapRight] using hu₁mem
    have hconst := sign_constant_of_no_zero
      (hcontgap m (le_refl m)) (hnzgap m (le_refl m))
      hu₁gap (gapSample_mem hab hmono hmem (le_refl m))
    rcases mul_pos_iff.mp hconst with ⟨h, _⟩ | ⟨_, h⟩
    · linarith
    · exact h
  -- alternation forces odd parity
  intro hev
  have hiff := parity_of_alternating
    (fun i => secular g ω (gapSample (ω j) (ω k) x m i)) h0 m
    (fun i hi => simplicity i hi)
  have := hiff.mpr hev
  linarith

/-- **THE PARITY LEMMA, opposite-sign core (left residue positive,
right residue negative)**: with the same listing and simplicity
hypotheses, opposite residue signs force an EVEN zero count — the
secular function now blows UP at both ends of the interval. -/
theorem zero_count_even_of_pos_neg {j k : ι} (hjk : ω j < ω k)
    (hsepj : ∀ l, l ≠ j → ω l ≠ ω j) (hsepk : ∀ l, l ≠ k → ω l ≠ ω k)
    (hgap : ∀ l, ω l ∉ Set.Ioo (ω j) (ω k))
    (hgj : 0 < g j) (hgk : g k < 0)
    {m : ℕ} {x : ℕ → ℝ}
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    (hmem : ∀ i, i < m → x i ∈ Set.Ioo (ω j) (ω k))
    (_hzero : ∀ i, i < m → secular g ω (x i) = 0)
    (hcomplete : ∀ u ∈ Set.Ioo (ω j) (ω k), secular g ω u = 0 →
      ∃ i < m, x i = u)
    (simplicity : ∀ i, i < m →
      secular g ω (gapSample (ω j) (ω k) x m i)
        * secular g ω (gapSample (ω j) (ω k) x m (i + 1)) < 0) :
    Even m := by
  have hab : ω j < ω k := hjk
  have hcontIoo : ∀ u ∈ Set.Ioo (ω j) (ω k),
      ContinuousAt (secular g ω) u := by
    intro u hu
    refine continuousAt_secular g ω fun l he => ?_
    exact hgap l (by rw [← he]; exact hu)
  have hnzgap : ∀ i, i ≤ m → ∀ u ∈ Set.Ioo (gapLeft (ω j) x i)
      (gapRight (ω k) x m i), secular g ω u ≠ 0 := by
    intro i hi u hu hz
    obtain ⟨l, hl, hxl⟩ :=
      hcomplete u (gap_subset hmem hi hu) hz
    exact listed_not_mem_gap hmono hi hl (hxl ▸ hu)
  have hcontgap : ∀ i, i ≤ m → ∀ u ∈ Set.Ioo (gapLeft (ω j) x i)
      (gapRight (ω k) x m i), ContinuousAt (secular g ω) u :=
    fun i hi u hu => hcontIoo u (gap_subset hmem hi hu)
  have h0 : 0 < secular g ω (gapSample (ω j) (ω k) x m 0) := by
    have hR : ω j < gapRight (ω k) x m 0 := by
      have h := gapLeft_lt_gapRight hab hmono hmem (Nat.zero_le m)
      simpa [gapLeft] using h
    have hIoo : Set.Ioo (ω j) (gapRight (ω k) x m 0) ∈ 𝓝[>] (ω j) :=
      Ioo_mem_nhdsGT hR
    have hev : ∀ᶠ u in 𝓝[>] (ω j), 0 < secular g ω u :=
      (tendsto_secular_atTop g ω hgj hsepj).eventually_gt_atTop 0
    obtain ⟨u₀, hu₀pos, hu₀mem⟩ :=
      (hev.and (eventually_of_mem hIoo fun u hu => hu)).exists
    have hu₀gap : u₀ ∈ Set.Ioo (gapLeft (ω j) x 0)
        (gapRight (ω k) x m 0) := by
      simpa [gapLeft] using hu₀mem
    have hconst := sign_constant_of_no_zero
      (hcontgap 0 (Nat.zero_le m)) (hnzgap 0 (Nat.zero_le m))
      hu₀gap (gapSample_mem hab hmono hmem (Nat.zero_le m))
    rcases mul_pos_iff.mp hconst with ⟨_, h⟩ | ⟨h, _⟩
    · exact h
    · linarith
  -- at the right end the NEGATIVE residue blows UP from the left
  have hm : 0 < secular g ω (gapSample (ω j) (ω k) x m m) := by
    have hL : gapLeft (ω j) x m < ω k := by
      have h := gapLeft_lt_gapRight hab hmono hmem (le_refl m)
      simpa [gapRight] using h
    have hIoo : Set.Ioo (gapLeft (ω j) x m) (ω k) ∈ 𝓝[<] (ω k) :=
      Ioo_mem_nhdsLT hL
    have hev : ∀ᶠ u in 𝓝[<] (ω k), 0 < secular g ω u :=
      (tendsto_secular_atTop_of_neg_left g ω hgk hsepk).eventually_gt_atTop 0
    obtain ⟨u₁, hu₁pos, hu₁mem⟩ :=
      (hev.and (eventually_of_mem hIoo fun u hu => hu)).exists
    have hu₁gap : u₁ ∈ Set.Ioo (gapLeft (ω j) x m)
        (gapRight (ω k) x m m) := by
      simpa [gapRight] using hu₁mem
    have hconst := sign_constant_of_no_zero
      (hcontgap m (le_refl m)) (hnzgap m (le_refl m))
      hu₁gap (gapSample_mem hab hmono hmem (le_refl m))
    rcases mul_pos_iff.mp hconst with ⟨_, h⟩ | ⟨h, _⟩
    · exact h
    · linarith
  have hiff := parity_of_alternating
    (fun i => secular g ω (gapSample (ω j) (ω k) x m i)) h0 m
    (fun i hi => simplicity i hi)
  exact hiff.mp hm

/-- **THE PARITY LEMMA (unified iff form)** — the exact S6 law of
tp_opus_probe / note CCCLXXXIV (2e): for nonzero boundary residues,
the zero count of the secular function in a pole-free mode interval
is EVEN iff the residue signs DIFFER, under the named simplicity
hypothesis and a complete finite zero listing.  All four sign cases
reduce to the two cores; the global residue flip g ↦ −g leaves the
zeros, the samples, and the alternation hypothesis invariant. -/
theorem zero_count_even_iff_opposite_residues {j k : ι}
    (hjk : ω j < ω k)
    (hsepj : ∀ l, l ≠ j → ω l ≠ ω j) (hsepk : ∀ l, l ≠ k → ω l ≠ ω k)
    (hgap : ∀ l, ω l ∉ Set.Ioo (ω j) (ω k))
    (hgj : g j ≠ 0) (hgk : g k ≠ 0)
    {m : ℕ} {x : ℕ → ℝ}
    (hmono : ∀ i₁ i₂, i₁ < i₂ → i₂ < m → x i₁ < x i₂)
    (hmem : ∀ i, i < m → x i ∈ Set.Ioo (ω j) (ω k))
    (hzero : ∀ i, i < m → secular g ω (x i) = 0)
    (hcomplete : ∀ u ∈ Set.Ioo (ω j) (ω k), secular g ω u = 0 →
      ∃ i < m, x i = u)
    (simplicity : ∀ i, i < m →
      secular g ω (gapSample (ω j) (ω k) x m i)
        * secular g ω (gapSample (ω j) (ω k) x m (i + 1)) < 0) :
    (Even m ↔ g j * g k < 0) := by
  -- transfer package for the global residue flip g ↦ −g
  have hzero' : ∀ i, i < m → secular (fun l => -g l) ω (x i) = 0 := by
    intro i hi
    rw [secular_neg, neg_eq_zero]
    exact hzero i hi
  have hcomp' : ∀ u ∈ Set.Ioo (ω j) (ω k),
      secular (fun l => -g l) ω u = 0 → ∃ i < m, x i = u := by
    intro u hu hz
    rw [secular_neg, neg_eq_zero] at hz
    exact hcomplete u hu hz
  have hsimp' : ∀ i, i < m →
      secular (fun l => -g l) ω (gapSample (ω j) (ω k) x m i)
        * secular (fun l => -g l) ω (gapSample (ω j) (ω k) x m (i + 1))
        < 0 := by
    intro i hi
    rw [secular_neg, secular_neg]
    simpa using simplicity i hi
  rcases lt_or_gt_of_ne hgj with hj | hj
  · rcases lt_or_gt_of_ne hgk with hk' | hk'
    · -- (−,−): flip to (+,+) ⇒ odd count; product positive
      have hodd := zero_count_odd_of_pos_pos (fun l => -g l) ω hjk
        hsepj hsepk hgap (by simpa using hj) (by simpa using hk')
        hmono hmem hzero' hcomp' hsimp'
      exact iff_of_false hodd (not_lt.mpr (mul_pos_of_neg_of_neg hj hk').le)
    · -- (−,+): flip to (+,−) ⇒ even count; product negative
      have heven := zero_count_even_of_pos_neg (fun l => -g l) ω hjk
        hsepj hsepk hgap (by simpa using hj) (by simpa using hk')
        hmono hmem hzero' hcomp' hsimp'
      exact iff_of_true heven (mul_neg_of_neg_of_pos hj hk')
  · rcases lt_or_gt_of_ne hgk with hk' | hk'
    · -- (+,−): even count; product negative
      have heven := zero_count_even_of_pos_neg g ω hjk
        hsepj hsepk hgap hj hk'
        hmono hmem hzero hcomplete simplicity
      exact iff_of_true heven (mul_neg_of_pos_of_neg hj hk')
    · -- (+,+): odd count; product positive
      have hodd := zero_count_odd_of_pos_pos g ω hjk
        hsepj hsepk hgap hj hk'
        hmono hmem hzero hcomplete simplicity
      exact iff_of_false hodd (not_lt.mpr (mul_pos hj hk').le)

end Parity

end ParityLemma
end TfptCarrier
