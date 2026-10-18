/-
RH/GaborDominanceProof.lean -- r569 remaining dominance bricks.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

After isolation the peak and κ windows contain no foreign ordinate,
so `T_gap = 0` (absorbed by `T_far`).  Phase-coherent quadrupoles
with a large minus-lobe exponent satisfy `Q < 0`.  The host
minus-lobe `−η m★` dominates the explicit remainders once the
r569 width cap is in force.

`GaborDominanceBound` is discharged from the one named remainder
`GaborDominanceAssembly` (= packing comparison
`GaborHonestWeilLeMajorant` ∧ remainder budget
`GaborRemainderBudget`).  T_gap = 0 and host `Q < 0` are proved.
-/
import RH.GaborDominance
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Order

namespace RH

open scoped Classical
open Set Finset

/-! ## Host / gap bookkeeping -/

theorem gaborHostSigma_max (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) {q : ℝ × ℝ} (hq : q ∈ Z.pts) :
    q.1 ≤ gaborHostSigma Z hZ := by
  simpa [gaborHostSigma] using Finset.le_sup' (fun r => r.1) hq

theorem gaborHost_unique_gamma_of_isolated (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hiso : Z.gammaHostIsolated hZ)
    {q : ℝ × ℝ} (hq : q ∈ Z.pts)
    (heq : q.2 = gaborHostGamma Z hZ) :
    q = (gaborHostSigma Z hZ, gaborHostGamma Z hZ) :=
  hiso q hq heq

theorem gaborHost_unique_gamma (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hdist : Z.gammaDistinct)
    {q : ℝ × ℝ} (hq : q ∈ Z.pts)
    (heq : q.2 = gaborHostGamma Z hZ) :
    q = (gaborHostSigma Z hZ, gaborHostGamma Z hZ) :=
  gaborHost_unique_gamma_of_isolated Z hZ
    (gammaDistinct_hostIsolated Z hZ hdist) hq heq

theorem gaborForeignDMin_le (Z : GaborCanonicalConfig) (gammaStar : ℝ)
    {q : ℝ × ℝ} (hq : q ∈ Z.pts) (hne : q.2 ≠ gammaStar) :
    gaborForeignDMin Z gammaStar ≤ |q.2 - gammaStar| := by
  have hmem : q ∈ Z.pts.filter (fun r => r.2 ≠ gammaStar) :=
    mem_filter.mpr ⟨hq, hne⟩
  have hne' : (Z.pts.filter (fun r => r.2 ≠ gammaStar)).Nonempty :=
    ⟨q, hmem⟩
  unfold gaborForeignDMin
  rw [dif_pos hne']
  exact Finset.inf'_le (fun r => |r.2 - gammaStar|) hmem

theorem gaborCInc_pos : 0 < gaborCInc :=
  mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos

/-! ## Piece 1: T_gap is empty after isolation -/

theorem admissible_peakWindow_empty {sigma gamma dMin a gamma' : ℝ}
    (hs : 0 < sigma) (hd : 0 < dMin)
    (hadm : gaborAdmissibleA sigma gamma dMin a)
    (hgap : dMin ≤ |gamma' - gamma|) :
    ¬ gaborInPeakWindow gamma' (gaborIsolationOmega sigma gamma a) a := by
  intro hwin
  have ha : 0 < a := hadm.1
  have hrad : Real.pi * a / sigma + gaborIsolationEpsilon a ≤ dMin / 2 := by
    simpa [gaborIsolationRadius] using hadm.2.2
  have hpi : 0 ≤ Real.pi * a / sigma :=
    div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
  have hdet : |gaborIsolationOmega sigma gamma a - gamma| =
      Real.pi * a / sigma := by
    unfold gaborIsolationOmega
    rw [abs_of_nonpos (by linarith [hpi])]
    ring
  have htri :=
    abs_sub_le gamma' (gaborIsolationOmega sigma gamma a) gamma
  have hεlt : gaborIsolationEpsilon a <
      |gamma' - gaborIsolationOmega sigma gamma a| := by
    have hlo : dMin - Real.pi * a / sigma ≤
        |gamma' - gaborIsolationOmega sigma gamma a| := by
      linarith [hgap, hdet, htri]
    linarith [hrad, hlo, hd]
  exact (not_le_of_gt hεlt) hwin

theorem admissible_kappaWindow_empty {sigma gamma dMin a gamma' : ℝ}
    (hs : 0 < sigma) (hd : 0 < dMin)
    (hadm : gaborAdmissibleA sigma gamma dMin a)
    (hgap : dMin ≤ |gamma' - gamma|) :
    ¬ gaborInKappaWindow gamma' gamma sigma a := by
  intro hwin
  have ha : 0 < a := hadm.1
  have hrad : Real.pi * a / sigma + gaborIsolationEpsilon a ≤ dMin / 2 := by
    simpa [gaborIsolationRadius] using hadm.2.2
  have hκ : gaborKappa * a / sigma = a / sigma := by
    unfold gaborKappa
    ring
  have hπa : a < Real.pi * a := by
    nlinarith [ha, Real.pi_gt_three]
  have hπ : a / sigma < Real.pi * a / sigma :=
    div_lt_div_of_pos_right hπa hs
  have hε : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
  have hκlt : gaborKappa * a / sigma < dMin := by
    rw [hκ]
    linarith [hrad, hπ, hε, hd]
  exact (not_le_of_gt hκlt) (hgap.trans hwin)

theorem isolationShrinkOfConfigRaw_of_foreign
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hfor : (Z.pts.filter
        (fun q => q.2 ≠ gaborHostGamma Z hZ)).Nonempty) :
    isolationShrinkOfConfigRaw Z hZ =
      isolationShrink (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
        (gaborForeignDMin Z (gaborHostGamma Z hZ))
        (gaborHostSigma_pos Z hZ) (gaborHostGamma_pos Z hZ)
        (gaborForeignDMin_pos Z (gaborHostGamma Z hZ)) := by
  simp [isolationShrinkOfConfigRaw, hfor]

theorem isolationShrinkOfConfig_admissible_of_foreign
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hfor : (Z.pts.filter
        (fun q => q.2 ≠ gaborHostGamma Z hZ)).Nonempty) :
    gaborAdmissibleA (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
      (gaborForeignDMin Z (gaborHostGamma Z hZ))
      (isolationShrinkOfConfig Z hZ).1 := by
  have hs := gaborHostSigma_pos Z hZ
  have hs1 := gaborHostSigma_lt_half Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hd := gaborForeignDMin_pos Z (gaborHostGamma Z hZ)
  have hraw := isolationShrinkOfConfigRaw_of_foreign Z hZ hfor
  have hspec :=
    isolationShrink_spec hs hg hd
  have hrawAdm : gaborAdmissibleA (gaborHostSigma Z hZ)
      (gaborHostGamma Z hZ) (gaborForeignDMin Z (gaborHostGamma Z hZ))
      (isolationShrinkOfConfigRaw Z hZ).1 := by
    rw [hraw]
    exact hspec.1
  have haeq := isolationShrinkOfConfig_a_eq Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hA : (isolationShrinkOfConfig Z hZ).1 ≤
      gaborAdmissibleAMax (gaborHostSigma Z hZ) (gaborHostGamma Z hZ) := by
    rw [haeq]
    exact (min_le_left _ _).trans hrawAdm.2.1
  have hlock : gaborAdmissibleAMax (gaborHostSigma Z hZ)
      (gaborHostGamma Z hZ) ≤ gaborALock (gaborHostSigma Z hZ) :=
    min_le_left _ _
  have hAC : (isolationShrinkOfConfigRaw Z hZ).1 ≤
      1 / (4 * (gaborKBin : ℝ)) :=
    hrawAdm.2.1.trans (hlock.trans (gaborALock_lt_inv_bin hs.le hs1).le)
  have hab : (isolationShrinkOfConfig Z hZ).1 ≤
      (isolationShrinkOfConfigRaw Z hZ).1 := by
    rw [haeq]
    exact min_le_left _ _
  have hrad : gaborIsolationRadius (gaborHostSigma Z hZ)
      (isolationShrinkOfConfig Z hZ).1 ≤
      gaborForeignDMin Z (gaborHostGamma Z hZ) / 2 :=
    (gaborIsolationRadius_mono_small hs ha hab hAC).trans hrawAdm.2.2
  exact ⟨ha, hA, hrad⟩

/-- Smaller positive widths stay admissible: isolation radius is
monotone on the canonical strip (`gaborIsolationRadius_mono_small`).
The packet centre retunes as `ω(a) = γ★ − πa/σ★`; this is not
the same (a,ω) pair.  Admissibility is a radius statement and
survives the retune. -/
theorem isolationShrinkOfConfig_admissible_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hfor : (Z.pts.filter
        (fun q => q.2 ≠ gaborHostGamma Z hZ)).Nonempty)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborAdmissibleA (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
      (gaborForeignDMin Z (gaborHostGamma Z hZ)) a := by
  have hadm0 := isolationShrinkOfConfig_admissible_of_foreign Z hZ hfor
  have hs := gaborHostSigma_pos Z hZ
  have hs1 := gaborHostSigma_lt_half Z hZ
  have hA : a ≤ gaborAdmissibleAMax (gaborHostSigma Z hZ)
      (gaborHostGamma Z hZ) :=
    hle.trans hadm0.2.1
  have hAmax_lock :
      gaborAdmissibleAMax (gaborHostSigma Z hZ) (gaborHostGamma Z hZ) ≤
        gaborALock (gaborHostSigma Z hZ) :=
    min_le_left _ _
  have hbin : (isolationShrinkOfConfig Z hZ).1 ≤
      1 / (4 * (gaborKBin : ℝ)) :=
    hadm0.2.1.trans
      (hAmax_lock.trans (gaborALock_lt_inv_bin hs.le hs1).le)
  have hrad : gaborIsolationRadius (gaborHostSigma Z hZ) a ≤
      gaborForeignDMin Z (gaborHostGamma Z hZ) / 2 :=
    (gaborIsolationRadius_mono_small hs ha hle hbin).trans hadm0.2.2
  exact ⟨ha, hA, hrad⟩

theorem gaborTGap_filter_empty (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hdist : Z.gammaDistinct) :
    Z.pts.filter (fun q =>
        q.1 < gaborHostSigma Z hZ ∧
          (gaborInPeakWindow q.2 (isolationShrinkOfConfig Z hZ).2
              (isolationShrinkOfConfig Z hZ).1 ∨
            gaborInKappaWindow q.2 (gaborHostGamma Z hZ)
              (gaborHostSigma Z hZ)
              (isolationShrinkOfConfig Z hZ).1) ∧
          ¬ gaborPhaseCoherent q.1 q.2 (gaborHostSigma Z hZ)
              (gaborHostGamma Z hZ)
              (isolationShrinkOfConfig Z hZ).1) = ∅ := by
  rw [filter_eq_empty_iff]
  intro q hq
  rintro ⟨hσlt, hwin, _hcoh⟩
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set ω := (isolationShrinkOfConfig Z hZ).2
  have hωeq : ω = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  by_cases hγeq : q.2 = γ
  · have hqeq := gaborHost_unique_gamma Z hZ hdist hq hγeq
    have hσeq : q.1 = σ := congrArg Prod.fst hqeq
    exact (not_lt_of_ge hσeq.ge) hσlt
  · have hfor : (Z.pts.filter (fun r => r.2 ≠ γ)).Nonempty :=
      ⟨q, mem_filter.mpr ⟨hq, hγeq⟩⟩
    have hadm := isolationShrinkOfConfig_admissible_of_foreign Z hZ hfor
    have hgap := gaborForeignDMin_le Z γ hq hγeq
    have hs := gaborHostSigma_pos Z hZ
    have hd := gaborForeignDMin_pos Z γ
    have hpeak : ¬ gaborInPeakWindow q.2 ω a := by
      rw [hωeq]
      exact admissible_peakWindow_empty hs hd hadm hgap
    have hκ : ¬ gaborInKappaWindow q.2 γ σ a :=
      admissible_kappaWindow_empty hs hd hadm hgap
    exact hwin.elim hpeak hκ

/-- After isolation + `gammaDistinct`, T_gap vanishes: foreign
ordinates lie outside both windows, and the host has `σ=σ★`. -/
theorem gaborTGap_eq_zero (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hdist : Z.gammaDistinct) :
    gaborTGap (isolationShrinkOfConfig Z hZ).1 Z
      (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
      (isolationShrinkOfConfig Z hZ).2 = 0 := by
  unfold gaborTGap
  rw [gaborTGap_filter_empty Z hZ hdist, sum_empty]

/-- r579: T_gap emptiness needs only host-ordinate isolation,
not global injectivity of `γ`. -/
theorem gaborTGap_filter_empty_of_isolated (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hiso : Z.gammaHostIsolated hZ) :
    Z.pts.filter (fun q =>
        q.1 < gaborHostSigma Z hZ ∧
          (gaborInPeakWindow q.2 (isolationShrinkOfConfig Z hZ).2
              (isolationShrinkOfConfig Z hZ).1 ∨
            gaborInKappaWindow q.2 (gaborHostGamma Z hZ)
              (gaborHostSigma Z hZ)
              (isolationShrinkOfConfig Z hZ).1) ∧
          ¬ gaborPhaseCoherent q.1 q.2 (gaborHostSigma Z hZ)
              (gaborHostGamma Z hZ)
              (isolationShrinkOfConfig Z hZ).1) = ∅ := by
  rw [filter_eq_empty_iff]
  intro q hq
  rintro ⟨hσlt, hwin, _hcoh⟩
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set ω := (isolationShrinkOfConfig Z hZ).2
  have hωeq : ω = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  by_cases hγeq : q.2 = γ
  · have hqeq := gaborHost_unique_gamma_of_isolated Z hZ hiso hq hγeq
    have hσeq : q.1 = σ := congrArg Prod.fst hqeq
    exact (not_lt_of_ge hσeq.ge) hσlt
  · have hfor : (Z.pts.filter (fun r => r.2 ≠ γ)).Nonempty :=
      ⟨q, mem_filter.mpr ⟨hq, hγeq⟩⟩
    have hadm := isolationShrinkOfConfig_admissible_of_foreign Z hZ hfor
    have hgap := gaborForeignDMin_le Z γ hq hγeq
    have hs := gaborHostSigma_pos Z hZ
    have hd := gaborForeignDMin_pos Z γ
    have hpeak : ¬ gaborInPeakWindow q.2 ω a := by
      rw [hωeq]
      exact admissible_peakWindow_empty hs hd hadm hgap
    have hκ : ¬ gaborInKappaWindow q.2 γ σ a :=
      admissible_kappaWindow_empty hs hd hadm hgap
    exact hwin.elim hpeak hκ

theorem gaborTGap_eq_zero_of_isolated (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (hiso : Z.gammaHostIsolated hZ) :
    gaborTGap (isolationShrinkOfConfig Z hZ).1 Z
      (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
      (isolationShrinkOfConfig Z hZ).2 = 0 := by
  unfold gaborTGap
  rw [gaborTGap_filter_empty_of_isolated Z hZ hiso, sum_empty]

/-! ## Piece 2: Q < 0 on κ-coherent points with large exponent -/

theorem gaborPhiMinus_sub_pi {sigma' gamma' sigmaStar gammaStar a : ℝ}
    (hs : sigmaStar ≠ 0) (ha : a ≠ 0) :
    gaborPhiMinus sigma' gamma'
        (gaborIsolationOmega sigmaStar gammaStar a) a - Real.pi =
      sigma' * (gamma' - gammaStar) / a +
        Real.pi * (sigma' / sigmaStar - 1) := by
  unfold gaborPhiMinus gaborIsolationOmega
  field_simp [hs, ha]
  ring

theorem gabor_phase_coherent_cos_general
    {sigma' gamma' sigmaStar gammaStar a : ℝ}
    (hs : sigmaStar ≠ 0) (ha : 0 < a)
    (hcoh : gaborPhaseCoherent sigma' gamma' sigmaStar gammaStar a) :
    Real.cos (gaborPhiMinus sigma' gamma'
        (gaborIsolationOmega sigmaStar gammaStar a) a) ≤
      -Real.cos gaborKappa := by
  have hφ :=
    gaborPhiMinus_sub_pi (sigma' := sigma') (gamma' := gamma')
      (sigmaStar := sigmaStar) (gammaStar := gammaStar) (a := a)
      hs (ne_of_gt ha)
  set θ : ℝ :=
    sigma' * (gamma' - gammaStar) / a +
      Real.pi * (sigma' / sigmaStar - 1)
  have hθ : |θ| ≤ gaborKappa := hcoh
  have hcos :
      Real.cos (gaborPhiMinus sigma' gamma'
          (gaborIsolationOmega sigmaStar gammaStar a) a) =
        -Real.cos θ := by
    have hsum : gaborPhiMinus sigma' gamma'
        (gaborIsolationOmega sigmaStar gammaStar a) a =
          Real.pi + θ := by linarith [hφ]
    rw [hsum, add_comm, Real.cos_add_pi]
  rw [hcos]
  have hκpi : gaborKappa ≤ Real.pi :=
    gaborKappa_lt_half_pi.le.trans
      (div_le_self Real.pi_pos.le (by norm_num))
  have hcmp : Real.cos gaborKappa ≤ Real.cos |θ| :=
    Real.cos_le_cos_of_nonneg_of_le_pi (abs_nonneg _) hκpi hθ
  linarith [(Real.cos_abs θ).symm ▸ hcmp]

noncomputable def gaborAmpPlus (a omega sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a))

noncomputable def gaborAmpMinus (a omega sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a))

noncomputable def gaborAmpCross (a omega sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a))

theorem gaborAmp_plus_div_minus {a omega sigma gamma : ℝ}
    (ha : 0 < a) :
    gaborAmpPlus a omega sigma gamma /
        gaborAmpMinus a omega sigma gamma =
      Real.exp (-(2 * gamma * omega / a)) := by
  unfold gaborAmpPlus gaborAmpMinus
  rw [← Real.exp_sub]
  congr 1
  field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]
  ring

theorem gaborAmp_cross_div_minus {a omega sigma gamma : ℝ}
    (ha : 0 < a) :
    gaborAmpCross a omega sigma gamma /
        gaborAmpMinus a omega sigma gamma =
      Real.exp (-(gamma * omega / a)) := by
  unfold gaborAmpCross gaborAmpMinus
  rw [← Real.exp_sub]
  congr 1
  field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]
  ring

theorem gaborCos_one_gt_half : (1 / 2 : ℝ) < Real.cos gaborKappa := by
  unfold gaborKappa
  have h1 : (1 : ℝ) < Real.pi / 3 := by
    linarith [Real.pi_gt_three]
  have hdec : Real.cos (Real.pi / 3) < Real.cos 1 :=
    Real.cos_lt_cos_of_nonneg_of_le_pi (by norm_num)
      (div_le_self Real.pi_pos.le (by norm_num)) h1
  linarith [hdec, Real.cos_pi_div_three]

theorem gaborExp_neg_four_le : Real.exp (-(4 : ℝ)) ≤ (1 / 16 : ℝ) := by
  have he2 : (2 : ℝ) ≤ Real.exp 1 := by
    linarith [Real.add_one_le_exp (1 : ℝ)]
  have he4 : (16 : ℝ) ≤ Real.exp 4 := by
    have hpow : (2 : ℝ) ^ 4 ≤ (Real.exp 1) ^ 4 :=
      pow_le_pow_left₀ (by norm_num) he2 4
    have hexp : (Real.exp 1) ^ 4 = Real.exp 4 := by
      rw [← Real.exp_nat_mul]
      norm_num
    calc
      (16 : ℝ) = (2 : ℝ) ^ 4 := by norm_num
      _ ≤ (Real.exp 1) ^ 4 := hpow
      _ = Real.exp 4 := hexp
  rw [Real.exp_neg, one_div]
  exact (inv_le_inv₀ (Real.exp_pos _) (by norm_num)).mpr he4

theorem gaborAmp_combo_lt {a omega sigma gamma : ℝ}
    (ha : 0 < a) (hexp : 4 ≤ gamma * omega / a) :
    gaborAmpPlus a omega sigma gamma +
        2 * gaborAmpCross a omega sigma gamma <
      Real.cos gaborKappa * gaborAmpMinus a omega sigma gamma := by
  have hA : 0 < gaborAmpMinus a omega sigma gamma := Real.exp_pos _
  have hx : Real.exp (-(gamma * omega / a)) ≤ Real.exp (-(4 : ℝ)) :=
    Real.exp_le_exp.mpr (neg_le_neg hexp)
  have hx' : Real.exp (-(gamma * omega / a)) ≤ (1 / 16 : ℝ) :=
    hx.trans gaborExp_neg_four_le
  have hplus :=
    gaborAmp_plus_div_minus (sigma := sigma) (gamma := gamma)
      (omega := omega) ha
  have hcross :=
    gaborAmp_cross_div_minus (sigma := sigma) (gamma := gamma)
      (omega := omega) ha
  have hsq : Real.exp (-(2 * gamma * omega / a)) =
      (Real.exp (-(gamma * omega / a))) ^ 2 := by
    have h2 : -(2 * gamma * omega / a) =
        (2 : ℕ) * (-(gamma * omega / a)) := by
      simp [nsmul_eq_mul]
      ring
    rw [h2, Real.exp_nat_mul]
  have hcombo :
      gaborAmpPlus a omega sigma gamma /
          gaborAmpMinus a omega sigma gamma +
        2 * (gaborAmpCross a omega sigma gamma /
          gaborAmpMinus a omega sigma gamma) ≤
        (1 / 16 : ℝ) ^ 2 + 2 * (1 / 16 : ℝ) := by
    rw [hplus, hcross, hsq]
    have hsqle := pow_le_pow_left₀ (Real.exp_pos _).le hx' 2
    nlinarith [hx', hsqle]
  have hsplit :
      (gaborAmpPlus a omega sigma gamma +
          2 * gaborAmpCross a omega sigma gamma) /
        gaborAmpMinus a omega sigma gamma =
        gaborAmpPlus a omega sigma gamma /
            gaborAmpMinus a omega sigma gamma +
          2 * (gaborAmpCross a omega sigma gamma /
            gaborAmpMinus a omega sigma gamma) := by
    field_simp [ne_of_gt hA]
  have hdiv :
      (gaborAmpPlus a omega sigma gamma +
          2 * gaborAmpCross a omega sigma gamma) /
        gaborAmpMinus a omega sigma gamma <
      Real.cos gaborKappa := by
    rw [hsplit]
    exact (hcombo.trans_lt (by norm_num)).trans gaborCos_one_gt_half
  exact (div_lt_iff₀ hA).mp hdiv

theorem gaborQuadrupole_le_of_phase_coherent
    {a sigma' gamma' sigmaStar gammaStar : ℝ}
    (ha : 0 < a) (hs : sigmaStar ≠ 0)
    (hcoh : gaborPhaseCoherent sigma' gamma' sigmaStar gammaStar a) :
    gaborQuadrupole a (gaborIsolationOmega sigmaStar gammaStar a)
        sigma' gamma' ≤
      Real.pi / a *
        (gaborAmpPlus a (gaborIsolationOmega sigmaStar gammaStar a)
            sigma' gamma' +
          2 * gaborAmpCross a (gaborIsolationOmega sigmaStar gammaStar a)
            sigma' gamma' -
          Real.cos gaborKappa *
            gaborAmpMinus a (gaborIsolationOmega sigmaStar gammaStar a)
              sigma' gamma') := by
  set ω := gaborIsolationOmega sigmaStar gammaStar a
  have hcos := gabor_phase_coherent_cos_general hs ha hcoh
  have hAp : 0 ≤ gaborAmpPlus a ω sigma' gamma' := (Real.exp_pos _).le
  have hAx : 0 ≤ gaborAmpCross a ω sigma' gamma' := (Real.exp_pos _).le
  have hc1 : Real.cos (sigma' * (gamma' + ω) / a) ≤ 1 := Real.cos_le_one _
  have hc2 : Real.cos (sigma' * gamma' / a) ≤ 1 := Real.cos_le_one _
  unfold gaborQuadrupole gaborAmpPlus gaborAmpMinus gaborAmpCross
  have hcos' : Real.cos (sigma' * (gamma' - ω) / a) ≤
      -Real.cos gaborKappa := by
    simpa [gaborPhiMinus] using hcos
  have hminus :
      Real.exp ((sigma' ^ 2 - (gamma' - ω) ^ 2) / (2 * a)) *
          Real.cos (sigma' * (gamma' - ω) / a) ≤
        -Real.cos gaborKappa *
          Real.exp ((sigma' ^ 2 - (gamma' - ω) ^ 2) / (2 * a)) := by
    have := mul_le_mul_of_nonneg_left hcos'
      (Real.exp_pos ((sigma' ^ 2 - (gamma' - ω) ^ 2) / (2 * a))).le
    linarith
  have hplus :
      Real.exp ((sigma' ^ 2 - (gamma' + ω) ^ 2) / (2 * a)) *
          Real.cos (sigma' * (gamma' + ω) / a) ≤
        Real.exp ((sigma' ^ 2 - (gamma' + ω) ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right (Real.exp_pos _).le hc1
  have hcross :
      Real.exp ((sigma' ^ 2 - gamma' ^ 2 - ω ^ 2) / (2 * a)) *
          Real.cos (sigma' * gamma' / a) ≤
        Real.exp ((sigma' ^ 2 - gamma' ^ 2 - ω ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right (Real.exp_pos _).le hc2
  have hπa : 0 ≤ Real.pi / a := div_nonneg Real.pi_pos.le ha.le
  nlinarith [hplus, hminus, hcross, hπa]

/-- Host exponent: `a ≤ γ★²/512` and `ω ≥ γ★/2` give `γ★ ω / a ≥ 256`. -/
theorem host_gamma_omega_div_a {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512) :
    4 ≤ gamma * gaborIsolationOmega sigma gamma a / a := by
  have hωhalf := gaborIsolationOmega_pos_of_cap hs hg ha.le hωcap
  have hprod : gamma * (gamma / 2) / a ≤
      gamma * gaborIsolationOmega sigma gamma a / a :=
    div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left hωhalf hg.le) ha.le
  have hform : gamma * (gamma / 2) / a = gamma ^ 2 / (2 * a) := by ring
  have h256 : (256 : ℝ) ≤ gamma ^ 2 / (2 * a) := by
    have : gamma ^ 2 / 512 ≥ a := hγsq
    have hpos : 0 < 2 * a := mul_pos (by norm_num) ha
    have : 256 * (2 * a) ≤ gamma ^ 2 := by
      have ha512 : a * 512 ≤ gamma ^ 2 := by
        rw [le_div_iff₀ (by norm_num : (0 : ℝ) < 512)] at hγsq
        exact hγsq
      linarith
    exact (le_div_iff₀ hpos).mpr this
  exact (by norm_num : (4 : ℝ) ≤ 256).trans (h256.trans (hform ▸ hprod))

theorem gaborHost_phase_coherent {sigma gamma a : ℝ}
    (hs : sigma ≠ 0) (ha : a ≠ 0) :
    gaborPhaseCoherent sigma gamma sigma gamma a := by
  unfold gaborPhaseCoherent gaborKappa
  have : sigma * (gamma - gamma) / a + Real.pi * (sigma / sigma - 1) = 0 := by
    field_simp [hs, ha]
    ring
  rw [this]
  simp

/-- Host quadrupole is strictly negative under the r569 width cap. -/
theorem gabor_host_quadrupole_neg {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a)
    (hωcap : a ≤ gaborOmegaCap sigma gamma)
    (hγsq : a ≤ gamma ^ 2 / 512) :
    gaborQuadrupole a (gaborIsolationOmega sigma gamma a) sigma gamma < 0 := by
  have hexp := host_gamma_omega_div_a hs hg ha hωcap hγsq
  have hcoh :=
    gaborHost_phase_coherent (sigma := sigma) (gamma := gamma)
      (ne_of_gt hs) (ne_of_gt ha)
  have hcombo :=
    gaborAmp_combo_lt (sigma := sigma) (gamma := gamma)
      (omega := gaborIsolationOmega sigma gamma a) ha hexp
  have hle := gaborQuadrupole_le_of_phase_coherent ha (ne_of_gt hs) hcoh
  have hπa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hparen :
      gaborAmpPlus a (gaborIsolationOmega sigma gamma a) sigma gamma +
        2 * gaborAmpCross a (gaborIsolationOmega sigma gamma a)
          sigma gamma -
        Real.cos gaborKappa *
          gaborAmpMinus a (gaborIsolationOmega sigma gamma a)
            sigma gamma < 0 := by
    linarith [hcombo]
  exact hle.trans_lt (mul_neg_of_pos_of_neg hπa hparen)

/-- General coherent `Q < 0` given the explicit exponent threshold.
The host case is discharged above; foreign coherent points are empty
after isolation, so this is the remaining analytic form. -/
theorem gabor_phase_coherent_quadrupole_neg_of_exp
    {sigma' gamma' sigmaStar gammaStar a : ℝ}
    (ha : 0 < a) (hs : sigmaStar ≠ 0)
    (hexp : 4 ≤ gamma' * gaborIsolationOmega sigmaStar gammaStar a / a)
    (hcoh : gaborPhaseCoherent sigma' gamma' sigmaStar gammaStar a) :
    gaborQuadrupole a (gaborIsolationOmega sigmaStar gammaStar a)
      sigma' gamma' < 0 := by
  have hcombo :=
    gaborAmp_combo_lt (sigma := sigma') (gamma := gamma')
      (omega := gaborIsolationOmega sigmaStar gammaStar a) ha hexp
  have hle := gaborQuadrupole_le_of_phase_coherent ha hs hcoh
  have hπa : 0 < Real.pi / a := div_pos Real.pi_pos ha
  have hparen :
      gaborAmpPlus a (gaborIsolationOmega sigmaStar gammaStar a)
          sigma' gamma' +
        2 * gaborAmpCross a (gaborIsolationOmega sigmaStar gammaStar a)
          sigma' gamma' -
        Real.cos gaborKappa *
          gaborAmpMinus a (gaborIsolationOmega sigmaStar gammaStar a)
            sigma' gamma' < 0 := by
    linarith [hcombo]
  exact hle.trans_lt (mul_neg_of_pos_of_neg hπa hparen)

/-! ## Piece 3: remainder smallness and assembly -/

theorem gaborEta_ge_lock {sigma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hlock : a ≤ gaborALock sigma) :
    Real.exp (-(Real.pi ^ 2 / 1024)) ≤ gaborEtaTune sigma a := by
  unfold gaborEtaTune
  have hden : 0 < 2 * sigma ^ 2 :=
    mul_pos (by norm_num) (sq_pos_of_pos hs)
  have hlock' : a ≤ sigma ^ 2 / 512 := by
    have : gaborALock sigma = (sigma ^ 2 / 64) / 8 := gaborALock_eq sigma
    rw [this] at hlock
    linarith [hlock]
  have hfrac : Real.pi ^ 2 * a / (2 * sigma ^ 2) ≤ Real.pi ^ 2 / 1024 := by
    have ha512 : a * 512 ≤ sigma ^ 2 := by
      rw [le_div_iff₀ (by norm_num : (0 : ℝ) < 512)] at hlock'
      exact hlock'
    have : a / (2 * sigma ^ 2) ≤ 1 / 1024 := by
      have : 1024 * a ≤ 2 * sigma ^ 2 := by linarith [ha512]
      exact (div_le_iff₀ hden).mpr (by linarith)
    have hπ : 0 ≤ Real.pi ^ 2 := sq_nonneg _
    have := mul_le_mul_of_nonneg_left this hπ
    convert this using 1 <;> field_simp [ne_of_gt hden, ne_of_gt hs]
  refine Real.exp_le_exp.mpr ?_
  have : -(Real.pi ^ 2 / 1024) ≤ -(Real.pi ^ 2 * a / (2 * sigma ^ 2)) :=
    neg_le_neg hfrac
  convert this using 1
  ring

theorem gaborEta_gt_nine_tenths {sigma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hlock : a ≤ gaborALock sigma) :
    (9 / 10 : ℝ) < gaborEtaTune sigma a := by
  have hη := gaborEta_ge_lock hs ha hlock
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
  have hlin : (9 / 10 : ℝ) < Real.exp (-(Real.pi ^ 2 / 1024)) := by
    have hle : 1 - Real.pi ^ 2 / 1024 ≤
        Real.exp (-(Real.pi ^ 2 / 1024)) := by
      have := Real.add_one_le_exp (-(Real.pi ^ 2 / 1024))
      linarith [this]
    have : (9 / 10 : ℝ) < 1 - Real.pi ^ 2 / 1024 := by linarith [hx]
    exact this.trans_le hle
  exact hlin.trans_le hη

theorem gaborIsolationEpsilon_sq_of_small {a : ℝ}
    (ha : 0 < a) (hle : a ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborIsolationEpsilon a ^ 2 / (2 * a) =
      Real.log (1 / a) := by
  have hmax := isolation_log_arg_eq ha hle
  have hlognn : (1 : ℝ) ≤ max (1 / a) (4 * (gaborKBin : ℝ)) :=
    le_trans (by norm_num : (1 : ℝ) ≤ 172)
      (by rw [← gaborKBin_four]; exact le_max_right _ _)
  have hsq : gaborIsolationEpsilon a ^ 2 =
      2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) := by
    unfold gaborIsolationEpsilon
    exact Real.sq_sqrt (mul_nonneg (mul_nonneg (by norm_num) ha.le)
      (Real.log_nonneg hlognn))
  rw [hsq, hmax]
  field_simp [ne_of_gt (mul_pos (by norm_num : (0 : ℝ) < 2) ha)]

theorem gaborTFar_of_small {a : ℝ}
    (ha : 0 < a) (hle : a ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborTFar a =
      (gaborKBin : ℝ) *
        (4 * a + (thetaLobe a - 3)) := by
  unfold gaborTFar
  have hε := gaborIsolationEpsilon_sq_of_small ha hle
  have hexp : Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) = a := by
    rw [neg_div, hε, Real.exp_neg, Real.exp_log (one_div_pos.mpr ha)]
    exact inv_eq_of_mul_eq_one_left (by field_simp [ne_of_gt ha])
  rw [hexp]

/-- Loose plus/cross majorant used in the packing comparison. -/
noncomputable def gaborTPlusLoose (a omega : ℝ) : ℝ :=
  (gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
    (1 / (1 - Real.exp (-omega / a)) + 2 * thetaLobe a)

/-- The one remaining comparison: the honest score is at most the
host minus-lobe plus the loose plus/cross packing, the far packing,
and the online budget.  T_gap is already proved to vanish. -/
def GaborHonestWeilLeMajorant : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliant Z →
    Z.gammaDistinct →
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc ≤
      gaborEnhancement (gaborHostSigma Z hZ)
            (isolationShrinkOfConfig Z hZ).1 *
          (-gaborEtaTune (gaborHostSigma Z hZ)
              (isolationShrinkOfConfig Z hZ).1 *
            (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLoose (isolationShrinkOfConfig Z hZ).1
              (isolationShrinkOfConfig Z hZ).2 +
            gaborTFar (isolationShrinkOfConfig Z hZ).1) +
        gaborHonestOnlineBudget (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc

/-- Remainder budget used by the assembly: under the r569 cap the
plus/far/online terms are jointly smaller than `9/10`. -/
def GaborRemainderBudget : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    gaborTPlusLoose (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 +
      gaborTFar (isolationShrinkOfConfig Z hZ).1 +
      gaborHonestOnlineBudget (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc /
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 < (9 / 10 : ℝ)

theorem gabor_dominanceBound_of_pack_and_budget
    (hpack : GaborHonestWeilLeMajorant)
    (hbud : GaborRemainderBudget) :
    GaborDominanceBound := by
  intro Z hZ hinc hdist
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hm := gaborHostMult_pos Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hlock : a ≤ gaborALock σ :=
    (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_lock σ γ)
  have hη : (9 / 10 : ℝ) < gaborEtaTune σ a :=
    gaborEta_gt_nine_tenths hs ha hlock
  have hWle := hpack Z hZ hinc hdist
  have hR := hbud Z hZ
  have hm1 : (1 : ℝ) ≤ (gaborHostMult Z hZ : ℝ) := by
    exact_mod_cast Nat.succ_le_of_lt hm
  have hneg :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
        gaborTPlusLoose a omega + gaborTFar a +
        gaborHonestOnlineBudget a omega gaborCInc /
          gaborEnhancement σ a < 0 := by
    have hηm : (9 / 10 : ℝ) <
        gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) :=
      lt_of_lt_of_le hη (le_mul_of_one_le_right (Real.exp_pos _).le hm1)
    linarith [hR, hηm]
  have hform :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLoose a omega + gaborTFar a) +
        gaborHonestOnlineBudget a omega gaborCInc =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLoose a omega + gaborTFar a +
            gaborHonestOnlineBudget a omega gaborCInc /
              gaborEnhancement σ a) := by
    field_simp [ne_of_gt hE]
  have hRHS :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLoose a omega + gaborTFar a) +
        gaborHonestOnlineBudget a omega gaborCInc < 0 := by
    rw [hform]
    exact mul_neg_of_pos_of_neg hE hneg
  exact hWle.trans_lt hRHS

/-- Combined remaining input: packing + remainder budget.
Both are explicit finite-sum / elementary estimates; they are
kept named rather than `sorry`. -/
def GaborDominanceAssembly : Prop :=
  GaborHonestWeilLeMajorant ∧ GaborRemainderBudget

theorem gabor_dominanceBound_of_assembly
    (h : GaborDominanceAssembly) :
    GaborDominanceBound :=
  gabor_dominanceBound_of_pack_and_budget h.1 h.2

/-! ## r574 log-compliant majorants and assembly -/

/-- Arithmetico-geometric series `Σ_{n≥0} (n+3) r^n`. -/
noncomputable def gaborArithGeomMajorant (r : ℝ) : ℝ :=
  3 / (1 - r) + r / (1 - r) ^ 2

/-- Far-bin weighted tail: distance class `n+1` carries linear
weight `n+|ω|+8`. -/
noncomputable def gaborFarTailLog (a omega : ℝ) : ℝ :=
  ∑' n : ℕ, ((n : ℝ) + |omega| + 8) *
    Real.exp (-((n + 1 : ℕ) : ℝ) ^ 2 / (2 * a))

/-- `|k|+3`-weighted theta, absorbing `1+log(|k|+3) ≤ |k|+3`.
r575: identified with the ω=0 far tail plus a central 12, so
cross packing reuses the far-tail comparison. Conservative. -/
noncomputable def gaborThetaLobeLog (a : ℝ) : ℝ :=
  12 + 2 * gaborFarTailLog a 0

/-- Plus/cross packing against the counting-theorem occupancy.
The theta coefficient is 4 (r575, conservative) so the `|k|+3`
weighted cross sum fits after `1+log ≤ |k|+3`. -/
noncomputable def gaborTPlusLooseLog (a omega : ℝ) : ℝ :=
  (2 * zetaZerosInDiskCardBoundInner) *
    Real.exp (-omega ^ 2 / (2 * a)) *
      (gaborArithGeomMajorant (Real.exp (-omega / a)) +
        4 * gaborThetaLobeLog a)

/-- Far packing (r575, conservative linear central cap):
`4 · 2 C_inner · (|⌊ω⌋|+4) · e^{-ε²/2a}` plus the two-sided
`|k|+3` tail.  The log occupancy is absorbed by `1+log ≤ |k|+3`. -/
noncomputable def gaborTFarLog (a omega : ℝ) : ℝ :=
  4 * (2 * zetaZerosInDiskCardBoundInner) *
      ((|Int.floor omega| : ℝ) + 4) *
      Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) +
    (2 * zetaZerosInDiskCardBoundInner) * (2 * gaborFarTailLog a omega)

def GaborHonestWeilLeMajorantLog : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliantLog Z →
    Z.gammaDistinct →
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc ≤
      gaborEnhancement (gaborHostSigma Z hZ)
            (isolationShrinkOfConfig Z hZ).1 *
          (-gaborEtaTune (gaborHostSigma Z hZ)
              (isolationShrinkOfConfig Z hZ).1 *
            (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog (isolationShrinkOfConfig Z hZ).1
              (isolationShrinkOfConfig Z hZ).2 +
            gaborTFarLog (isolationShrinkOfConfig Z hZ).1
              (isolationShrinkOfConfig Z hZ).2) +
        gaborHonestOnlineBudget (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc

def GaborRemainderBudgetLog : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    gaborTPlusLooseLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 +
      gaborTFarLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 +
      gaborHonestOnlineBudget (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 gaborCInc /
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 < (9 / 10 : ℝ)

theorem gabor_dominanceBoundLog_of_pack_and_budget
    (hpack : GaborHonestWeilLeMajorantLog)
    (hbud : GaborRemainderBudgetLog) :
    GaborDominanceBoundLog := by
  intro Z hZ hinc hdist
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hm := gaborHostMult_pos Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hlock : a ≤ gaborALock σ :=
    (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_lock σ γ)
  have hη : (9 / 10 : ℝ) < gaborEtaTune σ a :=
    gaborEta_gt_nine_tenths hs ha hlock
  have hWle := hpack Z hZ hinc hdist
  have hR := hbud Z hZ
  have hm1 : (1 : ℝ) ≤ (gaborHostMult Z hZ : ℝ) := by
    exact_mod_cast Nat.succ_le_of_lt hm
  have hneg :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
        gaborTPlusLooseLog a omega + gaborTFarLog a omega +
        gaborHonestOnlineBudget a omega gaborCInc /
          gaborEnhancement σ a < 0 := by
    have hηm : (9 / 10 : ℝ) <
        gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) :=
      lt_of_lt_of_le hη (le_mul_of_one_le_right (Real.exp_pos _).le hm1)
    linarith [hR, hηm]
  have hform :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudget a omega gaborCInc =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega +
            gaborHonestOnlineBudget a omega gaborCInc /
              gaborEnhancement σ a) := by
    field_simp [ne_of_gt hE]
  have hRHS :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudget a omega gaborCInc < 0 := by
    rw [hform]
    exact mul_neg_of_pos_of_neg hE hneg
  exact hWle.trans_lt hRHS

def GaborDominanceAssemblyLog : Prop :=
  GaborHonestWeilLeMajorantLog ∧ GaborRemainderBudgetLog

theorem gabor_dominanceBoundLog_of_assembly
    (h : GaborDominanceAssemblyLog) :
    GaborDominanceBoundLog :=
  gabor_dominanceBoundLog_of_pack_and_budget h.1 h.2

#print axioms gaborTGap_eq_zero
#print axioms gaborHost_unique_gamma_of_isolated
#print axioms gaborTGap_eq_zero_of_isolated
#print axioms gabor_phase_coherent_cos_general
#print axioms gaborAmp_combo_lt
#print axioms gabor_host_quadrupole_neg
#print axioms gabor_phase_coherent_quadrupole_neg_of_exp
#print axioms gaborEta_gt_nine_tenths
#print axioms gaborTFar_of_small
#print axioms gabor_dominanceBound_of_assembly
#print axioms gabor_dominanceBound_of_pack_and_budget
#print axioms gabor_dominanceBoundLog_of_assembly
#print axioms gabor_dominanceBoundLog_of_pack_and_budget

end RH
