/-
RH/GaborDominanceLog2.lean -- r583 log-compatible remainder budget.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r582 packed `GaborHonestWeilLeMajorantLog2` and left the named
remainder `GaborRemainderBudgetLog2`:
    T₊_log + T_far_log + R_on_log / E < 9/10.
T₊_log and T_far_log are the r575 bounds.  The new term is
`R_on_log = max((1+log(|ω|+3))·R_on, gaborOnlineLogBudget)`.

Both branches of the `max` absorb against `E` under
`gaborOnlineSmallnessALog` (`online_exp_le_log`):
  (i) `(1+log(γ+3))/(γ+3) ≤ 2` kills the Path-A increment;
  (ii) the r583 closed ĥ-side form is linear-central plus the
       r575 far tail, then the same `1/(γ+3)` and `e^{-256}`.

`GaborDominanceBoundLog2` is a theorem via
`gabor_dominanceBoundLog2_of_pack_and_budget`.

r589: every nonempty multiplicity-weighted FD window is a
`GaborCanonicalConfig` meeting BoundLog2's increment / host / `γ>0`
hypotheses.  BoundLog2 then gives
`W_log(isolationShrink(window)) < (9/10 − η) · E < 0`, and the
lock form `W_log < (9/10 − exp(−π²/1024)) · E`.  The packet and
`E` depend on the window; the fraction is n-free.  Packet-fixed
`GaborTruncationUniformNeg` is not implied.
-/
import RH.GaborSpectralBridge

namespace RH

set_option maxHeartbeats 2000000

open scoped Classical
open Set Finset

lemma gaborHatThreeLobeConst_half_div_E {sigma a : ℝ} (ha : 0 < a) :
    gaborHatThreeLobeConst a (1 / 2) / gaborEnhancement sigma a =
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) := by
  unfold gaborHatThreeLobeConst gaborEnhancement
  have hσ : ((1 : ℝ) / 2 - 1 / 2) ^ 2 = 0 := by ring
  rw [hσ, zero_div, Real.exp_zero, mul_one]
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hπ0 : Real.pi ≠ 0 := Real.pi_pos.ne'
  have hexp0 : Real.exp (sigma ^ 2 / (2 * a)) ≠ 0 := (Real.exp_pos _).ne'
  have hexp : (Real.exp (sigma ^ 2 / (2 * a)))⁻¹ =
      Real.exp (-sigma ^ 2 / (2 * a)) := by
    rw [← Real.exp_neg, neg_div]
  have hstep :
      (Real.pi / (4 * a)) /
          (Real.pi / a * Real.exp (sigma ^ 2 / (2 * a))) =
        (1 / 4 : ℝ) * (Real.exp (sigma ^ 2 / (2 * a)))⁻¹ := by
    field_simp [ha0, hπ0, hexp0]
    try ring
  rw [hstep, hexp]

lemma gaborOnlineBracket_le_six {a omega : ℝ}
    (ha : 0 < a) (hω : 0 < omega)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hξ : Real.exp (-omega / a) < (1 / 2 : ℝ))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2)) :
    thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega ≤
      (6 : ℝ) := by
  have hΘ := thetaLobe_lt_four_of_bin ha hbin
  have hΘ3 := thetaLobe_ge_three ha
  have hηexp : Real.exp (-omega ^ 2 / (2 * a)) ≤ Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg h64
  have hleft := thetaLeftPos_of_small (a := a) (omega := omega) hω hξ
  have hleft_le : thetaLeftPos a omega ≤ (1 : ℝ) := by
    rw [hleft]
    have hden : (1 / 2 : ℝ) ≤ 1 - Real.exp (-omega / a) := by linarith [hξ.le]
    have h1 :
        Real.exp (-omega ^ 2 / (2 * a)) / (1 - Real.exp (-omega / a)) ≤
          Real.exp (-(64 : ℝ)) / (1 - Real.exp (-omega / a)) :=
      div_le_div_of_nonneg_right hηexp (by linarith [hξ.le])
    have h2 :
        Real.exp (-(64 : ℝ)) / (1 - Real.exp (-omega / a)) ≤
          Real.exp (-(64 : ℝ)) / (1 / 2 : ℝ) :=
      div_le_div_of_nonneg_left (Real.exp_pos _).le (by norm_num) hden
    have h3 : Real.exp (-(64 : ℝ)) / (1 / 2 : ℝ) = 2 * Real.exp (-(64 : ℝ)) := by
      field_simp
    have hfrac := h1.trans (h2.trans_eq h3)
    have htiny : 2 * Real.exp (-(64 : ℝ)) ≤ 1 :=
      (mul_exp_neg_sixty_four_le 2 (by norm_num)).trans (by norm_num)
    exact hfrac.trans htiny
  have hcross_le : 2 * thetaCrossPos a omega ≤ (1 : ℝ) := by
    unfold thetaCrossPos
    have hident :
        2 * (Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) / 2) =
          Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) := by ring
    rw [hident]
    have hmul : Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) ≤
        Real.exp (-(64 : ℝ)) * 3 :=
      mul_le_mul hηexp (by linarith [hΘ]) (by linarith [hΘ3]) (Real.exp_pos _).le
    have htiny : 3 * Real.exp (-(64 : ℝ)) ≤ 1 :=
      (mul_exp_neg_sixty_four_le 3 (by norm_num)).trans (by norm_num)
    exact hmul.trans (by linarith [htiny])
  linarith [hΘ.le, hleft_le, hcross_le]

lemma gaborLogRon_div_E_le_one_hundred {sigma gamma a omega : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a) (hω : 0 < omega)
    (hωle : omega ≤ gamma)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hξ : Real.exp (-omega / a) < (1 / 2 : ℝ))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hon : a ≤ gaborOnlineSmallnessALog sigma gamma) :
    (1 + Real.log (|omega| + 3)) *
        gaborHonestOnlineBudget a omega gaborCInc /
          gaborEnhancement sigma a ≤ (1 / 100 : ℝ) := by
  rw [mul_div_assoc, gaborHonestOnline_div_E ha]
  have hB := gaborOnlineBracket_le_six ha hω h64 hξ hbin
  have hexp := online_exp_le_log hs (by linarith [hg]) ha hon
  have hC : 0 < gaborCInc := gaborCInc_pos
  have habs : |omega| = omega := abs_of_nonneg hω.le
  have hlogω : 1 + Real.log (|omega| + 3) ≤ 1 + Real.log (gamma + 3) := by
    rw [habs]
    have hx : 0 < omega + 3 := by linarith
    have hle : omega + 3 ≤ gamma + 3 := by linarith [hωle]
    have := Real.log_le_log hx hle
    linarith
  have hlogγ : 0 ≤ 1 + Real.log (gamma + 3) := by
    have : 0 ≤ Real.log (gamma + 3) := Real.log_nonneg (by linarith)
    linarith
  have hlogω0 : 0 ≤ 1 + Real.log (|omega| + 3) := by
    have : 0 ≤ Real.log (|omega| + 3) :=
      Real.log_nonneg (by nlinarith [abs_nonneg omega])
    linarith
  have hprod :
      (1 + Real.log (|omega| + 3)) *
          (gaborCInc / 2 *
            (thetaLobe a + thetaLeftPos a omega +
              2 * thetaCrossPos a omega) *
            Real.exp (-sigma ^ 2 / (2 * a))) ≤
        6 * Real.exp (-256) := by
    have h1 :
        gaborCInc / 2 *
            (thetaLobe a + thetaLeftPos a omega +
              2 * thetaCrossPos a omega) ≤
          gaborCInc / 2 * 6 :=
      mul_le_mul_of_nonneg_left hB (div_nonneg hC.le (by norm_num))
    have hL0 : 0 ≤ thetaLeftPos a omega := by
      rw [thetaLeftPos_of_small (a := a) (omega := omega) hω hξ]
      exact div_nonneg (Real.exp_pos _).le
        (sub_nonneg.mpr (le_of_lt (lt_trans hξ (by norm_num : (1 / 2 : ℝ) < 1))))
    have hX0 : 0 ≤ 2 * thetaCrossPos a omega := by
      unfold thetaCrossPos
      have hΘ3 := thetaLobe_ge_three ha
      have h1 : 0 ≤ Real.exp (-omega ^ 2 / (2 * a)) := (Real.exp_pos _).le
      have h2 : 0 ≤ thetaLobe a - 1 := by linarith
      have : 0 ≤ Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) / 2 :=
        div_nonneg (mul_nonneg h1 h2) (by norm_num)
      linarith
    have hbrack0 :
        0 ≤ thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega :=
      add_nonneg (add_nonneg (le_trans (by norm_num : (0 : ℝ) ≤ 3)
        (thetaLobe_ge_three ha)) hL0) hX0
    have h1nn : 0 ≤
        gaborCInc / 2 *
          (thetaLobe a + thetaLeftPos a omega +
            2 * thetaCrossPos a omega) :=
      mul_nonneg (div_nonneg hC.le (by norm_num)) hbrack0
    have h2 :
        (1 + Real.log (|omega| + 3)) *
            (gaborCInc / 2 *
              (thetaLobe a + thetaLeftPos a omega +
                2 * thetaCrossPos a omega)) ≤
          (1 + Real.log (gamma + 3)) * (gaborCInc / 2 * 6) :=
      mul_le_mul hlogω h1 h1nn hlogγ
    have h2right : 0 ≤
        (1 + Real.log (gamma + 3)) * (gaborCInc / 2 * 6) :=
      mul_nonneg hlogγ (mul_nonneg (div_nonneg hC.le (by norm_num)) (by norm_num))
    have h3 := mul_le_mul h2 hexp (Real.exp_pos _).le h2right
    have hident :
        (1 + Real.log (gamma + 3)) * (gaborCInc / 2 * 6) *
            (Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3))) =
          3 * (gaborCInc / (gaborCInc + 1)) *
            ((1 + Real.log (gamma + 3)) / (gamma + 3)) *
            Real.exp (-256) := by
      have hden : (gaborCInc + 1) * (gamma + 3) ≠ 0 := by
        exact mul_ne_zero (by linarith : gaborCInc + 1 ≠ 0)
          (by linarith : gamma + 3 ≠ 0)
      field_simp [hden, ne_of_gt hC]
      try ring
    have hC1 : gaborCInc / (gaborCInc + 1) ≤ 1 :=
      (div_le_one₀ (by linarith : (0 : ℝ) < gaborCInc + 1)).mpr (by linarith)
    have hlog2 := one_add_log_div_self_le_two hg.le
    have hlog2nn : 0 ≤ (1 + Real.log (gamma + 3)) / (gamma + 3) :=
      div_nonneg hlogγ (by linarith)
    have h4 :
        3 * (gaborCInc / (gaborCInc + 1)) *
            ((1 + Real.log (gamma + 3)) / (gamma + 3)) ≤
          (6 : ℝ) := by
      have hmul : (gaborCInc / (gaborCInc + 1)) *
          ((1 + Real.log (gamma + 3)) / (gamma + 3)) ≤ (2 : ℝ) :=
        (mul_le_mul hC1 hlog2 hlog2nn (by norm_num : (0 : ℝ) ≤ 1)).trans_eq
          (by norm_num)
      have hassoc :
          3 * (gaborCInc / (gaborCInc + 1)) *
              ((1 + Real.log (gamma + 3)) / (gamma + 3)) =
            3 * ((gaborCInc / (gaborCInc + 1)) *
              ((1 + Real.log (gamma + 3)) / (gamma + 3))) := by
        ring
      rw [hassoc]
      nlinarith [hmul]
    have h5 :
        3 * (gaborCInc / (gaborCInc + 1)) *
            ((1 + Real.log (gamma + 3)) / (gamma + 3)) *
            Real.exp (-256) ≤ 6 * Real.exp (-256) :=
      mul_le_mul_of_nonneg_right h4 (Real.exp_pos _).le
    have hassoc :
        (1 + Real.log (|omega| + 3)) *
            (gaborCInc / 2 *
              (thetaLobe a + thetaLeftPos a omega +
                2 * thetaCrossPos a omega) *
              Real.exp (-sigma ^ 2 / (2 * a))) =
          (1 + Real.log (|omega| + 3)) *
              (gaborCInc / 2 *
                (thetaLobe a + thetaLeftPos a omega +
                  2 * thetaCrossPos a omega)) *
            Real.exp (-sigma ^ 2 / (2 * a)) := by
      ring
    exact hassoc.trans_le (h3.trans (hident.trans_le h5))
  have h256 : 6 * Real.exp (-256) ≤ 6 / (2 : ℝ) ^ 256 := by
    have := mul_le_mul_of_nonneg_left (exp_neg_nat_le_inv_two_pow 256)
      (by norm_num : (0 : ℝ) ≤ 6)
    have hident : 6 * (1 / (2 : ℝ) ^ 256) = 6 / (2 : ℝ) ^ 256 := by ring
    rwa [hident] at this
  have htiny : 6 / (2 : ℝ) ^ 256 ≤ (1 / 100 : ℝ) := by norm_num
  exact hprod.trans (h256.trans htiny)

lemma gaborLogThreeLobeClosed_nonneg (a omega : ℝ) :
    0 ≤ gaborLogThreeLobeClosed a omega := by
  unfold gaborLogThreeLobeClosed
  have hC : 0 ≤ (2 * zetaZerosInDiskCardBoundInner : ℝ) :=
    (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos).le
  have htail := gaborFarTailLog_nonneg (a := a) (omega := omega)
  have htail0 := gaborFarTailLog_nonneg (a := a) (omega := (0 : ℝ))
  positivity

lemma gaborOnlineLogBudget_div_E_le_one_hundred {sigma gamma a omega : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a) (hω : 0 < omega)
    (hωle : omega ≤ gamma)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hfar : a ≤ gaborFarSmallnessA gamma)
    (hon : a ≤ gaborOnlineSmallnessALog sigma gamma) :
    gaborOnlineLogBudget a omega / gaborEnhancement sigma a ≤
      (1 / 100 : ℝ) := by
  have hE : 0 < gaborEnhancement sigma a := gaborEnhancement_pos ha
  have hC : 0 < gaborCInc := gaborCInc_pos
  have hclosed0 := gaborLogThreeLobeClosed_nonneg a omega
  have hChat0 : 0 ≤ gaborHatThreeLobeConst a (1 / 2) :=
    gaborHatThreeLobeConst_nonneg a (1 / 2) ha
  have hratio := gaborHatThreeLobeConst_half_div_E (sigma := sigma) ha
  have hexp := online_exp_le_log hs (by linarith [hg]) ha hon
  have habs : |omega| = omega := abs_of_nonneg hω.le
  have hηexp : Real.exp (-omega ^ 2 / (2 * a)) ≤ Real.exp (-(64 : ℝ)) := by
    refine Real.exp_le_exp.mpr ?_
    rw [neg_div]
    exact neg_le_neg h64
  have h64bin := inv_two_a_ge_sixty_four ha hbin
  have hξfar : Real.exp (-(1 : ℝ) / (2 * a)) ≤ (1 / 2 : ℝ) :=
    (Real.exp_le_exp.mpr (by
      rw [neg_div]; exact neg_le_neg h64bin)).trans
      (exp_neg_sixty_four_le.trans (by norm_num))
  have htail0geom := gaborFarTailLog_le_geom (omega := (0 : ℝ)) ha hξfar
  have htailω :=
    gaborCInc_two_farTail_le_one_two_hundred ha hg hω hωle hbin hfar
  have hident :
      gaborOnlineLogBudget a omega / gaborEnhancement sigma a =
        (gaborHatThreeLobeConst a (1 / 2) / gaborEnhancement sigma a) *
          gaborLogThreeLobeClosed a omega := by
    unfold gaborOnlineLogBudget
    field_simp [ne_of_gt hE]
  rw [hident, hratio]
  have hCinc : (2 * zetaZerosInDiskCardBoundInner : ℝ) = gaborCInc := rfl
  have htail0le : 12 + 2 * gaborFarTailLog a 0 ≤ (30 : ℝ) := by
    have hle : gaborFarTailLog a 0 ≤
        2 * Real.exp (-(1 : ℝ) / (2 * a)) * (|0| + 9) := htail0geom
    have habs0 : |(0 : ℝ)| + 9 = (9 : ℝ) := by simp
    rw [habs0] at hle
    have h2 : 2 * gaborFarTailLog a 0 ≤
        36 * Real.exp (-(1 : ℝ) / (2 * a)) := by
      have := mul_le_mul_of_nonneg_left hle (by norm_num : (0 : ℝ) ≤ 2)
      nlinarith [this]
    have hexp64 : Real.exp (-(1 : ℝ) / (2 * a)) ≤ Real.exp (-(64 : ℝ)) :=
      Real.exp_le_exp.mpr (by rw [neg_div]; exact neg_le_neg h64bin)
    have htiny : 36 * Real.exp (-(64 : ℝ)) ≤ (18 : ℝ) :=
      (mul_exp_neg_sixty_four_le 36 (by norm_num)).trans (by norm_num)
    linarith [h2, hexp64, htiny]
  have hClosed :
      gaborLogThreeLobeClosed a omega ≤
        gaborCInc * (6 * (gamma + 5)) + (1 / 100 : ℝ) +
          60 * gaborCInc * Real.exp (-(64 : ℝ)) := by
    unfold gaborLogThreeLobeClosed
    rw [hCinc]
    have hω5 : |omega| + 5 ≤ gamma + 5 := by linarith [habs, hωle]
    have hlin : gaborCInc * (6 * (|omega| + 5)) ≤
        gaborCInc * (6 * (gamma + 5)) :=
      mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_left hω5 (by norm_num)) hC.le
    have hT : gaborCInc * (4 * gaborFarTailLog a omega) ≤ (1 / 100 : ℝ) := by
      have : gaborCInc * (2 * gaborFarTailLog a omega) ≤ (1 / 200 : ℝ) := by
        simpa [gaborCInc] using htailω
      linarith [gaborFarTailLog_nonneg (a := a) (omega := omega)]
    have hX : gaborCInc *
        (2 * Real.exp (-omega ^ 2 / (2 * a)) *
          (12 + 2 * gaborFarTailLog a 0)) ≤
        60 * gaborCInc * Real.exp (-(64 : ℝ)) := by
      have h1 : 2 * Real.exp (-omega ^ 2 / (2 * a)) *
          (12 + 2 * gaborFarTailLog a 0) ≤
            2 * Real.exp (-(64 : ℝ)) * 30 :=
        mul_le_mul (mul_le_mul_of_nonneg_left hηexp (by norm_num))
          htail0le (by
            have := gaborFarTailLog_nonneg (a := a) (omega := (0 : ℝ))
            linarith) (by positivity)
      have h2 : 2 * Real.exp (-(64 : ℝ)) * 30 =
          60 * Real.exp (-(64 : ℝ)) := by ring
      rw [h2] at h1
      have := mul_le_mul_of_nonneg_left h1 hC.le
      convert this using 1
      ring
    have hsum :
        gaborCInc *
            (6 * (|omega| + 5) + 4 * gaborFarTailLog a omega +
              2 * Real.exp (-omega ^ 2 / (2 * a)) *
                (12 + 2 * gaborFarTailLog a 0)) =
          gaborCInc * (6 * (|omega| + 5)) +
            gaborCInc * (4 * gaborFarTailLog a omega) +
            gaborCInc * (2 * Real.exp (-omega ^ 2 / (2 * a)) *
              (12 + 2 * gaborFarTailLog a 0)) := by
      ring
    rw [hsum]
    linarith [hlin, hT, hX]
  have hmul :
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
          gaborLogThreeLobeClosed a omega ≤
        (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
          (gaborCInc * (6 * (gamma + 5)) + (1 / 100 : ℝ) +
            60 * gaborCInc * Real.exp (-(64 : ℝ))) :=
    mul_le_mul_of_nonneg_left hClosed (by positivity)
  have hA :
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
          (gaborCInc * (6 * (gamma + 5))) ≤ (3 / 1000 : ℝ) := by
    have hexp' :
        (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
            (gaborCInc * (6 * (gamma + 5))) ≤
          (1 / 4 : ℝ) *
            (Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3))) *
            (gaborCInc * (6 * (gamma + 5))) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hexp (by norm_num)) (by positivity)
    have hidentA :
        (1 / 4 : ℝ) *
            (Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3))) *
            (gaborCInc * (6 * (gamma + 5))) =
          (3 / 2 : ℝ) * (gaborCInc / (gaborCInc + 1)) *
            ((gamma + 5) / (gamma + 3)) * Real.exp (-256) := by
      have hden : (gaborCInc + 1) * (gamma + 3) ≠ 0 := by positivity
      field_simp [hden, ne_of_gt hC]
      ring
    have hC1 : gaborCInc / (gaborCInc + 1) ≤ 1 :=
      (div_le_one₀ (by linarith : (0 : ℝ) < gaborCInc + 1)).mpr (by linarith)
    have hγ2 := add_five_div_add_three_le_two hg.le
    have hγ2nn : 0 ≤ (gamma + 5) / (gamma + 3) :=
      div_nonneg (by linarith) (by linarith)
    have hprod : (gaborCInc / (gaborCInc + 1)) *
        ((gamma + 5) / (gamma + 3)) ≤ 2 :=
      (mul_le_mul hC1 hγ2 hγ2nn (by positivity)).trans_eq (by norm_num)
    have h32 : (3 / 2 : ℝ) * (gaborCInc / (gaborCInc + 1)) *
        ((gamma + 5) / (gamma + 3)) ≤ 3 := by
      have hassoc : (3 / 2 : ℝ) * (gaborCInc / (gaborCInc + 1)) *
          ((gamma + 5) / (gamma + 3)) =
          (3 / 2 : ℝ) * ((gaborCInc / (gaborCInc + 1)) *
            ((gamma + 5) / (gamma + 3))) := by ring
      rw [hassoc]
      have := mul_le_mul_of_nonneg_left hprod
        (by norm_num : (0 : ℝ) ≤ 3 / 2)
      linarith
    have h2 :
        (3 / 2 : ℝ) * (gaborCInc / (gaborCInc + 1)) *
            ((gamma + 5) / (gamma + 3)) * Real.exp (-256) ≤
          3 * Real.exp (-256) :=
      mul_le_mul_of_nonneg_right h32 (Real.exp_pos _).le
    have h256 : 3 * Real.exp (-256) ≤ 3 / (2 : ℝ) ^ 256 :=
      (mul_le_mul_of_nonneg_left (exp_neg_nat_le_inv_two_pow 256)
        (by norm_num : (0 : ℝ) ≤ 3)).trans_eq (by ring)
    have htiny : 3 / (2 : ℝ) ^ 256 ≤ (3 / 1000 : ℝ) := by norm_num
    exact hexp'.trans (hidentA.trans_le (h2.trans (h256.trans htiny)))
  have hT :
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) * (1 / 100 : ℝ) ≤
        (1 / 400 : ℝ) := by
    have hexp1 : Real.exp (-sigma ^ 2 / (2 * a)) ≤ 1 :=
      Real.exp_le_one_iff.mpr
        (div_nonpos_of_nonpos_of_nonneg
          (neg_nonpos.mpr (sq_nonneg _)) (mul_nonneg (by norm_num) ha.le))
    have : (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) * (1 / 100 : ℝ) ≤
        (1 / 4 : ℝ) * 1 * (1 / 100 : ℝ) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hexp1 (by norm_num)) (by norm_num)
    exact this.trans (by norm_num)
  have hX :
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
          (60 * gaborCInc * Real.exp (-(64 : ℝ))) ≤ (1 / 1000 : ℝ) := by
    have hexp' :
        (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
            (60 * gaborCInc * Real.exp (-(64 : ℝ))) ≤
          (1 / 4 : ℝ) *
            (Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3))) *
            (60 * gaborCInc * Real.exp (-(64 : ℝ))) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hexp (by norm_num)) (by positivity)
    have hidentX :
        (1 / 4 : ℝ) *
            (Real.exp (-256) / ((gaborCInc + 1) * (gamma + 3))) *
            (60 * gaborCInc * Real.exp (-(64 : ℝ))) =
          15 * (gaborCInc / ((gaborCInc + 1) * (gamma + 3))) *
            Real.exp (-(64 : ℝ)) * Real.exp (-256) := by
      have hden : (gaborCInc + 1) * (gamma + 3) ≠ 0 := by positivity
      field_simp [hden, ne_of_gt hC]
      ring
    have hCγ : gaborCInc / ((gaborCInc + 1) * (gamma + 3)) ≤ 1 := by
      have h1 : gaborCInc / (gaborCInc + 1) ≤ 1 :=
        (div_le_one₀ (by linarith : (0 : ℝ) < gaborCInc + 1)).mpr (by linarith)
      have h2 : (1 : ℝ) / (gamma + 3) ≤ 1 :=
        (div_le_one₀ (by linarith : (0 : ℝ) < gamma + 3)).mpr
          (by linarith [hg] : (1 : ℝ) ≤ gamma + 3)
      have : gaborCInc / ((gaborCInc + 1) * (gamma + 3)) =
          (gaborCInc / (gaborCInc + 1)) * (1 / (gamma + 3)) := by
        field_simp
      rw [this]
      exact (mul_le_mul h1 h2 (div_nonneg (by norm_num) (by linarith))
        (by norm_num : (0 : ℝ) ≤ 1)).trans_eq (by norm_num)
    have hfin :
        15 * (gaborCInc / ((gaborCInc + 1) * (gamma + 3))) *
            Real.exp (-(64 : ℝ)) * Real.exp (-256) ≤
          15 * Real.exp (-(64 : ℝ)) * Real.exp (-256) := by
      have hnn : 0 ≤ Real.exp (-(64 : ℝ)) * Real.exp (-256) :=
        mul_nonneg (Real.exp_pos _).le (Real.exp_pos _).le
      have hL :
          15 * (gaborCInc / ((gaborCInc + 1) * (gamma + 3))) *
              Real.exp (-(64 : ℝ)) * Real.exp (-256) =
            (15 * (gaborCInc / ((gaborCInc + 1) * (gamma + 3)))) *
              (Real.exp (-(64 : ℝ)) * Real.exp (-256)) := by
        ring
      have hR : 15 * Real.exp (-(64 : ℝ)) * Real.exp (-256) =
          (15 * (1 : ℝ)) *
            (Real.exp (-(64 : ℝ)) * Real.exp (-256)) := by
        ring
      rw [hL, hR]
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hCγ (by norm_num)) hnn
    have h256 : 15 * Real.exp (-(64 : ℝ)) * Real.exp (-256) ≤
        15 / ((2 : ℝ) ^ 64 * (2 : ℝ) ^ 256) := by
      have h64n : 0 ≤ 15 * (1 / (2 : ℝ) ^ 64) :=
        mul_nonneg (by norm_num) (div_nonneg (by norm_num)
          (pow_nonneg (by norm_num : (0 : ℝ) ≤ 2) 64))
      have h1 :=
        mul_le_mul
          (mul_le_mul_of_nonneg_left exp_neg_sixty_four_le
            (by norm_num : (0 : ℝ) ≤ 15))
          (exp_neg_nat_le_inv_two_pow 256) (Real.exp_pos _).le h64n
      have hid : 15 * (1 / (2 : ℝ) ^ 64) * (1 / (2 : ℝ) ^ 256) =
          15 / ((2 : ℝ) ^ 64 * (2 : ℝ) ^ 256) := by field_simp
      exact h1.trans_eq hid
    have htiny : 15 / ((2 : ℝ) ^ 64 * (2 : ℝ) ^ 256) ≤ (1 / 1000 : ℝ) := by
      norm_num
    exact hexp'.trans (hidentX.trans_le (hfin.trans (h256.trans htiny)))
  have hsum :
      (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
          (gaborCInc * (6 * (gamma + 5)) + (1 / 100 : ℝ) +
            60 * gaborCInc * Real.exp (-(64 : ℝ))) ≤
        (3 / 1000 : ℝ) + (1 / 400 : ℝ) + (1 / 1000 : ℝ) := by
    have hdist :
        (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
            (gaborCInc * (6 * (gamma + 5)) + (1 / 100 : ℝ) +
              60 * gaborCInc * Real.exp (-(64 : ℝ))) =
          (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
              (gaborCInc * (6 * (gamma + 5))) +
            (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) * (1 / 100 : ℝ) +
            (1 / 4 : ℝ) * Real.exp (-sigma ^ 2 / (2 * a)) *
              (60 * gaborCInc * Real.exp (-(64 : ℝ))) := by
      ring
    rw [hdist]
    linarith [hA, hT, hX]
  have htiny : (3 / 1000 : ℝ) + (1 / 400 : ℝ) + (1 / 1000 : ℝ) ≤
      (1 / 100 : ℝ) := by norm_num
  exact hmul.trans (hsum.trans htiny)

lemma gaborHonestOnlineBudgetLog_div_E_le_one_hundred
    {sigma gamma a omega : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 < a) (hω : 0 < omega)
    (hωle : omega ≤ gamma)
    (h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a))
    (hξ : Real.exp (-omega / a) < (1 / 2 : ℝ))
    (hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2))
    (hfar : a ≤ gaborFarSmallnessA gamma)
    (hon : a ≤ gaborOnlineSmallnessALog sigma gamma) :
    gaborHonestOnlineBudgetLog a omega gaborCInc /
        gaborEnhancement sigma a ≤ (1 / 100 : ℝ) := by
  have hE : 0 < gaborEnhancement sigma a := gaborEnhancement_pos ha
  have h1 :=
    gaborLogRon_div_E_le_one_hundred hs hg ha hω hωle h64 hξ hbin hon
  have h2 :=
    gaborOnlineLogBudget_div_E_le_one_hundred hs hg ha hω hωle h64 hbin
      hfar hon
  have hA :
      (1 + Real.log (|omega| + 3)) *
          gaborHonestOnlineBudget a omega gaborCInc ≤
        (1 / 100 : ℝ) * gaborEnhancement sigma a :=
    (div_le_iff₀ hE).mp h1
  have hB :
      gaborOnlineLogBudget a omega ≤
        (1 / 100 : ℝ) * gaborEnhancement sigma a :=
    (div_le_iff₀ hE).mp h2
  have hmax :
      gaborHonestOnlineBudgetLog a omega gaborCInc ≤
        (1 / 100 : ℝ) * gaborEnhancement sigma a :=
    max_le hA hB
  exact (div_le_iff₀ hE).mpr hmax

theorem gaborRemainderBudgetLog2_holds : GaborRemainderBudgetLog2 := by
  intro Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hω := isolationShrinkOfConfig_omega_pos Z hZ
  have hs := gaborHostSigma_pos Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hωcap := isolationShrinkOfConfig_le_omegaCap Z hZ
  have hγsq := isolationShrinkOfConfig_le_gamma_sq Z hZ
  have hbin := isolationShrinkOfConfig_le_binSq Z hZ
  have hon := isolationShrinkOfConfig_le_onlineLog Z hZ
  have hfour := isolationShrinkOfConfig_le_inv_four_bin Z hZ
  have hplus := isolationShrinkOfConfig_le_plus Z hZ
  have hfar := isolationShrinkOfConfig_le_far Z hZ
  have hωeq : omega = gaborIsolationOmega σ γ a :=
    isolationShrinkOfConfig_omega_eq Z hZ
  have hωle := isolationShrinkOfConfig_omega_le_gamma Z hZ
  have h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a) := by
    rw [hωeq]
    exact omega_sq_div_two_a_ge_sixty_four hs hg ha hωcap hγsq
  have hξlt : Real.exp (-omega / a) < (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_lt_half hs hg ha hωcap hγsq hbin
  have hTplus :=
    gaborTPlusLooseLog_le_one_hundred hs hg ha hω hωeq hωcap hγsq hbin hplus
  have hTfar :=
    gaborTFarLog_le_one_fifty ha hg hω hωle hfour hbin hfar
  have hRon :=
    gaborHonestOnlineBudgetLog_div_E_le_one_hundred hs hg ha hω hωle
      h64 hξlt hbin hfar hon
  linarith [hTplus, hTfar, hRon,
    (by norm_num : (1 / 100 : ℝ) + (1 / 50 : ℝ) + (1 / 100 : ℝ) < (9 / 10 : ℝ))]

theorem gabor_dominanceBoundLog2_holds : GaborDominanceBoundLog2 :=
  gabor_dominanceBoundLog2_of_pack_and_budget
    gaborHonestWeilLeMajorantLog2_holds gaborRemainderBudgetLog2_holds

/-! ## r589: window negativity from BoundLog2 -/

lemma thetaLeftPos_nonneg {a omega : ℝ} (ha : 0 < a) :
    0 ≤ thetaLeftPos a omega := by
  unfold thetaLeftPos
  split_ifs with h
  · linarith [thetaLobe_ge_three ha]
  · have hexp : Real.exp (-omega / a) < (1 / 2 : ℝ) :=
      lt_of_not_ge fun hle => h (Or.inr hle)
    have hden : 0 < 1 - Real.exp (-omega / a) := by
      linarith [hexp, (by norm_num : (1 / 2 : ℝ) < 1)]
    exact div_nonneg (Real.exp_pos _).le hden.le

lemma thetaCrossPos_nonneg {a omega : ℝ} (ha : 0 < a) :
    0 ≤ thetaCrossPos a omega := by
  unfold thetaCrossPos
  have : 0 ≤ thetaLobe a - 1 := by linarith [thetaLobe_ge_three ha]
  exact div_nonneg (mul_nonneg (Real.exp_pos _).le this) (by norm_num)

lemma gaborSCert_nonneg {a omega : ℝ} (ha : 0 < a) :
    0 ≤ gaborSCert a omega := by
  unfold gaborSCert
  have hπ : 0 ≤ Real.pi / (4 * a) :=
    div_nonneg Real.pi_pos.le (mul_pos (by norm_num) ha).le
  have hsum :
      0 ≤ thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega := by
    linarith [thetaLobe_ge_three ha, thetaLeftPos_nonneg (omega := omega) ha,
      thetaCrossPos_nonneg (omega := omega) ha]
  exact mul_nonneg hπ hsum

lemma gaborHonestOnlineBudget_nonneg {a omega Cinc : ℝ}
    (ha : 0 < a) (hC : 0 ≤ Cinc) :
    0 ≤ gaborHonestOnlineBudget a omega Cinc :=
  mul_nonneg (mul_nonneg (by norm_num) hC) (gaborSCert_nonneg ha)

/-- Proxy remainder `R_on` is absorbed by `R_on_log` (`1+log ≥ 1`).
Hence `W_log < 0` implies the historical `W_honest < 0`. -/
theorem gaborHonestWeil_le_honestWeilLog
    (a omega : ℝ) (Z : GaborCanonicalConfig) (ha : 0 < a) :
    gaborHonestWeil a omega Z gaborCInc ≤
      gaborHonestWeilLog a omega Z gaborCInc := by
  have hR : 0 ≤ gaborHonestOnlineBudget a omega gaborCInc :=
    gaborHonestOnlineBudget_nonneg ha gaborCInc_pos.le
  have hlog : (1 : ℝ) ≤ 1 + Real.log (|omega| + 3) := by
    have : (1 : ℝ) ≤ |omega| + 3 := by nlinarith [abs_nonneg omega]
    have : 0 ≤ Real.log (|omega| + 3) := Real.log_nonneg this
    linarith
  have hmul :
      gaborHonestOnlineBudget a omega gaborCInc ≤
        (1 + Real.log (|omega| + 3)) *
          gaborHonestOnlineBudget a omega gaborCInc :=
    le_mul_of_one_le_left hR hlog
  have hmax :
      gaborHonestOnlineBudget a omega gaborCInc ≤
        gaborHonestOnlineBudgetLog a omega gaborCInc :=
    le_max_of_le_left hmul
  unfold gaborHonestWeil gaborHonestWeilLog
  linarith

/-- Strongest n-free quantitative form of BoundLog2:
`W_log < (9/10 − η(σ,a)) · E(σ,a)`.  The factor is negative under
the lock (`η > 9/10`); `E` depends on the catalog's host and
isolation width. -/
theorem gaborHonestWeilLog_lt_etaMargin
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct) :
    gaborHonestWeilLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1) *
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 := by
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hm := gaborHostMult_pos Z hZ
  set a := (isolationShrinkOfConfig Z hZ).1
  set omega := (isolationShrinkOfConfig Z hZ).2
  set σ := gaborHostSigma Z hZ
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hlock : a ≤ gaborALock σ :=
    (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_lock σ (gaborHostGamma Z hZ))
  have hη : (9 / 10 : ℝ) < gaborEtaTune σ a :=
    gaborEta_gt_nine_tenths hs ha hlock
  have hWle := gaborHonestWeilLeMajorantLog2_holds Z hZ hinc hdist
  have hR := gaborRemainderBudgetLog2_holds Z hZ
  have hm1 : (1 : ℝ) ≤ (gaborHostMult Z hZ : ℝ) := by
    exact_mod_cast Nat.succ_le_of_lt hm
  have hform :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega +
            gaborHonestOnlineBudgetLog a omega gaborCInc /
              gaborEnhancement σ a) := by
    field_simp [ne_of_gt hE]
  have hinner :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
          gaborTPlusLooseLog a omega + gaborTFarLog a omega +
          gaborHonestOnlineBudgetLog a omega gaborCInc /
            gaborEnhancement σ a <
        -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ) := by
    linarith [hR]
  have hinner' :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ) ≤
        (9 / 10 : ℝ) - gaborEtaTune σ a := by
    have hmη : gaborEtaTune σ a ≤
        gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) :=
      le_mul_of_one_le_right (Real.exp_pos _).le hm1
    linarith [hmη]
  have hRHS :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune σ a) * gaborEnhancement σ a := by
    rw [hform]
    have hmul :=
      mul_lt_mul_of_pos_left hinner hE
    have hmul' :
        gaborEnhancement σ a *
            (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ)) ≤
          gaborEnhancement σ a * ((9 / 10 : ℝ) - gaborEtaTune σ a) :=
      mul_le_mul_of_nonneg_left hinner' hE.le
    have hcomm :
        ((9 / 10 : ℝ) - gaborEtaTune σ a) * gaborEnhancement σ a =
          gaborEnhancement σ a * ((9 / 10 : ℝ) - gaborEtaTune σ a) :=
      mul_comm _ _
    exact (hmul.trans_le hmul').trans_eq hcomm.symm
  exact hWle.trans_lt (by simpa [a, omega, σ] using hRHS)

/-- Lock-uniform fraction: `η ≥ exp(−π²/1024)` under `a ≤ a_lock`,
so `W_log < (9/10 − exp(−π²/1024)) · E`.  The numerical factor is
independent of the catalog and of the window height; only `E`
depends on `(σ,a)`. -/
theorem gaborHonestWeilLog_lt_lockMargin
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct) :
    gaborHonestWeilLog (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc <
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 := by
  have hs := gaborHostSigma_pos Z hZ
  have ha := isolationShrinkOfConfig_a_pos Z hZ
  have hlock : (isolationShrinkOfConfig Z hZ).1 ≤ gaborALock (gaborHostSigma Z hZ) :=
    (isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_lock (gaborHostSigma Z hZ) (gaborHostGamma Z hZ))
  have hηlock :
      Real.exp (-(Real.pi ^ 2 / 1024)) ≤
        gaborEtaTune (gaborHostSigma Z hZ) (isolationShrinkOfConfig Z hZ).1 :=
    gaborEta_ge_lock hs ha hlock
  have hE : 0 <
      gaborEnhancement (gaborHostSigma Z hZ) (isolationShrinkOfConfig Z hZ).1 :=
    gaborEnhancement_pos ha
  have hη := gaborHonestWeilLog_lt_etaMargin Z hZ hinc hdist
  have hfac :
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1) *
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 ≤
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma Z hZ)
          (isolationShrinkOfConfig Z hZ).1 :=
    mul_le_mul_of_nonneg_right (by linarith [hηlock]) hE.le
  exact hη.trans_le hfac

/-! ## r597: BoundLog2 packing + budget at free admissible width

All remainder-budget lemmas already take free `a` with smallness
caps.  Those caps are monotone: `a ≤ isolationShrink` inherits
every r569 smallness (`gaborSmallnessA_le_*`).

ω-dependence is not monotone — `ω(a) = γ★ − πa/σ★` moves toward
γ★ as a shrinks, so `|⌊ω⌋|` and `1+log(|ω|+3)` can grow.  The
live lemmas bound those terms by γ★-caps (`omega ≤ gamma`),
which hold for every `a > 0`.  Peak emptiness retunes with
`ω(a)` and uses the monotone radius constraint.  No extra
hypothesis is needed on the lock-margin Prop. -/

theorem gaborHonestWeilLeMajorantLog2_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborHonestWeilLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) Z gaborCInc ≤
      gaborEnhancement (gaborHostSigma Z hZ) a *
          (-gaborEtaTune (gaborHostSigma Z hZ) a *
            (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a
              (gaborIsolationOmega (gaborHostSigma Z hZ)
                (gaborHostGamma Z hZ) a) +
            gaborTFarLog a
              (gaborIsolationOmega (gaborHostSigma Z hZ)
                (gaborHostGamma Z hZ) a)) +
        gaborHonestOnlineBudgetLog a
          (gaborIsolationOmega (gaborHostSigma Z hZ)
            (gaborHostGamma Z hZ) a) gaborCInc := by
  have hW := gaborHonestWeilLeMajorantLog_of_le Z hZ hinc hdist ha hle
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set omega := gaborIsolationOmega σ γ a
  have hQ :
      Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) ≤
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) := by
    have hident :
        gaborHonestWeil a omega Z gaborCInc =
          Z.pts.sum (fun q =>
              (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
            gaborHonestOnlineBudget a omega gaborCInc :=
      rfl
    linarith [hW, hident]
  have hWlog :
      gaborHonestWeilLog a omega Z gaborCInc =
        Z.pts.sum (fun q =>
            (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
          gaborHonestOnlineBudgetLog a omega gaborCInc :=
    rfl
  have hQadd :
      Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
        gaborHonestOnlineBudgetLog a omega gaborCInc ≤
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc := by
    linarith [hQ]
  simpa [omega, σ] using hWlog.trans_le hQadd

theorem gaborRemainderBudgetLog2_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborTPlusLooseLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) +
      gaborTFarLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) +
      gaborHonestOnlineBudgetLog a
          (gaborIsolationOmega (gaborHostSigma Z hZ)
            (gaborHostGamma Z hZ) a) gaborCInc /
        gaborEnhancement (gaborHostSigma Z hZ) a < (9 / 10 : ℝ) := by
  set σ := gaborHostSigma Z hZ
  set γ := gaborHostGamma Z hZ
  set omega := gaborIsolationOmega σ γ a
  have hω : 0 < omega :=
    gaborIsolationOmega_pos (gaborHostSigma_pos Z hZ)
      (gaborHostGamma_pos Z hZ) ha.le
      (hle.trans (isolationShrinkOfConfig_le_omegaCap Z hZ))
  have hs := gaborHostSigma_pos Z hZ
  have hg := gaborHostGamma_pos Z hZ
  have hωcap : a ≤ gaborOmegaCap σ γ :=
    hle.trans (isolationShrinkOfConfig_le_omegaCap Z hZ)
  have hγsq : a ≤ γ ^ 2 / 512 :=
    hle.trans (isolationShrinkOfConfig_le_gamma_sq Z hZ)
  have hbin : a ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2) :=
    hle.trans (isolationShrinkOfConfig_le_binSq Z hZ)
  have hon : a ≤ gaborOnlineSmallnessALog σ γ :=
    hle.trans (isolationShrinkOfConfig_le_onlineLog Z hZ)
  have hfour : a ≤ 1 / (4 * (gaborKBin : ℝ)) :=
    hle.trans (isolationShrinkOfConfig_le_inv_four_bin Z hZ)
  have hplus : a ≤ gaborPlusSmallnessA γ :=
    hle.trans (isolationShrinkOfConfig_le_plus Z hZ)
  have hfar : a ≤ gaborFarSmallnessA γ :=
    hle.trans (isolationShrinkOfConfig_le_far Z hZ)
  have hωeq : omega = gaborIsolationOmega σ γ a := rfl
  have hωle : omega ≤ γ := by
    have hsub : 0 ≤ Real.pi * a / σ :=
      div_nonneg (mul_nonneg Real.pi_pos.le ha.le) hs.le
    have hdef : omega = γ - Real.pi * a / σ := rfl
    linarith [hdef, hsub]
  have h64 : (64 : ℝ) ≤ omega ^ 2 / (2 * a) := by
    rw [hωeq]
    exact omega_sq_div_two_a_ge_sixty_four hs hg ha hωcap hγsq
  have hξlt : Real.exp (-omega / a) < (1 / 2 : ℝ) := by
    rw [hωeq]
    exact exp_neg_omega_a_lt_half hs hg ha hωcap hγsq hbin
  have hTplus :=
    gaborTPlusLooseLog_le_one_hundred hs hg ha hω hωeq hωcap hγsq hbin hplus
  have hTfar :=
    gaborTFarLog_le_one_fifty ha hg hω hωle hfour hbin hfar
  have hRon :=
    gaborHonestOnlineBudgetLog_div_E_le_one_hundred hs hg ha hω hωle
      h64 hξlt hbin hfar hon
  linarith [hTplus, hTfar, hRon,
    (by norm_num : (1 / 100 : ℝ) + (1 / 50 : ℝ) + (1 / 100 : ℝ) < (9 / 10 : ℝ))]

theorem gaborHonestWeilLog_lt_etaMargin_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborHonestWeilLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) Z gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma Z hZ) a) *
        gaborEnhancement (gaborHostSigma Z hZ) a := by
  have hs := gaborHostSigma_pos Z hZ
  have hm := gaborHostMult_pos Z hZ
  set σ := gaborHostSigma Z hZ
  set omega := gaborIsolationOmega σ (gaborHostGamma Z hZ) a
  have hE : 0 < gaborEnhancement σ a := gaborEnhancement_pos ha
  have hlock : a ≤ gaborALock σ :=
    hle.trans (isolationShrinkOfConfig_le_lock Z hZ)
  have hη : (9 / 10 : ℝ) < gaborEtaTune σ a :=
    gaborEta_gt_nine_tenths hs ha hlock
  have hWle := gaborHonestWeilLeMajorantLog2_of_le Z hZ hinc hdist ha hle
  have hR := gaborRemainderBudgetLog2_of_le Z hZ ha hle
  have hm1 : (1 : ℝ) ≤ (gaborHostMult Z hZ : ℝ) := by
    exact_mod_cast Nat.succ_le_of_lt hm
  have hform :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc =
        gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega +
            gaborHonestOnlineBudgetLog a omega gaborCInc /
              gaborEnhancement σ a) := by
    field_simp [ne_of_gt hE]
  have hinner :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
          gaborTPlusLooseLog a omega + gaborTFarLog a omega +
          gaborHonestOnlineBudgetLog a omega gaborCInc /
            gaborEnhancement σ a <
        -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ) := by
    linarith [hR]
  have hinner' :
      -gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ) ≤
        (9 / 10 : ℝ) - gaborEtaTune σ a := by
    have hmη : gaborEtaTune σ a ≤
        gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) :=
      le_mul_of_one_le_right (Real.exp_pos _).le hm1
    linarith [hmη]
  have hRHS :
      gaborEnhancement σ a *
          (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) +
            gaborTPlusLooseLog a omega + gaborTFarLog a omega) +
        gaborHonestOnlineBudgetLog a omega gaborCInc <
      ((9 / 10 : ℝ) - gaborEtaTune σ a) * gaborEnhancement σ a := by
    rw [hform]
    have hmul := mul_lt_mul_of_pos_left hinner hE
    have hmul' :
        gaborEnhancement σ a *
            (-gaborEtaTune σ a * (gaborHostMult Z hZ : ℝ) + (9 / 10 : ℝ)) ≤
          gaborEnhancement σ a * ((9 / 10 : ℝ) - gaborEtaTune σ a) :=
      mul_le_mul_of_nonneg_left hinner' hE.le
    have hcomm :
        ((9 / 10 : ℝ) - gaborEtaTune σ a) * gaborEnhancement σ a =
          gaborEnhancement σ a * ((9 / 10 : ℝ) - gaborEtaTune σ a) :=
      mul_comm _ _
    exact (hmul.trans_le hmul').trans_eq hcomm.symm
  exact hWle.trans_lt (by simpa [omega, σ] using hRHS)

/-- Lock-uniform fraction at every `0 < a ≤ isolationShrink`.
`η ≥ exp(−π²/1024)` because `a ≤ shrink ≤ a_lock`. -/
theorem gaborHonestWeilLog_lt_lockMargin_of_le
    (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty)
    (hinc : GaborConfigIncrementCompliantLog Z)
    (hdist : Z.gammaDistinct)
    {a : ℝ} (ha : 0 < a)
    (hle : a ≤ (isolationShrinkOfConfig Z hZ).1) :
    gaborHonestWeilLog a
        (gaborIsolationOmega (gaborHostSigma Z hZ)
          (gaborHostGamma Z hZ) a) Z gaborCInc <
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma Z hZ) a := by
  have hs := gaborHostSigma_pos Z hZ
  have hlock : a ≤ gaborALock (gaborHostSigma Z hZ) :=
    hle.trans (isolationShrinkOfConfig_le_lock Z hZ)
  have hηlock :
      Real.exp (-(Real.pi ^ 2 / 1024)) ≤
        gaborEtaTune (gaborHostSigma Z hZ) a :=
    gaborEta_ge_lock hs ha hlock
  have hE : 0 < gaborEnhancement (gaborHostSigma Z hZ) a :=
    gaborEnhancement_pos ha
  have hη := gaborHonestWeilLog_lt_etaMargin_of_le Z hZ hinc hdist ha hle
  have hfac :
      ((9 / 10 : ℝ) - gaborEtaTune (gaborHostSigma Z hZ) a) *
        gaborEnhancement (gaborHostSigma Z hZ) a ≤
      ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
        gaborEnhancement (gaborHostSigma Z hZ) a :=
    mul_le_mul_of_nonneg_right (by linarith [hηlock]) hE.le
  exact hη.trans_le hfac

theorem gaborWeightedTruncationNegLog_holds :
    GaborWeightedTruncationNegLog := by
  intro T hZ hdist
  exact gabor_dominanceBoundLog2_holds (gaborWeightedTruncationConfig T) hZ
    (gaborWeightedTruncation_incrementCompliantLog T) hdist

theorem gaborWeightedTruncationNegLogQuant_holds :
    GaborWeightedTruncationNegLogQuant := by
  intro T hZ hdist
  exact gaborHonestWeilLog_lt_etaMargin (gaborWeightedTruncationConfig T) hZ
    (gaborWeightedTruncation_incrementCompliantLog T) hdist

/-- Window form of the lock-uniform fraction.  `δ` may not be
taken independent of the window: `E` depends on the host.  The
factor `9/10 − exp(−π²/1024)` does not. -/
theorem gaborWeightedTruncation_lockMargin
    (T : ℝ) (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty)
    (hdist : (gaborWeightedTruncationConfig T).gammaDistinct) :
    gaborHonestWeilLog
      (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
      (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
      (gaborWeightedTruncationConfig T) gaborCInc <
    ((9 / 10 : ℝ) - Real.exp (-(Real.pi ^ 2 / 1024))) *
      gaborEnhancement
        (gaborHostSigma (gaborWeightedTruncationConfig T) hZ)
        (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1 :=
  gaborHonestWeilLog_lt_lockMargin (gaborWeightedTruncationConfig T) hZ
    (gaborWeightedTruncation_incrementCompliantLog T) hdist

/-- `W_log < 0` on a nonempty increment-compliant isolated window
implies the historical `W_honest < 0` for the same isolation
packet (used by the named translation bridges). -/
theorem gaborWeightedTruncation_honestWeil_neg
    (T : ℝ) (hZ : (gaborWeightedTruncationConfig T).pts.Nonempty)
    (hdist : (gaborWeightedTruncationConfig T).gammaDistinct) :
    gaborHonestWeil
      (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).1
      (isolationShrinkOfConfig (gaborWeightedTruncationConfig T) hZ).2
      (gaborWeightedTruncationConfig T) gaborCInc < 0 := by
  have ha := isolationShrinkOfConfig_a_pos
    (gaborWeightedTruncationConfig T) hZ
  have hlog := gaborWeightedTruncationNegLog_holds T hZ hdist
  exact lt_of_le_of_lt
    (gaborHonestWeil_le_honestWeilLog _ _ _ ha) hlog

/-- Sorry-free logic: BoundLog2 plus the two named translation
bridges imply the live `∀`-zeros arithmetic inequality.  Same
shape as `gabor_dominanceLog_implies_separation`; the extra step
is `W ≤ W_log`.  The bridges stay hypotheses. -/
theorem gabor_dominanceLog2_implies_separation
    (hdom : GaborDominanceBoundLog2)
    (hhonest : GaborHonestNegImpliesIsolationArithmeticNeg)
    (hscale : GaborIsolationArithmeticImpliesScalingArithmetic) :
    GaborSeparationForAllZeros := by
  intro s hsz hcrit
  set sigma : ℝ := |s.re - 1 / 2|
  have hs : 0 < sigma := abs_pos.mpr (sub_ne_zero.mpr hcrit)
  by_cases him : s.im = 0
  · simpa [him] using hscale.2 s.re hcrit
  · have hs1 : sigma < 1 / 2 := abs_re_sub_half_lt_half hsz him
    have hg : 0 < |s.im| := abs_pos.mpr him
    let Z := gaborSingletonConfig sigma |s.im| hs hs1 hg
    have hZ : Z.pts.Nonempty := by
      simp [Z, gaborSingletonConfig]
    have hWlog :=
      hdom Z hZ (singleton_incrementCompliantLog sigma |s.im| hs hs1 hg)
        (singleton_gammaDistinct sigma |s.im| hs hs1 hg)
    have ha := isolationShrinkOfConfig_a_pos Z hZ
    have hW :
        gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
          (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0 :=
      lt_of_le_of_lt (gaborHonestWeil_le_honestWeilLog _ _ Z ha) hWlog
    have harith := hhonest Z hZ hW
    refine hscale.1 s.re s.im hcrit Z hZ ?_ ?_ harith
    · convert singleton_hostSigma sigma |s.im| hs hs1 hg
    · convert singleton_hostGamma sigma |s.im| hs hs1 hg

#print axioms one_add_log_div_self_le_two
#print axioms add_five_div_add_three_le_two
#print axioms gaborHatThreeLobeConst_half_div_E
#print axioms gaborLogRon_div_E_le_one_hundred
#print axioms gaborOnlineLogBudget_div_E_le_one_hundred
#print axioms gaborHonestOnlineBudgetLog_div_E_le_one_hundred
#print axioms gaborRemainderBudgetLog2_holds
#print axioms gabor_dominanceBoundLog2_holds
#print axioms gaborLogMajorantLeHonestBudgetLog_holds
#print axioms gabor_criticalLineMass_le_honest_of
#print axioms thetaLeftPos_nonneg
#print axioms gaborSCert_nonneg
#print axioms gaborHonestWeil_le_honestWeilLog
#print axioms gaborHonestWeilLog_lt_etaMargin
#print axioms gaborHonestWeilLog_lt_lockMargin
#print axioms gaborHonestWeilLeMajorantLog2_of_le
#print axioms gaborRemainderBudgetLog2_of_le
#print axioms gaborHonestWeilLog_lt_etaMargin_of_le
#print axioms gaborHonestWeilLog_lt_lockMargin_of_le
#print axioms gaborWeightedTruncationNegLog_holds
#print axioms gaborWeightedTruncationNegLogQuant_holds
#print axioms gaborWeightedTruncation_lockMargin
#print axioms gaborWeightedTruncation_honestWeil_neg
#print axioms gabor_dominanceLog2_implies_separation

end RH
