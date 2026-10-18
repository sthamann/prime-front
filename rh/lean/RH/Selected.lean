/-
RH/Selected.lean -- EXACT REAL DOMAIN AND THE MINIMAL QUANTIFIER
(r397, PRIME.RH.EXACT_SELECTED_DOMAIN.01; reviewer adjudication
DCCLXII).

WHY THIS FILE EXISTS.  The C1 domain `CanonicalWindow` (RH/Canonical.lean)
is a predicate on RATIONAL certificate windows: mesh-tolerance on
node/comb/arch, EXACT u/B match against the completed real source.
Two defects, both fatal as a quantifier domain:

  (A) POSSIBLE EMPTINESS.  After exact real transcription the border
      column and the budget are generically irrational, so no rational
      `VonMangoldtWindow` can satisfy u/B-fidelity.  The C1 docstring
      already records that nonemptiness is unprovable while the
      completion is opaque.  Then `lstar_canonical` /
      `terminal_q_canonical` would be vacuous.
  (B) TOO-COARSE APPROXIMATION.  Mesh-width error is not coupled to
      the shrinking L* margin (metric firewall: 10⁻³ sensitivity).
      "Real source near rational source" is not a positivity proof
      (the r310b warning at `rational_window_approximates`).

THE REPAIR.  Construct the real window TOTALLY, do not cut it out of
the rationals.

  * `RealCanonicalWindow` -- ℝ-fields, wellformedness of
    `PrimeWindow` plus `budget_pos`.  Not a parallel world:
    `toPrimeWindow` is definitional; the rational
    `VonMangoldtWindow` stays the certificate object;
    `RepresentsWindow` (RH/Source.lean) is the certificate
    relating a rational window to this real object, not a domain.
  * `W^ℝ(a,m) = ExactFold(ExactPrimeSource(a), ExactArch(a,m),
    ExactBorder(a,m), ExactBudget(a,m))` -- four Exact blocks as
    definitions over the genuine real source (`log` / `Λ` / the
    named opaque completion for arch/border/budget) plus the
    exact fold on the grid.  TOTAL: no emptiness question.
  * THE SELECTED SEQUENCE (one pre-defined cofinal ladder; no
    positivity transport along a mesh tower):
        a_k = 2^k,   r_k = ⌊√k⌋,   m_k = k·2^{r_k} − 1
    (k ≥ 1; k = 0 is excluded because 2^0 = 1 is not a prime power
    and m_0 underflows).  PROVED: Δ_k = log(a_k)/(m_k+1) =
    2^{−r_k}·log 2, a_k → ∞, Δ_k → 0, m_k → ∞.
  * `weil_nonneg_of_selected_windows` -- the reduction, honest to
    the existing extraction (RH/Elementwise.lean): the premise is
    plain-form nonnegativity of `fullRead` along the selected
    sequence (the type `WindowLocalPositive` already uses), plus
    per-element onset and mesh coverage, which the sequence
    supplies by cofinality.  Arch/pole stabilization is CONSUMED,
    not re-asserted.  L† / master positivity of the real windows
    is a STRICTLY STRONGER premise, connected by the named Prop
    `SelectedMasterImpliesPlainReads` (the existing
    `BorderedCompressionBridge` plus the real-window moment
    algebra, not formalized as a theorem in this round because L†
    is still typed on the rational `VonMangoldtWindow`).
  * THE r397 STRICT TAIL (kept as the stronger alternative):
    named Prop `selected_augDualResolvent_gt_half`
    (`∀ᶠ k, (R†(W^ℝ_k) − ½·1).PosDef`).  r430 degrades this to
    the stronger alt-form: the load-bearing mincut is
    `frequently_selected_augDualResolvent_ge_half` in
    RH/FrequentlySelected.lean (`∃ᶠ k, R† ⪰ ½I`).  The C1 holes
    `lstar_canonical` / `terminal_q_canonical` remain DEGRADED
    to conjectures / alternative route (kept, not deleted).

SORRY CENSUS OF THIS FILE: ZERO.  New openness is named Props only.
Since r638L the extraction theorem takes the unasserted
`ArchGaussMellinDigammaIdentity` contract explicitly; no arch
`sorry` is consumed.

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Canonical
import RH.DualResolvent
import RH.Elementwise
import RH.FaithfulFold
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace RH

open Filter Matrix
open scoped Topology

/-! ## Real canonical windows (the actual domain)

Docked to `PrimeWindow` (RH/Source.lean): same ℝ fields
(`nodes`, `combWeight`, `archWeight`, `u` = border, `B` = budget)
and the same wellformedness (`comb_nonneg`, `arch_nonneg`,
`window_rule`).  The extra field is budget positivity, the
transcribable r243 half already carried by `CanonicalCompletion`. -/

structure RealCanonicalWindow extends PrimeWindow where
  budget_pos : 0 < B

/-- a rational certificate window represents a real canonical
window at tolerance `δ` -- the r320 `RepresentsWindow`, retyped as
a CERTIFICATE over the real domain, not as a domain predicate. -/
def RepresentsRealCanonical (w : VonMangoldtWindow)
    (W : RealCanonicalWindow) (δ : ℝ) : Prop :=
  RepresentsWindow w W.toPrimeWindow δ

/-! ## The four Exact blocks and the total construction

r463 replaces the old raw-atom cosine quotient by the production
pipeline in `RH/FaithfulFold.lean`:

`prime powers -> tent lags -> cA+cP -> circulant density ->
 grid fold (L=2(m+1)-2) -> sign split`.

`ExactArch`/`ExactBorder`/`ExactBudget` now expose the typed
`ProductionCompletion` fields.  In particular no per-atom
`canonicalCompletion` value enters the selected real window.
The analytic values of the three external fields remain open, but
their production roles are explicit in the type and documentation. -/

/-- exact prime source at anchor `a`: the arithmetic layer of
`specFamily` (atoms, derived `log`/`Λ`).  Mesh-independent. -/
noncomputable def ExactPrimeSource (a : ℕ) (ha : IsPrimePow a) :
    PrimeWindowSpec :=
  specFamily a 0 ha

/-- Exact production archimedean lag vector
`arch_lags(m+1, log(a)/(m+1))`. -/
noncomputable def ExactArch (a m : ℕ) : ℕ → ℝ :=
  productionArchLag a m

/-- exact v958 border column at `(a, m)`. -/
noncomputable def ExactBorder (a m : ℕ) : ℕ → ℝ :=
  (productionCompletion a m).border

/-- exact r243 budget at `(a, m)`. -/
noncomputable def ExactBudget (a m : ℕ) : ℝ :=
  (productionCompletion a m).budget

theorem ExactBudget_pos (a m : ℕ) : 0 < ExactBudget a m :=
  (productionCompletion a m).budget_pos

/-- **ExactFold** is now the faithful production fold.  The primal
prime-power inventory is used inside `exactPrimeLag`; the final
support is the `m`-point spectral grid, and the positive/negative
parts are the two Hankel channels. -/
noncomputable def ExactFold (a m : ℕ) (ha : IsPrimePow a) :
    PrimeWindow :=
  productionFold a m

theorem ExactFold_B (a m : ℕ) (ha : IsPrimePow a) :
    (ExactFold a m ha).B = ExactBudget a m :=
  rfl

theorem ExactFold_u (a m : ℕ) (ha : IsPrimePow a) :
    (ExactFold a m ha).u = ExactBorder a m :=
  rfl

/-- **THE TOTAL REAL CANONICAL WINDOW** `W^ℝ(a,m)`.  Constructed,
not cut: every prime-power anchor and every mesh level yields a
window.  No emptiness question. -/
noncomputable def realCanonicalWindow (a m : ℕ) (ha : IsPrimePow a) :
    RealCanonicalWindow :=
  { ExactFold a m ha with
    budget_pos := by
      rw [ExactFold_B]
      exact ExactBudget_pos a m }

theorem realCanonicalWindow_B_pos (a m : ℕ) (ha : IsPrimePow a) :
    0 < (realCanonicalWindow a m ha).B :=
  (realCanonicalWindow a m ha).budget_pos

/-- the construction is total: every `(a,m)` produces a window
(the identity, recorded so the domain is visibly inhabited by
construction rather than by a representation witness). -/
theorem realCanonicalWindow_constructed (a m : ℕ) (ha : IsPrimePow a) :
    (realCanonicalWindow a m ha).toPrimeWindow = ExactFold a m ha :=
  rfl

/-- Named remaining identification (never asserted): after folding,
the Exact arch channel reproduces the tent-read `archRead` on
every grid element.  The functional `archRead` is the existing
opaque (r326); this is the window-object side of the same
classical TODO (`arch_A` / Titchmarsh Ch. X). -/
def ExactArchAgreesWithArchRead : Prop :=
  ∀ (a m : ℕ) (ha : IsPrimePow a) (f : GridElement),
    archRead a m f =
      ∑ i, (realCanonicalWindow a m ha).archWeight i *
        f.toFun ((realCanonicalWindow a m ha).nodes i)

/-- the production border passes through ExactFold definitionally.
The external value is the explicitly typed v958 field of
`ProductionCompletion`. -/
theorem ExactBorder_eq_window (a m : ℕ) (ha : IsPrimePow a) (k : ℕ) :
    (realCanonicalWindow a m ha).u k = ExactBorder a m k :=
  rfl

/-- the production budget passes through ExactFold definitionally.
The external value is the explicitly typed r243 field of
`ProductionCompletion`. -/
theorem ExactBudget_eq_window (a m : ℕ) (ha : IsPrimePow a) :
    (realCanonicalWindow a m ha).B = ExactBudget a m :=
  rfl

/-! ## Real-window moments (docked: the ℝ-form of the
`VonMangoldtWindow` derived objects, so R† can be stated on
`W^ℝ` without a parallel certificate domain) -/

namespace PrimeWindow

variable (w : PrimeWindow)

/-- half-filling cap `(S+1)/2`, same formula as the rational
certificate. -/
def cap : ℕ := (w.S + 1) / 2

def weight (j : Fin w.S) : ℝ := w.combWeight j - w.archWeight j

def mom (n : ℕ) : ℝ := ∑ j, w.weight j * w.nodes j ^ n

def combMom (n : ℕ) : ℝ := ∑ j, w.combWeight j * w.nodes j ^ n

def archMom (n : ℕ) : ℝ := ∑ j, w.archWeight j * w.nodes j ^ n

def hankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => w.mom ((i : ℕ) + (k : ℕ))

def combHankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => w.combMom ((i : ℕ) + (k : ℕ))

def archHankel (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  fun i k => w.archMom ((i : ℕ) + (k : ℕ))

def borderVec (n : ℕ) : Fin n → ℝ := fun i => w.u i

/-- augmented matrix `A_n = [[H_n, u_n], [u_nᵀ, B]]`. -/
def A (n : ℕ) : Matrix (Fin n ⊕ Unit) (Fin n ⊕ Unit) ℝ :=
  fromBlocks (w.hankel n)
    (fun i _ => w.u i) (fun _ k => w.u k) (fun _ _ => w.B)

/-- master positivity through the cap (the real-window L† /
master cone, typed on the constructed object). -/
def MasterPositive : Prop :=
  ∀ n ≤ w.cap, (w.A n).PosDef

end PrimeWindow

/-- μ-ONB Gram transcription of a REAL window (the r373
`RepresentsLEnsemble` equations, docked to `PrimeWindow`: no ℚ
casts). -/
def RepresentsLEnsembleReal (w : PrimeWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ) : Prop :=
  n = w.cap ∧
    0 < w.B ∧
    ∃ Q : Matrix (Fin n) (Fin n) ℝ, IsUnit Q.det ∧
      Qᵀ * w.combHankel n * Q = 1 ∧
      E = Qᵀ * w.archHankel n * Q ∧
      v = -((1 / Real.sqrt w.B) • (Qᵀ *ᵥ w.borderVec n)) ∧
      γ = 0

/-! ## The selected sequence

`a_k = 2^k`, `r_k = ⌊√k⌋`, `m_k = k·2^{r_k}−1`.  For `k ≥ 1`:
`a_k` is a prime power, `m_k + 1 = k·2^{r_k}`, and
`Δ_k = log(a_k)/(m_k+1) = 2^{−r_k}·log 2`. -/

def selectedAnchor (k : ℕ) : ℕ := 2 ^ k

noncomputable def selectedRoot (k : ℕ) : ℕ :=
  ⌊Real.sqrt (k : ℝ)⌋₊

noncomputable def selectedMesh (k : ℕ) : ℕ :=
  k * 2 ^ selectedRoot k - 1

noncomputable def selectedDelta (k : ℕ) : ℝ :=
  Real.log (selectedAnchor k) / (selectedMesh k + 1 : ℝ)

theorem selectedAnchor_isPrimePow {k : ℕ} (hk : 0 < k) :
    IsPrimePow (selectedAnchor k) :=
  ⟨2, k, Nat.prime_two.prime, hk, rfl⟩

theorem selectedMesh_add_one {k : ℕ} (hk : 0 < k) :
    selectedMesh k + 1 = k * 2 ^ selectedRoot k := by
  unfold selectedMesh
  have hle : 1 ≤ k * 2 ^ selectedRoot k :=
    Nat.one_le_iff_ne_zero.mpr
      (mul_ne_zero hk.ne' (pow_ne_zero _ (by decide : (2 : ℕ) ≠ 0)))
  exact Nat.sub_add_cancel hle

/-- **Δ_k = 2^{−r_k} · log 2** (r397; PROVED). -/
theorem selectedDelta_eq {k : ℕ} (hk : 0 < k) :
    selectedDelta k =
      (2 : ℝ) ^ (-(selectedRoot k : ℝ)) * Real.log 2 := by
  have hlog : Real.log (selectedAnchor k) = (k : ℝ) * Real.log 2 := by
    unfold selectedAnchor
    have hcast : ((2 ^ k : ℕ) : ℝ) = (2 : ℝ) ^ k := by norm_cast
    rw [hcast]
    exact Real.log_pow 2 k
  have hden : (selectedMesh k : ℝ) + 1 =
      (k : ℝ) * (2 : ℝ) ^ selectedRoot k := by
    rw [← Nat.cast_one, ← Nat.cast_add, selectedMesh_add_one hk]
    push_cast
    rfl
  unfold selectedDelta
  rw [hlog, hden]
  have hk0 : (k : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hk.ne'
  have hrpow : (2 : ℝ) ^ (-(selectedRoot k : ℝ)) =
      ((2 : ℝ) ^ selectedRoot k)⁻¹ := by
    rw [Real.rpow_neg two_pos.le, Real.rpow_natCast]
  rw [hrpow]
  have h2 : (2 : ℝ) ^ selectedRoot k ≠ 0 :=
    (pow_pos two_pos _).ne'
  field_simp [hk0, h2]

/-- **a_k → ∞** (r397; PROVED). -/
theorem selectedAnchor_tendsto :
    Tendsto selectedAnchor atTop atTop := by
  refine tendsto_atTop_atTop.2 fun n => ⟨n, fun k hk => ?_⟩
  have hlt : k < 2 ^ k := k.lt_two_pow_self
  exact le_trans hk (Nat.le_of_lt hlt)

/-- **r_k → ∞** (r397; PROVED). -/
theorem selectedRoot_tendsto :
    Tendsto selectedRoot atTop atTop := by
  refine tendsto_atTop_atTop.2 fun N => ⟨N ^ 2, fun k hk => ?_⟩
  unfold selectedRoot
  have hsqrt : (N : ℝ) ≤ Real.sqrt (k : ℝ) := by
    rw [Real.le_sqrt (Nat.cast_nonneg N) (Nat.cast_nonneg k)]
    have : ((N : ℝ) ^ 2) ≤ (k : ℝ) := by
      exact_mod_cast (show N ^ 2 ≤ k from hk)
    simpa [pow_two] using this
  exact (Nat.le_floor_iff (Real.sqrt_nonneg _)).2 hsqrt

/-- **m_k → ∞** (r397; PROVED -- mesh cofinality). -/
theorem selectedMesh_tendsto :
    Tendsto selectedMesh atTop atTop := by
  refine tendsto_atTop_atTop.2 fun N => ⟨N + 1, fun k hk => ?_⟩
  have hkpos : 0 < k := lt_of_lt_of_le (Nat.succ_pos N) hk
  have hadd := selectedMesh_add_one hkpos
  have hge : k ≤ selectedMesh k + 1 := by
    rw [hadd]
    exact Nat.le_mul_of_pos_right _ (pow_pos (by decide : (0 : ℕ) < 2) _)
  omega

/-- **Δ_k → 0** (r397; PROVED -- mesh cofinality in width). -/
theorem selectedDelta_tendsto_zero :
    Tendsto selectedDelta atTop (nhds 0) := by
  have hhalf : Tendsto (fun n : ℕ => ((1 : ℝ) / 2) ^ n) atTop (nhds 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by positivity) (by norm_num)
  have hcomp : Tendsto (fun k : ℕ => ((1 : ℝ) / 2) ^ selectedRoot k)
      atTop (nhds 0) :=
    hhalf.comp selectedRoot_tendsto
  have hmul : Tendsto
      (fun k : ℕ => ((1 : ℝ) / 2) ^ selectedRoot k * Real.log 2)
      atTop (nhds 0) := by
    simpa using hcomp.mul_const (Real.log 2)
  have heq : ∀ᶠ k in atTop,
      selectedDelta k =
        ((1 : ℝ) / 2) ^ selectedRoot k * Real.log 2 := by
    filter_upwards [eventually_gt_atTop 0] with k hk
    rw [selectedDelta_eq hk, Real.rpow_neg two_pos.le,
      Real.rpow_natCast, ← inv_pow, one_div]
  exact (tendsto_congr' heq).mpr hmul

/-- the selected real window `W^ℝ_k` (k ≥ 1). -/
noncomputable def selectedRealWindow (k : ℕ) (hk : 0 < k) :
    RealCanonicalWindow :=
  realCanonicalWindow (selectedAnchor k) (selectedMesh k)
    (selectedAnchor_isPrimePow hk)

theorem selectedRealWindow_constructed (k : ℕ) (hk : 0 < k) :
    (selectedRealWindow k hk).toPrimeWindow =
      ExactFold (selectedAnchor k) (selectedMesh k)
        (selectedAnchor_isPrimePow hk) :=
  rfl

/-- coverage: for any onset `a₀` and any native mesh exponent `M`,
eventually `a_k ≥ a₀`, `m_k ≥ M`, and `k ≥ 1` (so `a_k` is a
prime power).  This is the per-element onset + mesh coverage the
extraction needs, supplied by cofinality of ONE sequence. -/
theorem selected_covers (a₀ M : ℕ) :
    ∀ᶠ k in atTop,
      0 < k ∧ a₀ ≤ selectedAnchor k ∧ M ≤ selectedMesh k := by
  filter_upwards [eventually_gt_atTop 0,
    selectedAnchor_tendsto.eventually_ge_atTop a₀,
    selectedMesh_tendsto.eventually_ge_atTop M] with k hk hA hM
  exact ⟨hk, hA, hM⟩

/-! ## The reduction: selected-window positivity ⇒ Weil form

HYPOTHESES THE EXISTING EXTRACTION ACTUALLY NEEDS
(`weil_nonneg_of_windowlocal`, RH/Elementwise.lean):

  1. STABILIZATION (conditional, not asserted):
     `elementwise_finite_stabilization hArch f` -- comb PROVED,
     pole PROVED, arch supplied explicitly through the historical
     contract `ArchGaussMellinDigammaIdentity`.  Yields a finite onset
     `a₀(f)` past which `fullRead a m f = weilForm f` for every
     `m ≥ f.meshExp`.
  2. ONSET: one anchor `a ≥ a₀(f)` (the existing proof picks a
     prime via Euclid; here the selected sequence supplies it
     because `a_k → ∞`).
  3. MESH COVERAGE: `f.meshExp ≤ m` (the existing proof uses the
     element's own native mesh; here `m_k → ∞` covers every
     element).
  4. PLAIN-FORM POSITIVITY of `fullRead` at that `(a,m)`.  The
     existing `WindowLocalPositive` asks this for EVERY
     prime-power window.  The selected-sequence form asks it
     only eventually, along `W_k` -- enough, because each `f`
     needs only ONE pair `(a,m)`.

L† / master positivity of `W^ℝ_k` is NOT among these four.  It
implies (4) only through the named Prop
`SelectedMasterImpliesPlainReads` (bordered ⇒ plain, the existing
`BorderedCompressionBridge` class).  The theorem below is
therefore stated on (4), not on L†. -/

/-- selected-sequence window-local positivity (plain `fullRead`,
the type the extraction consumes). -/
def SelectedWindowLocalPositive : Prop :=
  ∀ᶠ k in atTop,
    ∀ f : GridElement, f.meshExp ≤ selectedMesh k →
      0 ≤ fullRead (selectedAnchor k) (selectedMesh k) f

/-- selected-sequence master positivity of the constructed real
windows. -/
def SelectedMasterPositive : Prop :=
  ∀ᶠ k in atTop,
    ∃ hk : 0 < k, (selectedRealWindow k hk).toPrimeWindow.MasterPositive

/-- Named (never asserted): master / L† positivity of `W^ℝ_k`
implies the plain-form `SelectedWindowLocalPositive`.  This is
the composition of the real-window master cone, the existing
named `BorderedCompressionBridge`, and grid-compatibility of
`m_k`.  Not a theorem in this round: L† is still typed on the
rational `VonMangoldtWindow`. -/
def SelectedMasterImpliesPlainReads : Prop :=
  SelectedMasterPositive → SelectedWindowLocalPositive

/-- **THE REDUCTION** (r397; PROVED as a finite instantiation per
element, no mesh-ladder transport).  Selected-sequence plain-form
positivity plus the existing elementwise stabilization imply
Weil-form nonnegativity on every grid element.

Honest hypotheses: `hArch` is the unasserted historical arch
exact-equality contract, `hpos` is (4) above; onset and mesh coverage
are proved (`selected_covers`).  NO RH
CLAIM. -/
theorem weil_nonneg_of_selected_windows
    (hArch : ArchGaussMellinDigammaIdentity)
    (hpos : SelectedWindowLocalPositive) :
    ∀ f : GridElement, 0 ≤ weilForm f := by
  intro f
  obtain ⟨a₀, hstab⟩ := elementwise_finite_stabilization hArch f
  have hcov := selected_covers a₀ f.meshExp
  have h : ∀ᶠ k in atTop,
      0 < k ∧ a₀ ≤ selectedAnchor k ∧ f.meshExp ≤ selectedMesh k ∧
        ∀ g : GridElement, g.meshExp ≤ selectedMesh k →
          0 ≤ fullRead (selectedAnchor k) (selectedMesh k) g := by
    filter_upwards [hcov, hpos] with k hcovk hposk
    exact ⟨hcovk.1, hcovk.2.1, hcovk.2.2, hposk⟩
  obtain ⟨k, hk⟩ := h.exists
  have hread := hk.2.2.2 f hk.2.2.1
  have heq := hstab (selectedAnchor k) hk.2.1 (selectedMesh k) hk.2.2.1
  rwa [heq] at hread

/-- the L† / master route, composed through the named bridge
(PROVED as a function of the named Prop, never asserting it). -/
theorem weil_nonneg_of_selected_master
    (hArch : ArchGaussMellinDigammaIdentity)
    (hbridge : SelectedMasterImpliesPlainReads)
    (hmaster : SelectedMasterPositive) :
    ∀ f : GridElement, 0 ≤ weilForm f :=
  weil_nonneg_of_selected_windows hArch (hbridge hmaster)

/-! ## The r397 strict tail (stronger alternative since r430)

Named Prop, never a `sorry`, never asserted.  The dual-resolvent
object is the r362/r373 `augDualResolvent` of a μ-ONB
transcription of `W^ℝ_k` (`RepresentsLEnsembleReal`).  The
finite-algebra identity `L† ⟺ R† ≻ ½I` remains
`augmentedSubordination_iff_dualResolvent` on the rational
certificate side.  r430: this is the stronger (`∀ᶠ`, `PosDef`)
alternative; the load-bearing mincut is
`frequently_selected_augDualResolvent_ge_half`. -/

/-- R† ≻ ½I for a μ-ONB transcription of one selected real
window. -/
def selectedWindowCone (k : ℕ) (hk : 0 < k) : Prop :=
  let W := (selectedRealWindow k hk).toPrimeWindow
  ∃ (E : Matrix (Fin W.cap) (Fin W.cap) ℝ) (v : Fin W.cap → ℝ) (γ : ℝ),
    RepresentsLEnsembleReal W W.cap E v γ ∧
    (dualZ E v γ).PosDef ∧
    (augDualResolvent E v γ
      - (1 / 2 : ℝ) •
        (1 : Matrix (Fin W.cap ⊕ Unit) (Fin W.cap ⊕ Unit) ℝ)).PosDef

/-- **STRONGER ALTERNATIVE** (r397; r430 degradation): eventually
the selected real windows satisfy `R†(W^ℝ_k) ≻ ½ I`.  Kept; not
the mincut.  The load-bearing open kernel is
`frequently_selected_augDualResolvent_ge_half`
(`RH/FrequentlySelected.lean`).  The C1 holes
`lstar_canonical` / `terminal_q_canonical` remain the
rational-certificate route.  NO RH CLAIM. -/
def selected_augDualResolvent_gt_half : Prop :=
  ∀ᶠ k in atTop, ∃ hk : 0 < k, selectedWindowCone k hk

end RH
