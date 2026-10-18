/-
RH/FaithfulFold.lean -- PRODUCTIVE TRANSCRIPTION OF THE r459 WINDOW
(r463, PRIME.RDAGGER.LEAN_FIDELITY_REPAIR.01).

This module transcribes the production object in the order used by
`fullcomb_cleanup_probe.py` / `verify_lstar_instance.py`:

  source atoms -> triangular prime lags -> total lags
  -> circulant spectral density -> grid fold -> sign split.

The geometry is exact: `M = m + 1`, `L = 2 M - 2`, grid indices
`j = 1,...,L/2`, and the endpoint `j=L/2` receives the half weight.
The resulting positive and negative spectral weights are respectively
the `combWeight` and `archWeight` channels of a `PrimeWindow`, so
`combHankel` is the production positive-measure Hankel matrix rather
than the old raw-prime-power Hankel matrix.

The classical values not yet formalized are isolated in explicit
interfaces: `productionArchLag` is exactly the vector returned by
Python `arch_lags(M, Delta)`; `ProductionCompletion.border` is the
v958 production border column; `budget` is the r243 scalar.  No
per-atom `canonicalCompletion` enters this object.

Claim boundary: research documentation.  NO RH CLAIM.
-/
import RH.Elementwise
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace RH

open scoped BigOperators

/-- Production dimensions.  In particular `productionL m = 2m`, hence
the non-duplicated folded grid has exactly `m` points. -/
def productionM (m : ℕ) : ℕ := m + 1
def productionL (m : ℕ) : ℕ := 2 * productionM m - 2

theorem productionL_eq_two_mul (m : ℕ) : productionL m = 2 * m := by
  simp [productionL, productionM, Nat.mul_add]

/-- Lag spacing `Delta = log(a)/M`. -/
noncomputable def productionDelta (a m : ℕ) : ℝ :=
  Real.log a / productionM m

/-- The triangular interpolation kernel used by `lags_from_rows`. -/
noncomputable def productionTent (Δ x : ℝ) : ℝ :=
  max 0 (1 - |x| / Δ)

/-- Exact arithmetic lag contribution.  The two tent terms are the
ordinary and reflected (`u < Delta`) contributions; the latter
vanishes automatically outside its support.  Since
`combMass n = 2 Λ(n)/sqrt(n)`, multiplication by `1/2` is exactly the
Python weight `Λ(n)/sqrt(n)`. -/
noncomputable def exactPrimeLag (a m i : ℕ) : ℝ :=
  -∑ n ∈ windowAtoms a,
    (combMass n / 2) *
      (productionTent (productionDelta a m)
          (i * productionDelta a m - Real.log n) +
       productionTent (productionDelta a m)
          (i * productionDelta a m + Real.log n))

/-- Explicit interface for the border/budget production values whose
analytic construction is still external to Lean.

* `border` is the v958 smooth-border column after the same fold;
* `budget = sum rho + 5/7`, hence positive.
-/
structure ProductionCompletion where
  border : ℕ → ℝ
  budget : ℝ
  budget_pos : 0 < budget

instance : Inhabited ProductionCompletion :=
  ⟨⟨fun _ => 0, 1, one_pos⟩⟩

/-- The one remaining external value interface for the faithful
builder.  Its fields and intended equations are explicit above. -/
opaque productionCompletion : ℕ → ℕ → ProductionCompletion

/-- Total lag vector `cA + cP`. -/
noncomputable def exactProductionLag (a m i : ℕ) : ℝ :=
  productionArchLag a m i + exactPrimeLag a m i

/-- Grid angle `theta_j`, with Lean index `j=0,...,m-1`
representing Python index `j+1=1,...,L/2`. -/
noncomputable def productionTheta (m : ℕ) (j : Fin m) : ℝ :=
  2 * Real.pi * ((j : ℕ) + 1) / productionL m

/-- Circulant spectral density
`d(theta)=c0+2 sum_{r=1}^{M-2} c_r cos(r theta)
             +c_{M-1} cos((M-1) theta)`. -/
noncomputable def exactSpectralDensity (a m : ℕ) (j : Fin m) : ℝ :=
  exactProductionLag a m 0 +
    2 * ∑ r ∈ Finset.Icc 1 (m - 1),
      exactProductionLag a m r * Real.cos (r * productionTheta m j) +
    exactProductionLag a m m * Real.cos (m * productionTheta m j)

/-- Folded signed weight.  The `j=L/2` endpoint is its own mirror and
therefore receives the production factor `1/2`. -/
noncomputable def exactSignedFoldWeight (a m : ℕ) (j : Fin m) : ℝ :=
  let raw :=
    (2 / productionL m : ℝ) *
      (1 - Real.cos (productionTheta m j)) *
      exactSpectralDensity a m j
  if (j : ℕ) + 1 = m then raw / 2 else raw

/-- Positive and negative parts of the signed folded measure. -/
noncomputable def exactPositiveFoldWeight (a m : ℕ) (j : Fin m) : ℝ :=
  max (exactSignedFoldWeight a m j) 0

noncomputable def exactNegativeFoldWeight (a m : ℕ) (j : Fin m) : ℝ :=
  max (-exactSignedFoldWeight a m j) 0

theorem exactPositiveFoldWeight_nonneg (a m : ℕ) (j : Fin m) :
    0 ≤ exactPositiveFoldWeight a m j :=
  le_max_right _ _

theorem exactNegativeFoldWeight_nonneg (a m : ℕ) (j : Fin m) :
    0 ≤ exactNegativeFoldWeight a m j :=
  le_max_right _ _

/-- **The faithful production fold.**  The support is the production
grid itself.  Zero numerical weights are retained: dropping values
below Python's `1e-300` threshold is a floating implementation detail,
not part of the mathematical object. -/
noncomputable def productionFold (a m : ℕ) : PrimeWindow where
  S := m
  nodes := fun j => Real.cos (productionTheta m j)
  combWeight := exactPositiveFoldWeight a m
  archWeight := exactNegativeFoldWeight a m
  comb_nonneg := exactPositiveFoldWeight_nonneg a m
  arch_nonneg := exactNegativeFoldWeight_nonneg a m
  lo := -1
  hi := 1
  window_rule := fun j => ⟨Real.neg_one_le_cos _, Real.cos_le_one _⟩
  u := (productionCompletion a m).border
  B := (productionCompletion a m).budget

theorem productionFold_B_pos (a m : ℕ) :
    0 < (productionFold a m).B :=
  (productionCompletion a m).budget_pos

theorem productionFold_support (a m : ℕ) :
    (productionFold a m).S = productionL m / 2 := by
  simp [productionFold, productionL_eq_two_mul]

end RH
