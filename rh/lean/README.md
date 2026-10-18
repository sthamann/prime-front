# rh/lean — the RH-program Lean 4 formalization pilot

> **Claim boundary.** Research documentation. NOT evidence for or against
> the Riemann Hypothesis in either direction. NO RH CLAIM. The `sorry`
> declarations below are **honest markers**. Since block C1 (the
> reviewer final-domain contract — see the C1 block below) there were
> exactly **seven**; **r362 DualResolvent** added the ONE named
> transcription `augmentedSubordination_iff_dualResolvent` (census
> **eight**); **r373** proves that bridge and the Haynsworth two-rank /
> mixed inertia theorems, census **seven**; **r376** proves the pole
> stabilization and demotes the source-exact completion to a named
> Prop, census **five**; **r380** kernel-anchors the five DCCXXXVII
> pivot-coordinate lemmas (`RH/PivotCoordinate.lean`) with **zero new
> `sorry`** (proved faces + named Props for Borodin/DPP remainder);
> **r384** kernel-anchors the r382 entry lemma (`RH/FlankEntry.lean`)
> with **zero new `sorry`** (proved finite algebra + named Props
> `FlankEntryPrefix` / `ChristoffelPivotBound`);
> **r397** constructs the exact real domain and the selected
> sequence (`RH/Selected.lean`) with **zero new `sorry`**:
> `lstar_canonical` / `terminal_q_canonical` are DEGRADED to the
> alternative (rational-certificate) route; the r397 named Prop
> `selected_augDualResolvent_gt_half` is the stronger (`∀ᶠ`, `PosDef`)
> alternative. Census stays **five**.
> **r406** proves the general one-defect absorption theorems
> (`RH/OneDefect.lean`) with **zero new `sorry`** (finite real
> matrix algebra; independent of source-side R404/R405). Census
> stays **five**.
> **r412** kernel-anchors the r407/r409/r411 graph-resolvent
> dictionaries (`RH/GraphResolvent.lean`) with **zero new `sorry`**
> (spectral bridge, Möbius inertia, energy-split contraction,
> zero-defect R† lift proved; named Prop
> `GraphResolventIsLEnsembleInv`). Census stays **five**.
> **r426** kernel-anchors the r417–r425 edge-balance chain
> (`RH/EdgeBalance.lean`) with **zero new `sorry`**
> (Woodbury-sch corollary of OneDefect, 3×3 chart trichotomy,
> vacuous τ²-separator, den formula and γ-bridge proved; named
> Props `BorderIsMuParseval` / `BorderLoewnerLeS` / `QNLtOne`).
> Census stays **five**.
> **r430** kernel-anchors the reviewer quantifier correction
> (`RH/FrequentlySelected.lean`) with **zero new `sorry`**:
> Loewner face `Rdagger_ge_half_iff_augmented_posSemidef`,
> FREQ extraction `weil_nonneg_of_frequently_selected` /
> `internal_weil_nonneg_of_frequently_selected` (arch sorry consumed, not new),
> density corollary and mean-value trick proved; the new mincut
> is `frequently_selected_augDualResolvent_ge_half`. Census
> stays **five**.
> **r434** audits the mincut path (`PRIME.RH.QUANTIFIER_MINCUT_AUDIT.01`):
> `lstar_canonical` / `terminal_q_canonical` /
> `pair_terminal_dictionary` / `mainWindow_iff_builtFromPrimeSource`
> are OFF the FREQ RH-path (kept as the alternative
> rational-certificate route).  The L† ⟺ R† identification on
> the real window is PROVED
> (`masterCap_posSemidef_iff_Rdagger_ge_half`);
> `SelectedSemidefImpliesPlainReads` is a theorem of the thinner
> remainder `SelectedACapPsdImpliesPlainReads` (Hankel/`fullRead`,
> not the dual-resolvent cone).  Zero new `sorry`; census stays
> **five**.
> The FREQ mincut path consumes only
> `frequently_selected_augDualResolvent_ge_half` (named) +
> `SelectedReadQuadraticRepresentation` (named; r464 exact channel
> seam, with its finite PSD consequence proved) +
> `arch_gauss_mellin_digamma_identity` (sorry, classical).  The
> **two true arithmetic gaps** remain as the alternative route:
> `lstar_canonical` (lemma L*, the base/wall hole)
> and `terminal_q_canonical` (the terminal cross-ratio, the
> border/fiber hole), both `RH/Canonical.lean`; plus the ONE named r263
> dictionary import `pair_terminal_dictionary` (measured exact,
> transcription-blocked), the r310/r320 opacity bridge
> (`RH/Source.lean`, definitional/technical — outside the load-bearing
> chain since C1; Alt-Last, not a hole), the remaining r326 Level-C
> classical statement `arch_elementwise_stabilization`
> (`RH/Elementwise.lean`; pole PROVED, completion a named Prop), and
> the r362/r373 window↔matrix dictionary
> (`RH/DualResolvent.lean`, **PROVED** as μ-ONB whitening). The Jacobi
> inertia theorem
> `crossing_budget` is PROVED since C1 (`RH/Inertia.lean`,
> sorry-free); Haynsworth additivity is PROVED since r373
> (`RH/Haynsworth.lean`, sorry-free); the former master-theorem `sorry`, the wave-5 fog-free
> form `free_window_positivity` and the pair closure
> `pair_closes_main` are PROVED as corollaries. Historical narrative
> (r305 four / r310 five / r326 eight / C1 seven / r376 five / r380 five / r384 five / r397 five / r406 five / r412 five / r426 five) in the blocks below.
>
> **r463 fidelity repair:** `RH/FaithfulFold.lean` replaces the
> selected raw-atom cosine fold by the production pipeline
> (tent lags, `L=2(m+1)-2`, circulant spectral density, grid fold,
> sign split). Exported k=5/9/10 pins agree with the Python builder.
> `archRead` is now a concrete lag pairing; only its coefficient
> values remain external. The endpoint is renamed
> `internal_weil_nonneg_of_frequently_selected`, and
> `FrequentlySelectedInternalMincut` exposes
> `SelectedACapPsdImpliesPlainReads` as an axiom candidate.
> `RH/ExternalBridges.lean` adds three honest `sorry`s: dense
> extension, standard explicit-formula identification, and Mathlib
> `RiemannHypothesis`. Census **5 → 8**. NO RH CLAIM.
>
> **r464 inner bridges:** `RH/InnerBridges.lean` proves the finite
> PSD half
> `selectedACapPsdImpliesPlainReads_of_representation`; the exact
> remaining channel seam is the named Prop
> `SelectedReadQuadraticRepresentation`.  The original target is not
> weakened: `GridElement.steps` remains unbounded, while only
> `meshExp` is guarded.  `productionArchLag` is now the concrete
> regularized near-cell/far-cell Gauss tent integral.  The former
> generic arch stabilization `sorry` is replaced one-for-one by
> `arch_gauss_mellin_digamma_identity`, matching Mathlib's explicit
> Gauss-integral TODO.  Census **8 → 8**. NO RH CLAIM.
>
> **Classical-rate audit:** `RH/SelectedArchErrorQuadraticRateClassical.lean`
> fixed-constant Prop FALSIFIED (`8.0283458222 > 4.1259765625`,
> small-support regime, kink defect `-θ(1-θ)/2` proved); the ∃C
> interface `SelectedArchErrorQuadraticRateExists` is proved
> CONDITIONALLY on the still-open
> `SelectedArchWeightedInterpolationEstimate` (theorem
> `selectedArchErrorQuadraticRateExists_of_weightedInterpolationEstimate`);
> the downstream convergence
> `selectedArchError_tendsto_zero_of_rateExists` is proved
> unconditionally from the ∃C form. Six theorems proved. NO RH CLAIM.
>
> **r487 outer bridges:** `RH/ExternalBridges.lean` types
> `FullWeilTest` as a continuous even fixed-support real
> autocorrelation.  The dense extension is split into the two exact
> bricks `fullWeil_fixedSupport_grid_density` and
> `fullWeil_channel_continuity`; form-limit positivity and the
> `grid_dense_extension` wrapper are proved.  The Mathlib interface
> `standard_weil_criterion_to_mathlib_rh_of_separation` is proved
> directly against `riemannZeta`; its remaining classical brick is
> `fullWeil_separates_offCritical_zeros`.  No `ZetaZero` enumeration
> exists in the installed Mathlib tag.  Mellin transform, inversion,
> and Mellin-to-Dirichlet infrastructure do exist; a Guinand--Weil
> explicit formula does not.
> The old density `sorry` split in two, so census **8 → 9**.
> NO RH CLAIM.
>
> **r489 outer bridges 2:** the fixed-support topology is strengthened
> to uniform convergence plus `L¹`, and the autocorrelation witness is
> compactly supported in `L²`.  `fullWeilCombSide_tendsto` and
> `fullWeilPoleIntegral_tendsto` are proved.  The existing r376
> native-grid pole/integral dictionary, dyadic `L²` step density, and
> r475 u-space arch continuity are separately named components of the
> sole dense remainder `FullWeilFixedSupportCompletion`.  Public grid
> density, channel continuity and positivity transfer are derived from
> that one package.  Census **9 → 8**. NO RH CLAIM.
>
> **r491 outer bridges 3 — HIDDEN GAP FOUND / REDUCED:** r489's
> completion has three components, not two: dyadic convergence, arch
> continuity, and pole identification.  The polar sign is corrected to
> `+2 cosh(u/2)`.  `fullWeilArchSide` is now concrete.  The witness has
> explicit Lipschitz and support-length contracts; `dyadicSampleGrid`
> is an explicit left-sampled dyadic sequence with a proved support
> bound.  Its remaining convergence is
> `FullWeilDyadicSampleConvergence`.  The pole seam is narrowed to
> `GridPoleHatIntegralIdentity`, whose implication to the sequence
> dictionary is proved.  Census **8 → 8**. NO RH CLAIM.
>
> **r638L claim-boundary repair (current census):** the overstrong
> `arch_gauss_mellin_digamma_identity` exact-quadrature theorem and the
> gauge-mismatched `standard_explicit_formula_identification` theorem
> are retired. Their Props remain unasserted; historical arch
> extraction theorems now take `ArchGaussMellinDigammaIdentity`
> explicitly. `standard_explicit_formula_identification_honest`
> remains proved. Full `lake build RH`: 3578 jobs, **five** intentional
> `sorry`s, no errors. NO RH CLAIM.
>
> **r320 (the R319 red-team repair).** The R319 audit found the r310b
> statement TYPES of the source interface jointly INCONSISTENT (U1: the
> bridge never bound `u`/`B` vs `terminal_positive_main`; U2: mesh-width
> tolerance admitted total node collision vs `lstar_subordination`; U3:
> `pair_margin_main` quantified `(Zloc, runs)` freely vs any main
> window). All three were kernel-reproduced and repaired in r320:
> retyped `RepresentsWindow`/`RepresentsSpec` (u/B-fidelity + separation
> discipline), the opaque `SourceExact` guard for the free arch/border
> spec channels (an r320 verification finding BEYOND the audit), the
> canonical `(Zloc, runs)` extraction as a definition, the three old
> types conserved and machine-refuted as permanent guards
> (`RH/Counterexamples.lean`), and an explicit satisfiability witness.
> The census is UNCHANGED at 5; `lstar_subordination`,
> `terminal_positive_main` and `crossing_budget` are byte-identical.
>
> **r326 (the R325 elementwise extraction architecture).** The R325
> extraction-repair fork (`extraction_order_probe.py`, sealed, primary
> verdict `ELEMENTWISE_STABILIZATION_GO`) adjudicated the repair of the
> missing Level-C layer (window-local positivity ⟹ Weil form): the
> ELEMENTWISE quantifier set, no mesh-cofinal ladder, no transport, no
> (H_cof). r326 implements it (`RH/Elementwise.lean`): the canonical
> window predicate `CanonicalPrimeWindow`, the PROVED construction
> theorem `sourceExact_buildPrimeWindow` (the wave-12 reviewer target —
> `SourceExact` is ELIMINATED as a free assumption from the extraction
> route), the native dense class `GridElement` built for real, the
> comb-channel elementwise stabilization PROVED with the onset
> predefined from the element, and the ladder-free extraction
> `weil_nonneg_of_windowlocal` PROVED as a finite instantiation.
> Census 5 → **8**: three NEW typed statements that were NOT
> formalizable before this round (the wave-12 reservation "the Level-C
> distance appears in no `sorry`" is thereby partially discharged — the
> distance is now named): the arch/pole kernel-channel stabilizations
> (classical, S2) and the source-exact completion (classical +
> opacity-forced). The five pre-existing sorrys are byte-identical.
>
> **r332 (the augmented subordination L†, the reviewer unification).**
> `RH/Augmented.lean` packages L* and the terminal statement as the
> distributed and the rank-one part of ONE strict sampling inequality,
> (L†): `0 < B_w` and `∫p²dν_w + |ℓ_w(p)|²/B_w < ∫p²dμ_w` for every
> `p ≠ 0` below the half-filling cap (`ℓ_w(p) = u_wᵀc` the border
> readout). The module is **sorry-free** ("closes without new
> arithmetic"): L† ⟺ `A_{w,n} ≻ 0` through the cap
> (`augmentedSubordination_iff_masterCap` — quadratic completion, test
> vector `(c, −ℓ(p)/B)`), L† ⟺ L* ∧ Terminal
> (`augmentedSubordination_iff_lstar_and_terminal` — the terminal
> direction through the determinant extraction instead of the `H⁻¹u`
> minimizer; the backward direction re-runs the wave-10 bricks so the
> corollary is non-circular), the r305 reconstruction theorem
> re-derived as a corollary (`reconstruction_via_augmented`; the
> Closure original is byte-stable, NOT replaced), and the combined
> target form on MAIN windows PROVED from the two existing holes
> (`augmentedSubordination_main` — deliberately NOT a new `sorry`: L†
> is the common target form of `lstar_subordination` +
> `terminal_positive_main`, not a third hole). Census unchanged:
> 8 → **8**, zero new; the two true holes are byte-identical.
>
> **C1 (the reviewer final-domain block: "reduce the Lean graph to the
> two true mathematical gaps").** Four moves, census 8 → **7**:
> (1) **the final-domain retype** — the two true holes are RETYPED off
> the opaque `MainWindow` onto the canonical construction
> (`RH/Canonical.lean`): `CanonicalWindow w := ∃ a m ha,
> RepresentsWindow w (canonicalWindow a m ha) mesh`, where
> `canonicalWindow` is the predefined family completed by the ONE named
> opaque constant `canonicalCompletion` (the r326 opacity convention
> extended from the kernel reads to the window-level arch/border/budget
> data — the residual opacity is exactly the classical transcription
> TODO). The holes are now `lstar_canonical` and `terminal_q_canonical`
> — the budget half `0 < B` of the old terminal statement is PROVED
> (`canonical_budget_pos`), so the terminal sorry carries only the
> genuinely open `q_N < 1`. The master theorem and all corollaries
> moved with them (statements verbatim modulo the domain); no free
> `SourceExact` and no `MainWindow` bridge appears in the final chain.
> (2) **the pair duplicate retired** — the r263 dictionary
> `Z² = (5/7)·q_N` is the ONE named lemma `pair_terminal_dictionary`
> (typed MEASURED/transcription-blocked), the pair closure
> `pair_closes_main` is a PROVED corollary of the terminal hole, and
> the margin law `pair_margin_main` is DEMOTED to the named Prop
> `PairBound.PairMarginLaw` (honest: the fixed pair form is measured
> to MISS on kz39/kz15 — asserting it as a sorry overclaimed).
> (3) **`crossing_budget` PROVED** — the r305 "mathlib carries neither"
> assessment was half stale: mathlib v4.29.1 has Sylvester's law of
> inertia (`QuadraticForm.sigNeg_of_equiv_weightedSumSquares`); the
> pivot/minor dictionary (Jacobi's rule as an LDL congruence +
> Vandermonde factorization) is built in `RH/Inertia.lean`, which is
> now **sorry-free**. (4) **the axiom audit** — `RH/Audit.lean` runs
> `#print axioms` on the whole chain at every build; results below.
>
> **Current asserting-`sorry` table (r638L census 5; historical path:
> C1 7, r362 8, r373 7, r376 5, outer/Gabor work 7, r638L 5):**
>
> | `sorry` | File | Type |
> |---|---|---|
> | `lstar_canonical` | `RH/Canonical.lean` | arithmetically open (the base/wall hole, lemma L*); **C1 RETYPE** of `lstar_subordination`; **r397 DEGRADED** to conjecture / alternative route; **r434 OFF the FREQ mincut path** |
> | `terminal_q_canonical` | `RH/Canonical.lean` | arithmetically open (the border/fiber hole); **C1 RETYPE + SHARPENING**; **r397 DEGRADED** to conjecture / alternative route; **r434 OFF the FREQ mincut path** (direct Selected-R† semidefiniteness bypasses `∀ CanonicalWindow, q_N < 1`) |
> | `pair_terminal_dictionary` | `RH/Canonical.lean` | **C1, replaces the `pair_margin_main` sorry** — the r263 dictionary `Z² = (5/7)·q_N` as ONE named lemma; type MEASURED DICTIONARY (42/42 exact) / transcription-blocked (the border orthopoly transform); consumed only by the pair closure corollary, never by the master chain; **r434 OFF the FREQ mincut path** |
> | `mainWindow_iff_builtFromPrimeSource` | `RH/Source.lean` | definitional/technical (opacity-forced, r320 form); **Alt-Last since C1** (outside the load-bearing chain: `CanonicalWindow` replaced `MainWindow`); not deleted — the r273 opaque marker and the U1–U3 guards still refer to it; **r434 OFF the FREQ mincut path** |
> | `fullWeil_separates_offCritical_zeros` | `RH/ExternalBridges.lean` | classical compact Paley–Wiener separation brick; the logical conversion to Mathlib `RiemannHypothesis` is proved, but the compact separating family is not yet formalized |
>
> Retired as asserting sorries by r638L:
> `arch_gauss_mellin_digamma_identity` → unasserted
> `ArchGaussMellinDigammaIdentity` (the original quantifier is
> overstrong; selected-path `O(Δ²)` is the honest replacement);
> `standard_explicit_formula_identification` → unasserted
> `StandardExplicitFormulaIdentification` (gauge mismatch exposed by
> `surplusComb + archGaugeDelta`; the honest-contour theorem is proved).
>
> Retired as sorries by r376: `pole_elementwise_stabilization` → **PROVED** (native-mesh second-difference of `polePotential`, comb-parallel; `#print axioms` has no `sorryAx`; remaining named identity `PoleDyadicIndependence`, not a hole); `specFamily_sourceExact_completion` → named Prop `SourceExactOfFamilyCompletion` (C1 `PairMarginLaw` convention: the opaque `SourceExact` filling is unprovable by design; transcribable half is the already-proved `sourceExact_buildPrimeWindow`; residual opacity is C1's `canonicalCompletion`).
>
> r380 named Props (not sorrys, census unchanged): `ComplementaryDualHankelInertia`, `DPPIdentity`, `SignedBorodinComplement`, `K2EqHankelRatio`, `P1EqCapInertia`, `P2EqPostcapAlternation` (`RH/PivotCoordinate.lean`; Borodin OP / discrete OPE remainder, same class as `CauchyInterlace`).
>
> r384 named Props (not sorrys, census unchanged): `FlankEntryPrefix`, `ChristoffelPivotBound` (`RH/FlankEntry.lean`; discrete OP / CD remainder of the r382 inductive core, same class as `ComplementaryDualHankelInertia`).
>
> r397 named Props (not sorrys, census unchanged at 5): `selected_augDualResolvent_gt_half` (r397 strict tail, r430 **degraded** to the stronger alternative: `∀ᶠ k, (R†(W^ℝ_k) − ½·1).PosDef`), `SelectedMasterImpliesPlainReads` (L†/master of the real windows ⇒ plain `fullRead` along the sequence), `ExactArchAgreesWithArchRead` (folded Exact arch vs opaque `archRead`).  Sequence identities (`selectedDelta_eq`, `a_k → ∞`, `Δ_k → 0`, `m_k → ∞`) and `weil_nonneg_of_selected_windows` are theorems; since r638L the latter takes the unasserted arch contract explicitly and consumes no arch `sorry`.  `lstar_canonical` / `terminal_q_canonical` remain typed `sorry`s on the alternative route.
>
> r406 proved theorems (not sorrys, census unchanged at 5): `indNeg_sub_rankOne_le_one`, `posDef_sub_rankOne_iff`, `woodbury_inv`, `oneDefect_update_posDef_iff`, `posDef_of_contractive_lift`, `cMin_normSq`, `posDef_gram_sub_rankOne_iff` (`RH/OneDefect.lean`; finite matrix algebra, independent of R404/R405).
>
> r412 proved theorems (not sorrys, census unchanged at 5): `graphResolvent_eq_dualResolvent_inv`, `graphResolvent_sub_half_eq`, `indNeg_graphResolvent_sub_half`, `indNeg_mobius`, `energy_split_contractive`, `energy_split_at_most_one`, `p1_coord_graphResolvent`, `augDualResolvent_gt_half_of_C_gt_one` (`RH/GraphResolvent.lean`; finite matrix algebra).  Named Prop `GraphResolventIsLEnsembleInv` (CD identification $E=C^{-1}$ on `RepresentsLEnsemble`; same class as `P1EqCapInertia`).
>
> r426 proved theorems (not sorrys, census unchanged at 5): `schWoodbury_eq_oneDefectDelta`, `schWoodbury_one_neg_iff_update`, `schWoodbury_eq_phiBB_sub`, `phiBB_eq_cJ_add_selfEnergy`, `schChart_eq_eps`, `vacuous_sch_neg_iff`, `den_lt_two_iff`, `gamma_lt_one_of_le_S_lt_Bw`, `parseval_normSq` (`RH/EdgeBalance.lean`; finite algebra).  Named Props `BorderIsMuParseval`, `BorderLoewnerLeS`, `QNLtOne` (r424/r425 source identifications; same class as `P1EqCapInertia`).
>
> r434 proved theorems (not sorrys, census unchanged at 5): `masterCap_posSemidef_iff_Rdagger_ge_half`, `masterCap_posDef_iff_Rdagger_gt_half`, `selectedWindowConeSemidef_implies_A_cap_posSemidef`, `selectedSemidefImpliesPlainReads_of_A_cap`, now named `internal_weil_nonneg_of_frequently_selected_of_A_cap` (`RH/FrequentlySelected.lean`; real-window Loewner).  Named Prop `SelectedACapPsdImpliesPlainReads` (Hankel/`fullRead` remainder after the Loewner identification).  `SelectedSemidefImpliesPlainReads` is now a theorem of that remainder.
>
> Retired as sorries by C1: `lstar_subordination` → `lstar_canonical`
> (retype), `terminal_positive_main` → `terminal_q_canonical` (retype,
> sharpened), `pair_margin_main` → named Prop `PairMarginLaw` + the
> dictionary lemma (duplicate retired), `crossing_budget` → PROVED.
> Retired as sorries by r373: `augmentedSubordination_iff_dualResolvent`
> → **PROVED** (μ-ONB Gram whitening `RepresentsLEnsemble` + congruence
> onto `I−G†` + A3).  Haynsworth (`haynsworth_two_rank`,
> `haynsworth_mixed`) entered as proved theorems, not sorrys.
>
> **The C1 axiom audit (`RH/Audit.lean`, verbatim build output):**
>
> ```
> 'RH.lstar_terminal_implies_master' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.augmentedSubordination_iff_lstar_and_terminal' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.crossing_budget' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.canonical_budget_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.lstar_canonical' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.terminal_q_canonical' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.augmented_prefix_positive' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.augmentedSubordination_main' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.terminal_crossratio_main' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.prefix_chain_positive_main' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.free_window_positivity' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.pair_closes_main' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.weil_nonneg_of_windowlocal' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.pole_elementwise_stabilization' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_one_sub_iff_dualResolvent_gt_half' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_one_sub_borderedGram_iff_augDualResolvent' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_one_sub_borderedGram_iff_qDagger' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.augDualResolvent_fromBlocks' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.augDualResolvent_gt_smul_implies_dualResolvent' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.augmentedSubordination_iff_dualResolvent' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.haynsworth_two_rank' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.haynsworth_mixed' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.haynsworth_sigNeg_₁₁' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.haynsworth_sigNeg_₂₂' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.polePotential_even' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.polePotential_eq_cosh' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.weilArchKernel_even' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.mainWindow_iff_builtFromPrimeSource' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
> 'RH.rankOne_inertia_antitone' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.adaptive_band_from_entry' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.sigNeg_full_hankel_eq_sigNeg_weights' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.postcap_pivot_ratio_eq_h_form' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_hankel_eq_neg_pivot_count' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.p1_p2_iff_cap_posDef' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.pair_energy_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.h_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.h_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.h0_pos_of_mass' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.h1_pos_of_pairEnergy' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.three_atom_mass_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.threeAtom_flank_pivots' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.clusterRun3_H3' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.fiveAtom_energy' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.christoffel_bound_k0' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.christoffel_bound_k1' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.threeAtom_christoffel_k1' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_entry_of_flank' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.adaptive_band_from_flank_entry' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_eq_zero_of_posDef' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_sub_rankOne_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_sub_rankOne_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.woodbury_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.oneDefect_update_posDef_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_of_contractive_lift' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.cMin_normSq' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_gram_sub_rankOne_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_eq_one_sub_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_eq_dualResolvent_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_lt_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_posDef' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_sub_half_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_one_add_inv_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_inv_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_graphResolvent_sub_half' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.indNeg_mobius' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posDef_one_sub_inv_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.posSemidef_one_sub_inv_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.graphResolvent_gt_half_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.contractive_iff_gram_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.energy_split_contractive' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.energy_split_at_most_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.p1_coord_graphResolvent' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.augDualResolvent_gt_half_of_C_gt_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.phiBB_eq_cJ_add_selfEnergy' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schWoodbury_eq_oneDefectDelta' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schWoodbury_one_neg_iff_update' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schWoodbury_eq_phiBB_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schChart_eq_eps' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schChart_p1' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schChart_vacuous' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.schChart_tot' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.vacuous_sch_neg_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.vacuous_live_of_phi_neg' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.den_lt_two_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.den_lt_two_of_gamma_lt_one' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.gamma_lt_one_of_le_S_lt_Bw' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.den_lt_two_of_le_S_lt_Bw' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.parseval_normSq' depends on axioms: [propext, Classical.choice, Quot.sound]
> 'RH.gamma_lt_one_of_named' depends on axioms: [propext, Classical.choice, Quot.sound]
> ```
>
> Reading (the `sorryAx` granularity is resolved by the proof terms —
> see the note in `RH/Audit.lean`): the sorry-free layer carries the
> three standard axioms ONLY; the master chain consumes exactly the two
> canonical holes; the pair closure additionally the named dictionary;
> the Level-C extraction exactly the remaining classical arch-channel sorry
> (`pole_elementwise_stabilization` has no `sorryAx`);
> r362 DualResolvent finite algebra (A2/A3/A4/A5/A7-min) is sorry-free;
> **r373: the window↔matrix bridge has no `sorryAx`**, Haynsworth has
> no `sorryAx`, the transcribed pole/arch closed forms have no
> `sorryAx`.  **r376: pole stabilization has no `sorryAx`.**  **r380: the
> proved pivot-coordinate faces have no `sorryAx`.**  **r384: the proved
> flank-entry faces have no `sorryAx`.**  **r406: the one-defect
> theorems have no `sorryAx`.**  **r412: the graph-resolvent
> identities have no `sorryAx`.**  **r426: the edge-balance
> identities have no `sorryAx`.**  Direct R† path: the two canonical holes (not consumed)
> by DualResolvent itself), arch (extraction only), named Prop
> `BorderedCompressionBridge`, density montage (unformalized).
> The reviewer target "the final theorem consumes only the two
> arithmetic window theorems plus clearly named classical results" is
> thereby machine-checked at the granularity Lean offers.

This is the pilot recommended by round r267 (after the external
Alpöge–Furman adjudication, `arXiv:2608.13637`, itself Lean-4-formalized):
layer the corpus by provability and actually prove the provable core.

**r273 reviewer repair.** The pre-r273 pilot stated its three open
problems as universally quantified theorems over pure bookkeeping
structures — all three REFUTABLE by trivial models (the reviewer
adjudication). The repair: (1) the three refutations are now permanent
machine-checked guards (`RH/Counterexamples.lean`); (2) a concrete window
structure `VonMangoldtWindow` with all derived objects as definitions
(`RH/Window.lean`); (3) ONE master theorem `augmented_prefix_positive`
(augmented-matrix positivity through the half-filling cap, conditioned on
the honest opaque predicate `MainWindow`) replaces the two separate open
edges — both former edges are PROVED from it by finite matrix algebra.

## Build

```bash
cd rh/lean
lake exe cache get   # fetch the mathlib olean cache (skips a 2-3 h build)
lake build           # => "Build completed successfully"
```

- Toolchain: `leanprover/lean4:v4.29.1` (pinned in `lean-toolchain`; same as
  the sibling project `experiments/lean4-carrier-rigidity`, so elan and the
  local mathlib cache are shared). If elan is not installed:
  `curl https://elan.lean-lang.org/elan-init.sh -sSf | sh`.
- **mathlib is required** (pinned tag `v4.29.1` in `lakefile.toml`): core
  Lean 4 has neither the algebra hierarchy (`Field`, `LinearOrder`,
  `IsStrictOrderedRing`) nor `ring` / `field_simp` / `linarith`, and the
  Inertia layer states matrix theorems against `Mathlib.LinearAlgebra.Matrix`.
  The proved layer touches only the algebra/tactic core of mathlib.
- Build status on this machine: **builds green** (`Build completed
  successfully`, **8 `sorry` warnings** since r463: the previous five
  plus the three external bridges; 5 since r376 (7 since r373, 8
  since r362 DualResolvent, 7 since C1, 8 since r326, 5 since r310),
  all intentional and typed — see the sorry table above:
  the two canonical arithmetic holes `lstar_canonical` +
  `terminal_q_canonical` and the named r263 dictionary
  `pair_terminal_dictionary` (`RH/Canonical.lean`), the r310/r320
  opacity bridge `mainWindow_iff_builtFromPrimeSource`
  (`RH/Source.lean`, Alt-Last since C1), and the remaining r326
  Level-C statement `arch_gauss_mellin_digamma_identity`
  (`RH/Elementwise.lean`; r464 concrete near/far lag integrals;
  `arch_elementwise_stabilization` is now its proved wrapper).
  The r362 window↔matrix dictionary
  `augmentedSubordination_iff_dualResolvent` is **PROVED** since r373.
  History: 7 before the r273 retype, 9 through wave 9, 4 since the r305
  reconstruction (master + fog-free hole + 4 of 5 Inertia statements
  PROVED), 5 since the r310 source interface, still 5 after r310b,
  8 since r326 (the three new statements make the previously
  statement-less Level-C distance visible), **7 since C1** (the two
  holes retyped onto the canonical domain, the pair duplicate replaced
  by the ONE dictionary lemma, `crossing_budget` PROVED —
  `RH/Inertia.lean` is now sorry-free), **8 since r362** (DualResolvent
  matrix duality proved; one named transcription sorry), **7 since
  r373** (bridge PROVED; Haynsworth PROVED; arch/pole kernels named),
  **5 since r376** (pole stabilization PROVED; source-exact completion
  demoted to `SourceExactOfFamilyCompletion`; arch remains classical).
  **r380 census unchanged at 5** (`RH/PivotCoordinate.lean` is
  sorry-free: proved rank-1 inertia / adaptive band / Jacobi synthesis
  plus named Props for the Borodin/DPP remainder).
  **r384 census unchanged at 5** (`RH/FlankEntry.lean` is sorry-free:
  pair energy, h₀/h₁, ℚ toys, Christoffel k=0,1, and the
  `adaptive_band_from_entry` bridge proved; named Props
  `FlankEntryPrefix` and `ChristoffelPivotBound` for the inductive
  remainder).
  **r397 census unchanged at 5** (`RH/Selected.lean` is
  sorry-free: exact real domain + selected sequence identities
  proved; named mincut was `selected_augDualResolvent_gt_half`,
  r430-degraded to the stronger alternative).
  **r406 census unchanged at 5** (`RH/OneDefect.lean` is
  sorry-free: SATZ A/B/C, Woodbury, and the min-norm Gram
  identity proved; independent of R404/R405).
  **r412 census unchanged at 5** (`RH/GraphResolvent.lean` is
  sorry-free: spectral dictionary, Möbius inertia, energy-split
  contraction, and the zero-defect R† lift proved; named Prop
  `GraphResolventIsLEnsembleInv`).
  **r426 census unchanged at 5** (`RH/EdgeBalance.lean` is
  sorry-free: Woodbury-sch, chart trichotomy, τ²-separator,
  den formula, and the γ-bridge proved; named Props
  `BorderIsMuParseval` / `BorderLoewnerLeS` / `QNLtOne`).
  **r430 census unchanged at 5** (`RH/FrequentlySelected.lean` is
  sorry-free: Loewner A3, FREQ extraction, density corollary,
  mean-value trick; named mincut
  `frequently_selected_augDualResolvent_ge_half`).

## Layering (r267 recommendation: order by provability)

### `RH/Basic.lean` — definitions (no theorems beyond bookkeeping)

Abstract chain data of one window over an arbitrary field `K`:
`c/h/F/B`, derived `a_n = c_n^2 h_n`, `b_n = -(c_n F_n)^2`,
`rho_n = F_n^2/h_n`, the coupled recursion `tau`/`tauAug`, `D = tauAug/tau`,
partial spends `S`, regularity predicate. Proved bookkeeping:
`tau_ne_zero` on regular windows.
*Header provenance: r256–r259, `PRIME.PORT.RHP.COUPLEDTAU.TERMINAL.01` [E],
`verification/v959_coupledtau_terminal_dictionary.py` S0,
`coupledtau_probe.py` (SPEC_SHA `73d8247f6de36a2b`).*

### `RH/Recursion.lean` — the PROVED core (zero `sorry`)

| Theorem | Statement | Corpus anchor |
|---|---|---|
| `bilinear` | `tauAug_n tau_{n+1} − tauAug_{n+1} tau_n = (c_n F_n)^2 tau_n^2` (pure `ring`) | v959 S0.2 |
| `drain` | coupled recursion ⇒ `D_{n+1} = D_n − rho_n` (division prerequisites explicit) | v959 S0.1 |
| `telescope` | `D_N = B − S_N` by induction on the drain | v959 S0.3 / r258 |
| `terminal_reduction` | `B = S_N + m` ⇒ `D_{N+1} = m − rho_N` | v959 S0.3 (r243 form) |
| `terminal_equiv` | `0 < m − r ↔ r/m < 1` for `m > 0` | v959 S0.3 consequence gate |
| `two_branch_cheap` / `_strict` | `\|Z\| ≤ U` and `U ≤ M` (resp. `<`) ⇒ `Z²/M² ≤ 1` (resp. `<`) | r263 cheap branch |
| `exception_scalar_closes` | `Z² < m` ⇒ `Z²/m < 1` | r263/r264 S6 shape |

### `RH/Inertia.lean` — the matrix-theorem layer (since C1: fully PROVED, zero `sorry`)

Proved since the start: `hankel_isHermitian`, `window_cap_arith`
(`2n − 1 ≤ S ↔ n ≤ (S+1)/2`, the counting half of half-filling, by `omega`),
and since wave 5 (v962 / r281, T1) `moment_counting_free_pivots`
(`2n ≤ S − 1 ↔ n < (S+1)/2`: the free pivots are exactly
`h_0 .. h_{N_w−1}` — half-filling is the end of the free moment space,
"why half-filling" answered by counting) and `first_forced_pivot`
(`h_{N_w}` is the first forced pivot), both by `omega`.

**PROVED since r305** (the reviewer plan §6.1 cleanup — mathlib-backed,
no axioms, no `native_decide`):

| Statement | Content | Corpus anchor |
|---|---|---|
| `posDef_of_isEmpty`, `posDef_of_posSemidef_det_ne_zero`, `posDef_submatrix_of_injective`, `posDef_fromBlocks_border`, `posDef_succ_of_posDef_det_pos`, `posDef_of_leading_det_pos` | the general PosDef layer, incl. **Sylvester's criterion** built from scratch (mathlib has no minor-based criterion) | r305 |
| `psd_base` | positive measure ⇒ Hankel PSD (`x^T H x = ∫ p_x² dμ ≥ 0`) | v958 S0 |
| `positive_prefix_firewall` | `H_p ≻ 0 ↔ h_0..h_{p−1} > 0` (Sylvester chain, **both directions**) | v959 S0.5 |
| `sylvester_pullback` | congruence `AᵀMA` with invertible `A` preserves PosDef | v956 r229 |
| `half_filling_boundary` | positive h-prefix ⇒ `H_{N_w} ≻ 0` (reverse Sylvester at the cap) | v956 r228/r229 |

**PROVED since C1** (formerly the ONE remaining `sorry` of this file):

| Statement | Content | Corpus anchor |
|---|---|---|
| `crossing_budget` — T2: `#(h_n < 0, n < S) = S_−` (Jacobi/Sylvester, world-blind) | **PROVED**: the r305 "mathlib carries neither" assessment was half stale — mathlib v4.29.1 has Sylvester's law of inertia at the quadratic-form level (`QuadraticForm.sigNeg_of_equiv_weightedSumSquares`); the pivot/minor dictionary is built in the `JacobiInertia` section: `exists_congruent_diagonal` (Jacobi's rule as an LDL-type congruence, Schur block-elimination induction), `hankel_eq_vand_conj` (`H_S = Vᵀ(diag w)V`, definitional — no Vandermonde determinant formula), `equivalent_toQuadraticMap'_congruence` (matrix congruence ⟹ equivalent forms); both counts equal the inertia invariant `sigNeg` | v962 T2 / r279 (`oriented_theorem_probe.py`, SPEC `9107709b4f4a65d1`) — the exact-rational certificate stands beside the proof |

### `RH/Haynsworth.lean` — THE R373 TWO-RANK / MIXED INERTIA THEOREMS (zero `sorry`)

Finite real algebra.  Does **not** assert the r367 census premises P1/P2
on any window.  NO RH CLAIM.

| Theorem | Status | Content |
|---|---|---|
| `haynsworth_sigNeg_₁₁`, `haynsworth_sigNeg_₂₂` | **proved** | Haynsworth additivity: inertia of a Hermitian block matrix splits as `In(A)+In(Schur)` along either diagonal |
| `haynsworth_two_rank` | **proved** | r367 J = I₂ cut: `ind₋(A₀)=1` and `det(I+UᵀA₀⁻¹U)<0` ⇒ `A₀+UUᵀ ≻ 0` |
| `haynsworth_mixed` | **proved** | r369 J-form: `In [[A,U],[Uᵀ,−J⁻¹]] = In(A)+In(−Φ) = In(−J⁻¹)+In(A+UJUᵀ)` for invertible Hermitian `J` |

Axiom census (`RH/Audit.lean` section (f)): `[propext, Classical.choice, Quot.sound]` only.

### `RH/PivotCoordinate.lean` — THE R380 PIVOT-COORDINATE LEMMAS (DCCXXXVII; zero `sorry`)

Finite real algebra on the existing `SignedAtoms` / `VonMangoldtWindow`
Hankel objects (no parallel types).  Does **not** assert Haynsworth
premises (P1)/(P2) on any window.  Census unchanged at 5.  NO RH CLAIM.

| Item | Exit | Content |
|---|---|---|
| `rankOne_inertia_antitone` | **proved** | `ind₋(A+vvᵀ) ≤ ind₋(A)` and `ind₋(A) ≤ ind₋(A+vvᵀ)+1` (`sigNeg` subspace argument; mathlib has no Weyl/Courant–Fischer; `CauchyInterlace` is not consumed) |
| `adaptive_band_from_entry` | **proved** | entry `ind₋(A_{n₀}) ≤ 1` along `A_{n+1}=A_n+v_n v_nᵀ` implies the bound for all later rungs |
| `sigNeg_full_hankel_eq_sigNeg_weights`, `hankel_eq_vand_rect` | **proved** | Vandermonde Gram and full-size `In H_S = In diag(w)` (nodes injective) |
| `ComplementaryDualHankelInertia` | named Prop | lemma-3 remainder: trailing Schur of `H_S` as dual Hankel `H_{S-k}(σa)` (discrete CD / Borodin OP; mathlib v4.29.1 has Vandermonde + Haynsworth, not the dual OP basis) |
| `signed_dual_hankel_complement_inertia` | hypothesis form | applies the named Prop |
| `postcap_pivot_ratio_eq_h_form` | **proved** | consecutive Hankel dets telescope to `1/(h_N h_{N+1} a.h_{N-3} a.h_{N-2})` |
| `DPPIdentity`, `SignedBorodinComplement`, `K2EqHankelRatio` | named Props | lemma-4 remainder: `det(I−2R_r)=H_r(σa)/H_r(a)`, signed Borodin complement, and `det K₂` as the Hankel ratio (OP construction of R is the DualResolvent-documented gap) |
| `detK2_eq_postcap_pivot_ratio` | hypothesis form | applies `K2EqHankelRatio` |
| `indNeg_hankel_eq_neg_pivot_count` | **proved** | Jacobi: `ind₋ H_p = #{h_i < 0 : i < p}` (existing `exists_congruent_diagonal`) |
| `p1_p2_iff_cap_posDef` | **proved** (Hankel / Jacobi face) | `{ind₋ H_{N+2} ≤ 1 ∧ h_N h_{N+1} < 0} ↔ {positive prefix ∧ one post-cap defect} ↔ {H_N ≻ 0 ∧ post-cap}` |
| `P1EqCapInertia`, `P2EqPostcapAlternation` | named Props | identification of that dictionary with Haynsworth (P1)/(P2) |

Axiom census (`RH/Audit.lean` section (i)): `[propext, Classical.choice, Quot.sound]` only — no `sorryAx`.

### `RH/FlankEntry.lean` — THE R384 FLANK-ENTRY PREFIX (r382 docking; zero `sorry`)

Finite real algebra on the existing `SignedAtoms` carrier (no parallel
Hankel types).  Does **not** assert L* or Haynsworth (P1)/(P2) on any
window.  Census unchanged at 5.  NO RH CLAIM.

| Item | Exit | Content |
|---|---|---|
| `FlankRunBound`, `FlankRatioBound`, `FlankTwoThird` | definitions | (F1) no three consecutive negative weights; (F2c) ν-mass of a maximal negative run ≤ c times flanking μ-mass; (F2_{2/3}) with ordered support |
| `FlankEntryPrefix` | named Prop | `FlankTwoThird m → ∀ i ≤ ⌊2N/5⌋, 0 < h_i` (r382 inductive core; discrete OP / CD remainder) |
| `pair_energy_identity` | **proved** | `m₀ m₂ − m₁² = ½ ∑∑ wᵢ wⱼ (xᵢ−xⱼ)²` |
| `h_zero`, `h_one`, `h0_pos_of_mass`, `h1_pos_of_pairEnergy` | **proved** | `h₀ = m₀`; `h₁ =` pair-energy `/ m₀`; positivity from mass and energy |
| `three_atom_mass_pos`, `three_atom_equal_flank_pairEnergy_pos` | **proved** | local 3-atom mass/energy positivity under `c < 1` |
| `threeAtom_flank_pivots` | **proved** (ℚ) | nodes `{0,1,2}`, weights `{3,−2,3}`: `h = (4, 6, −3)` |
| `clusterRun3_H3` | **proved** (ℚ) | weights `{2,2,−1,−1,−1,2,2}`: `H₃ = −28500` |
| `fiveAtom_energy`, `fiveAtom_h0_h1` | **proved** (ℚ) | 2-versus-1 interlacing: energy `56`, `h₀=4`, `h₁=14` |
| `ChristoffelPivotBound` | named Prop | `h_k(w) ≥ (1−λ) h_k(μ)` under a Rayleigh bound on the ν/μ Hankels (general k; CD kernel) |
| `christoffel_bound_k0`, `christoffel_bound_k1` | **proved** | special cases k = 0 (mass split) and k = 1 (completing the square, `λ ≤ 1`) |
| `threeAtom_christoffel_k1` | **proved** (ℚ) | `6 ≥ (1−1/3)·6` |
| `indNeg_entry_of_flank`, `adaptive_band_from_flank_entry` | **proved** | `FlankEntryPrefix` ⇒ `ind₋ H_{n₀+1} = 0`; composition with `adaptive_band_from_entry` |

Axiom census (`RH/Audit.lean` section (j)): `[propext, Classical.choice, Quot.sound]` only — no `sorryAx`.

### `RH/Window.lean` — the retyped window structure + the finite-algebra machinery (since C1: zero `sorry` — the L* hole moved to `RH/Canonical.lean` as `lstar_canonical`)

The concrete structure `VonMangoldtWindow` (exact rationals, like the
corpus): fields `S` (atom count), `nodes` (positions), `combWeight` /
`archWeight` (nonneg comb and archimedean parts, signed `weight` derived),
`lo`/`hi`/`window_rule` (window rule), `u` (border vector), `B` (budget).
Derived DEFINITIONS (not free fields): half-filling cap
`cap = (S+1)/2`, moments `mom`, Hankel `H_n`, chain
`h_k = det H_{k+1}/det H_k`, augmented matrix
`A_{w,n} = [[H_n, u_n], [u_n^T, B]]`, Schur margin
`D_n = det A_n/det H_n`, terminal cross-ratio `q`. An exact rational toy
instance (S = 3, cap = 2) tests the definitions.

| Theorem | Status | Content |
|---|---|---|
| `hankel_posDef_of_augmented`, `budget_pos_of_augmented` | proved | block/corner extraction from `A_n ≻ 0` |
| `h_pos_of_posDef`, `D_pos_of_augmented`, `q_lt_one_of_pos` | proved | Sylvester step, Schur-margin step, terminal gate |
| `D_eq_schur` | proved | `D_n = B − u^T H_n^{-1} u` (via mathlib `det_fromBlocks₁₁`) |
| `master_implies_free_window` | proved | hypothesis form: master conclusion ⇒ free-window positivity (block extraction + Sylvester ratio) |
| `main_window_reduction` | proved | **T4** (v962): on a nonvanishing chain, free-window positivity ⇔ "no crossing before the cap" |
| the L* hole | **C1 MOVE** | the open statement (lemma L*, the r283 reduction / v963; ledger `PRIME.LSTAR.SUBORDINATION.01` [O]; standalone statement `rh/problem/lstar_problem.tex`) lives since C1 in `RH/Canonical.lean` as `lstar_canonical : CanonicalWindow w → LStar w` |
| `hankel_quadform` | proved | the quadratic-form dictionary: `x ⬝ H_n x = ∫p_x²dμ − ∫p_x²dν` for the coefficient polynomial (finite algebra, wave 6) |
| `hankel_eq_comb_sub_arch`, `combHankel_eq_vand`, `archHankel_eq_vand` | proved (r373) | signed Hankel = μ-Gram − ν-Gram; each Gram is the Vandermonde evaluation form on the node basis |
| `lstar_implies_hankel_posDef`, `lstar_implies_free_window` | proved | hypothesis form: L* ⇒ every Hankel block through the cap PosDef ⇒ free-window positivity (the wave-6 direction tying the canonical form to the fog-free hole) |
| `lstar_free_window_main`, `free_window_positivity` | **C1 MOVE** (proved corollaries) | moved to `RH/Canonical.lean` with the domain retype (`CanonicalWindow`), proofs verbatim through `lstar_implies_free_window` |

**Wave-7 census (v964, rounds 286–289):** NO new statement — the hole
stays `lstar_subordination`; its
docstring now carries the wave-7 measured state (57/57 anchors positive,
margin decay resolved harmless per r286, the diophantine route excluded
per r289 `METRIC_ONLY` — the open front is the fraction-profile
functional, r290 in flight).

### `RH/Source.lean` — THE EXPLICIT SOURCE INTERFACE (r310, reviewer plan §6.3; refined r310b, reviewer plan §8; repaired r320, R319 audit U1/U2; one `sorry`: the opacity bridge in target form)

**r320 repair (R319 audit).** `RepresentsSpec`/`RepresentsWindow` are
RETYPED: besides the r310b node/comb/arch mesh clauses they now demand
(4) exact u-fidelity and (5) exact B-fidelity (U1: the old predicate
never bound `u`/`B`, so a `B = −1` window slipped through the bridge
against `terminal_positive_main`; the spec carries the new transcribable
field `budget_pos` — the r243 positivity half), and (6)/(7) the
separation discipline: the tolerance stays below HALF the minimal
spec-node gap and below every comb weight (U2: at mesh level 0 the
tolerance is the full `log anchor`, which identified all nodes — the
collided window killed `lstar_subordination` via `p = X − 1`; honest
price, documented: mesh level 0 represents nothing, representation
begins at sufficient refinement). The r320 verification additionally
found the FREE spec fields `archWeight`/`border` carry the same disease
one channel over (arbitrary arch mass vs L* at `p = 1`; arbitrary
border vs the retyped pair margin) — no honest finite clause can close
them before their transcriptions exist, so the bridge RHS now carries
the **opaque `SourceExact` guard** (the r273 `MainWindow` convention
applied to the spec side; its elimination = the named arch/border/fold
transcription TODO). A witness section proves the retyped predicate
satisfiable (anchor 2, atoms {2,3,4}, mesh level 4 — the first level
satisfying the separation discipline, `2^7 < 3^5`), and a documentation
block maps the mesh-vs-anchor cofinality seam (see below).

The source boundary as a construction instead of an opaque marker —
conservative route: `MainWindow` stays opaque and untouched; the explicit
layer enters beside it. `PrimeWindowSpec` carries the arithmetic data
(strictly increasing prime-power atoms `p^k`, anchor, mesh level,
arch/border fields); node positions and comb weights are **derived**, not
fields: `node j = Real.log (primePowers j)`,
`combWeight j = Λ (primePowers j)` (mathlib
`ArithmeticFunction.vonMangoldt`). `PrimeWindow` is the ℝ-valued mirror of
`VonMangoldtWindow`; `buildPrimeWindow : PrimeWindowSpec → PrimeWindow`
proves the window rule (`0 ≤ log p^k ≤ 2 log anchor`) from the source rule
`p^k ≤ anchor²`; `MainWindowExplicit w := ∃ s, w = buildPrimeWindow s`.
Python source of the construction (translated: the CONSTRUCTION, never a
measured value): `verification/v563_paper2_readouts.py`
(`von_mangoldt_table`, `U_ALL`/`MU_ALL`, `build_window`, `atom_lags_at`,
`arch_lags`) → `port_integrable_kernel_probe.folded_measure` →
`principal_bessel_probe.window_pack`/`smooth_comb` (border; r243 budget).

**r310b refinement (reviewer plan §8).** The injectivity claim is
restructured as an honest FOUR-STAGE SUPPORT CHAIN (the reviewer's
warning: after mirroring/folding/tent-sampling deliberately equal
geometric nodes arise, so raw injectivity of a folded map must not be
stated): stage 1 `primePow_index_injective`, stage 2 `nodes_injective`
(unfolded — exactly what `buildPrimeWindow` produces; FOLDING STATUS,
honest: the build map contains NO hidden fold), stage 3 `foldedWindow`
(the explicit quotient/aggregation: equal folded nodes merged, weights
added — Python `folded_measure`/`np.add.at`; arbitrary fold map
`φ : ℝ → ℝ`, the corpus `cos(2π j/L)` map is an instance whose exact
transcription belongs to the classical arch/border TODO), stage 4
`support_nodup` (AFTER the aggregation). On top: the four source
theorems (table below, all proved) and the bridge in the reviewer
target form. An APPROXIMATION WARNING block at
`rational_window_approximates` records (reviewer verbatim) that the
rational windows are certificate objects, not the definition — an
approximation proof chain would need error ≪ the shrinking L* margin,
which is not established; no statement uses approximation as a proof
path.

| Theorem | Status | Content |
|---|---|---|
| `primePow_index_injective` | proved (r310b) | **stage 1**: `p^k = q^ℓ` (primes, exponents ≥ 1) ⟹ `p = q ∧ k = ℓ` — unique factorization via `Nat.minFac`; the canonical `(p,k)` indexing is collision-free |
| `node_strictMono`, `nodes_injective` | proved | **stage 2**: the real `log p^k` node positions are strictly increasing, hence pairwise distinct (log monotonicity + ordered prime powers — the r310 reviewer target proof); scope: the UNFOLDED chain |
| `foldedWindow` (+ `foldedSupport`, `foldedNode`, `foldFiber`) | definition (r310b) | **stage 3**: the quotient/aggregation construction for the folded source — equal folded nodes merged (`Finset.image`), channel weights ADDED over each fiber (`np.add.at`), border/budget pass through |
| `foldedWindow_mass` (+ `_comb_mass`, `_arch_mass`) | proved (r310b) | **stage-3 structure theorem**: exact mass conservation for every channel — the aggregation is a quotient, not a projection (`Finset.sum_fiberwise_of_maps_to`) |
| `support_nodup` (+ `foldedWindow_nodes_strictMono`) | proved (r310b) | **stage 4**: AFTER the aggregation the merged support is duplicate-free (sorted strictly increasing); before it this is deliberately false in general |
| `buildPrimeWindow_source_exact` | proved (r310b) | **source theorem 1**: the built window carries DEFINITIONALLY the `Λ`/`log` source data (`rfl` by derivation — the spec derives nodes/weights instead of carrying them as free fields) |
| `buildPrimeWindow_weights_nonnegative` | proved (r310b) | **source theorem 2**: all weight channels nonnegative (comb via `vonMangoldt_nonneg`, strictly positive even; arch via the spec field), and both channels stay nonnegative under any fold |
| `buildPrimeWindow_support_canonical` | proved (r310b) | **source theorem 3**: the full stage-1/2/3/4 chain — unfolded nodes pairwise distinct, folded support duplicate-free after aggregation for ANY fold map |
| `buildPrimeWindow_refinement_compatible` | proved (r310b, `rfl` by design) | **source theorem 4**: the built family window is mesh-independent, also under any FIXED fold map; honest scope: the corpus fold map itself is mesh-dependent (`L = 2M−2`) — the mesh enters ONLY through the fold map, which is why folding is a separate stage |
| `node_pos`, `combWeight_pos`, `node_le_two_alpha` | proved | node positivity, `Λ(p^k) > 0` (via `vonMangoldt_ne_zero_iff`), the real window rule |
| `predefined_family` | proved (constructive) | **structure theorem 1**: the family atom set at anchor `a` is decided by arithmetic alone — `n` is an atom iff `IsPrimePow n ∧ n ≤ a²` (predefined, not result-dependent) |
| `mesh_refinement_compatible` (+ `mesh_refinement_shrinks`) | proved (constructive) | **structure theorem 2**: refinement changes only the mesh level, never the atom data (`rfl`-level by design); the mesh width strictly shrinks along refinement |
| `cofinal_prime_windows` | proved | **structure theorem 3**: for every `N` an anchor exists whose window carries ≥ `N` atoms (Euclid via `Nat.exists_infinite_primes`) |
| `finite_forms_converge_to_weil` | proved (stabilization form) | **structure theorem 4**, comb channel: for test data vanishing above `b` the finite comb forms EQUAL the Weil prime-side tsum `Σ' Λ(n) f(log n)` for every anchor `≥ max(1,⌈exp b⌉)` — pointwise convergence realized as exact stabilization. Scope: prime side only; the archimedean-kernel transcription (`arch_A`) is the documented classical TODO, the spectral/zero side stays the open program content |
| `rational_window_approximates` (+ `exists_rat_close`) | proved | the rational certificate layer: every real prime window admits rational node/weight data within every positive bound (density of ℚ); the frozen v962/v963 windows instantiate the mesh-level predicate `RepresentsSpec`. ⚠ Carries the r310b APPROXIMATION WARNING (see above) — certificate objects, not a proof path |
| `RepresentsWindow` (+ `representsSpec_iff`) | definition + proved (r310b; **retyped r320**) | the window-level representation predicate: node/comb/arch within `δ`, u/B EXACT (clauses 4/5, U1 repair), separation discipline `2δ <` every node gap and `δ <` every comb weight (clauses 6/7, U2 repair); `RepresentsSpec w s ↔ RepresentsWindow w (buildPrimeWindow s) s.mesh` stays definitional (`Iff.rfl`) |
| `SourceExact` | opaque predicate (r320) | the spec-side honesty guard: "arch/border/budget are the genuine Weil-kernel/v958/r243 data of this atom set" — deliberately opaque (r273 convention) because the free spec fields would otherwise re-import the U2/U3 disease through the arch and border channels (r320 verification finding); elimination = the arch/border/fold transcription TODO |
| `mainWindow_iff_builtFromPrimeSource` | **`sorry` = the opacity bridge, reviewer target form (definitional/technical; retyped r320)** | `MainWindow w ↔ ∃ s, SourceExact s ∧ RepresentsWindow w (buildPrimeWindow s) s.mesh` — unprovable BY DESIGN while `MainWindow` is `opaque` (r273). DOCSTRING CORRECTION (r320): the old "becomes `Iff.rfl` under the invasive route" promise was wrong — with the OLD predicate the invasive route would have made the library inconsistent (U1–U3 guards); the honest statement: definitional only AFTER the `SourceExact` elimination (arch/border/fold transcriptions) |
| `mainWindow_explicit_bridge` | proved (r310b, from the target form; carries the r320 retype) | `MainWindow w ↔ ∃ s, SourceExact s ∧ RepresentsSpec w s` — no own hole; the sorry lives in `mainWindow_iff_builtFromPrimeSource`; census unchanged at 5 |
| `witnessSpec` / `witnessWindow` / `witness_represents` / `representsWindow_nonempty` / `mainWindowExplicit_nonempty` | definitions + proved (r320, repair 4) | the nonemptiness witness: anchor 2, atoms {2,3,4}, mesh level 4 (`log 2 / 5` — separation satisfiable via `2^7 < 3^5` and `3^5 < 2^8`), exact-rational certificate window (nodes `7/10, 11/10, 139/100`); proves the retyped predicate SATISFIABLE. Honest form statement: `∃ w, MainWindow w` is deliberately NOT provable (`MainWindow` and `SourceExact` are opaque — exactly what blocks the U1–U3 adversaries) |
| mesh-vs-anchor cofinality seam | documentation block (r320, repair 5; **r326 UPDATE**) | `cofinal_prime_windows` = ANCHOR direction (atom count, Euclid) + `mesh_refinement_shrinks` (mesh → 0 at fixed anchor); hypothesis (H_cof) (carrier lane, `TfptCarrier/CofinalWeil.lean`, v849) needs PSD certificates along a pre-fixed MESH-REFINEMENT tower; no theorem of Source.lean feeds (H_cof), and none claims to. **r326**: (H_cof) is REPLACED as the target extraction route by the elementwise architecture (`RH/Elementwise.lean` — per-element predefined finite stabilization, no tower, no transport); the carrier-lane documentation stays historically correct, and the old seam-identification goal is superseded by the named Elementwise statements |

### `RH/Elementwise.lean` — THE ELEMENTWISE EXTRACTION ARCHITECTURE (r326, the R325 repair set; r376: one remaining typed `sorry` — arch stabilization)

The Level-C layer (window-local positivity ⟹ Weil form) as named
statements, per the R325 fork adjudication
(`extraction_order_probe.py`, sealed, primary
`ELEMENTWISE_STABILIZATION_GO`): no mesh-cofinal ladder, no transport,
no (H_cof) — per test element the finite forms stabilize at a
PREDEFINED anchor onset and the element's OWN native mesh, and the
extraction is one finite instantiation per element. Honest scope: the
comb channel is transcribed and PROVED (corpus gauge `2Λ(n)/√n`, exact
atom sum; the tent-assembled mesh read equals it on the native class —
R325 S1.3, measured, mesh-grid transcription = the fold TODO); the
pole channel is transcribed and PROVED (r376: native-mesh
second-difference of `polePotential`, parallel to mesh-free
`combRead`); the arch channel enters through OPAQUE reads
(`archRead`/`weilArchSide` — the r273/r320 opacity convention; their
elimination = the classical kernel transcription). Sign convention:
`fullRead = arch − comb + pole` (the corpus total `c = car + cat + cp`,
atom channel = MINUS the comb sum). `SourceExact` is eliminated as a
free assumption from the extraction route: the route consumes only the
CONSTRUCTION (`specFamily`), for which the transcribable source-exactness
is PROVED.

| Theorem | Status | Content |
|---|---|---|
| `CanonicalPrimeWindow` (+ `canonicalPrimeWindow_build`, `canonicalPrimeWindow_isExplicit`) | definition + proved | **(i)** the canonical family as a window predicate: `∃ a m ha, w = buildPrimeWindow (specFamily a m ha)`; every family member is canonical; canonical ⟹ explicitly-main |
| `SourceExactSpec` | definition | the TRANSCRIBABLE source-exactness as a real definition (contrast the opaque `SourceExact`): node/comb derivation clauses (definitional by the r310 interface — recorded), ATOM-SET COMPLETENESS (the genuine content), budget positivity; arch/border deliberately NOT bound (their transcriptions do not exist — r320 finding) |
| `sourceExact_buildPrimeWindow` | **proved** | **(i), the wave-12 reviewer target** ("exactly one construction theorem"): every canonical family member satisfies `SourceExactSpec` — clauses by `rfl` + `predefined_family` + the spec field; built windows PROVABLY carry their source |
| `specFamily_sourceExact_completion_transcribable` / `SourceExactOfFamilyCompletion` | **proved** (transcribable half) + named Prop (r376) | the opaque `SourceExact` filling is unprovable by design while `SourceExact` is opaque; r376 demotes the former `sorry` to the named Prop (C1 `PairMarginLaw` convention). Residual opacity: C1 `canonicalCompletion` in `RH/Canonical.lean` (lag-kernels `weilArchKernel`/`polePotential` are not per-atom `archWeight` / v958 border / r243 drain-sum). **Not consumed by the extraction route** |
| `GridElement` (+ `D0`, `acf`, `toFun`, `supportBound`, `elementAnchor`) | definitions | **(ii)** the native dense class built for real (the v749 "Weil form of step functions" class): step values on the dyadic grid `D0 = 2^{−meshExp}`, DERIVED autocorrelation `a_d = D0·Σᵢ xᵢxᵢ₊d`, DERIVED even piecewise-linear interpolant, support `steps·D0`, onset `a₀(f) = max(1, ⌈exp(supportBound)⌉)` predefined from the support alone |
| `acf_eq_zero`, `acf_zero_nonneg`, `toFun_even`, `toFun_eq_zero` | proved | class structure: autocorrelation vanishes beyond the support, is nonnegative at lag 0; the test function is even and has PROVED compact support (from the construction, not assumed) |
| `combMass`, `combRead`, `weilCombSide` (+ `combMass_nonneg`, `combMass_eq_gauge`) | definitions + proved | the corpus-gauge comb channel: masses `2Λ(n)/√n` (MU_ALL), the exact atom sum over `windowAtoms a`, the Weil prime side as tsum; the gauge relation to the window's `Λ` channel proved |
| `comb_elementwise_stabilization` | **proved** | **(ii), comb channel**: for EVERY grid element and EVERY anchor `a ≥ elementAnchor f` the finite comb read EQUALS the Weil prime side — onset predefined from the element, NO mesh quantifier (the read is mesh-free, the built window mesh-independent); the elementwise form of `finite_forms_converge_to_weil` in the corpus gauge |
| `combRead_eq_window_channel`, `comb_window_elementwise_stabilization` | proved | the honesty ties: the corpus-gauge read IS the built window's comb channel (orderIso reindex, `rfl` per atom); the Λ-gauge window form stabilizes with the same explicit onset |
| `archRead`, `weilArchSide` | opaque constants | tent-read and Weil pairing of the arch channel; r373 names the kernel they are to match |
| `poleRead`, `weilPoleSide`, `poleEvenRead`, `poleΔ`, `polePairingZ` | definitions (r376) | native-mesh second-difference pairing of `polePotential` (Python `pole_lags_closed`); `poleRead`/`weilPoleSide` equal by `rfl` |
| `weilArchKernel`, `weilArchDigamma` | definitions (r373) | Titchmarsh Ch. X / Weil 1952 digamma factor on the critical line (`Complex.digamma`); evenness PROVED |
| `polePotential` (+ `polePotential_even`, `polePotential_zero`, `polePotential_eq_cosh`, `polePotential_nonpos`) | definition + **proved** (r373) | v716 closed form `−8(cosh(t/2)−1)`; even/zero/nonpositive |
| `arch_elementwise_stabilization` | **`sorry` (classical, S2)** | tent-read = Weil pairing at native-or-finer mesh; remaining classical: Gauss integral / `Real.digamma` / ψ-monotonicity / Mellin identifying `arch_A` with `weilArchKernel` (mathlib v4.29.1 TODO on `Digamma.lean`) |
| `pole_elementwise_stabilization` | **proved** (r376) | native-mesh second-difference of `polePotential` equals the Weil pole side by `rfl`; remaining named (not a hole): `PoleDyadicIndependence` |
| `fullRead`, `weilForm`, `elementwise_finite_stabilization` | definitions + **proved** (from the three channels) | **(ii), full form**: `∃ a₀, ∀ a ≥ a₀, ∀ m ≥ f.meshExp: fullRead a m f = weilForm f` — comb and pole unconditional, arch through its typed sorry; `a₀`, `m_f` elementwise-predefined |
| `WindowLocalPositive`, `weil_nonneg_of_windowlocal` | definition + **proved** | **(iii), the extraction WITHOUT the ladder**: window-local positivity of the canonical family (typed honestly on the PLAIN full form, with the `f.meshExp ≤ m` grid-compatibility guard) ⟹ `0 ≤ weilForm f` for every grid element — ONE finite instantiation per element (Euclid anchor + the element's native mesh); replaces the (H_cof) route |
| `BorderedCompressionBridge`, `weil_nonneg_of_bordered` | named Prop + proved | the compression bridge (bordered tower form ⟹ plain form — the corpus certificates live on the BORDERED form; the documented S2 rest) as a NAMED statement, parametrized over the bordered read (no new opaque, no truth commitment); the composed extraction is proved from (iii) |

### `RH/Closure.lean` — THE RECONSTRUCTION THEOREM (r305, reviewer plan §3; since C1: zero `sorry` — the terminal hole moved to `RH/Canonical.lean`)

| Theorem | Status | Content |
|---|---|---|
| `LStar`, `TerminalPositive` | definitions | the two window predicates: L* verbatim, and the r258/r260 terminal statement `0 < B ∧ q_N < 1` (faithful to TERMINAL_Q_LAW + the v959 budget telescope) |
| `terminal_margin_pos_of_terminal` | proved | terminal ⇒ `D_cap = B(1 − q) > 0` (ordered-field algebra, cf. `terminal_equiv`) |
| `A_eq_submatrix_A_cap` | proved | `A_n` is a principal submatrix of `A_cap` (border column included) |
| `lstar_terminal_implies_master` | **proved** | **the reconstruction theorem**: `LStar w → TerminalPositive w → ∀ n ≤ cap, A_{w,n} ≻ 0` (L* ⇒ `H_cap ≻ 0`; terminal ⇒ `D_cap > 0`; `det A_cap = D_cap·det H_cap > 0`; Schur bordering ⇒ `A_cap ≻ 0`; principal-submatrix restriction ⇒ all `A_n ≻ 0` — the matrix form of the backward Riccati drain `D_n = D_N + Σρ_k ≥ D_N`) |
| the terminal hole + the master corollaries | **C1 MOVE** | `terminal_positive_main` is retyped/sharpened to `terminal_q_canonical` (`RH/Canonical.lean`; budget half PROVED there); `augmented_prefix_positive`, `prefix_chain_positive_main`, `terminal_margin_positive_main`, `terminal_crossratio_main` moved with it, statements verbatim modulo the `MainWindow → CanonicalWindow` domain retype |

**The two true holes after C1**: `lstar_canonical` (base/wall) and
`terminal_q_canonical` (border/fiber), both `RH/Canonical.lean` on the
canonical final domain. Everything else is finite matrix algebra over
them.

### `RH/Augmented.lean` — THE AUGMENTED SUBORDINATION L† (r332, the reviewer unification; **zero `sorry`**)

The bird's-eye packaging: L* and the terminal statement are the
distributed and the rank-one part of ONE strict sampling inequality.
With `ℓ_w(p) = u_wᵀc` the border readout (`borderFunctional`, the v958
border column against the coefficient vector through the cap),

`(L†): 0 < B_w ∧ ∀ p ≠ 0, deg p < N_w: ∫p²dν_w + |ℓ_w(p)|²/B_w < ∫p²dμ_w`

(`AugmentedSubordination`). Geometric reading (documentation only):
`‖T_w‖ < 1` for the observation operator
`T_w p = ((√ν_j·p(x_j))_j, ℓ_w(p)/√B)` on the μ-Hilbert space. All
connections are finite algebra and close sorry-free:

| Theorem | Status | Content |
|---|---|---|
| `coeffPoly_zero`, `coeffPoly_coeffs`, `muSq_zero`, `nuSq_zero` | proved | coefficient-vector bookkeeping: `coeffPoly` inverts coefficient extraction below the cap (mathlib `as_sum_range_C_mul_X_pow'`) |
| `A_isHermitian`, `A_quadform` | proved | the augmented quadratic form split: `(x,t)ᵀ A_n (x,t) = xᵀH_n x + 2t(u·x) + Bt²` |
| `borderFunctional` (+ `borderFunctional_coeffPoly`) | definition + proved | the border readout `ℓ_w(p) = u_wᵀc` |
| `augmentedSubordination_iff_masterCap` | **proved** | **L† ⟺ `A_{w,n} ≻ 0` for all `n ≤ cap`** — ⟸ by quadratic completion at the test vector `(c, −ℓ(p)/B)`; ⟹ by the split `(μ−ν)(p²) − ℓ²/B + B(t+ℓ/B)²` with the `x = 0` budget-corner case; smaller degrees as principal submatrices |
| `augmentedSubordination_implies_lstar` | proved | without the border term, L† is L* (drop the nonnegative border square) |
| `augmentedSubordination_implies_terminal` | proved | with L*, the border term is the Schur condition: `B > 0` via the budget corner, `q < 1` via `D_cap = det A_cap/det H_cap > 0` — the `uᵀH⁻¹u < B` route in determinant coordinates, no explicit `H⁻¹u` minimizer needed |
| `augmentedSubordination_iff_lstar_and_terminal` | **proved** | **L† ⟺ L* ∧ Terminal** — backward direction re-runs the wave-10 reconstruction bricks (NOT `lstar_terminal_implies_master`), keeping the corollary below non-circular |
| `reconstruction_via_augmented` | proved | the r305 reconstruction theorem re-derived as `iff_masterCap.mp ∘ iff_lstar_and_terminal.mpr` — the Closure original is byte-stable, NOT replaced |
| `augmentedSubordination_main`, `augmented_prefix_positive_via_ldagger` | **C1 MOVE** (proved from the two holes) | the combined target form and the L†-route master moved to `RH/Canonical.lean` with the domain retype (`CanonicalWindow`, consuming `lstar_canonical` + `terminal_canonical`) — deliberately NOT sorries; a direct proof of L† would close BOTH holes |

Axiom census: every theorem of this file (now sorry-free in its
entirety) depends only on `propext/Classical.choice/Quot.sound` —
machine-checked in `RH/Audit.lean`.

### `RH/DualResolvent.lean` — THE R362/R373 DUALITY L† ⟺ R† ≻ ½I (reviewer priority 2; **sorry-free** since r373)

Finite-matrix formalization of the r362 dual-resolvent identity.
**Not new RH mathematics** — the spectral equivalence belongs in the
kernel graph because it is the new central architecture.  Formulation
(kernel-friendly, D = I gauge): `R := (I+E)⁻¹`, `G† := [[E,v],[vᵀ,γ]]`,
`Z := I+G†`, `R† := Z⁻¹`.  The Borodin OP-construction of R stays
outside; Cauchy interlacing is the named Prop `CauchyInterlace` (mathlib
v4.29.1 has no interlacing lemma), never a `sorry`.

| Theorem | Status | Content |
|---|---|---|
| `dualResolvent`, `lEnsemble`, `borderedGram`, `dualZ`, `augDualResolvent`, `qDagger`, `shermanDenom` | definitions | L-ensemble dual resolvent and the rank-1 border |
| `posDef_nonsingInv_sub_smul_iff` | **proved** | spectral comparison: `S ≻ 0`, `c > 0` ⇒ (`S⁻¹ ≻ c I` ⟺ `c⁻¹ I ≻ S`) |
| `posSemidef_nonsingInv_sub_smul_iff` | **proved** (r430) | Loewner face: `S⁻¹ ⪰ c I` ⟺ `c⁻¹ I ⪰ S` |
| `posDef_one_sub_iff_dualResolvent_gt_half` | **proved** | **(r356-A / A2)** `I−E ≻ 0` ⟺ `R ≻ ½I`, given `I+E ≻ 0` |
| `posSemidef_one_sub_iff_dualResolvent_ge_half` | **proved** (r430) | A2 Loewner: `I−E ⪰ 0` ⟺ `R ⪰ ½I` |
| `posDef_one_sub_borderedGram_iff_augDualResolvent` | **proved** | **(A3)** `I−G† ≻ 0` ⟺ `R† ≻ ½I`, given `Z ≻ 0` |
| `Rdagger_ge_half_iff_augmented_posSemidef` | **proved** (r430) | A3 Loewner: `I−G† ⪰ 0` ⟺ `R† ⪰ ½I` |
| `augDualResolvent_fromBlocks` | **proved** | **(A4)** block inverse of `Z`; Y-block is Sherman–Morrison (`invOf_fromBlocks₁₁_eq`) |
| `posDef_one_sub_borderedGram_iff_qDagger` | **proved** | **(A5)** `I−G† ≻ 0` ⟺ `q† < 1`, given `I−E ≻ 0` |
| `augDualResolvent_gt_smul_implies_dualResolvent` | **proved** | **(A7-min)** `R† ≻ αI` ⟹ `R ≻ αI` (principal restriction of `Z`) |
| `CauchyInterlace` | named Prop, not asserted | classical interlacing; cone consequence is A7-min |
| `RepresentsLEnsemble` | **def** (r373, R319) | μ-ONB whitening: `n=cap`, `Qᵀ μ Q = I`, `E = Qᵀ ν Q`, `v = −Qᵀu/√B`, `γ=0` — equations, not the cone-iff |
| `augmentedSubordination_iff_dualResolvent` | **proved** (r373) | window L† ↔ `R† ≻ ½I` under the whitening; congruence of `A_cap` onto `I−G†` then A3 |

Axiom census (`RH/Audit.lean` section (e)): A2/A3/A4/A5/A7-min **and
the bridge** depend only on `propext/Classical.choice/Quot.sound`.
NO RH CLAIM.

### `RH/Open.lean` — ladder bookkeeping + kill lists (r273: no `sorry` anymore)

The pre-r273 universal statements `terminal_crossratio_cofinal` and
`prefix_resummation_positivity` are REMOVED — both are refutable over the
bare bookkeeping (see `RH/Counterexamples.lean`). The file keeps the
`WindowLadder` structure, the terminal cross-ratio `q`, the full measured
**kill lists** (r257–r265 no-gos) and pointers to the truth-capable
replacements in `RH/Window.lean`.

### `RH/Counterexamples.lean` — the r273 reviewer guards (proved, no `sorry`)

| Theorem | Refutes (pre-r273 form) | Model |
|---|---|---|
| `pair_margin_not_universal` | `pair_margin_cofinal` | `M = 1, Z = Zloc = 2, runs = []` — split holds with equality, margin would need `2 < 1` |
| `terminal_crossratio_not_universal` | `terminal_crossratio_cofinal` | `h = c = 1, F = 2, m = 1` ⇒ `q_N = 4` on every rung |
| `prefix_resummation_not_universal` | `prefix_resummation_positivity` | `MainSource := True`, `h_0 = −1` ⇒ `tau_1 = −1` |
| `upper_pinning_not_universal` (wave 5, v962 N1) | world-blind `C = 0` upper pinning (`minC ≤ N_w` for every signed measure) | the EXACT one-negative instance `onenegToy` (4 atoms `0..3`, weights `1,1,1,−1/1000`): Hankel minors computed from the atoms (`onenegToy_minors`, incl. the negative `det H_4 = −1962/13625`), first crossing at `3 = N_w + 1` — a genuine moment computation, not a bookkeeping model |
| `o1_pinning_escape` (proved) | any fixed `C` for the one-negative family | offset `(S−1) − N_w = (S−3)/2` is unbounded in `S` |
| `old_bridge_terminal_inconsistent` (r320, U1) | the pre-r320 bridge type (`OldRepresentsWindow`, conserved verbatim: nodes/comb/arch only) jointly with the `terminal_positive_main` type | the EMPTY spec is old-represented by the `B = −1` window (`guardWindow0` — the old predicate never reads `u`/`B`); the terminal type then demands `0 < −1`; quantified over an ARBITRARY predicate `P` (r273 G3 style) |
| `old_bridge_lstar_inconsistent` (r320, U2) | the pre-r320 bridge type jointly with the `lstar_subordination` type | the {2,3,4} spec at MESH LEVEL 0 (tolerance `log 2`) is old-represented by the TOTAL NODE COLLISION window (`guardWindow3`, all nodes = 1; exact d9 log-2 bounds); `p = X − 1` (degree `1 < cap = 2`) vanishes on the window, both integrals are 0, the strict subordination demands `0 < 0` |
| `old_pair_margin_forces_empty` (r320, U3) | the pre-r320 `pair_margin_main` type (free `(Zloc, runs)`, bound only by the split inequality) | for EVERY predicate `P` satisfying the old margin type, `P` is EMPTY: `Zloc = \|F\| + 1`, `runs = []` satisfies the split trivially and the margin demands `\|F\| + 1 < √(5/7) < 1` — the r273 disease one level up |

These are **permanent guards**: any future "proof from bookkeeping" of the
old universal forms now contradicts a proved theorem of this library, any
O(1) upper-pinning claim must consume the comb structure (v962 N1), and
any attempt to restore the pre-r320 source-interface types contradicts
the three r320 guards (all sorry-free, axiom census
`propext/Classical.choice/Quot.sound` only).

### `RH/PairBound.lean` — the PROVED finite pair algebra (r271; since C1: zero `sorry`)

The r269/r271 fixed drive bound c2PAIR as abstract list algebra over a
linearly ordered field (probe `universal_pair_theorem_probe.py`,
SPEC_SHA `66f61c8a436af90e`):

| Theorem | Statement | Corpus anchor |
|---|---|---|
| `blockSums_sum` | one blocking pass preserves the sum (exact pair decomposition) | r271 Leg A (i) |
| `abs_sum_le_pairBound` | `\|sum l\| ≤ pairBound l` — the c2PAIR validity theorem | r271 Leg A (iii) |
| `pairBound_le_absSum` | the pairing never exceeds the abs triangle | r269 G40 ward |
| `abs_sum_le_pairBound_level2` / `pairBound_level2_le` | the b2LEVEL2 refinement: valid and never worse | r271 Leg B |
| `pair_exact` | `\|sg·M₁ − sg·M₂\| = \|M₁ − M₂\|` for `sg = ±1` (alternation identity) | r271 Leg A (ii) |
| `boundary_triple_le` | the b1RAND boundary group never worse than pair + tail | r271 Leg B |
| `pair_certifies` / `pair_closes_cofinally` | margin ⇒ `Z²/M² < 1` (via `two_branch_cheap_strict`) | r263/r271 |

**r320: the canonical extraction as a definition (U3 repair).** New
layer `signRuns` (maximal same-sign run aggregation, r271 G21) with the
proved regrouping `signRuns_sum`, `terminalDrive` (`Z_w = F_{cap−1}`,
r263 dictionary), `bulkRuns` (sign runs of the pre-terminal border
column `u_0..u_{cap−2}`) and `edgeLocal` (the EXACT complement
`Z − Σ runs`), with the split inequality a PROVED property of the
canonical extraction (`canonical_split` — H1+H2 by construction).
Honest modeling scope (documented): the probe-side F = 0.20 mesh-cell
extraction lives below the window interface; the identification of the
Lean extraction with it is measured (r271, warded G20/G23), not
formalized — part of the border transcription TODO (`SourceExact`).

**C1: the margin law demoted to a named Prop (the pair duplicate
retired).** The H5 margin law — r273-typed on `MainWindow`, r320-typed
on the canonical extraction — was carried as a `sorry` although the
fixed pair form is measured to MISS on kz39 (0.002 dec) and kz15
(0.06 dec) under b2LEVEL2: asserting it overclaimed (the law is a
CERTIFICATE ROUTE — 35 cheap rungs + both mains via the triangle,
5/7 exception rungs via the pair form — not a faithful statement of
the terminal hole). Since C1 it is the named Prop `PairMarginLaw` (the
`BorderedCompressionBridge` convention: statable, consumable, never
asserted) with the certificate direction PROVED
(`pair_closes_of_marginLaw`, via `canonical_split`). The terminal hole
itself is `terminal_q_canonical` and the unconditional pair closure
`pair_closes_main` is a PROVED corollary through the ONE named r263
dictionary lemma `pair_terminal_dictionary` (both
`RH/Canonical.lean`). What a proof of the law would still need is the
r271 lemma list L1–L5 (L2 pair-sum decay measured trending the wrong
way, sp(N, eps) = +0.67, r272).

### `RH/Canonical.lean` — THE CANONICAL FINAL DOMAIN (C1; the two true holes + the named dictionary)

| Item | Status | Content |
|---|---|---|
| `CanonicalCompletion`, `canonicalCompletion` | structure + **opaque constant** | the named completion data of the canonical window at anchor `a` (arch weights, v958 border column, r243 budget — signs carried by the type, VALUES opaque = the classical transcription TODO; the r326 opacity convention extended from the kernel reads) |
| `canonicalSpec`, `canonicalWindow` | definitions | the predefined family spec (`specFamily`, r310 — atoms/nodes/comb provable) with the named completion filled in, and its built real window |
| `canonicalSpec_arith`, `canonicalWindow_nodes/_combWeight`, `sourceExact_canonicalSpec`, `canonicalWindow_isExplicit`, `canonicalWindow_B_pos` | proved | the canonical spec shares the arithmetic layer with the family bitwise (`rfl`); it is source-exact in the transcribable r326 sense; the window is explicitly-main with positive budget |
| `CanonicalWindow` | definition | **the final quantifier domain**: `∃ a m ha, RepresentsWindow w (canonicalWindow a m ha) mesh` — the r320 predicate binds the certificate to the completed construction (u/B EXACT, separation discipline); no free `SourceExact`, no opaque window predicate; nonemptiness deliberately unprovable while the completion is opaque |
| `canonical_budget_pos` | **proved** | `0 < B` on canonical windows (B-fidelity + the completion's `budget_pos`) — the budget half of the old terminal sorry is now finite bookkeeping |
| `lstar_canonical` | **`sorry` — the base/wall hole** | L* on canonical windows (C1 retype of `lstar_subordination`; content verbatim v963; measured support through EXT6, N_w up to 7942, r354) |
| `terminal_q_canonical` | **`sorry` — the border/fiber hole, sharpened** | `q_N < 1` on canonical windows (C1 retype of `terminal_positive_main` minus the proved budget half); `terminal_canonical : TerminalPositive w` is a proved corollary |
| `augmented_prefix_positive`, `prefix_chain_positive_main`, `terminal_margin_positive_main`, `terminal_crossratio_main`, `lstar_free_window_main`, `free_window_positivity`, `augmentedSubordination_main`, `augmented_prefix_positive_via_ldagger` | proved from the two holes | the master theorem and every corollary, statements verbatim modulo the `MainWindow → CanonicalWindow` retype, proofs verbatim through the r305/r332 machinery |
| `pair_terminal_dictionary` | **`sorry` — the ONE named dictionary** | `Z² = (5/7)·q_N` on canonical windows (r263, measured exact 42/42); type MEASURED DICTIONARY / transcription-blocked (the border orthopoly transform); consumed ONLY by the pair closure |
| `pair_closes_main` | **proved** | the pair closure `Z²/M² < 1` (`M² = 5/7`) as a corollary of `terminal_q_canonical` through the dictionary — formerly conditioned on the retired `pair_margin_main` sorry |

### `RH/Selected.lean` — EXACT REAL DOMAIN AND THE MINIMAL QUANTIFIER (r397)

| Item | Status | Content |
|---|---|---|
| `RealCanonicalWindow` | structure | ℝ-fields, extends `PrimeWindow` plus `budget_pos`.  Not a parallel world: `toPrimeWindow` is definitional |
| `ExactPrimeSource`, `ExactArch`, `ExactBorder`, `ExactBudget`, `ExactFold`, `realCanonicalWindow` | definitions | `W^ℝ(a,m)` constructed totally; no emptiness question |
| `RepresentsRealCanonical` | definition | `RepresentsWindow` as a certificate over a `RealCanonicalWindow` |
| `selectedAnchor` / `selectedRoot` / `selectedMesh` / `selectedDelta` | definitions | `a_k = 2^k`, `r_k = ⌊√k⌋`, `m_k = k·2^{r_k}−1`, `Δ_k = log(a_k)/(m_k+1)` |
| `selectedDelta_eq`, `selectedAnchor_tendsto`, `selectedRoot_tendsto`, `selectedMesh_tendsto`, `selectedDelta_tendsto_zero`, `selected_covers` | **proved** (no `sorryAx`) | `Δ_k = 2^{−r_k}·log 2`; cofinality in anchor and mesh |
| `weil_nonneg_of_selected_windows` | **proved** (consumes the existing arch sorry) | `SelectedWindowLocalPositive → ∀ f, 0 ≤ weilForm f`.  Honest hypotheses: plain `fullRead` along the sequence, per-element onset and mesh coverage (proved by cofinality), existing `elementwise_finite_stabilization` |
| `SelectedMasterImpliesPlainReads` | named Prop | L†/master of `W^ℝ_k` ⇒ plain reads (not asserted).  **r434 OFF the FREQ mincut path** (eventual-strict master route) |
| `selected_augDualResolvent_gt_half` | named Prop — **stronger alternative** (r430) | `∀ᶠ k, (R†(W^ℝ_k) − ½·1).PosDef`.  Kept; not the mincut |
| `ExactArchAgreesWithArchRead` | named Prop | folded Exact arch vs `archRead` (classical).  **r434 OFF the FREQ theorems**; would be consumed by any *proof* of the remaining read-identification |

Zero `sorry` in this file.  Census stays 5.

### `RH/OneDefect.lean` — GENERAL ONE-DEFECT ABSORPTION (r406)

| Item | Status | Content |
|---|---|---|
| `indNeg_eq_zero_of_posDef` | **proved** | `H ≻ 0 ⇒ ind₋ H = 0` |
| `indNeg_sub_rankOne_le_one` | **proved** (SATZ A) | `H ≻ 0 ⇒ ind₋(H − ℓℓᵀ) ≤ 1` (corollary of `rankOne_inertia_antitone`) |
| `posDef_sub_rankOne_iff` | **proved** | `H ≻ 0 ⇒ (H − ℓℓᵀ ≻ 0 ↔ ℓᵀ H⁻¹ ℓ < 1)` (rank-1 Schur) |
| `woodbury_inv` | **proved** | `(H + U J Uᵀ)⁻¹ = H⁻¹ − H⁻¹ U K⁻¹ Uᵀ H⁻¹`, `K = J⁻¹ + Uᵀ H⁻¹ U` (home-built; mathlib has Schur / WA / `det_add_mul`, not Woodbury) |
| `oneDefect_update_posDef_iff` | **proved** (SATZ B) | `H ≻ 0`, `J ≻ 0 ⇒ (H − ℓℓᵀ + U J Uᵀ ≻ 0 ↔ 0 < Δ)` |
| `posDef_of_contractive_lift` | **proved** (SATZ C) | `Vᵀ` injective, `ℓ = V c`, `‖c‖² < 1 ⇒ (V Vᵀ − ℓℓᵀ) ≻ 0` |
| `cMin` / `cMin_normSq` | **proved** | `‖c_min‖² = ℓᵀ (V Vᵀ)⁻¹ ℓ` |
| `posDef_gram_sub_rankOne_iff` | **proved** | Gram-side Δ: `(V Vᵀ − ℓℓᵀ) ≻ 0 ↔ 0 < 1 − ‖c_min‖²` |

Zero `sorry` in this file.  Independent of R404/R405.  Census stays 5.

### `RH/GraphResolvent.lean` — GRAPH-RESOLVENT DICTIONARY (r412)

| Item | Status | Content |
|---|---|---|
| `graphResolvent` | **def** | alias of `lEnsemble`: $R=C(I+C)^{-1}$ |
| `graphResolvent_eq_one_sub_inv` | **proved** | $R=I-(I+C)^{-1}$ |
| `graphResolvent_eq_dualResolvent_inv` | **proved** | $C(I+C)^{-1}=(I+C^{-1})^{-1}$ |
| `graphResolvent_lt_one` / `graphResolvent_posDef` | **proved** | $0\prec R\prec I$ |
| `graphResolvent_sub_half_eq` | **proved** | $R-\tfrac12 I=\tfrac12(I+C)^{-1}(C-I)$ |
| `indNeg_one_add_inv_congruence` / `indNeg_inv_congruence` | **proved** | Sylvester sandwiches |
| `indNeg_graphResolvent_sub_half` | **proved** (a) | $\mathrm{ind}_{-}(R-\tfrac12 I)=\mathrm{ind}_{-}(C-I)$ |
| `indNeg_mobius` | **proved** (b) | $\mathrm{ind}_{-}(C-I)=\mathrm{ind}_{-}(I-C^{-1})$ |
| `posDef_one_sub_inv_iff` / `posSemidef_one_sub_inv_iff` | **proved** | Möbius PosDef / Loewner faces |
| `graphResolvent_gt_half_iff` | **proved** | $R\succ\tfrac12 I\iff C\succ I$ |
| `graphResolvent_ge_half_iff` | **proved** (r430) | $R\succeq\tfrac12 I\iff C\succeq I$ |
| `contractive_iff_gram_le_one` | **proved** | Euclidean contraction $\iff I-\mathfrak{T}^T\mathfrak{T}\succeq0$ |
| `energy_split_contractive` | **proved** (c) | $\mathfrak{T}^T\mathfrak{T}=C^{-1}\Rightarrow$ contraction $\iff C\succeq I$ |
| `energy_split_at_most_one` / `p1_coord_graphResolvent` | **proved** (c) | at most one excess singular value $\iff\mathrm{ind}_{-}(C-I)\le1$ |
| `augDualResolvent_gt_half_of_C_gt_one` | **proved** (d, zero-defect) | $C\succ I$ and $q^\dagger<1$ $\Rightarrow R^\dagger\succ\tfrac12 I$ |
| `GraphResolventIsLEnsembleInv` | named Prop | CD identification $E=C^{-1}$ on `RepresentsLEnsemble` |

Zero `sorry` in this file.  Does not assert (P1) on any window.  Census stays 5.

### `RH/EdgeBalance.lean` — EDGE-BALANCE CHAIN (r426)

| Item | Status | Content |
|---|---|---|
| `schWoodbury` / `phiBB` | **def** | `sch = den−2+sᵀ(H+UUᵀ)⁻¹s`, `φ_bb = den−2+sᵀH⁻¹s` |
| `phiBB_eq_cJ_add_selfEnergy` | **proved** | `φ_bb = c_J + Σ` |
| `schWoodbury_eq_oneDefectDelta` | **proved** (a) | `sch = (den−1) − Δ` at `J = I` |
| `schWoodbury_one_neg_iff_update` | **proved** (a) | at `den=1`, `sch<0` iff one-defect PosDef |
| `schWoodbury_eq_phiBB_sub` | **proved** (a) | `sch = φ_bb − rᵀK⁻¹r` |
| `schChart` / `chartEps` | **def** | three `{±1}`-signatures of the 3×3 chart |
| `schChart_eq_eps` | **proved** (b) | `sch = φ − (ε_a ã² + ε_b b̃²)` |
| `schChart_p1` / `_vacuous` / `_tot` | **proved** (b) | P1 / vacuous / tot specializations |
| `vacuous_sch_neg_iff` | **proved** (c) | vacuous `sch<0 ↔ τ² > φ` |
| `vacuous_live_of_phi_neg` | **proved** (c) | `φ<0` ⇒ whole disk live |
| `denOf` / `gammaOf` | **def** | `den = 1+γ−v_t·s`, `γ = ‖b‖²/B_w` |
| `den_lt_two_iff` | **proved** (d) | `den<2 ↔ γ < 1 + v_t·s` |
| `den_lt_two_of_gamma_lt_one` | **proved** (d) | `γ<1` and `v_t·s≥0` ⇒ `den<2` |
| `gamma_lt_one_of_le_S_lt_Bw` | **proved** (d) | `‖b‖² ≤ S < B_w` ⇒ `γ<1` |
| `parseval_normSq` | **proved** | coefficient identity ⇒ `‖b‖² = ∑ ⟨σ,π̂_k⟩²` |
| `BorderIsMuParseval` | named Prop | r424 `b_k = ⟨σ, π̂_k^μ⟩` |
| `BorderLoewnerLeS` | named Prop | r425 `‖b‖² ≤ S` (kernel Loewner) |
| `QNLtOne` | named Prop | r425 remainder `S < B_w` (`q_N<1`) |

Zero `sorry` in this file.  Does not assert (P1) or cofinal `q_N<1` on any window.  Census stays 5.

### `RH/FrequentlySelected.lean` — SEMIDEFINITE + FREQUENTLY SELECTED (r430)

Two quantifier wins against the existing extraction.  Zero `sorry`.
The FREQ theorems consume the existing arch-channel sorry; the
Loewner identities and the density / mean-value lemmas do not.

| Item | Status | Content |
|---|---|---|
| `Rdagger_ge_half_iff_augmented_posSemidef` | **proved** (in DualResolvent) | `R† ⪰ ½I` ⟺ augmented form PSD, given `Z ≻ 0`.  `#print axioms` = `[propext, Classical.choice, Quot.sound]` |
| `graphResolvent_ge_half_iff` | **proved** (in GraphResolvent) | `R ⪰ ½I` ⟺ `C ⪰ I` |
| `masterCap_posSemidef_iff_Rdagger_ge_half` | **proved** (r434) | real-window Loewner: `A_cap ⪰ 0` ⟺ `R† ⪰ ½I` under `RepresentsLEnsembleReal`.  `#print axioms` = `[propext, Classical.choice, Quot.sound]` |
| `masterCap_posDef_iff_Rdagger_gt_half` | **proved** (r434) | strict face: `A_cap ≻ 0` ⟺ `R† ≻ ½I` on `PrimeWindow` |
| `selectedWindowConeSemidef` | definition | PSD face of `selectedWindowCone` |
| `frequently_selected_augDualResolvent_ge_half` | **named Prop — THE NEW MINCUT** | `∃ᶠ k, (R†(W^ℝ_k) − ½·1).PosSemidef`.  Never a `sorry` |
| `SelectedSemidefImpliesPlainReads` | named Prop; **r434 theorem of the thinner remainder** | `R† ⪰ ½I` on window k ⇒ plain `fullRead`.  Follows from `SelectedACapPsdImpliesPlainReads` via the proved Loewner identification |
| `SelectedACapPsdImpliesPlainReads` | named Prop (r434 remainder) | `A_cap ⪰ 0` ⇒ plain `fullRead`.  Hankel/Weil-read identification (`BorderedCompressionBridge` + channel reads); NOT the dual-resolvent cone |
| `selectedWindowConeSemidef_implies_A_cap_posSemidef` | **proved** (r434) | FREQ cone ⇒ `A_cap ⪰ 0` |
| `selectedSemidefImpliesPlainReads_of_A_cap` | **proved** (r434) | thinner remainder ⇒ the r430 named bridge |
| `FrequentlySelectedInternalMincut` | named Prop (r463) | FREQ cone + `SelectedACapPsdImpliesPlainReads`; both premises visible |
| `internal_weil_nonneg_of_frequently_selected_of_A_cap` | **proved** (r463 rename) | named mincut + `SelectedACapPsdImpliesPlainReads` ⇒ `∀ f, 0 ≤ weilForm f` |
| `weil_nonneg_of_frequently_plain` | **proved** (consumes the existing arch sorry) | FREQ of plain `fullRead` ⇒ `∀ f, 0 ≤ weilForm f`.  Coverage eventual, positivity frequent |
| `weil_nonneg_of_frequently_selected` | **proved** (named bridge + arch sorry) | `∀ K ∃ k ≥ K, R_k† ⪰ ½I` ⇒ Weil ≥ 0 |
| `internal_weil_nonneg_of_frequently_selected` | **proved** (r463 honest name) | compound internal mincut ⇒ custom `GridElement` interface `∀ f, 0 ≤ weilForm f` |
| `frequently_selected_of_eventually_gt_half` | **proved** | r397 strict tail ⇒ r430 mincut |
| `frequently_of_pos_lower_density` | **proved** | density `≥ ε > 0` eventually ⇒ frequently |
| `exists_index_zero_of_block_mean_lt_one` | **proved** | `κ : ℕ → ℕ`, block mean `< 1` ⇒ a zero in the block |

Zero `sorry` in this file.  Repository census is 8 after r491
(three external bridge sorries in `RH/ExternalBridges.lean`).

**r440 mean tau index (no new Lean).**  T1/T2/MI2 are
finite identities, machine-checked in
`mean_tau_index_probe.py` / `mean_tau_index.tex`.  The
landing site above is the only Lean object this round
consumes.  The unconditional block-mean bound is open
(Reviewer-R439).  No new `sorry`; census stays 5.

**r442 unconditional block mean (no new Lean).**  The
dictionary `κ† = 1{q† > 1}` is machine-checked in
`block_mean_probe.py` / `block_mean.tex`.  The landing
site above is the only Lean object this round consumes.
The frequency bound is open.  No new `sorry`; census
stays 5.

**r443 selected delta floor (no new Lean).**  The
chart `δ = R + τ-correction` is machine-checked in
`delta_floor_probe.py` / `delta_floor.tex`.  The
liminf itself is open (slice census).  No new
`sorry`; census stays 5.

**r444 signed border mean (no new Lean).**  The
triple sum and pole/regular split are machine-checked
in `signed_border_mean_probe.py` / `signed_border_mean.tex`.
The mean bound is circular (named missing signed
strength).  No new `sorry`; census stays 5.

**r445 deep builder (no new Lean).**  The unused-Lanczos
hotspot, $k=8$ live pin, and $k=10/11/12$ ABD-ok census
are machine-checked in `deep_builder_probe.py` /
`deep_builder.tex`.  Infra only; no new `sorry`; census
stays 5.

**r446 deep ABD adjudication (no new Lean).**  The
REAL verdict on the $k=10/11/12$ ABD breaks and the
failed mesh repair at the $2^k$ anchors are
machine-checked in `deep_abd_probe.py` /
`deep_abd.tex`.  Infra only; no new `sorry`; census
stays 5.

**r447 exact-atom adjudication (no new Lean).**  The
EXACT_DEAD verdict on the true $k=10$ window
(mpmath atoms from exact integer sources) is
machine-checked in `exact_atom_probe.py` /
`exact_atom.tex`.  Infra only; no new `sorry`; census
stays 5.

**r448 exact living band (no new Lean).**  The
NOT_COFINAL / COMMENSURABILITY_REFUTED census
(exact deaths at kz170/197/230/137; next-odd
family fails) is machine-checked in
`exact_band_probe.py` / `exact_band.tex`.
Infra only; no new `sorry`; census stays 5.

**r449 flip vs stabilization (no new Lean).**  The
TAIL_ONLY census (every measured chain flip sits
past $n_{\mathrm{stab}}$; prefix-$R^{\dagger}$ lives)
is machine-checked in `flip_vs_stab_probe.py` /
`flip_vs_stab.tex`.  Infra only; no new `sorry`;
census stays 5.  The existing mincut already
consumes the stabilized `fullRead` prefix.

**r450 prefix mincut (definitional sharpening).**
`frequently_selected_prefix_augDualResolvent_ge_half`
is the existing frequently-cone (`Iff.rfl`).  No new
`sorry`; census stays 5.  Machine-checked in
`prefix_mincut_probe.py` / `prefix_mincut.tex`.

**r456 prefix vacuity (red-team).**
The r450 `Iff.rfl` is a *naming* of the full-cap cone,
not an `n_stab`-truncation.  Worlds test: Python prefix
MAIN = ARCH to machine precision (prime-blind);
arithmetic lives at grades `≥ J_P` and in `combRead`.
Mincut unchanged.  Census stays 5.  Machine-checked in
`vacuity_redteam_probe.py` / `vacuity_redteam.tex`.
Ausgang `VACUOUS_CONFIRMED`.  NO RH CLAIM.

**r463 mincut-path graph** (what
`internal_weil_nonneg_of_frequently_selected` actually consumes).
`#print axioms` on the extraction showed the historical arch
`sorryAx`; r638L removes that assertion and makes the arch contract an
explicit hypothesis. The two C1 holes do not appear.

| Satz | konsumiert | Status |
|---|---|---|
| `internal_weil_nonneg_of_frequently_selected` | compound mincut + explicit arch contract | **proved** as a function of those; internal Weil form only |
| `frequently_selected_augDualResolvent_ge_half` | — | **named mincut** (`∃ᶠ`, `PosSemidef`) |
| `SelectedACapPsdImpliesPlainReads` | — | **named remainder** (Hankel/`fullRead`) |
| `SelectedSemidefImpliesPlainReads` | Loewner + `SelectedACapPsdImpliesPlainReads` | **proved** from the remainder (`selectedSemidefImpliesPlainReads_of_A_cap`) |
| `masterCap_posSemidef_iff_Rdagger_ge_half` | `RepresentsLEnsembleReal` | **proved** (real-window L† ⟺ R† PSD) |
| `ArchGaussMellinDigammaIdentity` | — | **named, unasserted historical contract**; original exact-equality quantifier is overstrong |
| `lstar_canonical` | — | sorry, **OFF PATH** (alt route `L† ⟺ L* ∧ Terminal` on all `CanonicalWindow`s) |
| `terminal_q_canonical` | — | sorry, **OFF PATH** (alt route; global `q_N < 1` bypassed) |
| `pair_terminal_dictionary` | — | sorry, **OFF PATH** (pair-closure only) |
| `mainWindow_iff_builtFromPrimeSource` | — | sorry, **OFF PATH** (historical Alt-Last) |
| `SelectedMasterImpliesPlainReads` | — | named, **OFF PATH** (eventual-strict master route) |
| `GraphResolventIsLEnsembleInv` | — | named, **OFF PATH** (graph-resolvent face, not consumed by FREQ) |

The arrows beyond this internal endpoint are explicit in
`RH/ExternalBridges.lean`. Density and channel continuity are proved.
The corpus normalization contract
`StandardExplicitFormulaIdentification` is unasserted since r638L;
the honest-contour identification is proved. The Mathlib endpoint is
a proved wrapper around the remaining
`fullWeil_separates_offCritical_zeros` classical brick.

BYPASS VERDICT: yes — Selected-R† semidefiniteness bypasses
`terminal_q_canonical` / `lstar_canonical`.  The remaining named
extraction remainder is `A_cap ⪰ 0` ⇒ `fullRead ≥ 0`, which does
**not** follow from L† ⟺ R† (`fullRead` is the three-channel Weil
pairing, not the quadratic form of `A_cap`).

### `RH/Audit.lean` — THE FINAL AXIOM AUDIT (C1; `#print axioms` at every build)

Runs `#print axioms` on the sorry-free layer (expected: the three
standard axioms, NO `sorryAx`), the two canonical holes (now the
alternative route), the master chain, the Level-C extraction, the
r380 pivot-coordinate faces (section (i)), the r384 flank-entry
faces (section (j)), the r397 selected-domain identities
(section (k): sequence and conditional extraction theorems NO
`sorryAx`),
and the r406 one-defect finite algebra (section (l): all
eight theorems NO `sorryAx`);
and the r412 graph-resolvent finite algebra (section (m): all
audited theorems NO `sorryAx`);
and the r426 edge-balance finite algebra (section (n): all
audited theorems NO `sorryAx`);
and the r430 semidefinite / frequently-selected layer
(section (o): Loewner faces, density, mean-value and conditional FREQ
extraction NO `sorryAx`);
and the r434 quantifier-mincut audit (section (p): real-window
Loewner and collapsed conditional FREQ interface NO `sorryAx`);
the C1 record is quoted verbatim in the claim-boundary
block above and in the file itself.

## TODO (second stage)

- ~~Prove the Inertia layer against mathlib (`Matrix.PosDef` API).~~
  DONE r305 except `crossing_budget`; ~~`crossing_budget`~~ DONE C1
  (Jacobi's rule as an LDL congruence + mathlib's Sylvester law —
  `RH/Inertia.lean` is sorry-free).
- ~~Formalize the r263 dictionary `Z²/m = q_N` connecting the terminal
  hole with the pair coordinates, so the terminal hole is ONE Lean
  statement.~~ DONE C1 as the ONE named (typed, transcription-blocked)
  lemma `pair_terminal_dictionary` (`RH/Canonical.lean`); the pair
  closure is a proved corollary, the margin law a named Prop.
  REMAINING (named): prove the dictionary itself once the border
  orthopoly transform (v958 column) is transcribed.
- C1 OPEN (named): eliminate the opaque `canonicalCompletion`
  (`RH/Canonical.lean`) — the same arch/border/budget transcription
  TODO that eliminates `SourceExact` and the opaque kernel reads; then
  `CanonicalWindow` becomes fully constructive and the dictionary
  lemma becomes provable window algebra.
- ~~Formalize the extraction of the r271 pair data (`Zloc`, `runs`) from
  `VonMangoldtWindow` (currently a hypothesis of `pair_margin_main`).~~
  DONE r320 as the canonical definition `edgeLocal`/`bulkRuns` with the
  proved `canonical_split` (U3 repair). REMAINING: identify the Lean
  extraction with the probe-side F = 0.20 mesh-cell extraction
  (measured r271, not formalized — border transcription TODO).
- r320 OPEN (named): eliminate `SourceExact` (`RH/Source.lean`) — the
  arch-kernel (`arch_A`), border-column (v958) and fold-map
  transcriptions; then the bridge becomes definitional under the
  invasive route. Also named open: the mesh-vs-anchor cofinality seam
  (identify the `specFamily` refinement tower with the v749 canonical
  tower and transport window positivity into the (H_cof) shape — see
  the seam block in `RH/Source.lean`).
  **r326/r376 update on both**: `SourceExact` is eliminated as a free
  assumption FROM THE EXTRACTION ROUTE (`RH/Elementwise.lean`:
  `CanonicalPrimeWindow` + the proved `sourceExact_buildPrimeWindow`;
  the opaque predicate itself stays, related by the named Prop
  `SourceExactOfFamilyCompletion`) — the transcriptions above remain
  the named TODO (they now additionally discharge the remaining
  arch-channel sorry and the opaque reads `archRead`/`weilArchSide`;
  pole reads are transcribed); the seam
  identification is SUPERSEDED as a goal by the elementwise
  architecture (no (H_cof) tower is consumed anywhere; the seam block
  carries the r326 update).
- r376 OPEN (named, `RH/Elementwise.lean`): (a) the arch kernel
  transcription (`arch_A` GL-48 tent integrals identified with
  `weilArchKernel` via Gauss/Mellin — mathlib gap) — turns the
  remaining classical sorry into a provable quadrature statement;
  named (not a hole): `PoleDyadicIndependence`; (b) the bordered-form transcription + the compression
  bridge `BorderedCompressionBridge` as a theorem (the odd-compression
  step; needs the border/fold data — part of the `SourceExact`
  elimination); (c) the window-local positivity premise
  `WindowLocalPositive` itself is Level B — the two true holes,
  untouched by this round.
- Give `MainWindow` its arithmetic content (the von-Mangoldt comb
  instantiation) only if/when a promotion wave needs it.
  **Partially addressed r310** (`RH/Source.lean`): the explicit content
  is constructed (`PrimeWindowSpec`/`buildPrimeWindow`/
  `MainWindowExplicit`); **refined r310b**: four-stage support chain
  with the explicit folding aggregation `foldedWindow` + the four
  source theorems, bridge in the reviewer target form. What remains is
  the invasive step — replace the opaque `MainWindow` by
  `fun w => ∃ s, RepresentsWindow w (buildPrimeWindow s) s.mesh` and
  re-check all dependents (then `mainWindow_iff_builtFromPrimeSource`
  becomes `Iff.rfl`), plus the border/budget fidelity (v958 column,
  r243 budget), the exact archimedean transcription (Weil kernel
  `arch_A` — classical analysis) and the corpus fold-map transcription
  (fold fidelity of the certificates).
- Keep SPEC SHAs in headers in sync with `rh/INVENTORY.json` on every wave.
- r380 OPEN (named, `RH/PivotCoordinate.lean`, not census holes):
  `ComplementaryDualHankelInertia`, `DPPIdentity`,
  `SignedBorodinComplement`, `K2EqHankelRatio`, `P1EqCapInertia`,
  `P2EqPostcapAlternation` — discrete CD / Borodin OP construction of
  the dual ensemble and of R (same class as DualResolvent's
  `CauchyInterlace`; mathlib v4.29.1 has no CD kernel / discrete OPE).
  The rank-1 inertia, adaptive band, Vandermonde Gram, h-ratio
  telescope, and Jacobi synthesis are PROVED.
- r384 OPEN (named, `RH/FlankEntry.lean`, not census holes):
  `FlankEntryPrefix` (the r382 inductive core: (F1)+(F2_{2/3}) ⇒
  positive pivots through `⌊2N/5⌋`) and `ChristoffelPivotBound`
  (general-k comparison `h_k(w) ≥ (1−λ) h_k(μ)` via the CD kernel;
  mathlib v4.29.1 has Hankel dets and completing-the-square for
  k ≤ 1, not the μ-orthonormal CD basis).  Pair energy, h₀/h₁,
  the ℚ toys, Christoffel k=0,1, and the adaptive-band bridge
  are PROVED.
