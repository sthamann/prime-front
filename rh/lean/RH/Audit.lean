/-
RH/Audit.lean -- THE FINAL AXIOM AUDIT (C1, the reviewer final-domain
contract, goal 4): `#print axioms` on the main theorem chain, run at
every build.

Results are recorded verbatim below after each command (and mirrored
in rh/lean/README.md).  The audit target: the master theorem and its
corollaries may consume ONLY the two canonical arithmetic window
holes (`lstar_canonical`, `terminal_q_canonical` -- both entering as
`sorryAx`), the named dictionary/classical imports (also `sorryAx`,
each individually typed at its statement), and the three standard
mathlib axioms `propext`, `Classical.choice`, `Quot.sound`.  The
sorry-free layer (the reconstruction theorem, the L† equivalences,
`crossing_budget`, the r373 Haynsworth theorems, the r373 dual-resolvent
bridge) must show the three standard axioms ONLY -- in
particular NO `sorryAx`: machine-checkable freedom from hidden holes.

NOTE on `#print axioms` granularity: Lean reports `sorryAx` once,
without naming which sorried declarations feed it.  The reduction "the
master consumes exactly the two canonical holes" is therefore checked
in two machine-verifiable halves: (a) the hypothesis-form
reconstruction `lstar_terminal_implies_master` is sorry-free (audited
below), and (b) the canonical master is literally its application to
`lstar_canonical`/`terminal_canonical` (one-line proof term,
RH/Canonical.lean) -- no other sorried name occurs in the proof.

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Canonical
import RH.DualResolvent
import RH.Haynsworth
import RH.Elementwise
import RH.PivotCoordinate
import RH.FlankEntry
import RH.Selected
import RH.OneDefect
import RH.GraphResolvent
import RH.EdgeBalance
import RH.FrequentlySelected
import RH.ExternalBridges
import RH.GaborExplicitFormula
import RH.GaborDominance
import RH.GaborCountableCriterion
import RH.CoxeterCompletion
import RH.PrimeLogIndependence

namespace RH

/-! ## (a) The sorry-free load-bearing layer
Expected AND MEASURED (C1 record, verbatim build output):
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`:
  * `RH.lstar_terminal_implies_master`
  * `RH.augmentedSubordination_iff_lstar_and_terminal`
  * `RH.crossing_budget`
  * `RH.canonical_budget_pos` -/

-- the r305 reconstruction theorem (hypothesis form)
#print axioms lstar_terminal_implies_master
-- the r332 L† equivalence (hypothesis form)
#print axioms augmentedSubordination_iff_lstar_and_terminal
-- the Jacobi/Sylvester crossing budget -- PROVED since C1
#print axioms crossing_budget
-- the canonical budget positivity (the proved half of the old
-- terminal statement)
#print axioms canonical_budget_pos

/-! ## (b) The two canonical arithmetic holes (the final domain)
Expected AND MEASURED: `[propext, sorryAx, Classical.choice,
Quot.sound]` -- each IS a typed `sorry`. -/

#print axioms lstar_canonical
#print axioms terminal_q_canonical

/-! ## (c) The main theorem chain on the final domain
Expected AND MEASURED: `[propext, sorryAx, Classical.choice,
Quot.sound]`, the `sorryAx` entering ONLY through (b) -- see the
granularity note in the header: the proof terms apply the sorry-free
layer (a) to the two holes (b) and to nothing else (the pair closure
additionally consumes the ONE named dictionary import
`pair_terminal_dictionary`, typed transcription-blocked). -/

#print axioms augmented_prefix_positive
#print axioms augmentedSubordination_main
#print axioms terminal_crossratio_main
#print axioms prefix_chain_positive_main
#print axioms free_window_positivity
#print axioms pair_closes_main

/-! ## (d) The Level-C extraction (classical kernel imports)
r638L: expected `[propext, Classical.choice, Quot.sound]` -- NO
`sorryAx`.  The ladder-free extraction is now a function of the
unasserted `ArchGaussMellinDigammaIdentity` contract; it no longer
asserts the overstrong exact quadrature identity.  The comb channel is
unconditional and the pole channel is PROVED as the native-mesh
second-difference pairing of `polePotential`. -/

#print axioms weil_nonneg_of_windowlocal
#print axioms pole_elementwise_stabilization

/-! ## (e) The r362/r373 dual-resolvent layer (reviewer priority 2)
Sorry-free finite algebra AND the window bridge, expected AND MEASURED:
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`:
  * `RH.posDef_one_sub_iff_dualResolvent_gt_half` (r356-A / A2)
  * `RH.posDef_one_sub_borderedGram_iff_augDualResolvent` (A3)
  * `RH.posDef_one_sub_borderedGram_iff_qDagger` (A5)
  * `RH.augDualResolvent_fromBlocks` (A4 Sherman–Morrison)
  * `RH.augDualResolvent_gt_smul_implies_dualResolvent` (A7-min)
  * `RH.augmentedSubordination_iff_dualResolvent` -- r373: the μ-ONB
    Gram transcription `RepresentsLEnsemble` is a real Prop (whitening
    equations, R319); the iff is congruence of `A_cap` onto `I − G†`
    then A3.  Census 8 → 7.  NO RH CLAIM. -/

#print axioms posDef_one_sub_iff_dualResolvent_gt_half
#print axioms posDef_one_sub_borderedGram_iff_augDualResolvent
#print axioms posDef_one_sub_borderedGram_iff_qDagger
#print axioms augDualResolvent_fromBlocks
#print axioms augDualResolvent_gt_smul_implies_dualResolvent
#print axioms augmentedSubordination_iff_dualResolvent

/-! ## (f) The r373 Haynsworth layer (reviewer goal 1)
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx`.  Finite real algebra; does not assert r367 P1/P2 on
any window. -/

#print axioms haynsworth_two_rank
#print axioms haynsworth_mixed
#print axioms haynsworth_sigNeg_₁₁
#print axioms haynsworth_sigNeg_₂₂

/-! ## (g) r373/r376 kernel objects
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx` on the transcribed closed forms, and NO `sorryAx` on
`pole_elementwise_stabilization` (r376).  The arch stabilization
sorry remains in (d). -/

#print axioms polePotential_even
#print axioms polePotential_eq_cosh
#print axioms weilArchKernel_even

/-! ## (h) Historical opacity bridge (Alt-Last, not a load-bearing hole)
`mainWindow_iff_builtFromPrimeSource` (RH/Source.lean) is the r310/r320
opacity bridge.  Since C1 the load-bearing chain quantifies over
`CanonicalWindow`, not `MainWindow`.  The bridge is consumed only by
`mainWindow_explicit_bridge` (itself a corollary of the bridge).  It
is an Alt-Last of the historical interface, not an arithmetic or
classical hole; it is NOT deleted (the r273 opaque marker and the
U1–U3 guards still refer to it).  Expected: `[propext, sorryAx,
Classical.choice, Quot.sound]`. -/

#print axioms mainWindow_iff_builtFromPrimeSource

/-! ## (i) The r380 pivot-coordinate layer (DCCXXXVII finite algebra)
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx` on the proved faces.  Named Props
(`ComplementaryDualHankelInertia`, `DPPIdentity`,
`SignedBorodinComplement`, `K2EqHankelRatio`, `P1EqCapInertia`,
`P2EqPostcapAlternation`) are hypotheses, not holes.  Census
unchanged at 5.  Does not assert (P1)/(P2) on any window.
NO RH CLAIM. -/

#print axioms rankOne_inertia_antitone
#print axioms adaptive_band_from_entry
#print axioms sigNeg_full_hankel_eq_sigNeg_weights
#print axioms postcap_pivot_ratio_eq_h_form
#print axioms indNeg_hankel_eq_neg_pivot_count
#print axioms p1_p2_iff_cap_posDef

/-! ## (j) The r384 flank-entry layer
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx` on the proved faces.  Named Props (`FlankEntryPrefix`,
`ChristoffelPivotBound`) are hypotheses, not holes.  Census
unchanged at 5.  Does not assert (P1)/(P2) or L* on any window.
NO RH CLAIM. -/

#print axioms pair_energy_identity
#print axioms h_zero
#print axioms h_one
#print axioms h0_pos_of_mass
#print axioms h1_pos_of_pairEnergy
#print axioms three_atom_mass_pos
#print axioms threeAtom_flank_pivots
#print axioms clusterRun3_H3
#print axioms fiveAtom_energy
#print axioms christoffel_bound_k0
#print axioms christoffel_bound_k1
#print axioms threeAtom_christoffel_k1
#print axioms indNeg_entry_of_flank
#print axioms adaptive_band_from_flank_entry

/-! ## (k) The r397 exact selected domain
Expected AND MEASURED: the sequence identities and cofinality
theorems are sorry-free
(`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`).
r638L makes `weil_nonneg_of_selected_windows` an explicit function of
`ArchGaussMellinDigammaIdentity`; no arch `sorryAx` is consumed.
Named Props (`selected_augDualResolvent_gt_half`,
`SelectedMasterImpliesPlainReads`, `ExactArchAgreesWithArchRead`)
are hypotheses, not holes.  Census of `sorry` declarations
unchanged at 5; the two C1 holes are degraded to the alternative
route.  NO RH CLAIM. -/

#print axioms selectedDelta_eq
#print axioms selectedAnchor_tendsto
#print axioms selectedRoot_tendsto
#print axioms selectedMesh_tendsto
#print axioms selectedDelta_tendsto_zero
#print axioms selected_covers
#print axioms realCanonicalWindow_B_pos
#print axioms ExactFold_B
#print axioms weil_nonneg_of_selected_windows
#print axioms weil_nonneg_of_selected_master

/-! ## (l) The r406 one-defect finite algebra
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx`.  Pure finite real matrix algebra (Schur rank-1
criterion, Woodbury identity, Cauchy--Schwarz Gram lift).
Independent of the source-side R404/R405 probes.  Census of
`sorry` declarations unchanged at 5.  NO RH CLAIM. -/

#print axioms indNeg_eq_zero_of_posDef
#print axioms indNeg_sub_rankOne_le_one
#print axioms posDef_sub_rankOne_iff
#print axioms woodbury_inv
#print axioms oneDefect_update_posDef_iff
#print axioms posDef_of_contractive_lift
#print axioms cMin_normSq
#print axioms posDef_gram_sub_rankOne_iff

/-! ## (m) The r412 graph-resolvent finite algebra
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx`.  Pure finite real matrix algebra (spectral dictionary
of `R = C(I+C)⁻¹`, Möbius inertia, energy-split contraction).
Named Prop `GraphResolventIsLEnsembleInv` is a hypothesis, not a
hole.  Census of `sorry` declarations unchanged at 5.  NO RH CLAIM. -/

#print axioms graphResolvent_eq_one_sub_inv
#print axioms graphResolvent_eq_dualResolvent_inv
#print axioms graphResolvent_lt_one
#print axioms graphResolvent_posDef
#print axioms graphResolvent_sub_half_eq
#print axioms indNeg_one_add_inv_congruence
#print axioms indNeg_inv_congruence
#print axioms indNeg_graphResolvent_sub_half
#print axioms indNeg_mobius
#print axioms posDef_one_sub_inv_iff
#print axioms posSemidef_one_sub_inv_iff
#print axioms graphResolvent_gt_half_iff
#print axioms graphResolvent_ge_half_iff
#print axioms contractive_iff_gram_le_one
#print axioms energy_split_contractive
#print axioms energy_split_at_most_one
#print axioms p1_coord_graphResolvent
#print axioms augDualResolvent_gt_half_of_C_gt_one

/-! ## (n) The r426 edge-balance finite algebra
Expected AND MEASURED: `[propext, Classical.choice, Quot.sound]` --
NO `sorryAx`.  Pure finite real algebra (Woodbury-sch corollary of
OneDefect, 3×3 chart trichotomy, vacuous τ²-separator, den formula).
Named Props `BorderIsMuParseval`, `BorderLoewnerLeS`, `QNLtOne` are
hypotheses, not holes.  Census of `sorry` declarations unchanged
at 5.  NO RH CLAIM. -/

#print axioms phiBB_eq_cJ_add_selfEnergy
#print axioms schWoodbury_eq_oneDefectDelta
#print axioms schWoodbury_one_neg_iff_update
#print axioms schWoodbury_eq_phiBB_sub
#print axioms schChart_eq_eps
#print axioms schChart_p1
#print axioms schChart_vacuous
#print axioms schChart_tot
#print axioms vacuous_sch_neg_iff
#print axioms vacuous_live_of_phi_neg
#print axioms den_lt_two_iff
#print axioms den_lt_two_of_gamma_lt_one
#print axioms gamma_lt_one_of_le_S_lt_Bw
#print axioms den_lt_two_of_le_S_lt_Bw
#print axioms parseval_normSq
#print axioms gamma_lt_one_of_named

/-! ## (o) The r430 semidefinite / frequently-selected layer
Expected AND MEASURED: the Loewner identities and the FREQ
extraction (plain) plus density / mean-value arithmetic are
sorry-free.  Since r638L `weil_nonneg_of_frequently_plain`,
`weil_nonneg_of_frequently_selected`, and
`internal_weil_nonneg_of_frequently_selected` take
`ArchGaussMellinDigammaIdentity` explicitly, so their expected axiom
set is `[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
The spectral Loewner faces and the arithmetic lemmas are
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
Named Props (`frequently_selected_augDualResolvent_ge_half`,
`frequently_selected_prefix_augDualResolvent_ge_half`,
`SelectedSemidefImpliesPlainReads`) are hypotheses, not holes.
The r450 prefix name is `Iff.rfl`-identical to the mincut
as a *Lean name* (r456: withdrawn as an `n_stab`
compression / RH-path reduction).
Census of `sorry` declarations unchanged at 5.  The r397 Prop
`selected_augDualResolvent_gt_half` is the stronger alternative.
NO RH CLAIM. -/

#print axioms posSemidef_nonsingInv_sub_smul_iff
#print axioms posSemidef_one_sub_iff_dualResolvent_ge_half
#print axioms Rdagger_ge_half_iff_augmented_posSemidef
#print axioms graphResolvent_ge_half_iff
#print axioms selectedWindowConeSemidef_of_posDef
#print axioms frequently_selected_iff_forall_exists
#print axioms frequently_selected_of_eventually_gt_half
#print axioms weil_nonneg_of_frequently_plain
#print axioms frequently_plain_of_frequently_selected
#print axioms weil_nonneg_of_frequently_selected
#print axioms internal_weil_nonneg_of_frequently_selected
#print axioms frequently_of_pos_lower_density
#print axioms frequently_selected_of_pos_lower_density
#print axioms exists_index_zero_of_block_mean_lt_one

/-! ## (p) The r434 quantifier-mincut audit
Expected AND MEASURED: the real-window Loewner identification
(`masterCap_posSemidef_iff_Rdagger_ge_half`,
`masterCap_posDef_iff_Rdagger_gt_half`,
`selectedWindowConeSemidef_implies_A_cap_posSemidef`,
`posSemidef_congruence_iff`) is sorry-free
(`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`).
`selectedSemidefImpliesPlainReads_of_A_cap` is the same
(a function of the named remainder, no hole).
`internal_weil_nonneg_of_frequently_selected_of_A_cap` is also an
explicit function of the unasserted arch contract, so its expected
axiom set is `[propext, Classical.choice, Quot.sound]`.

MINCUT-PATH CENSUS (what `internal_weil_nonneg_of_frequently_selected` actually
consumes):
  ON PATH, named hypothesis: `ArchGaussMellinDigammaIdentity`
    (historical exact-equality contract, known overstrong);
  Historical r461 sealed text-audit marker:
  ON PATH, formerly-sorry: `arch_elementwise_stabilization`
  ON PATH, named: `frequently_selected_augDualResolvent_ge_half`
    (the mincut) and `SelectedReadQuadraticRepresentation` (exact
    channel direction; r464 proves the finite PSD implication to
    `SelectedACapPsdImpliesPlainReads`).
  OFF PATH, sorry (alternative rational-certificate route):
    `lstar_canonical`, `terminal_q_canonical`,
    `pair_terminal_dictionary`, `mainWindow_iff_builtFromPrimeSource`.
  OFF PATH, named: `SelectedMasterImpliesPlainReads`,
    `GraphResolventIsLEnsembleInv`, `ExactArchAgreesWithArchRead`
    (the last would be consumed by any *proof* of the remaining
    read-identification, not by the FREQ theorems).
Census of asserting `sorry` declarations is 5 after r638L.  NO RH
CLAIM. -/

/-! ARCH RATE REPAIR: `SelectedArchErrorQuadraticRate` is FALSIFIED.
`SelectedArchErrorQuadraticRateExists` is OPEN pending
`SelectedArchWeightedInterpolationEstimate`; its tendsto theorem is PROVED. -/

#print axioms posSemidef_congruence_iff
#print axioms PrimeWindow.hankel_eq_comb_sub_arch
#print axioms PrimeWindow.A_eq_bordered
#print axioms muWhitening_congruence_real
#print axioms masterCap_posSemidef_iff_Rdagger_ge_half
#print axioms masterCap_posDef_iff_Rdagger_gt_half
#print axioms selectedWindowConeSemidef_implies_A_cap_posSemidef
#print axioms selectedACapPsdImpliesPlainReads_of_representation
#print axioms selectedSemidefImpliesPlainReads_of_A_cap
#print axioms internal_weil_nonneg_of_frequently_selected_of_A_cap
#print axioms selectedACapPsdImpliesPolynomialReads
#print axioms PrimeWindow.hankel_quadform
#print axioms fullRead_weilForm_gap_eq_arch
#print axioms selected_reads_ge_neg_archError_of_approx
#print axioms weilForm_ge_neg_two_archError_of_joint
#print axioms productionArchDelta_tendsto_atTop
#print axioms selectedArchError_tendsto_zero_of_rate

/-! ## (q) The r463/r487/r489/r491 explicit external-bridge census
r489 proves finite comb continuity and continuity of the standard
polar integral, strengthens the topology to uniform-on-fixed-support
plus `L¹`, and consolidates density, arch continuity, and the r376
native-grid pole dictionary into one typed completion `sorry`.
External census returns from four to three; repository census 9 -> 8.
`grid_dense_extension` remains a proved positivity-limit wrapper.
The Mathlib endpoint wrapper is proved from the one named
off-critical separation theorem.

r491 corrects the polar integral sign (`+2 cosh`, because the r376
pairing has an outer minus), makes `fullWeilArchSide` concrete, and
retypes the dense component around the explicit support-fitting
`dyadicSampleGrid`.  The remaining pole seam is the exact finite-hat
identity `GridPoleHatIntegralIdentity`; its implication to the
sequence dictionary is proved.  Completion still has three
components (dyadic convergence, arch continuity, pole hat identity),
so census honestly remains 8.  No hidden two-component closure is
claimed.

r493e proves Dini / u-space arch continuity
(`fullWeil_arch_continuity`, `fullWeil_arch_side_tendsto`) from
the common Lipschitz majorant and dominated convergence on
`Ioc 0 R`.  The completion theorem is now that proved arch
statement.  External census 3 → 2; repository census 8 → 7.
The remaining two outer-bridge `sorry`s are the Guinand–Weil
dictionary and off-critical separation.

r638L retires the gauge-mismatched corpus
`standard_explicit_formula_identification` assertion: the historical
Prop remains unasserted, while
`standard_explicit_formula_identification_honest` is the proved
dictionary.  External census 2 → 1 and repository census 7 → 5; the
remaining external `sorry` is off-critical compact separation.

r497 scopes the remaining lane: [2] before [3], because [3] is
stated on the opaque `standardExplicitFormula`.  Brick [2a] is
the proved finite-positive analytic order of `riemannZeta` at
every non-polar zero
(`riemannZeta_analyticOrderAt_finite_pos`).  r498 proves the
[2b] residue calculus at non-polar zeros
(`logDeriv_riemannZeta_eq_multiplicity_div_add_analytic`,
`tendsto_mul_logDeriv_riemannZeta`, meromorphy on `ℂ \ {1}`).
r499 proves local finiteness of non-polar zeros and finiteness
on every compact / closed strip rectangle
(`finite_riemannZeta_zeros_on_closedRect`).
r500 completes [2b]: holomorphic filling of `(s-1)ζ(s)` at
the pole, `ζ'/ζ = -1/(s-1) + analytic`, and
`MeromorphicOn (logDeriv riemannZeta) univ`.  [2c] cut 2
exposes `spectralPartialSum` as a finite rectangle sum
(interface only).
r501 scopes the zero-count (Jensen yes, `N(T)` / Hadamard
product no) and proves the spectral kernel
`FullWeilTest.hat` with exponential-type envelope
(`norm_hat_le_exp`).  r503 proves the ACF second
difference `O(δ²)` bound
(`autocorrelation_second_diff_le`,
`FullWeilTest.abs_second_diff_le`) and hat
translation (`hat_comp_sub`).  r504 adds the
two-step translation (`hat_comp_sub_twice`).
r505 lands the Weierstrass identity
(`hat_mul_weierstrass`) and `e^{sδ} = -e^{σδ}`
(`exp_mul_pi_div_abs_im`); the `1/t²` consumer is
parked as `FullWeilTest.NormHatLeInvSq`.  ζ-side:
termwise Dirichlet comparison and `1/ζ = L(μ)`
are in; `|ζ| ≤ |ζ(2)|` remains a named Prop.
r506 proves the parked strip bound
(`FullWeilTest.norm_hat_le_inv_sq`) and the
Dirichlet majorants `‖ζ(s)‖ ≤ ‖ζ(2)‖`,
`‖1/ζ(s)‖ ≤ ‖ζ(2)‖` on `Re s ≥ 2`.  ĥ-side of
[2c] is complete.  r507 lands FE pairing
(`riemannZeta_one_sub_eq_zero_of`) and the
Γ-free Euler–Maclaurin skeleton (FTC cell,
telescoping, `{x}`-cells, cell majorant).
r508 assembles the N=1 formula on `Re s>1`
and the poly bound there.  r509 fills
`ζ = s/(s-1) − s·I` to `{Re s>0, s≠1}`
by Weierstrass + identity theorem, and
extends the poly bound to `{Re>δ}`.
r510 proves the filling bound without `|s-1|≥1/2`
and the centre lower bound `|F(2+iT)| ≥ 1/|ζ(2)|`.
Jensen's formula is `Real.circleAverage` plus
`MeromorphicOn.circleAverage_log_norm`.  r511
proves the disk card
(`zetaZerosInDisk_card_le`,
`jensenDiskZeroCountBound`) with explicit
`C = (log K + log‖ζ(2)‖ + 2) / log(7/6)`.
r512 proves the height count
(`zetaZeroCountUpToXBound`) on the critical-strip
rectangle `[0,1]×[-X,X]` via the `r=13/8` disk
(`w=5/8`) and FE pairing.  r513 assembles the
dyadic sum `∑ 1/|ρ|² < ∞`
(`summable_inv_sq_zetaZeros`); [2c] counting is
complete.  r514 starts [2d]: rectangle winding
`rectangleIntegral_inv_of_zero_mem` (`∮ 1/z = 2πi`
on a positively oriented rectangle about `0`).
r515 wraps one and many simple poles
(`rectangleIntegral_simple_pole`,
`rectangleIntegral_sum_simple_poles`) and
bounds `|ζ'/ζ|` on `Re ≥ 2`.
r516 glues the punched `(ζ'/ζ)·F` remainder
(`exists_analyticAt_update_of_meromorphicOrderAt_nonneg`,
`logDerivHatRemainder`).
r517: `ĥ` entire, filled remainder on `Q_T`,
`contour_identity_fixed_T`.
r518: ĥ-decay on compact Re
(`norm_hat_le_inv_sq_on_contour`), Dirichlet
at Re ≥ 5/4, Lücken-Lemma
(`exists_gap_height`).
r519: Mathlib Borel–Carathéodory wrapped to
general balls; `logDeriv` primitive +
`norm_logDeriv_le_of_log_norm_le`.
r520: contour revision to the r510-safe
horizontal `[1/2, 2]`; logDeriv dictionary,
`landauPoly`, Jensen `Σ m`, gap sum
`O(log² T)`.
r521: `horizontalEdgeLandauBound` — `g = F/P`
update-fill, mid-sphere max modulus, r519
kernel; Prop closed on `σ ∈ [1/2, 2]`.
r522: parametric `contour_identity_fixed_T_of`
on `σ₁ ∈ (-1/4, 0)` and the `-1/16`
instance; r499 Finset bridge; two-sided
`exists_gap_height_abs`; horizontal
length×sup template.  `HorizontalEdgesTendstoZero`
stays a named Prop (sliver FE/`ψ` and the
`A=1` vs `ordinateGapConst` gap).
r523: wide `exists_gap_sequence_landau`
(Landau-disk window) and the `ψ` kernel
`sum_digamma_kernel_norm_le`.
r524: A-parametric
`horizontalEdgeLandauBound_of_gap` (B =
A · `landauHorizontalConst`) and
`horizontalEdgeLandauBound_landauGap`;
n>T tail `sum_digamma_kernel_tail_le`.
`DigammaHorizontalLogBound` stays named
(Mathlib: `logDeriv Gamma`, no series).
r525: route A (real convexity → series on
`(1,2)` → identity on the sliver strip)
chosen; the real-from-complex glue did not
close.  Prop narrowed to `Re ∈ [1/2, 17/16]`.
r526: `hasDerivAt_re_Gamma_ofReal` via
`HasDerivAt.real_of_complex` + `div_ofReal_re`;
Weierstrass on `(1,2)`; identity on
`{1/4 < Re < 2}`; `|ψ|` log bound.  The Prop
is now a theorem (`digammaHorizontalLogBound`).
r527: tan/cot on `|Im|≥2`; `ψ` sliver via
recurrence; FE `logDeriv`; lower-edge
`sliverEdgeBound_negIm`.  Horizontals stay
named.  Census stays 7.
r528: Schwarz `ζ(conj s)=conj(ζ s)` off the
pole; upper sliver + lower Landau by
reflection; glued `|ζ′/ζ|` on
`[-1/16,2]×{±T}`; `horizontalEdgesTendstoZero`.
Left edge and `T→∞` assembly stay named.
Census stays 7.
r529: left edge restated to `Re=-1/16`;
`leftEdgeLogDerivBound` is a theorem (FE +
Dirichlet at `17/16` + sliver `ψ`/`tan`,
gap-free).  Right-edge Dirichlet + pointwise
`ĥ` majorants.  `T→∞` identity stays named
(vertical `Integrable` + Finset exhaustion).
Census stays 7.
r530: vertical integrands are `Integrable` on `ℝ`
(right: Dirichlet × `1/(1+τ²)`; left: compact
bound plus `log/(1+τ²)` tail).  Weighted
`Summable (m_ρ ĥ(ρ))` by dyadic log-weight
blocks; Finset exhaustion along Landau `T_k`;
`contourIdentityLimitAlongGaps` is a theorem.
Census stays 7.
r531: `standardExplicitFormula` is the spectral
pairing `Re(∑ m_ρ ĥ(ρ) − ĥ(1))` (opaque retired).
Paley--Wiener slice `hatSlice`,
`hat_eq_fourier_slice`, integrable Fourier
transform, `fourierInv_hatSlice`, and the
`2π` form `hat_fourier_inversion` are
theorems.  Identification sorry stays; census
stays 7.
r532: the right vertical is the prime channel,
`∫ (ζ′/ζ)(2+iτ) ĥ dτ = -2π ∑ Λ(n) g(log n)`
(`rightVerticalIntegral_eq_prime_sum`), via
termwise Fourier inversion and an
`integral_tsum` swap over Dirichlet-summable
majorants.  The `2Λ/√n` corpus gauge is pinned,
not reconciled; census stays 7.
r533: the left vertical is the reflected prime
channel minus the arch clamp,
`∫ (ζ′/ζ)(-1/16+iτ) ĥ dτ = 2π ∑ Λ(n) n⁻¹ g(-log n)
− ∫ (χ′/χ) ĥ`
(`leftVerticalIntegral_eq_reflected_prime_sub_arch`).
The FE fold produces the weight `n⁻¹`, not the
corpus `2/√n`.  Combined pairing is
`∑ Λ(n)(1+n⁻¹)g(log n)`.  Arch integrand is
explicit; `leftEdgeArchIntegral` is the named
remaining clamp.  Census stays 7.
The internal endpoint is deliberately not named RH. -/

#print axioms dyadicSampleGrid_supportBound_le
#print axioms GridElement.toFun_eq_sum_linearCellPiece
#print axioms GridElement.toFun_eq_affine_on_nonneg_cell
#print axioms GridElement.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_cell
#print axioms gridPoleIntegral_eq_two_mul_sum_cell
#print axioms GridElement.intervalIntegral_toFun_mul_two_cosh_cell
#print axioms GridElement.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_increment
#print axioms polePairingZ_one_sided
#print axioms sum_cellCoshIncrement_eq_one_sided
#print axioms weilPoleSide_eq_two_mul_sum_cellCoshIncrement
#print axioms gridPoleHatIntegralIdentity
#print axioms meshWidth_tendsto_zero
#print axioms FullWeilTest.uniformContinuous_toFun
#print axioms FullWeilTest.toFun_zero_at_radius
#print axioms dyadicSampleGrid_acf_sub_toFun_le
#print axioms dyadicSampleGrid_toFun_uniform
#print axioms dyadicSampleGrid_l1_tendsto
#print axioms fullWeil_dyadic_sample_convergence
#print axioms fullWeilFixedSupportGridDensity_of_dyadicSample
#print axioms FullWeilTest.lipschitz_toFun
#print axioms GridElement.lipschitz_toFun_of_slope_bound
#print axioms dyadicSampleGrid_uniform_lipschitz
#print axioms archIntegrand_dini_bound
#print axioms weilArchSide_eq_cutoff
#print axioms fullWeil_arch_side_tendsto
#print axioms fullWeil_arch_continuity
#print axioms analyticAt_riemannZeta
#print axioms analyticOrderAt_riemannZeta_ne_top
#print axioms riemannZeta_analyticOrderAt_finite_pos
#print axioms riemannZetaMultiplicity_pos
#print axioms logDeriv_sub_const_pow
#print axioms exists_analytic_logDeriv_eq_order_div
#print axioms logDeriv_riemannZeta_eq_multiplicity_div_add_analytic
#print axioms meromorphicAt_logDeriv_riemannZeta
#print axioms meromorphicOn_logDeriv_riemannZeta_compl_one
#print axioms meromorphicOrderAt_logDeriv_riemannZeta
#print axioms tendsto_mul_logDeriv_riemannZeta
#print axioms isConnected_compl_one
#print axioms riemannZeta_eventually_ne_zero_punctured
#print axioms riemannZeta_eventually_ne_zero_nhdsNE_one
#print axioms isDiscrete_riemannZeta_zeros_compl_one
#print axioms riemannZeta_zeros_locallyFinite_compl_one
#print axioms finite_riemannZeta_zeros_of_isCompact
#print axioms finite_riemannZeta_zeros_of_isCompact_ne_one
#print axioms isCompact_zetaClosedRect
#print axioms finite_riemannZeta_zeros_on_closedRect
#print axioms analyticAt_riemannZetaMulSubOne
#print axioms analyticOnNhd_riemannZetaMulSubOne
#print axioms exists_analytic_riemannZeta_eq_one_div_add
#print axioms logDeriv_riemannZeta_eq_neg_one_div_add_analytic
#print axioms tendsto_mul_logDeriv_riemannZeta_one
#print axioms meromorphicAt_logDeriv_riemannZeta_one
#print axioms meromorphicOrderAt_logDeriv_riemannZeta_one
#print axioms meromorphicAt_logDeriv_riemannZeta_univ
#print axioms meromorphicOn_logDeriv_riemannZeta
#print axioms mem_riemannZetaZerosOnClosedRect
#print axioms FullWeilTest.hasCompactSupport_toFun
#print axioms FullWeilTest.abs_toFun_le
#print axioms FullWeilTest.hat_eq_setIntegral
#print axioms FullWeilTest.integrable_hat_integrand
#print axioms FullWeilTest.norm_hat_le_exp
#print axioms autocorrelation_second_diff_eq
#print axioms autocorrelation_second_diff_le
#print axioms FullWeilTest.abs_second_diff_le
#print axioms FullWeilTest.hat_comp_sub
#print axioms FullWeilTest.integrable_hat_comp_sub
#print axioms FullWeilTest.hat_comp_sub_twice
#print axioms FullWeilTest.integrable_hat_comp_sub_twice
#print axioms FullWeilTest.hat_mul_weierstrass
#print axioms exp_mul_pi_div_abs_im
#print axioms norm_one_sub_exp_pi
#print axioms one_add_exp_re_pi_ge_two
#print axioms FullWeilTest.norm_hat_le_inv_sq
#print axioms norm_one_div_nat_succ_cpow
#print axioms norm_riemannZeta_two
#print axioms norm_one_div_nat_succ_cpow_le_two
#print axioms inv_riemannZeta_eq_LSeries_moebius
#print axioms normRiemannZetaLeZetaTwo
#print axioms normInvRiemannZetaLeZetaTwo
#print axioms riemannZeta_one_sub_hypotheses
#print axioms riemannZeta_one_sub_eq_zero_of
#print axioms riemannZeta_zero_iff_one_sub
#print axioms fract_eq_sub_of_mem_Ico
#print axioms intervalIntegral_ofReal_cpow_deriv
#print axioms intervalIntegral_cpow_neg_succ
#print axioms sum_succ_mul_sub_cpow
#print axioms sub_cpow_eq_s_mul_intervalIntegral
#print axioms norm_zetaFractCellIntegrand_le
#print axioms norm_zetaFractCell_le
#print axioms finite_N_euler_maclaurin
#print axioms riemannZeta_eq_s_div_sub_s_mul_fractIntegral
#print axioms summable_zetaFractCell
#print axioms norm_zetaFractIntegral_le_zeta_two
#print axioms norm_riemannZeta_le_of_re_gt_one
#print axioms hasDerivAt_zetaFractCell
#print axioms differentiable_zetaFractCell
#print axioms differentiableOn_zetaFractIntegral_re_gt
#print axioms differentiableOn_zetaFractIntegral_re_pos
#print axioms riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos
#print axioms norm_zetaFractIntegral_le_of_re_gt
#print axioms norm_riemannZeta_le_of_re_gt
#print axioms norm_riemannZetaMulSubOne_le_of_re_gt
#print axioms norm_riemannZetaMulSubOne_center_ge
#print axioms riemannZetaMulSubOne_eq_zero_iff
#print axioms riemannZetaMulSubOne_meromorphicOrderAt_ne_top
#print axioms riemannZetaMulSubOne_divisor_ge_one_of_zero
#print axioms riemannZetaMulSubOne_jensen_identity
#print axioms riemannZetaMulSubOne_jensen_avg_le
#print axioms riemannZetaMulSubOne_jensen_sum_le
#print axioms zetaZerosInDisk_card_mul_log_le
#print axioms zetaZerosInDisk_card_le
#print axioms jensenDiskZeroCountBound
#print axioms zetaZerosInDisk_card_le_inner
#print axioms zetaZeroCountUpToXBound
#print axioms summable_inv_sq_zetaZeros
#print axioms rectangleIntegral_eq_zero_of_differentiableOn
#print axioms integral_inv_add_I_mul
#print axioms integral_inv_re_add_mul_I
#print axioms rectangle_inv_arctan_sum
#print axioms rectangleIntegral_inv_of_zero_mem
#print axioms rectangleIntegral_comp_add
#print axioms rectangleIntegral_inv_of_mem
#print axioms rectangleIntegral_simple_pole
#print axioms rectangleIntegral_sum_simple_poles
#print axioms logDeriv_riemannZeta_eq_neg_LSeries_vonMangoldt
#print axioms norm_logDeriv_riemannZeta_le_at_two
#print axioms exists_analyticAt_update_of_meromorphicOrderAt_nonneg
#print axioms exists_analytic_logDeriv_mul_sub
#print axioms exists_analytic_logDeriv_mul_sub_one
#print axioms meromorphicOrderAt_logDerivHatRemainder_at_zero
#print axioms meromorphicOrderAt_logDerivHatRemainder_at_one
#print axioms exists_analyticAt_update_logDerivHatRemainder_at_zero
#print axioms exists_analyticAt_update_logDerivHatRemainder_at_one
#print axioms FullWeilTest.analyticOnNhd_hat
#print axioms differentiableOn_logDerivHatRemainderFilled
#print axioms contour_identity_fixed_T
#print axioms FullWeilTest.norm_hat_le_inv_sq_of_abs_re_le
#print axioms FullWeilTest.norm_hat_le_inv_sq_on_Icc
#print axioms FullWeilTest.norm_hat_le_inv_sq_on_contour
#print axioms norm_logDeriv_riemannZeta_le_of_re_ge
#print axioms norm_logDeriv_riemannZeta_le_at_five_four
#print axioms riemannZeta_ne_zero_of_neg_quarter_lt_re_lt_zero
#print axioms exists_point_far_from_finset
#print axioms card_window_zeros_unit
#print axioms exists_gap_height
#print axioms exists_gap_sequence
#print axioms borelCaratheodory_ball
#print axioms borelCaratheodory_ball_zero
#print axioms borelCaratheodory_closedBall_zero
#print axioms exists_logDeriv_primitive
#print axioms re_logDeriv_primitive_eq
#print axioms norm_logDeriv_le_of_log_norm_le
#print axioms logDeriv_riemannZeta_eq_logDeriv_mulSubOne_sub
#print axioms norm_riemannZetaMulSubOne_le_on_landau_ball
#print axioms logDeriv_landauPoly
#print axioms sum_multiplicity_landauInnerDisk_le
#print axioms norm_sum_multiplicity_inv_le_of_gap
#print axioms analyticAt_landauQuotient
#print axioms landauQuotient_ne_zero_on_landau_ball
#print axioms logDeriv_riemannZeta_eq_landauQuotient_add
#print axioms norm_landauQuotient_le_on_mid_closedBall
#print axioms log_norm_landauQuotient_center_ge
#print axioms horizontalEdgeLandauBound
#print axioms horizontalEdgeLandauBound_of_gap
#print axioms landau_cubic_pack_scale
#print axioms horizontalEdgeLandauBound_landauGap
#print axioms ordinateGapConstLandau_one_le
#print axioms riemannZetaZerosOnClosedRect_eq_critical
#print axioms contour_identity_fixed_T_of
#print axioms contour_identity_fixed_T_neg_one_div_sixteen
#print axioms exists_gap_height_abs
#print axioms exists_gap_sequence_abs
#print axioms norm_horizontal_logDeriv_hat_integral_le
#print axioms exists_gap_height_landau
#print axioms exists_gap_sequence_landau
#print axioms landau_gap_of_wide_window
#print axioms digamma_add_nat
#print axioms sum_range_inv_succ_le_one_add_log
#print axioms sum_digamma_kernel_norm_le
#print axioms sum_digamma_kernel_tail_le
#print axioms ofReal_ne_neg_nat
#print axioms pos_ne_neg_nat
#print axioms hasDerivAt_re_Gamma_ofReal
#print axioms deriv_Gamma_ofReal
#print axioms digamma_ofReal
#print axioms monotoneOn_log_Gamma_deriv
#print axioms monotoneOn_re_digamma
#print axioms re_digamma_add_nat
#print axioms re_digamma_nat_succ
#print axioms summable_one_div_succ_sq
#print axioms summable_digamma_kernel_real
#print axioms sandwich_partial_digamma_kernel
#print axioms tendsto_partial_digamma_kernel_real
#print axioms re_digamma_weierstrass_Ioo
#print axioms ofReal_digamma_kernel
#print axioms digamma_eq_weierstrass_ofReal_Ioo
#print axioms isOpen_digammaStrip
#print axioms isPreconnected_digammaStrip
#print axioms mem_digammaStrip_ne_neg_nat
#print axioms nat_add_ne_zero_of_mem_digammaStrip
#print axioms analyticAt_Gamma_of_mem_digammaStrip
#print axioms analyticAt_digamma_of_mem_digammaStrip
#print axioms analyticOnNhd_digamma_strip
#print axioms digamma_kernel_term_norm_le_strip
#print axioms summable_digamma_kernel
#print axioms differentiableOn_digamma_kernel
#print axioms analyticAt_digammaWeierstrass
#print axioms analyticOnNhd_digammaWeierstrass
#print axioms three_halves_mem_digammaStrip
#print axioms xs_Ioo_three_halves
#print axioms tendsto_ofReal_punctured_three_halves
#print axioms frequently_eq_digamma_weierstrass_three_halves
#print axioms digamma_eq_weierstrass_on_strip
#print axioms mem_digammaStrip_of_horizontal
#print axioms sum_Ico_add_eq_sum_range
#print axioms tsum_digamma_kernel_norm_tail_le
#print axioms norm_digamma_le_log_of_horizontal
#print axioms digammaHorizontalLogBound
#print axioms normSq_cos
#print axioms normSq_sin
#print axioms cos_ne_zero_of_im_ne_zero
#print axioms norm_tan_sq_le_of_im_ne_zero
#print axioms norm_tan_le_of_two_le_abs_im
#print axioms ne_neg_nat_of_two_le_abs_im
#print axioms ne_one_of_two_le_abs_im
#print axioms digamma_eq_succ_sub_inv
#print axioms norm_digamma_le_log_of_sliver
#print axioms riemannZeta_one_sub_factor
#print axioms two_mul_pi_ne_zero
#print axioms logDeriv_neg_cpow_two_pi
#print axioms hasDerivAt_pi_mul_div_two
#print axioms logDeriv_cos_pi_div_two
#print axioms differentiableAt_zetaFEFactor
#print axioms logDeriv_zetaFEFactor
#print axioms ne_neg_nat_of_im_ne_zero
#print axioms ne_one_of_im_ne_zero
#print axioms im_pi_mul_div_two
#print axioms cos_pi_div_two_ne_zero_of_two_le_abs_im
#print axioms two_le_abs_im_pi_div_two
#print axioms zetaFEFactor_ne_zero_of_two_le_abs_im
#print axioms eventuallyEq_riemannZeta_one_sub_factor
#print axioms hasDerivAt_one_sub
#print axioms logDeriv_riemannZeta_functional
#print axioms norm_log_two_pi
#print axioms sliverEdgeConst_nonneg
#print axioms sliver_cubic_pack
#print axioms sliverEdgeBound_of_dual
#print axioms sliverEdgeBound_negIm
#print axioms riemannZeta_conj_of_one_lt_re
#print axioms riemannZeta_conj
#print axioms deriv_riemannZeta_conj
#print axioms logDeriv_riemannZeta_conj
#print axioms norm_logDeriv_riemannZeta_conj
#print axioms sliverEdgeBound_posIm
#print axioms horizontalEdgeLandauBound_negIm
#print axioms horizontalEdgeBound_glued
#print axioms riemannZeta_ne_zero_of_glued_gap
#print axioms tendsto_one_add_log_cubed_div_one_add_sq
#print axioms horizontalEdgesTendstoZero
#print axioms norm_logDeriv_riemannZeta_le_at_seventeen_sixteen
#print axioms riemannZeta_ne_zero_of_re_eq_neg_one_div_sixteen
#print axioms left_edge_logDeriv_bound
#print axioms leftEdgeLogDerivBound
#print axioms right_edge_logDeriv_bound
#print axioms left_edge_integrand_norm_le
#print axioms right_edge_integrand_norm_le
#print axioms abs_im_lt_of_landau_gaps
#print axioms continuous_vertical_path
#print axioms continuous_right_edge_integrand
#print axioms continuous_left_edge_integrand
#print axioms integrable_right_edge_integrand
#print axioms integrable_one_add_log_mul_inv_sq
#print axioms integrable_left_edge_integrand
#print axioms riemannZetaMultiplicity_eq_one_sub
#print axioms riemannZetaMultiplicity_le_log
#print axioms tendsto_right_edge_interval
#print axioms tendsto_left_edge_interval
#print axioms spectralPartialSum_eq_subtype
#print axioms exists_weighted_hat_bound
#print axioms summable_weighted_hat
#print axioms tendsto_spectralPartialSum_tsum
#print axioms contourIdentityLimitAlongGaps
#print axioms FullWeilTest.hat_eq_fourier_slice
#print axioms FullWeilTest.integrable_fourier_hatSlice
#print axioms FullWeilTest.fourierInv_hatSlice
#print axioms FullWeilTest.hat_fourier_inversion
#print axioms rightVerticalIntegral_eq_prime_sum
#print axioms leftVerticalIntegral_eq_reflected_prime_sub_arch
#print axioms logDeriv_riemannZeta_left_edge
#print axioms logDeriv_zetaFEFactor_left_edge
#print axioms contourPrimePairing_eq_one_add_inv_sum
#print axioms one_add_inv_ge_two_div_sqrt
#print axioms integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n
#print axioms sum_Ico_inv_telescope
#print axioms gridPoleIntegralIdentification_of_hat
#print axioms FullWeilTest.FixedSupportGridApproximation.tendsto_toFun
#print axioms GridElement.elementAnchor_le_fullAnchor
#print axioms weilCombSide_eq_fullAnchor
#print axioms fullWeilCombSide_tendsto
#print axioms fullWeilPoleIntegral_tendsto
#print axioms fullWeilChannelContinuity_of_components
#print axioms fullWeilForm_tendsto_of_channels
#print axioms fullWeilForm_nonneg_of_tendsto
#print axioms grid_dense_extension_of_fixedSupport
#print axioms fullWeil_fixedSupport_completion
#print axioms fullWeil_fixedSupport_grid_density
#print axioms fullWeil_channel_continuity
#print axioms grid_dense_extension
#print axioms standard_explicit_formula_identification_honest
#print axioms standard_weil_criterion_to_mathlib_rh_of_separation
#print axioms fullWeil_separates_offCritical_zeros
#print axioms standard_weil_criterion_to_mathlib_rh

/-! ## r558 Gabor split and EF wiring
Expected: `gabor_explicitFormula_of_remainders`,
`gabor_explicitFormula_pure_of_remainders`,
`gabor_contour_identity_along`,
`gabor_separation_of_inputs`,
`gabor_inputs_to_mathlib_rh`,
`gabor_separationInequality_of_parts`,
`gaborSeparationForAllZeros_of_inequality`
are `[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
r581: `gabor_vertical_arithmetic_remainder` is a theorem
(no `sorryAx`).  r612: the asserting theorem
`gabor_separationForAllZeros` is retired; `GaborSeparationForAllZeros`
is an unasserted Prop.  Census 8 → 7.
r564: `gabor_rightVerticalIntegral_eq_prime_sum`,
`gabor_hat_fourier_inversion`, and
`gabor_vertical_arithmetic_of_parts` are
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
r612C: `gaborZeroSideContinuous_holds` and
`gabor_zeroSide_rational_criterion_iff_rh_unconditional` are
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
Named-open list shrinks by one; census stays 7.
r634L: `gabor_explicitFormula_pure` and
`gabor_primeSide_rational_criterion_iff_rh` are
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
Census stays 7. -/
#print axioms gabor_contour_identity_along
#print axioms gabor_explicitFormula_pure_of_remainders
#print axioms gabor_explicitFormula_pure
#print axioms gabor_explicitFormula_of_remainders
#print axioms gabor_vertical_arithmetic_of_parts
#print axioms gabor_rightVerticalIntegral_eq_prime_sum
#print axioms gabor_hat_fourier_inversion
#print axioms gabor_vertical_arithmetic_remainder
#print axioms scalingGaborTest_coeffs
#print axioms gaborSeparationForAllZeros_of_inequality
#print axioms gaborSeparationPrecheck_of_inequality
#print axioms gabor_separationInequality_of_parts
#print axioms gabor_separation_of_inputs
#print axioms gabor_separation_of_inequality
#print axioms gabor_inputs_to_mathlib_rh
#print axioms gabor_inputs_to_mathlib_rh_of_inequality
#print axioms gabor_zeroSide_rational_of_rh
#print axioms gabor_zeroSide_nonneg_of_rational
#print axioms gabor_zeroSide_rational_criterion_iff_rh
#print axioms gaborZeroSideContinuous_holds
#print axioms gabor_zeroSide_rational_criterion_iff_rh_unconditional
#print axioms gabor_primeSide_rational_criterion_iff_rh

/-! ## r568 canonical isolation-shrink dominance bricks
Expected: Q-evenness, phase-coherence, plus-lobe majorant, host-merge,
ω>0 shrink existence / greatest-a, and the logical wrapper are
`[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
`GaborDominanceBound` and the two named translation bridges are
unasserted Props, not holes.  Census unchanged at 9. -/
#print axioms truncated_theta_binMax_sum_le
#print axioms truncated_theta_tsum_le
#print axioms gaborQuadrupole_eq_four_re_hat
#print axioms gaborQuadrupole_eq_four_re_integral
#print axioms gaborQuadrupole_even_gamma
#print axioms gabor_phase_coherent_cos
#print axioms gaborPlusAmp_le_exp_neg_omega_sq
#print axioms gaborPlusLobe_majorant
#print axioms gaborHostMerge_minusLobe
#print axioms exists_isolationShrink
#print axioms exists_isolationShrink_omega
#print axioms exists_greatest_isolationShrink
#print axioms isolationShrink_spec
#print axioms isolationShrink_exceptionWindow_empty
#print axioms gabor_dominance_implies_separation

/-! ## r617L Coxeter completion and prime-log independence
Expected: `cyclotomic30_explicit`, `moebius_identity_30`,
`completion_linear_coeff_zero`, `completion_explicit`,
`trace_eq_neg_one_of_charpoly_cyclotomic30`,
`linearIndependent_log_primes`, `log_ratio_irrational`
are `[propext, Classical.choice, Quot.sound]` -- NO `sorryAx`.
Census unchanged at 7. -/
#print axioms cyclotomic30_explicit
#print axioms moebius_identity_30
#print axioms completion_linear_coeff_zero
#print axioms completion_explicit
#print axioms trace_eq_neg_one_of_charpoly_cyclotomic30
#print axioms linearIndependent_log_primes
#print axioms log_ratio_irrational

end RH
