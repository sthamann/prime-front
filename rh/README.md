# rh/ — the consolidated RH-program workspace

> **Claim boundary (non-negotiable).** This workspace is **research
> documentation**. Nothing in it is evidence **for or against the Riemann
> Hypothesis, in either direction. NO RH CLAIM.** Status markers follow the
> repository ledger (`verification/status_ledger.csv`, which wins on any
> disagreement): **[E]** = certified finite theorems (machine-checked exact
> identities), **[O]** = honestly open. Mincut **base 4 / refined 5** —
> unchanged by anything in this tree.

`rh/` is the single home for the TFPT prime-front RH program: the certified
finite reduction chain, a focused paper, a Lean 4 formalization pilot, and an
RH-specific verification suite. It **references** the canonical sources in the
main tree (verification modules, sealed discovery probes, ledger rows) with
pinned SHA-256 hashes — it **never duplicates** them.

## What the RH program is

The program studies the *window object*: the finite Galerkin compression of
the localized Weil operator onto a window of the von-Mangoldt double comb
(the "MAIN world"), together with scramble / Epstein / smooth control worlds.
Positivity of this finite object through the whole window — "the wall" — is
a *finite, machine-decidable* statement per window. Two years of rounds have
compressed the entire question into an exact dictionary (tau functions,
bordered Riemann–Hilbert problems, a coupled two-term recursion) whose
**certified finite part is [E]** and whose **remaining arithmetic edge is two
precisely named open statements [O]**.

## The reduction chain (current state)

| Stage | Statement | Status | Module / round |
|---|---|---|---|
| 1 | Window object: Galerkin of the localized Weil operator; wall = quasi-definiteness of the signed defect measure `mu - nu` (`WALL_EQUIVALENT`) | [E] | `v955` (r224–r226) |
| 2 | Half-filling law `N_w = ceil(S/2)`: MAIN survives its entire free moment window, controls die at 0.11–0.15 `N_w`; four exact source-pure coordinates; dual-FIK L-gauge | [E] | `v956` (r228–r231) |
| 3 | Bordered-RHP dictionary: bordered PSD = wall + budget; Schlesinger rank-1 insertion; centering congruence; three exact error formulas; contour `R_1`; PSD base theorem | [E] | `v958` (r244–r253) |
| 4 | Coupled-tau recursion `tau_{n+1} = a_n tau_n`, `tau^aug_{n+1} = a_n tau^aug_n + b_n tau_n` ⇒ Riccati drain `D_{n+1} = D_n - rho_n`; bilinear identity; Schur budget telescope `D_N = B - sum rho`; terminal reduction `margin > 0 ⟺ q_N < 1` | [E] | `v959` (r256–r259) |
| 5 | Terminal-surface closure: two-branch theorem (`Z_w = r_{N-1}`, cheap branch 35/42 + both mains **without cancellation**, exception set 7 rungs) + sealed phase bounds (edge truncation, block alternation) + kz15 interval certificate (dps 640, width 1.5e-92, margin +0.0268) + universal pair theorem H1–H4 (Lean-proved) — **the 42-rung census `q_N < 1` certified on all 42 rungs** (41 mechanism target-blind + kz15 exact-finite); census + certificate, NOT cofinal | [E] | `v960` (r260–r275) |
| 6 | Midpoint-orientation dictionary: base Casoratian `= h_n` (`c' = 1`), h-free midpoint form = node polynomial, augmented telescope `D_{n+1} = B − W^aug/W^base`; Maslov census GO (rule R2 = Jacobi interlacing/reality, blind 42/42, controls at flip+1, one-way; raw atom-Sturm census REFUTED as winding quantity); metric-firewall measurements (graded continuum, exact Hellmann–Feynman gradients, u-profile predictive, stability law perturbative-only) | [E] | `v961` (r274–r278) |
| 7 | **Half-filling pinning theory** (wave 5): T1 moment counting (free pivots exactly `h_0..h_{N_w−1}` — half-filling is the end of the free moment space, "why half-filling" answered by counting) + T2 crossing budget (`#(h<0) = S_−`, Jacobi/Sylvester, world-blind) + T3 two-sided parity (h-blind; census bilanz + 87376-case exhaustion) + T4 main window reduction (**the entire open statement is `minC ≥ N_w` ⟺ `∀ n < N_w : h_n > 0`**) — plus the four refutations (no universal O(1) pinning, no extremality, no generic Maslov obstruction, no simple offset law) | [E] | `v962` (r279–r281) |
| 8 | **The L* reduction dictionary** (wave 6): the r283 A2 chain exact (mu-frame congruence `minor_k(D_mu − G) == D_k(mutilde)`; contraction `h > 0` through the window ⟺ `lambda_max(E_m) < 1`; crossing exactly at `minC + 1`; pigeonhole `minC ≤ S_+`; capacity-as-counting refuted by the rank-one pair) ⇒ **L\* is the canonical reduction** (`∫p²dnu < ∫p²dmu` for `deg p < N_w`); the r285 bookkeeping `lambda = maxdiag·(1+assist)` exact with sign-exact budget equivalence; the r282 four-language elimination as named negative gates (`CONTEST_ALL_DEAD` — every classical language forces positivity exactly for the positive measure class); typed measurements: one-atom wall, (D) separates, sub-classical `p = 0.38`, ensemble LOW_OUTLIER, the first two MAIN_SEPARATING detectors, the honest margin decay | [E] | `v963` (r282–r285) |
| 9 | **Edge A (fiber, cofinal front):** hypothesis H5 / lemma L2 — pair-sum decay via a non-adjacent/global generic mechanism (address c3, `delta' > 0.21` of available 0.45, TRUTH_ALLOWS); the r287 framework census (consumed in wave 7, `v964`) measures the generic half CLASSICAL: the exact van der Corput bound at `H = ceil(sqrt(m))` delivers `delta' +0.31` world-blindly and certifies 6/7 exceptions — only the kz15 razor stays open (0.07–0.12 dec on every surviving frame; exact-finite per r270) — the vdC form is registered as the named classical candidate: prove it as a *chain* statement (the remaining input: the chain origin of the P-variance scaling; r297 froze the target inequality — sigma ≤ −0.516, truth −0.714, margin 0.198 — and adjudicated the three classical provenance routes `CHAIN_PROVENANCE_PARTIAL(B3)`: the chain is exactly orthogonal on the *window* measure, the named rest is the bordered-form measure transfer + the signed-to-absolute gap; r298 delivered that transfer **exactly and sign-preservingly** — `S_F = B(omega,omega) + B(Delta,omega+beta)` on the frozen positional Fejér kernel, adjudicated `TRANSFER_DOMINANT`: the window main term is empty, `S_F ≈ B(PDelta,PDelta)` — the vdC input IS the Fejér energy of the difference measure; the wave-9 gap object is *prove the Δ-energy decay*; r299 decomposed that energy exactly into its frequency spectrum and adjudicated `DECAY_SPLIT`: the energy is LOWPASS (main-lobe share 0.93), Δ is a *pure c-value difference measure* (the unions share every position, 42/42), and the live edge is the pair split — the diagonal `sum PDelta_j²` already falls fast enough (slope −0.571 ≤ σ* −0.516) with a *falling* pair ratio B/D (−0.168): the frozen rest pair is `DIAG_TARGET` + ratio flatness (plus `CVALUE_TARGET` on the B3 side); the ET/Abel composition fails loudly (+1.948); r300 anatomized the diagonal exactly — `sl_D = 2·sl_L1 − sl_neff` with the effective-carrier count `n_eff = L1²/D` growing at +0.963 against an L1 mass at +0.196: the diagonal decay IS a participation statement; both magnitude factorizations fail (B1 −0.384, B2 −0.346 vs σ* −0.516; the fill decay −0.225 is the non-factorizable part; the |dw| sum-rule attach BREAKS), the **ratio half is settled structurally** (`RATIO_BOUNDED_STRUCTURAL`: the exact kernel-envelope majorant R_env med 1.61 falls at −0.122), and the refined freeze is ONE inequality — `NEFF_TARGET`: prove `slope(n_eff) ≥ +0.908` (measured +0.963, margin 0.055), with the falling D_rank (sp −0.81) as the named bridge to provable terrain; **rounds r296–r300 consumed in wave 9, `v966` = `PRIME.L2.REDUCTION_CHAIN.01` [E]** — the chain stands reduced to exactly this inequality, registered `PRIME.L2.NEFF_TARGET.01` [O]; r301 executed NEFF_TARGET (`neff_target_probe.py`, 32/32, `NEFF_SPLIT(B1|B3)`): the exact identity `n_eff = n_act/(1 + CV²)` with the PERFECT count link `n_act == m` on 42/42 — the carrier count IS the constructive level-2 block count (+1.002) — compresses the rest into **`UNIF_TARGET`**: slope(1 + CV²) ≤ +0.094 (measured +0.039, margin 0.055, jackknife-stable 0/42 below NEED); the weighted-discrepancy/max route is closed honestly (bound slope +0.074, the |dc|-weighted discrepancy is near-flat), the local sum-rule census breaks 24/24; experiments-side, consumed in wave 10, `v967`; r302 executed UNIF_TARGET (`unif_target_probe.py`, 30/30, **`UNIF_DERIVED(B1+A2)`** — the first sealed DERIVED verdict of the lane, every hypothesis typed MEASURED): the normalized block profile of \|PDelta\| is **stationary** (pooled KS(G1,G3) 0.043 over a 3× depth range, an exact-1/N transient onto a finite second moment m2_inf = 1.973 approached from above — the r299 pointwise-cconv negative was the wrong convergence notion), the exact coherence identity `1 + CV² = n_act·χ/(surv²·n_eff_atom)` (χ = D/Q the in-block coherence factor, med 0.63 DESTRUCTIVE and non-growing −0.060, the r301 lag-1 anti-correlation ρ₁ = −0.22 its atom-level mechanism) decomposes the uniformity head exactly; the r301 deep-half flag is carried ENTIRELY by the CV² head (+0.228), not the count (+1.030), and exactly this excess is what the 1/N transient explains; the ONE remaining measured growth statement is **`ATOM_TARGET`**: slope(n_eff_atom) ≥ +0.888 (measured +0.942, margin 0.055 — the same thin margin one level down); the local-pattern route (within-share 0.685) and the recursion-gain damping clause (g/N med 1.079 vs 1.0) closed honestly; experiments-side, consumed in wave 10, `v967`; r303 adjudicated the thrice-identical 0.055 margin (`atom_target_probe.py`, 26/26, **`REGRESS_CONFIRMED`**): the four target margins m_D/m_NEFF/m_UNIF/m_ATOM are ONE algebraic number `S = σ* − sl_D = +0.0547` (invariance ≤ 9e-16; Fractions re-proof; the ½-conversion conjecture refuted) — the cascade r297→r302 is an exact *dictionary* around one measured core, **closed**; the first non-tautological mechanism test (sealed synthetic dc rearrangements, exact marginal, steered ρ₁, 1008 builds) fired **`MIXING_INSUFFICIENT`** with a monotone ladder: flipping the mixing sign kills the inequality (margin −0.044), matching ρ₁ reproduces slopes + margin but not the χ level (0.764 vs 0.630) — the within-block structure beyond lag 1 is the named mechanism gap; `n_eff_atom` is a pure marginal functional (invariance 1.0e-15): stationarity and mixing are complementary; ρ₁-sign census honest 41/42; experiments-side, consumed in wave 10, `v967`; r304 executed the reviewer-mandated short-range-law test (`shortrange_law_probe.py`, 37/37, **`LONGRANGE_STRUCTURE` + `LAW_LONGRANGE`**): the lag profile ρ₁..₁₆ of the dc profile is a *stable period-4 comb* (strong lags at k = 4m and 4m+2 up to 16, halves-stable, world-specific), NOT a decaying tail — the sealed short-range rule finds no k₀ and the reviewer stop case fires; the reviewer condition *splits*: net covariance NC(16) = 0.712 < 1 HOLDS while summability-with-small-tail FAILS (SUM(16) = 1.563); the exact χ lag decomposition (χ = 1 + 2Σ T_k/Q, ward 4.7e-16) shows the χ-relevant within-block structure IS short-range (shares die out by k ~ 4; the r303 miss 0.134 sits at k ≤ 3, dominated by lag 2) — the comb is invisible to χ; lag-8 matching reproduces the χ level (0.652 vs 0.630) but breaks the slopes by 0.028/0.027 — the mechanism is TWO-SCALE, no lag-matching family reproduces both; graduated ρ₁ ladder monotone in χ, NOT in the margin (absolute levels do not kill the inequality — the r303 kill came from per-rung flipped targets); sign pattern −/−/+/+ Fractions-exact on kz18/kz23; the lane's global-profile mixing route is CLOSED (documented stop); experiments-side, consumed in wave 10, `v967`; **rounds r301–r304 consumed in wave 10, `v967` = `PRIME.L2.CASCADE_CLOSURE.01` [E] — the cascade closure and the documented lane stop**: the cascade r297→r302 stands RETYPED as an exact reduction dictionary around one measured core `S = σ* − sl_D = +0.0547` (r303 `REGRESS_CONFIRMED`, invariance ≤ 9e-16; the ½-conversion refuted; hard rule: a round counts only with NEW information); the first causal coordinate is real (ρ₁ ladder monotone, the flip kills at −0.044) but two-scale-insufficient; the global-profile mixing route is documented CLOSED (`LAW_LONGRANGE`: stable world-specific period-4 comb, no k₀; NC(16) = 0.712 < 1 holds, summability fails) — the honest stop state: **L2 generic ⟺ anti-concentration of the explicit dc block field with long-range period-4 structure; return with new tools**; `PRIME.L2.NEFF_TARGET.01` [O] retyped to the documented stop state) | **[O, documented stop]** | `PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01` → `PRIME.PORT.L2.VDC_LEMMA.01` (wave 7, `v964`) → `PRIME.L2.NEFF_TARGET.01` (wave 9, `v966`) → `PRIME.L2.CASCADE_CLOSURE.01` (wave 10, `v967` — documented stop) |
| 10 | **Edge B (base/orientation):** the oriented midpoint theorem — rounds 279–281 executed and consumed (wave 5): the theorem share promoted into stage 7, the generic two-sided obstruction refuted exactly, the center precisified to the budget localization; the successor representation contest is executed and consumed (wave 6, stage 8): `CONTEST_ALL_DEAD` — no classical representation carries the positivity, certified in `v963` with the common deep reason | **[O]** | `PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01` → `PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01` → `PRIME.PORT.REPRESENTATION.CONTEST.01` (consumed) |
| 11 | **THE NORTH STAR (the open center, canonical form since wave 6): lemma L\*** — for every admissible anchor `z` and every real polynomial `p ≠ 0` with `deg p < N_w`: `∫p²dnu_z < ∫p²dmu_z`, equivalently `lambda_max(E_{N_w}) < 1` (the nu-dressed mu-CD kernel is a strict contraction at half-filling depth). Via the v963 A-chain this ONE two-measure subordination inequality IS the full free-window quasi-definiteness (`∀ n < N_w : h_n > 0`, the reinstform north star of wave 5), hence via T4 the entire open statement of the wall. State: 42/42 measured, and since r286 **57/57 sign-safe measured** — the sealed extension rule (window cap lifted) added 15 new anchors `N_w` 942–1218, **all margins positive** (min `+1.81e-8` at z = 529, every sub-1e-5 margin mp-verified dps 30/45): **no counterexample**; the honest margin decay is now a measured law (POWER, `alpha ≈ 3.05` vs S, flattening at large S) with the harmless reading quantified (the margin falls *slower* than the local eigenvalue-loading speed at a fixed O(1) census offset; the r258-flat terminal `q_N` re-measured as a different object; r286–r289 consumed in wave 7, `v964` = `PRIME.LSTAR.COHERENCE_CENSUS.01` [E]). Anatomy: (D) per-atom (discrete, sub-classical `p = 0.38`) + (C) coherence (MAIN-destructive, ensemble LOW_OUTLIER, two MAIN_SEPARATING detectors; r288 carrier map: the wall destructivity = antiphase next-nearest (3–4 fold) ARCH–ARCH interference, sign-reversed on every control; plain phase dispersion world-blind — no source-pure separator yet, and the destructive sign flips already at jitter dose 0.005 while the phase field barely rotates; r289 twin adjudication `METRIC_ONLY`: replacing every `log n` by a small-denominator rational multiple of the grid spacing — position cost 2e-9, all exact log-relations destroyed — changes *nothing* (mp-confirmed at the 1.7e-4 margin), while metrically matched fraction shuffles lose exactly as the plain jitter ladder predicts; the coherence reads the tent-split fraction profile at ~1e-3 of the local gap, indifferent to number-theoretic exactness — Baker-class nonresonance input unnecessary on all tested scales; **r331 audit repair (r328C finding C2): the twin RESOLUTION is measured** — at the r289 precision the twin footprint sits ≥ 3.4 orders below every margin down to 1.8e-8 (11/11 anchors RESOLVE, mp pair-verified), the tight anchors are twin-stable from 1e-6 gap, and a gap-preserving genuinely diophantine detune keeps the wall at w9 AND kz119: `METRIC_ONLY_CONFIRMED_AT_RESOLUTION` — the switch carries a resolution certificate on the tight range; **r290–r295 consumed in wave 8, `v965` = `PRIME.LSTAR.CURVATURE_ARC.01` [E]**: the working-set geometry is now *measured* — a soft-shouldered anisotropic tube (killfrac 0.38/0.62/1.00 at 5e-4/1e-3/2e-3 gap), a real one-degree ridge (plateau minC 185, first-order budget threshold in (1.280, 1.291], MAIN-specific), a rank-1 DENS curvature valley (92.5 pct, lam_top −0.418) and simple h_184 flip zeros (alpha = 1; MSTAR_NO_LAW) — while the closed-functional search is sealed honestly NEGATIVE over five class families (r294 F10_FRAGILE + r295 F10_SP_MAJORITY 14/20: F10 unpromoted, R293_LUCK); the successor question is `PRIME.LSTAR.CLOSED_FUNCTIONAL.01` [O]; **r296 consumed in wave 9, `v966`: the DENS-identity fork on the rank-2 DENS core is closed — `DENS_WORLD_BLIND`, coupling number +0.394 < 0.40, the lane routed to L2**). Lean: `lstar_subordination` + `free_window_positivity` (`rh/lean/RH/Window.lean`; L\* ⇒ free-window PROVED); standalone problem statement `rh/problem/lstar_problem.tex`. Predecessor contract `PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` consumed by `v963` | **[O]** | `PRIME.LSTAR.SUBORDINATION.01` |
| 12 | **The metric firewall (global form):** wall lemma stable under small-dose permutations while consuming the metric data exactly (certified state: perturbative-only) | **[O]** | `PRIME.PORT.WALL.METRIC_FIREWALL.01` |

**The wall.** Every single-component attack class is measured dead
(compression, constants, band locality, mass majorants, level crossing,
one-swap, smooth dressing, bordered spectral bound, naive and IIKS
`s`-coordinates — `DEFINITENESS_WALL_EQUIVALENT`, r257 + r265). The obstacle
is coherent cancellation over the configuration ensemble; the wall contract is
`PRIME.CASE.PAIRCORR.CONTRACT.01` **[O]**. Since r267 the wall has an
**external anchor**: arXiv:2608.13637 (Alpöge–Furman, Lean-4-formalized,
unconditional ≥ 2/3 of zeros simple and on the line) proves a *ceiling*
(`p0 <= 0.6818` for all two-moment bandwidth-one certificates) whose binding
constraint — pair-correlation cancellation beyond diagonal control — is
**exactly the location of our measured wall** (`CEILING_IS_OUR_WALL`), while
being orthogonal in scope (`NO_IMPORT`, frame mismatch quantified: their
zero-atom near-tight frame vs our prime-comb half-filling regime, R ≈ 4/3 vs
73–126). Round r639 adjudicated the Lamzouri re-proof (arXiv:2609.02882, Hilbert-space inequality + unconditional BGSTB pair correlation): same two-moment class, same constants ($C_0 = p^*$ of r627), and the sole arithmetic input is the proven pair-correlation range $|\alpha| \le 1$ — the wall location is now explicit in the external proof itself (`SAME_CLASS`, `WALL_LOCATION_CONFIRMED`).

**The exception scalar.** After r263 the fiber edge is a two-branch statement:
the generic branch is a target-blind triangle certificate (no cancellation
needed); the whole difficulty is concentrated in one scalar `Z_w` on the
7-rung exception branch, with requirement **S6**: `|Z^RHP| + |E| < sqrt(5/7)`
on the branch `g_w < 0`. The r264 charter froze the campaign (SHA
`7b9e751d`); r264 delivered the exact RHP dictionary
`Z^RHP = (border-column readout)/(Y1 root)` and the data signature
(`S1_TERMDRIVE`, separation 0.959); r265 closed the `s`-coordinate class
(no admissible `s`-coordinate carries both the right endpoint and definite
dynamics); r266 searches for a border-dressed resolvent identity; r267
adjudicated the external position. r268 built the local drive asymptotics:
the exception branch is a **cancellation-depth anomaly** at fixed comb mass
(DEPTH power 0.812; mass/edge/participation all blind), the L-gauge frame
provably adds no new locality at the terminal (node collapse exact, dual
degree `N`), and the edge-region triangle bound (outer 20 % of the hull)
delivered the **first source-pure certification of an exception rung**
(kz22, margin +0.04), leaving 6 rungs open by 0.18–0.44 dec
(`DRIVE_LOCAL_PARTIAL`). r269 attacked exactly that gap with sealed
**phase-aware bulk bounds** (block alternation over adjacent sign-run pairs,
exact triangle theorems, chain-envelope variant honestly typed too coarse):
`PHASE_BOUND_PARTIAL(c3F0.30, cert 6/7)` — kz20/22/36/38/39/52 are now
certified source-purely (37/42 on the full ladder), no detector fired; the
razor kz15 misses by 0.12 dec, and its measured perfect-pairing potential is
0.49 dec against the needed 0.44: the remaining kz15 gap sits at the
**measured limit of the local class** at this window split (sub-paircorr).
r270 fought the kz15 boss under the binding reviewer adjudication (no F0.20
level-1 re-optimisation; three sealed attacks): the level-2 anatomy
**confirmed the reviewer's second-cancellation-level hypothesis in
substance** (pair-sum potential pot2 = 0.22 dec at kz15 vs the needed 0.18 —
headroom exists but only +0.04 dec) while measuring its limit: the pair-sum
sign sequence is coin-like (alternation fraction med 0.39), so the sealed
blind level-2 block triangle certifies 5/7 and leaves kz15 at 0.06 dec
(kz39 at 0.002 dec); the a-priori 2/3-absolute-mass split failed loudly
(`SPLIT_RULE_FAILED`, L2 4/7); and the third attack **closed the surface
honestly**: a certified outward-rounded interval evaluation of the full
bordered chain (mpmath.iv, dps 640, every f64 source atom exactly
converted, ~548 digits consumed by interval dependency over 202 steps)
encloses `Z_kz15` with width 1.5e-92 and proves `|Z| < sqrt(5/7)` **strictly,
margin +0.0268** — typed `EXACT_FINITE_CERTIFICATE`, a finite enclosure
statement (EnclOK kind), *not* a mechanism and *not* target-blind class
evidence. Verdict `KZ15_EXACT_ONLY`: the 42-rung surface is closed as
**41/42 mechanism-certified target-blind + kz15 exact-finite**; the open
mechanism edge is the kz15 level-2 sign structure beyond blind pairing
(0.06 dec, sub-paircorr).
r271 promoted the *fixed-form* r269 winner c2PAIR to a **theorem in pure
form** (hypothesis list H1–H5; H5 — the margin `|Z_local| + eps < sqrt(5/7)`
— is the only window-dependent input) with three sealed parameter-free
refinements: the exact boundary group (b1), the level-2 double-pair triangle
(b2, radius 4), the sharp envelope constant (b3, honestly coarser).
Verdict `UNIVERSAL_STILL_PARTIAL(c2PAIR, 5/7)` under the sealed tie-break;
the honest edge: **b2LEVEL2 leaves kz39 at 0.002 dec and kz15 at 0.06 dec**
(full ladder 31/42), no detector fired, the regression ward held. The
N-scaling census typed the cofinal entry door (lemma list L1–L5); the
measured pair-sum trend `sp(N, eps) = +0.67` says lemma L2 (pair-sum decay)
must supply a mechanism the plain pair triangle does not have. The finite
pair algebra is **proved in Lean** (`rh/lean/RH/PairBound.lean`); H5 stays
the documented `sorry`.
r272 dissected that alarm in a pure anatomy round (no new certificate, no
bound modification): the sealed c2PAIR bound factorizes **exactly** as
`eps = A x B x C + tail` (pair count x amplitude x bound-side cancellation,
all ratios to the demand `sqrt(5/7)`), and the measured exponents are
**alpha(A) = +1.01, beta(B/M) = -0.81, gamma(C) = -0.01**: the +0.67 trend
is carried by count x amplitude (`~N^0.2`) while the pairing's cancellation
capture is exactly **flat** (~53 % of the bulk mass at every depth). The
truth side moves the **other way**: the true bulk rest falls
(`sp(N, |R|/M) = -0.31`), the true cancellation deepens
(`gamma_true = +0.45`), and the truth margin `M - |Z|` **rises** with N
(sp +0.36, halves +0.26 → +0.41) — sealed adjudication
**`BOUND_COARSENESS_CONFIRMED`** (possibility B: H5 is not contradicted by
any measured truth trend; the bound loses cancellation, 0.35 → 0.63 dec).
The loss decomposes exactly as `loss = gap12 + slack2`; the growing part is
**c3 slack2** (beyond blind level-2 pairing, 0.22 → 0.50 dec, coin-like
P signs at every lag) — the quantified flip condition
(`FLIP_CONDITION`, typed task, no claim): the L2 lemma needs a
**non-adjacent/global mechanism** supplying `N^{-delta'}` with
`delta' > 0.21`, of the measured available truth decay `0.45`
(`TRUTH_ALLOWS`, ~0.25 exponent margin).
r273 ran the reviewer-adjudicated **mechanism round**: a sealed Euler
perturbation ladder (four graduated source surgeries on the comb — weight
assignment at reach `n^theta`, support jitter at local atom-spacing scale,
Euler-family (SAMEP) decoupling via the r254 integer-root labels, segment
shuffle at preserved local length `n^(1-theta)`; 3 thetas x 3 pinned
replicates x the full 42-rung ladder = 1512 perturbed worlds, conservation
identities exact on all) against `gamma_true`. Sealed outcome
**`PERTURBATION_INSENSITIVE`**: *no* surgery collapses the truth-side
cancellation at any strength — every stage median stays ≥ +0.20 and mostly
at or above the MAIN +0.45 (free permutations cancel even *deeper*): the
`N^{-0.45}` deepening is **near the generic root-scale baseline, not an
arithmetic fingerprint**. The sharp finding is the **firewall map**: every
tested surgery destroys free-prefix positivity (flip degrees 33–43 for
assignment/jitter/window, 66–101 for the family surgery — the r243 flip
census reproduced at ladder scale, pp = 0.00) — **the wall, not the
cancellation rate, is what is arithmetically special about MAIN**. The
resulting L2 hypothesis (typed task, no claim): the missing
`delta' > 0.21` is *generic* level-2 sign equidistribution; the lemma task
is to capture generic cancellation source-purely without crossing the
PAIRCORR firewall — mechanism candidates that need SAMEP coherence, exact
support or assignment structure are measured to aim at the wrong carrier.
In the same round the **Lean pilot was repaired** under the reviewer
adjudication: the three open statements were universally quantified over
pure bookkeeping structures and hence **refutable by trivial models**
(`q_N = 4` ladders, `tau_1 = -1` chains, `2 < 1` margins) — the
refutations are now permanent machine-checked guards
(`RH/Counterexamples.lean`), the window is a concrete structure
(`VonMangoldtWindow`: nodes, signed comb/archimedean weights, window
rule, derived half-filling cap, border vector, budget), and the two
former edges are consolidated into **one master target**:
`augmented_prefix_positive` — positivity of the augmented matrix
`A_{w,n} = [[H_n, u_n], [u_n^T, B]]` through the half-filling cap on a
MAIN window (`MainWindow` = the honest opaque source predicate). The
derivation chain is *proved* in Lean (upper block ⇒ Sylvester prefix
chain `h > 0` = former edge B; Schur complement ⇒ `D_n > 0` ⇒ `q_N < 1`
= former edge A; `D_n = B − u^T H_n^{-1} u` proved via mathlib
`det_fromBlocks₁₁`); the 5/7 floor falls out as a consequence instead of
entering as an axiom. Sorry count 7 → 6, every one truth-capable.
r274 built the reviewer-demanded **smallest hard test** before the oriented
midpoint theorem: the exact **Wronskian dictionary** for the two-sided
midpoint geometry (`wronskian_dictionary_probe.py`, 32/32). The right
solution exists in **three exact constructions** (residue route; *from the
right* with the exact Dirichlet boundary `q_S == 0` — the node polynomial
is the right boundary condition; r230 mirrored dual chain transported
through the r231 L-gauge), and the dictionary closes in both variants:
**base** `h_n = pihat_{n+1} q_n − pihat_n q_{n+1}` with constant `c' = 1`
(exact in rationals, symbolic in z, and at every degree on the mains and
the 42-rung ladder), with the **h-free midpoint form**
`pihat_{n+1} pihat#_{S−1−n} − beta_{n+1} pihat_n pihat#_{S−2−n} = L(z)` —
the r231 sign-blindness as an identity (the gauge-normalized midpoint
Wronskian is the node polynomial, carrying *no* orientation); and
**augmented** `D_{n+1} = B − W^aug_n / W^base_n` with the border-paired
Casoratian `W^aug_n = ∫ (pihat_{n+1} qs_n − pihat_n qs_{n+1}) dsigma =
h_n S_n` (exact against the independent determinant route on the r263
instances, at mp to the w9 terminal `D_N = +0.561250` dev 4.2e−12, and at
the kz15 razor terminal dev 3.5e−11). The honest c-typology: `c_n =
1/W^base_n = 1/(h_0 prod beta_k)` — a source-pure chain-coefficient
product whose positivity on the free prefix *is* the prefix positivity;
the orientation content of the dictionary sits **entirely in c_n** (r231
G12 at dictionary grade), and c is neither the wall nor the target
(fingerprints 0.74/0.36 < 0.9, scopes clean). Verdict
**`WRONSKIAN_DICTIONARY_GO + ORIENTATION_PREVIEW`**: the Prüfer band
`0 < Theta^L − Theta^R < pi` equals `h_n > 0` exactly, MAIN stays in-band
through the whole free window, the controls exit **degree-exactly at
25/21/27**, and the w9 winding census (mp, full continuation) measures
262/366 in-band with first exit at 184 = N_w — the **Maslov round is
freed**, the target `W_{w,n} > 0` (orientation, not magnitude) stays OPEN.
r275 ran the reviewer-authorized **track 2 of the double attack** — the
`l^1 → l^2` currency reform in state-space form (`kyp_memory_probe.py`,
24/24): the exact level-2 block decomposition of the bulk rest (run pairs,
offset 0, odd tail its own block) as a dimension-2 state system
`x_j = (acc, 1)`, `T_j = [[1, b_j], [0, 1]]`, `C_j = (0, b_j)` (pure exact
bookkeeping, `acc_J == Z` rational dev 0 on 47/47 worlds), with the
binding KYP memory ladder constant → even/odd → period 4 → Riccati
adjudicated **exactly** (rational LMI checks, no floats in any gate). The
outcome is a **two-sided no-go**: (i) every uniform quadratic memory is
**INFEASIBLE by structural algebra** — the homogenization fiber forces
`p11 = 0` (killing terminal usefulness) and the descent windows
`sum b^2 > 0` kill the LMI chain outright, machine-verified on 46/46
worlds including the trivial SMOOTH anchor (a structure theorem about
additive accumulation of sign-free drives, not a cancellation issue);
(ii) the unique admissible source-dependent memory (backward Riccati) is
**FORCED to carry the exact signed tail sums** — its budget is
`Z^2 + sum b^2`, the inverted terminal readout itself
(`KYP_IS_TARGET_INVERSE`, fingerprint sp +1.00; it "certifies" the
broken SCRAMBLE world — the friendliness signature — while failing EPST
exactly where its wall kips at the terminal); and (iii) the naive generic
root-scale `l^2` repackaging is QM-AM-coarser than the sealed `l^1`
pairing on every world (overhead med +0.15 dec, generic census 8/42).
Reading: the covariance a quadratic form would need is exactly what r273
typed GENERIC — per-window data, not source law; quadratic storage
without a sign/covariance law either dies (uniform) or reads the answer
(Riccati). The L2 task keeps its r272 address (non-adjacent/global
mechanism, `delta' > 0.21`) — with the state-space vehicle now excluded
alongside `l^1` refinement.
r276 measured the reviewer-adjudicated **dose-response curve of the
arithmetic** (`minimal_firewall_probe.py`, 25/25): the r273 firewall map
(every surgery kills the wall at binary strength) refined from binary to
graduated to **minimal** — five sealed surgeries (neighbor weight swap,
support jitter at `theta` × the local atom gap, family decoupling, and two
new grid-density surgeries separating the **sign field** from the
**magnitude field**) at doses SINGLE + `theta` 0.02–0.25 on three windows
(360 worlds, conservation and dose accounting exact, every borderline flip
mp-counter-checked at dps 40 — including the v956 boundary flip **at**
`N_w = 184`). Sealed outcome **`FIREWALL_LAW` + `CONTINUUM`**: the wall is
**not** an all-or-nothing firewall — single minimal operations typically
leave survival depth 0.88–1.00 of the free window (position-dependent
lethal exceptions at degrees 51–152), the v956 control level (0.11–0.15)
is reached only inside the graduated ladder, and the deficit laws are
shallow and saturating (`D ~ theta^b`, `b` +0.04…+1.09 — immediate onset,
no critical dose). The property ranking is the round's surprise:
**support exactness is the most wall-critical property** (jitter at 2 % of
the local atom gap already costs 3/4 of the depth; tolerance ranking
P2_JIT 0.343 < B2_MAG 0.389 < B1_SIGN 0.536 < P1_SWAP 0.621 < P3_FAM
0.700) — the wall reads the **metric placement** of the signed source
(positions, magnitude-position pairing) more exactly than the Euler-family
bookkeeping; the map transports across windows (sp +0.84/+0.86). Typed
MEASUREMENT_ONLY: the firewall hypothesis (wall carried by exact metric
placement, graded loss law) is a quantified falsifiable task, not a
mechanism claim.
r277 ran the reviewer-demanded **blind Prüfer/Maslov census**
(`maslov_census_probe.py`, 29/29) — predict the flip degrees from
phase/counting data instead of restating `h_n > 0`. The sealed protocol
(training = w9 + the 4 smallest-N rungs + their scramble(seed 2)
variants; three sealed candidate classes with fixed priority; blind =
the remaining 37 rungs + w12/w13/w26 + EPSTEIN/SCRAMBLE/SMOOTH) selected
**R2 = interlacing/reality of the Jacobi zeros** and passed the blind
GO: **37/37 rungs + all mains SAFE at full depth, controls fire at
26/22/28 = flips 25/21/27 + 1** (inside the sealed ±1), r259
energy-branch separation 17/6/9, and **not h-equivalent** (79 pattern
mismatches against the 78 h re-entry pivots on the w9 continuation —
the rule is a one-way break detector, not the sign chain). The round's
central finding answers the r274 winding warning: the **raw atom-counted
Sturm census is NOT the winding quantity** — on MAIN it breaks at
n = 56/48 with h positive throughout (zeros escape the atom hull, then
pair up inside single atom gaps: the positive-measure separation theorem
genuinely fails for the signed comb), while the interlacing/reality
structure provably holds on every positive prefix (β > 0 ⇒
symmetrizable ⇒ real + Cauchy-strict) and breaks at exactly `nf + 1`
everywhere (w9 continuation fire 185 = N_w + 1).
`STURM_CHAIN_VERIFIED` is honestly **not** awarded (the c1 atom-count
expectation is refuted — that refutation is the finding); the Sturm
rotation `#eig(J_n) < x* == n − #signchanges` is machine-exact on both
mains, and the oriented midpoint theorem (Maslov index through the
interlacing break) is the named next round.
r278 turned the r276 continuum into the reviewer's demanded **local
stability law** (`metric_stability_probe.py`, 31/31): the **exact
first-order sensitivities** of the wall against atom positions, derived
Hellmann–Feynman-style (`d log h_n/du_j = ⟨wdot_j, pihat_n²⟩/h_n` — the
polynomial variation drops by orthogonality) and via the border/CD kernel
(`dF_n/du_j = −⟨wdot_j, pihat_n B_n⟩`, `B_n = Σ_{k<n} F_k pihat_k/h_k`),
pushed through the sealed tent-grid channel (piecewise linear, lever
`m_j/(2D)`) and machine-gated against Richardson FD and mp (dps 40) to
1e−7. Structural disclosure: on w9 `alpha = log 16` makes the grid
commensurate with `log 2` — the **entire 2-power family sits exactly on
tent nodes**, so the gradient is carried as a one-sided pair with
side-selected predictions. Sealed outcome **`METRIC_STABILITY_LAW` +
`GRADIENT_EXPLAINS_DOSE(PARTIAL)`**: the local law exists (curvature
TAME, consistency 1.02), the stability inequality
`margin(c) ≥ margin_MAIN − L_D(w)·theta − O(theta²)` holds with exact
measured `L_D(w)`, **but its strict window `theta*` ~ 8e−4 (w9) / 1.2e−4
(kz55) sits 25–170× below the smallest r276 dose**: the measured 0.02
collapse is already a nonlinear cascade (first order under-predicts the
losses ~2.4×, ratio 0.41, and reaches the flip criterion on only 2/9
replicates). The **u-profile** (the r276 follow-up) is closed and
surprising twice: the gap-weighted sensitivity is **bottom-loaded — the
small primes 2, 3, 5 carry it** (hull correlation −0.80…−0.83, weight
+0.74…+0.82), it **predicts the single-op lethality** (deterministic
±gap singles, 66/70 flip, sp −0.82 — the r276 lethal exceptions located),
and the terminal-margin map shares the same geometry (sp +0.83). The
N-scaling says the margin sensitivity does **not** grow with N (halves
slope −1.09, non-monotone, decade 17.3): no fragility razor, but also
**no uniform stability constant** — the honest `MainWindow` consequence
is typed **PERTURBATIVE_ONLY**: `MetricNear(c, MAIN, theta) :=
max_j |u_j − u_j^MAIN|/g_j ≤ theta ≤ theta*(w)` inherits wall positivity
from MAIN positivity per window with window-specific `L_D(w)`; the MAIN
positivity itself remains the open center (H5 untouched). Control
contrast: at low degrees the arithmetic combs (MAIN, EPSTEIN) are
position-**blind** (~1e−14) while the metrically wrong worlds (SCRAMBLE,
SMOOTH) already carry O(1e−2…1) sensitivity — the low-degree gradient
separates metric randomness from arithmetic structure; the wall depth
separates the arithmetic combs among themselves.
**Wave 4 (2026-08-25)** promoted rounds r260–r278 into the load-bearing
suite as **`v960_terminal_surface_closure.py`** (r260/262/263/268–271
theorem set + r272/273/275 typed measurements; ledger
`PRIME.PORT.COUPLEDTAU.SURFACE_CLOSURE.01` [E]) and
**`v961_midpoint_orientation_dictionary.py`** (r274/277 theorem set +
r276/278 typed measurements; ledger
`PRIME.PORT.RHP.MIDPOINT.ORIENTATION_DICTIONARY.01` [E]) — both embed
their probes byte-exact and execute them in the sealed `--smoke` stage
(the full records stay sealed experiments-side and are re-verified by
this suite); two new open contracts registered:
`PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01` [O] (round 279 in flight)
and `PRIME.PORT.WALL.METRIC_FIREWALL.01` [O]. The rh/ pipeline gate
landed: `bash build.sh audit` now runs `run_rh.py --fast` as its own
"RH workspace" section.
r279 ran the **oriented-midpoint proof round** for exactly that first
open contract (`oriented_theorem_probe.py`, 32/32,
`PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01` — experiments-side, no
status move) — build the theorem or name the missing step-5 ingredient
exactly. The round constructs the **two-sided index bilanz** (left
chain degree `n` vs dual degree `S−1−n` against the S common nodes of
the gauge polynomial `L`) and delivers two new exact, world-blind
theorems: the **TWO_SIDED_PARITY_THEOREM** — from the r274 node
identity and the `L'` alternation, the union polynomial
`Q_n = pihat_n · pihat#_{S−1−n}` has `sign Q_n(x_j) =
e_j (−1)^{S−1−j} sign(h_n)`, so its real zeros are ODD-many in every
weight-agreement gap (≥ 1 forced, never empty) and EVEN-many in every
disagreement gap, at **every** degree and independent of the h sign
(exact in rationals on the toys; 246 212 sign gates + full-degree
occupancy sweeps on the real combs; the |D| weight-sign boundaries are
exactly the slack of the bilanz, and the census identity
`c + c# = (S−1) − |D| + 2·scD` is exhaustion-proved to k = 8); and the
**CROSSING_BUDGET_THEOREM** (Jacobi's minor-sign rule + Sylvester
congruence): the number of crossings over the FULL algebraic
continuation is **exactly the negative-atom count**,
`#{n < S : h_n < 0} = S_−`, machine-gated on every world (w9 104, w13
98, EPST/SCR/SMOOTH 141/94/6, kz15 121, kz52 551). The sealed
candidate adjudication is honest: **STEP5_OPEN** — no non-restatement
invariant kips at `N_w` (tight two-sidedness never fails anywhere = a
theorem, not a separator; union reality / shared gaps / left-in-D die
at degrees 1–4 world-blindly; the first crossing itself is the h
restatement), and the b2 obstruction implication is
**OBSTRUCTION_REFUTED by exact rational counterexamples** (the
two-sided compatibility state does not forbid a crossing). Two
measured surprises (disclosed amendments a1/a2): the localization
equality is **not universal** — w13 crosses first at `N_w + 2`, kz15
at `N_w + 1` (w9 and kz52 exactly at `N_w`) — and the r277 R2 anchor
is co-located with the **first crossing** (`min C + 1`), not with
`N_w`. Verdict **`MAIN_SPECIFICITY(LOCALIZATION_IS_THE_ARITHMETIC)`**:
every theorem of the bilanz holds on all controls before *and* after
their flips (25/21/27) — the two-sided machinery carries no
arithmetic; the **entire** arithmetic content of the wall is *where*
the world-blindly fixed budget `S_−` is spent. The precise
Lean-suitable gap statement (the honest step-5 sorry, matching the
`Window.lean` master theorem): for every MAIN window,
`∀ n < N_w : h_n > 0`, i.e. `min C ≥ N_w` — the localization of the
Jacobi-fixed crossing budget into the upper half of the continuation.
NO RH CLAIM.
r280 measured the **localization anatomy** of exactly that budget
(`budget_localization_probe.py`, 29/29,
`PRIME.PORT.WALL.BUDGET_LOCALIZATION.01` — experiments-side, no status
move): the **full 42-rung offset census** — `min C − N_w` takes the
values {+0: 18, +1: 10, +2: 6, +3: 6, +4: 1, +5: 1} across the entire
frame-A ladder (max **+5** at kz43; the v956/r279 anchors 0/2/2/3/1,
kz15 +1, kz52 +0 reproduced exactly; half-filling `N_w = ceil(S/2)` on
42/42; mp dps-40 arbitration exact), with `sp(offset, N) = +0.096` over
`N ∈ [142, 878]` — the offset stays O(1) with **no N-growth trend**, and
the r276 dose curve is the same coordinate (`min C == nf` definitional;
the P2_JIT medians 0.250/0.207 reproduced with the exact r276 seeds).
The round's core finding is the **extremality answer**: the w9 extremal
localization `min C = N_w` is **NOT a local maximum** of the
localization functional — the r278-gradient directions
(OPT/OPT_SAFE/SMALLPRIME) push the first crossing **past half-filling**
(`min C` 184 → 185 at `theta` 7.7e−5…1.6e−4, all mp-confirmed;
first-order census: every second random direction raises, because the
crossing is *shallow*, |h_184| rel margin 1.9e−3) — the b3 variational
hypothesis is **REFUTED in its local-maximum form**; the crossing
log-gradient is anti-aligned with the last free pivot on all three
tested worlds (`cos_w ≈ −0.97`, the h-sign flip of a raw-gradient
lockstep — `CRITICALITY_STRUCTURED` by the sealed cosine rule); the
offset windows kz15/w13 stay UNRESOLVED at the tested doses. The
**duality lens is exact**: `h_{S−m}·h#_{m−1} = 1` and the sign mirror
`sign h#_k = sign h_{S−1−k}` (toys in rationals, w9 at mp) translate the
localization statement exactly — `min C ≥ N_w` **is** the confinement of
all `S_− = 104` dual negative pivots to the lower dual half, and w9
**saturates** the bound (max negative dual pivot 182 = `S−1−N_w`);
typed `DUAL_RESTATEMENT` (same signature, no isolated carrier). The
moment view is honest: the natural mu/nu **Weyl minor-perturbation
argument dies at n = 3** (`X_weyl = 2` of `N_w = 184`, 1.1 %), the
raw-moment rest zone does not exist on any world, and the PAIRCORR
detector types **both** arguments WORLD_BLIND (SMOOTH exceeds MAIN at
Weyl level) — neither carries the localization; the r279-b3 gap
statement stands unchanged. NO RH CLAIM.
r281 ran the **pinning-anatomy round** on the reviewer's reframed
question — not maximality but *pinning*: why is half-filling the
natural pinning point? (`halffilling_pinning_probe.py`, 28/28,
`PRIME.PORT.WALL.HALFFILLING_PINNING.01` — experiments-side, no status
move). The round's exact core is the **counting theorem**: pivot `h_n`
consumes `m_0..m_{2n}`, an S-atom signed measure has exactly S free
moments (Vandermonde bijection, freedom demonstrated exactly: `dm =
e_{S−1}` moves the last free pivot alone), all `m_k, k ≥ S` are forced
by the node-polynomial L-recurrence (toys exact in rationals; w9 at mp
dps 200 with max rel residual 7.6e−157) — so the **free pivots are
EXACTLY `h_0..h_{N_w−1}`** and `h_{N_w}` is the first forced pivot:
"why half-filling" has the exact answer **because the free moments end
there**. The upper-side theorem attempt is adjudicated honestly:
**`UPPER_PINNING_MEASURED`** — the v956 boundary statement ("the wall
dies immediately past the cap") is two computational paths + an mp
ward on five windows, i.e. *measurement*; the measured pinning
constant is `C = 5` (42-rung census, minC ≥ N_w everywhere); the only
*proven* upper bound today is the pigeonhole ceiling `minC ≤ S − S_−`
(from the r279 budget theorem; w9: 184 ≤ 263 = p, 79 degrees above
`N_w`); and **world-blind O(1) upper pinning is REFUTED exactly** — a
single-tiny-negative toy measure has `minC = S−1` (offset `N_w − 2`,
unbounded in S): any O(1) upper side must consume the comb structure.
The offset anatomy is a clean negative: six sealed source-pure
tail-coupling candidates (last free margin, margin slope, first-forced
moment cancellation, negative-weight fraction, razor position) reach
max |spearman| = **0.273** vs offset over the 42 rungs —
`OFFSET_UNSTRUCTURED`, no predictive offset formula in this census.
The relay question closes honestly too: the per-degree condition
`B_n = [beta_n > 0]` is typed **RESTATEMENT** (no h-blind margin proxy
predicts the flip location on all five worlds), and the r280
anti-alignment `cos_w ≈ −0.97` is measured to be the **h-sign flip of
a raw-gradient lockstep** (`cos_raw ≈ +0.96..0.98` at every crossing;
all four dead-world crossings type CREEPING — crossing *type* does not
separate the worlds). Verdict **`PINNING_DECOMPOSED`**: pinning =
counting theorem (upper location, exact) + forced-pivot death within
O(1) (measured) + free-window survival (the lower side — the open
center, now with the sharpened reading "why does MAIN survive all its
free degrees"). NO RH CLAIM.
r282 ran the **representation contest** on the north-star question
"what IS `h_n`?" (`representation_contest_probe.py`, 30/30,
`PRIME.PORT.REPRESENTATION.CONTEST.01` — experiments-side, no status
move): four classical representation classes, each with a construction
attempt on exact toys and one brutal gate — the representation must
force MAIN positivity *structurally* AND provably reject an
early-dying control (calibrated on a positive-class toy, where the
classical structures MUST exist — and do). All four die with exact
eliminations: **K1 (RHP/monodromy)** is a RESTATEMENT — the Pontryagin
split `h_n = P_n − N_n` is exact everywhere, but the
`|m|²`/sum-of-squares structure exists iff the negative register is
empty (only the positive class; MAINLIKE has N/P = 0.538 at its last
free degree, w9 carries negfrac 0.498 at the wall), and the surviving
clause `N < P` is `h > 0` verbatim. **K2 (Hodge/Kasteleyn
orientation)** is NOT CONSTRUCTIBLE — full exhaustion over all `2^S`
gauges shows the coherent orientation class over the Cauchy–Binet
configuration space is *exactly* `{±sign w}` (the quadratic/edge class
collapses at the n = 3 cells), and that unique gauge changes the value
by exactly 2×(negative mass) (w9 defect 0.115): orientation exists iff
`S_− = 0`, and MAIN is signed — the r261 no-go upgraded from a pairing
failure to a **class obstruction**. **K3 (de Branges/canonical
system)** is a RESTATEMENT — Hamiltonian positivity ⟺ `h > 0` exactly,
and the only independent shadow (R2 interlacing) lags +1 on every
flipping world (toys exact, controls 26/22/28/26 = flip+1, w9 SAFE
through 183): it detects, it never forbids; forcing the Hamiltonian
positive (`|β|`) provably changes the measure. **K4 (operator/dual
pair)** is WORLD-BLIND by theorem — `h_n · h#_{S−1−n} = 1` exactly, so
the dual pair is sign-synchronized *identically* in every world: the
"joint positive structure" adds no second constraint, and global
positive structures are killed by the r279 budget theorem. Overall
verdict **`CONTEST_ALL_DEAD`** — a program finding: the pivot
positivity has *no representation in the four classical languages at
this resolution*; each language forces positivity exactly for the
positive measure class, and MAIN is signed. The lower side (why MAIN
survives its free window) stays the open center. NO RH CLAIM.
r283 ran the **big RHP attack** on the north star (full source →
monodromy property → quasi-definiteness of the complete free window;
`fullsource_quasidefiniteness_probe.py`, 26/26,
`PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` — experiments-side,
no status move): three sealed candidates. **A2 (monodromy
factorization over μ/ν)** is the carrier — verdict
**`MECHANISM_PARTIAL`**: in the μ-orthonormal frame the full Hankel
form of μ̃ is `I − M_n`, and the node Gram `E_n = B_n B_nᵀ` is
*exactly* the v881/r224 IIKS kernel (μ-CD kernel dressed by the ν
weights). Steps s1–s4 are EXACT (split; unit-triangular congruence
`minor_k(D_μ − G) == D_k(μ̃)` — rationals on five toys, slogdet dev
3.4e-9 on w9; frame contraction `h > 0` through degree m ⟺
`λ_max(E_m) < 1`; monotone rank-one loading ⇒ `λ_max` crosses 1
**exactly at minC+1**). World test exact on all seven worlds: w9 185
= minC+1, w13 171 = N+3, kz15 205 = N+2, controls 26/22/28/26 =
flip+1 — the *same* degrees as the r277 R2 fires: the contraction IS
the split-source form of the r277 reality/interlacing condition. The
capacity step is adjudicated both ways: the pigeonhole ceiling
`minC ≤ S₊` is *re-proved* in the frame (null-polynomial witness,
exact), and capacity-as-COUNTING is *refuted* exactly (rank-one pair
with identical rank/support and opposite window fate; the deciding
value is metric: 1.25e-13 vs 1.25e+2). What remains is ONE formal
scalar, the **missing lemma L\***: for MAIN, every real polynomial
`p` with `deg p < N_w` has `∫p²dν < ∫p²dμ`, i.e. `λ_max(E_{N_w}) < 1`
(measured margin 1.68e-4, top eigenvalues 0.99983/0.99874/0.99597 —
broadly tight, not a single-mode squeeze); given s1–s4 this single
inequality ⟺ full free-window quasi-definiteness. **A3
(free-window Fredholm determinant)** COLLAPSES onto A2 (zero-freeness
of `det(I − sE_{N_w})` on (0,1] is the contraction scalar; s* = 1/ρ
dictionary + degree-resolved slogdet co-location 185/26). **A1
(Schwarz/J-symmetry)** is DEAD at the residue-positivity step: the
reflection symmetry of the real jump data holds identically on every
world (world-blind, cannot carry), the Herglotz condition fails on
MAIN itself (S₋ = 104 negative residues), and the windowed η*
anatomy is world-blind by the sealed distance rule. Forbidden-list
bilanz: triangle/Gershgorin bounds die at n = 21 ≪ 185; no
target-inverse quantity, no truncation, no posthoc window (mutants
flagged). The RHP language holds exactly ONE invariant on this
question — the contraction scalar; the open center is L* itself.
NO RH CLAIM.
**Wave 5 (2026-08-25)** froze rounds r279–r281 as a **small mathematical
theory** (the reviewer demand: "not just as experiments") in
**`v962_halffilling_pinning_theory.py`** (ledger
`PRIME.WALL.HALFFILLING_PINNING_THEORY.01` [E]; the three probes embedded
byte-exact in the sealed `--smoke` stage, plus a module-own exact section
in pure Fractions): four named theorems — **T1 moment counting** (the
free pivots are exactly `h_0..h_{N_w−1}`; "why half-filling" = the free
moments end there), **T2 crossing budget** (`#(h<0) = S_−`,
Jacobi/Sylvester, world-blind), **T3 two-sided parity** (h-blind; census
bilanz + exhaustion), **T4 main window reduction** (the entire open
statement is `minC ≥ N_w` ⟺ `∀ n < N_w : h_n > 0`) — and four named
refutations (**no universal O(1) pinning** — exact, unbounded-offset
one-negative family; **no extremality** — the w9 crossing is liftable
past half-filling; **no generic Maslov obstruction** — 3 exact rational
counterexamples; **no simple offset law** — max |sp| 0.273, all
world-blind). Rounds 279–281 are consumed on
`PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01` [O] (theorem share
promoted, center precisified); the two successor lanes are registered as
`PRIME.PORT.REPRESENTATION.CONTEST.01` [O] and
`PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` [O] (the r282/r283
rounds are sealed experiments-side and NOT consumed by wave 5). In Lean
the hole is now fog-free: `free_window_positivity` is the one central
`sorry` in base coordinates (T1/T4 proved for real, T2 stated, the exact
one-negative instance a permanent counterexample guard; build green,
8 intentional `sorry`s). NO RH CLAIM.
r284 read the missing lemma L\* as a **two-measure subordination
problem** (`lstar_two_measure_probe.py`, 30/30,
`PRIME.PORT.LSTAR.TWO_MEASURE_ANATOMY.01` — experiments-side, no status
move): ν (104 atoms) strictly μ-subordinate (263 atoms) on polynomials
of degree < `N_w`, with the structurally motivated Nyquist/shielding
hypothesis (resolution `π/n` on the θ grid vs the ν→μ pairing scale)
adjudicated sealed. Outcome, honest on every leg: **`SHIELDING_BLIND`**
— the source-pure pairing geometry is a *builder-channel* property (on
w9 every ν atom sits exactly one fold step from a μ atom, 100/104 fully
μ-neighbored; all four dead controls mirror the same near-perfect
pairing; all four sealed geometry statistics world-blind);
**`NYQUIST_ORDERING` with the honesty clause** — the sealed crossing
formula `n_pred = L/(4s)` holds the factor-2 band on all 42 rungs but
**fails on all four controls by 1.5–3 octaves** (they die at 22–28
despite near-perfect pairing): the support-geometry form of the
resolution hypothesis is refuted where it matters (the +0.998 spearman
is carried by trivial `N_w` scaling); **`CHRISTOFFEL_RANGE`** — the
round's core: the exact sandwich `max_k v_k K_n(y_k) ≤ λ_max(E_n) ≤
trace(E_n)` brackets the wall, and on w9 the pure **single-atom
Christoffel bound crosses at `n_DIAG = 187`, only two degrees above the
true crossing 185** (coherent assist 3.1 %, aggregate ν coherence
destructive: slack 50×), while on all four controls `n_DIAG` is never
reached — **MAIN's crossing is a near-single-atom Christoffel event,
control death is a collective mode**; **`EXTREMAL_ANATOMY`** — the
near-breaking direction is 99.7 % two background atoms at the shallow-u
hull edge *below the first prime* (folds 2/4, `u` = 0.03/0.06, the two
weakest-shielded ν atoms; SMALLP_DEPLETED — the r278 small-prime
sensitivity profile and the near-null direction of `E` are different
coordinates), the top-3 eigenvectors are ONE oscillatory edge band, and
the controls' breaking modes are more diffuse (PR 5.0–9.7 vs 1.89).
Detector: all seven sealed stats world-blind — the arithmetic lives in
the spectral coherence of the weights, not in the support geometry.
mp dps-60 ward: `ρ_184 = 0.99983248 < 1 < 1.00003660 = ρ_185`.
NO RH CLAIM.
r285 adjudicated the **decomposition perspective on L\***
(`christoffel_decomposition_probe.py`, 33/33,
`PRIME.PORT.LSTAR.CHRISTOFFEL_DECOMPOSITION.01` — experiments-side, no
status move): L\* split candidate-wise into **(D)** the per-atom
diagonal condition `v_k K_{N_w}(y_k) < 1 − δ` and **(C)** the coherence
condition `assist = λ_max/maxdiag − 1 < δ'`, with **exact bookkeeping**
(multiplicative identity `λ_max = maxdiag·(1+assist)` and the budget
equivalence `margin > 0 ⟺ ρ < 1` gated at every degree; the additive
Weyl form measured coarse, slack 0.287 — the multiplicative form is the
honest one). Verdict **`DECOMPOSITION_EXACT`**: the ladder budgets are
measured on all 42 rungs (`maxdiag_{N_w}` 0.9343–0.9941 with
`sp(N, maxdiag) = +0.65` — **the per-atom budget tightens toward 1 with
N**; `assist_{N_w}` 0.0059–0.0702 with `sp = −0.65` — the coherent
assist shrinks: **no fixed δ/δ' budget is supported by the measured
trend**); the controls rip at (C) at their death degree (maxdiag
0.26–0.38, assist 1.69–2.99, off-diagonal share 0.63–0.75).
**`PERATOM_CLASSICAL`**: the binding atom is the shallow-u ARCH edge
below the first prime on 42/42 rungs (w9 leaders folds 2/4/6/8/10,
near-degenerate 0.9411–0.9700); the classical arcsine yardstick (typed
COMPARISON_ONLY) measures the binding atom's kernel growth at exponent
**0.38 — sub-classical** (bulk law 1): the classical isolation degree
`n*_bind = 58` misses `n_DIAG = 187` by 1.68 octaves and covers 0/42
rungs — **(D) survives *because* the discrete kernel grows
sub-classically at the binding atoms**; any provability route for (D)
must be a discrete bound, not continuum asymptotics. The round's
surprise is the **b3 answer**: (D) is **not** world-blind at window
scale — the controls' `n_DIAG` = 50–91 (≪ 184) vs MAIN's 187 > 185:
the per-atom half itself separates the worlds, refuting the clean
split "(D) metric-blind + (C) carries all arithmetic" *as stated*
(sealed verdict falls to `COHERENCE_UNSTRUCTURED` by the blind-D
clause), while at the **death degree** the split is clean and the
assist separates sharply (MAIN 0.0195 at its crossing vs controls
1.69–2.99, `MAIN_SEPARATING`; z-scores: MAIN −3.15 **destructive** vs
controls +4.95..+12.44 **constructive** — sign-clean, band-MIXED).
**`ENSEMBLE_POSITION`**: against both conservation-gated replicate
ensembles around MAIN (16 sign re-assignments, 12 position scrambles;
crossings 5–28), MAIN's **wall assist is the extreme low outlier
(pct 0.00)** while its early assist is scramble-generic (pct 0.75) —
the near-single-atom wall is MAIN-specific, the r273 genericity
finding measured from the other side. mp dps-60 ward incl.
`maxdiag_184`. NO RH CLAIM.
r286 measured the **decay law of the L\* margin and hunted the
large-S counterexample** (`lstar_margin_scaling_probe.py`, 29/29,
`PRIME.PORT.LSTAR.MARGIN_SCALING.01` — experiments-side, no status
move; the probe runs the **standalone document pipeline**
`rh/problem/verify_lstar_instance.py` verbatim and re-gates it
against the repository builders on the flagship *and* every new
anchor, devs ≤ 2.9e-15). **The law** (`MARGIN_LAW`): on the 42-rung
family the margin `1 − λ_max(E_{N_w})` follows a **power law in S**
(Theil–Sen `alpha = 3.05` vs S / 3.06 vs `N_w` / 2.39 vs z; MAD 0.61
vs 0.85 for the exp form; halves 3.67/2.07 — the law **flattens** at
large S, the honest anti-extrapolation flag), and the driver is
neither the diagonal nor the assist alone but the **cancellation
sharpening**: in the exact identity `margin = (1 − maxdiag)(1 − c_w)`
the factor `c_w = (λ − maxdiag)/(1 − maxdiag)` rises to 0.999991
while `1 − maxdiag` only decays with slope −0.69 — the r284/285
shallow-edge extremal band persists on all 42 rungs (PR median 1.81).
**The hunt** (`NO_CROSSING_EXTENDED`): the sealed extension rule (the
document admissibility rule with the window cap lifted, comb
completeness `z² ≤` table cap) admits 83 candidates; the first 15 by
`(N_w, kz)` — `N_w` 942–1218, S 1883–2435, z 101–547 — were built,
cross-checked and measured under the sealed sign-safety tier protocol
(f64 two-route equivalence via the r283 dictionary `margin > 0 ⟺
minC ≥ N_w`, plus mp dps-30/45 staggered verification on every
sub-1e-5 margin; 32/42 + 15/15 mp-verified, worst f64-vs-mp rel dev
6.6e-6): **all 15 margins strictly positive** (min `+1.806e-8` at
kz=119/z=529), the triple-verification counterexample protocol never
fired, and the 42-rung power fit **predicts** all 15 out-of-sample
margins inside one decade (`EXTRAP_CALIBRATED`, max dev 0.78 dec).
**The census** (`CENSUS_EXTENDED`): `minC − N_w` on the new anchors
is {0: 1, +1: 10, +2: 2, +3: 1, +4: 1}, max +4 — **the O(1) wall
offset survives beyond the family cap** (by the r283 equivalence
this is exactly why the margin *cannot* cross there). **The
reconciliation** (`QN_RECONCILED`): the r258 terminal bordered ratio
`q_N` measured on the same 57 rungs stays FLAT and O(1)-positive
(min `1 − q_N` = 0.019, spearman +0.35) while the spectral margin
falls 4.0 decades (spearman −0.87) — **two different objects**: the
exact Rayleigh inequality `λ_max ≥ ‖B[:, N_w−1]‖²` holds on 42/42
with the terminal direction far from the top (median 0.448), and the
extremal coefficient vector is **full-sector** (terminal-degree share
median 1.9e-8, degree PR median 188) — the terminal pivot cannot see
the sector the spectral margin lives in. The sealed HARMLESS/DANGER
adjudication (two disclosed calibration amendments, r270 precedent;
the original rule's outcome printed permanently) lands **HARMLESS**:
no crossing + census O(1) + the margin falls *slower* than the
pre-wall eigenvalue-loading speed (`margin/v8` 19–652, median 144 —
the benign direction) + `q_N` flat-positive: **the margin decay is
the spectral signature of the known O(1) wall offset (kinematic
eigenvalue-density shrinkage), not an approach to failure** — under
both sealed law forms the margin is positive at every finite S, and
any counterexample claim needs the measured census, not the fit.
NO L\* claim. NO RH CLAIM.
r287 ran the **standard-framework census for the L2 lemma** (the
30-pct lane of the reviewer split 70 L\* / 30 L2;
`l2_deterministic_cancellation_probe.py`, 25/25,
`PRIME.PORT.L2.DETERMINISTIC_CANCELLATION.01` — experiments-side, no
status move): WHICH classical deterministic cancellation framework
captures the level-2 block sums `P_j`? Four sealed frames, each an
exact per-rung bound on `|sum P_j| = |R|`, tested against the r272
flip condition `delta' > 0.21` and the 7-exception certification.
Verdict **`FRAMEWORK_PARTIAL`**: **F1** discrepancy/Erdős–Turán (exact
Abel form `D* × V`) dies loudly — both factors grow (`D*/sqrt(m)` med
1.90, no `N^{−β}`), delta' −0.21, cert 0/7, paircorr demand **FIRES**
(max +1.44 dec); **F2 van der Corput** at the frozen window
`H = ceil(sqrt(m))` — an **exact world-blind theorem**, no constant,
no fit, no arithmetic — delivers **delta' +0.31 > 0.21** and certifies
**6/7 exceptions** (kz20/22/36/38/39/52; ladder 38/42, demand max
+0.04); **F3** Salem–Zygmund sub-Gauss (measured constant `C` med 0.90
max 1.68, spread 1.86 STABLE, controls covered) delta' +0.38, 6/7;
**F4** MDS/Azuma against the sign-bin chain filtration (md_ratio 0.29
— the `P_j` are MDS-like; `C4` max 0.68 stable, covered) delta' +0.41,
6/7. The sealed `(cert, delta')` key adjudicates F4; the honest
research edge is **F2, the exact theorem at 6/7**. The kz15 razor
misses on every surviving frame by only **0.07–0.12 dec**. The
round's surprise, the **autocorrelation lag map**: only 5/44 rungs
(0 exceptions) have a positive root-scale cancellation deficit — on
39/44 worlds `(sum P)^2 > sum P^2`, the block sequence **reinforces**:
the c3 cancellation is already absorbed *into* the `P_j` magnitudes,
and the classical frames win by the `sqrt(m)`-count economy, not by
lag structure (large-lag mean `|rho|` 0.058). The L2 lemma candidate
after this round: **the vdC form as a provable chain statement**
(source-pure, window-independent) + the r269-known kz15 exact-finite
certificate for the razor. mp dps-60 wards; r272 regressions exact.
NO RH CLAIM.
r288 measured the **sign anatomy of the destructive coherence** (the
r285 `z_v = −3.15` address; `destructive_coherence_probe.py`, 31/31,
`PRIME.PORT.LSTAR.DESTRUCTIVE_COHERENCE.01` — experiments-side, no
status move): all E signs come from the mu-CD kernel `K_n` between nu
positions; phases measured against the zeros of the mu-orthonormal
`P_{N_w}` (Jacobi eigenvalues of the chain; Sturm counts, midpoint
alternation and mp dps-60 edge wards exact). **The carrier map**: the
sign field is band-structured — fold distance 1–2 is 87 pct
**positive** (in-phase sampling), distance 3–4 is 80 pct **negative**
(antiphase); the top mode at `N_w` rides the in-phase adjacent pairs
(band 1–2 = +0.68 of |T|, ARCH–ARCH +0.74) while the wall
destructivity in the source frame at the crossing (`X_v = −0.0517`,
`C_off = −0.105`) is carried by the **antiphase next-nearest (3–4
fold) ARCH–ARCH pairs**; the controls at their own crossing are ALL
constructive (`C_off` +0.30..+1.00) — a total sign reversal. The pure
sinc/CD sign formula explains the field only PARTIALLY (agreement
0.728 plain / 0.878 |E|-weighted, below the sealed 0.90 bar →
`SAMPLING_BLIND`); the sealed source-pure phase-dispersion separator
is **not found** (K_S1 world-blind, ensemble-generic; the plain
dispersion does not predict the wall, sp ≈ +0.2). The r287 object
comparison lands **`DIFFERENT_OBJECTS`** (the w9 block sequence
reinforces, canc = −4.5e-2 < 0, while the kernel-side wall
interference is destructive — two coordinates). The round's finding,
the **dose curve**: under conservation-faithful union jitter the
phase field barely rotates (turn rate 0.24/dose == the static
prediction; the chain zeros co-move) yet `z_v` flips destructive →
constructive already at dose 0.005 and the depth collapses — the
destructive coherence sits in hyper-fine alignments far below the
median phase resolution: **the r276 metric firewall is sharper than
any phase-rotation account** (measured; r276 P2_JIT quoted
COMPARISON_ONLY, different channel). Ensembles = the 28 r285
replicates, identical seeds, records re-gated; equidistribution
statistics typed MEASUREMENT_ONLY. NO L\* claim. NO RH CLAIM.
r289 ran the **arch-kernel diophantine relevance test** on exactly that
r288 finding (`arch_kernel_diophantine_probe.py`, 42/42,
`PRIME.PORT.LSTAR.ARCH_KERNEL_DIOPHANTINE_ANATOMY.01` —
experiments-side, no status move; strict reviewer contract: no proof
attack, **no Baker/Matveev application**, need documentation only) and
decided the sealed three-way question with the **arithmetic twin**
family. Verdict **`METRIC_ONLY`**: the **rational twin** — every tent
center `log n` replaced by a small-denominator rational multiple of
`Delta` (CF convergents, denominators ≤ 5.7e4, position cost ≤ 2.1e-9
= 1e-8 × the local gap; weights/cells/on-node family conserved
exactly) — **keeps the full signature identically** (minC 184,
crossing 185, `z_v` −3.149, carrier band 3–4 −0.105, AA −0.056; mp
dps-60 ward at the 1.7e-4 margin): every exact log-linear-form
relation is destroyed with **zero effect**; the **shuffle twin**
(tent-split fractions permuted, fraction *distribution*/cells/weights
preserved exactly, only the assignment destroyed) loses totally
(depth 0.21, `z_v` +4.4) but at effective metric dose 0.12 gap, where
the plain jitter ladder already loses — fully metric-explained. The
construction question is settled first: the lag vector factors
**exactly** through (cell, tent-split fraction, mass) — the fractions
`{log n/Delta} = {46 log2 n}` are the *only* sub-grid entry of the
source into the weights (completeness 4.2e-14; differences alone
underdetermine, LOUD; the folded weights are downstream-complete).
Q1 anatomy: `X_v` decomposes exactly over CD degrees; the
destructivity is carried by the **mid degree band 50–75 pct** (−3.17
z-units; carrier set −2.48), *not* the terminal degrees; at dose
0.005 with degree and frame fixed **no kernel band moves O(1)** — the
O(1) mover is the **crossing relocation itself** (pivot cascade 185 →
~131) while the phase stands still (0.0012). The measured **metric
threshold**: the coherence needs the fraction *profile* at ~1e-3 of
the local gap (ladder keeps at 1e-3, collapses at 3e-3) and is
indifferent to its number-theoretic exactness; the linear forms are
documented (28 exact 2-power resonances inside the window, min
nonzero `|{46 log2(n/m)}|` = 1.34e-6 at (181, 241), attribution tops
at the small primes 3, 7, 25, 8, 29, 17), and the need calculation
shows Baker/Matveev-class bounds ~7900× too weak in the exponent for
the unbounded family — **Baker is unnecessary on all tested scales**;
the sub-gap information the wall reads is metric, not diophantine.
NO L\* claim. NO RH CLAIM.
r290 mapped the **geometry of the working set in profile space**
(`profile_functional_probe.py`, 32/32, SPEC_SHA `f953dd71`,
`PRIME.PORT.LSTAR.PROFILE_FUNCTIONAL.01` — experiments-side, no
status move): profile = the signed lag density on the fixed grid
(the r289 completeness object; linear in the tent-split fractions
at fixed cells), distances = gap-equivalent doses `theta_eq` in the
exact lag coordinate (analytic reference `0.5 Σ m g/Δ`; amendment a1,
demanded by the sealed self-consistency gate). **The onset map**
(five sealed weight-profile interpolation paths, NEAR = 0.90 bar):
world-directed axes kill at `theta_eq` 4e-5..2.3e-4 — **5..50×
below** the 1e-3..3e-3 jitter threshold — the rim is strongly
**anisotropic**; every onset is **GRADUAL** (soft shoulder, s 0.95 →
0.77..0.89; curvature |kappa| ≤ 0.08 — no cliff). **Isotropy**: a
thin **TUBE** (killfrac 1.00 at 3e-3 over 16 conservation-gated
random directions; NEAR-radius ~5e-4..2e-3, consistent with the
r285 ensemble pct 0.00). The **SMOOTH (arithmetic) direction** is a
privileged killer axis (onset 1.36e-4) yet **orthogonal** to the
first-order wall gradient (cos −3e-5): its lethality is collective,
not gradient-linear. The **r280 ridge axis** is real geometry: the
rebuilt OPT direction (theta_up 3.873e-5 anchor exact) **lifts** the
wall (minC 185) at extension factors 1..8 = `theta_eq` up to 1.2e-3
— inside a tube where half the random directions already kill — and
only dies at 2.4e-3. The **functional contest** (four sealed
source-pure profile scalars: antiphase 3–4 autocorrelation = the
r288 carrier band, total variation, perturbative r278 gradient
alignment, mid-band 50–75 pct deviation energy = the r289 flip
carrier) ends **`ALL_FUNCTIONALS_BLIND`**: best spearman +0.263 over
the 187-point test set (bars 0.5/0.8), none separates the worlds
non-trivially — the coherence functional, if it exists as a closed
profile scalar, is **not among these classes**; the working set
remains implicitly characterized. Channel identity gated bitwise on
MAIN; r288/r289 records, the r289 jitter-ladder anchor (exact
seeds), the r285 control flips and all 28 replicates (ENS_SIGN as
exact density sign-flips) reproduced. NO L\* claim. NO RH CLAIM.
r291 dissected the **anatomy of the one known raising axis**
(`ridge_anatomy_probe.py`, 30/30, SPEC_SHA `bb512c17`,
`PRIME.PORT.LSTAR.RIDGE_ANATOMY.01` — experiments-side, no status
move; amendments a1–a3 disclosed: r290 pinned metric quadruple,
1e-9 conservation-gate headroom, matched-dose/global reporting
split). **Ridge section**: the lift is **not** a distinguished
sparse support, band, or hidden functional — near the threshold it
is a **first-order budget phenomenon**: a conservation-gated
sub-direction lifts exactly when its side-selected linearized wall
budget `-Σ c_j·dose` exceeds one sharp scalar threshold in
**(1.280, 1.291]** (~1.3× second-order resistance over the naive
flip level −1; perfect separation over all 18 matched-dose subset
cases: PRIME/HEAD/XIPOS lift, POWER/MID/TAIL/XINEG do not; k_min =
9 top-budget atoms n = 2, 3, 5, 13, 11, 4, 29, 7, 89 — small-prime
head-heavy, not one-atom), with exactly one **overdrive
retraction** deep in the over-driven few-atom regime (TOP6 at
factor 8, margin 9.09, back to minC 184 while fully alive).
**Fixpoint question**: the step-controlled r280 recipe saturates
at a **one-degree plateau** (minC 185 from iterate 1, never 186;
axis decoherence cos +0.92/+1.00/+0.43 → negative; every full step
rejected from iterate 3 on; final `theta_eq` 1.43e-3 = the tube
rim) — **`RIDGE_NO_FIXPOINT`**, no stationary better world; and
the lift is **`LIFT_MAIN_SPECIFIC`**: from EPSTEIN the same
iteration terminates at step 0 (first-order **flat** wall,
theta_up 5.03e10) and the matched-dose ladder 7.75e-5..0.1 never
lifts. **Non-local functional contest** (sealed, fresh 143-point
conservation-gated corpus, 103-point test split): ridge projection
(best, sp +0.471), rank-2 lethality Gram (train/test split-sealed,
+0.137) and antiphase deviation pair correlation (−0.463) all stay
below the trivial size baseline |sp| 0.881 —
**`NONLOCAL_BLIND`**, the working set remains implicitly
characterized. **SMOOTH anatomy**:
**`SMOOTH_COLLECTIVE_2ND_ORDER`** — the killer axis is delocalized
(PR 112 of dim 368) and its margin curvature is Richardson-stable
−23.3 vs −0.98 for a same-length random direction (ratio 23.7 ≥
10): a genuine **quadratic wall valley**, not an r259-style
higher-order resummation gap. NO L\* claim. NO RH CLAIM.
r292 measured the **curvature two-form** of the working set
(`curvature_form_probe.py`, 36/36, SPEC_SHA `050821ff`,
`PRIME.PORT.LSTAR.CURVATURE_FORM.01` — experiments-side, no status
move; amendments a1–a4 disclosed: Hessian step ladder halved at the
measured margin-valid scale, one-sided estimator for the
side-selected budget kink, fractional-dose gate pad 1e-7,
L2-unit-consistent ridge display). **Hessian spectroscopy** (29
sealed theta_eq-normalized directions, 3-step diagonals + the full
406-pair polarization matrix, expansion-identity crosscheck 15/15):
**`HESSIAN_LOW_RANK(1)`** in the sealed L2 spectral metric — one
eigendirection carries 92.5 pct of the curvature mass, a pure
on-support **DENS combination**, *not* the SMOOTH axis (|cos| 0.07)
and *not* the ridge (**`RIDGE_CURV_FLAT`**, L2-rank 28/29: the lift
axis sits in the flattest curvature sector, the r291 expectation);
all 29 diagonals negative — a genuine multi-directional quadratic
valley. **EPSTEIN contrast**: the first-order flat wall is *also*
second-order structureless (ratio 5.4e-15) — MAIN's wall has
curvature structure, EPSTEIN's has none. **The threshold object
m\***: the measured log|h_184| quadratic term along the 18 r291
matched-dose sub-directions is **negative on all 18** (one-sided
cubic-triple solve, linear identity vs the analytic budget 0.3 pct)
— a second-order *assist*, not resistance: the corrected budgets
still separate perfectly but the bracket midpoint moves to 1.761,
*away* from the naive flip level —
**`THRESHOLD_NOT_EXPLAINED`** + **`RETRACTION_HIGHER_ORDER`**
(B2/B3 over-predict the TOP6 factor-8 retraction): the ~1.3×
factor and the retraction are **near-flip nonlinearities invisible
to low-order jets**; m\* stays an emergent threshold object.
**Two-form functional contest** (split-sealed, disjoint 94-point
test corpus): F10 curvature energy sp **+0.884** vs the size
baseline 0.907 — **`CURVATURE_BLIND`**, the fourth honest negative
under the sealed rule, but the closest miss of the whole program
(r290 best 0.263, r291 best 0.471; AUC(dead) 0.097): the
working-set geometry is predominantly second-order visible, the
open edge is the theta_eq-vs-L2 metric reconciliation. NO L\*
claim. NO RH CLAIM.
r293 adjudicated that open edge — the **metric reconciliation**
(`metric_reconciliation_probe.py`, 43/43, SPEC_SHA `33c44cc6`,
`PRIME.PORT.LSTAR.METRIC_RECONCILIATION.01` — experiments-side, no
status move; amendment a1 disclosed: the Leg-C death watch redrawn
from the raw h_185 sign to the real criterion minC < 184, a
diagnostic display fix). **Leg A sealed three metrics before any
functional evaluation** (M1 theta_eq, M2 L2 on the signed density,
M3 the curvature metric \|delta\|² = x|H_tr|x with the
spectral-absolute-value rule; distortion factors max/min 11.0 /
59.5 / 123.5, largest-deviation sector DENS = the r292
top-eigenaxis sector). **The hammer landed**:
**`METRIC_RECONCILED(F10 in M2)`** — evaluated against the size
baseline *of its own metric*, the split-sealed curvature energy
F10 beats a baseline for the first time in four rounds (sp
**+0.884** vs sp(F0_M2) −0.860) *and* holds
**`FUNCTIONAL_BEYOND_BASELINE`** (partial spearman sp(F10, s |
F0_M2) = **+0.423** on the 94-point test split, sign-stable +0.826
on the train-side replica) — the first predictive closed
functional of the working set; **promotion candidate flagged** for
the next consolidation wave (nothing promoted).
**`MIX_IS_CAUSE`**: the r292 mixed margin −0.023 vs the reconciled
home margin +0.024 — the metric mix *was* the cause of the r292
near-miss. **m\* as a singularity object**: all 8 selected flips
are **simple zeros** of h_184 (alpha = 1.000 ± 0.003 both sides;
every flip lands at minC 185 with h_185 < 0) but
**`MSTAR_NO_LAW`**: the per-direction thresholds m\*_dir = b·f\*
range 1.13–1.39 — no fixed safety distance to the singularity in
budget, theta_eq, L2 or curvature units (spreads 3.0/3.0/3.8/10.2
vs bar 1.25): the r291 "one scalar m\*" bracket was a fixed-dose
artifact, the ~1.3 factor is typical, not universal. The TOP6
factor-8 retraction **is a second simple h_184 zero** at f_ret =
7.107 — on the side the monotone budget prognosis is structurally
blind to. **Baseline anatomy**: `F0_DIRECTIONAL` (median
within-band |sp| 0.370 > 0.3, dead-only −0.890 / alive-only
−0.005) — the baseline is not a pure radius artifact, the
r290–r292 bars stand as drawn. NO L\* claim. NO RH CLAIM.
r294 stress-tested exactly that promotion candidate **before** any
consolidation — the **F10 stability round**
(`f10_stability_probe.py`, 42/42, SPEC_SHA `88c6fd1e`,
`PRIME.PORT.LSTAR.F10_STABILITY.01` — experiments-side, no status
move). **Leg A, the sealed promotion bar** (fixed before any corpus
was built): five fresh, seed-disjoint 147-point corpora (same
conservation discipline and r293 test-family mixture; tag
disjointness gated pairwise and against the r292 training tags)
against the **unchanged, hash-sealed r293 `H_tr`** (re-training
mutant CAUGHT by the SHA gate). The **|sp| win replicates on every
corpus** (5/5: F10 +0.675..+0.787 vs F0_M2 −0.660..−0.714, margins
+0.003..+0.115) — F10 is *not* a split/corpus artifact as a
predictor — **but the partial-correlation channel does not
replicate at its r293 magnitude** (partials +0.248..+0.555, median
0.299; only 2/5 clear the sealed +0.3 bar, two miss by ≤ 0.003):
sealed verdict **`F10_FRAGILE`** (win 5/5, part 2/5, full 2/5) —
**promotion precondition NOT met**, recommendation NO for wave 8;
the r293 partial +0.423 was the *top* of the fresh distribution,
not the center. **Leg B robustness**: `TRAIN_ROBUST` (leave-3-out
jackknife sigma 0.0101 ≤ 0.012) + **`RANK2_CARRIES`** (the top DENS
eigenaxis alone reaches +0.855, two whitened eigendirections beat
the baseline; top-axis DENS share 0.989) + `STEP_STABLE` (half FD
ladder sp 0.9995; the double ladder MARGIN_INVALID — the r292-a1
NaN boundary reproduced and excluded by the sealed rule). **Leg C
window transport** (w7/w11, complete window-own chains: walls
59/63, extraction dose caps 0.157/0.068 after the measured w11
full-ridge collapse, 67-point window corpora): **knife-edge** —
w11 beats its own L2 baseline by +0.002, w7 loses by 0.009 →
**`WINDOW_PARTIAL(w11)`**; the solid transport finding is
**mechanism constancy**: the top curvature eigenaxis is a DENS
combination on w7/w9/w11 alike (shares 0.795/0.989/0.834). **Leg
D**: **`L2_NOT_DENS`** — the DENS-neutralized baseline (scales
2.2..75.6) is *weaker* than plain L2 (−0.828 vs −0.860) and the
partial against it rises to +0.586: the F10 information is not the
DENS-sector length distortion; *why* L2 is the right coordinate
stays open. NO promotion. NO L\* claim. NO RH CLAIM.
r295 executed the two r294 fronts — the **F10 sp-hardening round**
(`f10_sp_hardening_probe.py`, 44/44, SPEC_SHA `4d7d8095`,
`PRIME.PORT.LSTAR.F10_SP_HARDENING.01` — experiments-side, no
status move; no amendments after the freeze). **Leg A, the sealed
three-clause hardening bar** (fixed before any corpus was built,
untouchable): **twenty** fresh seed-disjoint 147-point corpora
(seeds 300000+1000k; the full 192-seed forbidden set of
r292/r293/r294 enumerated and gated) against the unchanged,
hash-gated `H_tr` (published seal `3447ed198a56` re-verified). The
result is an **honest negative**: F10 wins the |sp| contest only
on **14/20** corpora (margins −0.079..+0.125, median +0.028, six
losses) → sealed verdict **`F10_SP_MAJORITY`** — the HARDENED bar
(≥ 18/20 AND margin median ≥ +0.02 AND no loss beyond 0.02) fails
on two clauses: **the r294 5/5 was itself top-of-distribution**,
exactly the way the r293 partial was; the partial-free ranking
statement is a *documented regularity* (19/25 combined census),
not a theorem candidate — **promotion recommendation NO for wave
8**, the candidate statement (Leg C) VOID by the sealed rule.
PARTIAL20 median +0.279, IQR [+0.182, +0.401] (the r293 +0.423
confirmed top-of-distribution; **`PARTIAL_STD`** — the partial at
the fixed 147-point mix — sealed as the standardized statistic of
future rounds). **Leg B partial anatomy** (pooled 2921 points): no
direction family reaches the STRONG 0.4 bar (PATH +0.156 / WORLD
+0.245 / FRAC +0.067 NULL / DENS +0.104) — the beyond-distance
information is diffuse, strongest on structured deviations toward
dead worlds, near-null on random FRAC rays; the
r293-composition-matched subsample (the PATH-heavy r293 mix) lifts
the median partial to +0.346 — the sealed gain clause passes
(+0.067 ≥ +0.05) but the level clause fails by 0.004 →
**`R293_LUCK`**: composition explains *part* of the r293/r294
discrepancy, the rest was n=94 sampling noise. **Leg D**:
`L2_VIA_CONSERVATION` formally (the eta_0 projection leaves the
contest exactly invariant) but near-tautological (projected-out
share median 2.9e-30) — *why* L2 stays open in substance.
Must-fails m1 hash / m2 seed collision / m3 bar sharpness (every
clause has teeth, both directions) / m4 conservation all CAUGHT.
NO promotion. NO L\* claim. NO RH CLAIM.
**Wave 6 (2026-08-25)** froze the L\* arc (rounds r282–r285 plus the
standalone problem document) as
**`v963_lstar_reduction_dictionary.py`** (ledger
`PRIME.LSTAR.REDUCTION_DICTIONARY.01` [E]; the four probes embedded
byte-exact in the sealed `--smoke` stage, plus a module-own exact
section — Hankel determinants, frame congruence minors, full
Cauchy–Binet gauge exhaustion, dual chains in pure Fractions): the
r283 A2 chain as exact gates ⇒ **L\* is the canonical reduction of
the open center** (stage 8/11 of the chain above), the r282
four-language elimination as named negative gates
(`CONTEST_ALL_DEAD`), the r285 decomposition bookkeeping exact, and
the r284/r285 anatomy + the honest DCXX margin-decay finding as typed
measurement pins. The open center itself is re-registered in
canonical form as **`PRIME.LSTAR.SUBORDINATION.01` [O]** (the
predecessor `PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01` and
`PRIME.PORT.REPRESENTATION.CONTEST.01` are consumed). In Lean the
canonical form is stated (`lstar_subordination`, the wave-6 `sorry`)
and the direction L\* ⇒ free-window positivity is **proved**
(`lstar_implies_free_window` via the quadratic-form dictionary
`hankel_quadform`; build green, 9 intentional `sorry`s). The r286
margin-scaling round and the r287 L2 census (above) were sealed
experiments-side at that cut and are consumed in wave 7 (below).
NO RH CLAIM.
**Wave 7 (2026-08-25)** froze the coherence arc (rounds r286–r289) as
**`v964_lstar_coherence_census.py`** (ledger
`PRIME.LSTAR.COHERENCE_CENSUS.01` [E]; the four probes embedded
byte-exact in the sealed `--smoke` stage — SPEC SHAs
`0a44ac4e`/`761d88fa`/`da46f7ee`/`91cdc2b1` — plus a module-own exact
section: the Fejér window-sum identity, the van der Corput inequality
with its Cauchy–Schwarz proof route, the Abel/Erdős–Turán bound, the
mutant must-fails, the 2-power resonance count C(8,2) = 28, in pure
Fractions): the DCXX margin warning **resolved harmless** (r286: 15
new anchors N_w 942–1218 all mp-sign-safe positive, O(1) offset
survives, flattening power law, no counterexample), the generic L2
half **classical by a named theorem** (r287: exact vdC at
H = ceil(sqrt(m)), delta' +0.309 > 0.21 world-blind, 6/7 + 38/42 —
new open contract **`PRIME.PORT.L2.VDC_LEMMA.01` [O]**: the chain
origin of the P-variance scaling), the destructive coherence with a
**named carrier class** (r288: antiphase next-nearest ARCH–ARCH
pairs, z_v = −3.149, total control reversal, finest alignments below
phase resolution), and the diophantine route **excluded** (r289
`METRIC_ONLY`: the rational twin keeps the full signature identical;
metric coherence threshold 1e-3..3e-3 of the local gap; Baker ~7900x
too weak and unnecessary) — the open front is the **profile
functional** (`PRIME.LSTAR.SUBORDINATION.01` [O] carried at the
wave-7 state; r290 above, in flight at this cut, probes exactly this
question).  In Lean no new statement is needed — the hole stays
`lstar_subordination` (docstring refreshed to the wave-7 state).
NO RH CLAIM.

**Wave 8 (2026-08-26)** froze the curvature arc (rounds r290–r295) as
**`v965_lstar_curvature_arc.py`** (ledger
`PRIME.LSTAR.CURVATURE_ARC.01` [E]; the six probes embedded byte-exact
in the sealed `--smoke` stage — SPEC SHAs
`f953dd71`/`bb512c17`/`050821ff`/`33c44cc6`/`88c6fd1e`/`4d7d8095` —
plus a module-own exact section S0: the r292 polarization identity
H(u,v) = [d2(u+v) − d2(u−v)]/4 with its wrong-prefactor must-fail, the
r291 budget telescope (exact partition additivity) with the
dropped-atom must-fail, the r293 alpha = 1 simple-zero doubling law
with the double-zero mutant, and the sealed r294/r295 decision bars as
exact Fractions logic with tipping must-fails).  The wave freezes the
**measured geometry of the working set** — a soft-shouldered
anisotropic tube (killfrac 0.38/0.62/1.00 at 5e-4/1e-3/2e-3
gap-equivalent; world axes kill 5–50× earlier; the SMOOTH axis a
privileged yet gradient-orthogonal killer), a real one-degree ridge
(plateau minC 185; the lift a first-order budget phenomenon with the
threshold in (1.280, 1.291]; MAIN-specific), a rank-1 DENS curvature
valley (92.5 pct, lam_top −0.418; not SMOOTH, not the ridge), and
simple h_184 flip zeros (alpha = 1; the TOP6 retraction a second
simple zero at f_ret 7.107) — **together with the honest negatives of
the closed-functional search, verbatim**: `ALL_FUNCTIONALS_BLIND`
over five sealed class families, r294 `F10_FRAGILE` (win 5/5, part
2/5) and r295 `F10_SP_MAJORITY` (14/20) — **F10 is NOT promoted**,
the sealed bars rejected it twice and the rejections are the frozen
content; `MSTAR_NO_LAW`; `R293_LUCK` (the r293 partial and the r294
5/5 were both top-of-distribution).  The characterization question is
re-registered as **`PRIME.LSTAR.CLOSED_FUNCTIONAL.01` [O]** (open
fronts: loss-corpus forensics K05/K07/K19, the rank-2 DENS core as a
sharper candidate, why L2 is substantially the right coordinate);
`PRIME.LSTAR.SUBORDINATION.01` [O] carried at the wave-8 state (no
round in flight at this cut).  In Lean no new statement is needed —
the wave carries no new formal target form; the hole stays
`lstar_subordination`.  NO RH CLAIM.

r296 ran the reviewer's **hard identity fork** on the r292 axis — the
**DENS-identity round** (`dens_identity_probe.py`, 39/39, SPEC_SHA
`ffb413c8`; `PRIME.PORT.LSTAR.DENS_IDENTITY.01` — experiments-side;
consumed in wave 9, `v966`): is the 92.5-pct DENS top
curvature eigendirection *mathematically identifiable* and *coupled to
the L\* extremizer*?  One hash-sealed candidate library, frozen before
any cosine: **T1 = grad lambda_max(E_184)** via Hellmann–Feynman from
the extremal eigenvector (FD ward 3.8e-7; lam2/lam3 gradients as
excluded controls), the von-Mangoldt family, local-metric family,
kernel diagonals, the 4-dim moment-gradient subspace, 8 nulls + decoy;
primary metric = the in-span cosine on the 29-direction span (e_top
exists only there), honesty columns raw/lag/capture.  **Sealed verdict:
`DENS_WORLD_BLIND`** (base `DENS_PARTIAL(T5_MOMENTS, 0.825)` downgraded
by the world-contrast rule: the moment-subspace share *holds* at
EPST/SCR 0.57/0.60 ≥ 0.40 — construction-adjacent low-moment
smoothness, with the disclosed tension that the absolute 0.40 collapse
bar is conservative for subspace members).  **The coupling number of
the round: cos(e_top, grad lambda_max) = +0.394** — below the sealed
0.40 bar (noise max 0.331), and the lam3 control couples *harder*
(−0.574): what coupling exists is a near-crossing eigenvalue-*band*
property, not top-specific.  Every arithmetic candidate stays ≤ 0.38;
raw-grid overlaps ≤ 0.08 at captures ≤ 0.36 — the axis is dominated by
structure no on-support arithmetic profile in the library represents.
Window transport w7/w9/w11 measured (window DENS shares 0.795/0.834 ==
r294); amendments a1–a4 disclosed pre-freeze.  NO L\* claim, NO RH
CLAIM.

**Routing note (r296 → r297, pre-adjudicated reviewer fork):** with
`DENS_WORLD_BLIND` the DENS-identity lane is **closed** (coupling
number +0.394 below the sealed bar, no arithmetic candidate above
0.38) — resources move to the **L2 front**, where the exact vdC
theorem (v964-S0) already waits with a 0.24 exponent pad (need
> 0.21, truth ~0.45): **L2 is the active front**.

r297 opened the L2 lane with the **vdC chain-provenance round**
(`vdc_chain_provenance_probe.py`, 27/27, SPEC_SHA `e42a76eb`;
`PRIME.PORT.L2.VDC_CHAIN_PROVENANCE.01` — experiments-side; consumed
in wave 9, `v966`): can the vdC *input* (the P-variance /
autocorrelation scaling) be derived source-purely from the chain?
**Leg A freezes the target inequality** — the weakest sufficient input
bound, all constants live: `sigma := slope(S_F/M²) ≤ sigma* =
2·(slope(eps_c2/M) − 0.21) − slope(pref) = −0.516`; measured sigma
−0.714 — the truth clears the target with 0.198 sigma margin (0.099 in
delta'): *what is missing is not room, it is provenance* (pad
arithmetic exact; the pad-dropped mutant composes to delta' = 0).
Three source-pure routes, every chain step exact on 47 worlds
(world-blind by the same algebra): **B1 pair-identity** delta' −0.112
(break: the MAX pair gap falls at slope −0.535 where ≤ −1.178 would
suffice — the Jacobi near-balance is a *mean* statement); **B2
node-density** delta' −0.097 (the run-boundary *positions* are
near-equidistributed with falling discrepancy D_rank med 0.024, slope
−0.42 — provable terrain — but the *mass* imbalance grows, slope
+0.244); **B3 Fejér/Parseval** delta' −0.097, with **the surprise of
the round: the chain is exactly orthogonal w.r.t. the WINDOW measure**
(cross/diag devs 0.000; BORDER and WDIFF break) — the Parseval sum
rule (proved symbolically in Fractions) *attaches* there; what remains
is the measure transfer (the vdC input lives on the border union) and
the signed-to-absolute gap (med 4.3, growing).  **Sealed verdict:
`CHAIN_PROVENANCE_PARTIAL(B3_PARSEVAL, slope miss 0.307)`** — the
common obstruction named: every universal majorization of A(0) through
magnitudes pays a growing max/mean imbalance factor; the *signed*
structure carrying sigma = −0.71 is what magnitude chains cannot see.
kz15 structurally outside all three routes (r270 exact-finite stays
the permanent closure).  The two assets left for the lane: the exact
window-measure orthogonality (a bordered-form transfer statement is
the concrete named object) and the falling rank-coordinate
equidistribution.  NO L2-lemma claim, NO RH CLAIM.

r298 executed the named asset-1 attachment point with the
**window-border transfer round** (`window_border_transfer_probe.py`,
28/28, SPEC_SHA `05e831be`;
`PRIME.PORT.L2.WINDOW_BORDER_TRANSFER.01` — experiments-side;
consumed in wave 9, `v966`): does an exact, *sign-
preserving* transfer statement exist from the window measure (where
the chain is exactly orthogonal) to the border form (where the vdC
input lives)?  **It does, and it is exact:** with `Delta := border ⊖
window` and the frozen positional Fejér block kernel, the vdC input is
the quadratic form `S_F = B(beta,beta)` and splits per-rung exactly
(dev ≤ 8.8e-16 of scale, 47 worlds) as **`S_F = B(omega,omega) +
B(Delta, omega+beta)` = MAIN + T(Δ)** — nothing passes through
magnitudes (the `|Delta|` mutant breaks the identity by a factor ~1.7
of scale, LOUD: the r297 magnitude error certified as a must-fail);
the *linear* corollary is measured at float precision: the window
image of the drive functional **vanishes** — the drive is 100 pct
transfer at the linear level.  **Sealed verdict: `TRANSFER_DOMINANT`**
— the window main term is *empty* (med −3.94 dec, two decades below
S_F, slope −1.386 collapsing) and the omega-Delta cross term
negligible (med −1.4e-4), so **`S_F ≈ B(PDelta, PDelta)`: the vdC
input IS the Fejér energy of the difference measure itself**; sigma =
−0.714 is the decay exponent of this one named source-pure quantity;
the in-T sign cancellation (med 1.69) grows at +0.207 — the r297
imbalance factor localized *inside* T.  Leg-D bycatch: the imbalance
growth is broad-based (no outlier carrier), and its carriers coincide
with the T carriers (sp med +0.69) — **the two r297 gap halves are one
structure**.  Candidate theorem VOID (not subdominant); the precisely
narrowed wave-9 gap object: *prove the Fejér-energy decay of Delta*.
World-blind (EPST/SCR same class); anchors bit-near; amendments a1/a2
disclosed.  NO L2-lemma claim, NO RH CLAIM.

r299 executed that gap object with the **Fejér decay round**
(`fejer_decay_probe.py`, 32/32, SPEC_SHA `f432e944`;
`PRIME.PORT.L2.FEJER_DECAY.01` — experiments-side; consumed in wave
9, `v966`): can the decay of `B(PDelta,PDelta)` (sigma ≤
sigma* = −0.516) be derived source-purely from position
equidistribution plus a controllable signed-mass statement?  The
module-own **exact spectral representation** `B = (1/L) sum_k
F_H(theta_k) |Dhat(k)|²` (recomposition/Parseval/majorization wards ≤
7.1e-16 on 47 worlds) answers the anatomy question: **LOWPASS** — the
Δ energy sits inside the Fejér main lobe (band shares 0.93/0.04/0.02,
q50 = 0.19 lobes): sigma is a low-frequency phenomenon.  The
structural surprise: the border and window unions share their **full
support on 42/42 rungs** — `Delta_fresh ≡ 0`, **Δ is a pure c-value
difference measure** on one shared node set, and the relative
c-difference does *not* fall (cconv med 0.86, slope +0.045): the decay
is aggregate cancellation of a non-converging difference profile.
**Sealed verdict: `DECAY_SPLIT`** — the Erdős–Turán/Abel composition
fails loudly (composed slope +1.948 vs sigma* −0.516; the
position/kernel factor grows +1.504: the r297 magnitude wall recurs at
the frequency level; `MASS_TARGET` missed by 2.46), but the **pair
split fires**: the diagonal `sum PDelta_j²` already falls fast enough
(slope −0.571 ≤ −0.516, margin 0.055) and the pair ratio B/D (med
1.29) *falls* (−0.168) — the frozen rest pair is **`DIAG_TARGET`** (a
magnitude-density bound on one positive quantity) **+ ratio flatness**
(the off-diagonal reinforcement does not grow), with `CVALUE_TARGET`
frozen on the B3 side; the conditional candidate theorem (Leg-B bound
+ rest hypotheses ⇒ sigma ≤ sigma* ⇒ r297 target ⇒ v964-S0 vdC ⇒
delta' > 0.21 generic half) is printed, wave-9 candidate NOT promoted.
Bycatch: the in-T cancellation gap is entirely low-band and *not*
carried by the mass blocks (sp −0.01 vs the +0.69 energy coupling);
and the O-sign class separates MAIN (pair field *reinforces*, O < 0 on
13/42 only) from both dead controls (O < 0) — the first
world-separating sign class of the L2 lane, disclosed as
`WORLD_SENSITIVE`.  Anchors bit-near; Fractions ET section exact with
the prefactor-mutant family CAUGHT (v964-S0 T4 anchor); amendments
a1/a2 disclosed.  NO L2-lemma claim, NO RH CLAIM.

r300 executed the frozen rest pair with the **diag-target round**
(`diag_target_probe.py`, 31/31, SPEC_SHA `55218b5d`;
`PRIME.PORT.L2.DIAG_TARGET.01` — experiments-side; consumed in wave
9, `v966`): can the diagonal decay `sl_D ≤ sigma* = −0.516`
(margin 0.055, thin) be derived source-purely — and the ratio flatness
with it?  **The anatomy relocates the target:** in the exact
participation coordinates of the one positive vector `|PDelta|`
(`n_eff = L1²/D`, `fill = D/(mx·L1)`), the diagonal decay decomposes
*exactly* (dev 6.7e-16) as **`sl_D = 2·sl_L1 − sl_neff = 2·(+0.196) −
(+0.963)`** — the effective-carrier count grows at ~N (sp(N, n_eff)
+0.96) against a mildly growing L1 mass: "many small instead of few
large" is now a measured identity.  Both magnitude derivation routes
fail exactly the way r297 predicted: the B1 chain-norm Cauchy–Schwarz
on the `|dw|` measure composes to −0.384 (misses σ* by 0.133) *and*
the `|dw|` identity census BREAKS (cross med 0.932) — the proven
window sum rule does **not** attach to the difference measure; the B2
`max × L1` factorization composes to −0.346 (misses by 0.170) even
though the max itself is fully atom-controlled (a single c-value
distance, `mx/maxatom` med 1.07): the irreducible loss is the fill
decay −0.225, invisible to any max × mass bound.  **Sealed verdicts:
`DIAG_SPLIT(B3/NEFF_TARGET)` + `RATIO_BOUNDED_STRUCTURAL`** — the
ratio half of the r299 rest pair is *settled at the structural level*:
the exact kernel envelope `F_H(θ) ≤ min(H, 1/(H sin²(θ/2)))` majorizes
`B/D ≤ R_env` (med 1.61) and R_env itself falls (−0.122); the r299
lobe-width heuristic is refuted (sp(B/D, q50) = −0.47).  The refined
freeze is smaller than r299's: **one inequality remains — `NEFF_TARGET`:
prove `slope(n_eff) ≥ 2·sl_L1 − sigma* = +0.908`** (measured +0.963,
margin 0.055; disclosed as an exact reparametrization of DIAG_TARGET),
with the falling boundary discrepancy (D_rank(Δ) slope −0.117,
sp(D_rank, n_eff) = −0.81) as the named bridge to provable
equidistribution terrain.  Bycatch: D itself is BROADBAND
(0.27/0.26/0.46) — the low-pass character of sigma is pure Fejér
weighting; and the FILL class separates MAIN (FILL_LOW) from both dead
controls (FILL_HIGH) — the second world-separating class of the lane,
disclosed as `WORLD_SENSITIVE`.  Anchors bit-near (r297 + r298 + full
r299 set); amendment a1 (scale floor on the degenerate SMOOTH Δ ≡ 0)
disclosed.  NO L2-lemma claim, NO RH CLAIM.

**Wave 9 (2026-08-26)** froze the DENS fork and the L2 reduction chain
(rounds r296–r300) as **`v966_l2_reduction_chain.py`** (ledger
`PRIME.L2.REDUCTION_CHAIN.01` [E]; the five probes embedded byte-exact
in the sealed `--smoke` stage — SPEC SHAs
`ffb413c8`/`e42a76eb`/`05e831be`/`f432e944`/`55218b5d` — plus a
module-own exact section S0: the r297 σ\*-composition arithmetic
(δ′(σ\*(pad)) == pad exactly, the pad-dropped mutant composes to 0 —
the r297-m2 sharpness as an identity), the r298 decomposition identity
`S_F = B(omega,omega) + B(Delta,omega+beta)` on the exact positional
Fejér block form (toy 3 = 1 + 2; the |Δ| and wrong-weight mutants
break by exactly 4 and 2/3), the r300 participation identity
`D·n_eff == L1²` with ratio multiplicativity and the machine-checked
DIAG↔NEFF equivalence (margin 0.055 exact in both coordinates; the
signed-sum mutant breaks by 8/3), the r300 kernel envelope
`F_H(s) ≤ min(H, 1/(H·s))` exact-rational with equality witnesses on
both branches, and the five sealed verdict bars as exact decision
logic with tipping mutants).  The wave freezes **two things**: the
DENS-identity lane is **closed honestly** (r296 `DENS_WORLD_BLIND`:
coupling number +0.394 below the sealed 0.40 bar, λ3 couples harder
−0.574, every arithmetic candidate ≤ 0.38, the moment subspace
construction-adjacent — the lane routed to L2 per the pre-adjudicated
reviewer fork), and the **L2 chain stands reduced to ONE inequality**:
`[NEFF_TARGET, open] ⟹ sl_D ≤ σ* (exact participation algebra) ⟹
with RATIO_BOUNDED_STRUCTURAL sigma ≤ σ* ⟹ the r297 target
(margin 0.198) ⟹ the v964-S0 vdC theorem ⟹ delta' > 0.21 on the
generic half` (exceptions: 6 via r287 F2, kz15 exact-finite via
r270).  The magnitude no-go catalog is frozen verbatim (r297 B1/B2,
the r299 ET/Abel wall +1.948, the r300 chain-norm and max×L1 closures
with the invisible fill decay).  The one remaining inequality is
registered as **`PRIME.L2.NEFF_TARGET.01` [O]** (slope(n_eff) ≥
+0.908, measured +0.963, margin 0.055; the D_rank bridge sp −0.81 is
correlational, not causal; **r301 in flight, not consumed**).  In
Lean **no new statement** is added: NEFF_TARGET is a measured
ladder-slope aggregate (a halves log-slope estimator over 42 rungs
with a threshold derived from measured slopes), not an exact finite
identity and not a matrix theorem, and a universally quantified
ladder form would be refutable exactly like the pre-r273 universal
edge forms (the machine-checked guard pattern of
`RH/Counterexamples.lean`) — the hole stays `lstar_subordination`.
NO RH CLAIM.

r301 executed the wave-9 open inequality with the **neff-target
round** (`neff_target_probe.py`, 32/32, SPEC_SHA `6f8cc404`;
`PRIME.PORT.L2.NEFF_TARGET.01` — experiments-side; consumed by `v967`, wave 10): *why* does `n_eff = L1²/D` grow ~N, and can
`slope(n_eff) ≥ +0.908` (measured +0.963, margin 0.055) be derived
source-purely?  **The anatomy:** the whole Rényi order family
`N_2/N_3/N_4/N_inf` (med 37.41/27.88/24.04/15.47) grows at nearly one
exponent (+0.963/+0.926/+0.894/+0.738, tail slope only −0.069) —
**echt anti-concentration**, not a broadening tail; the positional
footprint is flat.  **The stability:** the thin margin is
jackknife-STABLE (min +0.936 ≥ +0.908, 0/42 leave-one-out ladders
below NEED — no `MARGIN_FRAGILE`), while the half-ladder census shows
the deep half at +0.802: the honest anti-extrapolation flag stands.
**The structural finding (B1):** `n_eff = n_act/(1 + CV²)` EXACTLY
(module-own Fractions re-proof, ward ≤ 6.8e-16 on 47 worlds) with the
PERFECT count link **`n_act == m` on 42/42** — the effective-carrier
count IS the constructive level-2 block count, growing at +1.002; the
entire NEFF_TARGET compresses into **`UNIF_TARGET`: slope(1 + CV²) ≤
sl_nact − NEED = +0.094** (measured +0.039, margin 0.055) — a growth
statement became a *boundedness* statement about the block profile of
`|PDelta|`; `NEFF_DERIVED` missed only the sealed CV-flat clause
(+0.039 > 0).  **Closed honestly (B2):** the exact
weighted-discrepancy interval chain (`|w_j/W − λ_j| ≤ 2·δ_w`, a
star-discrepancy theorem, wards exact on 47 worlds) fails by 0.834 —
the `|dc|`-WEIGHTED discrepancy (med 0.167, slope −0.017) is 10× the
raw D_rank and near-flat: the r300 bridge correlation lived on the
*raw* positions, the max-based equidistribution shortcut is closed.
**B3:** the difference profile decorrelates at lag ONE (l_loc med
1.0) and the atom-level participation grows at +0.942 (sp +0.96 to
the block level), but the LOCAL sum-rule census breaks 24/24 — the
`|dw|` non-orthogonality is scale-free.  Sealed verdict
`NEFF_SPLIT(B1(UNIF_TARGET) | B3(MIX_TARGET))` + `REST_FROZEN`;
bycatch: the new UNIF class does *not* separate worlds (MAIN CV² 1.03
bracketed by EPST 0.72 / SCR 2.76) — unlike the O-sign and FILL
classes.  Must-fails: the Fractions identity mutants (9 and 7/24
exact), the halved discrepancy prefactor (0.3 exact), the transposed
aggregation matrix (37/55 exact + column-sum flag), overlapping
sub-ladders CAUGHT, the synthetic one-block collapse to `n_eff == 1`.
NO L2-lemma claim, NO RH CLAIM.

r302 executed the r301 frozen rest with the **unif-target round**
(`unif_target_probe.py`, 30/30, SPEC_SHA `36df9424`;
`PRIME.PORT.L2.UNIF_TARGET.01` — experiments-side; consumed by `v967`, wave 10): *why* is the block profile of `|PDelta|` quasi-uniform
(slope(1 + CV²) ≤ +0.094, measured +0.039), and can it be derived
source-purely?  **The anatomy (A1):** the mild CV² rise is
**structureless** — no sealed class scheme (sign / position band /
atom-count pattern) fires the carrier rule (between-shares
0.012/0.216/0.111).  **The stationarity (A2, mechanism iii):** the
per-rung normalized block values have ONE stable distribution along
the ladder — pooled KS(G1,G3) 0.043, KS(G2,G3) 0.021, far under the
sealed 0.125: `PROFILE_STATIONARY`.  CV² boundedness is the second
moment of a stationary normalized profile, and the r299 cconv
negative is explained: convergence in *distribution*, not pointwise.
**The depth honesty (A3):** the r301 half-ladder flag is resolved by
exact per-half additivity — the deep-half flattening of n_eff
(+0.982 → +0.802) is carried ENTIRELY by the CV² head (+0.228), not
the count (+1.030); the sealed finite-size model fires
`TRANSIENT_1_OVER_N` (m2 group medians 2.07/2.02/2.00 fall on an
exact 1/N law onto A = 1.973, held-out dev 0.002): `DEPTH_HALF_MISS`
stands as an honest flag, `DEPTH_CAVEAT` does **not** fire; the
sl_cv2p jackknife is 0/42 above UNIF_NEED.  **The structural finding
(B1):** the exact coherence identity `1 + CV² =
n_act·χ/(surv²·n_eff_atom)` with `χ = D/Q` the in-block coherence
factor (module-own Fractions re-proof, wards ≤ 6.0e-16 on 47 worlds,
per-block Cauchy–Schwarz cap χ ≤ kmax with slack 0.0) — χ med 0.63
is **destructive and non-growing** (−0.060; the r301 lag-1
anti-correlation ρ₁ = −0.22 is its atom-level mechanism), surv flat
(−0.020), composed slope +0.039 == sl_cv2p exactly (5.4e-16).
**Closed honestly:** B2 local-pattern (PAT12 within-share 0.685 >
0.5 — the node pattern does not determine `|PDelta|`; k-profile KS
0.181 > 0.125) and the B3 damping clause (localized-perturbation
gain g/N med 1.079 vs the sealed 1.0 — the recursion responds *at*
the polynomial-degree rate, miss 0.079).  Sealed verdict
**`UNIF_DERIVED(B1 + A2)`** — the first DERIVED verdict of the lane,
with every hypothesis typed MEASURED; Leg C printed the full
r297→r302 candidate theorem (wave-10 candidate, NOT promoted).  The
one remaining measured growth statement is **`ATOM_TARGET`**:
slope(n_eff_atom) ≥ sl_nact + sl_χ − 2·sl_surv − UNIF_NEED = +0.888
(measured +0.942, margin 0.055 — the same thin margin relocated one
level down, onto an atom-level anti-concentration statement about
the c-difference profile itself).  Must-fails: wrong class weight
(3/4 exact), lag-0 double counting (5/7 exact), unnormalized-KS
mutant (re-anchored to the relative form per amendment a1, original
0.335 < 0.5 printed permanently; CAUGHT 8×), the two-point synthetic
(CV² = 729/196, LOUD on every route), scope mutants flagged.
World-blind by algebra on 47 worlds; UNIF non-separation reproduced
(MAIN 1.03 bracketed by EPST 0.72 / SCR 2.76).  NO L2-lemma claim,
NO RH CLAIM.

r303 ran the **atom-target round with hard regress audit**
(`atom_target_probe.py`, 26/26, SPEC_SHA `375e9f2b`;
`PRIME.PORT.L2.ATOM_TARGET.01` — experiments-side; consumed by `v967`, wave 10), adjudicating the warning signal that r300/r301/r302 froze
three targets with the *identical* margin 0.055.  **The regress
audit (Leg A): `REGRESS_CONFIRMED`** — the four target margins
m_D/m_NEFF/m_UNIF/m_ATOM all equal **+0.0547** with invariance devs
≤ 9e-16 (module-own `margin_chain`, re-proved exact in Fractions:
all four margins 3/50 on the rational slope set; the frozen
halves-slope estimator is exactly log-additive over the
r300/r301/r302 product identities): the cascade is an exact
**dictionary** around ONE measured core `S = σ* − sl_D = +0.0547`
(the r299 DIAG margin), not three reductions — further "reduction"
rounds may **not** be counted as progress on the inequality; the
r297 σ level is *not* the core (σ* − σ = +0.1976 = S + the ratio
surplus +0.1429 exactly; only the surplus's boundedness is
structural), and the charter's ½-conversion conjecture is
**refuted** (+0.0988 ≠ +0.0547 — the factor 2 lives only in
`NEED = 2·sl_L1 − σ*` and cancels in every margin difference).
**The mixing mechanism test (Leg B, the first non-tautological
test of the lane):** sealed synthetic rearrangements of the dc
profile per rung (bitwise-exact marginal, ρ₁ steered to matched /
zero / flipped targets by seeded greedy swaps; 1008 builds,
convergence 1008/1008): sealed verdict **`MIXING_INSUFFICIENT`**
with a *monotone* mechanism ladder — χ real 0.630 → matched 0.764 →
zero 1.029 → flipped 1.342, end margin +0.055 → +0.057 → +0.032 →
**−0.044**: flipping the mixing sign *kills* the target inequality
and matching ρ₁ reproduces the slopes and the end margin, but not
the destructive-coherence level (χ miss 0.134 > 0.05) — the
within-block structure beyond lag 1 carries the rest.  Bycatch
theorem-grade fact: `n_eff_atom = L1a²/Q` is a pure **marginal**
functional (invariance 1.0e-15 on all 1008 builds) — ATOM_TARGET's
growth lives in the value distribution alone; stationarity (r302
A2) and mixing are complementary, not redundant.  The ρ-sign census
is honest: S1 < 0 on **41/42** only (one rung positive — the
adjacent-π-orthogonality connection cannot be a raw per-rung
theorem; Fractions-exact negative certificates on the two smallest
rungs).  Consequence map (ii): the reduction cascade r297→r302 is
**closed as a dictionary**; the honest next object is the joint
short-range law of the dc profile (ρ₁..ρ_k / within-block
coherence), not another coordinate change.  Must-fails: the
wrong-½-factor propagation breaks by exactly sl_L1 = 1/5
(Fractions), the unmatched-marginal family LOUD (5.9e-1), the seed
collision CAUGHT, the swapped-D/Q coherence mutant breaks by 48/35
exact, scope mutants flagged; NO amendment after freeze.  NO
L2-lemma claim, NO RH CLAIM.

r304 ran the **short-range-law round** (`shortrange_law_probe.py`,
37/37, SPEC_SHA `2cc5d23f`; `PRIME.PORT.L2.SHORTRANGE_LAW.01` —
experiments-side; consumed by `v967`, wave 10), executing the reviewer
contract verbatim: *is the anti-correlation genuinely short-range
and summable (control of 1 + 2Σρ_k), or can higher lags eat the
lag-1 advantage?*  **The law (Leg A): `LONGRANGE_STRUCTURE`** — the
centered lag profile ρ₁..₁₆ over all 42 rungs is a **stable
period-4 comb** (med −0.222/−0.140/+0.089/+0.130, then recurring
strong lags at every k = 4m (≈ +0.13..+0.16) and k = 4m+2
(≈ −0.14..−0.15) up to 16; halves-stable 3/3 in sign;
world-specific — EPST/SCR differ), *not* a decaying tail: the
sealed rule (|med ρ_j| ≤ 0.05 for all j > k₀ ≤ 8) finds **no k₀**.
The reviewer condition **splits**: the net covariance
NC(16) = 1 + 2Σ med ρ_k = **0.712 < 1 holds** (net-negative,
the sign half of the contract) while summability-with-small-tail
**fails** (SUM(16) = 1.563, no decay); the zero-sum tautology
(1 + 2Σ_all ρ_k ≡ 0 for mean-removed finite profiles) is disclosed
and gated live — the truncated NC is the content.  **The structural
counterpoint (exact):** the χ lag decomposition χ = D/Q =
1 + 2Σ_k T_k/Q over within-block position pairs (recomposition ward
4.7e-16 on every non-degenerate world) shows the *χ-relevant*
structure **is** short-range — the real shares die out by k ~ 4
(c₁ −0.345, c₂ −0.139, c₃ +0.068, c₄ +0.028, Σ(5..16) −0.026,
tail 0.000) and the r303 χ-level miss 0.134 is attributed to
k ≤ 3 (dominated by lag 2: +0.181): the long-range comb is
**invisible to χ**.  **The sufficiency test (Leg B):** lag-8
matching (252 builds, 252/252 converged at tol 0.02, marginal
bitwise) reproduces the destructive χ **level** (0.652 vs 0.630,
|d| 0.022 ≤ 0.05 — where r303's ρ₁-only family missed by 0.134)
but breaks the **slopes** (sl_cv2p/sl_D miss by 0.028/0.027 >
0.02): the exact *complement* of r303 — the mechanism is
**two-scale** (level from the short lags, slopes from the
rung-wise lag-1 trend); no lag-matching family reproduces both
within the sealed bands.  The graduated reviewer ladder (absolute
ρ₁ targets +0.2/0.0/−0.1/−0.2/−0.3, 840/840 converged): χ
1.361/1.019/0.889/0.765/0.632 **monotone** in ρ₁, but the end
margin (+0.036/+0.074/+0.019/+0.045/+0.059) is **not** — honest
negative: absolute-level targets do not kill the inequality; the
r303 kill (−0.044) came from per-rung *flipped* targets — the
margin responds to the rung-wise trend of ρ₁, not its level.  Sign
pattern: med signs of S₁..₄ = −/−/+/+ with Fractions-exact
certificates on both smallest rungs (kz18, kz23: 4/4).  Leg 0
anchors bit-near (margin chain +0.0547 ×4; the r303 three-family
ladder replicated with the same seeds: χ 0.764/1.029/1.342,
margins +0.057/+0.032/−0.044; RHO_SIGN 41/42).  Consequence map
(iii, the reviewer stop case): the lane's **global-profile mixing
route is closed** (documented stop) — L2 ⟺ anti-concentration of
an explicit block field with *long-range (period-4 comb)*
structure; what survives as honest structure: the exact
within-block short-range decomposition of χ, the two-scale
mechanism split, NC < 1 and the exact sign pattern.  Must-fails:
factor-1 net covariance (1/2 ≠ 0 exact) and factor-1 χ
decomposition (6/7 vs 5/7 exact), unmatched marginal LOUD
(5.9e-1), uncentered field (3/4 exact + real 0.028), the
ρ₁-only-family smuggle against the lag-k₀ ward (dev 0.332 > 0.02)
CAUGHT, scope mutants flagged; NO amendment after freeze (the
pre-record G32 print fix disclosed in the spec).  NO L2-lemma
claim, NO RH CLAIM.

**Wave 10 (2026-08-26)** froze the cascade closure and the documented
lane stop (rounds r301–r304) as **`v967_l2_cascade_closure.py`**
(ledger `PRIME.L2.CASCADE_CLOSURE.01` [E]; the four probes embedded
byte-exact in the sealed `--smoke` stage — SPEC SHAs
`6f8cc404`/`36df9424`/`375e9f2b`/`2cc5d23f` — plus a module-own exact
section S0: the r303 margin-invariance algebra (all four target
margins `m_D = m_NEFF = m_UNIF = m_ATOM = 3/50` EXACT on the rational
slope set; the halved-need mutant breaks by exactly `sl_L1 = 1/5`; the
record-decimal chain 0.055/0.908/0.094/0.888 exact; the σ
decomposition 0.198 = 0.055 + 0.143 exact; the ½-conjecture
refutation 0.099 ≠ 0.055), the r302 coherence identity
`(1 + CV²)·surv²·n_eff_atom == n_act·χ` on two rational toys (mutant
breaks 5/7 and 48/35 exact), the r304 χ-lag decomposition
`χ = 1 + 2Σ T_k/Q == D/Q` on both toys (5/7 and 5/19 exact; factor-1
mutant 1/7), the r304 zero-sum tautology as a gate (factor-1 and
uncentered mutants 1/2 and 3/4 exact; NC(1) = 0.556 exact, NC(16) =
0.712 < 1; the period-4 comb certificate with NO k₀), the −/−/+/+
sign-pattern certificate with the kz18/kz23 Fractions pins, the four
sealed verdict bars as exact decision logic with tipping mutants, and
the lane-stop composition gate).  **The wave freezes the rejections
and retypings as the content**: the cascade r297→r302 is RETYPED as
an exact reduction *dictionary* (coordinate finding around one
measured core `S = σ* − sl_D = +0.0547`, not six proof steps; the
hard reviewer rule binds — a round counts only with NEW information);
the first causal coordinate is real but insufficient (the ρ₁ flip
kills the inequality, the χ level needs the short lags: the mechanism
is TWO-SCALE); and the sealed reviewer stop case fired
(`LAW_LONGRANGE`): **the global-profile mixing route of the L2 lane
is documented CLOSED** — the honest stop state is *L2 generic ⟺
anti-concentration of an explicit block field with long-range
(period-4 comb) structure; return later with new tools*.  What stands
honestly: the exact identity dictionary (count, coherence, χ-lag),
the two-scale split, NC < 1, the −/−/+/+ sign pattern, the
marginal-functional invariance of `n_eff_atom` (1e-15 on all
2100 + 1008 builds).  `PRIME.L2.NEFF_TARGET.01` [O] is retyped to the
documented stop state; `PRIME.L2.REDUCTION_CHAIN.01` [E] keeps its
exact identities with the reading refined.  In Lean **no new
statement** is added: the stop carries no new exact target form (the
period-4 comb and the two-scale split are measured ladder aggregates,
not exact finite identities, and a universally quantified ladder form
would be refutable — the r273 guard pattern of
`RH/Counterexamples.lean`); the hole stays `lstar_subordination`.
NO RH CLAIM.

**Lane status after wave 10.**  **L2 (edge A, the generic half):
documented STOPPED** — the global-profile mixing route is closed
(`LAW_LONGRANGE`), the clean equivalence state is frozen (`L2 generic
⟺ anti-concentration of the explicit dc block field`, core slack
`S = +0.0547` measured), and per the hard rule no further coordinate
change counts as progress; return with new tools.  **L\* (the open
center): dormant since r296** — the last L\*-side round was the DENS
fork closure (`DENS_WORLD_BLIND`, consumed in wave 9); the contract
`PRIME.LSTAR.SUBORDINATION.01` [O] stands at 57/57 sign-safe measured
with the harmless margin law, and `PRIME.LSTAR.CLOSED_FUNCTIONAL.01`
[O] keeps its named open fronts (loss-corpus forensics, why-L2, the
window knife edge).  Both edges rest with a clean documented state;
the mincut (base 4 / refined 5) is unchanged.  NO RH CLAIM.

r306 ran the **Rényi-3 round** (`renyi3_probe.py`, 27/27, SPEC_SHA
`3bb365e1`; contract `PRIME.L2.ATOM.RENYI3.01` — experiments-side,
exploration only, no ledger row; reviewer plan §5, the sharpest new
fiber attack — explicitly sanctioned as *new information* after the
r304 documented stop because it is **pointwise** instead of a slope
target and uses the **cubic moment** instead of the closed
max-/discrepancy routes): prove or refute
`Σ_j q_j³ ≤ C·(log m)^A/m²` pointwise on every rung of the atomic
|PΔ| profile (q = |PΔ|/L1 over the m level-2 blocks), the family
A ∈ {0, 1, 2} preregistered and C frozen on the first 5 rungs of the
(N, kz)-sorted ladder.  **Verdict `RENYI3_GO(C = 1.069, A = 2)`** —
the inequality **holds pointwise on all 57 rungs** (42 core + the 15
r286 extension anchors N_w 942..1218, rebuilt with the full block
machinery: contribution ward 4.9e-13, count link n_act == m 15/15)
with **growing reserve** (trend −0.322 on both frozen estimators;
the whole extension holds at reserve 2.6..5.7).  The polylog
exponent is real: A = 0 fails (the third shape moment
M₃ = m²S₃ rises +0.153 before decaying — exactly the disclosed
algebraic prior from the r301 records), A = 1 fails on precisely the
two near-critical rungs kz53/kz67, which sit 1.4–1.9 % under C₂ —
polylog-**squared** is the honest sharp form, with kz53/kz67 as the
sharpness witnesses.  Via the exact Rényi/Hill chain (two Lagrange
witnesses in pure Fractions, dev 0; equality exactly on the uniform
vector; the bridge rational with all constants; Lean-ready statement
printed for the Lean worker) the GO fixes the **new pointwise proof
target of the fiber**: `n_eff = N₂ ≥ N₃ ≥ m/(1.034·log m)` —
asymptotically above every demanded power m^0.888.  The anatomy is
the friendliest possible: the cubic mass is a **narrow-band**
functional (97 % within a factor 4 of q_max) carried ever more
**broadly** (top-8 share 0.780 falling at −0.268; strict triples
92 % of the cube) — no heavy-few obstruction; the minimal sufficient
statement is named **SHAPE3_TARGET** (M₃ polylog-bounded, the
third-moment sibling of the r302-proven M₂ stationarity 1.973; M₂
med here 2.03).  World census with the right sign:
**WORLD_SENSITIVE** — EPSTEIN holds the bound, SCRAMBLE **breaks**
it by 1.67× (the law is recursion structure, destroyed by
scrambling, not block combinatorics — the first world-separating
pointwise law of the lane).  Leg 0 anchors bit-near (Rényi family
meds/slopes, core slack S = +0.0547 at dev 6.7e-16, count link
42/42, n_eff_atom 118.0/+0.942, marginal invariance ≤ 8.7e-16).
Honest negatives: C₂ was frozen on the *shallowest* rung and the
kz53/kz67 margin is 1.4–1.9 % — the GO fixes a proof **target**, it
proves nothing beyond the 57 measured rungs; the atom-level (dc)
sibling stays unformalized.  Must-fails: power-mean flip breaks by
1/64 exact, the preregistration-breach mutant CAUGHT (set ward +
real C_full/C_cal 2.10 at A = 0), unnormalized q LOUD (factor L1³),
one-atom collapse 212× LOUD, scope mutants flagged; the two
disclosed pre-record code fixes (print format; mutant reference
aligned to the spec's w9) moved no bar, band or rule.  NO L2-lemma
claim, NO RH CLAIM.

r307 ran the **fixed-head kill round** (`fixed_head_probe.py`, 28/28,
SPEC_SHA `ec2bb008`; reviewer adjudication §4 solution C — the
cheapest kill test of proof architecture C (fixed head + contractive
tail); contract `PRIME.LSTAR.FIXED_HEAD.01`, experiments-side,
exploration only, no ledger row — this reopens the L\*-side after the
r296 dormancy noted above): in the μ-orthonormal frame
`E = E_H + E_T` with H = the first r **flat archimedean edge atoms
below the first prime** (u < log 2; the r284 carriers), under two
sealed window-fixed orderings (ascending fold; the frozen w9 extremal
rank permutation, regated exactly), λ_max(E_T(r)) was measured for
r = 0..16 on **77 windows** (42 core + 15 r286 anchors + 20 *new*
deeper windows N_w 1218..1650).  **Verdict `HEAD_GROWS`** — the
kill test *splits* the reviewer's question: **no fixed r ≤ 8 exists**
(best candidate leaves min reserve 6.5e-6, four decades below the
sealed 1e-2 bar; a fixed r_min ≤ 16 exists on 15/77 windows only,
all N_w ≤ 434; the fixed-head reserve falls with S at sp −0.93,
TS slope −3.15 — the r286 margin-law class: a fixed head changes the
prefactor, not the decay class), **but** the *full* edge (13..96
atoms, growing with the window at sp(edge, N_w) = +0.98) restores a
macroscopic reserve on 77/77 (min 2.19e-3, median amplification
3.1e4): the near-one-atom anatomy is **real and proof-relevant as a
coordinate, refuted as a fixed dimension** — architecture C in its
fixed-head form is dead; the honest successor object is the
window-dependent head of size ~ log2/(2Δ_w), whose own reserve
decays slowly (TS −0.87, disclosed).  The Schur/Woodbury ledger is
exact: `det(I−E) = det(I−E_T)·det(S_H)` on 57/57 (rational-exact on
the JF9 toy), the border-augmented identity against the independent
r244/r258 route on 57/57 (q_N < 1 reproduced, min gap 0.0195);
λ_min(S_H(8)) > 0 on 57/57 **but equals the wall margin to 4 digits
and is anchor-monotone along the r286 margin decay (sp −0.92) — the
hoped-for simplification is empty: S_H carries the whole problem**;
the border is inert (S_aug positive, degradation ≥ 0.873 —
`BORDER_BREAKS_HEAD` did not fire).  Hardening: the r289 rational
twin is `TWIN_METRIC_OK` (identical r_min, max |Δreserve| 1e-7);
EPSTEIN/SCRAMBLE are `CONTROL_COLLECTIVE` (EPST 2191 → 2189 at
r = 16, SCR 1.4e7 → 3.2e4 — no small head rescues a dead world);
Gershgorin/Schur-test row sums stay 1.5..3.6 on the tail (classical
bounds dead, as r283 measured on the full E); mp spots 3/3 at dps 30
(worst 2.8e-14); must-fails m1 target-inverse ordering AST-flagged /
m2 wrong-sign Woodbury 0.163 loud / m3 monomial frame hides the toy
wall 0.805 loud / m4 r = 0 exact.  Four pre-spec sizing scratches
disclosed in the spec.  NO L\* claim, NO RH CLAIM.

r308 ran the **block-Green discovery round** (`block_green_probe.py`,
30/30, SPEC_SHA `d5147850`; reviewer adjudication §4 solution A /
plan round "305" — experiments-side, exploration only, no ledger
row): the automated search for a **matrix-valued discrete Green
identity on fourfold fold blocks** — the route the reviewer named
after the scalar profile functionals (r290–r295), the
absolute-value majorants (r297/r299/r300) and the diophantine
relations (r289 `METRIC_ONLY`) all failed: does the augmented form
`Q(p,t) = ∫p² d(μ−ν) + 2t·u(p) + B·t²` (the v958 bordered object,
`B = S_{N−2} + 5/7`) admit an exact decomposition
`Q = Σ_r ⟨G_r Δ_r, Δ_r⟩ + (5/7)t²` with sealed fourfold-block
coordinates (first/second differences, the r288 antiphase
`layer_i − layer_{i+2}` coordinates, the local gross-mass mean, the
border `t`) and source-pure blocks `G_r`?  **Verdict
`IDENTITY_EXISTS` + `BLOCK_INDEFINITE_MAIN` + `FEAS_DIAG` world
separation.**  The identity **exists everywhere** (exact Fractions
with entrywise reconstruction on the hand toy, four synthetic small
models and the frozen real MINI16; f64 residuals ≤ 8.1e-14 on w9,
the r289 rational twin, EPSTEIN/SCRAMBLE/SMOOTH and all 57 rungs at
deg ≤ 8; kernel exclusion 100 %) — existence is the *disclosed easy
half* (linear in G, hugely underdetermined, dof 15..7593).  The
sealed eigenvalue-free minimum-Frobenius selection is indefinite
**everywhere** — even on the positive-class calibrator SM0: the
*selection*, not the world, produces the indefiniteness — so
`BLOCK_INDEFINITE_MAIN` fires on the letter of the sealed rule.
**The round's central measurement** (sealed diagnosis clause,
calibration amendment a1: one uniform two-stage Dykstra schedule
200/2000 for every world): the SDP-like feasibility census
**separates the worlds** — w9 and the rational twin at deg ≤ 8
converge to *genuinely all-psd block families* (min eig rel
+6.6e-16 / +2.0e-17 at affine residual 3.7e-14, after 200 steps)
while EPSTEIN/SCRAMBLE stall at −0.45/−0.49 after 2000 steps: on
the restricted subspace, where **every** world's target is positive
definite and nothing is theorem-forced, MAIN and its
diophantine-trivialized twin admit an all-psd fourfold-block Green
decomposition and the two hard controls (at this schedule) do
not — the first block-level world discriminator of the L\* lane,
**one-sided** (non-convergence proves no infeasibility) and
diagnosis-grade only.  SMOOTH sits marginal (−1.3e-05; its crossing
28 equals the second cap DEG_B — the sealed boundary case);
w9/twin at DEG_B = 28 stay **open** (−4.2e-05 after 2000).  The
DEG_B control negativity (crossings 26/22/28) is *forced by
theorem* given existence — gated live on EPSTEIN/SCRAMBLE (held),
disclosed, never sold as discovery.  R282 demarcation held
explicit: the Kasteleyn/SOS refutations concern the *full* signed
configuration class (every Cauchy–Binet cell, `h_n` itself); this
identity lives on the restricted subspace deg ≤ 8/28 ≪ N_w plus
one border coordinate — a different language, no contradiction.
Anchors bit-near (w9 367/263/104, crossing 185; r288 carrier pin
z_v −3.149 destructive; r282 pin N₂(MAINLIKE) exact; B_w9 =
8.368649 with 182 nonnegative ρ_k).  Must-fails: cholesky-of-target
FLAGGED, omitted remainder breaks by exactly 5/7 at (t,t), posthoc
family FLAGGED, partial monomial coverage leaves an exact defect
4.5e+01 LOUD.  Honest: a feasibility census fixes a **target**
(find a sealed *constructive* psd G rule on MAIN, extend it past
DEG_B, prove the world split), it proves neither L\* nor any
cofinal statement.  NO RH CLAIM.

r309 ran the **paired-cone pilot round** (`paired_cone_probe.py`,
33/33, SPEC_SHA `f8d99877`; reviewer adjudication §4 solution B /
plan round 306 — experiments-side, exploration only, no ledger
row): the third full proof architecture of the L\* lane — the
positive and negative source processed **pairwise as rank-one
updates** of the same augmented form `A = [[H, u], [uᵀ, B]]` as
r308, base and border together.  The form is rebuilt *exactly* as
an ordered signed rank-one stream (sealed base = the imported 5/7
`t`-floor + reserved/unmatched μ atoms; one signed budget step
`|S_{N−2}|`; every ν atom greedy-matched to its nearest free μ
partner; every border atom split exactly into a ±(η ± e_t) pair),
and at every negative step the reviewer's **local reserve**
`r = 1 − L_bb + L_ab²/(1 + L_aa)` is measured — the
Sherman–Morrison cancellation as an *explicit positive square*,
with the determinant dictionary `det(M₁) = (1 + L_aa)·det(M)`,
`det(M₂) = r·det(M₁)` exact on the Fractions toys (hand toy PC4:
reserve 7/9, dets 9/14 → 27/14 → 3/2) and f64-warded on w9
(reconstruction 4.8e-16; mp ward dps 60, dev 3.0e-13).  **Verdict
`DECOMP_EXACT` + `MAIN_RESERVE_POSITIVE` + `CONE_PARTIAL` +
`WORLD_DISCRIMINATOR`(all sealed stats world-blind).**  MAIN
survives the ordered chain at **both** caps with macroscopic
margin (w9 min r +0.9011 at deg ≤ 8 / +0.3232 at deg ≤ 28; the
r289 rational twin bit-near; 57/57 ladder rungs all-positive, min
+0.7357@kz97), and w9's two tightest pair reserves sit *exactly*
on the r284 extremal folds {2, 4}.  The reviewer's decisive cone
question **splits**: the sealed mass-ratio cone
`r ≥ 1 − c₁·(v/w_a)` (c₁ = 8.5436, frozen on the five shallowest
rungs) is **sound** — zero violations on all 20714 pointwise test
steps (52 rungs + w9 + twin) — but certifies only 56 % of the
steps (positive predicted bounds on 11643/20714); the sharper
local shield cone `r ≥ 1 − c₂·(v/SM₂)` overshoots exactly where
it is positive (54/54 positive bounds violated, every violated
step has true r ≥ +0.901).  Reading: the reserve **is**
predictable in the sound direction from one source quantity, but
no sealed *local* φ is yet a certificate — the named successor
object is a φ with a base-depth term (the deg-8 base carries most
of the reserve), not retro-fitted.  The information test stays
silent by the sealed letter (pooled tightest decile best |sp| =
0.50 at pair distance; on w9 alone the mass-ratio/shield features
reach −0.61/−0.58, reported), and the reviewer-B4 O(log N)
fold-bit register is measured **irrelevant** at this cap (max
|sp| 0.32).  Honest world census: at deg ≤ 8 the ordered *pair*
reserve is world-blind (the controls' pair phases are all
positive); the *entire* EPSTEIN/SCRAMBLE indefiniteness there is
the negative **budget step** (S_{N−2} = −3.992/−5.237 past the
flip — the r243 budget coordinate reads the wall; amendment a1
disclosed: the design-time "every deg-8 target is PD" sentence
was corrected, spec-prose + reporting only, no bar or rule
moved); the deg-28 control breaks are theorem-forced and
disclosed.  Anti-circularity at r275 sharpness: the o1/o2 +
forced-tail-sum pin re-run exact; the target-inverse cone mutant
and the posthoc-pairing mutant FLAGGED; wrong-sign
Sherman–Morrison caught by the exact det dictionary (dev 8/9
exact); the order-break mutant shifts the reserve by exactly 4/9
while the reconstruction stays exact — the r-sequence, not the
sum, is the ordered object.  Honest: a passing cone fixes a
**target** for proof work; this round proves neither L\* nor any
cofinal statement.  NO RH CLAIM.

r311 ran the **block-Green nontriviality round**
(`blockgreen_nontriviality_probe.py`, 34/34, SPEC_SHA `fac7a8df`;
the reviewer's *mandatory* round before any constructive G-search
— experiments-side, exploration only, no ledger row): is the r308
psd block family stronger and more local than `Q_w ⪰ 0`, or a
sparse-Gram / chordal restatement whose SDP separates the worlds
by force?  **Verdict `STRICT_SOURCE_CONE` with the binding
separation-mechanism clause** — both reviewer scenarios are true
at once, on different layers.  (1) **The r308 world separation is
fully the budget sign**: the sparsity graph of the Δ coordinates
(width-3 atom band + universal border vertex `t`) is **chordal**
on every size including the full w9 S = 367 graph (MCS +
Tarjan–Yannakakis, maximal cliques == the 364 sealed blocks;
C4/C5 control correctly non-chordal), every block spans its full
local R⁵, so on *evaluation* space the image cone is exactly the
chordal pattern-psd cone (Agler et al. / Grone et al.); the
control targets are **indefinite** at deg ≤ 8 through the one
negative budget diagonal (EPST −3.992 / SCR −5.237; λ_min rel
−0.86/−1.00 vs w9/twin +8.4e-4 PD) — the r308 Dykstra separation
was theorem-forced; the trivial common dual `Y_t = e_t e_tᵀ`
(**one** rational entry — the r243 budget positivity
`S_{N−2} ≥ 0`, the *known* wall reading) closes the r308
one-sided stalls two-sidedly and predicts two **new blind**
scramble worlds 2/2 before their runs; the decisive ablations
seal it: EPST/SCR with `(t,t) ← |S|` become PD and the Dykstra
**converges**, w9 with the EPST budget transplanted **dies** —
flip one scalar and the separation inverts; the exact Schur-tail
lemma (`Schur(A_sys@d) = S_{N−2} − Σ_{k≤d} F_k²/h_k`, exact on
SM0/SM1) shows the wall sign enters the target mechanically as
the budget ρ-tail and decides all four r308 small-model OPEN
stalls as trivially target-indefinite (even the positive-class
SM0: `−(ρ_3..ρ_8) = −7.08e-2` exact); SMOOTH's marginality is a
*boundary* target (S = +3.48, λ_min ≈ 0).  (2) **But the cone is
genuinely strict on the compressed subspace** — the round's
second discovery: 0/16 sealed random in-span PD samples decompose
(w9A 0/6, MINI16 0/6, SM1 0/4; staged Dykstra up to 20000), every
MINI16/SM1 stall carries a valid polished-numeric Farkas dual,
and MINI#0 + SM1#0 carry **fully exact in-span rational
certificates** (exact Chebyshev basis, denominator 1e6,
`⟨Y,Q⟩ < 0` exact; MINI16 = the real-w9 miniature with exact
full span 55/55) — `C_w` is *strictly* smaller than
span ∩ S₊: block membership is a genuinely stronger property
than positivity, which MAIN + twin **have** at deg ≤ 8 and
generic positive forms **lack**.  The ambient span layer is exact
too (codims TOY4 0 / SM0 11 / SM1 11 / SM2 2 / SM3 1 / MINI16 0
/ w9A 4 / w9B 236; exact annihilators, SM1 rank-one ambient
counter-model with exact rational Farkas).  Protocol audits
clean (r308 `feas_diag` objective-free, start ablations);
w9@deg 28 stays honestly **open** (PD-thin, −1.78e-5 after
20000, dual diverges — one-sided).  Consequence: the planned
R312 rank-one-conductivity round premised on the r308 *world
discriminator* is dead in that form (the discriminator was the
wall sign); the re-scoped GO object is cone **membership** — why
the bordered-Hankel world targets sit inside the strict cone
while generic PD forms do not.  NO RH CLAIM.

r312 ran the **block-Green membership round**
(`blockgreen_membership_probe.py`, 32/32, SPEC_SHA `6c32f749`;
THE one construction round granted by the reviewer tree after
r311's `STRICT_SOURCE_CONE` — experiments-side, exploration only,
no ledger row): does a source-pure **constructive rule** (no SDP
optimization in the final statement) write down an explicit psd
block family `G_r = Σ_ℓ c_{r,ℓ} v_ℓ v_ℓᵀ` with `c ≥ 0` for the
world targets, over a *pre-sealed* 22-generator library in the Δ
basis (fold distances 1/2, antiphase 3/4, the r307 arch
coordinates, border-vs-interior pairs `D_a ± D6`, symmetric /
antisymmetric four-block modes), with an explicit coefficient
formula `c_{r,ℓ}`(source quantities)?  **Verdict
`COEFFICIENT_SIGN_WALL`** — the library **span** carries the w9
identity exactly (unconstrained rel 2.4e-13; abstract span 15/21
exact) but the **cone** does not: deterministic Lawson–Hanson
NNLS stalls at rel 4.7e-4 with a **verified I-polished Farkas
certificate** (δ = 1e-4, min normalized column product +9.7e-5,
`⟨y,q⟩ = −0.9975`), and the certificate mass localizes on the
**border/budget row** (t-row fraction 0.583 ≥ the sealed 0.5; at
deg 28 even 0.725) — the identity forces negative coefficients
exactly on the wall coordinates: *the sign question of the c IS
the wall, in the constructive language too*; the twin is
type-identical (METRIC_ONLY holds).  **Exact grade** on the
miniatures: SM1 and MINI16 carry **fully exact I-polished
rational Farkas certificates** (den 100, `⟨Y,q⟩ = −0.9988 /
−1.0000` exact rational < 0, all 154/286 exact column products
≥ 0), and on SM1 even the library *span* fails exactly
(`[M_lib | q]` rank 41, EXISTS FALSE); rung census 1/57
NNLS-feasible (worst rel 8e-4 at kz12) — the sign wall is uniform
across the ladder; the four sealed formula candidates
Φ_A..Φ_D (masses, tent fractions, budget share, per-type table;
calibrate-on-w9 / freeze / verify-on-57+twin) never fire (best
calibration rel 7.7e-3 ≫ 1e-8).  **Membership anatomy** (the
round's discovery): the converged r308 Dykstra family is
high-rank ({rank 3: 17, rank 4: 79, rank 5: 268}) and
library-*aligned* (top-eigvec alignment med 0.9973) with
library-cone share med **0.976** — 97.6 % of the psd family lives
in the sealed rank-one cone and the *whole* membership
obstruction sits in the remaining 2.4 % of SDD-forbidden negative
cross mixtures; the dual anatomy of the 10 r311 sample duals
shows the generic-missing directions are low/mid-degree
**interior** mass (|z_t| med 0.000), not border mass.  w9@deg 28
stays honestly **open**, two-sidedly hardened (staged anchor
−1.784e-5 == the r311 record; library NNLS@B infeasible, same
wall class; +80000 extension steps improve only to −7.66e-6, a
slow tail consistent with asymptotic feasibility, not decided;
the strengthened dual POCS runs but polishes invalid).  Leg 0
reproduced every r311 record bit-near on the identical rng stream
(0/16 strictness, 10/10 polished duals, both exact certificates).
Consequence (sealed reviewer tree): **not a GO** — lane A closes
as cone language with the membership mechanism *named*
(block-psd membership **without** rank-one-SDD membership,
obstructed at the budget/border sign); the resources move to the
fiber.  Two disclosed calibration amendments (f64 I-polish
certificate bookkeeping; the m3 harness probes the r289
rationalization variable u/Δ) — the four-way adjudication tree
never moved.  NO RH CLAIM.

r313 ran the **Rényi-3 proof-form fork round**
(`renyi3_proof_fork_probe.py`, 32/32, SPEC_SHA `6505dd10`;
reviewer plan: triple incidence vs four-step Floquet —
experiments-side, exploration only, no ledger row): two sealed
proof architectures for the r306 pointwise cubic law
`Σq³ ≤ C·(log m)²/m²`, executed side by side under the binding
reviewer instructions (do **not** chase the sharp 1.069; the
theorem must not depend on von-Mangoldt arithmetic — sought class
`RecursiveDifferenceProfile` with MAIN + EPSTEIN in, SCRAMBLE
out).  **Verdict `BOTH_PARTIAL` (named remnants).**  Route R3A
(triple incidence): the raw atomic presentation is **exact** —
every block value is the sum of local c-differences, atoms at one
position form a β/ω **fold pair**, and the cube splits exactly
(block ward 3.9e-16 on 61 live worlds) into T1 diagonal / T2
two-equal / T3 near (shared fold) / T4 far (fully separated);
med signed shares +0.38 / +2.15 / −1.14 / −0.42 — the types
**cancel against each other** (T2 alone carries 2.15× the cube),
they are not independently small.  Two proof hopes are banked:
the fold multiplicity is **uniformly 2** on 57/57 rungs (an exact
structural class bound, not a census) and the far triples
genuinely **telescope** (TC_far med 0.069 — 93 % of their abs
mass cancels, falling).  Per-type prereg at A = 2
(first-5-frozen constants): T2 and T3 HOLD 0/57 with falling
trends (−0.400/−0.299); T1 fails 2/57 (kz55 2.54×, kz53 1.70×)
and T4 fails 1/57 (kz55 1.84×), both with **falling** trends —
shallow-calibration artifacts of the r306 A ≤ 1 kind, but the
sealed rule stands: COMPOSITION REFUTED-IN-FORM.  World census:
SCRAMBLE violates exactly T2 (2.85×) but EPSTEIN also violates
T2/T3 while its *total* holds the r306 bound — MAIN-frozen
per-type constants are **not world-portable**.  Route R3B
(four-step Floquet): the local transfer step is **real and
exact** (`r_{k+1} = t_k + ap_k·r_k + bp_k·r_{k−1}`, ward 1.9e-12,
det dictionary 4.4e-16, SMOOTH degenerate-skipped), but the
four-step monodromy on the split cubic mode space **expands**
(med sr 1.0600, contracting rungs 0/57, product exponent +1.917
vs the required −2): after r304 (single step) and this round
(period-4 Floquet step), **no transfer-operator contraction form
of the cubic law remains open at the chain level**.  The class
finding (sharpest honest negative): the four-block comb property
P4 excludes SCRAMBLE but **also EPSTEIN**; every other sealed
candidate (fold share, recursion, multiplicity, mass, assignment,
telescope) is world-**blind** — no boolean property separates
worlds the way the r306 total bound does; the separation lives in
the *size* of the type terms, so the class needs a
**quantitative membership functional**, not a property list.  The
m4 shuffle instance is rejected by P6 (293/300 atoms outside
their interval) while mass conservation still holds on it.
Anchors bit-near r306/r304 throughout.  Honest: nothing here
proves or refutes the cofinal law.  NO RH CLAIM.

r314 ran the **signed-cubic-flux round, part 1**
(`signed_cubic_flux_probe.py`, 29/29, SPEC_SHA `841b3196`;
reviewer contract after the r313 adjudication — **exact algebra
only**, no size estimate, quantification deferred to R315/R316;
experiments-side, exploration only, no ledger row): with
`x_j = (PΔ)_j`, `σ_j = sign(x_j)`, expand `|x_j|³ = σ_j·x_j³`
over the r313 fold genealogy into the signed cubic tensor
`C_{αβγ} = Σ_j σ_j·x_{j,α}x_{j,β}x_{j,γ}` and decompose
`C_cube = ΔF + C_collision + C_boundary`.  **Verdict
`SIGNED_CUBE_IDENTITY` with a vanishing boundary** — the
decomposition exists exactly: on w9 it is decided in **exact
Fractions on the real data** (35 blocks / 150 fold groups; brute
tensor enumeration == Newton aggregates == flux telescope, every
deviation the rational number 0 — `Fraction(float)` is exact on
dyadic f64 atoms) and to 4.5e-17 in f64 on all 57 rungs + mains
+ EPST/SCR (bar 1e-13).  The divergence form is genuinely
**local**: far triples enter as telescoping edge fluxes
`dF = 3G(s1² − s2)` consuming only the transported prefix state
along the position-ordered fold groups (telescope Newton-vs-path
worst 4.1e-16), and the **opening-flux lemma**
`F₁ = G³ − 3G·G² + 2G³ == 0` is cubic algebra, so
`C_boundary == 0` — the sealed language class closes without
remainder (disclosed: the razor acts *before* the genealogy; an
unmasked presentation would re-introduce a boundary term).  The
collision space is exactly **countable** by the banked r313
multiplicity-2 asset: config counts full/pair/far ==
`n / 3n(n−1) / n(n−1)(n−2)` and atom-triple count
`3p₁p₂ − 2p₃ == 8(n + 3n(n−1))` exact on 61/61 live worlds.
Measured preview for R315/R316 (labeled, no bound claim): med
signed shares ΔF −0.4226 (falling −0.422), C_pair +0.5980,
C_full +0.8537 (rising +0.213) — the two collision terms
together (+1.45) carry the cube against the negative far flux;
flux cancellation FC med 0.629 falling −0.141; the world table
(w9/w13/EPSTEIN/SCRAMBLE) is sealed record data — the SCRAMBLE
localization census names the **full-collision** column, but
EPSTEIN sits far from MAIN in every share while holding the
r306 total bound: single shares do **not** separate worlds; the
R315 functional Φ₃ must be built from the divergence-form
*structure* and must not be calibrated on these tables (sealing
discipline, disclosed).  Anchors bit-near r313 (type shares
+0.3808/+2.1542/−1.1442/−0.4226, TC_far 0.069/−0.050, fold
multiplicity == 2 on 57/57).  Must-fails: σ dropped (toy break
2 exact, w9 1.8e0 LOUD), double-counted fold group (breaks 2
and 98 exact, CAUGHT), unordered support (per-edge break
(0, 108, 108) exact, the total disclosed permutation-blind,
LOUD), mult-blind collision count (break 56 exact, 8× wrong,
CAUGHT), scope mutants flagged.  Honest: part 1 is bookkeeping
only — nothing here bounds anything.  NO RH CLAIM.

r315 ran the **Φ₃-functional round, part 2**
(`phi3_functional_probe.py`, 29/29, SPEC_SHA `92d35a3a`; reviewer
contract part 2 — define the quantitative membership functional
Φ₃ *in advance* from the r314 divergence-form **structure**,
normalized to the Rényi-3 scale `NORM = m²/((log m)²·L³)`, and
run the blind world test; experiments-side, exploration only, no
ledger row).  Three candidates sealed before evaluation:
`Φ₃a = NORM·(|COLL| + |BND| + |DFLUX|)` (reviewer raw),
`Φ₃b = NORM·|COLL|` (the combined signed collision sum),
`Φ₃c = NORM·|COLL|·FCIX` (flux-corrected); the honesty conditions
are **machine-audited** (AST identifier scan: no Σq³ read-back;
sealed literal scan: no r314 world-table number in any builder —
the e1/e2 must-fail mutants prove both audits bite), and the
literal `|Σ|x|³ − ΔF|` form is adjudicated read-back-adjacent and
demoted to a diagnostic column (== Φ₃b to 1.6e-15).  **Verdict
`PHI3_ALL_BLIND` on the sealed letter** — no candidate passes all
four reviewer criteria, and the anatomy is sharp and
concentrated: the *entire* failure sits on **kz55 + kz67** (the
only violators of all three first-5-frozen C₀ = 2.63/1.51/0.94;
kz55 alone tops SCRAMBLE in the rank test, Φ₃a 4.61 > 2.39, and
blows the b/c bands 66/88 vs bar 30) — the same near-critical
family that killed r306 `A ≤ 1` and the r313 T1/T4 constants,
with every trend **falling** (−0.40..−0.77 on both estimators):
the known shallow-calibration artifact, but the mid-ladder rule
was not sealed and is not applied post hoc.  The **local cause is
named by the probe's own coordinates**: kz55/kz67 carry FCIX
0.955/0.915 against med 0.629 — exactly the rungs where the
intra-block flux cancellation *dies*; the FCIX → 1 stratum is the
R316-relevant obstruction, and FCIX is source-pure and computable
in advance.  What *holds* of the reviewer table: EPSTEIN holds
all three frozen bounds (Φ₃c separates it 7× downward via its
world FC 0.101), the rational twin w13 is **near-identical** to
w9 (factor 1.07–1.17 — the strongest twin result of the lane),
the SCRAMBLE cause is named **COLL** (component devs dflux 1.33 /
coll 3.69 / fcix 0.10, K4 fires), and candidate (a) passes its
band bar (22.85 ≤ 30).  Both reviewer-table contrasts fired: the
multiplicity-3 control (half-atom split, G1/blocks/mass preserved
*bitwise*) breaks the collision count bound 48762 vs 14448 (toy
216 vs 64, break 152 exact) and is rejected by the cap while Φ₃
is provably **blind** to it — the multiplicity cap is a necessary
class side condition, not a consequence of the functional; the
assignment shuffle (seed 315001) is rejected 289/300 with the
flux profile broken edgewise.  Must-fails: e1 Σq³ read-back
AST-CAUGHT, e2 r314-table calibration literal-CAUGHT, e3
mult-2-built control accepted as normal (sharpness), e4 wrong
normalization exponent LOUD (factor m = 35 exact), scope mutants
flagged.  Anchors bit-near r314/r306.  Honest: ALL_BLIND stands —
the divergence-form structure with first-5-frozen constants is
*not* the membership functional; the kz55/kz67 + FCIX-stratum
diagnosis is post-hoc census, no rule; nothing here bounds
anything.  NO RH CLAIM.

r316 ran the **two-regime-bound round, part 3**
(`two_regime_bound_probe.py`, 35/35, SPEC_SHA `5c28b12b`; reviewer
contract part 3 — formulate the pointwise Rényi-3 bound as a
coupled two-regime statement over the source-pure FCIX stratum,
with θ = 0.85 sealed from the r315 record gap and a **mid-ladder
calibration sealed in advance** (CAL_START = n//3, N_CAL = 5,
small-m ranks certified individually); experiments-side,
exploration only, no ledger row).  Four sealed regime majorants,
all ≥ ρ₂ by exact algebra warded live (worst slack 6.5e-16 on 69
worlds): `ΦL2 = NORM(|COLL|+|BND|+FE)` (flux-index form), `ΦL1 =
NORM(|COLL|+|BND|+|DFLUX|)` (r315 raw), `ΦH2 = NORM(CNT3+|BND|+
FE)` (the multiplicity-2 collision **counting** majorant), `ΦH1 =
(m·QMAX/log m)²` (concentration); purity machine-audited (AST +
record-literal scans; θ-post-hoc, cubic read-back and literal
calibration mutants all caught).  **Verdict `TWO_REGIME_DEAD`
(L fails; H fails)** on the sealed letter — and the anatomy is
the round's find: (1) **the FCIX stratum is not the near-critical
family** — the mid-ladder freeze is killed on the regime-L side
by kz53 (ρ₂ 1.049 with bulk-normal FCIX 0.654) and deep spikes
kz83/kz105: the obstruction family cuts *across* the
flux-cancellation stratum, so FCIX is the wrong (or an
incomplete) regime coordinate; (2) ρ₂ itself is **not below its
mid-ladder window** (kz53 1.049 / kz83 0.779 vs the cal-window
max 0.458): any tight pointwise majorant fails at kz53 under a
mid-ladder freeze — the r306 first-5 protocol was not a
shallow-calibration artifact but **load-bearing** (the profile
is non-monotone with recurring near-critical spikes); (3) the
**regime-H mechanics object** delivered as census: the FCIX
outliers kz55/kz67 are near-**one-block** worlds — top-1 cube
share 0.558/0.785 vs 0.18 regime-L med (dev 2.68, the named
discriminator; kz55 additionally 10× compensation κ 0.105);
concentration, not counting tightness (dev 0.53), distinguishes
them — but kz67 misses the mid-window H constants by 1.4×/2.6×
and kz55 fell into the small-m set (rank 20/65), so the H test
stratum was one rung.  What holds: anchors bit-near (r314
shares/FC/mult, r315 C₀ + FCIX outliers 0.955/0.915, r306 C₂
1.069 with 0/57); the EXT2 extension clean (8 deep anchors to
N_w 1393, all mult 2, **no new H member** — the FCIX stratum did
not grow with depth); the 21-rung small-m certificate table
(C_small 1.0694 = the r306 shallow maximum); the class machinery
intact (EPSTEIN/twin/main admitted with the strongest twin band
of the lane 1.04, SCRAMBLE rejected via COLL attribution 3.69 +
edgewise flux break 290/300, mult-3 control rejected via the cap
with all four majorants provably blind).  Honest: DEAD stands —
no theorem candidate printed; the regime-L failure is partly
majorant looseness (NORM|COLL| rises vs ρ₂, trend +0.086/+0.202
— exactly the r314 warning that C_full grows), so a sharper
flux-exploiting majorant is not excluded, but the kz53 obstacle
binds every tight majorant under a mid-ladder freeze; R317
direction (census-grade): the regime coordinate must capture the
near-critical family itself (TOP1/QMAX separates kz55/kz67; kz53
needs a second coordinate) or the spikes become a certified
exception family (r287-F2 pattern).  NO RH CLAIM.

r317 executed **reviewer fork (b) — the exception-family census**
(`exception_families_probe.py`, 38/38, SPEC_SHA `04fbe5c0`;
contract `PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01`,
experiments-side, exploration only, no ledger row; coexisting
with the parallel r318/r319 rounds).  The statement form under
test: *all sufficiently large generic windows + explicitly
classified exception FAMILIES*, with the **hard gate sealed in
advance** — at most TWO source-pure families plus the generic
theorem; any uncovered violator, family growth or world leak
fires `WHAC_A_MOLE` by contract.  Two sealed source-pure class
functionals (AST + record-literal audited): `F_A` = rank-local
QMAX spike ratio (concentration), `F_B` = rank-local ΦL2 spike
ratio (divergence-mass spike), window W = 5, thresholds frozen by
the sealed largest-gap rule (k ≤ 6, gap ≥ 1.25) **before any
bound evaluation**.  **Verdict `WHAC_A_MOLE(kz53, kz83)`** on the
sealed letter — the hard gate fired exactly as the contract
demands: the sealed rule recovers **B = {kz55, kz67}** (the
r315/r316 FCIX pair, F_B 7.23/4.96 with a clean 1.78 gap; finite
certificates C_B = 1.0536 ≤ the r306 shallow max, ΦL2-warded,
non-growing, 0 EXT2 members), but class A stays EMPTY (best gap
1.233 misses the sealed 1.25 bar by 0.017), and on the 63-rung
complement the mid-ladder generic constant C_gen = 0.4579 is
violated by exactly the two uncovered rungs kz53 (ρ₂ 1.0493) and
kz83 (0.7791) — a third exception form would be needed; no third
class added, abort by contract, recommendation back to fork (a).
The census behind the letter is the round's find: the **F_A
top-3 are exactly kz53 (2.47), kz83 (2.39), kz67 (2.38)** — the
rank-local QMAX ratio ranks the complete mid/deep near-critical
family on top, refuting at census level the r316 conjecture that
kz53 needs a second coordinate; but the distribution below is a
**continuum** (1.93, 1.90, 1.74, …), not a gap-separated family,
and F_B over-ranks kz12 (2.79, ρ₂ 0.38 — a ΦL2 spike that is NOT
a ρ₂ spike) above kz53 (2.70): threshold classification on these
coordinates cannot cover kz53/kz83 without swallowing harmless
rungs — the exception-family FORM is the wrong statement shape
for a spike continuum.  What holds: anchors bit-near incl. the
complete r316 anatomy; the generic complement trend falls
(−0.170, reserve med 2.06); 21 small-m certificates; world
machinery intact (twin 1.04, SCRAMBLE rejected via COLL 3.69 +
edgewise shuffle break 288/300).  R318 direction (census-grade):
fork (a) with the QMAX local ratio as a *continuous* regime
coordinate (bound ρ₂ BY the coordinate, not classify by
threshold), or the generic constant at the r306 first-5 scale
where no exception family is needed on the measured ladder.
NO RH CLAIM.

**Wave 11 (2026-08-26)** froze the **architecture day** (rounds
r305–r316 incl. r310b) as **`v968_architecture_adjudication.py`**
(ledger `PRIME.LSTAR.ARCHITECTURE_ADJUDICATION.01` [E] +
`PRIME.SOURCE.RANKONE.UPDATE.IDENTITY.01` [E] +
`PRIME.SOURCE.TENSOR.MECHANISM.01` [O] +
`PRIME.L2.RENYI3.PROVENANCE.01` [O]; the TEN probes embedded
byte-exact in the sealed `--smoke` stage — SPEC SHAs
`3bb365e1`/`ec2bb008`/`d5147850`/`f8d99877`/`fac7a8df`/`6c32f749`/
`6505dd10`/`841b3196`/`92d35a3a`/`5c28b12b` — plus a module-own exact
section S0: the r306 Hill/Lagrange chain with both witnesses and the
Rényi bridge with all constants, the r314 opening-flux lemma
`F₁ == 0` with the exact flux telescope, the collision counting
identity `3p₁p₂ − 2p₃ == 8(n + 3n(n−1))` with the exact factor-8
mutant break (95 vs 760), an r311-class exact rational Farkas
mini-certificate — a PD target in the span with a *forced* negative
generator weight, strictly outside the cone, `⟨Y,Q⟩ = −2` exact —,
the TEN sealed verdict bars as exact decision logic with tipping
mutants at every live clause boundary, and the four-level
composition gate).  **The wave freezes the day in the reviewer's
binding FOUR-LEVEL STRUCTURE**: *Level 1* — real formal theorems
(Lean, already green, NO Lean change ships with the promotion:
`lstar_terminal_implies_master`, the four closed Inertia theorems,
the real PrimeWindow construction, source exactness + mass
conservation of any folding + the strong stabilization form, the
r309 rank-one update identities, the Hill monotonicity + Rényi-3⟹N₂
bridge; sorries 9 → 5, the two TRUE holes stand alone).  *Level 2* —
certified finite statements (Rényi-3 on 57 rungs at `C = 1.069`,
`A = 2`; the fixed-head census 77/77; the block-Green identity +
the strict cone with exact rational Farkas certificates; paired-cone
soundness on 20714 steps; fold multiplicity exactly 2; 93 %
far-triple cancellation; the signed cubic identity with vanishing
boundary term, Fractions-exact; the 21 small-m certificates).
*Level 3* — negative architecture decisions verbatim
(`FIXED_HEAD_DEAD`; `PAIRED_CONE_NO_INDUCTION` +
`PAIRED_CONE_WORLD_BLIND` — B does NOT overtake A; the r308
discriminator = the budget sign / a chordal restatement;
`COEFFICIENT_SIGN_WALL` — Lane A closed as cone language with the
mechanism *named*: block-psd membership without rank-one SDD,
obstructed at the budget/border sign; `FLOQUET_EXPANDING`;
`TRIPLE_TYPE_MAJORANTS_WRONG`; `PHI3_ALL_BLIND`; `TWO_REGIME_DEAD`
with the anatomy — the obstruction family cuts *across* the FCIX
stratum, the r306 first-5 protocol was load-bearing, kz55/kz67 are
near-one-block worlds).  *Level 4* — open mechanisms typed (the
constructive PSD-G rule as a question, the signed cubic flux
theorem, the quantitative source functional, the `crossing_budget`
mathlib gap, the definitional source bridge, L\*, the terminal).
**The claim split is binding and NOT one TRANSFER title**:
`RANKONE.UPDATE.IDENTITY` [E] carries only the exact update
identities (determinant dictionary, Sherman–Morrison chain,
±(η±e_t) border split, local Schur reserve, signed source updates);
`TENSOR.MECHANISM` [O] carries the open question, registered *after*
r313/r316 with the documented negatives.  Universality-class
framing: the base is fine-metric (`METRIC_ONLY`, twin invariance
everywhere), the fiber is recursive (EPSTEIN holds, SCRAMBLE breaks)
— shared algebra, not necessarily a shared mechanism; the reviewer
maturity raise 4 → 5 (formal architecture 9.5) is typed as a
**reviewer assessment**, not a machine-checked fact.  In Lean **no
change ships** with this promotion (r305/r310/r310b are already
merged and green).  NO RH CLAIM.

**Lane status after wave 11.**  **Lane A (block-Green / constructive
PSD-G): CLOSED as a cone language** — r311 `STRICT_SOURCE_CONE`
(exact rational in-span Farkas certificates; the r308 world
separation demarcated as the budget sign) and r312
`COEFFICIENT_SIGN_WALL` with the mechanism named (block-psd
membership without rank-one SDD, obstructed at the budget/border
sign); the PSD-G rule stays open as a *question*.  **Lane B
(paired-cone / rank-one stream): CLOSED, identities banked** — the
r309 B1–B4 adjudication (B does not overtake A) froze the exact
rank-one update identities per reviewer case 3
(`PRIME.SOURCE.RANKONE.UPDATE.IDENTITY.01` [E]); the mechanism
question lives in `PRIME.SOURCE.TENSOR.MECHANISM.01` [O].  **Lane C
(fixed head): PARKED** — `FIXED_HEAD_DEAD` (r307), the one-atom
anatomy is a coordinate, not a dimension.  **The fiber: the r306
Rényi-3 GO stands** (57/57, growing reserve), its **provenance is
open** (`PRIME.L2.RENYI3.PROVENANCE.01` [O]; trilogy: identity exact
(r314), functional blind (r315), two-regime dead (r316)); the
**R317 fork sits with the reviewer** (near-critical family
coordinate OR certified exception family) — r317 executed fork
(b) and sealed `WHAC_A_MOLE(kz53, kz83)`: the spike-family
census is real (B = {kz55, kz67} recovered blind; the F_A top-3
are exactly the near-critical family) but the tail is a
continuum — back to fork (a).  **Lean: 5 sorries, two
TRUE holes** (`lstar_subordination`, `terminal_positive_main`; plus
the `crossing_budget` mathlib gap, the definitional source bridge
and the pair-coordinate refinement).  The mincut (base 4 / refined
5) is unchanged.  NO RH CLAIM.

r318 ran the **indefinite-fork round — the new L\* idea class**
(`indefinite_fork_probe.py`, 25/25, SPEC_SHA `f2d98683`; reviewer
perspective shift after the r312 anatomy — "the signedness itself
is the mathematical object that is not yet understood": ONE
theoretical representation test, Pontryagin/Krein **index** vs
**sign regularity**, under the binding stop rule (both routes
world-blind/restatement ⇒ `FORK_DEAD`, lane stop);
experiments-side, exploration only, no ledger row).  **Verdict
`P2_MAIN_SPECIFIC` (fingerprint)**: the 2.4 % negative cross
mixtures of the converged r308 Dykstra family are **not
structureless** — on MAIN-class worlds the block residual lives
lawfully on the **antiphase pair (D3, D4) with fixed sign −1**
(modal share med 0.699, 12/12 sealed rungs, the r289 rational
twin exact — `METRIC_ONLY` holds), while the dead controls put
their residual on the **arch-mean × border pair (D5, D6)**
(shares 0.953/1.000, d6-class 0.962/1.000 vs MAIN 0.027) — the
fingerprint of the signedness is world-separating **in shape**;
honest caveat typed with the letter: the control fingerprints are
measured on non-psd-feasible 200-step iterates (the r308
non-convergence), labeled ITERATE.  **The P1 index route closes
as language**: the index bookkeeping is exact (spectral count ==
mp pivot count on all seven worlds, window + guarded deep depth;
window index defect 0/0/0 on w9/w13/twin vs 55/37/4/31 on
EPST/SCR/SMOOTH/HL2 — the control flips *are* negative directions
inside the window; ladder 42/42 defect 0), but the index
statement "n₊(window) == N_w" is a total **restatement** of L*
(equivalence with minC ≥ N_w on 3 exact toys + 7 real worlds,
both truth values realized), the global inequality n₊ ≥ N_w is
**vacuous** (carried by the μ-channel majority on every world),
and the negative-subspace invariants are all world-blind (and
not crossing-location proxies — no lever either way).  The SR
half of P2 is an honest negative: no census object is
MAIN-specifically sign-regular (orientation-sensitive minors are
coin-flip ~0.50 even on MAIN) ⇒ the variation-diminishing
implication chain to L* fails at its premise
(`PREMISE_FAILS_ON_MAIN`).  Dig site named per the stop rule: why
the antiphase (D3, D4) cross mixture carries a fixed negative
sign law on MAIN-class worlds.  Protocol disclosures: prefilled
placeholder record tables removed completely before the first run
(the r316 error class); one smoke-stage harness bugfix; one
reporting-only amendment a1 (dig-site label derived from the
measured modal pair).  NO RH CLAIM.

r321 ran **reviewer fork (a) in the r317-sharpened form — the
continuous-coordinate round** (`continuous_coordinate_probe.py`,
39/39, SPEC_SHA `e68883ad`; contract
`PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01`, experiments-side,
exploration only, no ledger row; coexisting with the parallel
r318/r320 rounds).  The statement-shape change the r317 abort
demanded: **bound ρ₂ BY the single source-pure coordinate**
F_A = rank-local QMAX ratio (r317 import, W = 5) — ρ₂(w) ≤
g(F_A(w)) with g explicit and monotone — instead of classifying
by threshold.  Sealed before evaluation: the exact concentration
bracket qmax·ΦH1 ≤ ρ₂ ≤ ΦH1 = (F_A·B)² with the source-pure
baseline B = medloc × m/log m (warded two-sided live on 69
worlds); a three-form monotone g-family with mid-ladder
calibration and derivation-strength precedence (G_SQ = b·F² with
b = (max cal B)², consuming **no target value**; G_TT = c₁ +
c₂·F³, the r317-named heuristic; G_LIN = a·F); a fit-free
upper-envelope rule on the declared test split; gain bar 1.5; a
four-branch verdict tree.  **Verdict `SLIDING_BOUND_GO(G_SQ)`**:
ρ₂ ≤ 1.3056·F_A² pointwise with **0/39 mid-ladder test
violations and all four named r316/r317 violators INSIDE**
(kz53/kz83/kz67/kz55 at reserves 7.0–9.6 — exactly what killed
every flat mid-ladder constant since r316 is absorbed by the
coordinate); reserve min/med 2.71/5.35, trend −0.341 falling;
the test envelope is **strictly monotone in F_A** (bin Spearman
+1.000, top bin 1.0536), bulk Spearman +0.84 — stronger than the
r317 continuum reading; gain 15.95.  Candidate theorem (sliding
cubic bound) printed: Σq³ ≤ 1.3056·F_A(w)²·(log m)²/m² for m ≥
73 + 21 small-m certificates (C_small 1.0694); corollary: F_A ≤
2.47 measured ⇒ uniform C_impl = 7.97 (disclosed 7.5× looser
than the r306 first-5 constant — the round buys FORM, not
sharpness).  Two honest structural finds: (1) the pure-algebra
transfer route does **not** close — B is not bounded by its cal
max (test max 1.4088 = 1.23×, trend +0.122 rising); the G_SQ
certificate holds on the measured ρ₂ directly because the
bracket's qmax slack falls faster than B² rises; (2) SCRAMBLE is
**not** rejected by the coordinate bound alone (F_ins 2.00,
covered at 5.21) — the rejection is carried by the r317 class
side condition (COLL 3.69, shuffle 294/300), honestly typed.
The remaining provenance question is now source-pure, local and
split in two: is F_A bounded (max 2.47), and what bounds the
qmax-share ρ₂/(F_A²·B²)?  NO RH CLAIM.

r322 ran the **antiphase-sign-law round — the dig after the r318
fork decision** (`antiphase_sign_law_probe.py`, 25/25, SPEC_SHA
`761b51d4`; contract `PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01`,
experiments-side, exploration only, no ledger row; coexisting
with the parallel r320/r321 rounds).  The three dig questions:
hardening (is the (D3, D4) sign law of the block-Green
cross-mixture residual iteration/construction-invariant, and
what do *fair* control objects carry — the r318 caveat was that
control fingerprints were ITERATE-grade), the law itself (is it
identity-forced — exact Fractions forced-component analysis of
the linear identity constraints on the (D3, D4) sector), and the
theorem candidate ("psd cone part + antiphase-supported
fixed-sign residual").  **Verdict `ALGORITHM_ARTIFACT`** on the
sealed tree: the law breaks under the sealed random-start
variants — their near-feasible points (staged to 20 000 Dykstra
steps, min eig rel −8.5e-9/−1.2e-9) carry modal pair (0, 2) with
shares 0.31/0.26 and cone share 0.78: **the sign law and the
r312 97.6/2.4 cone anatomy are properties of the
least-norm-proximal Dykstra basin, not of the psd solution set
as a whole** (the canonical variants LSTART/LONG/ZERO/REV all
carry the law exactly and coincide within rel 2e-7 — exactly the
9/15 variant pairs involving the random starts are distinct).
The r318 caveat resolved on fair objects: the least-norm census
reproduces the r318 shape contrast construction-fairly, **but
the budget-ablated converged controls split** — EPST-abl carries
the MAIN law *stronger than MAIN* (share 0.742 vs 0.692), SCR-abl
breaks (0.379) ⇒ `FAIR_CONTROL_CARRIES` 1/2: the r318 pattern
dichotomy does not survive fair convergence.  The law is **not
identity-forced** (TOY4 calibrator machine-exact 4/7; SM1 exact
free fraction 0.477 with *positive* forced value; MINI16
rowspace membership false) — the negative sign law lives
entirely in the selection geometry, as the D3 = −(D2 + 2 D1)
in-block dependence predicted.  Anatomy: total sign consistency
(1.000), position-structured (mid/tail thirds 0.29/0.86/0.93),
scale-stable magnitudes; best coupling correlate: the
block-local antiphase mass pairing (+0.81, below the sealed 0.9
bar).  The candidate form certifies 57/57 rungs + twin censally
but is demoted by the basin finding and the sharpened L5 gap.
Protocol: draft record block removed before the first run; one
amendment a1 (gate typing only, letter identical across passes).
NO RH CLAIM.

**Wave 12 (2026-08-27)** froze the **red-team / fork morning**
(rounds r317–r322, incl. the r319 extraction-chain audit and the
r320 Lean repair) as **`v969_forks_and_redteam.py`** (ledger
`PRIME.REDTEAM.EXTRACTION_AUDIT.01` [E] +
`PRIME.L2.RENYI3.SLIDING_BOUND.01` [O] + updates to
`PRIME.L2.RENYI3.PROVENANCE.01` [O] and
`PRIME.LSTAR.SUBORDINATION.01` [O]; the FOUR probes embedded
byte-exact in the sealed `--smoke` stage — SPEC SHAs
`04fbe5c0` (r317 `exception_families`, 38/38) /
`f2d98683` (r318 `indefinite_fork`, 25/25) /
`e68883ad` (r321 `continuous_coordinate`, 39/39) /
`761b51d4` (r322 `antiphase_sign_law`, 25/25) — plus a module-own
exact section S0: the exact two-sided concentration bracket
`qmax·ΦH1 ≤ ρ₂ ≤ ΦH1` re-proved from scratch with both mutant
directions caught, the U1–U3 red-team witnesses in exact
arithmetic (U1: the `B = −1` window against the terminal type;
U2: the mesh-level-0 total node collision reduced to three
rational facts about `e` on the certified bracket
`685/252 ≤ e ≤ 685/252 + 1/35280`, kill `0 < 0` exact; U3: the
adversary `(|F|+1)² < 5/7` false for every F), the r320
separation-discipline and canonical-split certificates (witness
mesh level 4 via `2⁷ < 3⁵ < 2⁸`, reduction `1/8 < 2/5` exact;
level-0 failure `4/3 < 4`), six sealed verdict bars with tipping
mutants, and the wave-12 composition gate; NO Lean call — the
r319/r320 Lean rounds are consumed as REPORTS, their artifacts in
`rh/lean/` re-verified by `lake build` + `run_rh.py`).  **The wave
adopts the reviewer's binding adjudication**: *(1)* the proof
graph has **three cleanly separated levels**, and the two true
holes are named **WINDOW-LOCAL** on every surface from now on —
**Level A** (local window mathematics, PROVED:
`L*(w) + T(w) ⟹ MasterPositive(w)`, cleanly typed per r305/r320;
"for every canonical finite window, L\* and terminal positivity
imply augmented prefix positivity — this is a window-local
theorem"), **Level B** (the universal window family — THE two
arithmetic *window-local* holes: `∀ w ∈ W_canonical: L*(w) ∧
T(w)`), **Level C** (extraction to Weil/RH, OPEN: source-exact
realization of the actual source + admissible transport +
convergence/stabilization in the correct directed order +
density/continuity for the Weil criterion).  *(2)* **The false
cofinality direction is documented, not solved** — and the sorry
census does **not** fully measure the global distance: the missing
Level-C extraction architecture appears in *no* `sorry`, because
the correct theorem statements do not yet exist.  *(3)*
`SourceExact` is a good firewall but must **not** stand as a free
assumption in a final proof — the named open Lean target is the
target architecture **`CanonicalPrimeWindow` + exactly one
construction theorem `sourceExact_buildPrimeWindow`**
(load-bearing for the global connection, not formalization
polish).  *(4)* the typed per-layer **reviewer assessment**
(supersedes the wave-11 4 → 5 scalar; an assessment, not a
machine-checked fact): finite dictionaries 9.5/10, formal
window-local architecture 9/10, terminal mechanism 6/10, L\*
mechanism 2/10, source/extraction architecture 2–3/10, complete
RH proof path ~3/10, audit quality 9/10 — *"stronger as a
window-local research program; as a complete RH proof chain
currently less far than previously assumed — the removal of a
shortcut that did not exist."*  NO RH CLAIM.

**Lane status after wave 12.**  **L\*: internally PAUSED**
(allocation 0 %, reviewer decision; the selection geometry is not
pursued further — the r322 `ALGORITHM_ARTIFACT` closed the
antiphase fingerprint as a Dykstra-basin property; reopening only
under the six documented conditions of the r322 round notes; as an
*external* object the two-weights sampling formulation
`‖J_N‖ < 1` stays the memo candidate, `rh/problem/`).  **The
terminal: sharpened to the QMAX × M₂ shape route** (the sliding
bound's two-part demand: is F_A bounded / what bounds the
qmax-share; **round R324 in flight — not consumed here**).  **The
extraction layer: the repair fork R325 measured** (primary verdict
`ELEMENTWISE_STABILIZATION_GO` — the repair is a quantifier set,
not a new mesh theory; see the r325 paragraph below; the Level-C
target `CanonicalPrimeWindow` + `sourceExact_buildPrimeWindow`
stays the named open Lean goal).  **The fiber: the sliding cubic bound stands as
the successor contract** (`PRIME.L2.RENYI3.SLIDING_BOUND.01` [O];
`Σq³ ≤ 1.3056·F_A²·(log m)²/m²` on the measured rungs, all four
named violators inside; C_impl 7.97 disclosed 7.5× looser — form,
not sharpness).  **The base fork: closed honestly** (r318 P1
banked as language — a total restatement, no lever; classical sign
regularity dead on MAIN).  **Lean: 5 sorries, the two true
WINDOW-LOCAL holes** (`lstar_subordination`,
`terminal_positive_main` — Level B; plus the `crossing_budget`
mathlib gap, the definitional source bridge and the
pair-coordinate refinement; census 5 → 5 across the r320 repair
with two typed retypes).  The mincut (base 4 / refined 5) is
unchanged.  NO RH CLAIM.

r324 ran the **QMAX × M₂ origin round — the reviewer-sharpened
terminal main lane after the r321 sliding-bound GO**
(`qmax_m2_origin_probe.py`, 36/36, SPEC_SHA `dc36cacb`; contract
`PRIME.L2.RENYI3.QMAX_M2_ORIGIN.01`, experiments-side, exploration
only, no ledger row; coexisting with the parallel wave-12 worker
and R325).  **Binding course correction mid-round, disclosed**: the
round's original F_A-provenance contract was executed and sealed
first (`fa_provenance_probe.py`, 36/36, SPEC_SHA `9a6696f8`,
r324-pre in the inventory — letters `FA_BOUNDED_DISTRIBUTIONAL` +
`QMAX_SHARE_OPEN`), then the reviewer adjudication demoted the
F_A-boundedness hunt as a potentially unnecessarily strong
statement — for the needed power N₂ ≳ m^0.888 it suffices that
F_A·log m = O(m^{0.112−ε}); the cleaner decomposition is
**QMAX × M₂**; the banked pre-work is reproduced bit-near as
anchors.  **S0 (exact)**: the interpolation `M₃ ≤ q_max·M₂` and
`M₂ ≤ q_max` (Fractions-proved, live-warded at slack 0.0), and the
identity `F_A·B·log m == m·q_max` (2.7e-16) — F_A is the rank-local
normalization of m·q_max, no black correction factor; the r321
bracket upper is improved by exactly the factor M₂/q_max ≤ 1.
**S1 (M₂ export)**: the pointwise export `m·M₂ ≤ C₂ = 2.2557`
(mid-ladder freeze) **fails 7/39** exactly on the banked violator
set (kz53/kz67/kz83 at 3.05–3.19) — the reviewer's "export should
carry" expectation is refuted pointwise (trend +0.014 flat,
envelope 3.1938; the distributional r302 export holds, KS
0.0230/0.0158).  **S2 (the multiscale pileup hypothesis, four
measurements)**: scale recomposition exact (2.2e-16); fold
multiplicity ≤ 2 on all 69 live worlds; per-scale mass C_PIL
9.3583 **fails 11/39** (clause refuted); active scales
nsc_rel/log m ≤ 2.026 **holds 0/39** (the O(log m) scale count
certifies); direct C_INF 1.7481 fails 5/39.  **Hardness census
answered**: the named near-critical spikes are *not* multiscale
convergence — one near-maximal source scale dominates the argmax
block (kz67 s0 = 22.4 of G 13.6; nsc at the ladder median): the
pileup tip is a **single heavy scale** — the reviewer hypothesis
refuted in clause (3), confirmed in clause (4).  **Verdict
`PILEUP_GROWS_SUBCRITICAL(+0.172)`** on the sealed six-letter
tree: e(G/log m) +0.158 + e(m·M₂) +0.014 = +0.172 < CRIT 0.224,
stability halves +0.141/−0.160 both subcritical — decided; by the
reviewer contract a sufficient first-class outcome.  **S3
composition (typed MEASURED)**: Σq³ ≤ 8.941·(log m)·m^{+0.172}/m²
⟹ N₂ ≥ N₃ ≥ m^{0.914}/√(8.941·log m) ⟹ N₂ ≥ m^0.888 for all
m ≥ m₀\* = 10^59.6; the measured ladder ends at m = 274 — the gap
is the disclosed extrapolation hypothesis, no cofinal claim.
Protocol: course correction documented in the docstring; the
banked pre-work outcomes disclosed pre-spec; one calibration-pass
solver fix before the record freeze (m₀\* search moved to log
space, sealed rule unchanged); deterministic run1/run2.  NO RH
CLAIM.

r325 ran the **extraction-repair fork — the new main strand after
the R319 red team** (`extraction_order_probe.py`, 18/18, SPEC_SHA
`31277f91` final with record / freeze-run `57e50d36`; contract
`PRIME.EXTRACTION.ORDER_REPAIR_FORK.01`, experiments-side,
exploration only, no ledger row; coexisting with the parallel
wave-12 worker and R324).  The round is mixed analytic + machine:
the three reviewer variants for repairing the RH-connection seam
(elementwise stabilization vs. canonical mesh rebuild vs. explicit
quadrature correction) were adjudicated on their machine-checkable
halves under a sealed tree.  **Verdict: primary
`ELEMENTWISE_STABILIZATION_GO`, co-letters
`CANONICAL_MESH_REBUILD_GO` +
`SIGNED_DEFECT_CORRECTION_GO(SIGN)` +
`ANCHOR_ONLY_INSUFFICIENT`.**  *(A)* On the native dense class
(dyadic step-function autocorrelations — the v749 "Weil form of
step functions" class, seed-sealed) **all three channels**
(comb/arch/pole) of the canonical tower windows stabilize
**exactly** at the predicted finite anchor onset α\* =
(n_g+1)·D₀/2 (comb rel dev 0.0/3.3e-18 above onset, 2.7e-2–5.3e-2
below — a real onset) and the value is **constant under dyadic
mesh refinement** (comb 3.3e-18, arch 1.5e-15, pole 2.0e-17): the
elementwise architecture consumes **no mesh-cofinal ladder and no
transport** — the R310 `finite_forms_converge_to_weil` shape
generalizes from the Lean comb channel to every channel on the
native class (derived tent-read identity `L_cat(F) = −Σ μₙ
(I_D F)(uₙ)` gated at 1e-12).  *(B)* v749 T1.4b reproduced: every
deployed frame-A window **is** a directly rebuilt tower member at
rel dev 0.0; the rebuild ladder is PD per stage with honestly
falling margins (λ_min/c₀ 1.33e-5 → 6.92e-7, reported not
consumed); the dyadic transport identity holds at 8.0e-17 but
variant B never uses it.  *(C)* On the sealed non-native C² class
the per-channel quadrature defect is **one-signed** (comb
negative, arch positive, pole positive, all stages), falls at the
D² class rate per channel (ratios 3.6–9.0; the *total* ratio
2.2–3.3 is reported only — comb/arch sign opposition cancels
there), and sits inside the **rigorous closed-form interpolation
envelope** |E_ch| ≤ (D²/8)‖F″‖·K_ch — controlled on its own, no
wall margin anywhere; the anchor-only floor is real (E_tot
constant +1.77e-4/+1.59e-4 across the anchor sweep at fixed mesh —
the R319 false-floor mechanism on this probe's own elements).
Fork consequence (analytic deliverable of the round): the repair
statement for the next Lean round is the **elementwise quantifier
set** — `CanonicalPrimeWindow = {w | ∃ a h, w = build(a, h)}` with
exactly one construction theorem, per-element predefined finite
stabilization on the native class, and the window-local positivity
premise quantified over the canonical family; **no new mesh theory
and no H_cof ladder**.  The mesh limit survives only as the
classical density/continuity step (the v912 topology caveat),
quantified by leg C.  Nothing here proves any window positivity or
any local lemma.  NO RH CLAIM.

r327 ran the **fold-group mass-cap round — the r324 follow-up on
the terminal main lane** (`group_mass_cap_probe.py`, 34/34,
SPEC_SHA `11e4fd40` final with record / freeze `71f8b7b4`;
contract `PRIME.L2.RENYI3.GROUP_MASS_CAP.01`, experiments-side,
exploration only, no ledger row; coexisting with the parallel
r326 Lean round).  The r324 hardness census had located the
near-critical spikes in a *single heavy source scale*; this round
descends one level: **what caps the mass of the dominant fold
group?**  New exact machinery (warded live on 69 worlds at slack
0.0): the per-group mass ledger on the identical r314 fold
segmentation, the partition `Σ_g gabs == A1_j`, the L1
recomposition, the **two-ancestor bound** `gabs ≤ mult·gmax ≤
2·vmax` (the proven mult-2 cap as a mass statement) and the exact
cap chain `m·q_max ≤ ng·hgn`.  **Q1 anatomy answered — sealed
letter `SOURCE`** (med named ratio 1.057 ≥ 0.5): the r324 heavy
scale *is* a single fold group at the two sharpest spikes, and the
structural finding of the round: on **all 65 rungs** the heaviest
group of the argmax block is **exactly one β/ω fold pair** (one
bulk + one window atom at one position; window-atom histogram
[0, 65, 0]) with median alignment 1.000 — the two ancestors
reinforce; at kz53 the single pair carries 88.8 % of the argmax
block's atom mass (second group 13× lighter): the spike is
literally **one bulk/window coincidence** (kz67 is the exception
shape: 6 groups, bshare 0.416).  **Q2 caps — verdict
`CAP_PARTIAL`** on the sealed six-letter tree: the λ-pair route
`hga ≤ 2·vmaxb` is exact but the source-size coordinate
`2·m·vmaxb/L` **fails the mid-ladder freeze 19/39** (C_LV 1.1838;
kz55 6.85 / kz53 5.77, named 0/4) — the von-Mangoldt size analogy
does not close as a polylog cap; the direct group cap fails at
A = 1 (18/39) and A = 2 (8/39); **the group count certifies**:
`ng(argmax block) ≤ 2.6351·log m` at 0/39 + named 4/4 — the third
certified O(log m) count of the lane.  Exponents: e(hgn/log m)
**−0.200 falling**, e(lvb/log m) −0.261 falling (the heavy-group
coordinate decays with depth — the spike set is a shallow/mid
phenomenon, not growth), e_route +0.106 < 0.224 but halves
+0.411/−1.183 straddle — `HEAVY_GROUP_UNBOUNDED` does **not**
fire.  **Q3**: no certifying cap ⟹ the r324 MEASURED composition
stands unchanged (m₀\* = 10^59.6); slim anchors bit-near (r306 /
r316 / r324 C_NSC 2.0258 · C_PIL 9.3583 · C_INF 1.7481 with
violation counts 0/11/5 exact / r324-pre C_M2 + seven-violator
set exact).  Must-fails e1 group-drop LOUD / e2 wrong-window-max
exact / e3 cap-posthoc AST+toy / e4 qmax-readback AST all CAUGHT.
Deterministic run1/run2; no amendment before or after the freeze
except the record-table insertion.  NO RH CLAIM.

**Wave 13 (2026-08-27)** froze the **extraction repair and the
terminal composition** (rounds r323–r327, incl. the r326 Lean round
and the r323 clean abort) as
**`v970_extraction_and_composition.py`** (ledger
`PRIME.EXTRACTION.ELEMENTWISE.01` [E] +
`PRIME.L2.RENYI3.MEASURED_COMPOSITION.01` [O] + updates to
`PRIME.L2.RENYI3.SLIDING_BOUND.01` [O],
`PRIME.L2.RENYI3.PROVENANCE.01` [O],
`PRIME.REDTEAM.EXTRACTION_AUDIT.01` [E, Lean note] and
`PRIME.LSTAR.SUBORDINATION.01` [O, Lean note]; the FOUR probes
embedded byte-exact in the sealed `--smoke` stage — SPEC SHAs
`9a6696f8` (r324-pre `fa_provenance`, 36/36 — banked) /
`dc36cacb` (r324 `qmax_m2_origin`, 36/36) /
`31277f91` (r325 `extraction_order`, 18/18) /
`11e4fd40` (r327 `group_mass_cap`, 34/34); r324 imports the
embedded r324-pre, r327 the embedded r324-pre AND r324 — plus a
module-own exact section S0: the r324 interpolation
`M₃ ≤ q_max·M₂` with slack exactly 1/36 and double equality at the
flat profile, the F_A identity `F_A·B·log m == m·q_max` as exact
constructional algebra (gauge mutant caught), the r327 group
ledger (partition, cap chain 12/7 ≤ 20/7, two-ancestor bound with
both mutants breaking by exactly 1), the r325 onset formula
`α* = (n_g+1)·D₀/2` as an **exact toy stabilization** (read ==
atom sum 35/16 for every α ≥ 5/8, constant under mesh refinement,
nearest-neighbour mutant caught), the m₀\* log-space solver
rebuilt verbatim (landing 10^59.6; the disclosed pre-freeze
linear-space bug rebuilt and caught), the r328B chain-audit gate
S0-T5d (block-level need 454/501, chain bar 0.188, verdict
survival 0.172 < 0.188 exact, chain-honest m₀\* = 10^238, the
false-fire window mutant caught), six sealed verdict bars with
tipping mutants, and the wave-13 composition gate; NO Lean call —
the r326 Lean round is consumed as a REPORT and the r323 abort as
a NOTE).  **The honest formulation of the new connection (binding,
verbatim)**: *two window-local lemmata (over the canonical family)
+ the elementwise architecture + cited classics (density, v912
continuity, the Weil criterion) ⟹ RH; open links: the arch/pole
transcription (classical), the compression bridge, the source
completion (definitional).*  NO RH CLAIM.

**The adversarial audits (r328A/B/C, read-only).**  Three
independent adversarial audits ran on the wave-13 state on the
same day; reports are with the coordinator (the full booking goes
into `next.txt` by the coordinator).  **A (methodology)**: no
verdict-tipping bug; a verifiability gap and a sequence-distortion
risk named.  **B (chains)**: found the one MODERATE transcription
error of the wave — the r324 composition bar CRIT = 0.224 was
derived from the ATOM-level need 0.888, while the composition
functional N₂ = n_eff is BLOCK-level (need 0.908 in N units,
908/1002 ≈ 0.9062 in m units), so **the chain-honest bar is
CRIT = 0.188 and the chain-honest m₀\* is 10^238** (the record
10^59.6 belonged to the atom-level need).  **The r324 verdict
SURVIVES** (+0.172 < 0.188); the sealed record is NOT edited — the
correction is carried as a chain annotation (ledger, the v970 gate
S0-T5d, the rh-paper S3′ item) and the going-forward bar is 0.188.
Otherwise clean, incl. two independent recomputations.  **C (blind
spots)**: the ladder selection effect, the twin resolution limit
and the missing second living world named.

**The EXT3 fresh anchors (r329, audit repairs 2+3 of r328A/C).**
`ext3_fresh_anchors_probe.py` (33/33, SPEC_SHA `bbfaf1990bd37061`,
under the two-commit freeze protocol: pre-freeze `604b8aaf`, record
`8cbd95f9`) repaired the sequence bias of the r321/r324 lane: 12
genuinely NEW windows (machine-checked disjoint from the 80-kz used
ledger of every prior round, all deeper than every prior window,
N_w 1721..2577), built with the IDENTICAL frame-A construction and
only the anchor CHOICE changed — 6 deliberately SMALL-GAP anchors
inside the core zone range (grel 0.28..0.53 vs ladder median 1.32;
the ladder is large-gap selected by construction, audit C1) + the 6
deepest fresh windows — tested pointwise against the four FROZEN
constants, nothing recalibrated.  **Verdict `EXT3_VIOLATIONS` +
`SMALL_GAP_DIFFERENT`(ρ₂ med ×10.29, F_A med ×3.21)**: the r306
uniform constant C = 1.069 BREAKS on the four sharpest small-gap
anchors (kz51 by 7.1×) — it is a large-gap-family statement; the
r321 sliding bound 1.3056·F_A² covers exactly those spikes with
reserves 5.0–6.1 at the frozen constant (the coordinate carries
genuine out-of-sample evidence) but misses four QUIET anchors
(F_A 0.27–0.39, excess ≤ 1.40×, convention-sensitive: inside under
the insertion rule) — the named successor question is a floor term
below the ladder's sampled F_A range; the two O(log m) counting
constants C_NSC 2.0258 and C_NG 2.6351 HOLD 12/12 (min reserves
1.6/1.8) — the counting side is the lane's most choice-robust
asset.  Four stratum-A candidates were the first POSITIVE_PREFIX
failures ever seen on this construction.  Experiments-side, NO
ledger row, NO RH CLAIM.

**The second living world (r330, audit repair 4 of r328C).**
`dirichlet_secondworld_probe.py` (24/24, SPEC_SHA `665260180de9`,
the first round under the two-commit freeze protocol: pre-freeze
`2b1b69ce`, record `4f2e4f52`) built the missing POSITIVE control —
a Dirichlet-L comb (primitive real χ mod 3; weights `χ(n)·MU_ALL`
bitwise in the v563 gauge, plus the milder magnitude variant
DIRICHLET_ABS without the p = 3 atoms) through the IDENTICAL frozen
machinery on the identical 42-rung ladder, nothing recalibrated.
**Verdict `SECOND_WORLD_SPLITS`** along a clean wall/cascade seam:
SHARED (genuine living-world properties, now n = 2 living
arithmetics vs 2 dead controls) = the r300 FILL class (med 0.436
FILL_LOW vs EPST/SCR FILL_HIGH), the n_eff growth direction
(+0.527) and the mult-2 one-pair fold geometry (42/42, mixed share
1.00); SPLIT (retyped as zeta-side idiosyncrasies INSIDE THIS
FRAME) = the half-filling wall itself (DIR nf None 0/42, depth
ratio med 0.080 — and sharpest: ABS, the mere REMOVAL of the three
p = 3 atoms, already kills the wall at control depth 37 at w9),
the r306 pointwise C₂ bound (32/42 violations, max 27.6×), the
σ decay (the diagonal GROWS, +0.793) and the r299 O-sign class
(O_NEG 27/42).  HONEST LIMIT (binding): the frame keeps zeta's
archimedean term/border/depth — the round cannot distinguish
"wall is zeta-specific" from "wall needs the matched
Γ/conductor frame"; the GRH-faithful Dirichlet window is the named
follow-up.  Experiments-side, NO ledger row, NO RH CLAIM.

**The twin resolution (r331, audit repair 5 of r328C).**
`twin_resolution_probe.py` (24/24, SPEC_SHA `f871fe84acdc0526`
final with record, freeze `8d771fae0a374fa8`, two-commit protocol:
pre-freeze `b8319121`, record `a45d4560`; seed-free deterministic)
measured the METRIC_ONLY reach the audit flagged as possibly
untested: is the r289 rational twin resolution-capable at the
r286 tight anchors (margins down to 1.8e-8), or is its own
construction disturbance larger than the margin there?  **Verdict
`METRIC_ONLY_CONFIRMED_AT_RESOLUTION` (margins 1.675e-4 ..
1.806e-8 over 11 anchors)**: at the r289 precision (1e-8 of the
local gap) the twin footprint `|Δ margin|` lands **3.4+ orders
below EVERY margin** (11/11 RESOLVE, worst ratio 3.7e-4 at kz98,
mp dps-30/45 pair-verified on every sub-1e-5 margin) — the feared
blindness does not occur, because the margin responds to the
rationalization far more weakly than 1:1 in gap units; the
precision sweep (1e-3/1e-6/1e-8/1e-10 on kz9/64/98/119) shows the
twin is BLIND at 1e-3 everywhere (signature broken) and
twin-stable from **t\* = 1e-6** down on all four anchors (kz98
the closest call at ratio 9.9e-2); the genuine diophantine
counter-test (golden-ratio detune, weights bitwise, gap structure
preserved ≤ 1e-4, the 28 exact w9 2-power resonances demonstrably
destroyed 28 → 0) **keeps the wall at every resolving dose** on
w9 AND on the tightest anchor kz119 (Δ +4.7e-11 at margin
1.8e-8) — METRIC_ONLY doubly confirmed, now WITH a resolution
certificate on the tight range instead of an untested
extrapolation.  Honest limits: the f64 construction floor caps
twin precision at ~1e-10 gap (floor censuses disclosed);
near-resonance structure untested; 11 anchors × 4 tolerances is
a finite census, not a family theorem.  Experiments-side, NO
ledger row, NO RH CLAIM.

**The β/ω companion-orbit packing (r333, reviewer rank 1 after the
r327 carrier).**  `companion_orbit_packing_probe.py` (34/34,
SPEC_SHA `02b22672e1c3f91d` final with record, freeze
`5567af41c0d4bc82`, two-commit protocol: pre-freeze `279ba0dd`,
record `55d4a832`) implemented the reviewer's packing theorem
candidate: to every dominant β/ω pair g\* a companion set O(g\*)
constructed CANONICALLY from its source data (same dyadic gmax bin
+ same fold parity + the maximal inner interval, BOUNDARY_F 0.10 —
NOT a similarity search, the e4 mutant proves it), with clauses
(T1) |O| ≥ c₀·m/(log m)^a, (T2) weight comparability, (T3)
overlap ≤ 2.  **Verdict `ORBIT_TOO_SHORT`**, with TWO
theorem-grade positives and ONE structural discovery: (T2) the
BAND DISCIPLINE certifies EXACTLY — inside one dyadic gmax bin the
two-ancestor bound forces `1/4 < gabs(g)/gabs(g') < 4` (derived
algebra, sharp near 1/4; live rmin worst 0.2819, cband worst 3.55
on 69 worlds): b = 0, c₁ = 1/4, the r327 λ-pair failure repaired
at band level; (T3) overlap is partition-exact (membership 1 ≤ 2);
the composed chain `q_max ≤ ng·κ/(|O|·rmin)` is exact live (κ =
L1_atom/L a stable ~3–4 factor, NOT the blocker).  But T1 fails at
all a ∈ (0,1,2) and the composed bound fails pointwise (named
coverage 0/4), because THE BOUNDARY CASE IS THE RULE: on 44/65
rungs the dominant pair sits in the outer 10 % margin of the
masked support (d\* med 0.072, min 0.002); the inner-interval
orbit is EMPTY at kz53/kz83/kz55 (|O| = 0; kz67: 2) while the
one-sided census shows same-key companions DO exist on the edge
side (1 each at the spikes, up to 25 elsewhere) — the spike
coincidence is an EDGE phenomenon; all four named spikes are
SMALL_ORBIT + HEAVY_BAND simultaneously.  Subcritical fallback
UNDECIDED (δ = e(hgn) = −0.004 < 0.112 but halves +0.148/+0.674
straddle).  Worlds: twin identical protocol; EPSTEIN different
band structure (10 vs 13 bins) with live orbit; SCRAMBLE orbit
DECAYS (|O| = 0) as predicted.  Named successor: the ONE-SIDED
edge companion construction (the boundary case as the main case)
or the martingale second route; the r324 MEASURED composition
stays the honest end state.  EXT3 anchors not adopted (r329
record uncommitted at spec time, disclosed).  Experiments-side,
NO ledger row, NO RH CLAIM.

**The L\* capacity fork (r334, reviewer rank 2 — the new L\*
language).**  `fold_capacity_probe.py` (26/26, SPEC_SHA
`d5698a1d2d9c96c3` final with record, two-commit protocol:
pre-freeze `67833ecf`, record `9bf3a0aa`) reopened L\* under the
Fold-Capacity-Packing reading: the polynomial capacity
`Cap_{μ,N}(E) = inf{∫p²dμ : deg p < N, |p| ≥ 1 on E}`, the exact
level-set formula, and the chain (K1) `ν(E) ≤ κ·Cap(E)` + (K2)
layer-cake `≤ C_lev·∫p²dμ` + (K3) `κ·C_lev < 1 ⟹ L*`.  The
machinery is certified (dual active-set solver with KKT
certificate on all 138 723 solves, exact-Fraction enumeration
route to 6.8e-16, point capacity == inverse Christoffel against
the r284 route to 9.7e-16, mp dps-40 wards).  **Verdict
`ALLSET_NEEDED` + `WORLD_SEEN` + `CAPACITY_CONTENT`** (the
restatement rule does not fire, on two clauses): the small exact
all-subset census (4 instances, S ≤ 16, `Cap_abs` by full sign
enumeration) shows the supremum is NOT uniformly
interval-carried (I4: an outermost symmetric two-component pair
wins, ratio 0.7013) and not uniformly the λ shadow (κ_all/λ down
to 0.8504); on w9 the interval clause is carried by the r284
SHALLOW-EDGE PAIR (folds 2/4) at κ_int = 0.999567 — a new
source-pure near-wall coordinate whose margin 1 − κ_int (2.6×
the spectral margin on w9) shrinks along the ladder at the same
locus; the K3 products 0.90..1.06 straddle 1 across the live
rungs (no reserve), and the gate-side structural ceiling is
explicit: the extremal direction's own chain gives
κ·C_lev = 1.0085 ≥ λ_max, so NO (K1, K2) pair valid for all
polynomials can put the product below λ_max — the capacity route
cannot out-margin the spectrum.  Honest content: the interval
clause is a sharp world DISCRIMINATOR (EPST κ_int 1794, SCR
8.5e6 — both dead worlds shout κ > 1 through intervals alone,
which certifies λ > 1 exactly; MAIN/TWIN < 1 everywhere,
twin-stable to 5.5e-9).  Experiments-side, NO ledger row, NO RH
CLAIM.

**The one-sided edge packing (r335, the edge form after the r333
structural finding).**  `edge_packing_dichotomy_probe.py` (36/36,
SPEC_SHA `950c9b9ee96298e0` final with record, freeze
`a1f4c0dd97edcbf4`, two-commit protocol: pre-freeze `ec0fd5d5`,
record `3fa88d02`) tested whether the one-sided edge-companion
construction carries: for every dominant β/ω pair a ONE-SIDED
orbit O_e (same key, window from ps toward the interior, reach =
the masked support radius W/2, parameter-free a-priori) plus the
margin mass census, combined into the exact dichotomy
`q_max ≤ min(Q_e, M_b)` with `Q_e = ng·κ/(|O_e|·rmin_e)` and
`M_b = ng·κ·S_marg/L1` — EITHER many companions OR small edge
mass; EXT3 = the 12 r329 record anchors adopted as pure test rows
(committed `8cbd95f9`).  **Verdict `EDGE_ORBIT_ALSO_SHORT`** — no
clause certifies (T1-edge viol 43/40/38 of 51 at a = 0/1/2, named
0/4; dichotomy C_D 141.84/33.06/7.71 viol 14/11/6) — but with two
structural findings: (1) **the spikes flip to COVERED** — the MASS
arm covers all four named rungs at every a (kz53 B^D_1 12.51 /
kz83 20.47 / kz67 2.62 / kz55 11.86 vs C_D(1) 33.06, reserves
1.6×–12.6×): the r333 spike blocker is resolved pointwise at the
named rungs by the edge-mass clause; what violates now is the
mid-band family (kz73/76/61 + deep kz95/98/109, margin share
0.18–0.28, both arms 6–10); (2) **the inward window misses the
edge companions** — at the spikes |O_e| = 1 (g\* alone; 6
inner-empty rungs gained 0): the r333 one-sided same-key
companions sit OUTWARD of g\* (between the support edge and ps),
so T1 in the inward one-sided form fails harder than the
two-sided T1 and the spike coverage comes entirely from the mass
arm.  T2/T3 stay theorem grade on the edge orbit (rmin_e worst
0.3162 > 1/4, cband_e worst 3.1630 < 4 on 81 live worlds;
membership 1 ≤ 2); both arms and the arm partition are exact live
(arm census O 15 / M 62 of 77 — the mass arm is the rule); δ =
e(hgn) = −0.004 with halves +0.148/+0.674 straddling (exact r333
continuity).  Worlds: twin identical protocol; EPSTEIN operates;
SCRAMBLE |O_e| = 2 vs inner 0 — the one-sided orbit does NOT
decay on SCRAMBLE (honest negative: the support-radius reach is
permissive).  Named successor: the packing language is exhausted
at the edge — the reviewer's martingale second route (named only,
not executed); the r324 MEASURED composition stays the honest end
state.  Experiments-side, NO ledger row, NO RH CLAIM.

**The Chebyshev T+H parity section (r336, reviewer rank 3 — the
last pre-authorized L\* arm).**  `lstar_parity_section_probe.py`
(25/25, SPEC_SHA `9e4bf4f129405a64` final with record, two-commit
protocol: pre-freeze `d38b43c1`) put the parity-section language to
its three kill tests.  The exact coordinate stands: with the signed
cosine moments `c_r = Σ(μ_j − ν_j)cos(rθ_j)` on the affinely
mapped hull, `∫p²d(μ−ν) = Σ a_k a_l (c_{|k−l|} + c_{k+l})/2`
EXACTLY (bit-equal in Fractions on the rational toy; 2.2e-15 on
w9; ≤ 5.9e-15 on the ladder sample) — **the L\* matrix is a finite
Toeplitz+Hankel parity section**, congruent by the exact rational
congruence `M = S·V₊ᵀT_M(c)·V₊·S` to the EVEN parity compression
of the full symmetric Toeplitz section (the mirror of the
v549/v550 odd-sector step-over machinery); section flip at f64
signs clean (+5.7e-8 at 184 / −1.2e-8 at 185, negative inertia
exactly 1).  **Verdict `PARITY_FINITESECTION_CARRIER` +
`NEGATIVE_WINDOW_STEP_OVER(ii)` + `PARITY_WORLD_BLIND` +
`PREDICTOR_ORDERING`** — kill test 1 CARRIES (the symbol attains
−5.07 in 127 negative zones, total measure 0.2766 π, while the
184-section is PD: the positivity is a genuine finite-section
effect, and the Fejér mean is positive on all 183 active parity
modes of MAIN and TWIN while 34 Dirichlet readings sit in Gibbs
zones — clause (ii) steps over, exactly the T151 template); kill
test 2 FAILS (all four sealed statistics world-blind under the
r281 rule; the near-separation — Fejér floor positive on
MAIN/TWIN, negative on EPST/SCR/HL2 — is broken by SMOOTH, a dead
world with positive Fejér floor: its death is not a
local-negative-mass event); kill test 3 PARTIAL (the blind
Fejér predictor lands in the 1-octave band on 42/42 rungs, max
dev 0.224, spearman +0.999, but only 1/4 controls — no law).
The honest central negative: the w9 Fejér floor does NOT dip at
the crossing (+2.16e-3 at 184, +1.99e-3 at 185) — the L\* flip is
not a local-mass event at Fejér resolution; it lives in the
sharper two-atom extremal of r284.  Banked: the Fejér floor as a
SECOND source-pure near-wall coordinate (positive with empty
Schur block on 42/42 rungs, min +4.44e-4; falls ~5× along the
ladder where 1 − κ_int falls ~50× — not the same number in
disguise).  With kill test 2 failed and kill test 3 partial, the
reviewer's own rule reads: the parity-section lane does NOT stay
open as an L\* proof arm; the exact T+H coordinate (C1) is
banked.  Experiments-side, NO ledger row, NO RH CLAIM.

**The fold-martingale second route (r337, the reviewer's
pre-named terminal route after the exhaustion of the packing
language).**  `fold_martingale_probe.py` (37/37, SPEC_SHA
`617a83a6b3105acb` final with record, freeze `5460c2fa54983956`,
two-commit protocol: pre-freeze `30ac0cb5`, record `d0d272e3`)
read the signed fold-group masses of the argmax block as an
adapted process along the SEALED dyadic source-scale filtration
(adjudicated a-priori before the freeze: parameter-free /
theorem-adjacent / canonical coarse-to-fine; a protocol mutant
proves the audit bites), with three exact wards live — the
telescope `X_K == x_{j*}`, Cauchy–Schwarz `zr ≤ √n_act`, and the
identity `q_max = zr·κ·√V/L1`.  **Verdict
`MARTINGALE_STRUCTURE_ONLY`** — the structure is there: the
Z-maximal certification carries at the Azuma form `zr ≤
C_Z(1)·√(log m)` with C_Z(1) = 0.7364 and **0 test violations of
51 (incl. all 12 EXT3), named 4/4** — but the derived maximal
arm `A_z = C_Z·√(log m)·κ·√V/L1` fails pointwise at every a
(viol 18/13/11), so no new m₀\*.  Three structural findings:
(1) the certification is tight but nearly structureless — c\*
med 0.949 (ONE increment dominates the quadratic variation: the
r324 single-heavy-scale finding recurs in signed form), zr med
1.1012 essentially flat, contraction median exactly 0.500;
(2) **the r335 mid-band blocker dissolves** under the martingale
arm — head-to-head at a = 1: kz73 B^D_1 54.40 → B^C_1 0.399,
kz76 53.59 → 0.483, kz61 48.91 → 0.755, kz95 41.96 → 0.352,
kz98 41.68 → 0.400, kz109 40.90 → 0.299 vs C_C(1) 0.5293
(coverage 5/6, improvement 70×–180×; pointwise q_max ≤ A_z on
77/77 rungs); (3) the violation margin **migrates to the deep
anchors and the spikes** — A_z undercuts the mass arm everywhere
(letters A 77 / M 0), the freeze collapses 33.06 → 0.5293, and
the new a = 1 violators are EXT3 kz51/62/54/123/125 (up to
3.95×) plus named kz53/kz67/kz83 (≤ 2×): the r335 mass-arm spike
coverage is lost inside the min (a two-constant certification,
each arm against its own freeze, was not this round's sealed
contract — named residual direction only).  Measured route
growth e(B^C_1) = +0.059 vs the r324 chain's +0.172 (3× flatter,
but the pointwise certification fails).  Worlds: SCRAMBLE zr
1.1159 / contr 0.500 vs ladder med 1.1012 / 0.500 —
DISTINGUISHED by a 1.3 % zr margin only (honest negative: the zr
statistic is essentially world-blind in magnitude; the
arithmetic content lives in the calibrated constants).  The r324
MEASURED composition stays the honest end state.
Experiments-side, NO ledger row, NO RH CLAIM.

**The density martingale and the moment dictionary (r339, the
reviewer's reformulation of the terminal — transport of mass
density through the fold genealogy instead of a maximum).**
`fold_density_dictionary_probe.py` (36/36, SPEC_SHA
`822d6bff564d88ba` final with record, freeze `a845041cdf866543`,
two-commit protocol: pre-freeze `907ebfd1`, record `7863495f`;
INDEPENDENT of r337 by the reviewer's verdict-reading rule — r337
tested the RAW signed process, the density per remaining
descendant is a martingale by algebra) built the canonical fold
genealogy over the m final atoms `a_i = |PΔ_i|` (Leg 0 sealed
BEFORE the freeze: the iterated r270 adjacent pairing —
parameter-free, construction-canonical, position-contiguous;
balanced bisection as sensitivity; a protocol mutant proves the
audit bites).  **The exact layer stands at theorem grade**:
`X_k = d(V_k)/d(root)` is a nonnegative martingale from mass
conservation alone (Fractions BIT-EQUAL on w9+w13, 76 nodes;
per-node identity 2.2e-16 on 81 live worlds; cubic recursion and
envelope exact; Jensen drift ≤ 0 exact), and the moment
dictionary `E[X_∞²] == m·M₂`, `E[X_∞³] == m²·M₃` is exact
against the r324 chain — the terminal target **is**
`E[X_∞³] ≤ C(log m)^A`, and the banked r306 C₂ = 1.069 (0/57,
re-gated) already certifies A = 2 on the 57-rung set.  **Verdict
`LOCAL_INFLATION_SUPERCRITICAL`** — neither Γ budget certifies:
the full worst-case budget `W_F = Π_k max_v Γ(v)` violates
44/43/40 of 51 at a = 1/2/3 (C_F 39.91/8.98/2.02), the good
tree (heavy jumps max R_c > 3/2 removed) violates 33/20/11;
e(W_F) = +0.956 DECIDED supercritical.  **The gap is the
finding**: the true expectation e(m²M₃) = +0.112 grows 8×
slower than the worst-case budget — Γ_max is dominated by
near-leaf degenerate pairs (per-level med profile 1.05 → 3.99
against the balanced-pair ceiling 4; the deep half carries med
0.712 of log W_F) where hardly any path mass sits: the concrete
R341 instruction is that the Bellman argument must weight Γ by
path probability, not take per-level maxima.  The Γ_max census
is world-blind (SCRAMBLE 51.76 below ladder med 223.86 — honest
negative) but the dictionary itself separates (SCRAMBLE m²M₃
20.59 vs ladder med 6.22); the worst W_F violators are the EXT3
deep anchors (kz42 at 18.29×) — the r337 deep-anchor margin
recurs; the drift is strictly ≤ 0 but NOT period-4 (r4c 0.957
vs bar 0.5 — the clause-5 coboundary subtraction does not
apply).  kz53 is the one spike with its Γ argmax mid-tree
(level 2, 4.303 — the r324 single-heavy-scale event as an early
heavy fold); every mid-band rung inflates at the last fold
level.  The r324 MEASURED composition stays the honest end
state.  Experiments-side, NO ledger row, NO RH CLAIM.

**The weighted Cauchy–Binet transport (r340, the new L\* base
architecture after the capping of capacity and parity: transport
instead of norm bound).**  `cauchybinet_hall_probe.py` (26/26,
SPEC_SHA `86587b4895e95689` final with record, freeze
`82c4d1839386a853`, two-commit protocol: pre-freeze `3736af89`,
record in the same change) re-read L\* through the exact signed
Cauchy–Binet split `D_n = det H_n(μ̃) = Σ_E W − Σ_O W` with
`W(I) = (Π|w_i|)·Δ(x_I)²` (Sylvester dictionary gated: `D_n > 0
∀ n ≤ N_w` IS L\*), built the sealed canonical fold-exchange
graph (companions = nearest free μ atoms per side, step cap 2;
exact edge ratio `W(J)/W(I) = (|w_x|/|w_y|)·Π((x−z)/(y−z))²`
bit-equal on 192 small-model edges, w9 log ward 2.3e-14), and
measured the transport by exact integer max-flow plus FULL
`2^|O|−1` Hall-cut enumeration on exact small models.  **Verdict
`CUT_REDUCTION_FAIL` + `SOURCE_EXCHANGE_INSUFFICIENT` +
`TRANSPORT_WORLD_BLIND` + `NEW_COORDINATE`** — the round's
central structural hypothesis (minimal weighted Hall cuts =
Gale-order interval ideals, which would have re-read 1 − κ_int
as a dual Hall slack) is **refuted at the smallest exact scale**:
5 of 9 fully enumerated loci carry NON-ideal argmin cuts
(antichain sections and mid-order singletons pinned to the
shallow negative atoms; the principal-ideal family misses the
exact minimum by 1.17×–10.2×, growing toward half-filling).
Coverage itself is exact almost everywhere (TOY 2/2, F1 3/3,
F2 4/4 with strict reserve `D_n > 0`), but on the PD instance I2
the elementary edge set fails exactly at half-filling depth
`n = N = 5` (deficiency 0.023).  The extremal test fails
honestly: the W9EDGE binding cut carries only 3.86e-3 of its
W-mass on configurations containing both r284 extremal atoms
(folds 2/4) — the extremal pair is a spectral object, not the
Hall-cut carrier.  **The structural finding: the shallow-edge
prefix of EVERY world, MAIN included, is locally indefinite from
n = 2 on its own configuration space** (W9EDGE D signs
+,−,−,−,+,+ at a resolved −9.7e-3 relative deficit; controls
break at n = 1) — the full-window positivity is a GLOBAL rescue,
not a local edge property, the flow-side mirror of r336
`PARITY_WORLD_BLIND`; the ladder edge Hall slack is NEGATIVE on
42/42 rungs (−0.13…−0.18) against uniformly positive margins — a
new sign-opposite near-edge coordinate, not a restatement.  m4
documents the r282 Kasteleyn boundary exactly (the sign gauge
shifts `D_2` by exactly `2Σ_O = 1/3`).  Twin: identical cut form
at 4.8e-8.  No R341 GO: the interval-Hall route to a quotable
theorem does not open; banked are the exact Cauchy–Binet/Hall
machinery, the local-edge indefiniteness of every world, and the
sign-opposite edge coordinate.  Experiments-side, NO ledger row,
NO RH CLAIM.

**The two-atom extremal solved as its own problem (r342, the Ü1
main find of the r338 door-2 full revision).**
`pair_extremal_probe.py` (38/38, SPEC_SHA `b09f8ccdcfdedc16`
final with record, freeze `4ca125c7906149bf`, two-commit
protocol: pre-freeze `bdc0b439`, record `5c80e561`) solved the
r284 two-atom extremal as its own problem: at the binding point
L\* is EXACTLY the determinant condition `c² < (1−d₁)(1−d₂)`
with `d_k = v_k K_N(y_k, y_k) = E_kk`, `c = √(v₁v₂) K_N(y₁, y₂)
= E_12` at the shallow-edge pair (folds 2/4, below log 2 — the
pair on 69/69 windows incl. the 12 r329 EXT3 fresh anchors as
pure test rows, pair mass 0.9352…0.9994).  **Verdict
`PAIR_LAW_FOUND` + `PAIR_WORLD_COMPLETE`** — (i) the component
laws are halves-stable on the 57 (p −0.754 / q −0.645 / c
−0.697 vs the disclosed r338 priors −0.71/−0.66) and extend to
the EXT3 pure test (11/12 per column); (ii) the pair WEIGHTS
are closed-form source objects: the digamma dictionary
`F_A(ξ) = −log π + Re ψ(1/4 + iξ/2)` for the archimedean layer
plus the EXACT two-cell tent closed form of the prime layer
predict v at median rel dev < 1e-4 over all 69 rungs; (iii) the
α composition closes bookkeeping-exactly (α_pair 3.341 vs
α_full 3.332 vs composed 3.333; 42-only 3.059 == r286 3.06)
with the OPEN analytic remainder ρ_r = 2.624 — the cancellation
exponent of the determinant reserve `r_det = 1 − c²/pq`, the
concretized specialist question; (iv) the sealed world census
closes Ü2: the union `{PR ≥ 3} ∪ {κ_int ≥ 1}` is the first
measured world-complete criterion of the L\* lane — with the
honest structure that the PR clause alone FAILS (the dead
worlds are also concentrated at their own N_w, PR 1.80…2.92)
while the κ_int clause alone is world-complete: EPST 1794 /
SCR 8.51e6 (== r334) / **SMOOTH 2.193 / HL2 1964 (first
evaluation)** ≥ 1, live MAIN/TWIN 0.999567 < 1.  **The R343
material, measured:** the exact Schur dressing makes L\*
equivalent to `{λ_rest < 1}` AND `{dressed pair determinant}`;
the rest margin decays parallel to the full margin (slope
−3.28, offset ~20×) while the DRESSED pair reserve `r'_det` is
FLAT (slope +0.018, w9 value 0.303) — the O(1) certificate
candidate a full L\* theorem needs.  Honest negatives: `r_det`
is halves-curved (−0.767); kz56 breaks the R2 band
(`EXT3_FAMILY_BREAK`, the 12–40 % 2×2-uniformity does not
extend unmodified to the small-gap family); the kernel side
(why `v_k K_N → 1` with deficit ~N^−0.7 at the hard edge; r285
sub-classical 0.38 confirmed as the deep-rung late-window
growth) stays without closed form.  Experiments-side, NO ledger
row, NO L\* claim, NO RH CLAIM.

**The dressed pair reserve under fire (r343, the r342 O(1)
certificate candidate: analytic lower bound or refutation).**
`pair_coupling_probe.py` (38/38, SPEC_SHA `9ffc2705f326d625`
final with record, freeze `a24718fcb8c72f85`, two-commit
protocol: pre-freeze `e652071f`, record `95fcdcae`) put the
r342 Schur coordinates under fire.  **The exact spine:** the
resolvent-correlation identity `r'_det = 1 − M₁₂²/(M₁₁M₂₂)`
with M = the pair block of `(I−E)^{-1}` (gated per rung against
the independent full-inverse route + EXACT-Fractions wards on
the r334 rational instances, incl. the exact leading-minors
criterion for `λ_rest < 1`), and the exact spectral
decomposition of the dressing over the rest eigenmodes — the
contract's formula `r'_det = f(bare scalars, coupling vectors)`
measured per rung.  **Verdict `DRESSED_RESERVE_DECAYS(soft:
curvature clause)` — read precisely:** every HARD kill clause
misses (slope +0.018 dead flat; the 12 EXT3 rows — genuinely
BLIND, their dressed columns were never printed in r342 —
12/12 in the 0.5-decade band, incl. kz56 whose dressed reserve
0.1605 is flat while its bare R2 breaks the band: the dressing
absorbs exactly the Klein-gap family effect; 6 fresh EXT4
windows at N_w 2656…3181 — the deepest L\*-lane windows ever
measured, sealed source-pure selection under the family domain
cap z² ≤ 400000 — 6/6 in band, margins positive), but the
sealed FLAT clause fails on the halves-curvature bar (−0.426 >
0.35, a bar inherited from the decay-law convention applied to
a flat O(1) column with ~×2 scatter — sealed before sight,
applied honestly): the candidate is neither refuted on any
family nor certified flat.  **The structural findings:** (i)
the dressing eats bare reserve and coupling in near-exact
proportion (Δd₁/p and Δc/c → 1.000/−1.000; ρ' pinned ~0.846;
`m2'/margin` 1.0003…1.031 — the dressed 2×2 is a near-exact
λ_max carrier); (ii) **the bound autopsy closes Leg C
honestly**: the theorem-grade triangle/Cauchy–Schwarz/operator
chain certifies ZERO of 75 rows — the dressing works by the
SIGNED cancellation Δc ≈ −c (overshoot 73× at w9, to 2.4e11 at
depth): an O(1) bound must control the signed cancellation —
the concretized specialist question; (iii) `r'_det` is a gated
**TOP-2 spectral object** (median top-2 dev 0.063, K_res ≤ 3
on 75/75): its flat content IS the flat gap ratio
`g21 = (1−λ₂)/(1−λ₁)` (median 8.2; kz56 at 16.0 with the
reserve unmoved) — the R344 coordinate; (iv) `λ_rest` alone
separates the six instrumented worlds (dead ≥ 1, live 0.9963;
Schur equivalence 6/6 exact; slope −3.276 == r342 bit-near,
offset ~21×); (v) **`PEELING_STRUCTURE_FOUND`**: the rest block
is again a shallow-edge two-atom extremal (median rest-pair
mass 0.9902; level-2 reserve ≥ 0.23 on the 57), the w9 cascade
peels (2,4)→(6,8)→(10,12) with monotone margins — concentration
breaks at level 4: a level-2 recursion statement, not an
induction; (vi) RESTATEMENT does not fire (median shadow dev
1.0): the dressing is real content.  Honest negatives: the
sealed flatness protocol needs a curvature-aware successor for
O(1) columns (R344 protocol material, not retrofitted); the
EXT4 rows are disclosed-seen, only EXT3 carried blind weight.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**The R\* mass balance and the two-scale freeze (r344, the named
r341 follow-up: each arm on its own sealed freeze).**
`fold_two_scale_balance_probe.py` (41/41, SPEC_SHA
`06375c3ade846178` final with record, freeze
`bf16912825178c44`, two-commit protocol: pre-freeze `d875647c`,
record `dfb8d1c1`; amendment a1 disclosed — two anchor-GATE
reading fixes only, no sealed surface touched) ran the stop
threshold R over the sealed grid (3/2, 8/5, 5/3, 12/7, 7/4, 2)
on the r341 exact path layer (imported verbatim; every exact
ward live at all six grid points, Fractions bit-equal at the
two sealed pins).  **Verdict `TWO_SCALE_PARTIAL`: the
three-arm min-coverage CERTIFIES at R̂ = 7/4 at a = 1 — 0
violations on the 51 test rows, named 4/4, midband 6/6 — but
the sealed choice formula (argmin max(e_H, e_G)) is not
halves-stable (the dyadic halves pick 8/5 vs 7/4): R\* remains
a tuning surface in the exponent language, said honestly.**
The findings: (i) **the mass-balance curve is measured** (four
interior grid points new): hsh med 0.872 → 0.266 → 0.000
across the grid, E3h share med 0.944 → 0.386 → 0.000, W_B med
1.489 → 3.796 → 6.096; at R = 2 the algebraic pair limit fires
as derived (no pair is ever heavy, 71/77 rungs lose the heavy
arm, the sealed eligibility guard fires); **the arm exponents
cross exactly once**, in the gap (12/7, 7/4) — the
equilibration point is real, its location not yet
halves-stable; (ii) **the disjunctive (complementarity)
coverage certifies at EVERY grid point already at a = 1**
(C_H on the hand-off column `(m·q_max)²·msh`, C_G on the
ε-chain column W_B, third arm = the banked r321 sliding bound
`1.3056·F_A²` at the frozen constant), while the r341
component-AND form still fails (13/10/10) — the r337 directive
is exactly what certifies; **the third arm is load-bearing**:
8 of 51 test rows are covered only by the r321 bound,
including the entire EXT3-B deep-anchor family 6/6 (kz51
F_A(ins) 5.54, reserve 5.3× — the r329 out-of-sample reading
reproduces under the insertion convention); (iii) **the
partition is NOT hsh-identifiable** (honest negative: the
sealed rule predicts the covering arm on 7/51 covered rows —
the partition is posthoc relative to hsh, a source-side
predictor remains open); (iv) kz55 is an EARLY-level ε-chain
anomaly (argmax level 1, the r339 kz53 class), NOT absorbed by
rebalancing (W_B 2.888 → 8.459) but covered comfortably by the
third arm (ratio 0.14): the single r341 Form-1 violator is a
sliding-bound row; (v) **the honest composition with a
certifying cover**: `E[X_∞³] ≤ [3.9859 + 1.1409](log m) +
1.3056·5.54²·(log m)²` on the covered set ⟹ m₀\* = 10^22.6 —
beats the r324 route 10^59.6 and the r341 envelope typing
10^24.0 (which had no cover), still above the r306 census
10^13.5; F_Amax = 5.54 is the kz51 insertion value, disclosed.
Worlds: the balance CURVE separates where the r341 point
budget was world-blind (SCRAMBLE stays heavy-flat, twin
collapses, EPSTEIN good-dominated).  Experiments-side, NO
ledger row, NO RH CLAIM.

**The gap ratio as primary coordinate (r345, the named r343
follow-up: the curvature-honest flatness protocol, the two-level
formula, the honest kill, the signed cancellation as object).**
`gap_ratio_primary_probe.py` (35/35, SPEC_SHA
`1f99235a1d870e42` final with record, freeze
`7d61df830ed54cf2`, two-commit protocol: pre-freeze `4a1362a0`,
record `4e5e1270`; NO amendments after freeze) promoted
`g21 = (1−λ₂)/(1−λ₁)` and the top-2 eigenvector geometry at the
pair to primary coordinates.  **The exact spine:** the TWO-LEVEL
FORMULA `r'_2 = g21·(t₂−t₁)²/((g21+t₁²)(g21+t₂²))` with the pair
angles `t_k = w₂(i_k)/w₁(i_k)` — an exact algebraic identity for
the top-2-truncated resolvent reserve, gated on 75/75 rows (max
dev 4.0e-15) with an independent resolvent-spectrum route for
g21 (anti-circular, devs ≤ 1.6e-8).  **Verdict
`GAP_RATIO_PRIMARY_CERTIFIED` — the first certificate-grade
letter on the O(1) coordinate:** the curvature-honest protocol
(sealed a priori, the explicit r343 mandate: median band on all
75 rows + Theil-Sen slope with a separation-restricted
pairwise-slope quantile CI containing 0 + no monotone cohort
drift) passes ALL clauses on BOTH candidates (`r'_det` and
`g21`, zero band outliers each) **while the old r343 clause
fails both candidates on its halves-curvature bar, reproduced
bit-near** (curv −0.426/+0.601): the r343 soft-decay letter is
re-adjudicated as a PROTOCOL artifact — the halves-curvature bar
reads the ~×2 scatter of a flat O(1) column as decay, the
scatter-honest CI reads it as flat; both protocols printed side
by side.  **The honest kill does not fire:** on the sealed
concentration-weak census (the two 6-row deciles, incl. kz44
rest-pair mass 0.6917 and kz59 pair mass 0.9352 at their record
minima) the median two-level dev is 0.1432 ≤ 0.30 (the weak
rungs DOUBLE the ladder median 0.0634; single worst kz28
0.4192 — honest), K_res ≤ 3 on 11/11, and `KILL_ABSORBED_BY_K3`
(median top-3 dev 0.0163: the K ≤ 3 shadow is ~9× tighter
exactly where K = 2 weakens).  **`CANCELLATION_LAW_FOUND`
(δ = 2.668, additive tag) — the r343 bound-autopsy question
answered as a measured structure statement:** the mirror
residual `c'/c = |1 + Δc/c|` decays as `N_w^−2.67` on the 57
(halves-stable, EXT3 10/12 in band with both misses HIGH side,
EXT4 6/6) — 'the rest space mirrors the pair cross-term up to
O(N_w^−2.7)'; the anatomy: the DIRECT overlap `u₁·u₂` carries
the mirror's bulk (order-0 share median 0.839) while the mode
profile is multi-mode (M90 ~30) — order-0-dominated in PATHS,
multi-mode in MODES; the finite-order mirror ρ₃₂ = 0.9225 on
both live worlds but DIVERGES on all four dead worlds
(λ_rest ≥ 1 explodes the path series): the mirroring exists only
where the rest clause holds.  **Further findings:** the second
eigenvector lives dominantly on the PAIR too (w2 pair mass
median 0.552; λ₂ is NOT the rest-block top anywhere); the angle
column is ladder-stable (t₁ ~ −0.47, t₂ ~ +1.12) yet
RESTATEMENT does not fire (fixed-angle inversion dev 0.1009 >
0.05 — g21 is not `r'_det` plus a constant angle); the world g21
census separates by magnitude (dead < 1 on 4/4, live > 7.5 —
the s1 sign conjecture honestly refuted: dead worlds have
λ₂ > 1 too).  Honest negatives: a sealed census certificate on
75 finite windows, never an asymptotic theorem — and r343's
letter was correct under its own seal (the re-adjudication
changes the protocol, not the data); δ = 2.67 sits below the
margin exponent 3.33 (real gap or c'-column curvature — the
typed R346 question via `c'² = (1−r'_det)·p'q'` with
`m2' == margin`).  Experiments-side, NO ledger row, NO L\*
claim, NO RH CLAIM.

**The cover canonization (r346, the named r344 follow-up: the
three residues of the r344 cover — canonical stop criterion,
source-side partition predictor, F_Amax defusal).**
`fold_cover_canonization_probe.py` (45/45, SPEC_SHA
`95559d5de07b304e` final with record, freeze
`306dba57867f2170`, two-commit protocol: pre-freeze `9fcc081b`,
record `bfe70fcf`; NO amendments — calibration pass 1 = first
full evaluation = 45/45) re-executed the ENTIRE r344 scaffold
through the same code path (balance curve, R̂ = 7/4 with halves
(8/5, 7/4), freezes 3.9859/1.1409, 0/51 at every grid point,
third-only 8, partition 7/51, F_Amax 5.54, m₀\* 10^22.6 — ALL
anchor-gated bit-near) and adjudicated the residues with sealed
machinery.  **Verdict `COVER_CANONIZED + PREDICTOR_FOUND(P02)`:**
(i) **the stop rule canonizes via the intrinsic pair-ceiling
formula, not via the exponent crossing** — K1
(`R_ALG = 4^(1/3) = 1.5874 →` grid 8/5, index 1, interior,
DATA-FREE: the same derived algebra that makes R = 2 the pair
limit) CERTIFIES at a = 1, landing exactly on the grid point one
r344 dyadic half picked; K4, the R-FREE ENVELOPE (per-rung
HB-min over grid indices 0–4 positive-guarded, W_B-min over all
six), ALSO certifies at a = 1 with `C_H_ENV 3.9859 + C_G_ENV
0.4867` — the good envelope drops to the W_B(3/2) freeze and
the threshold disappears by construction; K2
(first-equilibrated) and K3 (pooled interpolated crossing,
R_CROSS 1.7407) both pick 7/4 and are formally halves-stable
**but only via the no-crossing fallback** — neither dyadic half
shows a sign change at all (the halves e_G columns collapse to
−0.3…−1.4): the crossing LOCATION stays halves-invisible, the
exponent language stays soft, said honestly; (ii) **residue 2
CLOSED at the sealed bars — the partition is
source-predictable**: the sealed one-feature rule P02
(`F_A ≥ 1.5 →` third arm, else heavy; the r329 SPIKE_FA record
threshold) predicts a COVERING arm on **51/51** test rows (core
39/39, out-of-sample EXT3 12/12, non-degenerate; sealed 12-rule
threshold family, thresholds a-priori), exact-priority-label
46/51 vs the r344 hsh baseline 7/51 — the cover's working
partition is spike-vs-rest in the F_A coordinate, not
heavy-vs-good in hsh; (iii) **residue 3 stays OPEN (honest
negative): F_Amax is not uniformly defusable** — the six sharp
spikes kz53/kz67/kz51/kz54/kz42/kz62 are third-arm-only at
EVERY a ∈ (1, 2, 3); the uniform rescue fails for both the
class split (1.5) and the P90 cap (1.917), `FAMAX_DEFUSED`
stays silent and the honest uniform m₀\* stays **10^22.6**; the
class-conditional QUIET statement (cap 1.39) solves to 10^16.1
with the 13-row spike family as NAMED pointwise-certified
exceptions — a two-statement census, not a uniform bound; the
floor form (0.58) adds and loses nothing on-sample, the r329
below-range question stays open; (iv) worlds census: SCRAMBLE
is the only control the class rule flags SPIKE (F_A(ins) 2.00,
P02 says T) — w9/w13/EPSTEIN all QUIET/heavy.  Must-fails: e1
pred-from-coverage and e2 clsrule-posthoc and e4
crossing-posthoc protocol-CAUGHT twice each, e3 envelope
double-count CAUGHT exact (break 147/32 in Fractions).
Experiments-side, NO ledger row, NO RH CLAIM.

**The delta–alpha closure (r347, the named r345 follow-up: the
one-line identity — the margin exponent from the cancellation
law).**  `delta_alpha_closure_probe.py` (34/34, SPEC_SHA
`bd1aa7f393da057f` final with record, freeze
`99100cea2358fe56`, two-commit protocol: pre-freeze `95f7f944`,
record `8e489331`; NO amendments after freeze; one pre-freeze
machinery finding disclosed — an arithmetic slip in the w9
aspect anchor constant, corrected before the freeze commit)
put the exact 2×2 determinant identity of the dressed block in
charge of the exponent bookkeeping.  **The exact spine:** the
ONE-LINE IDENTITY `m2'·(p'+q'−m2') = p'q' − c'² = p'q'·r'_det`
(both eigenvalue deficits of the dressed 2×2 are the roots of
`t² − (p'+q')t + (p'q'−c'²)`) — exact Fractions on the hand toy,
f64 max residual 3.3e-9 on 75/75 rows at the backward-error
scale.  **Verdict `ALPHA_CLOSED` — the margin exponent FOLLOWS
from the cancellation law:** all four sealed closures hit inside
the 0.1 bar — C1 identity route |α 3.332 − α_id 3.382| = 0.050,
C2 margin bridge 0.001, C3 cancellation bookkeeping
|slope(c') − (slope(c) + slope(c'/c))| = 0.035, and **C4 THE ONE
LINE |α 3.332 − (a_c 0.697 + δ 2.668) = 3.366| = 0.033**; the
bridge clause `m2' == margin` is protocol-graded on all 75 rows
(max |m2'/margin − 1| = 0.0605 ≤ 0.10, ratio slope +0.0001);
`CURV_FLAT(r'_det)` re-gates under the r345 protocol verbatim (0
band outliers), both AUX aspect bands hold 0 out (p'/q' max
0.231 dec, (p'+q')/c' max 0.101 dec — the flat-aspect step that
turns the identity into the one line); the δ-law and c-law
re-gate on their sealed meters.  **Building blocks typed:** the
identity is THEOREM-GRADE; the bridge and the flatness
certificates are CERTIFIED CENSUS (0 violations); `a_c` and `δ`
are FIT-CENSUS laws — **the open analytic remainder of the L\*
margin law is reduced from ρ_r = 2.624 (r342) to the single
cancellation exponent δ**: one measured law instead of three,
connected by exact algebra and certified flats.
**`DRESSED_FACTOR_CENSUS` (Leg C, honest):** the dressed
diagonals do NOT inherit the bare dictionary slopes unchanged
(the GO clause fails loudly: p'/p, q'/q decay ~N^−2.6) and the
residual-law tag does not fire either (q'/q halves-curved
−0.508 > 0.35) — the factor laws stay census with the
universality census |δ_p − δ| = 0.059, |δ_q − δ| = 0.003: the
dressing eats p, q and c near a COMMON rate, census-grade, not
a sealed law.  **`MIRROR_WORLD_CLAUSE_SEALED` (Leg D):** mirror
exists iff λ_rest < 1, live iff |ρ₃₂ − 1| ≤ 0.5 — live 2/2
(ρ₃₂ 0.9225), dead 4/4 diverge, and **the r330 Dirichlet second
worlds enter the L\* lane for the first time, typed DEAD-side**
(DIR λ_rest 3.97e37, series NONFINITE; ABS 2.28e5, series
−3.85e176): the r330 half-filling split restates structurally
in the E-Gram frame — the χ-twist and even the bare p = 3 atom
removal destroy the rest-block contraction; typed, not forced.
Honest negatives: δ is NOT derived from the source (the typed
specialist question is now ONE exponent); the dressed decay
columns extend to EXT3/EXT4 only high-side (n_low 0 — the r286
deep-family curvature restated); α_id − α = 0.050 is pure
Theil-Sen non-additivity across curved columns (the identity
holds per row at 3.3e-9); no second living arithmetic exists
inside the MAIN frame (the GRH-faithful Dirichlet frame stays
the named follow-up).  Experiments-side, NO ledger row, NO L\*
claim, NO RH CLAIM.

**The delta source anatomy (r348, the named r347 follow-up: the
order-0 mirror as an object + the resolvent rate-equality theorem
candidate).**  `delta_source_anatomy_probe.py` (34/34, SPEC_SHA
`307814e9ef67e8a1` final with record, freeze `b43a635184c44d3c`,
two-commit protocol: pre-freeze `0d0849e6`, record `665ea4f6`; NO
amendment — calibration pass 1 = first full evaluation = 34/34)
put the one remaining measured exponent δ = 2.668 under source
anatomy.  **Two exact spines:** (i) the ORDER-0 SPLIT
`Δc = u₁·u₂ + Σ_m α_m β_m δ_m/(1−δ_m)` (direct path + resolvent
enhancement; Fractions exact, f64 max 5.8e-14 on 75/75, with the
bookkeeping identity `c'/c == (1−ρ₀) − ρ_hi` at 3.6e-8); (ii) the
TWO-LEVEL DRESSED-SCALAR IDENTITY `p'₂ = m(g21·a₂²+b₂²)/Δt²`,
`q'₂ = m(g21·a₁²+b₁²)/Δt²`, `c'₂ = m(g21·a₁a₂+b₁b₂)/Δt²`
(Fractions exact on the rank-2 model — 121/250, 79/250, 72/250 —
and through the full Schur chain; cross-tie r'₂ = 4375/9559 == the
r345 formula).  **Verdict `RATE_EQUALITY_THEOREM` — the common
dressing rate IS the margin rate:** under top-2 dominance with
flat geometry every dressed scalar is margin × an O(1) geometry
factor, hence `δ_x = α − a_x` exactly (rate toys: the naive
`δ_p == δ_q == δ` holds IFF `a_p == a_q == a_c` and breaks by
exactly the bare spread; a τ = 0.4 angle drift separates the
dressed slopes by 0.453 — flat geometry is load-bearing); LIVE
certified census: E1 `CURV_FLAT` (r345 protocol verbatim) passes
on ALL THREE margin-pinning ratios `p'/m`, `q'/m`, `|c'|/m`
(slopes −0.056/+0.016/−0.025, 0 out/0 hard of 75 each), E2
two-level truncation median 0.0879 ≤ 0.20, E3 sign 75/75, E4
theorem image max |δ_x − (α − a_x)| = 0.033 ≤ 0.1 — **the r347
universality census is upgraded to its exact form and δ == α −
a_c loses its independent-law status; the irreducible measured
rest of the L\* margin law is the pair {α, a_c}.**
**`ORDER0_LAW` with `CARRIES_DELTA` REFUTED:** the order-0 miss
`y₀ = 1 − ρ₀` carries its own slow law (δ₀ = 0.401, EXT3 12/12,
EXT4 6/6) but |δ₀ − δ| = 2.267 — the r347-sketch hypothesis dies
cleanly: u₁·u₂/c does NOT carry the N^−2.67 law; the δ law is an
INTER-ORDER NEAR-CANCELLATION (y₀ and ρ_hi are twin slow laws
whose difference is the c'/c column, pinned to the margin scale
by the resolvent; depth census |c'/c|/y₀ median 1.48e-3).
**`DICT_T0_GO`** (median 0.0177 ≤ 0.10 over the six sample rungs,
w9 honest worst 0.195): the weight side of the order-0 overlap
products is dictionary-explicit; the kernel side stays
census-grade (r342 negative #4).  **Honest negatives:**
`WEAK_FAMILY_STRAINED` fires (kz28 scalar shadows up to 0.91,
median 0.377 > 0.35; worst arbitrated row kz23 at 4.06 — K = 2 is
a median instrument on the scalars, not per-row); the certificate
is a sealed census on 75 finite windows; α and a_c stay UNDERIVED
from the source (`DELTA_SOURCE_DERIVED` cannot fire).  The mirror
world clause reproduces bit-near with the NEW ρ₀ world column
(live 0.5787 vs dead −220 … −1.06e6; SMOOTH +1.76 same sign wrong
size — census).  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.

**The path-weighted Bellman / Reverse-Hölder round (r341, the
terminal main round after the r339 dictionary — the two-arm
theorem candidate with path-probability weights instead of
per-level maxima).**  `fold_bellman_reverse_holder_probe.py`
(38/38, SPEC_SHA `7a9cf6b3fe24d0d7` final with record, freeze
`f0d2c744c46942bc`, two-commit protocol: pre-freeze `86f523e8`,
record `70d01ef8`) executed the r339 build instruction and the
r337 two-constant directive on the sealed r270 pairing tree.
**The exact path layer stands at theorem grade**: the
cubic-tilted tower `E[X_∞³] == E_Q[Π_k Γ(V_k)]` with steps
`p̃_c = p_c R_c³/Γ(v)` (the naive untilted form is FALSE — toy
break 7/18 EXACT, must-fail e1), the Φ–Γ identity
`Σ_c Φ(c)/Φ(v) == Γ(v)` with `Φ = A³/n²`, the stopped leaf
partition at τ = first heavy level with the exact hand-off
`E3h ≤ (m·q_max)²·msh` (the r335 q_max currency entering the
cubic layer exactly), and the good ε-chain envelope
`E3g ≤ W_B = Π(1+ε_k)` — all Fractions BIT-EQUAL on w9 + w13 +
three sealed toys.  **Verdict `PATHWEIGHT_ALSO_SUPERCRITICAL`
(per the sealed tree — the honest letter-reading: what fails is
the freeze-pointwise certification, NOT the growth: e(W_B) =
−0.214 and e(E3h) = +0.313 where r339 e(W_F) was +0.956)** —
the heavy arm fails its own freeze with NAMED 0/4 and the EXT3
deep anchors as worst violators (kz51 7.61×), Form 1 (the
integrated ε-chain) misses by the SINGLE violator kz55 (1.41×
at a = 2; EXT3 clean), Form 2 (Ψ-weight Bellman, prefactor 1)
certifies nowhere (best combo (A, C0) = (3, 1.0): 23 composed
node violations — the disclosed mid-tree risk is real).  **The
findings**: (1) the r339 thesis is CONFIRMED QUANTITATIVELY —
path weighting deflates the worst case 21× at the median
(E_P[ΠΓ] med 12.53 vs W_F med 265.54; path-weighted per-level
profile 1.05…1.80 vs Γ_max 1.05 → 3.99; near-ceiling nodes
carry pm3 med 0.161 of path mass); (2) **the stop at R* = 3/2
is too early on the path-mass scale** — the heavy arm inherits
med 94.4 % of the cubic mass with modal stop level 1 (the
mid-band stops its whole leaf mass at the FIRST fold level),
and the split is threshold-unstable (R_ALT = 7/4 moves the E3h
share to 0.386): R* is a tuning surface, not a canonical
constant — where between 3/2 and 7/4 the arms equilibrate is
the named open question; (3) the good arm is ONE RUNG from
certifying (kz55 only).  Worlds: the path-weighted budget is
also world-blind (honest negative; the dictionary stays the
only sharp separator).  Composition typed ENVELOPE ONLY (the
a = 3 envelopes would give the polylog m₀\* = 10^24.0 vs r324
10^59.6 and the r306 census reading 10^13.5) — **the honest
state of the route remains the r324 measured composition until
an arm certifies**.  Experiments-side, NO ledger row, NO RH
CLAIM.

**The third-arm spike law (r349, the named r346 residue: the
sliding coverage of the F_A ≥ 1.5 family as a law).**
`thirdarm_spike_law_probe.py` (44/44, SPEC_SHA
`9b593e63762ee698` final with record, freeze
`0016e2f1596978da`, two-commit protocol: pre-freeze `b2ef45ea`,
record `609346e6`; one DISCLOSED print-level amendment a1
between calibration passes — the sealed "every hole NAMED"
requirement extended to the EXT4 misses, no bar/rule moved; a
pre-run placeholder-removal disclosed, r321 protocol-error
class) re-executed the ENTIRE r344/r346 scaffold anchor-gated
bit-near (cover 0/51, P02 39/39 + 12/12, K1/K4 constants, V1/V2
class record, six-spike set + ratios) and adjudicated the spike
coverage with sealed machinery.  **The exact spine (warded
≤ 9.3e-16):** the sliding reserve FACTORIZES EXACTLY —
`RSV = GSQ·F_A²/ρ₂ = (GSQ/B²)·(pk/M2q)·(pk·M2q/Σq³)`, and via
the r324 identity `pk = F_A·B·log m/m` the dominance form reads
`ρ₂ = D·pk·(F_A·B)²` with `D = Σq³/pk³`.  **Verdict
`EXCEPTIONS_REMAIN + RESERVE_FLAT(−0.33) +
EXCEPTIONS_DISSOLVED(13/13) + HOLES([111, 75])` — the honest
split:** (i) **the RAW class law holds everywhere** — `ρ₂ ≤
1.3056·F_A²` on F_A ≥ 1.5 with ZERO hard violations on all 23
family rows across 65 ladder + 12 EXT3 + **6 fresh EXT4 anchors
(the r343/r345 L\*-lane list, first entry into the cubic lane —
ALL SIX are spike-class under the insertion coordinate, F_ins
1.58…6.68)**, including the new out-of-sample record F_ins =
6.68 (kz111); the 13 r346 class-conditional exceptions DISSOLVE
13/13 (reserves 3.2…12.1) and the hand-off is SEAMLESS (every
test row below 1.5 heavy/good-covered, 0 holes; boundary band
census 22 rows); (ii) **the sealed reserve floor 1.5 is
undercut out-of-sample** — the two deepest fresh EXT4 spikes
kz111/kz75 land at reserve 1.11/1.07: the honest family floor
is ~1.1, not ≥ 1.5, and the family F_A ceiling GROWS
out-of-sample (5.54 → 6.68) — the r346 census ceiling is not
stable; (iii) **the reserve anatomy**: the reserve is the
CONCENTRATION DEPTH `1/(D·pk)` (median log₁₀ shares
+0.01/+0.64/+0.26 — not the calibration slack: B² > GSQ on 7/17
family rows, the r321 pure-algebra caveat restated; no log
factors appear), and it is FLAT-to-eroding in F_A (rc −0.331,
neither sealed monotonicity bar fires) — upward safety comes
only from the measured `D·pk·B²` ceiling (0.409 ≤ 0.870 on the
77 sealed rows, ~1.2 on the EXT4 misses); (iv) **the dominance
structure is real but misses the sealed contrast bar** — family
med D = 1.79, max 2.13, the six sharp spikes D 1.07…2.06
(near-single-atom cubes), quiet med 5.03 → contrast 2.8× < 3.0:
`THIRDARM_LAW_DERIVED` stays unfired by the sealed letter; the
mechanism reading (r324 identity + near-dominance) stands as
census; (v) worlds: SCRAMBLE is spike-class and COVERED (rsv
2.9) — the class statement is ARITHMETIC-FREE by measurement, a
pure concentration-size statement, no world separation claimed.
m₀\*: uniform 10^22.6 UNCHANGED, two-statement composite
10^22.6 (spike side binding), V1 10^16.1 / V2 10^17.5
reprinted.  Must-fails: e1 reserve-bar-posthoc + e2 f0-posthoc
protocol-CAUGHT twice each, e3 dominance-circular CAUGHT twice
(Fractions pin 7/2 vs 28/27), e4 wrong-log-power CAUGHT exact
(break == 2).  Experiments-side, NO ledger row, NO RH CLAIM.

**The alpha source anatomy (r350, the named r348 follow-up: the
kernel side of the L\* margin legislation as an object).**
`alpha_source_anatomy_probe.py` (33/33, SPEC_SHA
`c3998c87777c975c` final with record, freeze
`f7d622d8e975b265`, two-commit protocol: pre-freeze `e3f53e1a`,
record `24f8ca0d`; TWO DISCLOSED calibration amendments a1/a2 of
the r342-a1 class — the BK1 and route-A after-fit slope sums
measured 0.137/0.170 of pure Theil-Sen non-additivity on the
strongly curved weight columns while the pointwise identities
hold at 1e-16; re-measured at the pointwise dictionary-
reconstruction scale and compose-then-fit, the after-fit sums
kept as census, no adjudication bar/candidate/verdict rule
moved) put the kernel side of {α, a_c} under sealed anatomy.
**Three exact spines:** (i) the KERNEL COLUMNS `K11 = d1/v1`,
`K22 = d2/v2`, `K12 = c/√(v1 v2)` with the INDEPENDENT
Christoffel–Darboux ward — K_N at the pair atoms recomputed from
the μ-chain recursion coefficients via the CD endpoint/confluent
formulas, == the Gram route at max 1.2e-10: **K_N is
source-computable; the open question is its LAW, not its
value**; (ii) the PINNING IDENTITIES exact in Fractions on two
rank-2 models — `m2'₂ == margin` IDENTICALLY (the bridge is 1 in
the top-2 truncation), `p'q' − c'² == margin²·g21/Δt²` (dets
7/100 and 3/25), `c' == margin × G` — **the r348 twin
near-cancellation is the algebraic self-consistency of the
resolvent equation**, with the pinned corollary `slope(y0 −
ρ_hi) == −(α − a_c)` (residual 0.033); (iii) the slope
BOOKKEEPING (BK2 Christoffel saturation 0.018/0.016: **the
diagonal kernel growths ARE the reciprocal weight laws**; BK3
backward-CS 0.0016: a_c == (a_p + a_q)/2 to 0.002).  **Verdict
`ALPHA_SOURCE_CLOSED` AT CANDIDATE-LAW GRADE + `PINNING_THEOREM`
+ `DELTA0_CANDIDATE`:** the exponent chain closes source-side
with ONE census member — `α == 3/4[cand a_p] + 2/3[cand a_q] +
ρ_r 2.624[census] − a_(p+q) 0.690 = 3.352` vs 3.332 (dev 0.019);
route A independently at 3.401 (dev 0.068); blocks typed:
weights WÖRTERBUCH (the r342 digamma/tent dictionary carries the
across-ladder weight LAWS, |s_v − s_vpred| = 0.0000 at slopes
−1.791/−1.683), deficits CANDIDATE-LAW (a_p 0.7539 hits [3/4,
2×0.38] clauses clean; a_q 0.6446 hits [2/3, 1−0.38]; a_κ 0.7111
hits [2/3, 3/4] — **every ambiguity printed: a sealed hit on 57
windows is NOT an identification**), pinning THEOREM (bridge max
0.0605, det-shadow median 0.0731, CURV_FLAT 3/3), ρ_r CENSUS.
**The kernel steckbrief (new numbers):** s_v1 −1.791 / s_v2
−1.683 (dictionary-grade), g_K11 +1.786 / g_K22 +1.683 (==
reciprocal weights), **g_K12 +0.902 the ONE dirty census column**
(no candidate hits, curv +0.500, EXT3 5/12 — the cross-kernel
growth at discrete arch-rim atoms is the honest kernel rest;
REL2 `g_K12 == (g_K11+g_K22)/4` hits at 0.035 but stays census),
a_κ 0.711.  By-catch: **the y0 world column separates live from
dead by size or sign on 6/6 std worlds** (the r348 ρ₀ column
managed 5/6 — SMOOTH flips sign in the y0 coordinate); on every
dead world the ρ_hi series diverges — the twin slow laws are a
live-world structure.  δ₀ = 0.401 re-gates with hits [0.38, 2/5]
mutually unresolvable.  Honest negatives: candidate-law grade is
never an asymptotic derivation (3/4 vs 2×0.38 at distance 0.01,
unresolved); the named rests are g_K12 and ρ_r (the r338 q1
backward-CS question in its sharpest form).  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.

**The family growth law (r351, the named r349 successor:
m·q_max ≤ C·log m as a law, and the stable reserve floor).**
`qmax_growth_law_probe.py` (43/43, SPEC_SHA `67102e4cb2aa17e6`
final with record, freeze `d556c758701c3a60`, two-commit
protocol: pre-freeze `8131ab53`, record `080d3711`; NO amendment
after freeze; the pre-spec scoping disclosed: selection
enumeration + two wpack timings only, no bound value computed)
adjudicated the r349-named growth law on the CONVENTION-FREE
coordinate `FAB = m·q_max/log m == F_A·B` (the exact r324
identity: FAB does not depend on the F_A convention).  **Verdict
`GROWTH_LAW_CERTIFIED` + `FLOOR_ERODES(10^3.7)` +
`INZONE_POOL_EXHAUSTED` + `EXT5_CLEAN(6)`:** the frozen ceiling
C_FAB = max FAB over the 83 sealed rows = **14.93 at kz111**
(EXT4 — the by-hand expectation ~7.44 from kz51 was low by 2×:
the EXT4 FAB column had never been computed); the FRESH EXT5
TRANCHE (the r343 selection rule verbatim on the extended used
ledger: used 98, fresh 17, B5 kz79/81/65 in-zone small-gap + A5
kz103/135/106 deepest, N_w 1771..2812, POSITIVE_PREFIX 6/6 —
and the **in-zone fresh pool is EXHAUSTED after this tranche**)
tests it with **ZERO violations** (fresh max 9.71 at kz135, 35 %
below the ceiling; rc_small +0.243 < +0.5): `m·q_max ≤
14.93·log m` holds on every measured row of every cohort (89
rows) and on all four instrumented worlds (SCRAMBLE FAB 2.09 —
arithmetic-free by measurement) — **the first uniform growth
statement of the lane that survives a fresh tranche**.  The F_A
census ceiling ticks up AGAIN (kz79 F_ins 6.69 > 6.68) while
the FAB ceiling stands: the law coordinate is measurably more
stable out-of-sample than the rank-local F_A.  **The source
derivation stays open** (src_ok False, typed honestly): the K3
pileup cap breaks on fresh (kz65 pil 184.6 > frozen 178.0) and
is vacuous, K4 group cap holds but vacuous, the K2 Klein-gap
formula `FAB·grel ≤ 11.87` holds 0/6 with Spearman(grel, FAB |
family) = −0.623 — the gap geometry genuinely sets the q_max
scale, census-grade; the FRESH COUNT TEST (first EXT4/EXT5
measurement ever) holds 12/12 at the r329 frozen constants (min
reserves 1.59/2.77) — the O(log m) counting side choice-robust
on a THIRD consecutive fresh cohort.  **The floor holds at 1.05
but erodes:** cert2 True on all 28 family rows (min RSV 1.07,
kz75; the five EXT5 family rows at RSV 2.22..3.38 — no new
hole) but e_RSV = −0.649 and rc_fam351 = −0.600 (vs the r349
prior −0.331): the census extrapolation crosses RSV = 1 at
log₁₀ m ~ 3.7 — the r349 floor question is answered
NEGATIVELY, no stable floor > 1 certified; anatomy: the floor
rows are the largest-FAB deepest-pk spikes — the reserve dies
exactly where the law coordinate peaks.  **The composition
moves the honest uniform m₀\* by ~4 decades:** the class-free
polylog route `ρ₂ ≤ C_FAB·C_M2ENV/log m` (14.93 × 26.01)
solves **m₀\* = 10^18.9 UNIFORM** — no spike/quiet split — vs
10^22.6 (r349 record) / 10^23.5 (the moved census-F ceiling) /
10^16.1–10^17.5 (class-conditional, non-uniform) / 10^13.5
(r306 census).  Cofinal typing: C_FAB/C_M2ENV are freeze-census
constants (the ladder-to-m₀\* step stays the extrapolation
hypothesis), the eroding floor is the open spike-arm need, the
source formula is the open mechanism, and the next fresh teeth
need a NEW construction family.  Experiments-side, NO ledger
row, NO RH CLAIM.

**The ρ_r source anatomy (r352, the named r350 follow-up: the
last census member of the closed L\* exponent chain, and the
g_K12 second-instrument lane).**  `rhor_source_anatomy_probe.py`
(33/33, SPEC_SHA `dc6bbd2cdfde8bbf` final with record, freeze
`ad7a56682b4ecfd7`, two-commit protocol: pre-freeze `88aae425`,
record `eb794e3a`; ONE disclosed print-only amendment a1 — the
EXT5 in/low band ledger field, the r349 every-hole-named
precedent, no bar or rule moved) put ρ_r = 2.624 — the
cancellation exponent of the bare reserve `r_det = 1 − c²/pq`,
the single non-dictionary non-theorem non-candidate block of the
r350 chain — under sealed decomposition through the WEIGHT-FREE
kernel correlation `ρ_K = K12²/(K11·K22) = c²/(d1·d2)` (the
weights cancel exactly), with the exact identities `c² == ρ_K
d1 d2`, `r_det == 1 − ρ_K d1 d2/(pq)` and the additive split
verified at machine precision on all 81 rows and in exact
Fractions on the r342 hand toy.  **Verdict `RHOR_REDUCED`
(one-object grade) + `RHOK_LAW_FOUND` + `DECOR_REFUTED` +
`GK12_EXPLAINED` + `CANDIDATES_UNRESOLVED`:** the leading laws
CANCEL (|s_csq − s_pq| = 0.0004 — ρ_r is a SECOND-ORDER object,
not composable from the candidate laws), and at the sealed
common leading law A_LEAD = 17/12 the deficit fine structure
`log(pq) + A_LEAD·lnN` and the kernel fine structure `log(c²) +
A_LEAD·lnN` are **ONE SHARED WANDER** (corr 0.999998; each
wanders 0.8787 nats, their difference is 0.0017 nats — 500×
smaller) whose difference IS the log reserve pointwise: **ρ_r is
exactly the decay of the shared-wander difference — the two
named r350 rests are ONE object** (|s_LR − s_rdet| = 0.0002; LR
curv −0.767 == rdet curv: no clean power law in the weight-free
normalization either — a reduction AND identification, NOT a
source derivation of 2.624).  The round's naming hypothesis is
refuted cleanly: `1 − ρ_K` saturates to 1 (slope +0.0006) — the
kernel DEcorrelates; the carrier is the saturation of c²/pq.
The κ law re-gates CLEAN (a_κ 0.7111, hits [2/3, 3/4] mutually
unresolvable) and ρ_K inherits a_ρK = 2a_κ = 1.4222 exactly.
**g_K12 is EXPLAINED:** the one dirty r350 column factorizes
pointwise as `K12 == c/√(v1·v2)` (recon 5.5e-4) — the CLEAN c
law over the closed-form dictionary weights; the CD-recursion
SECOND INSTRUMENT reproduces the Gram route on all 81 rows (max
7.4e-10 incl. N_w 5690) with an identical refit law (1.5e-11):
the dirtiness is a STRUCTURE effect, not a route effect; REL2
honest-negative (`K12/(K11 K22)^{1/4}` fails the r345 flat
protocol loudly, 1.21 dec — the r350 slope hit 0.035 was an
after-fit artifact).  **EXT5:** the r343 selection rule at the
raised h cap (3400, 6000] yields kz 69/107/101/99/115/89 with
N_w 4237..5690 — **the deepest L\* windows ever measured (1.8×
the EXT4 record), margins ALL POSITIVE** (1.5e-9..4.0e-9); the
bare laws p/q/c/κ extend in-band while margin/reserve/K12 sit
uniformly HIGH side of the 57-fit: the deep decay FLATTENS out
of sample (the opposite side from the r342 EXT3 steepening —
census, the running-exponent question named for r353).  **No
candidate ambiguity resolves** (required depths log₁₀ N\* =
29.5 / 8.3 / 4.7 for a_p / a_q / δ₀ — the ladder-depth
arithmetic is the deliverable; the closer-count leans, incl.
0.62 OVER 2/3 for a_q, are census, never identifications).  The
balance re-gates at dev 0.001 and **the specialist package is
FINAL: ONE object** (the r338-q1 backward-CS fine structure =
the shared wander φ, rms 0.88 nats — the single unexplained
function of the L\* margin legislation), all exponents measured,
all identities exact.  Experiments-side, NO ledger row, NO L\*
claim, NO RH CLAIM.

**The second construction family + the preregistered erosion
kill (r353, the named r351 follow-up: frame-B, the
half-resolution tent frame).**
`second_family_erosion_probe.py` (45/45, SPEC_SHA
`bd89e3316c332ded` final with record, freeze
`2c0e1c150b5721a8`, two-commit protocol: pre-freeze `ac4fbe28`,
record `b5e7f892`; NO amendment after freeze; the pre-spec
scoping disclosed: pool enumeration at NU ∈ {2, 6, 8} + two
wpack timings + the NU = 4 reproduction check only, no bound
value computed) freed the ONE construction parameter every
round r238–r351 had held fixed — the window aspect `NU` in the
mesh `D = 0.5·gap/NU` — and built **frame-B (NU_B = 2)** on the
canonical von-Mangoldt comb (no smoothing; tent assembly,
archimedean lags, chain machinery verbatim; the NU = 4
reproduction ward is EXACT: bit-identical wpack on w9, pool ==
`frame_a_zones` 70/70).  The sealed selection (used ledger 104,
fresh 24 at h_B ≤ 4000, strata BZ in-zone grel-asc kz69/kz80 —
the in-zone frame-B pool has EXACTLY 2 members — + BD deepest
kz133/129/124/117/107/101) admitted **8/8 with zero queue
failures** (POSITIVE_PREFIX + chain-complete, N_w 1792..3972 —
the r329 frame-A admission boundary nf 2125..2468 does NOT bind
the half-resolution frame); every admitted row is SMALL-gap and
SPIKE, and the family sets the lane depth record **m = 812
(log₁₀ 2.91)** vs the frame-A max 660 — the crossing target
3.7 is NOT reached (lever extension, disclosed up front).
**Verdict `SECOND_FAMILY_BUILT` + `FAB_LAW_BREAKS_ON_B(kz117
17.78, kz124 18.07)` + `FLOOR_KILLS(kz124 RSV 0.63, kz129
0.95)` + `GREL_LOWER_BOUND_CANDIDATE(0.187, 63.4)` +
`BZ_POOL_EXHAUSTED(2)` + `NEW_DEPTH_RECORD(812)` +
`NEW_FAB_RECORD(kz124, 18.07)`:** (1) **the r351 FAB ceiling is
a per-family census, not a cross-family law** — kz124 posts FAB
18.07 and kz117 17.78, both above the frozen C_FAB = 14.93 (up
to +21 %), and the combined SMALL-gap trend rc_small = +0.569
crosses the +0.5 growth bar for the first time; the law keeps
its FORM on frame-B (C' = 18.07) but the frozen constant is
family-indexed.  (2) **The preregistered kill FIRED — earlier
than the extrapolation predicted:** kz124 (m 757) RSV 0.63 and
kz129 (m 787) RSV 0.95 breach RSV_KILL = 1.00 (kz133 at 1.00,
bar miss) — the sliding spike coverage `GSQ·F² ≥ ρ₂` is FINITE:
it dies at m ~ 760 on the second family, not at the
extrapolated m ~ 5000 (combined 36-row fit e_RSV −0.889,
rc −0.706, crossing log₁₀ m ~ 3.4 — the erosion ACCELERATES
cross-family); the r346/r349 three-arm cover is hereby bounded
to the measured frame-A range and the cofinal reading needs a
FOURTH mechanism (or a family-indexed sliding constant — both
typed).  The kill rows are again the largest-FAB rows: the
reserve dies exactly where the law coordinate peaks, now on
both families.  (3) **The K2 Klein-gap product is the
cross-family survivor:** `FAB·grel ≤ 11.87` holds 0/8 on
frame-B (max 5.95) — the only frozen constant of the lane that
carries across the aspect change; g_min = 0.187 gives the first
non-vacuous implied ceiling 63.4 ≤ 4×18.07
(`GREL_LOWER_BOUND_CANDIDATE`, census).  The r329 counting
constants hold 8/8 (reserves 1.61/2.79) — the O(log m) counting
side survives its FOURTH fresh cohort and FIRST cross-family
test.  (4) The synthesis moves the ceilings and m₀\* backwards
honestly: C_FAB' = 18.07, C_M2ENV' = 44.18 → the class-free
polylog m₀\* = 10^20.5 (+1.6 decades vs r351).  Worlds: w9B
1.53 / w13B (twin) 1.64 — the twin protocol carries to frame B;
the frame-B SCRAMBLE control breaks AT ADMISSION (nf = 3).
Honest negatives: frame-B is a second CONSTRUCTION on the same
source comb, not a second arithmetic world; the depth gain is
0.09 decades; kz69/kz101/kz107 anchor zones were touched by the
parallel r352 L\*-lane EXT5 (margins only, a different window
construction — anchor-zone overlap disclosed, no law column was
shared).  Experiments-side, NO ledger row, NO RH CLAIM.

**The φ-wander anatomy (r354, the named r352 follow-up: the
single unexplained function as its own lane, plus the
running-exponent model of the EXT5 high-side flattening).**
`phi_wander_anatomy_probe.py` (33/33, SPEC_SHA
`f9db84da7f0f6f6e` final with record, freeze
`c37ac54e9cbe41e9`, two-commit protocol: pre-freeze `8b1361e9`,
record `4be9d3a6`; TWO disclosed calibration amendments a1/a2 —
measurement-scale/robustness class, no adjudication rule moved)
put the shared wander φ under sealed anatomy.  **Main verdict
`PHI_DICTIONARY_GO` — the φ lane is SOURCE-SIDE CLOSED at
computability grade:** the pointwise composition `c_pred =
√(v_pred1·v_pred2)·K12cd` (closed-form digamma/tent weights ×
the recursion-computable cross kernel, no measured kernel
column consumed) reconstructs c on all 85 rows at max 5.52e-4
and predicts the kernel fine structure at corr 1.0000000 / rms
ratio 0.0004 — honesty: a computability closure, NOT a closed
form and NOT a derivation of the wander.  **The atom
decomposition ends in a TWO-BLOCK INTERFERENCE reading**
(`PHI_CARRIER_CENSUS`): the pair-geometry composite P2/PG
carries the SHAPE (corr 0.887) at 2.4× amplitude while the
dictionary weight block is ANTI-correlated (−0.72) — φ is the
cancellation of a large pair-geometry wander against the weight
wander; no single block passes the sealed carrier clauses.  φ
is NOT a function of N alone (N-adjacency ratio 0.911; grel/lnz
do not carry) — the wander is pair-local.  **The
running-exponent model does NOT collapse the cohorts**
(`RUNNING_CENSUS`): the 0.88-nat wander defeats the 0.5-dec
band on margin/reserve/K12 regardless of the 1/lnN term;
s_inf(margin) = 1.65 vs 3.33 stays a FLATTER census (the
wall-friendly direction, not a law).  **EXT6:** the r343 rule
above h 6000 finds the pool EXHAUSTED at h 7942 — exactly 4
fresh windows (kz 133/129/124/117, N_w 6532..7942 = **the
deepest L\* windows ever measured, 1.4× the EXT5 record,
margins ALL POSITIVE** 1.13e-10..1.70e-9); the high-side
flattening CONTINUES AND SPREADS (now the bare p/κ laws sit
high too).  **δ₀ is UNDECIDABLE inside the document frame:**
the extended 28-row separation (y0 via the exact reduced route
`y0 = 1 + (u1·u2)/c`, warded 6.6e-14) moves the required depth
to 10^5.4 (pure) / 10^5.7 (running) while the pool ends at
10^3.90 — typed for the specialists; the a_q closer-count lean
to 0.62 over 2/3 is CONFIRMED (27/28, census).  First world
test of the fine structure: the φ coupling is NOT
live-exclusive where measurable (ABS corr 0.9988 at 3×
amplitude; DIR degenerate; SMOOTH/SCR below the usable minimum)
— only amplitudes separate, census; twin pointwise devs ≤
1.9e-7 nats.  The named rest is the two-block cancellation
ratio — the sharpest remaining form of the r338-q1 question.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**The K2 source formula: q_max from a lower gap bound (r355,
the reviewer fork after r353 — terminal lane, K2/Klein-gap
geometry only).**  `k2_source_formula_probe.py` (47/47,
SPEC_SHA `1f14bd938ba78cc4` final with record, freeze
`b0dd5a93a9d5b790`, two-commit protocol: pre-freeze `94f0683a`,
record `397a1032`; NO amendment after freeze; scoping
disclosed: NU = 3 pool enumeration — 16 fresh, in-zone EMPTY at
every aspect — + two admission timings, no bound value
computed) attacked the r353 cross-family survivor from both
ends.  **Verdict `K2_LAW_CERTIFIED_NU_FREE` +
`K2_SOURCE_CHAIN_OPEN` + `GMIN_LAW(e_g −0.252, mono 0.80)` +
`INZONE_EXHAUSTED_ALL_NU(0)` + `K2_TEST_MAX(kz103, NU3,
10.62)` + `GMIN_IMPLIED(NONE, e_impl +0.29)` +
`NU_RATIO_CENSUS(0.19)`:** (1) **K2 survives its SECOND
independence test — the window aspect:** the frozen C₂ = 11.87
(max FAB·grel over the 89 sealed r351 rows) holds with ZERO
violations on all 25 test rows — the 8-row frame-B regate,
12/12 admitted NU-test rebuilds of the sealed six zones
kz 111/75/51/65/79/103 at NU ∈ {2, 3}, and the 5/5 fresh
NU = 3 field kz 99/115/89/86/132 (N_w 2961..3805, 0 queue
failures); the closest call is kz103 at NU 3 (FAB·grel 10.62,
11 % below the ceiling).  The census contrast that makes this
meaningful: the bare FAB coordinate is aspect-WILD — kz99
posts FAB 19.38 at NU 3 (a NEW lane record above the r353
18.07) and kz103 jumps 3.69 → 12.98, while the median
FAB(NU2)/FAB(NU4) ratio is 0.19 — yet the K2 product absorbs
all of it: **the gap product is the aspect-stable coordinate
of the lane; the FAB ceiling is C(NU, family) census.**  (2)
**The source chain closes EXACTLY but its census caps are
vacuous:** FAB·grel ≤ (ngj/log m)·(hgn·grel) holds one-sided
exact on all 118 live worlds (r327 group chain), and the mesh
identity h − NU·u ∈ (0, 1.5] (u = α/gap, the NU-free depth
coordinate) is EXACT on every pool zone at all three aspects —
WHERE grel enters is now construction algebra (the Klein gap
sets the mesh depth); but the newly frozen caps C_H = max
hgn·grel = 141.71 and C_P = max pil·grel = 141.53 (both kz111)
imply ceilings 373.4 / 286.7 ≫ the a-priori bar 47.5 — the
r351 K3/K4 vacuity repeats at the grel-sharpened caps
(`K2_SOURCE_CHAIN_OPEN`; the chain loses too much at the
heavy-group step, bshare med 0.41 off-family).  The r329
counting constants hold on all 17 NU rows (reserves 1.35/1.81)
— FIFTH fresh cohort, FIRST aspect test.  (3) **The lower gap
bound is a slow measured law — but supercritical as a ceiling
route:** the g_min(u) curve over the 130 admissible zones (6
dyadic bins, minima 0.482 → 0.187, mono 0.80) falls at
halves-slope −0.252 (`GMIN_LAW`, census — the depth-gap
coupling partly builds this in, disclosed); the implied
exponent e_impl = −e_g/e_um = +0.286 > CRIT_EXP 0.224, so the
growing K2 ceiling C₂/g_min(m) yields NO m₀\* (supercritical);
the flat-floor route at the global pool floor 0.187 gives
C_FAB^K2 = 63.4 and m₀\* = 10^23.5 — 3 decades worse than the
r353 direct census 10^20.5.  Cofinal typing: SATZ links =
r324 identity + r327 group chain + mesh identity + dictionary;
CENSUS rest = C₂ (2 families + 3 aspects), C_NG, C_H/C_P
(vacuous), and g_min — **the whole spike mechanism now reduces
to the census-to-law promotion of [gap floor] × [counting] ×
[heavy-group mass], with the diophantine gap floor the named
rest** (no Baker bounds attempted — the r289/r331 lesson).
Worlds: w9B FABg 0.74 / twin 1.35 / EPSTEIN 0.41; frame-B
SCRAMBLE breaks at admission (nf 3, r353 reproduced).
Experiments-side, NO ledger row, NO RH CLAIM.

**Lane status after wave 13.**  **The terminal: the MEASURED
composition is the end state of the route** (r324
`PILEUP_GROWS_SUBCRITICAL` +0.172 < 0.224 record / 0.188
chain-honest per the r328B audit, `Σq³ ≤
8.941·(log m)·m^{+0.172}/m²` ⟹ the N₂ density need for m ≥ m₀\*
(record 10^59.6 at the atom-level need, chain-honest 10^238) — the
gap from 274 to m₀\* the disclosed extrapolation
hypothesis; the certified pieces: the O(log m) scale count C_NSC
2.0258 at 0/39 and the O(log m) group count C_NG 2.6351 at 0/39;
r327 anatomy SOURCE: the heaviest group is exactly ONE β/ω fold
pair on all 65 rungs, kz53 = one bulk/window coincidence at
88.8 %; **the named direction is the coincidence geometry** —
WHERE can the single heavy coincidence sit, a source-geometry
question, not group count or multiplicity; r337 probed the
reviewer's martingale second route — structure present, arm too
weak; r339 then re-formulated the terminal as the density
martingale + moment dictionary: the exact layer is theorem-grade
and the target reads `E[X_∞³] ≤ C(log m)^A`, but the worst-case
Γ budget is supercritical — `LOCAL_INFLATION_SUPERCRITICAL` —
so the named R341 form is Bellman with path-probability
weights, not per-level maxima; r341 then executed exactly that
form — the exact path layer (tilted tower, stopped
decomposition, ε-chain envelope, Φ–Γ identity, heavy hand-off)
is theorem-grade and path weighting deflates the worst case
21×, but `PATHWEIGHT_ALSO_SUPERCRITICAL` per the sealed tree:
no arm certifies on its own freeze — the R* = 3/2 stop sends
94 % of the cubic mass to the heavy arm (threshold-unstable vs
7/4), the good ε-chain misses by the single violator kz55, and
the Ψ-Bellman with prefactor 1 is denied mid-tree; the named
material is the R* mass balance and the kz55/deep-anchor freeze
structure; r344 then measured exactly that balance — the
mass-balance curve over the sealed grid (3/2 … 2) with the
arm-exponent crossing located in (12/7, 7/4), and the r337
complementarity form executed with the path-weighted machinery:
the three-arm min-coverage (hand-off freeze + ε-chain freeze +
the banked r321 sliding bound as third arm) certifies with 0
violations on the 51 test rows at EVERY grid point at a = 1,
composing to m₀\* = 10^22.6 < 10^59.6 — the first certifying
cover of the lane — but `TWO_SCALE_PARTIAL`: the sealed
argmin-max stop rule is not halves-stable (8/5 vs 7/4), the
partition is not hsh-identifiable, and the third arm is
load-bearing for the deep anchors (kz51 F_Amax 5.54 enters the
uniform constant); the named rests are the canonical stop
criterion and a source-side partition predictor; r346 then
canonized the cover — `COVER_CANONIZED + PREDICTOR_FOUND(P02)`:
the stop rule is carried by the DATA-FREE intrinsic pair-ceiling
formula `R_ALG = 4^(1/3) → 8/5` (certifies at a = 1) and by the
R-free envelope (certifies at a = 1, C_G_ENV drops to 0.4867 —
the threshold disappears by construction), while the exponent
crossing stays halves-invisible (K2/K3 stable only via the
no-crossing fallback, disclosed); the partition residue is
CLOSED — the one-feature rule P02 (F_A ≥ 1.5 → third arm, else
heavy) predicts a covering arm on 51/51 rows with EXT3 12/12
out-of-sample: the working partition is spike-vs-rest in F_A,
not heavy-vs-good in hsh; F_Amax is NOT uniformly defusable
(the six sharp spikes are third-arm-only at every a — honest
negative), so the uniform m₀\* stays 10^22.6 and the
class-conditional QUIET reading 10^16.1 carries a named 13-row
exception family; the named rest is the spike-free uniform
constant — or the derivation of the spike family's third-arm
coverage as a law; r349 then adjudicated exactly that
derivation — the sliding reserve factorizes exactly as
`(GSQ/B²)·(pk/M2q)·(pk·M2q/Σq³)` and the spike coverage reads
`ρ₂ = D·pk·(F_A·B)²` through the r324 identity: the RAW class
law `ρ₂ ≤ 1.3056·F_A²` on F_A ≥ 1.5 holds with zero hard
violations on all 23 family rows including six fresh EXT4
anchors (all spike-class, new F_ins record 6.68), the 13 r346
exceptions dissolve 13/13 and the hand-off is seamless — but
`EXCEPTIONS_REMAIN` by the sealed letter: the reserve floor
1.5 is undercut out-of-sample (kz111/kz75 at 1.11/1.07), the
reserve is flat-to-eroding in F_A, and the dominance contrast
misses its sealed bar (2.8× < 3.0) — the reserve IS the
concentration depth 1/(D·pk), the family F_A ceiling grows
out-of-sample (5.54 → 6.68), the uniform m₀\* stays 10^22.6;
the named rests are the stable reserve floor at the honest
~1.1 scale and the family growth law m·q_max ≤ C·log m; r351
then certified exactly that law on the convention-free
coordinate FAB = m·q_max/log m == F_A·B —
`GROWTH_LAW_CERTIFIED`: the frozen ceiling C_FAB = 14.93
(kz111) survives a fresh EXT5 tranche with zero violations
(the first uniform growth statement of the lane to survive
fresh rows; the in-zone fresh pool is now exhausted), the F_A
ceiling ticks up again (6.69) while the FAB ceiling stands,
and the class-free polylog composition moves the honest
uniform m₀\* to 10^18.9 — but `FLOOR_ERODES(10^3.7)`: the
reserve floor holds at 1.05 (min 1.07) yet erodes with depth
(e_RSV −0.649), so the r349 floor question closes NEGATIVELY;
the named rests are the source formula for the FAB ceiling
(K3/K4 vacuous, the Klein-gap census formula FAB·grel ≤ 11.87
as the lead) and the eroding spike-arm reserve).  **The extraction:
the architecture stands** (r325 `ELEMENTWISE_STABILIZATION_GO` +
r326 `RH/Elementwise.lean`: `sourceExact_buildPrimeWindow` PROVED,
the comb stabilization elementwise PROVED,
`weil_nonneg_of_windowlocal` PROVED — extraction without the
ladder, H_cof replaced as the target route; r376: pole
stabilization PROVED, completion a named Prop; **1 typed Level-C
rest**: the arch kernel transcription (classical; Gauss/Mellin
absent from mathlib v4.29.1)).  **L\*: reopened as the capacity fork** (the r323 fork was cleanly
aborted at the end of its design phase, before any write access —
nothing counted as a round; r334 reopened the lane under the
capacity language and measured its ceiling: `ALLSET_NEEDED` +
`CAPACITY_CONTENT` — the route cannot out-margin the spectrum,
its honest yields are the interval world-discriminator and the
new near-wall coordinate 1 − κ_int; the L\* contract itself
stays [O], nothing moved; r336 then executed the last
pre-authorized arm, the Chebyshev T+H parity section: the exact
parity-section coordinate is certified and banked, but kill test
2 fails — `PARITY_WORLD_BLIND` — and the blind predictor is
ordering-grade only, so the parity lane does not stay open as a
proof arm either; r340 then probed the reviewer's post-cap
transport architecture — the weighted Cauchy–Binet/Hall
transport, no norm bound — and the interval-Hall reduction is
refuted on exact small models (`CUT_REDUCTION_FAIL`), with the
structural finding that the shallow-edge prefix of every world,
MAIN included, is locally indefinite: the wall is a global
rescue, not a local edge property; r342 then solved the r338
two-atom extremal as its own problem — `PAIR_LAW_FOUND`: the
three binding-point scalars (d₁, d₂, c) carry stable laws incl.
the EXT3 pure test, their weights are closed-form source
objects (digamma dictionary + exact tent closed form), the α ≈
3.3 decay is their bookkeeping-exact composition with the open
remainder ρ_r = 2.624, and the union {PR ≥ 3} ∪ {κ_int ≥ 1} is
the first measured world-complete criterion (κ_int alone
suffices; SMOOTH 2.193 / HL2 1964 first evaluated); the Schur
dressing names the R343 coupling-control coordinates (rest
margin ∥ full margin, dressed reserve FLAT ~0.3); r343 then put
the dressed reserve under fire — no family refutes it (EXT3
blind 12/12 in band incl. the kz56 breaker, six fresh EXT4
windows to N_w 3181 in band), but the sealed flatness clause
fails on the halves-curvature bar, so the letter of record is
`DRESSED_RESERVE_DECAYS(soft)`; the triangle/operator bound
chain is measured DEAD on all 75 rows (the dressing is a signed
cancellation Δc ≈ −c — the typed specialist question), `r'_det`
is gated a TOP-2 spectral object (its flat content = the flat
gap ratio g21 ~ 8), λ_rest alone separates the six worlds, and
the rest block peels as a two-atom extremal again
(`PEELING_STRUCTURE_FOUND`, level-2 grade); r345 then promoted
g21 + the top-2 geometry to primary coordinates —
`GAP_RATIO_PRIMARY_CERTIFIED` under the a-priori-sealed
curvature-honest flatness protocol (both candidates pass with
zero band outliers on 75 rows while the old halves-curvature
clause fails both bit-near: the r343 soft decay was a protocol
artifact), the exact two-level formula `r'_2 = g21(t₂−t₁)²/
((g21+t₁²)(g21+t₂²))` gated 75/75, the concentration-weak kill
survives (kz44/kz59, absorbed by K ≤ 3), and the signed
cancellation is now a measured law — `CANCELLATION_LAW_FOUND`:
`c'/c ~ N_w^−2.67`, the rest space mirrors the pair cross-term,
with the finite-order mirror bounded exactly on the live worlds
and divergent on all dead ones; r347 then closed the exponent
accounting — `ALPHA_CLOSED`: through the exact one-line identity
`m2'(p'+q'−m2') = p'q'·r'_det` with the protocol-graded bridge
`m2' == margin` and the certified flats, the margin exponent
REDUCES to the one line `α = a_c + δ` (3.332 vs 0.697 + 2.668,
residual 0.033 ≤ 0.1) — the open analytic remainder of the
margin law shrinks from three exponents to the single
cancellation exponent δ, itself still a measured law; the
Dirichlet second worlds enter the lane for the first time and
type DEAD-side under the sealed mirror clause; r348 then put δ
itself under source anatomy — `RATE_EQUALITY_THEOREM`: under
top-2 dominance with flat geometry every dressed scalar is
margin × an O(1) geometry factor (two-level identity, Fractions
exact), so `δ_x = α − a_x` exactly — the margin-pinning ratios
p'/m, q'/m, |c'|/m are certified flat on 75/75 rows and δ == α −
a_c loses its independent-law status: the irreducible measured
rest of the margin law is the pair {α, a_c}; the order-0
hypothesis is refuted honestly (δ₀ = 0.401 ≠ δ: the cancellation
law is an inter-order near-cancellation of twin slow laws, not
an order-0 property), and the weight side of the order-0 overlap
is dictionary-explicit (`DICT_T0_GO`); r350 then put the kernel
side itself under sealed anatomy — `ALPHA_SOURCE_CLOSED` at
candidate-law grade + `PINNING_THEOREM`: K_N at the pair atoms
is source-computable from the μ-chain recursion (CD ward
1.2e-10), the diagonal kernel growths reduce to the reciprocal
dictionary weight laws (Christoffel saturation), the pinning is
algebraic (`m2'₂ == margin` identically and `p'q' − c'² ==
margin²·g21/Δt²` exact in Fractions — the near-cancellation is
resolvent self-consistency), and the exponent chain composes
source-side with ONE census member (α == 3/4 + 2/3 + ρ_r −
a_(p+q), dev 0.019; the deficit candidates a_p = 3/4 and a_q =
2/3 are sealed hits with printed ambiguity, never an
identification); the named rests are the cross-kernel growth
g_K12 = +0.902 (the one dirty census column) and ρ_r = 2.624;
r352 then decomposed exactly that last census member —
`RHOR_REDUCED` (one-object grade): through the weight-free
kernel correlation ρ_K = c²/(d1·d2) the leading laws cancel
exactly-near (BK3 image, 0.0004) and the deficit and kernel fine
structures are ONE SHARED WANDER (corr 0.999998, 0.88 nats each
vs 0.0017 nats difference) whose difference IS the log reserve:
ρ_r is the decay of the shared-wander difference — **the two
named r350 rests are ONE object** (a reduction and
identification, not a derivation; LR curv −0.767 stays); g_K12
is EXPLAINED (K12 == c/√(v1v2) pointwise, the CD second
instrument identical on 81 rows, REL2 honest-negative), the
naive decorrelation carrier is refuted (1 − ρ_K saturates), the
EXT5 tranche holds L\* at the deepest windows ever (N_w 5690,
margins positive, the deep decay FLATTENS out of sample), no
candidate ambiguity resolves (required depths 10^4.7..10^29.5
printed) — the specialist package is FINAL: one object (the
r338-q1 shared wander φ), all exponents measured, all identities
exact; the L\* contract still [O]).  **Lean: 8 sorries, all typed** (the
five window-local legacy sorries byte-identical — the two true
WINDOW-LOCAL holes `lstar_subordination` +
`terminal_positive_main` unchanged — plus the three named Level-C
statements; census 5 → 8, the wave-12 census reservation partially
discharged).  The window-local positivity premise is proved
NOWHERE.  The mincut (base 4 / refined 5) is unchanged.  NO RH
CLAIM.

**Lane status update (r354, additive).**  The L\* fine-structure
rest is now typed one level deeper: the shared wander φ is
POINTWISE PREDICTED by dictionary weights × the
recursion-computable cross kernel (`PHI_DICTIONARY_GO`,
computability grade — not a closed form), its anatomy is a
two-block interference (pair geometry vs weights), and it is
pair-local (not N-alone, not gap-class/prime-size carried); the
EXT5 high-side flattening survives a sealed two-parameter
running-exponent adjudication only as census (the wander defeats
the band), continues on the fresh EXT6 tranche (deepest windows
ever, N_w 7942, margins positive), and the δ₀ candidate
separation is UNDECIDABLE inside the document frame (pool
exhausted at 10^3.90 vs required 10^5.4) — the L\* contract
stays [O]; the mincut is unchanged.  NO RH CLAIM.

**Lane status update (L\* freeze, 2026-08-27, additive).**  **L\*:
FROZEN as specialist problem (reviewer decision, Aug 27): one object
— the φ co-wander cancellation; see
`rh/problem/lstar_problem.tex` §frozen** ("The frozen state
(August 2026): one object").  The reviewer adjudication: the lane is
compressed to the point where additional internal numerics adds
little — the memo carries exactly the one object (the deficit and
kernel fine structures at the common leading law `A_LEAD = 17/12`
are one shared wander of ~0.88 nats each, corr 0.999998, whose
difference of ~0.0017 nats — factor ~500 — IS pointwise the log
reserve, with ρ_r = 2.624 its decay) and the question why the two
blocks (pair geometry, corr +0.887 at 2.4× amplitude, against the
anti-correlated dictionary-weight wander −0.72) cancel so precisely,
plus the three specialist questions (q1 backward-CS = the
cancellation ratio; q2 sub-classical Christoffel growth, candidates
unresolvable below 10^5.4+; q3 the resolution paradox) and the
honest frame (census on 85 finite windows up to N_w 7942, all
margins positive, pool exhausted at 10^3.90).  Documentation move
only: no probe, no marker, the L\* contract
`PRIME.LSTAR.SUBORDINATION.01` stays [O], the history above is not
rewritten.  Memo sharpened with literature placement (Aug 27
evening, additive): the closing subsection "Placement in the
literature, and addressees" adds the multi-point Uvarov-transform
dictionary, the discrete-hard-edge / saturation-regime
classification (decorrelation and rescaled positions measured,
saturation adjacency marked as hypothesis) and the four addressee
communities — no new claims.  NO L\* CLAIM, NO RH CLAIM.

**The Borodin dual-hole round (r356, the ONE approved internal L\*
round after the idea search — then the lane is final at the memo).**
`borodin_dual_hole_probe.py` (34/34, SPEC_SHA `36141c0ae9ed8f35`
final with record, freeze `5d277d576df75d3a`, two-commit protocol:
pre-freeze `58bb09bb`, record `5d351e90`; ZERO amendments after the
freeze — calibration pass 1 = first full evaluation = 34/34)
executed Sol's Borodin particle-hole contract plus Fable's AC-class
falsifier.  **Verdict `DUALITY_REPARAM_ONLY` + `AC_CLASS_EXCLUDED`
+ `ANTI_DESIGN_GATED` + `RESERVE_LOCALIZED`:** (1) **the exact
algebra holds on the whole 85-row ladder** — lift to η = μ + ν,
Q = E(I+E)⁻¹ (Fractions exact, f64 ≤ 7.6e−12), Borodin
complementation at half filling S = 2N−1 (the support gate holds
BITWISE on 85/85: the union support IS the full folded cosine grid,
and the r228 half-filling law IS Borodin's rank condition), the
spectral map margin == 2 − 1/λ_min(R) — **L\* IS R > ½·I, measured
live** down to λ_min − ½ = +6e−11 at EXT6 — and the pair identities
c == ε₁ε₂(R⁻¹)₁₂, p == 2 − (R⁻¹)₁₁: the r342 pair block is exactly
the (1,2) principal minor of 2I − R⁻¹; the reciprocal weight
u∨ == c_j(1−x)/|f| is exact including the endpoint halving; (2)
**the r354 anti-correlation is duality algebra by design** —
corr(ψ₅₇ DW, ψ₅₇ W) = −0.999998 gated (+log|f| vs −log|f|); (3)
**no compression:** no dual block (DW/DK/GC) passes the sealed
carrier clauses and the compression clause against the in-run r354
four-block base does not fire (the near-tautological sum block
DW+DK = log c² − GC was excluded by design) — the duality is a
reparametrization; **the L\* lane is FINAL at the specialist
memo;** (4) **census-grade positive finding `RESERVE_LOCALIZED`:**
the LOCAL dual 2×2 block (R_pair)⁻¹ predicts the log reserve
without p/q/c readback and without global inversion (corr(ψ₅₇)
+0.9982 / leave-out 0.068 on the 57; EXT puretest +0.9828 / 0.165
on the 28 deep rows) — the 500× cancellation is carried by the
local dual two-point data; (5) **`AC_CLASS_EXCLUDED` for the
memo:** rescaled pair positions family-constant against π²f²/4
(folds (2,4) uniform, 85/85) while a_ρK = 1.4222 == the r352
record where the Lubinsky-type AC/Bessel class demands
ρ_K → const — the window-kernel universality class is NOT the AC
class; (6) **demarcation vs r227/r228 machine-checked:** the old
signed-Hankel duality died on zero weights (`R_DUAL_OBSTRUCTED`);
the positive lift removes the obstruction structurally, and the
`DUAL_WALL_EQUIVALENT` risk materialized exactly as the enum
anticipated — typed, not hidden.  Worlds: MAIN mini gate passes,
all four ladderable dead worlds LOSE (the reserve cone is empty
off the wall; λ_min(R) − ½ ∈ [−0.500, −0.083] vs MAIN positive),
twin dual-pointwise 7.8e−4 nats; the EXT6 f64 sign truth is
disclosed (the dual margin route cannot certify the ~4e−10 deepest
signs).  Experiments-side, NO ledger row, NO L\* claim, NO RH
CLAIM.  **R356 dual-hole addendum (memo, additive):** the frozen
memo `rh/problem/lstar_problem.tex` §frozen now closes with the
round-356 addendum — L\* ⟺ R > ½·I (exact equivalent form via
Borodin's particle–hole duality), the anti-correlation is by
design (duality algebra), the reserve localization as census —
the lane is finally at the memo.

**The GRH-faithful matched Dirichlet frame (r357, the reviewer
rank-2 fork — the missing second arithmetic, r338-Ü5 executed).**
`dirichlet_matched_frame_probe.py` (33/33, SPEC_SHA
`4bf1a94b03c7d227` final with record, freeze `4be4777fd6ec5bdf`,
two-commit protocol: pre-freeze `1381f6ea`, record `a953ab29`; one
disclosed calibration amendment a1 — the r330-a1 representation
lesson on the r329 counting literals, no adjudication rule moved)
built the matched Dirichlet window: from Λ(s,χ) =
(q/π)^((s+a)/2) Γ((s+a)/2) L(s,χ) the arch density F_A^χ(ξ) =
−log(π/q) + Re ψ((1+2a)/4 + iξ/2) — in lag space EXACTLY the
document arch body with kernel e^(−w/2) → e^(−(1/2+a)w) and
constant −(γ+log π) → −(γ+log(π/q)); trivial frame (a = 0, q = 1)
reproduces zeta's layers BITWISE; matched border companion; χ mod
3 primary (the r330 comb bitwise), χ mod 4 census.  **Verdict
`SECOND_ARITHMETIC_LIVES` + `MECHANISMS_TRANSFER(TWO_ATOM,
DET_COND, DICT)` + `K2_CENSUS` + `DICTIONARY_TRANSFERS` +
`PHI_CENSUS`:** (1) **the r330 death was a FRAME ARTIFACT** — on
the matched frame the χ mod 3 world holds the E-Gram wall on
42/42 windows (margins 8.1e−6..3.3e−3 all positive, minC None)
AND the terminal half-filling wall (nf None 42/42 — the same comb
that died at nf 24 unmatched, baseline-gated); χ mod 4 identical:
the living-world evidence moves from n = 1 to n = 3 arithmetics
on 126 windows; (2) the **verbatim r330 battery re-adjudication**
retypes ALL FOUR r330 splits as frame artifacts (HALF_FILLING,
RENYI3_C2 32/42→0/42, SIGMA_DECAY +0.79→−0.578, O_SIGN — battery
7/7 MAIN-side, both characters ALIVE); (3) **pinning fine
structure** (fresh coordinate): MAIN pins at minC_ext == N_w+1
exactly, the χ worlds are near-pinned (offsets 0..9, med 1.5) —
the exact pinning is so far zeta's sharpest signature; (4) **K2
splits**: the frozen C₂ = 11.87 holds 0/126 (the Klein-gap
product is arithmetic-robust census — 2 families + 3 aspects + 3
arithmetics) but the r329 counting constants BREAK on the second
arithmetic (up to +28 pct) — the O(log m) counting side is
zeta-calibrated census; (5) **the r342 weight dictionary
transfers** with the χ offset (median 4e−4 over 42 rungs); (6)
**φ does NOT transfer** (honest negative): co-wander suppression
3× vs MAIN 439× on the identical instrument — the χ pair sits far
from the binding point (r_det med 0.247): the 500× suppression is
the signature of near-cancellation, which only zeta exhibits at
these depths — information about the binding regime, not the
frame; (7) controls: rational χ twin carries (7.9e−6),
matched-frame scramble breaks.  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM, NO GRH CLAIM (GRH motivates the
candidate, used nowhere).

**The weighted small-gap Carleson packing (r358, reviewer
contract T1 — the theorem-first replacement of the global
minimal-gap composition).**  `local_gap_carleson_probe.py`
(20/20, SPEC_SHA `fb2d499fd984cef3` final with record, freeze
`8831b1410849f1b4`, two-commit protocol: pre-freeze `9141d3e7`,
record `f0f034a2`; NO amendment after freeze) built the sealed
local gap coordinate — block centers of the r314 fold groups on
the θ grid LL = 4N−2 (positions + block ids only), one-sided min
gaps in grid units, `EFA.grel_col` normalization verbatim (the
zone-grel convention one level down), q_i = |x_i|/L (the r339
FDD leaf convention); the mesh identity h − NU·u ∈ (0, 3/2]
re-warded exact — the coincidence is mesh-parametrized, fit-free.
**Verdict `QUADRATIC_LAW_PARTIAL(T1@all four)` +
`SIEVE_CORE_OPEN`** on 181 rows (89 frame A + 8 frame B + 42 χ3 +
42 χ4; anchors bit-near: C_K2X 11.87 at kz111, the r353 frame-B
table, the r357 χ maxima): (1) **the core holds — T2′ is a
0-violation census theorem on all four arithmetic/family
worlds**: the quadratic packing law Σ_{g_i ≤ 2^−r} q_i ≤
2^{−2r}(1+r)² holds pointwise on all 181 rows at every dyadic
level r = 1..12 with A-PRIORI bars (no calibration); the whole
small-gap mass lives at r = 1 (max S₁ 0.017/0.005/0.024/0.044
per family), S_r = 0 identically for r ≥ 2, and the minimal
normalized local gap of the entire round is **0.375** — gaps
below one quarter of the local median DO NOT OCCUR in either
construction family or any of the three arithmetics: "very tight
coincidences may exist, but not with mass" is measured, and
stronger — below g = 3/8 they do not exist at all; T2 census
C_G = 0.100 at A = 2 (dyadic summation T2′ ⇒ T2 warded exact);
(2) **T1 is depth-graded census, not a first-K law** (the honest
partial): the r306 first-K freeze fails the localization on ALL
FOUR families (frame A C_K 2.45 vs 15.93 at kz111; frame B 4.91
vs 23.70 at kz117, 6/6; χ3 1.52 vs 3.91; χ4 1.62 vs 3.09) — the
local product grows with depth exactly like the K2 product (the
max rows ARE the K2 spikes): the localization is the right
coordinate, a shallow-rows freeze is the wrong constant rule at
every level; the packing FORM is the family-robust statement;
(3) the small-ball band structure (D) carries as census (1033
bands, 0 violations; the stress spikes kz51/kz111 have NO
sub-half gap — spike atoms are not tight-gap atoms; band
comparability holds in MASS form, not signed-survival form);
(4) the composition is pure polylog but census-expensive: m₀* =
10^23.5 vs r351 10^18.9 / r353 10^20.5 (C_K enters squared) —
the two NAMED open items: the in-the-mean small-ball sieve on
the folded log p^k phases (per dyadic source band, no pointwise
Baker bounds) and a family-uniform T1 constant rule; (5) all
three matched scrambles break at the named precondition P1 =
POSITIVE_PREFIX admission (nf 21/3/37 — the r353/r355/r357
records); twin 1.0e−7; must-fails e1–e5 + m6a/m6b caught (e2 =
the r355 global-min error reproduced as a mutant, breaking the
sealed bar where the true column passes).  Experiments-side, NO
ledger row, NO RH CLAIM.

**The exact critical Schur block in the positive dual space
(r359, reviewer contract L1 — the favourable pre-attempt before
the RHP project).**  `schur_wronskian_dual_probe.py` (33/33,
SPEC_SHA `d00fdc96a3667a52` final with record, freeze
`f42fa664e6970863`, two-commit protocol: pre-freeze `ad74f3e0`,
record `b96f819d`; two disclosed calibration amendments a1/a2 — a
bar re-size inside the disclosed 1/eps noise class and a
census-label representation split, no adjudication rule moved)
built the exact Schur split of the r356 dual condition L\* ⟺
R > ½·I at the critical fold pair (2, 4): with M = R − ½I,
{M ≻ 0} ⟺ {M_CC ≻ 0} ∧ {S_N ≻ 0} plus the exact identity chain —
Sylvester bordered minors ((S_N)_kl·det M_CC == det M_{C+k,C+l},
the reserve as a ratio of bordered minors with the rest block
inside the border), the CD/Casoratian structure of R in the two
consecutive dual orthonormal polynomials, and the discrete IIKS
commutator identity: **the off-diagonal of the dual resolvent
(I − 2R)⁻¹ IS the Casoratian of resolvent-dressed consecutive
dual OPs** — all Fractions-exact on a rational model and graded
green on 85 MAIN + 42 χ3 + 42 χ4 rows.  **Verdict
`ASYMPTOTICS_REQUIRED` + `STURM_CENSUS`:** (1) **the binding
thesis is the round's sharpest measurement** — bind =
λ_min(S_N)/(λ_min(R)−½) ∈ [1.0003, 1.0605] med 1.0058 on the 74
resolvable rows: the critical 2×2 Schur block CARRIES the full
L\* margin (det S_N tracks margin², slope −6.742 vs −6.665); (2)
**no standalone explicit P_N exists** at the sealed bars: the
Christoffel-class candidate misses by ~14 orders, the diagonal-
parametrix form misses by exactly the measured cross share (med
0.702 — the off-diagonal Casoratian term carries 46..84 % of the
resolvent minor and cannot be dropped); P_N is NOT a margin
readout (restatement census corr +0.9924 < 0.999): the named
next step is L2/CRITICAL_SATURATION with the precise object —
the diagonal dual-resolvent pair data (A⁻¹)_kk — and the cross
share as handoff; (3) **the Sturm sign pattern is
near-wall-graded, not universal**: 84/85 MAIN rows sit in one
pattern (pair straddles one zero of each consecutive dual OP,
interlaced; ρ = p_{N−1}/p_{N−2} monotone; dressing
sign-preserving; P_N > 0; the single deviation kz133 is the
disclosed r356 f64 sign-resolution row), but far from saturation
P_N < 0 on 12/42 (χ3) and 13/42 (χ4) rows — a globally positive
standalone P_N is excluded at census grade, the universal Sturm
carrier is refuted, the near-wall pattern is banked with the
named theorem type (discrete Sturm interlacing /
Markov–Stieltjes); (4) **the rest clause (the reviewer's L2
clause) is measured**: λ_min(R_CC)−½ positive on every live row
but DECAYING PARALLEL (slope −3.276 vs margin −3.332, rest/eps
med 20.3) — the L2 rest-block clause must be phrased relatively;
(5) **the matched scramble breaks at the named precondition**:
R_CC ≻ ½I fails (−0.4962) while every algebraic ward passes and
the pair Schur block alone stays positive (+1.37e−2) — the
identity chain is world-blind algebra, the positivity is
arithmetic, and pair-only reasoning would misclassify the dead
world (the m3 lesson measured on a world).  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.

**The critical saturation scaffold (r360, reviewer contract L2 —
the RHP scaffold at the critical pair, triggered by the r359
`ASYMPTOTICS_REQUIRED`).**  `critical_saturation_probe.py` (34/34,
SPEC_SHA `ea24936c46407f48` final with record, freeze
`75f8ee55436ab173`, two-commit protocol: pre-freeze `8a835dc8`,
record `130a0889`, ZERO amendments after freeze) built and
measured the scaffold for the reviewer's steps (B)–(D): the exact
**occupation duality** o_η + o_dual == 1 on every union node (the
diagonal of the r356 Borodin complementation, Fractions-exact,
≤ 2.2e−11 live, trace exact) and a sealed zero-temperature
**obstacle-problem solver** (BKMM constrained equilibrium with
field −log u∨, FISTA + water-filling, KKT gates).  **Verdict
`SATURATION_EDGE_CONFIRMED` + `GAMMA_PARAMETRIX_CENSUS` +
`M0_PARTIAL(3.332)` + `REST_RELATIVE_CENSUS`:** (1) **the
saturation thesis is confirmed at census grade** — the QP
dual-void block is EXACTLY folds {1, 2, 3} with clean KKT on 4/4
sealed instances (by the exact complement the PRIMAL saturated
block), so **the critical pair (2, 4) straddles the
saturation-block edge 3|4**; the exact-occupation fold-1 anomaly
census holds 85/85 (dev −0.333..−0.253, pair folds flat), and the
χ contrast is a DIFFERENT partition (0/42 + 0/42 anomalies, both
χ QPs occupy fold 1; the scramble is disordered) — the reviewer's
step-B object, world-separating; (2) **the parametrix datum is
margin-locked**: t_geo = eps·√((A⁻¹)₁₁(A⁻¹)₂₂) has slope −0.009
on the 57 and range [0.222, 0.287] on all 74 resolvable rows +
χ w9 in band; the resolvent diagonals carry the margin exponent
(+3.365/+3.292 vs 3.332), NOT the 0.38/1.79 weight families —
the Gamma-class DERIVATION stays open (step C); (3) **α is
settled, M₀ is not a constant matrix**: the fresh λ_min(S_N)
slope −3.334 hits the sealed margin candidate 3.332 at 0.002 and
rejects the s_∞ = 1.65 reading at 1.684; bind med 1.0058 == r359
(the margin direction collapses) but κ_S = λ_max/λ_min wanders
4.88× > 1.5 — **the full M₀ collapse is honestly refuted**: the
reviewer's L1 form needs a relative/projective formulation; (4)
**the relative rest clause is a theorem at c = 1 only** — Cauchy
interlacing + the Schur-complement eigenvalue inequality hold
exactly (toy + 74/74 live), MAIN carries c ≥ 8.8, but the χ
ladders dip to the interlacing line (rest/eps mins 1.0 on 3 + 8
of 84 rows): `RELATIVE_REST_CERTIFIED` correctly did NOT fire —
the c > 1 margin is NOT world-uniform; (5) **the wander
cancellation is measured**: corr(ψ57 log det S_N, −ψ57 log(a₁₁
a₂₂)) = +0.9835 with the cross-share term ~5× subleading — the
leading common wander cancels algebraically inside the adjugate
minor.  Reviewer-step typing (the specialist handoff): (A)
theorem (r356); (B) saturation edge confirmed census-grade, the
asymptotic equilibrium-measure theorem OPEN; (C) parametrix
census, Gamma derivation OPEN; (D) adjugate theorem + measured
cancellation + M₀ partial; (E) rigorous error OPEN.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**The mean sieve on the folded log-p^k phases, floor-first (r361,
PRIME.L2.MEAN_SIEVE.01 — the named theorem rest of the terminal
lane after r358).**  `mean_sieve_floor_probe.py` (21/21, SPEC_SHA
`1bec71757eb909d7` final with record, freeze `0dafa3b962e337b3`,
two-commit protocol: pre-freeze `7f17e3cf`, record `2d7d0376`,
ZERO amendments after freeze) adjudicated the central new
question BEFORE the sieve: is the r358 0.375 floor derivable from
the construction algebra?  **Verdict `FLOOR_THEOREM`** — it is:
(1) **the two-step chain closes pointwise on all 32 728 atoms of
the 181-row surface**: SEP-SATZ (exact Fractions, derived a
priori — adjacent block centers of n_i/n_j distinct theta-grid
integers on disjoint contiguous supports separate by ≥
(n_i+n_j)/2 grid units) holds 0/32 547, and MED-CAP med_i ≤
(8/3)·sep_i holds 0/32 728 with worst ratio **exactly 1.000
saturated at the floor atom** (χ4 kz53: gap 3/2, med 4 =
(8/3)(3/2)) — the constant 8/3 is tight, min g over the round is
**exactly the mesh rational 3/8**, and only 5 sub-half atoms
exist (3/8 ×2, 5/12, 5/11 ×2); (2) **the floor survives
arithmetic destruction**: all three matched scrambles break at P1
admission as sealed (nf 21/3/37) yet their partial builds carry
gap floors 0.778/0.421/0.750 — all ≥ 3/8 — and remain
grid-quantized (qdev ≤ 4.5e−13): quantization and floor are
fold-machinery CONSTRUCTION, not log p^k arithmetic; (3) **T2′
trivializes modulo MED-CAP** (S_r ≡ 0 for r ≥ 2 forced) and the
continuous-t sieve census (t = j/32) holds 0-violation on 181
rows × 16 t and 1033 bands × 16 t (mean headroom 0.0014); the
steckbrief reduces both open sieve parts to MED-CAP — the MV
large-sieve spacing input IS SEP-SATZ; (4) **the direct chain
pays 7.4 decades**: M₃ ≤ (8/3)²C_K²(log m)²/m² (C_G and two log
powers drop) gives m₀\* = 10^16.1 at the measured census ceiling
C_K = 23.70 and 10^10.0 rule-conditional at the per-family freeze
4.91 — the family-uniform T1 constant rule is now THE single
remaining quantitative rest of the terminal lane.  Disclosed
epistemics: theorem-grade = the pointwise chain closes on the
surface with a saturated, scramble-robust cap; the paper lemma
MED-CAP (why the 5-window median of block gaps never exceeds
(8/3)(n_i+n_j)/2) is the one remaining formal step.
A 2026-08-28 proof attempt (`rh/problem/medcap_lemma.tex`)
**reduces** that step and names the obstruction: SEP-SATZ is cut
geometry; tiling (empty≡0, hull-solid — census 134 windows /
15 428 atoms, 0 exceptions) forces gap_i = sep_i, so MED-CAP is
an order-statistic bound on the length sequence n_i; the tiled
composition n=(1,2,8^{10}) violates with ratio 16/3, so the
lemma is **not** interval geometry.  The saturating prefix
(1,2,6,5,4,4) at χ4 kz53 is the edge window (third-smallest of
five neighbour-gaps = 4 = (8/3)·(3/2)).  Remainder X_n: the
source n-sequence forbids a C2 jump at small-sep loci (sign-run
pairing of an arbitrary ± colouring does not).  11/11 machine
gates, `MEDCAP STEPS VERIFIED`.  Round 364 (`xn_invariant.tex`)
proves the pairing half of that remainder and names $V_2$ (local
$v_2$-spacing at the $x$-mask); on the 134-window surface $X_n$
holds (unique $(1,2)$ = the equality case).  Round 365
(`v2_regularity.tex`) anatomizes $V_2$ and fires the hydra ward
`REGRESS_DETECTED`: $V_2$ is the final named lemma of the chain;
the $3/8$ floor is a theorem of the construction *modulo* $V_2$.
NO RH CLAIM.
Experiments-side, NO ledger row, NO RH CLAIM.

**The augmented Borodin–Uvarov duality — L† as ONE dual object
(r362, the reviewer moonshot PRIME.LDAGGER.AUGMENTED_DUALITY.01).**
`augmented_borodin_duality_probe.py` (30/30, SPEC_SHA
`7d810a9ab7db5c67` final with record, freeze `83b97cd57563e737`,
two-commit protocol: pre-freeze `62ca2bfa`, record `b8adbf01`;
three disclosed calibration amendments a1/a2/a3 — a chi clause
retype forced by a real finding, a chi cancellation-class bar and
a twin-bar re-size in the disclosed r356/r359 noise class; no
MAIN rule moved, every MAIN gate passed at first evaluation).
**Verdict `AUGMENTED_DUALITY_EXACT(route ii)` +
`BORDER_IN_LOCAL_BLOCK`** — the moonshot core stands: with β =
b/√B_w the μ-orthonormal border ray, v = B_m β its node-side CD
image, γ = βᵀβ and D the r356 sign matrix, the bordered dual
resolvent **R† := [[R^{-1}, Dv], [(Dv)ᵀ, 1+γ]]^{-1}** satisfies
EXACTLY (Fractions on rational toys, graded green on 75 MAIN +
42 χ3 + 42 χ4 rows + the kz133 deep census): (A1) G† = D†(R†^{-1}
− I)D† — the r356 complementation extends to the augmented node
Gram; (A2) the spectral map margin† = 2 − 1/λ_min(R†); (A3)
**L† ⟺ R† ≻ ½I**; (A4) the Y-block of R† is a Sherman–Morrison
rank-1 deformation of R — the border is a rank-1
Schlesinger/Uvarov insertion at the DUAL RESOLVENT level; (A5)
L† ⟺ L* ∧ Terminal in dual coordinates (q† := γ + vᵀ(I−E)^{-1}v
== uᵀH^{-1}u/B_w frame-invariant == the r266 crit1 coordinate;
1 − q† == (5/7)(1−q_N)/B_w); (A6) **the border-Schur closed
form**: the Schur complement of R† − ½I onto the border
coordinate equals (1−q†)/(2(1+q†)) exactly, and by the Schur
quotient the SAME value is carried inside the local 3×3 block
(pair + border) — the border fiber is not appended after the
fact, it sits in the same local object; (A7) interlacing
λ_k(R†) ≤ λ_k(R) ≤ λ_{k+1}(R†).  Measured: bind† =
λ_min(S†₃)/(λ_min(R†)−½) ∈ [1.0003, 1.0608] med 1.0056 — the
augmented 3×3 block carries the full L† margin AND the terminal
fiber; the equivalence census is exact and TWO-SIDED including
six TERMINAL-DEAD χ rungs (q_N up to 1.33, λ_min(R†) − ½ goes
negative there exactly as the theorem demands — both truth
directions live on real windows); the kz15 compression
mdag/margin = 0.8716 shows the two lanes couple spectrally where
the terminal channel is tight; share† == the r359 cross share
(0.6990 vs 0.6973 at w9) — the rank-1 deformation does NOT move
the critical resolvent structure at the pair, so the r360
saturation lane can consume R† verbatim: ONE critical saturation
theorem for the bordered dual resolvent would close BOTH lanes.
Route adjudication honest: route (i), the literal virtual node,
is DEAD on the real windows twice (the border is not a point
evaluation — representability spread 56.8 at w9 — and every
border atom collides bitwise with a union grid node); it
survives as the exact toy bridge (single-atom border: the
(S+1)-node Uvarov complementation holds Fractions-exact at the
SHIFTED rank N, S† = 2N — the half-filling arithmetic moves by
exactly one — and the literal (S+1)-point dual kernel equals
route (ii) up to sign conjugation).  Must-fails 6/6 (m1 budget
factor exact 8.3824, m2 rank shift Fractions-exact, m3 AST, m4
SM sign 4.9e−3, m5 collision ward, m6 wrong frame 0.769).  The
matched scramble breaks named, two prongs (border cone EMPTY at
chain flip n = 37; algebra world-blind at fallback budget with
the named R-block clause −0.4963).  Experiments-side, NO ledger
row, NO L\* claim, NO terminal claim, NO RH CLAIM.

**The internal full attack on R† ≻ ½I — two sharp internal
angles (r363, PRIME.LSTAR.DUAL.INTERNAL_ATTACK.01).**
`canonical_sturm_induction_probe.py` (32/32, SPEC_SHA
`09786c2e7b71c9a4` final with record, freeze `fd7613339dfc18a0`,
two-commit protocol: pre-freeze `de7c55ec`, record `4ee4543c`;
ZERO amendments after freeze; calibration = first full evaluation
= 32/32, 149.6 s; record run1/run2 byte-identical up to WALL
133.4/140.6 s).  **Verdict `BOTH_PARTIAL(PINNING_REFUTED+
EDGE_GAP_LEMMA_NAMED + TERMINAL_RANK_DEAD +
STURM_CANONICAL_CENSUS(84/85 MAIN) + COMPOSITION_TYPED +
INTERNAL_LIMIT)`.**  Angle A: the BKMM Thm 2.3 node-pinning
reading is **refuted** at census grade on 74 resolvable MAIN rows
(sat Hurwitz max 0.462 vs bar 0.15; bulk median 0.257; sat is
*larger* than bulk; pin3 in (0.15, 0.55) on 74/74 — Gauss-like
pair-gap placement, O(1), not shrinking in N).  Canonical Sturm
census 84/85 (miss kz133 = the r359 f64 floor); interpolated-zero
interlacing 85/85.  The remaining named lemma is **EDGE-GAP**
(why a zero of each consecutive dual OP occupies the unique
pair-gap (y₂, y₁) — Sturm/Markov gives interlacing and the count,
not the placement).  The r360 zone {1,2,3} is dual-void
(primal-sat), so dual-OP pinning if it applied would live in the
bulk.  Angle B: the CD update R_{n+1}=R_n+vvᵀ is exact
(Fractions rank-1; w9 residual 3.3e−17); n_cross sits at
terminal rank (183/184, 140/142, 435/436, 877/878) — Loewner
cannot start from a certified small-n head; window-ladder
LC_EDGE2 36/71 and LC_UVEE 32/71 violations, so INDUCTION_GO
does not fire.  Composition: Schur split and Cauchy rest≥eps
are SATZ; det S_N>0 and rest>0 are census; the hoped chain
Sturm ⇒ det S_N > 0 ⇒ [c=1] R ≻ ½I has two measured gaps
(Sturm does not give det S_N without P_N, W_N signs; c=1 does
not give rest>0 — scramble is the live counterexample, lamS
+1.37e−2 and rest −0.4962).  χ worlds MAY tip (30/42, 29/42);
scramble MUST tip (straddle fails).  Must-fails 5/5.  Honest:
both internal angles need genuine new analysis — INTERNAL_LIMIT
measured; the external RHP/BKMM path remains a documented
option, not a freeze for externals.  Experiments-side, NO
ledger row, NO L\* claim, NO R† claim, NO RH CLAIM.  Mincut
unchanged (base 4 / refined 5).

**The edge-gap lemma via Markov–Stieltjes mass counting (r366,
PRIME.LSTAR.DUAL.EDGE_GAP_MS.01).**
`edge_gap_ms_probe.py` (30/30, SPEC_SHA `2b75c2668f0ca545`
final with record, freeze `4164a1c1a1bd3aaf`, two-commit
protocol: pre-freeze `dbf340ab`; two disclosed calibration
amendments a1/a2 — f64 sandwich floor on 15/85 mid/deep MAIN
and chi shallow sum-λ bar 1e−12 → 1e−11; NO forcing candidate,
SCALED_BAND, MINC_HALF or verdict letter moved; record run1/run2
byte-identical up to WALL 260.3/267.2 s).  **Verdict
`MS_CENSUS(...) + REST_NECESSARY_ONLY + STURM_CANONICAL_CENSUS(84/85)
+ COMPOSITION_TYPED + INTERNAL_EXHAUSTED`.**  Leg A: the
classical MS sandwich and Gauss `∑λ = U` are SATZ (exact
arithmetic; f64-graded); the discrete gap theorem is SATZ.
The mass-forcing candidates are **refuted**: `n M_I/U ∈ (0.5, 1.5)`
on 0/74 resolvable MAIN, `M_I > chr_pair` on 0/74.  The pair-gap
is dual-void (`M_I/U = 1.3×10^{-7}` at w9, `n M_I/U = 2.4×10^{-5}`)
— proportional counting predicts `Z = 0`, measured `Z = 1` lives
in the O(1) MS buffer, which cannot distinguish 0 from 1.  The
closed dual-weight dictionary supplies `M_I` (fold-3 route B)
but not a Christoffel comparison without the OP kernel.
EDGE-GAP remains OPEN as a theorem.  Leg B: `min diag(R_CC) > ½`
on 74/74 (necessary, SATZ) but Gershgorin ≥ 0 on 0/74 (not
sufficient); the r360 fold-1 anomaly is a union μ-atom, not a
C-node.  Scramble breaks named at occupation (`minC = 0.186 < ½`,
23 C-nodes below) AND at `Z ≠ 1` AND at rest `−0.4962`.
`REST_MASS_GO` does not fire.  The r363 hoped chain still has
two gaps.  Honest: both mass paths fail to close the two r363
theorem-loci — **INTERNAL_EXHAUSTED**, the internal full attack
(pinning path then mass path) is finished at measured grade;
the external RHP path stays a documented option.  Experiments-side,
NO ledger row, NO L\* claim, NO R† claim, NO RH CLAIM.  Mincut
unchanged (base 4 / refined 5).  Coexistence: r365 (V₂, `rh/problem`)
is a parallel lane; this round is additive.

**The Haynsworth two-rank inertia cut (r367,
PRIME.LSTAR.DUAL.FINAL_TWO_RANK_INERTIA.01).**
`final_two_rank_inertia_probe.py` (34/34, SPEC_SHA `e0d79840fd7c9446`
final with record, freeze `471879d1858e4c57`, two-commit
protocol: pre-freeze `c9ecbadd`; one disclosed calibration
amendment a1 — G33/G34 retyped CENSUS after the first full
evaluation found P1 vacuous on 29/74; 0-violation stays in the
GO letter; NO bar, P1/P2 definition, scramble named-break,
Haynsworth SATZ or restatement threshold moved; record run1/run2
byte-identical up to WALL 236.0/228.9 s).  **Verdict
`PREMISE_FAILS(P1_VACUOUS 29/74, OVERLOAD 0/74) + THREE_RANK_Y_CENSUS
+ A5_LIFT_LEDGER + SOURCE_LEDGER(NOT restatement)`.**  Leg A:
Haynsworth is a finite-matrix SATZ (Fractions LDL toy exact;
live implication P1∧P2 ⇒ M≻0 on 74/74).  K₂ is built only from
the two CD columns and A₀⁻¹ (AST).  The Sol pilot reproduces
bit-near at w9, σ(K₂)=(−2.7938, 1.8036).  Lean form
`haynsworth_two_rank` is in the spec, not proved here.  Leg B:
P1 exact-one 45/74, vacuous 29/74 (A₀ already PD at rank N−3),
overload 0/74; P2 holds on the same 45; the remaining negative
direction on P1-true rows is rest-hosted 42/45 (the r359
pair-Schur is already positive at rank N−3).  Scramble breaks
named at P1 (nneg=21), P2 survives.  χ MAY tip (chi3 21/42,
chi4 19/42).  The Sol 4/4 sample was terminal-rank biased.
Leg C: −det K₂ is SRC_FLAT (slope +0.543), restatement corr
−0.0064 — not a margin rewrite.  `TWO_RANK_INERTIA_GO` does not
fire.  Leg D: A5 lift 4/4; three-rank Y-block mixed/PD 4/4;
one-shot full R† from A₀† off (the border is not a CD column);
`THREE_RANK_LDAGGER_GO` stays off.  Must-fails 5/5.
Experiments-side, NO ledger row, NO L\* claim, NO R† claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r365 (V₂), r366 (edge-gap MS) and r368 (weighted
L²-T1, now sealed) are parallel lanes; this round is additive.

**The weighted L²-T1 — the exact identity instead of the broken
supremum (r368, Sol rank 2 / G4, PRIME.L2.T1_WEIGHTED_L2.01).**
`weighted_l2_t1_probe.py` (20/20, SPEC_SHA `6d6da15ec8dd0cd7`
final with record, freeze `4a89ec1051877c09`, two-commit
protocol: pre-freeze `e1521f94`, record `b5a9a00f`, ZERO
amendments after freeze; calibration = first full evaluation =
20/20, 708.8 s; record run1/run2 byte-identical up to WALL
674.0/631.4 s).  **Verdict `WEIGHTED_L2_CENSUS+SPIKES_DOMINATE_PI`.**
The identity is SATZ, G4 is **not** replaced.  (1) **M₃ =
((log m)²/m²)·T₂·E_π(F²) closes exactly** on all 181 rows
(worst rel 5.5e−16, Fractions toy M₃ = 5/32); T₂·E_π =
(m²/(log m)²)·M₃ is tautological — T₂ is factorized, not
absorbed.  (2) **A-priori bars (C_F, B) = (1.0, 2.0) fail on
3/181**, exactly the K2-spike rows (kz111 E_π 52.276 vs bar
41.258; kz117 58.424 vs 42.09; kz124 75.691 vs 43.948); χ3/χ4
are clean (max 1.144/0.649); C_F_cens = 1.722.  Depth slope is
POWER (tercile C_obs ratio 16.414 vs bar 4.0).  (3)
**Leave-family-out fails on frame B** (C_fit 1.267, viol 2/8 at
kz117/kz124) and carries on A/χ3/χ4 — family-uniformity
answered directly and negatively.  (4) **Spike anatomy mixed**:
kz111 is π-light (share 0.337) — the Sol thesis holds there;
kz117 dominates (share 0.909, max F 23.70) — the weighted mean
*is* the spike, the retyping is useless on that row.  (5)
**Composition does not pay**: m₀\* = 10^29.8 vs r358 Carleson
10^23.5 and r361 floor 10^16.1 / 10^10.0; floor-T2 still
10^19.7.  Cofinal rest unchanged: MED-CAP as a lemma (V₂) + a
family-uniform T1/E_π theorem.  Scrambles P1 admission ×3 (nf
21/3/37) with measurable E_π on partial builds; twin 1.6e−07.
Must-fails 4/4 + m6a/m6b.  Experiments-side, NO ledger row,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).

**The mixed low-rank form of M† plus generalized Haynsworth
(r369, reviewer sequence step 1, PRIME.LDAGGER.MIXED_HAYNSWORTH.01).**
`mixed_haynsworth_probe.py` (20/20, SPEC_SHA `138d09978ff79556`
final with record, freeze `5a4a20db973700ba`, two-commit
protocol: pre-freeze `6ae366a2`, record `6072921f`; ZERO
amendments after freeze; calibration = first full evaluation =
20/20, 29.2 s; record run1/run2 byte-identical up to WALL
29.2/28.9 s).  **Verdict `MIXED_UPDATE_EXACT + HAYNSWORTH_MIXED_SATZ
+ PHI_LEDGER + JSIG_CENSUS`.**  Algebra only; existing records
are the anchors (10-row sample, no 85-row ladder).  (1) **The
mixed form is a finite-matrix SATZ.**  From r362 A4 and r363,
`M† = blkdiag(A₀, −½) + U J Uᵀ` with `U` the two last dual CD
columns plus the Sherman–Morrison vector `(s, −1)` and
`J = diag(1, 1, 1/den)` **derived**, not fitted.  Fractions toy
residual exact 0 (`den = 23/30`); live residual ≤ 1.04e−14
(bar 1e−10) on w9 + the 10-row sample + χ3-w9 + kz15.  The
r367 warning is resolved as a *form*: the border is not a third
unaugmented CD column, but on the R† level Sherman–Morrison
does supply a third column with explicit `J`.
`NO_LOWRANK_BOUNDARY_FORM` does not fire.  (2) **Generalized
Haynsworth is a SATZ** for arbitrary invertible symmetric `J`
(Fractions 4-node toy with indefinite `J = diag(1,1,−1)`:
`In(H) = In(A)+In(−Φ) = In(−J⁻¹)+In(M)` exact).  Lean form
`haynsworth_mixed` is in the spec, not proved here (R373).
(3) **`Φ_N(0)` live.**  w9 σ = (−2.813, −0.0665, 1.804); the
two large eigenvalues track r367 K₂, the small extra negative
is the border direction.  Signature balance 10/10.  Dichotomy:
P1-true 8/10 (`In(A)` nneg=2, `In(Φ)` nneg=2); vacuous kz42/
kz130 2/10 (`In(A)` nneg=1, pad only) — the r367 P1-vacuous
class in the 3×3 picture; χ3-w9 additionally `In(Φ)` nneg=1.
(4) **Honest J-signature.**  Empirical `J_sig = I₃` on 10/10
live rows (`den ∈ [1.460, 1.646]`, all positive).  The mixed
*signature* of `J` is the form plus the synthetic `den<0`
branch, not a Lorentz `J` on MAIN; the mixed-*ness* of the
update on the family is `A` indefinite + `Φ` mixed.  Must-fails
4/4.  Experiments-side, NO ledger row, NO L\* claim, NO R†
claim, NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r371 (compound-CD), r372 (source-Prüfer) and
r373 (Lean transcription) are parallel lanes; this round is
additive.

**The matrix-valued Weyl phase index (r370, reviewer sequence
step 2 after the r369 stop, PRIME.LDAGGER.MATRIX_WEYL_INDEX.01).**
`matrix_weyl_index_probe.py` (31/31, SPEC_SHA `b12b5fc38301767b`
final with record, freeze `f6e1a704fcaf838b`, two-commit
protocol: pre-freeze `e44af3cd`, record this change; ONE
disclosed instrument amendment a1 — cal1 killed on EXT6
Nw~8000; census Ξ := nneg Φ(0), EXT6 dropped from the Weyl
ladder; NO bar/kill-test/verdict letter moved; record
run1/run2 byte-identical up to WALL 707.9/704.3 s).
**Verdict `NO_JACOBI_LINEARIZATION + PHASE_RESTATEMENT +
PHI_MONOTONE_SATZ + PHASE_CENSUS`.**  `CANONICAL_PHASE_CARRIER`
does **not** fire (the 70% resource trigger stays off).
(1) **Φ_N(z) and Φ′ ⪰ 0 are SATZ.**  Block resolvent
(A₀-eigh + pad); Fractions det-lemma exact (`2293/150` at
z=−2, consumes the target char poly); live min eig Φ′ =
8.949e−09 on 18/18 admissible grid nodes.  w9 Φ(0) σ =
(−2.8132, −0.06648, 1.8039); large pair tracks r367 K₂;
mixed residual 1.9e−15.
(2) **The 3×3 Wronskian dictionary fails at a named place.**
Dual p and dual-measure Cauchy q satisfy the three-term
recurrence (2×2 Casoratian drift 3.1e−12, source-pure).
Border Cauchy r_n residual 3.615e−02 — not a homogeneous
dual solution, so there is no 3×3 Jacobi Casoratian of
(p, q, r).  r359 IIKS does not z-lift to A₀ (rel 1.003).
C_N > 0 is not constructed.
(3) **Phase census.**  Ξ := nneg Φ(0).  MAIN 81 rows
(a1: EXT6 dropped) resolvable 74/74 PD, Ξ==nnegΦ, balance
(bar 74+); twin |dΞ|=0; χ3-w9 vacuous positive; six
terminal-dead χ classified negative (χ3 5/5, χ4 1/1) via
want_pd/ctrl/q_N (Ξ follows nnegΦ and is 0 on kz23/33/20,
1 on kz15/19/39 — not a magic Ξ value); scramble named
nnegA₀=21 and nf=37.  Phase turns at A's poles, not at
named Y-nodes.  Shadow corr(Ξ, log|margin|) = +0.201.
(4) **Anti-restatement.**  Haynsworth auto-recognizes a
source-free PD target; the Wronskian dictionary is
undefined there.  Real-line Ξ **is** nneg Φ(0), so the
index is Haynsworth inertia in other coordinates.
Must-fails 4/4.  Experiments-side, NO ledger row, NO L\*
claim, NO R† claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).  Coexistence: r371 (compound-CD),
r372 (source-Prüfer) and r373 (Lean) are parallel lanes;
this round is additive.

**The exterior-square kill test of the canonical CD two-form
(r371, reviewer solution 3, PRIME.LSTAR.DUAL.COMPOUND_CD.01).**
`compound_cd_wedge_probe.py` (30/30, SPEC_SHA `3b5b3c887d515ffd`
final with record, freeze `85b31ee99180bf64`, two-commit
protocol: pre-freeze `ac7c0b0b`, record `13af4c78`; ONE
disclosed instrument amendment a1 — G35's second raw 1e-8
floor disagreed with the r367 Rayleigh inertia on 10/45 P1
near-zeros; the product formula is now the constructor;
SHARE_BAR, sign definition, MAJ construction and GO letters
NOT moved; record run1/run2 byte-identical up to WALL
283.3/239.3 s).  **Verdict `SIGNATURE_PARTIAL(wterm<0 45/45,
share≥0.50 27/45) + CAPTURE_HOLDS_CENSUS + OVERLOAD_CENSUS_ONLY`.**
Leg A: identities (12)(13) are finite-matrix SATZ (Fractions
toy det K₂ = −7 exact; CD-telescope exact; f64 (12) graded
74/74, live 1e-10 on 72/74; (13) live 74/74, c_N = 1/b_{N-3}
∈ (1.92, 2.06) all positive).  Leg B (the kill test): the
canonical wedge **sign is stable** on the nneg-1 branch
(wterm<0 45/45, range [−637.7, −1.32], 0 flips) — not the
r318 coin-flip of original-matrix minors; capture (14) holds
45/45 by algebra (≡ P2 via (12), not independent arithmetic);
the ∧²-subspace share is **not** stable (majority 27/45, min
0.001, med 0.601, max 0.905 — the Sol 4/4 sample was
terminal-rank biased).  `COMPOUND_SIGNATURE_STABLE` does not
fire.  ∧² inertia nneg(∧²A₀)=|Y|−1 on 45/45 (product formula).
r367 dichotomy reproduced (P1 45 / vacuous 29 / overload 0
on 74).  Leg C: Gershgorin-Stieltjes MAJ = n_hit ∈ [67, 1425]
on the branch, isolation 0/45, cert_lt2 0/45 — the
construction does not certify ind₋ < 2; occupation diagonal
of A₀ is n_diagneg = 0 on the whole branch (min diag > 0);
scramble MAJ = 49 > 2 (vacuity test holds).
`OVERLOAD_MAJORANT_GO` stays off; nneg ≤ 1 remains the r367
census.  Leg D: twin |d wterm| = 6.2e-5; χ3 21/42 and χ4
19/42 nneg-1 all sign-stable (χ MAY tip); scramble named P1
nneg=21, P2 survives, wterm = −3.022 measured.  Must-fails
5/5.  Honesty: the canonical two-form has a stable source
**sign** and an unstable ∧²-subspace share; capture is
algebra; the overload theorem stays census.  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).  Coexistence: r369 (mixed Haynsworth),
r370 (matrix Weyl), r372 (source-Prüfer) and r373 (Lean) are
parallel lanes; this round is additive.

**The source-Jacobi Prüfer one-defect test (r372, reviewer
solution 2 / Terminal, PRIME.TERMINAL.SOURCE_PRUFER_ONE_DEFECT.01).**
`source_prufer_one_defect_probe.py` (27/27, SPEC_SHA
`778403f6c5f898e9` final with record, freeze `ad13a2abd3dca0f2`,
two-commit protocol: pre-freeze `279c0f92`, record this
change; ONE disclosed instrument amendment a1 —
`twin_rational` arity copied from the r368 channel after
cal1 crashed at G91; NO bar, letter, turning rule or
verdict tree moved; record run1/run2 byte-identical up to
WALL 747.9/644.3 s).  **Verdict `SPIKE_NOT_UNIQUE`.** The
Prüfer-to-run dictionary is SATZ (181/181, XOR 181/181,
Fractions toy exact, interior chain progress min 2.062).
The one-defect thesis is refuted at census grade:
NOT_UNIQUE 181/181, MAIN unique 0/97, max n_turn 310
(w9 already 12/6/9/7).  Spike coincidence fails on
kz111/117/124 (canonical i*=0 vs argmax-q 168/140/111;
q* 4.3e-3 / 5.1e-3 / 4.9e-4, not the r368 mass spikes —
the same rule does not carry the three named rows).
Two-part bound after dominant-cluster extraction does not
replace T1: rest-T1 viol 0/181 only because (log m)² is
large while F_rest still equals the global max 23.704;
rest-M3 viol 24/181 (max 94.893 vs C_REST 1.0); m₀* =
10^{24.9} vs r361 10^{16.1}/10^{10.0}.  V₂ holds 181/181
combinatorially (0 phase-pattern violators) but not from
one-turning phase regularity.  Scrambles P1_ADMISSION ×3
(n_turn 7/40/3); twin 1.8e-08; must-fails e1–e5 + m6a/m6b.
Cofinal rest unchanged: V₂ as a lemma + a family-uniform
T1 theorem.  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r369 (mixed Haynsworth), r370 (matrix Weyl),
r371 (compound-CD) and r373 (Lean) are parallel lanes;
this round is additive.

**The $V_2$-lemma, reduced (r374, LEMMA.V2.01, lemma-first).**
No sealed discovery probe: `/tmp` proof verification plus
`rh/problem/v2_lemma_v3.tex` (+ PDF + `verify_v2_lemma.py`,
16/16, `V2 LEMMA V3 VERIFIED`).  **Ausgang REDUZIERT.**  The
r372 Prüfer-to-run dictionary is used as a theorem.  SATZ: the
discrete phase step of the scaled pair $(v_{N-2},v_{N-3})$ is
the two-point Wronskian (Lagrange identity over $\mathbb{Q}$;
f64 residual $1.0\cdot 10^{-15}$ on the pins); at the $+x$
$20\%$ mask $\mathrm{sign}(x)$ is constant, so the colouring is
$\mathrm{sign}(w)\,\mathrm{sign}(v_2)$.  Finite contrast
dichotomy: constant rigid steps never realise a $V_2$-violator;
a slow-then-fast block $(0.4^{21},2.8^{3})$ does ($347/1001$),
while $(1.0^{21},2.0^{3})$ does not.
$V_2$ is not a theorem of abstract Jacobi-positive chains (an
$8\times$ scale of the last twelve $\gamma$ on $\chi_3$ $w=9$
is a $v_2$-violator; scale $6$ is not).  A gap-then-spike
weight adversary on FRAME-A $w=9$ at $8\times$ and $64\times$
never produces a $V_2$-violator and always breaks Jacobi
positivity.
Reduced to the strictly smaller finite profile lemma $V_3'$:
the last fourteen Prüfer steps at the mask lie in
$\mathcal{A}_{15}$ ($V_2$-regular for every incoming remainder
$\eta\in[0,\pi)$).  Path A on the six pins ($0$ $\eta$-violators;
every $(1,1,1)$ is $V_2$-regular).  Chain
$T_2'\Leftarrow 3/8\Leftarrow\mathrm{MED\text{-}CAP}\Leftarrow X_n\Leftarrow V_2\Leftarrow V_3'$.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r375 and
r376 are parallel lemma-first lanes; this round is additive.

**The P2 lemma — source expansion and factorization (r375,
LEMMA.P2.01, lemma-first).**  No sealed discovery probe:
`/tmp` proof verification plus `rh/problem/p2_lemma_proof.tex`
(+ PDF + `verify_p2_steps.py`, 12/12, `P2 STEPS VERIFIED`).
**Ausgang REDUZIERT.**  SATZ (Fractions 4-node toy, det K₂ = −7
exact): on nneg-1, $K_2=(I+R_+)-ww^T/\lambda_-$ with
$w=U^T\psi_-$ and
$\det K_2=\det(I+R_+)(1-\gamma/\lambda_-)$; equivalently
$-\det K_2=\det(I+R_+)(\gamma/\lambda_--1)=(N-\lambda_-\det(I+R_+))/\lambda_-$
with $N=\|w\|^2+\langle\delta,A_+^{-1}\delta\rangle$ a sum of
positive structures.  The sign of det K₂ is carried by the
single scalar $\gamma-\lambda_-$.  $\det(I+R_+)\ge 1$ is SATZ.
P1 does not imply P2 (tiny-overlap adversary).  The $\delta$-term
is load-bearing (kz46: Cauchy-sufficient fails, P2 holds,
$\delta$-share $0.723$).  P2 is **not** the r359 bind ratio
(fold-pair Schur already PD at rank $N-3$ on $45/45$, rest-hosted
$42/45$; bind consumes the terminal margin).  A raw overlap
floor $\|w\|^2\ge\kappa_0$ is false (pair-span min $6\cdot10^{-4}$
on the branch, matching the r371 $\wedge^2$-share).  Live on the
45 resolvable nneg-1 windows: $\gamma>\lambda_-$ $45/45$,
excess $\gamma/\lambda_--1\in[0.275,3.295]$ (min at kz18, well-
conditioned), $\det(I+R_+)\ge 3.307$, $-\det K_2\in[1.157,1126.389]$;
$\chi_3$ $21/21$ and $\chi_4$ $19/19$ sign-stable on their
nneg-1 rows; scramble named-breaks at P1 (nneg $=21$).  Shadow
corr(excess, $\log|\mathrm{eps}|$)$=+0.046$ (not a margin
rewrite).  Reduced target (P2⁻): $\gamma>(1+\varepsilon)\lambda_-$,
which implies $-\det K_2\ge\varepsilon$ and does not consume
$\lambda_{\min}(S_N)$.  Named remainder: source expansion of
$U^T\psi_-$ via dual CD weights and the Borodin dual mode of
$R_{N-3}-\tfrac12 I$.  Experiments-side, NO ledger row, NO L\*
claim, NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374 and r376 are parallel lemma-first lanes;
this round is additive.

**The post-cap pivot lemmas (r377, LEMMA.POSTCAP_PIVOTS.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/postcap_pivots_probe.py` (18/18
full, 9/9 smoke, SPEC_SHA `b7167c3756c9b7a6`) plus
`rh/problem/postcap_pivots.tex` (+ PDF +
`verify_postcap_steps.py`, 16/16, `POSTCAP STEPS VERIFIED`).
**Ziel A (P2-POSTCAP) WIDERLEGT** as the universal statement
$h_N h_{N+1}<0$ on every canonical window: $35/85$ MAIN
LATE/NONE, explicit $kz=12$ (first defect at $N+2$,
$\det K_2=+12.4632$, $A_0\succ 0$).  Dictionary SATZ
(Fractions toy $\det K_2=-196/35719$ both routes; live
$(\det K_2<0)\Leftrightarrow(h_N h_{N+1}<0)$).  On the
nneg-$1$ branch the unique prefix defect sits in
$\{h_N,h_{N+1}\}$ and alternates, $50/50$ MAIN (PINNED-$N$
$19$, PINNED-$N{+}1$ $31$).  Node polynomial and Chebyshev
aliasing SATZ; the sign of the product remains an
$H_N^{-1}$ readback (kill).  **Ziel B (P1-SINGLE-DEFECT)
CENSUS** $\mathrm{ind}_- H_{N+2}\le 1$ on $85/85$ MAIN and
$84/84$ $\chi$; scramble named-breaks (first $=21$,
$n_{\mathrm{neg}}=37$).  Free window $h_0,\ldots,h_{N-1}>0$
on $85/85$ MAIN; $\chi$ defects wander through offsets
$0..3$ (NONE hunt $4..8$).  Dead $\chi$ still satisfy B.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r374,
r375, r376 and the parallel compose lane are not dropped;
this round is additive.

**The compose lemma, reduced (r378, LEMMA.COMPOSE.01,
lemma-first).**  No sealed discovery probe: `/tmp` proof
verification plus `rh/problem/compose_lemma.tex` (+ PDF +
`verify_compose_lemma.py`, 15/15, `COMPOSE LEMMA VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: van der Corput
$\lvert\sum P\rvert^2\le\mathrm{pref}\,S_F$ at
$H=\max(2,\lceil\sqrt{m}\rceil)$ (v964-S0); $\mathrm{pref}\le\sqrt{m}+1$;
participation $D N_2=L_1^2$; Rényi $N_2\ge N_3$; kernel envelope;
T1-floor algebra conditional on $8/3$ and $C_K$.  The slope
targets $\sigma\le-0.516$, $N_2$-need $0.908$, atom-need $0.888$
are conventions, not pointwise theorems; they are slope-proxies
for $\beta=1/2+2\gamma$ with measured $\gamma\approx 0.196$.
Pointwise H5-need with bounded $L_1,R_0$ is $\beta=1/2$.
H5/`PairMarginLaw` is a *sister* sufficient condition, not an
extra vdC-route premise.  Reduced implication COMPOSE⁻: if
$S_F\le R_0 D$, $L_1\le\Lambda$, $\lvert Z_{\mathrm{loc}}\rvert\le Z_0<M$
and $M_3\le\phi(m)=(M-Z_0)^4/(\mathrm{pref}^2 R_0^2\Lambda^4)$
then $\lvert Z\rvert<M$ (and $q_N<1$ given the r263 dictionary).
Log-complete $m_0$: $10^{25.81}$ ($C_K=4.91$) / $10^{32.85}$
($C_K=23.70$); r361 published $10^{10.0}$/$10^{16.1}$ drop
$2\log\log m$ (ratios $0.4517$/$0.5351<1$).  42-rung FRAME-A
certificate: $q_Z<1$ $42/42$, F2-split $42/42$, cheap triangle
$35/42$, exceptions $\{15,20,22,36,38,39,52\}$, vdC-F2 $38/42$,
H5-sister $21/42$, min $q$-margin $0.0195$.  T1 implication
$181/181$ on $89$ A $+8$ B $+42$ $\chi_3$ $+42$ $\chi_4$.
Remaining lemmas: (R)(L)(Z)(T1)(V₃')(Dict)(Head).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r374, r375,
r376 and r377 are parallel lemma-first lanes; this round is
additive.

**The $V_3'$-lemma, reduced (r379, LEMMA.V3PRIME.01, lemma-first).**
No sealed discovery probe: `/tmp` proof verification plus
`rh/problem/v3prime_proof.tex` (+ PDF + `verify_v3prime.py`,
17/17, `V3PRIME LEMMA VERIFIED`).  **Ausgang REDUZIERT.**
SATZ: smooth-border nodes are the cosine grid $x=\cos(2\pi k/L)$
with $L=4h-2$ ($M=2h$, $L=2M-2$); at the $+x$ $20\%$ mask
consecutive bulk nodes are equidistant in $\arccos$
($\Delta\theta$-ratio $1$ on all $181$ windows).  Equal weights
on the occupied cosine nodes reproduce Chebyshev coefficients
($\gamma_1=\tfrac12$, $\lvert\gamma_k-\tfrac14\rvert<10^{-5}$
for $k\ge 2$).  The Fejér factor is Jacobi-$(0,1)$ with
$\lvert\gamma_n-\tfrac14\rvert=1/(4(2n+1)^2)$.  Two-period
profiles about $\pi/2$ with amplitude $a\le 0.85$ lie in
$\mathcal{A}_{15}$; a slow-then-fast *block* with the same
extremes need not.  A coherent last-$12$ $\gamma$-scale of
$1.5$ stays in $\mathcal{A}_{15}$; scale $2.0$ leaves it
(actual $v_2$-violator at scale $6.5$--$8$).  Reduced to the
coefficient box $G_\varepsilon$: last twelve
$\lvert\gamma_k-\tfrac14\rvert\le\tfrac1{16}$ and
$\lvert\log(\gamma_{k+1}/\gamma_k)\rvert\le\tfrac25$.  On the
$181$-window surface $G_\varepsilon$ holds (max last-$3$
$0.0375$, max last-$12$ $0.0519$, max jump $0.337$) and $V_3'$
holds ($0$ remainder-violators).  Klein-gap and $\chi$ are not
exceptions.  Chain
$T_2'\Leftarrow\cdots\Leftarrow V_2\Leftarrow V_3'\Leftarrow G_\varepsilon$.
Remaining lemmas: (R)(L)(Z)(T1)($G_\varepsilon$)(Dict)(Head).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r374--r378
and r376/r380 (Lean) are parallel lanes; this round is additive.

**The $G_\varepsilon$-lemma, reduced (r381, LEMMA.G_EPS.01, lemma-first).**
`experiments/tfpt-discovery/g_eps_lemma_probe.py` (17/17 full,
14/14 smoke, SPEC_SHA `60ce9bc28fc7f171`) plus
`rh/problem/g_eps_lemma.tex` (+ PDF + `verify_g_eps.py`,
13/13, `G_EPS LEMMA VERIFIED`).  **Ausgang REDUZIERT.**
SATZ: the first-order formula
$\partial\gamma_k/\partial w_j=(p_k(x_j)^2-\gamma_k p_{k-1}(x_j)^2)/h_{k-1}$
(Fractions toy $\lvert\mathrm{CD}-\mathrm{FO}\rvert/\lvert\mathrm{FO}\rvert=2.092\cdot10^{-4}$
at $\varepsilon=1/200$; FRAME-A $w=9$ FO vs FD rel $5.446\cdot10^{-4}$).
Jacobi-$(0,1)$ and the cosine-grid mesh remain r379 SATZ.
$L^\infty$ of the Fejér-stripped $d_{\mathrm{arm}}$ is $O(1)$
($w=9$ $\lVert\varepsilon_\mu\rVert_\infty=5.166$) — the crude FO
majorant $\sim 3\gg 1/16$; cancellation is essential.
The jump half is not implied by the box ($\log(5/3)=0.5108>2/5$).
$\Lambda(n)\le\log n$ is PNT-free (trial division $n=2..120$).
The second-order midpoint remainder along Fejér-ref $\to$ actual
at degree $40$ has $\lvert\mathrm{quad}\rvert/\lvert\mathrm{lin}\rvert=1.013$
on the last twelve (not dominated).
FRAME-A $w=9$: signed last-$12$ $0.03417$, jump $0.2493$;
$\mu$-only last-$12$ $0.02605$, jump $0.1224$;
$\mathrm{mass}(\nu)/\mathrm{mass}(\mu)=0.0611$.
Scramble seed $1$ named-breaks last-$12$ $\lvert\gamma-1/4\rvert=6.841$
(lag $\lvert c_q\rvert$ is not the separator).
The slow-then-fast block is a step obstruction, not an FO-formula
fail.  Reduced to the pair $(C_\varepsilon,R_2)$: the explicit FO
pairing against reference OP squares, and the Taylor remainder
of the finite $\mu\to\mu-\nu$ (or Fejér-ref $\to$ actual) step.
Chain
$T_2'\Leftarrow\cdots\Leftarrow V_3'\Leftarrow G_\varepsilon\Leftarrow
G_\varepsilon^\mu\wedge C_\varepsilon\wedge R_2$.
Remaining lemmas: (R)(L)(Z)(T1)($C_\varepsilon$,$R_2$)(Dict)(Head)
($G_\varepsilon^\mu$ is the positive-measure sibling).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r374--r380
are parallel lanes; this round is additive.

**The pivot-band entry lemma, reduced (r382, LEMMA.PIVOT_ENTRY.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/pivot_entry_lemma_probe.py` (17/17
full, 10/10 smoke, SPEC_SHA `b7f53a93daf790bc`) plus
`rh/problem/pivot_entry_lemma.tex` (+ PDF +
`verify_pivot_entry.py`, 14/14, `PIVOT ENTRY STEPS VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: RKHS sum bound; pair-energy
identity; Christoffel comparison $h_k(w)\ge(1-\lambda_{\max}(E_{k+1}))h_k(\mu)$;
five-atom $2$-versus-$1$ interlacing ($h_0,h_1,h_2>0$,
$h_3=-144/7$); three-atom flank ratio $1/3$ with
$h_0=4$, $h_1=6$, $h_2=-3$; equal two-period $H_1=0$; clustered
run-of-three $H_3<0$ before half-filling.  The source ingredient
that protects the free window is the *flank*: every negative run
on the ordered cosine support has length at most $2$ (MAIN
$85/85$) and $\nu$-mass at most two-thirds of the flanking
$\mu$-mass (core $42/42$, MAIN $78/85$; seven EXT-heavy windows
remain under the weaker $c<1$).  Dead $\chi$ satisfy both;
scramble drops at both (max-run $5$, $r_{\max}=2.71$,
first-neg $21<\lfloor 2\cdot 184/5\rfloor=73$,
$\lambda_{\max}(E_{22})>1$).  Two-period amplitude $2/3$ first
goes negative at $\sim N/2$ (the binding adversary against
raising $\kappa$ to $1$); amplitude $1$ kills at $h_0$.  Reduced
entry $n_0=\lfloor 2N/5\rfloor$ under (F2$_{2/3}$), which docks
to r380 `adaptive_band_from_entry` as the named Prop
`FlankEntryPrefix` (no Lean edit this round; R384 formalizes).
What remains for $n_0=N-1$ is the $L^2$ Christoffel tail on the
flank blocks (r285 coherence).  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged (base 4 / refined
5).  Coexistence: r374--r381 and r376/r380 (Lean) are parallel
lanes; this round is additive.

**The compose premises $(R)$, $(L)$, $(Z)$ (r383,
LEMMA.COMPOSE.PREMISES.01, lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/compose_premises_probe.py` (20/20
full, 12/12 smoke, SPEC_SHA `146b0b45ad872d7e`) plus
`rh/problem/compose_premises.tex` (+ PDF +
`verify_compose_premises.py`, 16/16, `COMPOSE PREMISES VERIFIED`).
Three letters, one shared Fejér/vdC window.  SATZ: Fejér identity
and bilinear Cauchy--Schwarz; the $r298$ split; $Z=Z_{\mathrm{loc}}+t_{\mathrm{bulk}}$
(Lean `canonical_split`; not $\sum P_\Delta$); the $L^2$ identity
$M_3=(({\log m})^2/m^2)\,T_2\,E_\pi(F^2)$; $\Lambda(n)\le\log n$;
$\mathrm{pref}\le\sqrt{m}+1$; T1-floor algebra under $g_i\ge 3/8$.
**(R) REDUZIERT** to the census $R_0=4$ (sup $2.916788$ at FRAME-A
kz$37$; mutant $R_0/2=2$ fails $17/181$ and the DC toy).  Fold
pairing as a live SATZ is REFUTED (pair-residual median $0.512$);
MAIN-empty is a census (median $0.0086$), not a pairing theorem.
The trivial envelope $H_{\max}=29$ is too coarse.  **(L) REDUZIERT**
to $\Lambda=3$ (max $2.126$ at FRAME-B kz$124$).  The von~Mangoldt
triangle (slope $+0.307$ on FRAME-A) does not prove $\gamma<1/4$;
the measured $L_1$ slope $+0.202$ on the $42$ is not a theorem.
The T1-combo does **not** carry as a theorem ($E_\pi=52.276$ at
kz$111$, $75.691$ at kz$117$; identity SATZ, $T_2\le 1.329<(8/3)^2$).
**(Z) REDUZIERT** on FRAME-A ($Z_0=4/5$, $89/89$, max $0.755675$
at kz$16$) and FRAME-B $8/8$ and the $42$-rung ladder $42/42$;
**REFUTED** family-uniform on $\chi$ (six windows:
$\chi_3\{15,19,23,33,39\}$, $\chi_4\{20\}$; $175/181$ have
$\lvert Z_{\mathrm{loc}}\rvert<M$).  Finite-head Chebyshev is
REFUTED ($n_{\mathrm{edge}}$ $167$--$4689$).  Scramble seed $1$
named-breaks $(L)$ on the T1/$M_3$ polylog without breaking $R_0$
or $\Lambda$.  Remaining: a cofinal $R_0$, a proved $\gamma<1/4$
or a family-uniform $E_\pi$ bound, a cofinal $Z_0$ off $\chi$, T1
as a $C_K$-cap, Dict, Head.  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged (base 4 / refined
5).  Coexistence: r374--r382 and r376/r380/r384 (Lean) are parallel
lanes; this round is additive.

**Christoffel quietness, reduced (r385, LEMMA.CHRISTOFFEL_QUIET.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/christoffel_quiet_probe.py` (19/19
full, 13/13 smoke, SPEC_SHA `03bde46ec27d98ff`) plus
`rh/problem/christoffel_quiet.tex` (+ PDF +
`verify_christoffel_quiet.py`, 13/13, `CHRISTOFFEL QUIET VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: $T_k^2=(1+T_{2k})/2$;
$\mathrm{TV}(\cos 2k\theta)=4k$; Chebyshev--Gauss $Q_k\equiv 1$
on the equal-weight cosine grid; $\mathrm{FO}_k[-\nu]=\gamma_k(Q_k-Q_{k-1})$
(FRAME-A $w=9$ residual $2\cdot10^{-17}$); one-Rayleigh
$h_k(1-Q_k)$.  Chebyshev sampling of $\nu$ stays at the mass
ratio $\alpha$ under the *trivial* Weyl bound
($\lvert S_m\rvert\le\mathrm{mass}(\nu)$ already gives
$Q^T\le 2\alpha\sim 0.12<1$).  The deduction ``therefore $\mu$-OP
$Q_k\le\bar q$ from the $3/8$-floor + Koksma'' is false:
$w=9$ last-twelve $Q=0.389$ versus $\alpha=0.061$, deformation
$0.335$, $kD^*=33.4$ does not close;
$\lvert Q-\alpha\rvert/(kD^*)=0.0089=o(kD^*)$ but the error
still grows.  Weyl $\lvert S_{2k}\rvert/\mathrm{mass}$ sits in
$(0.04,0.33)$ --- **trivial, not PNT, not subconvex, not
RH-equivalent** (the Chebyshev--Weyl route never reaches a
zeta-quality demand).  Core-$42$ $Q_{\max}\in[0.164,0.483]<1$;
eleven small-$N$ last-twelve $\lvert\mathrm{FO}\rvert\le 0.01182<\tfrac1{32}$;
MAIN-$85$ $D^*\in[0.105,0.212]$.  Scramble seed $1$ crosses
$Q=1$ at $k=70$ (last-twelve $4.8\cdot10^6$).  Two-period
$c=2/3$ has $Q\equiv 0.683<1$ and still $\lambda_{\max}(E_{22})>1$
--- $Q<1$ is not the floor plate.  EXT-heavy seven stay quiet
at depth $200$ ($Q_{\max}\le 0.221$).  Remaining: the Fejér$/d_{\mathrm{arm}}$
deformation $\Delta_k=Q_k-Q_k^T$ (live $C_\varepsilon$ term) and
the coherence assist (r382 $L^2$ remainder).  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).  Coexistence: r374--r384 are parallel
lemma-first / Lean lanes; this round is additive.


**Living-ladder $(Z')$ and cofinal $R_0$ (r386,
LEMMA.COMPOSE.PREMISES2.01, lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/compose_premises2_probe.py` (20/20
full, 12/12 smoke, SPEC_SHA `82d07e568591c9fd`) plus
`rh/problem/compose_premises2.tex` (+ PDF +
`verify_compose_premises2.py`, 16/16, `COMPOSE PREMISES2 VERIFIED`).
Two letters.  **$(Z')$ REDUZIERT** to $Z_0'=21/25$ on the living
ladder $175/175$ (sup $0.833870$ at $\chi_4$ kz$46$, which
exceeds r383's $4/5$).  Death channel
$\lvert Z_{\mathrm{loc}}\rvert\ge M\iff q_N>1$ is a
biconditional census $181/181$; the six dead $\chi$ windows are
exactly the terminal-dead sprouts.  Finite-head Chebyshev and
uniform-cancel$\times$triangle are REFUTED.  **$(R)$ REDUZIERT:**
$R_0=4$ census; $B(\omega,\omega)/D\le 3/10$ census (falling);
CS SATZ; CS$+$FAB does not prove $O(\mathrm{polylog})$.  Named
remainder $B(\omega+\beta,\omega+\beta)\le K D$.  DC toy
kills a field-independent $C_{\mathrm{MAIN}}$; mutant $4/5$
fails on living $\chi_4$--$46$; scramble does not break $(Z')$
or $R_0$.  Experiments-side, NO ledger row, NO L\* claim, NO RH
CLAIM.  Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r385 are parallel lanes; this round is additive.

**Coherence assist, reduced (r387, LEMMA.COHERENCE_ASSIST.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/coherence_assist_probe.py` (20/20
full, 14/14 smoke, SPEC_SHA `6005359e0bafadb2`) plus
`rh/problem/coherence_assist.tex` (+ PDF +
`verify_coherence_assist.py`, 13/13, `COHERENCE ASSIST VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: Chebyshev-$T$ CD kernel
$=[D_{k-1}(\theta-\phi)+D_{k-1}(\theta+\phi)]/(2\pi)$;
bookkeeping $\lambda_{\max}=\mathrm{maxdiag}\cdot(1+\mathrm{assist})$
exact; Gershgorin/Schur majorant; cosine mesh $\Delta=\pi/S$;
two-period $=$ global AP ($\rho_{\mathrm{AP}}=1$).  The deduction
``therefore $\mathrm{assist}\le(1-Q)/Q$ from the $3/8$-floor +
Gershgorin'' is false: $w=9$ $k_{\mathrm{Gershgorin}}=21\ll n_0=73\ll N-1=183$
($k^*/N=0.109$); core-$42$ $k_{\mathrm{G}}/N\le 0.114<2/5$;
$d_{\min}/d_{\mathrm{med}}=1/3<3/8$.  Wall $w=9$: $\mathrm{maxdiag}=0.9614$,
$\mathrm{assist}=0.0399$ (r285 range; r385 mixed $Q_k$ with
$\mathrm{maxdiag}(E)$).  Named property $\rho_{\mathrm{AP}}<1/5$
kills the two-period (Dirichlet max-row $0.858$ vs source $0.291$
at $k=22$) and holds on EXT-heavy seven ($\rho_{\mathrm{AP}}\le 0.033$).
Scramble holds $\rho_{\mathrm{AP}}$ and dies on the product
($k_\lambda=22$).  Remaining: the *signed* $\mu$-CD off-diagonal
(true assist; unsigned/Gershgorin closed as too crude).
$n_0=\lfloor 2N/5\rfloor$ is not improved; $n_0=N-1$ stays open.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence: r374--r386
are parallel lemma-first / Lean lanes; this round is additive.

**The $\Delta$-deformation, reduced (r388, LEMMA.DELTA_DEFORMATION.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/delta_deformation_probe.py` (19/19
full, 12/12 smoke, SPEC_SHA `5613d035ac6bc11d`) plus
`rh/problem/delta_deformation.tex` (+ PDF +
`verify_delta_deformation.py`, 13/13, `DELTA DEFORMATION VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: $\mathrm{FO}_k=\gamma_k(\mathrm{d}Q^T+\mathrm{d}\Delta)$;
monic $\gamma$ homogeneous in total mass; Fejér-pure two-period
has $\varepsilon=0$ and $\mathrm{FO}=0$.  Osc-Geronimus
$\lvert\mathrm{d}\Delta\rvert\le C\cdot\mathrm{osc}(\varepsilon$ on $\nu)$
holds on MAIN with $C_*=0.0056$ and does **not** close $C_\varepsilon$
(majorant $0.191>1/32$, closes $5/42$; $C\times 2$ already overshoots
on $w=9$).  Consecutive $Q$ is uncorrelated with
$\lVert\varepsilon\rVert_\infty$ ($\rho=0.025$) and with range-oscillation
($\rho=-0.287$).  $R_2$ on the $\mu$-reference is **not** dominated:
$n=40$ ratio $0.8615$ (Fejér-path $1.0127$ reproduced); full $n=182$
ratio $0.6403$; $\lvert R_2\rvert/\lvert\mathrm{FO}\rvert=4.19$;
small-$N$ ratios in $[0.559,1.126]$, all $>1/4$.  Eleven small-$N$
last-twelve $\lvert\mathrm{FO}\rvert\le 0.01182$ (MAIN) and
$0.01541$ ($\chi_3$), both $<1/32$.  Scramble seed $1$:
$\mathrm{osc}_\nu=3.54<8.76$ but $\lvert\mathrm{d}\Delta\rvert=2.16\cdot10^6$.
Remaining: $C_\varepsilon$ as cancelled last-twelve pairing (not an
$\varepsilon$-size bound); $R_2$ of the finite $\mu\to\mu-\nu$ step;
$G_\varepsilon^\mu$ as the Jacobi box of Fejér$\times d_{\mathrm{arm}}$
(r342 dictionary $v_{\mathrm{pred}}<10^{-4}$ is the right language
for the sibling).  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r387 are parallel lemma-first / Lean lanes; this round is additive.

**The Weyl energy of cancellation, reduced (r389, LEMMA.WEYL_ENERGY.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/weyl_energy_probe.py` (27/27
full, 19/19 smoke, SPEC_SHA `c93fdc413980bf4a`) plus
`rh/problem/weyl_energy.tex` (+ PDF +
`verify_weyl_energy.py`, 14/14, `WEYL ENERGY VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: Chebyshev energy
$\Phi=(1/\pi)C_0^2+(2/\pi)\sum_{m<k}C_m^2$; off $=\Phi-$diag;
$Q^T=(C_0+C_{2k})_\nu/(C_0+C_{2k})_\mu$; $\pi_k^2$ Weyl;
finite-grid Parseval $\sum_{q<2S}\lvert S_q\rvert^2=2S\sum v^2$
(ratio $1$ on $S=21$ and $w=9$).  MAIN/$\chi$ at quadratic-mean
(core-$42$ $\mathrm{mean}/\mathrm{qm}\in[0.661,1.018]$,
$\lvert C\rvert/\mathrm{mass}$ max $<0.41$, HHI $<0.12$).
Two-period $S=81$ is a comb ($\lvert C_S\rvert/\mathrm{mass}=1$,
HHI $=0.727$) --- $\rho_{\mathrm{AP}}=1$ iff spectral concentration
on a progression.  $\mathrm{FO}^T$ last-twelve $0.00496$ and
small-$N$ max $0.01650$ both $<1/32$: the Chebyshev piece of
$C_\varepsilon$ closes at quadratic-mean; $d\Delta$ is the live
remainder.  Assist is not the Chebyshev all-ones energy
($1^TE^T1/n_\nu=0.114$ vs $\lambda=0.99983$).  $Z_{\mathrm{loc}}$
Chebyshev proxy cancel $0.47\neq$ r386 median $0.055$.
Von Mangoldt $\mathrm{mean}/\mathrm{qm}=0.718>$ equal $0.403$.
Scramble holds QM and diverges at $m=380,354,30$.  Remaining:
Weyl energy of the $\mu$-OP Chebyshev-coefficient Gram --- of
$\phi^*$ (assist), of consecutive $\alpha_k$ ($d\Delta$/$C_\varepsilon$),
of the edge-masked drive ($Z_{\mathrm{loc}}$).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r388 are parallel lemma-first / Lean lanes; this round is additive.

**The $G_\varepsilon^\mu$-lemma, reduced (r390, LEMMA.G_EPS_MU.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/g_eps_mu_probe.py` (24/24
full, 18/18 smoke, SPEC_SHA `c2c9c3f2d1eacd5e`) plus
`rh/problem/g_eps_mu.tex` (+ PDF +
`verify_g_eps_mu.py`, 13/13, `G_EPS_MU LEMMA VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: Jacobi-$(0,1)$
$\gamma=n(n+1)/(2n+1)^2$; Chebyshev-$U$ quarters
$\gamma_k=\tfrac14$; monic $\gamma$ homogeneous; full cosine-grid
Fejér is Bernstein--Szegő discrete
($\max_{k\ge2}\lvert\gamma-1/4\rvert=1.836\cdot10^{-6}$ on
$w=9$, union $=S_++S_-$).
Occupied-Fejér already lies in $\lvert\gamma-1/4\rvert$
($w=9$ $0.03596$; core-$42$ max $0.04892$) --- the r381 $0.071$
was *signed* Fejér.
Jump of occupied-Fejér is razor-thin (max $0.3942$ vs $\tfrac25$,
margin $0.0058$); $d_{\mathrm{arm}}$ pulls in on $40/42$ and
supplies jump headroom ($\mu$ max $0.03304$, jump $0.2469$).
Ratio bound $\kappa=4200.6$ is true and useless.
Not construction-pure: permutation of the same weights on the
same nodes kills $17/20$ (seed $3$: $0.07445/0.459$).
Scramble-seed $\mu$ kills (occupation moves); two-period weight
$a=0.95$ stays in.  No $m_4$ (smallest core $n=140$ already in).
Remaining: $F_\varepsilon$ (Fejér-on-occupied = node deletion
from Bernstein--Szegő) and $W_\varepsilon$ (r342 digamma/tent
multiplier vs scramble-of-weights).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r389 are parallel lemma-first / Lean lanes; this round is additive.

**Construction-pure $(R)$ and $(L)$ (r391, LEMMA.CONSTRUCTION_PURE.RL.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/construction_pure_rl_probe.py` (23/23
full, 15/15 smoke, SPEC_SHA `6699da51c8546495`) plus
`rh/problem/construction_rl.tex` (+ PDF +
`verify_construction_rl.py`, 17/17, `CONSTRUCTION PURE RL VERIFIED`).
Two letters.  **$(R)$ REDUZIERT** to the white-block class with
census $K=4$ (CORE-42 max $B_\Sigma/D=2.8196$ at kz$19$;
$\chi_3$-42 max $2.746$; $R$-star kz$37$ $2.975<4$).
Independent weight-rand at frozen fold geometry HOLDS;
positive alignment $P_\omega\approx P_\beta$ BREAKS ($a=0.3$
already $>4$, $a\to 1$ unbounded).  Superblock Gershgorin is
REFUTED as a SATZ (fully-DD only $4/42$).  Geometry kill is
DC/sign-flatten, not merged folds.  **$(L)$ REDUZIERT:**
CORE-42 $L_1$ slope $+0.202<1/4$; CS counting is SATZ but
tautological with $n_{\mathrm{eff}}\sim m$; DC $L_1=m$ kills
field-independent $\gamma<1/4$; the von Mangoldt triangle still
does not close.  COMPOSE$^-$ still needs $(Z')$, $M_3\le\phi$,
Dict, and the two census envelopes.  r389 Weyl energy owns the
signed objects (assist, $C_\varepsilon$, $Z_{\mathrm{loc}}$),
not $(R)(L)$.  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r390 are parallel lemma-first / Lean lanes; this round is additive.

**The deletion transform, reduced (r392, LEMMA.DELETION_TRANSFORM.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/deletion_transform_probe.py` (22/22
full, 19/19 smoke, SPEC_SHA `e4d6ced026e12433`) plus
`rh/problem/deletion_transform.tex` (+ PDF +
`verify_deletion_transform.py`, 14/14, `DELETION TRANSFORM VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: Uvarov
$\gamma_n(\mu)=\gamma_n(\sigma)\,\tau_{n+1}\tau_{n-1}/\tau_n^2$
with $\tau_n=\det(I-K_n[\Xi]W)$, $\tau_0=1$; block = iterated
over $\mathbb{Q}$; Bernstein--Szegő specialises to
$(1/4)\cdot\tau$-ratio up to the r390 residual $1.85\cdot10^{-6}$.
FRAME-A $w=9$ identity $8.993\cdot10^{-15}$ against occupied Fejér.
Assist Uvarov($\mu+\nu$) $\lambda=0.999830$, assist $0.0399$,
cancel $0.9970$; $\mathrm{d}\Delta_{12}=0.04946$ (r388).
Occupied-Fejér kernel does *not* carry Assist ($\lambda=10.12$).
AP deletion ($\rho_{\mathrm{AP}}=1$) stays at $\gamma=1/4$ ---
not a kill of $F_\varepsilon$; clustered run of $3$ kills;
scramble seed $3$ jump $0.4438$ OUT; kz~$55$ jump $0.3942$
(margin $0.0058$) is census, not a corollary of $\rho_{\mathrm{AP}}<1/5$.
Cancellation of Assist sits in the *signs* of $K^\mu[\Xi]$, not
the positive $\tau$-quotients.  Remaining: $\Delta^2\log\tau$
under $F_1$ ($F_\varepsilon$ rest) and Sign-Schur of $K^\mu[\Xi]$
(Assist rest).  $V_3'$ allows relaxing JUMP (not moved).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r391 are parallel lemma-first / Lean lanes; this round is additive.

**The $\tau$-field under $F_1$, reduced (r393, LEMMA.TAU_FIELD.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/tau_field_probe.py` (26/26
full, 20/20 smoke, SPEC_SHA `c3f6b3b94caa78d0`) plus
`rh/problem/tau_field.tex` (+ PDF +
`verify_tau_field.py`, 13/13, `TAU FIELD VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: $F_1$ splits $\Xi$ into singletons
and pairs; $\tau_{\mathrm{cluster}}$ is $1\times1$ Sherman--Morrison /
$2\times2$ det; $\Delta^2\log\tau=\sum_c\Delta^2\log\tau^{(c)}+\Delta^2\log\kappa$;
rank-one locality $\rho_n=\tau_{n+1}/\tau_n=1-(W\pi_n)^\top(I-K_n W)^{-1}\pi_n$
so $\Delta^2=\Delta\log\rho$ (volume does not enter linearly).
FRAME-A $w=9$: 102 clusters, last-12 $\lvert\Delta^2\rvert=0.1553$,
coupling $0.049$ ($\sim 31\%$, load-bearing);
$L^1=0.436>\log\tfrac54$ (triangle fails).
$F_1$ is necessary (run-$3$ jump $0.4619$ OUT at $2/5$ and at
$\mathrm{JUMP}'=0.45$) and not sufficient (random $F_1$ half-fill
jump $1.179$ OUT; isolated centre pair $0.4183$ OUT at $2/5$,
IN at $0.45$).  Scramble seed $3$ is an $F_1$/cluster break.
Core-$42$ $0/42$ OUT at $2/5$, kz~$55$ jump $0.3942$ remains
census even after legal $\mathrm{JUMP}'=0.45$ ($V_3'$ $A_{15}$ air).
Remaining: $L^*$-occupation regularity, sibling to Sign-Schur.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r392 are parallel lemma-first / Lean lanes; this round is additive.

**Sign-Schur, reduced (r394, LEMMA.SIGN_SCHUR.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/sign_schur_probe.py` (24/24
full, 19/19 smoke, SPEC_SHA `f77a50fee61dd4c5`) plus
`rh/problem/sign_schur.tex` (+ PDF +
`verify_sign_schur.py`, 14/14, `SIGN SCHUR VERIFIED`).
**Ausgang REDUZIERT.**  SATZ: Chebyshev-CD signs on the cosine
grid are Dirichlet-zonal; Dirichlet envelope
$\lvert D_n(\alpha)\rvert\le\min(2n+1,1/\lvert\sin(\alpha/2)\rvert)$;
the $2\times2$ Z-matrix bound is false ($\lambda=1+c>\mathrm{maxdiag}$).
Checkerboard / rank-1 conjugability REFUTED (FRAME-A mass-weighted
agree $0.504$; core-$42$ in $[0.429,0.512]$).
Mass-weighted Chebyshev inheritance is census ($0.810$ on FRAME-A;
$[0.810,0.894]$ on core-$42$), not a SATZ.
No source-defined $k^*>2N/5$ (oracle remainder bound $1.90>1$;
entry nearest neighbours constructive).
Two-period lag-$1$ is in-phase ($\lambda=1.0288$ at $k=22$);
scramble holds the mass-map and dies on the envelope;
$\lvert E\rvert$ mutant $\lambda=1.683>1$.
Remaining: Dirichlet/Abel (Weyl) energy of the $\mu$-OP Gram
(r389 rest).  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r393 are parallel lemma-first / Lean lanes; this round is additive.

**Three-gap of the fold mask, refuted (r395, LEMMA.THREE_GAP_MASK.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/three_gap_mask_probe.py` (29/29
full, 21/21 smoke, SPEC_SHA `4f246d22f6f0abe2`) plus
`rh/problem/three_gap_mask.tex` (+ PDF +
`verify_three_gap_mask.py`, 11/11, `THREE GAP MASK VERIFIED`).
**Ausgang REFUTED.**  SATZ: Steinhaus three-gap of $\{k\alpha\}$
on $\mathbb{Z}/q$ (309/309 Farey+Fibonacci, exact) with
$a+b=c$ when three gaps occur; PNT-free integer-log local
three-gap for $n\ge 512$, $M\le 64$ (small $n_0\le 64$ is a
census, $n_{\mathrm{uniq}}$ 8--19).
REFUTED: the $\nu$-mask of a canonical window is globally or
blockwise three-gap (FRAME-A $n_{\mathrm{uniq}}=12$; core-$42$
in $[8,18]$, $0/42\le 5$; EXT grows, $kz=97$ has 13);
$n_{\mathrm{uniq}}\le 3$ plus $F_1$ plus $\rho_{\mathrm{AP}}<1/5$
implies the $\Delta^2\log\tau$ box (wrapping $(1,2,3)$ jump $2.33$
OUT; mechanical $\varphi$ $d=0.1016$ OUT on the box;
wrapping $(2,3,4)$ isolated-singles $8/8$ IN at $h=80$ is a
different class).  The $3/8$-floor and MED-CAP $8/3$ are not
shadows of the cosine-grid gap spectrum ($d_{\min}/d_{\mathrm{med}}=1/3<3/8$,
$d_{\max}/d_{\min}=23>8/3$).
Two-period $\lambda_{22}=1.0288>1$; random $F_1$ jump $1.179$;
scramble seed $3$ sliding-12 three-gap fraction $0$; Assist at
$n_0$ splits random $F_1$ ($\lambda=2.01$) from sparse three-gap
($\lambda=0.997$) but does not identify the source
($2$--$3$-dominated histogram plus sparse tail).
Remaining: that histogram, strictly smaller than three-gap,
still the occupation object of both $F_\varepsilon$ and Assist.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r394 are parallel lemma-first / Lean lanes; this round is additive.

**Isolation of the fold mask, refuted (r396, LEMMA.ISOLATION.01,
lemma-first).**  Sealed census probe
`experiments/tfpt-discovery/isolation_lemma_probe.py` (29/29
full, 22/22 smoke, SPEC_SHA `eb6dca0e0d28d1d3`) plus
`rh/problem/isolation_lemma.tex` (+ PDF +
`verify_isolation_lemma.py`, 10/10, `ISOLATION LEMMA VERIFIED`).
**Ausgang REFUTED.**  SATZ: folded consecutive small integers
are not adjacent on the fold circle (PNT-free); wrapping
$\{2,3,4\}$ is isolated; pair counts on named windows are
machine identities; Dirichlet envelope at separation $2$ is
still $\gg 1$.
REFUTED: $P(N)/n_\nu\to 0$ or $P\le$ a fixed constant
(FRAME-A $2$ pairs; core-$42$ in $[0,16]$, $3/42$ zero-pair;
EXT $kz=97$ has $22$, density $O(0.03)$ stable);
pairs are small-$n$ log collisions (an atom $n\approx 211$
near the cap lands on a pair bin);
isolated + thin tail implies the $\Delta^2\log\tau$ box
($h=40$ wrapping $\{2,3,4\}$ $3/12$ IN; the r395 $8/8$ at
$h=80$ is $n_{\mathrm{ref}}=60$ truncation and dies at natural
depth $2/8$; denser isolated $\{2,2,3\}$ $0/8$; fat tail
helps);
isolated implies $\lambda_{\max}<1$ ($1010$ has $1.405$);
isolation plus the Dirichlet hull closes Gershgorin
($\mathrm{gersh}=1.768$).
Pair count does not drive the source jump (core $42/42$ IN,
$\mathrm{corr}=-0.38$).
Remaining: the r395 $2$--$3$ histogram with a sparse tail ---
pair density $\sim 2\%$ is a shadow of that shape, not a
closing lemma.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r395 are parallel lemma-first / Lean lanes; this round is additive.

**Exact selected domain (r397, PRIME.RH.EXACT_SELECTED_DOMAIN.01,
Lean-only, reviewer quantifier correction).**  `RH/Selected.lean`:
`RealCanonicalWindow` (ℝ-fields, extends `PrimeWindow`) plus the
total construction $W^{\mathbb R}(a,m)=$
`ExactFold`(`ExactPrimeSource`, `ExactArch`, `ExactBorder`,
`ExactBudget`).  Selected sequence $a_k=2^k$,
$r_k=\lfloor\sqrt{k}\rfloor$, $m_k=k\cdot 2^{r_k}-1$ with
$\Delta_k=2^{-r_k}\cdot\log 2$, $a_k\to\infty$, $\Delta_k\to 0$
**PROVED**.  Reduction `weil_nonneg_of_selected_windows` (plain
`fullRead` along the sequence; onset/mesh coverage by cofinality;
consumes the existing arch-channel `sorry`).  C1 holes
`lstar_canonical` / `terminal_q_canonical` **degraded** to the
alternative (rational-certificate) route.  New Lean mincut: named
Prop `selected_augDualResolvent_gt_half`.  Zero new `sorry`;
census **stays 5**.  NO RH CLAIM.  Coexistence: r398 is the
parallel numeric kill-test; this round does not touch
`experiments/next.txt`.

**High-moment inertia, killed (r398,
PRIME.LDAGGER.HIGH_MOMENT_INERTIA.01, reviewer-preregistered
kill-test of P1).**  Sealed census probe
`experiments/tfpt-discovery/high_moment_inertia_probe.py` (30/30
full, 21/21 smoke, SPEC_SHA `bb1dcf6ab66a6156`) plus
`rh/problem/high_moment_inertia.tex` (+ PDF +
`verify_high_moment.py`, 12/12, `HIGH MOMENT VERIFIED`).
**Ausgang KILL_FAIL.**  SATZ: $1_{\{r<1/2\}}\le[2(1-r)]^{2d}$
(Fractions $1296/625$); cycle-sum $\mathrm{tr}(A^k)$ equals
closed walks ($2\times2$ $\mathrm{tr}(A^2)=35/72$);
$0\preceq R_{N-3}\preceq I$ on the named census.
REFUTED as a route: a fixed $d\in\{2,3,4,6,8\}$ with
$2^{2d}\mathrm{tr}((I-R_{N-3})^{2d})<2$ and growing reserve.
FRAME-A $M_d=(33.48,26.79,22.75,18.23,16.03)$, all $\ge 2$,
$36$ eigenvalues in $[\tfrac12,3/5]$; core-$42$ $M_2$ grows
$34.9\to 224.5$ as $N=142\to 878$.
On $n_{-}=1$ no $d$ (even $>8$) yields $<2$ (minimum $15.06$
at $d=11$ on FRAME-A, then diverges).
Scramble $\mathrm{ind}_{-}=21$, $M_2=148$; two-period $M_2=52$;
dead $\chi$ $\ge 2$ but living $\chi$ also $\ge 2$ (not a
separator).  Cycle-sum is not the R399 target.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r396 are parallel lemma-first / Lean lanes; this round is additive.

**Source Weyl energy, refuted as a decay (r399,
PRIME.SOURCE.WEYL_ENERGY.THEOREM.01, reviewer 5.2/5.3).**  Sealed
census probe
`experiments/tfpt-discovery/source_weyl_energy_probe.py` (29/29
full, 22/22 smoke, SPEC_SHA `c5a74fda2d455a52`) plus
`rh/problem/source_weyl_energy.tex` (+ PDF +
`verify_source_weyl.py`, 11/11, `SOURCE WEYL VERIFIED`).
**Ausgang REFUTED** (decay $E^{\mathrm{bulk}}\to 0$ at the
CD-transfer norm).  SATZ: tent interpolant
$d^P_j=-\sum\Lambda(n)n^{-1/2}K_j(\log n)$ (machine
precision on $w=9$, $kz=18$, $kz=52$); Fej\'er Laplacian
$\mathrm{IFFT}(\mathrm{Fej}\odot d^P)=\Delta c^P_{\mathrm{ext}}/L$;
$C_0=C_1=0$; cap outside the CD band so $E^{\mathrm{bulk}}=E$;
transfer $\omega$ from r389 Chebyshev-CD at depth $N_w-3$.
Core-$42$ $E\in[1.178,5.983]$, slope $+0.542$ (grows);
$\mathrm{mean}\,C_m^2/\mathrm{qm}\in[0.427,0.848]$
(quadratic-mean).  Selected $a_k=2^k$, $k=3{\ldots}9$:
$E=0.033{\ldots}0.869$, not monotone to $0$.
Honesty gate: Montgomery--Vaughan MVT is $3\cdot 10^3$--$4\cdot 10^5$
short; a sub-QM bound would be RH-near (circular as a route to
$R^\dagger\succ\tfrac12 I$) and is contradicted by the census.
Scramble $E=3.39>1.2\times$ MAIN (centered $d$ sees $\log n$
cancellation); two-period HHI $0.629$; dead $\chi$ also $O(1)$.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r398 are parallel lemma-first / Lean lanes; this round is additive.



**Bulk one-defect, refuted as rank-one (r400,
PRIME.LDAGGER.BULK_ONE_DEFECT.01, reviewer 5.4).**  Sealed
census probe
`experiments/tfpt-discovery/bulk_one_defect_probe.py` (27/27
full, 22/22 smoke, SPEC_SHA `91a4afa27f249fbb`) plus
`rh/problem/bulk_one_defect.tex` (+ PDF +
`verify_bulk_one_defect.py`, 12/12, `BULK ONE DEFECT VERIFIED`).
**Ausgang FORM_T REFUTED / FORM_P REFUTED.**  SATZ: frame
implication $A+C\ell\otimes\ell\succeq c I\Rightarrow\mathrm{ind}_{-}\le 1$;
rank-$r$ interlacing; Weyl.
The Bernstein--Szegő dual on $Y$ has $\mathrm{ind}_{-}=49$;
MAIN kills $48$ (rank at least $48$, measured $r_{\mathrm{eff}}=9.55$,
leading share $0.105$, numerical rank $49$).
Source $\ell=$ centred difference on $Y$ is orthogonal to
$v_{-}$ (cosine $0.0075$); no source-defined edge functional.
Core-$42$ $\mathrm{ind}_{-}\in\{0,1\}$ on $42/42$ ($28$ P1 + $14$ vacuous),
$\lambda_2(R)-\tfrac12$ in $[4.3\cdot 10^{-8},2.0\cdot 10^{-4}]$.
$C_m$ consecutive-sign correlation does not track $\mathrm{ind}_{-}$
(MAIN $\rho_1=-0.341$ vs scramble $-0.363$, inertias $1$ vs $21$).
Dead $\chi$ satisfy P1 (death is $\mathrm{sch}>0$, r401).
Scramble $\mathrm{ind}_{-}=21$ kills only $14$ of $35$; two-period
kills $0$.  Honesty gate: sub-band MVT is unconditional but
does not see P1 ($d$ orthogonal to $v_{-}$).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r399 are parallel lemma-first / Lean lanes; this round is additive.


**Augmented edge signature (r401,
PRIME.LDAGGER.EDGE_SIGNATURE.01, reviewer 5.5).**  Sealed
census probe
`experiments/tfpt-discovery/edge_signature_probe.py` (33/33
full, 23/23 smoke, SPEC_SHA `395673f2b0b1cee5`) plus
`rh/problem/edge_signature.tex` (+ PDF +
`verify_edge_signature.py`, 13/13, `EDGE SIGNATURE VERIFIED`).
**Ausgang EDGE_SIGNATURE_MODEL.**  SATZ: mixed form; Haynsworth
balance; reconstruction $D^{T}\Phi D=\Phi_{\mathrm{edge}}(a,b)$
identically ($\|E\|=2.22\cdot 10^{-15}$ at FRAME-A); model
lemma $\mathrm{ind}_{-}(\Phi_{\mathrm{edge}})=1+\mathrm{ind}_{-}(A_{\mathrm{edge}})$
on both charts ($\det=\pm 1$).
Census: shift on core-$42$ (28 P1 / 14 vacuous), living
$\chi_{3}$ $37/37$, living $\chi_{4}$ $41/41$; $\tau=(a,b)$
in a disk of radius $3.2$ with $g^{*}\ge 0.08$, stable in $N$;
r375 pair compact but not the $3\times 3$ moduli (isotropic
$\|E\|/g=80.7$).
Dead $\chi$ violate the shift at $\mathrm{sch}>0$ (two-sided).
Scramble $\mathrm{ind}_{-}=21$; two-period $4$.
Cofinal $K$ is not proved.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r399 are parallel lemma-first / Lean lanes; this round is additive.


**P1 construction class, refuted (r403,
PRIME.LDAGGER.P1_CONSTRUCTION.01).**  Sealed
census probe
`experiments/tfpt-discovery/p1_construction_probe.py` (25/25
full, 21/21 smoke, SPEC_SHA `ba6817f54dc2b654`) plus
`rh/problem/p1_construction.tex` (+ PDF +
`verify_p1_construction.py`, 11/11, `P1 CONSTRUCTION VERIFIED`).
**Ausgang P1_CONSTRUCTION_REFUTED.**  SATZ: rank-1 interlacing;
PSD need not finish a lift; $R(cw)=R(w)$.
Fixed-mask weight-rand kills P1 (permute $\mathrm{ind}_{-}\in[20,22]$
on FRAME-A; rademacher-flatten $2$; mild $10^{-4}$ already tips).
The invariant is the von Mangoldt assignment, not the sign mask.
$48=49-1$ is a MAIN tautology; $B|_{\mathrm{neg}}$ is a Gram on
MAIN only (omit returns $49$, only-Gram leaves $13$).
Dead $\chi$ keep P1 on their true weights and leave under
the same permutation.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r401 are parallel lemma-first / Lean lanes; this round is additive.

**Source one-defect Gram, class 3 not reached (r404,
PRIME.LDAGGER.SOURCE_ONE_DEFECT_GRAM.01).**  Sealed
census probe
`experiments/tfpt-discovery/one_defect_gram_probe.py` (21/21
full, 19/19 smoke, SPEC_SHA `c0260053d759bd14`) plus
`rh/problem/one_defect_gram.tex` (+ PDF +
`verify_one_defect_gram.py`, 11/11, `ONE DEFECT GRAM VERIFIED`).
**Ausgang CHOLESKY_TAUTOLOGY / SOURCE_GRAM_NOT_EXACT.**
SATZ: Chebyshev addition; Cauchy kernel; Loewner identity
($4.6\cdot 10^{-41}$); fold linear in lags; $Q^T A_0 Q$ already
PD on FRAME-A ($\lambda_{\min}=5.227\cdot 10^{-3}$).
Euler Gram vs $M$ residual $209$ (align $0.767$); Loewner Gram
vs $A_0$ residual $207$ (align $0.098$); no Fourier $k$-subset
recovers $V_n$ (maxang $90^\circ$, greedy $104/49$); ones-mode
cosine $0.007$; only-Gram still $13$.
Cholesky of $M$ is exact on MAIN and dies under permute
($\mathrm{ind}_- M=6$).  Mutants stay $O(1)$.  Stop rule fires.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r403/r405/r406 are parallel lemma-first / Lean lanes; this round is additive.

**Edge contractive lift, partial (r405,
PRIME.LDAGGER.EDGE_CONTRACTIVE_LIFT.01, reviewer 8/12).**  Sealed
census probe
`experiments/tfpt-discovery/edge_contractive_lift_probe.py` (30/30
full, 25/25 smoke, SPEC_SHA `b91e6629ee86ce23`) plus
`rh/problem/edge_contractive_lift.tex` (+ PDF +
`verify_edge_lift.py`, 12/12, `EDGE LIFT VERIFIED`).
**Ausgang EDGE_LIFT_PARTIAL.**  SATZ: Euler tail; disk Parseval;
Woodbury $\Delta=\kappa_{\mathrm{closed}}(-\mathrm{sch})$ over
$\mathbb{Q}$; Cauchy Gram $\det=1/72$.
Census: geometric lift of the constant on $Y$ residual $8\cdot 10^{-16}$
(no optimiser); ones-split $\Delta>0$, $\kappa>0$, $\|c\|<1$ on
core-$42$; living $\chi_3$ $37/37$ the same.
Dead $\chi_3$ $5/5$ keep $\|c\|<1$ and die at $\mathrm{sch}>0$
(overflow $\|c\|>1$ REFUTED).  Border $\neq$ aggregated
$z^{K+1}$ (relres $0.996$).  Geometric sum and Woodbury $\Delta$
differ on scale; $\kappa$ is not a function of $(a,b)$ alone.
The $A_0$-defect lift stays open (r404 class 3; cosine $0.007$).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r403 are parallel lemma-first / Lean lanes; this round is additive.

**One-defect finite algebra (r406, PRIME.LDAGGER.ONE_DEFECT_LEAN.01,
Lean-only, independent of source-side R404/R405).**
`RH/OneDefect.lean`: three general finite-matrix theorems
**PROVED** sorry-free, plus the min-norm Gram identity.
SATZ A: $H\succ 0\Rightarrow\mathrm{ind}_-(H-\ell\ell^T)\le 1$
(corollary of `rankOne_inertia_antitone`).
SATZ B: $H\succ 0$, $J\succ 0\Rightarrow
(H-\ell\ell^T+UJU^T)\succ 0$ iff $0<\Delta=1-\ell^TH^{-1}\ell
+r^TK^{-1}r$ (rank-1 Schur + Woodbury; mathlib v4.29.1 has
Schur / Weinstein--Aronszajn / `det_add_mul` / `mul_inv_rev`,
not a named Woodbury).
SATZ C: $V^T$ injective, $\ell=Vc$, $\|c\|^2<1\Rightarrow
(VV^T-\ell\ell^T)\succ 0$ (Cauchy--Schwarz).
Fourth: $\|c_{\min}\|^2=\ell^T(VV^T)^{-1}\ell$ and the Gram-side
$\Delta$.  Zero new `sorry`; census **stays 5**.  NO RH CLAIM.
Coexistence: does not wait on R404/R405; this round does not
touch `experiments/next.txt`.

**Dual intertwiner, P1 reduced to $\lambda_2(C)\ge 1$ (r407,
PRIME.LDAGGER.DUAL_INTERTWINER.01).**  Sealed
census probe
`experiments/tfpt-discovery/dual_intertwiner_probe.py` (29/29
full, 26/26 smoke, SPEC_SHA `2ee74c59b57ed1c6`) plus
`rh/problem/dual_intertwiner.tex` (+ PDF +
`verify_dual_intertwiner.py`, 12/12, `DUAL INTERTWINER VERIFIED`).
**Ausgang INTERTWINER_EXACT / NU_RANK_NOT_ONE.**
SATZ: $R=C(I+C)^{-1}$ with $C$ the $\mu$-only dual CD Gram
on $Y$ (chain-stable Cholesky of $G_+$); fractional-linear
dictionary $\mathrm{eig}(R)=\lambda(C)/(1+\lambda(C))$, hence
$\mathrm{ind}_-(A_0)=\#\{\lambda(C)<1\}$ and P1
$\iff\lambda_2(C)\ge 1$; Hankel linearity; Woodbury;
inverse antitone; Euler moment $G=FF^T$ residual
$1.55\cdot 10^{-16}$ (SOURCE_GRAM_EXACT on the moment layer).
FRAME-A: $\|C(I+C)^{-1}-R\|=1.84\cdot 10^{-14}$,
$C_{\min}=0.85712$, $\lambda_2(C)=1.00018$,
$r_{\min}=0.46153$.  $\nu$-rank after compression is
$N_\nu=104$, not one.  Loewner sandwich of the inverse
upper-bounds $R$ (wrong direction for $R\succeq I/2$).
Euler source Gram is not the $G$ that $R$ inverts (rel $141$).
Core-$42$: $\mathrm{nneg}=C\#<1$ on $42/42$ (P1 $28$ /
vacuous $14$).  Dead $\chi_3$ $5/5$ fulfill the transport.
Scramble $21=21$; permute $20=20$.  Signed dual consumes $|u|$.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).  Coexistence:
r374--r406 are parallel lemma-first / Lean lanes; this round is additive.

**$C$-threshold, Nyquist-at-$\tfrac12$ refuted (r408,
PRIME.LDAGGER.C_THRESHOLD.01).**  Sealed
census probe
`experiments/tfpt-discovery/c_threshold_probe.py` (26/26
full, 22/22 smoke, SPEC_SHA `cb03729fa76c98bd`) plus
`rh/problem/c_threshold.tex` (+ PDF +
`verify_c_threshold.py`, 9/9, `C THRESHOLD VERIFIED`).
**Ausgang NYQUIST_REFUTED / AT_MOST_ONE_CENSUS.**
SATZ: $C=BB^T$ (dressed $\mu$-dual CD kernel on $Y$);
$2\times 2$ coherence $\det(C-I)<0$; Rayleigh
$\lambda_{\min}\le d_{\min}$; rank deficiency when
$|Y|>n$; Cauchy interlacing of principal submatrices.
FRAME-A: density $0.283$ not $\tfrac12$, $n=181>|Y|=104$,
$C_{\min}=0.85712$, $\lambda_2=1.00018$, $d_{\min}=1.656$
(diag not $\sim 1$), exception mode hole-Nyquist
$k_{\mathrm{peak}}=52$ not the ones-mode.
Periodic $1010$ at density $\tfrac12$ has a kernel
($nC=3$ or $4$, $\lambda_{\min}=0$) --- not
$\lambda_2=1$ exact.
Thinning $Y$ raises $C_{\min}$; densifying destroys.
Scramble $21$ / permute $20$ break $d_{\min}>1$.
Core-$42$: $nC\in\{0,1\}$ (census $14/28$), $d_{\min}>1$,
one-defect windows are hole-Nyquist.
Dead $\chi_3$ fulfill the threshold dictionary.
P1 remains $\iff\lambda_2(C)\ge 1$ (r407); the RHS is
not proved.  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r407 are parallel lemma-first / Lean
lanes; this round is additive.

**Borodin--Birkhoff intertwiner (r409,
PRIME.RDAGGER.BORODIN_BIRKHOFF_INTERTWINER.01).**  Sealed
census probe
`experiments/tfpt-discovery/borodin_birkhoff_intertwiner_probe.py`
(37/37 full, 31/31 smoke, SPEC_SHA `baee9fc568d8e4ee`) plus
`rh/problem/borodin_birkhoff_intertwiner.tex` (+ PDF +
`verify_borodin_birkhoff.py`, 11/11, `BORODIN BIRKHOFF VERIFIED`).
**Ausgang ONE_DEFECT_TRANSPORT_CENSUS.**
SATZ: Chebyshev CLS of the min-norm interpolant $Y\to X$
in $\mathcal{P}_{<d_0}$, $d_0=N_w-3$, is Jacobi-free and
satisfies $R=(I+\mathfrak{T}_0^*\mathfrak{T}_0)^{-1}$
(FRAME-A residual $2.16\cdot 10^{-14}$ against the r407
chain builder); three bases identical over $\mathbb{Q}$;
$\mathrm{ind}_-(I-\mathfrak{T}^*\mathfrak{T})=\mathrm{ind}_-A_0$.
Literal $\Theta_{\mathrm{terminal}}=C^T\Phi_N C$
**REFUTED** (Haynsworth $\Phi_N$ is the Woodbury template,
not the pair-plus-border Schur).  Unfitted Krein transport
**REFUTED**.  Sequential Uvarov $n_{\mathrm{neg}}^{\mathrm{inn}}\le 1$
on core-$42$ is a census ($42/42$), not a theorem, and
equals $\mathrm{ind}_-A_0$ only on $32/42$.
$\mathfrak{T}^\dagger$ equals the r362 graph factor
(dictionary, not a new $R^\dagger$ theorem); six
terminal-dead $\chi$ windows all flip ($\|\mathfrak{T}^\dagger\|>1$).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r408 are parallel lemma-first / Lean
lanes; this round is additive.

**Hole-Nyquist defect (r410,
PRIME.LDAGGER.HOLE_NYQUIST_DEFECT.01).**  Sealed
census probe
`experiments/tfpt-discovery/hole_nyquist_probe.py` (21/21
full, 20/20 smoke, SPEC_SHA `1ec4122ecc019cd6`) plus
`rh/problem/hole_nyquist.tex` (+ PDF +
`verify_hole_nyquist.py`, 9/9, `HOLE NYQUIST VERIFIED`).
**Ausgang N TESTPOLY_REFUTED / DMIN_CENSUS; Ausgang S
FOURIER_REFUTED / BERNSTEIN_REFUTED / SEQ_REDUCED.**
SATZ: reproducing-kernel bound for $p\in\mathcal{P}_n$;
degree obstruction; $C_{ii}=u^\vee K$; Rayleigh.
The $Y$-Lagrange test poly (deg $103<181$) does
\emph{not} prove $d_i\ge 1$ ($b_{\max}=0.071$, $0/104$).
Chebyshev-CD at full depth clears $81/104$.
$d_{\min}\ge 1$ remains a source census (core-$42$,
$[1.097,1.656]$).  Permute drops $d_{\min}$ by a
Christoffel collapse ($K=0.148$, same $Y$).
Hole-DFT of $C$ is not banded (off-fraction $0.968$).
$\|T_0 v_{\mathrm{Nyq}}\|=0.656<\|T_0\|=1.080$.
Theta-prefix hole-adding: $n_C$ jumps $0\to 1$ at $k=37$
and stays $1$.  P1 remains $\iff\lambda_2(C)\ge 1$;
neither half proves the RHS.  Experiments-side, NO ledger
row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).  Coexistence: r374--r409 are
parallel lemma-first / Lean lanes; this round is additive.

**Threshold identity / energy split (r411,
PRIME.LDAGGER.THRESHOLD_IDENTITY.01).**  Sealed
census probe
`experiments/tfpt-discovery/threshold_identity_probe.py`
(20/20 full, 17/17 smoke, SPEC_SHA `090cbc12b41cb27d`) plus
`rh/problem/threshold_identity.tex` (+ PDF +
`verify_threshold_identity.py`, 9/9, `THRESHOLD IDENTITY VERIFIED`).
**Ausgang ENERGY_SPLIT_EXACT / SATURATION_REFUTED.**
SATZ: $\mathfrak{T}_0^*\mathfrak{T}_0=C^{-1}$, so
$\|\mathfrak{T}_0\|=1/\sqrt{\lambda_{\min}(C)}$;
on the quotient $\mathcal{P}_{<d_0}/\mathcal{K}_0$ this
*is* the dual energy split
($\|q\|_X\le\|q\|_Y$ for every min-norm interpolant).
Exact $\|\mathfrak{T}_0\|=1$ on PD windows is
**REFUTED** ($C_{\min}-1=+4.57\cdot 10^{-8}$ at $k_z=42$,
core-42 PD in $[1.33\cdot 10^{-7},7.54\cdot 10^{-5}]$).
The excess direction is $C$'s lowest eigenvector, not the
Fourier hole-Nyquist face ($\|T v_F\|=0.656<1.080$).
$k=37$ is $\lambda_{\min}(C)$ crossing $1$, not a
Christoffel-weight hole ($K_{\mathrm{last}}=6.94$).
P1 is one excess direction on the quotient (r407 in energy
language).  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r410 are parallel lemma-first / Lean
lanes; this round is additive.

**Graph-resolvent consolidation (r412,
PRIME.LDAGGER.GRAPH_RESOLVENT_LEAN.01).**  Sorry-free finite
algebra in `RH/GraphResolvent.lean`: for $C\succ0$,
$R=C(I+C)^{-1}$ is well-defined, $0\prec R\prec I$,
$R-\tfrac12 I=\tfrac12(I+C)^{-1}(C-I)$, and
$\mathrm{ind}_{-}(R-\tfrac12 I)=\mathrm{ind}_{-}(C-I)=\mathrm{ind}_{-}(I-C^{-1})$.
Energy split: $\mathfrak{T}^*\mathfrak{T}=C^{-1}$ implies
Euclidean contraction iff $C\succeq I$, and at most one
singular value $>1$ iff $\mathrm{ind}_{-}(C-I)\le1$.
Zero-defect composition $C\succ I$ plus $q^\dagger<1$ lifts
to $R^\dagger\succ\tfrac12 I$.  Named Prop
`GraphResolventIsLEnsembleInv` (CD identification $E=C^{-1}$
on `RepresentsLEnsemble`; same class as `P1EqCapInertia`).
`#print axioms` = `[propext, Classical.choice, Quot.sound]`
on every named theorem in the file; zero `sorry`; census
**stays 5**.  Dossier `rdagger_saturation.tex` records P1 in
the four equivalent coordinates and the seventeen closed
languages (DCCXLVI--DCCLXXVIII).  NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged:
`selected_augDualResolvent_gt_half` (base 4 / refined 5).
Coexistence: r374--r411 are parallel lemma-first / Lean
lanes; this round is additive.

**Hole top mode (r413,
PRIME.RDAGGER.HOLE_TOP_MODE.01).**  Sealed
census probe
`experiments/tfpt-discovery/hole_top_mode_probe.py`
(23/23 full, 19/19 smoke, SPEC_SHA `9b0e69fefd5ff609`) plus
`rh/problem/hole_top_mode.tex` (+ PDF +
`verify_hole_top_mode.py`, 9/9, `HOLE TOP MODE VERIFIED`).
**Ausgang TOP_MODE_REFUTED.**
SATZ: Lagrange identity $\sum p(y_i)/P_Y'(y_i)=0$ for
$\deg p\le q-2$; $\pi_{q-1}^Y(y_i)=c/(\omega_i P_Y'(y_i))$
in three bases over $\mathbb{Q}$; $v_{\mathrm{top}}$ is
source-pure from $Y$, $u^\vee$, $P_Y'$ (no eig/SVD/target).
The primary test $Q(I-\mathfrak{T}_0^*\mathfrak{T}_0)Q\succeq 0$
**fails on flagship MAIN** ($\lambda_{\min}=-0.0476$, leftover
$\sigma=1.024$ on $w9$; $\mathrm{corr}(v_{\mathrm{top}},C\text{-ev}_0)=0.6766$,
better than the r410 Fourier face and still not the excess).
QD already fails for $p\equiv 1$ (mass ratio $1.357$).
Core-$42$ P1 hold $4/28$; living $\chi$ P1 $1/37$;
dead $\chi$ $4/6$ (architecture ``dead must hold'' fails).
Reviewer order: one clean MAIN violation closes the route.
P1 remains $\iff\lambda_2(C)\ge 1$; the RHS is not this
vector.  Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r412 are parallel lemma-first / Lean
lanes; this round is additive.

**Top-mode edge (r415,
PRIME.RDAGGER.TOP_MODE_EDGE.01).**  Sealed
census probe
`experiments/tfpt-discovery/top_mode_edge_probe.py`
(26/26 full, 22/22 smoke, SPEC_SHA `0911860fd986649d`) plus
`rh/problem/top_mode_edge.tex` (+ PDF +
`verify_top_mode_edge.py`, 9/9, `TOP MODE EDGE VERIFIED`).
**Ausgang CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT.**
SATZ: Euler tail and disk Parseval (r405, kept);
$-\mathrm{sch}=\beta-\alpha$ over $\mathbb{Q}$ with
$\alpha=(\eta-1)/\kappa$, $\beta=r^T K_W^{-1}r/\kappa$
(r405/r406 rewrite; residual $\le 2\cdot 10^{-17}$ on
the census).  $v_{\mathrm{top}}$ is **not** the bulk
defect ($\cos=0.6766$ at $k_z=9$, $0.058$ at $k_z=18$).
Euler-on-$v_{\mathrm{top}}$ is $|\langle 1,v_{\mathrm{top}}\rangle|^2$,
not $\alpha_T$.  Living $\beta>\alpha$ / dead $\beta<\alpha$
is exactly $\mathrm{sch}<0$ / $\mathrm{sch}>0$ (r401), for
$v_{\mathrm{top}}$ and for the constant.  $H=A_0+vv^T$
PD on only $18/42$ MAIN.  Parallel r413 independently
**REFUTED** HTM; this round shows the edge rewrite does
not become a top-mode-specific positivity.  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).  Coexistence: r374--r413 are parallel
lemma-first / Lean lanes; this round is additive.

**De Branges continuation index (r416,
PRIME.RDAGGER.DEBRANGES_CONTINUATION.01).**  Sealed
census probe
`experiments/tfpt-discovery/debranges_index_probe.py`
(25/25 full, 20/20 smoke, SPEC_SHA `68a6ee35a0dd9b29`) plus
`rh/problem/debranges_index.tex` (+ PDF +
`verify_debranges_index.py`, 9/9, `DEBRANGES INDEX VERIFIED`).
**Ausgang PHASE_DOMINANCE_REFUTED / HB_CENSUS.**
SATZ: Wronskian of the monic 3-atom $X$ pair is
$-\gamma_1$ independent of $z$; Hermite--Biehler interlacing
of $(p_n,q_n)$ on MAIN $42/42$ and $\chi$ $84/84$.
Degree balance at $k_z=9$: $n_X=d_0=181<|X|-1$,
$n_Y=q-1=103$.  Both Stieltjes transforms are Herglotz,
while $\mathrm{ind}_{-}(I-\mathfrak{T}_0^*\mathfrak{T}_0)=1$.
The candidate lemma (contractive $H(E_Y)\hookrightarrow H(E_X)$
up to one mode / $\kappa(\Theta)\le 1$ / phase dominance
with deficit $<2\pi$) **fails on flagship MAIN**:
combinatorial R\"ucklauf $\mathrm{yy}_A=3\not\le 1$,
same-degree $\mathrm{yy}_S=24$, uncorrelated with the
T0-index ($\mathrm{corr}=-0.17$).  Permute keeps
$\mathrm{yy}_A=4$ at $\mathrm{ind}_{-}=20$ (world-separator
silent).  Dead $\chi$ has *fewer* R\"uckl\"aufe, not a
bulk-phase overflow.  The fold-partition counting argument
is closed.  The Potapov index of $\mathfrak{T}_0$ remains
the r409 dictionary $\mathrm{ind}_{-}(I-\mathfrak{T}^*\mathfrak{T})$.
Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r415 are parallel lemma-first / Lean
lanes; this round is additive.

**Source Schur sign (r417,
PRIME.RDAGGER.SOURCE_SCH_SIGN.01).**  Sealed
census probe
`experiments/tfpt-discovery/source_sch_sign_probe.py`
(31/31 full, 19/19 smoke, SPEC_SHA `f2905f2a10fddc51`) plus
`rh/problem/source_sch_sign.tex` (+ PDF +
`verify_source_sch.py`, 10/10, `SOURCE SCH SIGN VERIFIED`).
**Ausgang CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN.**
SATZ: $\mathrm{sch}=\mathrm{den}-2+s^{T}(A_0+U_{\mathrm{CD}}U_{\mathrm{CD}}^{T})^{-1}s$
(Woodbury) equals the unnormalized Sylvester chart
($\mathrm{sch}=\varphi_{bb}+\tilde a^{2}-\tilde b^{2}$ on P1,
$\mathrm{sch}=\varphi_{bb}-(\tilde a^{2}+\tilde b^{2})$ vacuous);
rational toys $-2/3$ and $-7/6$.  Normalized $\tau=(a,b)$
cannot see the sign ($d_3$ quotients it out).  Vacuous chart
with $\varphi_{bb}<0$: the whole disk has $\mathrm{sch}<0$.
P1: hyperbola, large $|\tilde a|$ is the danger axis.
MAIN $42/42$ $\mathrm{sch}<0$; $Q\in[0.283,0.502]$ and
$\mathrm{den}\in[1.460,1.652]$ are $O(1)$, $\mathrm{sch}$ is
their $O(0.04)$ difference (not the r375 $K_2$-excess).
$|\tau|$ falls (slope $-0.41$); $|\mathrm{sch}|$ is flat
(slope $+0.09$).  EXT $k_z=119$, $N=1119$, $|\tau|=0.075$.
Selected $a_k=2^k$ at $k=5,9$ stay negative.  Dead $\chi$
$6/6$ have $\mathrm{sch}>0$, sit on/across the curve
(median distance $0.011$ vs live $0.180$), and $3/5$ escape
the living disk $R=3.2$, while dead P1 keeps $\det K_2<0$
--- $\mathrm{sch}$ is not the r377 product.  The observed
rate $|\tau|\sim N^{-0.47}$ is **not** derived from Uvarov
quotients or fold telescopy (`RATE_OPEN`; PNT-free in form,
no $k_0$).  Cofinal $\mathrm{sch}<0$ is not proved.
Experiments-side, NO ledger row, NO L\* claim,
NO RH CLAIM.  Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r416 are parallel lemma-first / Lean
lanes; this round is additive.

**Border-border sign (r418,
PRIME.RDAGGER.PHI_BB_SIGN.01).**  Sealed
census probe
`experiments/tfpt-discovery/phi_bb_sign_probe.py`
(30/30 full, 19/19 smoke, SPEC_SHA `6ef3a327d623c955`) plus
`rh/problem/phi_bb_sign.tex` (+ PDF +
`verify_phi_bb.py`, 10/10, `PHI BB SIGN VERIFIED`).
**Ausgang SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT.**
SATZ: $\varphi_{bb}=c_J+s^{T}A_0^{-1}s$ with $c_J=\mathrm{den}-2$
and $A_0^{-1}=2(C+I)(C-I)^{-1}$ (r407 $C$-resolvent of the
Sherman--Morrison border).  Uniform $\varphi_{bb}<0$ on the
named living census is **refuted** (vacuous $6/14$ overflow
at $k_z\in\{12,13,16,19,39,49\}$).  Pole-dominance on
living P1 is **refuted** ($3/28$ defect-saves;
median $|D|/|\varphi_{bb}|=0.076$).  Two mechanisms: on P1
$c_J+R_{+}$ is already negative on $25/28$; on the vacuous
chart $\Sigma>0$ and $\varphi_{bb}<0$ iff $c_J<-\Sigma$.
Selected $a_k=2^k$ at $k=4,5,6,7,9$ stay negative (census,
no $k_0$).  EXT six rows all $\varphi_{bb}<0$.
$\varphi_{bb}$ is **not** the sole life/death carrier:
dead P1 keep $\varphi_{bb}<0$ (death is the $\tau$-terms);
dead vacuous have $\varphi_{bb}>0$; $\chi_3$-15 is
pole-dominated *and* dead.  Experiments-side, NO ledger
row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r417 are parallel lemma-first / Lean
lanes; this round is additive.

**Vacuous overflow (r419,
PRIME.RDAGGER.VACUOUS_OVERFLOW.01).**  Sealed
census probe
`experiments/tfpt-discovery/vacuous_overflow_probe.py`
(24/24 full, 16/16 smoke, SPEC_SHA `4809213ddff8cddd`) plus
`rh/problem/vacuous_overflow.tex` (+ PDF +
`verify_vacuous_overflow.py`, 8/8, `VACUOUS OVERFLOW VERIFIED`).
**Ausgang H3_REFUTED / RAZOR_POLE_REFUTED / TAU_SAVE_FINITE / COFINAL_OPEN.**
The r417/r418 tension: $|\tau_{\mathrm{un}}|\to 0$ would make
$\varphi_{bb}$ the asymptotic sign carrier, but six vacuous
windows have $\varphi_{bb}>0$ and still live.
$H3$ (vacuous family empties) is **refuted** (terciles
$3/14\to 7/14$, EXT $3/6$).  The razor-pole account
($(C-I)^{-1}$ explosion) is **refuted** (all 14 VAC sit
at $C_{\min}-1\sim 10^{-7}$, healthy closer; $s$ overlap
$\sim 10^{-10}$).  $H2$ saves the six *now*
($\tau^{2}>\varphi_{bb}$) but vacuous $\tau$ is the vanishing
one, so a cofinal floor fails; the r417 $|\tau|$ fall is
vacuous-driven (slope $-1.24$), P1 is flat.  $H1$ is a
large-$N$ census (EXT/selected VAC $\varphi_{bb}<0$), not a
trend on the six (signed slope $-0.003$, $N$-ranges overlap).
Life of the overflow class vs dead VAC: $\tau^{2}\gtrless\varphi_{bb}$.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).
Coexistence: r374--r418 are parallel lemma-first / Lean
lanes; this round is additive.

**$c_J$ vs $\Sigma$ (r420,
PRIME.RDAGGER.CJ_SIGMA_THRESHOLD.01).**  Sealed
census probe
`experiments/tfpt-discovery/cj_sigma_probe.py`
(20/20 full, 15/15 smoke, SPEC_SHA `46409e2f11820dd6`) plus
`rh/problem/cj_sigma.tex` (+ PDF +
`verify_cj_sigma.py`, 8/8, `CJ SIGMA VERIFIED`).
**Ausgang DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS / COFINAL_OPEN.**
SATZ: $\mathrm{den}=1+\|b\|^{2}/B_w-v_t\cdot s$ with
$B_w=S_{N-2}+5/7$.  All 42 windows have $\mathrm{den}<2$
with $O(1)$ gap $[0.348,0.540]$ (flat).  $s$ sits on
moderate $C$-modes ($\lambda_w\sim 3$--$5$); the naive
occupied-max $\Sigma$-bound is $200$--$24000\times$ (loose).
The balance reserve $-\varphi_{bb}$ is $O(0.03)$ and
**shrinks** along selected $k=4..9$ ($0.105\to 0.038$).
The hoped $O(1)$ gap is refuted.  Both charts share one
$c_J$-vs-self-energy balance.  The overflow six remain a
named finite class.  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r419 are parallel lemma-first / Lean
lanes; this round is additive.

**Reserve limit (r421,
PRIME.RDAGGER.RESERVE_LIMIT.01).**  Sealed
census probe
`experiments/tfpt-discovery/reserve_limit_probe.py`
(22/22 full, 16/16 smoke, SPEC_SHA `234a1113450c476f`) plus
`rh/problem/reserve_limit.tex` (+ PDF +
`verify_reserve_limit.py`, 8/8, `RESERVE LIMIT VERIFIED`).
**Ausgang FLOOR_PREFERRED / LOG_KILLED / K10_BORDER_FAIL / COFINAL_OPEN.**
SATZ: $R=-\varphi_{bb}$; $\|T_0\|-1=-(C_{\min}-1)/2$
on vacuous windows (ratio $1.0000$).
The log model $R\sim c/\log k$ is killed
($\Delta$AIC $18.4$).
Five selected points prefer a floor
$R_\infty\approx 0.030$ versus $k$ (AIC);
$R\to 0$ loses by $\Delta$AIC $6.9$.
EXT vacuous $R$ sits in $[0.029,0.037]$.
$k=8$ pinned (builder, $N=5690$);
$k=10$ border-fails; $k=11$ skipped.
$\mathrm{den}$ is flat; $\Sigma$ moves because
occupation broadens, not because $\|s\|^{2}$ grows.
Three saturation scales (budget / razor /
edge-balance), not one exponent.
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r420 are parallel lemma-first / Lean
lanes; this round is additive.

**$\Sigma$ limit (r422,
PRIME.RDAGGER.SIGMA_LIMIT.01).**  Sealed
census probe
`experiments/tfpt-discovery/sigma_limit_probe.py`
(16/16 full, 12/12 smoke, SPEC_SHA `d81fc5fcb4e87711`) plus
`rh/problem/sigma_limit.tex` (+ PDF +
`verify_sigma_limit.py`, 7/7, `SIGMA LIMIT VERIFIED`).
**Ausgang STIELTJES_EXACT / DENSITY_REFUTED / NEAR1_STABLE / LIMITS_OPEN.**
SATZ: $\Sigma=2\|s\|^{2}+4s^{T}(C-I)^{-1}s$.
A one-pole / Cauchy closed occupancy density is
refuted (relative error $0.73$ / $0.95$).
Near-$1$ mass stays $O(0.01)$: $n_{\mathrm{eff}}$
growth is bulk broadening, not pole-creep.
KS distances fall $0.14\to 0.04$.
EXT vacuous $\Sigma\le 0.469$.
$\mathrm{den}_\infty$ and $\Sigma_\infty$ are not
constructed.  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r421 are parallel lemma-first / Lean
lanes; this round is additive.

**$\mathrm{den}$ limit (r423,
PRIME.RDAGGER.DEN_LIMIT.01).**  Sealed
census probe
`experiments/tfpt-discovery/den_limit_probe.py`
(16/16 full, 13/13 smoke, SPEC_SHA `156933164983782f`) plus
`rh/problem/den_limit.tex` (+ PDF +
`verify_den_limit.py`, 7/7, `DEN LIMIT VERIFIED`).
**Ausgang FORMULA_EXACT / GAMMA_LT1_CENSUS / LIMIT_OPEN / SUBSUM_REFUTED.**
SATZ: $\mathrm{den}=1+\gamma-v_t\cdot s$.
Hierarchy (i) (constructed $\mathrm{den}_\infty$)
is not reached.
$\gamma<1$ on $42/42$+EXT+dead (max $0.724$) is a
census, not a chain theorem;
$\|b\|^{2}$ is not a subsum of $S$.
Census $\mathrm{den}\le 1.652$, gap $\ge 0.348$.
$v_t\cdot s>0$ on the same set.
Dead $\chi$ keep $\mathrm{den}<2$.
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r422 are parallel lemma-first / Lean
lanes; this round is additive.


**$\gamma$ chain (r424,
PRIME.RDAGGER.GAMMA_CHAIN.01).**  Sealed
census probe
`experiments/tfpt-discovery/gamma_chain_probe.py`
(18/18 full, 15/15 smoke, SPEC_SHA `0c85977b0a25576e`) plus
`rh/problem/gamma_chain.tex` (+ PDF +
`verify_gamma_chain.py`, 7/7, `GAMMA CHAIN VERIFIED`).
**Ausgang BESSEL_EXACT / W_TERM_REFUTED / SHARP_CENSUS / GAMMA_OPEN.**
SATZ: $b_k=\langle\sigma,\hat\pi_k^\mu\rangle$,
$\|b\|^{2}$ equals the $\mu$-side Parseval budget.
Termwise $w_k=b_k^{2}/\rho_k$ is not uniform
($\sim 43\%$ of terms $>1$).
Census $\|b\|^{2}\le 0.80\,S$ (so the $5/7$
buffer is not needed) and $\gamma\le 0.724$
on $42/42$+EXT+dead.
Dead $\chi$ keep $\gamma<1$; scramble
border-fails; unnorm $b$ gives $\gamma=2.51>1$.
$\gamma<1$ as a theorem is OPEN (cross-chain).
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r423 are parallel lemma-first / Lean
lanes; this round is additive.


**Cross-chain $\gamma$ (r425,
PRIME.RDAGGER.CROSS_CHAIN_GAMMA.01).**  Sealed
census probe
`experiments/tfpt-discovery/cross_chain_gamma_probe.py`
(17/17 full, 14/14 smoke, SPEC_SHA `458ee51d6db76776`) plus
`rh/problem/cross_chain_gamma.tex` (+ PDF +
`verify_cross_chain.py`, 6/6, `CROSS CHAIN VERIFIED`).
**Ausgang B2_LE_S_SATZ / QN_BRIDGES_BW / DEAD_NEEDS_SLACK / COFINAL_OPEN.**
SATZ: $\|b\|^{2}\le S$ ($K_\mu\preccurlyeq K_{\mu-\nu}$ on $P_{<N}$).
Posted $\|b\|^{2}<B_w$ reduces to $q_N<1$.
On the 42-rung $q_N<1$ census this composes to $\gamma<1$.
Dead $\chi$ have $q_N>1$ (need kernel slack).
Cofinal $q_N$ remains open.
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r424 are parallel lemma-first / Lean
lanes; this round is additive.

**Edge-balance consolidation (r426,
PRIME.RDAGGER.EDGE_BALANCE_LEAN.01).**  Dossier section
"The edge balance chain" in `rh/problem/rdagger_saturation.tex`
(+ PDF) plus `rh/lean/RH/EdgeBalance.lean` (zero `sorry`).
Records the r417–r424 eight identities and the r425 reduction
as finite algebra: Woodbury-sch is the r406 discriminant at
$J=I$; the unnormalized chart is the $3\times 3$ Schur of a
$\{\pm1\}$-signature; vacuous $\mathrm{sch}<0\iff\tau^2>\varphi_{bb}$;
$\mathrm{den}=1+\gamma-v_t\cdot s$ with
$\mathrm{den}<2\iff\gamma<1+v_t\cdot s$;
$\|b\|^2\le S<B_w\Rightarrow\gamma<1$.  Named Props
`BorderIsMuParseval`, `BorderLoewnerLeS`, `QNLtOne`.
`#print axioms` = `propext/Classical.choice/Quot.sound` only.
Census stays **five**.  Floor $R_\infty\approx 0.030$ remains a
census (two lines).  Two open limits: cofinal $q_N<1$
(Problem, reduced $\gamma<1$; r425
`B2_LE_S_SATZ / QN_BRIDGES_BW / COFINAL_OPEN`) and constructed
$\Sigma_\infty$ with $\Sigma_\infty<2-\mathrm{den}_\infty$.
NO ledger row, NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).


**Campaign audit (r427,
PRIME.RDAGGER.CAMPAIGN\_AUDIT.01).**  Adversarial
re-verification of R397--R426 on independent
code paths.  Sealed probe
`experiments/tfpt-discovery/campaign_audit_probe.py`
(52/52 full, 44/44 smoke, SPEC\_SHA `b317327d451ab0c6`)
plus `rh/problem/campaign_audit.tex` (+ PDF +
`verify_campaign_audit.py`, 9/9, `CAMPAIGN AUDIT NOTE VERIFIED`).
**Ausgang 0 BUG / 2 SUSPECT / 5 CLEAN.**
CLEAN: intertwiner $R=C(I+C)^{-1}$ on $k_z=9,17,12$
(w9 formula $3.38\cdot10^{-12}$);
QD mass $1.357130$ from one full-carrier dual;
$\|\mathfrak{T}_0\|_{\mathrm{w9}}=1.080138437324$
($\kappa(C)=2.086\cdot10^3$, r409 $1.00000$ is
display rounding of a $2\cdot10^{-8}$ dip);
kernel Loewner on PD truncated Grams;
$6/6$ dead $q_N>1\Leftrightarrow\mathrm{sch}>0$.
SUSPECT: floor $R_\infty\approx0.030$ vs $k$ conceals
the $N=5690$ vs $1433$ inversion (vs $N$ the winner
is M3); disclosed $k=8$ pin reuse r421$\to$r425;
float64 \texttt{eigvalsh} razors at $56\times$ noise.
No round verdict of R397--R426 changes.
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r426 are parallel lemma-first / Lean
lanes; this round is additive.


**$q_N$ reopened (r428,
PRIME.TERMINAL.QN\_REOPENED.01).**  Sealed
census probe
`experiments/tfpt-discovery/qn_reopened_probe.py`
(23/23 full, 19/19 smoke, SPEC\_SHA `fc2c617a6bd34c6c`) plus
`rh/problem/qn_reopened.tex` (+ PDF +
`verify_qn_reopened.py`, 6/6, `QN REOPENED VERIFIED`).
**Ausgang SELECTED\_MARGIN\_GO / OVERLAP\_VAC\_ONLY / ZLOC\_WINS / COFINAL\_OPEN.**
On the selected sequence $a_k=2^k$ ($k=3,4,5,6,7,9$;
$k=8$ builder-pinned) $q_N$ stays in $[0.00070,0.3828]$
with minimum margin $0.617$ against the $42$-rung
minimum $0.0195$ at $\mathrm{kz}=16$.
COMPOSE envelopes are comfortable
($R\le 1.40\ll 4$, $L_1\le 0.63\ll 3$,
$\lvert Z_{\mathrm{loc}}\rvert\le 0.487<\tfrac12$).
Razor-overlap is **not** a global fourth death
coordinate (P1 living share up to $3.6\cdot 10^{-2}$
overlaps dead $\chi$; the r422 four-order split is
vacuous-only; $\mathrm{kz}=16$ near-death has share
$5.4\cdot 10^{-9}$).
The $C_{\min}$ Nyquist face is REFUTED on VAC
($\cos=-0.007$ vs P1 $-0.386$).
Winner coordinate $\lvert Z_{\mathrm{loc}}\rvert$;
sharpest sublemma $\lvert Z_{\mathrm{loc}}(W_k)\rvert\le\tfrac12$
on MAIN selected ($k=3$ tight; scramble breaks it).
Cofinal $q_N<1$ remains open.
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r427 are parallel lemma-first / Lean
lanes; this round is additive.


**$|Z_{\mathrm{loc}}|$ head bound (r429,
PRIME.TERMINAL.ZLOC\_HEAD\_BOUND.01).**  Sealed
probe
`experiments/tfpt-discovery/zloc_head_probe.py`
(24/24 full, 18/18 smoke, SPEC\_SHA `cb57a725042119da`)
plus `rh/problem/zloc_head.tex` (+ PDF +
`verify_zloc_head.py`, 6/6, `ZLOC HEAD VERIFIED`).
**Ausgang FORMULA\_SATZ / TRIANGLE\_REFUTED / BOUND\_CENSUS / NO\_K0.**
The identity $Z_{\mathrm{loc}}=t_{\mathrm{loc}}+\mathrm{chain}$
is SATZ (Lean `canonical_split`; pins $0.486846/0.157211/0.227187$).
The support is the geometric $F=1/5$ hull-edge on $[-1,1]$,
not a finite von~Mangoldt head ($n_{\mathrm{edge}}$ $85$--$1691$).
Unsigned triangle / Chebyshev / left--right Abel are REFUTED
on selected (tri $2.24$--$19.24$, two-point slope $+0.72$;
no explicit $k_0$).
$|Z_{\mathrm{loc}}|\le 1/2$ remains a finite census
($k=3$ tight, scramble $0.524$).
Hoped $L_1\le 3/5$ FAILS at $k=9$ ($0.628$); $2/3$ works.
$R\le 1.396<3/2$ is census.
Honest terminal balance: identity + COMPOSE$^-$ SATZ;
$|Z_{\mathrm{loc}}|$, $R$, $L_1$ census; $k=8$ pin; $k\to\infty$ open.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.
Coexistence: r374--r428 are parallel lemma-first / Lean
lanes; this round is additive.

**Dossier update (R-DOSSIER, reviewer DCCXCVII).**
Consolidation of `rh/problem/rdagger_saturation.tex` (+ PDF)
to the DCCXCVI campaign close.  No new probe, no new claim.
Adds: (i) section "The two cancellation cores" — bulk
$\lambda_2(C)\ge 1$ with the four killed candidate vectors
(ones-mode $|\langle v,1\rangle|=0.007$; centred difference
cosine $0.0075$; Fourier/Nyquist overlap $0.386$; $v_{\mathrm{top}}$
leftover $\sigma=1.024$), QD mass $1.357130$, min-norm save
$\|\mathfrak{T}_0 v_1\|=0.359$, r399 circularity; terminal
$Z_{\mathrm{loc}}$ identity (r429: $Z=t_{N-2}+\mathrm{chain}$,
hull-edge sum, pins $10^{-14}$, cancellation factor
$0.013$--$0.145$, triangle $2.24$--$19\times$ slope $+0.719$)
and the selected location change (r428: margin $0.617$ vs
$0.0195$, old ladder a quantifier artefact); (ii) section
"Audit" — r427 verdict table ($0$ BUG / $5$ CLEAN / $2$
disclosed SUSPECT; kernel-Loewner definiteness hypothesis
explicit); (iii) section "Current architecture (Potapov
program)" — open-program problem statements
$\mathcal{S}_{\le 1}$ bulk, $\mathcal{S}_0$ edge via Redheffer
pivot $\tfrac14-|Z_{\mathrm{loc}}|^2$, two quantifier
weakenings (semidefinite; frequently; positive-density
fallback with averaged index).  Refutation table extended to
$28$ entries (r413/r415/r416/r429 and the r409 graph-factor
closures).  NO ledger row, NO L\* claim, NO RH CLAIM.
Mincut unchanged (base 4 / refined 5).
Lean named-Prop mincut (r430):
`frequently_selected_augDualResolvent_ge_half`;
the r397 Prop `selected_augDualResolvent_gt_half` is the
stronger alternative.

**Semidefinite frequently selected (r430,
PRIME.RH.SEMIDEFINITE_FREQUENT_SELECTED.01, Lean-only,
reviewer quantifier correction).**  `RH/FrequentlySelected.lean`:
(1) **semidefinite suffices** —
`Rdagger_ge_half_iff_augmented_posSemidef` (`R† ⪰ ½I` ⟺
augmented form PSD; same spectral comparison as A3 with
`PosSemidef`); (2) **infinitely often suffices** —
`weil_nonneg_of_frequently_selected` / `rh_of_frequently_selected`
(`∃ᶠ k, R_k† ⪰ ½I` plus the named bridge
`SelectedSemidefImpliesPlainReads` ⇒ `∀ f, 0 ≤ weilForm f`;
onset/mesh by `selected_covers`; arch sorry consumed, not
new).  Density corollary and mean-value trick **PROVED**.
New Lean mincut: named Prop
`frequently_selected_augDualResolvent_ge_half`.  Zero new
`sorry`; census **stays 5**.  NO RH CLAIM.  Coexistence:
r431/r433 are the parallel discovery lanes; this round does
not touch `experiments/next.txt`.

**Quantifier mincut audit (r434,
PRIME.RH.QUANTIFIER_MINCUT_AUDIT.01, Lean-only, reviewer
DCCCII terminal-bypass question).**  Direct Selected-R†
semidefiniteness **bypasses** the old global terminal quantor:
`terminal_q_canonical` / `lstar_canonical` are OFF the FREQ
RH-path (kept, not deleted; alternative
`L† ⟺ L* ∧ Terminal` on all `CanonicalWindow`s).  Also OFF
PATH: `pair_terminal_dictionary`,
`mainWindow_iff_builtFromPrimeSource`.  ON PATH: named mincut
`frequently_selected_augDualResolvent_ge_half`, named remainder
`SelectedACapPsdImpliesPlainReads` (`A_cap ⪰ 0` ⇒ `fullRead`),
and the existing classical sorry
`arch_elementwise_stabilization`.  The L† ⟺ R† identification
on the real window is **PROVED**
(`masterCap_posSemidef_iff_Rdagger_ge_half`);
`SelectedSemidefImpliesPlainReads` is **not** a corollary of
that iff alone (`fullRead` is the three-channel Weil pairing)
but **is** a theorem of the thinner remainder.  Zero new
`sorry`; census **stays 5**.  NO RH CLAIM.

**Lean fidelity repair (r463,
PRIME.RDAGGER.LEAN\_FIDELITY\_REPAIR.01, Lean + sealed probe).**
Sealed probe
`experiments/tfpt-discovery/lean_fidelity_probe.py`
(11/11 smoke/full, SPEC\_SHA `0ef28519b5969b8a`, k=5/9/10 pins)
plus `rh/problem/lean_fidelity.tex` (+ PDF +
`verify_lean_fidelity.py`, 9/9, `LEAN FIDELITY REPAIR VERIFIED`).
**Ausgang FAITHFUL\_OBJECT\_PINNED / BRIDGES\_TYPED / CENSUS\_8.**
`RH/FaithfulFold.lean` replaces the selected raw-atom cosine fold
with the production pipeline (tent lags, circulant spectral density,
grid fold, sign split); exported k=5/9/10 values pin the
transcription against the Python builder.  `archRead` is a concrete
lag pairing; only coefficient values remain external.  The FREQ
endpoint is renamed
`internal_weil_nonneg_of_frequently_selected` (not RH).
`RH/ExternalBridges.lean` types dense extension, standard
explicit-formula identification, and Mathlib
`RiemannHypothesis` as three honest `sorry` candidates; Lean sorry
census **5 → 8**.  The r462 gap-map diagnostic
(`HIDDEN\_GAP\_FOUND`) is kept as sealed history only and is **not**
rerun — r463 invalidates its old success condition.  Experiments-side,
NO ledger row, NO L\* claim, NO RH CLAIM.

**Source Potapov factor (r431,
PRIME.RDAGGER.SOURCE\_POTAPOV\_FACTOR.01, reviewer
discovery 1 of 2).**  Sealed probe
`experiments/tfpt-discovery/source_potapov_probe.py`
(17/17 full, 17/17 smoke, SPEC\_SHA `64eabb7c2448dd48`)
plus `rh/problem/source_potapov.tex` (+ PDF +
`verify_source_potapov.py`, 7/7, `SOURCE POTAPOV VERIFIED`).
**Ausgang SOURCE\_FACTOR\_NOT\_FOUND.**
The unipotent Redheffer product of point-mass $2\times 2$
factors equals the Cauchy $m$-function of $X$ (exact over
$\mathbb{Q}$; $z=7/3$ gives $-7471/22950$).
Lagrange $S_0$ at kernel dimension $0$ is the Cauchy--$\pi$
kernel of the $\pi_Y(X)^2$-dressed $X$-measure (exact).
Gate 3 fails: that Pick is PD ($\kappa=0$) while
$I-\mathfrak{T}_0^*\mathfrak{T}_0$ has one negative square
on the $k_{\mathrm{dim}}=0$ toy ($D_{11}=-1744/2025$) and on
$w_9$ / $k_z=15$ / $k_z=18$ ($\|\mathfrak{T}_0\|=1.08014$,
$1.10672$, $1.24966$).
Source-order growing-$Y$ Uvarov has $0$ negative pivots
(min $3.25\cdot 10^{-7}$); lag-local $\mathrm{fold}(c^P_p)$
has $\mathrm{ind}_-=18/19/15$ for $p=2,3,5$ --- not simpler
(stop rule 3).  $\Lambda$-permute / jitter / scramble send
target $\mathrm{ind}_-$ to $20/19/21$; the Euler product
stays $\kappa=0$.  Twin keeps $\mathrm{ind}_-=1$.
R432 (Krein--Langer index one) is blocked (contract:
only if `FACTOR_EXACT`).
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.
Coexistence: r374--r430 and r433 are parallel lemma-first
/ Lean / edge-Redheffer lanes; this round is additive.

**Source Potapov audit (r431-AUDIT).**  Adversarial
re-check of `SOURCE_FACTOR_NOT_FOUND` on independent
constructors (no import of `source_potapov_probe`).
Sealed probe `experiments/tfpt-discovery/r431_audit_probe.py`
(22/22 full, 21/21 smoke, SPEC\_SHA `72f5484cc290b740`)
plus `rh/problem/r431_audit.tex` (+ PDF +
`verify_r431_audit.py`, 7/7, `R431 AUDIT NOTE VERIFIED`).
**Ausgang CONFIRMED.**  Positive-mass $J$-products stay
in $\mathcal{S}_0$ under multiplication and under the
Homma Redheffer star (non-commuting Blaschke--Potapov
$J$-kernel Pick $\mathrm{ind}_-=0$; unipotent star is
the mass sum).  R431 pins reproduce
($m_X(7/3)=-7471/22950$, $D_{11}=-1744/2025$,
$\lambda_{\min}(P_X)=8.67731$, source-order Uvarov
$0/104$ min $3.248\cdot 10^{-7}$, lag-local $18/19/15$).
Cauchy--$\pi$ holds on a second six-node $\mathbb{Q}$-window
(negatives live in $W_Y-S_0$, never in $P_X$).
No second discovery round.  Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.  Mincut unchanged
(base 4 / refined 5).
Coexistence: r374--r433 are parallel lemma-first / Lean
/ edge-Redheffer lanes; this round is additive.


**Edge as Redheffer step (r433,
PRIME.RDAGGER.EDGE\_REDHEFFER\_COMPLETION.01).**  Sealed
probe
`experiments/tfpt-discovery/edge_redheffer_probe.py`
(27/27 full, 24/24 smoke, SPEC\_SHA `8371b954f4d56847`)
plus `rh/problem/edge_redheffer.tex` (+ PDF +
`verify_edge_redheffer.py`, 8/8, `EDGE REDHEFFER VERIFIED`).
**Ausgang REDHEFFER\_EXACT / PIVOT\_IS\_ONE\_MINUS\_QDAG / QUARTER\_NOT\_UNIVERSAL.**
The r362/r369 augmentation $R\to R^{\dagger}$ **is** the
terminating $2\times 2$-block Redheffer star of the bulk
colligation $\Theta=[[A,U],[U^{T},0_{3}]]$ with edge factor
$E=J=\mathrm{diag}(I_{2},1/\mathrm{den})$ (SATZ: $\mathbb{Q}$
residual $0$, $\mathrm{den}=23/30$; w9 residual $1.9\cdot 10^{-15}$;
sequential CD-then-border equals the packed $3\times 3$).
Last Potapov pivot extracted from the border of
$M^{\dagger}$ (r362 $\mathrm{sch}_{b}/q^{\dagger}$), **not**
defined from $\mathrm{sch}$:
$\delta:=1-q^{\dagger}=4\,\mathrm{sch}_{b}/(1+2\,\mathrm{sch}_{b})=-\mathrm{sch}$
with $c'=1$ ($\mathbb{Q}$: $\mathrm{sch}=-187/450$,
$\mathrm{sch}_{b}=187/1426$, $\delta=187/450$).
Energy form $\delta=1-\lvert\alpha_{\mathrm{edge}}\rvert^{2}$
with $\lvert\alpha_{\mathrm{edge}}\rvert^{2}=q^{\dagger}$.
The companion $\delta=c(\tfrac14-\lvert Z_{\mathrm{loc}}\rvert^{2})$
is **not** world-blind (selected $c\in[0.155,5.51]$; living
$\chi_{3}$-$9$ and vacuous MAIN $\mathrm{kz}\,12/16$:
$\delta>0$ but quarter $<0$).
Dead $\chi$ $6/6$ via $\delta<0$; living MAIN+$\chi$ $\delta>0$;
scramble $\mathrm{nneg}(A_{0})=21$ (bulk already dead).
$k=3$: $\lvert Z_{\mathrm{loc}}\rvert=0.486846$, air $0.013154$,
$\delta=0.071564>0$.
Kills: drop-border (no $3\times 3$ pivot); ones-Woodbury
$\Delta=2.11\cdot 10^{-3}\neq\delta$; r263 $q_{N}=(7/5)Z^{2}$
on the full $Z$, not $Z_{\mathrm{loc}}$.
No Lean this round (Cayley mixed-form bridge not in Lean).
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row,
NO L\* claim, NO RH CLAIM.
Coexistence: r374--r430 are parallel lemma-first / Lean
lanes; this round is additive.

**P1 as an overload bound (r435,
PRIME.RDAGGER.P1\_OVERLOAD.01).**  Sealed probe
`experiments/tfpt-discovery/p1_overload_probe.py`
(23/23 full, 20/20 smoke, SPEC\_SHA `d032621d5417873f`)
plus `rh/problem/p1_overload.tex` (+ PDF +
`verify_p1_overload.py`, 8/8, `P1 OVERLOAD VERIFIED`).
**Ausgang DEPTH\_CHAIN\_EXACT / GK\_UNIVERSAL\_REFUTED / SAVE\_RATE\_CENSUS.**
$n_{-}(A_0)\le 1$ is a crossing budget on the selected
sequence (29 vacuous windows are case 1 of the two-case
inertia theorem).  Dictionary $n_{-}(A_0)=n_{\mathrm{C}}(N_w-3)$.
Gantmacher--Krein / Cauchy--$\pi$ universal $n_{-}\le 1$
REFUTED over $\mathbb{Q}$.  Core-42 ends in $\{0,1\}$
($28$ P1 / $14$ VAC).  No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r436 / r438 are parallel and not dropped.

**P2 determinant as reverse-CS (r436,
PRIME.RDAGGER.P2\_DETERMINANT.01).**  Sealed probe
`experiments/tfpt-discovery/p2_determinant_probe.py`
(26/26 full, 19/19 smoke, SPEC\_SHA `d596aecc4dff3ef1`)
plus `rh/problem/p2_determinant.tex` (+ PDF +
`verify_p2_determinant.py`, 8/8, `P2 DETERMINANT VERIFIED`).
**Ausgang REDUZIERT / IDENTITY\_EXACT / ANATOMY\_MIXED / COARSE\_KILLED\_AT\_KZ46 / ALTERNATION\_EXPLAINED.**
On the $n_{-}=1$ branch, $\det K_{2}=\det(K_{2,+})-Q$ with
$Q=p^{T}\operatorname{adj}(K_{2,+})p=\|p\|^{2}+p^{T}\operatorname{adj}(R_{+})p$
($\mathbb{Q}$-toy $\det=-7=2-9$).
$C_{\min}=\psi_{-}$ (r407).  Drop-$\psi_{-}$ kills P2;
vacuous $n_{-}=0$ has no pole ($14/42$ core, $\det K_{2}>0$).
Direction-free coarse bound $\|p\|^{2}>\lambda_{\max}(K_{2,+})$
is sufficient SATZ, $44/45$, killed at kz\,46 (same window
as the r375 Cauchy test).  Anatomy mixed ($T_a$ $25$,
$T_d$ $4$, $T_x$ $16$).  Alternation
$\det K_{2}<0\iff h_{N}h_{N+1}<0$ (r377; $\mathrm{sch}$ is
a different coordinate, r417).  Remainder:
$p^{T}K_{2,+}^{-1}p>1$ (CD--$C_{\min}$ coupling).
No Lean this round.  Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r438 are parallel and not dropped.

**Evolutionary certificate search (r438,
PRIME.SEARCH.EVOLUTIONARY\_CERTIFICATE.01).**  Sealed probe
`experiments/tfpt-discovery/evolutionary_certificate_probe.py`
(29/29 full, 29/29 smoke, SPEC\_SHA `d6c1624b82717fba`)
plus `rh/problem/evolutionary_certificate.tex` (+ PDF +
`verify_evolutionary_cert.py`, 10/10, `EVOLUTIONARY CERT VERIFIED`).
**Ausgang A:NOT\_FOUND / B:NOT\_FOUND / C:NOT\_FOUND.**
Hard train/holdout split.  Tracks A/B/C do not yield a
source-pure certificate for the $C$-defect / P2 identity /
canonical-cut $n_{\mathrm{C}}\le 1$ beyond the already named
r375/$\psi_{-}$ identity.  No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r440 are parallel and not dropped.

**Interpolant residual Loewner/Bezout (r439,
PRIME.RDAGGER.INTERPOLATION\_RESIDUAL\_LOEWNER\_BEZOUT.01).**
Sealed probe
`experiments/tfpt-discovery/residual_loewner_probe.py`
(25/25 full, 22/22 smoke, SPEC\_SHA `7a0b53f06d2c7564`)
plus `rh/problem/residual_loewner.tex` (+ PDF +
`verify_residual_loewner.py`, 7/7, `RESIDUAL LOEWNER VERIFIED`).
**Ausgang RESIDUAL\_LOEWNER\_PLUS\_CONTROLLED\_DIAGONAL.**
Displacement rank $2$ SATZ (exact $\mathbb{Q}$ on both toys;
$\sigma_3/\sigma_2\sim 10^{-14}$ on $w_9/k_z15/k_z18$;
survives permute).  $S_0=K_{YY}^{-1}$ SATZ.
At $k_{\dim}=0$, dressed Loewner
$\Delta D_0\Delta=L_{-\widetilde{m}}+\mathrm{diag}(w_Y(P_Y')^2)$
SATZ; $D_0$ itself is not ones-Loewner for $\lvert Y\rvert\ge 3$.
B1 $\mathrm{Bez}(P_Y,Q)$ miss (Cauchy--$\pi$ is $m$-like
with $P_X$ poles).  CInd of $\widetilde{m}/P_Y'$ is not P1.
P1 problem: $n_{-}(W_Y-K_{YY}^{-1})\le 1$.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 are parallel
and not dropped.

**Mean tau index (r440,
PRIME.RDAGGER.MEAN\_TAU\_INDEX.01).**  Sealed probe
`experiments/tfpt-discovery/mean_tau_index_probe.py`
(28/28 full, 28/28 smoke, SPEC\_SHA `3807189a56e259da`)
plus `rh/problem/mean_tau_index.tex` (+ PDF +
`verify_mean_tau.py`, 8/8, `MEAN TAU INDEX VERIFIED`).
**Ausgang IDENTITIES\_EXACT / COLLAR\_BOSS\_QUANTIFIED / BLOCK\_MEAN\_CENSUS / UNCONDITIONAL\_OPEN.**
Three finite identities, no analytic bound:
(T1)~$\kappa^{\dagger}=\mathrm{ind}_{-}(R^{\dagger}-\tfrac12 I)=\#\{s\in(0,1):\tau^{\dagger}(s)=0\}$
(SATZ over $\mathbb{Q}$; w9 three-way at $2\cdot 10^{-14}$);
(T2)~argument principle, integrand Jacobi SATZ, $\mathbb{Q}$ winding $1.000$;
(MI2)~block-mean identity, linearity $4\cdot 10^{-15}$, Lean landing
site `exists_index_zero_of_block_mean_lt_one` (r430).
The $1/2$-cluster of $R^{\dagger}$ maps to zeros of $\tau^{\dagger}$
in a shrinking collar of $s=1$ ($\mathrm{gap}_{+}$ $3.0\cdot 10^{-3}\to 1.9\cdot 10^{-8}$
on selected $k=3..9$); a circle of radius $0.40$ winds $0$, radius $0.499$ is fractional.
Source integrand: CD residual $2\cdot 10^{-12}$, cyclic $TT^{*}$ / Dirichlet diagonal.
Census: selected $6/6$ and core-42 $42/42$ have $\kappa^{\dagger}=0$ (mean $0<1$, no dead trend);
dead $\chi$ $6/6$ have $\kappa^{\dagger}=1$.
Soft mutants (tr $G$, $M_2$) blind; $s$ is a counting variable (r265 no-go stays).
$k=8$ not rebuilt.  No Lean this round (landing site already proved).
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 are parallel and not dropped.

**Diagonal lifts Loewner (r441,
PRIME.RDAGGER.DIAGONAL\_LIFTS\_LOEWNER.01).**
Sealed probe
`experiments/tfpt-discovery/diag_lifts_loewner_probe.py`
(17/17 full, 13/13 smoke, SPEC\_SHA `1de031a3dbd907af`)
plus `rh/problem/diag_lifts_loewner.tex` (+ PDF +
`verify_diag_lifts.py`, 6/6, `DIAG LIFTS VERIFIED`).
**Ausgang REDUZIERT.**
$L_{\widetilde{m}}$ is the dressed Cauchy Gram (always
PSD); $X$-between-$Y$ does not set $L$-inertia.
Lift count SATZ
$n_{-}(W_Y-K^{-1})=\#\{\lambda(W^{1/2}KW^{1/2})<1\}$.
$d_{\min}>1\Rightarrow n_{-}\le 1$ REFUTED (6-node).
Selected bound OPEN (census).  kz52 one slip.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r442 are
parallel and not dropped.

**Unconditional block mean (r442,
PRIME.RDAGGER.UNCONDITIONAL\_BLOCK\_MEAN.01).**
Sealed probe
`experiments/tfpt-discovery/block_mean_probe.py`
(19/19 full, 19/19 smoke, SPEC\_SHA `bc5644a9924f2eab`)
plus `rh/problem/block_mean.tex` (+ PDF +
`verify_block_mean.py`, 8/8, `BLOCK MEAN VERIFIED`).
**Ausgang REDUZIERT / DICTIONARY\_EXACT / UNSIGNED\_MAJORANT\_REFUTED / SELECTED\_POINTWISE\_CENSUS / MEAN\_BOUND\_OPEN.**
One lemma SATZ: $\kappa^{\dagger}=1\{q^{\dagger}>1\}$
(so the block mean is the frequency of $q^{\dagger}>1$).
Source double sum residual $1.2\cdot 10^{-15}$.
Unsigned Chebyshev/Mertens majorant REFUTED
($|b|$-envelope $38.5$; $|\sigma|$ $2.10$ / $87$ at $k=5,9$).
Selected $6/6$ and core-42 $42/42$ pointwise living
($q^{\dagger}<1$; mean $0.932$ / $0.961$; trend toward $1$,
not falling).  Mean bound OPEN.  $k=8$ not rebuilt.
No Lean this round (landing site already proved).
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 are
parallel and not dropped.

**Selected delta floor (r443,
PRIME.RDAGGER.DELTA\_FLOOR\_SELECTED.01).**
Sealed probe
`experiments/tfpt-discovery/delta_floor_probe.py`
(17/17 full, 17/17 smoke, SPEC\_SHA `80a676a7c804bdc8`)
plus `rh/problem/delta_floor.tex` (+ PDF +
`verify_delta_floor.py`, 6/6, `DELTA FLOOR VERIFIED`).
**Ausgang REDUZIERT / CHART\_EXACT / SLICE\_FLOOR\_PREFERRED / FULL\_SEQUENCE\_UNSETTLED / KZ16\_SELECTED\_SPECIFIC / DEEP\_LOCKED / COFINAL\_OPEN.**
Chart SATZ: $\delta=R+\tau$-correction.
Floor preferred only on the r421 $k=5..9$ slice
($\delta_{\infty}=+0.0267$, EXT band $[0.0264,0.0452]$).
Full selected $k=3..9$ prefers $M_3$ (the $k=5$ bump).
$N$-abscissa killed (r427).  $k_z16$ sits at $0.00151\ll 0.027$.
$k=8/10+$ not rebuilt (CG never reached).  Liminf OPEN.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442
are parallel and not dropped.

**Signed border mean (r444,
PRIME.RDAGGER.SIGNED\_BORDER\_MEAN.01).**
Sealed probe
`experiments/tfpt-discovery/signed_border_mean_probe.py`
(21/21 full, 21/21 smoke, SPEC\_SHA `16ac676cfc571660`)
plus `rh/problem/signed_border_mean.tex` (+ PDF +
`verify_signed_border.py`, 8/8, `SIGNED BORDER MEAN VERIFIED`).
**Ausgang ZIRKULAER / TRIPLE\_SUM\_EXACT / POLE\_NOT\_CARRIER / DIAGONAL\_OVERFLOWS / OFFDIAG\_LOADBEARING / DEAD\_CHI\_POLE\_OVERSHOOT.**
Triple sum SATZ.  Pole is not the living-mean carrier
(share $\le 0.003$).  Diagonal overflows from $k=7$
($40.8$ at $k=9$); signed off-diagonal is load-bearing.
Dead $\chi$ die by a pole overshoot.  The mean bound is
circular: regular off-diagonal cancellation against a
window-dependent OP kernel (second circularity after r399).
$k=8$ not rebuilt.  No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443
are parallel and not dropped.

**Deep builder (r445,
PRIME.INFRA.DEEP\_BUILDER.01).**
Sealed probe
`experiments/tfpt-discovery/deep_builder_probe.py`
(25/25 full, 24/24 smoke, SPEC\_SHA `57831e610b545e75`)
plus `rh/problem/deep_builder.tex` (+ PDF +
`verify_deep_builder.py`, 7/7, `DEEP BUILDER VERIFIED`).
**Ausgang INFRA\_UNLOCKED / K8\_CROSS\_CONFIRMED / DEEP\_NOT\_ABD\_LIVING / SLICE\_FLOOR\_PREFERRED / FULL\_SEQUENCE\_UNSETTLED / COFINAL\_OPEN.**
Hotspot is unused Lanczos in `HS.window_data`
($k=10$ $20.57\,\mathrm{s}$ = the r443 wall), not the
chain.  Skip-Lanczos atoms are bitwise identical.
$k=8$ live confirms the r421 pin (r427 circularity
closed).  $k=10/11/12$ are not ABD-living (sign-flip /
abort).  ABD-ok slice $k=5..9$ with live $k=8$ still
prefers a floor ($\delta_{\infty}=+0.02741$,
$\Delta\mathrm{AIC}=5.11$).  Deep windows do not
decide floor vs decay.  No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444
are parallel and not dropped.

**Deep ABD adjudication (r446,
PRIME.INFRA.DEEP\_ABD\_ADJUDICATION.01).**
Sealed probe
`experiments/tfpt-discovery/deep_abd_probe.py`
(smoke 17/17, SPEC\_SHA `a48e0aa443689acd`)
plus `rh/problem/deep_abd.tex` (+ PDF +
`verify_deep_abd.py`, 7/7, `DEEP ABD VERIFIED`).
**Ausgang REAL / MESH\_DOES\_NOT\_REPAIR / LAST\_LIVE\_KZ\_136 / K12\_ETA\_UNDERFLOW / SLICE\_FLOOR\_STANDS / COFINAL\_ABD\_OPEN.**
$k=10$ first flip at $n=3788$ is bit-identical
in mpmath dps 40 and 60
($\eta=-7.938908159491412\cdot 10^{-14}$).
The r445 breaks are REAL (not float64 recurrence
artefacts).  Legal $m$-neighbours of the $2^k$
anchors are ABD-dead; last observed living window
is $k_z136$.  r397 cofinality is not ABD-cofinality.
r445 slice floor stands (no new deep $\delta$-point).
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445
are parallel and not dropped.

**Exact-atom adjudication (r447,
PRIME.INFRA.EXACT\_ATOM\_ADJUDICATION.01).**
Sealed probe
`experiments/tfpt-discovery/exact_atom_probe.py`
(smoke 14/14, SPEC\_SHA `b84310d5668a0d4c`)
plus `rh/problem/exact_atom.tex` (+ PDF +
`verify_exact_atom.py`, 7/7, `EXACT ATOM VERIFIED`).
**Ausgang EXACT\_DEAD / ATOM\_ULP\_ONLY / FLIP\_STABLE\_3788 / BAND\_ENDS / SLICE\_FLOOR\_STANDS / THIS\_FAMILY\_FREQUENTLY\_FALSIFIED.**
Exact $k=10$ atoms agree with float64 to one ulp
($\mathrm{rel}_x=4.4\cdot 10^{-16}$).  The chain
still flips at $n=3788$, bit-identical at dps 50 and 70.
float64-log is not the cause.  This $2^k$ family does
not feed the frequently-quantifier; other cofinal
families are a reviewer fork.  r445 slice floor stands.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446
are parallel and not dropped.

**Exact living band (r448,
PRIME.INFRA.EXACT\_LIVING\_BAND.01).**
Sealed probe
`experiments/tfpt-discovery/exact_band_probe.py`
(smoke 21/21, SPEC\_SHA `d5278823e99ecea3`)
plus `rh/problem/exact_band.tex` (+ PDF +
`verify_exact_band.py`, 7/7, `EXACT BAND VERIFIED`).
**Ausgang NOT\_COFINAL / COMMENSURABILITY\_REFUTED / NEXT\_ODD\_FAILS / ZETA\_CHAIN\_DEATH / LAST\_LIVE\_136\_EXACT.**
Float mesh ends at $k_z136$.  Exact $k_z230$ (generic) dies at the same $n=1818$ as float (dps 50=70).  $2^k$ commensurability is refuted.
$k_z197$ is an in-chain $\zeta$-death ($n/N=0.931$), not a dead-$\chi$ pole overshoot.
$k_z137$ dies at $n=8283$ (float was $7511$: location-lie).  Next-odd-after-$2^k$ dies at $k=10$.  r445 slice floor stands.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447
are parallel and not dropped.

**Flip versus stabilization (r449,
PRIME.INFRA.FLIP\_VS\_STABILIZATION.01).**
Sealed probe
`experiments/tfpt-discovery/flip_vs_stab_probe.py`
(smoke 14/14, SPEC\_SHA `84ba4e6a83a627b9`)
plus `rh/problem/flip_vs_stab.tex` (+ PDF +
`verify_flip_vs_stab.py`, 6/6, `FLIP VS STAB VERIFIED`).
**Ausgang TAIL\_ONLY / PREFIX\_LIVE / SLICE\_FLOOR\_STANDS / MINCUT\_IS\_PREFIX.**
Every measured chain flip sits past $n_{\mathrm{stab}}$ (Chebyshev Fenster-Vergleich, $\varepsilon$-robust).  Prefix-$80$ $q^{\dagger}$ lives ($\delta\in[0.093,0.129]$).  The r430/r434 mincut already consumes the stabilized prefix.  No anti-RH candidate.
No Lean this round.
Mincut unchanged (base 4 / refined 5).
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448
are parallel and not dropped.

**Prefix mincut (r450,
PRIME.RDAGGER.PREFIX\_MINCUT.01).**
Sealed probe
`experiments/tfpt-discovery/prefix_mincut_probe.py`
(smoke 18/18, SPEC\_SHA `a105804e98ccf8d1`)
plus `rh/problem/prefix_mincut.tex` (+ PDF +
`verify_prefix_mincut.py`, 7/7, `PREFIX MINCUT VERIFIED`).
**Ausgang M2\_UNDECIDED / PREFIX\_OBJECT\_SPLIT / NSTAB\_GROWS / CHI\_PREFIX\_LIVES / LEAN\_IDENT\_RFL.**
The $n_{\mathrm{stab}}$-compression of $R^{\dagger}$ is the frequently-cone (`Iff.rfl`).  Living full-window $\delta$ and $n_{\mathrm{stab}}$-$\delta$ are not close.  Object-pure prefix chart prefers M2; slice floor $+0.02741$ stands on its own chart.  $n_{\mathrm{stab}}\sim a^{1.27}$.  $\chi$ prefix lives (full $\chi$ stays edge-dead).  Lean census stays 5.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449
are parallel and not dropped.

**n_stab transition (r451,
PRIME.RDAGGER.NSTAB\_TRANSITION.01).**
Sealed probe
`experiments/tfpt-discovery/nstab_transition_probe.py`
(smoke 19/19, SPEC\_SHA `dcda19ffb95b515b`)
plus `rh/problem/nstab_transition.tex` (+ PDF +
`verify_nstab_transition.py`, 6/6, `NSTAB TRANSITION VERIFIED`).
**Ausgang TRANSITION\_SMOOTH / RES\_MISMATCH / PREFIX\_Q\_PLATEAU.**
No universal cliff of conditioning, atom-Nyquist, or $q^{\dagger}_n$ at $n_{\mathrm{stab}}$.  $n_{\mathrm{stab}}/n_{\mathrm{res}}\in[0.010,0.094]$ (prefix is bandlimited).  $q^{\dagger}_n$ is constant and $<1$ on $n\le n_{\mathrm{stab}}$ of every measured window.  $n_{\mathrm{stab}}$ is a sufficient operational cut, not a unique mechanical cliff.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450
are parallel and not dropped.

**Plateau theorem (r452,
PRIME.RDAGGER.PLATEAU\_THEOREM.01).**
Sealed probe
`experiments/tfpt-discovery/plateau_theorem_probe.py`
(smoke 25/25, SPEC\_SHA `63758d55e84acb27`)
plus `rh/problem/plateau_theorem.tex` (+ PDF +
`verify_plateau_theorem.py`, 6/6, `PLATEAU THEOREM VERIFIED`).
**Ausgang PLATEAU\_IDENTITY\_PROVED / QSTAR\_UNDECIDED.**
Grade-0 SATZ $q_*=M_\partial/(M_\partial+5/7)$ on every window with $M_\partial=\tilde\mu_0-\tilde\nu_0$ (kz$\ge 69$, residual $<5\cdot10^{-5}$).  A(ii) value law refuted by the sister pair.  Constancy is $\rho_n=0$.  Whether $M_\partial$ is unbounded stays open.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451
are parallel and not dropped.

**Border mass (r453,
PRIME.RDAGGER.BORDER\_MASS\_INEQUALITY.01).**
Sealed probe
`experiments/tfpt-discovery/border_mass_probe.py`
(smoke 23/23, SPEC\_SHA `4378e2a6e5d0e76e`)
plus `rh/problem/border_mass.tex` (+ PDF +
`verify_border_mass.py`, 6/6, `BORDER MASS VERIFIED`).
**Ausgang BOUND\_PROVED / MASS\_CLASSICAL\_REDUCED\_GROWING / RACE\_WON.**
Exact pack identity $q_n=S_{n-1}/B_w$, $\delta=(5/7-\rho_n)/B_w$; first-leak $g=\rho_n/B_w$.  $M_\partial$ is folded $m_0$, grows with $\log N$.  At fixed $n\in\{20,40,80,160\}$ $\mathrm{err}\ll$ margin.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452
are parallel and not dropped.

**Limit object (r454,
PRIME.RDAGGER.LIMIT\_OBJECT.01).**
Sealed probe
`experiments/tfpt-discovery/limit_object_probe.py`
(smoke 20/20, SPEC\_SHA `1f4abe0f66e470e6`)
plus `rh/problem/limit_object.tex` (+ PDF +
`verify_limit_object.py`, 6/6, `LIMIT OBJECT VERIFIED`).
**Ausgang LIMIT\_CLASSICAL / LIMITCHAIN\_ALIVE\_200 / CHAIN\_DOCUMENTED.**
For $j\ge 2$, $m_\infty=m_{\mathrm{ARCH}}$ (comb in the rate, not the limit).  $\rho_j(\infty)=0\pm 10^{-4}$ through $j=200$.  [L1] MEASURED, [L2] MEASURED, [L3] MEASURED($j\le 200$)/OPEN.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453
are parallel and not dropped.

**ARCH chain (r455,
PRIME.RDAGGER.ARCH\_CHAIN\_THEOREM.01).**
Sealed probe
`experiments/tfpt-discovery/arch_chain_probe.py`
(smoke 20/20, SPEC\_SHA `8f353fbb11d03d43`)
plus `rh/problem/arch_chain.tex` (+ PDF +
`verify_arch_chain.py`, 6/6, `ARCH CHAIN VERIFIED`).
**Ausgang L3\_PROVED / L1\_PNT\_SUFFICIENT / CHAIN\_MAPPED.**
[L1] elementary (3-lag + $\Lambda(n)=0$ for $n<2$); not RH-circular.  [L3] $h>0$ classical, $\rho_n=0$ on $1..J_B-1$, $J_B=\mathtt{BG\_DU}/\Delta$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454
are parallel and not dropped.

**Prefix vacuity (r456,
PRIME.RDAGGER.VACUITY\_REDTEAM.01).**
Sealed probe
`experiments/tfpt-discovery/vacuity_redteam_probe.py`
(smoke 26/26, full 31/31, SPEC\_SHA `bbb203039bf73e98`)
plus `rh/problem/vacuity_redteam.tex` (+ PDF +
`verify_vacuity_redteam.py`, 6/6, `VACUITY REDTEAM VERIFIED`).
**Ausgang VACUOUS\_CONFIRMED.**
The r450 `Iff.rfl` is a naming of the full-cap cone, not an $n_{\mathrm{stab}}$-truncation.  Worlds test (MAIN vs ARCH-only, identical fold): prefix $q^{\dagger}$ is prime-blind (kz$69$ $n_{\mathrm{stab}}$ $\Delta q=3.33\cdot10^{-16}$); arithmetic onset at $J_P$ and in `combRead`.  r449--r455 retyped as anatomy of the prime-blind zone.  No Lean sorry.  Census stays 5.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455
are parallel and not dropped.

**$J_P$ increment (r457,
PRIME.RDAGGER.JP\_INCREMENT.01).**
Sealed probe
`experiments/tfpt-discovery/jp_increment_probe.py`
(smoke 13/13, SPEC\_SHA `344995a565d5b94a`)
plus `rh/problem/jp_increment.tex` (+ PDF +
`verify_jp_increment.py`, 6/6, `JP INCREMENT VERIFIED`).
**Ausgang INCREMENT\_DRIFT / RACE\_EATS\_K10 / LEMMA\_REDUCED.**
Accepts r456.  Prime increment from $J_P$ drifts (no rho-cancellation).  Race eats the $k=10$ margin.  Reduction is r453 at cap; not r429.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456
are parallel and not dropped.

**Cofinal family (r458,
PRIME.RDAGGER.COFINAL\_FAMILY.01).**
Sealed probe
`experiments/tfpt-discovery/cofinal_family_probe.py`
(smoke 13/13, SPEC\_SHA `a4aa21a54f33eace`)
plus `rh/problem/cofinal_family.tex` (+ PDF +
`verify_cofinal_family.py`, 6/6, `COFINAL FAMILY VERIFIED`).
**Ausgang FAMILY\_CANDIDATE / TABLE\_CAP\_ARTEFACT / RESIDUAL\_DEEP\_DEATH.**
Lean selected $(a_k,m_k)$ lives at the cap through $k=16$; $k=10$ is stable under the full $a^2$ comb.  The capped frame-A $a=631/641$ wall is $\sqrt{\mathrm{TABLE\_CAP}}$.  Completing the comb revives $k_z197$ and exact $k_z230$; $k_z137$ ($N=8300$) stays dead.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457
are parallel and not dropped.

**Full-comb cleanup (r459,
PRIME.RDAGGER.FULLCOMB\_CLEANUP.01).**
Sealed probe
`experiments/tfpt-discovery/fullcomb_cleanup_probe.py`
(smoke 18/18, SPEC\_SHA `a34f8d17d767d4d1`)
plus `rh/problem/fullcomb_cleanup.tex` (+ PDF +
`verify_fullcomb_cleanup.py`, 7/7, `FULLCOMB CLEANUP VERIFIED`).
**Ausgang RACE\_TREND\_BROKEN / LEANFAM\_EXACT\_ALIVE(12) / KZ137\_OUTSIDE\_MINCUT.**
r457 RACE\_EATS\_K10 was a TABLE\_CAP echo: completed races stay below 1 and the monotone climb breaks after $k_z136$.  Lean selectedMesh race stays in $0.61$--$0.76$ through exact $k=12$.  $k_z137$ dies on frame-A with a complete comb; the Lean window at $a=641$ lives.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457 / r458
are parallel and not dropped.

**Selected race proof attempt (r460,
PRIME.RDAGGER.RACE\_PROOF\_ATTEMPT.01).**
Sealed probe
`experiments/tfpt-discovery/race_proof_probe.py`
(smoke 28/28, full 29/29, SPEC\_SHA `58dd22a425266c7b`)
plus `rh/problem/race_proof.tex` (+ PDF +
`verify_race_proof.py`, 10/10,
`RACE PROOF ATTEMPT VERIFIED -- OUTCOME PARTIAL`).
**Ausgang PARTIAL: SPECTRAL\_REDUCTION\_PROVED /
NORM\_ROUTE\_REFUTED / PLATEAU\_ROUTE\_FINITE /
SPECTRAL\_OVERLAP\_OPEN.**
The exact spectral race identity and a two-band sufficient criterion
are proved; the latter certifies only $k=5$.  Raw norm and Gershgorin
fail on every complete $k=5..12$ row, and each fixed-$r$ plateau has
only $2r+1$ members.  The exact remaining gap is a source-derived
bound on the normalized border vector's spectral measure near
$\lambda=1$ for infinitely many selected $k$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457 / r458 / r459
are parallel and not dropped.

**Narrow-band Weil audit (r461,
PRIME.RDAGGER.NARROWBAND\_WEIL.01).**
Sealed probe
`experiments/tfpt-discovery/narrowband_weil_probe.py`
(smoke/full 21/21, SPEC\_SHA `5bf44fd807bb5a0c`)
plus `rh/problem/narrowband_weil.tex` (+ PDF +
`verify_narrowband_weil.py`, 9/9, `NARROWBAND WEIL VERIFIED`).
**Ausgang FORK\_SHARPENED.**
The Lean endpoint is GridElement Weil-form positivity, not RH:
the spectral/zero side and density completion are absent, while the
path consumes the arch stabilization `sorryAx` and a named
$A_{\rm cap}$-to-`fullRead` bridge.  In the r459 builder
$U_k=N_k\Delta_k=k\log2/2=1.732868..4.158883$ for $k=5..12$,
so every measured window lies beyond both the classical
$U<\log2$ range and the recent $U\le1.6$ certificate.
The completed mincut would be cofinal compact-window Weil positivity,
hence the full Weil criterion after the missing dictionary.
No Lean edit this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457 / r458 / r459 / r460
are parallel and not dropped.

**Octave renormalization (r468,
PRIME.RDAGGER.OCTAVE\_RENORMALIZATION.01).**
Sealed probe
`experiments/tfpt-discovery/octave_renorm_probe.py`
(smoke 24/24, SPEC\_SHA `0e693815a86ef0ff`)
plus `rh/problem/octave_renorm.tex` (+ PDF +
`verify_octave_renorm.py`, 7/7, `OCTAVE RENORM VERIFIED`).
**Ausgang OCTAVE\_NOT\_CAUCHY / EDGE\_TWO\_POINTS / REDUCTION\_ALIAS.**
The live increment is $n<a$, not the $a^2$-octave.  Intra-block $\Delta q$ oscillates; the octave-weight bound grows.  $9\to10$ is intra $r=3$.  Two $\Delta$-halving edges ($+0.045$, $+0.018$) are not a law.  The proposed block-limit cut is an alias of the original quantifier.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457 / r458 / r459 / r460 / r461
are parallel and not dropped.

**Correlation wall judgment (r469,
PRIME.RDAGGER.CORRELATION\_WALL\_JUDGMENT.01).**
Adjudication note `rh/problem/correlation_wall_judgment.tex` (+ PDF).
No probe, no new census, no Lean edit (the judge was forbidden to
write status lines).  **Ausgang U1 INTERNALLY\_EXHAUSTED / U2
EXTEND\_AND\_REFRAME / U3 REDIRECT\_TO\_FIXED\_L.**
The residual cofinal object is, after the named bridges, the full
Weil criterion.  Resources move to an unconditional classical theorem
at fixed support length (F1: channel representation, digamma/Mellin
identity, fixed-$L$ density).  Binding anti-list; no infinitely-many-$k$
restatement.  Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Quadratic representation obstruction (r470,
PRIME.RDAGGER.QUADREP.01).**
Sealed probe
`experiments/tfpt-discovery/quadrep_probe.py`
(smoke 10/10, SPEC\_SHA `74de4e263ac7fd7b`)
plus `rh/problem/quadrep.tex` (+ PDF +
`verify_quadrep.py`, 6/6, `QUADREP VERIFIED`).
**Ausgang OBSTRUCTION\_SEALED.**
F1(i) of the r469 U3 contract.  `SelectedReadQuadraticRepresentation`
is retained unweakened.  Lean proves the $k=5$ steps/cap mismatch
(`exists_mesh_compatible_steps_gt_cap`) and the finite implication
that a negative mesh-compatible read on a PSD cap refutes the
channel.  The named obstruction
`SelectedOnsetCompatibleNegativeRead` is sealed at $k=5$: an
onset-compatible native Hessian is indefinite of rank $24>\mathrm{cap}+1=11$
while $A_{\mathrm{cap}}$ is PD.  Sorry census stays **8**.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.
Coexistence: r434 / r435 / r436 / r438 / r440 / r441 / r442 / r443 / r444 / r445 / r446 / r447 / r448 / r449 / r450 / r451 / r452 / r453 / r454 / r455 / r456 / r457 / r458 / r459 / r460 / r461 / r468 / r469
are parallel and not dropped.

**Classical grid certificates (r471,
PRIME.RDAGGER.CLASSICAL\_CERT.01).**
Sealed probe
`experiments/tfpt-discovery/classical_cert_probe.py`
(smoke 14/14, full 25/25, SPEC\_SHA `18eb2a33651585f5`)
plus `rh/problem/classical_cert.tex` (+ PDF +
`verify_classical_cert.py`, 6/6, `CLASSICAL CERT VERIFIED -- GRID_CERTIFIED(L_max=2.7726)`).
**Ausgang GRID\_CERTIFIED($L_{\max}=2.7726$).**
Dictionary-free Guinand--Weil form $Q=A-P+\Pi$ on piecewise-constant $h$ supported in $[-L,L]$.  Calibration $L=0.8$ green; then $L_5$ through $L_{16}$.  Type is never $\lambda_*(L)\ge 0$; the discretization gap is named F2b.  Scramble-sensitive (literal $\log n$).  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Modulus upgrade (r474,
PRIME.RDAGGER.MODULUS\_UPGRADE.01).**
Sealed probe
`experiments/tfpt-discovery/modulus_upgrade_probe.py`
(smoke 11/11, full 21/21, SPEC\_SHA `45db1c92384913e8`)
plus `rh/problem/modulus_upgrade.tex` (+ PDF +
`verify_modulus_upgrade.py`, 6/6, `MODULUS UPGRADE VERIFIED -- PARTIAL`).
**Ausgang PARTIAL.**
F2b lemmas proved ($C_P=2S_{\mathrm{eff}}$, $C_\Pi=8\sinh L$, Jackson $1/\pi^2$).  Every sealed mesh is SHORT, including YB $L=0.3$ (modulus too crude).  No $\lambda_*(L)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Extraction-joint redesign (r473,
PRIME.RDAGGER.EXTRACTION\_JOINT\_REDESIGN.01).**
Sealed probe
`experiments/tfpt-discovery/extraction_joint_probe.py`
(smoke 13/13, SPEC\_SHA `0650125bd812c1f8`)
plus `rh/problem/extraction_joint.tex` (+ PDF +
`verify_extraction_joint.py`, 6/6, `EXTRACTION JOINT VERIFIED`).
**Ausgang ARTEFACT + POLY\_BRIDGE\_PROVED.**
At the r470 $k=5$ witness, classical $Q(g_f)=+0.0769078530458283$
while $\mathrm{fullRead}=-0.0428854252772195$; the gap is the arch
tent error $0.1197932783230478$ ($\hat g\ge0$).  Lean proves
`selectedACapPsdImpliesPolynomialReads` and
`fullRead_weilForm_gap_eq_arch`.  Named outer bridge
`SelectedPolynomialApproximatesGrid`.  Redesigned joint
`FrequentlySelectedPolynomialJoint` with fixed-$k$ readout
$\mathrm{weilForm}\ge-2\,\mathrm{err}_{\mathrm{arch}}$.
Sorry census stays **8**.  No infinitely-many-$k$ statement.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Arch identity and tent rate (r475,
PRIME.RDAGGER.ARCH\_IDENTITY\_AND\_RATE.01).**
Sealed probe
`experiments/tfpt-discovery/arch_rate_probe.py`
(smoke 9/9, SPEC\_SHA `e8a49c5895d3d382`)
plus `rh/problem/arch_rate.tex` (+ PDF +
`verify_arch_rate.py`, 6/6, `ARCH RATE VERIFIED`).
**Ausgang IDENTITY\_ISOLATED + RATE\_O\_DELTA2
(numeric large-support) + FIXED\_CONSTANT\_FALSIFIED
(r475-repair).**
F1(ii) not closed as exact equality (`Delta -> +infty` at fixed
mesh, proved; Mathlib Gauss TODO isolated as a named Prop).
`weilArchSide` is the concrete $u$-space pairing.  $O(\Delta_k^2)$
rate numerically supported (ratios $3.85$--$3.99$); fixed-constant
Prop FALSIFIED ($8.0283458222>4.1259765625$, small-support regime,
kink defect $-\theta(1-\theta)/2$ proved).  The $\exists C$ interface
`SelectedArchErrorQuadraticRateExists` is proved CONDITIONALLY on the
still-open `SelectedArchWeightedInterpolationEstimate` (theorem
`selectedArchErrorQuadraticRateExists_of_weightedInterpolationEstimate`);
the downstream convergence
`selectedArchError_tendsto_zero_of_rateExists` is proved
unconditionally from the $\exists C$ form
(`RH/SelectedArchErrorQuadraticRateClassical.lean`).  Witness:
$0.119793278323$ at $k=5$ ($\mathrm{err}/\Delta^2=3.9893$) and
$0.028876619985$ at $k=9$ ($3.8466$).  Sorry census stays **5**.
No infinitely-many-$k$ positivity.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Crossterm sharpening (r476,
PRIME.RDAGGER.CROSSTERM\_SHARPENING.01).**
Sealed probe
`experiments/tfpt-discovery/crossterm_probe.py`
(smoke 15/15, full 25/25, SPEC\_SHA `a123650e757b912d`)
plus `rh/problem/crossterm.tex` (+ PDF +
`verify_crossterm.py`, 6/6, `CROSSTERM VERIFIED -- UNCONDITIONAL(L_max=2.7726)`).
**Ausgang UNCONDITIONAL($L_{\max}=2.7726$) on the first Dirichlet $H^2$ ball.**
YB gate PASS ($r\in[1.163\cdot10^{-2},1.180\cdot10^{-2}]$, $P=0$).  All 12 schedule points H2BALL\_POS through $L_{16}$.  Not $\lambda_*(L)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**High-mode dominance (r477,
PRIME.RDAGGER.HIGHMODE\_DOMINANCE.01).**
Sealed probe
`experiments/tfpt-discovery/highmode_probe.py`
(smoke 18/18, full 28/28, SPEC\_SHA `57fd2de61c6fdcc9`)
plus `rh/problem/highmode.tex` (+ PDF +
`verify_highmode.py`, 6/6, `HIGHMODE VERIFIED -- ARCHITECTURE_STANDS(0.3,0.8,1.0)`).
**Regime ARCHITECTURE\_STANDS at $L=0.3,0.8,1.0$.**
Symbol identity sealed; $t_0=22/4300/2.44\cdot10^5$; crude Schur bound fails; direct $2\times2$ PD.  YB gate PASS.  Not $\lambda_*(L)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**End-to-end fixed-$L$ (r478,
PRIME.RDAGGER.ENDTOEND\_FIXEDL.01).**
Sealed probe
`experiments/tfpt-discovery/endtoend_fixedl_probe.py`
(smoke 17/17, full 27/27, SPEC\_SHA `138cbf9410486418`)
plus `rh/problem/endtoend_fixedl.tex` (+ PDF +
`verify_endtoend_fixedl.py`, 6/6, `ENDTOEND_FIXEDL VERIFIED -- PARTIAL(0.3-even-5x5-PD|tail-Schur)`).
**Regime PARTIAL: even Fourier $N=2..5$ PD at $L=0.3$; tail Schur OPEN.**
Not $\lambda_*(0.3)\ge0$.  $L=0.8$ Fourier $3\times3$ indefinite; $K_P$ gain $\le1.010$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Lambda-star $0.3$ keystone (r479,
PRIME.RDAGGER.LAMBDASTAR\_03\_KEYSTONE.01).**
Sealed probe
`experiments/tfpt-discovery/lambdastar03_probe.py`
(smoke 10/10, full 22/22, SPEC\_SHA `7a234db34c2ec6f0`)
plus `rh/problem/lambdastar03.tex` (+ PDF +
`verify_lambdastar03.py`, 6/6, `LAMBDASTAR03 VERIFIED -- REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)`).
**Regime REDUCED: $t_c$ and trace sealed; minorant+$\Pi$ indefinite; high-band coupling OPEN.**
Not $\lambda_*(0.3)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Kappa-high remainder (r480,
PRIME.RDAGGER.KAPPA\_HIGH.01).**
Sealed probe
`experiments/tfpt-discovery/kappa_high_probe.py`
(smoke 14/14, full 23/23, SPEC\_SHA `7be2cb1dcc994ba6`)
plus `rh/problem/kappa_high.tex` (+ PDF +
`verify_kappa_high.py`, 6/6, `KAPPA_HIGH VERIFIED -- REDUCED(refined-Schur; crude-kappa_high-killed@0.30)`).
**Regime REDUCED: crude $\kappa_{\mathrm{high}}\le1.79\cdot10^{-2}$ KILL ($\approx0.291$); refined even Schur numeric PD, interval OPEN.**
Not $\lambda_*(0.3)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Schur certificate (r481,
PRIME.RDAGGER.SCHUR\_CERTIFICATE.01).**
Sealed probe
`experiments/tfpt-discovery/schur_cert_probe.py`
(smoke 14/14, full 21/21, SPEC\_SHA `c81a0b2490cfb475`)
plus `rh/problem/schur_cert.tex` (+ PDF +
`verify_schur_cert.py`, 6/6, `SCHUR_CERT VERIFIED -- REDUCED(interval-FT+IBP-tail)`).
**Regime REDUCED: $\varepsilon$ lifts; interval FT + IBP tail OPEN.**
Not $\lambda_*(0.3)\ge0$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Carleson edgeband (r482,
PRIME.RDAGGER.CARLESON\_EDGEBAND.01).**
Sealed probe
`experiments/tfpt-discovery/carleson_edgeband_probe.py`
(smoke 15/15, full 29/29, SPEC\_SHA `c007a877653449ee`)
plus `rh/problem/carleson_edgeband.tex` (+ PDF +
`verify_carleson_edgeband.py`, `VERIFIED carleson_edgeband -- STUCK(SR_FAILS_FINITE_CENSUS;RESTRICTED_LARGE_SIEVE_IS_TARGET;STRICT_F_SCRAMBLE_PREMISE_FALSE)`).
**Regime STUCK: SR fails the finite census; restricted large sieve is TARGET; strict-$F$ scramble premise false.**
Not a Carleson law, not $\lambda_*$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Filon enclosure (r483,
PRIME.RDAGGER.FILON\_ENCLOSURE.01).**
Sealed probe
`experiments/tfpt-discovery/filon_enclosure_probe.py`
(smoke 17/17, full 27/27, SPEC\_SHA `54613b4a2a038342`)
plus `rh/problem/filon_enclosure.tex` (+ PDF +
`verify_filon_enclosure.py`, 6/6, `FILON_ENCLOSURE VERIFIED -- REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)`).
**Regime REDUCED: finite $S$ interval-PD; leftover $C$ HS $2.74\cdot10^{-2}$ vs budget $2.4\cdot10^{-4}$.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Block completion (r484,
PRIME.RDAGGER.BLOCK\_COMPLETION.01).**
Sealed probe
`experiments/tfpt-discovery/block_completion_probe.py`
(smoke 12/12, full 24/24, SPEC\_SHA `cd69a3e49978cf55`)
plus `rh/problem/block_completion.tex` (+ PDF +
`verify_block_completion.py`, 6/6, `BLOCK_COMPLETION VERIFIED -- STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)`).
**Regime STUCK: $20\times$ drop falsified at $n=96$; jets $\ge\psi_{10}$ garbage at $n=128$; QR--IBP kills $S$.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Weighted Schur (r485,
PRIME.RDAGGER.WEIGHTED\_SCHUR.01).**
Sealed probe
`experiments/tfpt-discovery/weighted_schur_probe.py`
(smoke 15/15, full 21/21, SPEC\_SHA `1d61f8c270a38c6a`)
plus `rh/problem/weighted_schur.tex` (+ PDF +
`verify_weighted_schur.py`, 6/6, `WEIGHTED_SCHUR VERIFIED -- REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT`).
**Regime REDUCED+CHECKPOINT: $A$-GO (hi-frac $0.991$); finite $S_w$ interval-PD; operator $M_\infty$ on the true complement open.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Woodbury / Birman--Schwinger (r486,
PRIME.RDAGGER.WOODBURY\_MINF.01).**
Sealed probe
`experiments/tfpt-discovery/woodbury_minf_probe.py`
(smoke 16/16, full 23/23, SPEC\_SHA `7f306746b2a2b517`)
plus `rh/problem/woodbury_minf.tex` (+ PDF +
`verify_woodbury_minf.py`, 6/6, `WOODBURY_MINF VERIFIED -- REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)`).
**Regime REDUCED: enemy $A^-$ is 3 certified modes; finite BS $<1$; operator $R^{-1}$ open.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Outer bridges lane start (r487,
PRIME.RDAGGER.OUTER\_BRIDGES.01).**
Structural probe
`experiments/tfpt-discovery/outer_bridges_probe.py`
(smoke 12/12, SPEC\_SHA `5ea36777bc6077e6`) plus
`rh/problem/outer_bridges.tex` (+ PDF +
`verify_outer_bridges.py`, 6/6, `OUTER BRIDGES VERIFIED`).
**Regime OUTER\_LANE\_TYPED / DENSE\_LIMIT\_REDUCED /
ZETA\_INTERFACE\_PROVED.**  The fixed-support autocorrelation class
and channel limits are typed; the positivity-limit and literal
Mathlib zeta wrappers are proved.  Four external bricks remain.
Sorry census **8 → 9** because density was split honestly in two.
Experiments-side seal, NO ledger row, NO L\* claim, NO RH CLAIM.


**Resolvent solve (r488,
PRIME.RDAGGER.RESOLVENT\_SOLVE.01).**
Sealed probe
`experiments/tfpt-discovery/resolvent_solve_probe.py`
(smoke 12/12, full 18/18, SPEC\_SHA `2ce1bae7228fb033`)
plus `rh/problem/resolvent_solve.tex` (+ PDF +
`verify_resolvent_solve.py`, 6/6, `RESOLVENT_SOLVE VERIFIED -- REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; operator-R-gap-open)`).
**Regime REDUCED: $R$ not coercive; shift $s=0.05$ $G$-certificate $N=5$ BS $0.994$; operator $R$-gap open.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Outer bridges II (r489,
PRIME.RDAGGER.OUTER\_BRIDGES.02).**
Structural probe `experiments/tfpt-discovery/outer_bridges2_probe.py`
(smoke 12/12, SPEC\_SHA `9952567c0a594287`) plus
`rh/problem/outer_bridges2.tex` (+ PDF +
`verify_outer_bridges2.py`, 6/6, `OUTER BRIDGES 2 VERIFIED`).
**Regime COMB\_CLOSED / POLAR\_INTEGRAL\_CLOSED /
DENSE\_COMPLETION\_ONE\_SORRY.**  The topology is uniform on a
common fixed support plus L1; the witness is compactly supported in
L2.  Common-anchor finite-comb and bounded-cosh polar-integral
continuity are proved.  Census **9 → 8**.  Experiments-side structural
seal, NO ledger row, NO L\* claim, NO RH CLAIM.

**Operator residual (r490,
PRIME.RDAGGER.OPERATOR\_RESIDUAL.01).**
Sealed probe
`experiments/tfpt-discovery/operator_residual_probe.py`
(smoke 11/11, full 16/16, SPEC\_SHA `162707324dc6b05c`)
plus `rh/problem/operator_residual.tex` (+ PDF +
`verify_operator_residual.py`, 6/6,
`OPERATOR\_RESIDUAL VERIFIED -- STUCK(off/s=5.86-eats-1000x; GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)`).
**Regime STUCK+FINAL\_CHECKPOINT: certificate
off/s $=5.86$ eats the $5.6\cdot10^{-3}$ margin
$\sim1000\times$; GL leftover of truncated $A^+$
is tiny at $n\ge96$ but is not the certificate
residual.**
Not $\lambda_*(0.3)\ge c$.  No Lean this round.
The $0.3$ keystone is frozen.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.


**Outer bridges III (r491,
PRIME.RDAGGER.OUTER\_BRIDGES.03).**
Structural probe `experiments/tfpt-discovery/outer_bridges3_probe.py`
(smoke 12/12, SPEC\_SHA `baaafe714f54eb07`) plus
`rh/problem/outer_bridges3.tex` (+ PDF +
`verify_outer_bridges3.py`, 7/7,
`OUTER BRIDGES 3 VERIFIED -- REDUCED`).
**Verdict HIDDEN\_GAP\_FOUND / DENSITY\_BRIDGE\_REDUCED.**
The r489 completion has three components, not two.  r491 corrects the
polar sign to `+2 cosh`, makes the full arch functional concrete, and
constructs the support-fitting sampled dyadic GridElement sequence.
Its support bound and the implication from hat identity to pole
sequence continuity are proved.  Census **8 → 8**.  NO RH CLAIM.

**Keystone judgment (r492,
PRIME.RDAGGER.KEYSTONE\_JUDGMENT.01).**
Adjudication note `rh/problem/keystone_judgment.tex` (+ PDF).
No probe, no verifier, no census, no sealed pin.
**Verdict U1 IDEA\_NAMED(kernel-Loewner) / U2 PROCEED\_UNDER\_BUDGET /
U3 REDIRECT\_TO\_KERNEL\_LANE.**
Four of the five proposed candidates die, three of them structurally
(the smooth $t$-cutoff misdiagnoses the $1/t$ tails, which are forced
by the compact time support; the Fredholm trace-power route lies in no
Schatten class with the shift and has no explicit kernels without it;
the smoothing preconditioner is incompatible with
$\operatorname{supp}\subset[-L,L]$).
The named idea is the classical $x$-space Weil kernel form with
$k(x)=e^{x/2}/\sinh x$, together with $I-\operatorname{Re}\tau_x\succeq0$:
every truncation of the $x$-integral is Loewner-safe, so the r483--r490
off-space obstruction has no analogue there.
Calibrated against three sealed numbers (`sigma_A(0)`, the r476
Dirichlet hull, the odd sector); closing budget measured.
Free diagnosis: the r488/r490 premise ``$R$ not coercive'' is false
($R\succeq1.568\cdot10^{-2}I$); no verdict is regressed.
The frequency-side $0.3$ lane is closed permanently; twenty kills are
consolidated into six families.
Experiments-side, NO ledger row, NO L\* claim, NO RH CLAIM.

**Kernel--Loewner operator certificate (r494,
PRIME.RDAGGER.KERNEL\_LOEWNER.01).**
Sealed probe `experiments/tfpt-discovery/kernel_loewner_probe.py`
(smoke/full 17/17, SPEC\_SHA `2e6d71138dff4540`) plus
`rh/problem/kernel_loewner.tex` (+ PDF +
`verify_kernel_loewner.py`, 6/6,
`KERNEL LOEWNER VERIFIED -- PROVED(c=2.1000e-3)`).
**Verdict PROVED(c=2.1000e-3).**
At $L=0.3$, all three identity calibrations pass; the
zero-extension proof retains both translation boundary strips; the
quintic $C^2$ cutoff has
$\kappa_w=3.698008040298977$ with the omitted prefix booked.
The $n=401$ Legendre certificate encloses the exact HS rest by
$7.0457565325\cdot10^{-4}<\text{margin}/3$ and charges it three
times, including both off-block terms.  The resulting operator floor
is $2.1220149285\cdot10^{-3}$, sealed at $c=2.1\cdot10^{-3}$.
Galerkin values remain upper-bound diagnostics.  Promoted
2026-09-01 as `v1017` / `PRIME.RDAGGER.KERNEL_LOEWNER.01`
**[Numerical/certified]**, not [E] (float64 floor, no
interval arithmetic).  NO L\* claim, NO RH CLAIM.


**Adversarial kernel--Loewner red team (r495,
PRIME.RDAGGER.KERNEL\_LOEWNER\_REDTEAM.01).**
Independent probe `experiments/tfpt-discovery/kernel_redteam_probe.py`
(smoke/full 11/11, SPEC\_SHA `431251a9bcfd40a1`) plus
`rh/problem/kernel_redteam.tex` (+ PDF +
`verify_kernel_redteam.py`, 6/6,
`KERNEL REDTEAM VERIFIED -- CONFIRMED(c=2.1000e-3)`).
**Verdict CONFIRMED(c=2.1000e-3).**
Five non-calibration digamma/$x$-space tests agree to
$5.736\cdot10^{-21}$; six rational step/shift tests retain positive
boundary-strip masses exactly.  A doubled-$c_L$ false world is
negative (Rayleigh $-1.924951$, chain $-2.188168$).
Independent Clenshaw--Curtis order 1025 gives
$\lambda_{\max}=1.501365808845941$ and
$r_{401}=6.7948687\cdot10^{-4}$.  The nonzero complementary
block-diagonal rest $6.2971739\cdot10^{-4}$ is explicitly included.
The outward floor is $2.12201489025\cdot10^{-3}$.
Fixed-support audit only; NO ledger row, NO L\* claim, NO RH CLAIM.


**Kernel--Loewner scaling test at $L=0.8$ (r496,
PRIME.RDAGGER.KERNEL\_LOEWNER.02).**
Sealed probe `experiments/tfpt-discovery/kernel_loewner08_probe.py`
(smoke/full 15/15, SPEC\_SHA `63f590d43c9ed63e`) plus
`rh/problem/kernel_loewner08.tex` (+ PDF +
`verify_kernel_loewner08.py`,
`VERIFIED kernel_loewner08 r496 NO_GO`).
**Verdict NO\_GO(kernel-Loewner-compact-tail@L=0.8).**
G1 passes ($c_L=3.5598735700355446$, factor-two prime $g(0)$ mass
$2\sum\Lambda(n)/\sqrt n=2.9419735252236205$, five dps-50 tests within
$5.499\cdot10^{-14}$).  G2 and G3 give a method no-go: the best booked
cutoff $[0.001,0.003]$ has $n=101$ section
$\lambda_{\min}=-1.610673\cdot10^{-4}$, the full $3\times$HS charge is
$27.367230540$, and the bounded prime translations are noncompact
(measured off-block $0.939496613$).
Method no-go only, no anti-positivity theorem; NO ledger row,
NO L\* claim, NO RH CLAIM.


**The $0.8$ rung judgment (r502,
PRIME.RDAGGER.L08\_JUDGMENT.01).**
Adjudication note `rh/problem/l08_judgment.tex` (+ PDF).
No probe, no verifier, no census, no sealed pin.
**Verdict U1 BLOCKED(no-certifiable-gap@$L\ge0.45$) /
U2 LADDER\_RESTS\_REDIRECT\_TO\_BRIDGE\_LANE /
U3 ANTI\_LIST\_EXTENDED.**
The r496 no-go is reproduced from an independent implementation (all
four cutoff rows, all four $\kappa_w$, $\|T_w\|_{\rm HS}=19.2177$,
$r_{101}=9.12241$), which also identifies its booking as the one that
retains the prime translations as operators.
Both r496 obstructions are then found to be mis-specified: an explicit
odd Legendre degree-13 witness gives
$\lambda_*(0.8)\le1.8170\cdot10^{-14}$, evaluated at `dps=30` in the
$x$-space form as $1.81691694981\cdot10^{-14}$ and bracketed from below
by the nonnegative spectral side of the explicit formula over the first
$60$ zeta zeros ($1.442289883\cdot10^{-14}$, $79\%$), with the
$\gamma_1$ term at $1.061\cdot10^{-26}$.  The r496 margins are ten
orders of magnitude above that target.  Measured ceiling ladder
$7.57\cdot10^{-3}$, $1.33\cdot10^{-3}$, $1.81\cdot10^{-4}$,
$1.62\cdot10^{-5}$, $9.34\cdot10^{-7}$, $1.61\cdot10^{-9}$,
$4.87\cdot10^{-13}$ at $L=0.30,0.34657,0.40,0.45,0.50,0.60,0.70$, with
the archimedean floor falling to $-0.92648$ at $L=0.8$: three-channel
cancellation to $13.6$ digits.  Four candidate refinements are
calibrated against these numbers and all four die.
$\lambda_*$-ladder closed as a proof route beyond the prime-free zone;
r494/r495 stand; resources to the bridge lane; new anti-list family
F-VII with N5--N10.
The ceiling is an **upper** bound on a quantity RH predicts to be
nonnegative, and both representations return a positive value: NO
counterexample, NO anti-positivity statement.
NO ledger row, NO L\* claim, NO RH CLAIM, NO anti-RH claim.


**Outer bridges r517–r532 (Lean-only campaign).**
No sealed probe, no ledger row, no status upgrade.
Sixteen sorry-free Lean rounds on
`RH/ExternalBridges.lean` (commits `4bf75f4f`–
`7fb2dbb0`): CONTOUR\_IDENTITY, GAP\_WIRED, BC\_WIRED,
LANDAU\_SUM\_WIRED, LANDAU\_WIRED, CONTOUR\_RESTATED,
WINDOW+PSI, LANDAU\_A, PSI\_OPEN, PSI\_ANCHORED,
SLIVER\_WIRED, HORIZONTALS\_CLOSED, LEFT\_EDGE,
LIMIT\_IDENTITY (`contourIdentityLimitAlongGaps` —
full spectral side of the explicit formula),
HAT\_INVERSION (`hat_fourier_inversion`;
`standardExplicitFormula` concretely the spectral
pairing), RIGHT\_PRIME
(`rightVerticalIntegral_eq_prime_sum`; $2\Lambda/\sqrt{n}$
gauge pinned, unresolved).  Named bridges now theorems:
`fullWeil_dyadic_sample_convergence`,
`gridPoleHatIntegralIdentity`,
`fullWeil_channel_continuity`.  Still OPEN:
`standard_explicit_formula_identification`,
`fullWeil_separates_offCritical_zeros`.  Sorry census
**stays 7** (external 2).  NO RH CLAIM.

**Outer bridges r534 (Lean-only, outer-bridges round 41).**
No sealed probe, no probe row (gap like r517–r532), no
ledger row.  Sorry-free in `RH/ExternalBridges.lean`:
`contourExplicitFormula_honest` and
`contourExplicitFormula_honest_complex`,
`leftEdgeArchIntegral_eq_explicit_factor_integral`,
`honest_contour_explicit_formula_identification`
(theorem `HonestContourExplicitFormulaIdentification`).
Bridge-2 contour half **PROVED** in the honest form
(weights $\Lambda(n)(1+n^{-1})$).  Corpus identification
`standard_explicit_formula_identification` stays honestly
**[O]** / BLOCKED (corpus $2\Lambda/\sqrt{n}$ vs contour
$\Lambda(1+n^{-1})$).  Lake green 3545 jobs, census
**stays 7**.  NO RH CLAIM.

**Weil-separation red team (r535,
PRIME.RDAGGER.WEIL\_SEPARATION\_REDTEAM.01).**
Sealed probe `experiments/tfpt-discovery/weil_separation_redteam_probe.py`
(sha256 `5f93716a824badebce7c5efcbe2b6523fb785668b5edca262e1f4b23d36dcfbc`,
SPEC\_SHA `c1d7caf1002067e6103f44d5470ddcdc4db321fd4918337ef813924dce8a0a15`).
**Verdict INCONCLUSIVE**(truncation=beta=0.51, gamma=1000.00,
margin=$-5.118815\cdot10^{-7}$, tail\_heur=$1.267461$,
reason=omitted\_online\_uncontrolled).
49/49 injected off-critical zeros truncated-negative, but
$\gamma=1000$ is not certified (omitted on-line mass $\sim+1.27$
swamps margins; Lipschitz tail certifies 0/49).
Do **not** attack the Lean `fullWeil_separates_offCritical_zeros`
sorry before a height-uniform construction exists.
Separation sorry stays **[O]**.  NO RH CLAIM.

**Kernel--Loewner window map (r536,
PRIME.RDAGGER.KERNEL\_LOEWNER.WINDOW.01).**
Sealed probe `experiments/tfpt-discovery/kernel_loewner_window_probe.py`
(sha256 `1dd7b6d9f68b343bdabf3890af2b8f2778b833951c648ed5471ff3d8d1b68744`,
SPEC\_SHA `82d1409e6924d928e7442fe805486d840f0220b858a89387a3b1de3706e40dca`).
**Verdict WINDOW\_MAPPED**($L_{\max}=0.300000$,
$\lambda(L_{\max})=2.1220149285\cdot10^{-3}$,
tail\_alt=GO(block-Schur-tail)).
Frozen r494 method on the grid $0.30$–$0.80$; only $L=0.30$
certifies; dies at the $3\times$ HS tail before the first prime
node ($L=0.3125$ fail); block-Schur tail ($2\|\mathrm{off}\|+\|\mathrm{rest}\|$,
$m=800$) recovers $+7.152\cdot10^{-4}$ at $L=0.3125$.
**Framing (not a reopened window):** r502 already closed the
$\lambda^*$-ladder as a **proof route** for $L\ge 0.45$.  r536 is a
method result about tail bounds, not a reopened positivity window.
NO RH CLAIM.

**Honest-contour audit (r537).**
Sealed probe `experiments/tfpt-discovery/honest_contour_audit_probe.py`
(sha256 `ee0dc0ad86cfe7648798254d9a1f0488e8ac4cb519332ca89706af6f6b71423d`,
final after a determinism fix: a `RUNTIME_SECONDS` wall-clock
line was removed from stdout; smoke now byte-identical;
SPEC\_SHA `00075ab3233b7630a3d0a4652ba079b88e8a5afc3718810c6f9221f8e8531dc8`).
**Verdict AUDIT\_CLEAN**($\mathrm{max\_rel\_err}=5.8852501\cdot10^{-5}$)+
**DICTIONARY\_RESOLVES**($g\mapsto g\cdot\cosh(u/2)$;
class\_not\_preserved).
External mpmath audit (200 zeros, 40 digits) of the r534 honest
contour identity: all identities confirmed within the truncation
budget, **no Lean definition bug**.  The $(1+n^{-1})$ vs $2/\sqrt{n}$
mismatch is pointwise resolvable via $g\mapsto g\cdot\cosh(u/2)$
but that map does **not** preserve the autocorrelation class
(mapped Fourier transforms go negative), so same-test
identification stays genuinely obstructed; surplus
$\Lambda(n)(1-n^{-1/2})^2$ has no universal positivity direction
on the class.  Terminology: the actual right contour edge is
$\mathrm{Re}=2$ (not $17/16$; $17/16$ is the reflected left-edge
Dirichlet line).  Corpus identification stays **[O]**.  NO RH CLAIM.

**Kernel--Loewner promotion (2026-09-01, v1017).**
r494/r495 promoted to `verification/v1017_kernel_loewner_positivity.py`
(26/26).  Ledger row `PRIME.RDAGGER.KERNEL_LOEWNER.01` marker
**Proven finite statement [Numerical/certified]** — explicitly
**not [E]** (float64 floor, no interval arithmetic; repo
convention [E] = exact/interval).  Suite 1009$\to$1010 scripts;
`rh/paper` §2 certbox added.  NO RH CLAIM.

**Outer bridges r538 (Lean-only, outer-bridges round 42).**
No sealed probe, no probe row (gap like r534), no ledger row.
Sorry-free in `RH/ExternalBridges.lean`:
`fullWeilFormHonest` (prime channel $\Lambda(n)(1+n^{-1})$),
`standard_explicit_formula_identification_honest`
(`fullWeilFormHonest = standardExplicitFormula`, no seam),
`fullWeilFormHonest_nonneg_iff_standard_nonneg`,
`honest_weil_criterion_to_mathlib_rh` (explicitly conditional
on `FullWeilSeparatesOffCriticalZeros`), `surplusComb`,
`archGaugeDelta`, and the decomposition
`fullWeilForm = fullWeilFormHonest + surplusComb + archGaugeDelta`.
Axiom-checked: no `sorryAx`.  Old corpus sorry stays
documented-blocked.  `Open.lean` doc comment fixed.
Bridge-2 honest identification **CLOSED** (sorry-free,
conditional wrapper).  Lake green 3545 jobs, census
**stays 7**.  NO RH CLAIM.

**Weil-Gaussian separation (r539,
PRIME.RDAGGER.WEIL\_GAUSSIAN\_SEPARATION.01).**
Sealed probe `experiments/tfpt-discovery/weil_gaussian_separation_probe.py`
(sha256 `a4e258600fff1999da2f98682d122ed6364688fd25d1f9e1daf65f8b795f9524`,
SPEC\_SHA `87a2a2356e937e30a69a19db6ab6976257d40619074d6c3531545a89a9465657`).
**Verdict INCONCLUSIVE\_TRUNCATION**(worst=beta=0.51, gamma=5,
trunc=$-9.377491\cdot10^{-13}$, n\_trunc\_neg=25/56,
n\_cert\_neg=25/56).
Centered even Hermite--Gaussian class (deg $\le 8$): exponential
hat decay **fixes** the r535 tail (certified omitted on-line
charge $=0$ on all 25 winning cells, Trudgian JNT 134 (2014)
CERTIFIED label + crude-safe $C=4$); $25/56$ cells
certified-negative for $\gamma\le 14.13$ with live prime coupling
(no Yoshida collapse); all $\gamma\ge 30$ fail at truncation —
a transform centered at $0$ has no mass at $t\approx\gamma$.
No Lean Gaussian-campaign mandate; diagnosis: frequency shift
needed.  Separation stays **[O]**.  NO RH CLAIM.

**Weil on-line-null separation (r540,
PRIME.RDAGGER.WEIL\_ONLINE\_NULL\_SEPARATION.01).**
Sealed probe `experiments/tfpt-discovery/weil_online_null_separation_probe.py`
(sha256 `047d933ffae4a62f73f2a2924cc9e7464276655088ba283bd57ee6e09114f25e`,
SPEC\_SHA `d09ff8f680650958c528b618285d50b22b51d1a5d397e6cc9ce196109c2fed26`).
**Verdict SUPPORT\_VS\_HEIGHT**(frontier all nine $(R,N)$ cells
none).  On-line nulling inside the compact class: nullspaces
nontrivial (dim $50$–$180$, residual $\le 3.8\cdot10^{-13}$),
r535 regression anchor exact, but $0/135$ cells
Lipschitz-certified (tail charge $+77\ldots+2.5\cdot10^{4}$ vs
margins $\le 96$); $\gamma=1000$ does not even couple
(Nyquist $\omega_{\max}=K\pi/R\le 346$).  Compact-class
nulling is **CLOSED** as a certification path; confirms
noncompact route priority.  Separation stays **[O]**.  NO RH CLAIM.

**Weil-Gabor separation (r541,
PRIME.RDAGGER.WEIL\_GABOR\_SEPARATION.01).**
Sealed probe `experiments/tfpt-discovery/weil_gabor_separation_probe.py`
(sha256 `d85802a10bcada19df300d5d03028cc3f100051a755b7e7f33f03938da284a27`,
SPEC\_SHA `f7c832d6640c84390982309065a70f426ccee42a0388e0636af2f110882af919`).
**Verdict SEPARATION\_GO\_GABOR**(min\_certified\_margin=$-3.557041$,
worst=beta=0.51, gamma=$10^{4}$,
scaling=$a\sim\mathrm{const}$, $\omega\sim\gamma-\pi a/\sigma$).
Breakthrough **certified numerical precheck** for the
separation sorry: Gabor wavepackets
$h=p(t)e^{-at^{2}}\cos(\omega t)$ ($p$ even deg $\le 4$)
separate $42/42$ cells including $\gamma=10000$ with certified
on-line mass (exact first $100$ ordinates + Trudgian envelope
integral around $\pm\omega$ — no `zetazero` enumeration at
height $10^{4}$).  Scaling law $a=\sigma^{2}/64$,
$\omega=\gamma-\pi\sigma/64$ ($\sigma=\beta-1/2$), off-line
enhancement $e^{\sigma^{2}/2a}=e^{32}$; prime coupling live
($\eta\in[1.3\cdot10^{-2},0.998]$, no Yoshida collapse);
$11/11$ checks, G5 anchor reproduces r539 to $8.9\cdot10^{-16}$.
Honest boundary: finite quadratic-form search in a $3$-D
subclass + cited Trudgian majorant — a negative certified
Rayleigh is **not** yet a theorem for the class; the three Lean
lemmas needed are named (class def, closed-form/enhancement
identity, Trudgian on-line majorant).  Lean campaign licensed,
no claim.  Separation sorry stays **[O]**.  NO RH CLAIM.

**Gabor Lean architecture (r542–r600; no RH claim).**
r542 added `RH/GaborSeparation.lean`: identities and the
logical reduction chain are sorry-free; four named classical
inputs.  Current brick status:

- **Input 1 (integral):** PROVED r543
  (`RH/GaborIntegral.lean`, Mathlib `integral_cexp_quadratic`).
- **Input 2 (increment):** PROVED r546/r547
  (`RH/ZeroIncrement.lean`; Path-A
  `GaborIncrementBound = 2\cdot\texttt{zetaZerosInDiskCardBoundInner}`).
- **EF front (Input 3):** PROVED in Lean r581.
  Right vertical PROVED r564; left vertical PROVED r570;
  ACF / half-comb PROVED r572; contour $T\to\infty$ PROVED
  r576; $\chi'/\chi$ on the critical line PROVED r577;
  arch pairing + fixed-$T$ residue PROVED r578; $T\to\infty$
  glue `gaborArchContourShift_holds` + Digamma identification
  PROVED r581.  `gabor_vertical_arithmetic_remainder` is a
  **theorem** (no `sorryAx`).  r548 sealed
  `weil_gabor_explicit_formula_probe.py`
  (SPEC\_SHA `1c641853ec1f7ad00b3c2c3e0708c224ecd43d107b8f79a2c6f848c658068048`,
  probe SHA `16f8f59638b091f09fef3e44561f70388f6ba7d26e0093471c77fbd7a03191b9`):
  **verdict EF\_CONFIRMED** ($\mathrm{max\_resid}=9.36\cdot10^{-3}$,
  $A=36/36$, $B_{\mathrm{scharf}}=0/24$).  Classical identity
  $Z=\mathrm{Pole}-\mathrm{Prime_{comb}}+\mathrm{Arch}$; the Lean
  $(1+1/n)$ prime side was a false contour inversion (comb
  $2\Lambda/\sqrt{n}$ is the correct gauge).  r550 rebuilt
  `GaborExplicitFormula` onto that gauge; r555–r558 added
  hat analyticity, zero-summability, horizontal edges, and
  the fixed-$T$ contour identity, all sorry-free.
- **Separation front (Input 4):** canonical dominance route.
  Rule+bound hold numerically 119/119 (r567
  `CANONICAL_DOMINANCE_HOLDS`, worst margin $0.990408$).
  Constant-cap `GaborDominanceBound` is a **theorem**
  (r569/r571: $T_{\mathrm{gap}}=0$ after isolation, host
  quadrupole $Q<0$ under $a_0=\texttt{gaborSmallnessA}$,
  assembly budget $T_{\mathrm{far}}\le 1/70$,
  $T_{\mathrm{plus}}\le 1/100$, $R_{\mathrm{on}}/E\le 1/100$
  vs $\eta>9/10$).  Log-cap `GaborDominanceBoundLog` is a
  **theorem** (r574/r575) under `gaborFarSmallnessA`.
  r573 L2 audit: **STATEMENT\_WEAKENED** (substantial, not
  rigged, but a finite proxy: $K_{\mathrm{bin}}=43$ unproved
  for genuine zeros; $R_{\mathrm{on}}$ defined only;
  singleton junction; eight named bridges).  r579/r580 add
  log-occupancy transfer and two summable theorems; honest
  finding: unrestricted `GaborLogMajorantLeHonestBudget` is
  **false** ($\omega$-lobe log-grows vs constant budget).
  r582: FE multiplicity $m(z)=m(1-z)$ on the open strip
  plus weighted truncation compliance are theorems;
  $\omega$-dependent $R_{\mathrm{on,log}}=\max((1+\log)\cdot\mathrm{proxy},\hat h$-log majorant).
  Log-compatible `GaborDominanceBoundLog2` is a
  **theorem** (r583: both $R_{\mathrm{on,log}}/E$ branches
  via `online_exp_le_log`; $\hat h$-side closed
  linear-central+far-tail form).  Finite/conditional
  proxy only.  r584: tsum $\le$ Closed attachment
  `gaborLogThreeLobeMajorant_le_closed` is a **theorem**
  (Closed budget dominates the Finset-transfer majorant).
  r585: Schwarz $m(\bar\rho)=m(\rho)$, $\hat h$-star,
  quadrupole $4\mathrm{Re}\,\hat h$, and on-line mass
  $\le C_{\mathrm{hat}}\cdot$log-majorant are theorems;
  honest finding: weight-4 quadrupole tsum over all
  $\mathrm{Im}>0$ double-counts.  r586: weighted FD tsum
  `gaborOffLineMassEqWeightedQuadrupoleTsum_holds` is a
  **theorem** ($\mathrm{Re}>1/2\wedge\mathrm{Im}>0$,
  weight 4, plus real-axis remainder).  r587:
  poly-in-$t$ majorant $\|\hat h\|\le C(\sigma)(1+|t|)^8$
  three-lobe and unrestricted On/Off-split
  `gaborZeroSideEqOffPlusOn_holds` are **theorems**.
  r588: $\zeta(\sigma)\ne 0$ on $(0,1)$ real (via the
  r509 Euler--Maclaurin identity, not Eta);
  `gaborOffLineRealAxisMass_eq_zero`; weighted Bridge-6
  identification
  `gaborWeightedQuadrupoleLimitEqOffLineMass_holds` is a
  **theorem**.  Unweighted identification only
  `_of_simple` (simple zeros).  Finite/conditional
  proxy only.  r589: window$\to$BoundLog2 bridge is a
  **theorem** — every nonempty weighted FD window is
  BoundLog2 input (`gaborWeightedTruncationNegLog_holds`;
  singleton card=1 supplies gammaDistinct+hostIsolated).
  L2 adjudication r589: verdict **BRIDGE\_A\_IS\_RH\_CORE**
  — the singleton route is not a translation lemma
  (hides full off-line tail control; factor
  $\exp((\sigma'^2-\sigma^2)/2a)$ has no fixed sign;
  $R_{\mathrm{on,log}}$ majorizes only on-line).  Bridge B
  has no Isolation $a\le\sigma^2/512$ $\to$ Scaling
  $a=\sigma^2/64$ monotonicity transfer.  r590:
  existential arithmetic endpoint
  `GaborArithmeticSeparatesOffCriticalZeros` plus a
  parallel Mathlib chain without `scalingGaborTest`
  (sorry-free logic; old chain unchanged).  r591:
  `GaborFixedPacketCofinalNegAt` is numerically tenable
  **only with an extremality gap** (strict
  $\sigma'\le\sigma-0.02$ holds 9/9, worst $-0.995$;
  tie / free $\sigma'$ break).  r592: window-adaptive
  packets vs outer tail are **CONDITIONAL** (IEEE
  $\omega$-floor at extreme near-tie; host-$\sigma$-max
  retune per height/$T$).  r593/r594: outer-tail
  **theorem** (strip width beats window distance;
  `GaborOuterTailTsumLeExp` and
  `GaborOuterTailSmallerThanLocalMargin` are theorems).
  r595: three-term window+tail glue and per-$T$
  checkpoint are **theorems**; named gap
  `GaborWindowAdaptiveUniformDelta` ($T$-uniform $\delta$
  missing because of lex host-retune — r592 condition,
  not missing algebra).  r596–r598: L2 verdict
  **ANKER\_TEILWEISE**; log-glue **theorem**; witness
  $\Rightarrow$ zeroSide $< 0$ at the own packet; Cover
  is the remaining geometric rest.
  `GaborSpectralToArithmetic` is a **proved** pole-sign
  lemma (`GaborSpectralToArithmetic_holds`, $\hat h(1)\ge 0$),
  **not** RH-core (r600).  RH-core is hpos* :=
  $\forall$ admissible $F$, $0\le$ `gaborZeroSide` $F$,
  equivalently (through r611) the living sorry
  `gabor_separationForAllZeros` (asserting theorem retired at r612;
  Prop retained unasserted).
  `GaborAnchoredWitnessExists` is **not** asserted
  (ordinate clusters / multi-point window open).
  Remaining named rest:
  `GaborAnchoredCoverAt` (ordinate isolation of
  genuine zeros), `GaborAnchoredWitnessExists`,
  `GaborWindowAdaptiveUniformDelta`,
  `GaborTruncationUniformNeg` (does NOT follow from
  BoundLog2 — packet retunes),
  `GaborWeightedTruncationGammaDistinct`,
  `GaborFixedPacketCofinalNegAt` (extremality gap),
  and (through r611) the living sorry
  `gabor_separationForAllZeros` (retired at r612).
  **r599/r600 vacuity audit (2026-09-01/02).**
  `gaborSpectralFormula` subtracts the pole $\hat h(1)$
  and is **not** the Weil functional.  For
  $F_0=$ `pureGaborTest 1 0` the zero-side sum is
  $\approx 3\cdot 10^{-43}$ while
  $\mathrm{Re}\,\hat h(F_0,1)=\pi e^{1/8}\approx 3.5599$,
  so `gaborSpectralFormula` $F_0\approx -3.56$
  unconditionally.  Old hpos is **FALSE**.  Live object:
  `gaborZeroSide`.  Live endpoints:
  `GaborZeroSideSeparatesOffCriticalZeros`,
  `GaborZeroSideCriterionToMathlibRH`,
  `gabor_zeroSide_criterion_to_mathlib_rh`,
  `gabor_zeroSide_inputs_to_mathlib_rh`,
  `gabor_arithmetic_zeroSide_inputs_to_mathlib_rh`,
  `gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh`,
  `gabor_zeroSide_pure_criterion_iff_rh` (pure family,
  takes `hsep`; r605A **FORALL\_ZERO\_OVERSPECIFIED**),
  `gabor_zeroSide_criterion_iff_rh` (all $F$, carries
  `hline`).  Live unconditional iff:
  `gabor_zeroSide_pure_criterion_iff_rh_unconditional`
  (`RH/GaborExposedOrbit.lean`).  **VACUOUS (r600):**
  `GaborSeparatesOffCriticalZeros`,
  `gabor_separation_of_inputs`,
  `gabor_criterion_to_mathlib_rh`,
  `gabor_inputs_to_mathlib_rh`,
  `gabor_separation_of_arithmetic_separators`,
  `gabor_arithmetic_inputs_to_mathlib_rh`,
  `gabor_window_adaptive_inputs_to_mathlib_rh`.
  Named open (no claim): rigorous tsum
  $Z(F_0)<\pi e^{1/8}$; on-line positivity for general
  even quartics (beyond $\langle 1,0,0\rangle$) so the
  iff holds without `hline`.
  Scramble-gate **passed** (r565).  Discrete density transfer
  remains PROVED (r549/r552).  Open: that remaining rest
  list.  The $\forall Z$ proof stays open.
  **r601/r603/r604 sealed probes (experiments only; no RH claim).**
  r601 `gabor_weil_positivity_subfamily_probe.py`
  (SHA `b7089c71\ldots`): **DOMINANCE\_FAILS** --- 132 cells,
  EF sanity $\le 1.4\cdot 10^{-15}$, no negative cell,
  POS\_CERT 38 only for $\omega\ge\omega_0(a)$;
  fixed-$a$ Gabor is a Bombieri/Connes--Consani sub-family,
  not $\mathrm{hpos}^*$.  r603
  `prime_inequality_evosearch_probe.py` (SHA `06d2ac9a\ldots`,
  $13/13$): grid **SURVIVORS\_FOUND(1378)** but
  discriminatively empty (Re$\,s=1$ constants / grid
  artefacts; C1--C4 all density).  r604
  `tfpt_spectrum_zero_crosscorr_probe.py` (SHA `748ae509\ldots`,
  $7/7$, $\sim 28$\,s): **ARTIFACT** (positives fire on
  $\log p$; TFPT tones are prime-line aliases; T2
  $p_{\mathrm{gue}}=0.008$ is a null-calibration residual).
  **r605A/N/B/C (2026-09-02).** r605A: `GaborZeroSideForAllZeros`
  $= \forall\rho$ with prescribed packet
  `scalingGaborTest`($a=\sigma^2/64$, $\omega=\gamma-\pi a/\sigma$)
  $\to$ **FORALL\_ZERO\_OVERSPECIFIED**;
  `gabor_zeroSide_pure_criterion_iff_rh` takes `hsep`.
  r605N `gabor_exposed_orbit_probe.py` (SHA `c99998c4\ldots`,
  SPEC `1a4bf949\ldots`, $40/40$, byte-identical):
  **EXPOSED\_ORBIT\_HOLDS** (9/9 configs negative at $n=0$,
  normalised limit $-4m(\rho^*)$ exact, tail bound holds).
  r605B+C `RH/GaborExposedOrbit.lean` (1734 lines, sorry-free):
  `gaborScore`, `ExposedOrbit`, `exists_exposedOrbit_of_not_rh`,
  phase lock $\cos=-1$, three-lobe majorant
  $\mathrm{Re}\,\hat h(\rho^*)\le -(\pi/4a)e^{M/2a}+(3\pi/4a)e^{(M-\Delta)/2a}$,
  `gaborExposedOrbitAssembly_holds`,
  `exists_negative_pureGabor_of_not_rh` (`hasm`),
  `gabor_zeroSide_pure_criterion_iff_rh_of_assembly` (`hasm`),
  `gabor_zeroSide_pure_criterion_iff_rh_unconditional`
  $(\forall a\,\omega\,ha,\ 0\le\texttt{gaborZeroSide}(\texttt{pureGaborTest}\,a\,\omega))\leftrightarrow\texttt{RiemannHypothesis}$;
  $\#$print axioms $=[$`propext`, `Classical.choice`, `Quot.sound`$]$.
  Census at this landing **8** (Canonical 3, Source 1, Elementwise 1,
  GaborSeparation 1, ExternalBridges 2); live **7** after r612.
  r605C-AUDIT (independent, read-only): **STATEMENT\_SOUND**.
  Mandatory wording: RH $\Leftrightarrow$ nonnegativity of the
  pure Gabor zero-side on the two-parameter family $(a,\omega)$.
  Sharpest live statement (r634L): RH $\Leftrightarrow$
  $\forall$ rational $(a,\omega)$: POLE $-$ PRIME $+$ ARCH $\ge 0$;
  positivity of `gaborZeroSide` itself remains open.
  This is **not** an RH proof; the Weil test space is reduced
  to a two-parameter pure Gabor family on the zero side.
  **r607 sealed probe (experiments only; no RH claim).**
  r607 `event_lindblad_twokey_probe.py` (SHA `3c1db81b\ldots`,
  SPEC `3abe6b9b\ldots`, $15/15$):
  **KILLED(RECOORDINATIZATION)** --- Lindblad CP
  $\Leftrightarrow\lambda_{\min}(Q_W)$ to $10^{-15}$ in
  TRUE/SCRAMBLE/EPSTEIN/WPERM; diagonal compensator
  $\Sigma\lambda$ diverges $\sim 2e^{X/2}$; Euler--Pick Gram
  needs 10 scalars; labels decorative.
  **r608 sealed probe (experiments only; no RH claim).**
  r608 `gabor_tropical_heat_probe.py` (SHA `574c1cc2\ldots`,
  SPEC `6fcc507d`, SPEC\_DESIGN `0008f535\ldots`, $9/9$):
  **TROPICAL\_CONFIRMED** --- $2a\cdot\log|Z|\to F(\omega)$ with
  error $\le 6.77\cdot a\cdot\log(1/a)$; on-line
  $F=-\mathrm{dist}(\omega,\{\gamma\})^2\le 0$; synthetic
  $\beta=0.9$ gives $F=+0.16$.  Heat equation
  $\partial_a\hat h=\tfrac12\partial_\omega^2\hat h-\hat h/(2a)$
  (rel $3\cdot10^{-9}$) on traveling lobes; $U=\sqrt{a}\,Z$ is
  **not** a heat solution.  Source budget
  $B(a)=2.05/4.18/13.6$ at $a=0.2/0.1/0.05$.
  HEAT.SOURCE lane **NOGO T1**, STOP.
  **r609 sealed probe (experiments only; no RH claim).**
  r609 `e8_directed_readout_probe.py` (SHA `9ab0a638\ldots`,
  SPEC `3edfb824\ldots`, $49/49$):
  **E8\_READOUT\_SEALED(7/8)** --- Seifert $S+S^T=A$,
  $\mathrm{charpoly}(-S^{-1}S^T)=\Phi_{30}$, $\mathrm{rank}(S-S^T)=8$.
  C7 NOT\_TESTED at probe time; later supplied in
  `note_e8_gaussian_code.tex`.  Gauss-code transform still
  undefined.  TFPT-side exact structure; **no prime bridge**;
  promotion to `verification/` is a pending user decision.
  **r610 Lean-only (no probe).**
  `GaborLowHeightZeroFree` $T_0=4$ unasserted Prop;
  pole $\pi e^{1/8}$ (`gaborHat_pure_one_zero`); zero side
  $\le 19/20$ of it; `gaborSpectralFormula_refuted_of_lowHeight`.
  Axioms `propext` / `Classical.choice` / `Quot.sound`.
  **r611 sealed probe (experiments only; no RH claim).**
  r611 `connes_observable_aubin_nitsche_probe.py` (SHA
  `93607746\ldots`, SPEC `647335a6\ldots`, $12/12$):
  **OBS\_NOT\_CONVERGING** --- $\eta_{\mathrm{obs}}(1.2)$ TRUE
  falls then rises; OFFLINE $\approx$ TRUE (blind to injected
  off-line zero at $\gamma=20$).  Herglotz/Aubin--Nitsche
  closure (Solution 1) **STOP**; PROLATE.GABOR.ALIGN moot.
  r606b CLOSED: `connes_prolate_residual_gap_probe.py`
  (SHA `aeef52a6\ldots`, SPEC `115c0409\ldots`, $\sim 0.4$ s,
  dual-run byte-identical):
  **INCONCLUSIVE(evals-not-converged, disc-disagree>5pct)** ---
  no $L$ meets successive-$N<1\%$ AND Slepian/Fourier
  agreement $<5\%$; wall is discretisation (Slepian $\lambda_2$
  pollution beyond $N=12$--$24$, Fourier odd-mode $\sim 2\%$,
  $t_{\mathrm{cut}}=1000$ blocked by spatial Nyquist), not a
  GO/STOP on $\eta$.  The r606 $\mu\approx 5.9$ jump is gone
  ($k$ tracks $\lambda_1$); $\lambda_1^{e}$ slightly negative
  ($-3\cdot 10^{-6}$--$-8\cdot 10^{-6}$) at $L\ge 0.5$ but
  unconverged --- not a Chuk contradiction; NREAL
  $\widehat\theta[0,30]=2,3,3,4,4,4$ vs Riemann count $3$
  (plateaus at $4$).  Lane CLOSED --- superseded by r611
  and KILLED(FACTORIZATION); diagnostic only.
  **r612 Lean-only (no probe).**
  Asserting theorem `gabor_separationForAllZeros` deleted;
  Prop `GaborSeparationForAllZeros` retained unasserted
  (OVERSPECIFIED / believed-false).  New module
  `RH/GaborCountableCriterion.lean` (later 551 lines at r612C):
  `gabor_zeroSide_rational_criterion_iff_rh` ($h_{\mathrm{cont}}$)
  $\leftrightarrow$ `RiemannHypothesis`.  Module count $53\to 54$.
  Tracked sorry census **8 → 7**.
  **r612C Lean-only (no probe).**
  `gaborZeroSideContinuous_holds` proves
  `GaborZeroSideContinuous` (joint continuity on $\{a>0\}\times\mathbb{R}$
  via a local uniform Gaussian majorant and `continuousOn_tsum`).
  The rational-packet criterion
  `gabor_zeroSide_rational_criterion_iff_rh_unconditional`
  is **unconditional**:
  $(\forall a,\omega\in\mathbb{Q},\ a>0:\ 0\le$
  `gaborZeroSide`(`pureGaborTest` $a\,\omega$)$)
  $\leftrightarrow$ `RiemannHypothesis`.
  Named-open list shrinks by one; census stays **7**.
  Axioms `propext` / `Classical.choice` / `Quot.sound`.
  **r613 sealed probe (experiments only; no RH claim).**
  r613 `prime_e8_ordered_herglotz_probe.py` (SHA `c89fc1ce\ldots`,
  SPEC `01b4a8be\ldots`):
  **NO\_IDENTIFICATION** --- Weyl Herglotz, $(JH)^2=0$ exact;
  $\varepsilon=0$ order decorative; $\varepsilon=0.05$ residuals
  TRUE $\approx$ SCRAMBLE/WPERM.  Ordered-E8 Herglotz
  canonical system (Paket C, `PRIME.E8.ORDERED.HERGLOTZ.01`)
  **dead as a lane**.
  **r615 sealed probe (experiments only; no RH claim).**
  r615 `semilocal_firststep_probe.py` (SHA `3a0741de\ldots`,
  SPEC `04f9c9ec\ldots`, $26/26$):
  **FIRSTSTEP\_LEAKAGE\_CONTROLLED** --- Weil window form with
  exactly one prime ($L\in(0.3466,0.5493)$,
  $w_2=\sqrt{2}\log 2=0.98026$); Ritz $\lambda^*(L)$ equals
  zero-side leakage to $10^{-4}$--$10^{-5}$; extremal vector
  Slepian-like (overlap with $\psi_0\ge 0.9989$,
  $\ge 99.8\%$ spectral mass below $\gamma_1=14.1347$).
  $\lambda^*(0.30)=7.57\cdot10^{-3}$ (v1017 padded floor
  $2.1\cdot10^{-3}$, factor $3.6$),
  $\lambda^*(0.40)=1.85\cdot10^{-4}$,
  $\lambda^*(0.549)=5.80\cdot10^{-8}$
  (POLE $+1.30$ / ARCH $-1.29$ / PRIME $1.78\cdot10^{-2}$,
  cancellation depth $2.25\cdot10^7$).
  Certificate obstruction: shift cross-block norm $0.50$
  for $N=40/80/160$ (no decay); Schur
  $R=0.25/\lambda^*=1.4\cdot10^3$ ($L=0.40$) $\ldots 4.45\cdot10^6$
  ($0.549$) --- r496 confirmed for every window containing a
  prime.  Mechanism (T9): fictitious prime-free POLE+ARCH
  minimizer is purely odd; $-w_2 g(\log 2)$ carries positivity.
  Named open lemma **PRIME.SEMILOCAL.ODDSECTOR.EDGE.01** [O]
  (r620 retype, oriented: for odd $h$ on $[-L,L]$,
  $\langle h,(\mathrm{POLE}+\mathrm{ARCH})h\rangle
  +w_2(\lVert f_+\rVert^2-\lVert f_-\rVert^2)\ge 0$;
  the negative direction of POLE+ARCH migrates from the inner
  region to the $R$-symmetric edge sector; the antisymmetric
  edge sector is safe without the prime; repair is quantitative
  dominance with margin $\lambda^*(L)$, not an exact sector
  identity).
  Fence: $L\lesssim 16$ cannot detect off-line zeros; first
  prime step is far weaker than RH.
  **r616 sealed probe (experiments only; no RH claim).**
  r616 `inertia_highermoment_probe.py` (SHA `26ee62ae\ldots`,
  SPEC `fef4a72f\ldots`, $16/16$):
  **C\_CAPPED** --- $k=2$ reproduces Alpöge--Furman $2/3$
  and ceiling $0.6818287$; $\mathrm{Tr}(W^3)$ at bandwidth one
  is not unconditional $\Rightarrow p_3^{\mathrm{uncond}}=p_2=0.6818$.
  Finite moments never force negative index $0$.
  **r617 sealed probe (experiments only; no RH claim).**
  r617 `e8_coxeter_euler_completion_probe.py` (SHA
  `6ac6bab2\ldots`, SPEC `5aa3935b\ldots`, $45/45$):
  **COMPLETION\_EXACT** --- $\mathrm{Tr}\,C=-1$; $\Phi_{30}$
  Möbius identity; $D_{E8}(s)$ residuals at $X=10^6$:
  $1.28\cdot10^{-4}$ ($s=0.75$), $3.5\cdot10^{-14}$ ($1.5$).
  Typed no-go **E8.COXETER.REGULARIZED\_SPLIT.NO\_GO.01**.
  Fence: trace-free completion zero-free and pole-free in
  $\mathrm{Re}\,s>1/2$; splitting into scalar zeta and Coxeter
  channels is open and RH-equivalent.  Promotion to
  `verification/` (v1018/v1019) is in progress (not promoted).
  **r617L Lean-only (no probe).**
  New modules `RH/CoxeterCompletion.lean` (96 lines) and
  `RH/PrimeLogIndependence.lean` (160 lines): $\Phi_{30}$
  identities, $\mathrm{Tr}\,C=-1$, and $\mathbb{Q}$-linear
  independence of $\{\log p\}$ (`linearIndependent_log_primes`;
  Mathlib had no such lemma).  lake build green (3578 jobs),
  no `sorry`, census stays **7**.  Module count **54 → 56**.
  **r618 sealed probe (experiments only; no RH claim).**
  r618 `jensen_compiler_rigidity_probe.py` (SHA
  `29ccf1c7\ldots`, SPEC `bc8d8624\ldots`, $43/43$):
  **COMPILERS\_STRUCTURALLY\_RIGID** --- (A) Seifert-compiler
  rigidity (Coxeter monodromy is a congruence invariant);
  (B) rank-one MSS mixed characteristic polynomial
  $=\det(xI-\sum A_e)$ exactly.  Fence: both compilers are
  generic real-rootedness certificates; existence for all
  $(n,d)\Leftrightarrow$ RH; E8 RH-neutral.
  **r619 sealed probe (experiments only; no RH claim).**
  r619 `support_relay_census_probe.py` (SHA `fcfa7771\ldots`,
  SPEC `7299737d\ldots`, RESULT\_SHA `e0379485\ldots`, $12/12$):
  **RELAY\_UNIVERSAL** --- prime powers $q\le 32$ (18 events),
  entry $L_j=\tfrac12\log q$; every ancestor $Q_{j-1}$ fails
  a finite lead after entry $\Delta_j=0.011$--$0.028$ (nearly
  constant at $N=80$; greedy $\Delta\approx 0.015$
  WITHDRAWN by r635 --- $N=80$ double-precision artefact;
  converged $\Delta_2=0.0253$, $\Delta_3=0.0083$,
  $\Delta_4=0.0064$ ($0.00606$ at $N=160$),
  $\Delta_5=0.0034$ ($0.00275$ at $N=160$); $q\ge 7$
  UNMEASURABLE at the $40$-digit floor);
  failing mode always odd, $g<0$, newest weight restores
  positivity (all 18).  $\lambda^*$ slopes $-50/-77/-79$
  at fixed $N=80$ (global $-68.6$; Slepian $-28.3$; r615
  $-44.8$) --- the $-77/-79$ values at $L=0.9$--$1.4$ are
  $N$-artifacts, corrected by r630b to $-50.6$ ($0.3$--$0.6$)
  and $-116$ ($0.6$--$1.0$); RELAY\_UNIVERSAL, entry census,
  odd/edge mode, and $L_{\mathrm{det}}$ unaffected ---
  super-exponential (Landau--Widom plunge).  Controls break
  at entry+lead (SCRAMBLE $0.376$, WPERM $0.402$, EPSTEIN
  $0.564$).  $L_{\mathrm{det}}(\beta=0.6,\gamma=20)=0.55$,
  $(0.75,20)=0.55$, $(0.6,50)=0.80$, $(0.9,20)=0.50$.
  PARENT TYPING: RELAY\_UNIVERSAL criteria are consequences
  of $Q_j\succeq 0$ (RH-consistency), not a mechanism;
  steps beyond $L\approx 0.5$ are RH-in-a-box.  Fence:
  window positivity for the scanned $L$ is RH-consistent;
  no RH claim.
  **r620 sealed probe (experiments only; no RH claim).**
  r620 `p2_reflection_factor_probe.py` (SHA `194fe9e5\ldots`,
  SPEC `7c8e73b7\ldots`, $73/73$):
  **MIXED\_SECTOR** --- exact identity $g_h(d)=-(\lVert f_+\rVert^2-\lVert f_-\rVert^2)$
  for odd $h$, $d=\log 2$; prime term stabilizes the symmetric
  edge and destabilizes the antisymmetric.  $\dim E_-(A^{\mathrm{odd}})=1$
  for $L\ge 0.38$; negative-vector mass migrates inner $\to$
  $R$-symmetric edge.  Oriented inequality
  $\lambda_{\min}(A^{\mathrm{odd}}+w_2(P_+-P_-))=\lambda^*(L)\ge 0$.
  Retypes **PRIME.SEMILOCAL.ODDSECTOR.EDGE.01** [O] to the
  oriented form (repair is quantitative dominance, not an
  exact sector identity).
  **r621 sealed probe (experiments only; no RH claim).**
  r621 `p2_digamma_duplication_probe.py` (SHA `dff2e1b3\ldots`,
  SPEC `78f47c87\ldots`, $37/37$):
  **DUPLICATION\_CONSTANT\_ONLY** --- duplication identity
  to $2\cdot 10^{-25}$; $\mathrm{ARCH}_{1/4}=\mathrm{ARCH}_{\mathbb{C}}-\mathrm{ARCH}_{3/4}-2\log 2\cdot G$
  to $2\cdot 10^{-15}$; prime-2 vs $\mathrm{span}\{\mathrm{ARCH}_{3/4},G\}$
  residual $0.997$--$0.998$ (HS cosine $\le 0.005$).
  No-go: the prime-2 repair is not a duplication factor of
  the archimedean operator.
  **r622 sealed probe (experiments only; no RH claim).**
  r622 `support_darboux_probe.py` (SHA `845bb937\ldots`,
  SPEC `27ffd017\ldots`, PAYLOAD `e1031d17\ldots`, $64/64$):
  **TRANSPORT\_FEASIBLE\_NORULE** --- $X=0$ feasible for
  $c=c_0(L)$ (finite; spike $368$ at prime entry, $1614$ at
  $0.549$); no two-term closed-form law (rms $347$);
  forbidden $X_0$ not in the source algebra (residual
  $0.88\to 1.0$); algebra rate $0$ vs required $31.8/46.0$.
  Transport relocates tiny margins into $c_0(L)$; no
  source-side rule.
  **r623 sealed probe (experiments only; no RH claim).**
  r623 `semilocal_p2_dilation_probe.py` (SHA `d1bec728\ldots`,
  SPEC `5890676d\ldots`, $128/128$):
  **P2\_DILATION\_STRUCTURALLY\_BLOCKED** --- $2$-adic channel
  $m_2(t)=\log 2\cdot(1-P_r(t\log 2))$, $r=2^{-1/2}$, $P_r$
  Poisson kernel (de Branges--Rovnyak of $b(z)=(z-r)/(1-rz)$);
  one Euler factor generates $2^k$ (active rungs $[2]$ for
  $L\le 0.65$, $[2,4]+3$ for $L\in\{0.72,0.80\}$); identity
  residual $4.9\cdot10^{-12}$.  Ancestor POLE+ARCH
  $\lambda_{\min}=-0.078$ ($L=0.40$) $\ldots$ $-0.926$ ($0.80$)
  --- not a PSD principal block; $M_2$ indefinite ($n_+/n_-$
  $9/9$ at $0.40$ $\ldots$ $14/10$ at $0.80$), rank$/N$
  $0.75$--$1.0$ (not rank one); generic dilation tracks
  $\lambda^*(L)$ (tautological).  No local SOS
  ($\lVert N\rVert/\lambda_{\min}(P)=2.75$--$5.27$).
  Literature stops at $\sqrt{2}$ (Connes--Consani 2021 Thm 1).
  Semilocal dilation lane **not opened**.  Fence: semilocal
  identities; window forms at these $L$ are RH-consistent.
  **r625 sealed probe (experiments only; no RH claim).**
  r625 `iiks_vanishing_metric_probe.py` (SHA `973a1ce2\ldots`,
  SPEC `7a4257e3\ldots`, NUM `2d066e2d\ldots`, $19/19$):
  **IIKS\_NO\_METRIC\_IN\_CLASS** (prose
  NOT\_TESTABLE\_IN\_CORPUS\_FORM) --- jump $J_s=I-2\pi i s\,fg^T$
  on real CD nodes fails $J^*=J^{-1}$ (rel $2.56\cdot10^{-2}$
  on WPERM kz9); $\det J=1$ at $s^*$ while $\tau(s^*)=0$
  ($\log\lvert\tau\rvert\approx-38$).  $H=I$ dissipativity is
  the wrong sufficient condition (TRUE min eig $1.93$--$1.99$
  *and* WPERM despite $\tau$-zeros).  Best $H=\mathrm{diag}(\mathrm{arch}^{1.50},\mathrm{arch}^{1.50})$:
  TRUE worst $-8.17\cdot10^{-10}$ (first pass $-3.36\cdot10^{-7}$;
  bar $-10^{-12}$); WPERM $-7.9\cdot10^{-9}\ldots-4.4\cdot10^{-4}$;
  EPSTEIN $-2.7\cdot10^{-2}\ldots-6\cdot10^{11}$; SCRAMBLE
  $-3\cdot10^{6}\ldots-9\cdot10^{57}$; controls fail pointwise
  before $\tau$-zero ($5/5$).  Vanishing-lemma route not
  testable on the corpus discrete object.
  **r626 sealed probe (experiments only; no RH claim).**
  r626 `xi_finitefree_collision_probe.py` (SHA `c4750063\ldots`,
  SPEC `c7cef974\ldots`, NUM `f533d168\ldots`, $51/51$):
  **COLLISION\_DETECTOR\_CALIBRATED\_NO\_BARRIER** ---
  $d/dt\log\lvert\mathrm{Disc}(P_t)\rvert=4\cdot\Phi_N(P_t)$
  (rel $8.9\cdot10^{-11}$) makes $\int\Phi\,dt<\infty$
  equivalent to $\mathrm{Disc}\ne0$ (tautological).  Taylor
  $\Xi$ sections not real-rooted at $t=0$ ($N=6/8/12$: $0$
  real roots); $t_0(N)$ always a spurious far-pair; inner
  collisions at $t_c>0$ every $N$.  Detector calibrated on
  $S_N=\prod(1-x^2/\gamma_k^2)$:
  $\varepsilon_{\mathrm{crit}}=-3.65\cdot10^{-4}$ ($a_1$,
  $N=8$), $t_c=0.597$.  Turán min ratio $1.02$; Newton/Laguerre
  $0.51$.  Second cut of the day (with r623/r625) closed
  negative; pause the active positivity campaign pending a
  genuinely new mechanism.
  **r627 sealed probe (experiments only; no RH claim).**
  r627 `af_twomoment_optimizer_probe.py` (SHA `da1a9118\ldots`,
  SPEC `9b95f564\ldots`, $17/17$):
  **NO\_GAIN** --- contract `PRIME.INERTIA.TWOMOMENT.OPT.01`.
  A--F two-moment $R(\psi)=[\int\psi^2+\iint\lvert u-v\rvert\psi(u)\psi(v)]/(\int\psi)^2$,
  $p=2-R$ on $\mathrm{supp}\,\psi\subset[-\tfrac12,\tfrac12]$;
  Euler--Lagrange $(I+K)\psi=\lambda\cdot 1\Rightarrow\psi''+2\psi=0$
  $\Rightarrow$ unique critical point $\psi^*=\cos(\sqrt{2}\,t)$
  (Montgomery--Taylor), $p^*=0.6725007037$ ($N=8$--$64$ identical,
  $\omega$-scan optimum $\sqrt{2}$); positivity slack
  $\min 0.760>3/4$; proved ceiling $0.6818287$ bounds the richer
  two-moment + on/off-block certificate, not the window optimum;
  gap $9.3\cdot 10^{-3}$ not closable by window optimization.
  **r628 sealed probe (experiments only; no RH claim).**
  r628 `window_box_verifier_probe.py` (SHA `9c99ed6a\ldots`,
  SPEC `36c0e66a\ldots`, NUM `84aaf685\ldots`, $12/12$):
  **COMPRESSION\_CERTIFIED\_BOX\_NUMERICAL** --- contract
  `PRIME.WINDOW.BOX.VERIFIER.01`.  Interval-certified (40 digits,
  interval Cholesky/Weyl) positivity
  $\lambda_{\min}\ge 1.05\cdot 10^{-7}$ ($L=0.55$, $N=24$,
  $\{2,3\}$), $\ge 6.1\cdot 10^{-11}$ ($0.65$, $N=40$),
  $\ge 9.3\cdot 10^{-17}$ ($0.80$, $N=40$, $\{2,3,4\}$);
  cancellation depth up to $6\cdot 10^{14}$.  Rigorous zero-free
  box NOT closed: Trudgian $\lvert S(T)\rvert\le 0.112\log T
  +0.278\log\log T+2.51$ (JNT 134, 2014) is $\sim 10^{7}$ too
  loose; numerical box nonempty.  Missing lemma: local
  zero-density bound or enumerated zeros (Booker/Turing-equivalent).
  Typed as Booker Exp.\ Math.\ 15 (2006) in window form.
  **r629 sealed probe (experiments only; no RH claim).**
  r629 `certificate_class_atlas_probe.py` (SHA `4dae1fbe\ldots`,
  SPEC `0bf7c64f\ldots`, $15/15$):
  **ATLAS\_NO\_NEW\_UNCONDITIONAL\_GAIN** --- contract
  `PRIME.CERTIFICATE.ATLAS.01`.  LP over hypothetical zero
  configurations: A1 two-moment reproduces $1-p_0=0.3181713$
  ($p_0=0.6818287$); A2 $+N(T)/S(T)$ unchanged; A3 $+$ prime-free
  window positivity (CC 2021) redundancy $0$ (min slack
  $2.2\cdot 10^{-4}$); A6 $+$ Huxley unchanged.  Conditional:
  GUE $k=3\to 5/6$, $k=4\to 31/36$; pair correlation
  $\alpha_{\max}=1.5/2/\infty\to 0.7046/0.7159/0.7500$.
  Only correlation input beyond support $1$ buys proportion.
  **r632 sealed probe (experiments only; no RH claim).**
  r632 `jet_deflated_ldet_probe.py` (SHA `63ecb68f\ldots`,
  SPEC `31a29760\ldots`, RESULT `6299cedc\ldots`, $14/14$):
  **JET\_GAIN\_SMALL** --- contract
  `PRIME.WINDOW.JETDEFLATION.01` (reviewer-proposed).
  Baseline reproduces r619 $L_{\mathrm{det}}$ ($0.55/0.50/0.80$).
  Deflation $\hat f^{(r)}(20)=0$: $m=0$ $G=0$, $m=1$ $G=0.40$
  ($L_{\mathrm{det}}$ $0.55\to 0.95$ at $(0.6,20)$); first eight
  true zeros $G=0.65$, sector Ritz floor at $L=0.6$ jumps
  $1.76\cdot 10^{-9}\to 2.02$.  Coverage kill: $\Gamma=50$ needs
  $\dim K/N=0.50$ (above Nyquist $31.8$), $\Gamma=100\to 1.45$,
  $\Gamma=200\to 3.95$ --- not a cheap RH-free statement.
  **r630/r630b sealed probe (experiments only; no RH claim).**
  r630 `margin_law_symreg_probe.py` (SHA `5b3d1125\ldots`,
  SPEC `87febb97\ldots`, RESULT `a0765d7f\ldots`, $19/19$,
  $166$ s, dual-run identical): **MARGIN\_LAW\_UNRESOLVED**
  --- $L_{\mathrm{cross}}=0.3716$, SVD floor $L=0.78$.
  Addendum r630b (tall QR, $40$ digits,
  $N\in\{40,60,80,120,160\}$, $L\in[0.30,1.40]$):
  **N\_LIMITED\_ARTIFACT** --- $\lambda^*$ converges in $N$
  for $L\le 1$ ($35/36$, rel.\ $120\to 160$ median
  $4.8\cdot 10^{-2}$) not for $L>1$ ($0/20$); log-slopes
  $-50.6$ ($0.3$--$0.6$) and $-116$ ($0.6$--$1.0$);
  $\lambda^*_{160}(0.6)=1.65\cdot 10^{-9}$,
  $\lambda^*_{160}(1.0)=9.93\cdot 10^{-30}$; quadratic
  $C=95.5$ (neither $2\gamma_1=28.27$ nor
  $\gamma_1^2/\pi=63.6$) --- Widom-$L^2$ and $-2\gamma_1 L^2$
  unsupported.  N2: minimizer nulls $4707$--$4831$ of $5000$
  zeros.  N3: density-driven Landau--Widom (true $169$ /
  const-density $101$ / first-zero@$10$ $105$ / @$20$ $271$
  / only first moved $172$), RH-neutral.  N4: dBN $B_k$
  on $4999$ gaps max $41.8$, $p_{99}=11.5$, median $2.13$,
  fraction $B_k<2=0.470$ --- no universal gap barrier.
  **r633 sealed probe (experiments only; no RH claim).**
  r633 `frontier_followups_probe.py` (SHA `9f5287e7\ldots`,
  SPEC `ee7c7ba7\ldots`, RESULT `814abdf5\ldots`, $16/16$,
  $18$ s, dual-run identical):
  **F1 A\_COMPACT\_OTHER($p\approx 1.02$)** --- $a_{\max}$
  linear in $\sigma$ not $\sigma^2$; compactification
  cosmetic ($a\to\infty$ RH-blind; $a\to 0$ unbounded).
  **F2 FORWARD\_INCREASES\_MARGIN** --- HF $=$ Loewner
  $10^{-15}$; $c(L)=+0.315/+0.582/+0.764$; detector, no lever.
  **F3 RANDOM\_EULER\_REFUTED** --- Haar MC $99.5\%$ negative
  stands; Baker $7.3$ decades; magnitude/Diophantine dead.
  $C(L)=1$ is NOT the mechanism (generic for minimizers,
  including negative Haar draws; r637).
  **F4 LEAD\_LAW\_INVARIANT** --- VOID (r635/r636); based on
  withdrawn $N=80$ $\Delta\approx 0.015$ values.
  **r635 sealed probe (experiments only; no RH claim).**
  r635 `relay_lead_precision_probe.py` (SHA `36c06826\ldots`,
  SPEC `28db9bef\ldots`, RESULT `3457e907\ldots`, $11/11$,
  $1260$ s): **LEAD\_PARTIAL**.  Converged leads
  $0.0253/0.0083/0.0064/0.0034$; $q\ge 7$ UNMEASURABLE
  (probe: later events already indefinite at entry;
  $q=7$ $\lambda_{\min}=-6.99\cdot 10^{-11}$).  Greedy
  $\Delta\approx 0.015$ WITHDRAWN.
  **r636 sealed probe (experiments only; no RH claim).**
  r636 `relay_lead_law_probe.py` (SHA `ee2deb46\ldots`,
  SPEC `6bf7a7ee\ldots`, RESULT `2a6bd720\ldots`, $6/6$,
  $0.5$ s): **LEAD\_LAW\_PARTIAL** --- no model $<20\%$ on
  all four; lead law dissolved; r633-F4 void.
  **r637 sealed probe (experiments only; no RH claim).**
  r637 `relay_vote_map_probe.py` (SHA `fc5c1426\ldots`,
  SPEC `44bf67f8\ldots`, RESULT `540557ad\ldots`, $14/14$):
  **VOTE\_MODE\_SPECIFIC** ($k_{\mathrm{thr}}=3$) +
  **FLIP\_COUNTEREXAMPLE**.  Unanimity GENERIC (SCRAMBLE
  $C=1$ at every $L$); $C$ not a positivity predictor.
  Decoding programme (r635--r637): constant lead, unanimity,
  and odd-edge defect type reduce to margin collapse and
  edge geometry; no side channel measured.
  **r638 sealed probe (experiments only; no RH claim).**
  r638 `gabor_first_contact_selberg_probe.py` (SHA `2ab532bc\ldots`,
  SPEC `22a92842\ldots`, RESULT `58a36aff\ldots`, $14/14$,
  $338$ s dual): **KILLED(STRUCTURAL: selberg-convolution-is-hankel)**.
  First-contact + Selberg square completion on the pure-Gabor
  zero side $G=\mathrm{POLE}-\mathrm{PRIME}+\mathrm{ARCH}$.
  Pre-registered Toeplitz gate: the Selberg term
  $\sum_N(\Lambda*\Lambda)(N)\psi(\log N)$ is a Hankel form in
  $(\log m,\log n)$; PSD completion over 15 operator-generated
  $\psi$ fails in $15/15$ cells (best $\lambda_{\min}=-0.0097$,
  tolerance $-10^{-9}$; $2\times 2$ minor violation $1.0$).
  Euler-local squares (the only ones compatible with the
  frequency support $\{\log n\}$) cost DC $\ge 3.28\times$ the
  POLE$+$ARCH budget at $a\le 0.3$, $\omega\ge 30$.
  Contact geometry (synthetic $\sigma=0.4/0.25/0.1$ at
  $\gamma_0=100$, $0.4$ at $250$): $a^*=0.142/0.088/0.037/0.113$,
  $\omega^*-\gamma_0\approx 0.55$--$0.66$, off/on block ratio
  $1.0000$; $\partial_aZ=\tfrac12\partial_\omega^2Z$ to
  $1.6\cdot10^{-16}$ --- the two contact conditions are one;
  negativity is a down-set in $a$.  True $\zeta$ ($a=1/0.5/0.3$,
  $\omega\in[10,50]$): $G\ge 0$ (min $2.2\cdot10^{-12}$ at $a=0.3$);
  helpful-sign fraction of the Selberg part at the local minima
  $0.25/0.22/0.33$ (MAIN) vs $0.22/0.31/0.22$ (SCRAMBLE) vs
  $0.29/0.20/0.20$ (WPERM): SELBERG\_SIGN\_INDEFINITE, WORLD\_BLIND;
  median $|\mathrm{Selberg}_1|/|\Lambda_{2,1}|=0.74$--$1.33$
  (cancellation relocated, cf.\ CCCXXXI).  Lane
  GABOR.CONTACT.SELBERG.01 STOP.
  **r639 sealed probe (experiments only; no RH claim).**
  r639 `lamzouri_hilbert_adjudication_probe.py` (SHA `61fbb4b9\ldots`,
  SPEC `4bc44422\ldots`, $23/23$):
  **SAME\_CLASS** + **CONSTANTS\_IDENTICAL** + **WALL\_LOCATION\_CONFIRMED**
  --- arXiv:2609.02882 (Lamzouri, 2026-09-02) re-proves the
  Alpöge--Furman theorem by a Hilbert-space (Bessel) inequality plus
  BGSTB unconditional pair correlation (support $[-1,1]$); the key
  proposition is rebuilt exactly on $921$ synthetic conjugation-invariant
  multisets; $C_\eta \equiv R(\eta^2)$ (r267 functional) to
  $1.7\cdot 10^{-15}$, bound $2N - \lVert\cdot\rVert_{\mathrm{HS}}^2$
  $=$ A--F chain; $C_0 = 0.672500703679 = p^*$ (r627), $C_1 = 0.83625$;
  $Q = \eta^2 * \eta^2$ vanishes for $|\alpha| \ge 1$; under the PCC form
  factor $p(\lambda) = 0.6725 \to 0.996$ ($\lambda = \tfrac12 \to 3$).
  NO\_IMPORT unchanged.  AxiomProver Lean certificates: proposition
  unconditional, theorem modulo BGSTB Lemma 5 + RvM hypotheses.
  **r631L Lean-only (no probe).**
  Classification of the $7$ tracked `sorry`s (no closure):
  | Class | Location | Name |
  |---|---|---|
  | **R** (RH-core) | Canonical.lean:264 | `lstar_canonical` |
  | **R** | Canonical.lean:273 | `terminal_q_canonical` |
  | **T** blocked | Canonical.lean:396 | `pair_terminal_dictionary` |
  | **T** blocked | Source.lean:1008 | `mainWindow_iff_builtFromPrimeSource` |
  | **A** | Elementwise.lean:1589 | `arch_gauss_mellin_digamma_identity` |
  | **A** | ExternalBridges.lean:15641 | `standard_explicit_formula_identification` |
  | **A** | ExternalBridges.lean:15708 | `fullWeil_separates_offCritical_zeros` |
  Docstring: `GaborContourLimitRemainder` is PROVED
  (`gaborContourLimitRemainder_holds`, r576).  Census stays **7**.
  **r634L Lean-only (no probe).**
  `gabor_explicitFormula_pure` UNCONDITIONAL for admissible
  pure $F$ (coeffs $\langle 1,0,0\rangle$):
  `gaborZeroSide F = gaborPoleSide F - gaborPrimeComb F + gaborArchSide F`
  (both remainders theorems).  Sharpest live statement
  `gabor_primeSide_rational_criterion_iff_rh`:
  $(\forall a,\omega\in\mathbb{Q},\,a>0:\ 0\le$
  POLE $-$ PRIME $+$ ARCH of `pureGaborTest` $a\,\omega$)
  $\leftrightarrow$ `RiemannHypothesis`; axioms
  `propext` / `Classical.choice` / `Quot.sound`.
  Remaining EF brick: `GaborHatQuarticExplicitRemainder`
  (non-pure quartics only).  Census stays **7**.
  **r638L Lean-only (no probe).**
  `lake build RH` 3578/3578, 0 errors.  Sorry census
  **7 → 5**.  Retired two wrong-type asserting theorems
  to unasserted Props: `arch_gauss_mellin_digamma_identity`
  (overstrong exact quadrature quantifier) and
  `standard_explicit_formula_identification` ($2\Lambda/\sqrt{n}$
  vs $\Lambda(1+1/n)$ gauge mismatch).  Honest-contour
  identification stays proved.  Seven affected probes
  passed twice byte-identically.  No RH claim/status
  upgrade.  NO RH CLAIM.
  **r475-repair Lean-only (no probe).**
  Additive repair in
  `RH/SelectedArchErrorQuadraticRateClassical.lean`
  (238 lines; catalog `part_18`).
  `SelectedArchErrorQuadraticRate` (fixed
  `archRateConst` $=4.1259765625$) FALSIFIED in the
  small-support regime (`err`/`\Delta^2` $=8.0283458222$).
  Endpoint-kink defect proved exactly.
  `SelectedArchErrorQuadraticRateExists` ($\exists C(f)$)
  is the correct interface; tendsto consumer proved;
  `SelectedArchWeightedInterpolationEstimate` OPEN.
  $O(\Delta^2)$ rate itself not refuted (ratios $3.85$--$3.99$).
  `lake build RH` 3578/3578; five protected sorries
  unchanged.  NO RH CLAIM.

r544 scout and Path-A/B notes stand.  `GaborSeparationForAllZeros`
stays an unasserted Prop **[O]** (r612: asserting theorem
retired).  Tracked sorry census **9 → 8** at r581
(Source 1, Elementwise 1, Canonical 3, ExternalBridges 2,
GaborSeparation 1; GaborExplicitFormula 0); stayed **8**
through r605 (2026-09-02); **8 → 7** at r612
(GaborSeparation 0); **7 → 5** at r638L (two asserting
theorems retired, not proved).  Conditional reduction only.  Separation
stays **[O]**.  NO RH CLAIM.

## Folder guide

```
rh/
├── README.md            — this file
├── INVENTORY.json       — machine-readable register of every RH-relevant
│                          file (path, SHA-256, round, ledger IDs, status);
│                          pinned entries drive the drift detector
├── lean/                — Lean 4 formalization pilot (r267 recommendation)
│   ├── README.md        — setup, build, proved-vs-sorry status
│   ├── lean-toolchain, lakefile.toml
│   └── RH/
│       ├── Basic.lean     — abstract chain data (h/F/c/rho/D/tau/tau^aug)
│       ├── Recursion.lean — PROVED core identities (recursion ⇒ drain,
│       │                    bilinear identity, telescope, terminal
│       │                    equivalence, two-branch trivial direction)
│       ├── Inertia.lean   — matrix-theorem layer (v956/v958); since the
│       │                    r305 Lean round PROVED except the Jacobi
│       │                    inertia theorem crossing_budget: psd_base,
│       │                    positive_prefix_firewall (Sylvester
│       │                    criterion, both directions),
│       │                    sylvester_pullback, half_filling_boundary
│       │                    + a general PosDef layer (bordered Schur
│       │                    step, injective principal submatrix)
│       ├── Window.lean    — r273: concrete VonMangoldtWindow structure,
│       │                    derived Hankel/chain/Schur objects, honest
│       │                    opaque MainWindow predicate; wave 5: T4
│       │                    proved; wave 6: the canonical form
│       │                    lstar_subordination (lemma L*, the ONE
│       │                    remaining sorry of this file) + L* ⇒
│       │                    free-window PROVED (free_window_positivity
│       │                    is a corollary of L* since r305)
│       ├── Source.lean    — r310 SOURCE INTERFACE (reviewer plan §6.3):
│       │                    explicit PrimeWindowSpec (prime powers,
│       │                    anchor, mesh level), buildPrimeWindow with
│       │                    Real.log nodes + mathlib Λ weights,
│       │                    MainWindowExplicit; PROVED: nodes_injective,
│       │                    predefined_family, mesh_refinement_compatible
│       │                    (+ mesh_refinement_shrinks),
│       │                    cofinal_prime_windows,
│       │                    finite_forms_converge_to_weil (prime side,
│       │                    stabilization form),
│       │                    rational_window_approximates; r310b
│       │                    (reviewer plan §8): four-stage support
│       │                    chain (primePow_index_injective →
│       │                    nodes_injective → foldedWindow
│       │                    aggregation → support_nodup) + the four
│       │                    source theorems (source_exact,
│       │                    weights_nonnegative, support_canonical,
│       │                    refinement_compatible — all PROVED);
│       │                    ONE documented sorry: the opacity bridge,
│       │                    since r310b in reviewer target form
│       │                    mainWindow_iff_builtFromPrimeSource
│       │                    (mainWindow_explicit_bridge proved from it;
│       │                    r376: Alt-Last since C1, not a load-bearing
│       │                    hole — CanonicalWindow replaced MainWindow)
│       ├── Closure.lean   — r305 RECONSTRUCTION: LStar + TerminalPositive
│       │                    predicates, lstar_terminal_implies_master
│       │                    (PROVED: L* + terminal q<1 ⇒ master
│       │                    positivity via Schur bordering + principal
│       │                    submatrices); THE MASTER THEOREM
│       │                    augmented_prefix_positive now a COROLLARY
│       │                    (no own sorry); the terminal hole named
│       │                    terminal_positive_main (sorry)
│       ├── Open.lean      — ladder bookkeeping + measured kill lists
│       │                    (r273: the two false-universal open theorems
│       │                    removed, no sorry anymore)
│       ├── PairBound.lean — PROVED finite pair algebra of the r269/r271
│       │                    fixed form c2PAIR (block decomposition, pair
│       │                    triangle, level-2 refinement); the H5 margin
│       │                    law retyped as pair_margin_main (sorry, r273)
│       ├── DualResolvent.lean — r362/r373: finite-matrix L† ⟺ R† ≻ ½I.
│       │                    PROVED sorry-free since r373: A2/A3/A4/A5/
│       │                    A7-min plus the μ-ONB window bridge
│       │                    (RepresentsLEnsemble).  NO RH CLAIM
│       ├── Haynsworth.lean  — r373: two-rank cut (haynsworth_two_rank)
│       │                    and mixed J-form (haynsworth_mixed),
│       │                    sorry-free.  Does not assert census
│       │                    premises P1/P2 on windows.  NO RH CLAIM
│       ├── PivotCoordinate.lean — r380: five DCCXXXVII lemmas
│       │                    (rank-1 inertia + adaptive band proved;
│       │                    dual-Hankel complement and det K₂ named-
│       │                    decomposed; Jacobi synthesis proved).
│       │                    Zero sorry; census stays 5.  NO RH CLAIM
│       ├── FlankEntry.lean — r384: R382 entry lemma kernel-anchor
│       │                    (pair energy, ℚ toys, h₀/h₁, Christoffel
│       │                    k=0,1 PROVED; FlankEntryPrefix and
│       │                    ChristoffelPivotBound named).  Zero sorry;
│       │                    census stays 5.  NO RH CLAIM
│       ├── Selected.lean  — r397: exact real domain + minimal
│       │                    quantifier (RealCanonicalWindow,
│       │                    ExactFold/ExactPrimeSource/ExactArch/
│       │                    ExactBorder/ExactBudget total;
│       │                    a_k=2^k, m_k=k·2^{⌊√k⌋}−1 with
│       │                    Δ_k=2^{−r_k}·log 2, a_k→∞, Δ_k→0
│       │                    PROVED; weil_nonneg_of_selected_windows
│       │                    (selected windows; r463 mincut fold in
│       │                    FaithfulFold); r397 named Prop
│       │                    selected_augDualResolvent_gt_half is the
│       │                    stronger alternative since r430).
│       │                    Zero sorry; census stays 5.  NO RH CLAIM
│       ├── InnerBridges.lean — r464/r470/r473: finite PSD half proved;
│       │                    SelectedReadQuadraticRepresentation
│       │                    retained; r470 obstruction sealed;
│       │                    r473 poly-class bridge proved
│       │                    (selectedACapPsdImpliesPolynomialReads)
│       │                    plus named approx and arch-gap identity.
│       │                    Zero sorry; live sorry census 5
│       │                    after r638L.  NO RH CLAIM
│       ├── SelectedArchErrorQuadraticRateClassical.lean —
│       │                    r475-repair: fixed archRateConst
│       │                    FALSIFIED (8.0283>4.126);
│       │                    Exists-rate OPEN; tendsto
│       │                    consumer proved.  NO RH CLAIM
│       ├── FrequentlySelected.lean — r430/r434/r463: semidefinite + FREQ
│       │                    (Rdagger_ge_half_iff_augmented_posSemidef;
│       │                    internal_weil_nonneg_of_frequently_selected;
│       │                    density and
│       │                    mean-value PROVED; named mincut
│       │                    frequently_selected_augDualResolvent_ge_half;
│       │                    r434: real-window Loewner PROVED,
│       │                    SelectedSemidefImpliesPlainReads theorem
│       │                    of SelectedACapPsdImpliesPlainReads;
│       │                    terminal_q_canonical OFF PATH; r463: uses
│       │                    FaithfulFold for the comb object).
│       │                    Zero sorry in-file; live sorry census 5
│       │                    after r638L (ExternalBridges 1).  NO RH CLAIM
│       ├── FaithfulFold.lean — r463: production-faithful comb fold
│       │                    (tent lags, L=2(m+1)-2, circulant spectral
│       │                    density, grid fold, sign split; k=5/9/10
│       │                    pins match lean_fidelity_probe).  Zero sorry;
│       │                    NO RH CLAIM
│       ├── ExternalBridges.lean — r463/r487/r489/r491 plus
│       │                    r517–r538 Lean-only outer-bridge
│       │                    campaign.  Theorems (not OPEN):
│       │                    fullWeil_dyadic_sample_convergence,
│       │                    gridPoleHatIntegralIdentity,
│       │                    fullWeil_channel_continuity;
│       │                    contourIdentityLimitAlongGaps,
│       │                    hat_fourier_inversion,
│       │                    rightVerticalIntegral_eq_prime_sum;
│       │                    r534: contourExplicitFormula_honest,
│       │                    leftEdgeArchIntegral_eq_explicit_factor_integral,
│       │                    HonestContourExplicitFormulaIdentification;
│       │                    r538: fullWeilFormHonest,
│       │                    standard_explicit_formula_identification_honest
│       │                    (honest identification CLOSED, sorry-free,
│       │                    conditional wrapper
│       │                    honest_weil_criterion_to_mathlib_rh).
│       │                    Remaining external sorry [O]:
│       │                    fullWeil_separates_offCritical_zeros
│       │                    (r541 Gabor GO precheck; certified
│       │                    numerical precheck, Lean campaign
│       │                    licensed, no claim).
│       │                    Historical unasserted Prop (r638L:
│       │                    asserting theorem retired, not
│       │                    proved; $2\Lambda/\sqrt{n}$ vs
│       │                    $\Lambda(1+1/n)$ gauge mismatch):
│       │                    standard_explicit_formula_identification.
│       │                    Compact-carrier census 5 (external 1)
│       │                    after r638L; Gabor lane is a
│       │                    separate module.  NO RH CLAIM
│       ├── ZeroIncrement.lean — r546: zeta_unit_increment +
│       │                    gaborIncrementBound_holds sorry-free
│       │                    (constant 2*zetaZerosInDiskCardBoundInner).
│       │                    Path A live; Trudgian Path B inactive.
│       │                    NO RH CLAIM
│       ├── GaborSeparation.lean — r542/r547/r550/r558/r600:
│       │                    Gabor class; live reduction
│       │                    gabor_zeroSide_inputs_to_mathlib_rh
│       │                    (hpos* on gaborZeroSide).
│       │                    Historical gabor_inputs_to_mathlib_rh
│       │                    VACUOUS (r600).  r558 split
│       │                    Precheck/ForAllZeros.  r610/r612:
│       │                    GaborLowHeightZeroFree unasserted;
│       │                    asserting gabor_separationForAllZeros
│       │                    retired (Prop retained [O]).
│       │                    Census 8 (this file carries 1;
│       │                    r600, 2026-09-02).
│       │                    NO RH CLAIM
│       ├── GaborHatAnalytic.lean — r555/r587: entirety,
│       │                    FE-symmetry, three-lobe, strip
│       │                    Gauss; r587 poly-in-t majorant
│       │                    theorem.  NO RH CLAIM
│       ├── GaborIntegral.lean — r543: pureGaborHat integral
│       │                    representation sorry-free (Mathlib
│       │                    integral_cexp_quadratic).  NO RH CLAIM
│       ├── GaborInequality.lean — r544/r552: sorry-free symbolic
│       │                    kernel + alias
│       │                    gauss_density_transfer_binMax.
│       │                    Does not discharge the named input.
│       │                    NO RH CLAIM
│       ├── GaborThetaBound.lean — r552: discrete theta-lobe
│       │                    bound sorry-free (center-independent
│       │                    Theta_lobe).  Continuous transfer
│       │                    remains open.  NO RH CLAIM
│       ├── GaborZeroSummable.lean — r557/r587:
│       │                    summable_gaborHat_over_zeros
│       │                    + quartic summability theorems.
│       │                    NO RH CLAIM
│       ├── GaborHorizontalEdges.lean — r557:
│       │                    gabor_horizontal_edges_tendsto_zero
│       │                    sorry-free.  NO RH CLAIM
│       ├── GaborContourResidue.lean — r557/r631L:
│       │                    gabor_contour_identity_fixed_T
│       │                    sorry-free; GaborContourLimitRemainder
│       │                    PROVED (r576).  NO RH CLAIM
│       ├── GaborVertical.lean — r564/r581: right-vertical prime
│       │                    sum + hat Fourier inversion sorry-free.
│       │                    GaborVerticalArithmeticRemainder
│       │                    proved (r581).  NO RH CLAIM
│       ├── GaborExplicitFormula.lean — r558/r564/r581/r634L:
│       │                    of_remainders / of_parts sorry-free.
│       │                    Pure-class EF unconditional
│       │                    (gabor_explicitFormula_pure, r634L);
│       │                    remaining brick quartic remainder.
│       │                    220 lines, 0 sorry.  NO RH CLAIM
│       ├── GaborLeftVertical.lean — r570: left vertical
│       │                    closed (FE + dual L-series).
│       │                    NO RH CLAIM
│       ├── GaborAutocorrelation.lean — r572: ACF closed
│       │                    form + half-comb sorry-free.
│       │                    NO RH CLAIM
│       ├── GaborVerticalLimit.lean — r576:
│       │                    gaborContourVerticalLimit_holds
│       │                    sorry-free.  NO RH CLAIM
│       ├── GaborArchDigamma.lean — r577: chi'/chi on the
│       │                    critical line sorry-free.
│       │                    NO RH CLAIM
│       ├── GaborArchContour.lean — r578/r581: pairing +
│       │                    fixed-T residue; T->inf glue
│       │                    theorem.  NO RH CLAIM
│       ├── GaborDominance.lean — r562/r568/r571: canonical
│       │                    isolation-shrink; GaborDominanceBound
│       │                    is a theorem.  NO RH CLAIM
│       ├── GaborDominanceProof.lean — r569: T_gap=0 +
│       │                    host Q<0 under a0.  NO RH CLAIM
│       ├── GaborDominanceAssembly.lean — r571: packing +
│       │                    budget assembly sorry-free.
│       │                    NO RH CLAIM
│       ├── GaborDominanceLog.lean — r574/r575:
│       │                    GaborDominanceBoundLog theorem.
│       │                    r573 STATEMENT_WEAKENED
│       │                    (finite proxy).  NO RH CLAIM
│       ├── GaborSpectralBridge.lean — r579–r589:
│       │                    log-occupancy transfer; tsum<=
│       │                    Closed theorem; unrestricted
│       │                    On/Off-split theorem; weighted
│       │                    Bridge-6 identification theorem
│       │                    (FD, weight 4; zeta != 0 on
│       │                    (0,1)); r589 window->BoundLog2
│       │                    hypotheses.  NO RH CLAIM
│       ├── GaborFEMultiplicity.lean — r582/r585: FE
│       │                    multiplicity m(z)=m(1-z) and
│       │                    m(bar z)=m(z) on the open strip
│       │                    + weighted truncation
│       │                    compliance theorem.  NO RH CLAIM
│       ├── GaborDominanceLog2.lean — r582/r583/r589:
│       │                    GaborDominanceBoundLog2 theorem
│       │                    (finite/conditional proxy);
│       │                    r589 window->BoundLog2 bridge
│       │                    theorem.  NO RH CLAIM
│       ├── GaborArithmeticSeparator.lean — r590:
│       │                    existential arithmetic
│       │                    endpoint; parallel Mathlib
│       │                    chain without scalingGaborTest.
│       │                    r591: fixed-packet cofinal
│       │                    only with extremality gap.
│       │                    r605A: pure iff takes hsep
│       │                    (OVERSPECIFIED).  NO RH CLAIM
│       ├── GaborExposedOrbit.lean — r605B+C:
│       │                    sorry-free exposed-orbit
│       │                    separator; unconditional
│       │                    zero-side iff on the pure
│       │                    (a,ω) family.  r634L adds the
│       │                    prime-side rational criterion.
│       │                    Positivity of gaborZeroSide
│       │                    remains open.  NOT an RH proof.
│       │                    Census at landing 8; live 7
│       │                    after r612.  NO RH CLAIM
│       ├── GaborCountableCriterion.lean — r612/r612C/r634L:
│       │                    rational-packet zero-side iff
│       │                    RH, unconditional
│       │                    (gaborZeroSideContinuous_holds);
│       │                    r634L prime-side rational
│       │                    criterion
│       │                    gabor_primeSide_rational_criterion_iff_rh
│       │                    (RH ⇔ ∀ rational (a,ω):
│       │                    POLE − PRIME + ARCH ≥ 0).
│       │                    Census 8 → 7 at r612;
│       │                    stays 7 at r634L (568 lines).
│       │                    NO RH CLAIM
│       ├── CoxeterCompletion.lean — r617L:
│       │                    Φ₃₀ identities and Tr C = −1
│       │                    sorry-free; Euler product not
│       │                    formalized.  Census stays 7.
│       │                    NO RH CLAIM
│       ├── PrimeLogIndependence.lean — r617L:
│       │                    ℚ-linear independence of
│       │                    {log p} (Mathlib had no such
│       │                    lemma) + log-ratio irrational.
│       │                    Module count 54 → 56.
│       │                    Census stays 7.  NO RH CLAIM
│       ├── GaborOuterTail.lean — r593/r594: outer-tail
│       │                    theorem (strip width beats
│       │                    window distance; tsum<=exp
│       │                    and tail<eps*E).  NO RH CLAIM
│       ├── GaborWindowGlue.lean — r595: three-term
│       │                    glue + per-T checkpoint;
│       │                    named gap UniformDelta.
│       │                    NO RH CLAIM
│       ├── GaborAnchoredWitness.lean — r596–r600:
│       │                    log-glue theorem; zeroSide<0
│       │                    at own packet; Cover residual
│       │                    (ordinate isolation);
│       │                    SpectralToArithmetic = proved
│       │                    pole-sign lemma (NOT RH-core);
│       │                    RH-core = hpos*; r612 retired
│       │                    the asserting theorem
│       │                    gabor_separationForAllZeros
│       │                    (Prop retained unasserted);
│       │                    WitnessExists NOT asserted.
│       │                    NO RH CLAIM
│       ├── OneDefect.lean — r406: general one-defect absorption
│       │                    (indNeg_sub_rankOne_le_one,
│       │                    oneDefect_update_posDef_iff,
│       │                    posDef_of_contractive_lift,
│       │                    cMin_normSq PROVED; Woodbury built).
│       │                    Independent of R404/R405.  Zero sorry;
│       │                    census stays 5.  NO RH CLAIM
│       ├── GraphResolvent.lean — r412: graph-resolvent dictionary
│       │                    (R=C(I+C)^{-1}, Möbius inertia,
│       │                    energy-split contraction, zero-defect
│       │                    R† lift PROVED; named Prop
│       │                    GraphResolventIsLEnsembleInv).
│       │                    Zero sorry; census stays 5.  NO RH CLAIM
│       ├── EdgeBalance.lean — r426: edge-balance chain
│       │                    (Woodbury-sch corollary of OneDefect,
│       │                    3×3 chart trichotomy, τ²-separator,
│       │                    den formula + γ-bridge PROVED; named
│       │                    Props BorderIsMuParseval /
│       │                    BorderLoewnerLeS / QNLtOne).
│       │                    Zero sorry; census stays 5.  NO RH CLAIM
│       └── Counterexamples.lean — r273 reviewer guards: machine-checked
│                            refutations of the three pre-r273 universal
│                            forms (proved, no sorry)
├── paper/
│   └── rh_program.tex   — the focused RH-program paper (English,
│                          self-contained, builds with pdflatex)
├── problem/
│   ├── lstar_problem.tex(+pdf) — the missing lemma L* as a fully
│   │                     standalone problem statement for external
│   │                     mathematicians (no project vocabulary)
│   ├── rdagger_saturation.tex(+pdf) — specialist dossier on the
│   │                     bordered dual resolvent R† (definition,
│   │                     duality formulae, critical 3×3, saturation
│   │                     edge, exponent, relative error form; since
│   │                     r367–r373 the PRIMARY question is the
│   │                     minimal inertia form (P1)+(P2); r412
│   │                     records the graph-resolvent coordinates
│   │                     of (P1); r426 records the edge-balance
│   │                     chain (eight identities, branch map,
│   │                     floor, two open limits); r427–r429 plus
│   │                     DCCXCVII add the two cancellation cores,
│   │                     the campaign-audit table, and the open
│   │                     Potapov program (S_{≤1} / S_0, Redheffer
│   │                     pivot, semidefinite + frequently
│   │                     quantifiers).  Refutation table: 28 named
│   │                     closed routes.  The older RHP/BKMM
│   │                     saturation question is the stronger
│   │                     variant).
│   │                     No RH claim
│   ├── medcap_lemma.tex(+pdf) — proof attempt for the r361
│   │                     MED-CAP inequality med_i ≤ (8/3) sep_i
│   │                     (SEP-SATZ proved; tiling reduction;
│   │                     C2 obstruction named).  No RH claim
│   ├── xn_invariant.tex(+pdf) — r364: pairing theorem for X_n
│   │                     (n=1 only odd tail; unique sep=3/2 is
│   │                     edge (1,2); remainder V2 named).  No RH claim
│   ├── v2_regularity.tex(+pdf) — r365: V2 anatomy + hydra freeze
│   │                     (REGRESS_DETECTED; T2' modulo V2).  No RH claim
│   ├── v2_lemma_v3.tex(+pdf) — r374: V2 reduced to V3'
│   │                     (Wronskian step + contrast; T2' modulo
│   │                     V3').  No RH claim
│   ├── p2_lemma_proof.tex(+pdf) — r375: P2 source expansion
│   │                     (factorization SATZ; reduced to the
│   │                     dressed overlap γ > (1+ε)λ₋).  No RH claim
│   ├── postcap_pivots.tex(+pdf) — r377: P2-POSTCAP + P1-SINGLE-DEFECT
│   │                     in source pivot coordinates (universal
│   │                     post-cap alternation REFUTED; prefix
│   │                     inertia CENSUS).  No RH claim
│   ├── compose_lemma.tex(+pdf) — r378: COMPOSE reduced to
│   │                     M3≤φ(m) ∧ (R)(L)(Z) ⇒ |Z|<M; H5 is
│   │                     a sister route; α* 0.888/0.908 are
│   │                     slope-proxies.  No RH claim
│   ├── v3prime_proof.tex(+pdf) — r379: V3' reduced to G_ε
│   │                     (cosine-grid mesh SATZ; last-12
│   │                     |γ-1/4|≤1/16).  No RH claim
│   ├── g_eps_lemma.tex(+pdf) — r381: G_ε reduced to
│   │                     (C_ε, R₂); FO formula SATZ;
│   │                     L^∞ too crude; R₂ not dominated.
│   │                     No RH claim
│   ├── pivot_entry_lemma.tex(+pdf) — r382: entry of the
│   │                     pivot band reduced to n₀=⌊2N/5⌋
│   │                     under (2/3)-flank; L² remainder
│   │                     named for n₀=N−1.  No RH claim
│   ├── compose_premises.tex(+pdf) — r383: COMPOSE⁻ inputs
│   │                     (R)(L)(Z).  Fejér/r298/L² SATZ;
│   │                     (R)(L) census-reduced; (Z) reduced
│   │                     on FRAME-A, refuted on χ.  No RH claim
│   ├── christoffel_quiet.tex(+pdf) — r385: Christoffel
│   │                     quietness reduced to (Δ, C);
│   │                     Chebyshev sampling SATZ at trivial
│   │                     Weyl; Q<1 is not the floor plate.
│   │                     No RH claim
│   ├── compose_premises2.tex(+pdf) — r386: living (Z')
│   │                     Z₀'=21/25; death channel census;
│   │                     cofinal R₀ reduced to B(ω+β,ω+β)≤KD.
│   │                     No RH claim
│   ├── coherence_assist.tex(+pdf) — r387: coherence
│   │                     assist reduced to signed μ-CD
│   │                     off-diagonal; Gershgorin too crude;
│   │                     two-period is a global AP.
│   │                     No RH claim
│   ├── delta_deformation.tex(+pdf) — r388: Δ-deformation
│   │                     reduced; osc-Geronimus does not
│   │                     close C_ε; R2 on μ-ref not dominated.
│   │                     No RH claim
│   ├── weyl_energy.tex(+pdf) — r389: Weyl energy of
│   │                     cancellation reduced; Parseval SATZ;
│   │                     FO^T closes at QM; assist/Z_loc remain.
│   │                     No RH claim
│   ├── g_eps_mu.tex(+pdf) — r390: G_ε^μ reduced to
│   │                     F_ε ∧ W_ε; occupied-Fejér already
│   │                     in |γ−1/4|; not construction-pure.
│   │                     No RH claim
│   ├── construction_rl.tex(+pdf) — r391: construction-pure
│   │                     (R)(L) reduced to the white-block
│   │                     class; block-Gershgorin refuted.
│   │                     No RH claim
│   ├── deletion_transform.tex(+pdf) — r392: Uvarov
│   │                     deletion algebra SATZ; F_eps not
│   │                     from rho_AP; Assist is Sign-Schur.
│   │                     No RH claim
│   ├── tau_field.tex(+pdf) — r393: d2 log tau under F1;
│   │                     cluster/rank-1 SATZ; F1 not sufficient.
│   │                     No RH claim
│   ├── sign_schur.tex(+pdf) — r394: Dirichlet zones SATZ;
│   │                     checkerboard/M-matrix REFUTED;
│   │                     Assist rest is Weyl energy.
│   │                     No RH claim
│   ├── three_gap_mask.tex(+pdf) — r395: Steinhaus +
│   │                     log-local SATZ; Drei-Gap-Maske
│   │                     REFUTED; occupation is a 2-3
│   │                     histogram with a sparse tail.
│   │                     No RH claim
│   ├── isolation_lemma.tex(+pdf) — r396: pair census
│   │                     SATZ (folded small integers);
│   │                     Isolation lemma REFUTED; pair
│   │                     density is a shadow of the 2-3
│   │                     histogram.  No RH claim
│   ├── high_moment_inertia.tex(+pdf) — r398: high-moment
│   │                     kill-test of P1; KILL_FAIL
│   │                     (cluster at 1/2).  No RH claim
│   ├── source_weyl_energy.tex(+pdf) — r399: source-pure
│   │                     Weyl energy; representation SATZ;
│   │                     decay REFUTED (QM, grows);
│   │                     bound circular if forced.  No RH claim
│   ├── bulk_one_defect.tex(+pdf) — r400: threshold/phase
│   │                     frame inequality; FORM_T REFUTED
│   │                     (rank-1); FORM_P REFUTED (phases);
│   │                     dead chi P1 holds.  No RH claim
│   ├── edge_signature.tex(+pdf) — r401: augmented 3x3
│   │                     edge signature; reconstruction SATZ;
│   │                     model lemma SATZ; compact K census;
│   │                     dead chi sch>0.  No RH claim
│   ├── p1_construction.tex(+pdf) — r403: P1 construction
│   │                     class; interlacing/PSD/scale SATZ;
│   │                     CLASS REFUTED (weight-rand on the
│   │                     frozen mask).  No RH claim
│   ├── one_defect_gram.tex(+pdf) — r404: source one-defect
│   │                     Gram; Loewner/addition/fold SATZ;
│   │                     class 3 not reached (Cholesky
│   │                     tautology).  No RH claim
│   ├── edge_contractive_lift.tex(+pdf) — r405: edge
│   │                     contractive lift; Euler/disk/
│   │                     Woodbury SATZ; EDGE_LIFT_PARTIAL
│   │                     (border=tail REFUTED; dead overflow
│   │                     REFUTED).  No RH claim
│   ├── dual_intertwiner.tex(+pdf) — r407: dual
│   │                     intertwiner $R=C(I+C)^{-1}$; FL
│   │                     dictionary SATZ; P1 $\iff\lambda_2(C)\ge 1$;
│   │                     $\nu$-rank not one.  No RH claim
│   ├── c_threshold.tex(+pdf) — r408: C-threshold /
│   │                     sampling; Nyquist-at-1/2 REFUTED;
│   │                     source nC<=1 CENSUS.  No RH claim
│   ├── borodin_birkhoff_intertwiner.tex(+pdf) — r409:
│   │                     source-pure Birkhoff CLS graph
│   │                     identity SATZ; Phi literal REFUTED;
│   │                     SEQ n_neg<=1 CENSUS.  No RH claim
│   ├── hole_nyquist.tex(+pdf) — r410: hole-Nyquist
│   │                     defect; test-poly REFUTED;
│   │                     Fourier/Bernstein REFUTED;
│   │                     dmin CENSUS; seq birth REDUCED.
│   │                     No RH claim
│   ├── threshold_identity.tex(+pdf) — r411: energy
│   │                     split SATZ; exact PD
│   │                     saturation REFUTED.  No RH claim
│   ├── hole_top_mode.tex(+pdf) — r413: hole top
│   │                     OP formula SATZ; HTM primary
│   │                     test REFUTED on MAIN; QD
│   │                     REFUTED.  No RH claim
│   ├── top_mode_edge.tex(+pdf) — r415: chart identity
│   │                     -sch=beta-alpha SATZ; v_top
│   │                     is not the bulk defect.  No RH claim
│   ├── source_potapov.tex(+pdf) — r431: source Potapov
│   │                     factor; Redheffer = Cauchy SATZ;
│   │                     Pick ≅ I-T*T REFUTED.
│   │                     SOURCE_FACTOR_NOT_FOUND.  No RH claim
│   ├── r431_audit.tex(+pdf) — r431-AUDIT: non-commuting
│   │                     Blaschke–Potapov + Redheffer star
│   │                     still S_0; numbers reproduced.
│   │                     CONFIRMED.  No RH claim
│   ├── p1_overload.tex(+pdf) — r435: n_-(A0)<=1 is a
│   │                     crossing budget.  No RH claim
│   ├── p2_determinant.tex(+pdf) — r436: reverse-CS
│   │                     identity SATZ; coarse lmax
│   │                     killed at kz46.  No RH claim
│   ├── evolutionary_certificate.tex(+pdf) — r438:
│   │                     GP/NNLS/cut search NOT_FOUND.
│   │                     No RH claim
│   ├── residual_loewner.tex(+pdf) — r439: D0 disp
│   │                     rank 2 SATZ; S0=K^{-1} SATZ;
│   │                     B1 Bez(P_Y,Q) miss.  No RH claim
│   ├── mean_tau_index.tex(+pdf) — r440: T1/T2/MI2 SATZ;
│   │                     s=1 collar is the contour boss;
│   │                     selected+core mean 0<1.  No RH claim
│   ├── diag_lifts_loewner.tex(+pdf) — r441: Gram SATZ;
│   │                     lift count SATZ; d_min theorem
│   │                     REFUTED.  REDUZIERT.  No RH claim
│   ├── block_mean.tex(+pdf) — r442: kappa=1{q>1} SATZ;
│   │                     unsigned majorant REFUTED;
│   │                     Selected living; mean OPEN.
│   │                     REDUZIERT.  No RH claim
│   ├── delta_floor.tex(+pdf) — r443: chart SATZ;
│   │                     slice floor preferred;
│   │                     kz16 below; liminf OPEN.
│   │                     REDUZIERT.  No RH claim
│   ├── signed_border_mean.tex(+pdf) — r444: triple-sum
│   │                     SATZ; pole not carrier; diagonal
│   │                     overflows; bound ZIRKULAER.
│   │                     No RH claim
│   ├── deep_builder.tex(+pdf) — r445: unused Lanczos
│   │                     hotspot; k=8 live pin;
│   │                     k=10/11/12 not ABD-living;
│   │                     slice floor with live k=8.
│   │                     INFRA_UNLOCKED.  No RH claim
│   ├── deep_abd.tex(+pdf) — r446: k=10/11/12 ABD
│   │                     breaks are REAL; mesh does
│   │                     not repair; last live kz=136.
│   │                     COFINAL_ABD_OPEN.  No RH claim
│   ├── exact_atom.tex(+pdf) — r447: k=10 EXACT_DEAD;
│   │                     atoms ulp-close; this 2^k
│   │                     family does not feed frequently.
│   │                     No RH claim
│   ├── exact_band.tex(+pdf) — r448: NOT_COFINAL;
│   │                     2^k commensurability refuted;
│   │                     kz197 zeta-chain death;
│   │                     next-odd fails.  No RH claim
│   ├── flip_vs_stab.tex(+pdf) — r449: TAIL_ONLY;
│   │                     flips past n_stab; prefix
│   │                     R^dagger lives.  No RH claim
│   ├── prefix_mincut.tex(+pdf) — r450: M2_UNDECIDED;
│   │                     n_stab-compression named;
│   │                     living split; chi prefix
│   │                     lives.  No RH claim
│   ├── nstab_transition.tex(+pdf) — r451: TRANSITION_SMOOTH;
│   │                     RES_MISMATCH; PREFIX_Q_PLATEAU;
│   │                     n_stab is a sufficient cut.
│   │                     No RH claim
│   ├── plateau_theorem.tex(+pdf) — r452: PLATEAU_IDENTITY_PROVED;
│   │                     QSTAR_UNDECIDED;
│   │                     q_* = M_d/(M_d+5/7).
│   │                     No RH claim
│   ├── border_mass.tex(+pdf) — r453: BOUND_PROVED;
│   │                     MASS_CLASSICAL_REDUCED_GROWING;
│   │                     RACE_WON.
│   │                     No RH claim
│   ├── limit_object.tex(+pdf) — r454: LIMIT_CLASSICAL;
│   │                     LIMITCHAIN_ALIVE_200;
│   │                     CHAIN_DOCUMENTED.
│   │                     No RH claim
│   ├── arch_chain.tex(+pdf) — r455: L3_PROVED;
│   │                     L1_PNT_SUFFICIENT;
│   │                     CHAIN_MAPPED.
│   │                     No RH claim
│   ├── vacuity_redteam.tex(+pdf) — r456: VACUOUS_CONFIRMED;
│   │                     prefix prime-blind; Iff.rfl naming.
│   │                     No RH claim
│   ├── jp_increment.tex(+pdf) — r457: INCREMENT_DRIFT;
│   │                     RACE_EATS_K10;
│   │                     LEMMA_REDUCED.
│   │                     No RH claim
│   ├── cofinal_family.tex(+pdf) — r458: FAMILY_CANDIDATE;
│   │                     TABLE_CAP_ARTEFACT;
│   │                     residual kz137.  No RH claim
│   ├── fullcomb_cleanup.tex(+pdf) — r459: RACE_TREND_BROKEN;
│   │                     LEANFAM_EXACT_ALIVE(12);
│   │                     KZ137_OUTSIDE_MINCUT.  No RH claim
│   ├── octave_renorm.tex(+pdf) — r468: OCTAVE_NOT_CAUCHY;
│   │                     EDGE_TWO_POINTS;
│   │                     REDUCTION_ALIAS.  No RH claim
│   ├── correlation_wall_judgment.tex(+pdf) — r469:
│   │                     U1 INTERNALLY_EXHAUSTED;
│   │                     U3 REDIRECT_TO_FIXED_L.  No RH claim
│   ├── quadrep.tex(+pdf) — r470: OBSTRUCTION_SEALED;
│   │                     F1(i) channel map; k=5 signed/rank
│   │                     Hessian witness.  No RH claim
│   ├── classical_cert.tex(+pdf) — r471: GRID_CERTIFIED
│   │                     (L_max=2.7726); dictionary-free
│   │                     Guinand--Weil grid family; F2b open.
│   │                     No RH claim
│   ├── modulus_upgrade.tex(+pdf) — r474: PARTIAL;
│   │                     F2b lemmas proved; mu-omega SHORT
│   │                     at every L including YB.  No RH claim
│   ├── extraction_joint.tex(+pdf) — r473: ARTEFACT +
│   │                     POLY_BRIDGE_PROVED; Q>0>fullRead
│   │                     at k=5; poly-class A_cap bridge.
│   │                     No RH claim
│   ├── arch_rate.tex(+pdf) — r475: IDENTITY_ISOLATED +
│   │                     RATE_O_DELTA2 (numeric
│   │                     large-support); fixed
│   │                     archRateConst FALSIFIED
│   │                     (8.0283>4.126, r475-repair);
│   │                     Exists C(f) OPEN.  No RH claim
│   ├── crossterm.tex(+pdf) — r476: UNCONDITIONAL
│   │                     (L_max=2.7726) on the first
│   │                     Dirichlet H^2 ball; YB gate PASS.
│   │                     Not lambda_*.  No RH claim
│   ├── highmode.tex(+pdf) — r477: ARCHITECTURE_STANDS
│   │                     (0.3,0.8,1.0); t0+Schur schema;
│   │                     not lambda_*.  No RH claim
│   ├── endtoend_fixedl.tex(+pdf) — r478: PARTIAL
│   │                     (0.3-even-5x5-PD|tail-Schur);
│   │                     block SATZ, tail OPEN.  No RH claim
│   ├── lambdastar03.tex(+pdf) — r479: REDUCED
│   │                     (kappa_high<=1.79e-2 at t*=8,N=5);
│   │                     not lambda_*.  No RH claim
│   ├── kappa_high.tex(+pdf) — r480: REDUCED
│   │                     (refined-Schur; crude-kappa_high
│   │                     killed@0.30); not lambda_*.  No RH claim
│   ├── schur_cert.tex(+pdf) — r481: REDUCED
│   │                     (interval-FT+IBP-tail);
│   │                     not lambda_*.  No RH claim
│   ├── carleson_edgeband.tex(+pdf) — r482: STUCK
│   ├── filon_enclosure.tex(+pdf) — r483: REDUCED
│   ├── block_completion.tex(+pdf) — r484: STUCK
│   ├── weighted_schur.tex(+pdf) — r485: REDUCED
│   ├── woodbury_minf.tex(+pdf) — r486: REDUCED
│   ├── resolvent_solve.tex(+pdf) — r488: REDUCED
│   │                     (R-not-coercive; s=0.05
│   │                     G-cert-N5-BS=0.994;
│   │                     operator-R-gap-open);
│   │                     not lambda_*.  No RH claim
│   ├── keystone_judgment.tex(+pdf) — r492:
│   │                     U1 IDEA_NAMED(kernel-Loewner) /
│   │                     U2 PROCEED_UNDER_BUDGET /
│   │                     U3 REDIRECT_TO_KERNEL_LANE;
│   │                     adjudication only, no pin.
│   │                     No RH claim
│   ├── kernel_loewner.tex(+pdf) — r494:
│   │                     PROVED(c=2.1000e-3);
│   │                     x-space Loewner minorant +
│   │                     n=401 exact-HS finite section;
│   │                     operator floor, not Galerkin.
│   │                     No RH claim
│   ├── kernel_redteam.tex(+pdf) — r495:
│   │                     CONFIRMED(c=2.1000e-3);
│   │                     independent digamma, rational boundary,
│   │                     false-world, CC/HS off-space audit.
│   │                     No RH claim
│   ├── kernel_loewner08.tex(+pdf) — r496:
│   │                     NO_GO(kernel-Loewner-compact-tail@L=0.8);
│   │                     G1 pass, G2/G3 no-go
│   │                     (section -1.6107e-4, 3xHS 27.367,
│   │                     prime off-block 0.9395).
│   │                     Method no-go only.  No RH claim
│   ├── l08_judgment.tex(+pdf) — r502:
│   │                     U1 BLOCKED(no-certifiable-gap@L>=0.45) /
│   │                     U2 LADDER_RESTS_REDIRECT_TO_BRIDGE_LANE /
│   │                     U3 ANTI_LIST_EXTENDED;
│   │                     lambda_*(0.8) <= 1.8170e-14 witnessed,
│   │                     x-space + spectral bracket;
│   │                     ceiling ladder + 4 calibrated kills.
│   │                     Upper bound, NOT anti-RH.  No RH claim
│   ├── operator_residual.tex(+pdf) — r490: STUCK
│   │                     (off/s=5.86-eats-1000x;
│   │                     GL-tiny-not-the-certificate)
│   │                     +FINAL_CHECKPOINT;
│   │                     not lambda_*.  No RH claim
│   │                     (enemy-3dim-BS<1; Q_E-Higham;
│   │                     operator-Rinv-open);
│   │                     not lambda_*.  No RH claim
│   │                     (A-GO; finite-S_w-PD;
│   │                     operator-M_inf-open)+CHECKPOINT;
│   │                     not lambda_*.  No RH claim
│   │                     (20x-drop-falsified;
│   │                     jets>=10 garbage; QR-IBP kills S);
│   │                     not lambda_*.  No RH claim
│   │                     (finite-S-interval-PD;
│   │                     leftover-C-HS vs budget);
│   │                     not lambda_*.  No RH claim
│   │                     (SR_FAILS_FINITE_CENSUS;
│   │                     large-sieve=TARGET);
│   │                     not lambda_*.  No RH claim
│   ├── race_proof.tex(+pdf) — r460: PARTIAL;
│   │                     spectral reduction proved; norm route
│   │                     refuted; spectral-overlap gap open.
│   │                     No RH claim
│   ├── narrowband_weil.tex(+pdf) — r461: FORK_SHARPENED;
│   │                     Lean endpoint mapped to cofinal
│   │                     compact-window Weil positivity.
│   │                     No RH claim
│   ├── verify_lstar_instance.py — machine check that the standalone
│   │                     L* definition IS the campaign object
│   ├── verify_medcap_steps.py — machine check of every numbered
│   │                     lemma in medcap_lemma.tex (11/11)
│   ├── verify_xn_steps.py — machine check of xn_invariant.tex
│   │                     (12/12, XN STEPS VERIFIED)
│   ├── verify_v2_steps.py — machine check of v2_regularity.tex
│   │                     (12/12, V2 STEPS VERIFIED)
│   ├── verify_v2_lemma.py — machine check of v2_lemma_v3.tex
│   │                     (16/16, V2 LEMMA V3 VERIFIED)
│   ├── verify_p2_steps.py — machine check of p2_lemma_proof.tex
│   │                     (12/12, P2 STEPS VERIFIED)
│   ├── verify_postcap_steps.py — machine check of
│   │                     postcap_pivots.tex (16/16,
│   │                     POSTCAP STEPS VERIFIED)
│   ├── verify_compose_lemma.py — machine check of
│                         compose_lemma.tex (15/15,
│                         COMPOSE LEMMA VERIFIED)
│   ├── verify_v3prime.py — machine check of
│                         v3prime_proof.tex (17/17,
│                         V3PRIME LEMMA VERIFIED)
│   ├── verify_g_eps.py — machine check of
│                         g_eps_lemma.tex (13/13,
│                         G_EPS LEMMA VERIFIED)
│   ├── verify_pivot_entry.py — machine check of
│                         pivot_entry_lemma.tex (14/14,
│                         PIVOT ENTRY STEPS VERIFIED)
│   ├── verify_compose_premises.py — machine check of
│                         compose_premises.tex (16/16,
│                         COMPOSE PREMISES VERIFIED)
│   ├── verify_christoffel_quiet.py — machine check of
│                         christoffel_quiet.tex (13/13,
│                         CHRISTOFFEL QUIET VERIFIED)
│   ├── verify_compose_premises2.py — machine check of
│                         compose_premises2.tex (16/16,
│                         COMPOSE PREMISES2 VERIFIED)
│   ├── verify_coherence_assist.py — machine check of
│                         coherence_assist.tex (13/13,
│                         COHERENCE ASSIST VERIFIED)
│   ├── verify_delta_deformation.py — machine check of
│                         delta_deformation.tex (13/13,
│                         DELTA DEFORMATION VERIFIED)
│   ├── verify_weyl_energy.py — machine check of
│                         weyl_energy.tex (14/14,
│                         WEYL ENERGY VERIFIED)
│   ├── verify_g_eps_mu.py — machine check of
│                         g_eps_mu.tex (13/13,
│                         G_EPS_MU LEMMA VERIFIED)
│   ├── verify_construction_rl.py — machine check of
│                         construction_rl.tex (17/17,
│                         CONSTRUCTION PURE RL VERIFIED)
│   ├── verify_deletion_transform.py — machine check of
│                         deletion_transform.tex (14/14,
│                         DELETION TRANSFORM VERIFIED)
│   ├── verify_tau_field.py — machine check of
│                         tau_field.tex (13/13,
│                         TAU FIELD VERIFIED)
│   ├── verify_sign_schur.py — machine check of
│                         sign_schur.tex (14/14,
│                         SIGN SCHUR VERIFIED)
│   ├── verify_three_gap_mask.py — machine check of
│                         three_gap_mask.tex (11/11,
│                         THREE GAP MASK VERIFIED)
│   ├── verify_isolation_lemma.py — machine check of
│                         isolation_lemma.tex (10/10,
│                         ISOLATION LEMMA VERIFIED)
│   ├── verify_high_moment.py — machine check of
│                         high_moment_inertia.tex (12/12,
│                         HIGH MOMENT VERIFIED)
│   ├── verify_source_weyl.py — machine check of
│                         source_weyl_energy.tex (11/11,
│                         SOURCE WEYL VERIFIED)
│   ├── verify_bulk_one_defect.py — machine check of
│                         bulk_one_defect.tex (12/12,
│                         BULK ONE DEFECT VERIFIED)
│   ├── verify_edge_signature.py — machine check of
│                         edge_signature.tex (13/13,
│                         EDGE SIGNATURE VERIFIED)
│   ├── verify_p1_construction.py — machine check of
│                         p1_construction.tex (11/11,
│                         P1 CONSTRUCTION VERIFIED)
│   ├── verify_one_defect_gram.py — machine check of
│                         one_defect_gram.tex (11/11,
│                         ONE DEFECT GRAM VERIFIED)
│   ├── verify_edge_lift.py — machine check of
│                         edge_contractive_lift.tex (12/12,
│                         EDGE LIFT VERIFIED)
│   ├── verify_dual_intertwiner.py — machine check of
│                         dual_intertwiner.tex (12/12,
│                         DUAL INTERTWINER VERIFIED)
│   ├── verify_c_threshold.py — machine check of
│                         c_threshold.tex (9/9,
│                         C THRESHOLD VERIFIED)
│   ├── verify_borodin_birkhoff.py — machine check of
│                         borodin_birkhoff_intertwiner.tex
│                         (11/11, BORODIN BIRKHOFF VERIFIED)
│   ├── verify_hole_nyquist.py — machine check of
│                         hole_nyquist.tex (9/9,
│                         HOLE NYQUIST VERIFIED)
│   ├── verify_threshold_identity.py — machine check of
│                         threshold_identity.tex (9/9,
│                         THRESHOLD IDENTITY VERIFIED)
│   ├── verify_hole_top_mode.py — machine check of
│                         hole_top_mode.tex (9/9,
│                         HOLE TOP MODE VERIFIED)
│   ├── verify_top_mode_edge.py — machine check of
│                         top_mode_edge.tex (9/9,
│                         TOP MODE EDGE VERIFIED)
│   ├── verify_debranges_index.py — machine check of
│                         debranges_index.tex (9/9,
│                         DEBRANGES INDEX VERIFIED)
│   └── verify_source_sch.py — machine check of
│                         source_sch_sign.tex (10/10,
│                         SOURCE SCH SIGN VERIFIED)
│   └── verify_phi_bb.py — machine check of
│                         phi_bb_sign.tex (10/10,
│                         PHI BB SIGN VERIFIED)
│   └── verify_vacuous_overflow.py — machine check of
│                         vacuous_overflow.tex (8/8,
│                         VACUOUS OVERFLOW VERIFIED)
│   └── verify_cj_sigma.py — machine check of
│                         cj_sigma.tex (8/8,
│                         CJ SIGMA VERIFIED)
│   └── verify_reserve_limit.py — machine check of
│                         reserve_limit.tex (8/8,
│                         RESERVE LIMIT VERIFIED)
│   └── verify_sigma_limit.py — machine check of
│                         sigma_limit.tex (7/7,
│                         SIGMA LIMIT VERIFIED)
│   └── verify_den_limit.py — machine check of
│                         den_limit.tex (7/7,
│                         DEN LIMIT VERIFIED)
│   └── verify_gamma_chain.py — machine check of
│                         gamma_chain.tex (7/7,
│                         GAMMA CHAIN VERIFIED)
│   └── verify_cross_chain.py — machine check of
│                         cross_chain_gamma.tex (6/6,
│                         CROSS CHAIN VERIFIED)
│   └── verify_campaign_audit.py — machine check of
│                         campaign_audit.tex (9/9,
│                         CAMPAIGN AUDIT NOTE VERIFIED)
│   └── verify_qn_reopened.py — machine check of
│                         qn_reopened.tex (6/6,
│                         QN REOPENED VERIFIED)
│   └── verify_zloc_head.py — machine check of
│                         zloc_head.tex (6/6,
│                         ZLOC HEAD VERIFIED)
│   └── verify_source_potapov.py — machine check of
│                         source_potapov.tex (7/7,
│                         SOURCE POTAPOV VERIFIED)
│   └── verify_edge_redheffer.py — machine check of
│                         edge_redheffer.tex (8/8,
│                         EDGE REDHEFFER VERIFIED)
│   └── verify_p1_overload.py — machine check of
│                         p1_overload.tex (8/8,
│                         P1 OVERLOAD VERIFIED)
│   └── verify_p2_determinant.py — machine check of
│                         p2_determinant.tex (8/8,
│                         P2 DETERMINANT VERIFIED)
│   └── verify_evolutionary_cert.py — machine check of
│                         evolutionary_certificate.tex (10/10,
│                         EVOLUTIONARY CERT VERIFIED)
│   └── verify_residual_loewner.py — machine check of
│                         residual_loewner.tex (7/7,
│                         RESIDUAL LOEWNER VERIFIED)
│   └── verify_mean_tau.py — machine check of
│                         mean_tau_index.tex (8/8,
│                         MEAN TAU INDEX VERIFIED)
│   └── verify_diag_lifts.py — machine check of
│                         diag_lifts_loewner.tex (6/6,
│                         DIAG LIFTS VERIFIED)
│   └── verify_block_mean.py — machine check of
│                         block_mean.tex (8/8,
│                         BLOCK MEAN VERIFIED)
│   └── verify_delta_floor.py — machine check of
│                         delta_floor.tex (6/6,
│                         DELTA FLOOR VERIFIED)
│   └── verify_signed_border.py — machine check of
│                         signed_border_mean.tex (8/8,
│                         SIGNED BORDER MEAN VERIFIED)
│   └── verify_deep_builder.py — machine check of
│                         deep_builder.tex (7/7,
│                         DEEP BUILDER VERIFIED)
│   └── verify_deep_abd.py — machine check of
│                         deep_abd.tex (7/7,
│                         DEEP ABD VERIFIED)
│   └── verify_exact_atom.py — machine check of
│                         exact_atom.tex (7/7,
│                         EXACT ATOM VERIFIED)
│   └── verify_exact_band.py — machine check of
│                         exact_band.tex (7/7,
│                         EXACT BAND VERIFIED)
│   └── verify_flip_vs_stab.py — machine check of
│                         flip_vs_stab.tex (6/6,
│                         FLIP VS STAB VERIFIED)
│   └── verify_prefix_mincut.py — machine check of
│                         prefix_mincut.tex (7/7,
│                         PREFIX MINCUT VERIFIED)
│   └── verify_nstab_transition.py — machine check of
│                         nstab_transition.tex (6/6,
│                         NSTAB TRANSITION VERIFIED)
│   └── verify_plateau_theorem.py — machine check of
│                         plateau_theorem.tex (6/6,
│                         PLATEAU THEOREM VERIFIED)
│   └── verify_border_mass.py — machine check of
│                         border_mass.tex (6/6,
│                         BORDER MASS VERIFIED)
│   └── verify_limit_object.py — machine check of
│                         limit_object.tex (6/6,
│                         LIMIT OBJECT VERIFIED)
│   └── verify_arch_chain.py — machine check of
│                         arch_chain.tex (6/6,
│                         ARCH CHAIN VERIFIED)
│   └── verify_vacuity_redteam.py — machine check of
│                         vacuity_redteam.tex (6/6,
│                         VACUITY REDTEAM VERIFIED)
│   └── verify_jp_increment.py — machine check of
│                         jp_increment.tex (6/6,
│                         JP INCREMENT VERIFIED)
└── verification/
    ├── make_inventory.py — regenerates INVENTORY.json
    └── run_rh.py         — the RH suite (see below)
```

## The standalone problem (`rh/problem/`)

The r283 attack reduced the open center to ONE scalar inequality, the
missing lemma L\*: for the window pair `(mu, nu)`, every real
polynomial `p != 0` with `deg p < (S+1)/2` satisfies
`int p^2 dnu < int p^2 dmu` (equivalently `lambda_max(E_{N_w}) < 1`).
`rh/problem/lstar_problem.pdf` states exactly this as a
**self-contained open problem** — the two measures defined from first
principles (von Mangoldt comb, tent sampling, archimedean lag
function, circulant spectral density, folding), the concrete
`S = 367` instance tabulated, equivalent Hankel / CD-kernel /
sampling formulations, the neutral numerical record, and the
moment-counting meaning of the degree bound — with **no project
vocabulary**, suitable for handing to external mathematicians
(approximation theory, orthogonal polynomials, sampling theory,
analytic number theory, operator theory).

`rh/problem/verify_lstar_instance.py` (numpy/mpmath only) rebuilds
the instance from the document's formulas alone and gates it against
the repository builders: atom positions/weights agree to `4e-16`
(relative), `lambda_max(E_184) = 0.99983248` and
`lambda_max(E_185) = 1.00003660` reproduced incl. a dps-60 mpmath
ward, the inequality checked on monomials and 500 random polynomials
— 12/12 gates, final line `LSTAR INSTANCE VERIFIED`.  The optional
`--ladder` sweep measures the margin `1 - lambda_max(E_{N_w})` on all
42 admissible windows: **all positive, but shrinking with S** — from
`1.68e-4` (S = 367, the *largest* margin of the family) down to
`1.42e-7` (kz64, S = 1717).  Honest note: the family margin loses
~3 orders of magnitude over the tested range, so the unbounded-family
version of the problem is genuinely uncertain in both directions.
The document claims nothing; L\* stays **[O]**, the open center —
since wave 6 registered in canonical form as its own ledger contract
**`PRIME.LSTAR.SUBORDINATION.01`** (established as the canonical
reduction by `v963_lstar_reduction_dictionary.py` [E]).
NO RH CLAIM.

Since 2026-08-27 the document additionally carries the freeze memo
as its final content section, "The frozen state (August 2026): one
object" (§frozen): the fully typed chain
(dictionary weights / candidate deficits / theorem-grade pinning /
computability closure), the one object (the φ co-wander and its
500× cancellation, ρ_r = 2.624 as the decay of the difference), the
three specialist questions in final form, and the honest census
frame (85 windows to N_w 7942, all margins positive, pool
exhausted).  The lane is FROZEN as a specialist problem (reviewer
decision; see the lane status update above); the sections of the
original problem statement are unchanged.

A second standalone note, `rh/problem/rdagger_saturation.pdf`
(August 30, 2026; updated after r367–r373, r412, r426, and
the DCCXCVII dossier consolidation), is a 17-page specialist
dossier.  The R360+R362 complex remains:
definition of the bordered dual resolvent
`R† = [[R⁻¹, Dv], [(Dv)ᵀ, 1+γ]]⁻¹`, the exact duality package
`(A1)–(A7)`, the critical 3×3 Schur block, the census that the
binding pair straddles the saturation-block edge `3|4`, the
observed exponent `α = 3.332`, the relative/projective error-
operator form.  After the two-rank inertia cut and the
matrix-Weyl sequence the **primary question is strictly weaker
and sharper**: (P1) `ind₋(R_{N-3} − ½I) ≤ 1` (integer mode
count; census 0 overload on 74/74, dichotomy 45 nneg-1 / 29
already-PD) and (P2) `det K₂ ≤ −c₀ < 0` on the nneg-1 branch
(sign of an O(1) source; `−det K₂ ∈ [1.157, 1126.389]`, floor
0.50, margin-uncorrelated corr `−0.0064`).  Haynsworth
(`haynsworth_two_rank`, `haynsworth_mixed`) and the R† layer
are Lean sorry-free (census 7); a proof of (P1)+(P2) for all
canonical windows beyond the certified head lands, via the
kernel-checked chain, at window-local master positivity — a
landing pad, not a theorem of the family.  The
older RHP/BKMM saturation question (BKMM 2007 Thm 2.7 / Rem 2.8)
is retained as the **stronger variant**.  Mixed 3×3 form,
wedge-sign census, Φ-monotonicity, Prüfer dictionary, and the
named dead ends (no 3×3 Jacobi Casoratian, phase restatement,
r366 O(1) mass-count buffer, r363 edge pinning) are recorded.
Finite census, no asymptotics, no claim.  L\* and L† stay
**[O]**.  NO RH CLAIM.

A third standalone note, `rh/problem/medcap_lemma.pdf` (August 28,
2026), is a proof attempt for the r361 median-cap inequality
`med_i ≤ (8/3)·sep_i` on the block packing of the folded measure
(reviewer priority 1, no further discovery round).  SEP-SATZ is
proved as cut geometry.  Tiling (no unoccupied integer between or
inside blocks) forces `gap_i = sep_i` and reduces MED-CAP to an
order-statistic bound on the length sequence `n_i`.  Tiling is a
census identity on 134 windows / 15 428 atoms (0 exceptions).
The tiled composition `n = (1,2,8^{10})` violates with ratio
`16/3`, so the inequality is **not** a theorem of interval
geometry; the remainder `X_n` is that the source length sequence
forbids a C2 jump at small-separation loci.  The constant `8/3`
is saturated by the edge prefix `(1,2,6,5,4,4)` at χ4 kz53
(third-smallest of five neighbour-gaps).  Companion script
`verify_medcap_steps.py`, 11/11 gates, `MEDCAP STEPS VERIFIED`.
Finite identities plus a named combinatorial remainder.  NO RH
CLAIM.

A fourth standalone note, `rh/problem/xn_invariant.pdf` (August 28,
2026), is the proof attempt for that remainder $X_n$ (round 364,
no sealed discovery probe).  Pairing of positive run lengths
proves: $n=1$ occurs only as the odd tail at $\theta$-min;
prefixes $(2,1)$ and $(1,1)$ are impossible; the unique possible
$\mathrm{sep}=\tfrac32$ locus is the edge pair $(1,2)$.  Pairing
does **not** forbid $C_2$ (random paired runs still violate; a
Chebyshev colouring after the $x$-mask never produces $(1,2)$).
On the 134-window surface $n=1$ occurs 32 times (always index 0)
and $(1,2)$ occurs **once**: $\chi_4$ kz53, saturating prefix
`(1,2,6,5,4,4)`, nearest $n\ge 7$ at index 7 (outside the
radius-5 window).  Named remainder $V_2$: local run-length
regularity of the bordered-chain polynomial $v_2$ at the 20%
$x$-mask (no 6-plateau after three singleton runs).  The minimal
grid-consistent violator is named.  On the surface, $X_n$ holds,
hence MED-CAP holds, hence the pointwise floor $g_i\ge 3/8$ holds,
hence $T_2'$ trivialises; $C_K$ is unchanged.  Companion script
`verify_xn_steps.py`, 12/12 gates, `XN STEPS VERIFIED`.  Finite
identities plus a named analytic remainder.  NO RH CLAIM.

A fifth standalone note, `rh/problem/v2_regularity.pdf` (August 28,
2026), is the proof attempt for that remainder $V_2$ (round 365,
no sealed discovery probe, hydra ward binding).  Anatomy: $v_2$ is
the degree-$(N-2)$ arithmetic-comb chain polynomial on the
smooth-border nodes (Jacobi from the source, not mesh-only); $w$
is the arm sign of the explicit smooth fold.  Proved: product
flip-XOR; $(1,1,1)$ yields the $\theta$-prefix $(1,2)$ iff the run
count is odd.  Refuted: a $2$-regular factor does **not** imply
$V_2$ (11/8000 random products still violate).  Chebyshev after
the $x$-mask never ends $(1,1,1)$; Chebyshev times a Nyquist burst
of $w$ never violates $V_2$ (425 windows).  On the 134-window
surface $V_2$ holds (0 violators); two colouring triples, both
regular, only one odd ($\chi_4$ kz53, $w$-driven saturator);
$\chi_3$ kz16 is a $v_2$-triple with even run count ($n_0=2$, not
small-sep).  The Jacobi-Chebyshev / Freud reductions are not
strictly more elementary (they are statements about the chain
itself).  Verdict `REGRESS_DETECTED`: the escape
$T_2'\Leftarrow\cdots\Leftarrow V_2$ freezes at $V_2$; the
pointwise floor $g_i\ge 3/8$ is a theorem of the construction
**modulo** $V_2$.  T1 / $C_K$ unchanged.  Companion script
`verify_v2_steps.py`, 12/12 gates, `V2 STEPS VERIFIED`.  Finite
identities plus a named freeze.  NO RH CLAIM.

Round 374 (`v2_lemma_v3.pdf`) reopens that freeze under the
lemma-first charter (exactly one named lemma; exit proved /
refuted / reduced).  **REDUZIERT** to $V_3'$: the last fourteen
Prüfer steps of $v_2$ at the $+x$ mask lie in the finite region
$\mathcal{A}_{15}$ of speed profiles that are $V_2$-regular for
every incoming remainder.  Proved: Wronskian step formula
(Lagrange over $\mathbb{Q}$; residual $1.0\cdot 10^{-15}$);
$x$ constant at the $+x$ mask; contrast dichotomy (constant
steps never violate; slow-then-fast $(0.4^{21},2.8^{3})$ does,
$(1.0^{21},2.0^{3})$ does not).  An $8\times$ last-$12$
$\gamma$-scale on $\chi_3$ $w=9$ is a $v_2$-violator, so $V_2$
is not abstract Jacobi-positivity.  Path A on the six pins
($0$ remainder-violators).  Companion script
`verify_v2_lemma.py`, 16/16 gates,
`V2 LEMMA V3 VERIFIED`.  The chain is now
$T_2'\Leftarrow\cdots\Leftarrow V_2\Leftarrow V_3'$.  Finite
identities plus a named reduction.  NO RH CLAIM.

A sixth standalone note, `rh/problem/p2_lemma_proof.pdf` (August 28,
2026), is the lemma-first attack on (P2) (round 375, no sealed
discovery probe).  On a real Hermitian nneg-1 matrix the Schur
block $K_2=I+U^T A_0^{-1}U$ factors as
$K_2=(I+R_+)-ww^T/\lambda_-$ with $w=U^T\psi_-$ and
$\det K_2=\det(I+R_+)(1-\gamma/\lambda_-)$ (Fractions toy
$\det K_2=-7$ exact).  The prefactor $\det(I+R_+)\ge 1$ is a sum
of positive Gram terms; the sign is carried by the dressed
overlap $\gamma-\lambda_-$.  P1 does not imply P2 (tiny-overlap
adversary).  The $\delta$-energy of the CD-wedge in the rest form
is load-bearing (kz46).  P2 is not the r359 bind ratio (fold-pair
Schur already PD at rank $N-3$, $45/45$).  **REDUZIERT** to the
dressed-overlap inequality $\gamma>(1+\varepsilon)\lambda_-$,
which implies $-\det K_2\ge\varepsilon$ and does not consume
$\lambda_{\min}(S_N)$.  Named remainder: source expansion of
$U^T\psi_-$ via dual CD weights and the Borodin dual mode of
$R_{N-3}-\tfrac12 I$.  Companion script `verify_p2_steps.py`,
12/12 gates, `P2 STEPS VERIFIED`.  Finite identities plus a named
remainder.  NO L\* claim.  NO RH CLAIM.

A seventh standalone note, `rh/problem/postcap_pivots.pdf` (August 28,
2026), is the lemma-first attack on the Fable source-pivot
coordinate (round 377, sealed census probe
`postcap_pivots_probe.py`).  The Hankel dictionary
$\det K_2=H_N(w)H_{N-3}(a)/(H_{N+2}(w)H_{N-1}(a))$ is SATZ
(Fractions toy $-196/35719$).  Universal post-cap alternation
$h_N h_{N+1}<0$ is **WIDERLEGT** ($kz=12$ and $34$ further
LATE/NONE MAIN rows).  On the nneg-$1$ branch the product is
negative $50/50$.  Node polynomial and Chebyshev aliasing are
theorems; they do not evaluate the sign without $H_N^{-1}$.
$\mathrm{ind}_- H_{N+2}\le 1$ is a construction census
($85/85$ MAIN, $84/84$ $\chi$, scramble breaks).  Companion
script `verify_postcap_steps.py`, 16/16 gates,
`POSTCAP STEPS VERIFIED`.  Finite identities plus a named
census.  NO L\* claim.  NO RH CLAIM.

An eighth standalone note, `rh/problem/compose_lemma.pdf` (August 28,
2026), is the lemma-first attack on the terminal composition
COMPOSE (round 378, no sealed discovery probe).  Van der Corput
at $H=\max(2,\lceil\sqrt{m}\rceil)$ is SATZ; the $H$-rule,
participation, Rényi, and kernel envelope are SATZ; T1-floor
algebra is SATZ conditional on $8/3$ and $C_K$.  The slope
chain $\sigma\le-0.516$, $N_2$-need $0.908$, atom-need $0.888$
is a convention, not a pointwise theorem.  **REDUZIERT** to
COMPOSE⁻: $M_3\le\phi(m)$ together with frozen $R_0$, $\Lambda$,
$Z_0<M$ implies $\lvert Z\rvert<M$.  H5 is a sister route.
Log-complete $m_0$ is $10^{25.81}$/$10^{32.85}$ (r361 dropped
$2\log\log m$).  Companion script `verify_compose_lemma.py`,
15/15 gates, `COMPOSE LEMMA VERIFIED`.  Finite identities plus
named remainders.  NO L\* claim.  NO RH CLAIM.

A ninth standalone note, `rh/problem/v3prime_proof.pdf` (August 28,
2026), is the lemma-first attack on $V_3'$ (round 379, no sealed
discovery probe).  The mask mesh is the cosine grid $x=\cos(2\pi k/L)$
with $L=4h-2$; consecutive bulk nodes at the $+x$ mask are
equidistant in $\arccos$ ($181/181$).  Equal weights on the
occupied cosine nodes are Chebyshev; the Fejér factor is
Jacobi-$(0,1)$ with an $O(1/n^2)$ closed form.  Two-period
profiles about $\pi/2$ with amplitude $a\le 0.85$ lie in
$\mathcal{A}_{15}$; a coherent last-$12$ $\gamma$-scale of $1.5$
stays in $\mathcal{A}_{15}$ and a scale of $2.0$ leaves it.
**REDUZIERT** to $G_\varepsilon$: last twelve
$\lvert\gamma_k-\tfrac14\rvert\le\tfrac1{16}$ and consecutive
log-ratio $\le\tfrac25$.  On $181$ windows $G_\varepsilon$ and
$V_3'$ both hold ($0$ remainder-violators).  Companion script
`verify_v3prime.py`, 17/17 gates, `V3PRIME LEMMA VERIFIED`.
Finite identities plus a named remainder.  NO L\* claim.  NO RH
CLAIM.

A tenth standalone note, `rh/problem/g_eps_lemma.pdf` (August 28,
2026), is the lemma-first attack on $G_\varepsilon$ (round 381).
The first-order Jacobi formula
$\partial\gamma_k/\partial w_j=(p_k(x_j)^2-\gamma_k p_{k-1}(x_j)^2)/h_{k-1}$
is SATZ (Fractions + FO vs FD).  An $L^\infty$ bound on
$d_{\mathrm{arm}}$ does not yield the $1/16$ box; the jump half
is independent of the box; the second-order remainder is not
dominated.  **REDUZIERT** to $(C_\varepsilon,R_2)$.  Scramble
seed $1$ named-breaks last-$12$ ($\lvert\gamma-1/4\rvert=6.841$).
Companion script `verify_g_eps.py`, 13/13 gates,
`G_EPS LEMMA VERIFIED`.  Discovery probe
`g_eps_lemma_probe.py`, 17/17, SPEC_SHA `60ce9bc28fc7f171`.
Finite identities plus a named reduction.  NO L\* claim.  NO RH
CLAIM.

An eleventh standalone note, `rh/problem/pivot_entry_lemma.pdf`
(August 28, 2026), is the lemma-first attack on the entry of the
pivot band (round 382, sealed census probe
`pivot_entry_lemma_probe.py`).  Rank-one inertia transport
(r380) reduces the cap to a source-defined $n_0$ with at most
one sign change in $h_0,\ldots,h_{n_0}$.  The three-term
recurrence alone does not forbid a second prefix return.  The
source ingredient is the flank condition (max $\nu$-run $\le 2$,
$\nu$-mass $\le (2/3)$ flanking $\mu$-mass).  **REDUZIERT** to
$n_0=\lfloor 2N/5\rfloor$ under that condition.  Two-period
amplitude $2/3$ is the binding adversary against $n_0=N-1$;
scramble named-breaks at run length and flank ratio.  Companion
script `verify_pivot_entry.py`, 14/14 gates,
`PIVOT ENTRY STEPS VERIFIED`.  Discovery probe 17/17, SPEC_SHA
`b7f53a93daf790bc`.  Finite identities plus a named reduction.
NO L\* claim.  NO RH CLAIM.

A twelfth standalone note, `rh/problem/compose_premises.pdf`
(August 28, 2026), is the lemma-first attack on the three
COMPOSE$^-$ input premises $(R)$, $(L)$, $(Z)$ (round 383, sealed
census probe `compose_premises_probe.py`).  The r378 implication
is a theorem of those three inequalities plus $M_3\le\phi(m)$.
Fejér, $r298$, $Z=Z_{\mathrm{loc}}+t_{\mathrm{bulk}}$, the $L^2$
identity, $\Lambda\le\log$, and the $H$-rule are SATZ.  Fold
pairing is REFUTED as a description of the live $P_\omega$.
**(R) REDUZIERT** ($R_0=4$).  **(L) REDUZIERT** ($\Lambda=3$);
the T1-combo does not close as a theorem ($E_\pi$ spikes).
**(Z) REDUZIERT** on FRAME-A ($Z_0=4/5$) and **REFUTED**
family-uniform on $\chi$ (six windows).  Companion script
`verify_compose_premises.py`, 16/16 gates,
`COMPOSE PREMISES VERIFIED`.  Discovery probe 20/20, SPEC_SHA
`146b0b45ad872d7e`.  Finite identities plus named reductions.
NO L\* claim.  NO RH CLAIM.

A thirteenth standalone note, `rh/problem/christoffel_quiet.pdf`
(August 28, 2026), is the lemma-first attack on the common
Christoffel-quietness core of $G_\varepsilon$ and $L^*$ (round
385, sealed census probe `christoffel_quiet_probe.py`).
Chebyshev sampling of $\nu$ is SATZ at *trivial* Weyl
($Q^T\le 2\alpha$).  The deduction to $\mu$-OP $Q_k$ from the
$3/8$-floor + Koksma is false ($w=9$ last-twelve $Q=0.389$ vs
$\alpha=0.061$).  $Q<1$ is not the floor plate (two-period
$c=2/3$: $Q\equiv 0.683$ and $\lambda_{\max}(E_{22})>1$).
**REDUZIERT** to the pair $(\Delta,C)$.  Weyl scale trivial,
not PNT, not subconvex, not RH-equivalent.  Companion script
`verify_christoffel_quiet.py`, 13/13 gates,
`CHRISTOFFEL QUIET VERIFIED`.  Discovery probe 19/19, SPEC_SHA
`03bde46ec27d98ff`.  Finite identities plus a named reduction.
NO L\* claim.  NO RH CLAIM.


A fourteenth standalone note, `rh/problem/compose_premises2.pdf`
(August 28, 2026), is the lemma-first attack on living-ladder
$(Z')$ and cofinal $R_0$ (round 386, sealed census probe
`compose_premises2_probe.py`).  The six r383 $\chi$-violators
are the terminal-dead $q_N>1$ sprouts.  **$(Z')$ REDUZIERT**
($Z_0'=21/25$ on $175$ living windows).  Death channel
biconditional CENSUS $181/181$.  Finite-head Chebyshev REFUTED;
uniform cancellation times triangle REFUTED.  **$(R)$ REDUZIERT**
to the Gram remainder $B(\omega+\beta,\omega+\beta)\le K D$.
Companion script `verify_compose_premises2.py`, 16/16 gates,
`COMPOSE PREMISES2 VERIFIED`.  Discovery probe 20/20, SPEC_SHA
`82d07e568591c9fd`.  Finite identities plus named reductions.
NO L\* claim.  NO RH CLAIM.

A fifteenth standalone note, `rh/problem/coherence_assist.pdf`
(August 28, 2026), is the lemma-first attack on the coherence
assist (round 387, sealed census probe
`coherence_assist_probe.py`).  Chebyshev--Dirichlet CD,
bookkeeping, Gershgorin, and the cosine mesh are SATZ.  The
two-period is a global arithmetic progression of $\nu$-angles
($\rho_{\mathrm{AP}}=1$).  Gershgorin plus the $3/8$-floor does
not close $\lambda_{\max}<1$ ($k^*_{\mathrm{G}}\sim 0.11\,N
<\lfloor 2N/5\rfloor$).  **REDUZIERT** to the signed $\mu$-CD
off-diagonal.  Named property $\rho_{\mathrm{AP}}<1/5$ kills
the two-period and holds on EXT-heavy seven; scramble holds it
and dies on the diagonal.  Companion script
`verify_coherence_assist.py`, 13/13 gates,
`COHERENCE ASSIST VERIFIED`.  Discovery probe 20/20, SPEC_SHA
`6005359e0bafadb2`.  Finite identities plus a named reduction.
NO L\* claim.  NO RH CLAIM.

A sixteenth standalone note, `rh/problem/delta_deformation.pdf`
(August 28, 2026), is the lemma-first attack on the
$\Delta$-deformation closing of $C_\varepsilon$ (round 388,
sealed census probe `delta_deformation_probe.py`).
The split $\mathrm{FO}=\gamma(\mathrm{d}Q^T+\mathrm{d}\Delta)$
and Fejér-pure $\varepsilon=0\Rightarrow\mathrm{FO}=0$ are SATZ.
Osc-Geronimus does not close $C_\varepsilon$ ($C_*=0.0056$,
majorant $0.191$).  $R_2$ on the $\mu$-reference is not dominated
(ratio $0.861$ at degree $40$, $0.640$ at full depth,
$\lvert R_2\rvert/\lvert\mathrm{FO}\rvert=4.19$).  **REDUZIERT**
to the r381 triple $G_\varepsilon^\mu\wedge C_\varepsilon\wedge R_2$.
Scramble keeps a smaller $\mathrm{osc}(\varepsilon)$ and explodes
$\mathrm{d}\Delta$.  Companion script
`verify_delta_deformation.py`, 13/13 gates,
`DELTA DEFORMATION VERIFIED`.  Discovery probe 19/19, SPEC_SHA
`5613d035ac6bc11d`.  Finite identities plus a named reduction.
NO L\* claim.  NO RH CLAIM.

## The RH suite

```bash
# from the repo root
python rh/verification/run_rh.py                 # full run (~8-9 min measured)
python rh/verification/run_rh.py --fast          # integrity + probes + lean (~36 s)
```

The suite runs, in order:

1. **Integrity** — SHA-256 of every pinned `INVENTORY.json` entry
   (drift in a pinned file = FAIL; unpinned living documents = INFO),
2. **Sealed probes** — the campaign probes r250–r496 + r535–r537 + r539–r541 + r544 + r548 + r549 + r551 + r553 + r560 + r561 + r563 + r565 + r567 + r591 + r592 + r601 + r603 + r604 + r605N + r606 + r607 + r608 + r609 + r611 + r613 + r615 + r616 + r617 + r618 + r619 + r620 + r621 + r622 + r623 + r625 + r626 + r627 + r628 + r629 + r630 + r632 + r633 + r635 + r636 + r637 + r638 + r639 from
   `experiments/tfpt-discovery/` in `--smoke` mode (fast, seconds each),
3. **The fifteen v9xx RH modules** — `v955`, `v956`, `v958`, `v959`,
   `v960`, `v961`, `v962`, `v963`, `v964`, `v965`, `v966`, `v967`,
   `v968`, `v969`, `v970` executed by path from
   `verification/` (never copied; `v959` ~3.5 min, `v968` ~50 s, the
   rest seconds — the wave-4/5/6/7/8/9/10/11/12/13 modules embed
   their probes in the sealed `--smoke` stage; skipped under
   `--fast`),
4. **Lean gate** — `lake build` in `rh/lean/` if a Lean toolchain is present.

Output is house-style: `[PASS/FAIL]` per item, final line
`RH SUITE: ALL CHECKS PASSED` or `RH SUITE: FAILURES n`.
It uses the repo venv `experiments/tfpt-discovery/.venv` if present.
Reference runs 2026-08-25: full **25/25 items PASS, wall 493 s, ALL CHECKS
PASSED** (pre-r268/r269 list); after the r268+r269 sync, fast mode
**23/23 items PASS, wall 37 s, ALL CHECKS PASSED**; after the r271 sync,
fast mode **24/24 items PASS, wall 36 s, ALL CHECKS PASSED** (Lean gate
included, 7 intentional `sorry` warnings); after the r270 sync (r270+r271
merged additively), fast mode **25/25 items PASS, ALL CHECKS PASSED**;
after the r272 sync, fast mode **26/26 items PASS, wall 43 s, ALL CHECKS
PASSED** (44/44 pinned entries byte-identical, Lean gate included); after
the r273 sync, fast mode **27/27 items PASS, ALL CHECKS PASSED** (45/45
pinned entries byte-identical); after the r273 Lean-pilot repair, fast
mode **27/27 items PASS, wall 43 s, ALL CHECKS PASSED** (Lean gate
included, **6 intentional `sorry` warnings** — down from 7: the two
Open-edge sorries consolidated into the one master-theorem sorry); after
the r274 sync, fast mode **28/28 items PASS, wall 45 s, ALL CHECKS
PASSED** (47/47 pinned entries byte-identical, Lean gate included,
6 intentional `sorry` warnings); after the r275+r276 sync (merged
additively), fast mode **30/30 items PASS, wall 47 s, ALL CHECKS
PASSED** (48/48 pinned entries byte-identical, Lean gate included,
6 intentional `sorry` warnings); after the r278 sync, fast mode
**31/31 items PASS, wall 50 s, ALL CHECKS PASSED** (49/49 pinned
entries byte-identical, Lean gate included, 6 intentional `sorry`
warnings); after the r277 sync (merged additively next to the
parallel r278 sync), fast mode **32/32 items PASS, wall 48 s, ALL
CHECKS PASSED** (50/50 pinned entries byte-identical, Lean gate
included, 6 intentional `sorry` warnings); after the wave-4 promotion
(v960/v961 pinned into the inventory, MODULES list extended), fast mode
**32/32 items PASS, wall 48 s, ALL CHECKS PASSED** (**52/52** pinned
entries byte-identical, Lean gate included, 6 intentional `sorry`
warnings); after the r279 sync (merged additively next to the parallel
wave-4 promotion), fast mode **33/33 items PASS, wall 49 s, ALL CHECKS
PASSED** (53/53 pinned entries byte-identical, Lean gate included,
6 intentional `sorry` warnings); after the r280 sync, fast mode
**34/34 items PASS, wall 49 s, ALL CHECKS PASSED** (54/54 pinned
entries byte-identical, Lean gate included, 6 intentional `sorry`
warnings); after the r281 sync, fast mode **35/35 items PASS, wall
50 s, ALL CHECKS PASSED** (55/55 pinned entries byte-identical, Lean
gate included, 6 intentional `sorry` warnings); after the r282 sync,
fast mode **36/36 items PASS, wall 53 s, ALL CHECKS PASSED** (56/56
pinned entries byte-identical, Lean gate included, 8 intentional
`sorry` warnings); after the r283 sync, fast mode **37/37 items PASS,
wall 49 s, ALL CHECKS PASSED** (57/57 pinned entries byte-identical,
Lean gate included, 8 intentional `sorry` warnings); after the wave-5
promotion (v962 pinned into the inventory, MODULES list extended to
seven, consumption notes on the r279–r281 probes), see the current
reference run recorded with the wave-5 exit gate; after the r284 sync,
fast mode **38/38 items PASS, wall 53 s, ALL CHECKS PASSED** (59/59
pinned entries byte-identical, Lean gate included, 8 intentional
`sorry` warnings); after the r285 sync (merged additively next to the
parallel `rh/problem/` registration), fast mode **39/39 items PASS,
wall 51 s, ALL CHECKS PASSED** (62/62 pinned entries byte-identical,
Lean gate included, 8 intentional `sorry` warnings); after the r287
sync (the L2 lane, merged additively next to the parallel r286 L\*
round), fast mode **40/40 items PASS, wall 49 s, ALL CHECKS PASSED**
(63/63 pinned entries byte-identical, Lean gate included, 8
intentional `sorry` warnings); after the wave-6 promotion (v963
pinned into the inventory, MODULES list extended to eight,
consumption notes on the r282–r285 probes, the r285
`make_inventory.py` sync repair included, merged additively next to
the parallel r287 sync), **full mode 48/48 items PASS, wall 519 s,
ALL CHECKS PASSED** (64/64 pinned entries byte-identical, all eight
modules green incl. v963 at 1.1 s, Lean gate included, **9
intentional `sorry` warnings** — the wave-6 canonical form
`lstar_subordination` added, the direction L\* ⇒ free-window
positivity proved); after the r286 sync (the L\* margin-scaling
round, merged additively), fast mode **41/41 items PASS, wall 48 s,
ALL CHECKS PASSED** (65/65 pinned entries byte-identical, Lean gate
included, 9 intentional `sorry` warnings); after the r289 sync (the
arch-kernel diophantine relevance test, merged additively next to the
parallel r288 sync), fast mode **43/43 items PASS, wall 52 s, ALL
CHECKS PASSED** (67/67 pinned entries byte-identical, Lean gate
included, 9 intentional `sorry` warnings); after the r290 sync (the
profile-space basin geometry round, merged additively next to the
parallel wave-7 `lstar_problem.tex` update whose refreshed pin the
parallel sync registered), fast mode **44/44 items PASS, wall 57 s,
ALL CHECKS PASSED** (69/69 pinned entries byte-identical, Lean gate
included, 9 intentional `sorry` warnings); after the r291 sync (the
ridge-anatomy round, merged additively), fast mode **45/45 items
PASS, wall 57 s, ALL CHECKS PASSED** (70/70 pinned entries
byte-identical, Lean gate included, 9 intentional `sorry`
warnings); after the r292 sync (the curvature two-form round,
merged additively), fast mode **46/46 items PASS, wall 51 s, ALL
CHECKS PASSED** (71/71 pinned entries byte-identical, Lean gate
included, 9 intentional `sorry` warnings); after the r293 sync
(the metric-reconciliation round, merged additively), fast mode
**47/47 items PASS, wall 53 s, ALL CHECKS PASSED** (72/72 pinned
entries byte-identical, Lean gate included, 9 intentional `sorry`
warnings); after the r294 sync (the F10 stability round, merged
additively), fast mode **48/48 items PASS, wall 53 s, ALL CHECKS
PASSED** (73/73 pinned entries byte-identical, Lean gate included,
9 intentional `sorry` warnings); after the r295 sync (the F10
sp-hardening round, merged additively), fast mode **49/49 items
PASS, ALL CHECKS PASSED** (74/74 pinned entries byte-identical,
Lean gate included, 9 intentional `sorry` warnings); after the
wave-9 promotion (v966 pinned into the inventory, MODULES list
extended to eleven, consumption notes on the r296–r300 probes —
strictly additive next to the in-flight r301 worker), **full mode
65/65 items PASS, wall 489 s, ALL CHECKS PASSED** (81/81 pinned
entries byte-identical, all eleven modules green incl. v966 at
1.4 s, Lean gate included, 9 intentional `sorry` warnings); after
the r302 sync (the unif-target round, merged strictly additively
next to the landed wave-9 state — all pre-existing inventory
entries byte-identical), fast mode **56/56 items PASS, wall 59 s,
ALL CHECKS PASSED** (83/83 pinned entries byte-identical, Lean
gate included, 9 intentional `sorry` warnings); after the r303 sync
(the atom-target regress-audit round, merged strictly additively —
all 83 pre-existing pinned entries byte-identical, the two unpinned
living-document rows refreshed their informational SHAs as
expected), fast mode **57/57 items PASS, wall 62 s, ALL CHECKS
PASSED** (84/84 pinned entries byte-identical, Lean gate included,
9 intentional `sorry` warnings); after the r304 sync (the
short-range-law round, merged strictly additively — all 84
pre-existing pinned entries byte-identical), fast mode **58/58
items PASS, wall 62 s, ALL CHECKS PASSED** (85/85 pinned entries
byte-identical, Lean gate included, 9 intentional `sorry`
warnings); after the wave-10 promotion (v967 pinned into the
inventory, MODULES list extended to twelve, consumption notes on
the r301–r304 probes — strictly additive, all 85 pre-existing
pinned entries byte-identical), **full mode 70/70 items PASS,
wall 515 s, ALL CHECKS PASSED** (86/86 pinned entries
byte-identical, all twelve modules green incl. v967 at 1.3 s,
Lean gate included); after the r305 Lean reconstruction round
(RH/Closure.lean added, Inertia layer proved — Lean-only, no
pinned entry touched; run coexisting with the parallel wave-10
consolidation), fast mode **59/59 items PASS, wall 62 s,
ALL CHECKS PASSED** (Lean gate included, **4 intentional `sorry`
warnings** — down from 9: the master theorem, the fog-free hole
and four of the five Inertia statements are now PROVED; see the
Lean status below); after the r310 source-interface round
(RH/Source.lean added — Lean-only, no pinned entry touched; run
coexisting with the parallel r309 probe round), fast mode
**61/61 items PASS, wall 77 s, ALL CHECKS PASSED** (Lean gate
included, **5 intentional `sorry` warnings** — up from 4 by exactly
the documented opacity bridge `mainWindow_explicit_bridge`; the
four pre-existing holes are byte-identical; see the r310 Lean
status paragraph below); after the r310b source-theorem refinement
round (reviewer plan §8 adjudication — RH/Source.lean restructured
in place, Lean-only, no pinned entry touched), fast mode
**62/62 items PASS, wall 69 s, ALL CHECKS PASSED** (Lean gate
included, **5 intentional `sorry` warnings** — count unchanged: the
one Source.lean sorry MOVED into the reviewer target form
`mainWindow_iff_builtFromPrimeSource`, and the r310 form
`mainWindow_explicit_bridge` is now PROVED from it; the four
pre-existing holes are byte-identical; see the r310b Lean status
paragraph below); after the r313 sync (the Rényi-3 proof-form
fork round, merged strictly additively — all pre-existing pinned
entries byte-identical, run coexisting with the parallel
r309/r311 rounds), fast mode **63/63 items PASS, wall 68 s, ALL
CHECKS PASSED** (95 inventory entries with the r313 probe pinned,
Lean gate included, 5 intentional `sorry` warnings — unchanged);
after the r311 sync (the block-Green nontriviality round, merged
strictly additively — all pre-existing pinned entries
byte-identical, run coexisting with the parallel r309/r313
rounds), fast mode **64/64 items PASS, wall 77 s, ALL CHECKS
PASSED** (96 inventory entries with the r311 probe pinned, Lean
gate included, 5 intentional `sorry` warnings — unchanged);
after the r314 sync (the signed-cubic-flux round part 1, merged
strictly additively — all pre-existing pinned entries
byte-identical, run coexisting with the parallel r311 round),
fast mode **65/65 items PASS, wall 75 s, ALL CHECKS PASSED**
(97 inventory entries with the r314 probe pinned, Lean gate
included, 5 intentional `sorry` warnings — unchanged);
after the r315 sync (the Φ₃-functional round part 2, merged
strictly additively — all pre-existing pinned entries
byte-identical, run coexisting with the parallel r312 round),
fast mode **66/66 items PASS, wall 75 s, ALL CHECKS PASSED**
(98 inventory entries with the r315 probe pinned, Lean gate
included, 5 intentional `sorry` warnings — unchanged);
after the r316 sync (the two-regime-bound round part 3, merged
strictly additively — all pre-existing pinned entries
byte-identical, run coexisting with the parallel r312 round),
fast mode **67/67 items PASS, wall 76 s, ALL CHECKS PASSED**
(99 inventory entries with the r316 probe pinned, Lean gate
included, 5 intentional `sorry` warnings — unchanged);
after the r312 sync (the block-Green membership round, merged
strictly additively — all pre-existing pinned entries
byte-identical, run coexisting with the parallel r314/r315/r316
fiber rounds), fast mode **68/68 items PASS, wall 109 s, ALL
CHECKS PASSED** (100 inventory entries with the r312 probe
pinned, Lean gate included, 5 intentional `sorry` warnings —
unchanged); after the wave-11 promotion (v968 pinned into the
inventory via head-sync, MODULES list extended to thirteen,
consumption notes on the r306–r316 probes — strictly additive,
all 100 pre-existing entries byte-identical), **full mode 81/81
items PASS, wall 579 s, ALL CHECKS PASSED** (97/97 pinned entries
byte-identical, all thirteen modules green incl. v968 at 49.6 s,
Lean gate included, 5 intentional `sorry` warnings — unchanged);
after the r318 sync (the indefinite-fork round, merged strictly
additively — all pre-existing pinned entries byte-identical, run
coexisting with the parallel r317/r319 rounds), fast mode
**70/70 items PASS, wall 115 s, ALL CHECKS PASSED** (103
inventory entries with the r318 probe pinned, Lean gate included,
5 intentional `sorry` warnings — unchanged); after the r321 sync
(the continuous-coordinate round, merged strictly additively —
all pre-existing pinned entries byte-identical, run coexisting
with the parallel r318/r320 rounds), fast mode **71/71 items
PASS, ALL CHECKS PASSED** (104 inventory entries with the r321
probe pinned, Lean gate included, 5 intentional `sorry` warnings
— unchanged); after the r322 sync (the antiphase-sign-law dig
round, merged strictly additively — all pre-existing pinned
entries byte-identical, run coexisting with the parallel
r320/r321 rounds), fast mode **72/72 items PASS, wall 110 s, ALL
CHECKS PASSED** (105 inventory entries with the r322 probe
pinned, Lean gate included, 5 intentional `sorry` warnings —
unchanged); after the r324 sync (the QMAX × M₂ origin round plus
its superseded r324-pre pre-work probe, merged strictly
additively — all pre-existing pinned entries byte-identical, run
coexisting with the parallel wave-12 worker and R325, whose v969
module and r325 probe land in the same window), fast mode
**75/75 items PASS, wall 120 s, ALL CHECKS PASSED** (109
inventory entries with the r324-pre and r324 probes pinned, Lean
gate included, 5 intentional `sorry` warnings — unchanged); after
the r327 sync (the fold-group mass-cap round, merged strictly
additively — all pre-existing pinned entries byte-identical, run
coexisting with the parallel r326 Lean round), fast mode **76/76
items PASS, wall 125 s, ALL CHECKS PASSED** (110 inventory
entries with the r327 probe pinned, Lean gate included; the Lean
gate measured 8 intentional `sorry` warnings in this window — the
parallel r326 Lean round in flight, not a change of this sync).
This sync (r548–r553 Gabor EF / density / selection / theta /
config-first; r542–r547 already synced): `python rh/verification/run_rh.py --fast`
must end `RH SUITE: ALL CHECKS PASSED`.  NO RH CLAIM.

## Lean status

See `rh/lean/README.md` for the authoritative list. Summary: the Lean 4
project builds green. **r362 DualResolvent** (reviewer priority 2,
`RH/DualResolvent.lean`) puts the finite-matrix identity
`I−G† ≻ 0 ⟺ R† ≻ ½I` in the kernel graph (A2/A3/A4/A5/A7-min
sorry-free; `#print axioms` = `propext/Classical.choice/Quot.sound`
only). Census **8** by the ONE named transcription
`augmentedSubordination_iff_dualResolvent` (window L† ↔ the node-Gram
cone; same class as `pair_terminal_dictionary`).  NO RH CLAIM.
**r373 transcription round.** `RH/Haynsworth.lean` (two-rank J=I₂ and
mixed J-form, sorry-free) and the DualResolvent bridge
`augmentedSubordination_iff_dualResolvent` (μ-ONB Gram whitening,
sorry-free). Census **8 → 7**. Arch/pole kernels named
(`weilArchKernel`, `polePotential`); the two stabilization sorrys
remain (tent-read = pairing).  NO RH CLAIM.
**r376 extraction-close round.** `RH/Elementwise.lean`: pole-channel
stabilization **PROVED** (native-mesh second-difference of
`polePotential`, comb-parallel; `#print axioms` has no `sorryAx`;
named remainder `PoleDyadicIndependence`). Source-exact completion
demoted from `sorry` to named Prop `SourceExactOfFamilyCompletion`
(opaque `SourceExact` filling unprovable by design; residual opacity
is C1 `canonicalCompletion` — lag-kernels are not per-atom
arch/border/budget). Arch stabilization remains the ONE classical
sorry (mathlib v4.29.1: no Gauss integral / `Real.digamma` /
ψ-monotonicity / Mellin identifying `arch_A` with `weilArchKernel`).
`mainWindow_iff_builtFromPrimeSource` documented as Alt-Last (outside
the load-bearing chain since C1; not deleted). Census **7 → 5**.
NO RH CLAIM.
**r380 pivot-coordinate round.** `RH/PivotCoordinate.lean`: the five
DCCXXXVII finite-algebra lemmas in source pivot coordinates (rank-1
inertia and adaptive band **PROVED**; complementary dual-Hankel inertia
and `det K₂` ratio **named-decomposed** against Vandermonde/Haynsworth
plus DPP/Borodin named Props; Jacobi synthesis `p1_p2_iff_cap_posDef`
**PROVED** on the Hankel face). Zero new `sorry`; census **stays 5**.
Does not assert (P1)/(P2) on any window.  Coexists with r377/r378/r379
in `rh/problem/`.  NO RH CLAIM.
**r384 flank-entry round.** `RH/FlankEntry.lean`: kernel-anchor of
the r382 entry lemma against the r380 pivot layer. Pair-energy
identity, $h_0$/$h_1$ from mass and energy, the 3-atom flank
($h=(4,6,-3)$) and clustered run-of-3 ($H_3=-28500$) toys, Christoffel
$k=0,1$, and the composition `FlankEntryPrefix` $+$
`adaptive_band_from_entry` **PROVED**. Named Props `FlankEntryPrefix`
(inductive core through $\lfloor 2N/5\rfloor$) and
`ChristoffelPivotBound` (general-$k$ CD remainder). Ausgang
**benannt-ZERLEGT**. Zero new `sorry`; census **stays 5**.
Does not assert L* or (P1)/(P2).  NO RH CLAIM.
**r397 exact-selected-domain round.** `RH/Selected.lean`:
exact real domain and the one cofinal sequence (reviewer
Problems A/B on `CanonicalWindow`).  Sequence identities and
`weil_nonneg_of_selected_windows` **PROVED** (the latter consumes
the existing arch sorry).  Named mincut
`selected_augDualResolvent_gt_half`.  C1 holes degraded to
conjectures / alternative route, not deleted.  Zero new `sorry`;
census **stays 5**.  NO RH CLAIM.
**r406 one-defect Lean round.** `RH/OneDefect.lean`: general
rank-one absorption as finite matrix algebra (reviewer R406,
independent of source-side R404/R405).  SATZ A/B/C and the
min-norm Gram identity **PROVED** (`#print axioms` =
`propext/Classical.choice/Quot.sound` only).  Woodbury is
home-built (mathlib has Schur, not Woodbury).  Zero new
`sorry`; census **stays 5**.  NO RH CLAIM.
**r412 graph-resolvent Lean round.** `RH/GraphResolvent.lean`:
r407/r409/r411 dictionaries as sorry-free finite matrix
algebra (spectral bridge, Möbius inertia, energy-split
contraction, zero-defect $R^\dagger$ lift **PROVED**).  Named
Prop `GraphResolventIsLEnsembleInv`.  `#print axioms` =
`propext/Classical.choice/Quot.sound` only.  Zero new
`sorry`; census **stays 5**.  NO RH CLAIM.
**r426 edge-balance Lean round.** `RH/EdgeBalance.lean`:
r417–r425 identities as sorry-free finite algebra
(Woodbury-sch corollary of OneDefect, chart trichotomy,
$\tau^2$-separator, den formula, $\gamma$-bridge
$\|b\|^2\le S<B_w\Rightarrow\gamma<1$).  Named Props
`BorderIsMuParseval` / `BorderLoewnerLeS` / `QNLtOne`.
`#print axioms` = `propext/Classical.choice/Quot.sound` only.
Zero new `sorry`; census **stays 5**.  NO RH CLAIM.
**r430 semidefinite / frequently-selected round.**
`RH/FrequentlySelected.lean`: Loewner A3 and the FREQ
extraction **PROVED** (the latter consumes the existing
arch sorry).  Named mincut
`frequently_selected_augDualResolvent_ge_half`.  The r397
Prop `selected_augDualResolvent_gt_half` degraded to the
stronger alternative.  Density corollary and mean-value
trick **PROVED**.  Zero new `sorry`; census **stays 5**.
NO RH CLAIM.
**r434 quantifier-mincut audit.**
`RH/FrequentlySelected.lean` / `RH/Selected.lean` /
`RH/Open.lean`: the FREQ RH-path does **not** consume
`lstar_canonical` or `terminal_q_canonical` (kept as the
alternative rational-certificate route).  Real-window Loewner
`A_cap ⪰ 0` ⟺ `R† ⪰ ½I` **PROVED**;
`SelectedSemidefImpliesPlainReads` is a theorem of the thinner
remainder `SelectedACapPsdImpliesPlainReads` (Hankel/`fullRead`,
not the dual-resolvent cone).  Zero new `sorry`; census
**stays 5**.  NO RH CLAIM.
**r517–r532 Lean-only outer-bridge campaign.**
`RH/ExternalBridges.lean` / `RH/Open.lean` /
`RH/Audit.lean` (commits `4bf75f4f`–`7fb2dbb0`; no
sealed probe).  Sorry-free throughout except the
standing census of 7.  r517 `contour_identity_fixed_T`;
r518 ĥ-decay + `exists_gap_height`; r519 Borel–
Carathéodory wrappers + `norm_logDeriv_le_of_log_norm_le`;
r520 Landau gap sum; r521 `horizontalEdgeLandauBound`
**PROVED**; r522 parametric `contour_identity_fixed_T_of`;
r523 `exists_gap_sequence_landau` + ψ kernel; r524
A-parametric Landau; r525 route A; r526
`DigammaHorizontalLogBound` **PROVED**; r527 FE sliver;
r528 `horizontalEdgesTendstoZero` **PROVED**; r529
`leftEdgeLogDerivBound` **PROVED**; r530
`contourIdentityLimitAlongGaps` **PROVED** (full spectral
side of the explicit formula); r531 `hat_fourier_inversion`
**PROVED** (`standardExplicitFormula` is the spectral
pairing; identification stays a typed `sorry`); r532
`rightVerticalIntegral_eq_prime_sum` **PROVED** (`2Λ/√n`
gauge pinned, unclaimed).  Previously OPEN named
bridges now theorems:
`fullWeil_dyadic_sample_convergence`,
`gridPoleHatIntegralIdentity`,
`fullWeil_channel_continuity`.  Still OPEN:
`standard_explicit_formula_identification`,
`fullWeil_separates_offCritical_zeros`.  Census
**stays 7** (external 2; internal 5:
`lstar_canonical`, `terminal_q_canonical`,
`pair_terminal_dictionary`,
`mainWindow_iff_builtFromPrimeSource`,
`arch_gauss_mellin_digamma_identity`).  NO RH CLAIM.
**r534 Lean-only honest-contour round (outer-bridges 41).**
`RH/ExternalBridges.lean` (no sealed probe).  Sorry-free:
`contourExplicitFormula_honest(_complex)`,
`leftEdgeArchIntegral_eq_explicit_factor_integral`,
`honest_contour_explicit_formula_identification`
(theorem `HonestContourExplicitFormulaIdentification`).
Bridge-2 contour half **PROVED** (honest $\Lambda(1+n^{-1})$
form).  `standard_explicit_formula_identification` stays
honestly BLOCKED / **[O]** (corpus $2\Lambda/\sqrt{n}$ vs
contour; r537: class not preserved under $g\mapsto g\cosh(u/2)$).
`fullWeil_separates_offCritical_zeros` stays **[O]** (r535:
height-uniform construction required).  Lake 3545 jobs,
census **stays 7**.  NO RH CLAIM.
**r538 Lean-only honest-Weil-identification round (outer-bridges 42).**
`RH/ExternalBridges.lean` (no sealed probe).  Sorry-free:
`fullWeilFormHonest`,
`standard_explicit_formula_identification_honest`
(`fullWeilFormHonest = standardExplicitFormula`, no seam),
`fullWeilFormHonest_nonneg_iff_standard_nonneg`,
`honest_weil_criterion_to_mathlib_rh` (conditional on
`FullWeilSeparatesOffCriticalZeros`), `surplusComb`,
`archGaugeDelta`, decomposition
`fullWeilForm = fullWeilFormHonest + surplusComb + archGaugeDelta`.
No `sorryAx`.  Honest identification **CLOSED**; old corpus
sorry stays documented-blocked.  Separation stays **[O]**
(r541: certified numerical Gabor precheck, Lean campaign
licensed, no claim).  Lake 3545 jobs, census **stays 7**.
NO RH CLAIM.
**r542–r600 Gabor Lean campaign.** `RH/GaborSeparation.lean`
(r542/r547/r550/r558), `RH/GaborIntegral.lean` (r543),
`RH/GaborInequality.lean` (r544/r552/r579, alias
`gauss_density_transfer_binMax` + log transfer),
`RH/ZeroIncrement.lean` (r546), `RH/GaborThetaBound.lean`
(r552/r579), plus r555–r598: `GaborHatAnalytic`,
`GaborZeroSummable`, `GaborFEMultiplicity`,
`GaborHorizontalEdges`,
`GaborContourResidue`, `GaborVertical`,
`GaborLeftVertical`, `GaborAutocorrelation`,
`GaborVerticalLimit`, `GaborArchDigamma`,
`GaborArchContour`, `GaborExplicitFormula`,
`GaborDominance`, `GaborDominanceProof`,
`GaborDominanceAssembly`, `GaborDominanceLog`,
`GaborSpectralBridge`, `GaborDominanceLog2`,
`GaborArithmeticSeparator`, `GaborExposedOrbit`,
`GaborOuterTail`,
`GaborWindowGlue`, `GaborAnchoredWitness`.  EF front:
**PROVED in Lean** (r581; `gabor_vertical_arithmetic_remainder`
is a theorem).  Dominance: canonical constant + log +
BoundLog2 forms are theorems (r571/r575/r583); r573 audit
`STATEMENT_WEAKENED` (finite proxy).  r584–r588: tsum$\le$Closed
attachment, unrestricted On/Off-split, and weighted
Bridge-6 identification are **theorems**; $\zeta\ne 0$ on
$(0,1)$ real (Euler--Maclaurin, not Eta).  Unweighted
identification only `_of_simple`.  r589: window$\to$BoundLog2
bridge is a **theorem**; L2 verdict **BRIDGE\_A\_IS\_RH\_CORE**
(singleton route is not a translation lemma).  r590:
existential arithmetic endpoint + parallel Mathlib chain
without `scalingGaborTest`.  r591: fixed-packet cofinal
**only with extremality** (tie / free $\sigma'$ break).
r592: window-adaptive tail **CONDITIONAL** (IEEE $\omega$-floor
at extreme near-tie).  r593/r594: outer-tail **theorem**
(tsum$\le$exp and tail$<\varepsilon\cdot E$).  r595: three-term
glue + per-$T$ checkpoint are **theorems**; named gap
`GaborWindowAdaptiveUniformDelta`.  r596–r598: L2
**ANKER\_TEILWEISE**; log-glue **theorem**; zeroSide $<0$
at own packet; Cover is the remaining geometric rest.
`GaborSpectralToArithmetic` is a **proved** pole-sign
lemma (`GaborSpectralToArithmetic_holds`), **not** RH-core
(r600).  `GaborAnchoredWitnessExists` **not** asserted.
**r599/r600 vacuity (2026-09-01/02):** `gaborSpectralFormula`
is not the Weil functional; old hpos is FALSE; live object
`gaborZeroSide`; historical Mathlib wrappers **VACUOUS**.
Live: `gabor_zeroSide_inputs_to_mathlib_rh` and companions.
Open pieces:
`GaborAnchoredCoverAt` (ordinate clusters),
`GaborAnchoredWitnessExists`,
`GaborWindowAdaptiveUniformDelta` ($T$-uniform $\delta$;
lex host-retune), `GaborTruncationUniformNeg` (does NOT follow
from BoundLog2), `GaborWeightedTruncationGammaDistinct`,
`GaborFixedPacketCofinalNegAt` (extremality gap),
unasserted Prop `GaborSeparationForAllZeros` (r612: asserting
theorem retired).  Named open
(no claim): tsum $Z(F_0)<\pi e^{1/8}$; on-line positivity
beyond $\langle 1,0,0\rangle$ without `hline`.  Scramble-gate
passed (r565).  Endpoint remains a conditional reduction
on `gaborZeroSide` / unasserted `GaborSeparationForAllZeros`.  Tracked sorry census
**9 → 8** at r581; stayed **8** through r605 (2026-09-02);
**8 → 7** at r612 (GaborSeparation 0);
**7 → 5** at r638L by retiring two wrong-type assertions to unasserted Props.
r601 **DOMINANCE\_FAILS** (fixed-$a$ subfamily, not hpos*).
r603 two-key GP discriminatively empty.
r604 TFPT/zero cross-corr **ARTIFACT**.
r605A `GaborZeroSideForAllZeros` **FORALL\_ZERO\_OVERSPECIFIED**.
r605N **EXPOSED\_ORBIT\_HOLDS** ($40/40$).
r605B+C `GaborExposedOrbit.lean` sorry-free; live
`gabor_zeroSide_pure_criterion_iff_rh_unconditional`.
RH $\Leftrightarrow$ nonnegativity of the pure Gabor zero-side
on the two-parameter family $(a,\omega)$.  Sharpest live
statement (r634L): RH $\Leftrightarrow$ $\forall$ rational
$(a,\omega)$: POLE $-$ PRIME $+$ ARCH $\ge 0$; positivity of
`gaborZeroSide` itself remains open.  Not an RH proof.
r605C-AUDIT **STATEMENT\_SOUND**.
r607 Lindblad two-key **KILLED(RECOORDINATIZATION)** ($15/15$).
r608 tropical heat **TROPICAL\_CONFIRMED** ($9/9$); HEAT.SOURCE **NOGO T1**.
r609 E8 readout **E8\_READOUT\_SEALED(7/8)** ($49/49$); no prime bridge; promotion pending.
r610 `GaborLowHeightZeroFree` $T_0$ unasserted; `gaborSpectralFormula_refuted_of_lowHeight`.
r611 Aubin--Nitsche **OBS\_NOT\_CONVERGING** ($12/12$); Herglotz closure STOP.
r612 countable criterion; census **7**; modules $53\to 54$.
r612C continuity discharged; rational criterion **unconditional**; census stays **7**; module $551$ lines.
r613 ordered-E8 Herglotz **NO\_IDENTIFICATION**; Paket C dead.
r615 first-prime-step **FIRSTSTEP\_LEAKAGE\_CONTROLLED** ($26/26$); named lemma **PRIME.SEMILOCAL.ODDSECTOR.EDGE.01** [O] (r620 retype, oriented); r496 confirmed.
r616 higher-moment inertia **C\_CAPPED** ($16/16$); $p_3^{\mathrm{uncond}}=p_2=0.6818$.
r617 Coxeter Euler completion **COMPLETION\_EXACT** ($45/45$); no-go **E8.COXETER.REGULARIZED\_SPLIT.NO\_GO.01**; promotion in progress.
r617L Lean `CoxeterCompletion` + `PrimeLogIndependence`; census **7**; modules $54\to 56$.
r618 Jensen-compiler rigidity **COMPILERS\_STRUCTURALLY\_RIGID** ($43/43$); E8 RH-neutral.
r619 support-relay census **RELAY\_UNIVERSAL** ($12/12$); greedy $\Delta\approx 0.015$ WITHDRAWN by r635; $L_{\mathrm{det}}$; RH-in-a-box beyond $L\approx 0.5$.
r620 P2 reflection factor **MIXED\_SECTOR** ($73/73$); ODDSECTOR lemma retyped oriented.
r621 P2 digamma duplication **DUPLICATION\_CONSTANT\_ONLY** ($37/37$); prime-2 is not a duplication factor.
r622 support Darboux **TRANSPORT\_FEASIBLE\_NORULE** ($64/64$); no source-side rule.
r623 P2 dilation **P2\_DILATION\_STRUCTURALLY\_BLOCKED** ($128/128$); principal-block/Schur obstruction; literature $\sqrt{2}$; lane not opened.
r625 IIKS vanishing metric **IIKS\_NO\_METRIC\_IN\_CLASS** ($19/19$); prose NOT\_TESTABLE\_IN\_CORPUS\_FORM; wrong RHP object; no metric in class.
r626 finite-free collision **COLLISION\_DETECTOR\_CALIBRATED\_NO\_BARRIER** ($51/51$); barrier tautological.
r627 A--F two-moment optimizer **NO\_GAIN** ($17/17$); Montgomery--Taylor $p^*=0.6725007037$; gap $9.3\cdot 10^{-3}$ not closable in class.
r628 window-box verifier **COMPRESSION\_CERTIFIED\_BOX\_NUMERICAL** ($12/12$); rigor blocked by $S(T)$ looseness.
r629 certificate-class atlas **ATLAS\_NO\_NEW\_UNCONDITIONAL\_GAIN** ($15/15$); only support $>1$ correlation buys proportion.
r632 jet deflation **JET\_GAIN\_SMALL** ($14/14$); coverage collapse above Nyquist.
r630/r630b margin-law symreg **MARGIN\_LAW\_UNRESOLVED** / **N\_LIMITED\_ARTIFACT** ($19/19$); slopes $-50.6/-116$; density-driven RH-neutral; no universal dBN gap barrier.
r633 frontier follow-ups **RANDOM\_EULER\_REFUTED** stands ($16/16$); $C=1$ not the mechanism (r637); F4 VOID.
r635 lead precision **LEAD\_PARTIAL** ($11/11$); greedy law WITHDRAWN; four leads $0.0253/0.0083/0.0064/0.0034$; $q\ge 7$ UNMEASURABLE.
r636 lead law **LEAD\_LAW\_PARTIAL** ($6/6$); no model on four points; message dissolved.
r637 vote map **VOTE\_MODE\_SPECIFIC** + **FLIP\_COUNTEREXAMPLE** ($14/14$); unanimity GENERIC; $C$ not a positivity predictor.
r639 Lamzouri Hilbert variant **SAME\_CLASS** + **CONSTANTS\_IDENTICAL** + **WALL\_LOCATION\_CONFIRMED** ($23/23$); two-moment class A1 unchanged; $C_0 = p^*$ (r627); sole arithmetic input pair correlation $|\alpha| \le 1$; NO\_IMPORT unchanged.
Decoding r635--r637: no side channel beyond the explicit formula (margin collapse + edge geometry).
r638 first-contact/Selberg **KILLED(STRUCTURAL)** ($14/14$); Selberg convolution is Hankel, no Toeplitz square; Euler-local squares cost $\ge 3.28\times$ budget; contact conditions collapse to one; sign world-blind.
r606b prolate residual-gap **INCONCLUSIVE** (evals/disc); lane CLOSED (superseded by r611 + KILLED(FACTORIZATION)).
r631L sorry classification R/T/A (census **7**, no closure); `GaborContourLimitRemainder` PROVED.
r634L pure-class EF **unconditional**; prime-side rational criterion `gabor_primeSide_rational_criterion_iff_rh` (axioms propext/choice/Quot.sound); census stays **7**.
r638L overstrong arch equality and gauge-mismatched corpus EF assertion retired; Lean 3578/3578; census **5**; honest contour retained; no RH claim.
r475-repair fixed `archRateConst` FALSIFIED ($8.0283>4.126$); $\exists C$ form OPEN (`SelectedArchWeightedInterpolationEstimate`); tendsto consumer proved; Lean 3578/3578; census **5**; catalog `part_18` KILLED/LOSSY_CONSTANT; no RH claim.
Second cut (r623/r625/r626) closed negative; r627/r628/r629/r630/r632/r633/r635/r636/r637/r638/r639 do not reopen a positivity lane.
Separation stays **[O]**.  NO RH CLAIM.
**r431 coexistence.** Round 431 (`source_potapov.tex`) is
additive on the reviewer Potapov discovery lane after
DCCXCVII; it does not touch `rh/lean/`. Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`).
Ausgang `SOURCE_FACTOR_NOT_FOUND`.  NO RH CLAIM.
**r431-AUDIT coexistence.** Round 431-AUDIT
(`r431_audit.tex`) is an adversarial re-check of that
verdict (non-commuting $J$-factors, independent numbers,
second Cauchy--$\pi$ window).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
Ausgang `CONFIRMED`.  NO RH CLAIM.
**r433 coexistence.** Round 433 (`edge_redheffer_probe.py`)
is additive on the $R^{\dagger}$ Potapov lane after r362/r369
and r429 (reviewer DCCXCVII Teil D: the border as an
identifiable Redheffer/Schur step).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(the Cayley mixed-form bridge is not in Lean).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the
sealed probe and the problem-document rows to the
inventory.  r430 is the parallel Lean quantifier lane
and is not dropped.
**r435 coexistence.** Round 435 (`p1_overload_probe.py`)
is additive on the $R^{\dagger}$ P1 lane after r400/r407.
It does not touch `experiments/next.txt` or `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r436 coexistence.** Round 436 (`p2_determinant_probe.py`)
is additive on the $R^{\dagger}$ P2 lane after r367/r369/r375/r377
(reviewer Hauptlane second half: exact reverse-CS
$2\times 2$ analysis of $\det K_{2}$).  It does not touch
`experiments/next.txt` or `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r438 coexistence.** Round 438 (`evolutionary_certificate_probe.py`)
is additive on the search lane (A/B/C NOT_FOUND).
It does not touch `experiments/next.txt` or `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r439 coexistence.** Round 439 (`residual_loewner_probe.py`)
is additive on the $R^{\dagger}$ interpolant-residual lane
after r431/r431-audit/r433 (reviewer DCCCIV:
Loewner/Bezout of $D_0=W_Y-S_0$).  It does not touch
`experiments/next.txt` or `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r440 coexistence.** Round 440 (`mean_tau_index_probe.py`)
is additive on the reviewer DCCCIV fallback lane (averaged
tau-winding as an exact integer; identities first, no
unconditional bound).  It does not touch
`experiments/next.txt`.  The Lean landing site
`exists_index_zero_of_block_mean_lt_one` is already proved
(r430); this round does not add Lean.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the sealed probe and the problem-document rows
to the inventory.  r434 / r435 / r436 / r438 are parallel
and are not dropped.
**r441 coexistence.** Round 441 (`diag_lifts_loewner_probe.py`)
is additive on the $R^{\dagger}$ interpolant-residual lane
after r439 (reviewer DCCCX: DIAG_LIFTS / diagonal lift
of $L_{-\widetilde{m}}$).  It does not touch
`experiments/next.txt` or `rh/lean/`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r442 coexistence.** Round 442 (`block_mean_probe.py`)
is additive on the reviewer-R439 unconditional-mean
lane after r440 (dictionary $\kappa^{\dagger}=1\{q^{\dagger}>1\}$;
unsigned majorant dead; mean bound open).  It does not
touch `experiments/next.txt`.  The Lean landing site
`exists_index_zero_of_block_mean_lt_one` is already
proved (r430); this round does not add Lean.  Suite
surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r443 coexistence.** Round 443 (`delta_floor_probe.py`)
is additive on the r421/r442 floor lane (`\delta=1-q^{\dagger}`
as the reserve floor in the last-pivot coordinate).
It does not touch `experiments/next.txt` or add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r444 coexistence.** Round 444 (`signed_border_mean_probe.py`)
is additive on the reviewer-R439 signed-mean lane after r442
(triple sum; pole not carrier; circularity gate).  It does
not touch `experiments/next.txt`.  The Lean landing site
`exists_index_zero_of_block_mean_lt_one` is already proved
(r430); this round does not add Lean.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`).
**r445 coexistence.** Round 445 (`deep_builder_probe.py`)
is additive on the r443 floor-fit infra lane (unlock
`border_chain_pack` for selected $k=10/11/12$).  It does
not touch `experiments/next.txt`.  The Lean landing site
`exists_index_zero_of_block_mean_lt_one` is already proved
(r430); this round does not add Lean.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`).
**r446 coexistence.** Round 446 (`deep_abd_probe.py`)
is additive on the r445 ABD-living / floor-fit infra
lane (REAL vs FLOAT adjudication of the deep breaks).
It does not touch `experiments/next.txt`.  The Lean
landing site `exists_index_zero_of_block_mean_lt_one`
is already proved (r430); this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r447 coexistence.** Round 447 (`exact_atom_probe.py`)
is additive on the r446 exact-vs-float atom fork
(EXACT_DEAD: the true k=10 window still flips).
It does not touch `experiments/next.txt`.  The Lean
landing site `exists_index_zero_of_block_mean_lt_one`
is already proved (r430); this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r448 coexistence.** Round 448 (`exact_band_probe.py`)
is additive on the r447 exact-atom builder
(NOT_COFINAL: the exact band ends at kz136;
2^k commensurability refuted; next-odd fails).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r449 coexistence.** Round 449 (`flip_vs_stab_probe.py`)
is additive on the r448 band census
(TAIL_ONLY: chain flips sit past n_stab;
prefix-R^dagger lives; mincut already is prefix).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r450 coexistence.** Round 450 (`prefix_mincut_probe.py`)
is additive on the r449 n_stab census
(M2_UNDECIDED: n_stab-delta chart prefers M2;
living full vs prefix split; chi prefix lives).
It does not touch `experiments/next.txt`.  Lean
names the prefix mincut by Iff.rfl; census stays 5.
Suite surface: integrity + probes + Lean
(`run_rh.py --fast`).
**r451 coexistence.** Round 451 (`nstab_transition_probe.py`)
is additive on the r449/r450 n_stab census
(TRANSITION_SMOOTH: no universal cliff at
n_stab; RES_MISMATCH; PREFIX_Q_PLATEAU).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r452 coexistence.** Round 452 (`plateau_theorem_probe.py`)
is additive on the r451 plateau census
(PLATEAU_IDENTITY_PROVED: q_* = M_d/(M_d+5/7)
on M_d = mu_0-nu_0; QSTAR_UNDECIDED).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r453 coexistence.** Round 453 (`border_mass_probe.py`)
is additive on the r452 plateau SATZ
(BOUND_PROVED: q_n = S_{n-1}/B_w;
MASS_CLASSICAL_REDUCED_GROWING; RACE_WON).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r454 coexistence.** Round 454 (`limit_object_probe.py`)
is additive on the r453 cofinal collapse
(LIMIT_CLASSICAL: m_inf = m_ARCH for j>=2;
LIMITCHAIN_ALIVE_200; CHAIN_DOCUMENTED).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r455 coexistence.** Round 455 (`arch_chain_probe.py`)
is additive on the r454 limit object
(L3_PROVED eventual per n; L1_PNT_SUFFICIENT,
actual strength elementary; CHAIN_MAPPED).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r456 coexistence.** Round 456 (`vacuity_redteam_probe.py`)
is a red-team of the r450–r455 prefix-mincut
(VACUOUS_CONFIRMED: Python prefix is prime-blind;
`Iff.rfl` is a naming of the full-cap cone).
It does not touch `experiments/next.txt`.  Lean census
comments retract the compression reading of `Iff.rfl`;
no new `sorry`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r457 coexistence.** Round 457 (`jp_increment_probe.py`)
accepts r456 and studies the J_P increment
(INCREMENT_DRIFT; RACE_EATS_K10; LEMMA_REDUCED).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r458 coexistence.** Round 458 (`cofinal_family_probe.py`)
is additive on the r456 full-cap retyping
(FAMILY_CANDIDATE: Lean selectedMesh lives;
TABLE_CAP_ARTEFACT on the frame-A 2^k deaths;
residual deep death kz137).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r459 coexistence.** Round 459 (`fullcomb_cleanup_probe.py`)
cleans the TABLE_CAP-contaminated r457 race
(RACE_TREND_BROKEN; LEANFAM_EXACT_ALIVE(12);
KZ137_OUTSIDE_MINCUT).
It does not touch `experiments/next.txt`.  The Lean
landing site is unchanged; this round does not add Lean.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r460 coexistence.** Round 460 (`race_proof_probe.py`)
is a PARTIAL proof attempt: exact spectral reduction and a finite
two-band certificate, with the cofinal source-derived spectral-overlap
estimate left open.  It does not touch `experiments/next.txt`, the
ledger, or Lean, and makes no RH claim.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r468 coexistence.** Round 468 (`octave_renorm_probe.py`)
tests the octave-renormalization cut
(OCTAVE_NOT_CAUCHY; EDGE_TWO_POINTS; REDUCTION_ALIAS).
It does not touch `experiments/next.txt`.  File domain
disjoint from r467.  The Lean landing site is unchanged.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r469 coexistence.** Round 469 (`correlation_wall_judgment.tex`)
is a pure adjudication (U1 INTERNALLY_EXHAUSTED; U3
REDIRECT_TO_FIXED_L).  It does not touch
`experiments/next.txt` or Lean.  Binding anti-list.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r470 coexistence.** Round 470 (`quadrep_probe.py`) seals
F1(i) as OBSTRUCTION_SEALED.  File domain is InnerBridges.lean,
the probe, the problem note, INVENTORY, and these status lines.
It does not touch `experiments/next.txt`.  Census stays 8.
Suite surface: integrity + probes + Lean
(`run_rh.py --fast`).
**r471 coexistence.** Round 471 (`classical_cert_probe.py`) seals
dictionary-free grid certificates GRID_CERTIFIED($L_{\max}=2.7726$).
File domain is the probe, `classical_cert.tex`, the verifier,
INVENTORY, `run_rh.py`, and these status lines.  It does not
touch Lean or `experiments/next.txt`.  Suite surface: integrity
+ probes (`run_rh.py --fast --skip-lean`).
**r474 coexistence.** Round 474 (`modulus_upgrade_probe.py`) seals
F2b as PARTIAL (lemmas proved, quantitative close STUCK).
File domain is the probe, `modulus_upgrade.tex`, the verifier,
INVENTORY, `run_rh.py`, and these status lines.  It does not
touch Lean or `experiments/next.txt`.  Suite surface: integrity
+ probes (`run_rh.py --fast --skip-lean`).
**r473 coexistence.** Round 473 (`extraction_joint_probe.py`) seals
F1-joint redesign as ARTEFACT + POLY_BRIDGE_PROVED.  File domain
is InnerBridges.lean, FrequentlySelected.lean, Open.lean,
Audit.lean, the probe, the problem note, INVENTORY, and these
status lines.  It does not touch `experiments/next.txt`.
Census stays 8.  Suite surface: integrity + probes + Lean
(`run_rh.py --fast`).
**r475 coexistence.** Round 475 (`arch_rate_probe.py`) isolates
F1(ii) and names the $O(\Delta^2)$ tent rate at fixed $f$
(numeric large-support ratios $3.85$--$3.99$).  The fixed
`archRateConst` is FALSIFIED at r475-repair (see that entry).
File domain is Elementwise.lean, InnerBridges.lean, Open.lean,
Audit.lean, the probe, the problem note, INVENTORY, and these
status lines.  It does not touch `experiments/next.txt`.
Census stays 8.  Suite surface: integrity + probes + Lean
(`run_rh.py --fast`).
**r475-repair coexistence.** Lean repair round
(`RH/SelectedArchErrorQuadraticRateClassical.lean`, catalog
`part_18`): falsifies the fixed `archRateConst`, adds the
$\exists C(f)$ interface, proves the tendsto consumer, leaves
`SelectedArchWeightedInterpolationEstimate` OPEN.  File domain
is InnerBridges.lean, SelectedArchErrorQuadraticRateClassical.lean,
Audit.lean, Lean README, INVENTORY, catalog `part_18`, and these
status lines.  It does not touch `experiments/next.txt`.
Census stays **5**.  Suite surface: integrity + probes + Lean
(`run_rh.py --fast`).
**r476 coexistence.** Round 476 (`crossterm_probe.py`) seals
the first-mode Rayleigh as UNCONDITIONAL(L_max=2.7726) on
the declared H^2 ball (not lambda_*).  File domain is the
probe, `crossterm.tex`, the verifier, INVENTORY, `run_rh.py`,
and these status lines.  It does not touch Lean or
`experiments/next.txt`.  Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r477 coexistence.** Round 477 (`highmode_probe.py`) seals
the high-mode / Schur architecture at L=0.3,0.8,1.0
(not lambda_*).  File domain is the probe, `highmode.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r478 coexistence.** Round 478 (`endtoend_fixedl_probe.py`)
seals the even Fourier block SATZ at L=0.3 (N=2..5 PD) and
records the tail-Schur obstruction (not lambda_*).  File
domain is the probe, `endtoend_fixedl.tex`, the verifier,
INVENTORY, `run_rh.py`, and these status lines.  It does
not touch Lean or `experiments/next.txt`.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`).
**r479 coexistence.** Round 479 (`lambdastar03_probe.py`)
reduces lambda_*(0.3)>=0 to a high-band coupling bound
(not lambda_*).  File domain is the probe, `lambdastar03.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r480 coexistence.** Round 480 (`kappa_high_probe.py`)
kills the r479 operator-norm remainder and reduces
lambda_*(0.3)>=0 to a refined even matrix Schur
(not lambda_*).  File domain is the probe, `kappa_high.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r481 coexistence.** Round 481 (`schur_cert_probe.py`)
lifts epsilon and kills the Fourier/sigma^2 routes;
the remainder is an oscillatory tail integral
(not lambda_*).  File domain is the probe, `schur_cert.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r482 coexistence.** Round 482 (`carleson_edgeband_probe.py`)
shows the Carleson sufficient rule fails the finite census
and the restricted large sieve is the target
(not a Carleson law).  File domain is the probe,
`carleson_edgeband.tex`, the verifier, INVENTORY,
`run_rh.py`, and these status lines.  It does not
touch Lean or `experiments/next.txt`.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`).
**r483 coexistence.** Round 483 (`filon_enclosure_probe.py`)
encloses the two integral classes of the refined Schur
and records the leftover-$C$ deficit
(not lambda_*).  File domain is the probe, `filon_enclosure.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r484 coexistence.** Round 484 (`block_completion_probe.py`)
falsifies the 20x leftover drop and records garbage jets
plus QR-IBP killing S
(not lambda_*).  File domain is the probe, `block_completion.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r485 coexistence.** Round 485 (`weighted_schur_probe.py`)
measures the frequency of leftover C (A-GO) and
records a finite weighted Schur that is PD, with
operator M_inf on the true complement left open
(not lambda_*).  File domain is the probe, `weighted_schur.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r486 coexistence.** Round 486 (`woodbury_minf_probe.py`)
represents the negative-symbol enemy $A^-$ by three
certified Slepians of $K_{t_c}$ and records a finite
Birman--Schwinger number $<1$, with operator $R^{-1}$
left open
(not lambda_*).  File domain is the probe, `woodbury_minf.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r487 coexistence.** Round 487 (`outer_bridges_probe.py`) starts
the permanent outer-bridge Lean lane.  File domain is
`RH/ExternalBridges.lean`, `RH/Audit.lean`, `RH/Open.lean`, Lean and
RH READMEs, the probe, `outer_bridges.tex`, verifier, INVENTORY, and
`run_rh.py`.  It does not touch `experiments/next.txt`.
Suite surface: integrity + probes + Lean (`run_rh.py --fast`).
**r488 coexistence.** Round 488 (`resolvent_solve_probe.py`)
shows $R=A^++\Pi$ is not coercive, records a shifted
$G$-certificate $<1$ on $V_n$, and leaves the operator
$R$-gap open
(not lambda_*).  File domain is the probe, `resolvent_solve.tex`,
the verifier, INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or `experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r489 coexistence.** Round 489 (`outer_bridges2_probe.py`) closes
finite-comb and standard polar-integral continuity and reduces the
dense bridge to one completion sorry.  File domain is
`RH/ExternalBridges.lean`, `RH/Audit.lean`, `RH/Open.lean`, Lean and
RH READMEs, the probe, `outer_bridges2.tex`, verifier, INVENTORY, and
`run_rh.py`.  It does not touch `experiments/next.txt`.
Suite surface: integrity + probes + Lean (`run_rh.py --fast`).
**r490 coexistence.** Round 490 (`operator_residual_probe.py`)
measures the operator leftover of the r488
certificate solves, records off/s $=5.86$
against the $5.6\cdot10^{-3}$ margin, and
freezes the $0.3$ keystone
(not lambda_*).  File domain is the probe,
`operator_residual.tex`, the verifier,
INVENTORY, `run_rh.py`, and these status
lines.  It does not touch Lean or
`experiments/next.txt`.
Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r491 coexistence.** Round 491 (`outer_bridges3_probe.py`) finds
the omitted arch component, repairs the polar sign, and narrows the
completion to explicit dyadic convergence, arch continuity, and the
finite-hat pole identity.  File domain is `RH/ExternalBridges.lean`,
`RH/Audit.lean`, `RH/Open.lean`, Lean and RH READMEs, the probe,
`outer_bridges3.tex`, verifier, INVENTORY, and `run_rh.py`.  It does
not touch `experiments/next.txt`.  Suite surface: integrity + probes +
Lean (`run_rh.py --fast`).
**r492 coexistence.** Round 492 (`keystone_judgment.tex`) is a pure
adjudication note on the frozen $0.3$ keystone.  It adds no probe, no
verifier and no pin, and it does not touch `rh/lean/` (r491 runs there
in parallel) or `experiments/next.txt`.  File domain is
`rh/problem/keystone_judgment.tex(+pdf)`, `make_inventory.py`,
`INVENTORY.json` and this README.  Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r494 coexistence.** Round 494 (`kernel_loewner_probe.py`) proves the
fixed-support Weil operator floor at $L=0.3$ in the x-space kernel
form.  It does not touch `rh/lean/` (parallel r493c1 owns that tree),
the main verification/ledger/docset, or `experiments/next.txt`.
File domain is the probe, `kernel_loewner.tex(+pdf)`, its verifier,
INVENTORY, `run_rh.py`, and the experiments/RH READMEs.  Suite
surface: integrity + probes (`run_rh.py --fast --skip-lean`).
**r495 coexistence.** Round 495
(`kernel_redteam_probe.py`) is an adversarial audit of the r494
fixed-support floor.  It does not touch `rh/lean/` (parallel r493d owns
that tree), the main verification/ledger/docset, or
`experiments/next.txt`.  File domain is the probe,
`kernel_redteam.tex(+pdf)`, its verifier, INVENTORY, `run_rh.py`, and
the experiments/RH READMEs.  Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r502 coexistence.** Round 502 (`l08_judgment.tex`) is a pure
adjudication note on the r496 no-go at $L=0.8$.  It adds no probe, no
verifier and no pin, and it does not touch `rh/lean/` (r501 runs there
in parallel), the main verification/ledger/docset, or
`experiments/next.txt`.  File domain is
`rh/problem/l08_judgment.tex(+pdf)`, `make_inventory.py`,
`INVENTORY.json` and this README (which also picks up the missing r496
status block).  Suite surface: integrity + probes
(`run_rh.py --fast --skip-lean`).
**r517–r532 coexistence.** Rounds 517–532 are a Lean-only
outer-bridge campaign (no sealed probe, no pin on
`ExternalBridges.lean` because a parallel editor owns that
file).  File domain is `RH/ExternalBridges.lean`,
`RH/Open.lean`, `RH/Audit.lean`, `make_inventory.py`,
`INVENTORY.json`, `run_rh.py`, and this README.  It does
not touch `experiments/next.txt`, the main
verification/ledger/docset, or any probe.  Suite surface:
integrity + probes (`run_rh.py --fast --skip-lean`).
Census stays 7.  NO RH CLAIM.
**r534 coexistence.** Round 534 is Lean-only (no sealed probe,
no pin change on `ExternalBridges.lean`).  File domain is
`RH/ExternalBridges.lean`, this README, `run_rh.py` (gap
comment), and `experiments/next.txt`.  It does not add a
probe row.  Census stays 7.  NO RH CLAIM.
**r535 coexistence.** Round 535 (`weil_separation_redteam_probe.py`)
is additive on the separation sorry.  It does not touch
`rh/lean/` (the sorry stays).  File domain is the probe,
INVENTORY, `run_rh.py`, this README, and `experiments/next.txt`.
Suite surface: integrity + probes (`run_rh.py --fast`).
NO RH CLAIM.
**r536 coexistence.** Round 536 (`kernel_loewner_window_probe.py`)
maps the r494 tail method; r502 already closed the
$\lambda^*$-ladder as a proof route for $L\ge 0.45$, so this
is not a reopened window.  File domain is the probe,
INVENTORY, `run_rh.py`, this README, and `experiments/next.txt`.
Suite surface: integrity + probes (`run_rh.py --fast`).
NO RH CLAIM.
**r537 coexistence.** Round 537 (`honest_contour_audit_probe.py`)
audits the r534 honest contour identity.  It does not touch
`rh/lean/`.  File domain is the probe, INVENTORY, `run_rh.py`,
this README, and `experiments/next.txt`.  Suite surface:
integrity + probes (`run_rh.py --fast`).  NO RH CLAIM.
**v1017 coexistence.** The 2026-09-01 promotion of r494/r495
to `verification/v1017_kernel_loewner_positivity.py` is
[Numerical/certified], not [E].  File domain of this rh-sync
note is this README and `experiments/next.txt`; the module,
ledger row, and `rh/paper` §2 certbox were added in the
promotion change.  NO RH CLAIM.
**r538 coexistence.** Round 538 is Lean-only (no sealed probe,
no probe row; gap like r534).  File domain is
`RH/ExternalBridges.lean`, `RH/Open.lean`, this README,
`run_rh.py` (gap comment), and `experiments/next.txt`.
It does not add a probe row.  Census stays 7.  NO RH CLAIM.
**r539 coexistence.** Round 539 (`weil_gaussian_separation_probe.py`)
is additive on the separation sorry.  It does not touch
`rh/lean/` (no Gaussian-campaign mandate).  File domain is
the probe, INVENTORY, `run_rh.py`, this README, and
`experiments/next.txt`.  Suite surface: integrity + probes
(`run_rh.py --fast`).  NO RH CLAIM.
**r540 coexistence.** Round 540 (`weil_online_null_separation_probe.py`)
closes compact-class on-line nulling as a certification path.
It does not touch `rh/lean/`.  File domain is the probe,
INVENTORY, `run_rh.py`, this README, and `experiments/next.txt`.
Suite surface: integrity + probes (`run_rh.py --fast`).
NO RH CLAIM.
**r541 coexistence.** Round 541 (`weil_gabor_separation_probe.py`)
is a certified numerical precheck of the separation sorry
(Gabor scaling law).  Lean campaign licensed, no claim;
the sorry stays **[O]**.  It does not touch `rh/lean/`.
File domain is the probe, INVENTORY, `run_rh.py`, this
README, and `experiments/next.txt`.  Suite surface:
integrity + probes (`run_rh.py --fast`).  NO RH CLAIM.
**r542 coexistence.** Round 542 is Lean-only
(`RH/GaborSeparation.lean`; identities + reduction chain
sorry-free; four named classical inputs).  No sealed probe.
Census later 7 → 9 at r547.  NO RH CLAIM.
**r543 coexistence.** Round 543 is Lean-only
(`RH/GaborIntegral.lean`; integral representation proved).
No sealed probe.  NO RH CLAIM.
**r544 coexistence.** Round 544 seals
`gabor_uniform_inequality_probe.py` and adds the sorry-free
`RH/GaborInequality.lean` kernel.  Global inequality not
proved; separation stays **[O]**.  File domain is the probe,
the Lean kernel, INVENTORY, `run_rh.py`, this README, and
`experiments/next.txt`.  NO RH CLAIM.
**r545 coexistence.** Round 545 is analysis only (Path A
chosen).  No artefact.  NO RH CLAIM.
**r546 coexistence.** Round 546 is Lean-only
(`RH/ZeroIncrement.lean`; increment bound proved).  No
sealed probe.  NO RH CLAIM.
**r547 coexistence.** Round 547 rebuilds
`RH/GaborSeparation.lean` onto the Path-A increment.
Endpoint two hypotheses; census 10 → 9.  File domain is
the Lean file, INVENTORY, `run_rh.py` (census-gate 7 → 9
on r487/r489/r491), this README, and
`experiments/next.txt`.  NO RH CLAIM.
**r548 coexistence.** Round 548 seals
`weil_gabor_explicit_formula_probe.py`
(VERDICT EF_CONFIRMED).  Classical identity confirmed;
`(1+1/n)` gauge is a false contour inversion.  No Lean
edit in this round.  File domain is the probe, INVENTORY,
`run_rh.py`, this README, and `experiments/next.txt`.
NO RH CLAIM.
**r549 coexistence.** Round 549 seals
`gabor_density_transfer_probe.py`
(TRANSFER_UNIFORM + OFFLINE_ADVERSARIAL).  Discrete
transfer uniform; off-line remains adversarial.  NO RH CLAIM.
**r550 coexistence.** Round 550 is Lean-only
(`RH/GaborSeparation.lean` EF renormalized to
`combMass = 2*Lambda/sqrt(n)`).  No sealed probe.
Census stays 9.  NO RH CLAIM.
**r551 coexistence.** Round 551 seals
`gabor_extremal_selection_probe.py`
(SELECTION_CONDITIONAL).  Off-line control stays
conditional.  NO RH CLAIM.
**r552 coexistence.** Round 552 is Lean-only
(`RH/GaborThetaBound.lean` sorry-free discrete theta
lobe; `RH/GaborInequality.lean` alias;
`RH.lean` import).  Continuous transfer remains open.
Census stays 9.  NO RH CLAIM.
**r553 coexistence.** Round 553 seals
`gabor_config_first_probe.py` (WITNESS_LOSES on both
1-packet and 2-packet classes).  Honest negative: the
Gabor class alone does not prove the forall-Z exists-h
form under pure counting control.  Separation stays
**[O]**.  File domain is the probe, INVENTORY,
`run_rh.py`, this README, `experiments/next.txt`, and
the already-present `experiments/README.md` catalog
row.  NO RH CLAIM.
**r364 coexistence.** Round 364 (`xn_invariant.tex`) does not
touch `rh/lean/`. DualResolvent.lean on disk is the committed r362
transcription. A parallel Lean worker may hold a red `lake build`
from WIP on that file; r364 does not treat a red Lean gate as its
own failure. The suite surface of this round is integrity +
probes (`run_rh.py --fast --skip-lean`).
**r365 coexistence.** Round 365 (`v2_regularity.tex`) does not
touch `rh/lean/`. Independently `lake build` completed
successfully (2632 jobs; historical `sorry` warnings on the
r362 DualResolvent / Source census, none introduced here).
Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) → `RH SUITE: ALL CHECKS PASSED`
(152/152 pinned). Parallel r363 L* Lean WIP is not this
round's failure.
**r366 coexistence.** Round 366 (`edge_gap_ms_probe.py`) is
additive on the L* dual lane after r363; it does not touch
`rh/problem/` (r364/r365) or `rh/lean/`. Suite surface of this
round: integrity + probes (`run_rh.py --fast`) after appending
the sealed probe to the inventory.
**r367 coexistence.** Round 367 (`final_two_rank_inertia_probe.py`)
is additive on the L* dual lane after r363/r366; it does not
touch `rh/problem/` (r364/r365) or `rh/lean/`. Suite surface of
this round: integrity + probes (`run_rh.py --fast`) after
appending the sealed probe to the inventory. r368 (weighted
L²-T1) is a parallel sealed lane and is not dropped.
**r368 coexistence.** Round 368 (`weighted_l2_t1_probe.py`) is
additive on the L2 terminal lane after r358/r361; it does not
touch `rh/problem/` (r364/r365) or `rh/lean/`. Suite surface of
this round: integrity + probes (`run_rh.py --fast`) after
appending the sealed probe to the inventory. r365–r367 are
parallel lanes and are not dropped.
**r369 coexistence.** Round 369 (`mixed_haynsworth_probe.py`) is
additive on the L† dual lane after r362/r367 (reviewer sequence
step 1); it does not touch `rh/problem/` or `rh/lean/` (the
`haynsworth_mixed` Lean statement lives in the probe spec;
proof is R373). Suite surface of this round: integrity +
probes (`run_rh.py --fast`) after appending the sealed probe
to the inventory. r370/r371/r372/r373 are parallel lanes and are
not dropped.
**r370 coexistence.** Round 370 (`matrix_weyl_index_probe.py`) is
additive on the L† dual lane after r369 (reviewer sequence
step 2, the matrix Weyl phase index); it does not touch
`rh/problem/` or `rh/lean/`. Suite surface of this round:
integrity + probes (`run_rh.py --fast`) after appending the
sealed probe to the inventory. r371/r372/r373 are parallel
lanes and are not dropped.
**r371 coexistence.** Round 371 (`compound_cd_wedge_probe.py`) is
additive on the L* dual lane after r367 (reviewer solution 3,
the canonical two-form); it does not touch `rh/problem/` or
`rh/lean/`. Suite surface of this round: integrity + probes
(`run_rh.py --fast`) after appending the sealed probe to the
inventory. r369/r370/r372/r373 are parallel lanes and are not
dropped.
**r372 coexistence.** Round 372 (`source_prufer_one_defect_probe.py`)
is additive on the Terminal/source-Jacobi lane after r365/r368
(reviewer solution 2); it does not touch `rh/problem/` or
`rh/lean/`. Suite surface of this round: integrity + probes
(`run_rh.py --fast`) after appending the sealed probe to the
inventory. r369/r370/r371/r373 are parallel lanes and are not
dropped.
**r374 coexistence.** Round 374 (`v2_lemma_v3.tex`) is additive
on the MED-CAP/$V_2$ lane after r364/r365/r372 (lemma-first
$V_2$: Wronskian step, contrast, reduction to $V_3'$).  It does
not touch `experiments/next.txt`, does not seal a discovery
probe, and does not touch `rh/lean/`.  Suite surface of this
round: integrity + probes (`run_rh.py --fast`) after appending
the problem-document rows to the inventory.  r375/r376 are
parallel lemma-first lanes and are not dropped.
**r375 coexistence.** Round 375 (`p2_lemma_proof.tex`) is additive
on the dual two-rank lane after r367/r371 (lemma-first P2:
source expansion of $-\det K_2$).  It does not touch
`experiments/next.txt`, does not seal a discovery probe, and
does not touch `rh/lean/` (a parallel Elementwise worker is not
this round's failure).  Suite surface of this round: integrity +
probes (`run_rh.py --fast --skip-lean`) after appending the
problem-document rows to the inventory.  r374/r376 are parallel
lemma-first lanes and are not dropped.
**r377 coexistence.** Round 377 (`postcap_pivots.tex` +
`postcap_pivots_probe.py`) is additive on the dual two-rank /
source-pivot lane after r367/r375 (lemma-first P2-POSTCAP and
P1-SINGLE-DEFECT in Jacobi-norm coordinates).  It does not
touch `experiments/next.txt` and does not touch `rh/lean/`.
Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the problem-
document rows and the sealed census probe to the inventory.
r374/r375/r376 and the parallel compose lane are not dropped.
**r378 coexistence.** Round 378 (`compose_lemma.tex`) is additive
on the terminal Fejér/vdC→H5→$q_N$ lane after r297–r306/r324
(lemma-first COMPOSE: pointwise chain with explicit constants,
reduction to (R)(L)(Z)(T1)).  It does not touch
`experiments/next.txt`, does not seal a discovery probe, and
does not touch `rh/lean/`.  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the problem-document rows to the inventory.
r374/r375/r376/r377 are parallel lemma-first lanes and are not
dropped.
**r379 coexistence.** Round 379 (`v3prime_proof.tex`) is additive
on the MED-CAP/$V_2$/$V_3'$ lane after r365/r374 (lemma-first
$V_3'$: cosine-grid mesh, Chebyshev source formula, reduction
to $G_\varepsilon$).  It does not touch `experiments/next.txt`,
does not seal a discovery probe, and does not touch `rh/lean/`
(r376/r380).  Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the problem-
document rows to the inventory.  r374--r378 are parallel
lemma-first lanes and are not dropped.
**r380 coexistence.** Round 380 (`RH/PivotCoordinate.lean`) is additive
on the Lean kernel: it formalizes the DCCXXXVII finite-algebra lemmas
and does not touch `rh/problem/` (r377/r378/r379) or
`experiments/next.txt`.  Census stays 5.  NO RH CLAIM.
**r381 coexistence.** Round 381 (`g_eps_lemma.tex` +
`g_eps_lemma_probe.py`) is additive on the MED-CAP/$V_2$/$V_3'$/
$G_\varepsilon$ lane after r379 (lemma-first $G_\varepsilon$: FO
formula SATZ, reduction to $(C_\varepsilon,R_2)$).  It does not
touch `experiments/next.txt` and does not touch `rh/lean/`
(r376/r380).  Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r380 are parallel
lemma-first / Lean lanes and are not dropped.
**r382 coexistence.** Round 382 (`pivot_entry_lemma.tex` +
`pivot_entry_lemma_probe.py`) is additive on the L* / pivot-band
lane after r377/r380 (lemma-first entry: $(2/3)$-flank, reduced
$n_0=\lfloor 2N/5\rfloor$).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/` (R384
formalizes `FlankEntryPrefix`).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the inventory.
r374--r381 are parallel lemma-first / Lean lanes and are not
dropped.
**r383 coexistence.** Round 383 (`compose_premises.tex` +
`compose_premises_probe.py`) is additive on the terminal
Fejér/vdC compose lane after r378 (lemma-first $(R)(L)(Z)$:
census $R_0=4$, $\Lambda=3$, $Z_0=4/5$ on FRAME-A; T1-combo
does not carry as a theorem; $\chi$ refutes family-uniform
$(Z)$).  It does not touch `experiments/next.txt` and does
not touch `rh/lean/` (r376/r380/r384).  Suite surface of this
round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r382 are parallel lemma-first / Lean lanes
and are not dropped.
**r384 coexistence.** Round 384 (`RH/FlankEntry.lean`) is additive
on the Lean kernel after r380/r382: it docks `FlankEntryPrefix` to
the pivot layer and does not touch `rh/problem/` (r382/r383) or
`experiments/next.txt`.  Census stays 5.  Ausgang
benannt-ZERLEGT.  NO RH CLAIM.
**r385 coexistence.** Round 385 (`christoffel_quiet.tex` +
`christoffel_quiet_probe.py`) is additive on the common
Christoffel-quietness core of r381 ($G_\varepsilon$) and r382
(pivot entry): Chebyshev sampling SATZ at trivial Weyl,
reduction to $(\Delta,C)$.  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384).  Suite surface of this round: integrity +
probes (`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.  r374--r384
are parallel lemma-first / Lean lanes and are not dropped.
**r386 coexistence.** Round 386 (`compose_premises2.tex` +
`compose_premises2_probe.py`) is additive on the terminal
Fejér/vdC compose lane after r383 (living-ladder $(Z')$ and
cofinal $R_0$).  It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r385 are parallel lemma-first / Lean lanes
and are not dropped.
**r387 coexistence.** Round 387 (`coherence_assist.tex` +
`coherence_assist_probe.py`) is additive on the L* / pivot-band
lane after r385 (lemma-first assist: Chebyshev--Dirichlet SATZ,
Gershgorin too crude, remainder the signed $\mu$-CD
off-diagonal).  It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r386 are parallel lemma-first / Lean lanes
and are not dropped.
**r388 coexistence.** Round 388 (`delta_deformation.tex` +
`delta_deformation_probe.py`) is additive on the MED-CAP/$V_2$/$V_3'$/
$G_\varepsilon$ lane after r381/r385 (lemma-first $\Delta$-deformation:
osc-Geronimus does not close $C_\varepsilon$; $R_2$ on the $\mu$-reference
is not dominated).  It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r387 are parallel lemma-first / Lean lanes
and are not dropped.
**r389 coexistence.** Round 389 (`weyl_energy.tex` +
`weyl_energy_probe.py`) is additive on the cancellation lane
after r381/r385/r387/r388 (lemma-first Weyl energy: Parseval SATZ,
FO^T closes $C_\varepsilon$ at quadratic-mean; assist and
$Z_{\mathrm{loc}}$ remain as $\mu$-OP Chebyshev-coefficient
Weyl).  It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r388 are parallel lemma-first / Lean lanes
and are not dropped.
**r390 coexistence.** Round 390 (`g_eps_mu.tex` +
`g_eps_mu_probe.py`) is additive on the $G_\varepsilon$ lane
after r381/r388 (lemma-first $G_\varepsilon^\mu$: occupied-Fejér
already in $\lvert\gamma-1/4\rvert$; permutation kill, not
construction-pure; remainder $F_\varepsilon\wedge W_\varepsilon$).
It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r389 are parallel lemma-first / Lean lanes
and are not dropped.
**r391 coexistence.** Round 391 (`construction_rl.tex` +
`construction_pure_rl_probe.py`) is additive on the COMPOSE$^-$
energy-premise lane after r383/r386 (lemma-first construction-pure
$(R)$ and $(L)$: white-block class, block-Gershgorin REFUTED,
DC/align kill, CS counting tautological with $n_{\mathrm{eff}}\sim m$).
It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r390 are parallel lemma-first / Lean lanes
and are not dropped.
**r392 coexistence.** Round 392 (`deletion_transform.tex` +
`deletion_transform_probe.py`) is additive on the $G_\varepsilon$ /
cancellation lane after r389/r390 (lemma-first deletion algebra:
Uvarov $\gamma$-ratio SATZ; $F_\varepsilon$ not from $\rho_{\mathrm{AP}}<1/5$;
Assist/d$\Delta$ are Uvarov readouts; cancellation is Sign-Schur).
It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r391 are parallel lemma-first / Lean lanes
and are not dropped.
**r393 coexistence.** Round 393 (`tau_field.tex` +
`tau_field_probe.py`) is additive on the $F_\varepsilon$ rest after r392
(lemma-first $\tau$-field under $F_1$: cluster/$1\times1$/$2\times2$
SATZ; rank-one locality SATZ; $F_1$ necessary not sufficient;
$\mathrm{JUMP}'=0.45$ legal, still census).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384).  Suite surface of this round: integrity +
probes (`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.  r374--r392
are parallel lemma-first / Lean lanes and are not dropped.
**r394 coexistence.** Round 394 (`sign_schur.tex` +
`sign_schur_probe.py`) is additive on the Assist / Sign-Schur
rest after r392 (lemma-first sign map of $K^\mu[\Xi]$:
Dirichlet-zonal Chebyshev-CD SATZ; checkerboard / M-matrix
REFUTED; mass-weighted Chebyshev inheritance census 81--89\%;
no $k^*>2N/5$).  It does not touch `experiments/next.txt` and
does not touch `rh/lean/` (r376/r380/r384).  Suite surface of
this round: integrity + probes (`run_rh.py --fast --skip-lean`)
after appending the probe and problem-document rows to the
inventory.  r374--r393 are parallel lemma-first / Lean lanes
and are not dropped.
**r395 coexistence.** Round 395 (`three_gap_mask.tex` +
`three_gap_mask_probe.py`) is additive on the occupation-
regularity rest after r393/r394 (lemma-first three-gap of the
fold mask: Steinhaus SATZ; log-local SATZ; Drei-Gap-Maske
REFUTED as a property of the $\nu$-mask and as a closing
implication for $F_\varepsilon$).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384).  Suite surface of this round: integrity +
probes (`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.  r374--r394
are parallel lemma-first / Lean lanes and are not dropped.
**r396 coexistence.** Round 396 (`isolation_lemma.tex` +
`isolation_lemma_probe.py`) is additive on the occupation-
regularity rest after r395 (lemma-first isolation / pair
density of the fold mask: folded-small-integer SATZ; Isolation
lemma REFUTED as a smallness SATZ of $P$ and as a closing
implication for $F_\varepsilon$ and Assist).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384).  Suite surface of this round: integrity +
probes (`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.  r374--r395
are parallel lemma-first / Lean lanes and are not dropped.
**r398 coexistence.** Round 398 (`high_moment_inertia.tex` +
`high_moment_inertia_probe.py`) is additive on the R-dagger
north star after DCCLXII (reviewer-preregistered high-moment
kill-test of P1: even-moment majorant SATZ; cycle-sum SATZ;
KILL_FAIL as a sufficient test of ind_-(R_{N-3}-I/2)<=1).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r397 are
parallel lemma-first / Lean lanes and are not dropped.
**r399 coexistence.** Round 399 (`source_weyl_energy.tex` +
`source_weyl_energy_probe.py`) is additive on the R-dagger
north star after DCCLXII 5.2/5.3 (source-pure Weyl energy of
the centered mass difference: Dirichlet representation SATZ;
Fejer Laplacian SATZ; CD-transfer norm named; decay
$E^{\mathrm{bulk}}\to 0$ REFUTED at quadratic-mean; honesty
gate ZIRKULAER for any RH-near large-sieve closing).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r398 are
parallel lemma-first / Lean lanes and are not dropped.


**r404 coexistence.** Round 404 (`one_defect_gram.tex` +
`one_defect_gram_probe.py`) is additive on the R-dagger
north star after DCCLXIX and r403 (source one-defect Gram:
Loewner/addition/fold SATZ; $Q^T A_0 Q$ PD SATZ; class 3
not reached -- CHOLESKY_TAUTOLOGY / SOURCE_GRAM_NOT_EXACT;
stop rule fires).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397/r406).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r403/r405/r406
are parallel lemma-first / Lean lanes and are not dropped.

**r403 coexistence.** Round 403 (`p1_construction.tex` +
`p1_construction_probe.py`) is additive on the R-dagger
north star after DCCLXVII and r400 (P1 as a construction
class of the fold mask: interlacing SATZ; incomplete PSD
lift SATZ; scale SATZ; CLASS REFUTED -- the invariant is
the von Mangoldt assignment, not the mask).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r401 are
parallel lemma-first / Lean lanes and are not dropped.

**r405 coexistence.** Round 405 (`edge_contractive_lift.tex` +
`edge_contractive_lift_probe.py`) is additive on the R-dagger
north star after DCCLXIX secs. 8/12 and r401 (edge half of
the one-defect factorisation: Euler/disk/Woodbury SATZ;
ones-lift residual 0; EDGE_LIFT_PARTIAL -- border=tail
REFUTED, dead overflow REFUTED, A0-defect c OPEN).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397/r406).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r403 are
parallel lemma-first / Lean lanes and are not dropped.

**r406 coexistence.** Round 406 (`RH/OneDefect.lean`) is
additive on the Lean lane after r397 (general one-defect
absorption as finite matrix algebra: SATZ A/B/C and
$c_{\min}$ **PROVED**).  It does not wait on R404/R405,
does not touch `experiments/next.txt`, and does not add a
sealed probe.  Suite surface of this round: integrity +
probes + Lean (`run_rh.py --fast`) after appending the
Lean-module row to the inventory.  r374--r405/r407/r408/r409/r410/r411 are parallel
lemma-first / probe lanes and are not dropped.

**r407 coexistence.** Round 407 (`dual_intertwiner.tex` +
`dual_intertwiner_probe.py`) is additive on the R-dagger
north star after DCCLXXI/DCCLXXII and r404/r405 (the shared
remainder: transport the Euler/Digamma Gram through the
dual resolvent).  SATZ $R=C(I+C)^{-1}$; P1 reduced to
$\lambda_2(C)\ge 1$; $\nu$-rank not one; Euler source Gram
is not the $G$ that $R$ inverts.  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384/r397/r406).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the
inventory.  r374--r406 are parallel lemma-first / Lean
lanes and are not dropped.

**r408 coexistence.** Round 408 (`c_threshold.tex` +
`c_threshold_probe.py`) is additive on the R-dagger
north star after r407 (the C-threshold / sampling
candidate: at most one $\lambda(C)<1$ because
half-filling is Nyquist-critical).  SATZ $C=BB^T$,
$2\times 2$ coherence, Rayleigh, rank, Cauchy;
Nyquist-at-density-$\tfrac12$ **REFUTED**; source
$nC\le 1$ is a census.  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384/r397/r406).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the
inventory.  r374--r407 are parallel lemma-first / Lean
lanes and are not dropped.

**r409 coexistence.** Round 409 (`borodin_birkhoff_intertwiner.tex` +
`borodin_birkhoff_intertwiner_probe.py`) is additive on the
R-dagger north star after DCCLXXIV and r407 (the source-pure
min-norm Birkhoff extension as graph of the dual resolvent).
SATZ $R=(I+\mathfrak{T}_0^*\mathfrak{T}_0)^{-1}$;
$\Phi_N$ literal identification **REFUTED**; unfitted Krein
**REFUTED**; sequential $n_{\mathrm{neg}}^{\mathrm{inn}}\le 1$
is a census.  $\mathfrak{T}^\dagger$ is the r362 graph
factor (dictionary).  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384/r397/r406).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the
inventory.  r374--r408 are parallel lemma-first / Lean
lanes and are not dropped.

**r410 coexistence.** Round 410 (`hole_nyquist.tex` +
`hole_nyquist_probe.py`) is additive on the R-dagger
north star after r407/r408/r409 (the hole-Nyquist
defect: $d_i\ge 1$ by a test polynomial, and why
off-diagonal mass hits only one mode).  SATZ RK / degree
/ $C_{ii}$ / Rayleigh; $Y$-Lagrange **REFUTED** as a
proof of $d_i\ge 1$; Fourier-block **REFUTED**;
Bernstein **REFUTED**; sequential birth is a named
reduction.  It does not touch `experiments/next.txt`
and does not touch `rh/lean/`
(r376/r380/r384/r397/r406).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the
inventory.  r374--r409 are parallel lemma-first / Lean
lanes and are not dropped.

**r411 coexistence.** Round 411 (`threshold_identity.tex` +
`threshold_identity_probe.py`) is additive on the R-dagger
north star after DCCLXXVI/DCCLXXVII and r409 (the energy-split
dictionary of $\|\mathfrak{T}_0\|$).
SATZ $\mathfrak{T}_0^*\mathfrak{T}_0=C^{-1}$;
exact PD saturation **REFUTED**; $k=37$ as a named
Christoffel hole **REFUTED**.  It does not touch
`experiments/next.txt` and does not touch `rh/lean/`
(r376/r380/r384/r397/r406).  Suite surface of this round:
integrity + probes (`run_rh.py --fast --skip-lean`) after
appending the probe and problem-document rows to the
inventory.  r374--r410 are parallel lemma-first / Lean
lanes and are not dropped.

**r412 coexistence.** Round 412 (`RH/GraphResolvent.lean` +
dossier section in `rdagger_saturation.tex`) is additive on
the R-dagger north star after r407/r409/r411: the three
core dictionaries as sorry-free finite algebra, P1 in four
equivalent coordinates, seventeen closed languages
tabulated.  Named remainder
`GraphResolventIsLEnsembleInv`.  Mincut unchanged
(`selected_augDualResolvent_gt_half`).  It does not touch
`experiments/next.txt`.  Suite surface of this round:
integrity + probes + Lean (`run_rh.py --fast`).
r374--r411 are parallel lemma-first / Lean lanes and are
not dropped.

**r413 coexistence.** Round 413 (`hole_top_mode.tex` +
`hole_top_mode_probe.py`) is additive on the R-dagger
north star after DCCLXXIX and r412 (the hole-top-mode
primary test).  SATZ: Lagrange / top hole OP over
$\mathbb{Q}$; $v_{\mathrm{top}}$ source-pure.
HTM on MAIN **REFUTED**; QD **REFUTED**; dead-$\chi$-hold
**REFUTED**.  It does not touch `experiments/next.txt`
and does not touch `rh/lean/` (r376/r380/r384/r397/r406/r412).
Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.
r374--r412 are parallel lemma-first / Lean lanes and are
not dropped.

**r415 coexistence.** Round 415 (`top_mode_edge.tex` +
`top_mode_edge_probe.py`) is additive on the R-dagger
north star after DCCLXXIX, parallel to r413 (the edge
half of the hole-top-mode architecture).  SATZ: Euler
tail / disk Parseval kept; $-\mathrm{sch}=\beta-\alpha$
as the r405/r406 chart rewrite.  $v_{\mathrm{top}}$ is
**not** the bulk defect; Euler-on-$v_{\mathrm{top}}$ is
constant content; living/dead is r401 $\mathrm{sch}$.
It does not touch `experiments/next.txt` and does not
touch `rh/lean/` (r376/r380/r384/r397/r406/r412).
Suite surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the
probe and problem-document rows to the inventory.
r374--r413 are parallel lemma-first / Lean lanes and are
not dropped.

**r401 coexistence.** Round 401 (`edge_signature.tex` +
`edge_signature_probe.py`) is additive on the R-dagger
north star after DCCLXII 5.5 (augmented 3x3 edge signature:
reconstruction SATZ; model lemma SATZ; living census in a
compact $K$ with $g^{*}>0$; dead $\chi$ leave by $\mathrm{sch}>0$).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r399 are
parallel lemma-first / Lean lanes and are not dropped.

**r400 coexistence.** Round 400 (`bulk_one_defect.tex` +
`bulk_one_defect_probe.py`) is additive on the R-dagger
north star after DCCLXII 5.4 and the r399 circularity
verdict (threshold/phase form of the frame inequality:
frame implication SATZ; rank-$r$ interlacing SATZ; Weyl SATZ;
FORM_T REFUTED as a rank-1 defect; FORM_P REFUTED as a
$C_m$-phase predictor of $\mathrm{ind}_{-}$; dead $\chi$
satisfy P1 and die at $\mathrm{sch}>0$).
It does not touch `experiments/next.txt` and does not touch
`rh/lean/` (r376/r380/r384/r397).  Suite
surface of this round: integrity + probes
(`run_rh.py --fast --skip-lean`) after appending the probe and
problem-document rows to the inventory.  r374--r399/r401 are
parallel lemma-first / Lean lanes and are not dropped.
Historical: since the r305 Lean reconstruction round
**4 intentional `sorry`s**, down from 9; since the r310 source-interface
round **5** — the fifth is the documented opacity bridge in
`RH/Source.lean`, since the r310b refinement in the reviewer target
form `mainWindow_iff_builtFromPrimeSource` (the r310 form
`mainWindow_explicit_bridge` is proved from it), type
definitional/technical; **since r320 still 5, two of them RETYPED** —
the R319 audit found the r310b statement types jointly inconsistent
(U1–U3) and r320 repaired them, see the r320 paragraphs below: the wave-6 canonical form
`lstar_subordination` [the base/wall hole], the terminal statement
`terminal_positive_main` [the border/fiber hole, new in
`RH/Closure.lean`], its pair-coordinate refinement `pair_margin_main`
[same hole, r263 dictionary not yet formalized], and the Jacobi inertia
theorem `crossing_budget` [a mathlib gap, exact-rationally certified in
v962 T2]); the **provable
core identities of stage 4 are actually proved** (no `sorry`, no mathlib —
abstract field/ordered-field algebra); since r271 the **finite pair
algebra of the fixed drive bound is proved too** (`RH/PairBound.lean`);
since r273 the pilot is **truth-capable**: the three pre-r273 universal
open statements (refutable over bare bookkeeping — machine-checked guards
in `RH/Counterexamples.lean`) are replaced by the concrete window
structure `VonMangoldtWindow` and ONE master theorem
`augmented_prefix_positive` (`RH/Window.lean`, augmented-matrix positivity
through the half-filling cap, conditioned on the honest opaque
`MainWindow` predicate). Both former open edges are PROVED from the master
theorem by finite matrix algebra (block extraction ⇒ Sylvester prefix
chain; Schur complement ⇒ terminal `q < 1`; the Schur identity
`D_n = B − u^T H_n^{-1} u` proved against mathlib). **Since wave 5** the
hole is additionally stated fog-free in base coordinates:
`free_window_positivity` (`∀ n < cap : 0 < h_n` on `MainWindow` — the
r279 b3 gap statement / v962 T4 reinstform; `master_implies_free_window`
PROVED shows it is the base half of the master `sorry`), the v962 T1
counting layer is **proved for real** (`moment_counting_free_pivots`,
`first_forced_pivot`), T4 is proved (`main_window_reduction`), T2 is
stated (`crossing_budget`, `sorry` with v962 reference), and the wave-5
guard `upper_pinning_not_universal` (the exact one-negative instance with
machine-checked Hankel minors) plus the proved escape `o1_pinning_escape`
extend the counterexample layer; the matrix-level theorems (PSD base,
half-filling, Sylvester pull-back) remain roadmap `sorry`s, each with
round, ledger ID and probe reference in the header. **Since wave 6** the
hole is additionally stated in its canonical two-measure form:
`lstar_subordination` (lemma L\* on `VonMangoldtWindow` — for every real
polynomial `p ≠ 0` with `deg p < cap`: `∫p²dν < ∫p²dμ`; the wave-6
`sorry`, ledger `PRIME.LSTAR.SUBORDINATION.01` [O]), with the direction
L\* ⇒ free-window positivity **proved for real**
(`lstar_implies_free_window` via `lstar_implies_hankel_posDef` and the
quadratic-form dictionary `hankel_quadform` — finite algebra, no
`sorry`) and the composed corollary `lstar_free_window_main`.

**Since the r305 Lean reconstruction round (reviewer plan §3 + §6.1)**
the pilot carries the RECONSTRUCTION THEOREM
(`RH/Closure.lean`, `lstar_terminal_implies_master`, PROVED):
`LStar w → TerminalPositive w → ∀ n ≤ cap, A_{w,n} ≻ 0` — L\* plus the
r258/r260 terminal statement (`B > 0 ∧ q_N < 1`, faithful to
TERMINAL_Q_LAW and the v959 budget telescope) imply the full master
positivity by finite matrix algebra (L\* ⇒ `H_cap ≻ 0`; terminal ⇒
`D_cap = B(1−q) > 0`; Schur bordering ⇒ `A_cap ≻ 0`; principal-submatrix
restriction ⇒ all `A_n ≻ 0` — the matrix form of the backward Riccati
drain `D_n = D_N + Σρ_k`). Consequently `augmented_prefix_positive` is
now a **corollary** (no own `sorry`, NOT a third arithmetic input) and
`free_window_positivity` is a **corollary of L\*** alone. The two true
**window-local** holes (Level B of the wave-12 three-level proof
graph) stand formally alone: `lstar_subordination` (`RH/Window.lean`,
base/wall) and the terminal statement — `terminal_positive_main`
(`RH/Closure.lean`, border/fiber), whose pair-coordinate form is
`pair_margin_main` (`RH/PairBound.lean`; the r263 dictionary
`Z² / m = q_N` connecting the two coordinates is measured on 42/42
rungs, not yet formalized, so both keep their own honest `sorry`).
In the same round the Inertia matrix layer was proved for real
(`psd_base`, `positive_prefix_firewall` — Sylvester's criterion built
from scratch against mathlib (`posDef_of_leading_det_pos`) —,
`sylvester_pullback`, `half_filling_boundary`); only the Jacobi inertia
theorem `crossing_budget` remains a `sorry` (mathlib v4.29.1 carries
neither Jacobi's minor-sign rule nor Sylvester's law of inertia in
matrix-counting form — a formalization gap, not a mathematical one; the
exact-rational v962 certificate stands). NO RH CLAIM.

**Since the r310 source-interface round (reviewer plan §6.3)** the
formerly fully opaque source boundary is an explicit proof interface
(`RH/Source.lean`, conservative route: `MainWindow` stays opaque and
byte-identical, all four existing holes untouched). The exact real
window source is now CONSTRUCTED: `PrimeWindowSpec` (strictly
increasing prime-power atoms, anchor `p^k`, mesh level, arch/border
fields) with the node positions and comb weights DERIVED — nodes
`= Real.log(p^k)`, weights `= Λ(p^k)` via mathlib's exact
`ArithmeticFunction.vonMangoldt` — faithful to the Python builder
chain (`v563_paper2_readouts.von_mangoldt_table`/`build_window` →
`port_integrable_kernel_probe.folded_measure` →
`principal_bessel_probe.window_pack`; the CONSTRUCTION is translated,
never a measured value). PROVED for real: `nodes_injective` (the
`log p^k` positions are pairwise distinct — log monotonicity on the
ordered prime powers), `node_pos`, `combWeight_pos`, and the four
reviewer structure theorems — `predefined_family` (the family atom set
is decided by arithmetic alone: `n` is an atom iff `IsPrimePow n ∧
n ≤ anchor²`; constructive), `mesh_refinement_compatible` (refinement
changes only the mesh level, never the atom data; `rfl`-level by
design, plus the real content `mesh_refinement_shrinks`),
`cofinal_prime_windows` (Euclid via `Nat.exists_infinite_primes`), and
`finite_forms_converge_to_weil` (PROVED in the strong stabilization
form: for compactly supported test data the finite comb forms EQUAL
the Weil prime-side tsum once the window covers the support — comb
channel only; the archimedean-kernel transcription is the documented
classical TODO, the spectral/zero side stays the open content of the
program). The rational certificate layer is connected by
`rational_window_approximates` (PROVED: every real prime window admits
rational certificate data within every positive bound — density of ℚ)
and the mesh-level predicate `RepresentsSpec`. The ONE new `sorry` is
the opacity bridge `mainWindow_explicit_bridge`
(`MainWindow w ↔ ∃ s, RepresentsSpec w s`; type
DEFINITIONAL/TECHNICAL, not arithmetic: nothing about an `opaque`
predicate is provable by design — the bridge IS the honest new
interface, and it becomes `Iff.rfl` if a future wave takes the
invasive route of redefining `MainWindow`). Census 4 → 5, with the
increase fully accounted: the new interface states what was not
formalizable before r310, and everything in it except the one
opacity-forced bridge is PROVED. NO RH CLAIM.

**Since the r310b source-theorem refinement round (reviewer plan §8,
accepted r310 + adjudicated refinements)** the interface carries the
honest folding layer and the four source theorems. (1) THE FOUR-STAGE
SUPPORT CHAIN — the reviewer's warning that `nodes_injective` must not
be overclaimed is heeded structurally: stage 1
`primePow_index_injective` (PROVED: `p^k = q^ℓ ⟹ p = q ∧ k = ℓ`,
unique factorization via `minFac`), stage 2 `nodes_injective`
(unchanged — valid for the UNFOLDED `log p^k` nodes, which is exactly
what `buildPrimeWindow` produces), stage 3 `foldedWindow` (NEW: the
explicit quotient/aggregation construction for the folded source —
equal folded nodes merged via `Finset.image`, weights ADDED over each
fiber, transcribing `folded_measure`/`np.add.at`; with the
mass-conservation structure theorem `foldedWindow_mass`, PROVED: the
aggregation is a quotient, not a projection), stage 4 `support_nodup`
(PROVED: distinctness returns AFTER the aggregation, on the merged
support). FOLDING STATUS, honest: `buildPrimeWindow` contains NO
hidden fold — it is the unfolded chain; the fold is the explicit
stage-3 step, stated for an arbitrary fold map `φ : ℝ → ℝ` of which
the corpus map (`min(j, L−j)` index fold, `cos(2π j/L)` nodes) is an
instance whose exact transcription belongs to the documented classical
arch/border TODO. (2) THE FOUR SOURCE THEOREMS, all PROVED:
`buildPrimeWindow_source_exact` (the built window carries
DEFINITIONALLY the `Λ`/`log` source data — `rfl` by derivation),
`buildPrimeWindow_weights_nonnegative` (all weight channels, comb and
arch, fold-stable), `buildPrimeWindow_support_canonical` (the full
stage-1/2/3/4 chain), `buildPrimeWindow_refinement_compatible` (the
built window is mesh-independent, also under any FIXED fold map; the
corpus fold map itself is mesh-dependent — the mesh enters ONLY
through the fold map, which is why the fold is a separate stage).
(3) THE BRIDGE IN TARGET FORM: the one Source.lean `sorry` moved into
`mainWindow_iff_builtFromPrimeSource`
(`MainWindow w ↔ ∃ s, RepresentsWindow w (buildPrimeWindow s) s.mesh`
— the reviewer's target semantics, via the new window-level predicate
`RepresentsWindow` with `representsSpec_iff` as the definitional
link), and `mainWindow_explicit_bridge` is now PROVED from it; same
type (DEFINITIONAL/TECHNICAL, opacity-forced), census unchanged at 5.
(4) APPROXIMATION WARNING (reviewer verbatim): a warning block at
`rational_window_approximates` records that the rational windows are
certificate objects, not the definition, and that an approximation
proof chain would need error ≪ the shrinking L* margin (1.68e-4 →
1.806e-8, v964) — NOT established; no statement of the file uses
approximation as a proof path; the intended route is the direct real
construction. NO RH CLAIM.

**Since the r320 bridge-repair round (the R319 red-team audit U1–U3,
all three kernel-reproduced before repair).** The r310b statement
TYPES of the source interface were jointly INCONSISTENT — not the
proofs (there are none; the sorries are the holes), the types: (U1)
the bridge + `terminal_positive_main` ⟹ `False` (`RepresentsWindow`
never bound `u`/`B`; a `B = −1` window represented the empty spec),
(U2) the bridge + `lstar_subordination` ⟹ `False` (mesh-level-0
tolerance `log anchor` admitted the TOTAL node collision on the
{2,3,4} spec; `p = X − 1` vanishes on the collided window at
`cap = 2`), (U3) `pair_margin_main` + any main window ⟹ `False`
(free `(Zloc, runs)`: `Zloc = |F| + 1`, `runs = []`). Repairs (r319
recommendations 1–5): `RepresentsSpec`/`RepresentsWindow` retyped
(exact u/B-fidelity; separation discipline — tolerance below half the
minimal node gap and below every comb weight; the spec carries the
transcribable `budget_pos`, the r243 positivity half); the free spec
channels `archWeight`/`border` — found by the r320 verification to
carry the same disease beyond the audit — are guarded by the NEW
opaque `SourceExact` (the r273 convention applied to the spec side;
elimination = the arch/border/fold transcription TODO); the old types
are conserved and machine-refuted as three PERMANENT sorry-free guards
(`RH/Counterexamples.lean`: `old_bridge_terminal_inconsistent`,
`old_bridge_lstar_inconsistent`, `old_pair_margin_forces_empty`, all
quantified over an arbitrary predicate `P` in r273-G3 style); the
`(Zloc, runs)` extraction is now a DEFINITION
(`RH/PairBound.lean`: `signRuns`/`terminalDrive`/`bulkRuns`/
`edgeLocal`, split inequality PROVED as `canonical_split`) and
`pair_margin_main` is stated for the canonical extraction only; a
satisfiability WITNESS (anchor 2, atoms {2,3,4}, mesh level 4, exact
rational certificate window; `witness_represents` sorry-free) proves
the retyped predicate nonempty — `∃ w, MainWindow w` itself stays
deliberately unprovable (two opaque predicates; exactly what blocks
the adversaries). The bridge docstring's false "becomes `Iff.rfl`"
promise is corrected. Census UNCHANGED at 5; `lstar_subordination`,
`terminal_positive_main`, `crossing_budget` byte-identical. Two
wave-12 reviewer notes are binding here: **the sorry census does not
fully measure the global distance** — the missing Level-C extraction
architecture appears in *no* `sorry`, because the correct theorem
statements do not yet exist (the census of five counts the
window-local layer only); and `SourceExact` is a good firewall but
must **not** stand as a free assumption in a final proof — the named
open Lean target is **`CanonicalPrimeWindow` + exactly one
construction theorem `sourceExact_buildPrimeWindow`** (load-bearing
for the global connection, not formalization polish; the extraction
repair fork R325 is in flight on exactly this, not consumed). NO RH
CLAIM.

**The mesh-vs-anchor cofinality seam (r320 documentation).** The word
"cofinal" names two different directions, and the seam is now mapped
(docstring block in `RH/Source.lean` after `cofinal_prime_windows`):
`cofinal_prime_windows` (PROVED, Euclid) is the ANCHOR direction —
for every `N` an anchor whose window carries ≥ `N` atoms; orthogonally
`mesh_refinement_shrinks` (PROVED) drives the mesh below every
positive bound at a fixed anchor. Hypothesis **(H_cof)** (the carrier
lane, `TfptCarrier/CofinalWeil.lean`, v849) demands something else:
PSD certificates along a PRE-FIXED mesh-refinement tower.
`cofinal_prime_windows` does NOT supply this — it produces anchors,
never PSD certificates, and its direction (atom count) is not the
(H_cof) direction (refinement along one pre-fixed tower). The named
OPEN Lean goal: identify the `specFamily` mesh-refinement tower with
the v749 canonical tower (`verification/v749_simpler_tower.py`, stages
`n_k = 2^{2k+1}`, the 2-adic nesting of the v755 Schur recursion) and
transport window positivity along it into the (H_cof) shape. Until
that identification exists, no theorem of `RH/Source.lean` feeds
(H_cof), and none claims to. NO RH CLAIM.

**Since the r326 elementwise-architecture round (the R325 repair set
in Lean).** The Level-C extraction layer exists as named statements
(`RH/Elementwise.lean`), implementing the R325 fork adjudication
(`extraction_order_probe.py`, sealed, primary
`ELEMENTWISE_STABILIZATION_GO`): **(i)** the canonical window
predicate `CanonicalPrimeWindow` (`∃ a m ha, w = buildPrimeWindow
(specFamily a m ha)`) with the PROVED construction theorem
`sourceExact_buildPrimeWindow` — the wave-12 reviewer target: the new
REAL predicate `SourceExactSpec` (node/comb derivation + atom-set
completeness + budget positivity; arch/border deliberately not bound)
is provably satisfied by every canonical family member, so
`SourceExact` is **eliminated as a free assumption from the
extraction route** (the opaque guard itself stays untouched in
`RH/Source.lean`; r376: the relation is the named Prop
`SourceExactOfFamilyCompletion`, not a `sorry` — every family
member's transcribable half is proved, the opaque filling remains
unprovable by design). **(ii)** the native
dense class `GridElement` is BUILT (dyadic step-function
autocorrelations, the v749 class: derived autocorrelation, derived
even piecewise-linear interpolant, PROVED compact support), and the
elementwise finite stabilization is PROVED for the comb channel in
the corpus gauge `2Λ(n)/√n` with the anchor onset PREDEFINED from
the element's support alone (`elementAnchor f = max(1,
⌈exp(steps·D0)⌉)`) and NO mesh quantifier — the elementwise form of
`finite_forms_converge_to_weil`; the pole kernel channel is
transcribed and PROVED (r376: native-mesh second-difference of
`polePotential`); the arch channel enters as an OPAQUE read with
its stabilization as a typed sorry (classical, S2 — Gauss/Mellin
absent from mathlib v4.29.1), and the full-form statement
`elementwise_finite_stabilization` is proved from the three
channels. **(iii)** the extraction WITHOUT the ladder is PROVED:
`weil_nonneg_of_windowlocal` — window-local positivity of the
canonical family (typed honestly on the plain full form with the
grid-compatibility guard) implies Weil-form nonnegativity on every
grid element by ONE finite instantiation per element (Euclid anchor
+ the element's own native mesh); **no mesh-cofinal PSD tower and no
transport is consumed** — (H_cof) is REPLACED as the target route
(the seam block in `RH/Source.lean` carries the r326 update; the
carrier-lane documentation stays historically correct). The bordered
⟹ plain compression step is the NAMED Prop
`BorderedCompressionBridge` (parametrized, no truth commitment) with
the composed extraction `weil_nonneg_of_bordered` proved. Census
5 → **8**: the three new sorrys are statements that were NOT
formalizable before this round — the wave-12 reviewer reservation
("the Level-C distance appears in no `sorry`") is thereby partially
discharged; the five pre-existing sorrys are byte-identical, and the
window-local premise (Level B, the two true holes) is untouched and
unclaimed. NO RH CLAIM.

**Since the r376 extraction-close round.** Pole-channel stabilization
PROVED (`pole_elementwise_stabilization`, native-mesh second-difference
of `polePotential`; `#print axioms` has no `sorryAx`). Source-exact
completion demoted to named Prop `SourceExactOfFamilyCompletion`.
Arch remains the ONE classical sorry. Census 7 → **5**. NO RH CLAIM.

## Canonical sources (never duplicated here)

- `verification/v955_…​.py`, `v956_…​.py`, `v958_…​.py`, `v959_…​.py`,
  `v960_…​.py`, `v961_…​.py`, `v962_…​.py`, `v963_…​.py`,
  `v964_…​.py`, `v965_…​.py`, `v966_…​.py`, `v967_…​.py`,
  `v968_…​.py`, `v969_…​.py` — the fourteen
  certified RH theorem modules (docstrings carry the exact theorem
  stock)
- `verification/v1017_kernel_loewner_positivity.py` — promoted
  r494/r495 kernel-Loewner floor, ledger marker
  [Numerical/certified] (not [E]).  NO RH CLAIM
- `verification/status_ledger.csv` — all `PRIME.*` rows: the formal claim
  state including fine types; **the ledger wins**
- `tfpt_prime_front.tex` — the program prose (root)
- `experiments/tfpt-discovery/*_probe.py` — the sealed probes (SHA-256 pinned
  in `INVENTORY.json`)
- `experiments/next.txt` — campaign notes (German, newest at bottom,
  r250–r273)

## TODO (later consolidation steps)

- [x] **Pipeline integration (audit gate, wave 4)**: `bash build.sh audit`
      now runs `rh/verification/run_rh.py --fast` as its own
      "RH workspace" section (must end `RH SUITE: ALL CHECKS PASSED`).
- [ ] **Pipeline integration (rest)**: register `rh/` in `docs_map` /
      `website_map` / manifest.
- [ ] **Lean full build-out**: prove the Inertia layer (needs mathlib —
      declared option, see `rh/lean/README.md`), replace the Open-edge
      `sorry`s only if/when the mathematics exists.
- [x] **Wave 4**: rounds r260–r278 promoted as `v960`/`v961`;
      `INVENTORY.json` and the suite MODULES list extended in the same
      change (probes stay sealed experiments-side, consumed byte-exact in
      the sealed smoke stage).
- [x] **Wave 5**: rounds r279–r281 frozen as the small mathematical
      theory `v962` (four theorems + four refutations); `INVENTORY.json`,
      `make_inventory.py` and the suite MODULES list extended in the same
      change; the Lean layer carries the fog-free central hole
      `free_window_positivity` (T1/T4 proved, T2 stated, N1 guard).
- [x] **Wave 6**: rounds r282–r285 + the standalone problem frozen as
      the L\* reduction dictionary `v963` (canonical form + four-language
      elimination + decomposition bookkeeping + honest margin decay);
      `INVENTORY.json`, `make_inventory.py` (r285 sync repair included)
      and the suite MODULES list extended in the same change; the Lean
      layer carries the canonical form `lstar_subordination` with the
      proved direction L\* ⇒ free-window positivity.
- [x] **Wave 7**: rounds r286–r289 frozen as the L\* coherence census
      `v964` (margin warning resolved harmless + the exact van der
      Corput theorem for L2 + the destructive-coherence carrier map +
      the METRIC_ONLY adjudication); `INVENTORY.json`,
      `make_inventory.py` (head-sync repair included) and the suite
      MODULES list extended in the same change; the Lean layer needs no
      new statement — the hole stays `lstar_subordination`.
- [x] **Wave 8**: rounds r290–r295 frozen as the L\* curvature arc
      `v965` (basin geometry + ridge anatomy + curvature spectroscopy +
      metric reconciliation + the honest F10 rejections: F10_FRAGILE +
      F10_SP_MAJORITY — F10 unpromoted, the rejections are the frozen
      content; new open contract `PRIME.LSTAR.CLOSED_FUNCTIONAL.01`);
      `INVENTORY.json`, `make_inventory.py` and the suite MODULES list
      extended in the same change; the Lean layer needs no new
      statement — the wave carries no new formal target form, the hole
      stays `lstar_subordination`.
- [x] **Wave 9**: rounds r296–r300 frozen as the L2 reduction chain
      `v966` (the DENS fork closed honestly: r296 DENS_WORLD_BLIND,
      the lane routed to L2; the four-round chain r297→r300 reducing
      the delta' > 0.21 target of the generic half to the one
      inequality NEFF_TARGET, with the magnitude no-go catalog and
      the two world-separating classes frozen verbatim; new open
      contract `PRIME.L2.NEFF_TARGET.01`); `INVENTORY.json`,
      `make_inventory.py` and the suite MODULES list extended in the
      same change (r301 in flight, not consumed — the sync is strictly
      additive); the Lean layer needs no new statement — NEFF_TARGET
      is a measured ladder-slope aggregate, not an exact finite
      identity, and a universal ladder form would be refutable (the
      r273 guard pattern); the hole stays `lstar_subordination`.
- [x] **Wave 10**: rounds r301–r304 frozen as the cascade closure
      `v967` (the wave-9 rest targets executed to their end: r301
      NEFF_SPLIT + r302 UNIF_DERIVED, the first DERIVED of the lane;
      the r303 regress audit RETYPING the cascade as an exact
      dictionary around one core S = +0.0547 with the hard reviewer
      rule; the r304 stop case LAW_LONGRANGE — the global-profile
      mixing route documented CLOSED, the period-4 comb the named
      open object; the rejections and retypings ARE the frozen
      content); `INVENTORY.json`, `make_inventory.py` and the suite
      MODULES list extended in the same change (consumption notes on
      the r301–r304 probes; no round in flight at this cut); the
      Lean layer needs no new statement — the stop carries no new
      formal target form (measured ladder aggregates, the r273
      guard pattern); the hole stays `lstar_subordination`.
- [x] **Wave 11**: rounds r305–r316 (incl. r310b) frozen as the
      architecture adjudication `v968` in the reviewer's binding
      four-level structure (Level 1 formal theorems — Lean already
      green, sorries 9 → 5; Level 2 certified finite statements;
      Level 3 negative architecture decisions verbatim — Lane A
      closed as cone language with the mechanism named, B not
      overtaking with the rank-one identities banked as
      `PRIME.SOURCE.RANKONE.UPDATE.IDENTITY.01` [E], C parked;
      Level 4 open mechanisms typed); the claim split is binding
      (`TENSOR.MECHANISM` [O] separate, NOT one TRANSFER title);
      the fiber GO stands with the provenance open
      (`PRIME.L2.RENYI3.PROVENANCE.01` [O], R317 fork at the
      reviewer); `INVENTORY.json` (head-sync: v968 entry +
      consumption notes r306–r316, all pre-existing entries
      byte-identical) and the suite MODULES list extended in the
      same change; the Lean layer ships NO change (r305/r310/r310b
      already merged and green); the holes stay
      `lstar_subordination` + `terminal_positive_main`.
- [x] **Wave 12**: rounds r317–r322 (the red-team / fork morning)
      frozen as `v969_forks_and_redteam.py` (the r319 extraction-chain
      audit U1–U3 + the r320 repair frozen as
      `PRIME.REDTEAM.EXTRACTION_AUDIT.01` [E]; the fiber fork frozen
      as `PRIME.L2.RENYI3.SLIDING_BOUND.01` [O]; the base fork closed
      honestly — P1 banked as language, the antiphase law
      `ALGORITHM_ARTIFACT`); the reviewer adjudication adopted (the
      two holes named WINDOW-LOCAL, the three-level proof graph A/B/C,
      the false cofinality direction documented NOT solved, the typed
      per-layer assessment table); `INVENTORY.json`,
      `make_inventory.py` and the suite MODULES list extended in the
      same change; the Lean layer ships NO change (r319/r320 already
      merged and green); rounds R324/R325 in flight, not consumed.
- [x] **Wave 13**: rounds r323–r327 (the extraction repair and the
      terminal composition) frozen as
      `v970_extraction_and_composition.py` (the r325 elementwise GO
      + the r326 Lean implementation frozen as
      `PRIME.EXTRACTION.ELEMENTWISE.01` [E] with the honest
      new-connection formulation verbatim; the r324 measured chain
      + the r327 SOURCE anatomy frozen as
      `PRIME.L2.RENYI3.MEASURED_COMPOSITION.01` [O] — subcritical
      +0.172, m₀\* record 10^59.6 / chain-honest 10^238 with bar
      0.188 per the r328B chain audit, the extrapolation gap typed;
      the r324-pre pre-work banked; the r323 abort consumed as a
      clean note); `INVENTORY.json`, `make_inventory.py` and the
      suite MODULES list extended in the same change; the Lean
      layer ships NO change (r326 already merged and green, census
      5 → 8); the audit rounds r328A/B/C read-only, reports with
      the coordinator; no measurement round in flight at this cut.
- [x] **Wave 14**: rounds r334–r357 (the terminal/L2/L* consolidation,
      reviewer-authorized after the double substance condition r355 +
      r357) frozen as FIVE modules —
      `v978_terminal_density_martingale.py` (the density martingale
      from mass conservation alone, the moment dictionary, the tilted
      tower, the exact hand-off and the pair ceiling;
      `PRIME.TERMINAL.DENSITY_MARTINGALE.01` [E]; the r324 MEASURED
      composition stays the terminal end state),
      `v979_cover_growth_k2.py` (the first certifying three-arm cover,
      the P02 predictor, the growth ceiling C_FAB = 14.93 and the K2
      two-family law — ALL Frame-A-typed census per the binding r353
      restriction: the sliding coverage is FINITE; K2 the sole
      cross-family survivor; `PRIME.L2.COVER_GROWTH_K2.01` [E]),
      `v980_lstar_margin_chain.py` (the one-line identity, the
      two-level theorem, the pinning theorem, the rate-equality
      theorem and the rho_K identities; the chain complete and typed;
      `PRIME.LSTAR.MARGIN_CHAIN.01` [E]),
      `v981_lstar_borodin_duality.py` (the Borodin complementation at
      half filling with rational conjugator: L* ⟺ R > ½·I, the
      reciprocal dual weight, the r354 anti-correlation retyped as
      duality algebra BY DESIGN; honest verdict DUALITY_REPARAM_ONLY;
      `PRIME.LSTAR.DUAL_HOLE.01` [E]) and
      `v982_dirichlet_matched_frame.py` (the derived matched Dirichlet
      frame: SECOND_ARITHMETIC_LIVES on 126 windows, the r330 death a
      frame artifact, K2 0/126;
      `PRIME.WORLD.DIRICHLET_MATCHED_FRAME.01` [E], census, kein
      Satz).  Unlike waves 8–13 the modules embed no probes: each
      re-derives its exact layer FROM SCRATCH (sympy + Fractions) and
      re-runs the sealed verdicts on the frozen record aggregates
      with tipping mutants (the 18 discovery probes stay sealed
      experiments-side, pinned and re-verified by this suite).
      LANE STATUS after the wave: terminal — reformulated as a
      martingale-moment statement, the MEASURED composition the end
      state; L2 — cover/growth/K2 consolidated Frame-A-typed, the K2
      gap geometry the NU-free coordinate; L* — FROZEN as a
      specialist problem (rh/problem/lstar_problem.tex) with the
      equivalent form L* ⟺ R > ½·I and the one-object question
      halved (the ~500x smallness of by-design-coupled blocks,
      localized in local dual two-point data); the second arithmetic
      lives (n = 3 on 126 windows).  `INVENTORY.json` (guard
      generator, 138 → 143), `run_rh.py` MODULES → v955–v982 and the
      ledger/paper/website surfaces extended in the same change; the
      Lean layer ships NO change (documented: the duality is a
      REPARAMETRIZATION of the existing hole `lstar_subordination` —
      no new target form; the two true window-local holes unchanged);
      `PRIME.LSTAR.SUBORDINATION.01` and
      `PRIME.L2.RENYI3.SLIDING_BOUND.01` stay [O] with wave-14 notes.
      No RH claim, no GRH claim, no L* claim.
- [x] **The Level-C construction theorem** (wave-12 reviewer target,
      load-bearing): the target architecture `CanonicalPrimeWindow`
      plus exactly one construction theorem
      `sourceExact_buildPrimeWindow`, eliminating `SourceExact` as a
      free assumption (the extraction-repair fork r325 measured its
      machine-checkable halves — primary
      `ELEMENTWISE_STABILIZATION_GO`: the repair is the elementwise
      quantifier set, not a new mesh theory).
      **DONE r326** (`RH/Elementwise.lean`, see the r326 Lean-status
      paragraph): construction theorem PROVED, comb-channel
      elementwise stabilization PROVED, extraction
      `weil_nonneg_of_windowlocal` PROVED; census 5 → 8 with the
      three new typed Level-C sorrys (arch/pole kernel stabilization
      — classical; the source-exact completion — opacity-forced).
      **r376:** pole PROVED, completion demoted to named Prop;
      remaining open there: the arch kernel transcription
      (Gauss/Mellin mathlib gap), the bordered compression bridge as
      a theorem, and the Level-B window-local premise itself.
- [x] **C1 — the Lean final-domain block** (reviewer contract
      RH.LEAN.FINAL_DOMAIN_AND_EXTRACTION.01: "reduce the Lean graph
      to the two true mathematical gaps"; formalization only, no
      probe, no ledger row, NO RH claim). **DONE** (`rh/lean/`, four
      moves, census 8 → 7, suite + lake green): (1) the two true
      holes RETYPED off the opaque `MainWindow` onto the canonical
      construction — `RH/Canonical.lean`: `CanonicalWindow w :=
      ∃ a m ha, RepresentsWindow w (canonicalWindow a m ha) mesh`
      with the predefined family completed by the ONE named opaque
      constant `canonicalCompletion` (arch/border/budget — the r326
      opacity convention extended; residual opacity = exactly the
      classical transcription TODO); the holes are now
      `lstar_canonical` and `terminal_q_canonical` (the budget half
      `0 < B` of the old terminal statement is PROVED,
      `canonical_budget_pos`); the master theorem + all corollaries
      moved with them, statements verbatim modulo the domain — no
      free `SourceExact`, no `MainWindow` bridge in the final chain;
      (2) the pair duplicate RETIRED: the r263 dictionary
      `Z² = (5/7)·q_N` typed as the ONE named lemma
      `pair_terminal_dictionary` (measured 42/42,
      transcription-blocked), `pair_closes_main` now a PROVED
      corollary of the terminal hole, the margin law demoted to the
      named Prop `PairBound.PairMarginLaw` (honest: measured misses
      kz39/kz15 — asserting it overclaimed); (3) `crossing_budget`
      PROVED — the r305 "mathlib carries neither" assessment was half
      stale (mathlib v4.29.1 has Sylvester's law of inertia,
      `QuadraticForm.sigNeg_of_equiv_weightedSumSquares`); the
      pivot/minor dictionary (Jacobi's rule as an LDL congruence +
      the Vandermonde factorization) is built in `RH/Inertia.lean`,
      now sorry-free; (4) the axiom audit `RH/Audit.lean`
      (`#print axioms` at every build, record verbatim in
      `rh/lean/README.md`): the sorry-free layer
      (`lstar_terminal_implies_master`, the L† equivalence,
      `crossing_budget`, `canonical_budget_pos`) carries
      `[propext, Classical.choice, Quot.sound]` ONLY; the master
      chain consumes exactly the two canonical holes; the Level-C
      extraction exactly the two classical kernel sorries.  **r362
      DualResolvent** (reviewer priority 2): the finite-matrix identity
      `L† ⟺ R† ≻ ½I` is kernel-checked as `I−G† ≻ 0 ⟺ R† ≻ ½I`
      (`RH/DualResolvent.lean`, sorry-free A2/A3/A4/A5/A7-min); census
      7 → 8 by the named window↔matrix transcription
      `augmentedSubordination_iff_dualResolvent`.  **r373:** that
      bridge is PROVED (μ-ONB whitening); Haynsworth two-rank/mixed
      PROVED; census 8 → 7.  The two
      window-local gaps themselves stay OPEN
      (`PRIME.LSTAR.SUBORDINATION.01`,
      `PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01` — both [O],
      untouched).  No RH claim.
- [ ] Wire the paper PDF into the docset once the pipeline integration
      fully lands.
