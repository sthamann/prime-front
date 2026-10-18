/-
RH/GaborAnchoredWitness.lean -- r598 singleton fragment + htail.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

L2 adjudication (binding): ANKER_TEILWEISE.  A window frozen at
a target fund-domain zero removes host-retuning of growing
`T`-catalogs (r592) and the r592 float64 ω-collapse (r593).
Remaining gaps, not claimed here:

  (i) self-consistency is relative to the *final* packet centre
      ω, not to γ₀;
  (ii) equal-ordinate σ-clusters (`gammaDistinct`) stay open on
      genuine zeros — merge covers only identical points
      (`GaborWeightedTruncationGammaDistinct`).

r597 discharges `GaborBoundLog2AtAdmissibleWidth` at every
`0 < a ≤ isolationShrink` with `ω(a) = γ★ − πa/σ★`.

r598 inhabits the algebraic singleton fragment at a given
fund-domain target: host / increment / `gammaDistinct` /
isolation packet / inner-window radius.  The tail modulus
`C(a,ω(a)) exp(−1/(8a))` holds for all sufficiently small
admissible `a` (θ_log at width 2 is capped by the γ★-host
as `ω(a)` retunes).  The residual geometric cover
`GaborAnchoredCoverAt` — ordinate isolation of `ρ₀` in the
retuned ω-window — remains an explicit hypothesis.
`GaborAnchoredWitnessExists` is **not** asserted: genuine
ordinate clusters and the multi-point window stay open.

STOP (L2): this round does **not** assert
`GaborAnchoredWitnessExists`,
`GaborWindowAdaptiveUniformDelta`, or
`GaborArithmeticSeparatesOffCriticalZeros`.
r600: `GaborSpectralToArithmetic` is a theorem
(pole-sign lemma from EF + `Re ĥ(1) ≥ 0`), NOT RH-core.

No asserting `sorry`.  Census unchanged.
-/
import RH.GaborWindowGlue

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical
open Set Finset Filter
open scoped Topology

/-! ## Log split (same Q-sum as r595; on-line budget is `R_on_log`) -/

theorem gaborHonestWeilLog_eq_quadrupoleSum
    (a omega : ℝ) (Z : GaborCanonicalConfig) (Cinc : ℝ) :
    gaborHonestWeilLog a omega Z Cinc =
      gaborQuadrupoleSum a omega Z +
        gaborHonestOnlineBudgetLog a omega Cinc :=
  rfl

/-- Linear split at a common packet: `R_on_log` is shared, so
`W_log(Z) = W_log(W) + Σ_{Z\W} Q`.  Log analog of
`gaborHonestWeil_of_subconfig` (r595). -/
theorem gaborHonestWeilLog_of_subconfig
    (a omega Cinc : ℝ) (W Z : GaborCanonicalConfig)
    (hsub : W.pts ⊆ Z.pts)
    (hmult : ∀ q ∈ W.pts, W.mult q = Z.mult q) :
    gaborHonestWeilLog a omega Z Cinc =
      gaborHonestWeilLog a omega W Cinc +
        (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
  have h := gaborHonestWeil_of_subconfig a omega Cinc W Z hsub hmult
  simp only [gaborHonestWeilLog, gaborHonestWeil] at h ⊢
  linarith [h]

theorem gaborHonestWeilLog_window_add_outer
    (a omega R Cinc : ℝ) (Z : GaborCanonicalConfig) :
    gaborHonestWeilLog a omega Z Cinc =
      gaborHonestWeilLog a omega (gaborWindowSlice Z omega R) Cinc +
        (gaborOuterSlice Z omega R).pts.sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) := by
  have h := gaborHonestWeil_window_add_outer a omega R Cinc Z
  simp only [gaborHonestWeilLog, gaborHonestWeil] at h ⊢
  linarith [h]

theorem gaborHonestWeilLog_le_window_plus_outerAbs
    (a omega R Cinc : ℝ) (Z : GaborCanonicalConfig) :
    gaborHonestWeilLog a omega Z Cinc ≤
      gaborHonestWeilLog a omega (gaborWindowSlice Z omega R) Cinc +
        gaborOuterAbsSum a omega Z R := by
  have h := gaborHonestWeil_le_window_plus_outerAbs a omega R Cinc Z
  simp only [gaborHonestWeilLog, gaborHonestWeil] at h ⊢
  linarith [h]

/-- Log three-term comparison.  Outer term identical to r595;
only the on-line budget is `R_on_log`. -/
theorem gaborHonestWeilLog_le_window_plus_theta
    {a omega R Cinc : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (hR : (1 : ℝ) ≤ R) (Z : GaborCanonicalConfig)
    (hinc : GaborConfigIncrementCompliantLog Z) :
    gaborHonestWeilLog a omega Z Cinc ≤
      gaborHonestWeilLog a omega (gaborWindowSlice Z omega R) Cinc +
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
  have h :=
    gaborHonestWeil_le_window_plus_theta (Cinc := Cinc) ha hω hR Z hinc
  simp only [gaborHonestWeilLog, gaborHonestWeil] at h ⊢
  linarith [h]

/-- Outer extension relative to an arbitrary packet centre `ω`
(not necessarily `isolationShrink.2`).  L2 (i): geometry is
judged at the final ω. -/
def GaborOuterExtensionAt (W Z : GaborCanonicalConfig)
    (omega R : ℝ) : Prop :=
  W.pts ⊆ Z.pts ∧
    (∀ q ∈ W.pts, W.mult q = Z.mult q) ∧
      ∀ q ∈ Z.pts, q ∉ W.pts → R ≤ |q.2 - omega|

lemma gaborOuterExtensionAt_absSum_le
    {a omega R : ℝ} (W Z : GaborCanonicalConfig)
    (hext : GaborOuterExtensionAt W Z omega R) :
    (Z.pts.filter (fun q => q ∉ W.pts)).sum
        (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) ≤
      gaborOuterAbsSum a omega Z R := by
  have hsub :
      Z.pts.filter (fun q => q ∉ W.pts) ⊆
        Z.pts.filter (fun q => R ≤ |q.2 - omega|) := by
    intro q hq
    have hqf := mem_filter.mp hq
    exact mem_filter.mpr ⟨hqf.1, hext.2.2 q hqf.1 hqf.2⟩
  unfold gaborOuterAbsSum
  exact sum_le_sum_of_subset_of_nonneg hsub fun _ _ _ =>
    mul_nonneg (Nat.cast_nonneg _) (abs_nonneg _)

theorem gaborHonestWeilLog_le_subconfig_plus_theta
    {a omega R : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (hR : (1 : ℝ) ≤ R) (W Z : GaborCanonicalConfig)
    (hincZ : GaborConfigIncrementCompliantLog Z)
    (hext : GaborOuterExtensionAt W Z omega R) :
    gaborHonestWeilLog a omega Z gaborCInc ≤
      gaborHonestWeilLog a omega W gaborCInc +
        gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
  have hsplit :=
    gaborHonestWeilLog_of_subconfig a omega gaborCInc W Z hext.1 hext.2.1
  have htri :
      (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) ≤
        (Z.pts.filter (fun q => q ∉ W.pts)).sum
          (fun q => (Z.mult q : ℝ) * |gaborQuadrupole a omega q.1 q.2|) :=
    sum_le_sum fun _ _ =>
      mul_le_mul_of_nonneg_left (le_abs_self _) (Nat.cast_nonneg _)
  have houter :=
    gaborOuterExtensionAt_absSum_le (a := a) (omega := omega) (R := R)
      W Z hext
  have hθ :=
    abs_gaborQuadrupole_outer_config_le_theta (a := a) (omega := omega)
      (R := R) ha hR hω Z hincZ
  have htail := (htri.trans houter).trans hθ
  linarith [hsplit, htail]

/-- Lock-margin + tail modulus ⇒ log-score of the finite
extension is negative.  The lock comparison is a *hypothesis*
so the packet `(a,ω)` need not be `isolationShrinkOfConfig`. -/
theorem gaborHonestWeilLog_neg_of_lock_and_tail
    {a omega R sigma : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (hR : (1 : ℝ) ≤ R) (W Z : GaborCanonicalConfig)
    (hincZ : GaborConfigIncrementCompliantLog Z)
    (hext : GaborOuterExtensionAt W Z omega R)
    (hWlock :
      gaborHonestWeilLog a omega W gaborCInc <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement sigma a)
    (htail :
      gaborOuterTailTsumPrefactor a omega *
          Real.exp (-(1 : ℝ) / (8 * a)) <
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement sigma a) :
    gaborHonestWeilLog a omega Z gaborCInc < 0 := by
  have hsum :=
    gaborHonestWeilLog_le_subconfig_plus_theta ha hω hR W Z hincZ hext
  have hrew :
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement sigma a +
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement sigma a = 0 := by
    ring
  have hcombo :
      gaborHonestWeilLog a omega W gaborCInc +
          (gaborOuterTailTsumPrefactor a omega *
            Real.exp (-(1 : ℝ) / (8 * a))) <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
            gaborEnhancement sigma a +
          (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
            gaborEnhancement sigma a :=
    add_lt_add hWlock htail
  exact hsum.trans_lt (hcombo.trans_eq hrew)

/-- Window BoundLog2 at the constructive shrink, then the r595
lock+tail arithmetic in log units. -/
theorem gaborHonestWeilLog_glue_neg_of_small_isolation
    (W Z : GaborCanonicalConfig) (hW : W.pts.Nonempty)
    (hincW : GaborConfigIncrementCompliantLog W)
    (hdistW : W.gammaDistinct)
    (hincZ : GaborConfigIncrementCompliantLog Z)
    {R : ℝ} (hR : (1 : ℝ) ≤ R)
    (hext : GaborOuterExtension W Z R hW)
    {a0 : ℝ} (_ha0 : 0 < a0)
    (hsmall : (isolationShrinkOfConfig W hW).1 < a0 →
      gaborOuterTailTsumPrefactor
          (isolationShrinkOfConfig W hW).1
          (isolationShrinkOfConfig W hW).2 *
        Real.exp (-(1 : ℝ) /
          (8 * (isolationShrinkOfConfig W hW).1)) <
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement (gaborHostSigma W hW)
            (isolationShrinkOfConfig W hW).1)
    (hlt : (isolationShrinkOfConfig W hW).1 < a0) :
    gaborHonestWeilLog
        (isolationShrinkOfConfig W hW).1
        (isolationShrinkOfConfig W hW).2
        Z gaborCInc < 0 := by
  set a := (isolationShrinkOfConfig W hW).1
  set omega := (isolationShrinkOfConfig W hW).2
  have ha := isolationShrinkOfConfig_a_pos W hW
  have hω := isolationShrinkOfConfig_omega_pos W hW
  have hext' : GaborOuterExtensionAt W Z omega R :=
    ⟨hext.1, hext.2.1, fun q hqZ hqW => by
      simpa [omega] using hext.2.2 q hqZ hqW⟩
  exact gaborHonestWeilLog_neg_of_lock_and_tail (sigma := gaborHostSigma W hW)
    ha hω hR W Z hincZ hext'
    (gaborHonestWeilLog_lt_lockMargin W hW hincW hdistW) (hsmall hlt)

theorem gaborCanonicalConfig_honestWeilLog_neg
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct) :
    gaborHonestWeilLog (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0 :=
  gabor_dominanceBoundLog2_holds Z hZ hinc hdist

/-! ## Log exhaustion algebra (fixed log budget, not constant `R_on`) -/

theorem gabor_exhaustion_algebra_log
    {a omega Cinc : ℝ} {s : ℕ → ℝ} {L B : ℝ}
    (hW : ∀ᶠ n in atTop,
      s n + gaborHonestOnlineBudgetLog a omega Cinc ≤ B)
    (hlim : Tendsto s atTop (𝓝 L)) :
    L + gaborHonestOnlineBudgetLog a omega Cinc ≤ B := by
  have htend :
      Tendsto (fun n => s n + gaborHonestOnlineBudgetLog a omega Cinc)
        atTop (𝓝 (L + gaborHonestOnlineBudgetLog a omega Cinc)) :=
    hlim.add tendsto_const_nhds
  exact le_of_tendsto htend hW

/-! ## Anchored witness (conditional Prop; all hypotheses explicit)

BoundLog2 needs `gammaDistinct`, not merely `gammaHostIsolated`
(`GaborDominanceBoundLog2`, `gaborHonestWeilLog_lt_lockMargin`).
`gammaHostIsolated` is implied by `gammaDistinct`
(`gammaDistinct_hostIsolated`) and is not sufficient for the
pack. -/

/-- Anchored window at a target fund-domain zero (Type bundle so
`W`, `a`, `ω`, `R` project).  Inhabitation is the conditional
Prop.  Does **not** assert existence (L2 STOP).  NO RH CLAIM. -/
structure GaborAnchoredWindowWitnessAt (ρ₀ : ℂ) where
  W : GaborCanonicalConfig
  hW : W.pts.Nonempty
  hρ₀crit : IsCriticalStripZetaZero ρ₀
  hρ₀fund : (1 / 2 : ℝ) < ρ₀.re ∧ 0 < ρ₀.im
  hρ₀mem : gaborFundKey ρ₀ ∈ W.pts
  /-- Lex host of the frozen window is the target key.  This is
  the r592 host-retune lock: `W` does not grow with `T`. -/
  hhost : (gaborHostSigma W hW, gaborHostGamma W hW) = gaborFundKey ρ₀
  hinc : GaborConfigIncrementCompliantLog W
  /-- Minimal BoundLog2 distinctness (pairwise ordinates).
  Open on genuine zeros; see
  `GaborWeightedTruncationGammaDistinct`. -/
  hdist : W.gammaDistinct
  a : ℝ
  ha : 0 < a
  /-- Below the constructive isolation width of `W`. -/
  hiso : a ≤ (isolationShrinkOfConfig W hW).1
  /-- Lock `a ≤ σ★²/512` (`gaborALock_eq`). -/
  hlock : a ≤ gaborALock (gaborHostSigma W hW)
  omega : ℝ
  hω : omega =
    gaborIsolationOmega (gaborHostSigma W hW) (gaborHostGamma W hW) a
  hωpos : 0 < omega
  R : ℝ
  hR : (1 : ℝ) ≤ R
  /-- `W` contains only inner points at the *final* ω. -/
  hinner : ∀ q ∈ W.pts, |q.2 - omega| < R
  /-- Tail modulus at this `(a,ω)` vs the lock gap.  Instantiates
  `∃ a₀(ω,ε)` from `exists_small_width_outerPrefactor_lt_enhancement`. -/
  htail :
    gaborOuterTailTsumPrefactor a omega *
        Real.exp (-(1 : ℝ) / (8 * a)) <
      (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
        gaborEnhancement (gaborHostSigma W hW) a
  /-- Genuine FD keys, matching analytic multiplicity. -/
  hgenuine : ∀ q ∈ W.pts,
    ∃ ρ : ℂ, IsCriticalStripZetaZero ρ ∧
      (1 / 2 : ℝ) < ρ.re ∧ 0 < ρ.im ∧
        gaborFundKey ρ = q ∧
          W.mult q = riemannZetaMultiplicity ρ
  /-- Self-consistency (L2 geometric core): every genuine
  fund-domain zero with `|Im ρ − ω| < R` lies in `W`, with
  matching multiplicity.  Relative to ω, not to γ₀. -/
  hcover :
    ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
      gaborFundDomain ρ → |(ρ : ℂ).im - omega| < R →
        gaborFundKey (ρ : ℂ) ∈ W.pts ∧
          W.mult (gaborFundKey (ρ : ℂ)) =
            riemannZetaMultiplicity (ρ : ℂ)

theorem gaborALock_eq_div512 (sigma : ℝ) :
    gaborALock sigma = sigma ^ 2 / 512 := by
  rw [gaborALock_eq]
  ring

theorem gaborAnchored_omega_eq_isolationShrink
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀)
    (heq : wit.a = (isolationShrinkOfConfig wit.W wit.hW).1) :
    wit.omega = (isolationShrinkOfConfig wit.W wit.hW).2 := by
  rw [wit.hω, heq, isolationShrinkOfConfig_omega_eq]

theorem gaborAnchored_windowLog_lt_lockMargin_of_isolation
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀)
    (heq : wit.a = (isolationShrinkOfConfig wit.W wit.hW).1) :
    gaborHonestWeilLog wit.a wit.omega wit.W gaborCInc <
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a := by
  have h :=
    gaborHonestWeilLog_lt_lockMargin wit.W wit.hW wit.hinc wit.hdist
  simpa [heq, gaborAnchored_omega_eq_isolationShrink wit heq] using h

theorem gaborAnchored_windowLog_plus_tail_neg_of_isolation
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀)
    (heq : wit.a = (isolationShrinkOfConfig wit.W wit.hW).1) :
    gaborHonestWeilLog wit.a wit.omega wit.W gaborCInc +
        gaborOuterTailTsumPrefactor wit.a wit.omega *
          Real.exp (-(1 : ℝ) / (8 * wit.a)) < 0 := by
  have hW :=
    gaborAnchored_windowLog_lt_lockMargin_of_isolation wit heq
  have hrew :
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a +
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a = 0 := by
    ring
  have hcombo := add_lt_add hW wit.htail
  exact hcombo.trans_eq hrew

/-! ## Coverage ⇒ weighted FD truncations are outer extensions -/

theorem gaborAnchored_window_subset_trunc
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) {T : ℝ}
    (hT : ∀ q ∈ wit.W.pts, q.2 ≤ T) :
    wit.W.pts ⊆ (gaborWeightedTruncationConfig T).pts := by
  intro q hq
  obtain ⟨ρ, hcrit, hre, him, hkey, _⟩ := wit.hgenuine q hq
  have himq : ρ.im = q.2 := by
    have := congrArg Prod.snd hkey
    simpa [gaborFundKey] using this
  have hγle : |ρ.im| ≤ T := by
    rw [himq, abs_of_pos (himq ▸ him)]
    exact hT q hq
  have hrect := mem_rect_of_criticalStrip hcrit hγle
  have hoff : ρ ∈ gaborOffLineZerosUpTo T :=
    mem_gaborOffLineZerosUpTo.mpr ⟨hrect, ne_of_gt hre, him⟩
  have hfund : ρ ∈ gaborFundZerosUpTo T :=
    mem_gaborFundZerosUpTo.mpr ⟨hoff, hre⟩
  exact mem_image.mpr ⟨ρ, hfund, hkey⟩

theorem gaborAnchored_mult_eq_trunc
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) {T : ℝ}
    {q : ℝ × ℝ} (hq : q ∈ wit.W.pts) :
    wit.W.mult q = (gaborWeightedTruncationConfig T).mult q := by
  obtain ⟨ρ, _, _, _, hkey, hmult⟩ := wit.hgenuine q hq
  have hR : gaborWeightedRightRep q = ρ := by
    simpa [hkey] using gaborFundKey_rightRep ρ
  unfold gaborWeightedTruncationConfig
  change wit.W.mult q = gaborWeightedTruncationMult q
  unfold gaborWeightedTruncationMult
  rw [hR, hmult]

theorem gaborAnchored_trunc_is_outerExtension
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) {T : ℝ}
    (hT : ∀ q ∈ wit.W.pts, q.2 ≤ T) :
    GaborOuterExtensionAt wit.W
      (gaborWeightedTruncationConfig T) wit.omega wit.R := by
  refine ⟨gaborAnchored_window_subset_trunc wit hT, ?_, ?_⟩
  · intro q hq
    exact gaborAnchored_mult_eq_trunc wit hq
  · intro q hqZ hqW
    have hqimg : q ∈ gaborWeightedTruncationPts T := hqZ
    obtain ⟨z, hz, rfl⟩ := mem_image.mp hqimg
    have hcrit := isCriticalStrip_of_mem_fundZeros hz
    have hD := gaborFundDomain_of_mem_fundZeros hz
    have hfund : gaborFundDomain ⟨z, hcrit⟩ := hD
    by_contra hnot
    have hlt : |z.im - wit.omega| < wit.R := lt_of_not_ge hnot
    have hcov := wit.hcover ⟨z, hcrit⟩ hfund (by simpa [gaborFundKey] using hlt)
    exact hqW hcov.1

theorem gaborAnchored_truncation_Q_le
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) {T : ℝ}
    (hT : ∀ q ∈ wit.W.pts, q.2 ≤ T) :
    gaborQuadrupoleSum wit.a wit.omega
        (gaborWeightedTruncationConfig T) ≤
      gaborQuadrupoleSum wit.a wit.omega wit.W +
        gaborOuterTailTsumPrefactor wit.a wit.omega *
          Real.exp (-(1 : ℝ) / (8 * wit.a)) := by
  have hext := gaborAnchored_trunc_is_outerExtension wit hT
  have hincZ := gaborWeightedTruncation_incrementCompliantLog T
  have hWlog :=
    gaborHonestWeilLog_le_subconfig_plus_theta wit.ha wit.hωpos wit.hR
      wit.W (gaborWeightedTruncationConfig T) hincZ hext
  have hgap (X : GaborCanonicalConfig) :
      gaborHonestWeilLog wit.a wit.omega X gaborCInc =
        gaborQuadrupoleSum wit.a wit.omega X +
          gaborHonestOnlineBudgetLog wit.a wit.omega gaborCInc :=
    rfl
  rw [hgap (gaborWeightedTruncationConfig T), hgap wit.W] at hWlog
  linarith [hWlog]

/-- Off-line mass ≤ window Q-sum + outer tail, via r588 FD-HasSum
exhaustion at the *fixed* log packet `(a,ω)`. -/
theorem gaborAnchored_offLine_le_windowQ_plus_tail
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) :
    gaborOffLineSpectralMass (pureGaborTest wit.a wit.omega wit.ha) ≤
      gaborQuadrupoleSum wit.a wit.omega wit.W +
        gaborOuterTailTsumPrefactor wit.a wit.omega *
          Real.exp (-(1 : ℝ) / (8 * wit.a)) := by
  set a := wit.a
  set omega := wit.omega
  set F := pureGaborTest a omega wit.ha
  have hFDlim := gaborWeightedQuadrupoleLimitEqFDTsum_holds a omega wit.ha
  have hmass :=
    gaborOffLineMassEqWeightedQuadrupoleTsum_holds a omega wit.ha
  have h0 := gaborOffLineRealAxisMass_eq_zero F
  have hrew :
      gaborOffLineSpectralMass F =
        (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            if gaborFundDomain ρ then
              (4 : ℂ) * (riemannZetaMultiplicity (ρ : ℂ) : ℂ) *
                gaborHat F ρ
            else 0).re := by
    rw [hmass, h0, add_zero]
  have hL : Tendsto (fun n : ℕ =>
        gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)))
      atTop (𝓝 (gaborOffLineSpectralMass F)) := by
    simpa [hrew] using hFDlim
  set T0 := wit.W.pts.sup' wit.hW (fun q => q.2)
  have hT0 : ∀ q ∈ wit.W.pts, q.2 ≤ T0 :=
    fun q hq => Finset.le_sup' (fun q => q.2) hq
  obtain ⟨n0, hn0⟩ := exists_nat_gt T0
  have hev : ∀ᶠ n : ℕ in atTop,
      gaborQuadrupoleSum a omega
          (gaborWeightedTruncationConfig ((n + 1 : ℕ) : ℝ)) ≤
        gaborQuadrupoleSum a omega wit.W +
          gaborOuterTailTsumPrefactor a omega *
            Real.exp (-(1 : ℝ) / (8 * a)) := by
    refine Filter.eventually_atTop.mpr ⟨n0, fun n hn => ?_⟩
    have hTn : ∀ q ∈ wit.W.pts, q.2 ≤ ((n + 1 : ℕ) : ℝ) := by
      intro q hq
      have : (n0 : ℝ) ≤ n := Nat.cast_le.mpr hn
      have hT0q := hT0 q hq
      have : T0 < (n : ℝ) := lt_of_lt_of_le hn0 this
      have : T0 < ((n + 1 : ℕ) : ℝ) := by
        have : (n : ℝ) < ((n + 1 : ℕ) : ℝ) := by
          exact_mod_cast Nat.lt_succ_self n
        linarith
      exact hT0q.trans this.le
    simpa [a, omega] using gaborAnchored_truncation_Q_le wit hTn
  exact le_of_tendsto hL hev

/-- Conditional: an anchored witness implies the fixed packet's
full spectral zero-side is at most the log window score plus the
outer tail.  On-line mass via the log majorant
(`gaborCriticalLineMassLeLogMajorant_holds` +
`gaborLogMajorantLeHonestBudgetLog_holds`); off-line via the
window Q-sum + r594 outer tsum, identified by r588 HasSum. -/
theorem gaborAnchored_zeroSide_le_windowLog_plus_tail
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) :
    gaborZeroSide (pureGaborTest wit.a wit.omega wit.ha) ≤
      gaborHonestWeilLog wit.a wit.omega wit.W gaborCInc +
        gaborOuterTailTsumPrefactor wit.a wit.omega *
          Real.exp (-(1 : ℝ) / (8 * wit.a)) := by
  set F := pureGaborTest wit.a wit.omega wit.ha
  have hsplit := gaborZeroSide_eq_off_plus_on_pure (F := F) rfl
  have hon :=
    gabor_criticalLineMass_le_honest_of
      gaborCriticalLineMassLeLogMajorant_holds
      gaborLogMajorantLeHonestBudgetLog_holds
      (F := F) rfl wit.hωpos
  have hoff := gaborAnchored_offLine_le_windowQ_plus_tail wit
  have hWlog :
      gaborHonestWeilLog wit.a wit.omega wit.W gaborCInc =
        gaborQuadrupoleSum wit.a wit.omega wit.W +
          gaborHonestOnlineBudgetLog wit.a wit.omega gaborCInc :=
    rfl
  have : gaborOffLineSpectralMass F + gaborCriticalLineMass F ≤
      gaborQuadrupoleSum wit.a wit.omega wit.W +
        gaborOuterTailTsumPrefactor wit.a wit.omega *
          Real.exp (-(1 : ℝ) / (8 * wit.a)) +
        gaborHonestOnlineBudgetLog wit.a wit.omega gaborCInc :=
    add_le_add hoff hon
  linarith [hsplit, this, hWlog]

/-- Isolation-packet special case: BoundLog2 lock + tail modulus
give a strictly negative full spectral zero-side.  Does not
assert that a witness exists, and does not claim a `T`-uniform
`δ`. -/
theorem gaborAnchored_zeroSide_neg_of_isolationPacket
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀)
    (heq : wit.a = (isolationShrinkOfConfig wit.W wit.hW).1) :
    gaborZeroSide (pureGaborTest wit.a wit.omega wit.ha) < 0 :=
  (gaborAnchored_zeroSide_le_windowLog_plus_tail wit).trans_lt
    (gaborAnchored_windowLog_plus_tail_neg_of_isolation wit heq)

/-! ## r598 singleton fragment

Algebraic inhabitation of `GaborAnchoredWindowWitnessAt` at a
given fund-domain target, with analytic multiplicity.  The
window is the singleton `{gaborFundKey ρ₀}`.  Increment uses
the strip-window multiplicity sum (not the historical
`mult = 1` catalog).  Tail is discharged for small admissible
widths; cover stays a geometric hypothesis.
-/

noncomputable def gaborFundSingletonConfig
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    GaborCanonicalConfig where
  pts := {gaborFundKey ρ₀}
  mult := fun _ => riemannZetaMultiplicity ρ₀
  mult_pos := by
    intro _q _hq
    exact riemannZetaMultiplicity_pos hcrit.1
      (isCriticalStripZetaZero_ne_one hcrit)
  sigma_off := by
    intro q hq
    have : q = gaborFundKey ρ₀ := by simpa using hq
    cases this
    constructor
    · exact sub_pos.mpr hre
    · change ρ₀.re - (1 / 2 : ℝ) < 1 / 2
      linarith [hcrit.2.2]
  gamma_pos := by
    intro q hq
    have : q = gaborFundKey ρ₀ := by simpa using hq
    cases this
    simpa [gaborFundKey] using him

lemma gaborFundSingleton_nonempty
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    (gaborFundSingletonConfig ρ₀ hcrit hre him).pts.Nonempty := by
  simp [gaborFundSingletonConfig]

lemma gaborFundSingleton_incrementCompliantLog
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    GaborConfigIncrementCompliantLog
      (gaborFundSingletonConfig ρ₀ hcrit hre him) := by
  intro k
  set Z := gaborFundSingletonConfig ρ₀ hcrit hre him
  set key := gaborFundKey ρ₀
  set Sk := Z.pts.filter
    (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)
  by_cases hmem : key ∈ Sk
  · have hbin : (k : ℝ) < ρ₀.im ∧ ρ₀.im ≤ (k : ℝ) + 1 := by
      have hqf := mem_filter.mp hmem
      simpa [key, gaborFundKey] using hqf.2
    have hzW : ρ₀ ∈ stripZerosWindow (k : ℝ) :=
      mem_stripZerosWindow_of_critical hcrit ⟨hbin.1.le, hbin.2⟩
    have hsingle :
        (riemannZetaMultiplicity ρ₀ : ℝ) ≤
          (stripZerosWindow (k : ℝ)).sum
            (fun z => (riemannZetaMultiplicity z : ℝ)) :=
      Finset.single_le_sum (fun _ _ => Nat.cast_nonneg _) hzW
    have hK :
        (stripZerosWindow (k : ℝ)).sum
            (fun z => (riemannZetaMultiplicity z : ℝ)) ≤
          gaborKBinAt (|k| : ℝ) := by
      simpa [gaborKBinAt] using
        sum_multiplicity_stripZerosWindow_le (k : ℝ)
    have hfeq : Sk = {key} := by
      ext q
      constructor
      · intro hq
        have : q = key := by
          simpa [Z, gaborFundSingletonConfig, key] using
            (mem_filter.mp hq).1
        simp [this]
      · intro hq
        have : q = key := by simpa using hq
        simpa [this] using hmem
    have hsum : Sk.sum (fun q => (Z.mult q : ℝ)) =
        (riemannZetaMultiplicity ρ₀ : ℝ) := by
      rw [hfeq, Finset.sum_singleton]
      simp [Z, gaborFundSingletonConfig]
    exact hsum.trans_le (hsingle.trans hK)
  · have hnotin : ∀ q ∈ Sk, False := by
      intro q hq
      have hqeq : q = key := by
        simpa [Z, gaborFundSingletonConfig, key] using
          (mem_filter.mp hq).1
      exact hmem (by simpa [hqeq] using hq)
    have hsum0 : Sk.sum (fun q => (Z.mult q : ℝ)) = 0 :=
      Finset.sum_eq_zero fun q hq => False.elim (hnotin q hq)
    have hKpos : 0 < gaborKBinAt (|k| : ℝ) :=
      gaborKBinAt_pos (le_trans (by norm_num : (-2 : ℝ) ≤ 0) (abs_nonneg _))
    rw [hsum0]
    exact hKpos.le

lemma gaborFundSingleton_gammaDistinct
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    (gaborFundSingletonConfig ρ₀ hcrit hre him).gammaDistinct := by
  intro q₁ hq₁ q₂ hq₂ _
  have h1 : q₁ = gaborFundKey ρ₀ := by
    simpa [gaborFundSingletonConfig] using hq₁
  have h2 : q₂ = gaborFundKey ρ₀ := by
    simpa [gaborFundSingletonConfig] using hq₂
  rw [h1, h2]

lemma gaborFundSingleton_hostSigma
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    gaborHostSigma (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him) =
        (gaborFundKey ρ₀).1 := by
  simp [gaborHostSigma, gaborFundSingletonConfig]

lemma gaborFundSingleton_hostGamma
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    gaborHostGamma (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him) =
        (gaborFundKey ρ₀).2 := by
  set W := gaborFundSingletonConfig ρ₀ hcrit hre him
  set hW := gaborFundSingleton_nonempty ρ₀ hcrit hre him
  unfold gaborHostGamma
  have hσ := gaborFundSingleton_hostSigma ρ₀ hcrit hre him
  apply le_antisymm
  · have hmem : gaborFundKey ρ₀ ∈
        W.pts.filter (fun q => q.1 = gaborHostSigma W hW) := by
      refine mem_filter.mpr ⟨by simp [W, gaborFundSingletonConfig], ?_⟩
      exact hσ.symm
    exact Finset.inf'_le (fun q => q.2) hmem
  · rw [Finset.le_inf'_iff]
    intro q hq
    have : q = gaborFundKey ρ₀ := by
      simpa [W, gaborFundSingletonConfig] using (mem_filter.mp hq).1
    rw [this]

lemma gaborFundSingleton_host
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    (gaborHostSigma (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him),
      gaborHostGamma (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him)) =
      gaborFundKey ρ₀ :=
  Prod.ext (gaborFundSingleton_hostSigma ρ₀ hcrit hre him)
    (gaborFundSingleton_hostGamma ρ₀ hcrit hre him)

lemma gaborFundSingleton_sigma_pos
    (ρ₀ : ℂ) (_hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (_him : 0 < ρ₀.im) :
    0 < (gaborFundKey ρ₀).1 :=
  sub_pos.mpr hre

lemma gaborFundSingleton_sigma_lt_half
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (_hre : (1 / 2 : ℝ) < ρ₀.re) (_him : 0 < ρ₀.im) :
    (gaborFundKey ρ₀).1 < (1 / 2 : ℝ) := by
  change ρ₀.re - (1 / 2 : ℝ) < 1 / 2
  linarith [hcrit.2.2]

lemma gaborIsolationOmega_abs_le_gamma
    {sigma gamma a : ℝ} (hs : 0 < sigma) (hg : 0 < gamma)
    (ha : 0 < a) (hcap : a ≤ gaborOmegaCap sigma gamma) :
    |gaborIsolationOmega sigma gamma a| ≤ gamma := by
  have hhalf := gaborIsolationOmega_pos_of_cap hs hg ha.le hcap
  have hnn : 0 ≤ gaborIsolationOmega sigma gamma a :=
    le_trans (half_pos hg).le hhalf
  rw [abs_of_nonneg hnn]
  exact (gaborIsolationOmega_lt_gamma hs ha).le


/-- BoundLog2 packing+budget at every admissible width
`0 < a ≤ isolationShrink`, not only at the constructive shrink.
Discharged by `gaborBoundLog2AtAdmissibleWidth_holds`.
ω retunes as `gaborIsolationOmega σ γ a`; no extra hypothesis.
Not a `sorry`.  NO RH CLAIM. -/
def GaborBoundLog2AtAdmissibleWidth : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliantLog Z →
    Z.gammaDistinct →
    ∀ a : ℝ, 0 < a →
      a ≤ (isolationShrinkOfConfig Z hZ).1 →
      gaborHonestWeilLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a)
        Z gaborCInc <
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma Z hZ) a

theorem gaborBoundLog2AtAdmissibleWidth_holds :
    GaborBoundLog2AtAdmissibleWidth :=
  fun Z hZ hinc hdist a ha hiso =>
    gaborHonestWeilLog_lt_lockMargin_of_le Z hZ hinc hdist ha hiso

/-- Sorry-free: the admissible-width BoundLog2 remainder plus an
anchored witness (free `a` below isolation/lock/tail) yields a
negative full spectral zero-side.  The remainder is now a
theorem; this form keeps the Prop as an explicit hypothesis. -/
theorem gaborAnchored_zeroSide_neg_of_admissibleWidth
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀)
    (hwidth : GaborBoundLog2AtAdmissibleWidth) :
    gaborZeroSide (pureGaborTest wit.a wit.omega wit.ha) < 0 := by
  have hWlock :=
    hwidth wit.W wit.hW wit.hinc wit.hdist wit.a wit.ha wit.hiso
  have hWlock' :
      gaborHonestWeilLog wit.a wit.omega wit.W gaborCInc <
        ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a := by
    simpa [wit.hω] using hWlock
  have hrew :
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
          gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a +
        (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
          gaborEnhancement (gaborHostSigma wit.W wit.hW) wit.a = 0 := by
    ring
  have hcombo := add_lt_add hWlock' wit.htail
  exact (gaborAnchored_zeroSide_le_windowLog_plus_tail wit).trans_lt
    (hcombo.trans_eq hrew)

/-- Witness at its own packet `(a,ω)` ⇒ full spectral zero-side
`< 0`.  Uses BoundLog2 at the witness width, not only at the
constructive shrink.  Does not assert that a witness exists.
NO RH CLAIM. -/
theorem gaborAnchored_zeroSide_neg
    {ρ₀ : ℂ} (wit : GaborAnchoredWindowWitnessAt ρ₀) :
    gaborZeroSide (pureGaborTest wit.a wit.omega wit.ha) < 0 :=
  gaborAnchored_zeroSide_neg_of_admissibleWidth wit
    gaborBoundLog2AtAdmissibleWidth_holds

/-- Width-2 log-theta at a retuned centre is majorized by the
host ordinate: `ω(a) ∈ [γ/2, γ]` under the omega-cap, so
`|ω| ≤ γ` and the Path-A closed bound is γ-monotone. -/
lemma gaborLogWeightedTheta_two_le_gammaCap
    {gamma omega : ℝ} (hg : 0 < gamma)
    (hω0 : 0 ≤ omega) (hle : omega ≤ gamma) :
    gaborLogWeightedTheta (2 : ℝ) omega ≤
      (2 * zetaZerosInDiskCardBoundInner) *
        (3 * (gamma + 5) + 2 * gaborFarTailLog (2 : ℝ) gamma) := by
  have hθ :=
    gaborLogWeightedTheta_le_linClosed (a := (2 : ℝ)) (c := omega)
      (by norm_num)
  have habs : |omega| ≤ gamma := by
    rwa [abs_of_nonneg hω0]
  have hfar :
      gaborFarTailLog (2 : ℝ) omega ≤
        gaborFarTailLog (2 : ℝ) gamma :=
    gaborFarTailLog_mono_abs (by norm_num : (0 : ℝ) < 2)
      (habs.trans_eq (abs_of_pos hg).symm)
  have hcen : 3 * (|omega| + 5) ≤ 3 * (gamma + 5) := by
    nlinarith [habs]
  have hC : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have hparen :
      3 * (|omega| + 5) + 2 * gaborFarTailLog (2 : ℝ) omega ≤
        3 * (gamma + 5) + 2 * gaborFarTailLog (2 : ℝ) gamma :=
    add_le_add hcen (mul_le_mul_of_nonneg_left hfar (by norm_num))
  exact hθ.trans (mul_le_mul_of_nonneg_left hparen hC)

/-- Frozen-theta comparison at the *retuned* centre
`ω(a) = γ − πa/σ`.  For `a ≤ γσ/(2π)` one has
`ω(a) ∈ [γ/2, γ]`, so `|ω(a)| ≤ γ` and `θ_log(2, ω(a))` is
capped by the γ-host (r597 absorption pattern).  Combined with
`exists_small_width_mul_exp_neg` this yields the lock-gap
comparison for all sufficiently small `a`.  NO RH CLAIM. -/
theorem exists_small_width_outerPrefactor_lt_enhancement_retuned
    {sigmaStar gamma ε : ℝ} (_hσ : 0 < sigmaStar) (hg : 0 < gamma)
    (hε : 0 < ε) :
    ∃ a0 : ℝ, 0 < a0 ∧ a0 ≤ 1 ∧
      ∀ {a : ℝ}, 0 < a → a < a0 →
        a ≤ gaborOmegaCap sigmaStar gamma →
          gaborOuterTailTsumPrefactor a
              (gaborIsolationOmega sigmaStar gamma a) *
            Real.exp (-(1 : ℝ) / (8 * a)) <
              ε * gaborEnhancement sigmaStar a := by
  set Cγ : ℝ :=
    (2 * zetaZerosInDiskCardBoundInner) *
      (3 * (gamma + 5) + 2 * gaborFarTailLog (2 : ℝ) gamma)
  have hCγ : 0 ≤ Cγ := by
    have hC : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
      (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
    have hfar : 0 ≤ gaborFarTailLog (2 : ℝ) gamma := by
      unfold gaborFarTailLog
      exact tsum_nonneg fun _ => by positivity
    have hparen :
        0 ≤ 3 * (gamma + 5) + 2 * gaborFarTailLog (2 : ℝ) gamma :=
      add_nonneg (by positivity) (mul_nonneg (by norm_num) hfar)
    exact mul_nonneg hC hparen
  have hC4 : 0 ≤ 4 * Cγ := mul_nonneg (by norm_num) hCγ
  obtain ⟨a0, ha0, ha0le, hsmall⟩ :=
    exists_small_width_mul_exp_neg hC4 hε
  refine ⟨a0, ha0, ha0le, ?_⟩
  intro a ha hlt hcap
  set omega := gaborIsolationOmega sigmaStar gamma a
  have hωnn : 0 ≤ omega :=
    le_trans (half_pos hg).le
      (gaborIsolationOmega_pos_of_cap _hσ hg ha.le hcap)
  have hωle : omega ≤ gamma :=
    (gaborIsolationOmega_lt_gamma _hσ ha).le
  have hθcap := gaborLogWeightedTheta_two_le_gammaCap hg hωnn hωle
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
        (4 * (Real.pi / a) * Cγ) *
          Real.exp (-(1 : ℝ) / (8 * a)) := by
    unfold gaborOuterTailTsumPrefactor
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left (hθle.trans hθcap)
        (mul_nonneg (by norm_num) hπa.le))
      hexp0
  have hcore :
      4 * Cγ * Real.exp (-(1 : ℝ) / (8 * a)) < ε :=
    hsmall ha hlt
  have hexpE :
      (1 : ℝ) ≤ Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    Real.one_le_exp
      (div_nonneg (sq_nonneg _) (mul_nonneg (by norm_num) ha.le))
  have hrhs :
      ε ≤ ε * Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    le_mul_of_one_le_right hε.le hexpE
  have hmid :
      (4 * (Real.pi / a) * Cγ) *
          Real.exp (-(1 : ℝ) / (8 * a)) <
        ε * (Real.pi / a) *
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    have hmul :
        (Real.pi / a) *
            (4 * Cγ * Real.exp (-(1 : ℝ) / (8 * a))) <
          (Real.pi / a) *
            (ε * Real.exp (sigmaStar ^ 2 / (2 * a))) :=
      mul_lt_mul_of_pos_left (hcore.trans_le hrhs) hπa
    have hl :
        (4 * (Real.pi / a) * Cγ) *
            Real.exp (-(1 : ℝ) / (8 * a)) =
          (Real.pi / a) *
            (4 * Cγ * Real.exp (-(1 : ℝ) / (8 * a))) := by
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

/-- Residual geometric cover: every genuine fund-domain zero
with `|Im ρ − ω(a)| < R` is the target key.  Equivalent to
ordinate isolation of `ρ₀` in the retuned ω-window.  Open on
genuine zeros (ordinate clusters).  The multi-point window
form is likewise open.  Not a `sorry`.  NO RH CLAIM. -/
def GaborAnchoredCoverAt (ρ₀ : ℂ) (a R : ℝ) : Prop :=
  ∀ ρ : {z : ℂ // IsCriticalStripZetaZero z},
    gaborFundDomain ρ →
      |(ρ : ℂ).im -
          gaborIsolationOmega (gaborFundKey ρ₀).1
            (gaborFundKey ρ₀).2 a| < R →
        gaborFundKey (ρ : ℂ) = gaborFundKey ρ₀

lemma gaborFundSingleton_inner
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im)
    {a R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R)
    (hle : a ≤ (isolationShrinkOfConfig
      (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1) :
    ∀ q ∈ (gaborFundSingletonConfig ρ₀ hcrit hre him).pts,
      |q.2 -
        gaborIsolationOmega
          (gaborHostSigma
            (gaborFundSingletonConfig ρ₀ hcrit hre him)
            (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
          (gaborHostGamma
            (gaborFundSingletonConfig ρ₀ hcrit hre him)
            (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
          a| < R := by
  intro q hq
  set W := gaborFundSingletonConfig ρ₀ hcrit hre him
  set hW := gaborFundSingleton_nonempty ρ₀ hcrit hre him
  set σ := gaborHostSigma W hW
  set γ := gaborHostGamma W hW
  have hqeq : q = gaborFundKey ρ₀ := by
    simpa [W, gaborFundSingletonConfig] using hq
  have hγeq : γ = (gaborFundKey ρ₀).2 :=
    gaborFundSingleton_hostGamma ρ₀ hcrit hre him
  have hs : 0 < σ := gaborHostSigma_pos W hW
  have hs1 : σ ≤ 1 / 2 := (gaborHostSigma_lt_half W hW).le
  have hlock : a ≤ gaborALock σ :=
    hle.trans (isolationShrinkOfConfig_le_lock W hW)
  have hqdet : gaborPhaseDetune σ a ≤ (1 / 4 : ℝ) :=
    gaborALock_detune_le_quarter hs hs1 ha.le hlock
  have hωeq : gaborIsolationOmega σ γ a = γ - Real.pi * a / σ := rfl
  have hpi : 0 ≤ Real.pi * a / σ :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
  have hq2 : q.2 = γ := by
    rw [hqeq]
    exact hγeq.symm
  have hdiff : q.2 - gaborIsolationOmega σ γ a = Real.pi * a / σ := by
    rw [hq2, hωeq]
    ring
  have hdist :
      |q.2 - gaborIsolationOmega σ γ a| = gaborPhaseDetune σ a := by
    rw [hdiff, abs_of_nonneg hpi]
    rfl
  rw [hdist]
  exact lt_of_le_of_lt hqdet
    (lt_of_lt_of_le (by norm_num : (1 / 4 : ℝ) < 1) hR)

/-- Algebraic singleton constructor: host / increment /
`gammaDistinct` / isolation packet / inner radius are
sorry-free.  The two residual fields `htail` and `hcover` are
explicit hypotheses.  Does not assert existence at every
target.  NO RH CLAIM. -/
noncomputable def gaborAnchoredSingletonWitness
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im)
    (a : ℝ) (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig
      (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1)
    (R : ℝ) (hR : (1 : ℝ) ≤ R)
    (htail :
      gaborOuterTailTsumPrefactor a
          (gaborIsolationOmega
            (gaborHostSigma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            (gaborHostGamma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            a) *
        Real.exp (-(1 : ℝ) / (8 * a)) <
          (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
            gaborEnhancement
              (gaborHostSigma
                (gaborFundSingletonConfig ρ₀ hcrit hre him)
                (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
              a)
    (hcover : GaborAnchoredCoverAt ρ₀ a R) :
    GaborAnchoredWindowWitnessAt ρ₀ where
  W := gaborFundSingletonConfig ρ₀ hcrit hre him
  hW := gaborFundSingleton_nonempty ρ₀ hcrit hre him
  hρ₀crit := hcrit
  hρ₀fund := ⟨hre, him⟩
  hρ₀mem := by simp [gaborFundSingletonConfig]
  hhost := gaborFundSingleton_host ρ₀ hcrit hre him
  hinc := gaborFundSingleton_incrementCompliantLog ρ₀ hcrit hre him
  hdist := gaborFundSingleton_gammaDistinct ρ₀ hcrit hre him
  a := a
  ha := ha
  hiso := hle
  hlock := hle.trans (isolationShrinkOfConfig_le_lock
    (gaborFundSingletonConfig ρ₀ hcrit hre him)
    (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
  omega :=
    gaborIsolationOmega
      (gaborHostSigma
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
      (gaborHostGamma
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
      a
  hω := rfl
  hωpos :=
    gaborIsolationOmega_pos
      (gaborHostSigma_pos
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
      (gaborHostGamma_pos
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
      ha.le
      (hle.trans (isolationShrinkOfConfig_le_omegaCap
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him)))
  R := R
  hR := hR
  hinner := gaborFundSingleton_inner ρ₀ hcrit hre him ha hR hle
  htail := htail
  hgenuine := by
    intro q hq
    have hqeq : q = gaborFundKey ρ₀ := by
      simpa [gaborFundSingletonConfig] using hq
    refine ⟨ρ₀, hcrit, hre, him, hqeq.symm, ?_⟩
    simp [gaborFundSingletonConfig, hqeq]
  hcover := by
    intro ρ hD hlt
    have hωkey :
        gaborIsolationOmega
            (gaborHostSigma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            (gaborHostGamma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            a =
          gaborIsolationOmega (gaborFundKey ρ₀).1
            (gaborFundKey ρ₀).2 a := by
      simp [gaborFundSingleton_hostSigma ρ₀ hcrit hre him,
        gaborFundSingleton_hostGamma ρ₀ hcrit hre him]
    have hcov := hcover ρ hD (by simpa [hωkey] using hlt)
    have hmem : gaborFundKey (ρ : ℂ) ∈
        (gaborFundSingletonConfig ρ₀ hcrit hre him).pts := by
      simpa [gaborFundSingletonConfig, hcov]
    have heq : (ρ : ℂ) = ρ₀ := by
      apply Complex.ext
      · have hf := congrArg Prod.fst hcov
        simp [gaborFundKey] at hf
        linarith
      · have hg := congrArg Prod.snd hcov
        simpa [gaborFundKey] using hg
    refine ⟨hmem, ?_⟩
    simp [gaborFundSingletonConfig, heq]

/-- Part (1): algebraic singleton fragment plus the two residual
fields as hypotheses.  NO RH CLAIM. -/
theorem gaborAnchoredSingleton_of_tail_cover
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im)
    {a R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R)
    (hle : a ≤ (isolationShrinkOfConfig
      (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1)
    (htail :
      gaborOuterTailTsumPrefactor a
          (gaborIsolationOmega
            (gaborHostSigma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            (gaborHostGamma
              (gaborFundSingletonConfig ρ₀ hcrit hre him)
              (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
            a) *
        Real.exp (-(1 : ℝ) / (8 * a)) <
          (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
            gaborEnhancement
              (gaborHostSigma
                (gaborFundSingletonConfig ρ₀ hcrit hre him)
                (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
              a)
    (hcover : GaborAnchoredCoverAt ρ₀ a R) :
    Nonempty (GaborAnchoredWindowWitnessAt ρ₀) :=
  ⟨gaborAnchoredSingletonWitness ρ₀ hcrit hre him a ha hle R hR
    htail hcover⟩

/-- Part (2): the htail threshold is always met for sufficiently
small admissible widths at the retuned centre `ω(a)`.
Does not assert a witness.  NO RH CLAIM. -/
theorem exists_gaborFundSingleton_htail
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im) :
    ∃ a1 : ℝ, 0 < a1 ∧
      ∀ {a : ℝ}, 0 < a → a < a1 →
        a ≤ (isolationShrinkOfConfig
          (gaborFundSingletonConfig ρ₀ hcrit hre him)
          (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1 →
          gaborOuterTailTsumPrefactor a
              (gaborIsolationOmega
                (gaborHostSigma
                  (gaborFundSingletonConfig ρ₀ hcrit hre him)
                  (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
                (gaborHostGamma
                  (gaborFundSingletonConfig ρ₀ hcrit hre him)
                  (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
                a) *
            Real.exp (-(1 : ℝ) / (8 * a)) <
              (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
                gaborEnhancement
                  (gaborHostSigma
                    (gaborFundSingletonConfig ρ₀ hcrit hre him)
                    (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
                  a := by
  set W := gaborFundSingletonConfig ρ₀ hcrit hre him
  set hW := gaborFundSingleton_nonempty ρ₀ hcrit hre him
  set σ := gaborHostSigma W hW
  set γ := gaborHostGamma W hW
  have hs := gaborHostSigma_pos W hW
  have hg := gaborHostGamma_pos W hW
  have hε := gaborLockMarginGap_pos
  obtain ⟨a0, ha0, _, hsmall⟩ :=
    exists_small_width_outerPrefactor_lt_enhancement_retuned
      (sigmaStar := σ) (gamma := γ)
      (ε := Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ))
      hs hg hε
  refine ⟨a0, ha0, ?_⟩
  intro a ha hlt hle
  have hcap : a ≤ gaborOmegaCap σ γ :=
    hle.trans (isolationShrinkOfConfig_le_omegaCap W hW)
  exact hsmall ha hlt hcap

/-- Part (3): cover at an admissible width below the r598 tail
threshold inhabits the singleton witness.  `hcover` is the
remaining geometric hypothesis (ordinate clusters on genuine
zeros; multi-point windows likewise open).  Does **not** assert
`GaborAnchoredWitnessExists`.  NO RH CLAIM. -/
theorem exists_gaborAnchored_of_cover
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im)
    {R : ℝ} (hR : (1 : ℝ) ≤ R) :
    ∃ a1 : ℝ, 0 < a1 ∧
      ∀ {a : ℝ}, 0 < a → a < a1 →
        a ≤ (isolationShrinkOfConfig
          (gaborFundSingletonConfig ρ₀ hcrit hre him)
          (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1 →
          GaborAnchoredCoverAt ρ₀ a R →
            Nonempty (GaborAnchoredWindowWitnessAt ρ₀) := by
  obtain ⟨a1, ha1, hth⟩ :=
    exists_gaborFundSingleton_htail ρ₀ hcrit hre him
  refine ⟨a1, ha1, ?_⟩
  intro a ha hlt hle hcover
  exact gaborAnchoredSingleton_of_tail_cover ρ₀ hcrit hre him
    ha hR hle (hth ha hlt hle) hcover

/-- Cover at a concrete admissible width already below the
r598 tail threshold ⇒ nonempty singleton witness.
Does **not** assert `GaborAnchoredWitnessExists`.  NO RH CLAIM. -/
theorem gaborAnchoredCoverAt_to_nonempty
    (ρ₀ : ℂ) (hcrit : IsCriticalStripZetaZero ρ₀)
    (hre : (1 / 2 : ℝ) < ρ₀.re) (him : 0 < ρ₀.im)
    {a R : ℝ} (ha : 0 < a) (hR : (1 : ℝ) ≤ R)
    (hle : a ≤ (isolationShrinkOfConfig
      (gaborFundSingletonConfig ρ₀ hcrit hre him)
      (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1)
    (hcover : GaborAnchoredCoverAt ρ₀ a R)
    {a1 : ℝ} (_ha1 : 0 < a1) (hlt : a < a1)
    (hth : ∀ {a' : ℝ}, 0 < a' → a' < a1 →
      a' ≤ (isolationShrinkOfConfig
        (gaborFundSingletonConfig ρ₀ hcrit hre him)
        (gaborFundSingleton_nonempty ρ₀ hcrit hre him)).1 →
        gaborOuterTailTsumPrefactor a'
            (gaborIsolationOmega
              (gaborHostSigma
                (gaborFundSingletonConfig ρ₀ hcrit hre him)
                (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
              (gaborHostGamma
                (gaborFundSingletonConfig ρ₀ hcrit hre him)
                (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
              a') *
          Real.exp (-(1 : ℝ) / (8 * a')) <
            (Real.exp (-(Real.pi ^ 2 / 1024)) - (9 / 10 : ℝ)) *
              gaborEnhancement
                (gaborHostSigma
                  (gaborFundSingletonConfig ρ₀ hcrit hre him)
                  (gaborFundSingleton_nonempty ρ₀ hcrit hre him))
                a') :
    Nonempty (GaborAnchoredWindowWitnessAt ρ₀) :=
  gaborAnchoredSingleton_of_tail_cover ρ₀ hcrit hre him
    ha hR hle (hth ha hlt hle) hcover

/-! ## Named unasserted remainders (not `sorry`; no RH claim)

Window geometry / γ-clusters = open mathematics.
Arithmetic identification = RH-core via `GaborExplicitFormula`.
r598 discharges the singleton algebra and the small-width tail;
`GaborAnchoredWitnessExists` stays unasserted. -/

/-- Existence of an anchored witness at a given target.
Open mathematics: window geometry self-consistent at the final
ω, and pairwise ordinate distinctness on genuine zeros.
Not a `sorry`.  NO RH CLAIM.  L2 STOP: not asserted. -/
def GaborAnchoredWitnessExists : Prop :=
  ∀ ρ₀ : ℂ, IsCriticalStripZetaZero ρ₀ →
    (1 / 2 : ℝ) < ρ₀.re → 0 < ρ₀.im →
      Nonempty (GaborAnchoredWindowWitnessAt ρ₀)

/-- Spectral zero-side negativity of a pure isolation packet
produces an admissible arithmetic separator.  Proved r600 —
pole-sign lemma from EF + `Re ĥ(1) ≥ 0`, NOT RH-core. -/
theorem gaborSpectralToArithmetic
    (hexp : GaborExplicitFormula)
    {a omega : ℝ} (ha : 0 < a)
    (_hω : 0 < omega)
    (hF : (pureGaborTest a omega ha).admissible)
    (hZ : gaborZeroSide (pureGaborTest a omega ha) < 0) :
    gaborArithmeticFormula (pureGaborTest a omega ha) < 0 :=
  gaborArithmeticFormula_neg_of_zeroSide_neg hF hexp
    (gaborHat_one_nonneg_pure a omega ha) hZ

/-- Package form of `gaborSpectralToArithmetic`.  Discharged r600
from `GaborExplicitFormula`. -/
def GaborSpectralToArithmetic : Prop :=
  ∀ {a omega : ℝ} (ha : 0 < a),
    0 < omega →
    (pureGaborTest a omega ha).admissible →
      gaborZeroSide (pureGaborTest a omega ha) < 0 →
        gaborArithmeticFormula (pureGaborTest a omega ha) < 0

theorem GaborSpectralToArithmetic_holds
    (hexp : GaborExplicitFormula) :
    GaborSpectralToArithmetic :=
  fun ha hω hF hZ => gaborSpectralToArithmetic hexp ha hω hF hZ

/-- Named implication only: existence of anchored witnesses at
every off-critical fund-domain zero, plus isolation-packet
negativity and the explicit formula (pole-sign remainder
discharged r600), would feed
`GaborArithmeticSeparatesOffCriticalZeros`.
Unasserted.  Not a `sorry`.
This round does **not** assert the conclusion. -/
def gabor_anchored_to_arithmetic_separator : Prop :=
  GaborAnchoredWitnessExists →
    GaborExplicitFormula →
      GaborArithmeticSeparatesOffCriticalZeros

#print axioms gaborHonestWeilLog_of_subconfig
#print axioms gaborHonestWeilLog_le_window_plus_theta
#print axioms gaborHonestWeilLog_le_subconfig_plus_theta
#print axioms gaborHonestWeilLog_neg_of_lock_and_tail
#print axioms gaborHonestWeilLog_glue_neg_of_small_isolation
#print axioms gaborCanonicalConfig_honestWeilLog_neg
#print axioms gabor_exhaustion_algebra_log
#print axioms gaborAnchored_zeroSide_le_windowLog_plus_tail
#print axioms gaborAnchored_zeroSide_neg_of_isolationPacket
#print axioms gaborAnchored_zeroSide_neg_of_admissibleWidth
#print axioms gaborBoundLog2AtAdmissibleWidth_holds
#print axioms gaborAnchored_zeroSide_neg
#print axioms gaborFundSingleton_incrementCompliantLog
#print axioms gaborFundSingleton_gammaDistinct
#print axioms gaborFundSingleton_host
#print axioms gaborIsolationOmega_abs_le_gamma
#print axioms gaborLogWeightedTheta_two_le_gammaCap
#print axioms exists_small_width_outerPrefactor_lt_enhancement_retuned
#print axioms gaborFundSingleton_inner
#print axioms gaborAnchoredSingleton_of_tail_cover
#print axioms exists_gaborFundSingleton_htail
#print axioms exists_gaborAnchored_of_cover
#print axioms gaborAnchoredCoverAt_to_nonempty
#print axioms gaborSpectralToArithmetic
#print axioms GaborSpectralToArithmetic_holds

end RH
