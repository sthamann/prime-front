/-
RH/GaborArchDigamma.lean -- r577 left-edge χ′/χ Digamma fold.

CLAIM BOUNDARY.  NO RH CLAIM.  Proves the meromorphic identification
`χ′/χ(1/2+it) = Re ψ(1/4+it/2) − log π` from Mathlib's `Gammaℝ`
reflection, and the implication from the named contour shift
`GaborArchContourShift` to `GaborArchDigammaIdentification`.
r581 discharges `GaborArchContourShift` and therefore
`gaborArchDigammaIdentification_holds` (in `GaborArchContour.lean`).
-/
import RH.GaborLeftVertical
import Mathlib.Analysis.SpecialFunctions.Gamma.Deligne
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace RH

open Complex Filter Function MeasureTheory Set
open scoped Topology ComplexConjugate

/-! ## `χ = Γℂ · cos = Γℝ / Γℝ(1−·)` -/

lemma zetaFEFactor_eq_Gammaℂ_mul_cos (s : ℂ) :
    zetaFEFactor s = Gammaℂ s * cos (Real.pi * s / 2) := by
  unfold zetaFEFactor Gammaℂ
  have hπ : (2 * (Real.pi : ℂ)) = ((2 * Real.pi : ℝ) : ℂ) := by
    rw [ofReal_mul, ofReal_ofNat]
  simp only [hπ, mul_assoc]

lemma zetaFEFactor_eq_Gammaℝ_div {s : ℂ}
    (hs : ∀ n : ℕ, s ≠ -n) :
    zetaFEFactor s = Gammaℝ s / Gammaℝ (1 - s) := by
  have hΓ : Gammaℝ s ≠ 0 := by
    intro h0
    obtain ⟨n, hn⟩ := Gammaℝ_eq_zero_iff.mp h0
    exact hs (2 * n) (by simpa using hn)
  have hinv := inv_Gammaℝ_one_sub hs
  rw [zetaFEFactor_eq_Gammaℂ_mul_cos]
  calc
    Gammaℂ s * cos (Real.pi * s / 2)
        = Gammaℝ s *
            (Gammaℂ s * cos (Real.pi * s / 2) * (Gammaℝ s)⁻¹) := by
          field_simp [hΓ]
    _ = Gammaℝ s * (Gammaℝ (1 - s))⁻¹ := by rw [← hinv]
    _ = Gammaℝ s / Gammaℝ (1 - s) := div_eq_mul_inv _ _

/-! ## `Γℝ` logarithmic derivative -/

lemma logDeriv_cpow_neg_div_two (s : ℂ) :
    logDeriv (fun w : ℂ => (Real.pi : ℂ) ^ (-w / 2)) s =
      - Complex.log (Real.pi : ℂ) / 2 := by
  have hc : (Real.pi : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
  have hd : HasDerivAt (fun w : ℂ => -w / 2) (-1 / 2) s :=
    (hasDerivAt_neg s).div_const 2
  have h := hd.const_cpow (Or.inl hc)
  have hne : (Real.pi : ℂ) ^ (-s / 2) ≠ 0 :=
    cpow_ne_zero_iff.mpr (Or.inl hc)
  rw [logDeriv_apply, h.deriv]
  field_simp [hne]

lemma logDeriv_Gamma_div_two {s : ℂ}
    (hG : ∀ n : ℕ, s / 2 ≠ -n) :
    logDeriv (fun w : ℂ => Gamma (w / 2)) s =
      (1 / 2 : ℂ) * digamma (s / 2) := by
  have hdiffΓ : DifferentiableAt ℂ Gamma (s / 2) :=
    differentiableAt_Gamma (s / 2) hG
  have hd : HasDerivAt (fun w : ℂ => w / 2) (1 / 2) s :=
    (hasDerivAt_id s).div_const 2
  have hcomp :=
    logDeriv_comp (f := Gamma) (g := fun w : ℂ => w / 2)
      hdiffΓ hd.differentiableAt
  have hfun : (fun w : ℂ => Gamma (w / 2)) =
      Gamma ∘ fun w : ℂ => w / 2 := rfl
  rw [hfun, hcomp, hd.deriv, digamma_def]
  ring

lemma differentiableAt_Gammaℝ_of {s : ℂ}
    (hG : ∀ n : ℕ, s / 2 ≠ -n) :
    DifferentiableAt ℂ Gammaℝ s := by
  have hc : (Real.pi : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
  have hcpow :
      DifferentiableAt ℂ (fun w : ℂ => (Real.pi : ℂ) ^ (-w / 2)) s := by
    have hd : HasDerivAt (fun w : ℂ => -w / 2) (-1 / 2) s :=
      (hasDerivAt_neg s).div_const 2
    exact (hd.const_cpow (Or.inl hc)).differentiableAt
  have hΓ : DifferentiableAt ℂ (fun w : ℂ => Gamma (w / 2)) s := by
    have hd : HasDerivAt (fun w : ℂ => w / 2) (1 / 2) s :=
      (hasDerivAt_id s).div_const 2
    exact (differentiableAt_Gamma (s / 2) hG).comp s hd.differentiableAt
  change DifferentiableAt ℂ
      (fun w => (Real.pi : ℂ) ^ (-w / 2) * Gamma (w / 2)) s
  exact hcpow.mul hΓ

lemma logDeriv_Gammaℝ {s : ℂ}
    (hG : ∀ n : ℕ, s / 2 ≠ -n) :
    logDeriv Gammaℝ s =
      - Complex.log (Real.pi : ℂ) / 2 +
        (1 / 2 : ℂ) * digamma (s / 2) := by
  have hc : (Real.pi : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
  have hcpow0 : (Real.pi : ℂ) ^ (-s / 2) ≠ 0 :=
    cpow_ne_zero_iff.mpr (Or.inl hc)
  have hΓ0 : Gamma (s / 2) ≠ 0 := Complex.Gamma_ne_zero hG
  have hcpow :
      DifferentiableAt ℂ (fun w : ℂ => (Real.pi : ℂ) ^ (-w / 2)) s := by
    have hd : HasDerivAt (fun w : ℂ => -w / 2) (-1 / 2) s :=
      (hasDerivAt_neg s).div_const 2
    exact (hd.const_cpow (Or.inl hc)).differentiableAt
  have hΓ : DifferentiableAt ℂ (fun w : ℂ => Gamma (w / 2)) s := by
    have hd : HasDerivAt (fun w : ℂ => w / 2) (1 / 2) s :=
      (hasDerivAt_id s).div_const 2
    exact (differentiableAt_Gamma (s / 2) hG).comp s hd.differentiableAt
  change logDeriv (fun w => (Real.pi : ℂ) ^ (-w / 2) * Gamma (w / 2)) s =
      - Complex.log (Real.pi : ℂ) / 2 + (1 / 2 : ℂ) * digamma (s / 2)
  rw [logDeriv_mul (f := fun w => (Real.pi : ℂ) ^ (-w / 2))
      (g := fun w => Gamma (w / 2)) s hcpow0 hΓ0 hcpow hΓ,
    logDeriv_cpow_neg_div_two, logDeriv_Gamma_div_two hG]

lemma ofReal_log_pi :
    Complex.log (Real.pi : ℂ) = (Real.log Real.pi : ℂ) :=
  (ofReal_log Real.pi_pos.le).symm

lemma digamma_conj (s : ℂ) :
    digamma (conj s) = conj (digamma s) := by
  have hid : (conj ∘ Gamma ∘ conj) = Gamma := by
    funext z; simp [Gamma_conj]
  have hcc : deriv (conj ∘ Gamma ∘ conj) s =
      conj (deriv Gamma (conj s)) := by
    simp [deriv_conj_conj]
  rw [hid] at hcc
  have hderiv : deriv Gamma (conj s) = conj (deriv Gamma s) := by
    simpa [conj_conj] using (congrArg conj hcc).symm
  rw [digamma_def, logDeriv_apply, logDeriv_apply, hderiv, Gamma_conj]
  simp [map_div₀]

/-! ## Critical-line identity `χ′/χ(1/2+it) = ω(t)` -/

lemma ne_neg_nat_of_re_pos {s : ℂ} (hs : 0 < s.re) (n : ℕ) : s ≠ -n := by
  intro hn
  have hre : s.re = -(n : ℝ) := by simpa using congrArg Complex.re hn
  have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  linarith

lemma half_im_ne_neg_nat (t : ℝ) (n : ℕ) :
    ((1 / 2 : ℂ) + t * I) / 2 ≠ -n := by
  intro hn
  have hre : (((1 / 2 : ℂ) + t * I) / 2).re = 1 / 4 := by
    simp [add_re, mul_re, I_re, I_im, ofReal_re, ofReal_im]
    norm_num
  have hre' : (((1 / 2 : ℂ) + t * I) / 2).re = -(n : ℝ) := by
    simpa using congrArg Complex.re hn
  have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  have hpos : (0 : ℝ) < (1 / 4 : ℝ) := by norm_num
  linarith [hre, hre']

lemma one_sub_half_im_ne_neg_nat (t : ℝ) (n : ℕ) :
    (1 - ((1 / 2 : ℂ) + t * I)) / 2 ≠ -n := by
  intro hn
  have hre : ((1 - ((1 / 2 : ℂ) + t * I)) / 2).re = 1 / 4 := by
    simp [sub_re, add_re, mul_re, I_re, I_im, ofReal_re, ofReal_im]
    norm_num
  have hre' : ((1 - ((1 / 2 : ℂ) + t * I)) / 2).re = -(n : ℝ) := by
    simpa using congrArg Complex.re hn
  have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  have hpos : (0 : ℝ) < (1 / 4 : ℝ) := by norm_num
  linarith [hre, hre']

lemma eventuallyEq_zetaFEFactor_Gammaℝ_div_critical (t : ℝ) :
    (fun w : ℂ => Gammaℝ w / Gammaℝ (1 - w))
      =ᶠ[𝓝 ((1 / 2 : ℂ) + t * I)] zetaFEFactor := by
  set s : ℂ := (1 / 2 : ℂ) + t * I
  refine Filter.eventuallyEq_of_mem
      (Metric.ball_mem_nhds s (by norm_num : (0 : ℝ) < (1 / 8 : ℝ))) ?_
  intro w hw
  have hd : ‖w - s‖ < 1 / 8 := mem_ball_iff_norm.mp hw
  have hre_le : |w.re - s.re| ≤ ‖w - s‖ := by
    simpa [sub_re] using abs_re_le_norm (w - s)
  have hre : |w.re - 1 / 2| < 1 / 8 := by
    have : s.re = 1 / 2 := by simp [s]
    rw [this] at hre_le
    exact lt_of_le_of_lt hre_le hd
  have hpos : 0 < w.re := by
    have := (abs_lt.mp hre).1
    linarith
  exact (zetaFEFactor_eq_Gammaℝ_div (ne_neg_nat_of_re_pos hpos)).symm

lemma logDeriv_zetaFEFactor_eq_Gammaℝ_pair_critical (t : ℝ) :
    logDeriv zetaFEFactor ((1 / 2 : ℂ) + t * I) =
      - Complex.log (Real.pi : ℂ) +
        (1 / 2 : ℂ) * digamma (((1 / 2 : ℂ) + t * I) / 2) +
        (1 / 2 : ℂ) * digamma ((1 - ((1 / 2 : ℂ) + t * I)) / 2) := by
  set s : ℂ := (1 / 2 : ℂ) + t * I
  have hs2 : ∀ n : ℕ, s / 2 ≠ -n := fun n => half_im_ne_neg_nat t n
  have h1s2 : ∀ n : ℕ, (1 - s) / 2 ≠ -n :=
    fun n => one_sub_half_im_ne_neg_nat t n
  have hΓs : Gammaℝ s ≠ 0 :=
    Gammaℝ_ne_zero_of_re_pos (by simp [s])
  have hΓ1 : Gammaℝ (1 - s) ≠ 0 :=
    Gammaℝ_ne_zero_of_re_pos (by simp [s, sub_re]; norm_num)
  have hdiffR := differentiableAt_Gammaℝ_of (s := s) hs2
  have hdiff1R := differentiableAt_Gammaℝ_of (s := 1 - s) h1s2
  have hd1 := hasDerivAt_one_sub s
  have hdiff1 : DifferentiableAt ℂ (fun w : ℂ => Gammaℝ (1 - w)) s :=
    hdiff1R.comp s hd1.differentiableAt
  have hdiv :=
    logDeriv_div (f := Gammaℝ) (g := fun w : ℂ => Gammaℝ (1 - w)) s
      hΓs hΓ1 hdiffR hdiff1
  have hcomp :
      logDeriv (fun w : ℂ => Gammaℝ (1 - w)) s =
        - logDeriv Gammaℝ (1 - s) := by
    have hcc :=
      logDeriv_comp (f := Gammaℝ) (g := fun w : ℂ => 1 - w)
        hdiff1R hd1.differentiableAt
    have hfun : (fun w : ℂ => Gammaℝ (1 - w)) =
        Gammaℝ ∘ fun w : ℂ => 1 - w := rfl
    rw [hfun, hcc, hd1.deriv]
    ring
  have hld :
      logDeriv (fun w : ℂ => Gammaℝ w / Gammaℝ (1 - w)) s =
        logDeriv zetaFEFactor s := by
    have heq := eventuallyEq_zetaFEFactor_Gammaℝ_div_critical t
    rw [logDeriv_apply, logDeriv_apply, heq.deriv_eq, heq.eq_of_nhds]
  rw [← hld, hdiv, hcomp, logDeriv_Gammaℝ hs2, logDeriv_Gammaℝ h1s2]
  ring

/-- On the critical line the FE log-derivative equals the real
archimedean density `ω(t) = Re ψ(1/4+it/2) − log π`. -/
theorem logDeriv_zetaFEFactor_criticalLine (t : ℝ) :
    logDeriv zetaFEFactor ((1 / 2 : ℂ) + t * Complex.I) =
      (gaborArchDensity t : ℂ) := by
  set s : ℂ := (1 / 2 : ℂ) + t * Complex.I
  have hpair := logDeriv_zetaFEFactor_eq_Gammaℝ_pair_critical t
  have hz : s / 2 = (1 / 4 : ℂ) + (t / 2 : ℝ) * Complex.I := by
    apply Complex.ext
    · simp [s]; norm_num
    · simp [s]
  have hconj : (1 - s) / 2 = conj (s / 2) := by
    rw [hz]
    apply Complex.ext
    · rw [conj_re]; simp [s]; norm_num
    · rw [conj_im]; simp [s]; ring
  have hsum :
      (1 / 2 : ℂ) * digamma (s / 2) +
          (1 / 2 : ℂ) * digamma ((1 - s) / 2) =
        ((digamma (s / 2)).re : ℂ) := by
    rw [hconj, digamma_conj]
    apply Complex.ext
    · simp [mul_re, add_re, conj_re]; ring
    · simp [mul_im, add_im, conj_im]
  have hlog : -Complex.log (Real.pi : ℂ) = (-Real.log Real.pi : ℂ) := by
    rw [ofReal_log_pi, ← ofReal_neg]
  have hψ :
      (1 / 2 : ℂ) * digamma (((1 / 2 : ℂ) + t * I) / 2) +
          (1 / 2 : ℂ) * digamma ((1 - ((1 / 2 : ℂ) + t * I)) / 2) =
        ((digamma (s / 2)).re : ℂ) := by
    simpa [s] using hsum
  unfold gaborArchDensity
  rw [hpair, add_assoc, hψ, hlog, hz, ofReal_sub]
  simp [sub_eq_add_neg, add_comm]

/-! ## Named contour remainder and the identification implication -/

/-- Contour shift of the archimedean clamp from the left edge to the
critical line, picking up `2π ĥ_W(0)`.  The meromorphic identity
`χ′/χ(1/2+it) = ω(t)` is a theorem; this Prop is the remaining
rectangle/T→∞ glue (residue `-1` of `χ′/χ` at `s = 0`).
Unasserted.  Not a `sorry`. -/
def GaborArchContourShift : Prop :=
  ∀ F : GaborWeilTest, F.admissible → F.coeffs = ⟨1, 0, 0⟩ →
    gaborLeftEdgeArchIntegral F =
      (2 * Real.pi : ℂ) * gaborHat F 0 +
        ∫ t : ℝ, (gaborArchDensity t : ℂ) *
          gaborHat F ((1 / 2 : ℂ) + t * Complex.I)

/-- Real-part form of the critical-line pairing, once the complex
integrand `ω(t) ĥ_W(1/2+it)` is integrable.  Smaller remainder than
the contour; kept named so the identification implication stays
sorry-free.  Unasserted.  Not a `sorry`. -/
def GaborArchCriticalPairingReal : Prop :=
  ∀ F : GaborWeilTest, F.coeffs = ⟨1, 0, 0⟩ →
    (∫ t : ℝ, (gaborArchDensity t : ℂ) *
        gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re =
      ∫ t : ℝ, (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re *
        gaborArchDensity t

/-! ## Real pairing: `ω` continuous and `ω ĥ` integrable by majorant -/

lemma isOpen_re_pos : IsOpen {z : ℂ | 0 < z.re} :=
  isOpen_lt continuous_const continuous_re

lemma analyticOnNhd_Gamma_re_pos :
    AnalyticOnNhd ℂ Gamma {z : ℂ | 0 < z.re} :=
  DifferentiableOn.analyticOnNhd
    (fun w hw =>
      (differentiableAt_Gamma w (ne_neg_nat_of_re_pos hw)).differentiableWithinAt)
    isOpen_re_pos

lemma analyticOnNhd_digamma_re_pos :
    AnalyticOnNhd ℂ digamma {z : ℂ | 0 < z.re} :=
  fun z hz =>
    (analyticOnNhd_Gamma_re_pos z hz).deriv.div
      (analyticOnNhd_Gamma_re_pos z hz)
      (Complex.Gamma_ne_zero_of_re_pos hz)

lemma continuousOn_digamma_re_pos :
    ContinuousOn digamma {z : ℂ | 0 < z.re} :=
  analyticOnNhd_digamma_re_pos.continuousOn

lemma continuous_quarter_im_half_path :
    Continuous fun t : ℝ => (1 / 4 : ℂ) + (t / 2 : ℝ) * I :=
  continuous_const.add
    ((continuous_ofReal.comp (continuous_id.div_const (2 : ℝ))).mul
      continuous_const)

lemma re_quarter_im_half_path (t : ℝ) :
    ((1 / 4 : ℂ) + (t / 2 : ℝ) * I).re = 1 / 4 := by
  simp [add_re, mul_re, I_re, I_im, ofReal_re, ofReal_im]

lemma im_quarter_im_half_path (t : ℝ) :
    ((1 / 4 : ℂ) + (t / 2 : ℝ) * I).im = t / 2 := by
  simp [add_im, mul_im, I_re, I_im, ofReal_re, ofReal_im]

lemma re_pos_quarter_path (t : ℝ) :
    0 < ((1 / 4 : ℂ) + (t / 2 : ℝ) * I).re := by
  rw [re_quarter_im_half_path]; norm_num

set_option maxHeartbeats 800000 in
lemma continuous_gaborArchDensity : Continuous gaborArchDensity := by
  refine continuous_iff_continuousAt.mpr fun t => ?_
  have hmem : ((1 / 4 : ℂ) + (t / 2 : ℝ) * I) ∈ {z : ℂ | 0 < z.re} :=
    re_pos_quarter_path t
  have hψ : ContinuousAt (fun u : ℝ =>
      digamma ((1 / 4 : ℂ) + (u / 2 : ℝ) * I)) t :=
    ContinuousAt.comp
      (continuousOn_digamma_re_pos.continuousAt
        (isOpen_re_pos.mem_nhds hmem))
      continuous_quarter_im_half_path.continuousAt
  unfold gaborArchDensity
  exact (continuous_re.continuousAt.comp hψ).sub
    continuous_const.continuousAt

lemma half_complex_ofReal : (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
  norm_num

lemma gaborHat_critical_cast (F : GaborWeilTest) (t : ℝ) :
    gaborHat F ((1 / 2 : ℂ) + t * Complex.I) =
      gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I) := by
  rw [half_complex_ofReal]

lemma continuous_arch_critical_integrand (F : GaborWeilTest) :
    Continuous fun t : ℝ =>
      (gaborArchDensity t : ℂ) *
        gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I) :=
  (continuous_ofReal.comp continuous_gaborArchDensity).mul
    (continuous_gaborHat_vertical F (1 / 2))

lemma ofReal_mul_re (c : ℝ) (z : ℂ) : ((c : ℂ) * z).re = c * z.re := by
  simp [mul_re, ofReal_re, ofReal_im]

lemma two_le_abs_im_quarter_path {t : ℝ} (ht : (4 : ℝ) ≤ |t|) :
    (2 : ℝ) ≤ |((1 / 4 : ℂ) + (t / 2 : ℝ) * I).im| := by
  rw [im_quarter_im_half_path]
  have h : |t / 2| = |t| / 2 := by
    rw [abs_div, abs_of_pos (by norm_num : (0 : ℝ) < 2)]
  rw [h]
  have hdiv := div_le_div_of_nonneg_right ht (by norm_num : (0 : ℝ) ≤ 2)
  have : (4 : ℝ) / 2 = 2 := by norm_num
  rwa [this] at hdiv

lemma norm_gaborArchDensity_le_of_two_le_half_abs {t : ℝ}
    (ht : (4 : ℝ) ≤ |t|) :
    |gaborArchDensity t| ≤
      (6 + |Real.eulerMascheroniConstant|) *
          (1 + Real.log (2 + |t / 2|)) + 1 / 2 + |Real.log Real.pi| := by
  have him := two_le_abs_im_quarter_path ht
  have hre1 : (-1 / 16 : ℝ) ≤ ((1 / 4 : ℂ) + (t / 2 : ℝ) * I).re := by
    rw [re_quarter_im_half_path]; norm_num
  have hre2 : ((1 / 4 : ℂ) + (t / 2 : ℝ) * I).re ≤ (1 / 2 : ℝ) := by
    rw [re_quarter_im_half_path]; norm_num
  have hψ := norm_digamma_le_log_of_sliver hre1 hre2 him
  have hψ' : ‖digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)‖ ≤
      (6 + |Real.eulerMascheroniConstant|) *
        (1 + Real.log (2 + |t / 2|)) + 1 / 2 := by
    simpa [im_quarter_im_half_path] using hψ
  unfold gaborArchDensity
  have hre : |(digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)).re| ≤
      ‖digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)‖ :=
    abs_re_le_norm _
  have habs :
      |(digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)).re - Real.log Real.pi| ≤
        |(digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)).re| +
          |Real.log Real.pi| := by
    simpa [sub_eq_add_neg, abs_neg] using
      abs_add_le (digamma ((1 / 4 : ℂ) + (t / 2 : ℝ) * I)).re
        (-Real.log Real.pi)
  exact habs.trans (add_le_add (hre.trans hψ') le_rfl)

lemma integrable_arch_critical_integrand
    {F : GaborWeilTest} (hF : F.coeffs = ⟨1, 0, 0⟩) :
    Integrable fun t : ℝ =>
      (gaborArchDensity t : ℂ) *
        gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I) := by
  obtain ⟨c, C, hc, hC, hhat⟩ :=
    norm_gaborHat_le_gaussian_strip (F := F) hF (1 / 2) (1 / 2)
  set f : ℝ → ℂ := fun t =>
    (gaborArchDensity t : ℂ) *
      gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)
  obtain ⟨M0, hM0⟩ :=
    isCompact_Icc.exists_bound_of_continuousOn
      (continuous_arch_critical_integrand F |>.continuousOn :
        ContinuousOn f (Icc (-4 : ℝ) 4))
  have hM0nn : 0 ≤ M0 :=
    le_trans (norm_nonneg (f 0)) (hM0 0 ⟨by norm_num, by norm_num⟩)
  set Cψ : ℝ := 6 + |Real.eulerMascheroniConstant|
  have hCψ0 : 0 ≤ Cψ := by unfold Cψ; positivity
  set K : ℝ := (Cψ + 1 / 2 + |Real.log Real.pi|) * C
  have hK0 : 0 ≤ K :=
    mul_nonneg (add_nonneg (add_nonneg hCψ0 (by norm_num))
      (abs_nonneg _)) hC.le
  set g : ℝ → ℝ := fun t =>
    Set.indicator (Icc (-4 : ℝ) 4) (fun _ => M0) t +
      K * ((1 + |t|) * Real.exp (-c * t ^ 2))
  have hind : Integrable
      (Set.indicator (Icc (-4 : ℝ) 4) (fun _ : ℝ => M0)) :=
    (continuousOn_const.integrableOn_compact isCompact_Icc).integrable_indicator
      measurableSet_Icc
  have hlog := (integrable_one_add_abs_mul_gaussian hc).const_mul K
  have hmaj : Integrable g := hind.add hlog
  have hbd : ∀ t, ‖f t‖ ≤ g t := by
    intro t
    have hlognn : 0 ≤ K * ((1 + |t|) * Real.exp (-c * t ^ 2)) :=
      mul_nonneg hK0
        (mul_nonneg (add_nonneg (by norm_num) (abs_nonneg _))
          (Real.exp_pos _).le)
    have hindnn : 0 ≤
        Set.indicator (Icc (-4 : ℝ) 4) (fun _ => M0) t :=
      Set.indicator_apply_nonneg (fun _ => hM0nn)
    by_cases ht : |t| ≤ 4
    · have hmem : t ∈ Icc (-4 : ℝ) 4 := abs_le.mp ht
      have : Set.indicator (Icc (-4 : ℝ) 4) (fun _ => M0) t = M0 :=
        Set.indicator_of_mem hmem (fun _ => M0)
      have hf : ‖f t‖ ≤ M0 := hM0 t hmem
      simpa [g, this] using le_add_of_le_of_nonneg hf hlognn
    · have hge : (4 : ℝ) ≤ |t| := le_of_lt (lt_of_not_ge ht)
      have hω := norm_gaborArchDensity_le_of_two_le_half_abs hge
      have hh := hhat (1 / 2) t le_rfl le_rfl
      have hnot : t ∉ Icc (-4 : ℝ) 4 := fun h => ht (abs_le.mpr h)
      have : Set.indicator (Icc (-4 : ℝ) 4) (fun _ => M0) t = 0 :=
        Set.indicator_of_notMem hnot (fun _ => M0)
      have hfn : ‖f t‖ =
          |gaborArchDensity t| *
            ‖gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)‖ := by
        simp [f, norm_mul, Complex.norm_real]
      have hlogarg : 1 + Real.log (2 + |t / 2|) ≤ 1 + |t| := by
        have hpos : 0 < 2 + |t / 2| := by positivity
        have hle : Real.log (2 + |t / 2|) ≤ 1 + |t / 2| :=
          le_trans (Real.log_le_sub_one_of_pos hpos) (by linarith)
        have h2 : (2 : ℝ) ≤ |t| := le_trans (by norm_num : (2 : ℝ) ≤ 4) hge
        have hhalf : 1 + |t / 2| ≤ |t| := by
          have hdiv : |t / 2| = |t| / 2 := by
            rw [abs_div, abs_of_pos (by norm_num : (0 : ℝ) < 2)]
          rw [hdiv]
          linarith
        linarith
      have hω' : |gaborArchDensity t| ≤
          (Cψ + 1 / 2 + |Real.log Real.pi|) * (1 + |t|) := by
        have h1 : (1 : ℝ) ≤ 1 + |t| := le_add_of_nonneg_right (abs_nonneg _)
        have hCψ : Cψ * (1 + Real.log (2 + |t / 2|)) ≤ Cψ * (1 + |t|) :=
          mul_le_mul_of_nonneg_left hlogarg hCψ0
        have hhalf : (1 / 2 : ℝ) ≤ (1 / 2) * (1 + |t|) :=
          le_mul_of_one_le_right (by norm_num) h1
        have hlogπ : |Real.log Real.pi| ≤ |Real.log Real.pi| * (1 + |t|) :=
          le_mul_of_one_le_right (abs_nonneg _) h1
        have hsum :
            Cψ * (1 + Real.log (2 + |t / 2|)) + 1 / 2 + |Real.log Real.pi| ≤
              Cψ * (1 + |t|) + (1 / 2) * (1 + |t|) +
                |Real.log Real.pi| * (1 + |t|) :=
          add_le_add (add_le_add hCψ hhalf) hlogπ
        have hrhs :
            Cψ * (1 + |t|) + (1 / 2) * (1 + |t|) +
                |Real.log Real.pi| * (1 + |t|) =
              (Cψ + 1 / 2 + |Real.log Real.pi|) * (1 + |t|) := by
          ring
        exact (hω.trans hsum).trans_eq hrhs
      have hf : ‖f t‖ ≤ K * ((1 + |t|) * Real.exp (-c * t ^ 2)) := by
        rw [hfn]
        have hmul :
            |gaborArchDensity t| *
                ‖gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)‖ ≤
              (Cψ + 1 / 2 + |Real.log Real.pi|) * (1 + |t|) *
                (C * Real.exp (-c * t ^ 2)) :=
          mul_le_mul hω' hh (norm_nonneg _)
            (mul_nonneg (add_nonneg (add_nonneg hCψ0 (by norm_num))
              (abs_nonneg _)) (add_nonneg (by norm_num) (abs_nonneg t)))
        refine hmul.trans_eq ?_
        unfold K
        ring
      simpa [g, this] using le_add_of_nonneg_of_le hindnn hf
  exact hmaj.mono' (continuous_arch_critical_integrand F).aestronglyMeasurable
    (Eventually.of_forall hbd)

theorem gaborArchCriticalPairingReal_holds :
    GaborArchCriticalPairingReal := by
  intro F hF
  have hf := integrable_arch_critical_integrand hF
  have hre := integral_re (𝕜 := ℂ) hf
  have hpt : ∀ t : ℝ,
      RCLike.re ((gaborArchDensity t : ℂ) *
          gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)) =
        (gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)).re *
          gaborArchDensity t := fun t => by
    change ((gaborArchDensity t : ℂ) *
        gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)).re = _
    rw [ofReal_mul_re, mul_comm]
  have hcast :
      (∫ t : ℝ, (gaborArchDensity t : ℂ) *
          gaborHat F ((1 / 2 : ℂ) + t * Complex.I)) =
        ∫ t : ℝ, (gaborArchDensity t : ℂ) *
          gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I) := by
    refine integral_congr_ae (Eventually.of_forall fun t => ?_)
    dsimp
    rw [gaborHat_critical_cast]
  have hcastRe :
      (∫ t : ℝ, (gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re *
          gaborArchDensity t) =
        ∫ t : ℝ, (gaborHat F (((1 / 2 : ℝ) : ℂ) + t * Complex.I)).re *
          gaborArchDensity t := by
    refine integral_congr_ae (Eventually.of_forall fun t => ?_)
    dsimp
    rw [gaborHat_critical_cast]
  rw [hcast, hcastRe]
  exact hre.symm.trans (integral_congr_ae (Eventually.of_forall hpt))

theorem gaborArchDigammaIdentification_of_parts
    (hshift : GaborArchContourShift)
    (hre : GaborArchCriticalPairingReal) :
    GaborArchDigammaIdentification := by
  intro F hFadm hF
  have hshiftF := hshift F hFadm hF
  have hπ : (2 * (Real.pi : ℂ)) ≠ 0 :=
    mul_ne_zero (by norm_num : (2 : ℂ) ≠ 0)
      (ofReal_ne_zero.mpr Real.pi_ne_zero)
  have hπc : (2 * (Real.pi : ℂ)) = ((2 * Real.pi : ℝ) : ℂ) := by
    norm_cast
  have hsplit :
      gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ)) =
        gaborHat F 0 +
          (∫ t : ℝ, (gaborArchDensity t : ℂ) *
              gaborHat F ((1 / 2 : ℂ) + t * Complex.I)) /
            (2 * (Real.pi : ℂ)) := by
    rw [hshiftF, add_div, mul_div_cancel_left₀ _ hπ]
  have hdiv :
      ((∫ t : ℝ, (gaborArchDensity t : ℂ) *
            gaborHat F ((1 / 2 : ℂ) + t * Complex.I)) /
          (2 * (Real.pi : ℂ))).re =
        (1 / (2 * Real.pi)) *
          (∫ t : ℝ, (gaborArchDensity t : ℂ) *
              gaborHat F ((1 / 2 : ℂ) + t * Complex.I)).re := by
    rw [hπc, div_ofReal_re, div_eq_inv_mul]
    simp [one_div]
  rw [gaborArchSide_eq_density_pairing, hsplit, Complex.add_re, hdiv, hre F hF]

#print axioms zetaFEFactor_eq_Gammaℝ_div
#print axioms logDeriv_zetaFEFactor_criticalLine
#print axioms gaborArchCriticalPairingReal_holds
#print axioms gaborArchDigammaIdentification_of_parts

end RH
