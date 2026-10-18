/-
RH/Canonical.lean -- THE CANONICAL FINAL DOMAIN (block C1, the reviewer
final-domain contract: "reduce the Lean graph to the two true
mathematical gaps").

WHY THIS FILE EXISTS.  Until C1 the two true arithmetic holes of the
library were conditioned on the deliberately `opaque` predicate
`MainWindow : VonMangoldtWindow → Prop` (r273): honest, but the
quantifier domain of the open statements was an unknowable marker, and
the only connection to the actual construction was the opacity bridge
(`mainWindow_iff_builtFromPrimeSource`, RH/Source.lean -- itself a
documented sorry) guarded by the free opaque `SourceExact`.  The C1
reviewer contract: put the open theorems DIRECTLY on the canonical
prime-window construction, so that the final theorem consumes neither
a free `SourceExact` hypothesis nor the opaque `MainWindow` bridge --
the actual arithmetic construction becomes the quantifier domain.

THE DESIGN (the r326 opacity convention, extended once more).  The
canonical family `specFamily a m ha` (RH/Source.lean, r310) carries
the full ARITHMETIC layer provably: atoms = ALL prime powers
`n ≤ a²` (`predefined_family`), nodes = `Real.log`, comb = `Λ` -- but
its arch/border/budget fields are zero/floor PLACEHOLDERS, because the
exact archimedean Weil kernel (`arch_A`, GL-48 tent integrals, v563),
the v958 border column and the full r243 budget identity are the named
classical transcription TODO (r320 finding: no honest finite clause
can bind those channels before their transcriptions exist).  Stating
the open holes over the placeholder family would be a SEMANTIC
CATASTROPHE: with `archWeight = 0` the subordination `∫p²dν < ∫p²dμ`
is trivially provable and the actual open problem would silently
vanish -- exactly the R319 seam-shift disease.  The honest repair is
the same move r326 made for the kernel READS (`archRead`/`poleRead`):
the genuine completion data enters as ONE named OPAQUE constant,
`canonicalCompletion : ℕ → CanonicalCompletion` -- "the exact
arch/border/budget data of the canonical window at anchor `a`".  Its
elimination = the same classical transcription TODO as always; until
then every statement consuming it is honestly typed, never provable,
and the intended semantics is documented at the constant.  (Relation
to `SourceExactOfFamilyCompletion`, RH/Elementwise.lean: that named
Prop (r376; formerly a `sorry`) ASSERTS a completion exists; this
constant NAMES the intended one, so the final statements can
quantify over the completed construction without an existential
import.)

THE FINAL DOMAIN.  `canonicalSpec a m ha` = the family spec with the
named completion filled in; `canonicalWindow a m ha` = its built real
window; and

  `CanonicalWindow w := ∃ a m ha,
      RepresentsWindow w (canonicalWindow a m ha) (canonicalSpec a m ha).mesh`

-- a rational certificate window is CANONICAL iff it mesh-represents
(r320 predicate: node/comb/arch within mesh, u/B EXACT, separation
discipline) the genuinely completed canonical construction at some
anchor.  Compare `MainWindow` (fully opaque) and the r320 bridge RHS
(`∃ s, SourceExact s ∧ RepresentsWindow ...` -- existentially FREE
spec bound only by an opaque guard): here the spec is the CONSTRUCTION
itself and only the three kernel-channel VALUES stay opaque.  The
U1-U3 adversaries are blocked structurally: budget = the named
positive completion budget (U1), separation discipline unchanged (U2),
border = the named completion column, not a free field (U3).

THE TWO C1 HOLES, canonical form (the C1 retype -- the r305/r320
statements are RETYPED onto this domain, not duplicated; the old
`MainWindow`-conditioned forms are REMOVED from RH/Window.lean and
RH/Closure.lean in the same change).  r397 DEGRADES both to the
alternative (rational-certificate) route: they stay as typed
`sorry`s so the finite-algebra corollaries still typecheck, but
they are NOT the mincut (domain may be empty; mesh-tolerance is
uncoupled from the L* margin).  The load-bearing open kernel is
`frequently_selected_augDualResolvent_ge_half` in
RH/FrequentlySelected.lean (r430); `selected_augDualResolvent_gt_half`
is the stronger alternative.
  * `lstar_canonical`     -- lemma L* on canonical windows (base/wall),
  * `terminal_q_canonical` -- the terminal cross-ratio `q < 1` on
    canonical windows (border/fiber).  NOTE the sharpening: the budget
    half `0 < B` of the old `terminal_positive_main` is now PROVED
    (`canonical_budget_pos` -- B-fidelity + the completion's
    `budget_pos`), so the sorry carries ONLY the genuinely open
    inequality; `terminal_canonical : TerminalPositive w` is a proved
    corollary of the two.
Everything downstream (master theorem, both former edges, free-window
positivity, L†) is PROVED from these two statements by the existing
finite algebra -- see the corollary section.  The pair-coordinate
duplicate `pair_margin_main` is RETIRED as a hole (C1 goal 2): the
r263 dictionary `Z² = m·q_N` is typed as the ONE named lemma
`pair_terminal_dictionary`, and the pair closure `pair_closes_main`
is now a PROVED corollary of `terminal_q_canonical` through it; the
margin LAW itself is demoted to the named Prop
`PairBound.PairMarginLaw` (no truth commitment -- honest: the fixed
pair form is measured to MISS on kz39/kz15 by 0.002/0.06 dec, so
asserting it as a hole overclaimed; the certificate route stays proved
as `PairBound.pair_closes_of_marginLaw`).

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Source
import RH.Closure
import RH.Augmented
import RH.PairBound
import RH.Elementwise

namespace RH

/-! ## The named completion data (opaque -- the classical import) -/

/-- the completion data of one canonical window: the not-yet-transcribed
kernel channels as explicit fields with their transcribable sign
constraints.  INTENDED CONTENT (per atom index of the anchor's atom
set): `arch` = the exact archimedean Weil-kernel masses (`arch_A`,
GL-48 tent integrals, v563), `border` = the v958 border column of this
atom set, `budget` = the full r243 scalar `B = S_{N-2} + 5/7` (whose
positivity IS transcribable and is carried as a field). -/
structure CanonicalCompletion where
  /-- archimedean/smooth weights per atom index (`nu` side). -/
  arch : ℕ → ℝ
  arch_nonneg : ∀ j, 0 ≤ arch j
  /-- the border column (v958). -/
  border : ℕ → ℝ
  /-- the budget scalar (r243 form). -/
  budget : ℝ
  budget_pos : 0 < budget

instance : Inhabited CanonicalCompletion :=
  ⟨⟨fun _ => 0, fun _ => le_rfl, fun _ => 0, 1, one_pos⟩⟩

/-- **THE NAMED COMPLETION** (C1; the r326 opacity convention extended
from the kernel reads to the window-level completion data): the genuine
arch/border/budget data of the canonical window at anchor `a`.  OPAQUE:
the exact kernel transcriptions are the named classical TODO
(RH/Source.lean header; `arch_A`/v958/r243) -- nothing about the VALUES
is provable inside the library, which is precisely the honest state;
the SIGNS (`arch_nonneg`, `budget_pos`) are carried by the type.
Eliminating this constant = writing the transcriptions = the same TODO
that eliminates `SourceExact` and the opaque reads of
RH/Elementwise.lean. -/
opaque canonicalCompletion : ℕ → CanonicalCompletion

/-! ## The completed canonical spec and window -/

/-- **the canonical spec** at anchor `a`, mesh level `m`: the
predefined family spec (arithmetic layer: all prime powers `≤ a²`,
sorted; nodes/comb DERIVED as `log`/`Λ`) with the named completion
filled into the three free channels.  This is the spec the final
statements quantify over -- no free field remains. -/
noncomputable def canonicalSpec (a m : ℕ) (ha : IsPrimePow a) :
    PrimeWindowSpec :=
  { specFamily a m ha with
    archWeight := fun j => (canonicalCompletion a).arch (j : ℕ)
    arch_nonneg := fun j => (canonicalCompletion a).arch_nonneg (j : ℕ)
    border := (canonicalCompletion a).border
    budget := (canonicalCompletion a).budget
    budget_pos := (canonicalCompletion a).budget_pos }

/-- **the canonical real window** at anchor `a`, mesh level `m` -- the
built window of the completed spec. -/
noncomputable def canonicalWindow (a m : ℕ) (ha : IsPrimePow a) :
    PrimeWindow :=
  buildPrimeWindow (canonicalSpec a m ha)

/-- the canonical spec shares the full arithmetic layer with the
predefined family (atoms, anchor, mesh level are bitwise the family
data -- only the three completion channels differ).  `rfl` by
construction. -/
theorem canonicalSpec_arith (a m : ℕ) (ha : IsPrimePow a) :
    (canonicalSpec a m ha).S = (specFamily a m ha).S ∧
    (∀ j, (canonicalSpec a m ha).primePowers j
      = (specFamily a m ha).primePowers j) ∧
    (canonicalSpec a m ha).anchor = a ∧
    (canonicalSpec a m ha).meshLevel = m :=
  ⟨rfl, fun _ => rfl, rfl, rfl⟩

/-- the canonical window's node and comb channels ARE the family's
(`log p^k` / `Λ(p^k)` -- the completion touches neither).  `rfl`. -/
theorem canonicalWindow_nodes (a m : ℕ) (ha : IsPrimePow a) :
    (canonicalWindow a m ha).nodes
      = (buildPrimeWindow (specFamily a m ha)).nodes := rfl

theorem canonicalWindow_combWeight (a m : ℕ) (ha : IsPrimePow a) :
    (canonicalWindow a m ha).combWeight
      = (buildPrimeWindow (specFamily a m ha)).combWeight := rfl

/-- the canonical spec is source-exact in the transcribable sense
(r326 `SourceExactSpec`): node/comb derivation, ATOM-SET COMPLETENESS
(`predefined_family`), budget positivity -- all PROVED, no opaque
guard consumed. -/
theorem sourceExact_canonicalSpec (a m : ℕ) (ha : IsPrimePow a) :
    SourceExactSpec (canonicalSpec a m ha) :=
  ⟨fun _ => rfl, fun _ => rfl, predefined_family a m ha,
    (canonicalCompletion a).budget_pos⟩

/-- canonical windows are explicitly-main (r310 sense). -/
theorem canonicalWindow_isExplicit (a m : ℕ) (ha : IsPrimePow a) :
    MainWindowExplicit (canonicalWindow a m ha) :=
  ⟨canonicalSpec a m ha, rfl⟩

/-- the canonical window's budget is the named completion budget
(`rfl`), hence positive. -/
theorem canonicalWindow_B_pos (a m : ℕ) (ha : IsPrimePow a) :
    0 < (canonicalWindow a m ha).B :=
  (canonicalCompletion a).budget_pos

/-! ## The final domain: the canonical certificate predicate -/

/-- **THE CANONICAL WINDOW PREDICATE** (C1 -- the rational-certificate
layer; r397: NOT the quantifier domain).  A rational certificate
window `w` mesh-represents the completed canonical construction at
some anchor and mesh level.  `RepresentsWindow` is the r320
certificate (node/comb/arch within one mesh, u/B EXACT, separation
discipline).

r397 DOMAIN CORRECTION: this predicate is a CERTIFICATE over the
real construction, not the domain of the open statements.  Two
defects as a domain: (A) possible emptiness after exact real
transcription (u/B exact against generically irrational completion
data -- nonemptiness unprovable while the completion is opaque);
(B) mesh-width error uncoupled from the shrinking L* margin.
The actual domain is `RealCanonicalWindow` / `W^ℝ(a,m)` in
RH/Selected.lean, constructed totally.  The C1 holes below are
kept as the alternative (rational-certificate) route.  NO RH CLAIM. -/
def CanonicalWindow (w : VonMangoldtWindow) : Prop :=
  ∃ (a m : ℕ) (ha : IsPrimePow a),
    RepresentsWindow w (canonicalWindow a m ha) (canonicalSpec a m ha).mesh

/-- **the budget half of the old terminal statement is PROVED on the
final domain** (C1 sharpening): B-fidelity (r320 clause 5) plus the
completion's `budget_pos` give `0 < B` -- the old
`terminal_positive_main` sorry carried this conjunct as open content;
canonically it is finite bookkeeping. -/
theorem canonical_budget_pos (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : (0 : ℝ) < ((w.B : ℚ) : ℝ) := by
  obtain ⟨a, m, ha, hrep⟩ := hw
  obtain ⟨hS, -, -, -, -, hB, -, -⟩ := hrep
  rw [hB]
  exact (canonicalCompletion a).budget_pos

/-! ## ALTERNATIVE ROUTE (r397 degradation): the C1 rational-certificate
holes, kept as conjectures

r397: `lstar_canonical` and `terminal_q_canonical` are NOT the mincut.
They quantify over `CanonicalWindow`, which may be empty (Problem A)
and whose mesh-tolerance is too coarse (Problem B).  They remain as
typed `sorry`s so the existing finite-algebra corollaries still
typecheck; they are the alternative (rational-certificate) route.
r434 PATH AUDIT: they are OFF the FREQ RH-path
(`internal_weil_nonneg_of_frequently_selected` does not apply either hole; the
mincut is `frequently_selected_augDualResolvent_ge_half` plus
the named read-identification remainder).  Direct Selected-R†
semidefiniteness bypasses the old global terminal quantor
`∀ CanonicalWindow, q_N < 1`.  Kept, not deleted.
The load-bearing open kernel is
`frequently_selected_augDualResolvent_ge_half` in
RH/FrequentlySelected.lean (r430);
`selected_augDualResolvent_gt_half` is the stronger
(`∀ᶠ`, `PosDef`) alternative. -/

/-- **CONJECTURE / ALTERNATIVE ROUTE** (C1 retype of
`lstar_subordination`; r397: degraded, not the mincut).
Lemma L* on rational certificate windows.  The `sorry` is kept;
the domain `CanonicalWindow` is the certificate layer, not the
real construction.  NO RH CLAIM. -/
theorem lstar_canonical (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : LStar w := by
  sorry

/-- **CONJECTURE / ALTERNATIVE ROUTE** (C1 retype of
`terminal_positive_main`; r397: degraded, not the mincut).
The terminal cross-ratio `q_N < 1` on rational certificate windows.
Budget positivity remains proved (`canonical_budget_pos`).  NO RH
CLAIM. -/
theorem terminal_q_canonical (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : w.q < 1 := by
  sorry

/-- the full terminal statement on canonical windows -- PROVED from
the sharpened hole plus the canonical budget positivity (statement
verbatim the old `terminal_positive_main` conclusion; the sorry
content shrank to `terminal_q_canonical`). -/
theorem terminal_canonical (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : TerminalPositive w :=
  ⟨canonical_budget_pos w hw, terminal_q_canonical w hw⟩

/-! ## The master theorem and its corollaries on the final domain
(statements verbatim the r305/r273 forms, hypothesis retyped
`MainWindow → CanonicalWindow`; proofs verbatim through the existing
finite algebra -- the open content is exactly the two holes above) -/

/-- **THE MASTER THEOREM, final domain** (C1; statement verbatim r273,
proof = the r305 reconstruction over the two canonical holes): for a
canonical window every augmented matrix `A_{w,n} = [[H_n, u_n],
[u_nᵀ, B]]` through the half-filling cap is positive definite.  NO RH
CLAIM. -/
theorem augmented_prefix_positive (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) :
    ∀ n ≤ w.cap, (w.A n).PosDef :=
  lstar_terminal_implies_master w (lstar_canonical w hw)
    (terminal_canonical w hw)

/-- **former edge B** (`PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01`
[O]): the whole prefix chain through the cap is positive on canonical
windows.  PROVED from the master theorem (block extraction + Sylvester
ratio); proof verbatim r305. -/
theorem prefix_chain_positive_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) :
    ∀ k, k + 1 ≤ w.cap → 0 < w.h k := by
  intro k hk
  have h1 := w.hankel_posDef_of_augmented
    (augmented_prefix_positive w hw k (le_trans (Nat.le_succ k) hk))
  have h2 := w.hankel_posDef_of_augmented
    (augmented_prefix_positive w hw (k + 1) hk)
  exact w.h_pos_of_posDef h1 h2

/-- the terminal Schur margin is positive on canonical windows.
PROVED (Schur step); proof verbatim r305. -/
theorem terminal_margin_positive_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : 0 < w.D w.cap := by
  have hA := augmented_prefix_positive w hw w.cap le_rfl
  exact w.D_pos_of_augmented hA (w.hankel_posDef_of_augmented hA)

/-- **former edge A** (`PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01`
[O]): the terminal cross-ratio inequality on canonical windows --
since C1 this is the hole `terminal_q_canonical` itself (kept as a
named theorem so downstream references survive verbatim). -/
theorem terminal_crossratio_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : w.q < 1 :=
  terminal_q_canonical w hw

/-- free-window positivity on canonical windows, via L* (the wave-6
finite-algebra direction; proof verbatim). -/
theorem lstar_free_window_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : ∀ n < w.cap, 0 < w.h n :=
  lstar_implies_free_window w (lstar_canonical w hw)

/-- **the fog-free central hole as a corollary** (wave-5 statement,
ledger `PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` [O]; statement
verbatim r305 modulo the C1 domain retype): on a canonical window the
whole pivot chain through the half-filling cap is positive.  The open
content lives entirely in `lstar_canonical`.  NO RH CLAIM. -/
theorem free_window_positivity (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : ∀ n < w.cap, 0 < w.h n :=
  lstar_free_window_main w hw

/-- **the combined target form L† on canonical windows** (r332
statement, C1 domain): PROVED from the two canonical holes through the
r332 equivalence -- deliberately NOT a new sorry. -/
theorem augmentedSubordination_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : AugmentedSubordination w :=
  (augmentedSubordination_iff_lstar_and_terminal w).mpr
    ⟨lstar_canonical w hw, terminal_canonical w hw⟩

/-- the master theorem through the L† route (record; verbatim r332
modulo the domain retype). -/
theorem augmented_prefix_positive_via_ldagger (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) : ∀ n ≤ w.cap, (w.A n).PosDef :=
  (augmentedSubordination_iff_masterCap w).mp
    (augmentedSubordination_main w hw)

/-! ## The pair coordinates: the r263 dictionary as ONE named lemma,
the pair closure as a corollary (C1 goal 2 -- the duplicate retired)

Until C1 the border/fiber hole existed TWICE: as the terminal
statement and as `pair_margin_main` (RH/PairBound.lean, the H5 margin
law), connected only by prose ("the r263 dictionary `Z²/m = q_N` is
measured, not formalized").  C1 formalizes the connection and removes
the duplication honestly:
  * the DICTIONARY is the one named lemma below -- it is NOT provable
    as window algebra over the current definitions: `q` is the
    determinant/Schur object of the moment basis while `Z =
    terminalDrive w = u_{cap-1}` reads the raw border column; the
    identification runs through the monic orthogonal-polynomial
    transform of the border data (r263 `Z_w = r_{N-1}`), whose
    transcription belongs to the border TODO.  Measured EXACT on
    42/42 rungs (r263, note DXCIV; re-gated r270/r271).  Type:
    MEASURED DICTIONARY / transcription-blocked -- honest input, not
    an arithmetic hole;
  * the pair CLOSURE (`Z²/M² < 1`, the conclusion the r271 route
    certifies) is then a PROVED corollary of `terminal_q_canonical`;
  * the pair margin LAW (the specific certificate route
    `|Zloc| + pairBound < M`) is DEMOTED to the named Prop
    `PairBound.PairMarginLaw`: it is measured to MISS on kz39/kz15
    (0.002/0.06 dec under b2LEVEL2), so it was never a faithful
    statement of the hole -- asserting it as a sorry overclaimed.
    The certificate direction stays proved
    (`PairBound.pair_closes_of_marginLaw`). -/

/-- **THE r263 DICTIONARY, named** (C1 goal 2): on a canonical window
the terminal drive readout squares to the budget-normalized terminal
cross-ratio, `Z² = (5/7)·q_N` (the r263 identities `Z_w = r_{N-1}`,
`Z²/m = q_N` with the r243 floor `m = 5/7`).  Measured exact on 42/42
rungs; NOT provable from the current window definitions (see the
section header) -- the `sorry` is a typed transcription-blocked
dictionary import, not a new arithmetic hole.  NO RH CLAIM. -/
theorem pair_terminal_dictionary (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) :
    PairBound.terminalDrive w ^ 2 = (5 / 7) * w.q := by
  sorry

/-- **the pair closure is a COROLLARY** (C1 goal 2 -- formerly
`pair_closes_main` conditioned on the `pair_margin_main` sorry; now
PROVED from the terminal hole through the named dictionary): on a
canonical window the terminal readout closes, `Z²/M² < 1` for the
r243 budget `M² = 5/7`. -/
theorem pair_closes_main (w : VonMangoldtWindow)
    (hw : CanonicalWindow w) {M : ℝ} (hM : 0 < M)
    (hM2 : M ^ 2 = 5 / 7) :
    PairBound.terminalDrive w ^ 2 / M ^ 2 < 1 := by
  have hq := terminal_q_canonical w hw
  have hlt : PairBound.terminalDrive w ^ 2 < M ^ 2 := by
    rw [pair_terminal_dictionary w hw, hM2]
    linarith
  exact (div_lt_one (by positivity)).mpr hlt

end RH
