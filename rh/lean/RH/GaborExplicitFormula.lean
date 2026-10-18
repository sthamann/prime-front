/-
RH/GaborExplicitFormula.lean -- r558 wiring of the r557 EF bricks.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not prove
`GaborExplicitFormula`.  It records the missing vertical/Schwartz
remainder and proves the implication from named remainders to EF.

r557 delivered, sorry-free:
  * `gabor_contour_identity_fixed_T`          (any even quartic)
  * `gabor_horizontal_edges_tendsto_zero`     (pure)
  * `summable_gaborHat_over_zeros`            (pure)
  * `GaborContourLimitRemainder`              (r576 theorem)

r581 closed the pure-class vertical identification
(`gabor_vertical_arithmetic_remainder`).  What remains, and is not
in Mathlib v4.29.1, is the same identification for a general even
quartic (`GaborHatQuarticExplicitRemainder`).

r581 discharges `gabor_vertical_arithmetic_remainder` from
`gaborArchDigammaIdentification_holds` (T→∞ arch contour shift).
r576 closed the Landau-gap contour T→∞ glue
(`gaborContourVerticalLimit_holds`).
-/
import RH.GaborContourResidue
import RH.GaborHorizontalEdges
import RH.GaborLeftVertical
import RH.GaborAutocorrelation
import RH.GaborVerticalLimit
import RH.GaborArchContour

namespace RH

open Complex Filter MeasureTheory
open scoped Topology

/-- Vertical-edge / Schwartz-inversion remainder after the r557 bricks.

Given a Landau-gap height sequence along which the fixed-`T` residue
identity holds and the spectral partial sums exhaust the zero series,
plus the already-proved horizontal vanishing and pure-zero summability,
the two improper vertical integrals of `(ζ′/ζ) ĥ_W` must still be
identified with
`gaborPoleSide − gaborPrimeComb + gaborArchSide`.
That identification is the missing analytic step (Schwartz Fourier
inversion + left-edge Digamma fold for a noncompact packet). -/
def GaborVerticalArithmeticRemainder : Prop :=
  ∀ F : GaborWeilTest, F.admissible → F.coeffs = ⟨1, 0, 0⟩ →
    ∀ T : ℕ → ℝ,
      Tendsto T atTop atTop →
      (∀ k, 0 < T k) →
      (∀ k, ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 (T k),
        |ρ.im| < T k) →
      (∀ k,
        rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
          (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
          (((2 : ℝ) : ℂ) + (T k : ℝ) * I) =
          (2 * (Real.pi : ℂ) * I) *
            (spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k) -
              gaborHat F 1)) →
      Tendsto (fun k =>
        spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k))
        atTop
        (nhds
          (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
            (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ)) →
      GaborHorizontalEdgesTendstoZero →
      (Summable fun ρ : {z : ℂ // IsCriticalStripZetaZero z} =>
        gaborHat F (ρ : ℂ)) →
      gaborZeroSide F =
        gaborPoleSide F - gaborPrimeComb F + gaborArchSide F

/-- Quartic lift of the explicit formula, once coefficient-dependent
strip majorants and the same vertical identification are available.
Unasserted.  Not a `sorry`. -/
def GaborHatQuarticExplicitRemainder : Prop :=
  ∀ F : GaborWeilTest, F.admissible → F.coeffs ≠ ⟨1, 0, 0⟩ →
    gaborZeroSide F =
      gaborPoleSide F - gaborPrimeComb F + gaborArchSide F

/-- Fixed-`T` residue identity along any positive height sequence
that avoids ordinates.  Thin wrapper around the r557 theorem. -/
theorem gabor_contour_identity_along
    (F : GaborWeilTest) {T : ℕ → ℝ}
    (hTpos : ∀ k, 0 < T k)
    (hord : ∀ k, ∀ ρ ∈ riemannZetaZerosOnClosedRect (-1 / 16) 2 (T k),
      |ρ.im| < T k) (k : ℕ) :
    rectangleIntegral (fun ζ => logDeriv riemannZeta ζ * gaborHat F ζ)
      (((-1 / 16 : ℝ) : ℂ) + (-(T k) : ℝ) * I)
      (((2 : ℝ) : ℂ) + (T k : ℝ) * I) =
      (2 * (Real.pi : ℂ) * I) *
        (spectralPartialSum (gaborHat F) (-1 / 16) 2 (T k) -
          gaborHat F 1) :=
  gabor_contour_identity_fixed_T F (hTpos k) (hord k)

/-- Pure-class EF from the r557 bricks plus the two named remainders.
Sorry-free: every r557 theorem is invoked as a proof term. -/
theorem gabor_explicitFormula_pure_of_remainders
    {F : GaborWeilTest} (hFadm : F.admissible)
    (hF : F.coeffs = ⟨1, 0, 0⟩)
    (hlim : GaborContourLimitRemainder)
    (hvert : GaborVerticalArithmeticRemainder) :
    gaborZeroSide F =
      gaborPoleSide F - gaborPrimeComb F + gaborArchSide F := by
  obtain ⟨T, hTtop, hTpos, hord, hspec⟩ := hlim F hF
  exact hvert F hFadm hF T hTtop hTpos hord
    (gabor_contour_identity_along F hTpos hord)
    hspec
    gabor_horizontal_edges_tendsto_zero
    (summable_gaborHat_over_zeros hF)

/-- r558: EF for every even-quartic Gabor test, from the named
remainders.  Pure tests use the r557 bricks; other quartics use
`GaborHatQuarticExplicitRemainder`.  Sorry-free. -/
theorem gabor_explicitFormula_of_remainders
    (hlim : GaborContourLimitRemainder)
    (hvert : GaborVerticalArithmeticRemainder)
    (hquart : GaborHatQuarticExplicitRemainder) :
    GaborExplicitFormula := by
  intro F hFadm
  by_cases hpure : F.coeffs = ⟨1, 0, 0⟩
  · exact gabor_explicitFormula_pure_of_remainders hFadm hpure hlim hvert
  · exact hquart F hFadm hpure

/-- r576: the vertical arithmetic remainder follows from the proved
right inversion, left reflection, ACF closed form, half-comb
real-part identification, and the Landau-gap contour T→∞ glue,
together with the named Digamma fold.  Sorry-free implication.
The remaining named input is the Digamma identification. -/
theorem gabor_vertical_arithmetic_of_parts
    (harch : GaborArchDigammaIdentification) :
    GaborVerticalArithmeticRemainder := by
  intro F hFadm hF _T _hTtop _hTpos _hord _hrect _hspec _hhoriz _hsum
  have hr := gabor_rightVerticalIntegral_eq_prime_sum hF
  have hl := gabor_leftVerticalIntegral_eq_reflected_prime_sub_arch hF
  have hc := gaborContourVerticalLimit_holds F hF
  have ha := harch F hFadm hF
  have hh := gaborHalfCombReal_holds F hF
  have href := gaborReflectedHalfPrimeComb_eq_half F
  have hI :
      (2 * (Real.pi : ℂ) * I) *
          ((∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
              (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) -
            gaborHat F 1) =
        I • (-(2 * Real.pi : ℂ) * gaborHalfPrimeComb F) -
          I • ((2 * Real.pi : ℂ) * gaborReflectedHalfPrimeComb F -
            gaborLeftEdgeArchIntegral F) := by
    rw [← hc, hr, hl]
  rw [href, smul_eq_mul, smul_eq_mul] at hI
  have hcancel :
      I * (-(2 * Real.pi : ℂ) * gaborHalfPrimeComb F) -
        I * ((2 * Real.pi : ℂ) * gaborHalfPrimeComb F -
          gaborLeftEdgeArchIntegral F) =
      I * gaborLeftEdgeArchIntegral F -
        (4 * Real.pi : ℂ) * I * gaborHalfPrimeComb F := by
    ring
  rw [hcancel] at hI
  have hπ : (2 * (Real.pi : ℂ)) ≠ 0 :=
    mul_ne_zero (by norm_num : (2 : ℂ) ≠ 0)
      (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero)
  have hπI : (2 * (Real.pi : ℂ) * I) ≠ 0 :=
    mul_ne_zero hπ Complex.I_ne_zero
  have hRHS :
      I * gaborLeftEdgeArchIntegral F -
          (4 * Real.pi : ℂ) * I * gaborHalfPrimeComb F =
        (2 * (Real.pi : ℂ) * I) *
          (gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ)) -
            (2 : ℂ) * gaborHalfPrimeComb F) := by
    field_simp [hπ]
    ring
  have hZ :
      (∑' ρ : {z : ℂ // IsCriticalStripZetaZero z},
          (riemannZetaMultiplicity (ρ : ℂ) : ℂ) * gaborHat F ρ) -
        gaborHat F 1 =
      gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ)) -
        (2 : ℂ) * gaborHalfPrimeComb F := by
    apply mul_left_cancel₀ hπI
    exact hI.trans hRHS
  have hZre :
      gaborZeroSide F - (gaborHat F 1).re =
        (gaborLeftEdgeArchIntegral F / (2 * (Real.pi : ℂ))).re -
          (2 * gaborHalfPrimeComb F).re := by
    unfold gaborZeroSide
    have hre := congrArg Complex.re hZ
    rw [← Complex.sub_re, hre, Complex.sub_re]
  have h2re : (2 * gaborHalfPrimeComb F).re =
      2 * (gaborHalfPrimeComb F).re := by
    rw [Complex.mul_re]
    simp
  rw [ha, h2re, hh] at hZre
  unfold gaborPoleSide
  have hP : (gaborHat F 0 + gaborHat F 1).re =
      (gaborHat F 0).re + (gaborHat F 1).re :=
    Complex.add_re _ _
  -- Zero = Re ĥ(1) + Re ĥ(0) + Arch − Comb = Pole − Comb + Arch
  linarith [hP, hZre]

/-- r581: vertical identification for pure packets.  The Digamma fold
is `gaborArchDigammaIdentification_holds`.  Contour T→∞ glue is
`gaborContourVerticalLimit_holds`.  NO RH CLAIM. -/
theorem gabor_vertical_arithmetic_remainder :
    GaborVerticalArithmeticRemainder :=
  gabor_vertical_arithmetic_of_parts gaborArchDigammaIdentification_holds

/-- r634L: pure-class explicit formula, unconditional; both named
remainders discharged (r576/r581).  NO RH CLAIM. -/
theorem gabor_explicitFormula_pure {F : GaborWeilTest}
    (hFadm : F.admissible) (hF : F.coeffs = ⟨1, 0, 0⟩) :
    gaborZeroSide F =
      gaborPoleSide F - gaborPrimeComb F + gaborArchSide F :=
  gabor_explicitFormula_pure_of_remainders hFadm hF
    gaborContourLimitRemainder_holds gabor_vertical_arithmetic_remainder

#print axioms gabor_explicitFormula_pure
#print axioms gabor_vertical_arithmetic_of_parts
#print axioms gabor_vertical_arithmetic_remainder
#print axioms gaborContourVerticalLimit_holds
#print axioms gaborAutocorrelationClosedForm_holds
#print axioms gaborHalfCombReal_holds

end RH
