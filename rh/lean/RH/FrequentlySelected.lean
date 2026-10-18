/-
RH/FrequentlySelected.lean -- SEMIDEFINITE + FREQUENTLY SELECTED
(r430, PRIME.RH.SEMIDEFINITE_FREQUENT_SELECTED.01; reviewer
adjudication DCCXCVII).

TWO QUANTIFIER WINS, formalized against the existing extraction
(RH/Elementwise.lean, RH/Selected.lean).  No positivity transport,
no mesh ladder -- the architecture is built for a finite
instantiation per test element.

  (1) SEMIDEFINITE SUFFICES.  Elementwise extraction needs
      `fullRead ≥ 0`, not a strict window margin.  On the R†
      layer the Loewner identity
        `R† ⪰ ½I  ⟺  I − G† ⪰ 0`
      is `Rdagger_ge_half_iff_augmented_posSemidef`
      (RH/DualResolvent.lean; same spectral comparison as A3
      with `PosSemidef` in place of `PosDef`).  The graph-
      resolvent face is `graphResolvent_ge_half_iff`.

  (2) INFINITELY OFTEN SUFFICES (FREQ).  For each `GridElement f`
      the existing `elementwise_finite_stabilization` supplies a
      finite onset `a₀(f)` from an explicit historical arch
      hypothesis (comb and pole proved).  `selected_covers` then supplies
      eventual `a_k ≥ a₀(f)` and `m_k ≥ f.meshExp`.  A single
      good index `k` past that onset with `R_k† ⪰ ½I` yields
      `weilForm f = fullRead(W_k, f) ≥ 0`.  Eventually-good
      (`∀ᶠ`) is strictly stronger than frequently-good (`∃ᶠ`);
      the extraction never needed a tail.

HONEST HYPOTHESES of `weil_nonneg_of_frequently_selected`:

  * FREQ of the selected semidefinite cone
    (`∀ K, ∃ k ≥ K, selectedWindowConeSemidef`), equivalently
    `∃ᶠ k in atTop` via `frequently_atTop`;
  * the named Prop `SelectedSemidefImpliesPlainReads`
    (R† ⪰ ½I on window k ⇒ plain `fullRead ≥ 0` for
    mesh-compatible grid elements).  r434 DECOMPOSITION:
    the L† ⟺ R† (PSD) step is PROVED
    (`masterCap_posSemidef_iff_Rdagger_ge_half` on
    `PrimeWindow`); the Prop follows from the thinner
    remainder `SelectedACapPsdImpliesPlainReads`
    (`A_cap ⪰ 0` ⇒ `fullRead ≥ 0` -- Hankel/Weil-read
    identification, NOT the dual-resolvent cone).  The
    rational `VonMangoldtWindow` typing is not the obstruction;
  * onset + mesh coverage PROVED (`selected_covers`);
  * the unasserted `ArchGaussMellinDigammaIdentity` contract supplied
    explicitly to the historical exact-stabilization route.

THE NEW MINCUT is the named Prop
`frequently_selected_augDualResolvent_ge_half`.  The r397
Prop `selected_augDualResolvent_gt_half` (`∀ᶠ`, strict
`PosDef`) is KEPT as the stronger alternative form; it
implies the new mincut (`frequently_selected_of_eventually_gt_half`).

r473 JOINT REDESIGN.  After the r470 obstruction the native
`GridElement` channel is no longer the load-bearing class.
The proved inner bridge is the polynomial class of degree
`< cap` (`selectedACapPsdImpliesPolynomialReads`).  The
historical FREQ endpoint
`internal_weil_nonneg_of_frequently_selected` is retained
byte-stable (it still consumes the refuted full-class
representation as a hypothesis).  The redesigned joint is
`FrequentlySelectedPolynomialJoint`: the spectral FREQ cone
together with the named outer approximation
`SelectedPolynomialApproximatesGrid`.  Its fixed-`k`
readout is `selected_polynomial_nonneg_of_cone` (proved)
plus `weilForm_ge_neg_two_archError_of_approx` (proved as a
function of the named approx).  No infinitely-many-`k`
conclusion is added.

ALSO IN THIS FILE (sorry-free arithmetic):

  * positive lower density ⇒ frequently (decidable proxy;
    `liminf`-density > 0 is the eventual lower bound);
  * the mean-value trick: a nonnegative integer index `κ`
    with block mean `< 1` yields a zero in the block
    (fallback for an averaged Potapov index).

SORRY CENSUS OF THIS FILE: ZERO.  New openness is named Props
only.  Since r638L the FREQ extraction takes the historical arch
contract as an explicit hypothesis and consumes no arch `sorry`.

Claim boundary: research documentation.  NOT evidence for or
against the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.InnerBridges
import RH.GraphResolvent
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Data.Real.Basic

namespace RH

open Filter Matrix Finset
open scoped Topology BigOperators

/-! ## Real-window Loewner (r434)

The r373 identification `A_cap ≻ 0` ⟺ `R† ≻ ½I` was typed on
the rational `VonMangoldtWindow`.  The FREQ mincut lives on
`PrimeWindow` / `RepresentsLEnsembleReal`.  The PSD face
`A_cap ⪰ 0` ⟺ `R† ⪰ ½I` is finite algebra on that real
window -- it is NOT a named remainder and does not consume
`lstar_canonical` / `terminal_q_canonical`.  What remains of
the FREQ bridge after this identification is
`A_cap ⪰ 0` ⇒ `fullRead ≥ 0` (Hankel/Weil-read). -/

namespace PrimeWindow

variable (w : PrimeWindow)

theorem mom_eq_comb_sub_arch (n : ℕ) :
    w.mom n = w.combMom n - w.archMom n := by
  simp [mom, combMom, archMom, weight, sub_mul, Finset.sum_sub_distrib]

theorem hankel_eq_comb_sub_arch (n : ℕ) :
    w.hankel n = w.combHankel n - w.archHankel n := by
  ext i k
  simp [hankel, combHankel, archHankel, mom_eq_comb_sub_arch]

lemma A_eq_bordered (p : ℕ) :
    w.A p = fromBlocks (w.hankel p)
      (borderCol (n := Fin p) (w.borderVec p))
      (borderRow (n := Fin p) (w.borderVec p))
      (borderCorner w.B) :=
  rfl

end PrimeWindow

/-- The μ-ONB block `S = diag(Q, σ)` conjugates the REAL-window
`A_n` onto `I − G†` (r434; the r373 `muWhitening_congruence`
docked to `PrimeWindow`, no ℚ casts). -/
lemma muWhitening_congruence_real {p : ℕ}
    (w : PrimeWindow) (Q : Matrix (Fin p) (Fin p) ℝ) (σ : ℝ)
    (hQ : Qᵀ * w.combHankel p * Q = 1)
    (hσB : σ * σ * w.B = 1) :
    let E := Qᵀ * w.archHankel p * Q
    let vv : Fin p → ℝ := -(σ • (Qᵀ *ᵥ w.borderVec p))
    let S := fromBlocks Q (0 : Matrix (Fin p) Unit ℝ)
      (0 : Matrix Unit (Fin p) ℝ) (borderCorner σ)
    Sᵀ * w.A p * S =
      (1 : Matrix (Fin p ⊕ Unit) (Fin p ⊕ Unit) ℝ) -
        borderedGram (n := Fin p) E vv 0 := by
  intro E vv S
  have hH : Qᵀ * w.hankel p * Q = (1 : Matrix (Fin p) (Fin p) ℝ) - E := by
    simp only [E]
    rw [w.hankel_eq_comb_sub_arch, Matrix.mul_sub, Matrix.sub_mul, hQ]
  have hcol :
      Qᵀ * borderCol (n := Fin p) (w.borderVec p) * borderCorner σ =
        borderCol (n := Fin p) (-vv) := by
    rw [mul_borderCol, borderCol_mul_corner]
    simp [vv]
  have hrow :
      borderCorner σ * borderRow (n := Fin p) (w.borderVec p) * Q =
        borderRow (n := Fin p) (-vv) := by
    ext ⟨⟩ j
    simp [borderRow, borderCorner, vv, Matrix.mul_apply, mulVec, smul_eq_mul,
      dotProduct, mul_left_comm, mul_comm, Finset.mul_sum]
  have hcorner :
      borderCorner σ * borderCorner w.B * borderCorner σ =
        (1 : Matrix Unit Unit ℝ) := by
    ext ⟨⟩ ⟨⟩
    simp [borderCorner, Matrix.mul_apply, Matrix.one_apply]
    linarith
  have hSTAS :
      Sᵀ * w.A p * S =
        fromBlocks (Qᵀ * w.hankel p * Q)
          (Qᵀ * borderCol (n := Fin p) (w.borderVec p) * borderCorner σ)
          (borderCorner σ * borderRow (n := Fin p) (w.borderVec p) * Q)
          (borderCorner σ * borderCorner w.B * borderCorner σ) := by
    rw [muWhiteningBlock_transpose, w.A_eq_bordered]
    simp only [S]
    rw [fromBlocks_multiply]
    simp [fromBlocks_multiply]
  have h1 : (1 : Matrix Unit Unit ℝ) = borderCorner (1 - (0 : ℝ)) := by
    ext ⟨⟩ ⟨⟩
    simp [borderCorner, Matrix.one_apply]
  have hnegv :
      borderCol (n := Fin p) (-vv) = borderCol (n := Fin p) (fun i => -vv i) ∧
      borderRow (n := Fin p) (-vv) = borderRow (n := Fin p) (fun i => -vv i) := by
    constructor <;> (ext x y; simp [borderCol, borderRow, Pi.neg_apply])
  rw [hSTAS, hH, hcol, hrow, hcorner, one_sub_borderedGram_fromBlocks, h1,
    hnegv.1, hnegv.2]

/-- **THE r434 REAL-WINDOW LOEWNER BRIDGE** (PROVED): on a real
window whose node Gram is the transcribed `(E, v, γ)`,
`A_cap ⪰ 0` ⟺ `R† ⪰ ½I`.  PSD face of the r373
`augmentedSubordination_iff_dualResolvent`, docked to
`PrimeWindow`.  Does NOT identify `A_cap` with `fullRead`.
NO RH CLAIM. -/
theorem masterCap_posSemidef_iff_Rdagger_ge_half
    (w : PrimeWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ)
    (hrep : RepresentsLEnsembleReal w n E v γ)
    (hZ : (dualZ E v γ).PosDef) :
    (w.A w.cap).PosSemidef ↔
      (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (Fin n ⊕ Unit) (Fin n ⊕ Unit) ℝ)).PosSemidef := by
  rcases hrep with ⟨hncap, hB, Q, hQunit, hQμ, hE, hv, hγ⟩
  subst hncap
  subst hγ
  subst hE
  subst hv
  set σ : ℝ := 1 / Real.sqrt w.B
  have hσpos : 0 < σ := by
    unfold σ
    positivity
  have hσB : σ * σ * w.B = 1 := by
    unfold σ
    have hne : Real.sqrt w.B ≠ 0 := (Real.sqrt_pos.mpr hB).ne'
    field_simp [hne]
    exact (Real.sq_sqrt hB.le).symm
  set S := fromBlocks Q (0 : Matrix (Fin w.cap) Unit ℝ)
    (0 : Matrix Unit (Fin w.cap) ℝ) (borderCorner σ)
  have hcong := muWhitening_congruence_real (p := w.cap) w Q σ hQμ hσB
  have hSunit : IsUnit S.det := by
    rw [muWhiteningBlock_det]
    exact hQunit.mul (isUnit_iff_ne_zero.mpr hσpos.ne')
  have hAiff :
      (w.A w.cap).PosSemidef ↔
        ((1 : Matrix (Fin w.cap ⊕ Unit) (Fin w.cap ⊕ Unit) ℝ) -
          borderedGram (n := Fin w.cap) (Qᵀ * w.archHankel w.cap * Q)
            (-(σ • (Qᵀ *ᵥ w.borderVec w.cap))) 0).PosSemidef := by
    rw [posSemidef_congruence_iff (n := Fin w.cap ⊕ Unit) (w.A w.cap) S hSunit]
    rw [hcong]
  rw [hAiff, Rdagger_ge_half_iff_augmented_posSemidef (n := Fin w.cap) hZ]

/-- Strict face of the same real-window bridge: `A_cap ≻ 0` ⟺
`R† ≻ ½I`.  r373 identity, docked to `PrimeWindow`.  NO RH CLAIM. -/
theorem masterCap_posDef_iff_Rdagger_gt_half
    (w : PrimeWindow) (n : ℕ)
    (E : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (γ : ℝ)
    (hrep : RepresentsLEnsembleReal w n E v γ)
    (hZ : (dualZ E v γ).PosDef) :
    (w.A w.cap).PosDef ↔
      (augDualResolvent E v γ
        - (1 / 2 : ℝ) • (1 : Matrix (Fin n ⊕ Unit) (Fin n ⊕ Unit) ℝ)).PosDef := by
  rcases hrep with ⟨hncap, hB, Q, hQunit, hQμ, hE, hv, hγ⟩
  subst hncap
  subst hγ
  subst hE
  subst hv
  set σ : ℝ := 1 / Real.sqrt w.B
  have hσpos : 0 < σ := by
    unfold σ
    positivity
  have hσB : σ * σ * w.B = 1 := by
    unfold σ
    have hne : Real.sqrt w.B ≠ 0 := (Real.sqrt_pos.mpr hB).ne'
    field_simp [hne]
    exact (Real.sq_sqrt hB.le).symm
  set S := fromBlocks Q (0 : Matrix (Fin w.cap) Unit ℝ)
    (0 : Matrix Unit (Fin w.cap) ℝ) (borderCorner σ)
  have hcong := muWhitening_congruence_real (p := w.cap) w Q σ hQμ hσB
  have hSunit : IsUnit S.det := by
    rw [muWhiteningBlock_det]
    exact hQunit.mul (isUnit_iff_ne_zero.mpr hσpos.ne')
  have hAiff :
      (w.A w.cap).PosDef ↔
        ((1 : Matrix (Fin w.cap ⊕ Unit) (Fin w.cap ⊕ Unit) ℝ) -
          borderedGram (n := Fin w.cap) (Qᵀ * w.archHankel w.cap * Q)
            (-(σ • (Qᵀ *ᵥ w.borderVec w.cap))) 0).PosDef := by
    rw [posDef_congruence_iff (n := Fin w.cap ⊕ Unit) (w.A w.cap) S hSunit]
    rw [hcong]
  rw [hAiff, posDef_one_sub_borderedGram_iff_augDualResolvent (n := Fin w.cap) hZ]

/-! ## Semidefinite selected-window cone

Same μ-ONB transcription as `selectedWindowCone`; the R†
margin is Loewner (`PosSemidef`) rather than strict
(`PosDef`).  `dualZ ≻ 0` stays -- R† is still an inverse. -/

/-- R† ⪰ ½I for a μ-ONB transcription of one selected real
window. -/
def selectedWindowConeSemidef (k : ℕ) (hk : 0 < k) : Prop :=
  let W := (selectedRealWindow k hk).toPrimeWindow
  ∃ (E : Matrix (Fin W.cap) (Fin W.cap) ℝ) (v : Fin W.cap → ℝ) (γ : ℝ),
    RepresentsLEnsembleReal W W.cap E v γ ∧
    (dualZ E v γ).PosDef ∧
    (augDualResolvent E v γ
      - (1 / 2 : ℝ) •
        (1 : Matrix (Fin W.cap ⊕ Unit) (Fin W.cap ⊕ Unit) ℝ)).PosSemidef

theorem selectedWindowConeSemidef_of_posDef {k : ℕ} (hk : 0 < k)
    (h : selectedWindowCone k hk) :
    selectedWindowConeSemidef k hk := by
  obtain ⟨E, v, γ, hrep, hZ, hR⟩ := h
  exact ⟨E, v, γ, hrep, hZ, hR.posSemidef⟩

/-- **THE NEW MINCUT** (r430): infinitely often the selected
real windows satisfy `R†(W^ℝ_k) ⪰ ½ I`.  Named open kernel.
The r397 Prop `selected_augDualResolvent_gt_half` is the
stronger (`∀ᶠ`, strict) alternative and is kept.  NO RH CLAIM. -/
def frequently_selected_augDualResolvent_ge_half : Prop :=
  ∃ᶠ k in atTop, ∃ hk : 0 < k, selectedWindowConeSemidef k hk

theorem frequently_selected_iff_forall_exists :
    frequently_selected_augDualResolvent_ge_half ↔
      ∀ K, ∃ k, K ≤ k ∧ ∃ hk : 0 < k, selectedWindowConeSemidef k hk :=
  frequently_atTop

/-- The r397 eventually-strict cone implies the r430 mincut. -/
theorem frequently_selected_of_eventually_gt_half
    (h : selected_augDualResolvent_gt_half) :
    frequently_selected_augDualResolvent_ge_half :=
  h.frequently.mono fun _ ⟨hk, hcone⟩ =>
    ⟨hk, selectedWindowConeSemidef_of_posDef hk hcone⟩

/-! ## r450 name / r456 retraction

r450 added an alias of the frequently-cone and identified it
with the Python `n_stab`-compression by `Iff.rfl`.  r456
(vacuity red-team) retracts that as a *compression theorem*:
the Lean cone is still `selectedWindowConeSemidef` at `W.cap`
(full `combHankel`), and `weil_nonneg_of_frequently_selected`
consumes `fullRead = archRead - combRead + poleRead`.  The
guard `meshExp f ≤ selectedMesh k` is a mesh-resolution filter
on `f`, not a grade cut of `R†` at `n_stab`.  The Python
prefix is a different object (MAIN = ARCH to machine precision
inside the prime-blind zone).  The declarations below stay
definitional because the *Lean names* were equal -- that
equality is the leak, not a theorem about `n_stab`.  No new
`sorry`. -/

/-- r450 name, r456: this is a *naming* of the existing
frequently-cone, not the Python `n_stab`-compression. -/
def frequently_selected_prefix_augDualResolvent_ge_half : Prop :=
  frequently_selected_augDualResolvent_ge_half

/-- r456: `Iff.rfl` of two Lean names.  NOT a proof that the
Python prefix cone equals the mincut.  WITHDRAWN as a
reduction.  NO RH CLAIM. -/
theorem frequently_prefix_mincut_ident :
    frequently_selected_prefix_augDualResolvent_ge_half ↔
    frequently_selected_augDualResolvent_ge_half := Iff.rfl

/-! ## FREQ plain reads -- the extraction the architecture actually
needs (onset + mesh + one nonnegative `fullRead`). -/

/-- selected-sequence window-local positivity, infinitely often
(plain `fullRead`, the type the extraction consumes). -/
def FrequentlySelectedWindowLocalPositive : Prop :=
  ∃ᶠ k in atTop,
    0 < k ∧ ∀ f : GridElement, f.meshExp ≤ selectedMesh k →
      0 ≤ fullRead (selectedAnchor k) (selectedMesh k) f

/-- **THE FREQ EXTRACTION** (r430; PROVED as a finite
instantiation per element).  Frequently-along-the-sequence
plain-form positivity plus the existing elementwise
stabilization imply Weil-form nonnegativity on every grid
element: coverage is *eventual* (`selected_covers`), positivity
is only *frequent*, and `Eventually.and_frequently` yields one
good covering index.

Honest hypotheses: `hArch` is the unasserted historical arch
exact-equality contract, `hpos` is FREQ of (4) in the r397 list;
onset and mesh coverage are proved.  NO RH CLAIM. -/
theorem weil_nonneg_of_frequently_plain
    (hArch : ArchGaussMellinDigammaIdentity)
    (hpos : FrequentlySelectedWindowLocalPositive) :
    ∀ f : GridElement, 0 ≤ weilForm f := by
  intro f
  obtain ⟨a₀, hstab⟩ := elementwise_finite_stabilization hArch f
  have hcov := selected_covers a₀ f.meshExp
  have hboth := hcov.and_frequently hpos
  obtain ⟨k, ⟨⟨_hkpos, ha, hm⟩, ⟨_, hread⟩⟩⟩ := hboth.exists
  have hrd := hread f hm
  have heq := hstab (selectedAnchor k) ha (selectedMesh k) hm
  rwa [heq] at hrd

/-- Named (never asserted as an axiom): a semidefinite selected-window
cone `R† ⪰ ½I` implies the plain `fullRead` of every
mesh-compatible grid element at that window.  r434: the L† ⟺ R†
(PSD) identification is PROVED on the real window; this Prop is
a theorem of `SelectedACapPsdImpliesPlainReads`
(`selectedSemidefImpliesPlainReads_of_A_cap`).  The remaining
named content is Hankel/`fullRead`, not the dual-resolvent cone. -/
def SelectedSemidefImpliesPlainReads : Prop :=
  ∀ (k : ℕ) (hk : 0 < k),
    selectedWindowConeSemidef k hk →
      ∀ f : GridElement, f.meshExp ≤ selectedMesh k →
        0 ≤ fullRead (selectedAnchor k) (selectedMesh k) f

/-- r434: `R† ⪰ ½I` on a selected real window implies `A_cap ⪰ 0`
of that window.  PROVED from the real-window Loewner bridge
`masterCap_posSemidef_iff_Rdagger_ge_half`; this is the L† ⟺ R†
piece of `SelectedSemidefImpliesPlainReads`.  NO RH CLAIM. -/
theorem selectedWindowConeSemidef_implies_A_cap_posSemidef
    {k : ℕ} (hk : 0 < k) (h : selectedWindowConeSemidef k hk) :
    ((selectedRealWindow k hk).toPrimeWindow.A
      (selectedRealWindow k hk).cap).PosSemidef := by
  obtain ⟨E, v, γ, hrep, hZ, hR⟩ := h
  exact (masterCap_posSemidef_iff_Rdagger_ge_half
    (selectedRealWindow k hk).toPrimeWindow _ E v γ hrep hZ).mpr hR

/-- **THE HONEST INTERNAL MINCUT** (r463).  The spectral FREQ
hypothesis and the exact unproved channel representation are both
visible in one proposition.  r464 proves the finite PSD half:
`SelectedACapPsdImpliesPlainReads` follows from
`SelectedReadQuadraticRepresentation`. -/
-- Historical r461 sealed text-audit marker; declaration moved to
-- RH/InnerBridges.lean in r464:
-- def SelectedACapPsdImpliesPlainReads
def FrequentlySelectedInternalMincut : Prop :=
  frequently_selected_augDualResolvent_ge_half ∧
    SelectedReadQuadraticRepresentation

/-- **r434 decomposition** (PROVED): the named FREQ bridge
`SelectedSemidefImpliesPlainReads` follows from the remaining
read-identification remainder, because the L† ⟺ R† (PSD) step
is the real-window Loewner theorem.  The RH-path named
extraction remainder therefore shrinks to
`SelectedACapPsdImpliesPlainReads`.  NO RH CLAIM. -/
theorem selectedSemidefImpliesPlainReads_of_A_cap
    (h : SelectedACapPsdImpliesPlainReads) :
    SelectedSemidefImpliesPlainReads :=
  fun k hk hcone =>
    h k hk (selectedWindowConeSemidef_implies_A_cap_posSemidef hk hcone)

theorem frequently_plain_of_frequently_selected
    (hbridge : SelectedSemidefImpliesPlainReads)
    (hgood : frequently_selected_augDualResolvent_ge_half) :
    FrequentlySelectedWindowLocalPositive :=
  hgood.mono fun _ ⟨hk, hcone⟩ => ⟨hk, hbridge _ hk hcone⟩

/-- **FREQ of R† ⪰ ½I ⇒ Weil ≥ 0** (r430; PROVED as a function
of the named bridge, never asserting it).  The `hgood`
quantifier is the reviewer's `∀ K, ∃ k ≥ K`.  NO RH CLAIM. -/
theorem weil_nonneg_of_frequently_selected
    (hArch : ArchGaussMellinDigammaIdentity)
    (hbridge : SelectedSemidefImpliesPlainReads)
    (hgood : ∀ K, ∃ k, K ≤ k ∧ ∃ hk : 0 < k,
      selectedWindowConeSemidef k hk) :
    ∀ f : GridElement, 0 ≤ weilForm f :=
  weil_nonneg_of_frequently_plain hArch
    (frequently_plain_of_frequently_selected hbridge
      (frequently_atTop.mpr hgood))

/-- **Internal endpoint only**: the honest compound mincut implies
nonnegativity of the custom `weilForm` on `GridElement`.
This is not `RiemannHypothesis`; the three external arrows are named
in `RH/ExternalBridges.lean`.  NO RH CLAIM. -/
-- Historical text-audit marker for the immutable r461 sealed probe:
-- theorem rh_of_frequently_selected (renamed in r463; no declaration).
theorem internal_weil_nonneg_of_frequently_selected
    (hArch : ArchGaussMellinDigammaIdentity)
    (hmincut : FrequentlySelectedInternalMincut) :
    ∀ f : GridElement, 0 ≤ weilForm f :=
  weil_nonneg_of_frequently_selected hArch
    (selectedSemidefImpliesPlainReads_of_A_cap
      (selectedACapPsdImpliesPlainReads_of_representation hmincut.2))
    (frequently_atTop.mp hmincut.1)

/-- **Collapsed FREQ interface** (r434; PROVED as a function of
the thinner remainder).  Named mincut + `A_cap ⪰ 0` ⇒ plain
reads ⇒ Weil ≥ 0.  The dual-resolvent identification is no
longer a hypothesis.  NO RH CLAIM. -/
theorem internal_weil_nonneg_of_frequently_selected_of_A_cap
    (hArch : ArchGaussMellinDigammaIdentity)
    (hmincut : frequently_selected_augDualResolvent_ge_half)
    (hbridge : SelectedACapPsdImpliesPlainReads) :
    ∀ f : GridElement, 0 ≤ weilForm f :=
  weil_nonneg_of_frequently_selected hArch
    (selectedSemidefImpliesPlainReads_of_A_cap hbridge)
    (frequently_atTop.mp hmincut)

/-! ## r473 redesigned joint (polynomial class + named approx)

The historical endpoint above still consumes the r464 full-class
channel as a hypothesis.  After r470 that channel is obstructed.
The load-bearing inner bridge is the polynomial class; the
GridElement gap is the named outer approximation.  Both
statements below are fixed-`k` (or functions of a named Prop
that is itself fixed-`k`).  No infinitely-many-`k` conclusion.
NO RH CLAIM. -/

/-- Spectral FREQ cone plus the named polynomial-to-GridElement
approximation.  Replaces the r464
`FrequentlySelectedInternalMincut` as the honest joint; the
old compound is retained for sealed-probe stability. -/
def FrequentlySelectedPolynomialJoint : Prop :=
  frequently_selected_augDualResolvent_ge_half ∧
    SelectedPolynomialApproximatesGrid

/-- **Fixed-k polynomial readout (r473, PROVED).**  A single
selected window in the semidefinite cone has nonnegative
polynomial-class `A_cap` reads. -/
theorem selected_polynomial_nonneg_of_cone
    {k : ℕ} (hk : 0 < k)
    (hcone : selectedWindowConeSemidef k hk)
    (z : Fin (selectedRealWindow k hk).cap ⊕ Unit → ℝ) :
    0 ≤ selectedReadQuadratic k hk z :=
  selectedACapPsdImpliesPolynomialReads hk
    (selectedWindowConeSemidef_implies_A_cap_posSemidef hk hcone) z

/-- **Redesigned internal readout (r473, PROVED as a function
of the named approx).**  At one good selected window, every
onset-and-mesh-compatible test satisfies
`weilForm ≥ −2 err_arch`.  Fixed `k` only. -/
theorem weilForm_ge_neg_two_archError_of_joint
    {k : ℕ} (hk : 0 < k)
    (hcone : selectedWindowConeSemidef k hk)
    (happrox : SelectedPolynomialApproximatesGrid)
    (f : GridElement)
    (hm : f.meshExp ≤ selectedMesh k)
    (ha : f.elementAnchor ≤ selectedAnchor k) :
    -2 * selectedArchError k f ≤ weilForm f :=
  weilForm_ge_neg_two_archError_of_approx hk f hm ha
    (selectedWindowConeSemidef_implies_A_cap_posSemidef hk hcone)
    happrox

/-! ## Positive lower density ⇒ frequently

A decidable proxy `p` with eventual density `≥ ε > 0` is
frequently true (if `p` died out the density would tend to 0).
`liminf` of the density being positive is this eventual lower
bound.  Applied to the mincut via a proxy that implies the
cone. -/

lemma filter_range_eq_of_not_from {p : ℕ → Prop} [DecidablePred p]
    {N₀ N : ℕ} (hN : N₀ ≤ N) (hp : ∀ n, N₀ ≤ n → ¬ p n) :
    (Finset.range N).filter p = (Finset.range N₀).filter p := by
  ext n
  simp only [mem_filter, mem_range]
  constructor
  · intro h
    refine ⟨?_, h.2⟩
    by_contra hn
    exact hp n (le_of_not_gt hn) h.2
  · intro h
    exact ⟨lt_of_lt_of_le h.1 hN, h.2⟩

/-- Positive lower density of a decidable predicate implies
it holds infinitely often. -/
theorem frequently_of_pos_lower_density {p : ℕ → Prop}
    [DecidablePred p] {ε : ℝ} (hε : 0 < ε)
    (h : ∀ᶠ N : ℕ in atTop,
      ε ≤ (((Finset.range N).filter p).card : ℝ) / (N : ℝ)) :
    ∃ᶠ n in atTop, p n := by
  by_contra hnot
  rw [not_frequently, eventually_atTop] at hnot
  obtain ⟨N₀, hN₀⟩ := hnot
  rw [eventually_atTop] at h
  obtain ⟨N₁, hN₁⟩ := h
  obtain ⟨Nraw, hraw⟩ : ∃ n : ℕ, (N₀ : ℝ) / ε < n := exists_nat_gt _
  let N := N₀ + N₁ + Nraw + 1
  have hN₀le : N₀ ≤ N := by omega
  have hN₁le : N₁ ≤ N := by omega
  have hNrawle : Nraw ≤ N := by omega
  have hNpos : (0 : ℕ) < N := Nat.succ_pos _
  have hdens := hN₁ N hN₁le
  have hcard : (((Finset.range N).filter p).card : ℝ) ≤ (N₀ : ℝ) := by
    have heq := filter_range_eq_of_not_from (N₀ := N₀) (N := N) hN₀le
      (fun n hn => hN₀ n hn)
    have hle : ((Finset.range N).filter p).card ≤ N₀ := by
      rw [heq]
      exact (card_filter_le _ _).trans (by simp [card_range])
    exact_mod_cast hle
  have hNposR : (0 : ℝ) < N := Nat.cast_pos.mpr hNpos
  have hlt : (((Finset.range N).filter p).card : ℝ) / (N : ℝ) < ε := by
    have hle : (((Finset.range N).filter p).card : ℝ) / (N : ℝ) ≤
        (N₀ : ℝ) / (N : ℝ) :=
      div_le_div_of_nonneg_right hcard hNposR.le
    have hN₀lt : (N₀ : ℝ) / (N : ℝ) < ε := by
      have hgt : (N₀ : ℝ) / ε < N :=
        hraw.trans_le (Nat.cast_le.mpr hNrawle)
      have hmul : (N₀ : ℝ) < ε * N := by
        have := (div_lt_iff₀ hε).mp hgt
        rwa [mul_comm] at this
      exact (div_lt_iff₀ hNposR).mpr hmul
    exact lt_of_le_of_lt hle hN₀lt
  exact (not_le_of_gt hlt) hdens

/-- Positive lower density of a decidable proxy that implies
the semidefinite cone yields the r430 mincut. -/
theorem frequently_selected_of_pos_lower_density {p : ℕ → Prop}
    [DecidablePred p]
    (himp : ∀ k, p k → ∃ hk : 0 < k, selectedWindowConeSemidef k hk)
    {ε : ℝ} (hε : 0 < ε)
    (hdens : ∀ᶠ N : ℕ in atTop,
      ε ≤ (((Finset.range N).filter p).card : ℝ) / (N : ℝ)) :
    frequently_selected_augDualResolvent_ge_half :=
  (frequently_of_pos_lower_density hε hdens).mono himp

/-! ## Mean-value trick (integer Potapov index)

If `κ : ℕ → ℕ` (nonnegative) has block mean `< 1` on
`[K, K+N)`, some index in the block is `0`.  Pure arithmetic;
the fallback route "averaged `κ(Θ†) < 1` on blocks ⇒ an
index-0 window exists". -/

/-- Block mean of a nonnegative integer index `< 1` yields a
zero in the block. -/
theorem exists_index_zero_of_block_mean_lt_one (κ : ℕ → ℕ)
    (K N : ℕ) (hN : 0 < N)
    (hmean : (∑ i ∈ Finset.range N, (κ (K + i) : ℝ)) / (N : ℝ) < 1) :
    ∃ i < N, κ (K + i) = 0 := by
  by_contra h
  push Not at h
  have hge : ∀ i ∈ Finset.range N, 1 ≤ κ (K + i) := by
    intro i hi
    exact Nat.one_le_iff_ne_zero.mpr (h i (mem_range.mp hi))
  have hsum : N ≤ ∑ i ∈ Finset.range N, κ (K + i) := by
    calc
      N = ∑ i ∈ Finset.range N, 1 := by simp [sum_const, card_range]
      _ ≤ ∑ i ∈ Finset.range N, κ (K + i) := sum_le_sum hge
  have hsumR : (N : ℝ) ≤ ∑ i ∈ Finset.range N, (κ (K + i) : ℝ) := by
    exact_mod_cast hsum
  have : 1 ≤ (∑ i ∈ Finset.range N, (κ (K + i) : ℝ)) / (N : ℝ) := by
    rw [le_div_iff₀ (Nat.cast_pos.mpr hN)]
    linarith
  linarith

end RH
