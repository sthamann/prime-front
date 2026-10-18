/-
RH/InnerBridges.lean -- FINITE INNER-BRIDGE ALGEBRA
(r464, PRIME.RDAGGER.INNER_BRIDGES.01).

The selected A-cap implication has two logically separate parts:

  (1) CHANNEL TRANSCRIPTION: every mesh-compatible GridElement read is
      the quadratic value of a direction in the augmented cap space;
  (2) FINITE PSD: A_cap.PosSemidef makes that quadratic value nonnegative.

Part (2) is proved below.  Part (1) is the one named remainder
`SelectedReadQuadraticRepresentation`.  It includes the real
quantifier issue: `GridElement.steps` is not bounded by the cap, so
the old bridge cannot be obtained from a degree-<cap polynomial
identification without an additional high-degree reduction theorem.

r470 seals the exact finite obstruction to part (1): the original
quantifier admits `steps > cap` (proved), and a mesh-and-onset-
compatible native Hessian at k=5 is indefinite of rank larger
than `cap+1` while `A_cap` is PD (numerical seal).  No new `sorry`.

r473 redesigns the extraction joint after that obstruction.
The class `A_cap` can carry is the polynomial class of degree
`< cap`: `selectedACapPsdImpliesPolynomialReads` is the r464
PSD algebra on that finite-dimensional space (moment evaluation,
no `steps` problem).  Native `GridElement` reads differ from
the classical Guinand--Weil value by the arch tent error
(`fullRead_weilForm_gap_eq_arch`, proved from the exact comb
and pole channels).  The polynomial-to-GridElement gap is the
named outer bridge `SelectedPolynomialApproximatesGrid`.
No infinitely-many-`k` statement.  No new `sorry`.

r475 isolates F1(ii) and seals the arch tent rate.  The exact
eventual identity is the wrong quantifier (`Δ = log a/(m+1)`
grows at fixed `m`) and Mathlib still lacks Gauss's integral
(`GaussDigammaIntegralRepresentation`, named, not a sorry).
The selected-path remainder is `O(Δ_k²)` for each fixed `f`
(`SelectedArchErrorQuadraticRate`); the implication
`err(k,f) → 0` as `k → ∞` at fixed `f` is proved from that
named rate and `selectedDelta_tendsto_zero`.  This is a
fixed-`f` convergence statement, not an infinitely-many-`k`
positivity claim.

Claim boundary: research documentation.  NO RH CLAIM.
-/
import RH.Selected
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Topology.Order.Basic

namespace RH

open Matrix

/-- The augmented quadratic read of a selected production window. -/
noncomputable def selectedReadQuadratic
    (k : ℕ) (hk : 0 < k)
    (z : Fin (selectedRealWindow k hk).cap ⊕ Unit → ℝ) : ℝ :=
  z ⬝ᵥ ((selectedRealWindow k hk).toPrimeWindow.A
    (selectedRealWindow k hk).cap *ᵥ z)

/-- **The exact remaining channel transcription.**

For every selected window and every mesh-compatible native test
element, construct the augmented cap-space direction whose quadratic
value is the concrete `fullRead`.  This is where the Fourier/Chebyshev
coordinates, whitening, border coordinate, and pole correction must
be identified.  It is a named Prop, not asserted.

The proposition deliberately retains the original unbounded `steps`
quantifier; no hidden `steps ≤ cap` weakening is introduced. -/
def SelectedReadQuadraticRepresentation : Prop :=
  ∀ (k : ℕ) (hk : 0 < k) (f : GridElement),
    f.meshExp ≤ selectedMesh k →
      ∃ z : Fin (selectedRealWindow k hk).cap ⊕ Unit → ℝ,
        fullRead (selectedAnchor k) (selectedMesh k) f =
          selectedReadQuadratic k hk z

/-- The original r434 target, retained byte-for-byte in mathematical
content: selected A-cap PSD implies every mesh-compatible plain read
is nonnegative. -/
def SelectedACapPsdImpliesPlainReads : Prop :=
  ∀ (k : ℕ) (hk : 0 < k),
    ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef →
      ∀ f : GridElement, f.meshExp ≤ selectedMesh k →
        0 ≤ fullRead (selectedAnchor k) (selectedMesh k) f

/-- **FINITE PSD HALF CLOSED (r464).**  Once the read direction is
transcribed, A-cap semidefiniteness proves the original plain-read
bridge by the defining quadratic inequality. -/
theorem selectedACapPsdImpliesPlainReads_of_representation
    (hrep : SelectedReadQuadraticRepresentation) :
    SelectedACapPsdImpliesPlainReads := by
  intro k hk hA f hm
  obtain ⟨z, hz⟩ := hrep k hk f hm
  rw [hz]
  exact hA.dotProduct_mulVec_nonneg z

/-! ## r470: exact finite obstruction to the channel map

The original representation quantifies over every mesh-compatible
`GridElement`, with `steps` unbounded.  The selected cap is
`(S+1)/2` with `S = selectedMesh k`, so a degree-`< cap`
identification cannot cover the original quantifier.  The
arithmetic witness is proved below.

A stronger finite obstruction is numerical (probe
`quadrep_probe.py`): even after the onset guard
`elementAnchor f ≤ selectedAnchor k`, the native Hessian of
`fullRead` at `k=5` is indefinite of rank `24 > cap+1 = 11`,
while `A_cap` is positive definite.  A negative native read
cannot equal a quadratic value of a PSD matrix.  The lemma
`quadraticRepresentation_refuted_of_negative_read` records
that finite implication; the signed witness itself is the
named Prop `SelectedOnsetCompatibleNegativeRead` (not a
`sorry`).  NO RH CLAIM. -/

lemma selectedRoot_five : selectedRoot 5 = 2 := by
  unfold selectedRoot
  rw [Nat.floor_eq_iff (Real.sqrt_nonneg _)]
  constructor
  · rw [Real.le_sqrt (Nat.cast_nonneg 2) (Nat.cast_nonneg 5)]
    norm_num
  · have h3 : ((2 : ℕ) : ℝ) + 1 = 3 := by norm_num
    rw [h3, Real.sqrt_lt (Nat.cast_nonneg 5) (by norm_num : (0 : ℝ) ≤ 3)]
    norm_num

lemma selectedMesh_five : selectedMesh 5 = 19 := by
  unfold selectedMesh
  rw [selectedRoot_five]
  native_decide

lemma selectedWindow_S_eq_mesh (k : ℕ) (hk : 0 < k) :
    (selectedRealWindow k hk).toPrimeWindow.S = selectedMesh k :=
  rfl

lemma selected_cap_five (hk : 0 < 5) :
    (selectedRealWindow 5 hk).toPrimeWindow.cap = 10 := by
  unfold PrimeWindow.cap
  rw [selectedWindow_S_eq_mesh 5 hk, selectedMesh_five]

/-- Concrete mesh-compatible native element with `steps > cap`
at the r464 k=5 arithmetic witness. -/
def selectedCapStepsWitness : GridElement where
  steps := 11
  meshExp := 19
  x := fun _ => 0

/-- **r470, proved:** the original mesh-only guard admits a
native element whose step count strictly exceeds the selected
cap.  This is the quantifier obstruction to a degree-`< cap`
channel, not a statement about infinitely many `k`. -/
theorem exists_mesh_compatible_steps_gt_cap :
    ∃ (k : ℕ) (hk : 0 < k) (f : GridElement),
      f.meshExp ≤ selectedMesh k ∧
      (selectedRealWindow k hk).toPrimeWindow.cap < f.steps := by
  refine ⟨5, Nat.succ_pos 4, selectedCapStepsWitness, ?_, ?_⟩
  · simp [selectedCapStepsWitness, selectedMesh_five]
  · simp [selectedCapStepsWitness, selected_cap_five (Nat.succ_pos 4)]

/-- **r470 named obstruction.**  A mesh-and-onset-compatible
native element with strictly negative `fullRead`.  On a PSD
cap this refutes `SelectedReadQuadraticRepresentation` by
`quadraticRepresentation_refuted_of_negative_read`.  Sealed
numerically at `k=5` (`meshExp=3`, `steps=24`); not a `sorry`. -/
def SelectedOnsetCompatibleNegativeRead : Prop :=
  ∃ (k : ℕ) (f : GridElement),
    0 < k ∧
    f.meshExp ≤ selectedMesh k ∧
    f.elementAnchor ≤ selectedAnchor k ∧
    fullRead (selectedAnchor k) (selectedMesh k) f < 0

/-- Finite implication: a negative mesh-compatible read on a
PSD selected cap refutes the r464 channel representation.
No new `sorry`.  NO RH CLAIM. -/
theorem quadraticRepresentation_refuted_of_negative_read
    {k : ℕ} (hk : 0 < k) (f : GridElement)
    (hm : f.meshExp ≤ selectedMesh k)
    (hneg : fullRead (selectedAnchor k) (selectedMesh k) f < 0)
    (hA : ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef) :
    ¬ SelectedReadQuadraticRepresentation := by
  intro hrep
  obtain ⟨z, hz⟩ := hrep k hk f hm
  have hnn : 0 ≤ fullRead (selectedAnchor k) (selectedMesh k) f := by
    rw [hz]
    exact hA.dotProduct_mulVec_nonneg z
  exact (not_le_of_gt hneg) hnn

/-! ## r473: polynomial-class bridge and the arch error identity

The r470 obstruction shows that the native `GridElement` class
is larger than the cap space.  The class the finite matrix
`A_cap` actually sees is the coefficient-plus-border space of
real polynomials of degree `< cap`.  On that class the channel
is the moment evaluation of `A_cap`, and PSD implies
nonnegativity by the r464 algebra.  NO RH CLAIM. -/

open Polynomial
open VonMangoldtWindow (coeffPoly coeffPoly_eval)

namespace PrimeWindow

variable (w : PrimeWindow)

/-- Discrete μ-mass of `p²` on the real window. -/
noncomputable def muSq (p : Polynomial ℝ) : ℝ :=
  ∑ j, w.combWeight j * p.eval (w.nodes j) ^ 2

/-- Discrete ν-mass of `p²` on the real window. -/
noncomputable def nuSq (p : Polynomial ℝ) : ℝ :=
  ∑ j, w.archWeight j * p.eval (w.nodes j) ^ 2

/-- **Moment dictionary (r473, PROVED).**  The Hankel quadratic
form is `μ(p_x²) − ν(p_x²)` for the coefficient polynomial of
`x`.  Finite algebra; no `GridElement.steps`. -/
theorem hankel_quadform (n : ℕ) (x : Fin n → ℝ) :
    x ⬝ᵥ (w.hankel n *ᵥ x) = w.muSq (coeffPoly x) - w.nuSq (coeffPoly x) := by
  classical
  have hmom : ∀ m : ℕ, w.mom m = ∑ j, w.weight j * w.nodes j ^ m := by
    intro m
    rfl
  have hsplit : w.muSq (coeffPoly x) - w.nuSq (coeffPoly x)
      = ∑ j, w.weight j * (coeffPoly x).eval (w.nodes j) ^ 2 := by
    rw [muSq, nuSq, ← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [weight]
    ring
  rw [hsplit]
  have hrhs : ∀ j : Fin w.S,
      w.weight j * (coeffPoly x).eval (w.nodes j) ^ 2
      = ∑ i : Fin n, ∑ k : Fin n,
          x i * x k * (w.weight j * w.nodes j ^ ((i : ℕ) + (k : ℕ))) := by
    intro j
    rw [coeffPoly_eval, sq, Finset.sum_mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [pow_add]
    ring
  calc x ⬝ᵥ (w.hankel n *ᵥ x)
      = ∑ i : Fin n, ∑ k : Fin n,
          x i * x k * w.mom ((i : ℕ) + (k : ℕ)) := by
        simp only [dotProduct, Matrix.mulVec, hankel, dotProduct]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun k _ => ?_
        ring
    _ = ∑ i : Fin n, ∑ k : Fin n, ∑ j,
          x i * x k * (w.weight j * w.nodes j ^ ((i : ℕ) + (k : ℕ))) := by
        refine Finset.sum_congr rfl fun i _ =>
          Finset.sum_congr rfl fun k _ => ?_
        rw [hmom, Finset.mul_sum]
    _ = ∑ i : Fin n, ∑ j, ∑ k : Fin n,
          x i * x k * (w.weight j * w.nodes j ^ ((i : ℕ) + (k : ℕ))) :=
        Finset.sum_congr rfl fun i _ => Finset.sum_comm
    _ = ∑ j, ∑ i : Fin n, ∑ k : Fin n,
          x i * x k * (w.weight j * w.nodes j ^ ((i : ℕ) + (k : ℕ))) :=
        Finset.sum_comm
    _ = ∑ j, w.weight j * (coeffPoly x).eval (w.nodes j) ^ 2 := by
        refine Finset.sum_congr rfl fun j _ => (hrhs j).symm

/-- **Augmented quadratic form (r473, PROVED).**  At the test
vector `(x, t)` the cap form splits as the Hankel wall, the
mixed border, and the budget corner. -/
theorem A_quadform (n : ℕ) (x : Fin n → ℝ) (t : ℝ) :
    Sum.elim x (fun _ : Unit => t) ⬝ᵥ (w.A n *ᵥ Sum.elim x (fun _ => t))
      = x ⬝ᵥ (w.hankel n *ᵥ x) + 2 * t * (w.borderVec n ⬝ᵥ x)
        + w.B * t ^ 2 := by
  have h1 : ∀ i : Fin n,
      (w.A n *ᵥ Sum.elim x (fun _ : Unit => t)) (Sum.inl i)
        = (w.hankel n *ᵥ x) i + w.u i * t := by
    intro i
    simp [A, Matrix.mulVec, dotProduct, Fintype.sum_sum_type, hankel]
  have h2 : (w.A n *ᵥ Sum.elim x (fun _ : Unit => t)) (Sum.inr ())
      = w.borderVec n ⬝ᵥ x + w.B * t := by
    simp [A, Matrix.mulVec, dotProduct, Fintype.sum_sum_type, borderVec]
  calc Sum.elim x (fun _ : Unit => t) ⬝ᵥ (w.A n *ᵥ Sum.elim x (fun _ => t))
      = (∑ i : Fin n,
          x i * (w.A n *ᵥ Sum.elim x (fun _ : Unit => t)) (Sum.inl i))
        + t * (w.A n *ᵥ Sum.elim x (fun _ : Unit => t)) (Sum.inr ()) := by
        simp [dotProduct, Fintype.sum_sum_type]
    _ = (∑ i : Fin n, x i * ((w.hankel n *ᵥ x) i + w.u i * t))
        + t * (w.borderVec n ⬝ᵥ x + w.B * t) := by
        rw [h2]
        congr 1
        exact Finset.sum_congr rfl fun i _ => by rw [h1 i]
    _ = x ⬝ᵥ (w.hankel n *ᵥ x) + 2 * t * (w.borderVec n ⬝ᵥ x)
        + w.B * t ^ 2 := by
        have hsum : ∑ i : Fin n,
            x i * ((w.hankel n *ᵥ x) i + w.u i * t)
            = (∑ i : Fin n, x i * (w.hankel n *ᵥ x) i)
              + t * ∑ i : Fin n, w.u i * x i := by
          rw [Finset.mul_sum, ← Finset.sum_add_distrib]
          exact Finset.sum_congr rfl fun i _ => by ring
        have hu : ∑ i : Fin n, w.u i * x i
            = ∑ i : Fin n, w.borderVec n i * x i := by
          simp [borderVec]
        simp only [dotProduct]
        rw [hsum, hu]
        ring

end PrimeWindow

/-- Polynomial-class read: the `A_cap` quadratic form of the
coefficient vector of `p` (degree `< cap` after truncation)
together with a border coordinate.  This is the moment
evaluation the finite matrix can see. -/
noncomputable def selectedPolynomialRead
    (k : ℕ) (hk : 0 < k) (p : Polynomial ℝ) (t : ℝ) : ℝ :=
  let x : Fin (selectedRealWindow k hk).cap → ℝ :=
    fun i => p.coeff (i : ℕ)
  selectedReadQuadratic k hk (Sum.elim x fun _ => t)

/-- **POLYNOMIAL-CLASS BRIDGE (r473, PROVED).**  `A_cap ⪰ 0`
implies every degree-`< cap` polynomial read is nonnegative.
The channel is the identity on the cap-plus-border space; there
is no `steps` quantifier.  Fixed `k` only.  NO RH CLAIM. -/
theorem selectedACapPsdImpliesPolynomialReads
    {k : ℕ} (hk : 0 < k)
    (hA : ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef)
    (z : Fin (selectedRealWindow k hk).cap ⊕ Unit → ℝ) :
    0 ≤ selectedReadQuadratic k hk z :=
  hA.dotProduct_mulVec_nonneg z

theorem selectedACapPsdImpliesPolynomialReads_poly
    {k : ℕ} (hk : 0 < k)
    (hA : ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef)
    (p : Polynomial ℝ) (t : ℝ) :
    0 ≤ selectedPolynomialRead k hk p t :=
  selectedACapPsdImpliesPolynomialReads hk hA _

/-- Arch tent discrepancy of a selected window against the
classical u-space pairing `weilArchSide` (r475: no longer
opaque). -/
noncomputable def selectedArchError (k : ℕ) (f : GridElement) : ℝ :=
  |archRead (selectedAnchor k) (selectedMesh k) f - weilArchSide f|

/-- **Exact onset gap (r473, PROVED).**  Once the comb channel
has covered the support, `fullRead − weilForm` is exactly the
arch tent error.  Pole equality is definitional.  Does not
consume `arch_gauss_mellin_digamma_identity`.  NO RH CLAIM. -/
theorem fullRead_weilForm_gap_eq_arch
    {a m : ℕ} (f : GridElement) (ha : f.elementAnchor ≤ a) :
    fullRead a m f - weilForm f = archRead a m f - weilArchSide f := by
  unfold fullRead weilForm poleRead weilPoleSide
  rw [comb_elementwise_stabilization f ha]
  ring

theorem selected_fullRead_weil_absError
    {k : ℕ} (f : GridElement)
    (ha : f.elementAnchor ≤ selectedAnchor k) :
    |fullRead (selectedAnchor k) (selectedMesh k) f - weilForm f|
      = selectedArchError k f := by
  unfold selectedArchError
  rw [fullRead_weilForm_gap_eq_arch f ha]

/-- **Named outer bridge (r473).**  At a fixed selected window,
every mesh-compatible native read lies within the arch tent
error of the polynomial-class `A_cap` image.  On a PSD cap
this is `fullRead ≥ −selectedArchError`.  Sealed numerically
at the r470 k=5 witness; not a `sorry`.  No infinitely-many-`k`
quantifier. -/
def SelectedPolynomialApproximatesGrid : Prop :=
  ∀ (k : ℕ) (hk : 0 < k) (f : GridElement),
    f.meshExp ≤ selectedMesh k →
      ∃ z : Fin (selectedRealWindow k hk).cap ⊕ Unit → ℝ,
        |fullRead (selectedAnchor k) (selectedMesh k) f
          - selectedReadQuadratic k hk z|
          ≤ selectedArchError k f

/-- **Cone plus named approx (r473, PROVED as a function of the
named bridge).**  PSD `A_cap` and the polynomial approximation
give `fullRead ≥ −err_arch` at a single window.  Fixed `k` only.
NO RH CLAIM. -/
theorem selected_reads_ge_neg_archError_of_approx
    {k : ℕ} (hk : 0 < k) (f : GridElement)
    (hm : f.meshExp ≤ selectedMesh k)
    (hA : ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef)
    (happrox : SelectedPolynomialApproximatesGrid) :
    -selectedArchError k f
      ≤ fullRead (selectedAnchor k) (selectedMesh k) f := by
  obtain ⟨z, hz⟩ := happrox k hk f hm
  have hnn : 0 ≤ selectedReadQuadratic k hk z :=
    selectedACapPsdImpliesPolynomialReads hk hA z
  have hside := abs_le.mp hz
  linarith

/-- Onset-compatible form: `weilForm ≥ −2 err_arch` at a single
window, from the proved arch-gap identity plus the named approx.
Fixed `k` only.  NO RH CLAIM. -/
theorem weilForm_ge_neg_two_archError_of_approx
    {k : ℕ} (hk : 0 < k) (f : GridElement)
    (hm : f.meshExp ≤ selectedMesh k)
    (ha : f.elementAnchor ≤ selectedAnchor k)
    (hA : ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef)
    (happrox : SelectedPolynomialApproximatesGrid) :
    -2 * selectedArchError k f ≤ weilForm f := by
  have hrd := selected_reads_ge_neg_archError_of_approx hk f hm hA happrox
  have hgap := selected_fullRead_weil_absError f ha
  have hpart : weilForm f
      ≥ fullRead (selectedAnchor k) (selectedMesh k) f
        - selectedArchError k f := by
    have := abs_le.mp (le_of_eq hgap)
    linarith
  linarith

/-! ## r475: arch tent rate at fixed `f`

`productionArchDelta a m = log a / (m+1)` grows in `a` at fixed
`m`, so the r464 exact-equality quantifier cannot be a
refinement statement.  Along the selected sequence
`Δ_k = 2^{-⌊√k⌋} log 2 → 0`, the tent error is `O(Δ_k²)`
(numerical seal: err/Δ² ≈ 3.99 at k=5 and ≈ 3.85 at k=9 for
the r470 witness).  The named rate plus the proved
`selectedDelta_tendsto_zero` give `err(k,f) → 0` at each
fixed `f`.  No infinitely-many-`k` positivity.  NO RH CLAIM. -/

open Filter
open scoped Topology

/-- Selected lag equals the production arch spacing. -/
theorem productionArchDelta_selected (k : ℕ) :
    productionArchDelta (selectedAnchor k) (selectedMesh k) =
      selectedDelta k :=
  rfl

/-- **Why the exact identity cannot close at fixed mesh (r475,
PROVED).**  For each fixed `m`, the production spacing
`log a / (m+1)` tends to `+∞` as `a → ∞`.  The inner
quantifier of `ArchGaussMellinDigammaIdentity` therefore
asks for exact tent/integral equality on meshes that become
arbitrarily coarse. -/
theorem productionArchDelta_tendsto_atTop (m : ℕ) :
    Tendsto (fun a : ℕ => productionArchDelta a m) atTop atTop := by
  have hden : (0 : ℝ) < (m + 1 : ℝ) := by positivity
  have hlog : Tendsto (fun a : ℕ => Real.log (a : ℝ)) atTop atTop :=
    Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop
  unfold productionArchDelta
  simpa [div_eq_mul_inv] using
    hlog.atTop_mul_const (inv_pos.mpr hden)

/-- Explicit majorant used by the named `O(Δ²)` rate.
Nonnegative by construction. -/
noncomputable def archRateConst (f : GridElement) : ℝ :=
  (1 + f.supportBound) ^ 2 *
    (1 + ∑ i : Fin f.steps, |f.x i|) ^ 2

theorem archRateConst_nonneg (f : GridElement) : 0 ≤ archRateConst f := by
  unfold archRateConst
  positivity

/- FALSIFIED as stated: `steps=1`, `meshExp=6`, `x₀=1` gives
normalized error `8.0283 > archRateConst = 4.1259765625`.
Use `SelectedArchErrorQuadraticRateExists` from
`RH.SelectedArchErrorQuadraticRateClassical`. -/
/-- **Named `O(Δ²)` rate (r475).**  For each fixed `f` there is a
finite onset `k₀` past which the selected arch tent error is
bounded by `archRateConst f · Δ_k²`.  Sealed numerically on
the r470 witness (`err/Δ² = 3.9893` at k=5, `3.8466` at k=9).
Not a `sorry`.  Fixed-`f` only. -/
def SelectedArchErrorQuadraticRate : Prop :=
  ∀ f : GridElement, ∃ k0 : ℕ,
    ∀ k : ℕ, k0 ≤ k → ∀ hk : 0 < k,
      f.meshExp ≤ selectedMesh k →
      f.elementAnchor ≤ selectedAnchor k →
        selectedArchError k f ≤ archRateConst f * selectedDelta k ^ 2

/-- **Fixed-`f` convergence (r475, PROVED as a function of the
named rate).**  `err_arch(k,f) → 0` as `k → ∞` for each fixed
`f`.  Uses `selectedDelta_tendsto_zero`.  This is not a
positivity statement and not a statement that infinitely many
windows lie in the cone.  NO RH CLAIM. -/
theorem selectedArchError_tendsto_zero_of_rate
    (hrate : SelectedArchErrorQuadraticRate) (f : GridElement) :
    Tendsto (fun k : ℕ => selectedArchError k f) atTop (nhds 0) := by
  obtain ⟨k0, hk0⟩ := hrate f
  have hΔ2 : Tendsto (fun k : ℕ => selectedDelta k ^ 2) atTop (nhds 0) := by
    simpa [pow_two] using selectedDelta_tendsto_zero.mul selectedDelta_tendsto_zero
  have hC : Tendsto (fun k : ℕ => archRateConst f * selectedDelta k ^ 2)
      atTop (nhds 0) := by
    convert hΔ2.const_mul (archRateConst f) using 1
    ring
  have hcov := selected_covers f.elementAnchor f.meshExp
  refine squeeze_zero' (Eventually.of_forall fun _ => abs_nonneg _) ?_ hC
  filter_upwards [eventually_ge_atTop k0, hcov] with k hk0' hcovk
  obtain ⟨hkpos, ha, hm⟩ := hcovk
  exact hk0 k hk0' hkpos hm ha

end RH
