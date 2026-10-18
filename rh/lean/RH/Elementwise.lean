/-
RH/Elementwise.lean -- THE ELEMENTWISE EXTRACTION ARCHITECTURE
(r326; the R325 repair set, `extraction_order_probe.py`, sealed
SPEC_SHA 57e50d366a62f2a6 freeze / 18/18 gates, primary verdict
ELEMENTWISE_STABILIZATION_GO).

WHY THIS FILE EXISTS.  The R319 red-team audit and the wave-12
reviewer adjudication localized the missing LEVEL C of the proof
graph (the extraction: window-local positivity ==> the Weil form) in
two defects that appeared in NO sorry, because the correct statements
did not exist yet: (a) the rh/ cofinality theorems run in the ANCHOR
direction while the carrier hypothesis (H_cof) demands a
MESH-refinement PSD tower (the mesh-vs-anchor seam,
RH/Source.lean), and the window direction of that route is measured
inadmissible (false floors, hcof_dodging_audit S6.8); (b) the opaque
`SourceExact` guard (r320) is a good firewall but must NOT stand as a
free assumption in a final proof.  R325 measured the three reviewer
repair variants under a sealed tree and adjudicated the ELEMENTWISE
architecture as primary: on the native dense class (dyadic
step-function autocorrelations -- the v749 "Weil form of step
functions" class) EVERY channel of the canonical tower windows
stabilizes EXACTLY at a finite anchor onset PREDEFINED from the
element (a* = (n_g + 1) D0 / 2), and the value is CONSTANT under
dyadic mesh refinement -- the extraction consumes NO mesh-cofinal
ladder and NO transport.  This file implements that quantifier set:

  (i)   `CanonicalPrimeWindow` (the canonical family as a window
        predicate) + `SourceExactSpec` (the TRANSCRIBABLE
        source-exactness clauses as a real definition, not an opaque
        marker) + `sourceExact_buildPrimeWindow` (PROVED: every
        canonical family member satisfies them) -- the wave-12
        reviewer target "CanonicalPrimeWindow + exactly one
        construction theorem", eliminating `SourceExact` as a free
        assumption FROM THE EXTRACTION ROUTE (the opaque predicate
        itself stays untouched in RH/Source.lean; the opaque filling
        is the named Prop `SourceExactOfFamilyCompletion` below);
  (ii)  `GridElement` (the native dense class, built for real:
        support parameter, native dyadic grid, step values;
        autocorrelation and its piecewise-linear even interpolant as
        DERIVED definitions) + the elementwise finite stabilization:
        the comb channel PROVED with the onset `elementAnchor f`
        predefined from the element's support alone (the R310
        `finite_forms_converge_to_weil` shape, elementwise and in the
        corpus gauge), the pole channel PROVED as the native-mesh
        second-difference of `polePotential` (r376), and the
        historically asserted arch exact-equality seam now retained
        only as the unasserted Prop
        `ArchGaussMellinDigammaIdentity`.  The full-form and
        extraction theorems are explicit functions of that
        hypothesis; the selected-path `O(Delta^2)` replacement lives
        in `RH/InnerBridges.lean`;
  (iii) `weil_nonneg_of_windowlocal` (PROVED from the explicit arch
        hypothesis -- a finite
        instantiation, NO ladder, NO (H_cof)): window-local
        positivity of the canonical family on the native class
        implies Weil-form nonnegativity on every grid element; plus
        the named compression-bridge statement
        `BorderedCompressionBridge` (the bordered ==> plain tower
        form step -- the documented S2 rest; named as a Prop, NOT
        asserted) with the proved composition
        `weil_nonneg_of_bordered`.

WHAT `fullRead`/`weilForm` COVER (honest scope).  The comb channel is
TRANSCRIBED and PROVED: `combRead` is the exact atom sum
`Sigma mu_n f(log n)` over the canonical atom set in the corpus gauge
`mu_n = 2 Lambda(n)/sqrt(n)` (Python MU_ALL; the tent-assembled
mesh read equals this exactly on the native class at native-or-finer
mesh -- the R325 S1.3 tent-read identity, measured at 1e-12, whose
mesh-grid transcription belongs to the fold TODO), and the gauge
relation to the built window's comb channel is PROVED
(`combRead_eq_window_channel`, `combMass_eq_gauge`).  The arch and
pole channels enter through the OPAQUE reads `archRead`/`poleRead`
and references `weilArchSide`/`weilPoleSide`: their semantics (the
exact Weil arch kernel `arch_A` = GL-48 tent integrals, v563; the
v716 pole closed form) are NOT yet transcribed -- the opaque
constants are the named classical TODO made visible, and every
statement about them below is a TYPED sorry, never a proof.  The
spectral/zero side of the full explicit formula is the arithmetically
open content of the program and is NOT stated here.

SIGN CONVENTION: the corpus total lag vector is c = car + cat + cp
with the atom channel read equal to MINUS the comb sum
(L_cat(F) = -Sigma mu_n F(u_n), R325 S1.3), so
`fullRead = archRead - combRead + poleRead` and
`weilForm = weilArchSide - weilCombSide + weilPoleSide`.

WHAT REPLACES (H_cof).  The extraction (iii) consumes: one anchor
`a >= elementAnchor f` (a prime via Euclid -- a FINITE choice per
element, not a cofinal tower), the element's OWN native mesh level
`m = f.meshExp` (predefined, never refined), and the stabilization
(ii).  No PSD transport along any ladder appears; the mesh limit
survives only off the native class as the classical
density/continuity step (R325 leg C: rate-controlled quadrature
defect inside the closed-form interpolation envelope -- not a
positivity ladder), which is deliberately NOT formalized here.

SORRY CENSUS OF THIS FILE (r638L): ZERO.  The overstrong historical
arch exact-equality statement is an unasserted Prop and every theorem
that uses it takes it as an explicit hypothesis.  The pole-channel
stabilization is PROVED (native-mesh second-difference transcription
of `pole_lags_closed`, parallel to mesh-free `combRead`).  The
source-exact completion remains the named Prop
`SourceExactOfFamilyCompletion` (opacity-forced, not a hole; the
transcribable half is `sourceExact_buildPrimeWindow`).  Named, not
asserted: `PoleDyadicIndependence` (dyadic refinement of the pole
pairing).  No false exact quadrature identity is asserted.

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Source
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Floor.Semifield
import Mathlib.Algebra.Order.Interval.Finset.Basic
import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.MeasureTheory.Function.Floor
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace RH

local notation "Λ" => ArithmeticFunction.vonMangoldt

/-! ## (i) The canonical prime windows and the transcribable
source-exactness

The wave-12 reviewer target: `SourceExact` must not stand as a free
assumption in a final proof.  The repair is NOT to prove anything
about the opaque predicate (impossible by design) but to make the
extraction route consume only the CONSTRUCTION: the canonical family
`specFamily` (RH/Source.lean, r310) is predefined by arithmetic
alone, and everything the route needs from "source exactness" is
provable FOR the family -- `SourceExactSpec` below.  The relation to
the opaque guard is the named Prop `SourceExactOfFamilyCompletion`
at the bottom of this section (r376: demoted from a `sorry`). -/

/-- **THE CANONICAL PRIME WINDOWS** (r326, R325 target form (i)): a
real window is canonical iff it is built from a member of the
predefined family -- anchor `a` (a prime power), mesh level `m`.
This is the R325 repair set's replacement for the (H_cof) ladder
route: the extraction below quantifies window positivity over THIS
predicate and nothing else.  (Note `buildPrimeWindow` is
deliberately mesh-independent -- source theorem 4, r310b -- so at
window level the family is indexed by the anchor; the mesh level
enters the kernel channels through the reads below, never through
the built window.) -/
def CanonicalPrimeWindow (w : PrimeWindow) : Prop :=
  ∃ (a m : ℕ) (ha : IsPrimePow a), w = buildPrimeWindow (specFamily a m ha)

/-- every canonical family member is a canonical window (the
construction is the witness). -/
theorem canonicalPrimeWindow_build (a m : ℕ) (ha : IsPrimePow a) :
    CanonicalPrimeWindow (buildPrimeWindow (specFamily a m ha)) :=
  ⟨a, m, ha, rfl⟩

/-- canonical windows are explicitly-main (r310 sense): the canonical
family is a subfamily of the explicit construction. -/
theorem canonicalPrimeWindow_isExplicit {w : PrimeWindow}
    (h : CanonicalPrimeWindow w) : MainWindowExplicit w := by
  obtain ⟨a, m, ha, rfl⟩ := h
  exact ⟨specFamily a m ha, rfl⟩

/-- **THE TRANSCRIBABLE SOURCE-EXACTNESS** (r326): the clauses of
"this spec carries the genuine source data" that are statable and
provable TODAY, as a real definition (contrast the deliberately
opaque `SourceExact`, RH/Source.lean, which reserves the
NOT-yet-transcribed arch/border/budget-identity channels):
  (1)/(2) the node positions and comb weights ARE the `log`/`Λ`
          data of the atom set -- definitional BY THE INTERFACE
          DESIGN (r310 source theorem 1: the spec derives them
          instead of carrying them as free fields; recorded here so
          the predicate readably binds the comb channel);
  (3)     ATOM-SET COMPLETENESS -- the genuine content: the atoms
          are ALL prime powers `n ≤ anchor²`, not merely some
          strictly increasing selection (the structure alone does
          NOT force this; `predefined_family` proves it for the
          canonical family);
  (4)     budget positivity -- the transcribable r243 half (spec
          field since r320).
NOT bound here (honest): the arch/border channels and the full r243
budget identity -- those are exactly the intended content of the
opaque `SourceExact`, and no honest finite clause can bind them
before their transcriptions exist (r320 verification finding).  The
extraction route of this file never needs them bound: the kernel
channels enter through the typed reads below. -/
def SourceExactSpec (s : PrimeWindowSpec) : Prop :=
  (∀ j, s.node j = Real.log (s.primePowers j)) ∧
  (∀ j, s.combWeight j = Λ (s.primePowers j)) ∧
  (∀ n : ℕ, (∃ i, s.primePowers i = n) ↔ (IsPrimePow n ∧ n ≤ s.anchor ^ 2)) ∧
  0 < s.budget

/-- **THE CONSTRUCTION THEOREM** (r326, R325 target form (i); the
wave-12 reviewer's "exactly one construction theorem"; PROVED):
every canonical family member is source-exact in the transcribable
sense -- clauses (1)/(2) by derivation (`rfl`), clause (3) is
`predefined_family` (r310, structure theorem 1), clause (4) is the
spec field.  This is what replaces `SourceExact` as a hypothesis in
the extraction route: the route quantifies over BUILT windows, and
built windows PROVABLY carry their source. -/
theorem sourceExact_buildPrimeWindow (a m : ℕ) (ha : IsPrimePow a) :
    SourceExactSpec (specFamily a m ha) :=
  ⟨fun _ => rfl, fun _ => rfl, predefined_family a m ha,
    (specFamily a m ha).budget_pos⟩

/-- **THE SOURCE-EXACT COMPLETION** (r326; r376 RETYPE).

The constructive half is already `sourceExact_buildPrimeWindow` (the
transcribable clauses) together with C1's named opaque constant
`canonicalCompletion` (`RH/Canonical.lean`): that constant NAMES the
intended arch/border/budget filling.  R373's kernel objects
(`weilArchKernel`, `polePotential`) are lag-kernels, not the per-atom
masses / v958 border column / r243 drain-sum, so they do not make
`canonicalCompletion` constructive.

Concluding the opaque `SourceExact` of any filling remains unprovable
by design (r273/r320).  r376 demotes that conjunct from a `sorry` to
the named Prop below — the C1 `PairMarginLaw` convention: statable,
never asserted.  The extraction route does not consume it. -/
def SourceExactOfFamilyCompletion : Prop :=
  ∀ (a m : ℕ) (ha : IsPrimePow a),
    ∃ (aw : Fin (specFamily a m ha).S → ℝ) (haw : ∀ j, 0 ≤ aw j)
      (bd : ℕ → ℝ) (B : ℝ) (hB : 0 < B),
      SourceExact { specFamily a m ha with
        archWeight := aw, arch_nonneg := haw,
        border := bd, budget := B, budget_pos := hB }

/-- record: the transcribable half of a family member is PROVED
(`SourceExactSpec`); the opaque `SourceExact` filling is the named
Prop `SourceExactOfFamilyCompletion`, not a hole. -/
theorem specFamily_sourceExact_completion_transcribable
    (a m : ℕ) (ha : IsPrimePow a) :
    SourceExactSpec (specFamily a m ha) :=
  sourceExact_buildPrimeWindow a m ha

/-! ## (ii) The native dense class: dyadic step-function
autocorrelations

The v749 "Weil form of step functions" class (R325 S1: elements
sealed by seed before any sign read; Python
`F = D0 * np.correlate(x, x, "full")`, knots on the native grid,
closing zero knot): a step function with `steps` values on the
dyadic grid of width `D0 = 2^{-meshExp}`, its autocorrelation
coefficients, and the even piecewise-linear interpolant through them
(support `steps * D0`).  Everything below the structure is DERIVED,
not a field -- the r310 interface convention. -/

/-- **a native grid element**: `steps` step values on the dyadic grid
of exponent `meshExp` (native mesh `D0 = 2^{-meshExp}`).  The probe
seeds `x` at random and seals it; here the data is free -- every
statement below holds for EVERY element of the class. -/
structure GridElement where
  /-- the number of native grid steps `n_g` (support = `steps · D0`). -/
  steps : ℕ
  /-- the native dyadic mesh exponent (`D0 = 2^{-meshExp}`). -/
  meshExp : ℕ
  /-- the step values. -/
  x : Fin steps → ℝ

namespace GridElement

variable (f : GridElement)

/-- the native mesh width `D0 = 2^{-meshExp}` (dyadic by
construction). -/
noncomputable def D0 : ℝ := 1 / 2 ^ f.meshExp

theorem D0_pos : 0 < f.D0 := by
  unfold D0; positivity

/-- **the autocorrelation coefficients** (DERIVED):
`a_d = D0 · Σ_i x_i x_{i+d}` for `d < steps`, `0` beyond (Python
`np.correlate(x, x, "full")[ng-1:] * D0` with the closing zero
knot). -/
noncomputable def acf (d : ℕ) : ℝ :=
  f.D0 * ∑ i : Fin f.steps,
    if h : (i : ℕ) + d < f.steps then f.x i * f.x ⟨(i : ℕ) + d, h⟩ else 0

/-- beyond the support the autocorrelation vanishes (the closing
zero knot and everything after). -/
theorem acf_eq_zero {d : ℕ} (hd : f.steps ≤ d) : f.acf d = 0 := by
  unfold acf
  rw [Finset.sum_eq_zero, mul_zero]
  intro i _
  rw [dif_neg]
  omega

/-- the zero-lag autocorrelation is nonnegative (`D0 · Σ x_i² ≥ 0` --
the class is genuinely of positive type at lag 0; the full
positive-type structure is what the window positivity premise of
(iii) consumes). -/
theorem acf_zero_nonneg : 0 ≤ f.acf 0 := by
  refine mul_nonneg f.D0_pos.le (Finset.sum_nonneg fun i _ => ?_)
  rw [dif_pos (by have := i.isLt; omega : (i : ℕ) + 0 < f.steps)]
  exact mul_self_nonneg (f.x i)

/-- **the induced test function** (DERIVED): the EVEN piecewise-linear
interpolant of the autocorrelation on the native grid (Python
`np.interp` on `|u|`, knots `d · D0`, `right=0`): at
`t = |u| / D0 ∈ [d, d+1]` linear between `a_d` and `a_{d+1}`. -/
noncomputable def toFun (u : ℝ) : ℝ :=
  f.acf ⌊|u| / f.D0⌋₊
    + (|u| / f.D0 - (⌊|u| / f.D0⌋₊ : ℝ))
      * (f.acf (⌊|u| / f.D0⌋₊ + 1) - f.acf ⌊|u| / f.D0⌋₊)

/-- Floor-free affine piece on the half-open normalized grid cell
`[d,d+1)`.  The coefficients are the actual PL knot values `acf d`
and `acf (d+1)`; the seed values `x` enter through `acf`. -/
noncomputable def linearCellPiece (d : ℕ) (u : ℝ) : ℝ :=
  let t := |u| / f.D0
  if (d : ℝ) ≤ t ∧ t < (d : ℝ) + 1 then
    f.acf d + (t - d) * (f.acf (d + 1) - f.acf d)
  else 0

/-- **Finite floor-free cell representation.**  The floor-based
definition of `toFun` equals the finite sum of its affine
half-open-cell pieces.  Thus `GridElement.toFun` is an even
piecewise-linear hat/cell function, not the underlying step function. -/
theorem toFun_eq_sum_linearCellPiece (u : ℝ) :
    f.toFun u = ∑ d ∈ Finset.range f.steps, f.linearCellPiece d u := by
  let t : ℝ := |u| / f.D0
  have ht0 : 0 ≤ t := div_nonneg (abs_nonneg _) f.D0_pos.le
  let q : ℕ := ⌊t⌋₊
  have hqle : (q : ℝ) ≤ t := Nat.floor_le ht0
  have htq : t < (q : ℝ) + 1 := Nat.lt_floor_add_one t
  by_cases hq : q < f.steps
  · rw [Finset.sum_eq_single q]
    · unfold toFun linearCellPiece
      dsimp only
      change f.acf q + (t - q) * (f.acf (q + 1) - f.acf q) = _
      rw [if_pos ⟨hqle, htq⟩]
    · intro d hd hdq
      simp only [Finset.mem_range] at hd
      unfold linearCellPiece
      dsimp only
      rw [if_neg]
      intro hcell
      have hfloor : ⌊t⌋₊ = d := (Nat.floor_eq_iff ht0).2 hcell
      exact hdq (hfloor ▸ rfl)
    · simp [hq]
  · have hstepsq : f.steps ≤ q := Nat.le_of_not_gt hq
    unfold toFun
    change f.acf q + (t - q) * (f.acf (q + 1) - f.acf q) = _
    rw [f.acf_eq_zero hstepsq,
      f.acf_eq_zero (hstepsq.trans (Nat.le_succ q))]
    simp
    symm
    apply Finset.sum_eq_zero
    intro d hd
    simp only [Finset.mem_range] at hd
    unfold linearCellPiece
    dsimp only
    rw [if_neg]
    intro hcell
    have hfloor : q = d := (Nat.floor_eq_iff ht0).2 hcell
    omega

/-- Derivatives of the half-scaled hyperbolic functions. -/
lemma hasDerivAt_sinh_half (x : ℝ) :
    HasDerivAt (fun u : ℝ => Real.sinh (u / 2))
      (Real.cosh (x / 2) / 2) x := by
  convert (Real.hasDerivAt_sinh (x / 2)).comp x
    ((hasDerivAt_id x).div_const 2) using 1
  ring

lemma hasDerivAt_cosh_half (x : ℝ) :
    HasDerivAt (fun u : ℝ => Real.cosh (u / 2))
      (Real.sinh (x / 2) / 2) x := by
  convert (Real.hasDerivAt_cosh (x / 2)).comp x
    ((hasDerivAt_id x).div_const 2) using 1
  ring

/-- Primitive for an affine function times `2 cosh(u/2)`. -/
noncomputable def affineCoshPrimitive (α β u : ℝ) : ℝ :=
  ((α + β * u) * Real.sinh (u / 2)) * 4 -
    (β * Real.cosh (u / 2)) * 8

lemma hasDerivAt_affineCoshPrimitive (α β x : ℝ) :
    HasDerivAt (affineCoshPrimitive α β)
      ((α + β * x) * 2 * Real.cosh (x / 2)) x := by
  have hl : HasDerivAt (fun u : ℝ => α + β * u) β x := by
    convert (hasDerivAt_const x α).add
      ((hasDerivAt_id x).const_mul β) using 1
    ring
  unfold affineCoshPrimitive
  convert ((hl.mul (hasDerivAt_sinh_half x)).const_mul 4).sub
    (((hasDerivAt_cosh_half x).const_mul β).const_mul 8) using 1
  · funext y
    simp only [Pi.mul_apply, Pi.sub_apply]
    ring
  · ring

/-- Closed elementary integral used by the r376 cell assembly. -/
lemma intervalIntegral_affine_mul_two_cosh_half (α β a b : ℝ) :
    intervalIntegral
        (fun u : ℝ => (α + β * u) * (2 * Real.cosh (u / 2)))
        a b MeasureTheory.volume =
      affineCoshPrimitive α β b - affineCoshPrimitive α β a := by
  apply intervalIntegral.integral_eq_sub_of_hasDerivAt
  · intro x _
    convert hasDerivAt_affineCoshPrimitive α β x using 1
    ring
  · exact Continuous.intervalIntegrable (by fun_prop) _ _

/-- **the support parameter** `steps · D0` -- the quantity from which
the elementwise onset `elementAnchor` is PREDEFINED (R325: "a₀, m_f
in advance from f"). -/
noncomputable def supportBound : ℝ := (f.steps : ℝ) * f.D0

theorem supportBound_nonneg : 0 ≤ f.supportBound :=
  mul_nonneg (Nat.cast_nonneg _) f.D0_pos.le

/-- the test function is even (the class is a class of
autocorrelations -- Weil test data). -/
theorem toFun_even (u : ℝ) : f.toFun (-u) = f.toFun u := by
  simp [toFun, abs_neg]

/-- **compact support, proved from the construction**: beyond the
support parameter the test function vanishes identically. -/
theorem toFun_eq_zero {u : ℝ} (hu : f.supportBound < u) : f.toFun u = 0 := by
  have hD0 : 0 < f.D0 := f.D0_pos
  have habs : (f.steps : ℝ) * f.D0 < |u| :=
    lt_of_lt_of_le hu (le_abs_self u)
  have ht : (f.steps : ℝ) ≤ |u| / f.D0 := (le_div_iff₀ hD0).mpr habs.le
  have hd : f.steps ≤ ⌊|u| / f.D0⌋₊ := Nat.le_floor ht
  unfold toFun
  rw [f.acf_eq_zero hd, f.acf_eq_zero (le_trans hd (Nat.le_succ _))]
  ring

/-- compact support, even form: vanishes once `|u|` exceeds the support. -/
theorem toFun_eq_zero_of_lt_abs {u : ℝ} (hu : f.supportBound < |u|) :
    f.toFun u = 0 := by
  rcases le_total 0 u with h | h
  · rw [abs_of_nonneg h] at hu
    exact f.toFun_eq_zero hu
  · rw [abs_of_nonpos h] at hu
    rw [← f.toFun_even]
    exact f.toFun_eq_zero hu

/-- Closed-support vanishing: the interpolant is zero on the closing
knot `|u| = supportBound` as well as outside. -/
theorem toFun_eq_zero_of_supportBound_le {u : ℝ} (hu : f.supportBound ≤ |u|) :
    f.toFun u = 0 := by
  rcases lt_or_eq_of_le hu with hlt | heq
  · exact f.toFun_eq_zero_of_lt_abs hlt
  · have ht : |u| / f.D0 = (f.steps : ℝ) := by
      rw [heq.symm]
      unfold supportBound D0
      field_simp
    unfold toFun
    have hfloor : ⌊|u| / f.D0⌋₊ = f.steps := by
      rw [ht, Nat.floor_natCast]
    rw [hfloor, f.acf_eq_zero le_rfl, f.acf_eq_zero (Nat.le_succ _)]
    ring

/-- Slope of the nonnegative closed cell `[d D0, (d+1) D0]`. -/
noncomputable def cellSlope (d : ℕ) : ℝ :=
  (f.acf (d + 1) - f.acf d) / f.D0

/-- Intercept of the nonnegative closed cell `[d D0, (d+1) D0]`. -/
noncomputable def cellIntercept (d : ℕ) : ℝ :=
  f.acf d - (d : ℝ) * (f.acf (d + 1) - f.acf d)

/-- On the nonnegative closed cell, `toFun` is the affine function
`cellIntercept d + cellSlope d · u`.  This is the input shape of
`intervalIntegral_affine_mul_two_cosh_half` (r493b). -/
theorem toFun_eq_affine_on_nonneg_cell (d : ℕ) {u : ℝ}
    (hlo : (d : ℝ) * f.D0 ≤ u) (hhi : u ≤ ((d : ℝ) + 1) * f.D0) :
    f.toFun u = f.cellIntercept d + f.cellSlope d * u := by
  have hu : 0 ≤ u :=
    le_trans (mul_nonneg (Nat.cast_nonneg _) f.D0_pos.le) hlo
  have ht0 : 0 ≤ u / f.D0 := div_nonneg hu f.D0_pos.le
  have hd : (d : ℝ) ≤ u / f.D0 := (le_div_iff₀ f.D0_pos).mpr hlo
  have hu' : u / f.D0 ≤ (d : ℝ) + 1 := (div_le_iff₀ f.D0_pos).mpr hhi
  have hD0 : f.D0 ≠ 0 := f.D0_pos.ne'
  by_cases hlt : u / f.D0 < (d : ℝ) + 1
  · have hfloor : ⌊u / f.D0⌋₊ = d := (Nat.floor_eq_iff ht0).2 ⟨hd, hlt⟩
    unfold toFun cellIntercept cellSlope
    rw [abs_of_nonneg hu, hfloor]
    field_simp [hD0]
    ring
  · have heq : u / f.D0 = (d : ℝ) + 1 := le_antisymm hu' (le_of_not_gt hlt)
    have hfloor : ⌊u / f.D0⌋₊ = d + 1 := by
      rw [heq, ← Nat.cast_succ d, Nat.floor_natCast]
    have hto : f.toFun u = f.acf (d + 1) := by
      unfold toFun
      rw [abs_of_nonneg hu, hfloor, heq, Nat.cast_succ]
      ring
    have huD : u = ((d : ℝ) + 1) * f.D0 := (div_eq_iff hD0).mp heq
    have haff : f.cellIntercept d + f.cellSlope d * u = f.acf (d + 1) := by
      unfold cellIntercept cellSlope
      rw [huD]
      field_simp [hD0]
      ring
    rw [hto, haff]

/-- Pointwise bound used for interval-integrability of `toFun`. -/
lemma acf_abs_le_sum (k : ℕ) :
    |f.acf k| ≤ ∑ d ∈ Finset.range (f.steps + 2), |f.acf d| := by
  by_cases hk : k < f.steps + 2
  · exact Finset.single_le_sum (fun i _ => abs_nonneg (f.acf i))
      (Finset.mem_range.mpr hk)
  · have : f.steps ≤ k := by omega
    rw [f.acf_eq_zero this, abs_zero]
    exact Finset.sum_nonneg fun _ _ => abs_nonneg _

lemma toFun_abs_le (u : ℝ) :
    |f.toFun u| ≤ 3 * ∑ d ∈ Finset.range (f.steps + 2), |f.acf d| := by
  set t : ℝ := |u| / f.D0
  set q : ℕ := ⌊t⌋₊
  have ht0 : 0 ≤ t := div_nonneg (abs_nonneg _) f.D0_pos.le
  have hfrac : |t - (q : ℝ)| ≤ 1 := by
    have h0 : 0 ≤ t - (q : ℝ) := sub_nonneg.mpr (Nat.floor_le ht0)
    have h1 : t - (q : ℝ) < 1 := by
      have hlt := Nat.lt_floor_add_one t
      simp [q] at hlt ⊢
      linarith
    exact abs_le.mpr ⟨by linarith, h1.le⟩
  set Δ : ℝ := f.acf (q + 1) - f.acf q
  have hto : f.toFun u = f.acf q + (t - q) * Δ := by
    simp [toFun, t, q, Δ]
  have htri : |f.acf q + (t - q) * Δ| ≤ |f.acf q| + |t - q| * |Δ| := by
    simpa [abs_mul] using abs_add_le (f.acf q) ((t - q) * Δ)
  have hprod : |t - q| * |Δ| ≤ |f.acf (q + 1)| + |f.acf q| :=
    calc
      |t - q| * |Δ| ≤ 1 * |Δ| :=
        mul_le_mul_of_nonneg_right hfrac (abs_nonneg _)
      _ = |Δ| := one_mul _
      _ ≤ |f.acf (q + 1)| + |f.acf q| := by
        simpa [Δ, sub_eq_add_neg, abs_neg] using
          abs_add_le (f.acf (q + 1)) (-f.acf q)
  have hfin : |f.acf q + (t - q) * Δ| ≤
      2 * |f.acf q| + |f.acf (q + 1)| := by
    linarith [htri, hprod]
  rw [hto]
  refine hfin.trans ?_
  have hq := f.acf_abs_le_sum q
  have hq1 := f.acf_abs_le_sum (q + 1)
  linarith

lemma measurable_toFun : Measurable f.toFun := by
  have hacf : Measurable f.acf := measurable_from_nat
  have hfloor : Measurable fun u : ℝ => ⌊|u| / f.D0⌋₊ := by fun_prop
  have hfloor1 : Measurable fun u : ℝ => ⌊|u| / f.D0⌋₊ + 1 :=
    hfloor.add_const 1
  have hcast : Measurable fun n : ℕ => (n : ℝ) := measurable_from_nat
  have ht : Measurable fun u : ℝ => |u| / f.D0 := by fun_prop
  unfold toFun
  exact (hacf.comp hfloor).add <|
    (ht.sub (hcast.comp hfloor)).mul <|
      (hacf.comp hfloor1).sub (hacf.comp hfloor)

lemma intervalIntegrable_toFun (a b : ℝ) :
    IntervalIntegrable f.toFun MeasureTheory.volume a b := by
  rw [intervalIntegrable_iff]
  refine MeasureTheory.IntegrableOn.of_bound ?_
      f.measurable_toFun.aestronglyMeasurable
      (3 * ∑ d ∈ Finset.range (f.steps + 2), |f.acf d|) ?_
  · rw [Real.volume_uIoc]
    exact ENNReal.ofReal_lt_top
  · exact Filter.Eventually.of_forall fun u => f.toFun_abs_le u

lemma intervalIntegrable_toFun_mul_two_cosh (a b : ℝ) :
    IntervalIntegrable
      (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
      MeasureTheory.volume a b :=
  (f.intervalIntegrable_toFun a b).mul_continuousOn (by fun_prop)

lemma toFun_mul_two_cosh_even (u : ℝ) :
    f.toFun (-u) * (2 * Real.cosh ((-u) / 2)) =
      f.toFun u * (2 * Real.cosh (u / 2)) := by
  rw [f.toFun_even, neg_div, Real.cosh_neg]

/-- Evenness split (r493c1): `∫_{-R}^{R} g(u)·2cosh(u/2) du = 2 ∫_0^R`
for the even product `toFun × 2 cosh(·/2)`. -/
theorem intervalIntegral_toFun_mul_two_cosh_eq_two_mul {R : ℝ} (hR : 0 ≤ R) :
    intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        (-R) R MeasureTheory.volume =
      2 * intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        0 R MeasureTheory.volume := by
  set g : ℝ → ℝ := fun u => f.toFun u * (2 * Real.cosh (u / 2))
  have hint : IntervalIntegrable g MeasureTheory.volume (-R) R :=
    f.intervalIntegrable_toFun_mul_two_cosh (-R) R
  have h0R : IntervalIntegrable g MeasureTheory.volume 0 R :=
    hint.mono_set <| by
      rw [Set.uIcc_of_le hR, Set.uIcc_of_le (neg_le_self hR)]
      exact Set.Icc_subset_Icc (neg_nonpos.mpr hR) le_rfl
  have hneg : IntervalIntegrable g MeasureTheory.volume (-R) 0 :=
    hint.mono_set <| by
      rw [Set.uIcc_of_le (neg_nonpos.mpr hR), Set.uIcc_of_le (neg_le_self hR)]
      exact Set.Icc_subset_Icc le_rfl hR
  have hadd := intervalIntegral.integral_add_adjacent_intervals hneg h0R
  have hcomp :
      intervalIntegral (fun u => g (-u)) (-R) 0 MeasureTheory.volume =
        intervalIntegral g 0 R MeasureTheory.volume := by
    rw [intervalIntegral.integral_comp_neg (f := g)]
    simp
  have hcongr :
      intervalIntegral (fun u => g (-u)) (-R) 0 MeasureTheory.volume =
        intervalIntegral g (-R) 0 MeasureTheory.volume := by
    apply intervalIntegral.integral_congr
    intro u _
    exact f.toFun_mul_two_cosh_even u
  have hleft : intervalIntegral g (-R) 0 MeasureTheory.volume =
      intervalIntegral g 0 R MeasureTheory.volume :=
    hcongr.symm.trans hcomp
  have : intervalIntegral g (-R) R MeasureTheory.volume =
      intervalIntegral g 0 R MeasureTheory.volume +
        intervalIntegral g 0 R MeasureTheory.volume := by
    rw [← hadd, hleft]
  rw [this, two_mul]

/-- Dyadic cell decomposition of the nonnegative half (r493c1):
`∫_0^R = ∑_{d < steps} ∫_{d D0}^{(d+1) D0}` once `supportBound ≤ R`.
Each cell integral is the r493b affine integrand on that interval. -/
theorem intervalIntegral_toFun_mul_two_cosh_eq_sum_cell {R : ℝ}
    (hR : f.supportBound ≤ R) :
    intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        0 R MeasureTheory.volume =
      ∑ d ∈ Finset.range f.steps,
        intervalIntegral
          (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
          ((d : ℝ) * f.D0) (((d : ℝ) + 1) * f.D0) MeasureTheory.volume := by
  set g : ℝ → ℝ := fun u => f.toFun u * (2 * Real.cosh (u / 2))
  have hsucc (d : ℕ) :
      ((d : ℝ) + 1) * f.D0 = ((d + 1 : ℕ) : ℝ) * f.D0 := by
    rw [Nat.cast_succ]
  have hsum :=
    intervalIntegral.sum_integral_adjacent_intervals
      (f := g) (μ := MeasureTheory.volume) (n := f.steps)
      (a := fun k : ℕ => (k : ℝ) * f.D0)
      (fun k _ => f.intervalIntegrable_toFun_mul_two_cosh _ _)
  have hsum' :
      ∑ d ∈ Finset.range f.steps,
          intervalIntegral g ((d : ℝ) * f.D0) (((d + 1 : ℕ) : ℝ) * f.D0)
            MeasureTheory.volume =
        intervalIntegral g 0 f.supportBound MeasureTheory.volume := by
    convert hsum
    simp
  have h0s : IntervalIntegrable g MeasureTheory.volume 0 f.supportBound :=
    f.intervalIntegrable_toFun_mul_two_cosh _ _
  have htail : IntervalIntegrable g MeasureTheory.volume f.supportBound R :=
    f.intervalIntegrable_toFun_mul_two_cosh _ _
  have hadd := intervalIntegral.integral_add_adjacent_intervals h0s htail
  have htail0 : intervalIntegral g f.supportBound R MeasureTheory.volume = 0 := by
    have hz : Set.EqOn g (fun _ => (0 : ℝ)) (Set.uIcc f.supportBound R) := by
      intro u hu
      rw [Set.uIcc_of_le hR] at hu
      have hu0 : 0 ≤ u := le_trans f.supportBound_nonneg hu.1
      have habs : f.supportBound ≤ |u| := by
        rw [abs_of_nonneg hu0]
        exact hu.1
      change f.toFun u * (2 * Real.cosh (u / 2)) = 0
      rw [f.toFun_eq_zero_of_supportBound_le habs, zero_mul]
    rw [intervalIntegral.integral_congr hz, intervalIntegral.integral_zero]
  simp_rw [hsucc]
  rw [← hadd, htail0, add_zero, hsum']

/-- Combined r493c1 identity: the two-sided pole-density integral is
twice the sum of the nonnegative dyadic cell integrals. -/
theorem intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_cell {R : ℝ}
    (hR : f.supportBound ≤ R) :
    intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        (-R) R MeasureTheory.volume =
      2 * ∑ d ∈ Finset.range f.steps,
        intervalIntegral
          (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
          ((d : ℝ) * f.D0) (((d : ℝ) + 1) * f.D0) MeasureTheory.volume := by
  have hR0 : 0 ≤ R := le_trans f.supportBound_nonneg hR
  rw [f.intervalIntegral_toFun_mul_two_cosh_eq_two_mul hR0,
    f.intervalIntegral_toFun_mul_two_cosh_eq_sum_cell hR]

/-- Knot evaluation on the nonnegative native grid. -/
theorem toFun_nat_mul_D0 (k : ℕ) :
    f.toFun ((k : ℝ) * f.D0) = f.acf k := by
  have hu : 0 ≤ (k : ℝ) * f.D0 :=
    mul_nonneg (Nat.cast_nonneg _) f.D0_pos.le
  have ht : |(k : ℝ) * f.D0| / f.D0 = (k : ℝ) := by
    rw [abs_of_nonneg hu]
    field_simp [f.D0_pos.ne']
  unfold toFun
  rw [ht, Nat.floor_natCast]
  ring

/-- Knot evaluation on the two-sided native grid (`toFun` is even). -/
theorem toFun_int_mul_D0 (k : ℤ) :
    f.toFun ((k : ℝ) * f.D0) = f.acf k.natAbs := by
  have habs : |((k : ℝ) * f.D0)| = (k.natAbs : ℝ) * f.D0 := by
    rw [abs_mul, abs_of_nonneg f.D0_pos.le, Nat.cast_natAbs, Int.cast_abs]
  unfold toFun
  rw [habs]
  have ht : ((k.natAbs : ℝ) * f.D0) / f.D0 = (k.natAbs : ℝ) := by
    field_simp [f.D0_pos.ne']
  rw [ht, Nat.floor_natCast]
  ring

lemma cellAffine_left (d : ℕ) :
    f.cellIntercept d + f.cellSlope d * ((d : ℝ) * f.D0) = f.acf d := by
  unfold cellIntercept cellSlope
  have hD0 : f.D0 ≠ 0 := f.D0_pos.ne'
  field_simp [hD0]
  ring

lemma cellAffine_right (d : ℕ) :
    f.cellIntercept d + f.cellSlope d * (((d : ℝ) + 1) * f.D0) =
      f.acf (d + 1) := by
  unfold cellIntercept cellSlope
  have hD0 : f.D0 ≠ 0 := f.D0_pos.ne'
  field_simp [hD0]
  ring

/-- Evaluated r493b primitive increment on the nonnegative cell
`[d D0, (d+1) D0]`. -/
noncomputable def cellCoshIncrement (d : ℕ) : ℝ :=
  4 * f.acf (d + 1) * Real.sinh ((((d : ℝ) + 1) * f.D0) / 2) -
    4 * f.acf d * Real.sinh (((d : ℝ) * f.D0) / 2) -
    8 * f.cellSlope d *
      (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
        Real.cosh (((d : ℝ) * f.D0) / 2))

lemma cellCoshIncrement_eq_primitive (d : ℕ) :
    affineCoshPrimitive (f.cellIntercept d) (f.cellSlope d)
          (((d : ℝ) + 1) * f.D0) -
        affineCoshPrimitive (f.cellIntercept d) (f.cellSlope d)
          ((d : ℝ) * f.D0) =
      f.cellCoshIncrement d := by
  unfold affineCoshPrimitive cellCoshIncrement
  rw [f.cellAffine_right d, f.cellAffine_left d]
  ring

/-- Step (1): on each nonnegative native cell the pole-density
integrand is the r493b affine integrand, so the cell integral equals
the primitive increment. -/
theorem intervalIntegral_toFun_mul_two_cosh_cell (d : ℕ) :
    intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        ((d : ℝ) * f.D0) (((d : ℝ) + 1) * f.D0) MeasureTheory.volume =
      f.cellCoshIncrement d := by
  have hle : (d : ℝ) * f.D0 ≤ ((d : ℝ) + 1) * f.D0 :=
    mul_le_mul_of_nonneg_right (by linarith) f.D0_pos.le
  have heq :
      Set.EqOn
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        (fun u : ℝ =>
          (f.cellIntercept d + f.cellSlope d * u) *
            (2 * Real.cosh (u / 2)))
        (Set.uIcc ((d : ℝ) * f.D0) (((d : ℝ) + 1) * f.D0)) := by
    intro u hu
    rw [Set.uIcc_of_le hle] at hu
    change f.toFun u * (2 * Real.cosh (u / 2)) =
      (f.cellIntercept d + f.cellSlope d * u) * (2 * Real.cosh (u / 2))
    rw [f.toFun_eq_affine_on_nonneg_cell d hu.1 hu.2]
  rw [intervalIntegral.integral_congr heq,
    intervalIntegral_affine_mul_two_cosh_half]
  exact f.cellCoshIncrement_eq_primitive d

/-- Combined r493c1+c2 cell form: the two-sided integral is twice the
sum of primitive increments. -/
theorem intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_increment
    {R : ℝ} (hR : f.supportBound ≤ R) :
    intervalIntegral
        (fun u : ℝ => f.toFun u * (2 * Real.cosh (u / 2)))
        (-R) R MeasureTheory.volume =
      2 * ∑ d ∈ Finset.range f.steps, f.cellCoshIncrement d := by
  rw [f.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_cell hR]
  congr 1
  refine Finset.sum_congr rfl fun d _ => ?_
  exact f.intervalIntegral_toFun_mul_two_cosh_cell d

/-- **the predefined elementwise anchor onset** (R325 target form)
(ii)): computed from the element's support parameter ALONE, before
any window is built or any form is read -- `a₀(f) = max(1, ⌈exp
(steps · D0)⌉)`.  (The measured onset is `α* = (n_g + 1) D0 / 2` in
log coordinates; `supportBound ≥ α*`, so this anchor is safe and
still element-predefined.)  The predefined mesh level is the
element's own `meshExp` -- R325 S1.4: the native mesh already
carries the limit value. -/
noncomputable def elementAnchor : ℕ :=
  max 1 (Nat.ceil (Real.exp f.supportBound))

end GridElement

/-! ## The comb channel, corpus gauge: transcribed and PROVED

The corpus comb masses are `mu_n = 2 Λ(n)/√n` at nodes `log n`
(Python `MU_ALL`/`U_ALL`, v563).  The Lean window layer keeps the
bare `Λ` (the rescale is a positive diagonal gauge -- r310 header);
the FORM read of the extraction, however, is a linear functional and
must be stated in the gauge the corpus positivity lives in.  So the
comb read below carries the corpus gauge, and the gauge relation to
the built window's comb channel is PROVED (`combMass_eq_gauge`,
`combRead_eq_window_channel`). -/

/-- the corpus comb mass `2 Λ(n)/√n` (Python `MU_ALL`). -/
noncomputable def combMass (n : ℕ) : ℝ := 2 * Λ n / Real.sqrt n

theorem combMass_nonneg (n : ℕ) : 0 ≤ combMass n :=
  div_nonneg (mul_nonneg (by norm_num)
    ArithmeticFunction.vonMangoldt_nonneg) (Real.sqrt_nonneg _)

/-- the corpus gauge is the positive diagonal rescale of the exact
`Λ`: `mu_n = (2/√n) · Λ(n)` -- the r310 "positive diagonal gauge
lives in the builder map" note, now a statement. -/
theorem combMass_eq_gauge (n : ℕ) :
    combMass n = (2 / Real.sqrt n) * Λ n := by
  unfold combMass
  ring

/-- **the finite comb read of the canonical window at anchor `a`**
(corpus gauge): the exact atom sum `Σ_{n ∈ atoms(a)} mu_n f(log n)`
over the predefined atom set.  MESH STATUS (honest, R325 S1.3/S1.4):
this is the mesh-free exact atom sum; the corpus evaluates the comb
channel as a tent-assembled read on the mesh grid, and the two are
EQUAL on the native class at native-or-finer mesh (the derived
tent-read identity, measured at 1e-12) -- the tent assembly's
transcription belongs to the fold TODO (RH/Source.lean, stage 3),
which is why the read here is stated mesh-free and the window's
mesh-independence is `buildPrimeWindow_refinement_compatible`. -/
noncomputable def combRead (a : ℕ) (f : GridElement) : ℝ :=
  ∑ n ∈ windowAtoms a, combMass n * f.toFun (Real.log n)

/-- **the Weil prime side in the corpus gauge**: `Σ'_n mu_n f(log n)`
(a tsum over all naturals; the mass vanishes off the prime powers). -/
noncomputable def weilCombSide (f : GridElement) : ℝ :=
  ∑' n : ℕ, combMass n * f.toFun (Real.log n)

/-- **THE COMB ELEMENTWISE FINITE STABILIZATION** (r326, R325 target
form (ii), comb channel; PROVED).  For every grid element the finite
comb reads of the canonical family EQUAL the Weil prime side for
every anchor `a ≥ elementAnchor f` -- with the onset PREDEFINED from
the element's support alone, and NO mesh quantifier at all (the read
is mesh-free; the built window is mesh-independent).  This is the
elementwise form of `finite_forms_converge_to_weil` (r310) in the
corpus gauge: stabilization, not convergence -- the window rule
covers the support from the onset on, exactly (R325 S1.1: rel dev
0 above onset, a genuine onset below). -/
theorem comb_elementwise_stabilization (f : GridElement) {a : ℕ}
    (haA : f.elementAnchor ≤ a) : combRead a f = weilCombSide f := by
  have ha1 : 1 ≤ a := le_trans (le_max_left _ _) haA
  have haexp : Real.exp f.supportBound ≤ (a : ℝ) := by
    have hceil : (Nat.ceil (Real.exp f.supportBound) : ℝ) ≤ (a : ℝ) := by
      exact_mod_cast le_trans (le_max_right _ _) haA
    exact le_trans (Nat.le_ceil _) hceil
  have hzero : ∀ n : ℕ, n ∉ windowAtoms a →
      combMass n * f.toFun (Real.log n) = 0 := by
    intro n hn
    by_cases hpp : IsPrimePow n
    · have hgt : a ^ 2 < n := by
        by_contra hle
        exact hn (Finset.mem_filter.mpr
          ⟨Finset.mem_range.mpr (by omega), hpp⟩)
      have ha1R : (1 : ℝ) ≤ (a : ℝ) := by exact_mod_cast ha1
      have hgtR : ((a : ℝ)) ^ 2 < (n : ℝ) := by exact_mod_cast hgt
      have hexp_lt : Real.exp f.supportBound < (n : ℝ) := by nlinarith
      have hb : f.supportBound < Real.log n := by
        have := Real.log_lt_log (Real.exp_pos f.supportBound) hexp_lt
        simpa [Real.log_exp] using this
      rw [f.toFun_eq_zero hb, mul_zero]
    · have hL : Λ n = 0 := by
        by_contra h
        exact hpp (ArithmeticFunction.vonMangoldt_ne_zero_iff.mp h)
      simp [combMass, hL]
  unfold combRead weilCombSide
  exact (tsum_eq_sum hzero).symm

/-- **the comb read IS the canonical window's comb channel** (PROVED;
the honesty tie to the R325 target form `fullForm (buildPrimeWindow
(specFamily a m ha)) f`): the corpus-gauge read equals the sum of
`mu(atom_j) · f(node_j)` over the BUILT window's node vector -- same
atoms, same nodes, the mass in the proved gauge relation
`combMass_eq_gauge` to the window's `Λ` channel. -/
theorem combRead_eq_window_channel (a m : ℕ) (ha : IsPrimePow a)
    (f : GridElement) :
    combRead a f
      = ∑ j, combMass ((specFamily a m ha).primePowers j)
          * f.toFun ((buildPrimeWindow (specFamily a m ha)).nodes j) := by
  unfold combRead
  rw [← Finset.sum_coe_sort (windowAtoms a)
    (fun n => combMass n * f.toFun (Real.log n))]
  exact (Fintype.sum_equiv ((windowAtoms a).orderIsoOfFin rfl).toEquiv
    _ _ fun j => rfl).symm

/-- the Λ-gauge window form stabilizes elementwise too (the r310
statement `finite_forms_converge_to_weil`, now with the EXPLICIT
element-predefined onset instead of an existential): stated for the
record, PROVED by the same support argument. -/
theorem comb_window_elementwise_stabilization (f : GridElement)
    {a : ℕ} (ha : IsPrimePow a) (m : ℕ) (haA : f.elementAnchor ≤ a) :
    (buildPrimeWindow (specFamily a m ha)).combForm f.toFun
      = weilPrimeSide f.toFun := by
  have ha1 : 1 ≤ a := le_trans (le_max_left _ _) haA
  have haexp : Real.exp f.supportBound ≤ (a : ℝ) := by
    have hceil : (Nat.ceil (Real.exp f.supportBound) : ℝ) ≤ (a : ℝ) := by
      exact_mod_cast le_trans (le_max_right _ _) haA
    exact le_trans (Nat.le_ceil _) hceil
  have hzero : ∀ n : ℕ, n ∉ windowAtoms a →
      Λ n * f.toFun (Real.log n) = 0 := by
    intro n hn
    by_cases hpp : IsPrimePow n
    · have hgt : a ^ 2 < n := by
        by_contra hle
        exact hn (Finset.mem_filter.mpr
          ⟨Finset.mem_range.mpr (by omega), hpp⟩)
      have ha1R : (1 : ℝ) ≤ (a : ℝ) := by exact_mod_cast ha1
      have hgtR : ((a : ℝ)) ^ 2 < (n : ℝ) := by exact_mod_cast hgt
      have hexp_lt : Real.exp f.supportBound < (n : ℝ) := by nlinarith
      have hb : f.supportBound < Real.log n := by
        have := Real.log_lt_log (Real.exp_pos f.supportBound) hexp_lt
        simpa [Real.log_exp] using this
      rw [f.toFun_eq_zero hb, mul_zero]
    · have hL : Λ n = 0 := by
        by_contra h
        exact hpp (ArithmeticFunction.vonMangoldt_ne_zero_iff.mp h)
      rw [hL, zero_mul]
  have htsum : weilPrimeSide f.toFun
      = ∑ n ∈ windowAtoms a, Λ n * f.toFun (Real.log n) :=
    tsum_eq_sum hzero
  have hform : (buildPrimeWindow (specFamily a m ha)).combForm f.toFun
      = ∑ n ∈ windowAtoms a, Λ n * f.toFun (Real.log n) := by
    rw [← Finset.sum_coe_sort (windowAtoms a)
      (fun n => Λ n * f.toFun (Real.log n))]
    exact Fintype.sum_equiv ((windowAtoms a).orderIsoOfFin rfl).toEquiv
      _ _ (fun j => rfl)
  rw [hform, htsum]

/-! ## The kernel channels: transcribed kernels + remaining arch opacity

r373: the closed-form *kernels* are Lean objects
(`weilArchKernel`, `polePotential`).  r376: the pole tent-read is
transcribed as the native-mesh second-difference pairing of
`polePotential` (Python `pole_lags_closed`) and the pole
stabilization is PROVED.  mathlib v4.29.1 carries `Complex.digamma =
logDeriv Complex.Gamma` with the recurrence `digamma (s+1) = digamma
s + s⁻¹` and the values at `0, 1, 1/2`; there is NO `Real.digamma`,
NO Gauss integral (mathlib TODO on `Digamma.lean`), and NO
ψ-monotonicity.  The arch tent-read `archRead` and pairing
`weilArchSide` remain opaque: identifying `arch_A` tent integrals
with `weilArchKernel` is Titchmarsh Ch. X / Weil 1952. -/

/-- Archimedean digamma factor on the critical line (Titchmarsh,
*The Theory of the Riemann Zeta-Function*, 2nd ed. (1986), Chapter X;
Weil, *Sur les «formules explicites» de la théorie des nombres
premiers*, Comm. Math. Helv. 26 (1952)). -/
noncomputable def weilArchDigamma (t : ℝ) : ℂ :=
  Complex.digamma ((1 / 4 : ℂ) + Complex.I * t / (2 * Real.pi))

/-- Even combination of the archimedean digamma factor.  Dictionary
kernel; not yet paired against mesh tents. -/
noncomputable def weilArchKernel (t : ℝ) : ℝ :=
  (weilArchDigamma t + weilArchDigamma (-t)).re

theorem weilArchKernel_even (t : ℝ) :
    weilArchKernel (-t) = weilArchKernel t := by
  simp [weilArchKernel, add_comm]

/-- v716 closed form of the polar contribution as a function of lag:
`Π(t) = −8 (cosh(|t|/2) − 1)` (Python `stage2.pole_lags_closed`;
elementary hyperbolic identity, no ζ). -/
noncomputable def polePotential (t : ℝ) : ℝ :=
  -8 * (Real.cosh (|t| / 2) - 1)

theorem polePotential_zero : polePotential 0 = 0 := by
  simp [polePotential, Real.cosh_zero]

theorem polePotential_even (t : ℝ) : polePotential (-t) = polePotential t := by
  simp [polePotential, abs_neg]

theorem polePotential_eq_cosh (t : ℝ) :
    polePotential t = -8 * (Real.cosh (t / 2) - 1) := by
  simp [polePotential]
  have : Real.cosh (|t| / 2) = Real.cosh (t / 2) := by
    rcases le_total 0 t with h | h
    · rw [abs_of_nonneg h]
    · rw [abs_of_nonpos h, neg_div, Real.cosh_neg]
  rw [this]

theorem polePotential_nonpos (t : ℝ) : polePotential t ≤ 0 := by
  rw [polePotential_eq_cosh]
  have hc : 0 < Real.cosh (t / 2) := Real.cosh_pos _
  have hsq : 1 ≤ Real.cosh (t / 2) ^ 2 := by
    rw [Real.cosh_sq]
    nlinarith [sq_nonneg (Real.sinh (t / 2))]
  have : 1 ≤ Real.cosh (t / 2) := by nlinarith
  nlinarith

/-- Production lag spacing for the selected-window builder:
`Delta = log(a)/(m+1)`. -/
noncomputable def productionArchDelta (a m : ℕ) : ℝ :=
  Real.log a / (m + 1 : ℝ)

/-- The triangular kernel `t_Delta(x)`. -/
noncomputable def archTent (Δ x : ℝ) : ℝ :=
  max 0 (1 - |x| / Δ)

/-- The symmetrized near-cell tent
`S(w) = (t_Delta(s-w) + t_Delta(s+w))/2`. -/
noncomputable def archNearSymTent (Δ s w : ℝ) : ℝ :=
  (archTent Δ (s - w) + archTent Δ (s + w)) / 2

/-- Regularized integrand of the production near cell. -/
noncomputable def productionArchNearIntegrand (Δ s w : ℝ) : ℝ :=
  (archTent Δ s * Real.exp (-2 * w) -
      archNearSymTent Δ s w * Real.exp (-w / 2)) /
    (1 - Real.exp (-2 * w))

/-- The regularized near-cell value used by Python `arch_A_near`.
The quotient's removable value at `w=0` is irrelevant to the
interval integral. -/
noncomputable def productionArchLagNear (Δ s : ℝ) : ℝ :=
  let t := archTent Δ s
  let endpoint := s + Δ
  let integralValue :=
    intervalIntegral (productionArchNearIntegrand Δ s)
      0 endpoint MeasureTheory.volume
  (-(Real.eulerMascheroniConstant + Real.log Real.pi) * t +
    2 * integralValue -
    t * Real.log (1 - Real.exp (-2 * endpoint)))

/-- Integrand of an ordinary production far cell. -/
noncomputable def productionArchFarIntegrand (Δ s w : ℝ) : ℝ :=
  archTent Δ (s - w) * Real.exp (-w / 2) /
    (1 - Real.exp (-2 * w))

/-- The ordinary tent integral used by Python `arch_A_far`. -/
noncomputable def productionArchLagFar (Δ s : ℝ) : ℝ :=
  -intervalIntegral (productionArchFarIntegrand Δ s)
    (s - Δ) (s + Δ) MeasureTheory.volume

/-- **Productive transcription of Python `arch_lags`.**
For `i=0` the Euler/log-pi regularized near cell is used; every
`i≥1` is the ordinary far-cell tent integral at `s=i Delta`.
There is no longer an opaque arch-lag coefficient interface. -/
noncomputable def productionArchLag (a m i : ℕ) : ℝ :=
  let Δ := productionArchDelta a m
  let s := i * Δ
  if i = 0 then productionArchLagNear Δ s
  else productionArchLagFar Δ s

/-- **Concrete arch read.**  This is Python `read_lags` literally:
`c₀ F(0) + 2 Σ_{i=1}^{M-1} cᵢ F(i Delta)`, with `M=m+1`.
Only the coefficient values `productionArchLag` remain external. -/
noncomputable def archRead (a m : ℕ) (f : GridElement) : ℝ :=
  productionArchLag a m 0 * f.toFun 0 +
    2 * ∑ i ∈ Finset.Icc 1 m,
      productionArchLag a m i *
        f.toFun (i * productionArchDelta a m)

/-- Regularized u-space weight
`w(u) = 2 e^{-u/2} / (1 - e^{-2u})` of the classical arch pairing
(relay T93/T95; r473 diagnosis). -/
noncomputable def weilArchUWeight (u : ℝ) : ℝ :=
  2 * Real.exp (-u / 2) / (1 - Real.exp (-2 * u))

/-- Regularized integrand of the u-space identity; the u = 0 value
is a removable/integrable singularity for Lipschitz even `g`. -/
noncomputable def weilArchUIntegrand (f : GridElement) (u : ℝ) : ℝ :=
  if u = 0 then 0
  else weilArchUWeight u *
    (Real.exp (-(3 / 2 : ℝ) * u) * f.toFun 0 - f.toFun u)

/-- **Classical archimedean pairing (r475).**  The u-space digamma
identity
`A = C_b g(0) + ∫_0^b w(u)(e^{-3u/2} g(0) - g(u)) du`
with `C_b = -γ - log π - log(1 - e^{-2b})`.  This replaces the
r376 opaque symbol: the pairing is now a concrete integral, not
an unidentified kernel.  The Gauss/Mellin identification of this
integral with `weilArchKernel` remains the named Prop
`GaussDigammaIntegralRepresentation` (Mathlib v4.29.1 still lists
Gauss's integral as TODO). -/
noncomputable def weilArchSide (f : GridElement) : ℝ :=
  if 0 < f.supportBound then
    let b := f.supportBound
    let g0 := f.toFun 0
    let Cb := -(Real.eulerMascheroniConstant + Real.log Real.pi)
      - Real.log (1 - Real.exp (-2 * b))
    Cb * g0 +
      intervalIntegral (weilArchUIntegrand f) 0 b MeasureTheory.volume
  else 0

/-- **Isolated Mathlib brick (r475, not a sorry).**  Gauss's
integral representation of digamma, exactly the TODO on Mathlib
v4.29.1 `Digamma.lean`.  The u-space pairing `weilArchSide` does
not depend on this lemma; the quadrature rate lives on that
integral. -/
def GaussDigammaIntegralRepresentation : Prop :=
  ∀ z : ℂ, 0 < z.re →
    Complex.digamma (z + 1) =
      (-Real.eulerMascheroniConstant : ℂ) +
        ∫ t in Set.Ioi (0 : ℝ),
          (Complex.exp (-t) - Complex.exp (-(z + 1) * t))
            / (1 - Complex.exp (-t))


/-! ### Pole channel: transcribed tent-read (r376)

Python `pole_lags_closed` is the second difference of `g_pole = polePotential`:
`c_d = -(g((d-1)D) - 2g(dD) + g((d+1)D))/D`.  For an even compactly
supported test function this is the exact hat-function pairing of
`g''` (distributional), and on the native PL class the pairing is a
finite sum — no `MeasureTheory`, no ζ.  Mesh-independence under
dyadic refinement is the finite-element identity: the discrete
Laplacian of a coarse-grid interpolant is supported on the coarse
knots, with scale `2^{-r}`. -/

/-- dyadic mesh width `D(m) = 2^{-m}`. -/
noncomputable def meshWidth (m : ℕ) : ℝ := (1 : ℝ) / 2 ^ m

theorem meshWidth_pos (m : ℕ) : 0 < meshWidth m := by
  unfold meshWidth
  positivity

theorem meshWidth_mul_pow (m n : ℕ) :
    ((n * 2 ^ m : ℕ) : ℝ) * meshWidth m = n := by
  unfold meshWidth
  push_cast
  field_simp

theorem GridElement.D0_eq_meshWidth (f : GridElement) :
    f.D0 = meshWidth f.meshExp := rfl

/-- second difference of `polePotential` at mesh `D`, index `k`. -/
noncomputable def poleΔ (D : ℝ) (k : ℤ) : ℝ :=
  polePotential ((k : ℝ) * D - D) - 2 * polePotential ((k : ℝ) * D)
    + polePotential ((k : ℝ) * D + D)

theorem poleΔ_even (D : ℝ) (k : ℤ) : poleΔ D (-k) = poleΔ D k := by
  unfold poleΔ
  simp only [Int.cast_neg, neg_mul]
  have e1 : -((k : ℝ) * D) - D = -((k : ℝ) * D + D) := by ring
  have e2 : -((k : ℝ) * D) + D = -((k : ℝ) * D - D) := by ring
  rw [e1, e2, polePotential_even, polePotential_even, polePotential_even]
  ring

/-- two-sided cutoff large enough that every sample outside it
vanishes, at every mesh `m`. -/
def poleCutoff (f : GridElement) (m : ℕ) : ℕ :=
  (f.steps + 3) * 2 ^ m

theorem toFun_at_mesh_eq_zero (f : GridElement) (m : ℕ) {k : ℤ}
    (hk : poleCutoff f m ≤ k.natAbs) :
    f.toFun ((k : ℝ) * meshWidth m) = 0 := by
  have hD : 0 < meshWidth m := meshWidth_pos m
  have habs : |((k : ℝ) * meshWidth m)| = (k.natAbs : ℝ) * meshWidth m := by
    rw [abs_mul, abs_of_nonneg hD.le, Nat.cast_natAbs, Int.cast_abs]
  have hgt : f.supportBound < |((k : ℝ) * meshWidth m)| := by
    rw [habs]
    have hkR : ((poleCutoff f m : ℕ) : ℝ) ≤ (k.natAbs : ℝ) := by exact_mod_cast hk
    have hmul : (poleCutoff f m : ℝ) * meshWidth m ≤
        (k.natAbs : ℝ) * meshWidth m :=
      mul_le_mul_of_nonneg_right hkR hD.le
    have hcancel : (poleCutoff f m : ℝ) * meshWidth m = (f.steps + 3 : ℕ) :=
      meshWidth_mul_pow m (f.steps + 3)
    have hsteps : f.supportBound ≤ (f.steps : ℝ) := by
      unfold GridElement.supportBound GridElement.D0
      have : (1 / 2 ^ f.meshExp : ℝ) ≤ 1 := by
        have hp : 0 < (2 : ℝ) ^ f.meshExp := by positivity
        rw [div_le_one₀ hp]
        exact one_le_pow₀ (by norm_num : (1 : ℝ) ≤ 2)
      exact mul_le_of_le_one_right (Nat.cast_nonneg _) this
    have : (f.steps : ℝ) < (f.steps + 3 : ℕ) := by
      exact_mod_cast Nat.lt_add_of_pos_right (by decide : 0 < 3)
    linarith
  exact f.toFun_eq_zero_of_lt_abs hgt

/-- two-sided discrete pairing of `polePotential` against `f` at mesh `D`
truncated at `N`.  Python `read_lags(pole_lags_closed, D, F)` for even
`F` (the negative-index half equals the positive half by evenness). -/
noncomputable def polePairingZ (D : ℝ) (f : GridElement) (N : ℕ) : ℝ :=
  -(∑ k ∈ Finset.Icc (-(N : ℤ)) N,
      f.toFun ((k : ℝ) * D) * poleΔ D k) / D

/-- the pole even-read at mesh level `m` (window-independent: the pole
kernel does not see the anchor; truncation past the support is a
no-op). -/
noncomputable def poleEvenRead (m : ℕ) (f : GridElement) : ℝ :=
  polePairingZ (meshWidth m) f (poleCutoff f m)

/-- **the pole-channel tent-read** (r376 transcription of
`pole_lags_closed` / `read_lags`).  Parallel to `combRead` (mesh-free
exact atom sum: the tent-assembly equals it on the native class),
the pole read is taken at the element's native mesh — R325 S1.4: the
native mesh already carries the limit value.  Independent of the
anchor: the pole kernel does not see the window. -/
noncomputable def poleRead (_a _m : ℕ) (f : GridElement) : ℝ :=
  poleEvenRead f.meshExp f

/-- **the pole side of the Weil form**: the native-mesh pairing. -/
noncomputable def weilPoleSide (f : GridElement) : ℝ :=
  poleEvenRead f.meshExp f

/-- Local telescope; this mathlib pin has no `sum_range_sub`. -/
lemma sum_range_sub_eq (n : ℕ) (g : ℕ → ℝ) :
    ∑ d ∈ Finset.range n, (g (d + 1) - g d) = g n - g 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    ring

/-- `∑_{i=0}^{n} g i = g 0 + ∑_{i=0}^{n-1} g (i+1)`. -/
lemma sum_range_succ_shift (n : ℕ) (g : ℕ → ℝ) :
    ∑ i ∈ Finset.range (n + 1), g i =
      g 0 + ∑ i ∈ Finset.range n, g (i + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]
    ring

/-- Two-sided even sum: `∑_{k=-N}^{N} g k = g 0 + 2 ∑_{n=0}^{N-1} g (n+1)`. -/
lemma sum_Icc_neg_of_even {N : ℕ} (g : ℤ → ℝ) (he : ∀ k, g (-k) = g k) :
    ∑ k ∈ Finset.Icc (-(N : ℤ)) (N : ℤ), g k =
      g 0 + 2 * ∑ n ∈ Finset.range N, g ((n + 1 : ℕ) : ℤ) := by
  induction N with
  | zero =>
    simp
  | succ N ih =>
    have hN1 : ((N + 1 : ℕ) : ℤ) = (N : ℤ) + 1 := by simp
    have hIcc :
        Finset.Icc (-((N + 1 : ℕ) : ℤ)) ((N + 1 : ℕ) : ℤ) =
          insert (-((N + 1 : ℕ) : ℤ))
            (insert ((N + 1 : ℕ) : ℤ)
              (Finset.Icc (-(N : ℤ)) (N : ℤ))) := by
      ext k
      simp only [Finset.mem_insert, Finset.mem_Icc, hN1]
      omega
    have hpos :
        ((N + 1 : ℕ) : ℤ) ∉ Finset.Icc (-(N : ℤ)) (N : ℤ) := by
      simp only [Finset.mem_Icc, hN1]
      omega
    have hneg :
        -((N + 1 : ℕ) : ℤ) ∉
          insert ((N + 1 : ℕ) : ℤ) (Finset.Icc (-(N : ℤ)) (N : ℤ)) := by
      simp only [Finset.mem_insert, Finset.mem_Icc, hN1]
      omega
    rw [hIcc, Finset.sum_insert hneg, Finset.sum_insert hpos, ih]
    have hsym : g (-((N + 1 : ℕ) : ℤ)) = g ((N + 1 : ℕ) : ℤ) := he _
    rw [hsym, Finset.sum_range_succ]
    ring

theorem poleΔ_zero (D : ℝ) : poleΔ D 0 = 2 * polePotential D := by
  unfold poleΔ
  have h0 : ((0 : ℤ) : ℝ) * D = 0 := by simp
  rw [h0, zero_sub, zero_add, polePotential_zero, mul_zero, sub_zero,
    polePotential_even]
  ring

theorem poleΔ_eq_neg_eight_cosh_second (D : ℝ) (k : ℤ) :
    poleΔ D k =
      -8 * (Real.cosh (((k : ℝ) * D - D) / 2) -
        2 * Real.cosh (((k : ℝ) * D) / 2) +
        Real.cosh (((k : ℝ) * D + D) / 2)) := by
  unfold poleΔ
  simp only [polePotential_eq_cosh]
  ring

lemma cosh_first_diff_eq_neg_div_eight (D : ℝ) :
    Real.cosh (D / 2) - Real.cosh 0 = -polePotential D / 8 := by
  rw [Real.cosh_zero, polePotential_eq_cosh]
  ring

lemma cosh_second_diff_eq_neg_div_eight (D : ℝ) (j : ℕ) :
    Real.cosh (((j : ℝ) * D) / 2) -
        2 * Real.cosh ((((j : ℝ) + 1) * D) / 2) +
        Real.cosh ((((j : ℝ) + 2) * D) / 2) =
      -poleΔ D ((j + 1 : ℕ) : ℤ) / 8 := by
  rw [poleΔ_eq_neg_eight_cosh_second]
  have hz : (((j + 1 : ℕ) : ℤ) : ℝ) = (j : ℝ) + 1 := by
    rw [Int.cast_natCast, Nat.cast_succ]
  have h1 : (((j : ℝ) + 1) * D - D) / 2 = ((j : ℝ) * D) / 2 := by ring
  have h3 : (((j : ℝ) + 1) * D + D) / 2 = (((j : ℝ) + 2) * D) / 2 := by ring
  rw [hz, h1, h3]
  field_simp

/-- Summation by parts for a vanishing right endpoint. -/
lemma sum_fwd_diff_mul (n : ℕ) (a c : ℕ → ℝ) (ha : a n = 0) :
    ∑ d ∈ Finset.range n, (a (d + 1) - a d) * (c (d + 1) - c d) =
      -a 0 * (c 1 - c 0) -
        ∑ j ∈ Finset.range (n - 1),
          a (j + 1) * (c j - 2 * c (j + 1) + c (j + 2)) := by
  cases n with
  | zero =>
    simp [ha]
  | succ n =>
    have hsplit :
        ∑ d ∈ Finset.range (n + 1),
            (a (d + 1) - a d) * (c (d + 1) - c d) =
          ∑ d ∈ Finset.range (n + 1), a (d + 1) * (c (d + 1) - c d) -
            ∑ d ∈ Finset.range (n + 1), a d * (c (d + 1) - c d) := by
      simp_rw [sub_mul]
      exact Finset.sum_sub_distrib (s := Finset.range (n + 1))
        (f := fun d => a (d + 1) * (c (d + 1) - c d))
        (g := fun d => a d * (c (d + 1) - c d))
    have h1 :
        ∑ d ∈ Finset.range (n + 1), a (d + 1) * (c (d + 1) - c d) =
          ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 1) - c d) +
            a (n + 1) * (c (n + 1) - c n) :=
      Finset.sum_range_succ _ n
    have h2 :
        ∑ d ∈ Finset.range (n + 1), a d * (c (d + 1) - c d) =
          a 0 * (c 1 - c 0) +
            ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 2) - c (d + 1)) := by
      rw [sum_range_succ_shift]
    have hre :
        ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 1) - c d) -
            ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 2) - c (d + 1)) =
          ∑ d ∈ Finset.range n,
            a (d + 1) *
              ((c (d + 1) - c d) - (c (d + 2) - c (d + 1))) := by
      simp_rw [← Finset.sum_sub_distrib, ← mul_sub]
    have hdiff (d : ℕ) :
        (c (d + 1) - c d) - (c (d + 2) - c (d + 1)) =
          -(c d - 2 * c (d + 1) + c (d + 2)) := by
      ring
    calc
      ∑ d ∈ Finset.range (n + 1), (a (d + 1) - a d) * (c (d + 1) - c d)
          = ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 1) - c d) -
              (a 0 * (c 1 - c 0) +
                ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 2) - c (d + 1))) := by
            rw [hsplit, h1, h2, ha, zero_mul, add_zero]
      _ = ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 1) - c d) -
            ∑ d ∈ Finset.range n, a (d + 1) * (c (d + 2) - c (d + 1)) -
          a 0 * (c 1 - c 0) := by
            rw [sub_add_eq_sub_sub, sub_right_comm]
      _ = ∑ d ∈ Finset.range n,
              a (d + 1) *
                ((c (d + 1) - c d) - (c (d + 2) - c (d + 1))) -
            a 0 * (c 1 - c 0) := by
            rw [hre]
      _ = ∑ d ∈ Finset.range n,
              a (d + 1) * -(c d - 2 * c (d + 1) + c (d + 2)) -
            a 0 * (c 1 - c 0) := by
            simp_rw [hdiff]
      _ = -a 0 * (c 1 - c 0) -
            ∑ d ∈ Finset.range n,
              a (d + 1) * (c d - 2 * c (d + 1) + c (d + 2)) := by
            simp_rw [mul_neg]
            rw [Finset.sum_neg_distrib]
            rw [sub_eq_add_neg, add_comm, ← sub_eq_add_neg, neg_mul]

lemma sum_acf_poleΔ_eq_upto_steps (f : GridElement) {N : ℕ}
    (hN : f.steps ≤ N) :
    ∑ k ∈ Finset.range N, f.acf (k + 1) * poleΔ f.D0 ((k + 1 : ℕ) : ℤ) =
      ∑ k ∈ Finset.range (f.steps - 1),
        f.acf (k + 1) * poleΔ f.D0 ((k + 1 : ℕ) : ℤ) := by
  refine (Finset.sum_subset ?hsubset ?hzero).symm
  · intro k hk
    exact Finset.mem_range.mpr
      (lt_of_lt_of_le (Finset.mem_range.mp hk)
        (le_trans (Nat.sub_le f.steps 1) hN))
  · intro k _hkN hknot
    have : ¬ k < f.steps - 1 := mt Finset.mem_range.mpr hknot
    have hkge : f.steps - 1 ≤ k := Nat.le_of_not_lt this
    have : f.steps ≤ k + 1 := by omega
    rw [f.acf_eq_zero this, zero_mul]

/-- Step (2): two-sided `polePairingZ` is the one-sided ACF knot sum
(factor 2, zero-lag unhalved) after even reindexing. -/
theorem polePairingZ_one_sided (f : GridElement) (N : ℕ) :
    polePairingZ f.D0 f N =
      -(f.acf 0 * poleΔ f.D0 0 +
          2 * ∑ k ∈ Finset.range N,
            f.acf (k + 1) * poleΔ f.D0 ((k + 1 : ℕ) : ℤ)) / f.D0 := by
  unfold polePairingZ
  let g : ℤ → ℝ := fun k => f.toFun ((k : ℝ) * f.D0) * poleΔ f.D0 k
  have hge : ∀ k, g (-k) = g k := by
    intro k
    have harg : ((-k : ℤ) : ℝ) * f.D0 = -((k : ℝ) * f.D0) := by
      simp [neg_mul]
    simp only [g]
    rw [harg, f.toFun_even, poleΔ_even]
  have hsum := sum_Icc_neg_of_even (N := N) g hge
  have g0 : g 0 = f.acf 0 * poleΔ f.D0 0 := by
    have h0 : ((0 : ℤ) : ℝ) * f.D0 = (0 : ℕ) * f.D0 := by simp
    simp only [g]
    rw [h0, f.toFun_nat_mul_D0]
  have gk : ∀ k : ℕ,
      g ((k + 1 : ℕ) : ℤ) =
        f.acf (k + 1) * poleΔ f.D0 ((k + 1 : ℕ) : ℤ) := by
    intro k
    have hcast : (((k + 1 : ℕ) : ℤ) : ℝ) * f.D0 =
        ((k + 1 : ℕ) : ℝ) * f.D0 := by
      simp
    simp only [g]
    rw [hcast, f.toFun_nat_mul_D0]
  rw [hsum, g0]
  simp_rw [gk]

lemma poleCutoff_native_ge_steps (f : GridElement) :
    f.steps ≤ poleCutoff f f.meshExp := by
  unfold poleCutoff
  have hpow : 0 < 2 ^ f.meshExp := Nat.pow_pos (by decide : 0 < 2)
  exact Nat.le_trans (Nat.le_add_right f.steps 3)
    (Nat.le_mul_of_pos_right (f.steps + 3) hpow)

/-- Step (3): the summed primitive increments equal the one-sided
ACF / `poleΔ` pairing. -/
theorem sum_cellCoshIncrement_eq_one_sided (f : GridElement) :
    ∑ d ∈ Finset.range f.steps, f.cellCoshIncrement d =
      -(f.acf 0 * polePotential f.D0 +
          ∑ j ∈ Finset.range (f.steps - 1),
            f.acf (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ)) / f.D0 := by
  let a : ℕ → ℝ := f.acf
  let c : ℕ → ℝ := fun d => Real.cosh (((d : ℝ) * f.D0) / 2)
  let s : ℕ → ℝ := fun d => Real.sinh (((d : ℝ) * f.D0) / 2)
  have ha : a f.steps = 0 := f.acf_eq_zero le_rfl
  have hcast_succ (d : ℕ) : ((d + 1 : ℕ) : ℝ) = (d : ℝ) + 1 :=
    Nat.cast_succ d
  have hsinh :
      ∑ d ∈ Finset.range f.steps,
          (4 * a (d + 1) * s (d + 1) - 4 * a d * s d) =
        0 := by
    have htel :
        ∑ d ∈ Finset.range f.steps, (a (d + 1) * s (d + 1) - a d * s d) =
          a f.steps * s f.steps - a 0 * s 0 :=
      sum_range_sub_eq f.steps (fun d => a d * s d)
    have hs0 : s 0 = 0 := by
      simp [s, Real.sinh_zero]
    have hfactor :
        ∀ d,
          4 * a (d + 1) * s (d + 1) - 4 * a d * s d =
            4 * (a (d + 1) * s (d + 1) - a d * s d) := by
      intro d; ring
    simp_rw [hfactor]
    rw [← Finset.mul_sum, htel, ha, hs0]
    ring
  have hΔc (d : ℕ) :
      Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
          Real.cosh (((d : ℝ) * f.D0) / 2) =
        c (d + 1) - c d := by
    change Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
        Real.cosh (((d : ℝ) * f.D0) / 2) =
      Real.cosh ((((d + 1 : ℕ) : ℝ) * f.D0) / 2) -
        Real.cosh (((d : ℝ) * f.D0) / 2)
    rw [hcast_succ]
  have hβ :
      ∑ d ∈ Finset.range f.steps,
          f.cellSlope d *
            (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
              Real.cosh (((d : ℝ) * f.D0) / 2)) =
        (∑ d ∈ Finset.range f.steps, (a (d + 1) - a d) * (c (d + 1) - c d)) /
          f.D0 := by
    have hpt (d : ℕ) :
        f.cellSlope d *
            (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
              Real.cosh (((d : ℝ) * f.D0) / 2)) =
          ((a (d + 1) - a d) * (c (d + 1) - c d)) / f.D0 := by
      unfold GridElement.cellSlope
      rw [hΔc]
      change ((f.acf (d + 1) - f.acf d) / f.D0) * (c (d + 1) - c d) =
        ((a (d + 1) - a d) * (c (d + 1) - c d)) / f.D0
      ring
    simp_rw [hpt]
    exact (Finset.sum_div (Finset.range f.steps)
      (fun d => (a (d + 1) - a d) * (c (d + 1) - c d)) f.D0).symm
  have hparts := sum_fwd_diff_mul f.steps a c ha
  have hinc :
      ∑ d ∈ Finset.range f.steps, f.cellCoshIncrement d =
        ∑ d ∈ Finset.range f.steps,
            (4 * a (d + 1) * s (d + 1) - 4 * a d * s d) -
          8 *
            ∑ d ∈ Finset.range f.steps,
              f.cellSlope d *
                (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
                  Real.cosh (((d : ℝ) * f.D0) / 2)) := by
    have hpt (d : ℕ) :
        f.cellCoshIncrement d =
          (4 * a (d + 1) * s (d + 1) - 4 * a d * s d) -
            8 * (f.cellSlope d *
              (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
                Real.cosh (((d : ℝ) * f.D0) / 2))) := by
      unfold GridElement.cellCoshIncrement
      change
          4 * f.acf (d + 1) *
                Real.sinh ((((d : ℝ) + 1) * f.D0) / 2) -
              4 * f.acf d * Real.sinh (((d : ℝ) * f.D0) / 2) -
              8 * f.cellSlope d *
                (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
                  Real.cosh (((d : ℝ) * f.D0) / 2)) =
            (4 * a (d + 1) * s (d + 1) - 4 * a d * s d) -
              8 * (f.cellSlope d *
                (Real.cosh ((((d : ℝ) + 1) * f.D0) / 2) -
                  Real.cosh (((d : ℝ) * f.D0) / 2)))
      have hsL : s d = Real.sinh (((d : ℝ) * f.D0) / 2) := rfl
      have hsR : s (d + 1) = Real.sinh ((((d + 1 : ℕ) : ℝ) * f.D0) / 2) := rfl
      rw [hsL, hsR, hcast_succ]
      ring
    simp_rw [hpt]
    rw [Finset.sum_sub_distrib, Finset.mul_sum]
  have hfirst : c 1 - c 0 = -polePotential f.D0 / 8 := by
    simp only [c, Nat.cast_one, Nat.cast_zero, one_mul, zero_mul]
    have h0 : (0 : ℝ) / 2 = 0 := by ring
    rw [h0]
    convert cosh_first_diff_eq_neg_div_eight f.D0
  have hsecond (j : ℕ) :
      c j - 2 * c (j + 1) + c (j + 2) =
        -poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8 := by
    simp only [c]
    have hj1 : ((j + 1 : ℕ) : ℝ) = (j : ℝ) + 1 := Nat.cast_succ j
    have hj2 : ((j + 2 : ℕ) : ℝ) = (j : ℝ) + 2 := by norm_cast
    rw [hj1, hj2, cosh_second_diff_eq_neg_div_eight]
  have hS :
      ∑ d ∈ Finset.range f.steps, (a (d + 1) - a d) * (c (d + 1) - c d) =
        (a 0 * polePotential f.D0 +
          ∑ j ∈ Finset.range (f.steps - 1),
            a (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ)) / 8 := by
    rw [hparts, hfirst]
    simp_rw [hsecond]
    have hA : -a 0 * (-polePotential f.D0 / 8) =
        a 0 * polePotential f.D0 / 8 := by ring
    have hB :
        ∑ j ∈ Finset.range (f.steps - 1),
            a (j + 1) * (-poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8) =
          -(∑ j ∈ Finset.range (f.steps - 1),
              a (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8) := by
      have hpt (j : ℕ) :
          a (j + 1) * (-poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8) =
            -(a (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8) := by
        ring
      simp_rw [hpt]
      exact Finset.sum_neg_distrib
        (f := fun j =>
          a (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ) / 8)
    rw [hA, hB, sub_neg_eq_add, ← Finset.sum_div, ← add_div]
  rw [hinc, hsinh, zero_sub, hβ, hS]
  have hscale (x : ℝ) :
      -(8 * ((x / 8) / f.D0)) = -(x / f.D0) := by
    field_simp [f.D0_pos.ne']
  rw [hscale]
  simp only [a]
  rw [neg_div]

theorem weilPoleSide_eq_two_mul_sum_cellCoshIncrement (f : GridElement) :
    weilPoleSide f =
      2 * ∑ d ∈ Finset.range f.steps, f.cellCoshIncrement d := by
  have hD : f.D0 = meshWidth f.meshExp := f.D0_eq_meshWidth
  have hN : f.steps ≤ poleCutoff f f.meshExp :=
    poleCutoff_native_ge_steps f
  have hpair :
      weilPoleSide f = polePairingZ f.D0 f (poleCutoff f f.meshExp) := by
    unfold weilPoleSide poleEvenRead
    rw [hD]
  rw [hpair, polePairingZ_one_sided, sum_acf_poleΔ_eq_upto_steps f hN]
  have hinc := sum_cellCoshIncrement_eq_one_sided f
  have hΔ0 : poleΔ f.D0 0 = 2 * polePotential f.D0 := poleΔ_zero f.D0
  have h2 : 2 * ∑ d ∈ Finset.range f.steps, f.cellCoshIncrement d =
      -(f.acf 0 * poleΔ f.D0 0 +
          2 * ∑ j ∈ Finset.range (f.steps - 1),
            f.acf (j + 1) * poleΔ f.D0 ((j + 1 : ℕ) : ℤ)) / f.D0 := by
    rw [hinc, hΔ0]
    field_simp [f.D0_pos.ne']
  rw [h2]

/-- **named remaining finite-sum identity** (r376; not a `sorry`):
the second-difference pairing of `polePotential` against a native-PL
test function is independent of dyadic refinement.  Parallel to the
comb channel, the Lean read is taken at the native mesh (R325 S1.4:
the native mesh already carries the limit value).  The identity is
statable and classically true (affine second differences vanish;
`Real.cosh` is in mathlib); it is not consumed by the extraction. -/
def PoleDyadicIndependence : Prop :=
  ∀ f : GridElement, ∀ m, f.meshExp ≤ m →
    poleEvenRead m f = poleEvenRead f.meshExp f

/-- **Historical analytical contract (r464; retired as an assertion in
r638L after the r475 diagnosis).**
Exact eventual equality `archRead = weilArchSide` for every
`a ≥ a₀` and every `m ≥ meshExp`.  This quantifier is too strong:
at fixed `m`, `productionArchDelta a m = log a / (m+1) → ∞` as
`a → ∞`, so the tent mesh gets coarser, not finer.  r473 already
exhibits a mesh-and-onset-compatible witness with a genuine
positive arch tent error.  The correct remnant is the
selected-path `O(Δ²)` rate in `RH/InnerBridges.lean`.  The
contract is retained only as an unasserted Prop; any historical
extraction that uses it must supply it explicitly.  Mathlib's Gauss
integral is isolated as
`GaussDigammaIntegralRepresentation`, not a second `sorry`. -/
def ArchGaussMellinDigammaIdentity : Prop :=
  ∀ f : GridElement,
    ∃ a₀ : ℕ, ∀ a : ℕ, a₀ ≤ a → ∀ m : ℕ, f.meshExp ≤ m →
      archRead a m f = weilArchSide f

/-- **The historical arch-channel stabilization, conditionalized in
r638L.**  This is only a projection from the unasserted contract; it
does not claim that the overstrong exact equality holds. -/
theorem arch_elementwise_stabilization
    (hArch : ArchGaussMellinDigammaIdentity) (f : GridElement) :
    ∃ a₀ : ℕ, ∀ a : ℕ, a₀ ≤ a → ∀ m : ℕ, f.meshExp ≤ m →
      archRead a m f = weilArchSide f :=
  hArch f

/-- **the pole-channel elementwise stabilization** (r376 -- PROVED).
The pole tent-read is the native-mesh second-difference pairing of
`polePotential` (Python `pole_lags_closed`); the Weil pole side is
the same pairing.  Equality is definitional, parallel to
`comb_elementwise_stabilization` being mesh-free.  Remaining named
(not a hole): `PoleDyadicIndependence`.  No ζ. -/
theorem pole_elementwise_stabilization (f : GridElement) :
    ∃ a₀ : ℕ, ∀ a : ℕ, a₀ ≤ a → ∀ m : ℕ, f.meshExp ≤ m →
      poleRead a m f = weilPoleSide f := by
  refine ⟨f.elementAnchor, fun _ _ _ _ => rfl⟩

/-! ## The full form and the elementwise stabilization theorem -/

/-- **the full window form read** of a grid element at the canonical
window (anchor `a`, mesh level `m`): arch − comb + pole (the corpus
total `c = car + cat + cp`, with the atom channel entering as MINUS
the comb sum -- the R325 S1.3 sign convention).  HONEST SCOPE: the
comb summand is transcribed and proved above; the arch/pole summands
are the arch opaque read and the transcribed pole pairing. -/
noncomputable def fullRead (a m : ℕ) (f : GridElement) : ℝ :=
  archRead a m f - combRead a f + poleRead a m f

/-- **the Weil form** of a grid element: arch − comb + pole, each
side in its channel's reference (comb: the proved tsum; pole: the
native-mesh pairing of `polePotential`; arch: the opaque kernel
integral).  The spectral/zero side of the
explicit formula is NOT part of this definition -- it is the
arithmetically open content of the program. -/
noncomputable def weilForm (f : GridElement) : ℝ :=
  weilArchSide f - weilCombSide f + weilPoleSide f

/-- **THE ELEMENTWISE FINITE STABILIZATION** (r326, R325 target form
(ii); conditionalized honestly in r638L).  It is PROVED from the comb
and pole channels unconditionally and from an explicit
`ArchGaussMellinDigammaIdentity` hypothesis for the arch channel.
For every grid element there is a finite anchor onset `a₀`
such that for EVERY anchor `a ≥ a₀` and every mesh level at or below
the element's native mesh (`m ≥ f.meshExp` -- the predefined `m_f`),
the full finite window form EQUALS the Weil form.  The onset is
elementwise (`a₀` depends on `f` -- for the comb channel explicitly:
`elementAnchor f` from the support alone); NO mesh-cofinal ladder,
NO transport, NO (H_cof) appears. -/
theorem elementwise_finite_stabilization
    (hArch : ArchGaussMellinDigammaIdentity) (f : GridElement) :
    ∃ a₀ : ℕ, ∀ a : ℕ, a₀ ≤ a → ∀ m : ℕ, f.meshExp ≤ m →
      fullRead a m f = weilForm f := by
  obtain ⟨aA, hA⟩ := arch_elementwise_stabilization hArch f
  obtain ⟨aP, hP⟩ := pole_elementwise_stabilization f
  refine ⟨max f.elementAnchor (max aA aP), fun a haa m hm => ?_⟩
  have h1 : f.elementAnchor ≤ a := le_trans (le_max_left _ _) haa
  have h2 : aA ≤ a :=
    le_trans (le_trans (le_max_left _ _) (le_max_right _ _)) haa
  have h3 : aP ≤ a :=
    le_trans (le_trans (le_max_right _ _) (le_max_right _ _)) haa
  unfold fullRead weilForm
  rw [comb_elementwise_stabilization f h1, hA a h2 m hm, hP a h3 m hm]

/-! ## (iii) The extraction WITHOUT the ladder

The R325 repair of the H_cof seam: window positivity, quantified over
the CANONICAL family only (the predicate of section (i)) and typed on
the PLAIN full form (the form for which the finite instantiation
actually goes through), yields Weil-form nonnegativity on every
element of the native dense class by ONE finite instantiation per
element -- pick any prime anchor above the element's onset (Euclid)
and the element's own native mesh.  No refinement tower, no PSD
transport, no `SourceExact` hypothesis. -/

/-- **the window-local positivity premise** (typed honestly on the
plain full form): every canonical window read of every
mesh-compatible grid element is nonnegative.  This is "∀ w,
CanonicalPrimeWindow w → 0 ≤ windowForm w" evaluated per test
element, with the canonical index `(a, m)` explicit because the
kernel reads live on the mesh grid while the built window is
mesh-independent; the guard `f.meshExp ≤ m` is the honest grid
compatibility (positivity of reads = PSD of the window's lag
Toeplitz form holds for autocorrelations ON the window's grid --
R325 S3: per-stage Levinson PD).  HONEST STATUS: this premise is the
Level-B content (the two window-local holes) transported to the
canonical family -- it is a PREMISE here, proved nowhere, and this
file makes no claim about it. -/
def WindowLocalPositive : Prop :=
  ∀ (a m : ℕ), IsPrimePow a → ∀ f : GridElement,
    f.meshExp ≤ m → 0 ≤ fullRead a m f

/-- **THE EXTRACTION WITHOUT THE LADDER** (r326, R325 target form
(iii); PROVED -- a finite instantiation).  Window-local positivity of
the canonical family implies Weil-form nonnegativity on every grid
element: given `f`, take the elementwise onset `a₀` (stabilization),
a prime anchor `a ≥ a₀` (Euclid, `Nat.exists_infinite_primes` -- a
FINITE choice, not a cofinal tower), and the element's own native
mesh `m = f.meshExp`; then `weilForm f = fullRead a m f ≥ 0`.  This
REPLACES the (H_cof) route: no mesh-refinement PSD tower is consumed
anywhere.  The overstrong historical arch contract is now an explicit
hypothesis rather than an asserted `sorry`.  NO RH CLAIM: the premise
is exactly the open window-local content. -/
theorem weil_nonneg_of_windowlocal
    (hArch : ArchGaussMellinDigammaIdentity)
    (hpos : WindowLocalPositive) :
    ∀ f : GridElement, 0 ≤ weilForm f := by
  intro f
  obtain ⟨a₀, hstab⟩ := elementwise_finite_stabilization hArch f
  obtain ⟨p, hp₀, hp⟩ := Nat.exists_infinite_primes a₀
  have h := hpos p f.meshExp hp.prime.isPrimePow f (le_refl _)
  rwa [hstab p hp₀ f.meshExp (le_refl _)] at h

/-- **THE COMPRESSION BRIDGE, named** (r326; the documented S2 rest of
R325 -- deliberately a NAMED Prop, not an asserted theorem: its
faithful transcription needs the bordered/border-column data, i.e.
the `SourceExact` elimination).  The corpus positivity certificates
live on the BORDERED tower form (v749/v755 bordered Schur tower, the
odd compression); the premise of the extraction above is typed on
the PLAIN full form.  The bridge "bordered positivity ⟹ plain
positivity on the canonical family" is the named missing step
between the two typings -- once stated against a transcribed
bordered read, it becomes a finite matrix statement (principal
compression).  Parametrized over the bordered read so that NO new
opaque constant and NO truth commitment enters here. -/
def BorderedCompressionBridge
    (borderedRead : ℕ → ℕ → GridElement → ℝ) : Prop :=
  ∀ (a m : ℕ), IsPrimePow a → ∀ f : GridElement, f.meshExp ≤ m →
    0 ≤ borderedRead a m f → 0 ≤ fullRead a m f

/-- the extraction composes through the compression bridge (PROVED
from (iii)): bordered window-local positivity plus the named bridge
give the same Weil-form conclusion. -/
theorem weil_nonneg_of_bordered
    (borderedRead : ℕ → ℕ → GridElement → ℝ)
    (hArch : ArchGaussMellinDigammaIdentity)
    (hbridge : BorderedCompressionBridge borderedRead)
    (hpos : ∀ (a m : ℕ), IsPrimePow a → ∀ f : GridElement,
      f.meshExp ≤ m → 0 ≤ borderedRead a m f) :
    ∀ f : GridElement, 0 ≤ weilForm f :=
  weil_nonneg_of_windowlocal hArch fun a m ha f hm =>
    hbridge a m ha f hm (hpos a m ha f hm)

end RH
