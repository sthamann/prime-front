/-
RH/Source.lean -- THE EXPLICIT SOURCE INTERFACE (r310, reviewer plan
section 6.3): the exact real window source as a proof interface.

WHY THIS FILE EXISTS.  Until r310 the source boundary of the pilot was
the deliberately `opaque` predicate `MainWindow : VonMangoldtWindow →
Prop` (RH/Window.lean, r273): honest, but NOT a construction -- the
real window positions and weights contain quantities like `log p^k`,
while the certificate windows are exact rationals.  The reviewer's
section 6.3 mandate: separate, as three explicit Lean objects,
  (a) the MATHEMATICAL window built from `Real.log` on prime powers
      and the von-Mangoldt weights `Λ(p^k)` (this file:
      `PrimeWindowSpec`, `buildPrimeWindow`, `MainWindowExplicit`),
  (b) the RATIONAL certificate window (the existing
      `VonMangoldtWindow` of RH/Window.lean -- the frozen v962/v963
      exact-rational data), and
  (c) the proved inclusion/approximation layer between them
      (`rational_window_approximates`, PROVED; the mesh-level
      representation predicates `RepresentsSpec`/`RepresentsWindow`;
      the opacity bridge -- since r310b in the reviewer target form
      `mainWindow_iff_builtFromPrimeSource`, a documented `sorry`,
      with the r310 form `mainWindow_explicit_bridge` proved from it).

STRATEGY DECISION (documented, per the r310 work order): the
CONSERVATIVE route.  `MainWindow` stays opaque and untouched -- every
downstream theorem of RH/Window.lean, RH/Closure.lean and
RH/PairBound.lean keeps its exact statement.  The explicit source
enters as the NEW predicate `MainWindowExplicit` on the new real
window structure `PrimeWindow`, plus the bridge statement connecting
the two (since r310b: `mainWindow_iff_builtFromPrimeSource`).  The
bridge carries a
documented `sorry` (type: DEFINITIONAL/TECHNICAL -- forced by the r273
opacity: no statement about an `opaque` predicate is provable by
design; the bridge itself IS the honest new interface).  The invasive
route (redefining `MainWindow`) was rejected because it would silently
change the mathematical content of the four existing intentional
`sorry`s (`lstar_subordination`, `terminal_positive_main`,
`pair_margin_main`, `crossing_budget`) -- those are the holes of other
lanes and MUST stay byte-identical.

PYTHON SOURCE OF THE CONSTRUCTION (translated here is the
CONSTRUCTION, never any measured value).  The authoritative builder
chain of the corpus windows:
  * verification/v563_paper2_readouts.py -- `von_mangoldt_table`
    (sieve; `Λ(n) = log p` iff `n = p^k`), `_NN` (the prime powers),
    `U_ALL = log(_NN)` (node positions `log p^k`),
    `MU_ALL = 2 Λ(n)/sqrt(n)` (comb masses), `build_window(kz)`
    (anchor `alpha = U_ALL[kz] = log p^k` of the zone, mesh
    `Δ = gap/(2 ν)`, atoms = all prime powers with `log n ≤ 2 alpha`,
    i.e. `n ≤ (p^k)^2`), `atom_lags_at` (tent assembly on the mesh),
    `arch_lags`/`arch_A` (the exact archimedean Weil kernel);
  * experiments/tfpt-discovery/port_integrable_kernel_probe.py --
    `build_rung`, `folded_measure` (fold onto `cos(2π j/L)` nodes,
    sign split into the `mu` and `nu` zones);
  * experiments/tfpt-discovery/principal_bessel_probe.py --
    `window_pack`, `smooth_comb` (the sealed smooth border zone;
    border column `F` via the same builder map), budget
    `B = S_{N-2} + 5/7` (r243 form).
This file transcribes the ARITHMETIC layer of that chain exactly: the
atom set (prime powers up to the squared anchor), the node positions
(`Real.log` of the prime powers -- genuine irrationals now, via
mathlib), the comb weights (mathlib's `ArithmeticFunction.vonMangoldt`
-- the exact `Λ`), the anchor/mesh bookkeeping and the window rule
`0 ≤ log n ≤ 2 log(anchor)`.  The archimedean weights and the border
data enter the spec as EXPLICIT FIELDS with nonnegativity (their exact
integral-kernel transcription -- `arch_A`, the folded tent masses, the
v958 border column -- is the documented next step of this lane: it is
classical analysis, typed below, not arithmetic).

THE FOUR STRUCTURE THEOREMS of the reviewer plan, status:
  * `predefined_family`      -- PROVED (constructive): the family atom
                                set is decided by arithmetic alone.
  * `mesh_refinement_compatible` -- PROVED (constructive, `rfl`-level
                                BY DESIGN: refinement changes only the
                                mesh level, never the atom data) plus
                                the real content `mesh_refinement_shrinks`.
  * `cofinal_prime_windows`  -- PROVED (Euclid via
                                `Nat.exists_infinite_primes`).
  * `finite_forms_converge_to_weil` -- PROVED in the strong
                                stabilization form for the prime side:
                                for compactly supported test data the
                                finite comb forms EQUAL the Weil
                                prime-side tsum once the window covers
                                the support.  (The archimedean side
                                and the spectral/zero side of the full
                                Weil form are NOT formalized here --
                                the former is the classical-analysis
                                TODO above, the latter is the
                                arithmetically open content of the
                                program.)
Genuine new proofs besides these: `nodes_injective` (the real window
nodes are pairwise distinct -- `Real.log` strict monotonicity on the
strictly increasing prime powers), `node_pos`, `combWeight_pos`
(via mathlib `vonMangoldt_ne_zero_iff`), and
`rational_window_approximates` (density of ℚ: every real prime window
admits rational certificate data within every positive bound).

r310b REFINEMENTS (reviewer plan section 8, accepted r310 +
adjudicated refinements):
  * THE FOUR-STAGE SUPPORT CHAIN (the reviewer's injectivity warning:
    the r310 `nodes_injective` holds for the UNFOLDED log nodes only;
    after mirroring/folding/tent-sampling deliberately equal geometric
    nodes arise, so raw injectivity must not be overclaimed):
      stage 1  `primePow_index_injective`  -- `p^k = q^ℓ ⟹ p = q, k = ℓ`
               (unique factorization via `minFac`; PROVED),
      stage 2  `nodes_injective`           -- unfolded `log p^k` nodes
               pairwise distinct (PROVED, unchanged from r310),
      stage 3  `foldedWindow`              -- the explicit
               quotient/aggregation construction (equal folded nodes
               merged, weights ADDED; Python `folded_measure` /
               `np.add.at`) with the mass-conservation structure
               theorem `foldedWindow_mass` (PROVED),
      stage 4  `support_nodup`             -- distinctness AFTER the
               aggregation, on the merged support (PROVED).
    FOLDING STATUS (honest): `buildPrimeWindow` transcribes the
    UNFOLDED two-zone comb -- the fold is NOT hidden inside it; it is
    the explicit stage-3 step `foldedWindow`, stated for an arbitrary
    fold map `φ : ℝ → ℝ` of which the corpus map
    `u ↦ cos(2π u/(Δ L))` (folded_measure: index fold `min(j, L-j)`,
    plus the `u < Δ` mirror of `atom_lags_at`) is an instance.
  * THE FOUR SOURCE THEOREMS: `buildPrimeWindow_source_exact` (the
    built window carries DEFINITIONALLY the `Λ`/`log` source data),
    `buildPrimeWindow_weights_nonnegative` (all weight channels,
    fold-stable), `buildPrimeWindow_support_canonical` (the full
    stage-1/2/3/4 chain), `buildPrimeWindow_refinement_compatible`
    (the built window is mesh-independent, also under any fixed fold
    map; the corpus fold map itself is mesh-dependent -- documented
    at the theorem).  All four PROVED.
  * THE BRIDGE IN TARGET FORM: the ONE documented `sorry` of this
    file is now `mainWindow_iff_builtFromPrimeSource` (the reviewer's
    target semantics: MAIN ⟺ the certificate window mesh-represents a
    window BUILT from a prime source); the r310 form
    `mainWindow_explicit_bridge` is a PROVED corollary of it.  Census
    unchanged: the sorry moved into the sharper statement.
  * APPROXIMATION WARNING (reviewer, verbatim adjudication): because
    the measured L* margin shrinks, a proof chain "real source ≈
    rational source" would be unsound unless the approximation error
    is controlled BELOW the margin -- not established.  The rational
    windows are certificate objects, not the definition; the intended
    route is the direct real construction.  See the warning block at
    `rational_window_approximates`; no statement of this file uses
    approximation as a proof path.

r320 REPAIR (the R319 red-team audit U1-U3, all three kernel-verified
reproducible against the r310b library):
  * U1: the old bridge never bound `u`/`B` -- a `B = -1` window slipped
    through and contradicted `terminal_positive_main`.  Repair: exact
    u/B-fidelity clauses in `RepresentsSpec`/`RepresentsWindow` + the
    transcribable spec field `budget_pos` (r243 positivity half).
  * U2: the old tolerance was the bare mesh width (level 0:
    `log anchor`) -- a total node collision slipped through and
    contradicted `lstar_subordination` (witness `p = X - 1`).  Repair:
    the separation discipline (tolerance < half the minimal node gap
    AND < every comb weight); honest price: mesh level 0 represents
    nothing, representation begins at sufficient refinement.
  * r320 verification finding BEYOND the audit: the free spec fields
    `archWeight`/`border` admit the same disease one channel over
    (arbitrary arch mass vs L* at p = 1; arbitrary border vs the
    retyped pair margin) -- no honest finite clause can close them
    before their transcriptions exist.  Repair: the opaque
    `SourceExact` guard (the r273 convention applied to the spec side).
  * the pre-r320 statement TYPES are conserved and machine-refuted as
    permanent guards in RH/Counterexamples.lean; the witness section
    at the bottom proves the retyped predicate satisfiable.

SORRY CENSUS OF THIS FILE: exactly ONE --
`mainWindow_iff_builtFromPrimeSource` (type: DEFINITIONAL/TECHNICAL,
opacity-forced; see its docstring; since r320 in the repaired
consistency-capable form; `mainWindow_explicit_bridge` is proved from
it).  The four pre-existing intentional sorrys of the pilot are
untouched (r320 retyped `pair_margin_main` in RH/PairBound.lean -- the
extraction is now a definition, the margin law stays the same hole).

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Window
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Topology.Algebra.InfiniteSum.Basic

namespace RH

local notation "Λ" => ArithmeticFunction.vonMangoldt

/-! ## Stage 1 of the support chain: the canonical prime-power index -/

/-- **STAGE 1 (r310b): the canonical prime-power index is faithful** --
`p^k = q^ℓ` with `p, q` prime and `k, ℓ ≥ 1` forces `p = q` and
`k = ℓ` (unique factorization, via `Nat.minFac` on the power).  This
is the arithmetic reason the atom list of a spec can be indexed by
`(p, k)` pairs without collision; stage 2 (`nodes_injective` below) is
its analytic image under `Real.log`, and stages 3/4 (`foldedWindow`,
`support_nodup`) handle the deliberate node merging of the folded
source. -/
theorem primePow_index_injective {p q k l : ℕ} (hp : p.Prime)
    (hq : q.Prime) (hk : k ≠ 0) (hl : l ≠ 0) (h : p ^ k = q ^ l) :
    p = q ∧ k = l := by
  have hpq : p = q := by
    have h1 : (p ^ k).minFac = p := by
      rw [Nat.pow_minFac hk, hp.minFac_eq]
    have h2 : (q ^ l).minFac = q := by
      rw [Nat.pow_minFac hl, hq.minFac_eq]
    rw [← h1, h, h2]
  subst hpq
  exact ⟨rfl, Nat.pow_right_injective hp.two_le h⟩

/-! ## (a) The mathematical window: spec and build -/

/-- **The explicit prime window spec** (r310, reviewer plan 6.3).
One corpus window is DETERMINED by this data: the strictly increasing
list of prime powers (the von-Mangoldt support atoms), the zone anchor
`p^k` (Python: `alpha = U_ALL[kz] = log(anchor)`), the mesh refinement
level (Python: `ν`, mesh `Δ = gap/(2ν)`), the archimedean weights (the
`nu` side; Python `arch_lags`/`folded_measure` -- exact transcription
of the Weil kernel is the documented classical TODO, hence a field
with nonnegativity here) and the border source data (v958 border
column + r243 budget).  Node positions and comb weights are NOT fields
-- they are DERIVED below as `Real.log` and `Λ` of `primePowers`:
that is the point of the interface. -/
structure PrimeWindowSpec where
  /-- number of source atoms. -/
  S : ℕ
  /-- the prime-power atoms `p^k` (Python `_NN[:ka]`). -/
  primePowers : Fin S → ℕ
  /-- every atom is a genuine prime power. -/
  pp_isPrimePow : ∀ j, IsPrimePow (primePowers j)
  /-- the atoms are strictly increasing (sorted, no repeats). -/
  pp_strictMono : StrictMono primePowers
  /-- the zone anchor `p^k` (Python: `alpha = log anchor`). -/
  anchor : ℕ
  anchor_isPrimePow : IsPrimePow anchor
  /-- mesh refinement level (Python `ν`; larger = finer mesh). -/
  meshLevel : ℕ
  /-- the window rule at source level: every atom `n` satisfies
  `log n ≤ 2 log anchor`, i.e. `n ≤ anchor²` (Python `atoms_in`). -/
  pp_le : ∀ j, primePowers j ≤ anchor ^ 2
  /-- archimedean/smooth weights (the `nu` side; exact Weil-kernel
  transcription = documented classical TODO). -/
  archWeight : Fin S → ℝ
  arch_nonneg : ∀ j, 0 ≤ archWeight j
  /-- border source data (v958 border column of the smooth zone). -/
  border : ℕ → ℝ
  /-- budget scalar (r243 form `B = S_{N-2} + 5/7`). -/
  budget : ℝ
  /-- budget positivity (r320, U1 repair): the r243 budget form is a sum
  of nonnegative drain increments `rho_k = F_k^2/h_k >= 0` plus the
  positive floor `5/7`, hence positive -- this is the TRANSCRIBABLE half
  of the budget form and is carried as a spec field; the exact drain-sum
  identity stays with the border TODO (`SourceExact` below). -/
  budget_pos : 0 < budget

namespace PrimeWindowSpec

variable (s : PrimeWindowSpec)

/-- **the real node positions** `log p^k` -- DERIVED, not a field
(Python `U_ALL = np.log(_NN)`). -/
noncomputable def node (j : Fin s.S) : ℝ := Real.log (s.primePowers j)

/-- **the real comb weights** `Λ(p^k)` -- DERIVED, not a field, via
mathlib's exact von-Mangoldt function (Python `von_mangoldt_table`;
the corpus rescale `2Λ(n)/√n` is a positive diagonal gauge and lives
in the builder map, not in the arithmetic). -/
noncomputable def combWeight (j : Fin s.S) : ℝ := Λ (s.primePowers j)

/-- the window half-length `alpha = log anchor` (Python `U_ALL[kz]`). -/
noncomputable def alpha : ℝ := Real.log s.anchor

/-- the mesh width at refinement level `meshLevel`: `alpha/(ν+1)`
(the Lean-side normalization of the Python `Δ = gap/(2ν)`; only the
strict shrinking along refinement is consumed downstream). -/
noncomputable def mesh : ℝ := s.alpha / (s.meshLevel + 1)

theorem two_le_pp (j : Fin s.S) : 2 ≤ s.primePowers j :=
  (s.pp_isPrimePow j).two_le

/-- the real node map is strictly monotone: `Real.log` is strictly
monotone on the positive reals and the prime powers increase. -/
theorem node_strictMono : StrictMono s.node := by
  intro i j hij
  have h2 : (2 : ℝ) ≤ (s.primePowers i : ℝ) := by
    exact_mod_cast s.two_le_pp i
  have hlt : (s.primePowers i : ℝ) < (s.primePowers j : ℝ) := by
    exact_mod_cast s.pp_strictMono hij
  exact Real.log_lt_log (by linarith) hlt

/-- **nodes_injective, spec level** (the reviewer's requested genuine
proof): the real `log p^k` positions are pairwise distinct --
log-monotonicity + strict ordering of the prime powers. -/
theorem node_injective : Function.Injective s.node :=
  s.node_strictMono.injective

/-- every real node is strictly positive (`p^k ≥ 2 > 1`). -/
theorem node_pos (j : Fin s.S) : 0 < s.node j :=
  Real.log_pos (by exact_mod_cast (s.pp_isPrimePow j).one_lt)

theorem combWeight_nonneg (j : Fin s.S) : 0 ≤ s.combWeight j :=
  ArithmeticFunction.vonMangoldt_nonneg

/-- the comb weight of a genuine prime power is strictly positive
(mathlib `vonMangoldt_ne_zero_iff`). -/
theorem combWeight_pos (j : Fin s.S) : 0 < s.combWeight j := by
  have hne : Λ (s.primePowers j) ≠ 0 :=
    ArithmeticFunction.vonMangoldt_ne_zero_iff.mpr (s.pp_isPrimePow j)
  exact lt_of_le_of_ne ArithmeticFunction.vonMangoldt_nonneg (Ne.symm hne)

/-- the source-level window rule in real coordinates:
`log n ≤ 2 log anchor` from `n ≤ anchor²`. -/
theorem node_le_two_alpha (j : Fin s.S) : s.node j ≤ 2 * s.alpha := by
  have hpos : (0 : ℝ) < (s.primePowers j : ℝ) := by
    have := s.two_le_pp j
    exact_mod_cast Nat.lt_of_lt_of_le Nat.zero_lt_two this
  have h1 : (s.primePowers j : ℝ) ≤ ((s.anchor : ℝ)) ^ 2 := by
    have := s.pp_le j
    exact_mod_cast this
  have hlog : Real.log (s.primePowers j) ≤ Real.log ((s.anchor : ℝ) ^ 2) := by
    rcases eq_or_lt_of_le h1 with heq | hlt
    · rw [heq]
    · exact le_of_lt (Real.log_lt_log hpos hlt)
  rw [Real.log_pow] at hlog
  simpa [node, alpha] using hlog

end PrimeWindowSpec

/-- **The mathematical (real) window** -- the ℝ-valued mirror of the
rational certificate structure `VonMangoldtWindow` (RH/Window.lean):
same fields, real entries.  The corpus real windows instantiate it
through `buildPrimeWindow`; the rational certificate windows relate to
it through `RepresentsSpec`/`rational_window_approximates` below. -/
structure PrimeWindow where
  S : ℕ
  nodes : Fin S → ℝ
  combWeight : Fin S → ℝ
  archWeight : Fin S → ℝ
  comb_nonneg : ∀ j, 0 ≤ combWeight j
  arch_nonneg : ∀ j, 0 ≤ archWeight j
  lo : ℝ
  hi : ℝ
  window_rule : ∀ j, lo ≤ nodes j ∧ nodes j ≤ hi
  u : ℕ → ℝ
  B : ℝ

/-- **the build map** (reviewer plan 6.3 target type): the mathematical
window IS a function of the spec -- nodes are `Real.log` of the prime
powers, comb weights are the exact `Λ`, the window rule is PROVED from
the source-level rule, arch/border/budget pass through. -/
noncomputable def buildPrimeWindow (s : PrimeWindowSpec) : PrimeWindow where
  S := s.S
  nodes := s.node
  combWeight := s.combWeight
  archWeight := s.archWeight
  comb_nonneg := s.combWeight_nonneg
  arch_nonneg := s.arch_nonneg
  lo := 0
  hi := 2 * s.alpha
  window_rule := fun j => ⟨le_of_lt (s.node_pos j), s.node_le_two_alpha j⟩
  u := s.border
  B := s.budget

/-- **the explicit main-window predicate** (reviewer plan 6.3 target
type): a real window is explicitly-main iff it is BUILT from a prime
window spec.  This is a genuine construction, not an opaque marker --
compare `MainWindow` (RH/Window.lean), which stays the honest opaque
predicate of the rational certificate layer; the two are connected by
`mainWindow_explicit_bridge` below. -/
def MainWindowExplicit (w : PrimeWindow) : Prop :=
  ∃ s : PrimeWindowSpec, w = buildPrimeWindow s

/-- **STAGE 2 -- nodes_injective, window level**: the built window has
pairwise distinct node positions -- the r310 reviewer target proof.
SCOPE (r310b, reviewer warning heeded): this holds for the UNFOLDED
`log p^k` nodes, which is exactly what `buildPrimeWindow` produces.
After folding, deliberately equal geometric nodes arise and raw
injectivity is FALSE in general -- the folded source is handled by the
explicit aggregation `foldedWindow` (stage 3) and distinctness returns
only on the merged support (`support_nodup`, stage 4). -/
theorem nodes_injective (s : PrimeWindowSpec) :
    Function.Injective (buildPrimeWindow s).nodes :=
  s.node_injective

/-! ## Stages 3/4: the folding layer (r310b, reviewer plan section 8)

FOLDING STATUS (honest): `buildPrimeWindow` transcribes the UNFOLDED
two-zone comb -- the r310 file contained NO folding step, and none was
hidden inside the build map.  The Python source additionally FOLDS
before running the chain (port_integrable_kernel_probe.folded_measure:
index fold `min(j, L-j)`, node map `cos(2π j/L)`, weight aggregation
`np.add.at`; plus the `u < Δ` mirror inside v563 `atom_lags_at`).
Under such a fold, deliberately EQUAL geometric nodes arise; stating
injectivity of the raw folded map would be wrong and is NOT done.
Instead the fold is an explicit quotient/aggregation step: equal
folded nodes are merged into a `Finset` support and the weights of
every channel are ADDED over each fiber.  The layer is stated for an
arbitrary fold map `φ : ℝ → ℝ`; the corpus map is an instance (its
exact transcription -- mesh embedding, `cos`, `4 sin²(θ/2)` factor --
belongs to the documented classical arch/border TODO of the header). -/

/-- the folded support: the image of the window nodes under the fold
map, MERGED (equal folded nodes appear once -- `Finset.image`). -/
noncomputable def foldedSupport (w : PrimeWindow) (φ : ℝ → ℝ) : Finset ℝ :=
  Finset.univ.image fun j => φ (w.nodes j)

/-- the folded node positions: the merged support, sorted increasingly
(`Finset.orderIsoOfFin`). -/
noncomputable def foldedNode (w : PrimeWindow) (φ : ℝ → ℝ)
    (i : Fin (foldedSupport w φ).card) : ℝ :=
  (((foldedSupport w φ).orderIsoOfFin rfl) i : ℝ)

/-- the fiber of a folded node: all original atoms folding onto it
(the `np.add.at` index set). -/
noncomputable def foldFiber (w : PrimeWindow) (φ : ℝ → ℝ)
    (i : Fin (foldedSupport w φ).card) : Finset (Fin w.S) :=
  Finset.univ.filter fun j => φ (w.nodes j) = foldedNode w φ i

/-- **STAGE 3 -- the folded window** (r310b): the quotient/aggregation
construction.  Equal folded nodes are merged (`foldedSupport`), the
weights of each channel are ADDED over the fiber (Python `np.add.at`);
border/budget pass through (the corpus border zone is folded by the
same map upstream of the chain). -/
noncomputable def foldedWindow (w : PrimeWindow) (φ : ℝ → ℝ) :
    PrimeWindow where
  S := (foldedSupport w φ).card
  nodes := foldedNode w φ
  combWeight := fun i => ∑ j ∈ foldFiber w φ i, w.combWeight j
  archWeight := fun i => ∑ j ∈ foldFiber w φ i, w.archWeight j
  comb_nonneg := fun i => Finset.sum_nonneg fun j _ => w.comb_nonneg j
  arch_nonneg := fun i => Finset.sum_nonneg fun j _ => w.arch_nonneg j
  lo := if h : (foldedSupport w φ).Nonempty
    then (foldedSupport w φ).min' h else 0
  hi := if h : (foldedSupport w φ).Nonempty
    then (foldedSupport w φ).max' h else 0
  window_rule := fun i => by
    have hne : (foldedSupport w φ).Nonempty := Finset.card_pos.mp i.pos
    have hmem : foldedNode w φ i ∈ foldedSupport w φ :=
      (((foldedSupport w φ).orderIsoOfFin rfl) i).2
    simp only [dif_pos hne]
    exact ⟨Finset.min'_le _ _ hmem, Finset.le_max' _ _ hmem⟩
  u := w.u
  B := w.B

/-- the folded nodes are strictly increasing (the sorted merged
support). -/
theorem foldedWindow_nodes_strictMono (w : PrimeWindow) (φ : ℝ → ℝ) :
    StrictMono (foldedWindow w φ).nodes := fun _ _ hij =>
  Subtype.coe_lt_coe.mpr
    (((foldedSupport w φ).orderIsoOfFin rfl).strictMono hij)

/-- **STAGE 4 -- support_nodup** (r310b): AFTER the aggregation the
folded support carries no duplicate -- the folded node positions are
strictly increasing, hence pairwise distinct.  (BEFORE the aggregation
this is deliberately false in general: merging IS the purpose of the
fold.  Compare stage 2 `nodes_injective`, which lives on the unfolded
chain.) -/
theorem support_nodup (w : PrimeWindow) (φ : ℝ → ℝ) :
    Function.Injective (foldedWindow w φ).nodes :=
  (foldedWindow_nodes_strictMono w φ).injective

/-- **the stage-3 structure theorem -- exact mass conservation**: the
aggregation is a quotient, not a projection -- for EVERY weight
channel `f` the folded fiber sums recover the total mass exactly
(`Finset.sum_fiberwise_of_maps_to`; the Lean form of the `np.add.at`
bookkeeping identity). -/
theorem foldedWindow_mass (w : PrimeWindow) (φ : ℝ → ℝ)
    (f : Fin w.S → ℝ) :
    ∑ i, (∑ j ∈ foldFiber w φ i, f j) = ∑ j, f j := by
  have h1 : ∑ i : Fin (foldedSupport w φ).card,
      (∑ j ∈ foldFiber w φ i, f j)
      = ∑ x ∈ foldedSupport w φ,
          ∑ j ∈ Finset.univ.filter (fun j => φ (w.nodes j) = x), f j := by
    rw [← Finset.sum_coe_sort (foldedSupport w φ)]
    exact Fintype.sum_equiv
      ((foldedSupport w φ).orderIsoOfFin rfl).toEquiv _ _ (fun i => rfl)
  rw [h1]
  exact Finset.sum_fiberwise_of_maps_to
    (fun j _ => Finset.mem_image_of_mem _ (Finset.mem_univ j)) f

/-- comb-channel mass conservation under folding. -/
theorem foldedWindow_comb_mass (w : PrimeWindow) (φ : ℝ → ℝ) :
    ∑ i, (foldedWindow w φ).combWeight i = ∑ j, w.combWeight j :=
  foldedWindow_mass w φ w.combWeight

/-- arch-channel mass conservation under folding. -/
theorem foldedWindow_arch_mass (w : PrimeWindow) (φ : ℝ → ℝ) :
    ∑ i, (foldedWindow w φ).archWeight i = ∑ j, w.archWeight j :=
  foldedWindow_mass w φ w.archWeight

/-! ## The four source theorems (r310b, reviewer plan section 8) -/

/-- **SOURCE THEOREM 1 -- the built window is source-exact** (r310b;
PROVED, constructive: `rfl` BY DERIVATION, which is the content --
nodes and comb weights of the built window are not merely close to
but DEFINITIONALLY the `log p^k` / `Λ(p^k)` source data, because the
spec derives them instead of carrying them as free fields). -/
theorem buildPrimeWindow_source_exact (s : PrimeWindowSpec) :
    (buildPrimeWindow s).S = s.S ∧
    (∀ j : Fin s.S, (buildPrimeWindow s).nodes j
      = Real.log (s.primePowers j)) ∧
    (∀ j : Fin s.S, (buildPrimeWindow s).combWeight j
      = Λ (s.primePowers j)) :=
  ⟨rfl, fun _ => rfl, fun _ => rfl⟩

/-- **SOURCE THEOREM 2 -- all weight channels are nonnegative**
(r310b; PROVED): comb via mathlib `vonMangoldt_nonneg` (strictly
positive even, `combWeight_pos`), arch via the spec field -- and both
channels STAY nonnegative under any fold (the aggregation adds
nonnegatives). -/
theorem buildPrimeWindow_weights_nonnegative (s : PrimeWindowSpec) :
    (∀ j, 0 ≤ (buildPrimeWindow s).combWeight j) ∧
    (∀ j, 0 ≤ (buildPrimeWindow s).archWeight j) ∧
    ∀ φ : ℝ → ℝ,
      (∀ i, 0 ≤ (foldedWindow (buildPrimeWindow s) φ).combWeight i) ∧
      (∀ i, 0 ≤ (foldedWindow (buildPrimeWindow s) φ).archWeight i) :=
  ⟨s.combWeight_nonneg, s.arch_nonneg, fun φ =>
    ⟨(foldedWindow (buildPrimeWindow s) φ).comb_nonneg,
     (foldedWindow (buildPrimeWindow s) φ).arch_nonneg⟩⟩

/-- **SOURCE THEOREM 3 -- the support is canonical** (r310b; PROVED):
the full four-stage chain -- stage 1 `primePow_index_injective` (the
canonical `(p,k) ↦ p^k` indexing is collision-free), stage 2: the
UNFOLDED built nodes are pairwise distinct, stages 3/4: after ANY fold
the aggregated support is again duplicate-free. -/
theorem buildPrimeWindow_support_canonical (s : PrimeWindowSpec) :
    Function.Injective (buildPrimeWindow s).nodes ∧
    ∀ φ : ℝ → ℝ,
      Function.Injective (foldedWindow (buildPrimeWindow s) φ).nodes :=
  ⟨nodes_injective s, fun φ => support_nodup (buildPrimeWindow s) φ⟩

/-! ## The predefined window family (structure theorems 1-3)

The Python family (`build_window(kz)` for the zone index, `ν` for the
mesh): the atom set of the window at anchor `a` is ALL prime powers
`n ≤ a²` -- decided by arithmetic alone, before any chain is run.  The
Lean transcription indexes the family by `(a, m)` = (anchor, mesh
level); the family members are `specFamily a m ha` with zero
arch/border placeholder data (the family statements below quantify the
ARITHMETIC layer -- predefinedness, refinement compatibility,
cofinality of the atom sets; the exact archimedean transcription is
the documented classical TODO of the file header, and NO statement
below consumes the placeholder fields). -/

/-- the atom set of the window at anchor `a`: all prime powers
`n ≤ a²` (Python `atoms_in(alpha) = #{n : log n ≤ 2 alpha}`). -/
def windowAtoms (a : ℕ) : Finset ℕ :=
  (Finset.range (a ^ 2 + 1)).filter IsPrimePow

/-- **the predefined window family**: the spec at anchor `a` and mesh
level `m` -- atoms sorted by `Finset.orderIsoOfFin`, arch/border zero
placeholders (see section header). -/
noncomputable def specFamily (a m : ℕ) (ha : IsPrimePow a) :
    PrimeWindowSpec where
  S := (windowAtoms a).card
  primePowers := fun j => (((windowAtoms a).orderIsoOfFin rfl) j : ℕ)
  pp_isPrimePow := fun j =>
    (Finset.mem_filter.mp (((windowAtoms a).orderIsoOfFin rfl) j).2).2
  pp_strictMono := fun _ _ hij =>
    Subtype.coe_lt_coe.mpr (((windowAtoms a).orderIsoOfFin rfl).strictMono hij)
  anchor := a
  anchor_isPrimePow := ha
  meshLevel := m
  pp_le := fun j => Nat.lt_succ_iff.mp (Finset.mem_range.mp
    (Finset.mem_filter.mp (((windowAtoms a).orderIsoOfFin rfl) j).2).1)
  archWeight := fun _ => 0
  arch_nonneg := fun _ => le_refl 0
  border := fun _ => 0
  -- placeholder budget = the bare r243 floor `5/7` (r320: the spec now
  -- carries budget positivity, so the pre-r320 placeholder `0` is no
  -- longer admissible; the family statements consume no budget data).
  budget := 5 / 7
  budget_pos := by norm_num

/-- **STRUCTURE THEOREM 1 -- the family is predefined** (r310,
reviewer plan 6.3; PROVED, constructive).  The atom set of the family
member at anchor `a` is characterized by arithmetic alone: `n` is an
atom iff `n` is a prime power with `n ≤ a²`.  Nothing about the
family depends on any measured chain output -- the family is fixed
BEFORE any positivity is evaluated (the reviewer's "vordefiniert,
nicht ergebnisabhängig"). -/
theorem predefined_family (a m : ℕ) (ha : IsPrimePow a) (n : ℕ) :
    (∃ i, (specFamily a m ha).primePowers i = n) ↔
      (IsPrimePow n ∧ n ≤ a ^ 2) := by
  constructor
  · rintro ⟨i, rfl⟩
    have hmem := (((windowAtoms a).orderIsoOfFin rfl) i).2
    have h := Finset.mem_filter.mp hmem
    exact ⟨h.2, Nat.lt_succ_iff.mp (Finset.mem_range.mp h.1)⟩
  · rintro ⟨hpp, hle⟩
    have hmem : n ∈ windowAtoms a :=
      Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (Nat.lt_succ_iff.mpr hle), hpp⟩
    refine ⟨((windowAtoms a).orderIsoOfFin rfl).symm ⟨n, hmem⟩, ?_⟩
    show (((windowAtoms a).orderIsoOfFin rfl)
      (((windowAtoms a).orderIsoOfFin rfl).symm ⟨n, hmem⟩) : ℕ) = n
    rw [OrderIso.apply_symm_apply]

/-- **STRUCTURE THEOREM 2 -- mesh refinement compatibility** (r310;
PROVED, constructive -- `rfl`-level BY DESIGN, which is the content:
in the explicit family, changing the mesh level changes ONLY the
`meshLevel` field; atom count and atom data are bitwise identical,
so no refinement step can smuggle in new source data). -/
theorem mesh_refinement_compatible (a : ℕ) (ha : IsPrimePow a)
    (m m' : ℕ) :
    (specFamily a m ha).S = (specFamily a m' ha).S ∧
    (specFamily a m ha).meshLevel = m ∧
    ∀ i, (specFamily a m ha).primePowers i
      = (specFamily a m' ha).primePowers i :=
  ⟨rfl, rfl, fun _ => rfl⟩

/-- the real content of refinement: the mesh width strictly shrinks
along the refinement order (so the family is a genuine refinement
ladder, not a relabeling). -/
theorem mesh_refinement_shrinks (a : ℕ) (ha : IsPrimePow a)
    {m m' : ℕ} (h : m < m') :
    (specFamily a m' ha).mesh < (specFamily a m ha).mesh := by
  have halpha : 0 < Real.log a :=
    Real.log_pos (by exact_mod_cast ha.one_lt)
  have h1 : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  have h2 : (m : ℝ) + 1 < (m' : ℝ) + 1 := by exact_mod_cast Nat.succ_lt_succ h
  have := div_lt_div_of_pos_left halpha h1 h2
  simpa [PrimeWindowSpec.mesh, PrimeWindowSpec.alpha, specFamily] using this

/-- **SOURCE THEOREM 4 -- refinement compatibility of the built
window** (r310b; PROVED, `rfl` by design).  The BUILT window of the
family does not depend on the mesh level at all -- and therefore
neither does any folded image at a FIXED fold map.  HONEST SCOPE NOTE
(the r310b folding check): in the corpus the fold map itself is
mesh-dependent (`L = 2M − 2` grid points, node map `cos(2π j/L)`), so
refinement compatibility of the SOURCE holds unconditionally (this
statement), while the mesh enters ONLY through the fold map -- which
is exactly why the fold is the explicit stage-3 step `foldedWindow`
and not part of `buildPrimeWindow`.  The r310 statement
`mesh_refinement_compatible` (spec level) is unchanged by the folding
layer. -/
theorem buildPrimeWindow_refinement_compatible (a : ℕ)
    (ha : IsPrimePow a) (m m' : ℕ) :
    buildPrimeWindow (specFamily a m ha)
      = buildPrimeWindow (specFamily a m' ha) ∧
    ∀ φ : ℝ → ℝ,
      foldedWindow (buildPrimeWindow (specFamily a m ha)) φ
        = foldedWindow (buildPrimeWindow (specFamily a m' ha)) φ :=
  ⟨rfl, fun _ => rfl⟩

/-- the auxiliary strictly increasing prime sequence (Euclid via
`Nat.exists_infinite_primes`) feeding the cofinality theorem. -/
noncomputable def primeSeq : ℕ → ℕ
  | 0 => 2
  | k + 1 => (Nat.exists_infinite_primes (primeSeq k + 1)).choose

theorem primeSeq_prime (k : ℕ) : (primeSeq k).Prime := by
  cases k with
  | zero => exact Nat.prime_two
  | succ k =>
      exact (Nat.exists_infinite_primes (primeSeq k + 1)).choose_spec.2

theorem primeSeq_strictMono : StrictMono primeSeq := by
  apply strictMono_nat_of_lt_succ
  intro k
  exact Nat.lt_of_succ_le
    (Nat.exists_infinite_primes (primeSeq k + 1)).choose_spec.1

/-- **STRUCTURE THEOREM 3 -- the family is cofinal** (r310; PROVED --
Euclid): for every requested atom count `N` there is an anchor whose
window (at every mesh level) carries at least `N` atoms.  Proof: `N`
distinct primes below the `N`-th member of `primeSeq` inject into the
atom set of the window anchored there. -/
theorem cofinal_prime_windows (N : ℕ) :
    ∃ (a : ℕ) (ha : IsPrimePow a), ∀ m : ℕ,
      N ≤ (specFamily a m ha).S := by
  refine ⟨primeSeq N, (primeSeq_prime N).prime.isPrimePow, fun m => ?_⟩
  have hmaps : ∀ i ∈ Finset.range N,
      primeSeq i ∈ windowAtoms (primeSeq N) := by
    intro i hi
    have hlt : primeSeq i < primeSeq N :=
      primeSeq_strictMono (Finset.mem_range.mp hi)
    have hself : primeSeq N ≤ primeSeq N ^ 2 :=
      Nat.le_self_pow two_ne_zero _
    exact Finset.mem_filter.mpr
      ⟨Finset.mem_range.mpr (by omega),
       (primeSeq_prime i).prime.isPrimePow⟩
  have hinj : Set.InjOn primeSeq (Finset.range N) :=
    Function.Injective.injOn primeSeq_strictMono.injective
  calc N = (Finset.range N).card := (Finset.card_range N).symm
    _ ≤ (windowAtoms (primeSeq N)).card :=
        Finset.card_le_card_of_injOn primeSeq hmaps hinj
    _ = (specFamily (primeSeq N) m
          ((primeSeq_prime N).prime.isPrimePow)).S := rfl

/-! ## THE MESH-vs-ANCHOR COFINALITY SEAM (r320, documentation --
the honest map, NO new statement forced)

The word "cofinal" names TWO DIFFERENT directions in this program, and
the seam between them was nowhere documented in rh/ before r320:

  * ANCHOR DIRECTION (this file, PROVED): `cofinal_prime_windows`
    says the predefined family is cofinal in ATOM COUNT -- for every
    `N` there is an anchor whose window carries at least `N` atoms
    (Euclid).  Orthogonally, at a FIXED anchor the mesh ladder
    refines: `mesh_refinement_shrinks` (strict shrinking; by
    Archimedes the mesh drops below every positive bound, which is
    what the r320 separation discipline of `RepresentsSpec` consumes).
    Both are statements about the WINDOW FAMILY.

  * MESH-REFINEMENT / CARRIER DIRECTION (hypothesis (H_cof),
    TfptCarrier/CofinalWeil.lean, v849): the carrier lane needs a
    PRE-FIXED strictly monotone index sequence along which the ladder
    MATRICES are PSD -- positivity data along a refinement tower, not
    atom-count growth.  `cofinal_prime_windows` does NOT supply this:
    it produces anchors, never PSD certificates, and its direction
    (more atoms) is not the (H_cof) direction (finer mesh along one
    pre-fixed tower).

  * THE OPEN SEAM (named Lean goal, not stated here): identify the
    mesh-refinement tower of `specFamily a m ha` (`m -> infinity` at
    fixed anchor) with the v749 canonical tower
    (`verification/v749_simpler_tower.py`, stages `n_k = 2^{2k+1}`,
    the 2-adic nesting on which the Schur recursion of v755 lives),
    and transport window positivity along it into the (H_cof) shape.
    Until that identification exists as a Lean statement, no theorem
    of this file feeds (H_cof), and none claims to.  NO RH CLAIM.

  * r326 UPDATE (the R325 extraction-order fork,
    `extraction_order_probe.py`, sealed, primary verdict
    ELEMENTWISE_STABILIZATION_GO): (H_cof) is REPLACED as the TARGET
    ROUTE of the extraction by the elementwise architecture of
    RH/Elementwise.lean -- per test element the finite forms
    stabilize at a PREDEFINED anchor onset and the element's OWN
    native mesh level (measured exact on the native class, S1), so
    the extraction consumes NO mesh-cofinal PSD tower and NO
    transport (`weil_nonneg_of_windowlocal`: one finite
    instantiation per element).  The R319 finding stands confirmed:
    the anchor direction alone cannot repair a mesh defect off the
    native class (the anchor-only floor, R325 S2.4) -- but the
    repair is a quantifier set, not a new mesh theory.  The carrier
    lane documentation above stays historically correct, and (H_cof)
    remains a correct statement of the OLD route; the open seam
    identification above is SUPERSEDED as a goal by the named
    statements of RH/Elementwise.lean (r376: remaining arch-channel
    stabilization sorry; pole PROVED; completion demoted to the
    named Prop SourceExactOfFamilyCompletion).  NO RH CLAIM. -/

/-! ## (c) Convergence to the Weil form (structure theorem 4) -/

/-- the finite comb-channel form of a window: `Σ_j Λ(p^k_j) f(log p^k_j)`
(the `mu` side of the finite Weil pairing; the full finite form is
comb minus arch). -/
noncomputable def PrimeWindow.combForm (w : PrimeWindow) (f : ℝ → ℝ) : ℝ :=
  ∑ j, w.combWeight j * f (w.nodes j)

/-- the prime side of the Weil explicit-formula pairing:
`Σ'_n Λ(n) f(log n)` (a tsum over ALL naturals; `Λ` vanishes off the
prime powers). -/
noncomputable def weilPrimeSide (f : ℝ → ℝ) : ℝ :=
  ∑' n : ℕ, Λ n * f (Real.log n)

/-- **STRUCTURE THEOREM 4 -- the finite forms converge to the Weil
prime side** (r310; PROVED in the strong stabilization form).  For a
test function vanishing above `b`, the finite comb forms of the
predefined family EQUAL the Weil prime-side sum for every anchor
`a ≥ max(1, ⌈exp b⌉)` -- pointwise convergence is realized as exact
stabilization, because the window rule eventually covers the support.

SCOPE (honest): this is the COMB channel of the Weil form.  The
archimedean channel (Python `arch_A`, an explicit integral kernel) is
the documented classical-analysis TODO of the file header; the
spectral/zero side of the full explicit formula is the arithmetically
open content of the program and is NOT stated here.  NO RH CLAIM. -/
theorem finite_forms_converge_to_weil (f : ℝ → ℝ) (b : ℝ)
    (hsupp : ∀ x, b < x → f x = 0) :
    ∃ A : ℕ, ∀ a (ha : IsPrimePow a) (m : ℕ), A ≤ a →
      (buildPrimeWindow (specFamily a m ha)).combForm f
        = weilPrimeSide f := by
  refine ⟨max 1 (Nat.ceil (Real.exp b)), fun a ha m haA => ?_⟩
  have ha1 : 1 ≤ a := le_trans (le_max_left _ _) haA
  have haexp : Real.exp b ≤ (a : ℝ) := by
    have hceil : (Nat.ceil (Real.exp b) : ℝ) ≤ (a : ℝ) := by
      exact_mod_cast le_trans (le_max_right _ _) haA
    exact le_trans (Nat.le_ceil _) hceil
  -- every contribution outside the atom set vanishes
  have hzero : ∀ n : ℕ, n ∉ windowAtoms a → Λ n * f (Real.log n) = 0 := by
    intro n hn
    by_cases hpp : IsPrimePow n
    · have hgt : a ^ 2 < n := by
        by_contra hle
        exact hn (Finset.mem_filter.mpr
          ⟨Finset.mem_range.mpr (by omega), hpp⟩)
      have ha1R : (1 : ℝ) ≤ (a : ℝ) := by exact_mod_cast ha1
      have hgtR : ((a : ℝ)) ^ 2 < (n : ℝ) := by exact_mod_cast hgt
      have hexp_lt : Real.exp b < (n : ℝ) := by nlinarith
      have hb : b < Real.log n := by
        have := Real.log_lt_log (Real.exp_pos b) hexp_lt
        simpa [Real.log_exp] using this
      rw [hsupp _ hb, mul_zero]
    · have hL : Λ n = 0 := by
        by_contra h
        exact hpp (ArithmeticFunction.vonMangoldt_ne_zero_iff.mp h)
      rw [hL, zero_mul]
  have htsum : weilPrimeSide f
      = ∑ n ∈ windowAtoms a, Λ n * f (Real.log n) :=
    tsum_eq_sum hzero
  have hform : (buildPrimeWindow (specFamily a m ha)).combForm f
      = ∑ n ∈ windowAtoms a, Λ n * f (Real.log n) := by
    rw [← Finset.sum_coe_sort (windowAtoms a)
      (fun n => Λ n * f (Real.log n))]
    exact Fintype.sum_equiv ((windowAtoms a).orderIsoOfFin rfl).toEquiv
      _ _ (fun j => rfl)
  rw [hform, htsum]

/-! ## (b) The rational certificate layer and the bridge -/

/-- **the mesh-level representation predicate** (r320 RETYPE -- the U1/U2
repair; pre-r320 form conserved as
`Counterexamples.OldRepresentsWindow`): the rational certificate window
`w` (RH/Window.lean structure; frozen v962/v963 exact-rational data)
represents the spec `s` when
  (1-3) its per-atom node, comb and arch data agree with the REAL
        source within one mesh width (the pre-r320 clauses -- the
        faithful transcription of the corpus convention: the frozen
        rationals are the builder-map images of the true `log p^k`
        comb, localized by the tent assembly to within the mesh,
        v563 `atom_lags_at`);
  (4)   u-FIDELITY (r320, per U1): the border column of `w` IS the
        spec's border data, exactly -- the spec field is free until the
        v958 transcription exists, so exact binding is satisfiable and
        says the certificate border is the spec border verbatim;
  (5)   B-FIDELITY (r320, per U1): the budget of `w` IS the spec's
        budget, exactly; with the new spec field `budget_pos` this
        closes the U1 hole (a represented window can no longer carry
        `B <= 0` against `TerminalPositive`);
  (6-7) the SEPARATION DISCIPLINE (r320, per U2): the tolerance must
        not destroy the source structure -- (6) it is strictly below
        HALF the minimal spec-node gap (so the rational nodes stay
        pairwise distinct: no total or partial node collision), and
        (7) strictly below every spec comb weight (so the rational
        comb masses stay strictly positive: no silently vanishing
        atom).  Both clauses together exclude every `p != 0` with
        `deg p < cap` that vanishes `mu`-almost-everywhere on the
        window -- the U2 witness class.
HONEST MESH-LEVEL-0 NOTE (the price of (6)/(7), documented as
demanded): at mesh level 0 the tolerance is the full half-window
`log(anchor)`, which generically VIOLATES (6) (e.g. anchor 2, atoms
{2,3,4}: `2 log 2 > log(4/3)`) -- coarse mesh levels represent
nothing; representation begins at sufficient refinement
(`mesh_refinement_shrinks` drives the mesh below every positive
bound, so the predicate is satisfiable -- witness below).
CERTIFICATE BOOKKEEPING ONLY: no positivity or margin statement is
transported across this predicate -- see the approximation warning at
`rational_window_approximates`. -/
def RepresentsSpec (w : VonMangoldtWindow) (s : PrimeWindowSpec) : Prop :=
  ∃ hS : w.S = s.S,
    (∀ j : Fin w.S,
      |((w.nodes j : ℚ) : ℝ) - s.node (Fin.cast hS j)| ≤ s.mesh) ∧
    (∀ j : Fin w.S,
      |((w.combWeight j : ℚ) : ℝ) - s.combWeight (Fin.cast hS j)| ≤ s.mesh) ∧
    (∀ j : Fin w.S,
      |((w.archWeight j : ℚ) : ℝ) - s.archWeight (Fin.cast hS j)| ≤ s.mesh) ∧
    (∀ k : ℕ, ((w.u k : ℚ) : ℝ) = s.border k) ∧
    ((w.B : ℚ) : ℝ) = s.budget ∧
    (∀ i j : Fin s.S, i ≠ j → 2 * s.mesh < |s.node i - s.node j|) ∧
    (∀ j : Fin s.S, s.mesh < s.combWeight j)

/-- rationals approximate any real within any positive bound
(density; the workhorse of the certificate layer). -/
theorem exists_rat_close (x : ℝ) {ε : ℝ} (hε : 0 < ε) :
    ∃ q : ℚ, |(q : ℝ) - x| < ε := by
  obtain ⟨q, hq1, hq2⟩ := exists_rat_btwn (sub_lt_self x hε)
  exact ⟨q, abs_sub_lt_iff.mpr ⟨by linarith, by linarith⟩⟩

/-- **the rational certificate window approximates the real one**
(r310; PROVED).  For every prime window spec and every positive bound
`ε` there are rational node and comb-weight vectors within `ε` of the
exact real source data -- the existence half of the certificate
convention; the frozen v962/v963 windows instantiate it with
`ε = mesh` (that instantiation is `RepresentsSpec`, definitional).

⚠ APPROXIMATION WARNING (r310b, reviewer plan section 8, adjudicated
verbatim): "Weil die L*-Marge schrumpft, wäre eine Beweiskette 'reelle
Quelle nahe rationaler Quelle' gefährlich, solange der
Approximationsfehler nicht mit der Marge mithält.  Besser ist die
direkte reelle Konstruktion."  Concretely: the rational windows are
CERTIFICATE OBJECTS, not the definition -- the definition is the
direct real construction `buildPrimeWindow`.  The measured L* margin
SHRINKS along the ladder (1.68e-4 → 1.806e-8, v964), so a proof chain
of the shape "real source ≈ rational source, hence positivity
transfers" would be UNSOUND unless the approximation error is
controlled uniformly BELOW the margin -- which is NOT established, and
this theorem does NOT claim it: it gives existence for each fixed
`ε > 0` with no coupling between `ε` and any margin.  No statement of
this file uses approximation as a proof path; the intended route for
any future positivity argument is the direct real construction. -/
theorem rational_window_approximates (s : PrimeWindowSpec) {ε : ℝ}
    (hε : 0 < ε) :
    ∃ (qn qc : Fin s.S → ℚ),
      (∀ j, |(qn j : ℝ) - s.node j| < ε) ∧
      (∀ j, |(qc j : ℝ) - s.combWeight j| < ε) := by
  choose qn hqn using fun j => exists_rat_close (s.node j) hε
  choose qc hqc using fun j => exists_rat_close (s.combWeight j) hε
  exact ⟨qn, qc, hqn, hqc⟩

/-- **the window-level representation predicate** (r310b, reviewer
target form; r320 RETYPE -- see `RepresentsSpec` for the clause-by-
clause rationale, U1/U2 repair): the rational certificate window `w`
represents the REAL window `v` within per-atom tolerance `δ` on the
node/comb/arch channels, EXACTLY on the border/budget channels
(u/B-fidelity, clauses 4/5), with the separation discipline on the
tolerance (clauses 6/7: `2δ` below every node gap of `v`, `δ` below
every comb weight of `v`).  `RepresentsSpec w s` is definitionally
`RepresentsWindow w (buildPrimeWindow s) s.mesh`
(`representsSpec_iff`) -- the spec-level predicate was already the
built-window predicate in disguise; this form makes the reviewer's
target semantics ("built from a prime source") syntactically explicit.
CERTIFICATE BOOKKEEPING ONLY (see `rational_window_approximates`).
r397: this is a CERTIFICATE over a `RealCanonicalWindow` (via
`W.toPrimeWindow`), not a domain predicate.  The domain is the
constructed real window (`RH/Selected.lean`). -/
def RepresentsWindow (w : VonMangoldtWindow) (v : PrimeWindow)
    (δ : ℝ) : Prop :=
  ∃ hS : w.S = v.S,
    (∀ j : Fin w.S,
      |((w.nodes j : ℚ) : ℝ) - v.nodes (Fin.cast hS j)| ≤ δ) ∧
    (∀ j : Fin w.S,
      |((w.combWeight j : ℚ) : ℝ) - v.combWeight (Fin.cast hS j)| ≤ δ) ∧
    (∀ j : Fin w.S,
      |((w.archWeight j : ℚ) : ℝ) - v.archWeight (Fin.cast hS j)| ≤ δ) ∧
    (∀ k : ℕ, ((w.u k : ℚ) : ℝ) = v.u k) ∧
    ((w.B : ℚ) : ℝ) = v.B ∧
    (∀ i j : Fin v.S, i ≠ j → 2 * δ < |v.nodes i - v.nodes j|) ∧
    (∀ j : Fin v.S, δ < v.combWeight j)

/-- the spec-level and window-level representation predicates coincide
definitionally (nodes/weights of `buildPrimeWindow s` ARE the derived
spec data -- `buildPrimeWindow_source_exact`). -/
theorem representsSpec_iff (w : VonMangoldtWindow)
    (s : PrimeWindowSpec) :
    RepresentsSpec w s ↔ RepresentsWindow w (buildPrimeWindow s) s.mesh :=
  Iff.rfl

/-- **the source-exactness predicate** (r320; deliberately `opaque`,
the r273 `MainWindow` convention applied to the SPEC side).

INTENDED CONTENT (what it must eventually say -- exactly the r310b
"not yet captured" list of the old bridge docstring): the spec's
`archWeight` is the exact archimedean Weil-kernel transcription
(`arch_A` -- classical analysis, the documented TODO of the file
header), its `border` is the v958 border column OF THAT COMB, and its
`budget` satisfies the full r243 drain-sum identity
`B = S_{N-2} + 5/7` (the positivity half is already the transcribable
spec field `budget_pos`).

WHY IT MUST BE OPAQUE (r320 verification finding, beyond the R319
audit): `archWeight` and `border` are FREE spec fields until their
transcriptions exist.  An iff-bridge quantifying over free
arch/border data manufactures `MainWindow` witnesses with arbitrary
arch mass (contradicting `lstar_subordination` at `p = 1` -- the same
disease as U2, one channel over) and arbitrary border columns
(contradicting the retyped `pair_margin_main` -- the same disease as
U3).  The fidelity/separation clauses of `RepresentsWindow` cannot
close these channels, because they bind `w` to the SPEC, not the spec
to the SOURCE.  `SourceExact` reserves exactly that missing binding,
the way `MainWindow` reserves the window-side content; eliminating it
= the named arch/border/fold transcription TODO. -/
opaque SourceExact : PrimeWindowSpec → Prop

/-- **THE OPACITY BRIDGE, reviewer target form** (r310b; r320 RETYPE
per the R319 audit U1-U3 -- the ONE documented `sorry` of this file;
census unchanged; the pre-r320 statement TYPE is conserved and
machine-refuted in `RH/Counterexamples.lean`,
`old_bridge_terminal_inconsistent` / `old_bridge_lstar_inconsistent`).

A rational certificate window is MAIN (in the sense of the opaque r273
predicate) iff it mesh-represents a window BUILT FROM A SOURCE-EXACT
PRIME SOURCE -- the reviewer's target semantics, with the r320
repairs: u/B-fidelity and the separation discipline inside
`RepresentsWindow` (U1/U2), and the opaque `SourceExact` guarding the
not-yet-transcribed arch/border/budget-identity channels (the r320
verification finding above).

SORRY TYPE: DEFINITIONAL/TECHNICAL -- NOT arithmetic.  `MainWindow` is
`opaque` BY DESIGN (r273: its content was the open problem); no
statement about an opaque constant is provable or refutable inside the
library, so this bridge cannot be discharged without replacing the
opaque predicates themselves.  The bridge is the honest NEW INTERFACE:
the forward direction says the opaque marker never certifies anything
that is not the faithful mesh-certificate of an explicitly built,
source-exact prime window; the backward direction says the explicit
construction is what MAIN always meant.

DOCSTRING CORRECTION (r320, per the R319 audit): the pre-r320 promise
"when a future wave replaces `MainWindow` by the RHS, this `sorry`
becomes `Iff.rfl`" was WRONG twice over -- (i) with the OLD
`RepresentsWindow` that invasive route would have made the library
outright inconsistent (U1-U3: the RHS admitted windows refuting
`terminal_positive_main`, `lstar_subordination` and
`pair_margin_main`; kernel-checked guards in Counterexamples.lean),
and (ii) even with the NEW predicate the route first requires
eliminating `SourceExact` (the arch/border transcription).  The honest
statement: under the invasive route AFTER the transcriptions, the
bridge becomes definitional; until then it is the interface and stays
a typed `sorry`.

Fold fidelity stays documented and NOT captured (the corpus
certificate windows are FOLDED objects; tying them to
`foldedWindow (buildPrimeWindow s) φ_corpus` needs the fold-map
transcription -- see the stage-3 section); it is part of the intended
content of `SourceExact`'s elimination.  NO RH CLAIM. -/
theorem mainWindow_iff_builtFromPrimeSource (w : VonMangoldtWindow) :
    MainWindow w ↔ ∃ s : PrimeWindowSpec, SourceExact s ∧
      RepresentsWindow w (buildPrimeWindow s) s.mesh := by
  sorry

/-- **the r310 bridge form** -- a PROVED corollary of the target form
(r310b; r320: carries the same retype, `SourceExact` conjunct and the
retyped `RepresentsSpec`): the `sorry` lives in
`mainWindow_iff_builtFromPrimeSource`; this statement does not carry
its own hole. -/
theorem mainWindow_explicit_bridge (w : VonMangoldtWindow) :
    MainWindow w ↔ ∃ s : PrimeWindowSpec, SourceExact s ∧
      RepresentsSpec w s := by
  rw [mainWindow_iff_builtFromPrimeSource]
  exact exists_congr fun s =>
    and_congr_right fun _ => (representsSpec_iff w s).symm

/-! ## THE NONEMPTINESS WITNESS (r320, repair 4)

The smallest full corpus window: anchor 2, atom set
`windowAtoms 2 = {2, 3, 4}` (all prime powers `<= 4`), mesh level 4
(mesh = `log 2 / 5` -- the first level at which the r320 separation
discipline is satisfiable on this atom set: `2 log 2 / 5 < log(4/3)`
iff `2^7 < 3^5`, i.e. `128 < 243`), with an exact-rational certificate
window in the v962/v963 convention (nodes `7/10, 11/10, 139/100` and
comb masses `7/10, 11/10, 7/10` within one mesh of the true
`log 2, log 3, 2 log 2` and `Λ = log 2, log 3, log 2`).

HONEST FORM STATEMENT (which nonemptiness is provable, documented as
demanded): `∃ w, MainWindow w` is NOT provable and not stated --
`MainWindow` is `opaque` (r273), and the bridge RHS carries the opaque
`SourceExact` guard, so even bridge-mediated nonemptiness is
unprovable BY DESIGN (that unprovability is exactly what blocks the
U1-U3 adversarial constructions).  What IS proved:
  * `witness_represents` -- the retyped `RepresentsWindow` (all seven
    clauses, incl. u/B-fidelity and the separation discipline) is
    SATISFIABLE on a genuine built prime window: the r320 clauses do
    not empty the predicate;
  * `mainWindowExplicit_nonempty` -- the explicit real predicate has a
    witness (trivial by construction, stated for the record). -/

/-- the witness spec: anchor 2, atoms `{2, 3, 4}` (as `j + 2`),
mesh level 4, placeholder arch/border, budget = the r243 floor. -/
noncomputable def witnessSpec : PrimeWindowSpec where
  S := 3
  primePowers := fun j => (j : ℕ) + 2
  pp_isPrimePow := by
    intro j
    fin_cases j
    · exact Nat.prime_two.prime.isPrimePow
    · exact Nat.prime_three.prime.isPrimePow
    · exact ⟨2, 2, Nat.prime_two.prime, two_pos, by norm_num⟩
  pp_strictMono := by
    intro i j hij
    simpa using Nat.add_lt_add_right (Fin.lt_def.mp hij) 2
  anchor := 2
  anchor_isPrimePow := Nat.prime_two.prime.isPrimePow
  meshLevel := 4
  pp_le := by intro j; have := j.isLt; simp; omega
  archWeight := fun _ => 0
  arch_nonneg := fun _ => le_refl 0
  border := fun _ => 0
  budget := 5 / 7
  budget_pos := by norm_num

/-- the exact-rational certificate window of the witness spec
(v962/v963 convention: exact rationals throughout). -/
def witnessWindow : VonMangoldtWindow where
  S := 3
  nodes := ![7/10, 11/10, 139/100]
  combWeight := ![7/10, 11/10, 7/10]
  archWeight := fun _ => 0
  comb_nonneg := by intro j; fin_cases j <;> norm_num
  arch_nonneg := fun _ => le_refl 0
  lo := 0
  hi := 2
  window_rule := by intro j; fin_cases j <;> norm_num
  u := fun _ => 0
  B := 5 / 7

theorem witnessSpec_mesh : witnessSpec.mesh = Real.log 2 / 5 := by
  simp [PrimeWindowSpec.mesh, PrimeWindowSpec.alpha, witnessSpec]
  norm_num

/-- `3 log 2 < 2 log 3` (i.e. `log 8 < log 9`) -- the lower separation
input. -/
theorem witness_log89 : 3 * Real.log 2 < 2 * Real.log 3 := by
  have h : Real.log 8 < Real.log 9 :=
    Real.log_lt_log (by norm_num) (by norm_num)
  rw [show (8 : ℝ) = 2 ^ 3 by norm_num, show (9 : ℝ) = 3 ^ 2 by norm_num,
    Real.log_pow, Real.log_pow] at h
  push_cast at h
  linarith

/-- `5 log 3 < 8 log 2` (i.e. `log 243 < log 256`) -- the upper
separation input. -/
theorem witness_log243 : 5 * Real.log 3 < 8 * Real.log 2 := by
  have h : Real.log 243 < Real.log 256 :=
    Real.log_lt_log (by norm_num) (by norm_num)
  rw [show (243 : ℝ) = 3 ^ 5 by norm_num,
    show (256 : ℝ) = 2 ^ 8 by norm_num,
    Real.log_pow, Real.log_pow] at h
  push_cast at h
  linarith

theorem witness_log4 : Real.log 4 = 2 * Real.log 2 := by
  rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
  push_cast
  ring

/-- **the witness theorem** (r320): the retyped representation
predicate is satisfiable on a genuine built prime window -- all seven
clauses proved (d9 log-2 bounds + the exact-exponent inequalities
`2^7 < 3^5` and `3^5 < 2^8`). -/
theorem witness_represents :
    RepresentsWindow witnessWindow (buildPrimeWindow witnessSpec)
      witnessSpec.mesh := by
  have h2 := Real.log_two_gt_d9
  have h2' := Real.log_two_lt_d9
  have h89 := witness_log89
  have h243 := witness_log243
  refine ⟨rfl, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · -- nodes within one mesh
    intro j
    rw [witnessSpec_mesh]
    fin_cases j
    · show |((7/10 : ℚ) : ℝ) - Real.log ((2 : ℕ) : ℝ)| ≤ Real.log 2 / 5
      rw [abs_le]
      constructor <;> push_cast <;> linarith
    · show |((11/10 : ℚ) : ℝ) - Real.log ((3 : ℕ) : ℝ)| ≤ Real.log 2 / 5
      rw [abs_le]
      constructor <;> push_cast <;> linarith
    · show |((139/100 : ℚ) : ℝ) - Real.log ((4 : ℕ) : ℝ)| ≤ Real.log 2 / 5
      have h4 := witness_log4
      rw [abs_le]
      constructor <;> push_cast <;> linarith
  · -- comb weights within one mesh
    intro j
    rw [witnessSpec_mesh]
    fin_cases j
    · show |((7/10 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 2|
        ≤ Real.log 2 / 5
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two,
        abs_le]
      constructor <;> push_cast <;> linarith
    · show |((11/10 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 3|
        ≤ Real.log 2 / 5
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_three,
        abs_le]
      constructor <;> push_cast <;> linarith
    · show |((7/10 : ℚ) : ℝ) - ArithmeticFunction.vonMangoldt 4|
        ≤ Real.log 2 / 5
      have hL4 : ArithmeticFunction.vonMangoldt 4
          = Real.log ((2 : ℕ) : ℝ) := by
        show ArithmeticFunction.vonMangoldt (2 ^ 2)
          = Real.log ((2 : ℕ) : ℝ)
        rw [ArithmeticFunction.vonMangoldt_apply_pow (by norm_num),
          ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
      rw [hL4, abs_le]
      constructor <;> push_cast <;> linarith
  · -- arch weights within one mesh (both sides zero)
    intro j
    rw [witnessSpec_mesh]
    show |((0 : ℚ) : ℝ) - 0| ≤ Real.log 2 / 5
    push_cast
    rw [sub_zero, abs_zero]
    linarith
  · -- u-fidelity (exact)
    intro k
    show ((0 : ℚ) : ℝ) = 0
    norm_num
  · -- B-fidelity (exact)
    show ((5/7 : ℚ) : ℝ) = 5 / 7
    norm_num
  · -- separation clause: 2 mesh below every node gap
    intro i j hij
    rw [witnessSpec_mesh]
    have h4 := witness_log4
    fin_cases i <;> fin_cases j
    · exact absurd rfl hij
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((2 : ℕ) : ℝ) - Real.log ((3 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (neg_le_abs _)
      push_cast
      linarith
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((2 : ℕ) : ℝ) - Real.log ((4 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (neg_le_abs _)
      push_cast
      linarith
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((3 : ℕ) : ℝ) - Real.log ((2 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (le_abs_self _)
      push_cast
      linarith
    · exact absurd rfl hij
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((3 : ℕ) : ℝ) - Real.log ((4 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (neg_le_abs _)
      push_cast
      linarith
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((4 : ℕ) : ℝ) - Real.log ((2 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (le_abs_self _)
      push_cast
      linarith
    · show 2 * (Real.log 2 / 5)
        < |Real.log ((4 : ℕ) : ℝ) - Real.log ((3 : ℕ) : ℝ)|
      refine lt_of_lt_of_le ?_ (le_abs_self _)
      push_cast
      linarith
    · exact absurd rfl hij
  · -- comb-positivity clause: mesh below every comb weight
    intro j
    rw [witnessSpec_mesh]
    fin_cases j
    · show Real.log 2 / 5 < ArithmeticFunction.vonMangoldt 2
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
      push_cast
      linarith
    · show Real.log 2 / 5 < ArithmeticFunction.vonMangoldt 3
      rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_three]
      push_cast
      linarith
    · show Real.log 2 / 5 < ArithmeticFunction.vonMangoldt 4
      have hL4 : ArithmeticFunction.vonMangoldt 4
          = Real.log ((2 : ℕ) : ℝ) := by
        show ArithmeticFunction.vonMangoldt (2 ^ 2)
          = Real.log ((2 : ℕ) : ℝ)
        rw [ArithmeticFunction.vonMangoldt_apply_pow (by norm_num),
          ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
      rw [hL4]
      push_cast
      linarith

/-- the retyped representation predicate is nonempty -- the r320
clauses do not empty the certificate layer. -/
theorem representsWindow_nonempty :
    ∃ (w : VonMangoldtWindow) (s : PrimeWindowSpec),
      RepresentsWindow w (buildPrimeWindow s) s.mesh :=
  ⟨witnessWindow, witnessSpec, witness_represents⟩

/-- the explicit real predicate has a witness (by construction; stated
for the record -- see the section header for why `∃ w, MainWindow w`
itself is deliberately NOT provable). -/
theorem mainWindowExplicit_nonempty : ∃ v, MainWindowExplicit v :=
  ⟨buildPrimeWindow witnessSpec, witnessSpec, rfl⟩

end RH
