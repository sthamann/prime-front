/-
RH/GaborWindowGlue.lean -- r595 three-term window+tail comparison.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r594 supplied the outer `|Q|` Finset bound
`abs_gaborQuadrupole_outer_mult_finset_le_theta` and the local-
margin comparison `GaborOuterTailSmallerThanLocalMargin_holds`.
r589/r594 already give window negativity
(`gaborWeightedTruncation_honestWeil_neg`, BoundLog2:
`W_honest < (9/10 − η) · E < 0`) on every nonempty increment-
compliant isolated catalog.

This round glues those bricks on finite catalogs:

  (1) `W_honest(Z) = W_honest(window) + Σ_outer Q
                    ≤ W_honest(window) + Σ_outer m|Q|
                    ≤ W_honest(window) + C(a,ω) exp(−1/(8a))`.

  (2) Window BoundLog2 plus the r594 tail-vs-margin modulus:
      if the isolation width sits below that `a₀`, the whole
      finite extension scores `W_honest < 0`.

  (3) Per-`T` instantiation of `GaborWindowAdaptiveCofinalNeg`
      on `gaborWeightedTruncationConfig T` (some `δ(T) > 0`).
      A `T`-uniform `δ` is *not* implied: the isolation host is
      retuned as `T` grows (r592).  That gap is the unasserted
      `GaborWindowAdaptiveUniformDelta`, not a `sorry`.

No asserting `sorry`.  Census unchanged.
-/
import RH.GaborOuterTail
import RH.GaborDominanceLog2

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical
open Set Finset

/-! ## Catalog slices -/

/-- Restrict a catalog to a decidable predicate on points.
Multiplicities and off-line / `γ > 0` constraints are inherited. -/
noncomputable def gaborFilterConfig (Z : GaborCanonicalConfig)
    (p : ℝ × ℝ → Prop) [DecidablePred p] : GaborCanonicalConfig where
  pts := Z.pts.filter p
  mult := Z.mult
  mult_pos := fun q hq => Z.mult_pos q (mem_filter.mp hq).1
  sigma_off := fun q hq => Z.sigma_off q (mem_filter.mp hq).1
  gamma_pos := fun q hq => Z.gamma_pos q (mem_filter.mp hq).1

/-- Window slice `|γ − ω| < R`. -/
noncomputable def gaborWindowSlice (Z : GaborCanonicalConfig)
    (omega R : ℝ) : GaborCanonicalConfig :=
  gaborFilterConfig Z (fun q => |q.2 - omega| < R)

/-- Outer slice `|γ − ω| ≥ R`. -/
noncomputable def gaborOuterSlice (Z : GaborCanonicalConfig)
    (omega R : ℝ) : GaborCanonicalConfig :=
  gaborFilterConfig Z (fun q => R ≤ |q.2 - omega|)

theorem gaborFilterConfig_incrementCompliantLog
    (Z : GaborCanonicalConfig)
    (h : GaborConfigIncrementCompliantLog Z)
    (p : ℝ × ℝ → Prop) [DecidablePred p] :
    GaborConfigIncrementCompliantLog (gaborFilterConfig Z p) := by
  intro k
  have hsub :
      ((gaborFilterConfig Z p).pts.filter
          (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)) ⊆
        Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1) := by
    intro q hq
    have hqf := mem_filter.mp hq
    have hqZ := (mem_filter.mp hqf.1).1
    exact mem_filter.mpr ⟨hqZ, hqf.2⟩
  exact (sum_le_sum_of_subset_of_nonneg hsub
      (fun _ _ _ => Nat.cast_nonneg _)).trans (h k)

theorem gaborFilterConfig_gammaDistinct
    (Z : GaborCanonicalConfig) (h : Z.gammaDistinct)
    (p : ℝ × ℝ → Prop) [DecidablePred p] :
    (gaborFilterConfig Z p).gammaDistinct := by
  intro q₁ hq₁ q₂ hq₂ hγ
  exact h q₁ (mem_filter.mp hq₁).1 q₂ (mem_filter.mp hq₂).1 hγ

theorem gaborWindowSlice_incrementCompliantLog
    (Z : GaborCanonicalConfig)
    (h : GaborConfigIncrementCompliantLog Z) (omega R : ℝ) :
    GaborConfigIncrementCompliantLog (gaborWindowSlice Z omega R) :=
  gaborFilterConfig_incrementCompliantLog Z h _

theorem gaborWindowSlice_gammaDistinct
    (Z : GaborCanonicalConfig) (h : Z.gammaDistinct) (omega R : ℝ) :
    (gaborWindowSlice Z omega R).gammaDistinct :=
  gaborFilterConfig_gammaDistinct Z h _

theorem gaborOuterSlice_incrementCompliantLog
    (Z : GaborCanonicalConfig)
    (h : GaborConfigIncrementCompliantLog Z) (omega R : ℝ) :
    GaborConfigIncrementCompliantLog (gaborOuterSlice Z omega R) :=
  gaborFilterConfig_incrementCompliantLog Z h _

lemma gaborWindow_disj_outer (Z : GaborCanonicalConfig) (omega R : ℝ) :
    Disjoint
      (Z.pts.filter (fun q => |q.2 - omega| < R))
      (Z.pts.filter (fun q => R ≤ |q.2 - omega|)) := by
  rw [Finset.disjoint_left]
  intro q hqW hqO
  exact not_lt.mpr (mem_filter.mp hqO).2 (mem_filter.mp hqW).2

lemma gaborWindow_union_outer (Z : GaborCanonicalConfig) (omega R : ℝ) :
    Z.pts.filter (fun q => |q.2 - omega| < R) ∪
      Z.pts.filter (fun q => R ≤ |q.2 - omega|) = Z.pts := by
  ext q
  simp only [Finset.mem_union, mem_filter]
  constructor
  · intro h
    rcases h with h | h <;> exact h.1
  · intro hq
    by_cases hlt : |q.2 - omega| < R
    · exact Or.inl ⟨hq, hlt⟩
    · exact Or.inr ⟨hq, le_of_not_gt hlt⟩

/-! ## (1) Honest-Weil split and outer `|Q|` tail -/

/-- Multiplicity-weighted outer `|Q|` sum of a catalog. -/
noncomputable def gaborOuterAbsSum (a omega : ℝ)
    (Z : GaborCanonicalConfig) (R : ℝ) : ℝ :=
  (Z.pts.filter (fun q => R ≤ |q.2 - omega|)).sum
    (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|)

/-- Linear split at a common packet: the on-line budget is shared,
so `W_honest(Z) = W_honest(window) + Σ_outer Q`. -/
theorem gaborHonestWeil_window_add_outer
    (a omega R Cinc : ℝ) (Z : GaborCanonicalConfig) :
    gaborHonestWeil a omega Z Cinc =
      gaborHonestWeil a omega (gaborWindowSlice Z omega R) Cinc +
        (gaborOuterSlice Z omega R).pts.sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
  rw [gaborHonestWeil_linear, gaborHonestWeil_linear]
  have hdisj := gaborWindow_disj_outer Z omega R
  have hunion := gaborWindow_union_outer Z omega R
  have hQ :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) =
        (Z.pts.filter (fun q => |q.2 - omega| < R)).sum
            (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
          (Z.pts.filter (fun q => R ≤ |q.2 - omega|)).sum
            (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
    rw [← sum_union hdisj, hunion]
  simp only [gaborWindowSlice, gaborOuterSlice, gaborFilterConfig] at hQ ⊢
  linarith [hQ]

/-- Triangle: `Σ_outer Q ≤ Σ_outer m|Q|`. -/
theorem gaborHonestWeil_le_window_plus_outerAbs
    (a omega R Cinc : ℝ) (Z : GaborCanonicalConfig) :
    gaborHonestWeil a omega Z Cinc ≤
      gaborHonestWeil a omega (gaborWindowSlice Z omega R) Cinc +
        gaborOuterAbsSum a omega Z R := by
  rw [gaborHonestWeil_window_add_outer]
  refine add_le_add (le_refl _) ?_
  unfold gaborOuterAbsSum gaborOuterSlice gaborFilterConfig
  refine sum_le_sum fun q _ =>
    mul_le_mul_of_nonneg_left (le_abs_self _) (Nat.cast_nonneg _)

/-- Increment-compliant catalogs pack into the same Path-A log-theta
as the zero Finset bound.  Used to transport
`abs_gaborQuadrupole_outer_mult_finset_le_theta` off the zero
subtype and onto `GaborCanonicalConfig`. -/
lemma gaborOuter_gaussMass_le_theta
    {a omega R : ℝ} (ha : 0 < a) (_hω : 0 < omega)
    (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z) :
    (Z.pts.filter (fun q => R ≤ |q.2 - omega|)).sum
        (fun q => (Z.mult q : ℝ) * gaussWeight (2 * a) omega q.2) ≤
      gaborLogWeightedTheta (2 * a) omega := by
  have h2a : 0 < 2 * a := mul_pos (by norm_num) ha
  have hMs : Summable fun k : ℤ =>
      gaborBinCountMajorant k * gaussBinMax (2 * a) omega k :=
    gaborLogWeightedThetaSummable h2a omega
  refine bin_partial_summation_mass (w := gaussWeight (2 * a) omega)
      (fun _ => gaussWeight_nonneg _ _ _)
      (Z.pts.filter (fun q => R ≤ |q.2 - omega|))
      (fun q => q.2) (fun q => (Z.mult q : ℝ))
      (fun _ => Nat.cast_nonneg _)
      gaborBinCountMajorant gaborBinCountMajorant_nonneg
      (fun k => ?hC) (fun k => gaussBinMax_nonneg h2a k)
      (fun _k _t ht => le_gaussBinMax h2a ht) hMs
  · have hsub :
        ((Z.pts.filter (fun q => R ≤ |q.2 - omega|)).filter
            (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)) ⊆
          Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1) := by
      intro q hq
      have hqf := mem_filter.mp hq
      exact mem_filter.mpr ⟨(mem_filter.mp hqf.1).1, hqf.2⟩
    exact (sum_le_sum_of_subset_of_nonneg hsub
        (fun _ _ _ => Nat.cast_nonneg _)).trans
      ((hinc k).trans_eq (gaborKBinAt_eq_binCountMajorant k))

/-- Catalog form of `abs_gaborQuadrupole_outer_mult_finset_le_theta`:
increment compliance replaces the zero-bin majorant, same
`C(a,ω) exp(−1/(8a))` ceiling.  Rate at `R ≥ 1`. -/
theorem abs_gaborQuadrupole_outer_config_le_theta
    {a omega R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega)
    (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z) :
    gaborOuterAbsSum a omega Z R ≤
      gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  set S := Z.pts.filter (fun q => R ≤ |q.2 - omega|)
  have hpt : ∀ q ∈ S,
      (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2| ≤
        (Z.mult q : ℝ) *
          ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            gaborThreeLobe a omega q.2) := by
    intro q hq
    have hqZ := (mem_filter.mp hq).1
    have hQ := abs_gaborQuadrupole_le_enhancement_threeLobe
      (a := a) (omega := omega) (sigma := q.1) (gamma := q.2) ha
    have hσ2 : q.1 ^ 2 ≤ (1 / 4 : ℝ) :=
      (gabor_sigma_sq_lt_quarter (Z.sigma_off q hqZ).1
        (Z.sigma_off q hqZ).2).le
    have hE :
        gaborEnhancement q.1 a ≤
          (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
      unfold gaborEnhancement
      refine mul_le_mul_of_nonneg_left ?_
        (div_nonneg Real.pi_pos.le ha.le)
      exact Real.exp_le_exp.mpr
        (div_le_div_of_nonneg_right hσ2
          (mul_nonneg (by norm_num) ha.le))
    exact mul_le_mul_of_nonneg_left
      (hQ.trans (mul_le_mul_of_nonneg_right hE
        (gaborThreeLobe_nonneg _ _ _)))
      (Nat.cast_nonneg _)
  have hsum := sum_le_sum hpt
  have hC : 0 ≤ (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) := by
    positivity
  have hfactor :
      S.sum (fun q =>
          (Z.mult q : ℝ) *
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
              gaborThreeLobe a omega q.2)) =
        (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          S.sum (fun q =>
            (Z.mult q : ℝ) * gaborThreeLobe a omega q.2) := by
    calc
      S.sum (fun q =>
          (Z.mult q : ℝ) *
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
              gaborThreeLobe a omega q.2)) =
          S.sum (fun q =>
            ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a))) *
              ((Z.mult q : ℝ) * gaborThreeLobe a omega q.2)) :=
        sum_congr rfl fun _ _ => by ring
      _ = ((Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a))) *
          S.sum (fun q =>
            (Z.mult q : ℝ) * gaborThreeLobe a omega q.2) :=
        (mul_sum _ _ _).symm
  have hthree : ∀ q ∈ S,
      (Z.mult q : ℝ) * gaborThreeLobe a omega q.2 ≤
        (Z.mult q : ℝ) *
          (4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaussWeight (2 * a) omega q.2) := by
    intro q hq
    have hqZ := (mem_filter.mp hq).1
    have hd := (mem_filter.mp hq).2
    have hsign : 0 ≤ omega * q.2 :=
      mul_nonneg hω.le (Z.gamma_pos q hqZ).le
    have hfour := gaborThreeLobe_le_four_minus (a := a) ha hsign
    have hsplit := gaussWeight_outer_split (a := a) (omega := omega)
      (t := q.2) (R := R) ha (by linarith [hR]) hd
    have hcomb := hfour.trans
      (mul_le_mul_of_nonneg_left hsplit (by norm_num : (0 : ℝ) ≤ 4))
    exact mul_le_mul_of_nonneg_left
      (hcomb.trans_eq (by ring)) (Nat.cast_nonneg _)
  have hsum₃ := sum_le_sum hthree
  have he : 0 ≤ 4 * Real.exp (-R ^ 2 / (4 * a)) := by positivity
  have hfactor₃ :
      S.sum (fun q =>
          (Z.mult q : ℝ) *
            (4 * Real.exp (-R ^ 2 / (4 * a)) *
              gaussWeight (2 * a) omega q.2)) =
        4 * Real.exp (-R ^ 2 / (4 * a)) *
          S.sum (fun q =>
            (Z.mult q : ℝ) * gaussWeight (2 * a) omega q.2) := by
    calc
      S.sum (fun q =>
          (Z.mult q : ℝ) *
            (4 * Real.exp (-R ^ 2 / (4 * a)) *
              gaussWeight (2 * a) omega q.2)) =
          S.sum (fun q =>
            (4 * Real.exp (-R ^ 2 / (4 * a))) *
              ((Z.mult q : ℝ) * gaussWeight (2 * a) omega q.2)) :=
        sum_congr rfl fun _ _ => by ring
      _ = (4 * Real.exp (-R ^ 2 / (4 * a))) *
          S.sum (fun q =>
            (Z.mult q : ℝ) * gaussWeight (2 * a) omega q.2) :=
        (mul_sum _ _ _).symm
  have hθ := gaborOuter_gaussMass_le_theta (R := R) ha hω Z hinc
  have hR2 : -R ^ 2 / (4 * a) ≤ -(1 : ℝ) / (4 * a) := by
    have hsq : (1 : ℝ) ≤ R ^ 2 := by nlinarith [hR]
    exact div_le_div_of_nonneg_right (neg_le_neg hsq)
      (mul_pos (by norm_num) ha).le
  have hexpR :
      Real.exp ((1 / 4 : ℝ) / (2 * a)) * Real.exp (-R ^ 2 / (4 * a)) ≤
        Real.exp (-(1 : ℝ) / (8 * a)) := by
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have h1 : (1 / 4 : ℝ) / (2 * a) = (1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    have : (1 : ℝ) / (8 * a) + (-R ^ 2 / (4 * a)) ≤
        (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) := by
      linarith [hR2]
    have h2 : (1 : ℝ) / (8 * a) + (-(1 : ℝ) / (4 * a)) =
        -(1 : ℝ) / (8 * a) := by
      field_simp [ha.ne']
      ring
    rw [h1]
    exact this.trans_eq h2
  unfold gaborOuterAbsSum
  refine hsum.trans ?_
  rw [hfactor]
  have hthreeBound :
      S.sum (fun q => (Z.mult q : ℝ) * gaborThreeLobe a omega q.2) ≤
        4 * Real.exp (-R ^ 2 / (4 * a)) *
          gaborLogWeightedTheta (2 * a) omega := by
    refine hsum₃.trans ?_
    rw [hfactor₃]
    exact mul_le_mul_of_nonneg_left hθ he
  refine (mul_le_mul_of_nonneg_left hthreeBound hC).trans ?_
  have hrew :
      (Real.pi / a) * Real.exp ((1 / 4 : ℝ) / (2 * a)) *
          (4 * Real.exp (-R ^ 2 / (4 * a)) *
            gaborLogWeightedTheta (2 * a) omega) =
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega) *
          (Real.exp ((1 / 4 : ℝ) / (2 * a)) *
            Real.exp (-R ^ 2 / (4 * a))) := by
    ring
  rw [hrew]
  have hθ0 : 0 ≤ gaborLogWeightedTheta (2 * a) omega :=
    gaborLogWeightedTheta_nonneg (mul_pos (by norm_num) ha)
  have hpre : 0 ≤ 4 * (Real.pi / a) * gaborLogWeightedTheta (2 * a) omega :=
    mul_nonneg (mul_nonneg (by norm_num) (div_nonneg Real.pi_pos.le ha.le))
      hθ0
  unfold gaborOuterTailTsumPrefactor
  exact mul_le_mul_of_nonneg_left hexpR hpre

/-- Three-term comparison on any increment-compliant catalog. -/
theorem gaborHonestWeil_le_window_plus_theta
    {a omega R Cinc : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (hR : (1 : ℝ) ≤ R) (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z) :
    gaborHonestWeil a omega Z Cinc ≤
      gaborHonestWeil a omega (gaborWindowSlice Z omega R) Cinc +
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) :=
  (gaborHonestWeil_le_window_plus_outerAbs a omega R Cinc Z).trans
    (add_le_add (le_refl _)
      (abs_gaborQuadrupole_outer_config_le_theta ha hR hω Z hinc))

/-- Outer fund-domain zeros of a weighted truncation, as the
subtype Finset consumed by
`abs_gaborQuadrupole_outer_mult_finset_le_theta`. -/
noncomputable def gaborFundZerosOuterSubtype (T omega R : ℝ) :
    Finset {z : ℂ // IsCriticalStripZetaZero z} :=
  ((gaborFundZerosUpTo T).filter
      (fun z => R ≤ |z.im - omega|)).subtype IsCriticalStripZetaZero

lemma mem_gaborFundZerosOuterSubtype {T omega R : ℝ}
    {ρ : {z : ℂ // IsCriticalStripZetaZero z}} :
    ρ ∈ gaborFundZerosOuterSubtype T omega R ↔
      ρ.val ∈ gaborFundZerosUpTo T ∧ R ≤ |ρ.val.im - omega| := by
  constructor
  · intro hρ
    have hmem : ρ.val ∈ (gaborFundZerosUpTo T).filter
        (fun z => R ≤ |z.im - omega|) :=
      (Finset.mem_subtype (p := IsCriticalStripZetaZero)).mp hρ
    exact mem_filter.mp hmem
  · intro h
    exact (Finset.mem_subtype (p := IsCriticalStripZetaZero)).mpr
      (mem_filter.mpr h)

/-- Direct application of the r594 zero-Finset tail to a weighted
FD truncation.  Companion of `abs_gaborQuadrupole_outer_config_le_theta`. -/
theorem abs_gaborQuadrupole_outer_fundZeros_le_theta
    {a omega R T : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R) (hω : 0 < omega) :
    (gaborFundZerosOuterSubtype T omega R).sum
        (fun ρ =>
          (riemannZetaMultiplicity (ρ : ℂ) : ℝ) *
            |gaborQuadrupole a omega
              ((ρ : ℂ).re - 1 / 2) (ρ : ℂ).im|) ≤
      gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a)) := by
  refine abs_gaborQuadrupole_outer_mult_finset_le_theta
      (a := a) (omega := omega) (R := R) ha hR hω
      (gaborFundZerosOuterSubtype T omega R) ?_
  intro ρ hρ
  have hmem := (mem_gaborFundZerosOuterSubtype (T := T)
      (omega := omega) (R := R)).mp hρ
  have hD := (mem_gaborFundZerosUpTo.mp hmem.1).2
  have hcrit := isCriticalStrip_of_mem_fundZeros hmem.1
  have hγ := (gaborFundDomain_of_mem_fundZeros hmem.1).2
  refine ⟨sub_pos.mpr hD, ?_, hγ, hmem.2⟩
  change (ρ : ℂ).re - 1 / 2 < 1 / 2
  linarith [hcrit.2.2]

/-! ## (2) Glue negativity on finite extensions -/

/-- `Z` extends a nonempty window catalog by points that are
outer at the window's isolation packet (`R ≥ 1`).  Multiplicities
agree on the window.  This is the r592/r595 split: host and
`(a,ω)` are computed on the window, not on the global `σ`-max. -/
def GaborOuterExtension (W Z : GaborCanonicalConfig) (R : ℝ)
    (hW : W.pts.Nonempty) : Prop :=
  W.pts ⊆ Z.pts ∧
    (∀ q ∈ W.pts, W.mult q = Z.mult q) ∧
      ∀ q ∈ Z.pts, q ∉ W.pts →
        R ≤ |q.2 - (isolationShrinkOfConfig W hW).2|

lemma gaborHonestWeil_of_subconfig
    (a omega Cinc : ℝ) (W Z : GaborCanonicalConfig)
    (hsub : W.pts ⊆ Z.pts)
    (hmult : ∀ q ∈ W.pts, W.mult q = Z.mult q) :
    gaborHonestWeil a omega Z Cinc =
      gaborHonestWeil a omega W Cinc +
        (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
  rw [gaborHonestWeil_linear, gaborHonestWeil_linear]
  have hdisj : Disjoint W.pts (Z.pts.filter (fun q => q ∉ W.pts)) := by
    rw [Finset.disjoint_left]
    intro q hqW hqO
    exact (mem_filter.mp hqO).2 hqW
  have hunion : W.pts ∪ Z.pts.filter (fun q => q ∉ W.pts) = Z.pts := by
    ext q
    simp only [Finset.mem_union, mem_filter]
    constructor
    · intro h
      rcases h with h | h
      · exact hsub h
      · exact h.1
    · intro hq
      by_cases hW : q ∈ W.pts
      · exact Or.inl hW
      · exact Or.inr ⟨hq, hW⟩
  have hQW :
      W.pts.sum (fun q =>
          (W.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) =
        W.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) :=
    sum_congr rfl fun q hq => by rw [hmult q hq]
  have hQ :
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) =
        W.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
          (Z.pts.filter (fun q => q ∉ W.pts)).sum
            (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
    rw [← sum_union hdisj, hunion]
  linarith [hQ, hQW]

lemma gaborOuterExtension_absSum_le
    {a omega R : ℝ} (W Z : GaborCanonicalConfig)
    (hW : W.pts.Nonempty) (hext : GaborOuterExtension W Z R hW)
    (hωeq : omega = (isolationShrinkOfConfig W hW).2) :
    (Z.pts.filter (fun q => q ∉ W.pts)).sum
        (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) ≤
      gaborOuterAbsSum a omega Z R := by
  have hsub :
      Z.pts.filter (fun q => q ∉ W.pts) ⊆
        Z.pts.filter (fun q => R ≤ |q.2 - omega|) := by
    intro q hq
    have hqf := mem_filter.mp hq
    refine mem_filter.mpr ⟨hqf.1, ?_⟩
    simpa [hωeq] using hext.2.2 q hqf.1 hqf.2
  unfold gaborOuterAbsSum
  exact sum_le_sum_of_subset_of_nonneg hsub fun q _ _ =>
    mul_nonneg (Nat.cast_nonneg _) (abs_nonneg _)

/-- Lock-margin gap `exp(−π²/1024) − 9/10 > 0`.  Copied from the
numerical comparison inside `gaborEta_gt_nine_tenths`. -/
lemma gaborLockMarginGap_pos :
    0 < Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ) := by
  have hπ : Real.pi ^ 2 < 10 := by
    have h : Real.pi < 315 / 100 :=
      Real.pi_lt_d2.trans_le (by norm_num)
    have hsq : Real.pi ^ 2 < (315 / 100) ^ 2 :=
      sq_lt_sq' (by nlinarith [Real.pi_pos.le, h]) h
    exact hsq.trans (by norm_num)
  have hx : Real.pi ^ 2 / 1024 < (1 / 10 : ℝ) := by
    have : Real.pi ^ 2 < 1024 / 10 := by
      have : (10 : ℝ) < 1024 / 10 := by norm_num
      linarith [hπ]
    exact (div_lt_div_iff₀ (by norm_num : (0 : ℝ) < 1024)
      (by norm_num : (0 : ℝ) < 10)).mpr (by linarith)
  have hle : 1 - Real.pi ^ 2 / 1024 ≤
      Real.exp (-(Real.pi ^ 2 / 1024)) := by
    have := Real.add_one_le_exp (-(Real.pi ^ 2 / 1024))
    linarith [this]
  have : (9 / 10 : ℝ) < 1 - Real.pi ^ 2 / 1024 := by linarith [hx]
  linarith [this.trans_le hle]

/-- Frozen-theta comparison: `C(a,ω) exp(−1/(8a)) < ε · E(σ,a)`
for all sufficiently small `a`.  Same modulus construction as
`GaborOuterTailSmallerThanLocalMargin_holds` (r594). -/
theorem exists_small_width_outerPrefactor_lt_enhancement
    {sigmaStar omega ε : ℝ} (_hσ0 : 0 < sigmaStar)
    (_hω : 0 < omega) (hε : 0 < ε) :
    ∃ a0 : ℝ, 0 < a0 ∧ a0 ≤ 1 ∧
      ∀ {a : ℝ}, 0 < a → a < a0 →
        gaborOuterTailTsumPrefactor a omega *
            Real.exp (-(1 : ℝ) / (8 * a)) <
          ε * gaborEnhancement sigmaStar a := by
  have hθ2 : 0 ≤ gaborLogWeightedTheta (2 : ℝ) omega :=
    gaborLogWeightedTheta_nonneg (by norm_num)
  have hC : 0 ≤ 4 * gaborLogWeightedTheta (2 : ℝ) omega :=
    mul_nonneg (by norm_num) hθ2
  obtain ⟨a0, ha0, ha0le, hsmall⟩ :=
    exists_small_width_mul_exp_neg hC hε
  refine ⟨a0, ha0, ha0le, ?_⟩
  intro a ha hlt
  have h2a : 0 < 2 * a := mul_pos (by norm_num) ha
  have h2a_le : 2 * a ≤ (2 : ℝ) := by
    have : a < 1 := lt_of_lt_of_le hlt ha0le
    nlinarith
  have hθle :
      gaborLogWeightedTheta (2 * a) omega ≤
        gaborLogWeightedTheta (2 : ℝ) omega :=
    gaborLogWeightedTheta_mono_a h2a h2a_le
  have hπa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hexp0 : 0 ≤ Real.exp (-(1 : ℝ) / (8 * a)) :=
    (Real.exp_pos _).le
  have hpre_le :
      gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) ≤
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
    unfold gaborOuterTailTsumPrefactor
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left hθle
        (mul_nonneg (by norm_num) hπa.le))
      hexp0
  have hcore :
      4 * gaborLogWeightedTheta (2 : ℝ) omega *
        Real.exp (-(1 : ℝ) / (8 * a)) < ε :=
    hsmall ha hlt
  have hexpE :
      (1 : ℝ) ≤ Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    Real.one_le_exp
      (div_nonneg (sq_nonneg _) (mul_nonneg (by norm_num) ha.le))
  have hrhs :
      ε ≤ ε * Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    le_mul_of_one_le_right hε.le hexpE
  have hmid :
      (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
          Real.exp (-(1 : ℝ) / (8 * a)) <
        ε * (Real.pi / a) *
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    have hmul :
        (Real.pi / a) *
            (4 * gaborLogWeightedTheta (2 : ℝ) omega *
              Real.exp (-(1 : ℝ) / (8 * a))) <
          (Real.pi / a) *
            (ε * Real.exp (sigmaStar ^ 2 / (2 * a))) :=
      mul_lt_mul_of_pos_left (hcore.trans_le hrhs) hπa
    have hl :
        (4 * (Real.pi / a) * gaborLogWeightedTheta (2 : ℝ) omega) *
            Real.exp (-(1 : ℝ) / (8 * a)) =
          (Real.pi / a) *
            (4 * gaborLogWeightedTheta (2 : ℝ) omega *
              Real.exp (-(1 : ℝ) / (8 * a))) := by
      ring
    have hr :
        ε * (Real.pi / a) * Real.exp (sigmaStar ^ 2 / (2 * a)) =
          (Real.pi / a) *
            (ε * Real.exp (sigmaStar ^ 2 / (2 * a))) := by
      ring
    exact hl.trans_lt (hmul.trans_eq hr.symm)
  have hE :
      ε * (Real.pi / a) * Real.exp (sigmaStar ^ 2 / (2 * a)) =
        ε * gaborEnhancement sigmaStar a := by
    unfold gaborEnhancement
    ring
  exact hpre_le.trans_lt (hmid.trans_eq hE)

/-- Window BoundLog2 plus the catalog tail: at the window's
isolation packet,
`W_honest(Z) < (9/10 − η) · E + C(a,ω) exp(−1/(8a))`.
`W` must be increment-compliant and `γ`-distinct; `Z` must be
increment-compliant and an `R ≥ 1` outer extension. -/
theorem gaborHonestWeil_glue_lt_etaMargin_plus_tail
    (W Z : GaborCanonicalConfig) (hW : W.pts.Nonempty)
    (hincW : GaborConfigIncrementCompliantLog W)
    (hdistW : W.gammaDistinct)
    (hincZ : GaborConfigIncrementCompliantLog Z)
    {R : ℝ} (hR : (1 : ℝ) ≤ R)
    (hext : GaborOuterExtension W Z R hW) :
    gaborHonestWeil
        (isolationShrinkOfConfig W hW).1
        (isolationShrinkOfConfig W hW).2
        Z gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma W hW)
          (isolationShrinkOfConfig W hW).1) *
        gaborEnhancement (gaborHostSigma W hW)
          (isolationShrinkOfConfig W hW).1 +
      gaborOuterTailTsumPrefactor
        (isolationShrinkOfConfig W hW).1
        (isolationShrinkOfConfig W hW).2 *
        Real.exp (-(1 : ℝ) / (8 * (isolationShrinkOfConfig W hW).1)) := by
  set a := (isolationShrinkOfConfig W hW).1
  set omega := (isolationShrinkOfConfig W hW).2
  have ha := isolationShrinkOfConfig_a_pos W hW
  have hω := isolationShrinkOfConfig_omega_pos W hW
  have hsplit :=
    gaborHonestWeil_of_subconfig a omega gaborCInc W Z hext.1 hext.2.1
  have htri :
      (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) ≤
        (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) :=
    sum_le_sum fun q _ =>
      mul_le_mul_of_nonneg_left (le_abs_self _) (Nat.cast_nonneg _)
  have houter :=
    gaborOuterExtension_absSum_le (a := a) (omega := omega) (R := R)
      W Z hW hext rfl
  have hθ :=
    abs_gaborQuadrupole_outer_config_le_theta (a := a) (omega := omega)
      (R := R) ha hR hω Z hincZ
  have hWlog := gaborHonestWeilLog_lt_etaMargin W hW hincW hdistW
  have hWle := gaborHonestWeil_le_honestWeilLog a omega W ha
  have hWlt : gaborHonestWeil a omega W gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma W hW) a) *
        gaborEnhancement (gaborHostSigma W hW) a :=
    hWle.trans_lt hWlog
  have hsum : gaborHonestWeil a omega Z gaborCInc ≤
      gaborHonestWeil a omega W gaborCInc +
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
    have := (htri.trans houter).trans hθ
    linarith [hsplit, this]
  exact hsum.trans_lt
    (add_lt_add_left hWlt
      (gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a))))

/-- Any nonempty increment-compliant `γ`-distinct catalog is
already a window: BoundLog2 plus `W ≤ W_log` give
`W_honest < 0` at its isolation packet. -/
theorem gaborCanonicalConfig_honestWeil_neg
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct) :
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0 := by
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  exact (gaborHonestWeil_le_honestWeilLog _ _ Z ha).trans_lt
    (gabor_dominanceBoundLog2_holds Z hZ hinc hdist)

/-- Quantitative glue: if the window isolation width is below the
r594 tail-vs-margin modulus, the whole finite extension is
negative.  The modulus depends on the window host `(σ★,ω)` and
on the lock gap; it is not uniform in the host (r594). -/
theorem gaborHonestWeil_glue_neg_of_small_isolation
    (W Z : GaborCanonicalConfig) (hW : W.pts.Nonempty)
    (hincW : GaborConfigIncrementCompliantLog W)
    (hdistW : W.gammaDistinct)
    (hincZ : GaborConfigIncrementCompliantLog Z)
    {R : ℝ} (hR : (1 : ℝ) ≤ R)
    (hext : GaborOuterExtension W Z R hW) :
    ∃ a0 : ℝ, 0 < a0 ∧
      ((isolationShrinkOfConfig W hW).1 < a0 →
        gaborHonestWeil
          (isolationShrinkOfConfig W hW).1
          (isolationShrinkOfConfig W hW).2
          Z gaborCInc < 0) := by
  set a := (isolationShrinkOfConfig W hW).1
  set omega := (isolationShrinkOfConfig W hW).2
  set σ := gaborHostSigma W hW
  have hs := gaborHostSigma_pos W hW
  have ha := isolationShrinkOfConfig_a_pos W hW
  have hω := isolationShrinkOfConfig_omega_pos W hW
  have hgap := gaborLockMarginGap_pos
  have hε : 0 < Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ) := hgap
  obtain ⟨a0, ha0, _, hsmall⟩ :=
    exists_small_width_outerPrefactor_lt_enhancement
      (sigmaStar := σ) (omega := omega)
      (ε := Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ))
      hs hω hε
  refine ⟨a0, ha0, ?_⟩
  intro hlt
  have hlock := gaborHonestWeilLog_lt_lockMargin W hW hincW hdistW
  have hWle := gaborHonestWeil_le_honestWeilLog a omega W ha
  have hWlt :
      gaborHonestWeil a omega W gaborCInc <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement σ a :=
    hWle.trans_lt hlock
  have hsplit :=
    gaborHonestWeil_of_subconfig a omega gaborCInc W Z hext.1 hext.2.1
  have htri :
      (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) ≤
        (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) :=
    sum_le_sum fun q _ =>
      mul_le_mul_of_nonneg_left (le_abs_self _) (Nat.cast_nonneg _)
  have houter :=
    gaborOuterExtension_absSum_le (a := a) (omega := omega) (R := R)
      W Z hW hext rfl
  have hθ :=
    abs_gaborQuadrupole_outer_config_le_theta (a := a) (omega := omega)
      (R := R) ha hR hω Z hincZ
  have htail := (htri.trans houter).trans hθ
  have hCexp :
      gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) <
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement σ a :=
    hsmall ha hlt
  have hrew :
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement σ a +
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement σ a = 0 := by
    ring
  have hsum' :
      gaborHonestWeil a omega W gaborCInc +
          (gaborOuterTailTsumPrefactor a omega *
            Real.exp (-(1 : ℝ) / (8 * a))) <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
            gaborEnhancement σ a +
          (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
            gaborEnhancement σ a :=
    add_lt_add hWlt hCexp
  have hz : gaborHonestWeil a omega Z gaborCInc ≤
      gaborHonestWeil a omega W gaborCInc +
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
    linarith [hsplit, htail]
  exact hz.trans_lt (hsum'.trans_eq hrew)

/-! ## (3) Per-`T` checkpoint and the uniform-`δ` gap -/

/-- Per-`T` window-adaptive negativity: the isolation packet of
`gaborWeightedTruncationConfig T` scores `W_honest ≤ −δ(T) < 0`.
`δ` depends on the window through its lex host and isolation
width.  Needs `gammaDistinct` (BoundLog2); two fund-domain zeros
may share an ordinate (named remainder
`GaborWeightedTruncationGammaDistinct`). -/
theorem gaborWeightedTruncation_windowAdaptive_existsDelta
    (T : ℝ) (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty)
    (hdist : (gaborWeightedTruncationConfig T).gammaDistinct) :
    ∃ δ : ℝ, 0 < δ ∧
      gaborHonestWeil
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
        (gaborWeightedTruncationConfig T) gaborCInc ≤ -δ := by
  set Z := gaborWeightedTruncationConfig T
  set W := gaborHonestWeil
      (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc
  have hneg : W < 0 :=
    gaborWeightedTruncation_honestWeil_neg T hZ hdist
  refine ⟨-W / 2, half_pos (neg_pos.mpr hneg), ?_⟩
  linarith [hneg]

/-- Lock-margin form of the per-`T` δ: 
`δ = ½ (exp(−π²/1024) − 9/10) E(σ★,a)`.
The factor is `T`-free; `E` is not. -/
theorem gaborWeightedTruncation_windowAdaptive_lockDelta
    (T : ℝ) (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty)
    (hdist : (gaborWeightedTruncationConfig T).gammaDistinct) :
    0 < (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) / 2 *
        gaborEnhancement
          (gaborHostSigma (gaborWeightedTruncationConfig T) hZ)
          (isolationShrinkOfConfig
            (gaborWeightedTruncationConfig T) hZ).1 ∧
      gaborHonestWeil
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
        (gaborWeightedTruncationConfig T) gaborCInc <
      -((Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) / 2 *
        gaborEnhancement
          (gaborHostSigma (gaborWeightedTruncationConfig T) hZ)
          (isolationShrinkOfConfig
            (gaborWeightedTruncationConfig T) hZ).1) := by
  set Z := gaborWeightedTruncationConfig T
  set a := (isolationShrinkOfConfig Z hZ).1
  set σ := gaborHostSigma Z hZ
  set δ := (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) / 2 *
    gaborEnhancement σ a
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hgap := gaborLockMarginGap_pos
  have hδ : 0 < δ :=
    mul_pos (div_pos hgap (by norm_num)) hE
  have hlock := gaborWeightedTruncation_lockMargin T hZ hdist
  have hWle :=
    gaborHonestWeil_le_honestWeilLog a
      (isolationShrinkOfConfig Z hZ).2 Z ha
  have hW :
      gaborHonestWeil a (isolationShrinkOfConfig Z hZ).2 Z gaborCInc <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement σ a :=
    hWle.trans_lt hlock
  have hfac :
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement σ a =
        -((Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement σ a) := by
    ring
  have hhalf :
      -((Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement σ a) < -δ := by
    have hpos :
        0 < (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement σ a :=
      mul_pos hgap hE
    have : δ * 2 = (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
        gaborEnhancement σ a := by
      unfold δ
      ring
    linarith [hpos]
  exact ⟨hδ, (hW.trans_eq hfac).trans hhalf⟩

/-- `T`-uniform strengthening of
`gaborWeightedTruncation_windowAdaptive_existsDelta`.

Quantifier: a single `δ > 0` and a cutoff `T₀` such that every
nonempty `γ`-distinct weighted FD window `T ≥ T₀` scores
`W_honest(isolationShrink(Z_T), Z_T) ≤ −δ`.

This is the content of `GaborWindowAdaptiveCofinalNeg` plus the
honest `gammaDistinct` hypothesis.  It does **not** follow from
the per-`T` theorem: BoundLog2 retunes the lex host as `T` grows
(a newly included larger-`σ` zero becomes the host; isolation
width collapses with `d_min`).  The lock fraction
`η − 9/10 ≥ exp(−π²/1024) − 9/10` is `T`-free, but `E(σ★(T), a(T))`
has no `T`-independent positive lower bound.  That is the r592
host-retuning obstruction, not a missing algebra step.

Unasserted.  Not a `sorry`.  NO RH CLAIM. -/
def GaborWindowAdaptiveUniformDelta : Prop :=
  ∃ δ : ℝ, 0 < δ ∧
    ∃ T0 : ℝ, ∀ T : ℝ, T0 ≤ T →
      ∀ hZ : (gaborWeightedTruncationConfig T).pts.Nonempty,
        (gaborWeightedTruncationConfig T).gammaDistinct →
          gaborHonestWeil
            (isolationShrinkOfConfig
              (gaborWeightedTruncationConfig T) hZ).1
            (isolationShrinkOfConfig
              (gaborWeightedTruncationConfig T) hZ).2
            (gaborWeightedTruncationConfig T) gaborCInc ≤ -δ

/-- Named implication: a uniform `δ` is exactly
`GaborWindowAdaptiveCofinalNeg` on the `gammaDistinct` windows.
The extra `gammaDistinct` hypothesis is the r589 remainder
`GaborWeightedTruncationGammaDistinct`.  Unasserted. -/
def gabor_window_adaptive_uniform_to_cofinal : Prop :=
  GaborWindowAdaptiveUniformDelta →
    (GaborWeightedTruncationGammaDistinct → GaborWindowAdaptiveCofinalNeg)

/-- Sorry-free logic: the named implication plus the two
unasserted inputs produce the r594 checkpoint.  Does not assert
the inputs. -/
theorem gabor_uniformDelta_to_cofinal_neg
    (hδ : GaborWindowAdaptiveUniformDelta)
    (himp : gabor_window_adaptive_uniform_to_cofinal)
    (hdist : GaborWeightedTruncationGammaDistinct) :
    GaborWindowAdaptiveCofinalNeg :=
  himp hδ hdist

#print axioms gaborHonestWeil_window_add_outer
#print axioms gaborHonestWeil_le_window_plus_outerAbs
#print axioms abs_gaborQuadrupole_outer_config_le_theta
#print axioms gaborHonestWeil_le_window_plus_theta
#print axioms abs_gaborQuadrupole_outer_fundZeros_le_theta
#print axioms gaborHonestWeil_glue_lt_etaMargin_plus_tail
#print axioms gaborCanonicalConfig_honestWeil_neg
#print axioms gaborHonestWeil_glue_neg_of_small_isolation
#print axioms gaborWeightedTruncation_windowAdaptive_existsDelta
#print axioms gaborWeightedTruncation_windowAdaptive_lockDelta
#print axioms gabor_uniformDelta_to_cofinal_neg

end RH
