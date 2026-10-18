# What the TFPT arithmetic mechanism encodes

Claim boundary: research-map synthesis only; no claim for or against RH.

## Q1 — Mechanism anatomy

| Step | Input → operation → output | Universal vs TFPT-specific |
|---|---|---|
| 1 | [E] `c3=1/(8π)`, `g_car=5` → forced completion → `D5⊕A3+μ4 ⇒ E8` (`tfpt_prime_front.tex:632-640`; `verification/v53_compiler_core.py:1-13`) | TFPT-specific selection. |
| 2 | [E] E8 → shell count/theta → `θ_E8=E4`, `N(n)=240σ3(n)` (`tfpt_prime_front.tex:716-732`; `verification/v1018_e8_directed_readout.py:21-34`) | Rank 8 → weight 4 is universal; selecting this E8 is TFPT-specific. |
| 3 | [E] μ4-marked Gaussian glue → sign by the mod-4 character → `θ3²=r2`, signed census `c=θ3²θ4⁶=Θ0−Θ2` (`tfpt_prime_front.tex:637-651`; `experiments/tfpt-discovery/relative_trace_compiler_probe.py:281`) | Signed quadratic counting is universal; the μ4 mark is TFPT-specific. |
| 4 | [E] Theta coefficients → Dirichlet series/Euler product → `240ζ(s)ζ(s−3)`, χ−4 splitting, `Dχ=L(s,χ)L(s−3,χ)` (`tfpt_prime_front.tex:716-742`; `verification/v1018_e8_directed_readout.py:27-34`) | Euler products are universal; TFPT selects the channels. |
| 5 | [E] Four marked theta classes → Kneser p-neighbours → `νp=aI+bTp`, `ap=b−σ3(p)` (`verification/v535_hecke_from_geometry.py:6-29`) | Kneser/Hecke is universal; the marked class space and recovered cusp system are TFPT-specific. |
| 6 | [E] Seven-dimensional census span → oldform resolution → five `E4(q^d)`, `d=1,2,4,8,16`, plus `f8(q),f8(q²)` (`verification/v535_hecke_from_geometry.py:733-795`) | Oldform theory is universal; this 2-adic pattern is the glue census. |
| 7 | [E] 70-object weight-5/2 monoid → Shimura lift → unique `Sh(g)=−8f8`, `U4(g)=0`; level 32 is the Kohnen scope fence, not an oldform level (`verification/v537_halfintegral_bridge.py:7-33`) | Shimura is universal; uniqueness in this monoid is TFPT-specific. |
| 8 | [E] Signed periods/projectors → relative trace → `λgeom=λEis+ap²`; [N] Waldspurger ratios (`verification/v538_relative_trace_identity.py:5-38`; `verification/v537_halfintegral_bridge.py:33-54`) | Classical RTF/Waldspurger with a TFPT-specific finite match. |

Primes first enter explicitly when the universal Hecke/Kneser correspondence is indexed by a prime `p` (`verification/v535_hecke_from_geometry.py:6-20`). Before that they are implicit in coefficient multiplicativity and Euler products, not generated as events. [E] The TFPT-specific arithmetic content exceeds the E8 Eisenstein factor: it selects χ−4 and the GL(2) form `f8`. [E] It does **not** yet transport those data to new GL(1)/ξ zero information: weight-4 → GL(1) is open (`verification/v535_hecke_from_geometry.py:41-48`).

[E] “No prime-table/zero oracle” firewalls establish source purity of particular computations (`verification/v963_lstar_reduction_dictionary.py:38-41`). [I] They do not establish autonomous prime generation.

## Q2 — Which sequence is the “event log”?

The corpus uses the metaphor for several related but distinct static sequences:

1. [E] `N(n)=240σ3(n)`: the E8 shell ledger. A prime obeys `N(p)=240(1+p³)`; conversely a composite has extra positive divisors, so the equality detects primality. Its Dirichlet series is exactly `240ζ(s)ζ(s−3)` (`tfpt_prime_front.tex:716-732`).
2. [E/P] `r2(n)` and the χ−4-signed Gaussian census: records splitting `p≡1 mod 4 ⇔ p=a²+b²` (`tfpt_prime_front.tex:641-651`).
3. [E] Marked census coefficients `c(n)` with `ap=−c(p)/8`: records the `f8` Hecke channel (`tfpt_prime_front.tex:1075-1091`).
4. [E] The actual ordered Weil-window event list is the von Mangoldt comb `Λ(n)` at `log(p^k)`. The relay probe declares those prime-power events as input (`support_relay_census_probe.py:3-7`).
5. [E] `Dχ` records character-twisted divisor sums and factors as `L(s,χ)L(s−3,χ)` on the certified window (`verification/v1018_e8_directed_readout.py:30-34`).

Zeros: [E] the paper proves the E8 Eisenstein zero set is exactly `{ρ}∪{ρ+3}` and calls the bridge RH-neutral (`tfpt_prime_front.tex:851-890`). [I] Once a Dirichlet series is identified with a known Euler product, it carries that L-function’s information; its coefficients add no independent zero theorem beyond analytic continuation/functional equation. The corpus proves this for the displayed E8 and character-product bridges, not as a universal information theorem.

Dynamics:

- [E] Finite E8/Coxeter/μ4 clocks cannot realize `{log p}`: their periods are commensurable while distinct `log p` are Q-linearly independent (`tfpt_prime_front.tex:921-951`).
- [N] Ordered E8 jumps are order-blind without free evolution; free evolution adds order but no prime specificity (`tfpt_prime_front.tex:953-968`).
- [N] Relay leads consume supplied prime-power events; r635 is `LEAD_PARTIAL`, r636 `LEAD_LAW_NULL`, and the map marks the relation inactive (`experiments/tfpt-discovery/relay_lead_precision_result.json:1`; `experiments/tfpt-discovery/relay_lead_law_result.json:1`; `rh/catalog/map/rh_concept_map.json:2250-2269`).
- [N] Clock torsion reproduces known constant-factor ECM gains, no new exponent (`clock_torsion_ecm_result.json:117-123`).
- [N] Seam geodesics reduce to SQUFOF/class-group period finding on a supplied composite, not a prime generator (`seam_geodesic_infrastructure_result.json:102-108`).
- [E/I] Gate 0, extraction, arch-rate and L2 cascade transport or test an already assembled comb; none emits `log(p^k)` autonomously.

## Q3 — Why the mechanism is not understood precisely

- [I] No autonomous state law derived from P1/P2/E8/μ4 emits the support and weights of `Λ`.
- [I] No general theorem identifies the information content of the μ4 mark beyond χ−4 plus its selected `f8` isotype.
- [I] Weight 4 is explained universally by rank 8; levels 8/16/32 are recovered from the Gaussian/2-adic census, but a direct theorem “P1/P2 selects exactly `f8`” is absent. Existing uniqueness is only inside a finite 70-object monoid (`verification/v537_halfintegral_bridge.py:7-16`).
- [I] `g_car` has zero text occurrences in `verification/v535_hecke_from_geometry.py` and `verification/v536_eichler_trace_layer.py`. The five E4 copies are the five divisors `1,2,4,8,16` (`verification/v535_hecke_from_geometry.py:733-795`); equating that five with `g_car=5` has no proved mechanism.
- [I] The corpus has not transported a source-positive automorphic period identity to the GL(1) Weil form without rebuilding the explicit formula.
- [E] The Siegel–Weil carrier is positive only in the Euler region and leaves `λ*` open (`verification/v540_amplitude_linear_carrier.py:70-87`).

Independent positivity candidates:

- Waldspurger squares: **yes**, independent source; blocker = GL(2)/weight-4 → GL(1), numerical constancy only, and no Eisenstein square (`verification/v537_halfintegral_bridge.py:33-54`; `verification/v535_hecke_from_geometry.py:41-48`).
- Siegel–Weil positive theta carrier: **yes**; blocker = shifted/off-centre Euler-region positivity and the surviving Farkas gap (`verification/v540_amplitude_linear_carrier.py:35-87`).
- Rankin–Selberg norm-square: **yes**; blocker = even-k deletion/doubling and wrong-sign or shifted copies (`verification/v539_weil_structure_family.py:20-29`; `verification/v540_amplitude_linear_carrier.py:24-45`).
- GNS family: **unknown** as an independent source; wrong doubling sign and non-automorphic correction are proved obstructions (`verification/v539_weil_structure_family.py:20-50`).
- W1/L*: **no**; these identify or reparameterize the same explicit-formula wall (`notes/arxiv_w1_note/note_w1_suzuki_identification.tex:405-436`; `verification/v963_lstar_reduction_dictionary.py:1-8`).

## Q4 — Top untested combinations

The catalog co-mention audit found zero shared curated records for each pair below.

1. **Chuk L=0.8 × Siegel–Weil carrier** — [I] insert the positive theta carrier at the first non-prime-free compact window. Kill if its reserve disappears under half-line normalization or assumes finite Weil positivity. F1 pass; F2 pass; low (`verification/v540_amplitude_linear_carrier.py:70-87`; `rh/problem/narrowband_weil.tex:223-232`).
2. **Waldspurger × v963 L*** — [I] pull the `f8` twist-square measure into the μ/ν CD frame. Kill on SOS/Hamiltonian retyping, frame-genericity, or dependence on the open GL(1) bridge. F1 pass; F2 pass; medium (`verification/v537_halfintegral_bridge.py:33-54`; `verification/v963_lstar_reduction_dictionary.py:1-8`).
3. **Siegel–Weil × additive self-dual adeles** — [I] seek an all-place positive identity before the explicit formula. Kill on hand-inserted arch factors, p=2 mismatch, or Tate-formula restatement. F1 pass; F2 pass; high (`verification/v540_amplitude_linear_carrier.py:14-45`; `rh/catalog/map/gaps_report.json:1-20`).
4. **Finite RTF × Chuk L=0.8** — [I] transport v538’s finite projector identity to the compact frame. Kill if spectral identification imports the explicit formula or the all-prime/arch gap appears already there. F1 pass; F2 unknown; medium (`verification/v538_relative_trace_identity.py:43-45`; `rh/problem/narrowband_weil.tex:334-377`).
5. **Borodin dual hole × Siegel–Weil** — [I] derive `R>½I` from a positive-measure comparison. Kill if complementation only reparameterizes the same spectrum. F1 fail; F2 pass; low (`verification/v981_lstar_borodin_duality.py:14-60`; `verification/v540_amplitude_linear_carrier.py:35-45`).
6. **Matched χ frame × Waldspurger** — [I] test whether source-positive cusp data survive on the second arithmetics. Kill if the reserve is explicit-formula-generic or lacks an Eisenstein complement. F1 pass; F2 pass; medium (`verification/v982_dirichlet_matched_frame.py:12-69`; `verification/v537_halfintegral_bridge.py:33-54`).
7. **Lean Window × Siegel–Weil** — [I] formalize the positive carrier against `lstar_subordination`. Kill if the statement is only L*⇒master positivity or assumes the converse. F1 fail; F2 pass; medium (`rh/lean/RH/Window.lean:463-472`; `verification/v540_amplitude_linear_carrier.py:70-87`).
8. **Additive adeles × v963 L*** — [I] compare the global self-dual measure with the local μ/ν pair. Kill if arch compensation is assumed or the comparison is finite-window Weil positivity. F1 fail; F2 unknown; high (`rh/catalog/map/gaps_report.json:1605-1630`; `verification/v963_lstar_reduction_dictionary.py:1-8`).

## Q5 — Blind spots

- **r129, self-dual no-go:** [E/N] interior self-duality selects violations; per-window CMV self-duality survives but the limit is RH-priced. Carried as no-go; blind spot only if future proposals ignore its interior hypothesis (git `d58cb7e3`).
- **r461, mincut:** [P/E] translates mincut to cofinal compact Weil positivity, conditional from k=5. Carried into L*/window language; it is a reduction, not an independent lever (git `97c4771c`; `verification/v963_lstar_reduction_dictionary.py:1-8`).
- **r108, big-picture audit:** [N] found one-sided equivalences, entry/form mismatch, finite reach cap. Corrections were carried forward; “transfer none” should gate every new combination (git `c28c7936`).
- **r103/r102:** [N/P] huge finite positivity/Hausdorff equivalence, but finite or not world-new. Durable pieces reached `verification/v914_pascal_region_theorem.py` and `verification/v915_eulerpick_certified_floors.py`; no cofinal source (git `93e5d941`, `34597a2b`).
- **W1:** [E] exact Galerkin/measure dictionary; carried via `verification/v630_suzuki_contact.py` through `verification/v644_w2_form_density.py`. Its scope explicitly leaves W2-W4 open, so not forgotten (`notes/arxiv_w1_note/note_w1_suzuki_identification.tex:405-460`).
- **W3:** [E/N] exact structure plus finite detector; uniform W3 is declared RH-equivalent with “no ladder underneath.” Treat as a stop rule (`notes/arxiv_w3_note/note_w3_detector_structure.tex:549-590`).
- **DenseWeilCore/WeilDictionary:** [E] sorry-free finite enumeration/refinement and smooth Lerch identities. `rh/lean/` does not duplicate the named files; under-linked, but analytically incomplete (`experiments/lean4-carrier-rigidity/TfptCarrier/DenseWeilCore.lean:59-78`; `experiments/lean4-carrier-rigidity/TfptCarrier/WeilDictionary.lean:56-149`).
- **Sections 11/12:** [E/N/P] §11 closes finite parity formulas; §12 has more than 70 subsections but repeatedly returns to one cofinal positivity wall. The keystone is PD persistence / equivalent Hankel, Levinson, symbol and Krein languages; positivity remains measured per window. W1 is closed at measure level, while uniform W3 and `PRIME.Z1.OPERATOR.01` remain open (`tfpt_prime_front.tex:11853-11855`; `tfpt_prime_front.tex:12149-12216`).

## Q6 — The story

### Proved

[E] TFPT selects an E8 lattice whose theta series is `E4`; its shells are `240σ3`, its μ4 mark carries χ−4/Gaussian splitting, and Kneser neighbours recover Hecke data including the `f8` cusp channel. The seven-dimensional census resolves into five E4 oldforms plus two f8 oldforms, and a unique compiler half-integral object maps to `−8f8`. The E8 Eisenstein L-function is exactly `ζ(s)ζ(s−3)` and is RH-neutral. Finite TFPT clocks cannot realize the incommensurable prime-period spectrum.

### Numerical

[N] Finite splitting censuses, Waldspurger-ratio constancy, per-window positivity, matched χ worlds, relay leads, clock/ECM gains and seam-geodesic factoring are finite measurements or certificates.

### Asserted

[P] “Primes as shadow/checksum/event log” interprets shell, character and Hecke coefficients as an arithmetic consistency record. It is not a theorem that TFPT dynamics generates primes, their temporal order, or new zero information.

### Missing

[I] Precision requires either an autonomous non-periodic TFPT flow with primitive periods `log p` and correct amplitudes, derived without a prime oracle, or a theorem that finite/algebraic compiler data can only re-encode known Euler products. Cheapest decisive test: freeze a P1/P2/E8/μ4-only transition rule, predict events before comparison, and require exact held-out prime-power support and weights against scrambled/Epstein controls. Any sieve, `Λ`, primality test, or fitted event location fails the firewall.
