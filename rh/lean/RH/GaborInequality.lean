/-
RH/GaborInequality.lean -- r544 symbolic Gabor-inequality boundary.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not modify or discharge
`GaborSeparationInequality`.  It proves the elementary Gaussian, logarithmic,
scaling, ratio, and pole-sign statements that a uniform argument would use,
then names the two missing analytic controls exactly:

  (1) Trudgian's unit-interval zero count does not by itself turn a discrete
      zero sum into the continuous Gaussian-density integral;
  (2) critical-line positivity does not upper-bound contributions from other
      off-critical zeros.

There are no `sorry` declarations in this file.  The finite r541 certificate
is therefore not replaced by a global theorem here.  The definitions at the
end are boundary Props, not asserted axioms.

r552 proves the *discrete* bin-max Gauss transfer
(`RH.GaborThetaBound.gauss_online_mass_uniform`): a unit-bin count
bound C yields on-line Gaussian mass `≤ C · Θ_lobe(a)`, independently
of the packet center.  That is not `TrudgianGaussianMeasureTransfer`,
which still asks for the continuous `sqrt(2πa)` integral and remains
an open boundary Prop.
-/
import RH.GaborSeparation
import RH.GaborThetaBound
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral

namespace RH

open MeasureTheory

/-- The r542/r544 scaling `a = σ²/64`. -/
noncomputable def gaborScalingA (sigma : ℝ) : ℝ :=
  sigma ^ 2 / 64

/-- The phase-tuned packet center. -/
noncomputable def gaborScalingOmega (sigma gamma : ℝ) : ℝ :=
  gamma - Real.pi * gaborScalingA sigma / sigma

theorem gaborScalingA_pos {sigma : ℝ} (hsigma : sigma ≠ 0) :
    0 < gaborScalingA sigma := by
  unfold gaborScalingA
  positivity

/-- The exact Gaussian integral used by the continuous-density heuristic.
No zero-density statement is contained in this identity. -/
theorem gabor_gaussian_integral_exact (b : ℝ) :
    (∫ x : ℝ, Real.exp (-b * x ^ 2)) = Real.sqrt (Real.pi / b) :=
  integral_gaussian b

/-- A convenient nonnegative form of the Gaussian integral value. -/
theorem gabor_gaussian_integral_value_nonneg (b : ℝ) :
    0 ≤ Real.sqrt (Real.pi / b) :=
  Real.sqrt_nonneg _

/-- Elementary log monotonicity, isolated for envelope estimates. -/
theorem gabor_log_mono {x y : ℝ} (hx : 0 < x) (hxy : x ≤ y) :
    Real.log x ≤ Real.log y :=
  Real.log_le_log hx hxy

/-- The phase-tuned displacement is exactly `πa/σ`. -/
theorem gaborScaling_detune
    {sigma gamma : ℝ} :
    gamma - gaborScalingOmega sigma gamma =
      Real.pi * gaborScalingA sigma / sigma := by
  unfold gaborScalingOmega
  ring

/-- The phase of the selected lobe is exactly `π`. -/
theorem gaborScaling_phase
    {sigma gamma : ℝ} (hsigma : sigma ≠ 0) :
    sigma * (gamma - gaborScalingOmega sigma gamma) /
        gaborScalingA sigma = Real.pi := by
  rw [gaborScaling_detune]
  unfold gaborScalingA
  field_simp [hsigma]

/-- The phase-tuned main lobe includes the detuning price
`exp (-π²/128)` in addition to the real-direction enhancement `exp 32`. -/
theorem gaborScaling_main_exponent
    {sigma gamma : ℝ} (hsigma : sigma ≠ 0) :
    (sigma ^ 2 -
        (gamma - gaborScalingOmega sigma gamma) ^ 2) /
          (2 * gaborScalingA sigma) =
      32 - Real.pi ^ 2 / 128 := by
  rw [gaborScaling_detune]
  unfold gaborScalingA
  field_simp [hsigma]
  ring

/-- Three exact amplitudes in the phase-tuned FE-quadruple formula. -/
noncomputable def gaborMainAmplitude (sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 -
    (gamma - gaborScalingOmega sigma gamma) ^ 2) /
      (2 * gaborScalingA sigma))

noncomputable def gaborPlusAmplitude (sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 -
    (gamma + gaborScalingOmega sigma gamma) ^ 2) /
      (2 * gaborScalingA sigma))

noncomputable def gaborCrossAmplitude (sigma gamma : ℝ) : ℝ :=
  Real.exp ((sigma ^ 2 - gamma ^ 2 -
    gaborScalingOmega sigma gamma ^ 2) /
      (2 * gaborScalingA sigma))

/-- Exact closed form for `4 Re ĥ_W(β+iγ)` after the selected lobe has
phase `π`; this books the complete functional-equation quadruple. -/
noncomputable def pureGaborFEQuadrupleClosed (sigma gamma : ℝ) : ℝ :=
  let a := gaborScalingA sigma
  let omega := gaborScalingOmega sigma gamma
  Real.pi / a *
    (gaborPlusAmplitude sigma gamma *
        Real.cos (sigma * (gamma + omega) / a) -
      gaborMainAmplitude sigma gamma +
      2 * gaborCrossAmplitude sigma gamma *
        Real.cos (sigma * gamma / a))

/-- Explicit positive-margin candidate. -/
noncomputable def gaborDominanceMargin (sigma gamma : ℝ) : ℝ :=
  gaborMainAmplitude sigma gamma -
    gaborPlusAmplitude sigma gamma -
    2 * gaborCrossAmplitude sigma gamma

/-- Cosine majorization reduces the exact quadruple to `-(π/a)D`. -/
theorem pureGaborFEQuadrupleClosed_le
    {sigma gamma : ℝ} (hsigma : sigma ≠ 0) :
    pureGaborFEQuadrupleClosed sigma gamma ≤
      -(Real.pi / gaborScalingA sigma *
        gaborDominanceMargin sigma gamma) := by
  have ha := gaborScalingA_pos hsigma
  have hpi : 0 < Real.pi := Real.pi_pos
  have hplus : 0 ≤ gaborPlusAmplitude sigma gamma :=
    (Real.exp_pos _).le
  have hcross : 0 ≤ gaborCrossAmplitude sigma gamma :=
    (Real.exp_pos _).le
  have hcosPlus := Real.cos_le_one
    (sigma * (gamma + gaborScalingOmega sigma gamma) /
      gaborScalingA sigma)
  have hcosCross := Real.cos_le_one
    (sigma * gamma / gaborScalingA sigma)
  unfold pureGaborFEQuadrupleClosed gaborDominanceMargin
  dsimp
  have hinside :
      gaborPlusAmplitude sigma gamma *
            Real.cos (sigma *
              (gamma + gaborScalingOmega sigma gamma) /
                gaborScalingA sigma) -
          gaborMainAmplitude sigma gamma +
          2 * gaborCrossAmplitude sigma gamma *
            Real.cos (sigma * gamma / gaborScalingA sigma) ≤
        -gaborMainAmplitude sigma gamma +
          gaborPlusAmplitude sigma gamma +
          2 * gaborCrossAmplitude sigma gamma := by
    nlinarith
  have hpref : 0 ≤ Real.pi / gaborScalingA sigma :=
    (div_pos hpi ha).le
  calc
    Real.pi / gaborScalingA sigma *
          (gaborPlusAmplitude sigma gamma *
              Real.cos (sigma *
                (gamma + gaborScalingOmega sigma gamma) /
                  gaborScalingA sigma) -
            gaborMainAmplitude sigma gamma +
            2 * gaborCrossAmplitude sigma gamma *
              Real.cos (sigma * gamma / gaborScalingA sigma)) ≤
        Real.pi / gaborScalingA sigma *
          (-gaborMainAmplitude sigma gamma +
            gaborPlusAmplitude sigma gamma +
            2 * gaborCrossAmplitude sigma gamma) :=
      mul_le_mul_of_nonneg_left hinside hpref
    _ = -(Real.pi / gaborScalingA sigma *
          (gaborMainAmplitude sigma gamma -
            gaborPlusAmplitude sigma gamma -
            2 * gaborCrossAmplitude sigma gamma)) := by ring

theorem pureGaborFEQuadrupleClosed_neg
    {sigma gamma : ℝ} (hsigma : sigma ≠ 0)
    (hD : 0 < gaborDominanceMargin sigma gamma) :
    pureGaborFEQuadrupleClosed sigma gamma < 0 := by
  have hpi : 0 < Real.pi := Real.pi_pos
  have ha := gaborScalingA_pos hsigma
  exact lt_of_le_of_lt (pureGaborFEQuadrupleClosed_le hsigma)
    (neg_lt_zero.mpr (mul_pos (div_pos hpi ha) hD))

/-- Closed pole value for the pure Gabor packet.  The factor
`exp ((1/4-ω²)/(2a))` records the frequency-shift suppression omitted by the
naive `exp (1/(8a))` comparison. -/
noncomputable def pureGaborPoleClosed (a omega : ℝ) : ℝ :=
  Real.pi / a *
    Real.exp (((1 / 4 : ℝ) - omega ^ 2) / (2 * a)) *
    Real.cos (omega / (4 * a)) ^ 2

theorem pureGaborPoleClosed_nonneg
    {a omega : ℝ} (ha : 0 < a) :
    0 ≤ pureGaborPoleClosed a omega := by
  unfold pureGaborPoleClosed
  positivity

/-- In `gaborSpectralFormula` the pole is subtracted, hence it can only lower
the target upper bound. -/
theorem gabor_pole_subtraction_helps
    {total a omega : ℝ} (ha : 0 < a) :
    total - pureGaborPoleClosed a omega ≤ total := by
  linarith [pureGaborPoleClosed_nonneg (a := a) (omega := omega) ha]

/-- Once `ω² ≥ 1/4`, the complete pole exponent is nonpositive. -/
theorem gabor_pole_exponent_nonpos
    {a omega : ℝ} (ha : 0 < a) (homega : (1 / 4 : ℝ) ≤ omega ^ 2) :
    ((1 / 4 : ℝ) - omega ^ 2) / (2 * a) ≤ 0 := by
  exact div_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr homega)
    (mul_nonneg (by norm_num) ha.le)

/-- Ratio lemma for the continuous-density model.  The factor `sqrt(2πa)`
is valid only after a separate measure-transfer theorem turns the discrete
zero sum into the displayed integral bound. -/
theorem gabor_continuous_ratio_bound
    {a C gamma D online offAbs : ℝ}
    (ha : 0 < a) (hD : 0 < D) (hoff : Real.pi / a * D ≤ offAbs)
    (hon : online ≤
      Real.pi / (4 * a) * C * Real.log (gamma + 2) *
        Real.sqrt (2 * Real.pi * a))
    (hoffPos : 0 < offAbs)
    (hnumer : 0 ≤
      C * Real.log (gamma + 2) * Real.sqrt (2 * Real.pi * a)) :
    online / offAbs ≤
      C * Real.log (gamma + 2) * Real.sqrt (2 * Real.pi * a) /
        (4 * D) := by
  have hpi : 0 < Real.pi := Real.pi_pos
  have hbase : 0 < Real.pi / a * D := mul_pos (div_pos hpi ha) hD
  have hfactor :
      Real.pi / (4 * a) * C * Real.log (gamma + 2) *
          Real.sqrt (2 * Real.pi * a) =
        (Real.pi / a * D) *
          (C * Real.log (gamma + 2) * Real.sqrt (2 * Real.pi * a) /
            (4 * D)) := by
    field_simp [ne_of_gt ha, ne_of_gt hD]
  rw [hfactor] at hon
  have hratio :
      0 ≤ C * Real.log (gamma + 2) *
        Real.sqrt (2 * Real.pi * a) / (4 * D) :=
    div_nonneg hnumer (mul_nonneg (by norm_num) hD.le)
  calc
    online / offAbs ≤
        (Real.pi / a * D) *
          (C * Real.log (gamma + 2) * Real.sqrt (2 * Real.pi * a) /
            (4 * D)) / offAbs :=
      (div_le_div_of_nonneg_right hon hoffPos.le)
    _ ≤ C * Real.log (gamma + 2) * Real.sqrt (2 * Real.pi * a) /
          (4 * D) := by
      have hquot : Real.pi / a * D / offAbs ≤ 1 :=
        (div_le_one hoffPos).2 hoff
      calc
        (Real.pi / a * D) *
              (C * Real.log (gamma + 2) *
                Real.sqrt (2 * Real.pi * a) / (4 * D)) / offAbs =
            (Real.pi / a * D / offAbs) *
              (C * Real.log (gamma + 2) *
                Real.sqrt (2 * Real.pi * a) / (4 * D)) := by ring
        _ ≤ 1 *
                (C * Real.log (gamma + 2) *
                Real.sqrt (2 * Real.pi * a) / (4 * D)) :=
          mul_le_mul_of_nonneg_right hquot hratio
        _ = _ := one_mul _

/-- Ratio lemma matching what Trudgian's unit-interval estimate actually
supplies for a packet narrower than one: peak times a bin count.  The scale
`a` cancels completely; there is no `sqrt a` gain. -/
theorem gabor_unitBin_ratio_bound
    {a C L gamma D online offAbs : ℝ}
    (ha : 0 < a) (hD : 0 < D) (hoff : Real.pi / a * D ≤ offAbs)
    (hon : online ≤
      2 * C * Real.log (gamma + 3) * (Real.pi / (4 * a)) * L)
    (hoffPos : 0 < offAbs)
    (hnumer : 0 ≤ C * Real.log (gamma + 3) * L) :
    online / offAbs ≤ C * Real.log (gamma + 3) * L / (2 * D) := by
  have hpi : 0 < Real.pi := Real.pi_pos
  have hbase : 0 < Real.pi / a * D := mul_pos (div_pos hpi ha) hD
  have hfactor :
      2 * C * Real.log (gamma + 3) * (Real.pi / (4 * a)) * L =
        (Real.pi / a * D) *
          (C * Real.log (gamma + 3) * L / (2 * D)) := by
    field_simp [ne_of_gt ha, ne_of_gt hD]
    ring
  rw [hfactor] at hon
  have hratio : 0 ≤ C * Real.log (gamma + 3) * L / (2 * D) :=
    div_nonneg hnumer (mul_nonneg (by norm_num) hD.le)
  calc
    online / offAbs ≤
        (Real.pi / a * D) *
          (C * Real.log (gamma + 3) * L / (2 * D)) / offAbs :=
      div_le_div_of_nonneg_right hon hoffPos.le
    _ = (Real.pi / a * D / offAbs) *
          (C * Real.log (gamma + 3) * L / (2 * D)) := by ring
    _ ≤ 1 * (C * Real.log (gamma + 3) * L / (2 * D)) := by
      exact mul_le_mul_of_nonneg_right ((div_le_one hoffPos).2 hoff) hratio
    _ = _ := one_mul _

/-- The contribution of zeros on the critical line. -/
noncomputable def gaborCriticalLineMass (F : GaborWeilTest) : ℝ :=
  (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
    if (ρ : ℂ).re = 1 / 2 then
      (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
    else 0).re

/-- r552 discrete bin-max transfer (proved).  This is the unit-bin
Gaussian majorant of r549, not the continuous-density integral below. -/
theorem gauss_density_transfer_binMax
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        2 * zetaZerosInDiskCardBoundInner) :
    (S.sum (gaussWeight a c) : ℝ) ≤
      2 * zetaZerosInDiskCardBoundInner * thetaLobe a :=
  gauss_online_mass_uniform_ordinates ha c S hinc

/-- r579 log-occupancy discrete transfer (Bridge 2, Finset form).
The constant-cap theorem above is the historical special case
`C k ≡ 2 C_inner`.  Here each unit bin may carry a *different*
occupancy `C k` (Path-A `2 C_inner (1+log(|k|+3))`).  The resulting
majorant is the log-weighted Jacobi-theta series, not `C · Θ_lobe`. -/
theorem gauss_density_transfer_binMax_log
    {a : ℝ} (ha : 0 < a) (c : ℝ) (S : Finset ℝ)
    (C : ℤ → ℝ) (hC0 : ∀ k, 0 ≤ C k)
    (hinc : ∀ k : ℤ,
      ((S.filter (fun t => (k : ℝ) < t ∧ t ≤ (k : ℝ) + 1)).card : ℝ) ≤
        C k)
    (hMs : Summable fun k : ℤ => C k * gaussBinMax a c k) :
    (S.sum (gaussWeight a c) : ℝ) ≤
      ∑' k : ℤ, C k * gaussBinMax a c k :=
  gauss_online_mass_varC_ordinates ha c S C hC0 hinc hMs

/-- Missing analytic brick A: a measure-transfer estimate strong enough to
justify the continuous Gaussian integral instead of unit-bin suprema.  This
does not follow definitionally from `TrudgianZeroDensityBound`, and it is
not discharged by the discrete r552 bound `gauss_density_transfer_binMax`. -/
def TrudgianGaussianMeasureTransfer : Prop :=
  TrudgianZeroDensityBound →
    ∃ K : ℝ, 0 < K ∧
      ∀ sigma gamma : ℝ, ∀ hsigma : sigma ≠ 0,
        gaborCriticalLineMass
            (scalingGaborTest (sigma + 1 / 2) gamma (by
              intro heq
              apply hsigma
              linarith)) ≤
          K * Real.pi / (4 * gaborScalingA sigma) *
            Real.log (|gamma| + 3) *
            Real.sqrt (2 * Real.pi * gaborScalingA sigma)

/-- Membership in the functional-equation quadruple generated by `s`. -/
def sameZetaFEQuadruple (z s : ℂ) : Prop :=
  z = s ∨ z = starRingEnd ℂ s ∨ z = 1 - s ∨
    z = 1 - starRingEnd ℂ s

/-- Every off-critical zero contribution except the selected FE quadruple. -/
noncomputable def gaborAdditionalOffCriticalRemainder
    (F : GaborWeilTest) (s : ℂ) : ℝ := by
  classical
  exact
    (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
      if (ρ : ℂ).re ≠ 1 / 2 ∧
          ¬sameZetaFEQuadruple (ρ : ℂ) s then
        (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ
      else 0).re

/-- Missing analytic brick B: control of every zero not belonging to the
selected functional-equation quadruple.  Critical-line nonnegativity alone
does not provide this when other off-critical zeros are allowed. -/
def AdditionalOffCriticalZeroControl : Prop :=
  ∀ s : ℂ, IsNontrivialRiemannZetaZero s →
    ∀ hcritical : s.re ≠ 1 / 2,
    let F := scalingGaborTest s.re s.im hcritical
    gaborAdditionalOffCriticalRemainder F s <
      -(4 * (gaborHat F s).re)

/-- Precise r544 boundary: either a global replacement of the finite table
must prove both controls, or it must change the test/scaling so that the
uncontrolled remainder is absent.  This Prop is documentation, not asserted. -/
def GaborUniformInequalityBoundary : Prop :=
  TrudgianGaussianMeasureTransfer ∧ AdditionalOffCriticalZeroControl

#print axioms gabor_gaussian_integral_exact
#print axioms gabor_log_mono
#print axioms gaborScaling_phase
#print axioms gaborScaling_main_exponent
#print axioms pureGaborFEQuadrupleClosed_le
#print axioms pureGaborFEQuadrupleClosed_neg
#print axioms pureGaborPoleClosed_nonneg
#print axioms gabor_pole_subtraction_helps
#print axioms gabor_continuous_ratio_bound
#print axioms gabor_unitBin_ratio_bound
#print axioms gauss_density_transfer_binMax
#print axioms gauss_density_transfer_binMax_log

end RH
